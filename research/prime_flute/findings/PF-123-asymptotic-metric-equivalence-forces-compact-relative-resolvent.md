# PF-123 — asymptotic metric equivalence forces compact relative resolvent

**Status:** `LITERATURE+DERIVED + CONDITIONAL/NEGATIVE`. The operator theorem is established prior art: Georgescu--Golénia prove compactness of the resolvent difference for complete Riemannian structures whose metric and volume coefficients are uniformly equivalent and tend to each other at infinity. The project-specific conclusion is that the accepted prime/shift-clone operator clue has **no additional decay-rate or integrability gate at the compact-resolvent level**. If the still-missing global marked comparison has metric distortion tending to `1` and volume-density ratio tending to `1`, then compact relative resolvent and equality of essential Laplace spectra follow. This finding does not construct that global comparison and does not claim trace-class, scattering, resonance, determinant, or RH consequences.

## Claim

Let `X` be the underlying topological/smooth flute, let `g` be the complete exact prime-flute metric, and let `g_+` be the shift-clone metric transported to `X` by a marked homeomorphism `F`. Assume the transported metric is locally bounded measurable and locally uniformly positive and that, outside a compact head, the two cotangent norms satisfy

\[
\alpha(x)\,|\xi|_g\le |\xi|_{g_+}\le \beta(x)\,|\xi|_g
\tag{1}
\]

for all cotangent vectors, with global constants

\[
0<c\le \alpha(x)\le \beta(x)\le C<\infty
\tag{2}
\]

and

\[
\boxed{\alpha(x)\to1,\qquad \beta(x)\to1\qquad (x\to\infty).}
\tag{3}
\]

Let

\[
\lambda(x)=\frac{d\operatorname{vol}_{g_+}}{d\operatorname{vol}_g}(x).
\tag{4}
\]

If

\[
\boxed{\lambda(x)\to1}
\tag{5}
\]

(and hence, after enlarging the compact head if needed, `lambda` is globally bounded above and below by positive constants), then Georgescu--Golénia Theorem 5.3 and Proposition 5.4 apply. If

\[
J:L^2(X,d\operatorname{vol}_{g_+})\longrightarrow L^2(X,d\operatorname{vol}_g)
\]

is the identity on functions, viewed as a bounded invertible topological identification, then

\[
\boxed{
(\Delta_g+1)^{-1}
-
J(\Delta_{g_+}+1)^{-1}J^{-1}
\in \mathcal K\bigl(L^2(X,d\operatorname{vol}_g)\bigr).
}
\tag{6}
\]

Consequently

\[
\boxed{\sigma_{\mathrm{ess}}(\Delta_g)=\sigma_{\mathrm{ess}}(\Delta_{g_+}).}
\tag{7}
\]

The important point for the prime-flute program is that (3)--(5) are **vanishing-at-infinity conditions only**. No `L^1`, `L^2`, Schatten, finite-volume, bounded-injectivity-radius, or quantitative convergence-rate assumption is present in Proposition 5.4.

Thus, for the accepted shift-clone clue, once one proves a global marked map whose pulled-back metric tensor tends uniformly to the prime metric, the compact-resolvent/essential-spectrum stage is already classical. The unresolved gate is geometric, not operator-theoretic.

## 1. Exact theorem bridge

Georgescu--Golénia work on a noncompact `C^1` manifold `X` with a locally bounded measurable Riemannian structure and a measure satisfying local upper/lower density bounds. They put

\[
H=L^2(X,\mu),
\]

let `d` be the closure of exterior differentiation, and represent a second metric/measure structure by positive bounded coefficient operators `Lambda` on one-forms and `lambda` on functions. Their Theorem 5.3 assumes, in the notation relevant here,

\[
\lambda-1\in B_0(H),
\qquad
\Lambda-1\in B_0(K),
\tag{8}
\]

where `B_0` is the algebra of bounded multiplication coefficients vanishing at infinity. The proof establishes directly that the resolvent difference at `-1` is compact.

Their Proposition 5.4 then specializes the abstract theorem to two Riemannian structures. It assumes that the new cotangent norms obey (1), with

\[
\alpha(x),\beta(x)\to1,
\]

and that the new measure is `mu_+=lambda mu` with `lambda->1`. It concludes equality of essential spectra. The proof is not merely a Weyl-sequence comparison: it verifies Theorem 5.3, whose proof gives the compact resolvent difference in (6).

This distinction matters because the accepted clue asked whether, after constructing a common-manifold identification, one would still need a separate integrability estimate to reach compactness. At the level of this theorem, the answer is no.

## 2. Metric-tensor convergence automatically supplies the theorem coefficients

Suppose the geometric construction sought in the clue achieves a global bilipschitz marking and, after transporting the clone metric,

\[
\|g_+-g\|_g\longrightarrow0
\tag{9}
\]

uniformly outside compact sets. Equivalently, the eigenvalues of the positive endomorphism `g^{-1}g_+` tend uniformly to `1`. Inverting those eigenvalues gives the same conclusion for cotangent norms, so functions `alpha,beta` satisfying (1)--(3) exist.

In dimension two the volume ratio is the square root of the determinant of `g^{-1}g_+`. Therefore (9) also gives

