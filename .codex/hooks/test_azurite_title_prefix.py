#!/usr/bin/env python3
"""Deterministic isolated verification for the Azurite Codex title hook."""

from __future__ import annotations

import importlib.util
import json
import os
import sqlite3
import subprocess
import tempfile
import unittest
from pathlib import Path


HOOK_PATH = Path(__file__).with_name("azurite_title_prefix.py")
SPEC = importlib.util.spec_from_file_location("azurite_title_prefix", HOOK_PATH)
assert SPEC and SPEC.loader
HOOK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(HOOK)
WORKSPACE = HOOK.REPOSITORY_ROOT


class TitleHookTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_directory = tempfile.TemporaryDirectory()
        self.database = Path(self.temp_directory.name) / "state.sqlite"
        self.environment = {"CODEX_STATE_DB": str(self.database)}
        self.previous_environment = {
            key: os.environ.get(key) for key in ("CODEX_STATE_DB", "CODEX_HOME")
        }
        os.environ.update(self.environment)
        os.environ.pop("CODEX_HOME", None)
        self.connection = sqlite3.connect(self.database)
        self.connection.execute(
            "CREATE TABLE threads (id TEXT PRIMARY KEY, title TEXT, cwd TEXT, "
            "created_at_ms INTEGER, created_at INTEGER)"
        )

    def tearDown(self) -> None:
        self.connection.close()
        for key, value in self.previous_environment.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value
        self.temp_directory.cleanup()

    def add_thread(
        self, identifier: str, title: str, cwd: Path, created_at_ms: int = 1
    ) -> None:
        self.connection.execute(
            "INSERT INTO threads VALUES (?, ?, ?, ?, ?)",
            (identifier, title, str(cwd), created_at_ms, created_at_ms),
        )
        self.connection.commit()

    def title_for(self, identifier: str) -> str:
        row = self.connection.execute(
            "SELECT title FROM threads WHERE id = ?", (identifier,)
        ).fetchone()
        assert row is not None
        return str(row[0])

    def test_explicit_event_id_prefixes_once(self) -> None:
        self.add_thread("selected", "Work on sync", WORKSPACE)

        self.assertEqual(
            HOOK.prefix_session_title({"thread-id": "selected"}),
            "added task title prefix",
        )
        self.assertEqual(self.title_for("selected"), "[Azurite] Work on sync")

        self.assertEqual(
            HOOK.prefix_session_title({"thread_id": "selected"}),
            "task title prefix already present",
        )
        self.assertEqual(self.title_for("selected"), "[Azurite] Work on sync")

    def test_fallback_uses_newest_workspace_task(self) -> None:
        self.add_thread("older", "Older", WORKSPACE, 1)
        self.add_thread("newer", "Newer", WORKSPACE, 2)

        self.assertEqual(HOOK.prefix_session_title({}), "added task title prefix")
        self.assertEqual(self.title_for("older"), "Older")
        self.assertEqual(self.title_for("newer"), "[Azurite] Newer")

    def test_outside_workspace_is_unchanged(self) -> None:
        self.add_thread("outside", "Elsewhere", Path("/tmp/not-azurite"))

        self.assertEqual(
            HOOK.prefix_session_title({"session_id": "outside"}),
            "task is outside the Azurite workspace",
        )
        self.assertEqual(self.title_for("outside"), "Elsewhere")

    def test_failures_and_malformed_input_fail_open(self) -> None:
        self.assertIn("no matching", HOOK.prefix_session_title({"thread-id": "missing"}))
        self.connection.close()
        self.database.unlink()
        self.assertIn("skipped", HOOK.prefix_session_title({}))
        self.database.write_text("not a SQLite database")
        self.assertIn("skipped", HOOK.prefix_session_title({}))

        result = self.run_hook("{")
        self.assertEqual(result.returncode, 0)
        output = json.loads(result.stdout)
        self.assertTrue(output["continue"])

    def test_state_database_overrides_are_respected(self) -> None:
        self.assertEqual(HOOK.codex_state_db(), self.database)
        os.environ.pop("CODEX_STATE_DB")
        codex_home = Path(self.temp_directory.name) / "codex-home"
        os.environ["CODEX_HOME"] = str(codex_home)
        self.assertEqual(HOOK.codex_state_db(), codex_home / "state_5.sqlite")

    def test_config_uses_local_hook_for_both_events(self) -> None:
        config = json.loads(HOOK_PATH.parent.parent.joinpath("hooks.json").read_text())
        hooks = config["hooks"]
        self.assertEqual(set(hooks), {"SessionStart", "Stop"})
        for event in ("SessionStart", "Stop"):
            command = hooks[event][0]["hooks"][0]["command"]
            self.assertIn(".codex/hooks/azurite_title_prefix.py", command)

    def test_completed_hook_files_are_independent(self) -> None:
        completed_files = [
            HOOK_PATH,
            HOOK_PATH.parent.parent / "hooks.json",
            HOOK_PATH.parent / "README.md",
        ]
        forbidden = str(WORKSPACE.parent / "azurite")
        self.assertTrue(all(forbidden not in path.read_text() for path in completed_files))
        self.assertNotIn("subprocess", HOOK_PATH.read_text())

    def run_hook(self, input_value: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["/usr/bin/python3", str(HOOK_PATH)],
            input=input_value,
            text=True,
            capture_output=True,
            check=False,
            env={**os.environ, **self.environment},
        )


if __name__ == "__main__":
    unittest.main()
