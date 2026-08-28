# WI-002 — the density-one moment tower is a live candidate, but its all-order arithmetic transport is not yet established

**Status:** `NEEDS-AUDIT` — material prior-art redirection. The external preprint described here is explicitly unreviewed and self-graded `certified-candidate`; none of its new percentage or density-one claims are accepted as established evidence in Mathia at this stage.

## 1. Precise external claim

Hongyi Yang and Shihua Yang posted a 17 August 2026 preprint claiming

\[
\liminf_{T\to\infty}\frac{N_0^s(T,2T)}{N(T,2T)}\ge 0.7962,
\qquad
\liminf_{T\to\infty}\frac{N_d(T,2T)}{N(T,2T)}\ge 0.8981,
\]

by extending the Alpöge--Furman compressed-Weil-matrix method through the sixth trace moment. A second preprint from the same program, posted 22 August 2026, claims the much stronger density-one statement

\[
\boxed{
\lim_{T\to\infty}\frac{N_0^s(T,2T)}{N(T,2T)}
=
\lim_{T\to\infty}\frac{N_d(T,2T)}{N(T,2T)}=1.
}
\]

It also gives a finite instantiated rung through moment order 14 of

\[
\frac{N_0^s}{N}\ge0.910460\ldots,
\qquad
\frac{N_d}{N}\ge0.955230\ldots.
\]

The density-one manuscript and reproduction repository explicitly say that the analytic chain is not formalized, has had no external review, and is a `certified-candidate`, not an established record. The exact-rational and Lean artifacts certify algebraic/model-side identities and finite certificates; they do not by themselves certify the analytic transfer from primes to the claimed trace moments.

## 2. The proposed defect-to-zero mechanism

The capstone mechanism is directly relevant to the objective of `weil_inertia`.

For every fixed order `k`, the manuscript proposes an unconditional arithmetic moment theorem for the compressed Weil matrix and then applies the same Christoffel/moment-counting mechanism used at low order. This gives

\[
\liminf_T \frac{N_0^s}{N}\ge 1-2\lambda_k(0),
\qquad
\liminf_T \frac{N_d}{N}\ge 1-\lambda_k(0),
\]

where `lambda_k(0)` is the Christoffel value determined by the first `2k` limiting moments.

On the model side the moments are realized by the finite-`N` positive Gram matrix

\[
\widehat G_N=WW^*/N,
\]

for Fourier vectors evaluated at Haar-CUE eigenangles. The manuscript derives an exact log-determinant identity from the Vandermonde/Morris integral,

\[
\mathbb E\!\left[\frac1N\sum_i\log\lambda_i\right]
=H_N-1-\log N,
\]

and uses it to bound the negative logarithmic moment uniformly. Combined with a factorial-squared moment-growth bound, Stieltjes--Carleman determinacy, and the classical Christoffel-function limit

\[
\lambda_k(0)\downarrow \nu(\{0\}),
\]

the model measure has `nu({0})=0`, hence `lambda_k(0) -> 0`.

Importantly, the final supremum argument is not obviously a forbidden interchange of `k` and `T`: if the fixed-order arithmetic theorem is true for every `k`, the single number `liminf_T N_0^s/N` is bounded below by every fixed-order rung and therefore by their supremum. No uniform error estimate in `k` is needed for that logical step.

Thus the proposed route is a genuine **defect-to-zero architecture**:

\[
\text{all fixed trace moments}
\Longrightarrow
\text{determinate positive model measure with no atom at }0
\Longrightarrow
\lambda_k(0)\to0
\Longrightarrow
\text{density-one simple critical zeros}.
\]

It would not prove RH: an `o(N)` exceptional set of off-line zeros can remain.

## 3. Where the claim actually lives or dies

The decisive issue is therefore not the soft density-one capstone. It is the claimed **all-order arithmetic moment transport** (`Order schema`, together with the pure-class and multi-block transport theorems).

The paper asserts that every singleton-free class at every fixed order can be reduced, after a truncation, to logarithmic-size moduli and then closed factor by factor by Siegel--Walfisz on major arcs and Vaughan bounds on minor arcs. If correct, this is exactly the missing arithmetic input identified in WI-001: higher moments become unconditionally accessible without assuming the higher prime correlations that a naive full-band expansion appears to require.

The audit must therefore reconstruct this reduction directly from the original trace expansion rather than accepting the model calculations, finite-height faces, exact rational constants, or Lean certificate layer as evidence for it.

## 4. A load-bearing ambiguity in the current manuscript

There is already a precise problem that prevents treating the analytic chain as established **as written**.

