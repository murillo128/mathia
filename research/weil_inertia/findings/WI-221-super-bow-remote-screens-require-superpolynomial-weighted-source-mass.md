# WI-221 — super-bow remote screens require superpolynomial weighted source mass

**Status:** `EXACT-DERIVED + STRUCTURAL-RIGIDITY + DECISIVE-NEGATIVE + CLASSICAL-FOURIER + LITERATURE-CONTEXT`.

WI-220 proves that, on a proper fixed power-scale band, arbitrarily remote exponential frequencies are still complete in the free screen model. That is a genuine obstruction to any localization argument based only on support separation: a finite remote tail can approximate the bow as accurately as desired if its coefficients and channel count are unconstrained. The missing question left explicitly open there was whether that remote completeness can be realized at source-compatible cost.

It cannot at **super-bow-scale** separation. In the exact post-box natural coordinate of WI-218, let

\[
g_M(u)=\sum_{\ell=1}^{n_M}c_{\ell,M}e^{z_{\ell,M}u},
\qquad
z_{\ell,M}=\alpha_{\ell,M}+2\pi i\xi_{\ell,M},
\tag{1}
\]

be a finite screen and suppose every screen frequency satisfies

\[
|\xi_{\ell,M}|\ge R_M,
\qquad R_M\to\infty.
\tag{2}
\]

If the post-box bow-plus-screen residual tends to zero in `L^2` on one fixed natural-coordinate neighbourhood of a reciprocal harmonic, then for every fixed integer `N>=1`,

\[
\boxed{
\sum_{\ell=1}^{n_M}|c_{\ell,M}|
 e^{C|\alpha_{\ell,M}|}
 (1+|\alpha_{\ell,M}|)^N
\ \gg_N\ R_M^N,
}
\tag{3}
\]

where `C>0` depends only on the chosen fixed neighbourhood. Thus a remote screen whose radial exponents stay bounded cannot have coefficient `l^1` mass bounded by any fixed power of `R_M`. The qualitative completeness theorem used in WI-220 is therefore necessarily accompanied by a hidden superpolynomial coefficient cost when the screen is pushed farther than every fixed multiple of the bow bandwidth.

For actual functional-equation mirror-pair channels in the WI-214--WI-220 normalization, a pair with radial parameter `a>=0`, multiplicity `mu`, and unfolded phase frequency `nu` contributes two natural exponential channels. Equation (3) becomes the source-weighted tariff

\[
\boxed{
\sum_{\rho\in\mathcal S_M}
\mu_\rho\cosh(k a_\rho)
 e^{C a_\rho/M}
 (1+a_\rho/M)^N
\ \gg_N\ M R_M^N
}
\tag{4}
\]

whenever `|nu_rho|/M>=R_M` for every pair in the screen. In particular, at bounded radial depth,

\[
\boxed{
N_{\rm scr}\gg_N M R_M^N
\qquad\text{for every fixed }N.
}
\tag{5}
\]

This closes the cheapest escape left by WI-220: **free remote completeness cannot be converted into a polynomial-cost zeta-zero screen at super-bow-scale distance.** It does not yet localize a screen to a fixed multiple of the bow, because (3) is intentionally silent when `R_M=O(1)`. It also does not turn weighted source mass into raw zero count when radial depths are allowed to grow. Those are the remaining transport problems.

## 1. Exact post-box model and a fixed detector for the bow

Use WI-218's notation. At a fixed reciprocal harmonic `k`,

\[
\eta_M=\frac{\log T}{2dM}\to0,
\qquad
(K_\eta r)(s)=\int_0^1e^{\eta v}r(s+v)\,dv,
\tag{6}
\]

and the exact normalized bow is

\[
f_{M,k}(u)
=C_k\operatorname{sinc}(u)\rho_M(u),
\qquad
C_k=2\cosh(hk),
\tag{7}
\]

with `rho_M(u)->1` uniformly on every fixed compact interval. Put

\[
F_M:=K_{\eta_M}f_{M,k},
\qquad
F:=K_0(C_k\operatorname{sinc}).
\tag{8}
\]

Then `F_M->F` uniformly on compact intervals. Moreover `F` is not identically zero. Indeed `sinc` has Fourier support `[-1/2,1/2]`, and the box multiplier

\[
m_0(\xi)=\int_0^1e^{2\pi i\xi v}\,dv
\tag{9}
\]

has no zero on that closed band: `|m_0(xi)|>=2/pi` there, exactly as used in WI-218.

