# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

Finite negative inertia detects off-line packets exactly but can lose coercivity with height. The unconditional critical-line exponentials are complete on bounded windows without forming a Bessel/Riesz family, so ordinary separation cannot rule out spectral collapse. Any truncation route still has to price coefficient growth and height tightness explicitly.

## Use amplitude-bearing null-mode structure beyond complete screening and support topology

**Linked intuitions:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols`, `MI-018-one-signed-first-crossings-pay-prime-overlap-or-short-range-mass`, `MI-019-simultaneous-cuts-create-a-positive-saturated-source-reserve`, `MI-020-complete-one-signed-screening-trades-discrete-vanishing-for-support-packing`.

WI-274--WI-280 separate scalar firstness, retained Hilbert orientation and source-specific compatibility. Arbitrary finite covariance mixtures on the generic PSD/null-partition class still admit two-pulse countergeometry, so generic Hilbert optimization does not cross the scalar budget wall by itself.

WI-281 shows that actual arithmetic screening can shrink the one-signed admissible class: powers of two force support packing modulo `log 2`, yielding the strict budget `K_pack<K_+`.

WI-282 proves that this packing mechanism is already sharp under two obvious refinements. The length-`log 2` optimizer automatically screens every active prime-power lag, so adding the other primes does not lower the relaxed supremum. Requiring full essential span also leaves the same supremum because arbitrarily small boundary satellites can enforce span while converging back to the packing optimizer.

WI-283 now closes the remaining qualitative support-topology refinement coming from the actual Suzuki null equation. Every true null mode satisfies a prime-translation support-domination condition, but a maximal open finite-distance-avoiding set can satisfy that domination while remaining exactly screened. Adding arbitrarily small `L^2` mass on the saturated support changes the support topology drastically while changing `B_+` arbitrarily little. Consequently

`nonnegativity + complete screening + full span + support domination`

still has exact supremum `K_pack`.

The next one-signed theorem must therefore consume **amplitude-bearing** information that the support relaxation discards: the full distributional equation `A_a f=0`, a quantitative lower mass requirement in prime-translated regions, regularity/nodal/boundary-flux estimates that force non-negligible amplitude at the support contacts, a signed balance identity between archimedean and von-Mangoldt terms, a positive first-crossing spectral-area margin, or simultaneous-cut relations coupling amplitudes at several cuts. The target remains a strict decrement below `K_pack` or another contradiction-strength invariant derived from actual null-mode structure.

The sign-changing branch remains separate. Screening no longer implies support disjointness there, so the one-signed packing argument cannot simply be transferred.

## Keep relaxation sharpness, support topology and source realization distinct

WI-281 proves a source-induced packing bound; WI-282 proves that complete screening and full span do not lower it; WI-283 proves that even the exact support-domination shadow of the null equation can be imposed at arbitrarily small analytic cost. None of those profiles is asserted to satisfy `A_a f=0`. A future improvement must distinguish realizable first null modes by a **quantitative amplitude/operator law**, not by another qualitative property of their support.

## Keep endpoint firstness, source reserve and sign geometry as separate gates

The reserve inequalities are sign-independent, while the packing bootstrap uses a one-signed mode. A stronger one-signed null-equation theorem would not prove that the relevant first mode has one sign, and a sign theorem would not by itself close the quantitative reserve. Future work should state which gate is being crossed.
