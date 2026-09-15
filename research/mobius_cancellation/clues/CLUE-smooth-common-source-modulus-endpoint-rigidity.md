---
id: CLUE-mobius-cancellation-smooth-common-source-modulus-endpoint-rigidity
type: research-clue
status: resolved
origin: research-watch
target_line: mobius_cancellation
based_on:
  - research/mobius_cancellation/findings/MC-304-fixed-ramification-radical-capacity-dichotomy.md
  - research/mobius_cancellation/findings/MC-305-endpoint-coset-occupancy-forces-near-shell-radical.md
  - research/mobius_cancellation/findings/MC-312-generalized-hamming-source-redundancy-scale-tradeoff.md
  - research/mobius_cancellation/findings/MC-314-second-order-source-scale-near-capacity-erasure-boundary.md
  - research/mobius_cancellation/findings/MC-317-random-linear-erasure-augmentation-closes-generic-endpoint.md
---

# Can smooth common-source-modulus zero-free rigidity kill the arithmetic endpoint that generic codes realize?

## Observation

`MC-317` shows that the near-capacity generalized-weight profile forced by the reciprocal endpoint is compatible with ordinary binary `[2R,R]` codes, so another generic coding inequality cannot close the route. The actual Legendre realization carries extra arithmetic structure that the random-code control does not: by `MC-304`, all selected source characters have primitive conductors dividing one common squarefree lower-prime radical

\[
P=\prod_{p\in U}p.
\]

At the exact natural-scale boundary isolated by `MC-314`, a source package with `n=2R` and largest source prime `Z\le y^{1/R}` has

\[
P\le Z^n\le y^2,
\qquad
P^+(P)\le y^{1/R}.
\]

Meanwhile `MC-305` forces the same endpoint radical to be near the shell scale at critical rank, in particular `P\ge y/(\log y)^{O(1)}` when `2^R\asymp\log y`. Hence

\[
\frac{\log P^+(P)}{\log P}=O(1/R)=o(1).
\]

So the natural low-redundancy arithmetic escape left after `MC-317` would have to live inside the character group of an exceptionally smooth common modulus, not an arbitrary binary code.

A targeted prior-art check points to a potentially relevant rigidity theorem rather than another coding bound. Chang's smooth-composite-modulus zero-free theory (*Short character sums for composite moduli*, J. Analyse Math. 123 (2014), arXiv:1201.0299) gives enlarged zero-free regions depending on the largest prime factor of the modulus. Klurman--Mangerel--Teräväinen (*Multiplicative functions in short arithmetic progressions*, PLMS 127 (2023), Lemma 12.3) record a joint smooth-modulus zero-free region for the product of Dirichlet `L`-functions modulo `q`, with at most one real simple exceptional zero. Banks--Shparlinski's smooth-modulus work likewise emphasizes a single possible problem character. None of these statements has yet been converted here into the exact dyadic prime-shell estimate needed below.

## Research question

Let the endpoint source characters `\chi_1,\ldots,\chi_R` be induced to the common modulus `P`, and impose the shell condition `r\equiv1\pmod4` by passing to modulus `4P`. Does the existing smooth-modulus zero-free theory imply, uniformly in the critical regime

\[
P\in\left[y(\log y)^{-O(1)},y^2\right],
\qquad
P^+(P)\le y^{1/R},
\qquad
R\asymp\log\log y,
\]

that all but at most one relevant character satisfy

\[
\sum_{y<r\le2y\atop r\text{ prime},\ r\equiv1\pmod4}
\chi(r)\log r=o(y)?
\]

The mod-4 restriction can be written using the pair `\chi` and `\chi\chi_4`. Thus an exact endpoint, which requires `R` independent characters with shell average `-1+2/R`, would force large prime-shell bias in many distinct characters modulo `4P`. If smooth-modulus zero-free rigidity permits at most one such character at this prime scale, the arithmetic endpoint would be impossible even though its abstract `[2R,R]` code exists.

## Why it may matter

This is a candidate answer to the precise realizability gap exposed by `MC-317`. The common smooth modulus is forced by actual lower-prime provenance and disappears completely when the endpoint is replaced by a generic binary code. A successful theorem would therefore distinguish rational-prime source incidence from the matched random-code control using arithmetic information already present in the construction, rather than adding another representation or generic capacity inequality.

It would also connect two previously separate currencies in the line: the source-scale/coding frontier of `MC-312`--`MC-317` and the character zero-free/exceptional-mode machinery used earlier for source-cost bounds. The desired conclusion is still local to the endpoint model; no Mertens or RH estimate is being assumed.

## Decisive test

First verify the parameter bridge exactly from the canonical findings: under the natural-scale endpoint escape, derive the common-modulus bounds on `P` and `P^+(P)` with all `o(1)` terms and the factor `4` restored. Then audit the strongest applicable form of Chang/Iwaniec smooth-modulus zero-free theory and the KMT joint zero-free lemma for characters induced from divisors of `P` and for their `\chi_4` twists.

The decisive analytic step is to pass from that zero-free region to a **uniform dyadic prime-character estimate at prime variable `y`**, not at a much larger scale. Track the width of the zero-free strip, the allowed height, conductor dependence, logarithmic losses in `L'/L` or the explicit formula, and the possible exceptional real character. Keep the direction only if the resulting bound is genuinely `o(y)` throughout the displayed `P` range. Kill or narrow it if the zero-free theorem requires the prime variable to be polynomially larger than `P`, if its quantitative losses swamp the `R\asymp\log\log y` gain, or if more than one endpoint-sized prime-shell bias can coexist without contradicting the one-problem-character statement.

## Evidence boundary

The common-radical smoothness calculation is only a conditional consequence of the exact natural-scale, low-redundancy endpoint escape already isolated by the stored findings; it is not asserted for every possible source package. The literature establishes strong smooth-modulus zero-free and character-sum phenomena, but this clue has **not** established the required prime-shell cancellation uniformly at `y` in the moving-modulus regime above.

In particular, smooth-number equidistribution results such as Banks--Shparlinski cannot be substituted for the needed twisted prime sum, and a zero-free region alone is not yet the endpoint contradiction until the explicit-formula/PNT conversion is quantitatively checked. No impossibility theorem for the arithmetic endpoint, no improvement for `M(x)`, and no RH consequence is claimed.

## Research disposition

Outcome: narrowed

Resolved by:
- [[research/mobius_cancellation/findings/MC-319-smooth-modulus-zero-free-dyadic-resolution-barrier.md]]

`MC-319` verifies the common-modulus parameter bridge and shows that the cited smooth-modulus zero-free theorem genuinely constrains the entire relevant character family, up to at most one exceptional real character. The available KMT Rodosskii conversion nevertheless resolves only broad power intervals at harmonic scale `O((\log\log q)^{-1/2})`, while the endpoint needs one-dyadic-shell control at scale `o(1/\log y)`. The clue is therefore resolved in the narrowed direction: existing smooth-modulus zero-free machinery does not close the endpoint by itself, and the residual question is a genuinely dyadic prime-character estimate or another arithmetic realizability obstruction.