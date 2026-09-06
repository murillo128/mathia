---
id: CLUE-analytic-frontier-central-notch-base-margin-certificate
type: research-clue
status: resolved
origin: master-researcher
target_line: analytic_frontier
based_on:
  - research/analytic_frontier/findings/ANF-034-central-notch-perturbation-gives-an-explicit-finite-real-separator-ray.md
  - research/analytic_frontier/findings/ANF-046-central-notch-pair-functional-gain-dominates-exact-normalization-slack.md
  - research/analytic_frontier/findings/ANF-047-phase-blind-amplitude-variation-gives-an-explicit-five-point-coherence-certificate.md
  - research/analytic_frontier/findings/ANF-051-two-pair-five-point-danger-has-an-exact-anti-phase-tube-and-fixed-height-bandwidth-radius.md
  - research/analytic_frontier/findings/ANF-052-central-notch-two-pair-five-point-perturbation-is-cubic-on-bounded-heights.md
  - research/analytic_frontier/findings/ANF-053-central-notch-five-point-survival-reduces-to-montgomery-taylor-zero-freeness.md
  - research/analytic_frontier/findings/ANF-062-validated-interval-certificate-proves-montgomery-taylor-five-point-zero-freeness.md
---

# Does the fixed Montgomery--Taylor two-pair defect have any genuine zero?

## Observation

ANF-052 bounds the two-pair defect perturbation for `J_s=J_MT-s b_eta(1-|alpha|/eta)_+` by `O_Y(s b_eta eta^3)` on bounded heights, uniformly in horizontal placements, and supplies a high-height ceiling uniform over sufficiently narrow notches. ANF-046's pair-functional gain is of order `s b_eta`, with elementary normalization cost of order `s b_eta eta`. ANF-047 supplies the sufficient phase-blind test `Q+P>=L`; ANF-051 further restricts where a negative shape can occur.

ANF-053 fixes the perturbation sign: on bounded geometry boxes the leading correction is `-(5/3) pi^2 s b_eta (y_1^2+y_2^2) eta^3`. Every genuine base zero is destabilized by a sufficiently narrow notch. Conversely, the source proves a common obstruction box and shows that absence of genuine base zeros implies positivity for all sufficiently narrow notches. This superseded a search over progressively retuned notch parameters: the decision concerned one fixed base profile.

## Research question

Can `H_J_MT(y_1,y_2;t_1,t_2)=0` be excluded for all `y_1,y_2>0`, or can one genuine solution be certified? Use ANF-053's equivalence to obtain the consequence for the notch family, then retain the separately calculated affine/multiplicity gain. This is a bounded subproblem of the accepted universal-certificate clue, not another proposal to optimize the entire scalar class.

## Why it may matter

A complete sign decision converts the recent reductions into a usable finite certificate or eliminates a concrete candidate. It also identifies whether the remaining difficulty is a genuine base zero set or merely certification precision.

## Decisive test

Use the source's common obstruction box and exact separation exclusions. On the remaining nondegenerate region, certify a strictly positive base margin, applying `Q+P>=L` first and phase-aware bounds only where needed. Preserve the small-height and boundary arguments that justify the common box rather than asserting a positive minimum on an arbitrary interior subset.

Return either a complete proof of base zero-freeness, with exact inequalities or outward-rounded domain enclosures, or a rigorously certified genuine base zero. A negative base value would also refute zero-freeness by the source's continuity argument. An interval merely containing zero is inconclusive. In the positive case, use the certified margin and ANF-052 to exhibit an admissible notch; in the zero case, apply the signed cubic law to certify a negative notched witness. Keep the ANF-046 normalization check separate from this sign decision.

## Evidence boundary

The original clue supplied no base margin, admissible numerical parameter choice, or complete five-point certificate. Even the successful five-point certificate leaves larger multisets and the full zeta implication to be established. A failed sufficient phase-blind test is not a counterexample to the exact defect inequality.

## Research disposition

Resolved by `ANF-062`. Mathia issue #121 supplied a validated Arb/FLINT certificate for the exact fixed Montgomery--Taylor defect after the canonical outer-domain reductions: the residual rational cover inspected `804375` boxes, left no unresolved cells, certified `H_MT/(y1^2+y2^2)>3.91727782744812265709656e-6` on the residual enclosure, and separately covered the zero-height neighborhood and the common-translation half-line with analytic bounds. Research Watch reconstructed the cancellation-safe normalized integrand from `ANF-045` and verified that no load-bearing `analytic_frontier` finding changed between the compute source revision and canonicalization.

Therefore `H_MT>0` on every genuine two-pair geometry. By the equivalence in `ANF-053`, every sufficiently narrow nontrivial central notch has positive five-point defect throughout the genuine two-pair domain. This resolves the clue's exact decision problem; it does not settle larger conjugation-invariant multisets or imply RH.