# VIS-109 — third-order correlation crosses the exact local-block boundary at minimal span four

## Claim

Let

`a = 01000111001011`,

`b = 01001011100011`

be the Fourier-homometric exact order-three Markov-type pair from `VIS-108`. For a finite real sequence `x=(x_0,...,x_(N-1))`, define the aperiodic third-order correlation for nonnegative lags by

`C_x(k,l) = sum_(0<=j<N-max(k,l)) x_j x_(j+k) x_(j+l)`.

Then two exact facts hold.

First, for **every** pair of sequences in the same order-three Markov type of `VIS-099`, `C_x(k,l)` is fixed whenever `max(k,l)<=3`. Those coordinates contain no chronology beyond the admitted length-four transition inventory and its boundary context.

Second, the explicit `VIS-108` pair separates immediately at the first larger span:

`C_a(1,4)=1`,

`C_b(1,4)=0`.

Thus third-order correlation has a sharp information boundary relative to the exact local quotient: spans through three are forced by the order-three Markov type, while span four can already retain assembly chronology that the quotient forgets.

If

`X_x(z)=sum_(j=0)^(N-1) x_j z^j`

and

`B_x(z,w)=X_x(z) X_x(w) X_x((zw)^(-1))`,

then the coefficient of `z^k w^l` in this Laurent polynomial is exactly `C_x(k,l)`. On the unit torus this is the usual phase-sensitive bispectral product, up to Fourier-sign convention. Hence

`B_a != B_b`

even though `VIS-108` proves

`X_a(z)X_a(z^(-1)) = X_b(z)X_b(z^(-1))`.

So the full power spectrum loses the distinction, while a third-order spectral invariant can recover it at the first lag span not already fixed by the local four-block quotient.

**Evidence/status:** `EXACT-DERIVED + INFORMATION-BOUNDARY + CLASSICAL-BISPECTRUM PRIOR ART + CANDIDATE-CARRIER + NO-ZETA-SPECIFIC CLAIM + NO-NOVELTY-CLAIM`.

This finding does not establish that a bispectral statistic of Riemann-zero data is unusual, arithmetic-specific, useful for RH, or superior to the existing path-signature carrier. It establishes only that third-order correlation/bispectrum passes the exact information-admission test that magnitude-only Fourier representations fail in `VIS-108`.

## 1. Local third-order correlations are fixed by the exact type

Fix one exact order-three Markov type in the sense of `VIS-099`: the initial triple and the complete transition counts of length-four blocks are fixed.

Let `r=max(k,l)<=3`. Then

`C_x(k,l)=sum_(j=0)^(N-1-r) f_(k,l)(x_j,...,x_(j+r))`,

where `f_(k,l)` is simply the product of coordinates at offsets `0,k,l`.

For every start `j<=N-4`, this contribution is a function of the length-four transition block beginning at `j`. Summing over those starts therefore depends only on the fixed multiset of length-four blocks.

When `r<3`, the remaining `3-r` starts lie inside the final three-symbol context. That final context is itself fixed by the exact type: the directed transition-count multigraph and the fixed initial context determine the terminal context through their in-degree/out-degree imbalance (and in the balanced case the terminal context equals the initial one).

Therefore every `C_x(k,l)` with `max(k,l)<=3` is constant on the entire exact type class.

This is not a special property of the displayed binary pair. It is an information theorem for the quotient used by the current visual branch: any third-order statistic built only from lag spans at most three is already determined before alternative Eulerian assembly is sampled.

## 2. The first nonlocal span already distinguishes the homometric pair

Use zero-based support sets from `VIS-108`:

`S_a={1,5,6,7,10,12,13}`,

`S_b={1,4,6,7,8,12,13}`.

For binary sequences, `C_x(1,4)` counts indices `j` for which

`j, j+1, j+4`

all lie in the support.

For `a`, exactly one index contributes: `j=6`, because `{6,7,10} subset S_a`. Hence

`C_a(1,4)=1`.

For `b`, no index satisfies the same condition, so

`C_b(1,4)=0`.

The maximum lag is four, exactly one step beyond the span forced by the length-four local inventory. The witness is therefore minimal in span: no `C(k,l)` with maximum lag at most three can distinguish any two members of the exact type, while this pair is distinguished at maximum lag four.

This gives a cleaner information accounting than saying merely that “the bispectrum has phase.” The admitted local quotient fixes a concrete lower-left `4 x 4` lag block of the third-order correlation surface; chronology can first enter immediately outside that block.

## 3. The bispectrum is the Fourier image of the same distinction

Expand

`B_x(z,w)=X_x(z)X_x(w)X_x((zw)^(-1))`.

Then

`B_x(z,w)`
` = sum_(p,q,r) x_p x_q x_r z^(p-r) w^(q-r)`.

Collecting the coefficient of `z^k w^l` gives

`[z^k w^l] B_x = sum_r x_r x_(r+k) x_(r+l) = C_x(k,l)`,

