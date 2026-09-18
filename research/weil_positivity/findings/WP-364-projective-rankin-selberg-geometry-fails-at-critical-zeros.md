---
id: WP-364
title: Projectivizing the Eisenstein Rankin--Selberg Gram removes the universal zero but produces unbounded critical overlaps and negative Fubini--Study metric
branch: weil_positivity
status: supported
kind: projective-rankin-selberg-critical-geometry-obstruction
claim_strength: exact projective-Hilbert derivation with unconditional critical-line-zero falsification
created: 2026-09-18
related: [WP-352, WP-361, WP-362, WP-363]
clues: [CLUE-maass-selberg-remainder-sign-interface]
prior_art:
  - B. M. Wilson, Proofs of Some Formulae Enunciated by Ramanujan, Proceedings of the London Mathematical Society (2) 21 (1923), 235-255, DOI 10.1112/plms/s2-21.1.235
  - Dorje C. Brody and Lane P. Hughston, Geometric quantum mechanics, Journal of Geometry and Physics 38 (2001), no. 1, 19-53, DOI 10.1016/S0393-0440(00)00052-8
  - E. C. Titchmarsh, The Theory of the Riemann Zeta-function, 2nd ed. revised by D. R. Heath-Brown, Oxford University Press, 1986
---

# WP-364 — Projectivizing the Eisenstein Rankin--Selberg Gram removes the universal zero but produces unbounded critical overlaps and negative Fubini--Study metric

## Claim

`WP-363` leaves one particularly natural objection open. Its positive Eisenstein coefficient Gram

\[
K_s(r,u)=\left\langle v_r^{(s)},v_u^{(s)}\right\rangle,
\qquad
v_r^{(s)}=(\lambda_r(n)n^{-s/2})_{n\ge1},
\qquad s>1,
\tag{1}
\]

collapses at `s=1/2` because the exact Rankin--Selberg factorization contains the scalar factor `1/zeta(2s)`. One can reasonably object that this scalar norm should be irrelevant to the **intrinsic projective geometry** of the Hecke coefficient vectors. Passing from `v_r^(s)` to its ray `[v_r^(s)]` is canonical, preserves a genuine positive geometric theorem for `s>1`, and exactly quotients out every nonzero scalar normalization of the feature vector.

That stronger escape also fails, and it fails without making an arbitrary regularization choice.

For `s>1`, define the normalized projective overlap

\[
C_s(r,u)
:=
\frac{K_s(r,u)}{\sqrt{K_s(r,r)K_s(u,u)}}.
\tag{2}
\]

Because `K_s` is a Hilbert Gram, `C_s` is positive semidefinite, `C_s(r,r)=1`, and Cauchy--Schwarz gives `|C_s(r,u)|<=1`. With

\[
A_s(t):=\zeta(s+it)\zeta(s-it)=|\zeta(s+it)|^2
\qquad(s,t\in\mathbb R,\ s>1),
\tag{3}
\]

`WP-363`'s Ramanujan--Wilson identity becomes

\[
K_s(r,u)=\frac{A_s(r+u)A_s(r-u)}{\zeta(2s)}.
\tag{4}
\]

The universal `1/zeta(2s)` factor cancels **identically** in (2):

\[
\boxed{
C_s(r,u)=
\frac{A_s(r+u)A_s(r-u)}
{A_s(0)\sqrt{A_s(2r)A_s(2u)}}.
}
\tag{5}
\]

Thus projectivization really does bypass the zero of the whole Gram found in `WP-363`; this is not multiplication by a hand-picked counterterm.

However, the canonical continuation of (5) to the critical exponent is already incompatible with projective Hilbert geometry. Put

\[
F(t):=\left|\zeta\!\left(\frac12+it\right)\right|^2.
\tag{6}
\]

Away from zeros in the denominator, (5) continues to

\[
\boxed{
C_{\!*}(r,u)=
\frac{F(r+u)F(r-u)}
{F(0)\sqrt{F(2r)F(2u)}}.
}
\tag{7}
\]

Let `gamma!=0` be the ordinate of any zero on the critical line; Hardy's theorem supplies infinitely many such `gamma`. Choose a real `u` such that

\[
F(\gamma/2+u)F(\gamma/2-u)F(2u)>0,
\tag{8}
\]

which is possible because the critical-line zero ordinates are discrete. As `r -> gamma/2` through values with `F(2r)>0`, the numerator of (7) tends to the positive number in (8), whereas `F(2r)->0`. Hence

\[
\boxed{|C_{\!*}(r,u)|\longrightarrow\infty.}
\tag{9}
\]