Early in the manuscript the symbol

\[
\ell_1=\log(T/2\pi)+2\log2-1
\]

is defined globally as the Riemann--von Mangoldt normalization, so it is a single quantity depending only on `T`. Later, the truncation section uses the same symbol as a varying **cell parameter**:

- the cell-mass lemma speaks of a cell "at parameter `ell_1`";
- the multiplicity lemma counts prime-power tuples with "cell parameter `ell_1 = ell`";
- the truncation proposition restricts cells to `ell_1 <= P` and derives a tail by summing `ell^{-k} * ell * ell^epsilon`;
- the all-order transport then invokes this proposition to conclude that only moduli `<= (log X)^B` need to be handled.

No second definition identifying this varying cell parameter with an explicit function of the prime-power tuple is supplied before this use. With the earlier global definition, the truncation statements are not mathematically interpretable: a global `ell_1 ~ log T` cannot simultaneously index different cells or have divisor-bounded tuple multiplicity.

This may be a repairable notation/substitution error rather than a false theorem, so it is **not** recorded as a refutation. But it is load-bearing. The logarithmic-modulus truncation is what makes the claimed Siegel--Walfisz/Vaughan closure possible; until the missing cell quantity and its exact coefficient in the trace expansion are reconstructed and the displayed absolute tail bound is proved for that quantity, the claimed higher-moment and density-one results cannot be imported as evidence.

## 5. Additional all-order audit target

Even after repairing the truncation variable, the multi-block theorem has another explicit burden: it replaces a joint arithmetic class by products of per-block main terms plus deviations and claims that the resolved Parseval/CRT structure makes cross-block errors negligible at every fixed order.

This is precisely where a hidden higher-correlation assumption could enter. A serious audit should verify, from the exact prime-side sum, that:

1. the block decomposition preserves every cross-block congruence and singular-series factor;
2. the multidimensional Fourier transforms really range over complete periods, so the claimed coordinatewise orthogonality is exact;
3. the product-of-deviations estimate has enough summability after all lock, shift, and cell sums;
4. the constants hidden in fixed-order estimates are harmless before taking `T -> infinity`;
5. no arithmetic class discarded by the truncation contributes at main-term scale.

Finite-height agreement with the CUE model does not establish any of these asymptotic statements.

## 6. Prior-art and novelty assessment

The density-one preprint is not an established theorem or peer-reviewed source. No independent mathematical validation was located in this audit. Its authors themselves distinguish the exact-rational/model/certificate layers from the unformalized analytic chain and explicitly retain `certified-candidate` status.

Nevertheless, this is not a low-value speculative note. It proposes a concrete all-order extension of the exact direction singled out by Alpöge--Furman as the escape from the first-two-moment barrier, provides public source and reproduction artifacts, and reaches the exact target of this research line: a mechanism that would make the exceptional density tend to zero without first proving full Weil positivity.

The correct Mathia classification is therefore `NEEDS-AUDIT`, not dismissal and not acceptance.

## 7. Decisive falsification / verification test

The next audit should ignore the high-order rational constants initially and attack the first nontrivial arithmetic rung.

Starting from the prime-side formula for the fourth trace moment:

1. define every cell variable without reusing the global Riemann--von Mangoldt `ell_1`;
2. derive the exact coefficient of a cell from the trace expansion;
3. prove, on absolute values, the claimed tail estimate that reduces the relevant prime-power moduli to `P=(log X)^B`;
4. only then prove the truncated fourth-moment variance theorem from standard Siegel--Walfisz/Vaughan inputs;
5. recover `m_4=13/4` and the `13/18` simple-critical-zero rung independently of the manuscript's numerical/model pipeline.

If this base case fails, the all-order tower and density-one capstone lose their arithmetic foundation. If it survives, the same reconstruction should be repeated for the first genuinely multi-block case before accepting the order-uniform schema.

## 8. Consequence for `weil_inertia`

WI-001 showed that the first-two-moment, bandwidth-one information has explicit extremizers and cannot by itself eliminate the exceptional mass. The Yang--Yang program proposes exactly the missing escape: **higher moments that progressively resolve the extremizers, followed by a moment-problem limit in which the zero-defect certificate tends to one**.

Accordingly, the highest-value immediate task is no longer to invent another abstract higher-moment certificate from scratch. It is to independently settle whether this claimed arithmetic moment tower is valid. A successful verification would radically advance the line to density one; a rigorous failure at the truncation or multi-block transport would identify the exact arithmetic obstruction that any genuine extension must overcome.
