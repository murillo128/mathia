---
name: codex-github-operations
description: Publish branches and commits, operate issues and pull requests, and preserve exact review targets using the simplest available Git and GitHub transport.
---

# Codex GitHub Operations

## Responsibility

This skill owns Git publication and GitHub control-plane operations requested by the calling workflow. It does not decide architecture, scientific scope, implementation correctness, review requirements, or progression.

## Use the simplest capable transport

Use local `git` for worktree inspection, branches, commits, fetch, push, and exact ref verification. Prefer the connected GitHub app for issues, comments, labels, pull requests, reviews, and metadata when available. Use an already-authenticated `gh` only when it provides a needed operation not covered cleanly elsewhere; do not install or authenticate it merely for routine publication.

### Detached local-runner sessions

A Codex turn launched through `.github/workflows/codex-execute-ready.yml` outlives the GitHub Actions job that authorized it. Treat the session as detached from Actions credentials.

Do not depend on `GH_TOKEN`, `GITHUB_TOKEN`, `CI`, or `GITHUB_ACTIONS` being present after launch and never recover, copy, persist, or reuse an Actions token from runner files, process environments, logs, or job metadata. Use the host user's already-established persistent transports instead: normal Git SSH/credential-helper state, an already-authenticated `gh` CLI when needed, or another explicitly available secure transport.

Before mutating remote state, verify that the selected persistent transport is authenticated for the exact Mathia repository. If persistent Git/GitHub authentication is genuinely unavailable and the operation is required, report that precise blocker rather than synthesizing credentials or weakening the workflow.

A failure of one replaceable transport is not a technical blocker when another permitted route or precise handoff can complete the operation.

## Workflow state

For non-trivial controlling issues that use the generic issue workflow, the current workflow state is authoritative through exactly one state label:

- `execution-ready`
- `in-progress`
- `design-required`
- `investigation-required`
- `blocked`
- `completed`

Preserve unrelated labels but replace the prior workflow-state label rather than adding another. Use state-only label mutations without comments; reserve comments for material technical findings, contract amendments, checkpoint targets/verdicts, blockers, or handoffs.

Before relying on issue state, verify that exactly one workflow-state label is present. Repair an unambiguous inconsistency; stop when the intended state is ambiguous.

For the generic PR-backed Codex executor, keep the issue `in-progress` through the ready-for-review handoff. Set `completed` and close only after a later explicit user-facing merge decision is executed and the merge is observed.

Mathia's explicit no-PR executor skills are deliberate exceptions: `mathia-compute-executor` and `mathia-formalization-executor` define their own valid completion transition after their respective execution/publication gates. Do not force their lifecycle through PR-backed post-merge semantics.

Specialized campaign/control-plane issues that explicitly define another state system are not generic controlling issues merely because they are GitHub issues. Do not add these workflow labels to them unless their owning skill/contract adopts the generic workflow.

## Commit messages

Agent-created commits should use Conventional Commits syntax where compatible with the owning Mathia skill: `<type>(<optional-scope>): <imperative summary>`.

Use `feat`, `fix`, `refactor`, `perf`, `test`, `docs`, `build`, `ci`, `chore`, `style`, or `revert` unless a specialized Mathia research skill defines a narrower commit convention. Keep summaries concise and outcome-oriented; do not combine unrelated outcomes just to reduce commit count.

Explicit research publication conventions such as `research(<line>): ...` remain authoritative when a Mathia skill requires them.

## Publish a branch

Before publication, confirm the intended branch, ensure unrelated changes are excluded, require a clean worktree unless the caller explicitly documents otherwise, and never rewrite valid shared history without authorization.

When the local runner supplied a persistent issue worktree/branch, preserve that `codex/issue-N` branch for PR-backed implementation. Do not switch publication to the durable coordination clone or invent a second branch merely because execution was launched automatically.

