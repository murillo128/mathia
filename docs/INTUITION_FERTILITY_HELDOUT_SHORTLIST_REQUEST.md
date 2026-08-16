# Heldout replacement shortlist request for #30

## Purpose

This is the exact CPU-only information request needed from the local qwen-lean Phase-2 artifact to finish target selection for Mathia #30. It must not run qwen-lean inference or rank candidates by model success.

## Input

Use the actual local corpus:

`artifacts/phase2/mathlib-whole-proof-v1/heldout.jsonl`

and the pinned source checkout/trace needed to inspect declarations, retained proofs, premises, and nearby doc comments.

## Hard filters

A candidate must:

- be in Phase-2 `heldout`;
- have a valid retained theorem/lemma record and source identity;
- be compatible with the current whole-proof verifier/reconstruction path;
- fit the intended whole-proof prompt/context budget;
- not be an obvious trivial wrapper/alias whose proof is essentially one direct reuse of a nearby theorem;
- admit a faithful name-free natural-language statement for the Mathia intuition generator;
- not require concrete arithmetic execution as the conceptual task.

Do not run base, Phase-4, Phase-5, or any other qwen-lean inference on candidates.

## Desired shortlist

Return roughly 20 candidates rather than choosing the final panel. Seek diversity across domains and conceptual mechanisms, for example:

- quotient/equivalence/information-loss or representation change;
- decomposition and synthesis;
- symmetry/action/invariance;
- preservation/transport in topology or analysis;
- combinatorial/order construction;
- abstraction/generalization or assumption sensitivity.

Do not force categories if the heldout data do not support clean examples.

Prefer a spread of moderate and harder proof-bearing examples. Completion token length may be used as a rough diagnostic but must not be the sole ranking criterion.

## Fields for every candidate

Return:

- exact `declaration_name`;
- record id;
- component id;
- file path;
- split (must be heldout);
- exact declaration / theorem statement;
- completion token count and full serialized `mathlib-sft-v1` length if easy;
- retained proof token count if distinct;
- number/list of recorded premises, or a compact summary if large;
- whether the retained proof looks `wrapper_like`, `moderate`, or `proof_bearing`, with one-sentence justification based on private source inspection;
- one private scoping note describing the likely high-level mathematical mechanism/move without copying the proof;
- whether a source doc comment exists;
- any obvious human-readable theorem name/reference suggested by source comments or mathlib documentation;
- any caveat that would make name-free presentation misleading.

The private scoping note is selection metadata; it is not a future Mathia-visible prompt and must remain separate from generated intuition data.

## Ranking discipline

Rank candidates for **experimental usefulness**, not proof easiness for qwen-lean. Favor cases where:

- a compact strategic insight plausibly changes the proof route;
- substantial formal work remains after stating that insight;
- the mechanism can be distinguished from generic advice such as “try an invariant”;
- the set of chosen candidates would exercise different conceptual moves/domains.

Explicitly flag candidates whose exact proof is very short or directly invokes a single strong library theorem; these may be calibration items but should not dominate the final panel.

## Output

Return a compact table for the shortlist followed by short notes for the strongest 8–10 candidates. Do not modify qwen-lean and do not consume GPU.