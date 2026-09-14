# RE-128 — Gevrey localization squeezes strong-atom companions to inverse-window spacing

**Status:** `EXACT-DERIVED + FINITE-ZERO-EDGE + NONISOLATED-EDGE + SPECTRAL-LOCALIZATION + GEVREY-FILTER + PHASE-SECTOR + LOCAL-ZERO-COUNT + COMPANION-LOCALIZATION + CA-PHASE-TRANSFER + REPRESENTATION-AUDITED + PRIOR-ART-AUDITED`.

Assume the attained finite-edge branch and notation of `RE-121`--`RE-127`,

\[
\frac12<\Theta:=\sup_{\zeta(\rho)=0}\Re\rho<1,
\qquad
\frac12<\sigma_0<\Theta.
\]

Fix `K>=0`, `A>0`, `0<theta<1`, and `varepsilon>0`. For a positive-ordinate subedge zero `rho=beta+i gamma`, write

\[
a_{\rho,K}(u)
:=e^{-(\Theta-\beta)u}
\left[
\frac1{\rho(1-\rho)}
+
\sum_{k=1}^{K}
\frac{(-1)^k k!}{u^k(1-\rho)^{k+1}}
\right]
\tag{1}
\]

and

\[
\mathcal S_K(u)
=
2\Re
\sum_{\substack{\zeta(\rho)=0\\
\sigma_0\le\Re\rho<\Theta\\
\Im\rho>0}}
 a_{\rho,K}(u)e^{i\gamma u}.
\tag{2}
\]

Let `rho_0=beta_0+i gamma_0` be individually algebraically strong at `U`,

\[
|a_{\rho_0,K}(U)|\ge cU^{-A},
\tag{3}
\]

and put

\[
H:=U^{1-\theta}.
\tag{4}
\]

Let `c_*>0` be the reinforcing inner-radius constant from `RE-125`. Then there are constants `epsilon_*>0`, `c_1>0`, `C_1>0`, and `U_0`, depending only on the fixed parameters, such that if `U>=U_0` and

\[
\sup_{|u-U|\le H}|\mathcal S_K(u)|
\le
\epsilon_*|a_{\rho_0,K}(U)|,
\tag{5}
\]

there exists a distinct-ordinate zero `rho_1=beta_1+i gamma_1` for which

\[
\boxed{
\frac{c_*}{U}
<
|\gamma_1-\gamma_0|
\le
C_1\frac{(\log U)^{1+\varepsilon}}{H}
=
C_1U^{-1+\theta}(\log U)^{1+\varepsilon}
}
\tag{6}
\]

and

\[
\boxed{
|a_{\rho_1,K}(U)|
\ge
c_1\frac{|a_{\rho_0,K}(U)|}{\log U}
\gg
\frac{U^{-A}}{\log U}.
}
\tag{7}
\]

Thus the strong-atom companion forced by `RE-125`--`RE-126` can be localized at essentially the inverse length of the interval on which the residual is hidden, with only an arbitrarily small power above one of `log U` lost.

For the observation window used in `RE-124`--`RE-127`, `H=U^(1-eta/2)`, (6) gives for every fixed `varepsilon>0`

\[
\boxed{
|\gamma_1-\gamma_0|
\le
C_{\eta,\varepsilon}
U^{-1+\eta/2}(\log U)^{1+\varepsilon},
}
\tag{8}
\]

which is asymptotically narrower than the former outer radius `U^(-1+eta)`. The companion also satisfies

\[
\Theta-\beta_1
\le
\frac{A\log U+\log\log U+O(1)}{U},
\tag{9}
\]

and, because (6) is `o(1)` while `gamma_0\ll_A U^(A/2)` by `RE-124`, one has `gamma_1\ll_A U^(A/2)`. Along an unbounded hidden-atom sequence whose target ordinates tend to infinity,

\[
|\gamma_1-\gamma_0|\log(2+\gamma_0)\to0.
\tag{10}
\]

The conclusion is deliberately about **magnitude and spacing**. The argument below does not move the signed center-phase companion of `RE-127` into the smaller annulus (6).

## 1. Gevrey cutoff and almost-exponential time decay

Set `s:=1+varepsilon>1`. Choose a real even cutoff satisfying

\[
0\le\widehat\phi\le1,
\qquad
\widehat\phi(\xi)=1\quad(|\xi|\le1/2),
\qquad
\widehat\phi(\xi)=0\quad(|\xi|\ge1),
\tag{11}
\]

with `hat(phi)` Gevrey of order `s`. A direct construction starts from

\[
g(x)=
\begin{cases}
0,&x\le0,\\
\exp(-x^{-1/(s-1)}),&x>0,
\end{cases}
\]

uses `g(x)/(g(x)+g(1-x))` as a transition, and glues symmetric copies around the plateau. Direct differentiation gives

