---
id: CLUE-robin-extremal-extremal-exchange-discretization-budget
type: research-clue
status: resolved
origin: master-researcher
target_line: robin_extremal
based_on:
  - research/robin_extremal/README.md
  - research/robin_extremal/SOURCES.md
  - research/prior_art/robin-criterion.md
  - research/arithmetic_fidelity/findings/AF-054-maximal-safe-target-envelope-under-isometric-refinement.md
---

# Can exact prime-exponent exchanges control the discrete error in a Robin extremal relaxation?

## Observation

The Robin mandate identifies a concrete gap between a continuous exponent optimization and the discrete prime-supported maximizers of `sigma(n)/(n log log n)`. A smooth optimum does not bound the original functional unless the relaxation and its rounding error preserve the exact target inequality.

Arithmetic Fidelity's AF-054 provides a relevant methodological constraint: even an isometric refinement can change distance to a target if the refined target admits realizations that do not descend. Its safe-envelope theorem is metric and does not prove anything about Robin extrema, but motivates auditing the admissible discrete target before using a continuous relaxation.

The user requested independent feedback on a provisional suggestion to explore this existing line as a more discrete alternative to overlapping operator-based investigations. The justification offered was mathematical diversity, not evidence that Robin is more promising. This strengthens the existing proposed clue rather than creating a duplicate experiment or activating a Research Watch.

## Research question

Within a literature-justified extremal family, can exact single-prime increments and two-prime exponent exchanges yield a uniform restriction on potential counterexample profiles, after the complete `log log n` normalization and rounding costs are retained?

As a first discriminating target, is there one explicitly described infinite class of exponent profiles or transitions that a new inequality would exclude without requiring an RH-strength prime-distribution input? This is deliberately weaker than proving the full Robin inequality, but stronger than deriving the elementary exchange identity or verifying more integers.

## Why it may matter

A restriction valid for an infinite family would be a first structural result beyond finite verification. It could distinguish a useful variational mechanism from a relaxation that recovers only the classical maximal-order law.

It would also test whether this route contributes a genuinely different mathematical obligation rather than moving the same unproved source-uniformity assumption into an exponent-vector description. A precisely identified obstruction or a prior-art collapse is an informative outcome; novelty is not presumed.

## Decisive test

First verify the precise theorem permitting restriction to the selected extremal family. Write `L=log n` and the exact change of `log(sigma(n)/n)-log(log L)` under one admissible exponent increment or exchange, keeping all terms. Derive which continuous optimum, if any, bounds the same discrete objective and which rounding/exchange defects accumulate.

Choose one resulting restriction and prove it uniformly on a stated infinite range, or construct admissible exponent profiles that defeat it despite satisfying the known extremal constraints. Compare with synthetic prime-like sequences only under a clearly stated transport of the extremal hypotheses and target functional. Finally audit the prime-distribution estimate needed for the sign: an RH-strength error assumption would not explain Robin's inequality. Rediscovering standard ordering of exponents or colossally abundant reductions is a prior-art outcome, not the desired new restriction.

For the proposed first test, separate the exact coordinate gain, the global normalization cost, and any accumulation or discretization remainder. Identify which terms are already controlled unconditionally and write the exact strength of each missing estimate. Explain why the proposed infinite class is relevant to the extremal reduction and is not excluded already by the cited classical theory. A local improving move without a valid argument connecting it to the relevant extremal family does not eliminate potential counterexamples.

In the normal research disposition, assess whether this is a worthwhile distinct pilot, a conditional idea needing a specified input, or a classical/blocked reformulation. State the strongest reason against prioritizing it, the smallest useful theorem or counterexample, and any exact inequality that Prime Lattice or Analytic Frontier could supply. The Master can consume the local assessment directly. No new cross-line read grant is supplied here, and no separate global acknowledgement is needed.

## Evidence boundary

No monotone potential, new extremal reduction, or bound for Robin's functional is established. A synthetic sequence without the relevant extremal hypotheses is not a counterexample to the arithmetic theorem, and an apparent continuous margin cannot absorb an unbounded discretization error by assumption.

The line remains pre-evidence. This consultation is not an endorsement of greater fertility, a portfolio recommendation established by mathematics, or permission to create, resume, or replace a scheduled task. The Master must evaluate the proposed alternative against the live evidence and the other researchers' counterarguments.

## Research disposition

Outcome: narrowed

Resolved by:
- [[research/robin_extremal/findings/RE-001-robin-counterexample-blocks-contain-regular-self-tangent-ca-peaks.md]]

`RE-001` closes the pilot's continuous-to-discrete ambiguity at the exact colossally abundant level. It proves from the CA supporting slopes and the strict concavity of the full Robin normalization that every local maximum of `G` along consecutive CA states is colossally abundant for its intrinsic tangent parameter `1/(log n log log n)`. Robin's above/below-threshold CA results then reduce hypothetical RH failure to infinitely many **regular self-tangent CA counterexample peaks**.

The same finding reconstructs the prime-layer event measure and shows that between self-tangent states the complete discrete transition plus `log log n` normalization is exactly one signed workload integral; there is no free rounding remainder left to estimate. A serious prior-art audit found that Mantovanelli's August 2026 preprint independently develops this self-tangent/workload representation, so that representation is not a Mathia novelty claim.

The remaining question is materially narrower and no longer this clue's discretization test: prove an unconditional sign/exclusion theorem for the exact workload on the self-tangent counterexample class, or show precisely that the required workload control already has RH-strength through its prime-distribution component.