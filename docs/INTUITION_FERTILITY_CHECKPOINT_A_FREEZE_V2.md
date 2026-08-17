# Intuition-fertility Checkpoint-A freeze v2

Status: `ACCEPTED` as a complete pre-registration artifact; protected execution
and Checkpoints B–F remain unauthorized.

This is the separate Checkpoint-A v2 required by the issue #32 design amendment
of 2026-08-17. PR #37 and its exact head
`76d64ddb61825bf76a6fc12f5d26b1facad59fcf` remain the historical v1 blocker.
V2 does not rewrite, reinterpret, or remove that evidence.

The machine-readable source of truth is
`experiments/intuition_fertility/checkpoint_a_v2.json`. Its strict loader first
validates the exact v1 artifact and then permits one scientific-contract delta:
the protected formal-worker seed values. Hashes bind every inherited section, so
panel B, every other panel item, worker identity, controls, donors, prompts,
sample policy, leakage policy, candidate budget, sampling settings, run order,
and metrics cannot drift through the amendment.

## Blind historical-execution audit

The audit compared the exact A–G record IDs against selected-worker Phase-5
execution membership. It read only run configuration and membership metadata at
qwen-lean commit `ef09f5e0f11a54a25fcb95b324d766f675be49a3`:

- `evidence/phase5/workloads.json`;
- `evidence/phase5/heldout-comparison.json`;
- `evidence/phase5/adapter-reload.json`;
- `evidence/phase5/minif2f.json`.

Candidate continuations, raw result files, per-item verification results, and
protected outcome values were not opened. No outcome influenced the target,
worker, protocol, audit rule, or replacement seeds.

Exactly one A–G membership was found. B is selected-record index 351 (position
352) in `phase5-heldout512-v1`, whose selected step-9962 adapter arm used seed 0
and four candidates per task. The other six exact records are absent. The
adapter-reload check is a forward-only smoke with a different record; miniF2F is
a disjoint benchmark namespace. The later Hugging Face adapter smoke recorded in
qwen-lean PR #21 was also forward-only and generated no candidate draw.

The four B/no-guidance/seed-0 selected-worker draws, candidate indexes 0–3, are
individually recorded as:

- `burned`: they can never be a protected draw;
- `sealed`: their outputs and item-level results remain unopened;
- `excluded`: they cannot enter a future experiment bundle or metric.

The unchanged-base Phase-5 comparison arm is not the selected formal worker and
therefore does not add a selected-worker seed. It remains part of the historical
v1 provenance and is not imported into v2.

## Mechanical prospective draws

The seed domain is the nonnegative integers in ascending order. A seed is used
when the selected Phase-5 worker previously generated any candidate on any exact
A–G record. The audited used set is `{0}`. Taking the first four values outside
that set yields exactly:

```text
[1, 2, 3, 4]
```

Every eligible condition for every theorem A–G uses that same seed set. Each seed
requests four candidates, so every eligible cell retains `k=16`. Candidate order
remains seed-ascending and then within-request candidate-index ascending. All
other generation and verification fields are byte-for-byte inherited from v1.

## Frozen gates

This change performed no Qwen generation, Codex generation, qwen-lean inference,
Lean proof search, or GPU work. It used neither Phase 4 nor an intermediate
Phase-5 checkpoint. It authorizes neither protected execution nor Checkpoints
B–F, and it does not authorize merge or auto-merge. Progression requires a fresh
independent review of the exact published v2 commit and later explicit user
authorization.

## CPU-only validation

From the repository root:

```bash
python3 -m experiments.intuition_fertility checkpoint-a
python3 -m experiments.intuition_fertility checkpoint-a-v2
python3 -m unittest discover -s experiments/intuition_fertility/tests -v
python3 -m compileall -q experiments/intuition_fertility
```

The first command deliberately continues to report the v1 blocker. The second
validates the separate content-addressed v2 overlay, its audit ledger, the
mechanical seed derivation, and all no-progression gates.
