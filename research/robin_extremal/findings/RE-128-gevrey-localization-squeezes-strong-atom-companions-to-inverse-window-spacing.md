# RE-128 — Gevrey localization squeezes strong-atom companions to inverse-window spacing

**Status:** `EXACT-DERIVED + FINITE-ZERO-EDGE + NONISOLATED-EDGE + SPECTRAL-LOCALIZATION + GEVREY-FILTER + PHASE-SECTOR + LOCAL-ZERO-COUNT + COMPANION-LOCALIZATION + CA-PHASE-TRANSFER + REPRESENTATION-AUDITED + PRIOR-ART-AUDITED`.

Assume the attained finite-edge branch and notation of `RE-121`--`RE-127`,

\[
\frac12<\Theta:=\sup_{\zeta(\rho)=0}\Re\rho<1,
\qquad
\frac12<\sigma_0<\Theta,
\]

and fix `K>=0`, `A>0`, `0<theta<1`, and `varepsilon>0`. For a positive-ordinate subedge zero

\[
\rho=\beta+i\gamma,
\qquad
\sigma_0\le\beta<\Theta,
\qquad
\gamma>0,
\]

write

\[
a_{\rho,K}(u)
:=
 e^{-(\Theta-\beta)u}
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
|a_{\rho_0,K}(U)|\ge cU^{-A}
\tag{3}
\]

for fixed `c>0`, and put

\[
H:=U^{1-\theta}.
\tag{4}
\]

Let `c_*>0` be the reinforcing inner-radius constant from `RE-125`. Then there are constants `epsilon_*>0`, `c_1>0`, `C_1>0`, and `U_0`, depending only on the fixed parameters, such that whenever `U>=U_0` and

\[
\sup_{|u-U|\le H}|\mathcal S_K(u)|
\le
\epsilon_*|a_{\rho_0,K}(U)|,
\tag{5}
\]

there exists a distinct-ordinate zero `rho_1=beta_1+i gamma_1` satisfying

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

Thus the strong-atom companion forced by `RE-125`--`RE-126` is not merely `U^(-1+eta)`-close for arbitrary fixed `eta`. If the residual is hidden on a window of half-length `H`, some logarithmically comparable companion is forced at inverse observation-window spacing, up to an arbitrarily small power above one of `log U`.

For the specific observation window used in `RE-124`--`RE-127`,

\[
H=U^{1-\eta/2},
\]

(6) becomes, for every fixed `varepsilon>0`,

\[
\boxed{
|\gamma_1-\gamma_0|
\le
C_{\eta,\varepsilon}
U^{-1+\eta/2}(\log U)^{1+\varepsilon}.
}
\tag{8}
\]

This is asymptotically narrower than the previous outer radius `U^(-1+eta)` by the factor

\[
U^{-\eta/2}(\log U)^{1+\varepsilon}=o(1).
\tag{9}
\]

As before, the companion is itself forced toward the attained edge:

\[
\Theta-\beta_1
\le
\frac{A\log U+\log\log U+O(1)}{U}.
\tag{10}
\]

Because (6) is `o(1)` and the target already satisfies `gamma_0\ll_A U^(A/2)` by `RE-124`, one also has `gamma_1\ll_A U^(A/2)` for large `U`. Along any unbounded hidden-atom sequence on which the target ordinates tend to infinity,

\[
|\gamma_1-\gamma_0|\log(2+\gamma_0)\to0.
\tag{11}
\]

The theorem is intentionally a **magnitude-and-spacing** statement. The Gevrey sharpening below does not by itself move the signed center-phase companion of `RE-127` into the smaller annulus (6); Taylor terms in the transition band can affect signed filtered projections when a neighboring coefficient is much larger than the target. No stronger phase conclusion is claimed here.

## 1. A compact Gevrey cutoff has almost-exponential time decay

Set

\[
s:=1+\varepsilon>1.
\tag{12}
\]

Choose a real even frequency cutoff `hat(phi)` such that

\[
0\le\widehat\phi\le1,
\qquad
\widehat\phi(\xi)=1\quad(|\xi|\le1/2),
\qquad
\widehat\phi(\xi)=0\quad(|\xi|\ge1),
\tag{13}
\]

and `hat(phi)` is Gevrey of order `s`. One may construct it directly from the standard transition

\[
g(x)=
\begin{cases}
0,&x\le0,\\
\exp(-x^{-1/(s-1)}),&x>0,
\end{cases}
\tag{14}
\]

