# WP-022 — Prime-torus Poisson score recovers the finite Weil comb, but Fisher positivity becomes infinite at the critical boundary

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the direct product-Poisson score / Fisher-information route.

## Claim

`PL-030` identifies a canonical positive harmonic geometry of the exact Prime-Lattice exponent metric. For `sigma>0`, let

\[
P_r(\theta)=\frac{1-r^2}{1-2r\cos\theta+r^2},
\qquad r_p=p^{-\sigma},
\]

and let

\[
\nu_\sigma=\bigotimes_p P_{p^{-\sigma}}(\theta_p)\,dm(\theta_p)
\tag{1}
\]

on the infinite prime torus, where `m` is normalized Haar measure on the circle. `PL-030` proves that its Fourier coefficients are the canonical normalized GCD kernel

\[
\widehat\nu_\sigma(v(m)-v(n))
=\frac{(m,n)^{2\sigma}}{(mn)^\sigma},
\tag{2}
\]

and that `nu_sigma` is equivalent to product Haar exactly for `sigma>1/2` and singular to Haar for `0<sigma<=1/2`.

Differentiating the **log density** of this same canonical family produces a surprisingly close arithmetic object. For any finite set of primes `F`, define the honest finite-product score

\[
S_{\sigma,F}(\theta)
=\partial_\sigma
\log\prod_{p\in F}P_{p^{-\sigma}}(\theta_p).
\tag{3}
\]

Then exactly

\[
\boxed{
S_{\sigma,F}(\theta)
=
2\sum_{p\in F}(\log p)\frac{p^{-2\sigma}}{1-p^{-2\sigma}}
-
2\sum_{p\in F}\sum_{k\ge1}
(\log p)p^{-k\sigma}\cos(k\theta_p).
}
\tag{4}
\]

At the critical value `sigma=1/2`, the nonconstant Fourier coefficients in (4) are

\[
-2\frac{\log p}{p^{k/2}},
\tag{5}
\]

which are **exactly the finite-prime Weil cosine coefficients** in `WP-005`, including the sign. Thus the prime-power support and the `log p` normalization arise intrinsically from the radial derivative of the `PL-030` positive Poisson geometry; they are not inserted by a prime-power projector.

The constant term in (4) is equally forced: it is the normalization needed to make a probability score have mean zero. Writing

\[
\zeta_F(s)=\prod_{p\in F}(1-p^{-s})^{-1},
\]

it is