In particular, on ordinary regular points arbitrarily close to `gamma/2`, one has `|C_*(r,u)|>1`. No positive-semidefinite normalized Gram can do this. Therefore the source-defined projective overlap has **no critical continuation preserving its Hilbert-space positivity**.

The infinitesimal projective geometry fails with the same sign. The pullback of the Fubini--Study metric along the ray curve `r -> [v_r^(s)]` is

\[
\begin{aligned}
g_s(r)
&=
\frac{\|\partial_r v_r^{(s)}\|^2}{\|v_r^{(s)}\|^2}
-
\frac{|\langle \partial_r v_r^{(s)},v_r^{(s)}\rangle|^2}{\|v_r^{(s)}\|^4}\\
&=
\left.\partial_r\partial_u\log K_s(r,u)\right|_{u=r}
\ge0.
\end{aligned}
\tag{10}
\]

Writing `L_s(t)=log A_s(t)`, equations (4) and (10) give the exact scalar-free formula

\[
\boxed{g_s(r)=L_s''(2r)-L_s''(0),\qquad s>1.}
\tag{11}
\]

The factor `1/zeta(2s)` again disappears automatically because it is independent of `r,u`. At `s=1/2`, away from critical-line zeros, the corresponding continuation is

\[
\boxed{
g_{\!*}(r)
=
(\log F)''(2r)-(\log F)''(0).
}
\tag{12}
\]

If `gamma` is a critical-line zero of multiplicity `m>=1`, then locally

\[
F(t)=|t-\gamma|^{2m}H(t),
\qquad H(\gamma)>0,
\tag{13}
\]

with `H` smooth and positive near `gamma`. Therefore

\[
(\log F)''(t)
=-\frac{2m}{(t-\gamma)^2}+O(1),
\tag{14}
\]

and, since `F(0)!=0`,

\[
\boxed{
g_{\!*}(r)\longrightarrow-\infty
\quad\text{as}\quad
r\to\gamma/2,
\ r\ne\gamma/2.}
\tag{15}
\]

So the analytically continued Fubini--Study pullback is negative on punctured neighborhoods of every known critical-line zero. The sign loss is not confined to the singular point itself.

This closes the canonical **projectivize before continuing** repair of `WP-363`. The universal Rankin--Selberg zero can indeed be removed geometrically rather than by an arbitrary scalar renormalization, but the resulting projective overlap violates Cauchy--Schwarz and its intrinsic metric becomes negative at the Weil exponent. Scalar archimedean completions cannot repair this because projective geometry is exactly invariant under `v_r -> a_s(r)v_r` for every nonzero scalar factor `a_s(r)`.

**Classification:** `CLASSICAL-RAMANUJAN-WILSON + CLASSICAL-FUBINI-STUDY + EXACT-DERIVED + SOURCE-DEFINED-PROJECTIVIZATION + UNIVERSAL-GRAM-ZERO-REMOVED + CRITICAL-OVERLAP-UNBOUNDED + CRITICAL-METRIC-NEGATIVE + HARDY-ZERO-CONTROL + SCALAR-COMPLETION-INVARIANT + DECISIVE-NARROWING + NO-NOVELTY-CLAIM-FOR-CLASSICAL-INGREDIENTS`.

## 1. Projectivization is a genuine positive construction before continuation

For `s>1`, the coefficient vectors `v_r^(s)` lie in `l^2(N)`. Their derivatives in `r` also lie in `l^2`: differentiating the divisor phases contributes at most logarithmic factors, while the standard divisor-function bounds leave the resulting squared Dirichlet series absolutely convergent for every `s>1`. Thus the ray curve

\[
r\longmapsto[v_r^{(s)}]\in\mathbb P(\ell^2)
\tag{16}
\]

has ordinary projective Hilbert geometry in the entire source domain where (1) is a Gram.

Two independent positivity statements follow. First, normalized overlaps satisfy

\[
|C_s(r,u)|\le1.
\tag{17}
\]

Second, the Fubini--Study pullback (10) is a squared norm of the component of `partial_r v_r` orthogonal to the ray `v_r`, hence is nonnegative. Neither statement knows anything about zeta zeros or RH.

This is a stronger normalization test than simply multiplying `K_s` by `zeta(2s)`. Projective space is the canonical quotient of nonzero Hilbert vectors by scalar multiplication. If the `1/zeta(2s)` collapse of `WP-363` were merely an irrelevant choice of vector norm, the ray geometry would be the natural place for the independent positivity to survive.

