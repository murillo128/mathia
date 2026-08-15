# Gold set v0 audit and pre-registered expectations

## What this set is trying to distinguish

The experiment is designed to separate at least four hypotheses that can otherwise look identical in prose:

1. **More tokens help.** Any relevant-sounding extra context improves the solver.
2. **Facts help.** Supplying concise mathematical facts improves the solver, with no special role for representation.
3. **Procedures help.** A local algorithm/checklist is the main useful intervention.
4. **Structural representation helps selectively.** A compact mechanism improves transfer, counterfactual reasoning, diagnosis, composition, and representation change more than controls of comparable length.

A Mathia-like signal requires evidence closer to (4), not merely (1)-(3).

## Directional expectations fixed before model results

These are hypotheses, not acceptance criteria to tune against.

- `structural` should not be required to beat `procedural` on direct local computations.
- `structural` should outperform `sterile` if operational structure matters more than conceptual rhetoric.
- `wrong` should often hurt relative to `none` or `factual`; if it does not, either the solver ignores contexts or the tasks are too easy.
- `shuffled` should not reproduce the structural advantage. A large shuffled gain would suggest generic priming/style rather than mechanism-specific representation.
- The most informative positive effect would be an interaction: structural context helps more on `transfer`, `counterfactual`, `diagnosis`, `composition`, or far-distance tasks than on near/local tasks.

## Leakage audit criteria

A hidden task is weak if its answer is stated or trivially paraphrased in the context. During audit, flag tasks where:

- the structural context names the exact requested conclusion rather than the mechanism;
- visible metadata gives a sufficient numeric answer (for example, exposing a full distinct-output count for a permutation question);
- a procedural context contains the exact future instance rather than a generic method;
- the context contains the same constants or witness that appear only in the hidden task;
- the shuffled source accidentally expresses the same mechanism under different terminology.

Gold set v0 already avoids exposing full distinct-output counts in the public situations and keeps exact answers in `private_truth.py`.

## Ceiling audit criteria

Do not make arithmetic larger merely to lower accuracy. Flag a task family if a strong base solver is essentially perfect under `none` context.

Preferred ways to increase discrimination are:

- change representation;
- require a consequence of the mechanism rather than its definition;
- introduce a plausible but unnecessary assumption;
- ask for a witness/counterexample;
- compose two transformations;
- distinguish coprime and non-coprime decompositions;
- diagnose why an analogy fails.

## Current known limitations

- The contexts are hand-written and share wording within clusters; this is useful for v0 control but could create phrase-level regularities.
- Most mathematics is elementary finite arithmetic, so a capable 8B model may show ceiling effects.
- The set tests whether an **externalized conceptual representation** helps a solver. It does not prove that the solver internally represents mathematics in the same way.
- Some tasks can be solved by brute-force reasoning. That is acceptable for scoring, but a positive Mathia signal should appear specifically in paired context differences rather than raw task difficulty.
- “Beauty” and canonicality are not directly tested in v0; they remain later hypotheses.

## Freeze rule

Once the first Qwen3-8B run begins, do not change these 20 situations or their hidden answers in response to results. Any fixes for genuine leakage/correctness defects create a new named version and the original result remains preserved.
