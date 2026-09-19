---
id: WP-367
title: Common dilation-homogeneous radial positive forms still separate Whittaker incidence into Rankin--Selberg data
branch: weil_positivity
status: supported
kind: whittaker-radial-positive-form-homogeneity-obstruction
claim_strength: exact finite-cutoff factorization with critical null-or-divergent dichotomy
created: 2026-09-19
related: [WP-116, WP-359, WP-363, WP-365, WP-366]
clues: [CLUE-maass-selberg-remainder-sign-interface]
prior_art:
  - Classical Mellin diagonalization of dilations on the multiplicative group of positive reals
  - Classical Rankin--Selberg theory for Eisenstein/Hecke coefficient correlations
  - Audrey Terras, The Chowla-Selberg Method for Fourier Expansion of Higher Rank Eisenstein Series, Canadian Mathematical Bulletin 28 (1985), 280--294, doi:10.4153/CMB-1985-034-1
---

# WP-367 — Common dilation-homogeneous radial positive forms still separate Whittaker incidence into Rankin--Selberg data

## Claim

`WP-366` showed that integrating the fixed-height Whittaker--Hecke Gram against a positive dilation-covariant scalar measure forces Mellin separation. Replacing that scalar measure by a much larger class of radial positive geometries does not rescue the route.

Let

\[
F_r(Y)=K_{ir}(2\pi Y),\qquad (D_a f)(Y)=f(aY),
\tag{1}
\]

and let `b` be a positive-semidefinite sesquilinear form on radial height profiles whose domain contains the dilates under consideration. Suppose the same radial form is applied componentwise to every Fourier/Whittaker coordinate and is exactly homogeneous under dilation:

\[
\mathfrak b(D_a f,D_a g)=a^{-\delta}\mathfrak b(f,g)
\qquad(a>0).
\tag{2}
\]

Then at every finite Fourier cutoff `X`, the resulting finite--archimedean form factors exactly as

\[
\boxed{
\mathcal E_{\delta,X}(r,u)
=
\mathfrak b(F_r,F_u)
\sum_{n\le X}\overline{\lambda_r(n)}\lambda_u(n)n^{-\delta}.
}
\tag{3}
\]

Thus even an arbitrary nonlocal, differential, integral-kernel, or Sobolev-type **common positive radial form** cannot preserve the nonseparable `nY` incidence once exact dilation homogeneity is imposed: it becomes an archimedean radial scalar times a finite Rankin--Selberg Dirichlet kernel.

At the critical half-density `delta=1/2`, positivity gives a sharp dichotomy on the diagonal. If `b(F_r,F_r)>0`, then the finite-cutoff diagonals grow without bound. If `b(F_r,F_r)=0`, then `F_r` is a null vector for `b` and its entire row and column vanish. Hence no nontrivial finite critical positive form exists in this class.

**Classification:** `EXACT-DERIVED + COMMON-RADIAL-POSITIVE-FORM + DILATION-HOMOGENEITY + FINITE-CUTOFF-FACTORIZATION + RANKIN-SELBERG-REDUCTION + CRITICAL-NULL-OR-DIVERGENT-DICHOTOMY + MATCHED-CONTROL + ROUTE-CLOSURE + CLASSICAL-INGREDIENTS + NO-GRAND-NOVELTY-CLAIM`.

## 1. Exact finite-cutoff factorization

The Whittaker coordinate of Fourier index `n` is

\[
\lambda_r(n)F_r(nY)=\lambda_r(n)(D_nF_r)(Y).
\tag{4}
\]

For a cutoff `X`, lift the same radial form componentwise:

\[
\mathcal E_{\delta,X}(r,u)
=
\sum_{n\le X}
\overline{\lambda_r(n)}\lambda_u(n)
\mathfrak b(D_nF_r,D_nF_u).
\tag{5}
\]

Equation (2) immediately gives

