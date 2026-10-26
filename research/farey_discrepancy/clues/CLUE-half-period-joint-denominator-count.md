---
id: CLUE-farey-discrepancy-half-period-joint-denominator-count
type: research-clue
status: accepted
origin: research-watch
target_line: farey_discrepancy
based_on:
  - research/farey_discrepancy/clues/CLUE-half-period-gap-decorrelation.md
  - research/farey_discrepancy/findings/FD-346-classical-gap-correlations-separate-high-band-farey-transport.md
  - research/farey_discrepancy/findings/FD-347-finite-half-period-tests-miss-reflected-gap-sector-bias.md
  - research/visual_exploration/visualizations/farey-half-period-denominator-shells.md
---

# Can joint small-denominator counts control half-period Farey gap products?

## Observation

The accepted [half-period correlation question](CLUE-half-period-gap-decorrelation.md)
asks for every fixed offset, not a finite set. FD-347's reflected-rotation
control shows why the latter is insufficient. The present proposal is a
narrower **uniform denominator-count lemma** for the genuine Farey word,
with a proved elementary sufficient implication to that parent question.
It does not replace the parent clue or its disposition.

The [denominator-shell view](../../visual_exploration/visualizations/farey-half-period-denominator-shells.md)
resolves each positive gap product by its two minimum denominators.
Identical repetition aligns each shell with itself, while the genuine
half-period pairing moves much of that weight off the diagonal. At prime
order 2039, the genuine and self-pairing totals on the squared-order
scale are 5.898335775 and 11.259599091. Off-diagonal suppression alone is
not sufficient: the proposed test counts all threshold rectangles.

## Research question

For prime order \(p\), let \(q_0,\ldots,q_N\) be the denominator list
of \(0=x_0<\cdots<x_N=1\), where \(N=\sum_{q\le p}\varphi(q)=2h\).
Write \(g_k=1/(q_kq_{k+1})\), \(s_k=\min(q_k,q_{k+1})\), periodically
extended with period \(N\). For every fixed integer \(r\), does a
constant \(K_r\), independent of \(p,A,B\), satisfy

\[
C_{p,r}(A,B):=\#\{0\le k<N:s_k\le A,\ s_{k+h+r}\le B\}
\le K_r\left(\frac{A^2B^2}{p^2}+\min(A,B)\right)
\quad(1\le A,B\le p)? \tag{D}
\]

Thresholds are integers. The linear overlap allowance is a proposed
hypothesis, not a derived mixing error. If (D) fails, a weaker useful
target is \(K^{\mathrm{dyad}}_{p,r}=o(\log p)\), where this quantity
is the maximum ratio in (D) on thresholds
\(\{1,2,4,\ldots,2^{\lfloor\log_2p\rfloor},p\}\).

## Why it may matter

The gap/denominator dictionary converts this count estimate into the
parent correlation bound. Adjacent denominators sum to more than \(p\),
so their maximum lies in \((p/2,p]\), and
\(1/s_k\le p g_k<2/s_k\). In the shells
\(2^a\le s_k<2^{a+1}\), \(2^b\le s_{k+h+r}<2^{b+1}\), the
contribution to \(p^2 S_{h+r}\) is at most

\[
4\,2^{-a-b}
C_{p,r}(\min(p,2^{a+1}),\min(p,2^{b+1})).
\]

Summing (D) therefore gives

\[
p^2S_{h+r}\ll K_r\left[
 p^{-2}\Big(\sum_{0\le a\le\log_2p}2^a\Big)^2
 +\sum_{a,b\ge0}2^{-\max(a,b)}\right]\ll K_r, \tag{E}
\]

since the first geometric sum is below \(2p\) and the double sum is
six. Thus (D) implies \(S_{h+r}=O_r(p^{-2})\). The same argument
with \(K^{\mathrm{dyad}}_{p,r}\) implies
\(S_{h+r}=o(\log p/p^2)\) under the weaker sublogarithmic target.
These are sufficient criteria, not necessary ones.