by normalizing `g(x)/(g(x)+g(1-x))` on a transition interval and gluing two symmetric copies around the plateau. Direct differentiation (or Faà di Bruno applied to (14)) gives constants `C_0,C_2` such that

\[
\|\widehat\phi^{(m)}\|_1
\le
C_0 C_2^m(m!)^s
\qquad(m\ge0).
\tag{15}
\]

Let `phi` be the inverse Fourier transform in the convention already used by `RE-124`. Integrating by parts `m` times gives

\[
|t|^m|\phi(t)|
\le
C_0 C_2^m(m!)^s.
\tag{16}
\]

Optimizing over `m` with Stirling's formula yields constants `c_s,C_s>0` for which

\[
\boxed{
|\phi(t)|
\le
C_s\exp(-c_s|t|^{1/s}).
}
\tag{17}
\]

Thus exact compact frequency support is compatible with a time tail that is much better than arbitrary fixed Schwartz power decay. The analyticity endpoint `s=1` is excluded: a nonzero compactly supported cutoff with a genuine plateau cannot be analytic. This is why the proof below produces `(log U)^(1+varepsilon)` for every fixed `varepsilon>0`, not an exact logarithmic or constant loss.

## 2. The Gevrey tail lets the filter occupy almost the full observation window

Fix a large constant `B>1`, to be chosen after `A,K,theta,s`, and set

\[
L
:=
\frac{H}{B(\log U)^s},
\qquad
\phi_L(t):=L^{-1}\phi(t/L).
\tag{18}
\]

Then

\[
\frac{H}{L}=B(\log U)^s
\tag{19}
\]

and (17) implies, for every fixed nonnegative integer `m`,

