# WI-291 — Heath-Brown large-gap sparsity confines complete screening to rare upper deserts

## Status

- **Evidence:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + PRIOR-ART-AUDITED`.
- **Scope:** the one-signed, completely screened, symmetric two-island branch of `WI-288`--`WI-290`. This finding addresses only the unresolved `k=1` ordinary-prime part of the Lambert screening condition and its incidence with the composite-safe residual.
- **Result:** Roger Heath-Brown's published large-prime-gap theorem implies that, on a dyadic shell `[X,2X]`, the set of centers that can satisfy the ordinary-prime Lambert screening threshold has total measure

  \[
  \boxed{|\mathcal A_c(X)|\ll_{c,\varepsilon}X^{3/5+\varepsilon}}
  \]

  and is contained in at most

  \[
  \boxed{K_c(X)\ll_{c,\varepsilon}\frac{X^{1/10+\varepsilon}}{\log X}}
  \]

  ordinary-prime gap hosts. In separation coordinates `Delta=log x`, its dyadic measure is `O(X^{-2/5+epsilon})`, hence summable over dyadic shells for every fixed `epsilon<2/5`.
- **Consequence:** `WI-290` proves that the lower-scale composite-safe residual already has at least `X^{3/8-o(1)}` positive-length components using the published prime-gap second moment. The present upper-scale estimate shows that raw abundance of those components cannot by itself close the screening problem: a successful argument must localize or couple them to the far rarer `X^{1/10+o(1)}` family of upper ordinary-prime deserts.
- **What it does not claim:** no fully screened center is ruled out; no cross-scale independence, correlation, intersection, or avoidance theorem is proved; no simple-critical-zero proportion is improved; no statement is made for many-component, sign-changing, or incomplete-screening topologies; and finite total measure in `Delta` does not imply finitely many candidate separations.
- **Novelty boundary:** Heath-Brown's large-gap estimate is prior art, while the Lambert screening threshold comes from `WI-288`--`WI-289`. The line-local deduction is their specialization to the screening geometry, the resulting measure/host-count bounds, and the comparison with `WI-290`. Targeted prior-art searches did not locate this exact screening consequence; search absence is audit context only, not a priority claim.

## Claim

Fix `c>0`. With the notation of `WI-289`, write

\[
D_c(x)=\frac{W(c\sqrt x)}{\sqrt x}
\]

and let `delta_p(x)` denote the nearest ordinary-prime logarithmic distance appearing in the `k=1` factor of the exact prime-power decomposition. Define

\[
\mathcal A_c(X)
:=\{x\in[X,2X]:\delta_p(x)\ge D_c(x)\}.
\tag{1}
\]

Then for every `epsilon>0`,

\[
\boxed{|\mathcal A_c(X)|\ll_{c,\varepsilon}X^{3/5+\varepsilon}.}
\tag{2}
\]

Moreover, if `K_c(X)` is the number of ordinary-prime gaps that meet `\mathcal A_c(X)`, then

\[
\boxed{K_c(X)\ll_{c,\varepsilon}
\frac{X^{1/10+\varepsilon}}{\log X}.}
\tag{3}
\]

Every completely screened symmetric two-island center from `WI-288` lies in

\[
\mathcal A_c(X)\cap R_c(X),
\tag{4}
\]

where `R_c(X)` is the composite-safe residual of `WI-289`--`WI-290`. Thus (2)--(3) apply a fortiori to the full screening candidate set.

## 1. Heath-Brown's published large-gap theorem

Roger Heath-Brown, *The Differences Between Consecutive Primes, V*, International Mathematics Research Notices 2021, no. 22, 17514--17562, DOI `10.1093/imrn/rnz295`, proves in Theorem 1 that for every fixed `epsilon>0`,

\[
\boxed{
\sum_{\substack{p_n\le Y\\
p_{n+1}-p_n\ge\sqrt{p_n}}}
(p_{n+1}-p_n)
\ll_\varepsilon Y^{3/5+\varepsilon}.}
\tag{5}
\]

The paper was published online in 2019 and in the 2021 journal issue; arXiv:1906.09555 is the corresponding preprint. Theorem 2 gives a stronger exceptional-set formulation from which (5) is deduced. Only the published Theorem 1 is needed here.

Equation (5) controls the **total length** of all square-root-large prime gaps, not merely their number. That is exactly the form needed for the screening-center measure estimate below.

## 2. The Lambert threshold forces a square-root-large upper prime gap

Take `x in A_c(X)` and let

\[
p_-<x<p_+
\]

be the neighboring ordinary primes. The definition of `delta_p` and (1) give

\[
\log(x/p_-)\ge D_c(x),
\qquad
\log(p_+/x)\ge D_c(x).
\tag{6}
\]

Hence

\[
p_+-p_-
\ge x\left(e^{D_c(x)}-e^{-D_c(x)}\right)
\ge 2xD_c(x),
\tag{7}
\]

because `sinh u>=u` for `u>=0`. Therefore

\[
p_+-p_-
\ge 2\sqrt x\,W(c\sqrt x).
\tag{8}
\]

For fixed `c>0`, `W(c sqrt(x))=\tfrac12\log x-\log\log x+O_c(1)`. Uniformly for `x in [X,2X]`, (8) gives

\[
p_+-p_-\gg_c\sqrt X\log X.
\tag{9}
\]

In particular, for all sufficiently large `X`,

\[
p_+-p_-\ge\sqrt{p_-},
\tag{10}
\]

since `p_-<2X` and the right side of (9) exceeds `sqrt(2X)` by a logarithmic factor. Thus every gap that hosts a center in `A_c(X)` is among the gaps counted by Heath-Brown's sum (5), with left endpoint below `2X`.

No short-interval prime theorem is used here. The screening threshold itself supplies the much stronger gap length (9).

## 3. Measure and host-count bounds

Distinct prime gaps are disjoint. Since `A_c(X)` is contained in the union of the qualifying host gaps, (5) with `Y=2X` and (10) give

\[
|\mathcal A_c(X)|
\le
\sum_{\substack{p_n\le2X\\g_n\ge\sqrt{p_n}}}g_n
\ll_\varepsilon X^{3/5+\varepsilon},
\tag{11}
\]

which proves (2). A gap crossing the boundary of `[X,2X]` causes no difficulty: its left endpoint is still at most `2X`, so it is already included in the same sum.

Every host gap meeting `A_c(X)` also has, by (9),

\[
g_n\gg_c\sqrt X\log X.
\tag{12}
\]

Therefore

\[
K_c(X)\sqrt X\log X
\ll_c
\sum_{\substack{p_n\le2X\\g_n\ge\sqrt{p_n}}}g_n
\ll_\varepsilon X^{3/5+\varepsilon},
\tag{13}
\]

and (3) follows from `3/5-1/2=1/10`.

## 4. Separation-coordinate sparsity

Put `Delta=log x`. On one dyadic shell,

\[
\operatorname{meas}_\Delta
\{\Delta:e^\Delta\in\mathcal A_c(X)\}
=
\int_{\mathcal A_c(X)}\frac{dx}{x}
\le
\frac{|\mathcal A_c(X)|}{X}
\ll_\varepsilon X^{-2/5+\varepsilon}.
\tag{14}
\]

For any fixed `epsilon<2/5`, summing (14) over `X=2^jX_0` converges and gives a tail bound

\[
\operatorname{meas}_\Delta
\{\Delta\ge\log X_0:e^\Delta\in\mathcal A_c(e^\Delta)\}
\ll_{c,\varepsilon}X_0^{-2/5+\varepsilon}.
\tag{15}
\]

This is a strong rarity statement in the natural separation coordinate. It is not a discreteness theorem: a set of finite measure may contain infinitely many points and intervals.

## 5. Comparison with the lower-scale residual from WI-290

`WI-290` proves, from the published Peck--Maynard mean-square prime-gap exponent `theta=1/4`, that the composite-safe residual `R_c(X)` has at least

\[
M_c(X)
\gg_{c,\varepsilon}
X^{3/8-\varepsilon}
\left(\frac{\log\log X}{\log X}\right)^2
\tag{16}
\]

positive-length components. The present result says that the ordinary-prime part of complete screening can occur inside only

\[
K_c(X)\ll_{c,\varepsilon}X^{1/10+\varepsilon}/\log X
\tag{17}
\]

upper prime-gap hosts.

The exponents `3/8` and `1/10` do **not** yield an intersection by pigeonhole: (16) is a global count of lower-scale residual components, while (17) identifies a rare and arithmetically selected family of upper-scale host intervals. All residual components could, on present information, avoid those hosts. What the exponent mismatch does prove is a methodological barrier: increasing a global count of residual windows, without any localization to the upper deserts, cannot resolve the remaining incidence question.

Thus the live bridge after `WI-290` is more precise than “prove there are many safe windows.” One needs arithmetic information that couples the prime process near `sqrt x` (and the thinner higher-power exclusions) to the exceptional ordinary-prime gaps near `x` selected by (8).

## 6. Prior-art audit and boundaries

Heath-Brown's Theorem 1 is classical prior art for the upper-gap sparsity input. `WI-288` gives the exact two-island prime-power screening condition and `WI-289` decomposes it root by root, identifying the `k=1` ordinary-prime desert and `k=2` prime-square layer. `WI-290` supplies the independent lower bound on the number of composite-safe components.

Searches around large prime gaps, square-root-large gap exceptional sets, prime powers inside large gaps, and prime-gap moment estimates did not locate a theorem coupling a Heath-Brown-large gap near `x` to the prime-square-scale residual near `sqrt x`. Accordingly, this finding does not claim such a coupling or priority for one. Its durable content is the exact specialization (6)--(17), which sharply identifies how rare the upper hosts are relative to the lower-scale reservoir.

The argument also does not improve Heath-Brown's exponent, prove that any eligible upper gap exists at arbitrarily large scales, or say that an eligible gap intersects `R_c(X)`. Those are genuinely stronger arithmetic questions.

## Consequence for the research line

The two-island complete-screening obstruction has now been split into two quantitatively very different pieces. The composite-prime-power side leaves a large, polynomially fragmented reservoir (`WI-289`--`WI-290`), while the ordinary-prime Lambert side can live only in a total upper-gap length `O(X^{3/5+epsilon})` and at most `X^{1/10+epsilon}/log X` hosts.

This closes the **raw-abundance-only** route: merely proving more composite-safe components cannot force complete-screening failure. Any decisive next step must use a cross-scale incidence theorem, a conditional distribution of primes inside the rare Heath-Brown gap family, or a different spectral/topological mechanism that bypasses complete screening altogether.
