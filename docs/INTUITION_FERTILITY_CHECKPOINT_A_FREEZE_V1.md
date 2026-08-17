# Intuition-fertility Checkpoint A freeze v1

## Status — blocked

This is the exact Checkpoint A blocker/freeze package for Mathia issue #32. The
prospective A1–A11 choices are content-addressed, but Checkpoint A cannot pass:
the selected Phase-5 worker had already been run on exact panel target B before
its complete A7 binding was frozen. It is bound to accepted Mathia main commit
`185754c55344760ac44365915643bdae447b3416` and to the merged #30/#31
contract. The machine-readable source of truth is
`experiments/intuition_fertility/checkpoint_a_v1.json`; its strict content ID
at this commit is
`checkpoint_a_97083c4054bde854af64f4d531f8ae9db7c1d9182a1f1ff22c551146c3b035fa`.

This Mathia Checkpoint-A work performed no new Qwen inference, Codex generation,
qwen-lean inference, Lean verification, or GPU work. The Hugging Face adapter
files were downloaded from their immutable revision only to verify their hashes;
no model was loaded. The prior Phase-5 execution is external historical evidence
and is the blocker documented below. This package does not authorize Checkpoints
B–F.

## Exact validation

Run from the Mathia repository root:

```bash
python3 -m experiments.intuition_fertility checkpoint-a
python3 -m unittest discover -s experiments/intuition_fertility/tests -v
python3 -m compileall -q experiments/intuition_fertility
```

The first command must report the content ID above, `valid: true`, status
`blocked_pre_freeze_target_execution`,
`checkpoint_a_successfully_completed: false`,
`protected_formal_worker_execution_authorized: false`, and blocker
`PRE_FREEZE_TARGET_EXECUTION_CONTAMINATION`.

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

## Material pre-freeze execution blocker

The immutable Phase-5 workload evidence at qwen-lean commit
`ef09f5e0f11a54a25fcb95b324d766f675be49a3` contains exact PANEL_V2 record B,
`9db61d80db52314e83addee2d556253ee17ad710d1a597725a0a6390d2009073`,
at zero-based index `351` of `phase5-heldout512-v1`. The matching heldout
comparison records complete base and validation-selected-adapter runs over all
512 tasks with four candidates per task, seed `0`, `whole-proof-v1`, the same
sampling settings and Lean verification semantics.

The selected adapter arm therefore already generated and verified the exact
four-candidate seed-`0` slice of the future B `no_guidance` cell before the
complete A7 freeze. Issue #32 requires the freeze before qwen-lean is run on any
A–G target under any condition. That chronology cannot be repaired
retroactively.

No item-level B candidate text or verification result was opened for this
audit. The workload membership and complete-run metadata alone establish the
contract violation. The hash-based Phase-5 workload selection was prospective
and outcome-independent, so this is accidental contamination, not evidence of
post-hoc target selection; it nevertheless invalidates the required temporal
gate.

Checkpoint A therefore records
`PRE_FREEZE_TARGET_EXECUTION_CONTAMINATION` and requires
`REVISE_INTUITION_FERTILITY_PROTOCOL` before any later checkpoint. This package
does not choose a repair. In particular, it does not silently remove or replace
B, reinterpret the historical run as frozen, complete only the remaining 12
candidates, selectively rerun targets, or alter controls/donors/metrics/worker
lineage. A separate prospective design decision is required.

## Frozen Phase-5 formal worker

A7 is resolved from completed qwen-lean Phase-5 evidence, not from Phase 4 or an
intermediate checkpoint:

- qwen-lean source is commit
  `ef09f5e0f11a54a25fcb95b324d766f675be49a3`, the exact qwen-lean `main`
  commit explicitly selected for issue #32;
- the standard unmerged PEFT LoRA artifact is
  `phase5-train-full-v1-lora`, validation-selected at optimizer step `9962`;
- the qwen-lean training-artifact binding SHA-256 is
  `48d33bc2f276d6f8c22525a5cb30fafe8677da95e866dbf3f37116e78e8ae990`;
- the Hub repository is
  `murillo2000/qwen3-8b-base-lean-sft-qlora` at immutable revision
  `5a5fadc8ecfd46b31c7c6c2f3b8c00f1bcea6af5`; a floating `main` is forbidden;
- the downloaded exact-revision `adapter_model.safetensors` and
  `adapter_config.json` SHA-256 values are respectively
  `8aa50fa56f6a1d03a702abcaafc20e11d661a4a2ac935864bf5648411e5cdc58`
  and `4b7b513b216484554e05d3c75ecf0777ee1fbae94935e93d949d63cf4a76481c`;
- base and tokenizer are `Qwen/Qwen3-8B-Base` revision
  `49e3418fbbbca6ecbdf9608b4d22e5a407081db4`, with no chat template or added
  special tokens;
- the worker uses qwen-lean `whole-proof-v1`, raw continuation transport and
  original Phase-2 source-span reconstruction without extraction or repair;
- the formal environment is mathlib
  `81a5d257c8e410db227a6665ed08f64fea08e997` under
  `leanprover/lean4:v4.32.0`, verified with
  `lake env lean -E hasSorry Reconstructed.lean`;
- the frozen runtime identity is local vLLM `0.10.2`, Python `3.12.14`, Torch
  `2.8.0+cu128` / CUDA `12.8`, on an NVIDIA RTX 4000 Ada Generation. The
  exact qwen-lean dependency lock hash and adapter-reload package versions are
  retained in the machine-readable artifact.

The Phase-5 evidence authenticated the selected worker lineage and runtime and,
during the same identity audit, exposed B's workload membership. It did not
alter `k`, sampling, seeds, run order, panel, conditions, donor mappings, prompt
intervention, leakage policy, or analysis. No item-level B output or outcome was
inspected.

Phase 4 and every intermediate/midpoint Phase-5 checkpoint remain explicitly
forbidden. Any mismatch in base, adapter bytes/revision, source, tokenizer,
prompt, formal environment, verifier, packages, or runtime stops execution.

Protected qwen-lean execution remains unauthorized because Checkpoint A is
materially blocked. The only next scientific action is a separate prospective
design revision that explicitly resolves the contamination, followed by a fresh
freeze/review and explicit user authorization. Checkpoints B–F must not begin
under this contract.