\[
\int_{|t|>H}
|\phi_L(t)|\,|t|^m\,dt
\ll_{m,s}
L^m\,U^{-c_s'B^{1/s}}
(\log U)^{O_{m,s}(1)}.
\tag{20}
\]

Choosing `B` sufficiently large makes (20) `o(U^-D)` after multiplication by every fixed algebraic factor needed below, for any prescribed fixed `D`. In particular, the filter may be extended from the observed interval `|t|<=H` to the whole line at algebraic accuracy while its exact Fourier support has width

\[
L^{-1}
=B\frac{(\log U)^s}{H}.
\tag{21}
\]

This is the quantitative gain over the polynomial-tail implementation in `RE-124`, where `L` was kept a fixed power of `U` shorter than the observation window.

## 3. Slow horizontal drift survives the longer filter

Consider the same target-demodulated average as in `RE-124`,

\[
I_{\rho_0}(U)
:=
\int_{1-U}^{\infty}
\phi_L(t)\mathcal S_K(U+t)
 e^{-i\gamma_0(U+t)}\,dt.
\tag{22}
\]

The packet remains absolutely convergent because its coefficients have reciprocal-square ordinate weight. Split the zeros at

\[
\delta_\rho:=\Theta-\beta
\le
D\frac{\log U}{U}.
\tag{23}
\]

For the complementary horizontal region, uniformly on `|t|<=H=o(U)`,

\[
e^{-\delta_\rho(U+t)}
\le
U^{-D+o(1)},
\tag{24}
\]

so its total contribution is algebraically negligible once `D` is chosen large.

For zeros satisfying (23), `RE-124`'s derivative estimate gives, for every fixed `m`,

\[
|a_{\rho,K}^{(m)}(u)|
\ll_{K,m,D}
\frac{e^{-\delta_\rho U}}{1+\gamma^2}
\left(\frac{\log U}{U}\right)^m,
\qquad
u=U+O(H).
\tag{25}
\]

Taylor expansion at `U` through a sufficiently large fixed order has aggregate remainder

\[
\ll
\left(H\frac{\log U}{U}\right)^M
=
\left(U^{-\theta}\log U\right)^M
=o(U^{-A})
\tag{26}
\]

when `M` is chosen large enough. For each retained Taylor monomial, (20) permits whole-line extension with the same algebraic accuracy. The Fourier integral is then a derivative of

\[
\widehat\phi\bigl(L(\gamma-\gamma_0)\bigr),
\tag{27}
\]

so every Taylor term vanishes identically whenever

\[
|\gamma-\gamma_0|>L^{-1}.
\tag{28}
\]

For surviving modes, the `m`th Taylor term is bounded relative to the frozen coefficient by

\[
O_{K,m,D,s}\!\left(
\left(L\frac{\log U}{U}\right)^m
\right)
=
O\!\left(
\left(
\frac{U^{-\theta}}{B(\log U)^{s-1}}
\right)^m
\right),
\tag{29}
\]

and hence the full filtered contribution of each surviving mode is bounded by a fixed constant times `|a_(rho,K)(U)|`. This is all that the magnitude localization argument needs.

For the target itself, and more generally for every mode in the reinforcing inner ball

\[
|\gamma-\gamma_0|\le\frac{c_*}{U},
\tag{30}
\]

one has

\[
L|\gamma-\gamma_0|
\le
\frac{c_*U^{-\theta}}{B(\log U)^s}<\frac12
\tag{31}
\]

for large `U`. Since `hat(phi)` is identically one there, all positive-order Fourier derivatives vanish. Up to the aggregate `o(U^-A)` remainder, inner-ball atoms therefore enter with their **actual center coefficients**, exactly as in the phase-sector argument of `RE-125`.

## 4. Hiding the target forces absolute mass in the narrow annulus

The Gevrey tail and hypothesis (5) give

\[
|I_{\rho_0}(U)|
\le
\|\phi\|_1\epsilon_*|a_{\rho_0,K}(U)|
+o(U^{-A}).
\tag{32}
\]

By `RE-125`, every inner-ball contribution after target-frequency demodulation has real part at least a fixed positive fraction of its modulus. In particular, the target contributes a positive amount `>=q_*|a_(rho_0,K)(U)|` for some fixed `q_*>0`.

All other surviving positive-frequency modes lie in

\[
\mathcal A_{\theta,\varepsilon}(\rho_0;U)
:=
\left\{
\rho\ne\rho_0:
\frac{c_*}{U}<|\gamma-\gamma_0|
\le
B\frac{(\log U)^s}{H}
\right\}.
\tag{33}
\]

The negative-frequency conjugate packet remains outside the compact Fourier window for large `U`, exactly as in `RE-124`--`RE-125`. Using (29) to bound every annular filtered term by its center modulus, and taking `epsilon_*` sufficiently small, equations (3) and (32) imply

\[
\boxed{
\sum_{\rho\in\mathcal A_{\theta,\varepsilon}(\rho_0;U)}
|a_{\rho,K}(U)|
\gg
|a_{\rho_0,K}(U)|.
}
\tag{34}
\]

This is the Gevrey-sharpened version of the absolute-mass alternative from `RE-124`--`RE-125`.

The target height satisfies `gamma_0\ll_A U^(A/2)` by (3) and the reciprocal-square coefficient. The annulus (33) has width `o(1)`, so the ordinary Riemann--von Mangoldt local count used in `RE-126` gives

\[
\#\mathcal A_{\theta,\varepsilon}(\rho_0;U)
\ll_A\log U,
\tag{35}
\]

counting multiplicity. Pigeonholing (34) through (35) gives a zero `rho_1` satisfying (6)--(7). The lower radius excludes equal-ordinate multiplicity as the companion.

Equation (10) follows from (7) and the coefficient asymptotic

\[
|a_{\rho,K}(U)|
\asymp_K
\frac{e^{-(\Theta-\beta)U}}{1+\gamma^2},
\tag{36}
\]

already established in `RE-124`. Equations (11) and the stated height bound then follow exactly as above.

## 5. CA consequence and what this does not prove

The contrapositive is useful in the same way as `RE-124`--`RE-126`. If a strong target has no logarithmically comparable companion in the annulus (33), then

\[
\sup_{|u-U|\le H}|\mathcal S_K(u)|
\gg
|a_{\rho_0,K}(U)|
\gg U^{-A}.
\tag{37}
\]

When `A<K+1`, `RE-123` transfers such an algebraic continuum excursion to an actual regular CA state because the regular-CA phase mesh is superalgebraically finer than `H`.

The result is necessary, not sufficient. A companion satisfying (6)--(7) need not have the phase required to cancel the target. Conversely, the signed center-phase conclusion of `RE-127` is not automatically sharpened from `U^(-1+eta)` to (6) by this proof. The reason is precise: outside the flat part of the Fourier cutoff, positive Taylor terms of the slowly varying amplitude produce small **relative** corrections to each annular mode, but an annular mode can be much larger than the target. Those corrections are harmless for the absolute-mass estimate (34) and are not discarded here when reasoning about sign.

The diffuse-cloud branch also remains untouched: (3) assumes one individual atom already reaches algebraic scale. The theorem only narrows where a strong-atom cancellation mechanism must place at least one comparably strong neighboring zero.

## 6. Representation and adversarial audit

The source object is unchanged: the same absolutely convergent subedge zero packet and the same Robin/CA coefficient `a_(rho,K)`. The Gevrey filter is a linear readout, not a new arithmetic coordinate. The observation window `H`, filter length `L`, frequency radius `1/L`, and center coefficient are kept distinct; no raw/presentation coordinate is identified with another.

The main adversarial checks are the following. First, the proof never differentiates the full oscillatory packet, avoiding the divergent `sum 1/|gamma|` majorant already identified in `RE-123`; only the slowly varying amplitude is Taylor-expanded, preserving reciprocal-square summability. Second, the Gevrey cutoff has exact compact frequency support, so distant ordinates are removed exactly after each finite Taylor term rather than estimated by cancellation. Third, the tail estimate uses fixed `s>1` and a fixed sufficiently large `B`; there is no uniform passage `s->1`, so (6) does not imply an exact `O(H^-1 log U)` or `O(H^-1)` theorem.

Fourth, multiplicity cannot realize the required companion because equal ordinates lie in the reinforcing inner ball. Fifth, the local zero count is used only after (3) has placed the target at polynomial height and (33) has become a subunit interval; no short-interval zero-density asymptotic is assumed. Sixth, the phase-sensitive transition-band issue is kept explicit rather than silently replacing filtered coefficients by center coefficients at accuracy relative to the target. This is why the canonical conclusion is (7), not a strengthened version of the signed projection in `RE-127`.

A separate reconstruction of the Gevrey decay, physical-tail estimate, Taylor remainder, compact frequency support, inner-sector positivity, local-count pigeonhole, multiplicity boundary, and CA transfer found no material objection. No `.review.md` sidecar is opened.

## 7. Prior-art boundary

The harmonic-analysis ingredient is classical. Compactly supported Gevrey cutoffs have Fourier transforms with fractional-exponential decay, and band-limited smooth windows with subexponential time decay are standard; for a modern windowing discussion, see Bergold--Lasser, *Fourier Series Windowed by a Bump Function*, Journal of Fourier Analysis and Applications **26** (2020), article 65. The proof above includes the derivative-growth-to-decay argument needed here, so no external Gevrey theorem is load-bearing.

The nearest zeta-zero neighbors remain Bui--Goldston--Milinovich--Montgomery, *Small gaps and small spacings between zeta zeros* (Acta Arithmetica **210** (2023), 133--153, DOI `10.4064/aa220731-15-2`), and Maynard--Pratt, *Half-Isolated Zeros and Zero-Density Estimates* (International Mathematics Research Notices **2024** (19), 12978--13014, DOI `10.1093/imrn/rnae191`). They study unusually close or vertically isolated zeta zeros, but do not attach the finite-edge Robin/CA coefficient, a hidden residual on an observation window, or the inverse-window companion requirement (6).

A targeted search by Gevrey band-limited localization, exponential-sum uncertainty, vertical zero isolation, and small zeta-zero spacing found no prior theorem asserting this particular Robin/CA implication. The novelty claim is restricted to the line-specific splice: algebraic horizontal drift plus an almost-full-window Gevrey matched filter plus the `RE-125` positive inner sector plus the `RE-126` local-count step.

No new external theorem is required by the derivation, so `SOURCES.md` is unchanged.

## 8. Research effect

`RE-124`--`RE-126` showed that an invisible strong atom needs comparable mass, then a comparable individual companion, in every fixed near-reciprocal window `U^(-1+eta)`. `RE-128` ties the necessary spacing to the **actual length of the interval on which the residual is hidden**. A window of length `H` forces a logarithmically comparable companion within

\[
H^{-1}(\log U)^{1+\varepsilon}
\]

for every fixed `varepsilon>0`, up to a fixed constant.

For the existing `H=U^(1-eta/2)` window this nearly halves the exponent slack, from `U^(-1+eta)` to `U^(-1+eta/2)` times a near-logarithmic factor. The remaining strong-atom problem is correspondingly sharper: determine whether an attained off-critical edge can support infinitely many near-edge pairs this close **and** with the phase geometry needed to keep the Robin/CA subedge residual hidden. The genuinely diffuse-cloud branch remains separate.