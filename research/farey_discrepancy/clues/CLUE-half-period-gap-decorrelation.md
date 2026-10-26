---
id: CLUE-farey-discrepancy-half-period-gap-decorrelation
type: research-clue
status: accepted
origin: research-watch
target_line: farey_discrepancy
based_on:
  - research/farey_discrepancy/findings/FD-346-classical-gap-correlations-separate-high-band-farey-transport.md
  - research/visual_exploration/findings/VIS-468-four-defect-farey-reassembly-preserves-source-sector.md
  - research/visual_exploration/visualizations/farey-half-period-gap-control.md
  - research/farey_discrepancy/clues/CLUE-inherited-high-band-farey-source-sector.md
---

# Does half-period Farey gap decorrelation resolve the alternating source sectors?

## Observation

FD-346 already excludes projected high-band transport matching by a fixed
frequency event. It leaves the genuine source's alternating frequency
sectors unresolved. This is a proposed **residual source-correlation
test**, not a reopening of the resolved matching question in the inherited
sector clue.

For prime order \(p\), use its genuine Farey gaps \(g_k=x_{k+1}-x_k\),
period \(N=\sum_{q\le p}\varphi(q)=2h\), and uncentered correlations
\(S_r=\sum_{k=0}^{N-1}g_kg_{k+r}\). The
[visual panel](../../visual_exploration/visualizations/farey-half-period-gap-control.md)
inspects \(S_{h+r}\) directly, rather than estimating a
microscopic sector split from a smooth frequency CDF. Across the seven
prime orders \(31,61,127,251,509,1021,2039\), \(p^2S_h\) ranges from
4.473284 to 5.898336; the plotted fixed offsets remain on a similar scale.
These observations motivate a bound, not an asymptotic assertion.

A deterministic negative control makes the missing input visible.
Concatenate two copies of the entire grid scaled by one-half. The new
rank count is \(2N\), its gaps are \((g/2,g/2)\), and reflection is exact.
Its upper-band frequency CDF is exactly the source CDF, but all nonzero
sine coefficients have indices divisible by four. The normalized gap
multiset \(N g_k\) is also preserved after doubling multiplicities.
It is an artificial grid, not a second Farey source, and does not preserve
the original denominator labels or cutoff. This control does not refute
an arithmetic sector theorem; it prevents inferring one from those coarse
summaries and reflection alone.

## Research question

For **every fixed integer** \(r\), is

\[
S_{h+r}(p)=o\!\left(\frac{\log p}{p^2}\right)
\quad\text{as primes }p\to\infty? \tag{A}
\]

The stronger \(S_{h+r}(p)=O_r(p^{-2})\) is a concrete candidate suggested
by the finite panel. It is not needed if the weaker (A) can be proved.
The offset is fixed before the limit; the actual rank lag \(h+r\) grows
like \(p^2\). Centering gaps subtracts \(1/N=\Theta(p^{-2})\), so it does
not change (A), but it does change finite constants on the stronger scale.

## Why it may matter

Condition (A) would settle the source-sector split left open by FD-346
without requiring a uniform estimate over a growing set of offsets.
It is stronger than needed for one band and is not asserted necessary.
It targets actual arithmetic long-rank correlations, while ordinary
fixed-lag gap moments only determine the coarse profile.

Here is the conditional bridge, using FD-346's unitary gap transform
\(G_j=N^{-1/2}\sum_k g_ke^{-2\pi ijk/N}\) and
\(\theta_j=2\pi j/N\). Define

\[
\mu_p=\frac{p^2}{\log p}\sum_j|G_j|^2\delta_{\theta_j},\qquad
\nu_p=\frac{p^2}{\log p}\sum_j(-1)^j|G_j|^2\delta_{\theta_j}.
\]

Exactly,

\[
|\nu_p|=\mu_p,\qquad
\int e^{ir\theta}\,d\nu_p(\theta)
=\frac{p^2}{\log p}S_{h+r}(p). \tag{B}
\]

FD-346 proves that \(\mu_p\) has bounded mass and an absolutely continuous
weak limit. If (A) holds, trigonometric-polynomial approximation gives
\(\nu_p\Rightarrow0\). Domination by \(\mu_p\) allows restriction to
fixed bands with atom-free limiting boundaries. On a band away from zero,
apply the bounded discrepancy multiplier \(1/[4\sin^2(\theta/2)]\).
For \(D_k=x_k-k/N\) and its orthonormal DST-I coefficients
\(d_m=\sqrt{2/N}\sum_{k=1}^{N-1}D_k\sin(\pi mk/N)\),
\(1\le m<N\), this yields

