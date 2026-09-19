# WI-354 — short-interval pair correlation has a support-localization barrier

**Status:** `LITERATURE+DERIVED + RECENT-PREPRINT-AUDITED + PRIOR-ART-REDIRECT + DECISIVE-NEGATIVE + NON-RH`

## Claim

Biao Wang's September 2026 short-interval extension of the unconditional Montgomery/Lamzouri argument gives a useful new localization theorem, but its present arithmetic error term closes a tempting RH-facing shortcut: **simply shrinking the interval in the existing pair-correlation/simple-zero argument cannot turn the positive-proportion theorem into exclusion of sparse or finite off-critical defects.**

For a fixed power interval
\[
I=(T,T+H],\qquad H=T^\theta,\qquad 0<\theta<1,
\]
Wang proves, for every fixed `0<lambda<theta` and every fixed real even `g` supported in `[-lambda,lambda]`,
\[
\sum_{\gamma,\gamma'\in I}
\widehat g\!\left(\frac{i(\rho-\rho')L}{2\pi}\right)
 w(\rho-\rho')
=
\frac{HL}{2\pi}
\left(g(0)+\int_{\mathbb R}|\alpha|g(\alpha)\,d\alpha\right)
+O_g(H+T^\lambda L^2),
\tag{1}
\]
where `L=log T` and `w(z)=4/(4-z^2)`. Relative to the main scale `HL`, the endpoint error is
\[
\boxed{
\frac{T^\lambda L^2}{HL}=T^{\lambda-\theta}L.
}
\tag{2}
\]
Thus this proof interface requires a strict fixed support-versus-localization gap
\[
\boxed{\lambda<\theta.}
\tag{3}
\]
A fixed positive Fourier-support width cannot be retained while sending the power exponent of the interval to zero through this error term. In particular, if one formally keeps the same error interface while taking a subpower interval `H=T^{o(1)}`, then for every fixed `lambda>0` the term `T^lambda L^2` dominates `HL`.

After removing the rational weight and optimizing the Lamzouri functional, Wang obtains
\[
\boxed{
\liminf_{T\to\infty}
\frac{N_0^s(T,T^\theta)}{N(T,T^\theta)}
\ge
c(\theta)
:=2-\frac\theta2-
\frac1{\sqrt2}\cot\!\left(\frac\theta{\sqrt2}\right).
}
\tag{4}
\]
The function is strictly increasing,
\[
c'(\theta)=\frac12\cot^2(\theta/\sqrt2)>0,
\tag{5}
\]
with unique zero
\[
\theta_0=0.550193964744154\ldots.
\tag{6}
\]
At the global endpoint,
\[
c(1)=
\frac32-\frac1{\sqrt2}\cot(1/\sqrt2)
=0.672500703679\ldots,
\tag{7}
\]
the Montgomery--Taylor constant. Hence **localizing the same optimized pair-correlation mechanism makes the certified proportion strictly weaker, not stronger**: for every fixed `theta<1`, `c(theta)<c(1)<1`, and for `theta<=theta_0` the simple-critical lower bound itself is nonpositive.

The exact consequence for the canonical Weil-inertia objective is that this short-interval theorem does not provide a defect-to-zero bootstrap. For fixed `theta>0`,
\[
N(T,T^\theta)=\frac{T^\theta L}{2\pi}+O(T^\theta+L),
\tag{8}
\]
so (4) is compatible with `asymp T^theta L` uncertified zeros in every interval and a fortiori with any finite or zero-density off-critical set. Shrinking the interval while retaining the same theorem cannot improve this: the optimized coefficient decreases, while the arithmetic pair-correlation input simultaneously loses Fourier support according to (2)--(3).

This is a route-specific barrier, not a theorem that short-interval information can never prove RH. A new arithmetic estimate that substantially improves the `T^lambda L^2` error, decouples support from interval length, or supplies an individual/cofinal inertia mechanism not normalized by the local zero count would evade it.

## 1. Exact recent theorem and provenance

The primary source is:

Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918v1, submitted 7 September 2026, https://arxiv.org/abs/2609.07918.

This is a recent unrefereed preprint, so its theorem is not silently promoted to peer-reviewed literature. The present audit checked the displayed statements and their proof chain directly in v1.

Wang fixes
\[
0<\lambda<\theta<1,
\qquad H=T^\theta,
\qquad L=\log T,
\tag{9}
\]
and proves (1) as Theorem 2.2. The argument localizes the Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh unconditional pair-correlation machinery. Its explicit-formula estimate culminates in Proposition 2.6,
\[
\mathcal F_I(x)=
\frac{H}{2\pi}
\left(\frac{L^2}{x^2}+\log x\right)
+O\!\left(
H+\frac{HL}{x^2}+\frac{H\sqrt L}{x}
+xL^3+\frac{L}{\sqrt x}
\right),
\tag{10}
\]
uniformly for `1<=x<=T^lambda`. Integrating this with `x=T^alpha` over test support `|alpha|<=lambda` produces exactly the error `O_g(H+T^lambda L^2)` in (1). The support restriction is therefore not merely notation in the theorem statement: it is coupled to the largest prime-side scale entering the explicit formula.

Wang then applies Lamzouri's finite-multiset inequality to the zeros in `I`. For `f=eta^2` supported in `[-lambda/2,lambda/2]`, the relevant cost is
\[
C(f)=\int f(u)^2\,du+
\iint |u-v|f(u)f(v)\,du\,dv.
\tag{11}
\]
His Proposition 4.1 identifies the unique minimizer on `[-lambda/2,lambda/2]`,
\[
f_\lambda(u)=
\frac{\cos(\sqrt2 u)}{\sqrt2\sin(\lambda/\sqrt2)}
\mathbf 1_{[-\lambda/2,\lambda/2]}(u),
\tag{12}
\]
with
\[
C_\lambda=
\frac\lambda2+
\frac1{\sqrt2}\cot(\lambda/\sqrt2).
\tag{13}
\]
For fixed `lambda<theta`, the simple-critical proportion is at least `2-C_lambda`; letting `lambda` increase to `theta` yields (4). This verifies that the same parameter that controls arithmetic support also controls the best available zero-side constant.

The paper also proves the distinct-zero bound
\[
\liminf_{T\to\infty}
\frac{N^d(T,T^\theta)}{N(T,T^\theta)}
\ge
\frac{1+c(\theta)}2,
\tag{14}
\]
whose positivity threshold is `theta_d=0.346658926139761...`. That is useful short-interval information but does not alter the RH-facing obstruction here, which concerns exclusion of every off-critical zero rather than distinctness density.

## 2. The support-localization tradeoff is the first blocker

The main term in (1) has size `HL`. Dividing the error by that scale gives
\[
O_g\!\left(\frac1L+T^{\lambda-\theta}L\right).
\tag{15}
\]
For fixed exponents, this tends to zero exactly in the regime used by the theorem, `lambda<theta`. At `lambda=theta`, the second term is `L`, already larger than the normalized main scale; for `lambda>theta` it is polynomially larger.

This makes the localization cost quantitative. If a future application needs a fixed Fourier-support window `lambda=lambda_*>0`, the present theorem can only place it inside power intervals with exponent strictly larger than `lambda_*`. Conversely, decreasing `theta` forces the admissible fixed support toward zero. No improvement of the finite-dimensional Lamzouri/inertia inequality alone changes (15), because the loss occurs before that step in the prime-side pair-correlation evaluation.

The statement about subpower intervals is intentionally limited to the **displayed error interface**, not asserted as a theorem of Wang outside his hypotheses. If one asks the same proof to handle `H=T^{o(1)}` while retaining a fixed `lambda>0`, then
\[
\frac{T^\lambda L^2}{HL}=
\frac{T^\lambda L}{H}\to\infty.
\tag{16}
\]
Therefore an extension to such intervals would need genuinely stronger arithmetic cancellation, not just bookkeeping in the existing proof.

## 3. Localization cannot bootstrap the proportion to zero defect

There are two independent failures of the naive bootstrap.

First, the optimized coefficient moves in the wrong direction. Equation (5) implies
\[
0<\theta_1<\theta_2\le1
\quad\Longrightarrow\quad
c(\theta_1)<c(\theta_2).
\tag{17}
\]
Thus replacing a global or long interval by a shorter fixed-power interval does not squeeze the exceptional fraction; it enlarges the fraction left uncertified. In particular the short-interval theorem cannot be iterated toward `c(theta)=1` as `theta` decreases.

Second, a proportion theorem normalized by (8) is intrinsically insensitive to sparse defects at every fixed positive power scale. Even if the certified coefficient were much larger but still bounded away from one, a fixed number of off-critical zeros in a window contributes `O(1)/(T^theta L)=o(1)` to the normalized statistic. To force an individual exception out merely by a fixed proportion inequality, one would have to reach windows containing only `O(1)` zeros, heuristically `H=O(1/L)`, or obtain a coefficient tending to one sufficiently fast. Wang's present interface does neither: it assumes `H=T^theta` with fixed positive `theta`, its coefficient is below the global Montgomery--Taylor constant, and (15) prohibits carrying fixed positive support down to microscopic windows using the same arithmetic estimate.

This directly interfaces with the canonical Mathia distinction between density statements and RH. A theorem giving a positive proportion, or even a fixed proportion arbitrarily close to one, does not by itself exclude a finite or zero-density off-line divisor. Locality becomes an RH mechanism only when it is strong enough to make an individual defect visible or is coupled to a separate persistence/coercivity theorem.

## 4. Relation to the current Weil-inertia frontier

This result does not weaken the existing Alpöge--Furman/Lamzouri or local Gram-defect proportion improvements. It isolates a different obstruction: **vertical localization of the arithmetic input is not presently a path from those bulk certificates to sparse-defect exclusion.**

The distinction is useful because several current WI directions operate after the pair-correlation evaluation, optimizing Gram defect, rank/trace conversion, local windows, or feature geometry. Those refinements can raise a certified proportion while staying inside support one. Wang's theorem shows that if one instead tries to obtain RH by repeatedly shrinking the height window around a hypothetical bad zero, the prime-side support budget becomes more restrictive at the same time. A stronger local matrix inequality cannot by itself pay the `T^lambda L^2` arithmetic error.

This is complementary to `WI-116`, which found a microscopic **horizontal** zero-density slope barrier in the BGSTB/Tsang tail, and to `WI-195`, which found an `L^2` norm-strength barrier for the multiplicative Gallagher representation of the distinguished bow covariance. Here the obstruction is a **vertical interval length versus Fourier-support** tradeoff inside a newly available short-interval pair-correlation theorem. None of the three barriers implies the others.

The cofinal Bombieri-inertia direction is also not closed by this result. It is precisely an example of a possible non-normalized, individual-defect mechanism that need not infer RH from a local positive proportion.

## 5. Prior art and novelty boundary

The mathematical ingredients in Wang's theorem are prior art or belong to Wang's preprint: unconditional Montgomery pair correlation from Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh, Lamzouri's conjugation-invariant finite-multiset inequality, the short-interval adaptation and its error term, and the optimization of `C(f)`. No novelty is claimed for those results.

The classical short-interval context is also already recorded by Wang: Hardy--Littlewood/Selberg/Karatsuba give critical-line zeros in power intervals, Steuding gives simple critical zeros for `H>=T^0.552`, and Levinson-type mollifier methods give different longer-interval proportion results. Wang's threshold `theta_0=0.550193...` slightly shortens the range for an explicit positive simple-critical proportion within this pair-correlation method; that is his result, not Mathia's.

The durable Mathia delta is the interface audit against the current research mandate. Equations (2), (5), and (8) together show that the newly available localization theorem does **not** supply the missing defect-to-zero bridge: shorter intervals simultaneously lose Fourier support and weaken the optimized proportion, while every fixed-power window remains macroscopically populated. A repository audit found no preceding `WI` finding recording arXiv:2609.07918 or this support-localization consequence. This negative repository search is not a priority claim.

## 6. Boundary conditions and falsification

The barrier is deliberately narrow.

It does **not** prove that pair correlation in sufficiently short intervals is impossible, that support `lambda>=theta` is mathematically forbidden, or that no local zeta statistic can detect an isolated off-line zero. It proves only that Wang's current theorem and its displayed prime-side error do not provide those conclusions.

A material way to evade the obstruction would be any one of the following: an unconditional short-interval pair-correlation formula whose error remains `o(HL)` for a fixed positive support as `H` becomes subpower or microscopic; a support-expanding theorem with a quantitatively improving zero-side constant; a signed/arithmetic observable that detects one off-line block without normalization by `N(T,H)`; or a cofinal inertia/coercivity statement that turns a sparse defect into a uniformly persistent negative direction.

The claim should be withdrawn or narrowed if Wang's stated error has been misread, if its main scale is not `HL` in the application used to derive (4), or if an already established theorem supplies the same pair-correlation input on substantially shorter intervals with fixed positive support and adequate error. None of those was found in the present bounded audit.

## Research consequence

The new short-interval theorem is useful evidence, but not the missing RH bootstrap. It closes the cheap strategy
\[
\text{global pair-correlation proportion}
\longrightarrow
\text{same theorem on ever shorter windows}
\longrightarrow
\text{individual-defect exclusion}
\]
within the current arithmetic interface.

For the Weil-inertia program, further work on sparse defects must therefore obtain genuinely stronger short-interval arithmetic, retain a source-specific signed covariance such as the distinguished bow target, or use a non-normalized cofinal negative-index mechanism. Merely localizing the existing Montgomery/Lamzouri proportion argument cannot reach the canonical objective.