\[
\|\widehat\phi^{(m)}\|_1
\le
C_0C_2^m(m!)^s.
\tag{12}
\]

If `phi` is the inverse Fourier transform, integrating by parts `m` times and optimizing `m` with Stirling gives

\[
\boxed{
|\phi(t)|
\le
C_s\exp(-c_s|t|^{1/s}).
}
\tag{13}
\]

The endpoint `s=1` is unavailable because a nonzero compactly supported cutoff with a plateau cannot be analytic. Hence the proof gives `(log U)^(1+varepsilon)` for each fixed `varepsilon>0`, not an exact logarithmic or constant loss.

## 2. The filter can occupy almost the full observation window

Fix a sufficiently large constant `B>1` and set

\[
L:=\frac{H}{B(\log U)^s},
\qquad
\phi_L(t):=L^{-1}\phi(t/L).
\tag{14}
\]

Then `H/L=B(log U)^s`, and (13) implies for each fixed nonnegative integer `m`

\[
\int_{|t|>H}|\phi_L(t)|\,|t|^m\,dt
\ll_{m,s}
L^mU^{-c_s'B^{1/s}}(\log U)^{O_{m,s}(1)}.
\tag{15}
\]

By taking `B` large after all fixed parameters, every time-tail term needed below is smaller than any prescribed algebraic power. At the same time the exact frequency radius is

\[
L^{-1}=B\frac{(\log U)^s}{H}.
\tag{16}
\]

This replaces the fixed-power separation between filter length and observation length used in `RE-124` by a near-logarithmic separation.

## 3. Horizontal damping can still be frozen to algebraic accuracy

Consider the target-demodulated average

\[
I_{\rho_0}(U)
:=
\int_{1-U}^{\infty}
\phi_L(t)\mathcal S_K(U+t)e^{-i\gamma_0(U+t)}\,dt.
\tag{17}
\]

The packet is absolutely convergent because its coefficients retain reciprocal-square ordinate weight. Split the zeros according to

\[
\delta_\rho:=\Theta-\beta
\le
D\frac{\log U}{U}.
\tag{18}
\]

The complementary region contributes `O(U^(-D+o(1)))` uniformly on `|t|<=H=o(U)`. In the near-edge region, the derivative estimate already proved in `RE-124` is

\[
|a_{\rho,K}^{(m)}(u)|
\ll_{K,m,D}
\frac{e^{-\delta_\rho U}}{1+\gamma^2}
\left(\frac{\log U}{U}\right)^m,
\qquad
u=U+O(H).
\tag{19}
\]

Taylor expansion at `U` to a sufficiently large fixed order therefore has aggregate remainder

\[
\ll
\left(H\frac{\log U}{U}\right)^M
=
(U^{-\theta}\log U)^M
=o(U^{-A}).
\tag{20}
\]

After whole-line extension using (15), every retained Taylor monomial is a derivative of

\[
\widehat\phi(L(\gamma-\gamma_0)),
\]

and hence vanishes identically when `|gamma-gamma_0|>L^-1`. For a surviving mode its `m`th Taylor contribution is bounded relative to the frozen center coefficient by

\[
O\!\left(
\left(L\frac{\log U}{U}\right)^m
\right)
=
O\!\left(
\left(
\frac{U^{-\theta}}{B(\log U)^{s-1}}
\right)^m
\right).
\tag{21}
\]

Thus each surviving filtered mode is bounded by a fixed constant times `|a_(rho,K)(U)|`.

For the reinforcing inner ball `|gamma-gamma_0|<=c_*/U`,

\[
L|\gamma-\gamma_0|
\le
\frac{c_*U^{-\theta}}{B(\log U)^s}<\frac12
\]

for large `U`. Since `hat(phi)` is constant there, all positive-order Fourier derivatives vanish. Up to the aggregate `o(U^-A)` error, inner-ball atoms enter with their actual center coefficients, so the positive phase sector from `RE-125` is preserved.

## 4. Hidden residual forces mass in the narrow annulus

The observation hypothesis and the Gevrey tail give

\[
|I_{\rho_0}(U)|
\le
\|\phi\|_1\epsilon_*|a_{\rho_0,K}(U)|+o(U^{-A}).
\tag{22}
\]

The target and every other inner-ball atom have positive target-demodulated real projection by `RE-125`. All remaining surviving positive-frequency modes lie in

\[
\mathcal A_{\theta,\varepsilon}(\rho_0;U)
:=
\left\{
\rho\ne\rho_0:
\frac{c_*}{U}<|\gamma-\gamma_0|
\le
B\frac{(\log U)^s}{H}
\right\}.
\tag{23}
\]

The conjugate negative-frequency packet is outside the compact Fourier window for large `U`. Combining inner-sector positivity, (21), and (22), and choosing `epsilon_*` sufficiently small, gives

\[
\boxed{
\sum_{\rho\in\mathcal A_{\theta,\varepsilon}(\rho_0;U)}
|a_{\rho,K}(U)|
\gg
|a_{\rho_0,K}(U)|.
}
\tag{24}
\]

The target has `gamma_0\ll_A U^(A/2)`, while (23) has subunit width. The Riemann--von Mangoldt local count already used in `RE-126` therefore yields

\[
\#\mathcal A_{\theta,\varepsilon}(\rho_0;U)
\ll_A\log U
\tag{25}
\]

with multiplicity. Pigeonholing (24) proves (6)--(7); the inner radius excludes equal-ordinate multiplicity. Equation (9) follows from (7) and the coefficient asymptotic

\[
|a_{\rho,K}(U)|
\asymp_K
\frac{e^{-(\Theta-\beta)U}}{1+\gamma^2}
\]

from `RE-124`.

## 5. CA consequence and exact boundary of the claim

If a strong target has no logarithmically comparable companion in (23), the contrapositive gives

\[
\sup_{|u-U|\le H}|\mathcal S_K(u)|
\gg
|a_{\rho_0,K}(U)|
\gg U^{-A}.
\tag{26}
\]

When `A<K+1`, `RE-123` transfers this algebraic continuum excursion to an actual regular CA state on its superalgebraically fine phase mesh.

The condition (6)--(7) is necessary, not sufficient: the companion need not have the phase required to cancel the target. In particular, this proof does **not** sharpen the signed center-phase conclusion of `RE-127`. In the transition part of the Fourier cutoff, positive Taylor terms are small relative to each annular coefficient but need not be small relative to the target when that coefficient is much larger. The absolute-mass estimate (24) is stable under those terms; a center-phase sign claim is not obtained by discarding them. The diffuse-cloud branch also remains untouched because (3) assumes an individually strong atom.

## 6. Representation and adversarial audit

No new arithmetic coordinate is introduced. The theorem uses the same subedge zero packet and Robin/CA coefficients as `RE-124`--`RE-127`; `H`, `L`, `1/L`, and the center coefficient remain distinct quantities. The filter is only a linear readout.

The proof never differentiates the full oscillatory packet, avoiding the divergent `sum 1/|gamma|` majorant identified in `RE-123`. Only the slowly varying amplitude is differentiated, so reciprocal-square summability is retained. Exact compact Fourier support removes distant ordinates after each finite Taylor term. The `s>1` quantifier is fixed before `U->infinity`; no uniform `s->1` passage is claimed. Multiplicity lies inside the reinforcing ball and cannot provide the distinct-ordinate companion. The local zero count is used only after the strong target has forced polynomial height and the annulus has subunit width.

A separate reconstruction of the Gevrey decay, time-tail estimate, Taylor remainder, compact support, inner-sector positivity, local-count pigeonhole, multiplicity boundary, and CA transfer found no material objection. No `.review.md` sidecar is opened.

## 7. Prior-art boundary and research effect

The harmonic-analysis ingredient is classical: compactly supported Gevrey cutoffs have fractional-exponential inverse-Fourier decay, and band-limited smooth windows with subexponential decay are standard. A modern neighboring reference is Bergold--Lasser, *Fourier Series Windowed by a Bump Function*, Journal of Fourier Analysis and Applications **26** (2020), article 65. The derivative-growth-to-decay step required here is included above, so no external Gevrey theorem is load-bearing.

The nearest zero-spacing literature remains Bui--Goldston--Milinovich--Montgomery, *Small gaps and small spacings between zeta zeros* (Acta Arithmetica **210** (2023), 133--153, DOI `10.4064/aa220731-15-2`), and Maynard--Pratt, *Half-Isolated Zeros and Zero-Density Estimates* (International Mathematics Research Notices **2024** (19), 12978--13014, DOI `10.1093/imrn/rnae191`). Those works study unusually close or vertically isolated zeta zeros but not the finite-edge Robin/CA residual or the inverse-observation-window implication (6). A targeted search found no prior theorem asserting this line-specific splice, and no new external dependency is needed, so `SOURCES.md` is unchanged.

`RE-124`--`RE-126` forced a logarithmically comparable companion somewhere in every fixed `U^(-1+eta)` neighborhood. `RE-128` makes the scale depend on the actual hidden-residual window: a window of length `H` forces such a companion within `H^-1(log U)^(1+varepsilon)` for every fixed `varepsilon>0`. For the existing `H=U^(1-eta/2)` window, the exponent slack drops from `eta` to `eta/2` up to a near-logarithmic factor. The remaining strong-atom question is whether an attained off-critical edge can support infinitely many near-edge pairs this close **and** with the phase geometry needed for cancellation; the diffuse-cloud branch remains separate.