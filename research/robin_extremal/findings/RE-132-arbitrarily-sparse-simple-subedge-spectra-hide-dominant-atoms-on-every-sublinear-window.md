# RE-132 — arbitrarily sparse simple subedge spectra hide dominant atoms on every sublinear window

**Status:** `EXACT-DERIVED + MATCHED-CONTROL + FINITE-ZERO-EDGE + NONISOLATED-EDGE + SIMPLE-SPECTRUM + FUNCTIONAL-EQUATION-SYMMETRY + ARBITRARILY-SPARSE-OFF-CRITICAL-DENSITY + DOMINANT-ATOM-HIDING + RECIPROCAL-DOUBLET + SUBLINEAR-WINDOW-SHARPNESS + DECISIVE-NEGATIVE + REPRESENTATION-AUDITED + PRIOR-ART-AUDITED`.

The zero-density refinement in `RE-130` materially strengthens the atom extracted from an algebraic subedge packet, while `RE-129` shows that hiding such a dominant atom on a power-sublinear observation window forces a logarithmically comparable cancelling companion at inverse-window scale. It is tempting to try to close that branch by strengthening the **global number** of off-critical zeros. That information carrier is insufficient by itself.

Fix

\[
\frac12<\sigma_0<\Theta<1,
\qquad K\ge0,
\qquad A>0.
\]

There exists a formal simple zero spectrum, closed under the zeta symmetries

\[
\rho\mapsto\bar\rho,
\qquad
\rho\mapsto1-\rho,
\tag{1}
\]

with a finite attained right edge `Re rho=Theta` and an infinite subedge set in `sigma_0<=Re rho<Theta`, together with phases `U_j->infinity`, such that the following all hold. The word **formal** is essential: these coordinates are a matched control for the zero geometry and coefficient kernel used in `RE-124`--`RE-131`; they are not asserted to be zeros of `zeta` or of any Euler-product function.

For the same order-`K` coefficient law

\[
a_{\rho,K}(u)
:=e^{-(\Theta-\beta)u}
\left[
\frac1{\rho(1-\rho)}
+
\sum_{k=1}^{K}\frac{(-1)^k k!}{u^k(1-\rho)^{k+1}}
\right],
\tag{2}
\]

and formal positive-frequency subedge packet

\[
\mathcal S_K^{\rm ctl}(u)
:=2\Re\sum_{\substack{\rho\in\mathcal Z_{\rm ctl}\\
\sigma_0\le\Re\rho<\Theta\\
\Im\rho>0}}
a_{\rho,K}(u)e^{i\Im(\rho)u},
\tag{3}
\]

one can arrange

\[
\boxed{
M_K^{\rm ctl}(U_j)
:=\max_\rho|a_{\rho,K}(U_j)|
=(1+o(1))U_j^{-A},
}
\tag{4}
\]

and, for **every** window sequence `H_j=o(U_j)`,

\[
\boxed{
\sup_{|u-U_j|\le H_j}
|\mathcal S_K^{\rm ctl}(u)|
\ll
M_K^{\rm ctl}(U_j)
\left(
\frac{H_j}{U_j}+\frac1{U_j}+U_j^{-j}
\right)
=o(M_K^{\rm ctl}(U_j)).
}
\tag{5}
\]

In particular, for each fixed `0<theta<1`, the full packet hides a globally dominant algebraic atom throughout

\[
|u-U_j|\le U_j^{1-\theta}
\]

with relative size `O(U_j^-theta)+o(1)`. Thus every fixed-power sublinear window used in `RE-124`--`RE-129` is compatible with arbitrarily sparse off-critical support.

At the same time the positive-ordinate right-half-strip counting function can be made as small as

\[
\boxed{
N_{\rm ctl}(\sigma_0,T)=O(\log\log T).
}
\tag{6}
\]

Hence the control satisfies every polynomial zero-density upper bound

\[
N_{\rm ctl}(\sigma_0,T)\ll_\varepsilon T^\varepsilon
\qquad(\varepsilon>0),
\tag{7}
\]

and therefore, a fortiori, all fixed-strip one-level upper bounds of the form used in `RE-130`. The obstruction is not a shortage of global density strength. It is local phase geometry.

## 1. One simple reciprocal doublet gives the required local cancellation

Choose a rapidly increasing sequence `U_j`, to be specified below, and put

\[
\delta_j:=U_j^{-2},
\qquad
\beta_j:=\Theta-\delta_j,
\qquad
\Gamma_j:=U_j^{A/2},
\qquad
h_j:=\frac\pi{U_j}.
\tag{8}
\]

For all sufficiently large `j`, `beta_j>=sigma_0`. Insert the two simple positive-ordinate subedge coordinates

\[
\rho_{j,0}:=\beta_j+i\Gamma_j,
\qquad
\rho_{j,1}:=\beta_j+i(\Gamma_j+h_j),
\tag{9}
\]

