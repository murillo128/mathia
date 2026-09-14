# RE-131 — macroscopic hiding forces polylogarithmic reciprocal-scale horizontally locked companions

**Status:** `EXACT-DERIVED + FINITE-ZERO-EDGE + NONISOLATED-EDGE + DOMINANT-ATOM-REDUCTION + MACROSCOPIC-WINDOW + GEVREY-LOCALIZATION + POLYLOG-RECIPROCAL-SPACING + HORIZONTAL-LOCKING + CANCELLING-PHASE + TWO-DIMENSIONAL-ZERO-DOUBLET + CA-PHASE-TRANSFER + REPRESENTATION-AUDITED + PRIOR-ART-AUDITED`.

Assume the attained finite-edge branch and notation of `RE-121`--`RE-130`,

\[
\frac12<\Theta:=\sup_{\zeta(\rho)=0}\Re\rho<1,
\qquad
\frac12<\sigma_0<\Theta,
\]

and fix `K>=0`. For a positive-ordinate subedge zero

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

Let

\[
M_K(U):=
\max_\rho |a_{\rho,K}(U)|,
\tag{3}
\]

and choose a maximizing zero

\[
\rho_0=\beta_0+i\gamma_0.
\tag{4}
\]

Fix `A>0`, a relative-window constant `0<kappa<1/2`, and a logarithmic exponent `D>2`. Suppose

\[
M_K(U)\ge cU^{-A}
\tag{5}
\]

for fixed `c>0`, and suppose the finite-edge packet is hidden on the macroscopic observation window

\[
\boxed{
\sup_{|u-U|\le\kappa U}|\mathcal S_K(u)|
\le
\epsilon_*M_K(U).
}
\tag{6}
\]

Then there are constants `epsilon_*>0`, `c_1>0`, `C_D>0`, and `U_0`, depending only on the fixed parameters, such that for `U>=U_0` there exists a distinct-ordinate zero

\[
\rho_1=\beta_1+i\gamma_1
\tag{7}
\]

with

\[
\boxed{
\frac{c_*}{U}
<
|\gamma_1-\gamma_0|
\le
C_D\frac{(\log U)^D}{U},
}
\tag{8}
\]

where `c_*>0` is the reinforcing inner-radius constant of `RE-125`, and with the same genuinely cancelling center projection as in `RE-129`,

\[
\boxed{
-\Re\!\left(
a_{\rho_1,K}(U)e^{i(\gamma_1-\gamma_0)U}
\right)
\ge
c_1\frac{M_K(U)}{\log U}.
}
\tag{9}
\]

In particular,

\[
\boxed{
c_1\frac{M_K(U)}{\log U}
\le
|a_{\rho_1,K}(U)|
\le
M_K(U).
}
\tag{10}
\]

The coefficient ratio in (10), together with the exact finite-edge coefficient law, also forces the two zeros to be horizontally locked:

\[
\boxed{
-\frac{\log\log U+O(1)}{U}
\le
\beta_1-\beta_0
\le
\frac{O(1)}{U}.
}
\tag{11}
\]

Hence

\[
\boxed{
|\beta_1-\beta_0|
\ll
\frac{\log\log U}{U},
\qquad
|\rho_1-\rho_0|
\ll_D
\frac{(\log U)^D}{U}.
}
\tag{12}
\]

Thus macroscopic hiding does not merely require a small normalized ordinate gap. It forces a **two-dimensional near-edge zero doublet**: the companion has logarithmically comparable coefficient, cancelling phase, ordinate spacing reciprocal up to an arbitrarily fixed power `D>2` of `log U`, and real part locked to the dominant zero at the much thinner `log log U/U` scale.

The macroscopic hypothesis (6) is stronger than the sublinear-window hypothesis of `RE-129`. The gain is correspondingly sharper: `RE-129` gives `U^{-1+theta}(log U)^(1+varepsilon)` spacing from a window of length `U^(1-theta)`, whereas (8) is `U^-1` up to polylogarithms. No exact `O(1/U)` spacing theorem is claimed.

## 1. A macroscopic window allows a reciprocal-scale Fourier filter

