# Intuition-fertility Checkpoint A freeze v1

## Status

This is the exact Checkpoint A pre-registration package for Mathia issue #32.
It is bound to accepted Mathia main commit
`185754c55344760ac44365915643bdae447b3416` and to the merged #30/#31
contract. The machine-readable source of truth is
`experiments/intuition_fertility/checkpoint_a_v1.json`; its strict content ID
at this commit is
`checkpoint_a_68dc6f09ac292213b4734ec2c6d87d91c5952a217d64e1bdd30cdd354c762f2d`.

This checkpoint performed no Qwen inference, Codex generation, qwen-lean
inference, Lean verification, or GPU work. It freezes prospective choices only.
It does not authorize Checkpoints B–F.

## Exact validation

Run from the Mathia repository root:

```bash
python3 -m experiments.intuition_fertility checkpoint-a
python3 -m unittest discover -s experiments/intuition_fertility/tests -v
python3 -m compileall -q experiments/intuition_fertility
```

The first command must report the content ID above, `valid: true`,
`protected_formal_worker_execution_authorized: false`, and blocker
`PENDING_PHASE5_SELECTED_ADAPTER`.

## Frozen experiment choices

### Panel and public presentation

- Primary targets are exactly A–F and calibration is exactly G from PANEL_V2.
- The primary pre-test uses only the standard public presentation. Genericity
  variants remain separate robustness probes and are not pooled.
- Each target remains bound to its canonical declaration, Phase-2 record ID,
  record-local declaration name and hash, pinned source and source revision.
  The legacy D/E over-qualified names remain provenance only.
- Every generator receives the exact public statement plus the accepted common
  intuition request in the byte-exact template frozen in the JSON artifact.
  It receives no canonical name, record/source/proof material, audit note, or
  formal-worker output.

### Qwen-base generator

The generator is exactly `Qwen/Qwen3-8B-Base` and its tokenizer at revision
`49e3418fbbbca6ecbdf9608b4d22e5a407081db4`. It uses no chat template and
no added special tokens. The exact prompt is passed as pre-tokenized IDs. One
greedy sample is generated per theorem with `max_new_tokens=96`, seed `0`,
BF16 vLLM `0.10.2`, and EOS/token-limit stopping on project-controlled local
GPU compute.

The generated text is not shortened. Eligibility is determined only after
deterministic Lean-comment escaping with the pinned qwen-lean tokenizer; more
than 96 tokens makes the cell ineligible.

### Codex strong reference