and close them under (1). If the ambient branch is required to have an attained finite edge exactly as in `RE-121`--`RE-131`, adjoin any fixed finite simple quartet with right member on `Re rho=Theta`; those edge coordinates are absent from the strict-subedge sum (3) and change every count below only by `O(1)`.

The uniform coefficient expansion already proved in `RE-124` gives, for `u` comparable with `U_j`,

\[
a_{\rho,K}(u)
=
\frac{e^{-(\Theta-\beta)u}}{\rho(1-\rho)}
\left(1+O_K(u^{-1})\right).
\tag{10}
\]

Since `Gamma_j->infinity`, equations (8)--(10) yield

\[
|a_{\rho_{j,\ell},K}(U_j)|
=(1+o(1))\Gamma_j^{-2}
=(1+o(1))U_j^{-A}
\qquad(\ell=0,1).
\tag{11}
\]

The two coefficients are asymptotically equal. Their real parts are positive and

\[
\arg a_{\rho_{j,\ell},K}(U_j)=o(1),
\tag{12}
\]

because `1/[rho(1-rho)]` approaches the positive real axis as the ordinate tends to infinity.

But

\[
h_jU_j=\pi.
\tag{13}
\]

Therefore the second atom has an asymptotically maximally cancelling target-demodulated center projection,

\[
\boxed{
-\Re\left(
a_{\rho_{j,1},K}(U_j)e^{ih_jU_j}
\right)
=(1-o(1))|a_{\rho_{j,1},K}(U_j)|.
}
\tag{14}
\]

The geometry is strictly stronger than the necessary conclusion of `RE-129` and `RE-131`:

\[
|\gamma_{j,1}-\gamma_{j,0}|=\frac\pi{U_j},
\qquad
\beta_{j,1}-\beta_{j,0}=0,
\qquad
\frac{|a_{\rho_{j,1},K}(U_j)|}
{|a_{\rho_{j,0},K}(U_j)|}
=1+o(1).
\tag{15}
\]

In particular,

\[
|\gamma_{j,1}-\gamma_{j,0}|\log(2+\Gamma_j)
\longrightarrow0.
\tag{16}
\]

The pair is simple, exactly horizontally locked, separated by a genuine constant multiple of reciprocal scale, and has much more than the `1/log U` amplitude fraction required by the forced-companion theorem.

## 2. The same pair hides uniformly on every sublinear observation window

Write `u=U_j+t`. Since the two points in (9) have the same real part, their exponential damping is identical. Direct differentiation of the rational bracket in (2), or simply (10) together with `h_j/Gamma_j=o(U_j^-1)`, gives uniformly for `|t|=o(U_j)`

\[
\frac{a_{\rho_{j,1},K}(U_j+t)}
{a_{\rho_{j,0},K}(U_j+t)}
=1+O_K(U_j^{-1}).
\tag{17}
\]

The common damping is also stable because

\[
\delta_j|t|=\frac{|t|}{U_j^2}=o(U_j^{-1}).
\tag{18}
\]

Using (13), the positive-frequency contribution of this doublet is

\[
\begin{aligned}
&a_{\rho_{j,0},K}(u)e^{i\Gamma_ju}
+a_{\rho_{j,1},K}(u)e^{i(\Gamma_j+h_j)u}
\\
&\qquad=
a_{\rho_{j,0},K}(u)e^{i\Gamma_ju}
\left[
1-\left(1+O_K(U_j^{-1})\right)e^{i\pi t/U_j}
\right].
\end{aligned}
\tag{19}
\]

Hence for every `H_j=o(U_j)`,

\[
\sup_{|t|\le H_j}
\left|
 a_{\rho_{j,0},K}(U_j+t)e^{i\Gamma_j(U_j+t)}
+a_{\rho_{j,1},K}(U_j+t)e^{i(\Gamma_j+h_j)(U_j+t)}
\right|
\ll
U_j^{-A}
\left(
\frac{H_j}{U_j}+\frac1{U_j}
\right).
\tag{20}
\]

Taking `2Re` cannot increase this bound. Thus the `pi/U` matched control from the order-sharpness test in `RE-125` is not merely a frozen two-mode picture: with the actual finite-order coefficient law it suppresses an algebraically strong pair uniformly throughout every sublinear window.

The scale distinction is real. If `t=kappa U_j` with fixed nonzero `kappa`, then the cancellation factor in (19) contains

\[
1-e^{i\pi\kappa},
\tag{21}
\]

which is a fixed nonzero quantity. The construction therefore does **not** furnish the macroscopic-window hiding hypothesis of `RE-131`. This is a feature, not a gap in the claim: it identifies the precise point at which `RE-131` leaves the present matched-control class.

## 3. Lacunarity makes the target doublet globally dominant while preserving extreme sparsity

It remains to embed the local doublets into one infinite spectrum without allowing older or future clusters to spoil (4)--(5). This is achieved by choosing `U_j` recursively and sufficiently lacunarly.

At every stage require at least

\[
U_{j+1}\ge U_j^4.
\tag{22}
\]

When choosing `U_{j+1}`, enlarge it further so that two finite conditions hold. First, every already chosen cluster is exponentially damped at the next phase:

