# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## Replace generic uniformity hierarchies by a signed two-point covariance mechanism

**Linked intuitions:** `MI-036-exact-zero-density-locks-bow-reciprocal-scale-at-riemann-siegel-length` through `MI-042-any-fixed-finite-hierarchy-of-local-gowers-norms-can-miss-the-bow-covariance-sign`.

WI-322--WI-329 progressively remove sparsity, direct-duality contraction, raw-positive resonance and bow-height phase diversity as generic escape mechanisms. The exact signed source `Lambda-Lambda_X^sharp` destroys the generic raw-positivity resonance on typical starts, but varying bow heights does not create independent source starts.

WI-331 identifies a genuine regime split. When `0<theta<3/16`, the natural bow length lies inside an all-interval nilsequence theorem, so the distinguished-start exceptional-set problem disappears. For `3/16<=theta<=3943/12011`, the natural bow lies beyond that all-start range and the common exceptional-start issue remains.

WI-332--WI-334 close the obvious hierarchy of fixed-complexity black-box upgrades. Local `U^2` loses a factor of `K`; square-root cancellation against every fixed-degree polynomial phase can still leave the full diagonal variance; and power-small `U^s` control on every bow-scale interval for every order in any fixed finite hierarchy can coexist with sliding variance `(1+o(1))NK log N` against any prescribed unit carrier.

WI-335 now makes the previously open `K`-dependent-order escape quantitative. A single Rademacher model with the same `log N` diagonal-energy normalization has

`sup_(I, 2<=s<=S_N) ||b||_(U^s(I)) = o(1)`

on every interval `K<=|I|<=2K` whenever

`2^(S_N) log log N = o(log K)`,

while its twisted sliding square remains `(1+o(1))NK log N`. In particular the obstruction reaches hierarchies with `S_N=(1-o(1))log_2 log K`.

This does **not** prove that order `~log log K` is sufficient. It says that a generic norm-only route cannot escape merely by allowing the Gowers order to drift slowly with scale. Any such route must reach essentially the `log log K` complexity scale with quantitatively stronger information that actually controls the bow covariance, or use arithmetic structure outside generic Gowers smallness.

The live theorem below `theta<3/16` is therefore genuinely **signed two-point control**: an arithmetic covariance identity, a source-fixed diagonal subtraction before sign information is lost, or another theorem that directly forces a macroscopic negative off-diagonal contribution at the WI-195 scale. Above `3/16`, the same covariance problem remains together with the location/exceptional-start quantifier.

The accepted local clue `CLUE-bow-distinguished-twist-offdiagonal-cancellation` already carries the destination test: expand the exact distinguished-twist variance with `Lambda^sharp` retained in the same norm and prove either the required negative off-diagonal cancellation or a pointwise obstruction. WI-335 narrows the admissible tools for that test; it does not resolve the clue.

## Keep source cancellation, start quantifiers, uniformity complexity and covariance sign separate

Density-one source cancellation, all-start source cancellation, one-point phase pseudorandomness, fixed-order Gowers uniformity, growing-order Gowers smallness and pointwise Weil covariance are different statements. WI-331 settles the start quantifier only in the low-theta regime. WI-332--WI-335 show that even very rich generic one-point/uniformity information need not imply the signed covariance needed after squaring.

A proposed bridge should therefore state separately: the source-start quantifier, the phase/Gowers family, the maximum order and its scaling with `K`, the quantitative norm strength, the exact diagonal contribution, the off-diagonal covariance it can force, and the mechanism giving the required sign. The decisive question is not whether the source looks pseudorandom against an increasingly rich generic hierarchy, but whether its **arithmetic two-point structure** can beat the diagonal variance at the distinguished bow twist.