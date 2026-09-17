# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## Replace ordinary Gowers-smallness by a signed two-point covariance mechanism or a genuinely renormalized critical statistic

**Linked intuitions:** `MI-036-exact-zero-density-locks-bow-reciprocal-scale-at-riemann-siegel-length` through `MI-043-diagonal-cubes-squeeze-ordinary-gowers-smallness-to-one-critical-order-window`.

WI-322--WI-329 progressively remove sparsity, direct-duality contraction, raw-positive resonance and bow-height phase diversity as generic escape mechanisms. The exact signed source `Lambda-Lambda_X^sharp` destroys the generic raw-positivity resonance on typical starts, but varying bow heights does not create independent source starts.

WI-331 identifies a genuine regime split. When `0<theta<3/16`, the natural bow length lies inside an all-interval nilsequence theorem, so the distinguished-start exceptional-set problem disappears. For `3/16<=theta<=3943/12011`, the natural bow lies beyond that all-start range and the common exceptional-start issue remains.

WI-332--WI-334 close the obvious hierarchy of fixed-complexity black-box upgrades. Local `U^2` loses a factor of `K`; square-root cancellation against every fixed-degree polynomial phase can still leave the full diagonal variance; and power-small `U^s` control on every bow-scale interval for every order in any fixed finite hierarchy can coexist with sliding variance `(1+o(1))NK log N` against any prescribed unit carrier.

WI-335 then shows that allowing the order to drift slowly does not rescue ordinary Gowers smallness. A matched-energy Rademacher model keeps every local `U^s` small through orders satisfying `2^s loglog N=o(log K)` while preserving full diagonal sliding variance.

WI-336 supplies the complementary high-order obstruction. For an interval of length `L` and energy `E` comparable to `L log N`, diagonal zero-increment cubes give

`||f||_(U^s(I)) >= sqrt(E/(2L)) L^(-1/2^s)`.

With `R_s(L,N)=2^s loglog N/log L`, any comparable-energy source is forced to have non-small ordinary `U^s` at the diagonal threshold. Its original all-start Rademacher construction reached only below `R_s<=1-eta`, leaving a one-order concentration gap.

WI-337 closes that gap for **almost-all/density-one** information. For every fixed margin below `R_s=2`, one matched-energy Rademacher realization is simultaneously `U^s=o(1)` for all retained orders on a set of starts of density one, and those same good starts retain asymptotically the entire diagonal sliding variance.

WI-338 now closes the remaining **all-start/all-interval** ordinary-Gowers escape. The random cube count has an exact Walsh expansion; nonconstant cube characters have only subpower multiplicity, so Parseval plus Bonami--Beckner hypercontractivity concentrates every local `U^s` essentially at its `1/L` random scale simultaneously over all intervals. The countermodel reaches `R_s<=2-delta_N` for every `delta_N loglog N -> infinity`, exactly the asymptotic region in which the WI-336 diagonal floor permits `U^s=o(1)` at all. If `(2-R_s)_+ loglog N=O(1)`, the deterministic floor itself keeps the norm bounded away from zero.

The live theorem is therefore no longer rescued by changing the start quantifier while retaining the same ordinary-Gowers output. The stronger 2023 all-interval arithmetic theorem can still matter, especially below `theta<3/16`, but only through information richer than black-box `U^s=o(1)`: source-specific signed two-point covariance, the exact structured `Lambda^sharp` coupling, a relative linear-forms statement, or a statistic from which the diagonal cubes have been genuinely removed/renormalized.

The accepted local clue `CLUE-bow-distinguished-twist-offdiagonal-cancellation` carries the destination test: expand the exact distinguished-twist variance with `Lambda^sharp` retained in the same norm and prove either the required negative off-diagonal cancellation or a pointwise obstruction. WI-338 removes the last ordinary-Gowers quantifier/order detour: any continuation must change the observable or use source arithmetic that the norm list forgets.

## Keep source cancellation, start quantifiers, uniformity complexity, diagonal energy and covariance sign separate

Density-one source cancellation, all-start source cancellation, one-point phase pseudorandomness, fixed-order Gowers uniformity, growing-order Gowers smallness, diagonal-cube energy and pointwise Weil covariance are different statements. WI-331 settles the start quantifier only in the low-theta regime. WI-332--WI-336 show that increasingly rich generic one-point/uniformity information first fails to determine the needed signed covariance and then becomes impossible to keep small because the source's own diagonal energy enters the norm. WI-337 pushes generic countermodels to the diagonal threshold on density-one starts; WI-338 upgrades the same obstruction to every interval, at the exact shrinking-margin scale where ordinary norm smallness remains compatible with the energy.

A proposed bridge should therefore state separately: the source-start quantifier, the phase/Gowers family, the maximum order and its scaling with `K`, the quantitative norm strength, whether the diagonal cubes are retained or renormalized away, the exact diagonal contribution, the off-diagonal covariance it can force, and the mechanism giving the required sign. The decisive question is not whether the source looks pseudorandom against an increasingly rich generic hierarchy, but whether its **arithmetic two-point structure** can beat the diagonal variance at the distinguished bow twist.