\[
\mathfrak b(D_nF_r,D_nF_u)
=n^{-\delta}\mathfrak b(F_r,F_u),
\tag{6}
\]

so substituting (6) into (5) proves (3).

This argument is deliberately made at finite `X`. No interchange of infinite sums, no analytic continuation, no regularization, and no convergence hypothesis are needed. The separation is an algebraic consequence of applying one common dilation-homogeneous radial geometry to the source-defined Whittaker incidence.

The class is substantially broader than the scalar measures of `WP-366`. Whenever they are defined on the relevant profiles, positive integral-kernel forms, positive differential energies, Mellin-Sobolev forms, and other nonlocal radial sesquilinear geometries are included. Their internal complexity affects only the scalar factor `b(F_r,F_u)`; exact dilation homogeneity removes the Fourier index from that factor as `n^{-delta}`.

## 2. Critical positivity gives a null-or-divergent dichotomy

Set `u=r` and `delta=1/2`. Then

\[
\mathcal E_{1/2,X}(r,r)
=
\mathfrak b(F_r,F_r)
\sum_{n\le X}|\lambda_r(n)|^2n^{-1/2}.
\tag{7}
\]

Every term is nonnegative. The canonical Rankin--Selberg diagonal used in `WP-363`, `WP-365`, and `WP-366` has

\[
\sum_{n\ge1}\frac{|\lambda_r(n)|^2}{n}=+\infty.
\tag{8}
\]

Since `n^{-1/2} >= n^{-1}` for every `n>=1`, its critical half-density majorant also diverges:

\[
\sum_{n\ge1}|\lambda_r(n)|^2n^{-1/2}=+\infty.
\tag{9}
\]

Therefore, if

\[
\mathfrak b(F_r,F_r)>0,
\tag{10}
\]

then

\[
\lim_{X\to\infty}\mathcal E_{1/2,X}(r,r)=+\infty.
\tag{11}
\]

The only way a positive-semidefinite `b` can avoid this diagonal divergence for that spectral profile is

\[
\mathfrak b(F_r,F_r)=0.
\tag{12}
\]

But Cauchy--Schwarz for a positive-semidefinite sesquilinear form gives

\[
|\mathfrak b(F_r,g)|^2
\le
\mathfrak b(F_r,F_r)\mathfrak b(g,g)=0,
\tag{13}
\]

so `b(F_r,g)=0` for every `g` in the domain. The profile is then a null vector, not a finite nonzero critical state.

Hence the class has the exact dichotomy

\[
\boxed{
\text{nonzero radial norm}\Rightarrow\text{critical diagonal diverges},
\qquad
\text{finite critical diagonal}\Rightarrow\text{radial profile is null}.
}
\tag{14}
\]

The obstruction occurs before any question about zeta zeros and uses no RH input.

## 3. Matched controls identify the actual culprit

Positivity by itself does **not** cause the separation. For any fixed `Y_0>0`, point evaluation

\[
\mathfrak b_{Y_0}(f,g)=\overline{f(Y_0)}g(Y_0)
\tag{15}
\]

is positive semidefinite, but it is not dilation-homogeneous in the sense of (2). Its lifted Whittaker kernel retains the genuine nonseparable incidence

\[
K_{ir}(2\pi nY_0)K_{iu}(2\pi nY_0),
\tag{16}
\]

exactly as in the fixed-height control of `WP-366`. Therefore the loss of finite--archimedean coupling comes from **scale globalization through exact homogeneity**, not from positivity alone.

The theorem also does not prohibit assigning an arbitrary separate form `b_n` to every Fourier index. Such a choice can encode essentially arbitrary arithmetic weights and is therefore not an intrinsic source-free construction unless Mathia supplies a geometric mechanism that forces the entire family. Likewise, forms with cross-index terms `n != m`, a source-fixed absolute scale, nonhomogeneous radial geometry, nonlinear constructions, or an indefinite/intersection/cohomological sign theorem lie outside the claim.

