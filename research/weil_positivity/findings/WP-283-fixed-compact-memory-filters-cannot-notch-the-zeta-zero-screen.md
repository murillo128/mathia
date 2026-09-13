---
id: WP-283
title: Fixed compact-memory filters cannot notch the critical zeta-zero screen
branch: weil_positivity
status: supported
kind: compact-memory-zero-density-obstruction
claim_strength: exact favorable-RH no-go for every fixed bounded scalar finite-memory logarithmic-translation-invariant linear response preserving the constant mode
created: 2026-09-13
related: [WP-279, WP-280, WP-281, WP-282]
prior_art:
  - classical Paley-Wiener theory for Fourier transforms of compactly supported measures
  - classical Jensen zero-counting for entire functions of exponential type
  - B. Ya. Levin, Distribution of Zeros of Entire Functions, AMS Translations of Mathematical Monographs 5
  - Levent Alpöge and Ralph Furman, More than two thirds of the zeta zeros are simple and on the critical line, arXiv:2608.13637 (2026)
---

# WP-283 — Fixed compact-memory filters cannot notch the critical zeta-zero screen

## Claim

`WP-281` proves that every fixed finite-state logarithmic-scale response fails to extract the Gamma-center constant from the critical Chebyshev residual because a rational transfer function cannot vanish at all nontrivial-zero frequencies. `WP-282` then closes a genuinely infinite-dimensional positive relaxation class: completely monotone/Stieltjes responses cannot notch even one finite nonzero frequency.

A natural gap remains between those classes. A fixed **finite-memory** response can be infinite-dimensional and strongly oscillatory. Its transfer function need not be rational or Stieltjes and can have infinitely many real zeros. Delay lines, distributed finite windows, signed FIR kernels, and finite signed/complex combinations of point delays all live in this class. Nevertheless the class still cannot remove the zeta-zero screen.

Assume RH only as the same favorable control used in `WP-281`. For fixed `a>0`, write its regularized critical source as

\[
Y_a(E)=C_\Gamma+A_a(E)+r_a(E),\qquad r_a(E)\to0,
\tag{1}
\]

with

\[
A_a(E)
=-\sum_{\rho=1/2+i\gamma}
\frac{a}{(i\gamma)(a+i\gamma)}e^{i\gamma E},
\tag{2}
\]

an absolutely and uniformly convergent nonconstant Bohr almost-periodic field.

Let `mu` be any fixed finite complex Borel measure supported in `[0,L]`, and define the bounded finite-memory translation-invariant readout

\[
(\mathcal F_\mu Y)(E)
:=\int_{[0,L]}Y(E-t)\,d\mu(t).
\tag{3}
\]

Its transfer function is

\[
H_\mu(z)=\int_{[0,L]}e^{-izt}\,d\mu(t).
\tag{4}
\]

Suppose `H_mu(0)=mu([0,L]) != 0`, so the constant Gamma mode is retained. Then `H_mu` is a nonzero entire function of exponential type at most `L`, bounded on the real axis, and its zero count satisfies

\[
n_{H_\mu}(T)=O_\mu(T).
\tag{5}
\]

By contrast, Alpöge--Furman prove unconditionally that a positive proportion of the nontrivial zeta zeros are simple and lie on the critical line; combined with the Riemann--von Mangoldt law, the number of their distinct positive ordinates below `T` is

\[
\gg T\log T.
\tag{6}
\]

Under the favorable RH control these ordinates are frequencies occurring with nonzero Fourier--Bohr coefficient in (2). Therefore no fixed `H_mu` can vanish at all of them. At least one, in fact infinitely many, zero frequencies survive the filter. The filtered almost-periodic part is consequently nonconstant, while the filtered remainder still tends to zero. Hence

\[
\boxed{
H_\mu(0)\ne0
\quad\Longrightarrow\quad
\lim_{E\to\infty}(\mathcal F_\mu Y_a)(E)
\text{ does not exist.}
}
\tag{7}
\]

Thus **every fixed bounded finite-memory scalar linear boundary response fails to extract the Gamma-center mode from the critical arithmetic source, even when signed or oscillatory kernels and infinitely many transfer zeros are allowed.**

