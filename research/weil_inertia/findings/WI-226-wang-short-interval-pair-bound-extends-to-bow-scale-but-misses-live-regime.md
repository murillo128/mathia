# WI-226 — Wang's short-interval pair bound extends to bow scale but turns positive too late

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + PRIOR-ART-REDIRECT + DECISIVE-NEGATIVE`.

Biao Wang's fresh preprint arXiv:2609.07918 proves an unconditional Montgomery pair-correlation formula and Lamzouri-type simple-critical/distinct-zero proportions in every fixed power interval `I=(T,T+T^theta]`, `0<theta<1`. The displayed error terms in Wang's proof actually give the same limiting constants for any interval length

\[
H(T)=T^{\theta+o(1)}
\tag{1}
\]

with fixed `0<theta<1`. This includes the logarithmically shortened physical span of a fixed-power Maynard--Pratt bow.

That extension does **not** close the surviving bow regime. Wang's simple-critical lower bound becomes positive only for

\[
\theta>\theta_0=0.550193964744154\ldots,
\tag{2}
\]

and his distinct-zero lower bound only for

\[
\theta>\theta_d=0.346658926139761\ldots.
\tag{3}
\]

After WI-202, the still-live count-saturating fixed-power bow range is

\[
0<\vartheta\le \frac{3943}{12011}
=0.3282824077928565\ldots .
\tag{4}
\]

Since `3943/12011 < theta_d < theta_0`, **both of Wang's generic proportion bounds are nonpositive on the entire surviving count-saturating bow range**, even when one uses the stronger `T^{theta+o(1)}` reading justified below. Thus this new short-interval theorem is not the missing complementary reservoir theorem for the current bow obstruction.

The underlying short-interval pair-correlation identity remains potentially useful as an input to a future source-aware or coupled observable: it is valid on bow-scale intervals at any fixed exponent `vartheta>0`, but only with fixed Fourier support `lambda<vartheta`. In the live range this lies strictly below support one, where WI-115 and the subsequent screening controls warn that a universal vertical pair statistic alone can be cancelled. The preprint therefore redirects the program toward extracting **source-fixed signed/covariance information** from the local pair formula rather than treating its standalone simple/distinct proportions as a bow contradiction.

No unconditional global simple-critical-zero proportion changes here, and no claim is made that bow configurations occur among zeta zeros.

## 1. Primary theorem and provenance

The primary source is Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918v1, submitted 7 September 2026. It is a fresh unrefereed preprint and is not treated as peer-reviewed evidence.

For `H=T^theta`, Wang's Theorem 1.1 states, for every fixed `0<theta<1`,

\[
\liminf_{T\to\infty}
\frac{N_0^s(T,T^\theta)}{N(T,T^\theta)}
\ge c(\theta),
\qquad
c(\theta)=2-\frac\theta2-\frac1{\sqrt2}\cot\!\frac{\theta}{\sqrt2},
\tag{5}
\]

and

\[
\liminf_{T\to\infty}
\frac{N^d(T,T^\theta)}{N(T,T^\theta)}
\ge d(\theta),
\qquad
d(\theta)=\frac{1+c(\theta)}2
=\frac32-\frac\theta4-\frac1{2\sqrt2}\cot\!\frac{\theta}{\sqrt2}.
\tag{6}
\]

Here `N_0^s` counts simple critical-line zeros and `N^d` counts distinct nontrivial zeros regardless of real part. Wang records

\[
c'(\theta)=\frac12\cot^2(\theta/\sqrt2)>0,
\qquad
d'(\theta)=\frac14\cot^2(\theta/\sqrt2)>0,
\tag{7}
\]

with the unique positivity thresholds (2)--(3). In particular the distinct-zero statement is **not** a critical-line statement.

The analytic input is Wang's Theorem 2.2. For fixed

\[
0<\lambda<\theta<1
\tag{8}
\]

and fixed real even `g in C_c^infty(R)` supported in `[-lambda,lambda]`, putting `L=log T`,

\[
\sum_{\gamma,\gamma'\in I}
\widehat g\!\left(\frac{i(\rho-\rho')L}{2\pi}\right)
\frac{4}{4-(\rho-\rho')^2}
=
\frac{HL}{2\pi}
\left(g(0)+\int_{\mathbb R}|\alpha|g(\alpha)\,d\alpha\right)
+O_g(H+T^\lambda L^2).
\tag{9}
\]

Wang obtains this by adapting the unconditional Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh explicit-formula calculation to a short ordinate interval. The finite-multiset inequality converting the kernel sum to (5)--(6) is Lamzouri's Proposition 2.1; Wang does not assume RH.

The final variational problem is also explicit. For support length `lambda`, Wang minimizes

\[
C(f)=\int f(u)^2\,du+
\iint |u-v|f(u)f(v)\,du\,dv
\tag{10}
\]

and obtains the unique minimizer

\[
f_\lambda(u)=
\frac{\cos(\sqrt2 u)}{\sqrt2\sin(\lambda/\sqrt2)}
\mathbf 1_{[-\lambda/2,\lambda/2]}(u),
\tag{11}
\]

with

\[
C_\lambda=\frac\lambda2+\frac1{\sqrt2}\cot\!\frac\lambda{\sqrt2}.
\tag{12}
\]

Hence `2-C_lambda=c(lambda)` and `3/2-C_lambda/2=d(lambda)`. Letting `lambda` approach `theta` from below gives Theorem 1.1.

## 2. The proof is uniform enough for `H=T^{theta+o(1)}`

The statement of Wang's theorem fixes `H=T^theta`, so (1) is **not** quoted as a theorem from the preprint. It is an exact consequence of the error bookkeeping printed in its proof.

The Riemann--von Mangoldt formula used there is already written uniformly for `1<=H<=T`:

\[
N(T,H)=\frac{HL}{2\pi}+O(H+L).
\tag{13}
\]

For the pair correlation, Wang's Proposition 2.6 is uniform for `1<=x<=T^lambda` and keeps `H` explicit. After integrating `x=T^alpha`, `0<=alpha<=lambda`, the proof of Theorem 2.2 gives exactly the error in (9), namely

\[
O_g(H+T^\lambda L^2).
\tag{14}
\]

The rational-weight removal in Lemma 3.1 has the same error scale. Relative to the main scale `HL`, (14) is

\[
O_g\!\left(\frac1L+\frac{T^\lambda L}{H}\right).
\tag{15}
\]

Now assume (1) and fix any `lambda<theta`. Then

\[
\frac{T^\lambda L}{H}
=T^{\lambda-\theta+o(1)}L=o(1),
\tag{16}
\]

while `1/L=o(1)`. Since fixed `0<theta<1` also gives `1<=H<=T` eventually and `L/H=o(1)`, (13)--(16) reproduce Wang's normalized kernel limit and the Lamzouri inequalities for this more general `H`.

For each fixed `lambda<theta` this yields

\[
\liminf
\frac{N_0^s(T,H)}{N(T,H)}\ge c(\lambda),
\qquad
\liminf
\frac{N^d(T,H)}{N(T,H)}\ge d(\lambda).
\tag{17}
\]

Only after taking `T to infinity` do we let the fixed parameter `lambda` increase to `theta`. Continuity of (5)--(6) then gives the same endpoint constants `c(theta)` and `d(theta)`. No uniformity as `lambda=lambda(T)` approaches `theta` is asserted or needed.

This derivation uses no unprinted power saving. Its load-bearing conditions are precisely: a fixed exponent `theta`, a fixed strict support margin `lambda<theta`, polynomial interval length as in (1), and the explicit errors (13)--(14).

## 3. Specialization to the source-compatible bow scale

Maynard--Pratt's bow model has a fixed-power number of selected labels

\[
M=T^{\vartheta+o(1)}
\tag{18}
\]

with ordinate spacing on the natural `1/log T` scale. After functional-equation reflection and count normalization, WI-184 identifies `4 pi` as the count-saturating symmetrized spacing scale; WI-202 carries the resulting fixed-power bow bookkeeping through the currently source-safe short-interval critical-line input.

Consequently a count-saturating bow of fixed exponent `vartheta` has physical ordinate span

\[
H_{\rm bow}=T^{\vartheta+o(1)}
\tag{19}
\]

(the explicit `1/log T` factor and fixed spacing constants are absorbed into `T^{o(1)}`). Equation (1) therefore applies with `theta=vartheta`.

This observation removes a possible technical escape route: Wang states exact power intervals, whereas the bow is logarithmically shorter than `T^vartheta`. The displayed proof errors show that this logarithmic shortening does **not** matter. The obstruction is instead numerical and structural.

WI-202 uses the verified ANTEDB exponent pair

\[
\left(\frac{3316}{8695},\frac{914}{1739}\right)
\tag{20}
\]

to push the source-safe every-interval odd-critical reservoir far enough to exclude count-saturating bows for every fixed

\[
\vartheta>\vartheta_*
:=\frac{3943}{12011}
=0.3282824077928565\ldots.
\tag{21}
\]

Hence the only count-saturating fixed-power range still needing a different argument is `0<vartheta<=vartheta_*`. But Wang's own thresholds satisfy

\[
\vartheta_*=0.3282824\ldots
<\theta_d=0.3466589\ldots
<\theta_0=0.5501939\ldots.
\tag{22}
\]

By the monotonicity (7), throughout the whole live range

\[
\boxed{c(\vartheta)<0,\qquad d(\vartheta)<0.}
\tag{23}
\]

At its upper endpoint, for orientation,

\[
c(3943/12011)=-1.155387654276\ldots,
\qquad
d(3943/12011)=-0.077693827138\ldots.
\tag{24}
\]

Thus the simple-critical inequality gives no positive reservoir there, and even the formally easier distinct-zero inequality is still below the trivial zero lower bound.

There is a second, independent reason not to overread the distinct-zero part. Even where `d(theta)>0`, it counts distinct zeros **regardless of real part**. A mirror-closed bow already consists predominantly of distinct off-line zero labels, so a generic distinctness proportion would not by itself force the complementary critical-line population needed to contradict the bow. In the current live range this issue is secondary because (23) already makes the numerical bound vacuous.

## 4. What survives from Wang as a useful input

The negative result concerns Wang's **standalone proportion corollaries**, not the short-interval pair formula itself. Equation (9), with the extension above, remains a genuine unconditional local identity on every bow-scale interval `H=T^{vartheta+o(1)}` provided one fixes

\[
0<\lambda<\vartheta.
\tag{25}
\]

For the surviving bow range this forces `lambda<0.3283...`, well inside support one. WI-115 already gives an exact critical-lattice screening control for a support-one pair horizontal signal, and the subsequent bow findings show why universal vertical observables can be cancelled unless the actual source population is coupled into the test.

Accordingly, simply optimizing Wang's one-profile functional (10) cannot repair the bow problem: its optimal value is already (12), and its positivity threshold lies beyond the live range. A potentially nontrivial use of Wang's theorem would have to retain information discarded by (10), for example a **signed source-fixed covariance**, a coupled observable distinguishing the selected off-line bow from its complementary screening reservoir, or another arithmetic constraint on the local zero population. Such a construction would require a new proof; it is not supplied by the preprint or by this finding.

## 5. Prior-art, novelty, and evidence boundary

**Literature-backed input.** Theorem 1.1, Theorem 2.2, Proposition 2.6, Lamzouri's finite-multiset step as cited by Wang, the functional `C(f)`, its optimizer, and the numerical thresholds `theta_0,theta_d` are statements or calculations in Wang's preprint. The underlying unconditional explicit-formula method is Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh/Lamzouri prior art as identified by Wang.

**Exact Mathia deduction.** Extending the printed theorem from `H=T^theta` to `H=T^{theta+o(1)}` using (13)--(16), applying that extension to the logarithmically shortened bow span, and comparing its positivity thresholds with WI-202's exact rational cutoff are repository deductions. They should not be attributed to Wang unless a later version states them.

A bounded novelty search for arXiv:2609.07918, its exact title, and the bow-scale comparison found the fresh Wang preprint but no independent source making this specific `T^{theta+o(1)}` bow deduction. Absence of a search hit is not evidence of priority, and no priority claim is made.

This finding would fail if Wang's displayed error `O_g(H+T^lambda L^2)` concealed an `H=T^theta`-specific dependence elsewhere in the proof, if the uniform Riemann--von Mangoldt estimate (13) were unavailable on the generalized interval, or if WI-202's live bow cutoff were wrong. The first two points were checked against the proof line by line: the local estimates retain `H` explicitly, use only `1<=H<=T`, and normalize through (15). The third is an already-persisted exact rational consequence of the source-audited exponent-pair input.

## Primary sources

- Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918v1, 7 Sep 2026, https://arxiv.org/abs/2609.07918.
- Youness Lamzouri, **A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line**, arXiv:2609.02882v1, 2 Sep 2026.
- S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya, C. L. Turnage-Butterbaugh, **An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta-function**, *Acta Arithmetica* 214 (2024), 357--376; arXiv:2306.04799.

## Research consequence

The fresh short-interval Montgomery theorem reaches the **physical scale** of the surviving bows once its printed errors are read at their natural uniformity, so the logarithmic shortening of a bow is not the missing technical obstacle. But its optimized universal proportion constants turn positive too late: even `d(theta)` is vacuous before `theta=0.3466589...`, while the current count-saturating bow frontier is already below `0.3282825`.

Therefore the live RH-facing problem is sharpened rather than solved. Future work should not spend effort trying to insert Wang's standalone `c(theta)` or `d(theta)` into WI-202. The reusable new input is instead the **bow-scale pair-correlation identity with support `lambda<vartheta`**; to gain traction it must be coupled to information that distinguishes the selected off-line source from the critical/off-line reservoir capable of screening an ordinary vertical pair statistic.