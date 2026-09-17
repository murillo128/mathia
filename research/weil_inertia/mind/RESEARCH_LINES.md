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

With `R_s(L,N)=2^s loglog N/log L`, any comparable-energy source is forced to have non-small ordinary `U^s` once `R_s>=2+eta`. Its first all-start random-sign construction reached only `R_s<=1-eta`, while WI-337 pushed density-one countermodels to every fixed margin below `R_s=2`.

WI-338 now closes the remaining **all-start** gap at the natural diagonal threshold. For `K=N^(kappa+o(1))`, one matched-energy Rademacher realization can be chosen so that simultaneously on every interval `I` with `K<=|I|<=2K` and every order satisfying

`R_s(K,N) <= 2-delta_N`,  with  `delta_N loglog N -> infinity`,

one has `||b||_(U^s(I))=o(1)`, while the same realization retains the full diagonal sliding variance `(1+o(1))NK log N`. The proof uses the Walsh expansion of the cube count, a subpower multiplicity bound for each nonconstant character, the resulting very small `L^2` fluctuation, and Bonami--Beckner hypercontractivity to union-bound over all intervals and retained orders.

This matches the deterministic diagonal floor at its natural resolution. If `R_s=2-delta_N` with `delta_N loglog N=O(1)`, ordinary normalized `U^s=o(1)` is already impossible for every comparable-energy source; whenever the diagonal floor itself tends to zero by `delta_N loglog N->infinity`, WI-338 supplies an all-interval countermodel with full destination variance. There is therefore **no remaining ordinary-Gowers order window, even under an all-start theorem**, in which mere `U^s=o(1)` can force the WI-195 signed covariance saving.

The live theorem is no longer a stronger ordinary-Gowers statement. A viable route must retain information that this interface discards: prove source-specific signed two-point covariance for `Lambda-Lambda^sharp`, establish a relative linear-forms statement that keeps the distinguished shifted-prime structure, subtract or renormalize the diagonal cubes before measuring higher-order structure, or define another statistic that couples directly to the distinguished bow variance.

The accepted local clue `CLUE-bow-distinguished-twist-offdiagonal-cancellation` carries the destination test: expand the exact distinguished-twist variance with `Lambda^sharp` retained in the same norm and prove either the required negative off-diagonal cancellation or a pointwise obstruction. WI-338 makes the generic-norm alternative definitive: increasing the order of an **ordinary** normalized Gowers norm cannot bridge the bow variance, regardless of whether the source theorem is all-start or density-one, except by changing the statistic itself.

## Keep source cancellation, start quantifiers, uniformity complexity, diagonal energy and covariance sign separate

Density-one source cancellation, all-start source cancellation, one-point phase pseudorandomness, fixed-order Gowers uniformity, growing-order Gowers smallness, diagonal-cube energy and pointwise Weil covariance are different statements. WI-331 still matters because it determines where existing arithmetic inputs hold all-start, but WI-338 shows that this stronger quantifier does not rescue the ordinary-Gowers black-box interface. WI-332--WI-338 now squeeze that interface from both sides at the same natural threshold: below the diagonal wall, random-sign sources can look Gowers-small while retaining full variance; at the wall, the source's own energy prevents ordinary smallness.

A proposed bridge should therefore state separately: the source-start quantifier, the phase/Gowers family, the maximum order and its scaling with `K`, the quantitative norm strength, whether the diagonal cubes are retained or renormalized away, the exact diagonal contribution, the off-diagonal covariance it can force, and the mechanism giving the required sign. The decisive question is not whether the source looks pseudorandom against an increasingly rich generic hierarchy, but whether its **arithmetic two-point structure or a genuinely diagonal-free statistic** can beat the diagonal variance at the distinguished bow twist.
