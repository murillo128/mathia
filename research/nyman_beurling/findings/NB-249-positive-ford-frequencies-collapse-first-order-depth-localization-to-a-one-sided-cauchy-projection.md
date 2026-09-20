# NB-249 — Positive Ford frequencies collapse first-order depth localization to a one-sided Cauchy projection

**Date:** 2026-09-20  
**Status:** `EXACT-DERIVED + HARDY/CAUCHY-PROJECTION + ONE-SIDED-DEPTH-LOCALIZATION + NB-236/NB-237/NB-248-REFINEMENT + OPERATION-ORDER-CORRECTION + SOURCE-ONLY + PRIOR-ART-AUDITED`.

`NB-248` shows that the first-order Ford representation of `NB-237` cannot be squared as a planar `L^2` field before the divisor pairing: every visible zero produces a Cauchy pole at the critical two-dimensional `L^2` endpoint. That leaves a natural question about the permitted order of operations. Is there a canonical one-copy operation that can be performed **before** squaring, preserves the exact residue current, and removes the pole singularity without inserting an artificial exclusion radius?

For the actual smooth Mellin shell, there is. After resolving the shell transform into its positive Fourier frequencies, the Ford-scaled Cauchy kernel is an exact Hardy projection. Every shell frequency has positive sign, so it sees only the cumulative part of the depth edge lying at smaller Ford depth than the zero. The exponential produced by that Cauchy projection cancels the depth factors in the edge kernel **exactly**, leaving the original zero coefficient

\[
\frac{e^{-r-d_\rho}}{J}\,\chi(d_\rho)
 e^{iYJ\tau_\rho}
 F(\tau_\rho+i\eta_\rho).
\]

For a zero in the plateau `chi=1`, this means that the positive-frequency carrier reconstructs the zero entirely from the shallower transition edge; the deeper transition edge is spectrally invisible to that pole. More generally the edge enters only through the cumulative identity

\[
\int_{-\infty}^{d_\rho}\chi'(d)\,dd=\chi(d_\rho).
\]

This does **not** prove Ford decay. It does something more representation-specific: it identifies the exact operation that must precede any Hilbert-space or second-moment step. The planar pole must first be Hardy-projected at the shell frequency; only then may the resulting finite marked zero current be squared. The dangerous matched packets of `NB-231` survive this projection unchanged, so the remaining theorem is still the hard-window marked pair-energy estimate of `NB-243`/`NB-247`.

## 1. Start from the exact first-order Ford edge current

Use the notation stabilized in `NB-237`--`NB-248`:

\[
Q:=\log(10+|t|),
\qquad
R:=Q^{2/3}(\log Q)^{1/3},
\qquad
Y:=\frac XR\asymp1,
\qquad
J:=\frac RH\to\infty.
\tag{1}
\]

Let

\[
F(z)=\int_a^b\phi(u)e^{izu}\,du,
\qquad
0<a<b<1,
\qquad
\phi\in C_c^\infty((0,1)),
\tag{2}
\]

and retain the Ford coordinates

\[
d=X(1-\Re s)-\log J,
\qquad
\tau=H(\Im s-t),
\tag{3}
\]

with

\[
\eta_{d,J}:=\frac{\log J+d+r}{YJ}.
\tag{4}
\]

`NB-237` gives the exact divisor identity

