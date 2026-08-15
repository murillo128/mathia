---
name: codex-github-operations
description: Publish branches and commits, operate issues and pull requests, and preserve exact review targets using the simplest available Git and GitHub transport.
---

# Codex GitHub Operations

## Responsibility

This skill owns Git publication and GitHub control-plane operations requested by the calling workflow.

It does not decide architecture, implementation scope, correctness, review requirements, or progression. Those belong to the controlling issue, executor, design authority, independent reviewer, and explicit user-facing merge decision.

## Use the simplest capable transport

Prefer local `git` for worktree/branch/commit operations and the connected GitHub app for issues, comments, labels, pull requests, reviews, and metadata. Use `gh` only when it provides a needed operation not covered cleanly elsewhere.

A failure of one replaceable transport is not a technical blocker when another route or a precise handoff can complete the operation.

## Publish a branch

Before publication:

- confirm the intended branch;
- ensure unrelated changes are not included;
- require a clean worktree unless the caller explicitly documents otherwise;
- do not rewrite shared valid history.

Publish and verify the remote ref. Use a full SHA when another actor must inspect an exact target.

## Pull requests

Create or reuse one PR per controlling issue unless the issue explicitly requires decomposition.

The PR should summarize delivered behavior, current validation/review status, and material deviations or residual risks. Do not duplicate complete logs or history already visible in GitHub.

Keep the PR draft while required implementation, validation, or independent review remains incomplete. When the execution workflow has completed its technical work, mark the PR **ready for review** and hand it off.

### Merge authority

A Codex executor must not merge a PR or enable auto-merge.

A merge operation through this skill is allowed only when:

1. the PR is ready for review;
2. the implementation workflow has handed it off;
3. the current user-facing interaction explicitly asks ChatGPT to merge it;
4. the requested user/ChatGPT review has found no material blocker.

CI success, issue acceptance criteria, or independent-review `PASS` / `PASS_WITH_NOTES` are not merge authorization by themselves.

## Exact review targets

An independent review request must identify an exact published target. Preserve that target unchanged during review. A later technical change creates a new target and invalidates the prior final technical verdict for the changed content.

Do not amend, reset, rebase, squash, cherry-pick, force-push, or otherwise rewrite valid shared review targets merely to repair workflow metadata.

## Safety

- Never force-push or rewrite shared history without explicit user authorization.
- Never publish unrelated changes, secrets, credentials, restricted artifacts, or data without distribution rights.
- Never silently change the controlling issue, base branch, head branch, labels, or PR state.
- Never merge or enable auto-merge from an executor workflow.
- Never treat technical review success as user merge authorization.
- Never claim a GitHub state change that was not observed.

## Completion report

Report only the operational facts the caller needs: target affected, operation completed, verification result, exact target when needed, PR state, and any degraded operation or real blocker.