Choose a fixed compact interval `J` on which `F` is nonzero. There is a real nonnegative `chi in C_c^infty(J)` such that

\[
A:=\int_J\chi(s)|F(s)|^2\,ds>0.
\tag{10}
\]

Set

\[
\phi(s):=\chi(s)\overline{F(s)}.
\tag{11}
\]

Then `phi in C_c^infty(J)` and

\[
\int_J\phi(s)F_M(s)\,ds=A+o(1).
\tag{12}
\]

Suppose now that the finite screen (1) satisfies

\[
\left\|F_M+K_{\eta_M}g_M\right\|_{L^2(J)}=o(1).
\tag{13}
\]

Cauchy--Schwarz and (12) give, for all large `M`,

\[
\boxed{
\left|\int_J\phi(s)K_{\eta_M}g_M(s)\,ds\right|
\ge \frac A2.
}
\tag{14}
\]

The argument needs no pointwise approximation and no inversion of the box operator. It probes exactly the post-box observable already tied to the physical Gallagher norm in WI-218.

The local hypothesis (13) is necessary for the uniform subdiagonal-screening regime considered there. WI-218 gives, on each fixed-multiplicative physical block `S_b`,

\[
\frac{\text{selected source energy}}{\text{raw-prime diagonal}}
\asymp L\int_{S_b}|K_{\eta_M}(f_{M,k}+g_M)(s)|^2ds,
\tag{15}
\]

up to fixed block-dependent constants. If the same screen is `o` of the diagonal on every block in the fixed power-scale band, the block containing `J` forces (13), in fact with the stronger local square norm `o(1/L)`.

## 2. A remote exponential has rapidly decaying pairing with the detector

For one channel `e^{zu}`, `z=alpha+2 pi i xi`, the box acts diagonally:

\[
K_\eta(e^{z\cdot})(s)
=q_\eta(z)e^{zs},
\qquad
q_\eta(z):=\int_0^1e^{(\eta+z)v}\,dv.
\tag{16}
\]

If `|eta|<=1`, then

\[
|q_\eta(z)|
\le e^{1+|\alpha|}.
\tag{17}
\]

Let the support of `phi` be contained in `[-C_0,C_0]`. Repeated integration by parts against the imaginary phase gives, for every fixed `N>=1`,

\[
\begin{aligned}
\left|\int_J\phi(s)e^{(\alpha+2\pi i\xi)s}\,ds\right|
&\le
\frac{1}{(2\pi|\xi|)^N}
\left\|\frac{d^N}{ds^N}\bigl(\phi(s)e^{\alpha s}\bigr)\right\|_{L^1}\\
&\le
C_{\phi,N}
 e^{C_0|\alpha|}
 (1+|\alpha|)^N
 |\xi|^{-N}.
\end{aligned}
\tag{18}
\]

Combining (16)--(18), and enlarging the fixed constant in the radial exponential,

\[
\left|
\int_J\phi(s)K_{\eta_M}g_M(s)\,ds
\right|
\le
C_N R_M^{-N}
\sum_{\ell=1}^{n_M}|c_{\ell,M}|
 e^{C|\alpha_{\ell,M}|}
 (1+|\alpha_{\ell,M}|)^N.
\tag{19}
\]

Equation (14) now yields (3). Every step is finite and exact; no asymptotic theorem about zeta enters the coefficient-cost inequality itself. The only limits used are the already established compact convergence `rho_M->1` and `eta_M->0` in the WI-218 bow normalization.

A useful formulation is the following polynomial-budget no-go. If for some fixed `A,B` one has

\[
\sum_\ell |c_{\ell,M}|
 e^{C|\alpha_{\ell,M}|}
 (1+|\alpha_{\ell,M}|)^N
\ll R_M^A(\log R_M)^B
\tag{20}
\]

with the radial factor uniformly controlled, then choosing any fixed `N>A` contradicts (3) once `R_M->infinity`. The constants in (3) depend on `N`, so the claim is deliberately **superpolynomial**, not a uniform exponential lower bound with `N=N(M)`.

## 3. Translation to functional-equation mirror-pair source cost

The natural-coordinate coefficient ledger is explicit. Before rescaling, one off-line functional-equation mirror pair with radial parameter `a>=0` and unfolded phase frequency `nu` contributes

\[
2\cosh(at)e^{2\pi i\nu t}.
\tag{21}
\]

Write

