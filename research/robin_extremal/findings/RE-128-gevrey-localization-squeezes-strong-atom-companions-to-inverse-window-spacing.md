# RE-128 — Gevrey localization squeezes strong-atom companions to inverse-window spacing

**Status:** `EXACT-DERIVED + FINITE-ZERO-EDGE + NONISOLATED-EDGE + SPECTRAL-LOCALIZATION + GEVREY-FILTER + PHASE-SECTOR + LOCAL-ZERO-COUNT + COMPANION-LOCALIZATION + CA-PHASE-TRANSFER + REPRESENTATION-AUDITED + PRIOR-ART-AUDITED`.

Assume the attained finite-edge branch and notation of `RE-121`--`RE-127`,

\[
\frac12<\Theta:=\sup_{\zeta(\rho)=0}\Re\rho<1,
\qquad
\frac12<\sigma_0<\Theta.
\]

For a positive-ordinate subedge zero `rho=beta+i gamma`, write

\[
a_{\rho,K}(u)
:=e^{-(\Theta-\beta)u}
\left[
\frac1{\rho(1-\rho)}
+
\sum_{k=1}^{K}\frac{(-1)^k k!}{u^k(1-\rho)^{k+1}}
\right]
\tag{1}
\]

and

\[
\mathcal S_K(u)
=
2\Re\sum_{\substack{\zeta(\rho)=0\\
\sigma_0\le\Re\rho<\Theta\\
\Im\rho>0}}
a_{\rho,K}(u)e^{i\gamma u}.
\tag{2}
\]

Fix `K>=0`, `A>0`, `0<theta<1`, and `varepsilon>0`. Let `rho_0=beta_0+i gamma_0` satisfy

\[
|a_{\rho_0,K}(U)|\ge cU^{-A}
\tag{3}
\]

for fixed `c>0`, and put `H:=U^(1-theta)`. Let `c_*>0` be the reinforcing inner-radius constant from `RE-125`.

Then there are constants `epsilon_*>0`, `c_1>0`, `C_1>0`, and `U_0`, depending only on the fixed parameters, such that if `U>=U_0` and

\[
\sup_{|u-U|\le H}|\mathcal S_K(u)|
\le
\epsilon_*|a_{\rho_0,K}(U)|,
\tag{4}
\]

there exists a distinct-ordinate zero `rho_1=beta_1+i gamma_1` with

\[
\boxed{
\frac{c_*}{U}
<|\gamma_1-\gamma_0|
\le
C_1\frac{(\log U)^{1+\varepsilon}}{H}
=C_1U^{-1+\theta}(\log U)^{1+\varepsilon}
}
\tag{5}
\]

and

\[
\boxed{
|a_{\rho_1,K}(U)|
\ge
c_1\frac{|a_{\rho_0,K}(U)|}{\log U}
\gg\frac{U^{-A}}{\log U}.
}
\tag{6}
\]

Thus a hidden strong atom forces a logarithmically comparable companion at essentially the inverse length of the interval on which the residual is hidden. For the window used in `RE-124`--`RE-127`, `H=U^(1-eta/2)`, this gives for every fixed `varepsilon>0`

\[
\boxed{
|\gamma_1-\gamma_0|
\le
C_{\eta,\varepsilon}U^{-1+\eta/2}(\log U)^{1+\varepsilon},
}
\tag{7}
\]

which is asymptotically narrower than the previous `U^(-1+eta)` outer radius.

The companion is again near the attained edge:

\[
\Theta-\beta_1
\le
\frac{A\log U+\log\log U+O(1)}{U}.
\tag{8}
\]

Since the target has `gamma_0\ll_A U^(A/2)` by `RE-124` and (5) is `o(1)`, also `gamma_1\ll_A U^(A/2)`. Along an unbounded hidden-atom sequence whose target ordinates tend to infinity,

\[
|\gamma_1-\gamma_0|\log(2+\gamma_0)\to0.
\tag{9}
\]

The result is deliberately a **magnitude-and-spacing** statement. It does not move the signed center-phase companion of `RE-127` into the smaller annulus (5).

## 1. Gevrey cutoff

Set `s:=1+varepsilon>1`. Choose a real even frequency cutoff with

\[
0\le\widehat\phi\le1,
\qquad
\widehat\phi(\xi)=1\ (|\xi|\le1/2),
\qquad
\widehat\phi(\xi)=0\ (|\xi|\ge1),
\tag{10}
\]

and Gevrey order `s`. One direct construction starts from