The reference is OpenAI Codex CLI `0.147.0` (executable SHA-256 frozen in the
artifact), model `gpt-5.6-sol`, reasoning effort `xhigh`. The current official
[OpenAI Codex model documentation](https://learn.chatgpt.com/docs/models)
documents that model selection and reasoning effort are explicit CLI choices.

Each theorem uses a fresh ephemeral session in an empty non-repository working
directory, with user config and project rules ignored and a read-only sandbox.
Only the same exact public prompt used for Qwen is supplied. The exact final
message and JSONL transcript are retained. Any tool call, model/product identity
mismatch, missing output, or execution error leaves the sample missing or
ineligible without retry. Codex CLI does not receive user-set temperature,
top-p, seed, or provider token-limit controls; those remain product-managed,
while the common post-capture 96-token eligibility rule still applies. Codex is
a strong channel/headroom reference, not a
compute-matched baseline or truth oracle.

### Sample and leakage policy

There is exactly one sample, index `0`, per theorem and generator. There are no
regeneration attempts and no later selection. Missing, over-budget,
`borderline`, or `proof_like` samples remain visible and are never replaced.

Leakage review sees only the public statement and candidate guidance. Overt
Lean markers detected by the #31 deterministic screen yield `proof_like`.
Otherwise two fresh, isolated Codex reviews apply only the exact PANEL_V2
proof-transmission rubric. Matching non-uncertain labels are used; disagreement,
uncertainty, malformed output, or missing review yields `borderline` without
retry. The procedure does not score correctness, elegance, expected proof
success, or teacher similarity. All labels freeze before formal-worker outcomes,
and all label rates are reported.

### Conditions and prompt intervention

For each primary theorem there are three shared cells (`no_guidance`, factual,
generic) and, for each of the Qwen and Codex anchors, relevant, adjacent, and
distant cells. This is 54 primary cells before ineligibility. G has only the
three shared cells plus the two relevant-generator cells, for five calibration
cells. The adjacent/distant mappings are unchanged from #30/#31, and donor cells
must bind the exact same-generator/configuration sample.

The formal-worker prompt uses the #31 renderer unchanged: baseline is exact;
guided conditions insert the escaped frozen natural-language block comment
immediately before the exact record-local declaration; every non-intervention
byte remains identical. No semantic padding or truncation is allowed. The
relevant/distant 20%-of-longer token-length gate is unchanged.

### Formal-worker generation budget

Each eligible cell has `k=16`, materialized as four candidates for each seed in
`[0, 1, 2, 3]`. Candidate order is seed-ascending then within-request index.
All conditions use the same seed set and settings: temperature `0.8`, top-p
`0.95`, top-k disabled, `max_new_tokens=1024`, model length `2048`, BF16,
EOS/token-limit stopping, no quantization, tensor parallel size 1, and no prompt
truncation. Generation batches have a 3600-second process limit; verification
has 300 seconds per candidate with eight workers.

The 59 possible cells imply at most 944 candidates before ineligibility. `k=16`
gives 6.25-percentage-point within-cell yield resolution. It doubles the
accepted miniF2F diagnostic depth of `k=8` while remaining bounded under the
accepted Phase-4 non-target throughput observations (256 candidates completed
in about 471 adapter seconds and 631 base seconds). Those observations informed
budget feasibility and inherited sampling semantics only; no Phase-4 checkpoint
is an allowed worker and no A–G model outcome informed the choice.

### Primary analysis

The analysis is theorem-level and condition-level. It reports verified count
and rate, pass@16, completeness, matched deltas, adjacent transfer separately,
relevant/distant length eligibility, all leakage rates, first verified rank,
cumulative generated tokens to first verified candidate, and floor/ceiling
behavior. Runtime is secondary and is compared only under one exact runtime
comparability identity. G is always separate from A–F.

A theorem-specific content claim requires a complete strategic relevant cell
whose verified rate strictly exceeds no-guidance, factual, generic, and the
same-generator strategic distant cell; the no-guidance cell must not be at
ceiling and the distant comparison must satisfy the length gate. Missing or
incomplete cells are not imputed. Aggregate summaries are descriptive only and
cannot replace theorem-level results.

The interpretation matrix and five possible final decisions remain exactly
those in issue #32. No exit decision is made at Checkpoint A.

## Required external binding and current blocker

As observed at freeze time, `murillo128/qwen-lean#19` is still open and has no
validation-selected Phase-5 adapter. Therefore A7 cannot honestly contain an
adapter identity yet. The artifact freezes the only permitted resolution:

1. wait for Phase 5 to complete under its own contract;
2. obtain the validation-selected final adapter and actual evidence/runtime;
3. bind exact base, adapter hash/path/logical identity, selected step,
   qwen-lean commit, tokenizer/template, whole-proof prompt, Lean/mathlib,
   verifier, packages, inference engine, GPU and runtime into `FormalWorkerRun`
   at Checkpoint C;
4. stop if any required field is absent or incompatible.

Phase 4 and intermediate/midpoint Phase-5 checkpoints are explicitly forbidden.
If Phase 5 ultimately yields no valid selected adapter, issue #32 must record the
appropriate blocker exit decision rather than change worker lineage.

Protected qwen-lean execution remains unauthorized until a fresh independent
Checkpoint-A review passes, the completed Phase-5 binding exists, and the exact
shared GPU/runtime is approved and available.
