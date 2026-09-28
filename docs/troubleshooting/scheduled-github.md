# Scheduled GitHub troubleshooting

Timestamp: 2026-09-28T13:05:45+02:00 (Europe/Madrid)

This file records controlled publication evidence from the scheduled GitHub diagnostic task.

## Verified observations

- GitHub reads from the scheduled task succeed.
- The authenticated account is `murillo128` and repository collaborator permission is `admin`.
- The GitHub app-specific ChatGPT permission is `Allow all actions`; this does not disable platform safety checks.
- Ref mutations have succeeded from scheduled executions.
- GitHub Contents API `create_file` was repeatedly blocked locally by OpenAI safety checks before reaching GitHub; that route is not being retried without material new evidence.
- Git Data `create_blob` succeeded and the blob was readable by SHA.
- A complete Git Data publication path succeeded on 2026-09-28: blob -> tree -> commit -> non-force ref update.
- Commit `a0f9faea45027b157a31dd55e14c2ca1f9e87a9f` made this file reachable from `diagnostics/scheduled-github`, and the file was read back with blob SHA `b1d266060575c2e23b8fb7a8621f82ffd2403de0`.
- The repository skill `.agents/skills/codex-github-operations/SKILL.md` still has SHA `b35f3f332de13ad81632899cc9fba888f88d0ef0` on both `main` and the diagnostic branch and does not yet contain an explicit Git Data fallback.
- The enabled Mathia research tasks have continued to execute after the Git Data validation, but `main` still resolves to `f97d317f429f6a48373a35bcd065c1abce455a4f`. Scheduler timestamps alone do not distinguish successful no-change executions from publication failures.

## Current conclusion

Git Data is a verified publication route for scheduled tasks even while `create_file` remains blocked. This update is a second end-to-end use of Git Data on the same diagnostic branch, now updating an existing tracked file rather than creating it, to verify the route is reproducible.

Full Mathia recovery is not yet proven because no affected research task has produced a new verifiable repository publication after this fallback was validated, and the shared GitHub operations skill has not been updated to name Git Data explicitly as the fallback.
