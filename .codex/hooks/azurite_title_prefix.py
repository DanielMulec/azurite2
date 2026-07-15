#!/usr/bin/env python3
"""Fail-open Codex hook that marks Azurite workspace task titles."""

from __future__ import annotations

import json
import os
import sqlite3
import sys
from pathlib import Path
from typing import Any


SESSION_TITLE_PREFIX = "[Azurite] "
REPOSITORY_ROOT = Path(__file__).resolve().parents[2]


def read_event() -> dict[str, Any]:
    """Return the hook event, treating malformed standard input as an empty event."""
    try:
        value = json.loads(sys.stdin.read() or "{}")
    except (json.JSONDecodeError, OSError):
        return {}
    return value if isinstance(value, dict) else {}


def event_thread_id(event: dict[str, Any]) -> str | None:
    """Find a supported Codex thread identifier in an event payload."""
    for key in ("thread-id", "thread_id", "session_id"):
        value = event.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return None


def codex_state_db() -> Path:
    """Resolve Codex's state database while preserving test-friendly overrides."""
    codex_home = Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex")
    return Path(os.environ.get("CODEX_STATE_DB") or codex_home / "state_5.sqlite").expanduser()


def newest_workspace_thread_id(connection: sqlite3.Connection, root: Path) -> str | None:
    """Return the most recently created task recorded for this exact workspace."""
    row = connection.execute(
        "SELECT id FROM threads WHERE cwd = ? "
        "ORDER BY created_at_ms DESC, created_at DESC, id DESC LIMIT 1",
        (str(root),),
    ).fetchone()
    return str(row[0]) if row else None


def prefix_session_title(event: dict[str, Any], root: Path = REPOSITORY_ROOT) -> str:
    """Prefix one matching task title, returning a diagnostic instead of raising."""
    try:
        database = codex_state_db()
        # SQLite's read-write URI prevents a missing state database from being created.
        database_uri = f"{database.resolve().as_uri()}?mode=rw"
        with sqlite3.connect(database_uri, uri=True, timeout=5) as connection:
            connection.execute("PRAGMA busy_timeout = 5000")
            thread_id = event_thread_id(event) or newest_workspace_thread_id(connection, root)
            if thread_id is None:
                return "no Codex task found"

            row = connection.execute(
                "SELECT title, cwd FROM threads WHERE id = ?", (thread_id,)
            ).fetchone()
            if row is None:
                return "no matching Codex task found"

            title, cwd = row
            if not isinstance(cwd, str) or Path(cwd).expanduser().resolve() != root:
                return "task is outside the Azurite workspace"

            current_title = title if isinstance(title, str) else ""
            if current_title.startswith(SESSION_TITLE_PREFIX):
                return "task title prefix already present"

            connection.execute(
                "UPDATE threads SET title = ? WHERE id = ?",
                (SESSION_TITLE_PREFIX + current_title, thread_id),
            )
            connection.commit()
            return "added task title prefix"
    except Exception as error:  # Hook faults must never block the active Codex task.
        return f"task title prefix skipped: {error}"


def main() -> int:
    """Run the title update and always emit a non-blocking Codex hook response."""
    message = prefix_session_title(read_event())
    print(json.dumps({"continue": True, "systemMessage": message, "suppressOutput": True}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
