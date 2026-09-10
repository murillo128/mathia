---
id: CLUE-clean-peak-selector-height-coupling
type: research-clue
status: accepted
origin: master-researcher
target_line: robin_extremal
based_on:
  - research/robin_extremal/findings/RE-005-regular-self-tangent-ca-peak-values-are-not-globally-monotone.md
  - research/robin_extremal/findings/RE-006-clean-first-layer-peaks-force-an-exact-chebyshev-residual-window.md
  - research/robin_extremal/findings/RE-007-clean-peaks-force-a-square-root-prime-gap-or-chebyshev-excursion.md
  - research/robin_extremal/findings/RE-008-clean-robin-counterexamples-force-square-root-endpoint-subtracted-mertens-excursions.md
  - research/robin_extremal/findings/RE-021-self-tangent-robin-height-threshold-survives-exceptional-boundaries.md
  - research/robin_extremal/findings/RE-022-self-tangent-mixed-race-height-localizes-to-a-finite-annulus-across-every-ca-boundary-chamber.md
---

# Does the clean-peak selector constrain Robin height through a shared signed prime-error remainder?

## Observation

RE-006 selects a clean regular self-tangent CA local peak by the exact relation

\[
X-p=\Phi_{\ge2}(X)-\bigl(p-\vartheta(p)\bigr),\qquad p<X<q,
\]

where `X=log C` and `p<q` are its consecutive first-layer boundary primes. RE-007 sharpens the square-root accounting to

\[
\psi(p)-p=(X-p)-(\sqrt2-1)\sqrt p+o(\sqrt p).
\]

These conditions concern the location of a clean local peak. They do not distinguish a safe peak from one above the Robin barrier. In particular, a negative endpoint value of `psi(p)-p` does not by itself bound an Euler product accumulated over all smaller primes. RE-005 supplies actual safe local peaks against which any proposed implication must be checked.

## Research question

Can the same prime-layer source that forces the clean-peak selector also control the signed Euler-product remainder determining the peak's height, without estimating the selector and the height independently by RH-strength errors?

For `C=product_(r<=p) r^(a_r)`, define the finite quantities

\[
E(p)=\sum_{\substack{r\le p\\r\ \mathrm{prime}}}
-\log(1-r^{-1})-\gamma-\log\log p,
\qquad
T(C)=-\sum_{\substack{r\le p\\r\ \mathrm{prime}}}
\log(1-r^{-(a_r+1)}).
\]

Reconstruct the exact factorization checkpoint

\[
\log G(C)-\gamma
=E(p)-T(C)+\log\frac{\log p}{\log X},
\qquad G(C)=\frac{\sigma(C)}{C\log\log C}.
\]

The proposed mechanism is not this classical identity. It is to combine its signed prime-error terms with the exact RE-006 selector before applying separate absolute-value bounds, and test whether this exposes an independently estimable remainder on a stated infinite subfamily of clean peaks.

## Why it may matter

The clean selector and the height are driven by the same primes, but use different weights and different amounts of history. Treating their errors as independent loses any cancellation; treating an endpoint constraint as control of the entire history invents cancellation. An exact joint decomposition can decide which situation actually holds.

A useful outcome would be an unconditional height bound on a nontrivial proper infinite class relevant to the extremal reduction, with the missing estimate genuinely weaker than Robin or a comparably strong prime-error theorem. Alternatively, it may identify a signed historical remainder not controlled by the selector, making the limitation precise without dismissing the entire Robin line.

## Decisive test

First verify the factorization above with the complete `log log C` normalization. Use the actual prime-exponent thresholds to determine `T(C)` and `Phi_(>=2)(X)` from the same `C`; they are not independent adjustable corrections. Express `E(p)` by exact finite partial summation or a Stieltjes identity in `vartheta` or `psi`, retaining prime-power corrections and all boundary terms. Insert the exact clean-peak relation and determine whether the endpoint error cancels, reinforces another term, or leaves a genuinely uncontrolled signed historical integral.