For an explicit no-PR Mathia executor, the local `codex/issue-N` worktree is execution isolation only. Follow that executor's direct-main publication gate exactly and do not push the issue branch unless its controlling contract independently authorizes doing so.

### Direct-main publication from an issue worktree

When a no-PR Mathia skill has passed every gate and the accepted candidate currently lives on the **unpublished local** `codex/issue-N` branch, do not attempt to `checkout main` inside that worktree. Instead fetch `origin/main`, reconcile concurrent changes under the owning skill's rules, ensure the candidate commit is based on the current `origin/main`, and prove that the diff from `origin/main` contains only the paths authorized by that skill.

Publish the accepted commit as a normal fast-forward update of the default branch, equivalent to `git push origin HEAD:main`, without publishing `codex/issue-N` as a remote branch. Verify immediately afterward that fetched `origin/main` resolves to the intended commit. A non-fast-forward rejection means main changed concurrently: refresh and re-run every gate affected by that movement. Never force-push. Rebasing the unpublished local scratch branch is allowed only before publication and only when doing so does not bypass any exact-target validation/review requirement owned by the calling skill.

Publish and verify the remote ref. Use a full SHA only when another actor must inspect an exact target.

## Pull requests

Create or reuse one PR per generic controlling issue unless the issue explicitly requires decomposition. The PR should use the intended base/head, link the controlling issue, summarize delivered behavior, state current validation/review status, and list material deviations or residual risks.

Keep it draft while required implementation, validation, or independent review remains incomplete. When the generic execution workflow completes its required technical work and final-capable review, mark the PR **ready for review** and hand it off.

### Merge authority

A Codex executor must not merge a PR or enable auto-merge. Merge through this skill is allowed only after the PR is ready for review, the executor has handed it off, the current user-facing interaction explicitly asks ChatGPT to merge it, and that requested review finds no material blocker.

An issue body, acceptance criteria, independent-review `PASS`/`PASS_WITH_NOTES`, final-capable checkpoint, or CI success is not merge authorization by itself.

## Exact review targets

An independent review request must identify one exact published project target and any exact dependency revision required by the issue. Verify those targets before review and preserve them unchanged during review.

Do not amend, reset, rebase, squash, cherry-pick, or force-push a valid review target merely to repair comments, labels, PR descriptions, or other workflow metadata. A later technical change creates a new review target.

## Active executor ownership

Once a Codex executor creates or adopts a PR for a controlling issue, it owns that PR head branch and execution control plane until handoff, closure, merge, or explicit ownership transfer. Other actors may inspect read-only but should not silently push, rebase, reset, or otherwise modify the active executor branch.

If ownership is ambiguous, resolve it before mutating shared state.

## Technical evidence and runner state

Technical manifests/evidence should contain technical and reproducibility information, not GitHub bookkeeping unless workflow metadata is itself a technical input.

Host-local runner PID files, generated launcher clients, thread/turn identifiers, and logs under `$HOME/.skillforge/**` are operational infrastructure state. Never add them to Mathia or treat them as mathematical/technical evidence unless an issue explicitly studies runner infrastructure.

## Degraded control-plane operation

When a requested GitHub operation cannot be completed in the current surface, try another permitted transport when practical, preserve valid branch/commit history, leave a concise exact handoff only when needed, and verify later mutations before relying on them. Use `blocked` only when the missing capability is required before safe meaningful progress and no practical alternative exists.

## Safety

Never force-push or rewrite shared history without explicit authorization. Never publish unrelated changes, secrets, private credentials, restricted artifacts, or data without distribution rights. Never persist an ephemeral Actions token for a detached executor. Never silently change the controlling issue, branch, labels, or PR state. Never merge/enable auto-merge from an executor workflow, and never claim a state change that was not observed.

## Completion report

Report only the operational facts the caller needs: affected branch/issue/PR, operation completed, verification result, exact target when another actor needs it, PR state when relevant, and any degraded operation or real blocker.