\[
g(x)=0\quad(x\le0),
\qquad
g(x)=e^{-x^{-1/(s-1)}}\quad(x>0),
\]

uses `g(x)/(g(x)+g(1-x))` as a transition, and glues symmetric copies around the plateau. Direct differentiation gives

\[
\|\widehat\phi^{(m)}\|_1\le C_0C_2^m(m!)^s.
\tag{11}
\]

For the inverse Fourier transform `phi`, integration by parts `m` times and optimization with Stirling therefore give

\[
\boxed{|\phi(t)|\le C_s e^{-c_s|t|^{1/s}}.}
\tag{12}
\]

The endpoint `s=1` is unavailable because a nonzero compactly supported cutoff with a plateau cannot be analytic. This is the source of the `(log U)^(1+varepsilon)` loss.

## 2. Almost-full-window filtering

Fix a sufficiently large constant `B>1` and set

\[
L:=\frac{H}{B(\log U)^s},
\qquad
\phi_L(t):=L^{-1}\phi(t/L).
\tag{13}
\]

Then `H/L=B(log U)^s`, and (12) implies for every fixed `m>=0`

\[
\int_{|t|>H}|\phi_L(t)|\,|t|^m\,dt
\ll_{m,s}
L^mU^{-c_s'B^{1/s}}(\log U)^{O_{m,s}(1)}.
\tag{14}
\]

Choosing `B` after all fixed parameters makes every time-tail contribution smaller than any prescribed algebraic power. At the same time the exact frequency radius is

\[
L^{-1}=B\frac{(\log U)^s}{H}.
\tag{15}
\]

Consider the target-demodulated average

\[
I_{\rho_0}(U)
:=
\int_{1-U}^{\infty}
\phi_L(t)\mathcal S_K(U+t)e^{-i\gamma_0(U+t)}\,dt.
\tag{16}
\]

As in `RE-124`, split the zeros at `delta_rho:=Theta-beta <= D log U/U`. The complementary horizontal region contributes `O(U^(-D+o(1)))` on `|t|<=H`. For the near-edge region, `RE-124` gives, uniformly for `u=U+O(H)`,

\[
|a_{\rho,K}^{(m)}(u)|
\ll_{K,m,D}
\frac{e^{-\delta_\rho U}}{1+\gamma^2}
\left(\frac{\log U}{U}\right)^m.
\tag{17}
\]

Taylor expansion at `U` to sufficiently large fixed order has aggregate remainder

\[
\ll
\left(H\frac{\log U}{U}\right)^M
=(U^{-\theta}\log U)^M
=o(U^{-A}).
\tag{18}
\]

After whole-line extension using (14), each retained Taylor monomial is a derivative of `hat(phi)(L(gamma-gamma_0))`; hence it vanishes exactly for `|gamma-gamma_0|>L^-1`. For surviving modes, the `m`th term is bounded relative to its frozen center coefficient by

\[
O\!\left(\left(L\frac{\log U}{U}\right)^m\right)
=
O\!\left(\left(\frac{U^{-\theta}}{B(\log U)^{s-1}}\right)^m\right),
\tag{19}
\]

so the full filtered contribution of each surviving mode is bounded by a fixed multiple of `|a_(rho,K)(U)|`.

Inside `|gamma-gamma_0|<=c_*/U`, one has `L|gamma-gamma_0|<1/2` for large `U`. The multiplier is flat there, so all positive-order Fourier derivatives vanish. Up to the aggregate `o(U^-A)` error, inner-ball atoms therefore enter with their actual center coefficients, preserving the positive phase sector proved in `RE-125`.

## 3. Narrow-annulus mass and one companion

Hypothesis (4) and the Gevrey tail imply

\[
|I_{\rho_0}(U)|
\le
\|\phi\|_1\epsilon_*|a_{\rho_0,K}(U)|+o(U^{-A}).
\tag{20}
\]

The target and all other inner-ball atoms have positive target-demodulated real projection. Every remaining surviving positive-frequency mode lies in

\[
\mathcal A_{\theta,\varepsilon}(\rho_0;U)
:=
\left\{\rho\ne\rho_0:
\frac{c_*}{U}<|\gamma-\gamma_0|
\le B\frac{(\log U)^s}{H}\right\}.
\tag{21}
\]

The conjugate negative-frequency packet is outside the compact Fourier window for large `U`. Combining inner-sector positivity, (19), and (20), and choosing `epsilon_*` sufficiently small, yields

\[
\boxed{
\sum_{\rho\in\mathcal A_{\theta,\varepsilon}(\rho_0;U)}
|a_{\rho,K}(U)|
\gg|a_{\rho_0,K}(U)|.
}
\tag{22}
\]

The target is at polynomial height, and (21) has subunit width. The Riemann--von Mangoldt local count already used in `RE-126` therefore gives

\[
\#\mathcal A_{\theta,\varepsilon}(\rho_0;U)\ll_A\log U
\tag{23}
\]

with multiplicity. Pigeonholing (22) through (23) proves (5)--(6); the lower radius excludes equal-ordinate multiplicity. Equation (8) follows from (6) and the coefficient asymptotic from `RE-124`,

\[
|a_{\rho,K}(U)|
\asymp_K\frac{e^{-(\Theta-\beta)U}}{1+\gamma^2}.
\tag{24}
\]

## 4. CA consequence and boundary

If no logarithmically comparable companion exists in (21), the contrapositive gives

\[
\sup_{|u-U|\le H}|\mathcal S_K(u)|
\gg|a_{\rho_0,K}(U)|
\gg U^{-A}.
\tag{25}
\]

When `A<K+1`, `RE-123` transfers this algebraic continuum excursion to an actual regular CA state on its superalgebraically fine phase mesh.

Condition (5)--(6) is necessary, not sufficient. A close strong companion need not have the phase required to cancel the target. This proof also does **not** sharpen the signed center-phase conclusion of `RE-127`: in the transition part of the Fourier cutoff, positive Taylor terms are small relative to each annular coefficient but need not be small relative to the target when that coefficient is much larger. The absolute-mass estimate (22) is stable under those terms; a stronger center-phase assertion would need another argument. The diffuse-cloud branch remains untouched because (3) assumes an individually strong atom.

## 5. Representation and adversarial audit

No new arithmetic coordinate is introduced. The source remains the same absolutely convergent subedge packet, and the Gevrey filter is only a linear readout. The proof keeps the observation window `H`, filter length `L`, frequency radius `1/L`, and center coefficients distinct.

The proof never differentiates the full oscillatory packet, avoiding the divergent `sum 1/|gamma|` majorant identified in `RE-123`; only the slowly varying amplitude is differentiated, retaining reciprocal-square summability. Exact compact Fourier support removes distant ordinates after each finite Taylor term. The quantifier `s>1` is fixed before `U->infinity`, so no exact `O(H^-1 log U)` or `O(H^-1)` result is claimed. Multiplicity lies inside the reinforcing ball and cannot provide the required distinct-ordinate companion. The local zero count is invoked only after polynomial height and subunit width are established.

A separate reconstruction of the Gevrey decay, tail estimate, Taylor remainder, compact support, inner-sector positivity, local-count pigeonhole, multiplicity boundary, and CA transfer found no material objection. No `.review.md` sidecar is opened.

## 6. Prior-art boundary and research effect

The harmonic-analysis ingredient is classical. Compactly supported Gevrey cutoffs have fractional-exponential inverse-Fourier decay, and band-limited smooth windows with subexponential decay are standard. A modern neighboring reference is Bergold--Lasser, *Fourier Series Windowed by a Bump Function*, Journal of Fourier Analysis and Applications **26** (2020), article 65. The derivative-growth-to-decay step needed here is included above, so no external Gevrey theorem is load-bearing.

The nearest zero-spacing literature remains Bui--Goldston--Milinovich--Montgomery, *Small gaps and small spacings between zeta zeros* (Acta Arithmetica **210** (2023), 133--153, DOI `10.4064/aa220731-15-2`), and Maynard--Pratt, *Half-Isolated Zeros and Zero-Density Estimates* (International Mathematics Research Notices **2024** (19), 12978--13014, DOI `10.1093/imrn/rnae191`). They study unusually close or vertically isolated zeta zeros but not the finite-edge Robin/CA residual or the inverse-observation-window implication (5). A targeted search found no prior theorem asserting this line-specific splice, and no new external dependency is needed, so `SOURCES.md` is unchanged.

`RE-124`--`RE-126` forced a logarithmically comparable companion somewhere in every fixed `U^(-1+eta)` neighborhood. `RE-128` makes the scale depend on the actual hidden-residual window: a window of length `H` forces such a companion within `H^-1(log U)^(1+varepsilon)` for every fixed `varepsilon>0`. For `H=U^(1-eta/2)`, the exponent slack drops from `eta` to `eta/2` up to a near-logarithmic factor. The remaining strong-atom question is whether an attained off-critical edge can support infinitely many near-edge pairs this close **and** with the phase geometry needed for cancellation; the diffuse-cloud branch remains separate.