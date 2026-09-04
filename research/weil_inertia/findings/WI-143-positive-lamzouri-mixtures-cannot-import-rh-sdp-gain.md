# WI-143 — positive Lamzouri window mixtures cannot import the Chirre--Gonçalves--de Laat RH gain

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT`. Chirre--Gonçalves--de Laat (CGdL) obtain, under RH, the stronger pair-correlation multiplicity bound `N^*(T) <= (1.3208+o(1))N(T)`, hence at least `67.92%` simple zeros by the usual inequality `N_s >= 2N-N^*`. Their gain over Montgomery--Taylor uses a sphere-packing/semidefinite test whose **Fourier profile is allowed to be non-positive outside the interval where Montgomery's asymptotic is known**, while the form factor is globally nonnegative. A tempting route after Lamzouri's unconditional Hilbert-space proof is therefore to combine several Lamzouri windows and hope to reproduce the CGdL tail-sign freedom without assuming RH.

That route fails already at the exact finite Hilbert interface. Every Lamzouri window contributes a squared kernel `K_j^2`, whose real Fourier profile is, up to the harmless reflection fixed by Fourier convention, the convolution `eta_j^2 * eta_j^2` and is therefore nonnegative. Every positive convex combination or Hilbert direct sum of such propositions remains in the same Fourier-positive autocorrelation cone. Moreover, because Lamzouri's finite inequality is affine in its quadratic statistic, a convex mixture has asymptotic cost equal to the same convex mixture of the individual costs and can never beat the best constituent window. Thus **plain positive mixing of Lamzouri windows cannot import the CGdL `0.6792` mechanism**.

This obstruction is direct prior art at the broader Alpöge--Furman level: `teal-sea/zeta-lab` independently identified the CGdL transplant bottleneck as the fact that its out-of-band Fourier-sign condition is not realized by a Gram/autocorrelation kernel. The Mathia contribution here is only the exact convex-cone specialization to Lamzouri Proposition 2.1 and the resulting no-go for averaging/direct-sum repairs. No novelty or priority is claimed for the CGdL method or for the broader transplant obstruction.

## 1. Lamzouri's finite proposition is affine in a square-kernel statistic

Use Proposition 2.1 of Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1. Let `Z` be a finite conjugation-invariant multiset, `N=|Z|` count multiplicity, and `n` count simple real elements. For an admissible real even compactly supported window `eta`, normalized by

\[
\int_{\mathbb R}\eta(u)^2\,du=1,
\]

put

\[
q(u):=\eta(u)^2\ge0,
\qquad
K(\xi):=\widehat q(\xi).
\]

Lamzouri proves

\[
\boxed{
 n\ge 2N-Q_\eta,
 \qquad
 Q_\eta:=\sum_{z,s\in Z}K(z-s)^2.
}
\tag{1}
\]

The whole conjugation-adapted Hilbert argument is encoded in the validity of (1); no RH or zero-density hypothesis is used. WI-126 reconstructs the nonnegative slack discarded inside this proposition, but the present argument needs only the published inequality.

Take finitely many admissible windows `eta_1,...,eta_J` and weights

\[
a_j\ge0,
\qquad
\sum_{j=1}^J a_j=1.
\tag{2}
\]

Multiplying (1) by `a_j` and summing gives the exact finite inequality

\[
\boxed{
 n\ge 2N-Q_a,
 \qquad
 Q_a:=\sum_{j=1}^J a_jQ_{\eta_j}.
}
\tag{3}
\]

This is also exactly what a Hilbert direct sum produces after scaling the `j`-th component by `sqrt(a_j)`: the squared norm of the direct-sum tensor is the positive weighted sum of the component squared norms. Thus positive averaging and direct-sum packaging do not create a new cross-window invariant.

Negative coefficients are not an escape from (3). Multiplying a lower bound by a negative number reverses its direction, so an arbitrary signed linear combination is not a consequence of the individual Lamzouri propositions. At the Hilbert level the component weights enter as squared norms and are again nonnegative.

## 2. The square-kernel cone is Fourier-positive

For real `x`, evenness and reality of `q_j=eta_j^2` make

\[
K_j(x)\in\mathbb R,
\qquad
K_j(x)^2\ge0.
\tag{4}
\]

More importantly, the Fourier-side structure is rigid. With the convention

\[
\widehat f(\xi)=\int_{\mathbb R}f(u)e^{-2\pi iu\xi}\,du,
\]

we have `K_j=\widehat q_j`, and the Fourier transform of `K_j^2` is, up to reflection,

\[
\boxed{
\widehat{K_j^2}=q_j*q_j\ge0.
}
\tag{5}
\]

Because `q_j` is even, the reflection is immaterial. Therefore the real-gap profile associated with (3),

\[
g_a(x):=\sum_{j=1}^Ja_jK_j(x)^2,
\tag{6}
\]

satisfies

\[
\boxed{
\widehat g_a=\sum_{j=1}^Ja_j(q_j*q_j)\ge0.
}
\tag{7}
\]

In the unconditional support-one regime the relevant convolutions are also supported inside the evaluated Fourier band. In particular, a positive mixture can make the out-of-band profile zero, but it cannot make it negative. This sign constraint is not a numerical accident of the Montgomery--Taylor optimizer; it is a cone invariant of the Gram/autocorrelation construction.

The same observation survives arbitrary finite positive measures of windows: if `a` is a probability measure on an admissible window family and the integral exists, then

\[
g_a(x)=\int K_\eta(x)^2\,da(\eta)
\]

still has nonnegative Fourier profile because it is an integral of nonnegative convolutions. Hence passing from a finite mixture to a continuous window ensemble does not change the obstruction.

## 3. Convex mixing cannot improve the best Lamzouri cost

For the zeta-zero multiset at height `T`, suppose the unconditional pair-correlation evaluation gives, for each fixed admissible window,

\[
\frac{Q_{\eta_j}(T)}{N(T)}\longrightarrow R_j.
\tag{8}
\]

Then (3) gives

\[
\liminf_{T\to\infty}\frac{N_0^s(T)}{N(T)}
\ge
2-\sum_{j=1}^Ja_jR_j.
\tag{9}
\]

But

\[
\sum_{j=1}^Ja_jR_j\ge\min_jR_j,
\]

so

\[
\boxed{
2-\sum_ja_jR_j
\le
\max_j(2-R_j).
}
\tag{10}
\]

Thus the scalar convex hull of the Lamzouri inequalities has exactly the same optimum as its best extreme point. Within the standard single-window support-one class, the Montgomery--Taylor extremal problem is already solved; this is the optimization recorded in WI-001 and in the Carneiro--Chandee--Littmann--Milinovich Hilbert-space framework. Convexification does not enlarge the attainable constant.

Equation (10) is deliberately narrower than a general statement about using several profiles. A genuinely joint certificate may retain the vector `(Q_{eta_1},...,Q_{eta_J})` and impose configuration-wise nonlinear constraints that are not implied by its scalar average. WI-001 already leaves this as a live category, and several later Mathia audits study such joint information. The present no-go applies only when the multiple windows are collapsed through positive averaging/direct sum before the zero configuration is constrained.

## 4. Why the CGdL semidefinite gain lies outside this cone

Andrés Chirre, Felipe Gonçalves and David de Laat, *Pair Correlation Estimates for the Zeros of the Zeta Function via Semidefinite Programming*, Advances in Mathematics 361 (2020), 106926; arXiv:1810.08843v2, introduce the class `A_LP` of even continuous integrable functions `f` satisfying

\[
f(0)=\widehat f(0)=1,
\qquad
\widehat f\ge0,
\qquad
f\text{ eventually non-positive}.
\tag{11}
\]

For their multiplicity argument they rescale the nonnegative gap kernel

\[
g(x)=\frac1{r(f)}\widehat f\!\left(\frac{x}{r(f)}\right),
\tag{12}
\]

where `r(f)` is the last sign change. Consequently `g(x)>=0`, but its Fourier transform is a rescaling of `f` and obeys

\[
\boxed{
\widehat g(\alpha)\le0
\quad\text{outside the normalized known-correlation band}.
}
\tag{13}
\]

Their Lemma 8 combines this tail sign with the global nonnegativity of Montgomery's form factor. The unknown out-of-band contribution then has the favorable sign and may be discarded in an **upper** bound for the multiplicity statistic, while `g>=0` gives the diagonal/multiplicity lower bound. The resulting semidefinite optimization yields under RH the improved multiplicity constant around `1.3208`, hence the familiar `67.92%` simple-zero consequence.

The load-bearing distinction from (7) is therefore Fourier-side, not real-gap positivity: both constructions use nonnegative real-gap kernels in the RH scalar setting, but the CGdL improvement permits a **negative Fourier tail**, whereas every Lamzouri square kernel and every positive mixture of them has nonnegative Fourier profile everywhere. A positive Lamzouri mixture cannot approximate (13) while preserving the sign that makes (3) valid.

This explains why merely observing that the unconditional Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh form factor is nonnegative does not automatically make the CGdL `0.6792` proof unconditional. One still needs a zero-side finite inequality capable of consuming a sign-indefinite Fourier profile in the presence of off-critical conjugate pairs. Lamzouri Proposition 2.1 supplies such control only for its square-kernel tensor class.

## 5. Direct prior art and novelty boundary

The broader transplant obstruction is not new. The public `teal-sea/zeta-lab` audit `hunts/frontier_math/RESULTS-frontier-math.md`, section 4, explicitly studies the CGdL transplant after Alpöge--Furman. It notes that unconditional form-factor nonnegativity is available, but that the required out-of-band Fourier-sign profile is **not the Gram matrix of a window family because autocorrelations are nonnegative**; hence the existing inertia machinery does not apply as written. That audit also separates this obstruction from a different withdrawn candidate whose failure came from confusing transpose with conjugate transpose.

Accordingly, no novelty is claimed here for identifying CGdL's tail sign as the missing ingredient. The durable Mathia result is the exact specialization (3)--(10): at the newer Lamzouri Hilbert interface, every positive mixture/direct sum stays inside the autocorrelation cone and its zeta cost is only a convex average, so this particular repair is algebraically exhausted before any numerical SDP search begins.

The peer-reviewed CGdL theorem and the classical convolution identity behind (5) are literature-backed. Lamzouri's Proposition 2.1 is current primary-source input. The convex-mixture no-go (3), (7), and (10) is `EXACT-DERIVED`; its interpretation as a route closure is `LITERATURE+DERIVED + PRIOR-ART-REDIRECT` because the wider obstruction had already been identified by `zeta-lab`.

## 6. Boundaries and surviving routes

This finding does **not** prove that `0.6792` is unreachable unconditionally, nor does it strengthen the current Mathia simple-critical proportion. It rules out only the cheapest transplant: take several valid Lamzouri square-kernel propositions, combine them with positive scalar weights or a Hilbert direct sum, and hope the mixture itself reproduces CGdL's Fourier-tail freedom.

Several materially different routes remain outside the theorem. A joint multi-profile certificate may exploit incompatibility among the individual statistics without collapsing them to one convex average. A new matrix/Hilbert inequality could conceivably admit a sign-indefinite Fourier majorant while controlling the off-line signature blocks by another invariant. A source-specific near-line or separation theorem could restore a scalar argument on a restricted zero set. Finally, genuinely wider support remains possible only if the corresponding arithmetic evaluation is proved rather than assumed.

The decisive test for any proposed “CGdL + Lamzouri” splice is therefore simple. If its only zero-side justification is a positive sum/direct sum of Proposition 2.1 inequalities, then (7) and (10) reduce it to the best constituent window and the route is closed. To escape, the proposal must exhibit a new **joint or sign-indefinite zero-side inequality** and prove why it remains valid for the functional-equation/conjugation blocks off the critical line.

## Research consequence

Do not spend computation on semidefinite optimization over positive Lamzouri window mixtures: the feasible cone cannot realize the Fourier-tail sign responsible for the classical RH gain, and its scalar objective is extremized at one window. The relevant question is instead whether the CGdL negative-tail idea can be coupled to the modern off-line signature/Hilbert geometry through a genuinely new finite inequality, or whether a separate source-specific constraint makes that sign-indefinite observable controllable. This keeps the `0.6792` prior art as a useful target while removing a false cheap bridge to it.