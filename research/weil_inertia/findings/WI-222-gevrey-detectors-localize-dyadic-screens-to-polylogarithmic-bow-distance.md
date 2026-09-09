# WI-222 — Gevrey detectors localize dyadic screens to polylogarithmic bow distance

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + CLASSICAL-FOURIER + PRIOR-ART-REDIRECT`.

WI-221 proves that a screen pushed a natural-frequency distance `R_M -> infinity` from the distinguished bow must pay more than every fixed power of `R_M` in weighted coefficient mass. Coupled only with Jutila's published near-line zero-density theorem, that argument localizes an order-`M` radial-weighted dyadic zero source to `T^delta` bow widths for every fixed `delta>0`. The limitation there is not intrinsic to the source ledger: it comes from using an arbitrary compact `C^infty` detector and then fixing the number of integrations by parts before `T` grows.

A compact Gevrey detector gives a stronger quantitative tariff. Fix an interior reciprocal harmonic `k<d`, a bow population

\[
M=T^{\vartheta+o(1)},\qquad 0<\vartheta<1,
\tag{1}
\]

and any `s>1`. Under the same **dyadic-zero-screen hypothesis** as WI-221 §4 — namely, a finite screen assembled from zeros with `T<gamma<=2T` makes the normalized post-box bow-plus-screen residue tend to zero in `L^2` on one fixed natural-coordinate neighbourhood of the harmonic — there is a constant `A_s>0` such that

\[
\boxed{
\sum_{\substack{T<\gamma\le2T\\
|\nu_\rho|<A_s M(\log T)^s}}
\mu_\rho\cosh(k a_\rho)
\gg_{s,k,d} M.
}
\tag{2}
\]

Here `a_rho` and `nu_rho` are exactly the radial and phase parameters of the WI-214--WI-221 source dictionary. Equivalently, because

\[
\nu_\rho=\frac{(\gamma-\gamma_0)\log T}{2\pi d}
\tag{3}
\]

relative to the distinguished bow center `gamma_0`, (2) forces order-`M` radial-weighted source inside

\[
\boxed{
|\gamma-\gamma_0|
\ll_{s,k,d}
M(\log T)^{s-1}.
}
\tag{4}
\]

Taking `s=1+epsilon` gives, for every fixed `epsilon>0`, localization to physical ordinate radius

\[
\boxed{O_\epsilon\!\left(M(\log T)^\epsilon\right),}
\tag{5}
\]

or `O_epsilon((log T)^{1+epsilon})` natural bow widths. This is a strict strengthening of WI-221's `T^delta`-width localization for a dyadic zeta-zero screen.

The conclusion is still **weighted source localization, not raw zero-count localization**. It does not yet contradict the local Riemann--von Mangoldt budget, does not control non-dyadic explicit-formula tails, and does not touch WI-219's co-localized `Theta(M)` free companion. Its value is that the source-transport gap is now polylogarithmic rather than subpower.

## 1. Exact post-box model inherited from WI-218 and WI-221

At one fixed reciprocal harmonic, WI-218 writes the normalized bow as

\[
f_{M,k}(u)
=C_k\operatorname{sinc}(u)\rho_M(u),
\qquad
C_k=2\cosh(hk),
\tag{6}
\]

with `rho_M -> 1` uniformly on every fixed compact interval, and removes the outer physical tilt by the exact box operator

\[
(K_\eta r)(x)
:=\int_0^1e^{\eta v}r(x+v)\,dv,
\qquad
\eta_M=\frac{\log T}{2dM}\to0.
\tag{7}
\]

Put

\[
F_M:=K_{\eta_M}f_{M,k},
\qquad
F:=K_0(C_k\operatorname{sinc}).
\tag{8}
\]

Then `F_M -> F` uniformly on fixed compact intervals and `F` is not identically zero. A finite screen has the natural-coordinate form

\[
g_M(u)=\sum_\ell c_{\ell,M}e^{z_{\ell,M}u},
\qquad
z_{\ell,M}=\alpha_{\ell,M}+2\pi i\xi_{\ell,M}.
\tag{9}
\]

The hypothesis retained from WI-221 is that on one fixed compact interval `J`

\[
\boxed{
\|F_M+K_{\eta_M}g_M\|_{L^2(J)}=o(1).
}
\tag{10}
\]

For a screen that is subdiagonal on every fixed-multiplicative slab in WI-218's fixed power-scale band, (10) is necessary; WI-221 in fact records the stronger local square-norm `o(1/log T)` in that setting. Nothing below requires that stronger rate.

## 2. A compact Gevrey detector with stretched-exponential Fourier decay

Fix `s>1` and put

\[
q:=\frac1{s-1}>0.
\tag{11}
\]

The standard flat function

\[
\psi(x)
=
\begin{cases}
\exp(-x^{-q}),&x>0,\\
0,&x\le0,
\end{cases}
\tag{12}
\]

is Gevrey of order `s`. For completeness, the derivative estimate needed here can be obtained directly. For `x>0`, apply Cauchy's formula on a disk of radius `theta x`, with `theta=theta(q)>0` chosen so that throughout the disk

\[
\Re z^{-q}\ge c_q x^{-q}.
\]

Then

\[
|\psi^{(n)}(x)|
\le n!(\theta x)^{-n}e^{-c_qx^{-q}}.
\tag{13}
\]

Writing `y=x^{-q}`, the last factor has supremum

\[
\sup_{y>0} y^{n/q}e^{-c_qy}
=\left(\frac{n}{c_q q e}\right)^{n/q}.
\tag{14}
\]

Since `1/q=s-1` and `n^n<=e^n n!`, (13)--(14) imply constants `C_s,B_s>0` with

\[
\boxed{
\sup_x|\psi^{(n)}(x)|
\le C_s B_s^n(n!)^s
\qquad(n\ge0).
}
\tag{15}
\]

Products and affine translates preserve the same Gevrey order. Choose a nonnegative compactly supported Gevrey-`s` cutoff `chi` in `J`, supported where `F` is not identically zero, and define

\[
\phi(u):=\chi(u)\overline{F(u)}.
\tag{16}
\]

The function `F` is real-analytic on a neighbourhood of `J`, so `phi` is again compact Gevrey-`s`. Moreover

\[
A:=\int_J\phi(u)F(u)\,du
=\int_J\chi(u)|F(u)|^2\,du>0.
\tag{17}
\]

Thus, after changing constants,

\[
\|\phi^{(n)}\|_1
\le C B^n(n!)^s.
\tag{18}
\]

This derivative control gives a uniform stretched-exponential Fourier estimate even after a bounded real tilt. For `|alpha|<=1`, Leibniz and (18) give

\[
\left\|\frac{d^n}{du^n}\bigl(\phi(u)e^{\alpha u}\bigr)\right\|_1
\le C_1B_1^n(n!)^s.
\tag{19}
\]

Integrating by parts `n` times,

\[
\left|
\int_J\phi(u)e^{(\alpha+2\pi i\xi)u}\,du
\right|
\le
C_1\left(\frac{B_1n^s}{2\pi|\xi|}\right)^n.
\tag{20}
\]

Choose

\[
n=\left\lfloor c_0|\xi|^{1/s}\right\rfloor
\]

with fixed `c_0>0` small enough that the parenthesis in (20) is at most `1/2` once `|xi|` is large. Enlarging the constant for bounded `xi` yields

\[
\boxed{
\sup_{|\alpha|\le1}
\left|
\int_J\phi(u)e^{(\alpha+2\pi i\xi)u}\,du
\right|
\le C_s' e^{-c_s|\xi|^{1/s}}.
}
\tag{21}
\]

Finally `K_eta` acts diagonally on an exponential:

\[
K_\eta(e^{z\cdot})(u)
=q_\eta(z)e^{zu},
\qquad
q_\eta(z)=\int_0^1e^{(\eta+z)v}\,dv.
\tag{22}
\]

For `|eta|<=1` and `|Re z|<=1`, `|q_eta(z)|<=e^2`. Therefore

\[
\boxed{
\left|
\int_J\phi(u)K_\eta(e^{(\alpha+2\pi i\xi)\cdot})(u)\,du
\right|
\le C_s''e^{-c_s|\xi|^{1/s}}
}
\tag{23}
\]

uniformly for those bounded tilts.

Equation (23) is the quantitative replacement for WI-221's fixed-`N` integration-by-parts estimate.

## 3. Translation to actual functional-equation mirror pairs

For one off-line functional-equation mirror pair with radial parameter `a>=0`, unfolded phase frequency `nu`, and multiplicity `mu`, the pre-rescaling contribution is

\[
2\mu\cosh(at)e^{2\pi i\nu t}.
\tag{24}
\]

At `t=k+u/M`, after division by the bow population `M`, this is the sum of two exponential channels with

\[
|c_+|=\frac{\mu e^{ak}}M,
\qquad
|c_-|=\frac{\mu e^{-ak}}M,
\qquad
|\alpha_\pm|=\frac aM,
\qquad
|\xi_\pm|=\frac{|\nu|}M.
\tag{25}
\]

For a zeta zero in the critical strip,

\[
Y_\rho:=|\beta-\tfrac12|\log(T/2\pi)
\le\frac12\log T+O(1),
\qquad
a_\rho=\frac{Y_\rho}{d}.
\tag{26}
\]

Because `M=T^{vartheta+o(1)}` with `vartheta>0`, (26) gives

\[
\frac{a_\rho}{M}=o(1)
\tag{27}
\]

uniformly for the whole dyadic zero population. Thus the bounded-tilt hypothesis in (23) applies automatically for all sufficiently large `T`.

If every pair in a chosen far part satisfies

\[
\frac{|\nu_\rho|}{M}\ge R,
\tag{28}
\]

then (23)--(25) give

\[
\left|
\int_J\phi K_{\eta_M}g_{\rm far}
\right|
\ll_s
\frac{e^{-c_sR^{1/s}}}{M}
\sum_{\rho\in\mathcal S_{\rm far}}
\mu_\rho\cosh(ka_\rho).
\tag{29}
\]

No free coefficient assumption remains in (29): the coefficient is the exact source amplitude of the functional-equation pair.

## 4. Jutila's published density theorem closes the far tail at polylogarithmic distance

WI-029 and WI-221 already audit the published near-critical-line density input of Jutila. In the normalized horizontal coordinate `Y_rho`, it gives density-normalized exponential moments at every exponent strictly below one. Since the harmonic is interior,

\[
\frac{k}{d}<1,
\]

and therefore

\[
\boxed{
\sum_{T<\gamma\le2T}
\mu_\rho\cosh(ka_\rho)
\ll_{k,d}N_T,
}
\tag{30}
\]

where `N_T=N(2T)-N(T) asymp T log T`. This is the same load-bearing arithmetic input as WI-221; no Conrey-strength unpublished density estimate is used.

Combining (29)--(30), the complete far dyadic population contributes at most

\[
\ll_{s,k,d}
\frac{N_T}{M}e^{-c_sR^{1/s}}
=
T^{1-\vartheta+o(1)}e^{-c_sR^{1/s}}
	ag{31}
\]

to the detector.

Now choose

\[
R_T:=A_s(\log T)^s
\tag{32}
\]

with `A_s` fixed and sufficiently large that

\[
c_sA_s^{1/s}>1-\vartheta.
\tag{33}
\]

Then (31) is `o(1)`. Thus all zeros farther than `A_s(log T)^s` natural bow widths contribute negligibly to the fixed detector.

On the other hand, (10), (17), compact convergence `F_M->F`, and Cauchy--Schwarz imply

\[
\left|
\int_J\phi K_{\eta_M}g_M
\right|
=A+o(1).
\tag{34}
\]

Subtracting the `o(1)` far part, the near part has detector magnitude at least `A/2` for all sufficiently large `T`. Applying the bounded-frequency version of (23) and (25) in the opposite direction gives

\[
\frac1M
\sum_{\substack{T<\gamma\le2T\\
|\nu_\rho|<MR_T}}
\mu_\rho\cosh(ka_\rho)
\gg_{s,k,d}1.
\tag{35}
\]

Equations (32) and (35) are exactly (2).

## 5. Physical ordinate scale and the remaining count gap

The source dictionary identifies the phase by comparing

\[
e^{i(\gamma-\gamma_0)\log x}
\quad\text{with}\quad
e^{2\pi i\nu t},
\qquad
t=\frac{d\log x}{\log T}.
\]

Therefore

\[
\nu=\frac{(\gamma-\gamma_0)\log T}{2\pi d},
\]

which proves (3). The cutoff `|nu|<A_sM(log T)^s` becomes

\[
|\gamma-\gamma_0|
<2\pi dA_s M(\log T)^{s-1}.
\tag{36}
\]

The original bow occupies ordinate scale `M/log T`, so (36) is a radius of order `(log T)^s` bow widths. With `s=1+epsilon`, this is the polylogarithmic localization stated in (5).

This still does not pay the local zero-count bill. A vertical interval of length `M(log T)^epsilon` has a crude Riemann--von Mangoldt population scale of order `M(log T)^{1+epsilon}`, whereas (35) asks only for order-`M` **radial-weighted** mass. Moreover a small number of deeper off-line pairs can carry larger `cosh(ka)` weight. Thus (35) does not yet contradict source admissibility.

The source-count target is nevertheless much narrower than after WI-221. A continuation no longer needs to transport a dyadic screen from arbitrary `T^{o(1)}` distance. It must bridge only the residual logarithmic scale and convert the radial weight to a count or another source-controlled currency.

## 6. Why the Gevrey exponent cannot simply be set to one

The compact-detector argument above requires `s>1`. At `s=1`, the derivative bound is analytic; a nonzero real-analytic function cannot have compact support. Equivalently, a nonzero compactly supported function cannot have genuinely exponential Fourier decay of the form needed to replace (21) by `exp(-c|xi|)` uniformly at infinity.

This is classical Paley--Wiener/Gevrey territory, not a Mathia novelty claim. Tamer Tlas, **Bump functions with monotone Fourier transforms satisfying decay bounds**, *Journal of Approximation Theory* 278 (2022), 105742, DOI `10.1016/j.jat.2022.105742`, gives explicit compact smooth bumps with stretched-exponential Fourier decay `exp(-C|xi|^delta)` for every fixed `0<delta<1` and discusses the obstruction to true exponential decay for nonzero compact support. The elementary construction in §2 is self-contained and is the load-bearing proof here.

The `s>1` barrier should not be overread as an optimal localization theorem. More refined compact multipliers of Beurling--Malliavin/Denjoy--Carleman type can have decay closer to exponential than any fixed Gevrey order at the price of slowly varying losses. This finding does not audit or use such a theorem. It proves the clean fixed-`epsilon` statement (5) and leaves any `M loglog T`, `M`, or fixed-bow-width localization as a separate problem.

## 7. Prior-art and novelty boundary

**Literature-backed input.** Jutila's published near-line zero-density theorem and its `theta<1` exponential-moment consequence are already audited in WI-029/WI-221. Compact Gevrey functions and stretched-exponential Fourier decay are classical; Tlas gives a modern explicit bump construction and decay statement. No novelty is claimed for either ingredient separately.

A bounded search also found recent zeta-oriented proposals invoking Gevrey/Paley--Wiener decay for spectral confinement. The accessible metadata did not expose a theorem with the WI-218 post-box normalization, the functional-equation-pair coefficient ledger, Jutila's radial moment, or the polylogarithmic source-localization conclusion (2)--(5). Those proposals are not used as evidence. Absence of a matching search hit is not a priority claim.

**New repository deduction.** The substantive step is the exact coupling of a fixed compact Gevrey detector to WI-221's source dictionary and Jutila's dyadic radial budget. It upgrades the previously proved far-tail estimate from `R^{-N}` for each fixed `N` to `exp(-cR^{1/s})`, and therefore upgrades dyadic screen localization from `T^delta` bow widths for every fixed `delta>0` to `(log T)^{1+epsilon}` bow widths for every fixed `epsilon>0`.

This does not improve the current unconditional simple-critical-zero proportion and does not prove that the hypothetical screen exists. It is a structural constraint on any dyadic zeta-zero reservoir that could realize the selected cancellation.

## 8. Falsification hooks and research consequence

The finding would fail if any of the following occurred:

1. the compact cutoff in §2 failed to satisfy the Gevrey derivative estimate (15);
2. optimizing the integration-by-parts order did not give (21) uniformly for bounded real tilts;
3. `K_eta` introduced frequency growth rather than the bounded multiplier in (22)--(23);
4. the WI-214--WI-221 pair dictionary differed from (25);
5. a dyadic zeta zero could have `a/M` non-negligible in the polynomial-bow regime (1);
6. Jutila's audited moment (30) were being used at `k/d>=1` rather than the strictly interior harmonic `k<d`;
7. the conversion from `nu` to ordinate displacement in (3) missed the factor `log T/(2 pi d)`.

All seven checks are explicit in §§1--5 and in the previously audited WI-214/WI-218/WI-221 source normalizations.

The immediate research target is now sharper. **Do not spend further cycles proving only fixed-power remote localization.** For a dyadic zero reservoir that cancels the fixed-band bow, compact Gevrey detection already forces order-`M` radial-weighted source back to within `M(log T)^epsilon` ordinate distance for every fixed `epsilon>0`. The remaining RH-facing gate is to remove the logarithmic/local-count mismatch: either turn that radial-weighted mass into an order-`M` raw label charge in a genuinely `O(M/log T)` neighbourhood, or obtain a source/covariance theorem whose coercivity survives the remaining polylogarithmic transport freedom.