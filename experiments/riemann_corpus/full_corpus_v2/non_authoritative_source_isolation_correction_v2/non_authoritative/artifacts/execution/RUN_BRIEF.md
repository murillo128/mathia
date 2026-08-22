# Riemann–Mathia v2 execution brief

This is the compact run context for GitHub issue #42 v2. It implements the token/agent-compute policy at https://github.com/murillo128/mathia/issues/42#issuecomment-5354075669 and the dual-stream #46 amendment at https://github.com/murillo128/mathia/issues/42#issuecomment-5354363863.

## Fixed scope and lineage

- Corpus only: no training, Qwen/qwen-lean inference, GPU use, RL, weight merging, Lean work, or RH proof attempt.
- Parent: `riemann-mathia-full-v1` at freeze `riemann_mathia_full_e9f9f663e6f3a777ab7545f088f39d0662462f5da622364204e52be6fcf42cd6`; PR #43/v1 is immutable.
- Second immutable baseline: `agnostic-mathia-full-v1` at freeze `freeze_eeeeb89af3d2ac75d1ff5dad5623b63d1d24dfbddb965beca2f1c4aac9f9867f` from merged PR #45. It is a comparison parent for a separate agnostic OpenAlex supplement, never Riemann content.
- Reuse the unchanged `mathia-interchange-v1` canonical interchange. V2 is additive and source linked.
- Consumed issue #46 Riemann handoff ID: **riemann_fulltext_v2**, freeze `openalex_handoff_89e50c9a268c116f9ca85d457e4cae8e3efa6f7feed64fbd1f815f0ded9d0dc6`, manifest SHA-256 `c83758e4feed61ce55b1098317ef32398775344a8548d29d7b4b86653fae63bb`. The earlier `riemann_fulltext_v1` is immutable superseded evidence only.
- Consumed issue #46 agnostic Mathia handoff ID: **agnostic_mathia_fulltext_v2**, freeze `openalex_handoff_7a0112075a605e14f20e1de307e73799898ceadc6007837faeb83468bec5691c`, manifest SHA-256 `56282413a704775ddaca0a62090dce03037c8ea55aa2d3be9ce98f542c468942`. The earlier `agnostic_mathia_fulltext_v1` is immutable superseded evidence only.
- The agnostic comparison parent is the exact merged #44 release above, including reviewed-content freeze `review_content_d1d1d7152fa2c2ddd3a4f6d26a4fa4b3f6d64129392b7c79ea72f125b5d95c0b`; do not rewrite or rematerialize that parent during #42.
- The #46 processing cutoff is **frozen**. #42 consumes only hash-bound local artifacts and performs no repeated acquisition or OpenAlex/API request.
- Future `riemann_fulltext_vN` batches continue Riemann v2. Future `agnostic_mathia_fulltext_vN` batches are deterministically deduplicated against #44 and can only enter `agnostic-mathia-openalex-supplement-v1`.

## Evidence and context protocol

- Deterministic code owns acquisition state, hashes, dedup/version checks, normalization diagnostics, exact spans, manifests, dossiers, batching, and validation.
- The source dossier is a routing cache, not mathematical authority or automatically trainable content.
- For unit analysis read only this brief, the frozen stage prompt, the exact unit span, its bounded nearby context, the assigned dossier fragment, and the explicitly named prior-stage record.
- Do not read the full issue history, whole source, unrelated batches, v1 teacher/critic outputs, or other agents' reasoning unless an explicit evidence correction requires it.
- Exact source text wins over dossier summaries. Keep spontaneous/directed outputs distinct. A critic must be fresh and isolated from teacher reasoning.

## Quality states and gates

- `candidate`: exact accepted depth unit awaiting interpretation.
- `accept_as_is`: source-grounded candidate requiring no model revision; deterministic finalization is allowed.
- `revise`: critic identified a bounded repair; revision sees exact span, compact candidate, and findings only.
- `reject`: unsupported/shallow candidate excluded from training; sampled rejects may enter QA.
- `quarantine`: corrupt, OCR/formula-unsafe, identity/context-defective, or isolation-compromised evidence; inspect at 100% where applicable.
- Synthesis begins from accepted linked interpretations/dossier relations and reopens only the exact supporting spans required to verify a proposed relation.
- The 28 #44 ecosystem families are retrieval and saturation lenses, not target labels or a permanent ontology. Source evidence may reinforce, challenge, or extend that map.

## Stop conditions

- Never stop a source because of an arbitrary unit quota; depth ends only after an exact whole-source partition and source-specific saturation account.
- Do not repeat frozen v1/v2 work unless evidence or execution context materially changed, and preserve the superseded artifact when it did.
- Stop network/OpenAlex work in this session; preserve the offline #46 boundary.
- Do not freeze the final release until a finite #46 cutoff records a disposition for every published Riemann and agnostic handoff through that cutoff.
- Stop an agent task on any source/hash/span mismatch, missing exact evidence, cross-batch context exposure, or schema/order failure.
- Optimize mathematical information per agent token, not minimum tokens; expand context only when the exact unit cannot be judged safely from the bounded packet.
