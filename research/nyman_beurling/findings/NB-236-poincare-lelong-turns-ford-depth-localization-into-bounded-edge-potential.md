# NB-236 — Poincaré–Lelong turns Ford depth localization into a bounded edge potential

**Date:** 2026-09-20  
**Status:** `EXACT-DERIVED + ZETA-SPECTRAL-REDUCTION + POTENTIAL-THEORETIC + BOUNDED-LOCALIZATION-TARIFF + NB-235-REFINEMENT + SOURCE-ONLY + PRIOR-ART-AUDITED`.

`NB-235` isolates the unresolved Ford transition as a microlocal Landau–Gonek remainder with an additional horizontal cutoff

\[
|X(1-\beta)-\log J|\le C.
\]

The classical cumulative Landau–Gonek formula does not provide that horizontal information, and black-box one-dimensional smoothing loses the microscopic ordinate scale. This finding changes representation in the missing direction. A smooth cutoff in Ford depth can be inserted directly into a Poincaré–Lelong pairing for `log|zeta|`. The resulting Laplacian is supported only on the two *edges* of the depth cutoff, and on the Ford scaling its total `L^1` mass is bounded by `O(Y)` rather than paying a positive power of `X`, `H`, or `J`.

Thus horizontal depth localization itself is not the next tariff. The remaining difficulty is cancellation of the local `log|zeta|` potential against a bounded-mass signed edge kernel. Equivalently, one needs local harmonic approximation or a cancellation-sensitive mean estimate for `log|zeta|` across the two transition strips. This is a sharper source-side target than either global Landau–Gonek or a population-only zero-density bound.

## 1. A smooth Ford cutoff has an exact potential representation

Use the coupled notation of `NB-228`--`NB-235`:

\[
Q=\log(10+|t|),
\qquad
R=Q^{2/3}(\log Q)^{1/3},
\qquad
Y=\frac XR,
\]

and define the exact carrier-capacity parameter

\[
J_0:=\frac RH\to\infty.
\tag{1}
\]

Fix `r>0`, put

\[
\sigma_X=1+\frac rX,
\qquad
s_X=\sigma_X+it,
\]

and let

\[
F(z)=\int_0^1\phi(y)e^{izy}\,dy,
\qquad
0\ne\phi\in C_c^\infty((0,1)).
\tag{2}
\]

The analytic continuation of the carrier from the zero set to a complex variable `s` is

\[
K_{X,H}(s)
:=e^{X(s-s_X)}F\!\left(-iH(s-s_X)\right).
\tag{3}
\]

At a zero `rho=beta+i gamma`, this is exactly the coefficient from `NB-235`:

\[
K_{X,H}(\rho)
=x^{\rho-s_X}F(Hv_\rho),
\qquad
v_\rho=(\gamma-t)+i(\sigma_X-\beta),
\qquad
x=e^X.
\tag{4}
\]

Now define the Ford-depth coordinate on the plane by

\[
d(s):=X(1-\Re s)-\log J_0.
\tag{5}
\]

Choose a real cutoff `chi in C_c^infty(R)` with `chi=1` on `[-C,C]`. The smoothly depth-localized test function is

\[
\Psi(s):=K_{X,H}(s)\chi(d(s)).
\tag{6}
\]

Distributionally,

\[
\Delta\log|\zeta(s)|
=2\pi\sum_\rho m(\rho)\delta_\rho-2\pi\delta_1,
\tag{7}
\]

where the sum is over zeros with multiplicity and the second term is the pole at `1`. Pairing (7) with `Psi`, and integrating by parts after a harmless vertical truncation, gives

\[
\boxed{
\sum_\rho m(\rho)\Psi(\rho)
=
\Psi(1)
+\frac1{2\pi}
\int_{\mathbb C}
\log|\zeta(s)|\,\Delta\Psi(s)\,dA(s).
}
\tag{8}
\]

Because `d(1)=-log J_0`, the pole term `Psi(1)` is exactly zero for all sufficiently large `J_0`: the pole lies outside the fixed compact support of `chi`. The trivial zeros are also outside the horizontal support once `X` is large, since their depth is `X(1+2n)-log J_0`. Thus (8) isolates the nontrivial Ford layer without introducing a separate pole or trivial-zero correction.