Equation (5) confirms the intended effect exactly: the problematic scalar disappears without being chosen or subtracted by hand.

## 2. The critical projective overlap violates its own Cauchy--Schwarz bound

For a normalized positive-semidefinite kernel with unit diagonal, every `2 x 2` principal minor gives

\[
1-|C(r,u)|^2\ge0.
\tag{18}
\]

Thus `|C(r,u)|<=1` is not a weak diagnostic; it is a necessary local consequence of the same Hilbert positivity that created the candidate.

At `s=1/2`, equation (7) is the unique pointwise continuation furnished by the exact Rankin--Selberg formula wherever its denominator is nonzero. Fix a critical-line zero ordinate `gamma`. The exceptional set of `u` for which one of the three factors in (8) vanishes is discrete, so generic real `u` satisfies (8). Then (9) proves a much stronger failure than a slightly negative principal minor: the continued normalized overlap is **unbounded** near the zero ray.

This argument does not assume that the zero is simple. It uses only the unconditional existence of a critical-line zero and the discreteness of the zeta divisor. It also does not insert a zero into the construction: the zero is used adversarially to test a kernel already forced by the Hecke coefficient geometry.

The same argument rules out declaring the singular ray absent while keeping the neighboring continuation. Every punctured neighborhood contains regular `r` with `|C_*(r,u)|>1`. Removing only the exact zero therefore does not restore positivity. Removing an entire data-dependent neighborhood around each zero would use the target divisor to define the geometric domain and would not be an intrinsic Weil-positivity theorem.

## 3. The Fubini--Study metric gives the infinitesimal sign obstruction

Equation (10) is the standard Fubini--Study formula for a differentiable ray curve in projective Hilbert space. It is invariant under any nonzero scalar gauge

\[
v_r^{(s)}\longmapsto a_s(r)v_r^{(s)}.
\tag{19}
\]

For a Gram kernel this invariance is visible algebraically because the mixed derivative `partial_r partial_u log K_s(r,u)` kills every separated factor `a_s(r)\overline{a_s(u)}`.

Using (4), set `x=r+u` and `y=r-u`. Since

\[
\partial_r\partial_u
=\partial_x^2-\partial_y^2,
\tag{20}
\]

one obtains (11) on the diagonal `u=r`. This identity itself provides an exact check on the sign: for every `s>1`, Hilbert geometry proves

\[
L_s''(2r)\ge L_s''(0).
\tag{21}
\]

The critical continuation reverses this near every critical-line zero. Factorization (13) gives (14), while the subtraction term `(log F)''(0)` is finite because `zeta(1/2)!=0`. Hence (15) follows.

A smooth change of spectral coordinate cannot fix the sign: under a local reparameterization `r=phi(q)`, a one-dimensional Riemannian metric transforms by multiplication with `(phi'(q))^2`. Thus negative `g_*` remains negative at every regular point where the coordinate change is nondegenerate.

The divergence in (15) is also the infinitesimal form of (9). The normalized projective kernel is trying to pass through a point where the continued vector norm has collapsed while generic cross-correlations remain nonzero; projective distance and local metric therefore cease to have Hilbert sign.

## 4. Matched controls and attempted repairs

**Multiply the coefficient vectors by Gamma or completed-zeta factors.** Any completion of the form

\[
\widetilde v_r^{(s)}=a_s(r)v_r^{(s)},
\qquad a_s(r)\ne0,
\tag{22}
\]

leaves `[v_r^(s)]`, `C_s` up to an irrelevant phase gauge, and the Fubini--Study metric exactly unchanged. In particular, a scalar archimedean Gamma completion cannot supply the missing sign or counterterm in this projective route. An archimedean sector that changes the answer must be genuinely nonseparable/non-scalar in the feature geometry.

**Cancel `1/zeta(2s)` first and then projectivize.** The order does not matter: any common positive scalar in `K_s` cancels from (2), and its logarithm is annihilated by the mixed derivative in (10). Thus the obstruction is not an artifact of whether normalization happens before or after analytic continuation in the absolutely convergent region.

**Delete the zero rays.** Equations (9) and (15) are failures on regular points arbitrarily close to the deleted rays. The sign is not restored by puncturing the divisor.

**Take an absolute value of the continued overlap or metric.** This creates a new nonlinear object and destroys the projective-Hilbert derivation. It is not a continuation of the source positivity theorem, and it has no reason to preserve the linear Weil readout.