\[
t=k+\frac uM
\tag{22}
\]

and divide by `M`, as in the normalized bow (7). Then (21) becomes

\[
\frac{e^{2\pi i\nu k}}{M}
\left[
 e^{ak}e^{(a/M+2\pi i\nu/M)u}
+
 e^{-ak}e^{(-a/M+2\pi i\nu/M)u}
\right].
\tag{23}
\]

Thus one pair contributes two channels with

\[
|c_+|=\frac{e^{ak}}M,
\quad
|c_-|=\frac{e^{-ak}}M,
\quad
|\alpha_\pm|=\frac aM,
\quad
|\xi_\pm|=\frac{|\nu|}{M}.
\tag{24}
\]

Positive integral multiplicity simply multiplies both coefficients by that integer. Substituting (24) in (3) and absorbing fixed factors gives (4).

Equation (4) keeps the currencies that WI-220 had to separate: phase distance, pair multiplicity, coefficient mass, and radial depth. In particular:

- if `a_rho=O(1)` uniformly, then the radial factor is bounded and (5) follows;
- if the pair count is only `O(M R_M^A)`, then any successful far screen must compensate by radial amplitude large enough to make the left side of (4) at least `M R_M^N` for every fixed `N`;
- if radial depth is itself source-controlled, the same inequality converts directly into a count lower bound.

This is why the result is stronger than merely saying that the WI-220 approximation coefficients “might be large.” Their weighted `l^1` mass is forced to beat **every fixed power** of the natural separation whenever the separation tends to infinity.

## 4. A dyadic zeta-source corollary from the existing zero-density ledger

There is one source-specific consequence that can already be made without a new zero-density theorem. WI-029 records that Jutila's published near-line density estimate controls density-normalized exponential moments

\[
\frac1{N_T}
\sum_{T<\gamma\le2T}
 e^{\theta Y_\rho}
\ll_\theta 1
\qquad(0\le\theta<1),
\tag{25}
\]

where

\[
Y_\rho=|\beta-\tfrac12|\log(T/2\pi).
\tag{26}
\]

At a strictly interior reciprocal harmonic `k<d`, the source radial parameter is `a=Y/d`, so

\[
\cosh(ka)
\ll e^{(k/d)Y},
\qquad \frac kd<1.
\tag{27}
\]

Hence the entire dyadic zero population has finite radial-weighted mass

\[
\boxed{
\sum_{T<\gamma\le2T}\mu_\rho\cosh(ka_\rho)
\ll_{k,d}N_T.
}
\tag{28}
\]

This is exactly below the `theta=1` borderline already discussed in WI-029; no unpublished Conrey-strength density estimate is being used.

Suppose, only for this corollary, that a screen assembled from the same dyadic zero population is responsible for the local post-box cancellation (13), and split it at natural ordinate distance `R`. The contribution of the far part `|nu|/M>=R` to the detector (14) is, by (19) and (28),

\[
\ll_N R^{-N}\frac{N_T}{M}
\tag{29}
\]

because `a/M=o(1)` throughout the critical strip when `M=T^{\vartheta+o(1)}`. Since

\[
\frac{N_T}{M}=T^{1-\vartheta+o(1)},
\tag{30}
\]

for every fixed `delta>0`, taking

\[
R=T^\delta
\tag{31}
\]

and then choosing a fixed

\[
N>\frac{1-\vartheta}{\delta}
\tag{32}
\]

makes (29) tend to zero. Therefore the near part must carry a fixed fraction of the nonzero detector moment. Reversing the bounded-frequency estimate gives

\[
\boxed{
\sum_{\substack{T<\gamma\le2T\\ |\nu_\rho|<MT^\delta}}
\mu_\rho\cosh(ka_\rho)
\gg_{k,d,\delta}M
}
\tag{33}
\]

for every fixed `delta>0`, under the stated dyadic-screen hypothesis.

Thus a dyadic zeta-zero reservoir cannot hide the entire screen at polynomially many bow widths away: an order-`M` **radial-weighted** amount of source must return within `T^delta` bow widths for every fixed positive `delta`. This is a genuine source-localization statement, but it is only subpower localization. The interval is still much larger than the original bow, so (33) does not yet recover WI-210's sharp local Riemann--von Mangoldt count budget.

The full source-fixed explicit formula can also draw on non-dyadic zero ranges and structured prime-side terms. Equation (33) therefore is not asserted for the entire complementary explicit-formula vector without a separate tail ledger. The unconditional and architecture-independent result of this finding is (3)--(4).