\[
2\sum_{p\in F}(\log p)\frac{p^{-2\sigma}}{1-p^{-2\sigma}}
=-2\frac{\zeta_F'}{\zeta_F}(2\sigma).
\tag{6}
\]

For `sigma>1/2`, the limit over all primes is the ordinary

\[
-2\frac{\zeta'}{\zeta}(2\sigma),
\tag{7}
\]

so the same local normalization carries the zeta pole at `2 sigma=1`. However this is only a zero-frequency **probability-normalization counterterm**; it is not the full polar functional of Weil's explicit formula, and there is still no archimedean Gamma/digamma sector.

The direct positivity route then fails at exactly the critical exponent. The canonical positive metric on a statistical family is its Fisher information. A single Poisson/wrapped-Cauchy factor has radial Fisher information

\[
I_r
=\mathbb E_r\!\left[(\partial_r\log P_r)^2\right]
=\frac{2}{(1-r^2)^2}.
\tag{8}
\]

By the chain rule `r_p=p^{-sigma}`,

\[
I_{\sigma,p}
=
\frac{2(\log p)^2p^{-2\sigma}}
{(1-p^{-2\sigma})^2}.
\tag{9}
\]

Independence and centering of local scores give

\[
\boxed{
I_\sigma
=2\sum_p
\frac{(\log p)^2p^{-2\sigma}}
{(1-p^{-2\sigma})^2}.
}
\tag{10}
\]

This is finite **if and only if `sigma>1/2`** and diverges for every `sigma<=1/2`. At `sigma=1/2`, the canonical positive score norm is therefore infinite. The measure-class result of `PL-030` makes the obstruction stronger: `nu_{1/2}` is singular to Haar, whereas `nu_{1/2+epsilon}` is equivalent to Haar for every `epsilon>0`; hence these two measures are mutually singular. There is no regular likelihood-ratio/Fisher tangent crossing the critical point from the side where the positive Hilbert geometry exists.

Consequently the direct route

```text
Prime-Lattice weighted exponent metric
    -> canonical product-Poisson positive geometry
    -> radial logarithmic score
    -> exact critical finite Weil coefficients
    -> Fisher / information-geometric positivity
    -> global Weil positivity
```

is closed. The score really does recover the correct finite arithmetic comb, and even forces a pole-bearing normalization term, but **the score is signed and the positive Fisher quadratic form ceases to be finite exactly when the attenuation reaches `p^{-k/2}`**. The same object also supplies no Gamma/infinite-place term. Any successful use of this Poisson geometry must therefore add a genuinely new coupled, relative, boundary, cohomological, or renormalized structure with an independent sign theorem; subtracting the divergent Fisher/self-normalization by hand would not qualify.

## 1. Exact score calculation

For `|r|<1`, the Poisson kernel has the logarithmic Fourier expansion

\[
\log P_r(\theta)
=\log(1-r^2)
+2\sum_{k\ge1}\frac{r^k}{k}\cos(k\theta).
\tag{11}
\]

With `r=p^{-sigma}` and `dr/dsigma=-(log p)r`, termwise differentiation is legitimate for each fixed prime and gives

\[
\partial_\sigma\log P_{p^{-\sigma}}(\theta)
=
2(\log p)\frac{p^{-2\sigma}}{1-p^{-2\sigma}}
-
2(\log p)\sum_{k\ge1}p^{-k\sigma}\cos(k\theta).
\tag{12}
\]

Summing (12) over a finite set `F` proves (4). There is no analytic continuation and no zero input in this calculation.

At `sigma=1/2`, (12) becomes

\[
2(\log p)\frac{p^{-1}}{1-p^{-1}}
-
2\sum_{k\ge1}\frac{\log p}{p^{k/2}}\cos(k\theta).
\tag{13}
\]

The second term is precisely the `p`-ray contribution to the finite Weil multiplier of `WP-005`. On the Prime-Lattice/Kronecker orbit `theta_p=t log p`, it is

\[
-2\sum_{k\ge1}\frac{\log p}{p^{k/2}}
\cos(t\log p^k),
\tag{14}
\]

the exact finite-place cosine comb.

The first term is not an arbitrary diagonal inserted to center the expression. The score identity

\[
\mathbb E_{\nu_{\sigma,F}} S_{\sigma,F}=0
\tag{15}
\]

forces it. Indeed the Poisson moments satisfy

\[
\mathbb E_r[\cos(k\theta)]=r^k,
\]

so the expected nonconstant part of (12) equals

\[
-2(\log p)\sum_{k\ge1}p^{-2k\sigma}
=-2(\log p)\frac{p^{-2\sigma}}{1-p^{-2\sigma}},
\]

which cancels the normalization term exactly.

This is the strongest positive feature of the route: one normalized local object produces both the prime-power hierarchy and its own compensating zero-frequency term.

## 2. The normalization term reaches the zeta pole, but not the Weil completion

For a finite set `F`, logarithmic differentiation of the partial Euler product gives

\[
-\frac{\zeta_F'}{\zeta_F}(s)
=
\sum_{p\in F}(\log p)\frac{p^{-s}}{1-p^{-s}}.
\tag{16}
\]

Putting `s=2 sigma` yields (6). If `sigma>1/2`, the all-prime series converges absolutely, so (7) is an ordinary Euler-product identity. As `sigma` decreases to `1/2`,

\[
-2\frac{\zeta'}{\zeta}(2\sigma)
\sim\frac{1}{\sigma-1/2},
\tag{17}
\]

because `zeta(s)` has its simple pole at `s=1`.

Thus the product-Poisson geometry does intrinsically know a **pole singularity at the same critical parameter** where its local score has the Weil attenuation. But (17) must not be overinterpreted. In the Weil explicit formula the polar contribution is a specific functional of the test function, and the archimedean contribution contains the Gamma/digamma factor. Equation (17) is only the scalar normalization of a probability density family. It neither reproduces the full polar test functional nor generates the Gamma sector.

Appending those terms externally would return to the kind of formula assembly excluded by the research target. A viable completion would have to force them from the same enlarged geometry and prove its sign independently.

## 3. Along the vertical prime flow the density is already normalized zeta modulus

There is a sharp novelty/circularity control in the half-plane where the Euler product converges absolutely. Set

\[
\theta_p=t\log p.
\]

For `sigma>1`,

\[
\begin{aligned}
\prod_p P_{p^{-\sigma}}(t\log p)
&=
\prod_p
\frac{1-p^{-2\sigma}}
{|1-p^{-\sigma}e^{it\log p}|^2}\\
&=
\frac{|\zeta(\sigma+it)|^2}{\zeta(2\sigma)}.
\end{aligned}
\tag{18}
\]

Therefore

\[
\partial_\sigma\log
\prod_p P_{p^{-\sigma}}(t\log p)
=
2\operatorname{Re}\frac{\zeta'}{\zeta}(\sigma+it)
-2\frac{\zeta'}{\zeta}(2\sigma).
\tag{19}
\]

This is exactly (4) after summing the Euler series. Hence in the region where the orbitwise density is an ordinary convergent product, the score mechanism is literally the logarithmic derivative of a normalized zeta modulus. It cannot be claimed as a new zeta-free explanation there.

Equation (18) is deliberately asserted only for `sigma>1`. For `1/2<sigma<=1`, `PL-030` still gives a product measure equivalent to Haar, but the distinguished one-dimensional Kronecker orbit is exceptional and the ordinary Euler product for `zeta(sigma+it)` is unavailable. The present finding does not smuggle analytic continuation into that range.

## 4. Fisher positivity has the wrong critical behavior

The positive quadratic form canonically associated with the score is Fisher information. For the single-factor family, direct integration gives

\[
I_r
=\int_0^{2\pi}
(\partial_r\log P_r(\theta))^2
P_r(\theta)\,\frac{d\theta}{2\pi}
=\frac{2}{(1-r^2)^2}.
\tag{20}
\]

This is also the standard radial component of the Fisher information matrix of the wrapped Cauchy family. Substitution `r=p^{-sigma}` gives (9).

For a finite product, score centering and independence eliminate all cross terms, so Fisher information is additive. The all-prime candidate is therefore (10). For large `p` its summand is asymptotic to

\[
2(\log p)^2p^{-2\sigma}.
\tag{21}
\]

If `sigma>1/2`, convergence follows even after majorizing the prime sum by

\[
\sum_{n\ge2}(\log n)^2n^{-2\sigma}<\infty.
\]

If `sigma=1/2`, the summand dominates a constant multiple of `(log p)^2/p`, whose sum diverges since `sum_p 1/p` diverges. For `sigma<1/2` the divergence is only stronger. This proves the exact threshold claimed after (10).

The divergence is coordinate invariant in the relevant sense. Reparameterizing the one-dimensional family can change the numerical coefficient of the Fisher metric, but the line element `I_sigma dsigma^2` is invariant. More decisively, at the boundary the measures themselves jump measure class:

\[
\nu_{1/2}\perp m_\infty,
\qquad
\nu_{1/2+\varepsilon}\sim m_\infty
\quad(\varepsilon>0),
\tag{22}
\]

by `PL-030` and Kakutani. Hence

\[
\nu_{1/2}\perp\nu_{1/2+\varepsilon}.
\tag{23}
\]

No smooth reparameterization restores a regular `L^2` score tangent across mutually singular measures while preserving a nonzero critical derivative and the coefficients (5).

## 5. Why Fisher positivity is not Weil positivity even before the divergence

For every finite `F`, the score `S_{sigma,F}` is a **signed** function with mean zero. Its nonconstant part can therefore match the signed finite Weil multiplier. Positivity appears only after taking the square/covariance that defines Fisher information:

\[
I_{\sigma,F}=\|S_{\sigma,F}\|^2_{L^2(\nu_{\sigma,F})}\ge0.
\tag{24}
\]

That operation changes the arithmetic structure. The local contribution is proportional to

\[
(\log p)^2p^{-2\sigma}(1-p^{-2\sigma})^{-2},
\]

not linearly to `(log p)p^{-k sigma}`. Thus the theorem `I>=0` does not prove the sign of the linear score functional that matches the finite Weil comb.

This distinction is analogous to, but not identical with, `WP-004`/`WP-005`: a positive object contains the exact arithmetic coefficients, yet the map that turns those coefficients into the required signed Weil observable is not positivity-preserving. Here the positive object is even more geometric — a canonical harmonic probability family — but its positive tangent norm becomes infinite at the critical parameter.

A hand-chosen preconditioner or subtraction could alter (24), but that would require a separate canonical construction and sign theorem. It is not supplied by the product-Poisson/Fisher geometry itself.

## 6. Matched free-monoid / generalized-prime control

The score mechanism is not specific to rational primes. Let a free commutative monoid have generator energies `a_j>0`, and put

\[
r_j=e^{-\sigma a_j}.
\]

The same one-circle calculation gives

\[
\partial_\sigma\log P_{e^{-\sigma a_j}}(\theta_j)
=
2a_j\frac{e^{-2\sigma a_j}}{1-e^{-2\sigma a_j}}
-
2a_j\sum_{k\ge1}e^{-k\sigma a_j}\cos(k\theta_j).
\tag{25}
\]

Thus every such weighted free monoid automatically produces generator-power coefficients

\[
a_j e^{-k\sigma a_j}
\tag{26}
\]

from its Poisson score. Choosing `a_j=log p` turns (26) into `(log p)p^{-k sigma}`; nothing in the derivation uses the functional equation, the Riemann zeros, or a property unique to the rational primes.

Likewise the Fisher metric is

\[
2\sum_j
\frac{a_j^2e^{-2\sigma a_j}}
{(1-e^{-2\sigma a_j})^2},
\tag{27}
\]

so its critical behavior is controlled by square-summability of the chosen generator radii/energies, not by RH. This is the information-geometric version of the Beurling/generalized-prime control already used in `WP-004`: exact prime-power-looking coefficients plus a half-boundary do not by themselves force the global Riemann completion or its positivity.

## 7. Prior art and novelty assessment

No novelty is claimed for any of the following ingredients:

- the normalized GCD kernel and its Poisson-polydisc representation;
- product-measure equivalence/singularity via Kakutani's theorem;
- the Poisson kernel / wrapped Cauchy family and its Fisher information;
- logarithmic differentiation of Euler products;
- the identity (18) in the absolute-convergence half-plane;
- Fisher-information positivity.

Primary audit anchors are:

- Christoph Aistleitner, Istvan Berkes, and Kristian Seip, **“GCD sums from Poisson integrals and systems of dilated functions,”** *Journal of the European Mathematical Society* 17 (2015), no. 6, 1517–1546, DOI `10.4171/JEMS/537`. They identify the normalized GCD quadratic form with a Poisson integral on a polydisc and isolate `alpha=1/2` as the delicate endpoint.
- Shizuo Kakutani, **“On equivalence of infinite product measures,”** *Annals of Mathematics* (2) 49 (1948), 214–224, DOI `10.2307/1969123`. This is the classical measure-class theorem behind the `PL-030` transition and (22).
- Naoki Otani and Takeru Matsuda, **“Wasserstein projection estimators for circular distributions,”** *Information Geometry* (published 24 August 2026), DOI `10.1007/s41884-026-00214-6`. Section 3.2 records the wrapped-Cauchy density and Fisher matrix, whose radial entry is `2/(1-rho^2)^2`, independently checking (20).

The Mathia-specific durable result is the combined bridge-and-obstruction:

1. differentiating the **canonical `PL-030` Poisson family** generates the exact finite Weil prime-power cosine coefficients at `sigma=1/2`;
2. probability normalization simultaneously forces the logarithmic-derivative counterterm (6), whose all-prime limit reaches the zeta pole;
3. the canonical positive Fisher geometry diverges exactly at the same `1/2` boundary and the measures across that boundary are mutually singular;
4. the construction supplies no Gamma/infinite-place term and survives arbitrary weighted-free-monoid controls.

So this is not a new positivity criterion for RH. It is a new no-go identification inside Mathia: the most canonical positive harmonic measure recently exposed by Prime Lattice gets closer to the finite Weil formula under differentiation than its bare GCD spectrum does, but **its own positivity is unavailable precisely at the critical score and is not the sign of the score anyway**.

## 8. Falsification tests and boundary of the obstruction

The exact part can be falsified by any failure of the following checks:

1. expand `log P_r` as in (11) and differentiate with `r=p^{-sigma}`;
2. compare the coefficient at `sigma=1/2` with the finite multiplier in `WP-005`;
3. verify the score-centering identity (15);
4. logarithmically differentiate the partial Euler product to obtain (6);
5. directly integrate the single-factor score square to obtain (20), then sum independent factors;
6. verify convergence of (10) exactly for `sigma>1/2`;
7. use the `PL-030` Kakutani dichotomy to obtain the mutual singularity (23);
8. on `sigma>1`, multiply Euler factors to obtain (18).

The obstruction is intentionally narrow. It does **not** rule out:

- using `nu_{1/2}` itself in a different, non-likelihood positive pairing;
- a canonical singular/relative renormalization if its counterterm and sign are forced independently rather than chosen to cancel (10);
- coupling the prime-torus Poisson family nontrivially to an archimedean factor before taking a quotient, boundary response, superconnection, or intersection form;
- a compression or cohomological operation whose positivity acts on a different observable than the Fisher score;
- an adelic construction in which (1) is only the finite boundary data.

But simply saying that the `PL-030` Poisson family is positive, differentiating it to see the Weil weights, and then invoking Fisher/information geometry does not solve the research question. At the critical boundary the regular positive tangent geometry has already broken, and the missing Gamma/polar structure still has to be supplied by new mathematics.
