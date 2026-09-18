# MI-052 — Rankin--Selberg positive Grams die at the Weil half-density

**Evidence level:** exact synthesis from [WP-363](../../findings/WP-363-eisenstein-rankin-selberg-gram-collapses-at-critical-exponent-and-first-jet-is-indefinite.md). The Rankin--Selberg Euler factorization is classical; the Mathia content is the critical-survival/sign audit of this canonical positive kernel.

For real spectral parameters `r,u` and real `s>1`, the Eisenstein Hecke coefficients give the genuine positive Gram kernel

`K_s(r,u)=sum_n lambda_r(n)lambda_u(n)n^(-s)`.

Its exact meromorphic factorization is

`K_s(r,u)=zeta(s+i(r+u))zeta(s+i(r-u))zeta(s-i(r-u))zeta(s-i(r+u))/zeta(2s)`.

This is stronger than the one-dimensional scalar Eisenstein completion: cross-parameter arithmetic coherence is present before positivity, and the kernel is positive semidefinite in its convergence half-plane.

The critical exponent destroys that advantage. At `s=1/2`, the pole of `zeta(2s)` forces

`K_(1/2)(r,u)=0`

for every real `r,u`. The whole positive Gram collapses precisely where the Weil prime amplitude would have the desired half-density. Positivity does not merely square the coefficient here; the canonical Rankin--Selberg diagonal normalization annihilates the carrier.

Renormalizing by the first nonzero `s`-jet does not preserve the cone. Up to the normalization used in WP-363,

`J(r,u)=F(r+u)F(r-u)`, with `F(t)=|zeta(1/2+it)|^2`.

Although every entry of `J` is nonnegative, `J` is not positive semidefinite. If `gamma` is a critical zero ordinate and `r=gamma/2`, then `J(r,r)=0`, while a generic `u` can make `J(r,u)>0`; the corresponding `2x2` principal determinant is negative. The first surviving infinitesimal layer is therefore not another hidden positive Gram.

The logarithmic derivative shows where the desired arithmetic coefficient reappears:

`-d_s log K_s = 4 sum_n Lambda(n)n^(-s) cos(r log n)cos(u log n) - 2 sum_n Lambda(n)n^(-2s)`

in the absolute-convergence region. Formally at `s=1/2`, the first term has exactly the linear Mangoldt half-density that the Weil criterion wants. But this readout is reached only after taking a logarithmic derivative of the collapsed kernel; meromorphic continuation imports the zeta divisor and the inherited Gram positivity is gone.

The reusable lesson is that **non-scalar positivity is not enough; the positive object must survive the critical specialization in the same category that carries the linear arithmetic amplitude**. A canonical positive family can contain rich arithmetic correlations for `s>1` yet become identically zero at the target exponent, while its first nonzero renormalization loses positivity.

For the automorphic route, the remaining structural possibility must couple finite arithmetic to archimedean/scattering data before the `1/zeta(2s)` Rankin--Selberg diagonal factor, or replace this closure by a different source-forced positive/order structure whose critical limit remains nondegenerate and whose sign is not reconstructed from the target divisor.

**Boundary.** This does not rule out all automorphic or higher-rank positivity mechanisms, all Maaß--Selberg remainder terms, or all renormalized kernels. It rules out reading the canonical level-one Eisenstein Rankin--Selberg Gram, or its first critical jet, as the missing Weil-positive object. No RH implication follows.