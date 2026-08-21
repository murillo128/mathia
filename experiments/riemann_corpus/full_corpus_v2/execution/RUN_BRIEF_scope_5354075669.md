# Riemann–Mathia v2 execution brief

This is the compact run context for GitHub issue #42 v2. It implements the token/agent-compute policy recorded at https://github.com/murillo128/mathia/issues/42#issuecomment-5354075669.

## Fixed scope and lineage

- Corpus only: no training, Qwen/qwen-lean inference, GPU use, RL, weight merging, Lean work, or RH proof attempt.
- Parent: `riemann-mathia-full-v1` at freeze `riemann_mathia_full_e9f9f663e6f3a777ab7545f088f39d0662462f5da622364204e52be6fcf42cd6`; PR #43/v1 is immutable.
- Reuse the unchanged `mathia-interchange-v1` canonical interchange. V2 is additive and source linked.
- Consumed issue #46 offline full-text handoff IDs: **none**. #46 is still open and has not emitted a frozen full-text batch; #42 performs no further OpenAlex/API acquisition in this session.

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

## Stop conditions

- Never stop a source because of an arbitrary unit quota; depth ends only after an exact whole-source partition and source-specific saturation account.
- Do not repeat frozen v1/v2 work unless evidence or execution context materially changed, and preserve the superseded artifact when it did.
- Stop network/OpenAlex work in this session; preserve the offline #46 boundary.
- Stop an agent task on any source/hash/span mismatch, missing exact evidence, cross-batch context exposure, or schema/order failure.
- Optimize mathematical information per agent token, not minimum tokens; expand context only when the exact unit cannot be judged safely from the bounded packet.