\[
\frac{p^2}{\log p}
\left(\sum_{\substack{m/N\ge\alpha\\4\mid m}}d_m^2
-\sum_{\substack{m/N\ge\alpha\\m\equiv2\ (4)}}d_m^2\right)\to0,
\quad 0<\alpha<1. \tag{C}
\]

The positive total-band asymptotic in FD-346 then gives sector fraction
one-half. For its prime-order reassembly \(y=CD+w\), the same finding
proves \(\|P_B y\|^2/\|P_B D\|^2\to1\); consequently VIS-468's inherited
ratio \(\eta_p\) would also tend to one-half in the upper band. This would
improve that event's TV lower bound, not identify the full discrete TV
limit or give an RH estimate.

## Decisive test

Reconstruct (B) with the cyclic indexing, then prove or falsify (A) from
actual Farey arithmetic. A promising first target is \(S_h=O(p^{-2})\),
but proving it only at \(r=0\), or checking finitely many offsets, does
not complete the stated route. Seek an argument for every fixed \(r\),
or an independently sufficient estimate for the band-weighted signed
measure. A failure of (A) would kill this sufficient route, not by itself
refute band equipartition.

The repeated-grid control must fail (A), and it does: with effective
scale \(\widetilde p=\sqrt2p\) and period \(\widetilde N=2N\), its
half-period gap correlation equals \(S_0(p)/2\). Thus
\(\widetilde p^2\widetilde S_{\widetilde N/2}/\log\widetilde p\to12/\pi^2\),
while its fixed-lag normalized moments have the same limits as the source.
The effective scale is an analysis normalization, not an integer Farey
order. This rules out proving (A) from those moments alone.

Audit closest prior art before promoting any estimate. The explicit
fixed-lag formulas in
[Dong–Nguyen–Nguyen–Zaharescu, equation (2.2) and Theorem 2.3](https://arxiv.org/html/2606.12907v1)
include lag-dependent ranges and errors; they do not license substituting
\(h+r\). Classical shift/replication and Fourier-correlation identities
explain (B) and the control. Targeted searches for Farey gap half-period,
growing-rank-lag and spectral-sector results did not provide (A); this
is bounded orientation, not an exhaustive novelty verdict. In particular,
position pair-correlation theorems and fixed-rank-gap theorems must not be
silently interchanged.

## Evidence boundary

The proposed asymptotic (A) and the stronger bound are unproved. The
finite panel has no untouched confirmation sample and supplies no uniform
lag estimate, limiting constant or rate. All source/theorem/review states
must be checked when triaging this clue. The conditional Fourier bridge
and deterministic repetition are standard algebraic motivation, not a
new general theorem or independent arithmetic validation. The paired
visualization documents its numerical and exact rational checks.

FD-346 has already settled the comparator's nonconvergence. This clue
addresses the remaining arithmetic sector question through a more
specific sufficient correlation estimate. It claims no full TV limit,
new cancellation theorem, formal verification or RH improvement.

## Research disposition

The all-fixed-offset arithmetic question remains worth investigating;
acceptance asserts neither its truth nor its novelty.
[FD-347](../findings/FD-347-finite-half-period-tests-miss-reflected-gap-sector-bias.md)
establishes a stronger control boundary than identical replication:
rotating the genuine gap list and adjoining its reversal preserves the
normalized gap multiset and the full coarse high-band law, while passing
any prescribed finite window `S_(M/2+r)=O(Q^-2)` and retaining a nonzero
limiting sector bias. Even the single-offset test can pass with the
`4|m` upper-band fraction tending to `0.1701038168...`.

This does not challenge (A) for actual Farey gaps: the control lacks the
original denominator cutoff and adjacency labels. The remaining test is
a proof of (A) for every fixed offset, an independently sufficient
band-weighted estimate, or an arithmetic rigidity theorem that justifies
reducing to fewer offsets. The existing source dictionary and the
bounded-multiplier implication (B)–(C) survive independent reconstruction;
the fixed-lag literature does not supply the missing moving-lag bound.