The identity is a smooth one-variable Poincaré–Lelong/Littlewood representation. Its use here is not the classical formula itself, but the scaling of its kernel for the exact Ford carrier.

## 2. The Laplacian lives only on the cutoff edges

The carrier `K_{X,H}` is holomorphic. Since

\[
\partial d=\bar\partial d=-\frac X2,
\]

all nonholomorphicity in (6) comes from the depth cutoff. A direct Wirtinger calculation gives

\[
\boxed{
\Delta\Psi(s)
=
X^2K_{X,H}(s)\chi''(d(s))
-2XK'_{X,H}(s)\chi'(d(s)).
}
\tag{9}
\]

Consequently `Delta Psi` vanishes throughout the plateau where `chi=1`. It is supported only in the two fixed-width transition strips where `chi'` or `chi''` is nonzero. The zeros in the entire critical interior are therefore represented by the potential `log|zeta|` measured on the *edges* of the horizontal layer.

There is a second useful cancellation. Since `Psi` is compactly supported horizontally and Schwartz in the ordinate direction,

\[
\boxed{
\int_{\mathbb C}\Delta\Psi(s)\,dA(s)=0.
}
\tag{10}
\]

Hence constants in `log|zeta|` disappear automatically. More generally, any harmonic comparison function `h` for which the integration by parts is justified satisfies

\[
\int h\,\Delta\Psi\,dA=0.
\tag{11}
\]

The pairing in (8) therefore sees the non-harmonic local fluctuation of the zeta potential, not its slowly varying harmonic background. This is the potential-theoretic analogue of the shell cancellation that removed the constant-in-ordinate Landau main term in `NB-235`.

## 3. Ford scaling makes the horizontal localization tariff bounded

The important point is the size of the edge kernel. Write

\[
\tau:=H(\Im s-t),
\qquad
 d:=X(1-\Re s)-\log J_0.
\tag{12}
\]

Then

\[
\Re s
=1-\frac{\log J_0+d}{X},
\qquad
X(\Re s-\sigma_X)
=-(r+\log J_0+d),
\tag{13}
\]

so on the fixed support of `chi'` and `chi''`,

\[
\left|e^{X(s-s_X)}\right|
=
\frac{e^{-r-d}}{J_0}.
\tag{14}
\]

Also

\[
-iH(s-s_X)
=
\tau+i\frac{r+\log J_0+d}{YJ_0}.
\tag{15}
\]

The imaginary displacement in (15) tends to zero uniformly on the cutoff edges. Since `F` is the Fourier transform of a smooth compactly supported profile, `F` and `F'` have uniform Schwartz bounds in `tau` for these small imaginary displacements.

Differentiate (3):

\[
K'_{X,H}(s)
=e^{X(s-s_X)}
\left[
XF\!\left(-iH(s-s_X)\right)
-iHF'\!\left(-iH(s-s_X)\right)
\right].
\tag{16}
\]

The coordinate Jacobian is

\[
dA(s)=\frac1{XH}\,dd\,d\tau.
\tag{17}
\]

Using (14)--(17) in the two terms of (9) yields

\[
\int_{\mathbb C}
|X^2K_{X,H}(s)\chi''(d(s))|\,dA(s)
\ll
\frac{X}{J_0H}
=
\frac XR
=Y,
\tag{18}
\]

and

\[
\int_{\mathbb C}
2X|K'_{X,H}(s)\chi'(d(s))|\,dA(s)
\ll
\frac{X}{J_0H}+\frac1{J_0}
=Y+J_0^{-1}.
\tag{19}
\]

Therefore

\[
\boxed{
\|\Delta\Psi\|_{L^1(\mathbb C)}
\ll_{\phi,\chi,r,C}
Y+J_0^{-1}.
}
\tag{20}
\]

On the Ford diagonal `Y -> Y_* in (0,infinity)` and `J_0 -> infinity`, the right-hand side is `O(1)`.

This cancellation of scales is the substantive point. The depth transition has physical horizontal thickness `1/X`, the ordinate packet has width `1/H`, the Ford carrier contributes `1/J_0`, and `J_0H=R`; after the derivatives in (9) are paid, the entire localization costs only `X/R=Y`. There is **no additional `X`, `H`, or `J_0` blow-up from imposing the horizontal cutoff smoothly**.