The parent clue's Fourier bridge would then settle sector equipartition
if the hypothesis holds for **every** fixed offset. FD-346 already
settles projected-transport nonconvergence; this would refine the
residual source-sector split only. No low-frequency or RH bound follows.

## Decisive test

Prove (D) from genuine denominator adjacency and rank arithmetic, or
exhibit a family for which its ratio is unbounded. A failure at one
provisionally chosen finite constant is not an asymptotic refutation.
If (D) fails, check the weaker sublogarithmic maximum before abandoning
this sufficient route; failure of either count criterion does not by
itself refute the original correlation question.

The finite view measures only seven prime orders and offsets
\(0,1,2,4,8,12\). For \(r=0\), the dyadic maximum reaches 4.517955
at \(p=1021\), with thresholds \((64,128)\), and is 4.217537 at
\(p=2039\). There is no claimed uniform constant or growth rate.
For every odd prime, four endpoint/half-point directed pairs contribute
exactly two to \(p^2 S_h\), so bounded cusp effects must be allowed.
FD-347 forbids interpreting a fixed finite offset panel as sufficient
for sector equipartition; any theorem here must retain the all-fixed-offset
quantifier or supply a separately proved reduction.

Audit the dynamical route against its actual measures and observables.
[Athreya–Cheung, Section 1.3.3](https://arxiv.org/pdf/1206.6597)
identifies normalized successive denominators as a periodic orbit of
the BCZ map, with roof \(R(a,b)=1/(ab)\).
[Artiles–Best–Bordignon, Theorem 1.1](https://arxiv.org/html/2610.07347v1)
proves strong mixing for normalized Lebesgue measure. Transfer to the
changing periodic-orbit measures, uniformity in shrinking denominator
thresholds, and control of the unbounded roof products are additional
requirements. Qualitative mixing with fixed sets is not (D).
[Dong–Nguyen–Nguyen–Zaharescu, Theorem 2.3](https://arxiv.org/html/2606.12907v1)
retains lag-dependent hypotheses that exclude substitution of \(h+r\).
Targeted orientation by BCZ mixing, Farey denominator correlations and
long-rank gap counts did not supply (D); a full novelty/proof audit remains
part of any promotion.

## Evidence boundary

(D) and its sublogarithmic variant are unproved. The chosen count
normalization is an exploratory sufficient-condition design, not a
calibrated null, an estimated expectation, or an independently confirmed
asymptotic. The paired visualization records exact finite audits and
numerical construction controls; all displayed data informed exploration.

The dyadic implication (E) is elementary conditional motivation, not new
arithmetic evidence. The proposal is distinct from the parent correlation
question because its specific uniform count bound is stronger and can
fail while the parent remains true. Neither count bound, a sector law,
nor an RH improvement is established. The exact finite restriction in
the research disposition is a separate result, not a proof of (D).

## Research disposition

The uniform count direction is accepted for investigation, not established.
[FD-348](../findings/FD-348-small-denominator-half-period-pairs-are-exact-rational-translates.md)
reconstructs an exact arithmetic restriction: if
`2AB(2/p+(|r|+1)/N)<1`, every counted gap pair touches vertices differing
by exactly one half. Their reduced denominators have ratio `1/2`, `1`,
or `2`. The count is exactly a triangularly weighted count of rank defects
`delta_p(u)` in `{r-1,r,r+1}`, with `delta_p` given by a periodic Mertens
filter. Thus the small-product part of (D) requires a linear bound on
these coincidences; at `A=B=t`, `t^2<=p/8`, the eligible rational
population before imposing the rank condition is quadratic in `t`.

The dyadic sufficient implication (E) survives reconstruction. The new
finite reduction neither proves nor refutes (D), its sublogarithmic
variant, or the parent correlation question. The remaining test must
control these rank resonances and the threshold rectangles outside the
small-product range. BCZ mixing for normalized Lebesgue measure does not
by itself supply either estimate for the changing finite Farey orbit.