For normalized positive windows there is a quantitative version. If `mu_T` is a probability measure supported in `[0,L_T]` and its transfer vanishes at every simple critical-line zero ordinate `gamma<=T`, Jensen's formula forces

\[
L_T \gg \log T.
\tag{8}
\]

So even a cutoff-dependent positive FIR family can track the growing zero screen only by letting its logarithmic-scale memory horizon diverge at least logarithmically. This is no longer one fixed local geometry; it crosses directly into the growing-window/nonlocal regime already separated from local extraction by `WP-280`.

**Classification:** `EXACT-DERIVED + DECISIVE-NEGATIVE-FOR-FIXED-COMPACT-MEMORY-LINEAR-EXTRACTION + FAVORABLE-RH-MATCHED-CONTROL + PALEY-WIENER-JENSEN-ZERO-DENSITY + CURRENT-DISTINCT-FREQUENCY-INPUT + PRIOR-ART-CLASSICALIZED-INGREDIENTS + NOT-A-WEIL-POSITIVITY-PROOF`.

## 1. The source after the canonical one-state regularizer

The starting point is exactly the favorable-RH representation already derived in `WP-281`. With

\[
G(E)=\psi_{1/2}(e^E)-2e^{E/2}
\tag{9}
\]

and

\[
Y_a'(E)+aY_a(E)=aG(E),
\tag{10}
\]

the weighted explicit formula gives (1)--(2). The coefficient at a distinct zero ordinate `gamma` is nonzero; if a zero has multiplicity greater than one, that multiplicity simply multiplies the coefficient. Moreover

\[
\sum_\rho\frac1{1+\gamma^2}<\infty,
\tag{11}
\]

so (2) converges absolutely and uniformly.

The one-state regularizer is important only for making the zero field an ordinary bounded almost-periodic signal on which a bounded finite-window functional is unproblematic. It is not the candidate extraction mechanism. The candidate is the additional finite-memory response (3), which is much broader than the rational finite-state class excluded in `WP-281`.

A bounded scalar functional of a fixed continuous history window `C([0,L])` is represented by a finite complex Borel measure by the Riesz representation theorem. Therefore (3) is the natural general form of a bounded scalar finite-memory linear time-invariant readout. It includes absolutely continuous kernels, singular measures, point delays, finite-tap filters, and arbitrary fixed signed or oscillatory mixtures of those.

## 2. Compact memory gives an entire transfer of finite exponential type

For `z=x+iy`, (4) is entire and obeys the direct bound

\[
|H_\mu(z)|
\le \|\mu\|_{TV}\,e^{L|y|}.
\tag{12}
\]

No positivity or passivity is used. This is the elementary compact-measure case of Paley--Wiener theory.

Assume `H_mu(0) != 0`. Jensen's formula for the zeros `zeta_j` of `H_mu` in the disk `|z|<R` gives

\[
\sum_{|\zeta_j|<R}\log\frac{R}{|\zeta_j|}
=
\frac1{2\pi}\int_0^{2\pi}
\log|H_\mu(Re^{i\theta})|\,d\theta
-\log|H_\mu(0)|.
\tag{13}
\]

Using (12) and

\[
\frac1{2\pi}\int_0^{2\pi}|\sin\theta|\,d\theta
=\frac2\pi,
\tag{14}
\]

one obtains

\[
n_{H_\mu}(R/2)\log2
\le
\frac{2LR}{\pi}
+\log\frac{\|\mu\|_{TV}}{|H_\mu(0)|}.
\tag{15}
\]

Hence

\[
n_{H_\mu}(T)
\le
\frac{4LT}{\pi\log2}+O_\mu(1).
\tag{16}
\]

This is the only entire-function input needed. One does not need a delicate density theorem for Cartwright or Bernstein spaces: compact memory itself gives a linear zero budget by the elementary Jensen estimate.

The estimate also exposes why allowing infinitely many transfer zeros does not help. A finite-memory filter may indeed have infinitely many notches -- for example a two-delay filter already gives a periodic zero set -- but those zeros have at most linear density. The zeta-zero screen is asymptotically much denser.