\[
\lambda=\sqrt{\det(g^{-1}g_+)}\longrightarrow1.
\tag{10}
\]

A finite number of head pants is irrelevant to the limit at infinity. Any locally bilipschitz construction on that compact head supplies finite global upper/lower bounds, while the tail estimate supplies (3) and (5). Since `g` is complete and the two metrics are globally uniformly equivalent, `g_+` is complete as well.

Hence the operator bridge reduces to

\[
\boxed{
\text{global marked }K(x)\to1
\Longrightarrow
\text{Georgescu--Golénia hypotheses}
\Longrightarrow
\text{compact relative resolvent}.
}
\tag{11}
\]

No summation over pants occurs in this implication.

## 3. Consequence for the shift-clone program

PF-108, PF-119, and PF-122 contain several `ell^1` geometric defects, while PF-107/PF-114 also expose natural reciprocal-prime quantities that are not in `ell^1`. Before the present audit it was plausible that an operator theorem might require the stronger summable estimates and therefore reintroduce a hidden obstruction.

Proposition 5.4 rules out that issue for compact resolvent. If the remaining PF-121/PF-122 boundary-coherent gluing can produce a global metric comparison with

\[
K_n\to1
\tag{12}
\]

on the escaping pants, then the rate is immaterial for (6)--(7). In particular, a nonsummable coordinate-level defect is not an operator obstruction merely because its sum diverges; only the actual metric coefficients after the global marking matter.

This makes the accepted clue sharper:

\[
\boxed{
\text{bounded-height/cuff-coherent gluing is now the only missing gate}
\quad\text{before essential-spectrum equivalence.}
}
\tag{13}
\]

The statement is conditional because PF-121 proves only one-quadrilateral maps and PF-122 only the canonical deep-cusp strip map. Their lower traces have not yet been reconciled into a complete global homeomorphism.

## 4. What this does not give

Compact resolvent difference is much weaker than the operator ideals and dynamical data that appear elsewhere in the line. In particular, PF-123 does **not** imply:

- the first resolvent difference is trace class; PF-112 gives a generic local obstruction to that stronger property;
- any Schatten class `S_q` for a specified `q`;
- trace-class heat differences or a relative determinant;
- existence/completeness of wave operators;
- equality of scattering matrices or resonance sets;
- equality of discrete eigenvalues below/inside the essential spectrum;
- equality of Selberg/Ruelle-type products;
- any RH or zeta-zero statement.

It also does not say that an arbitrary quasiconformal, length-spectrum, or pantwise Lipschitz equivalence is enough. The hypothesis needed here is the concrete common-manifold coefficient convergence (3)--(5).

## 5. Prior art and novelty audit

The operator theorem is not new. The primary source audited is:

- V. Georgescu and S. Golénia, *Quasilocal Operators and Stability of the Essential Spectrum* (2004 preprint), Theorem 5.3 and Proposition 5.4; the revised published article is *Compact perturbations and stability of the essential spectrum of singular differential operators*, Journal of Operator Theory 59 (2008), 115--155.

The published abstract explicitly lists Laplace--Beltrami operators for measurable Riemannian metrics among the applications. The preprint's Proposition 5.4 states the asymptotically equivalent metric criterion used above, and its proof invokes Theorem 5.3, where compactness of the resolvent difference is proved.

No novelty is claimed for essential-spectrum stability under asymptotically equal elliptic coefficients, local compactness of Sobolev embeddings, or the Banach-module/quasilocal machinery. The Mathia-specific contribution is the **hypothesis audit against the exact accepted prime-flute control**: it shows that the future operator step is already covered if the remaining geometric marking reaches `K(x)->1`, and that no unproved `ell^1`-to-operator leap is needed for compactness.

Directed searches for the prime flute, shifted composite endpoint controls, and this exact geometric specialization found no pre-existing arithmetic statement. That does not make the operator mechanism novel; it is an application boundary for this construction.

## 6. Falsification core

This finding should be withdrawn or corrected if any of the following fails:

1. Georgescu--Golénia Theorem 5.3 does not in fact prove compactness of the resolvent difference under its `B_0` coefficient hypotheses;
2. Proposition 5.4 does not reduce asymptotic equivalence of the two metric norms plus `lambda->1` to those hypotheses;
3. a future prime/clone global marking fails to define a locally bounded uniformly positive transported metric on the same `C^1` manifold;
4. the future marking has only length-spectrum/quasiconformal convergence but not metric coefficient convergence at infinity;
5. one silently replaces the bounded topological `L^2` identification used in the theorem by a stronger unitary/Schatten assertion not proved there.

Items 1--2 were checked directly against the primary preprint. Items 3--4 remain exactly the unresolved geometric part of the accepted clue. Item 5 is a boundary condition protecting the conclusion from being over-read.

## Consequence

At the compact-resolvent level the prime-flute/shift-clone program has become a clean two-stage question:

\[
\boxed{
\text{construct global marked asymptotic metric equivalence}
\quad\Longrightarrow\quad
\text{compact relative resolvent and equal essential spectra}.}
\]

The second arrow is established prior art. Future Research Watch effort should therefore concentrate on the first arrow or on stronger spectral invariants that survive compact perturbation, rather than searching for a new essential-spectrum theorem.