\[
\sum_\rho m(\rho)\Psi(\rho)
=
\frac{e^{-r}}{2\pi R}
\int_{\mathbb R^2}
\frac{\zeta'}{\zeta}(s(d,\tau))
 e^{-d}\chi'(d)
 e^{iYJ\tau}
 F(\tau+i\eta_{d,J})
\,dd\,d\tau.
\tag{5}
\]

For a nontrivial zero `rho=beta+i gamma`, define

\[
d_\rho:=X(1-\beta)-\log J,
\qquad
\tau_\rho:=H(\gamma-t),
\qquad
\eta_\rho:=\frac{\log J+d_\rho+r}{YJ}.
\tag{6}
\]

Near that zero,

\[
\frac1R\frac{m(\rho)}{s(d,\tau)-\rho}
=
\frac{m(\rho)}{-(d-d_\rho)/Y+iJ(\tau-\tau_\rho)}.
\tag{7}
\]

The model-pole action associated with (5) is therefore

\[
\begin{aligned}
\mathcal P_{\rho,J}
:=\frac{e^{-r}m(\rho)}{2\pi}
\int_{\mathbb R^2}
&\frac{e^{-d}\chi'(d)e^{iYJ\tau}}
{-(d-d_\rho)/Y+iJ(\tau-\tau_\rho)}\\
&\times F(\tau+i\eta_{d,J})
\,dd\,d\tau.
\end{aligned}
\tag{8}
\]

Equation (8) should be read as the action of the Cauchy kernel as a tempered distribution. It is not an invitation to take the planar square from `NB-248`.

## 2. Every shell frequency has positive Hardy sign

Insert (2) into (8):

\[
F(\tau+i\eta_{d,J})
=
\int_a^b
\phi(u)e^{i\tau u}e^{-\eta_{d,J}u}\,du.
\tag{9}
\]

Now set

\[
y:=J(\tau-\tau_\rho).
\tag{10}
\]

For a fixed shell frequency `u`, the oscillatory factor in `y` is

\[
e^{i\lambda_{u,J}y},
\qquad
\lambda_{u,J}:=Y+\frac uJ.
\tag{11}
\]

Because `Y` is bounded below by a positive constant and `u in [a,b] subset (0,1)`, one has

\[
\boxed{
\lambda_{u,J}>0
}
\tag{12}
\]

uniformly throughout the Ford regime.

The elementary Cauchy/Hardy projection identity is, for `lambda>0` and `x ne 0`,

\[
\boxed{
\int_{\mathbb R}
\frac{e^{i\lambda y}}{-x+iy}\,dy
=
2\pi e^{\lambda x}\mathbf 1_{\{x<0\}}.
}
\tag{13}
\]

With the opposite sign of frequency, the complementary half-line is selected. Formula (13) is just the Fourier-support form of the Cauchy projection: for positive frequency one closes the contour in the upper half-plane, and the pole `y=-ix` is enclosed precisely when `x<0`.

At `x=0`, (13) is interpreted distributionally; the value on that measure-zero slice is irrelevant for the depth integral. A fully regularized derivation is obtained by multiplying the `y` integral by `e^{-epsilon y^2}`, evaluating, and passing to `epsilon downarrow0` in tempered distributions. Thus no absolute Fubini claim across the pole is being made.

Apply (13) with

\[
x=\frac{d-d_\rho}{Y},
\qquad
\lambda=Y+\frac uJ.
\tag{14}
\]

The positive shell frequency then gives

\[
\int_{\mathbb R}
\frac{e^{i(Y+u/J)y}}
{-(d-d_\rho)/Y+iy}\,dy
=
2\pi
\exp\!\left[
\left(Y+\frac uJ\right)\frac{d-d_\rho}{Y}
\right]
\mathbf 1_{\{d<d_\rho\}}.
\tag{15}
\]

This is the exact one-sidedness. The analytic shell does not sample both depth directions symmetrically.

## 3. The Ford exponents cancel exactly

After the change of variables (10), the remaining factors depending on `d` are

\[
e^{-d}
\exp\!\left[-\frac{u(\log J+d+r)}{YJ}\right]
\exp\!\left[
\left(Y+\frac uJ\right)
\frac{d-d_\rho}{Y}
\right].
\tag{16}
\]

The dependence on the integration variable `d` cancels identically:

\[
\boxed{
(16)
=
e^{-d_\rho}
\exp\!\left[-\frac{u(\log J+d_\rho+r)}{YJ}\right].
}
\tag{17}
\]

Nothing asymptotic has been used here. In particular, there is no Taylor expansion in `1/J` and no replacement of `F(\tau+i\eta_{d,J})` by `F(\tau)`.

The depth integral left by (15) is simply

\[
\int_{-\infty}^{d_\rho}\chi'(d)\,dd
=
\chi(d_\rho),
\tag{18}
\]

because `chi` is compactly supported. Restoring the factor `d\tau=dy/J` and the phase at the zero gives

\[
\begin{aligned}
\mathcal P_{\rho,J}
&=
\frac{e^{-r-d_\rho}}J
m(\rho)\chi(d_\rho)
 e^{iYJ\tau_\rho}
\\
&\qquad\times
\int_a^b
\phi(u)
 e^{iu\tau_\rho}
 e^{-u(\log J+d_\rho+r)/(YJ)}
\,du.
\end{aligned}
\tag{19}
\]

The last integral is exactly `F(\tau_\rho+i\eta_\rho)`. Hence

\[
\boxed{
\mathcal P_{\rho,J}
=
\frac{e^{-r-d_\rho}}J
m(\rho)\chi(d_\rho)
 e^{iYJ\tau_\rho}
 F(\tau_\rho+i\eta_\rho).
}
\tag{20}
\]

Since

\[
YJ\tau_\rho=X(\gamma-t),
\tag{21}
\]

(20) is precisely the zero coefficient in the smooth Ford current of `NB-243` and `NB-247`.

Thus the first-order edge representation contains an exact factorization:

\[
\boxed{
\text{Cauchy pole}
\xrightarrow{\text{positive-frequency Hardy projection}}
\text{cumulative shallow edge}
\xrightarrow{\int\chi'}
\text{finite Ford zero mark}.
}
\tag{22}
\]

For a zero in the plateau where `chi(d_rho)=1`, all of (18) is accumulated before the deeper transition begins. Such a zero is reconstructed entirely from the shallower edge. If the zero itself lies in a transition region, (18) remains exact but should be interpreted as the cumulative edge up to `d_rho`, not as a claim that one fixed geometric edge alone contributes.

## 4. This identifies the legal order around the `NB-248` endpoint

The local obstruction in `NB-248` came from squaring

\[
\frac1{-x+iy}
\]

in the two-dimensional `(x,y)` plane. Its square has the logarithmic divergence

\[
\int_{x^2+y^2<1}\frac{dx\,dy}{x^2+y^2}=+\infty.
\tag{23}
\]

Equation (13) shows why that operation is too early for the actual shell. The observable never asks for the full planar `L^2` mass of the pole. It first applies a one-sided Fourier projection in the scaled ordinate variable, at frequencies

\[
\lambda_{u,J}=Y+O(J^{-1}),
\tag{24}
\]

and only then uses the resulting finite residue coefficient.

This also resolves a superficial scale paradox. In the original `tau` coordinate the carrier frequency is `YJ`, which diverges. In the pole coordinate

\[
y=J(\tau-\tau_\rho),
\]

the same carrier is the fixed frequency `Y`, with only the shell-width perturbation `u/J`. The matched packet from `NB-231` has fixed spacing in this `y` coordinate, so the high-frequency carrier has not created generic oscillatory decay; it has merely become the natural fixed-frequency Hardy probe of the local pole geometry.

The correct operation order is therefore

\[
\boxed{
\text{project the signed Cauchy current}
\;\longrightarrow\;
\text{form the finite marked zero current}
\;\longrightarrow\;
\text{square/bilinearize}.
}
\tag{25}
\]

Reversing the first two analytic operations gives the pole-critical divergence of `NB-248`. Applying them in the order (25) reproduces the finite pair-energy object of `NB-243` with no exclusion radius and no renormalized self-energy.

## 5. The two-edge potential picture is equivalent but not a two-edge decorrelation requirement

`NB-236` represents the same localized zero coefficient through `log|zeta|` and a Laplacian supported on both transition strips of `chi`. That representation is exact. Equation (20) adds a useful analytic asymmetry that is hidden in the second-order potential form.

For the positive-frequency analytic shell, a plateau zero is reconstructed by the first-order current from the **shallower cumulative edge alone**. Therefore a future proof does not intrinsically need to show an independent cancellation or decorrelation between the two Ford edges. Any such two-edge argument is one possible potential-theoretic implementation, not a structural requirement imposed by the divisor.

This is especially relevant after `NB-248`. Returning to the potential representation can remove the Cauchy pole singularity, but the present calculation shows a more direct alternative: preserve the analytic frequency sign and perform the Cauchy projection before taking any quadratic norm. Both routes must ultimately control the same marked zero current.

The simplification does not remove the actual obstruction. For a matched packet with `M asymp J` and

\[
\tau_{j+1}-\tau_j
=\frac{2\pi q}{YJ},
\tag{26}
\]

one still has

\[
e^{iYJ(\tau_{j+1}-\tau_j)}=1.
\tag{27}
\]

Each projected coefficient has size `asymp 1/J`, so `Theta(J)` such coefficients can remain phase coherent and produce order-one current. After squaring, the diagonal is only `O(1/J)` as in `NB-243`; the unresolved mass is again the off-diagonal depth-marked carrier energy.

Thus (20) is a representation correction, not a new zero-density theorem.

## 6. Prior-art and novelty boundary

The Fourier-support statement behind (13) is classical Hardy-space/Cauchy-transform theory, equivalent to the standard fact that boundary values of half-plane Hardy functions have one-sided Fourier support. The Sokhotski--Plemelj/Cauchy projection viewpoint and the contour computation of (13) are not new.

A targeted prior-art search for this pass checked those classical Cauchy/Hardy projection formulations and zeta logarithmic-derivative literature. It did not locate a source that couples the projection to the specific Ford variables `(d,tau)`, the positive Mellin shell `u in (0,1)`, and the exact cancellation (16)--(20). This is only a search boundary; no uniqueness claim is made.

No external theorem is load-bearing in the line-local calculation: (13) is proved by the elementary contour choice, while all Ford identities come from the already persisted representation. Therefore `SOURCES.md` does not need a new durable dependency.

The project-specific content is the combination of four ingredients: the exact `NB-237` first-order edge current, the positive-frequency support of the actual Mellin shell, the Ford scaling `JH=R`, and the depth exponential `e^{-d}`. Together they turn a generic Cauchy projection into the exact finite mark (20).

## 7. Adversarial review and falsification boundary

Several restrictions are essential.

First, the one-sided conclusion uses the actual support condition `supp phi subset (0,1)`. If the shell were replaced by a profile with substantial negative Fourier frequencies and `Y+u/J` changed sign, the complementary depth side would enter through the negative-frequency version of (13). The result is therefore source-faithful, not a statement about arbitrary smoothing kernels.

Second, the derivation is distributional at the pole. Separating the shell into Fourier frequencies and then integrating the Cauchy kernel must be justified by an Abel/Gaussian regularization or tempered-distribution Fourier transform. Treating the `y` integral as absolutely convergent would be incorrect. This is compatible with `NB-248`: the original two-dimensional pole is locally `L^1` but not `L^2`.

Third, (20) evaluates the model-pole action. It does not assert a globally absolutely convergent partial-fraction expansion for `zeta'/zeta`. Its use inside (5) is licensed by the same distributional divisor identity that produced `NB-237`: the holomorphic background carries no divisor mass, while each pole acts through the Cauchy projector above.

Fourth, the right/deeper edge is spectrally invisible only for zeros already in the plateau. For zeros in a transition, the cumulative integral (18) can include part of that transition and equals the intended fractional mark `chi(d_rho)`.

Finally, nothing here proves that the actual zeta zeros avoid a matched Ford packet, proves the hard-window mean of `NB-247`, or supplies the missing bridge from Nyman--Beurling distance to the source current. The surviving analytic target is still

\[
\sup_{t_0}
H\int_{t_0-A/H}^{t_0+A/H}
|\mathcal R_{t_0}(s)|^2\,ds
=o(1),
\tag{28}
\]

or an exactly equivalent depth-marked two-copy carrier estimate.

A decisive falsification of the one-sided projection claim would be a positive shell frequency for which the model kernel in (13) receives nonzero contribution from `d>d_rho`; the contour identity excludes this. A change of representation that introduces negative shell frequencies falls outside the claim rather than falsifying it.

## Conclusion

The pole-critical `L^2` obstruction of `NB-248` is real, but it occurs only if the first-order Ford field is squared **before** the analytic shell has performed its natural Cauchy projection. In the Ford pole coordinate, the supposedly large carrier becomes the fixed positive frequency `Y+O(1/J)`. That positive frequency projects onto `d<d_rho`, the Ford exponentials cancel exactly, and the cumulative edge integral returns `chi(d_rho)` with the correct `1/J` zero weight.

So the first-order route has a canonical legal order: **Hardy-project first, square second**. For plateau zeros this also removes an unnecessary interpretation from `NB-236`: two geometric cutoff edges appear in the potential formula, but the positive analytic carrier reconstructs each zero from the shallow cumulative side alone. What remains is not a pole-regularization problem; it is the same genuine off-diagonal carrier-coherence problem already isolated by `NB-243` and required in hard-window form by `NB-247`.