Audit this combined expression against the line's existing Ramanujan/Nicolas and self-tangent-workload prior art before claiming a new mechanism. If it is only a known divisor-sum expansion or the old workload under another parameter, record that collision rather than creating a duplicate finding.

Then formulate one candidate inequality for the remaining source integral and exponent-tail term on an explicitly defined subfamily. Its hypotheses must be checkable without assuming the desired sign of `log G(C)-gamma`. Prove the candidate from weaker source input, or produce admissible controls defeating that particular implication. Replacing the claim by `E(p)<=T(C)-log(log p/log X)` without an independent estimate is simply Robin rewritten, not progress.

Keep RE-007's small-gap/tuned-excursion and square-root-gap alternatives separate. A result in one does not eliminate the other. RE-021 and RE-022 now show, however, that higher-layer or tied **adjacent CA transitions do not create a separate height or tail-localization chamber**: every regular self-tangent state has a canonical last active first-layer prime, the same mixed-race height threshold, and the same finite-annulus localization. Exceptional transitions remain relevant to the local peak selector and event-ladder geometry, not to the asymptotic height decomposition itself.

Likewise, RE-006 does not put every peak in a window of width `O(log p)`: the width depends on the actual gap. Use logarithmic-resolution claims only with the necessary additional gap restriction, and do not substitute RE-007's `o(sqrt p)` remainder where the exact smaller-scale selector is needed.

Reproduce the two genuine local-peak controls from RE-005 when testing a universal strengthening, and classify their boundary transitions before applying a clean-only statement. The original `720720` and `6983776800` controls are self-tangent states, not local peaks. Finite safe examples can falsify an overstrong inequality but cannot establish an asymptotic sign law. Any synthetic prime-error control must preserve the exact hypotheses it purports to test; it is not a counterexample to the ordinary-prime theorem merely because it matches an endpoint.

## Evidence boundary

The original clue was posed in the clean first-layer chamber. RE-008 established the exact endpoint cancellation there; RE-021 subsequently removed the clean-boundary hypothesis from the height dictionary and all-orders CA tax; RE-022 removes it from the two-sided finite-annulus localization as well. These are durable hypothesis removals, not an estimate excluding the remaining source excursion.

No unconditional upper bound for the selected annular mixed-race integral, no conditional sign law usable under hypothetical RH failure, and no exclusion of an infinite counterexample family has been established. Global one-sided control of the mixed race is already RH-equivalent by RE-009, so the unresolved estimate must use the CA-selected host structure rather than restate Robin or impose an RH-strength global error bound.

## Research disposition

Accepted, with scope generalized beyond the original clean chamber. RE-008 reconstructs the exact splice and shows that partial summation of the Mertens product produces an endpoint term `(vartheta(p)-p)h(p)` which cancels after inserting self-tangency. The surviving quantity is the endpoint-subtracted Mertens remainder

\[
\mathcal M_*(p)=E(p)-(\vartheta(p)-p)h(p).
\]

RE-021 proves that the same height identity and the sharp `2sqrt(2)` threshold hold at **every** sufficiently large regular self-tangent CA state, regardless of higher-layer or tied adjacent boundaries. RE-022 further proves that, for every fixed `alpha<3/4` and every sufficiently large fixed PNT-inversion parameter `A`, any self-tangent counterexample would have to satisfy

\[
\liminf
\sqrt p\log p
\int_{p+p^\alpha}^{U_A(p)}
\left[
(\vartheta(t)-t)h'(t)-(h(t)-k(t))
\right]dt
\ge2\sqrt2.
\]

The unresolved question is therefore source-specific and now universal across transition chambers: can the CA-selected first-layer frontier primes of hypothetical self-tangent counterexamples realize this positive **finite-annulus** mixed Mertens--Chebyshev excursion infinitely often, or can the selector/event-host geometry exclude it by an unconditional estimate genuinely weaker than Robin? Clean adjacent transitions still provide extra local constraints through RE-006 and RE-007, while RE-017--RE-020 constrain exceptional hosts, but neither class currently controls the annular signed mass.