## 5. Prior-art audit and novelty boundary

The Fourier input behind (18) is classical: a compactly supported `C^infty` test function has Fourier transform decaying faster than every fixed power, equivalently obtainable here by repeated integration by parts. No novelty is claimed for that fact.

A bounded prior-art audit also found the expected neighboring theory:

- Tathagata Karmakar and Andrew N. Jordan, **Beyond Superoscillation: General Theory of Approximation with Bandlimited Functions**, arXiv:2306.03963 (2023), gives general constructions that mimic prescribed behavior on finite intervals and discusses the energetic price of superoscillatory/supergrowing behavior.
- Omer Friedland and Yosef Yomdin, **An observation on the Turán--Nazarov inequality**, *Studia Mathematica* 218 (2013), 27--39, DOI `10.4064/sm218-1-2`, is established Remez/Turán prior art for exponential polynomials on restricted sets.
- T. Tlas, **Bump functions with monotone Fourier transforms satisfying decay bounds**, *Journal of Approximation Theory* 278 (2022), 105742, DOI `10.1016/j.jat.2022.105742`, records compactly supported smooth test functions with explicit subexponential Fourier-decay behavior and the classical obstruction to true exponential decay for nonzero compact support.

These sources are context, not load-bearing inputs to (3). The exact WI-218 post-box coefficient/radial/source tariff (3)--(4) was not found in the bounded audit. Absence of a search hit is not evidence of priority and no priority claim is made.

The relation to existing Mathia results is strict:

- WI-218 charges **rank** `Omega(M)` when the same screen is subdiagonal over a fixed power-scale band, but is invariant under coefficient magnitude and phase distance.
- WI-219 shows that this linear rank tariff is order-sharp for a co-localized free screen with `Theta(M)` channels.
- WI-220 shows that support separation alone cannot improve it, because remote tails are complete on a proper band when coefficients are free.
- WI-221 adds the missing norm currency: once the natural separation `R_M` itself tends to infinity, the weighted coefficient/source mass must be at least `R_M^N` for every fixed `N`.

So WI-220 remains correct and essential. Its remote approximation is not refuted; its hidden coefficient cost is now quantified.

## 6. Barrier boundary and next target

The theorem deliberately does **not** prove any of the following:

1. It does not exclude screens at a fixed natural separation `R_M=O(1)`. In particular it does not touch WI-219's co-localized `Theta(M)` witness or a screen living a fixed number of bow widths away.
2. It does not replace weighted source mass by raw pair count when `a_rho` grows. Deep off-line zeros have larger `cosh(k a_rho)` amplitude and must be charged with a radial theorem, not silently counted as unit channels.
3. It does not control the non-dyadic zero tail or the complete signed `Lambda-Lambda^sharp` source vector. Section 4 is a dyadic zero-screen corollary, not an end-to-end explicit-formula theorem.
4. The constants `c_N` are fixed only after `N` is fixed. Equation (3) rules out every fixed polynomial budget, but does not justify choosing `N=N(T)` and claiming an exponential tariff.

These limitations identify the next useful transport theorem much more narrowly. A successful continuation should either obtain an explicit Gevrey/Paley--Wiener tariff with constants strong enough to shrink the `T^{o(1)}` localization window toward a fixed bow multiple, or combine (4) with a source-specific radial/count ledger that bounds the weighted mass available outside the WI-210 local interval. Merely moving a free screen farther away, with no coefficient accounting, is now closed as a cheap route.

## 7. Falsification hooks

The finding would fail if any of the following occurs:

- `K_eta` did not act diagonally on exponential channels as in (16);
- the WI-218 normalized bow failed to converge on fixed compact sets to `C_k sinc` after the exact box normalization;
- a nonzero compact detector `phi` could not be chosen for `F=K_0(C_k sinc)`;
- the repeated-integration-by-parts estimate (18) lost a factor depending on `xi` with the wrong sign;
- the mirror-pair dictionary (23)--(24) used a different natural-frequency normalization than WI-214--WI-220;
- WI-029's exponential-moment consequence were applied at `theta>=1` rather than the strictly interior value `theta=k/d<1`.

All six points have been checked against the exact formulas in WI-218, WI-214/WI-213, and WI-029. The mathematical claim retained here is the coefficient/source-cost barrier (3)--(4); the dyadic localization (33) is explicitly conditional on using that dyadic zero reservoir as the cancelling screen.