In particular, horizontal translation invariance may diagonalize Fourier modes, but it does not by itself force the same radial form on every mode. The conclusion here is intentionally narrower: **once a common componentwise radial form is chosen and exact height-dilation homogeneity is required, Rankin--Selberg separation is unavoidable.**

## 4. Relation to the existing Mathia obstruction pattern

`WP-116` found an analogous mechanism on the Prime-Torus side: positivity plus exact power-map covariance forced homogeneous spectral multipliers, and the critical homogeneous weighting then diverged. The present result is not the same theorem in different notation. Its source object is the Eisenstein Whittaker incidence `lambda_r(n)K_{ir}(2 pi nY)`, its symmetry is height dilation, and its forced output is the Rankin--Selberg partial Dirichlet kernel in (3).

The structural recurrence is nevertheless useful. In both cases an exact scale symmetry converts a potentially richer positive geometry into a homogeneous multiplier law before critical specialization. `WP-359` supplies a complementary boundary warning: straightforward Fourier-diagonal positive squares naturally produce the wrong prime scale (`1/p` rather than the desired half-density). Here even allowing a much richer common radial geometry cannot alter the homogeneous exponent independently of the scale law.

This materially narrows the open Maaß--Selberg clue. A surviving construction cannot merely replace the scalar height measure of `WP-366` by a more sophisticated positive radial norm while keeping componentwise commonality and exact dilation homogeneity. It must obtain its sign from geometry that couples Fourier indices or scale sectors more essentially, introduces a source-forced nonhomogeneous/global counterterm, or uses a different sign theorem altogether.

## 5. Prior-art and novelty audit

The ingredients are classical. Dilation homogeneity on `R_{>0}` is naturally diagonalized by Mellin analysis, and Rankin--Selberg theory classically organizes Hecke-coefficient correlations through Dirichlet series. Terras's Chowla--Selberg treatment is representative background for the Eisenstein/Whittaker side. The diagonal Rankin--Selberg pole used in (8) is the same established input already audited in `WP-363`--`WP-366`.

A targeted search for homogeneous positive sesquilinear forms under dilation, Mellin diagonalization, Whittaker/K-Bessel pairings, and Rankin--Selberg positivity did not locate a source asserting this exact Mathia-specific route closure. That search is not a historical novelty proof. No novelty is claimed for Mellin analysis, homogeneous forms, K-Bessel/Whittaker expansions, Rankin--Selberg identities, or the diagonal pole.

The substantive result is the exact finite-cutoff classification (3) and the critical dichotomy (14) for the **specific source-defined Whittaker `nY` construction** left open after `WP-366`. It shows that promoting scalar scale averaging to a general common positive radial operator/form does not create the missing noncentral finite--archimedean sign mechanism.

## Representation audit

The construction starts from the actual Eisenstein Whittaker coordinate and an independently positive radial form. Neither zeta zeros nor a target Weil kernel define the geometry. The dilation law is imposed before testing the arithmetic sign, and the Rankin--Selberg kernel is derived from that law at finite cutoff rather than inserted by hand.

The critical failure is also independent of zero data: either the radial norm is positive and a nonnegative coefficient sum diverges, or positivity makes the spectral profile null. Analytic continuation or subtraction of the divergence would therefore be an additional operation not justified by the positive form itself and is not counted as a rescue.

## Verdict

**Supported exact negative.** `WP-366` cannot be escaped merely by replacing its scalar power-Haar height measure with an arbitrary common positive dilation-homogeneous radial form. Exact homogeneity already factors every finite cutoff into an archimedean scalar and a Rankin--Selberg Dirichlet kernel, while the critical half-density is either divergent or geometrically null.

Do not spend further search budget on componentwise common positive radial norms/operators with exact dilation homogeneity. The remaining frontier is genuinely noncentral: cross-Fourier coupling, source-forced nonhomogeneous scale interaction, additional global degrees of freedom/counterterms, or an independent indefinite/intersection/cohomological sign theorem.