**Add a new orthogonal archimedean feature sector.** This can in principle change the projective metric and overlap matrix because it is not a scalar gauge. But it is exactly the structure the branch has not yet derived: the new sector must be source-forced, must produce the finite-prime and Gamma/polar terms in one local-to-global theorem, and must prove its sign independently. The present result does not rule out such a genuinely enlarged automorphic/cohomological construction.

## 5. Relation to the existing negative frontier

This is not the scalar-blindness result of `WP-352`. There the proposed projective/Berry geometry was built from an operator family `U=gR`; projectors were exactly blind to the common scalar scattering factor `g`, so they could not recover its phase. Here the projective object is instead the **non-scalar family of Hecke coefficient rays** `r -> [v_r^(s)]`. It contains real arithmetic variation and has a nontrivial Fubini--Study metric for `s>1`. The failure occurs only when that genuine geometry is continued to the critical half-density.

It is also stronger than the bare scalar-renormalization check in `WP-363`. That finding shows that cancelling the source-forced `1/zeta(2s)` zero produces the indefinite kernel `J(r,u)=F(r+u)F(r-u)`. The present construction asks whether the scalar factor can be discarded for an **intrinsic geometric reason** before continuation. Projectivization does exactly that, but normalized overlaps then blow up and the Fubini--Study metric becomes negative. Thus the apparently innocent geometric quotient does not preserve the positivity either.

The resulting narrowing is precise. The surviving Maaß--Selberg/Hecke route cannot rely on a positive coefficient Gram plus scalar/projective normalization, even when the normalization is forced by Hilbert geometry itself. It needs a new operator or cohomological coupling that changes cross-parameter correlations before the critical specialization.

## 6. Prior-art and novelty audit

The ingredients are classical. The generalized divisor-product identity behind (4) is the Ramanujan--Wilson identity already audited in `WP-363`. Projective Hilbert space and its Fubini--Study metric are standard; Brody and Hughston give a modern geometric-quantum-mechanics account of the unitary-invariant projective metric and its Hilbert-space interpretation. Hardy's theorem on infinitely many zeta zeros on the critical line is classical; Titchmarsh is the standard reference used by `WP-363`.

A targeted literature search for combinations of `Fubini--Study`, `projective metric`, Eisenstein/Hecke coefficient families, Rankin--Selberg kernels, and zeta did not surface a source asserting that this normalized Ramanujan--Wilson kernel gives a positive critical metric. The search did surface the standard projective-Hilbert geometry but no theorem changing the elementary obstruction (9) or (15). This is not a historical novelty proof, and no novelty is claimed for the ingredients.

The Mathia-specific contribution is the **candidate audit**: take the exact non-scalar positive Hecke Gram from `WP-363`, apply the canonical scalar quotient that most directly addresses its universal critical zero, and test the inherited positivity rather than assuming projectivization preserves it through analytic continuation. The result is an exact no-go at the target exponent.

## Representation audit

The source-first object is the Eisenstein Hecke coefficient vector `v_r^(s)` and its Hilbert ray, not a statistic designed from the zeta zeros. Positivity for `s>1` comes independently from ordinary Hilbert/projective geometry. The arithmetic bridge is the exact Ramanujan--Wilson factorization forced by the Hecke coefficients. The target specialization `s=1/2` is the same critical half-density selected by the Weil finite-prime weights.

Critical-line zeros enter only after the candidate has been fully defined, as an adversarial falsification of the continued positivity. No zero-defined spectrum, hand-picked kernel, RH assumption, or sign-forcing regularization is used. Scalar Gamma/completion factors are tested as matched controls and are proved invisible to the projective metric rather than being omitted by convenience.

What remains outside the obstruction is precisely a category change relevant to the README: a source-forced finite--archimedean feature space, boundary response, intersection/cohomological form, or noncentral operator coupling whose positivity exists before scalarization and whose critical specialization does not pass through the projective Rankin--Selberg geometry above.

## Verdict

**Supported exact negative.** The most canonical geometric way to remove `WP-363`'s universal Rankin--Selberg zero is to pass to projective Hilbert space. It succeeds algebraically—the `1/zeta(2s)` factor cancels exactly—but fails geometrically at the target. The continued normalized overlap becomes unbounded near every unconditional critical-line zero, violating the projective Cauchy--Schwarz bound, and the continued Fubini--Study metric tends to `-infinity` on the same regular punctured neighborhoods.

Therefore the bare Eisenstein coefficient family cannot yield a global Weil-type positivity theorem by scalar completion, norm normalization, or intrinsic projectivization. Any surviving construction must change the non-scalar finite--archimedean geometry before the critical specialization rather than merely quotienting its scalar normalization.
