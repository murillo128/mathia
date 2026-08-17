# Intuition-fertility harness

This package implements the deterministic CPU-side mechanics accepted in issue
#31. Separate write-once Checkpoint-B runners capture the frozen v1 and v2
Qwen-base/Codex-reference samples and blind leakage reviews. They have no
qwen-lean, Lean, formal-worker, proof-verification, or training interface.

Issue #32 Checkpoint-A v1 remains frozen in `checkpoint_a_v1.json` as the
historical `PRE_FREEZE_TARGET_EXECUTION_CONTAMINATION` blocker reviewed in PR
#37. The separate design-amended freeze is `checkpoint_a_v2.json`; its loader in
`checkpoint_a_v2.py` validates the exact v1 artifact, preserves B and every
scientific-contract section, seals/excludes the four historical B/seed-0 worker
draws, and mechanically freezes the first unused seeds `[1, 2, 3, 4]`. Every A–G
condition uses those seeds with four candidates per seed and unchanged `k=16`.
No candidate output or item-level result was inspected. Phase 4, intermediate
Phase-5 checkpoints, floating Hub revisions, protected formal-worker execution,
and Checkpoints C–F remain forbidden without later explicit authorization.

Checkpoint-B v1 remains preserved in `checkpoint_b_v1.json`, validated by
`checkpoint_b.py`. It contains exactly one
Qwen-base and one Codex-reference sample for every A–G target, the two blind
leakage reviews per sample, post-escape tokenizer evidence, exact transcript and
source hashes, deterministic eligibility, and explicit no-progression gates.
All seven Qwen samples are `strategic` at exactly 96 tokens. All seven Codex
samples are preserved over-budget and therefore ineligible; D/F/G are also
`borderline` by the frozen disagreement rule. No sample was repaired or replaced.

The prospective brevity amendment is frozen separately in
`checkpoint_b_v2.json`, validated by `checkpoint_b_v2.py`. Both roles received
14 entirely new sample-index-0 captures under the same public prompt with only
`Keep the entire strategy to at most 45 words.` added after the unchanged
intuition request. All 14 are within the unchanged 96-token post-escape cap;
Codex-reference G is preserved `borderline` and ineligible after a disputed
blind review, leaving 13 eligible samples. B v1 was not mixed, selected, or
substituted. Checkpoint C and protected formal-worker execution remain
unauthorized.

Checkpoint C is frozen in `checkpoint_c_v1.json`, with its exact transport
bundle in `checkpoint_c_bundle_v1.json`. It binds the accepted Phase-5 worker,
materializes 54 primary cells and five G-calibration cells, renders and parity
checks all 58 eligible prompts, and preserves Codex-reference G as the sole
ineligible cell without a prompt or execution slot. The single frozen run uses
seeds `[1, 2, 3, 4]`, four candidates per seed, and `k=16`, for 928 prospective
candidate slots. The bundle contains zero candidate results: qwen-lean, Lean,
GPU work, the sealed historical B/seed-0 draws, and Checkpoint D remain outside
this checkpoint.

The contract is split into three channels:

- `generator_payload(...)` exposes only the selected name-free theorem statement
  and the common intuition request;
- fixed factual/generic controls enter only through formal-worker condition cells;
- canonical declarations, Phase-2 records, pinned source provenance, and audit
  notes require the explicit private panel accessor or `panel --include-private`.

Core records are immutable and content-addressed. Canonical JSON uses sorted
object keys, while bundle arrays are sorted by their content IDs, so filesystem
and JSON object order do not affect scientific identities. The interchange is
provider-neutral; generator, model, tokenizer, worker, environment, budget,
sampling, and seed identities are supplied by the later run rather than chosen
here.

## #32 integration sequence

1. Use `generator_payload` for the frozen standard or genericity presentation.
2. Capture exact output with `IntuitionSample.capture` and a qwen-lean tokenizer
   adapter. Token counts use the deterministically escaped guidance bytes that
   will appear inside the Lean comment, before wrapper delimiters. The included
   whitespace adapter is synthetic and test-only.
3. Import a frozen leakage-only decision with `LeakageDecision.create`. Its
   classifier payload contains exactly the visible theorem statement and raw
   guidance. Uncertain or disputed decisions become `borderline`.
4. Build relevant and fixed cells, then bind adjacent/distant donors by exact
   frozen sample ID. Missing, non-strategic, or over-budget donors remain explicit
   ineligible cells.
5. Split the existing qwen-lean baseline into a `PromptTemplate` bound to the
   theorem id, canonical target, record id, exact prefix, and the exact Phase-2
   record-local declaration. Rendering inserts one escaped block comment at that
   frozen split; the baseline and non-intervention bytes remain in the prompt
   artifact for inspection.
6. Supply `FormalWorkerRun` identities and import each continuation with formal
   verification evidence bound to its exact environment/mathlib/Lean context,
   target, record, prompt, and continuation. Only matching `accepted` evidence
   can produce `verified_proof`.
7. Store artifacts in `ExperimentBundle`; validate and score them with the CLI.

The comment renderer preserves the raw guidance record and deterministically
escapes only `/-` and `-/` inside the rendered copy. It never truncates, pads, or
rewrites a stored sample after classification or outcomes.

## Commands

From the repository root:

```bash
python3 -m experiments.intuition_fertility panel
python3 -m experiments.intuition_fertility panel --include-private
python3 -m experiments.intuition_fertility checkpoint-a
python3 -m experiments.intuition_fertility checkpoint-a-v2
python3 -m experiments.intuition_fertility checkpoint-b
python3 -m experiments.intuition_fertility checkpoint-b-v2
python3 -m experiments.intuition_fertility checkpoint-c
python3 -m experiments.intuition_fertility validate path/to/bundle.json
python3 -m experiments.intuition_fertility summarize path/to/bundle.json
python3 -m unittest discover -s experiments/intuition_fertility/tests -v
python3 -m compileall -q experiments/intuition_fertility
```

The summary retains theorem-level result cells, reports adjacent guidance only as
a transfer probe, marks length-ineligible relevant/distant comparisons, reports
all leakage labels by theorem/generator, and excludes calibration G from every
primary aggregate.
