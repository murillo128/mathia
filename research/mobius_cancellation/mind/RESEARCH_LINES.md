# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Control the signed linear residual at the rowwise Christoffel margin before aggregation hides the blind atom

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category`, `MI-014-centered-parity-and-zero-mode-are-separate-currencies`, `MI-015-sign-support-covariance-gives-a-conditioned-quadratic-bridge`, `MI-016-source-aligned-shifts-face-a-defect-or-mertens-dichotomy`, `MI-017-first-shell-crt-common-mode-is-a-source-coupled-energy-coordinate`, `MI-018-nonnegative-transference-does-not-create-fixed-power-sign-balance`, `MI-019-shell-square-blindness-is-a-cross-prime-common-quotient-problem`, `MI-020-explicit-large-sieve-uniformity-stops-before-blind-support-scale`, `MI-021-support-matched-high-moments-cross-the-single-blind-shell-threshold`, `MI-022-positive-shell-envelopes-erase-the-phase-cancellation-needed-below-the-blind-atom`, `MI-023-negative-witness-collapse-trades-rowwise-simplicity-for-source-depth`.

MC-266--MC-272 close arbitrary-coefficient operator norms, positive generating majorants and raw complex-circle norms at the one-blind-row threshold. MC-273--MC-275 then separate witness discovery from normalization: a negative witness collapses a row to one homogeneous shell, all negative witnesses can be aggregated at degree only `m+1`, but exact or pointwise approximate normalization reconstructs Boolean OR and spends too much source degree on the generic cube.

MC-276 closes the natural distributional escape. Quadratic/L2 normalization with the correct blind-point value is cheap because its loss removes the blind atom exactly. The uniform optimizer is the same Christoffel kernel already present in the endpoint-energy route, and on the arithmetic shell

`empirical L2 error = (E_(m,y)(t)-A_y(t))/C`.

MC-277 now shows that this failure is **not** loss of the blind bit inside the degree-`m` row representation. The normalized Christoffel scalar `P_m=g_m/Z_m` equals `1` on the blind vector and is at most `h=binom(k-1,m)/Z_m` on every nonblind vector, with equality already on one-negative rows. Its exact separation margin is

`delta_(k,m)=1-h ~ 2m/k`.

Uniform adversarial scalar noise is tolerable exactly below `delta_(k,m)/2`, and every Lipschitz decoder pays condition number at least `1/delta_(k,m)`. At the live support-matched scale the rowwise robustness radius is only polynomially small, of order `log y log log y/y`, while the mass of one exceptional target row is vastly smaller. Thus the current representation retains blindness; the severe loss appears when many row identities are aggregated and one asks a scalar sum, norm or loss to certify that **no** exceptional row exists.

The live theorem is therefore sharper than another classifier construction. Control the existing row scalar at its natural margin using arithmetic information **before** row identities are discarded, or derive genuinely signed cross-row cancellation in the linear residual while retaining enough provenance that one blind contribution cannot be masked by nonblind phase. Equivalently, control the original uncentered Christoffel energy without replacing it by a loss that subtracts the target atom.

## Keep representation, conditioning, normalization and aggregation separate

A negative witness simplifies one row; overlapping all witnesses remains low-degree; pointwise normalization is generically expensive; L2 normalization is cheap but target-blind; and MC-277 proves that the unnormalized row scalar itself still has an exact blind/nonblind gap. These are different statements. A future proof should state whether its observable preserves the target atom, what noise scale it controls relative to `delta_(k,m)`, and where aggregation over the `C` target rows first loses exceptional-row provenance.

MC-252 remains the matched control: once tight prime-shell localization is removed, genuine separated-prime Legendre data can realize the full Boolean cube. Any signed escape must therefore use localized arithmetic structure or a source-specific cross-row relation, not the generic polynomial-threshold geometry by itself.