## 3. The zeta-zero frequencies have superlinear density

Let `N(T)` denote the number of nontrivial zeta zeros with `0<Im rho<=T`, counted with multiplicity. The Riemann--von Mangoldt formula gives

\[
N(T)
=\frac{T}{2\pi}\log\frac{T}{2\pi}
-\frac{T}{2\pi}+O(\log T).
\tag{17}
\]

For the present argument one needs not merely infinitely many ordinates but `gg T log T` **distinct** ordinates. This is now available with substantial room. Alpöge and Furman prove unconditionally that at least two thirds of the nontrivial zeros, counted with multiplicity, are simple and lie on the critical line; their optimized Montgomery--Taylor window raises the constant to about `0.6725`. Every simple critical-line zero contributes a distinct positive ordinate. Consequently, for some absolute `c>0` and all sufficiently large `T`, there are at least

\[
cT\log T
\tag{18}
\]

distinct positive critical-line zero ordinates below `T`.

The new zero-density theorem is not being used as evidence for RH. It is only a frequency-counting input. The extraction no-go itself grants RH because that is the most favorable setting for the source decomposition (1): under RH all nontrivial-zero exponents in the critical residual become purely oscillatory.

If convergence of (3) were possible, the filtered almost-periodic part would have to be constant. Mode-by-mode application is justified by uniform absolute convergence and yields

\[
\mathcal F_\mu A_a(E)
=-\sum_\rho
\frac{aH_\mu(\gamma)}{(i\gamma)(a+i\gamma)}e^{i\gamma E},
\tag{19}
\]

with the harmless convention that equal ordinates are combined. A constant almost-periodic function has zero Fourier--Bohr coefficients at every nonzero frequency, hence convergence would require

\[
H_\mu(\gamma)=0
\tag{20}
\]

for every simple critical-line zero ordinate `gamma`.

But (16) allows only `O(T)` zeros of `H_mu` in `[-T,T]`, while (18) requires `gg T log T` real zeros. This contradiction proves that (19) is nonconstant.

Finally, because `r_a(E)->0` and `mu` has fixed compact support and finite total variation,

\[
\left|\int_{[0,L]}r_a(E-t)\,d\mu(t)\right|
\le
\|\mu\|_{TV}
\sup_{0\le t\le L}|r_a(E-t)|
\longrightarrow0.
\tag{21}
\]

The constant input contributes `C_Gamma H_mu(0)`. A nonconstant Bohr almost-periodic function cannot have a limit at `+infinity`, exactly as in `WP-281`. Therefore the complete filtered signal cannot converge, proving (7).

## 4. Quantitative memory lower bound for positive moving windows

The fixed-filter theorem is enough for the category obstruction, but the same estimate quantifies what a cutoff-dependent positive escape must pay.

Let `mu_T` be a probability measure on `[0,L_T]`. Then `H_T(0)=1` and `||mu_T||_TV=1`, so (16) has no amplitude-condition term:

\[
n_{H_T}(T)
\le\frac{4L_TT}{\pi\log2}.
\tag{22}
\]

If `H_T` is required to vanish at all simple critical-line zero ordinates below `T`, Alpöge--Furman plus (17) gives

\[
n_{H_T}(T)
\ge \left(\frac{1}{3\pi}+o(1)\right)T\log T
\tag{23}
\]

using only their clean two-thirds bound. Combining (22)--(23),

\[
L_T
\ge\left(\frac{\log2}{12}+o(1)\right)\log T.
\tag{24}
\]

Using their optimized `0.6725` constant improves the numerical coefficient slightly; the asymptotic point is the logarithmic divergence, not that constant.

Thus a family of positive finite-window averages can gain enough notch density only by increasing its logarithmic-scale memory without bound. If signed/complex filters are allowed with growing total variation, Jensen's estimate also permits zero budget to be purchased through the term `log ||mu_T||_TV`; that is a different instability/target-coding cost rather than a fixed bounded geometry. Neither possibility contradicts the fixed-filter theorem.

