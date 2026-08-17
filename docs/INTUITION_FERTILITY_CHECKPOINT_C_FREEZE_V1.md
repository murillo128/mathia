# Intuition-fertility Checkpoint C freeze v1

## Status

Checkpoint C for issue #32 is complete on Mathia main commit
`0f4da8f2a9520345c2aa450f756b9a9319d5ae8b`. It uses the merged Checkpoint-A
v2 and Checkpoint-B v2 freezes exactly. This checkpoint materializes only the
prospective formal-worker experiment; it does not run qwen-lean, Lean, or GPU
work and contains no protected candidate result.

The content identities are:

- Checkpoint C:
  `checkpoint_c_f3bebc4787712fec867107ecb0ca26cf9c9ee0cacaad9bac3e4fa5078fa17ccc`;
- experiment bundle:
  `bundle_5dcb4f97f22dadd8ba9b4135489ab2006d796dde9510ec518e44ab3a0fbbe600`;
- formal-worker run:
  `run_15eb7b5d3d3ff8772f246bb882d8786ee3c0169d47bda4dfd4b46e2076829b13`.

## Frozen materialization

The bundle contains the 14 Checkpoint-B v2 samples and leakage decisions, 59
condition cells, 58 rendered prompts, one formal-worker run, and zero candidate
results. The 54 A–F cells are the three shared controls plus relevant,
adjacent-donor, and distant-donor conditions for each of the Qwen-base and
Codex-reference generators. The five G calibration cells are no guidance,
factual control, generic strategy control, Qwen-base intuition, and
Codex-reference intuition.

Donor cells bind the exact Checkpoint-B v2 sample from the frozen donor theorem,
the same generator configuration, and the standard presentation. No donor text
is regenerated or copied through a new record. The accepted adjacent and distant
mappings are unchanged.

Codex-reference G is retained as
`condition_50d290019cf1839d5f4f5055665836adacc91c48796c8a83ed475fb9f0012c60`.
Its blind Checkpoint-B v2 label remains `borderline`, so it is ineligible and has
neither a rendered prompt nor a future execution slot. It was not replaced.

## Worker, prompts, and plan

The run binds qwen-lean source
`ef09f5e0f11a54a25fcb95b324d766f675be49a3`, the validation-selected Phase-5
step 9962, immutable Hub revision
`5a5fadc8ecfd46b31c7c6c2f3b8c00f1bcea6af5`, and adapter artifact SHA256
`48d33bc2f276d6f8c22525a5cb30fafe8677da95e866dbf3f37116e78e8ae990`.
Phase 4 and intermediate Phase-5 checkpoints are explicitly excluded.

At the frozen qwen-lean source revision, Phase 5 selects heldout prompts through
`render_sft_prompt(record)`, which calls `render_proof_request` without a source
preamble. The checkpoint records the SHA256 of the three source files that bind
this resolution. Every eligible condition has a content-addressed prompt.
Guided prompts differ
from the exact whole-proof baseline only by the frozen escaped natural-language
comment immediately before the bound Phase-2 record-local declaration. All
non-intervention bytes pass parity checks. Pinned-tokenizer prompt counts range
from 81 to 216, below the frozen 1024-token prompt allowance implied by
`max_model_len=2048` and `max_new_tokens=1024`.

The run uses seeds `[1, 2, 3, 4]`, four candidates per seed, and 16 candidates
per eligible cell. Candidate indices 0–15 are frozen as seed-ascending and then
within-request candidate-index ascending. The theorem/condition submission order
is also explicit in the checkpoint artifact, yielding 928 prospective slots.

## Boundary

No qwen-lean continuation was generated, no Lean verification was invoked, no
GPU was used, and the sealed historical B/seed-0 outputs were not opened.
Checkpoint D, protected formal-worker execution, merging, and auto-merge require
separate authorization after fresh independent review of the published commit.
