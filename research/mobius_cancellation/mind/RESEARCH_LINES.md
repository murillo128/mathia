# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Price factor-lift information after source projection and symmetry quotient

**Linked intuitions:** `MI-073-source-mode-averaging-collapses-to-a-signature-projector`, `MI-074-thin-hyperbolic-shells-tax-independent-coordinate-bandwidth`, `MI-075-exact-product-tangent-fibers-have-subpolynomial-state-volume`, `MI-076-fixed-depth-factor-lifts-cannot-amplify-the-short-shell-state-exponent`, `MI-077-factor-multiplicity-does-not-survive-a-mobius-sign-projection`, `MI-078-unbounded-additive-factor-data-buys-state-capacity-only-through-retained-precision`, `MI-079-permutation-invariant-factor-size-needs-inverse-logarithmic-precision-for-polynomial-state-capacity`, `MI-080-fixed-dimensional-symmetric-factor-data-obeys-a-dimension-precision-law`, `MI-081-exact-factor-identity-has-near-linear-orbit-capacity-but-mobius-sign-erases-it`.

MC-423--MC-425 show that fixed-depth exact-product fibers, whole short factor shells and arbitrary-depth Möbius-sign words do not manufacture an additional polynomial source exponent. MC-426--MC-428 then price bounded and unbounded additive summaries: after quotienting factor-slot permutations, scalar log-size needs inverse-logarithmic precision before polynomial orbit-state capacity is even possible.

MC-429 extends that count to every fixed-dimensional nonnegative additive vector summary. For `k` retained coordinates with total `O(log X)` mass, polynomial symmetric state capacity forces inverse precision at least `(log X)^(1/k)`; every strictly smaller power remains subpolynomial. Finite dimension can trade against precision, but it does not make coarse resolution free.

MC-430 then identifies a genuine boundary of all those coarse-summary counts. Full exact factor identity has Bell-number orbit capacity: along squarefree primorials it carries `n^(1-o(1))` unordered factor states. This capacity is real even after quotienting factor order. Yet projecting those exact factors to the unordered multiset of their Möbius signs collapses the same family to only `O(omega(n)^2)` states. The surviving information is therefore prime-block incidence, not factor multiplicity or sign alone.

The live question is now semantic rather than merely combinatorial. Can an exact-identity or comparably rich relational factor lift feed the cancellation mechanism **before** source projection destroys its Bell-scale information? If only fixed-dimensional additive summaries survive, MC-429 gives the precision tariff. If full identities survive, the mechanism must specify which prime-block relations are analytically observable, how they avoid collapsing to the symmetric sign quotient, and why those relations contribute to Möbius cancellation rather than only to raw decoding capacity.

## Audit labels, state count, retained precision and closure faces in the same coordinates

MC-423--MC-430 show that tangent dimension, raw factor multiplicity, Möbius-sign words, additive coordinate count, precision, named factor slots and exact factor identity are different currencies and must be charged in the order actually used by the destination.

Any proposed escape should remove unit padding, project to the datum actually consumed, quotient factor permutations unless the slots have a proved asymmetric role, price retained dimension and precision, and only then count independent channels. Exact factor identity now demonstrably escapes the coarse state-count barrier, but only by retaining prime-block incidence that the Möbius-sign quotient erases. A viable construction must show that this richer relation survives coefficient formation, shell aggregation, positivity/closure and final cancellation; Bell capacity by itself is not analytic leverage.