This control is useful because it distinguishes a genuine finite-memory no-go from the tautology that an arbitrarily redesigned filter can interpolate a finite target set. A target-dependent family may always add more delay length or more variation as the zero cutoff increases. Such a family is not one source-fixed local completion.

## 5. Adversarial controls and exact boundary

Several apparent counterexamples do not attack the claim.

A compactly supported filter can have infinitely many zeros. The theorem does not deny that; it uses their **linear** Jensen density. Periodic delay notches therefore remain admissible controls and still lose against the `T log T` zeta frequency count.

A transfer with unbounded memory can have a much denser zero divisor. The argument does not cover it because compact support, hence finite exponential type, is the load-bearing hypothesis. This is the intended boundary. `WP-282` already closes the positive completely-monotone infinite-memory subclass, but a genuinely oscillatory infinite-memory/non-Stieltjes response remains open.

A growing support length `L_T` also escapes the fixed theorem. Equation (24) shows that this escape is necessarily scale-nonlocal: to suppress more and more zero modes, the observation window must grow at least logarithmically with the frequency cutoff even for normalized positive kernels. `WP-280` is precisely a growing-window construction of a different kind, and its exact successful limit is RH-equivalent by Suzuki. The present theorem does not reclassify every growing-window response as Suzuki's criterion.

A filter explicitly manufactured from the zeta zero divisor can of course annihilate the frequencies. That is target insertion and is excluded by the research mandate independently of the analytic argument. The value of (5)--(7) is stronger: even before applying the source-selection gate, **no fixed compact-memory transfer has enough zero density to do the job at all**.

Nonlinear and pre-scalarization couplings remain outside scope. A nonlinear energy can mix frequencies rather than notch them, and a finite--archimedean operator coupling formed before the source is reduced to (1) need not be represented by a scalar convolution transfer. Those routes require independent sign and source-forcing audits.

## 6. Prior-art and novelty audit

The analytic ingredients are classical except for the strength of the current distinct-frequency input. Fourier transforms of compactly supported finite measures are entire functions of exponential type; Jensen's formula gives the linear zero-count estimate used above. This belongs to standard Paley--Wiener/entire-function theory, classically treated for example by Levin. No novelty is claimed for (12)--(16).

The zeta-frequency count is also external number theory. Alpöge--Furman's 2026 theorem supplies an unconditional positive-proportion set of simple critical-line zeros, and the classical Riemann--von Mangoldt formula turns it into the `T log T` density needed here. No novelty is claimed for their result or for zero counting.

A targeted prior-art search for combinations of zeta ordinates with Bernstein/Cartwright or compact-support Fourier zero sets found the surrounding classical uniqueness/zero-distribution theory but no need to invoke a zeta-specific theorem: the contradiction follows immediately from Jensen plus the now-available simple-zero density. The Mathia-specific content is therefore the **frontier reduction**, not a new theorem in complex analysis: once `WP-281` turns the critical residual into an absolutely convergent zero-frequency field, every fixed bounded finite-memory extraction mechanism is forced into an entire transfer whose notch budget is only linear.

This finding should be read as a decisive category boundary and prior-art-classicalized obstruction. It does not prove RH, Weil positivity, or a new zero-density theorem.

## Consequence for `weil_positivity`

The post-scalarization extraction frontier is now split more sharply. `WP-281` excludes rational finite-state filters. `WP-282` excludes completely monotone positive infinite-dimensional relaxations. The present result excludes the orthogonal-looking class that those two leave open: **arbitrary fixed bounded compact-memory convolution responses, including signed and oscillatory FIR/delay geometries**.

A surviving scalar linear route therefore needs genuinely unbounded memory and a non-Stieltjes oscillatory transfer derived independently from source geometry; if it instead uses a cutoff-dependent finite window, its horizon must grow and it becomes scale-nonlocal. Alternatively the research must move earlier in the construction, before the critical source is scalarized into the almost-periodic field (1), where finite--archimedean incidence, operator-category changes, or cohomological pairings may still alter the sign mechanism rather than merely filter zero frequencies.