\[
\sum_{n\le j}
\frac{
\exp[-U_{j+1}/(2U_n^2)]
}{1+\Gamma_n^2}
\le
U_{j+1}^{-A-j-3}.
\tag{23}
\]

This is always possible because each `U_n^-2` is a fixed positive number once the earlier cluster has been chosen. Second, force the first future reciprocal-square height tail to satisfy

\[
U_{j+1}^{-A}
\le
2^{-j}U_j^{-A-j-2}.
\tag{24}
\]

After increasing subsequent phases similarly, (22) makes the entire future tail comparable with its first term. The universal coefficient envelope

\[
|a_{\rho,K}(u)|\ll_K(1+\gamma^2)^{-1}
\tag{25}
\]

then gives, uniformly on `|u-U_j|<=U_j/2`,

\[
\sum_{n>j}\sum_{\ell=0}^1
|a_{\rho_{n,\ell},K}(u)|
\ll U_j^{-A-j-2},
\tag{26}
\]

while (23), applied inductively, gives the same bound for all `n<j`. Consequently the `j`th pair contains the global maximizing subedge atoms at phase `U_j`, proving (4), and adding (20), (23), and (26) proves (5).

The same lacunarity makes the off-critical spectrum extraordinarily sparse. From (22),

\[
\log U_j\ge4^{j-1}\log U_1,
\]

and therefore, since `Gamma_j=U_j^(A/2)`, the number of positive-ordinate right-half-strip control zeros below height `T` is at most

\[
N_{\rm ctl}(\sigma_0,T)
\ll\log\log T.
\tag{27}
\]

All of these points are simple. Adding their functional-equation mirrors, conjugates, a finite edge quartet, or an arbitrary critical-line background with the usual total-zero density does not change the strict right-half-strip estimate (27). Thus neither functional-equation symmetry, simplicity, the global Riemann--von Mangoldt scale, nor any stronger **one-level upper density estimate** by itself conflicts with the local hiding mechanism.

## 4. Adversarial audit and prior-art boundary

The control was tested against the hypotheses that actually do work in `RE-124`--`RE-131`. It does not use exact multiplicity or coincident ordinates; every right-half-strip point can be simple. Its cancelling companion lies outside the reinforcing `c_*/U` inner ball of `RE-125` because that constant satisfies `c_*<pi/8`, while the control spacing is `pi/U`. It obeys the same coefficient kernel, not arbitrary signed exponential weights. The central atom is globally dominant in the complete synthetic subedge packet, so the example does not hide behind a diffuse cloud. The cross-cluster estimates are uniform on the observation window rather than pointwise at its center.

The construction also respects the distinction between a zero-density theorem and a local spacing theorem. Ingham and Guth--Maynard, already anchored in `SOURCES.md` and used in `RE-130`, control how many zeros can inhabit a fixed off-critical half-strip; they do not give a minimum separation between those zeros. The present spectrum is much sparser than either theorem requires and nevertheless contains the exact reciprocal doublets needed for cancellation.

A targeted literature audit also checked Maynard--Pratt, *Half-Isolated Zeros and Zero-Density Estimates* (IMRN 2024, DOI `10.1093/imrn/rnae191`, arXiv:2206.11729). Their work is explicitly sensitive to vertical zero distribution and identifies local progression/clustering configurations as obstructions to zero detection; it does not provide an unconditional theorem excluding sparse off-critical reciprocal-scale doublets of the kind above. No theorem from that paper is used in the derivation, so no new source dependency is introduced here.

The main kill test is the macroscopic scale. Equation (21) shows that this control stops hiding once the observation interval has fixed relative width. Therefore the finding does not contradict `RE-131`, does not show that its macroscopic hypothesis can occur for actual zeta zeros, and does not rule out a theorem combining macroscopic packet smallness with local zero geometry. It also does not construct an analytic function with this zero set, preserve an Euler product, or satisfy the full explicit-formula identities of `zeta`; those would be additional arithmetic information carriers absent from the density-only route being tested.

## 5. Research effect

`RE-130` and the present control separate two roles that should no longer be conflated. Better off-critical zero-density estimates **do** strengthen the conversion from algebraic packet mass to an algebraically strong dominant atom. But once such an atom has been extracted, global counting strength alone cannot exclude the `RE-129` cancellation geometry: even an `O(log log T)` simple off-critical spectrum can contain globally dominant, equal-amplitude `pi/U` doublets whose full packet is invisible on every sublinear window.

Thus the route

\[
\text{stronger one-level zero density}
\Longrightarrow
\text{no hidden dominant subedge atom}
\]

is false without an additional local input. The remaining useful inputs are genuinely different: derive the **macroscopic** hiding/visibility information exploited by `RE-131`, prove a source-specific local spacing or phase restriction for actual off-critical zeta zeros, or introduce an arithmetic zero-detection relation that the matched spectrum above cannot satisfy. Sharpening the exponent in `N(\sigma,T)` alone cannot close this branch.