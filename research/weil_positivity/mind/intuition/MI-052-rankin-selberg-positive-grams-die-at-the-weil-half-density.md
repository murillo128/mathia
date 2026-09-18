# MI-052 — Rankin--Selberg positive geometry fails at the Weil half-density even after projectivization

**Evidence level:** exact synthesis from [WP-363](../../findings/WP-363-eisenstein-rankin-selberg-gram-collapses-at-critical-exponent-and-first-jet-is-indefinite.md) and [WP-364](../../findings/WP-364-projective-rankin-selberg-geometry-fails-at-critical-zeros.md). The Rankin--Selberg factorization and Fubini--Study geometry are classical ingredients; the Mathia content is the critical-survival/sign audit.

For real spectral parameters `r,u` and real `s>1`, the Eisenstein Hecke coefficients give the genuine positive Gram kernel

`K_s(r,u)=sum_n lambda_r(n)lambda_u(n)n^(-s)`.

Its exact meromorphic factorization contains four zeta factors divided by `zeta(2s)`. WP-363 shows that the denominator pole at `s=1/2` forces the whole Gram to vanish precisely at the Weil half-density. The first nonzero critical jet is proportional to

`J(r,u)=F(r+u)F(r-u)`, with `F(t)=|zeta(1/2+it)|^2`,

and is not positive semidefinite: a critical zero can make one diagonal entry vanish while a generic off-diagonal entry remains positive. Taking the logarithmic derivative recovers the desired linear Mangoldt half-density only after the positive Gram category has collapsed and the zeta divisor has entered the meromorphic readout.

WP-364 tests the strongest canonical scalar-removal repair. For `s>1`, projectivize the Hecke coefficient vectors and form the normalized overlap

`C_s(r,u)=K_s(r,u)/sqrt(K_s(r,r)K_s(u,u))`.

The common `1/zeta(2s)` factor cancels **identically**, so this is a genuine intrinsic quotient of Hilbert vectors rather than a hand-chosen renormalization. Its source-defined critical continuation is

`C_*(r,u)=F(r+u)F(r-u)/(F(0)sqrt(F(2r)F(2u)))`.

Let `gamma` be any ordinate of a critical-line zero. For generic fixed `u`, the numerator remains nonzero while `F(2r)->0` as `r->gamma/2` through regular points. Hence

`|C_*(r,u)| -> infinity`,

violating the necessary projective Gram bound `|C|<=1` on punctured neighborhoods of the zero ray, not merely at the singular point itself.

The infinitesimal projective geometry fails with the same sign. The Fubini--Study pullback for `s>1` is

`g_s(r)=partial_r partial_u log K_s(r,u)|_(u=r) >= 0`.

After the common scalar has disappeared, the critical continuation becomes

`g_*(r)=(log F)''(2r)-(log F)''(0)`.

If `gamma` has multiplicity `m`, then `(log F)''(t)=-2m/(t-gamma)^2+O(1)`, so `g_*(r)->-infinity` as `r->gamma/2`. This sign cannot be repaired by a smooth reparameterization, and scalar Gamma/completion factors are invisible because Fubini--Study geometry is gauge-invariant under `v_r -> a(r)v_r`.

The reusable lesson is stronger than “non-scalar positivity must survive the critical specialization.” Even when the universal critical scalar collapse can be removed **canonically before continuation**, the inherited cross-parameter projective geometry can still lose its Hilbert inequalities at the target. A viable automorphic route must therefore alter the nonseparable finite--archimedean correlations themselves before the critical specialization, rather than normalize, complete or projectivize the bare Eisenstein coefficient family.

**Boundary.** This does not rule out all automorphic/cohomological positivity mechanisms, genuinely enlarged feature spaces, Maaß--Selberg remainder structures or noncentral operator couplings. It rules out the canonical level-one Eisenstein coefficient Gram, its first critical jet, scalar completions and its intrinsic projectivization as the missing Weil-positive object. No RH implication follows.