Choose a Gevrey order `s` with

\[
1<s<D
\tag{13}
\]

and use the same nonnegative compact-frequency cutoff as `RE-128`--`RE-129`,

\[
0\le\widehat\phi\le1,
\qquad
\widehat\phi(\xi)=1\quad(|\xi|\le1/2),
\qquad
\widehat\phi(\xi)=0\quad(|\xi|\ge1),
\tag{14}
\]

whose inverse Fourier transform satisfies

\[
|\phi(t)|\le C_s\exp(-c_s|t|^{1/s}).
\tag{15}
\]

Put

\[
H:=\kappa U,
\qquad
L:=\frac{H}{B(\log U)^D}
\tag{16}
\]

for a sufficiently large fixed `B`. The surviving frequency radius is now

\[
\boxed{
L^{-1}
=
\frac{B}{\kappa}\frac{(\log U)^D}{U}.
}
\tag{17}
\]

The time tail outside the observed window is superalgebraically small. Indeed,

\[
\frac{H}{L}=B(\log U)^D,
\]

so (15) gives

\[
\exp\!\left[-c_s(H/L)^{1/s}\right]
=
\exp\!\left[-c'_s(\log U)^{D/s}\right]
=U^{-\omega(1)},
\tag{18}
\]

because `D/s>1`. The lower endpoint `u=1` in the residual representation is even farther from the filter center on the `L` scale, and the packet is uniformly bounded there by the summable `1/(1+gamma^2)` envelope from `RE-130`. Thus the truncation and unobserved time tails are `o(U^-A)=o(M_K(U))`.

The target-demodulated filtered integral may therefore be treated exactly as in `RE-129`, but with the scale (16). Its zeroth-order positive-frequency terms are

\[
w_\rho(U)
a_{\rho,K}(U)e^{i(\gamma-\gamma_0)U},
\qquad
w_\rho(U)
:=
\widehat\phi\!\left(L(\gamma-\gamma_0)\right)
\in[0,1],
\tag{19}
\]

and vanish unless `|gamma-gamma_0|<=L^-1`.

## 2. Why the logarithmic exponent must exceed two in this argument

The only new bookkeeping issue is the frozen-coefficient error. First discard zeros with

\[
\Theta-\beta>C_0\frac{\log U}{U}
\tag{20}
\]

for a sufficiently large fixed `C_0`. By (1), the universal `1/(1+gamma^2)` height envelope, and absolute summability from `RE-130`, their total contribution at the filter scale is `o(U^-A)=o(M_K(U))` after choosing `C_0` in terms of `A` and the fixed Taylor order.

For every remaining mode, logarithmic differentiation of (1) gives the same relative drift scale used in `RE-128`--`RE-129`,

\[
\frac{d^j}{du^j}a_{\rho,K}(u)
=
a_{\rho,K}(U)
O_j\!\left(\left(\frac{\log U}{U}\right)^j\right)
\tag{21}
\]

through the effective support `|u-U|=O(L log^O(1) U)` of the filter. Hence the first Taylor scale is

\[
\lambda_U
:=
L\frac{\log U}{U}
\asymp
\frac1{(\log U)^{D-1}}.
\tag{22}
\]

By (5) and the coefficient estimate of `RE-124`, the dominant ordinate is polynomially bounded,

\[
\gamma_0\ll_A U^{A/2}.
\tag{23}
\]

Since `L^-1=o(1)`, Riemann--von Mangoldt gives only

\[
\#\{\rho:|\gamma-\gamma_0|\le L^{-1}\}
\ll_A\log U
\tag{24}
\]

zeros with multiplicity. Dominance gives `|a_(rho,K)(U)|<=M_K(U)` for all of them. Therefore the aggregate positive-order Taylor contamination is

\[
\ll
M_K(U)(\log U)\lambda_U
\ll
\frac{M_K(U)}{(\log U)^{D-2}}
=o(M_K(U)).
\tag{25}
\]

This identifies the threshold in the present proof. A macroscopic window alone would suggest a reciprocal filter, but the local `O(log U)` zero count costs one logarithm and coefficient drift costs another. Taking any fixed `D>2` absorbs both. The theorem does not assert that the power `2` is intrinsic; removing either loss could sharpen (8).

## 3. Sector positivity forces a cancelling companion inside the polylogarithmic reciprocal annulus

For the reinforcing inner ball

\[
|\gamma-\gamma_0|\le\frac{c_*}{U},
\tag{26}
\]

we have `L|gamma-gamma_0|=O((log U)^-D)<1/2`, so `w_rho(U)=1` and every positive Fourier derivative of the multiplier vanishes. The phase-sector lemma of `RE-125` therefore applies without loss: for some fixed `q_*>0`,

\[
\Re\!\left(
a_{\rho,K}(U)e^{i(\gamma-\gamma_0)U}
\right)
\ge
q_*|a_{\rho,K}(U)|.
\tag{27}
\]

In particular, the dominant target contributes at least `q_*M_K(U)` to the real part of the filtered integral.

On the other hand, (6), the superalgebraic time tail (18), the far-left horizontal split, and the aggregate Taylor estimate (25) make the filtered integral at most

\[
\|\phi\|_1\epsilon_*M_K(U)+o(M_K(U)).
\tag{28}
\]

Choose `epsilon_*` so that the first term is less than `q_*M_K(U)/4`. Exactly as in `RE-129`, the zeroth-order modes in

\[
\mathcal A_D(\rho_0;U)
:=
\left\{
\rho\ne\rho_0:
\frac{c_*}{U}<|\gamma-\gamma_0|
\le
L^{-1}
\right\}
\tag{29}
\]

must then carry total negative target-demodulated projection `gg M_K(U)`. The weights `w_rho` are real and lie in `[0,1]`, so passing from weighted to unweighted negative mass loses no sign information.

By the local count (24), the annulus contains only `O_A(log U)` zeros. Pigeonholing its negative projected mass yields a zero `rho_1` satisfying (8)--(10). In particular,

\[
\cos\!\left(
(\gamma_1-\gamma_0)U+\arg a_{\rho_1,K}(U)
\right)
\le
-\frac{c_1}{\log U},
\tag{30}
\]

so the extracted close pair has the required cancelling phase, not merely comparable magnitude.

## 4. Amplitude comparability locks the real parts

The uniform coefficient asymptotic from `RE-124`--`RE-130` is

\[
a_{\rho,K}(U)
=
\frac{e^{-(\Theta-\beta)U}}{\rho(1-\rho)}
\left(1+O_K(U^{-1})\right).
\tag{31}
\]

Because `beta` stays in the fixed compact interval `[sigma_0,Theta]`,

\[
|\rho(1-\rho)|\asymp 1+\gamma^2.
\tag{32}
\]

Moreover, (8) gives `|gamma_1-gamma_0|=o(1)`. Hence

\[
\left|
\log
\frac{|\rho_0(1-\rho_0)|}
{|\rho_1(1-\rho_1)|}
\right|
\le C
\tag{33}
\]

uniformly, and (31) gives

\[
\log\frac{|a_{\rho_1,K}(U)|}{|a_{\rho_0,K}(U)|}
=
(\beta_1-\beta_0)U+O(1).
\tag{34}
\]

Now use (10). Its lower bound gives

\[
-\log\log U+O(1)
\le
(\beta_1-\beta_0)U+O(1),
\tag{35}
\]

while maximality gives

\[
(\beta_1-\beta_0)U+O(1)
\le0.
\tag{36}
\]

These are exactly (11)--(12). Along any unbounded hidden-atom sequence, `RE-126` gives `gamma_0->infinity`; then the denominator ratio in (33) is in fact `1+o(1)`, so the right-hand side of (11) sharpens to `o(1/U)`. No such refinement is needed for the main conclusion.

Combining (8), (11), and (23) also gives

\[
|\rho_1-\rho_0|\log(2+\gamma_0)
\ll_{A,D}
\frac{(\log U)^{D+1}}{U}
\longrightarrow0.
\tag{37}
\]

Thus the forced pair is asymptotically much closer than the conventional local `1/log gamma` spacing scale even in the full complex plane, not merely in ordinate.

## 5. Adversarial audit

The main quantifier change from `RE-129` was checked explicitly. The theorem assumes hiding on a fixed relative window `|u-U|<=kappa U`; it does not infer this hypothesis from pointwise hiding at `U`, nor does it silently set the fixed `theta` of `RE-129` to a `U`-dependent value. The stronger spacing conclusion is paid for by the stronger observation window.

The Gevrey tail remains superalgebraic because the Fourier scale is smaller than the macroscopic window by `(log U)^D`, and `D/s>1`. The Taylor contamination is summed before taking signs; the bound (25) uses dominance and the full `O(log U)` local zero count, so no single-mode relative error is mistaken for a packet-relative error. The strict condition `D>2` is retained instead of claiming an unjustified `log U/U` or exact `1/U` radius.

Multiplicity cannot supply the companion because the lower radius in (8) excludes equal ordinates. The horizontal estimate does not assume that `beta_1<=beta_0`; it derives the asymmetric bounds in (11) from the exact amplitude ratio and maximality. The bounded denominator ratio in (33) is uniform even at bounded height, while along unbounded sequences it improves automatically. Finally, the theorem still gives only a necessary geometry for cancellation. It does not rule out such polylogarithmic reciprocal-scale off-critical doublets.

A separate adversarial pass over the window scaling, Gevrey tail, far-left horizontal discard, aggregate Taylor budget, local zero count, signed pigeonhole, coefficient-ratio logarithm, multiplicity, and CA transfer found no material objection, so no `.review.md` sidecar is opened.

## 6. Prior-art boundary

No new external theorem is load-bearing. Riemann--von Mangoldt and the standard coefficient estimates were already anchored in this research line, so `SOURCES.md` does not require a new entry.

A targeted literature audit checked the closest modern zero-geometry results. Bui--Goldston--Milinovich--Montgomery study small gaps and spacings between zeta zeros, principally in the RH/critical-line setting. Maynard--Pratt's half-isolated-zero method is explicitly sensitive to vertical zero distribution and yields zero-density consequences under additional structural hypotheses. Guth--Maynard's 2026 large-values theorem gives the current stronger global zero-density estimate `N(sigma,T)<=T^(30(1-sigma)/13+o(1))`. None of these results supplies, or excludes, the specific off-critical two-dimensional doublet forced here: a dominant near-edge atom with a logarithmically comparable companion at `O((log U)^D/U)` ordinate distance, `O(log log U/U)` horizontal distance, and a prescribed cancelling center phase.

No novelty is claimed for Gevrey localization, local `O(log T)` zero counting, or the elementary comparison of two exponentially damped coefficients. The line-specific result is the combination of a macroscopic Robin/CA hiding window with the dominant-atom mechanism of `RE-129`: **persistent hiding on a fixed relative phase window collapses the allowed companion geometry from power-loss inverse-window scale to polylogarithmic reciprocal scale and simultaneously locks the two real parts.**

## 7. Research effect

`RE-129` showed that a hidden dominant atom has a correctly phased companion within `U^(-1+theta)` up to logarithms, while `RE-130` showed that every algebraically relevant finite-edge packet contains such a dominant atom. `RE-131` identifies a stronger regime that is relevant to any contradiction argument supplying uniform algebraic smallness over a fixed relative range of phases: in that regime the power loss disappears entirely.

The remaining finite-edge obstruction is now more concrete. Macroscopic hiding requires infinitely many near-edge, phase-tuned **two-dimensional zero doublets** with vertical gap at most `U^-1` times a fixed polylogarithm and horizontal gap only `O(log log U/U)`. Current zero-density and small-gap theorems do not exclude such a sparse off-critical configuration. A next theorem would have to exploit actual zeta zero geometry to rule out these doublets, reduce the polylogarithmic loss toward the exact reciprocal scale, or show that the Robin residual cannot remain hidden on the macroscopic windows required above. The nonattained-edge branch and `Theta=1` remain separate frontiers.