## 4. What the reduction does and does not buy

Combining (8) and (20), the critical-layer problem from `NB-235` can be attacked through the signed potential pairing

\[
\boxed{
\frac1{2\pi}
\int_{\mathbb C}
\log|\zeta(s)|
\left[
X^2K_{X,H}(s)\chi''(d(s))
-2XK'_{X,H}(s)\chi'(d(s))
\right]
\,dA(s).
}
\tag{21}
\]

The kernel in (21) has bounded total mass and is confined to two microscopic horizontal edge strips, while remaining Schwartz-localized vertically at scale `1/H`. This removes one ambiguity left by `NB-235`: the missing horizontal cutoff does **not** by itself force an expensive inversion or a growing variation norm.

But (20) is not an `o(1)` estimate. Taking absolute values against a crude local size bound for `log|zeta|` would at best give a bounded-mass average, and `log|zeta|` is itself singular at zeros. The useful cancellation is instead encoded in (10)--(11): one needs to show that, on these paired edge strips, the local zeta potential is well approximated by a harmonic background, or otherwise has sufficiently small signed correlation with `Delta Psi`.

This also clarifies why returning immediately to a zero-counting bound would be circular. The Poincaré–Lelong identity converts the weighted zeros into exactly the potential generated by those zeros. A population estimate that ignores the sign and oscillation of the edge kernel would simply recover the tariffs already exposed in `NB-230`--`NB-234`. The next input has to control the *potential fluctuation* or the signed edge pairing itself.

## 5. Prior-art and representation audit

The distributional identity (7) is classical Poincaré–Lelong in one complex variable, and rectangle versions are the familiar Littlewood lemma used throughout analytic number theory. Existing generalized Littlewood formulas likewise relate weighted zero sums to integrals of logarithms of analytic or meromorphic functions. No novelty is claimed for that machinery.

The prior-art search for this pass did not identify a published or posted estimate matching the coupled object in (21): a Ford-depth cutoff at horizontal scale `1/X`, a microscopic ordinate window `1/H`, and the exact carrier normalization `x^{s-s_X}` with a bound exploiting the resulting `O(Y)` Laplacian mass. This is a search boundary, not a claim that no such formulation exists.

The representation audit is correspondingly narrow. Equations (7)--(11) are generic complex analysis and would apply to another meromorphic function. The project-specific content is the exact carrier (3), Ford depth (5), and the scale cancellation in (18)--(20). Arithmetic enters through the zeta potential and through whatever future estimate controls its local non-harmonic part. Thus `NB-236` is a reduction and method-boundary result, not a new theorem about the actual distribution of zeta zeros.

No new external theorem beyond classical Poincaré–Lelong/Littlewood machinery is load-bearing in the quantitative calculation, so no new durable source dependency is required.

## 6. Adversarial review and durable frontier

Several possible overclaims were checked.

First, the cutoff is smooth, not a sharp characteristic function. It can equal one on the entire target layer `|d|<=C`, but zeros in the transition strips receive intermediate weights; (8) is therefore a smooth localization theorem, not an exact formula for a hard truncated sum. Second, `Psi` is not compactly supported vertically. Its Schwartz decay permits the distributional identity by truncation, but that truncation is part of the justification. Third, `log|zeta|` is only locally integrable near zeros, so (21) must be understood as a potential pairing rather than a pointwise bounded integrand estimate.

Fourth, bounded `L^1` mass of `Delta Psi` is only a tariff calculation. It proves that horizontal localization is affordable; it does not supply the cancellation needed for `o(1)`. Finally, the entire statement remains source-side. No implication from a small optimal Nyman–Beurling distance to the vanishing of (21) is established here.

Subject to those calibrations, the durable reduction is

\[
\boxed{
\text{critical Ford zero coefficient}
\quad\Longrightarrow\quad
\text{bounded-mass signed edge pairing with }\log|\zeta|,
}
\tag{22}
\]

with localization tariff `O(Y)`. The next non-circular source-side advance should therefore be a **microlocal harmonic-approximation or signed mean theorem for `log|zeta|` on the two Ford edge strips**, strong enough to make (21) `o(1)`. Improving global cumulative Landau–Gonek or population-only zero density cannot by itself exploit the cancellation exposed by this representation.
