# Azurite Codex Title Hook

This repository-local, dependency-free Python hook prefixes Codex task titles
for the Azurite2 workspace with `[Azurite] `. It runs for `SessionStart` and
`Stop`, because Codex can set or replace a readable title after startup.

The hook uses `CODEX_STATE_DB` when set. Otherwise it uses
`CODEX_HOME/state_5.sqlite`, or `~/.codex/state_5.sqlite`. It only updates a
thread whose stored `cwd` resolves exactly to this repository. Missing state,
unexpected input, and SQLite errors fail open so a hook issue cannot block a
Codex task.

Codex requires repository-local hooks to be reviewed and trusted. After pulling
this change, open `/hooks` in Codex and trust the Azurite2 repository hooks.

Run the isolated proof with:

```sh
/usr/bin/python3 .codex/hooks/test_azurite_title_prefix.py
```

The test creates only a temporary SQLite database. It never accesses the real
Codex state database.