with terms outside the finite support understood as zero.

Consequently the exact inequality

`C_a(1,4) != C_b(1,4)`

forces

`B_a(z,w) != B_b(z,w)`

as Laurent polynomials. On `|z|=|w|=1` and for real sequences,

`X_x((zw)^(-1)) = conjugate(X_x(zw))`,

so this is the standard bispectral phase-coupling form

`X(omega_1) X(omega_2) conjugate(X(omega_1+omega_2))`

modulo the sign convention used for the Fourier transform.

By contrast, `VIS-108` proves equality of the complete second-order Laurent polynomial `X(z)X(z^(-1))`, equivalently equality of every aperiodic two-point autocorrelation and every Fourier magnitude. The third-order surface therefore contains information that the full power spectrum provably erased for this exact chronology witness.

## 4. Prior art and novelty assessment

The bispectrum and higher-order spectra are classical signal-processing objects. C. L. Nikias and M. R. Raghuveer, **Bispectrum estimation: A digital signal processing framework**, *Proceedings of the IEEE* 75:7 (1987), 869–891, DOI `10.1109/PROC.1987.13824`, develops the standard digital-signal-processing framework for bispectral estimation. Jerry M. Mendel, **Tutorial on higher-order statistics (spectra) in signal processing and system theory: theoretical results and some applications**, *Proceedings of the IEEE* 79:3 (1991), 278–305, DOI `10.1109/5.75086`, surveys the classical relation between higher-order moments/cumulants and their spectra.

Phase recovery from third-order spectral information is likewise established prior art. Moon G. Kang, Kuen Tsair Lay, and Aggelos K. Katsaggelos, **Phase estimation using the bispectrum and its application to image restoration**, *Optical Engineering* 30:7 (1991), 976–985, DOI `10.1117/12.55893`, explicitly treats the bispectrum as the Fourier transform of triple correlation and uses it for phase estimation. More recent finite-signal work by Tamir Bendory, Dan Edidin, and Shay Kreymer, **Signal recovery from a few linear measurements of its high-order spectra**, *Applied and Computational Harmonic Analysis* 56 (2022), 391–401, DOI `10.1016/j.acha.2021.10.003`, places completeness of high-order spectral invariants up to shift in a modern algebraic framework.

Accordingly, no novelty is claimed for third-order correlation, bispectra, phase coupling, shift invariance, or signal-recovery results from higher-order spectra.

The Mathia-specific content is narrower: relative to the exact order-three Markov-type quotient already used as the local chronology null, the finding identifies the **precise lag-span boundary** below which third-order correlation is forced and gives an explicit same-type, power-homometric pair that crosses that boundary at the first possible span.

## Boundary and falsification

This result is an information-admission theorem, not a source-discovery result. It does **not** prove that:

- a particular bispectral coefficient or summary is statistically powerful on zeta-zero gaps;
- third-order spectral information is arithmetic-specific rather than generic long-range chronology;
- zeta differs from a finite-size CUE or another matched non-arithmetic source under such a statistic;
- a full bispectrum is preferable to a sparse lag-domain statistic;
- phase-sensitive spectra retain every path-signature coordinate;
- higher-order spectral structure yields an RH criterion.

The local-boundary statement would be falsified by two sequences in one exact order-three Markov type with different `C(k,l)` for some `max(k,l)<=3`. The explicit witness would be falsified by direct evaluation giving `C_a(1,4)=C_b(1,4)`. The spectral consequence would be falsified if the displayed Laurent coefficient identity failed.

For source work, the main statistical danger is adaptivity. A two-dimensional bispectrum contains many coefficients, so inspecting a source heatmap and then choosing an anomalous-looking frequency or lag would recreate the representation-selection problem this line has been trying to remove. Any source test must freeze the lag/frequency region and statistic before confirmation material is inspected.

## Visual consequence

No canonical PNG is retained. A third-order-correlation or bispectral heatmap would illustrate the distinction, but the exact coefficient `C_a(1,4)-C_b(1,4)=1` already certifies it without relying on color scale, interpolation, FFT grid, or visual salience.

If a later source experiment uses this carrier, a 2D lag-domain or bispectral view may be useful for human inspection only after the statistic and admissible region have been specified independently.

## Research consequence

The accepted critical-strip multiscale clue asked for a carrier that demonstrably retains information beyond both the exact local four-block quotient and the two-point Fourier-magnitude quotient. `VIS-109` supplies the first exact positive admission result for a higher-order spectral candidate: **third-order correlation/bispectrum survives the `VIS-108` homometric witness, and the first available nonlocal lag span is exactly four.**

The next step is not another adaptive picture. A continuation should choose, before new source inspection, a low-dimensional statistic built from lag spans strictly beyond the local boundary, specify how it is conditioned against the exact order-three Markov type, and then compare the frozen statistic on fresh source material against an appropriate finite-size CUE or other non-arithmetic control.