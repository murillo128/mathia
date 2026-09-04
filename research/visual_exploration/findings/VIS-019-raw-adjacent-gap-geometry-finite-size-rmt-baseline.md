# VIS-019 — raw adjacent-gap geometry is a finite-size RMT baseline

## Claim

Let `gamma_n` denote consecutive ordinates of high nontrivial Riemann-zeta zeros and let adjacent gaps be unfolded to unit mean density. A visual observable that is determined only by the **joint distribution of two consecutive unfolded gaps** `(a,b)`, or by the derived gap ratio `r=a/b`, is not a new arithmetic-specific geometric channel merely because its return map, density plot, or ratio histogram has structured shape.

Existing finite-size random-matrix theory already models these observables at the level needed to explain their dominant high-zero geometry. In particular, Nishigaki (2026) derives the joint two-spacing law for `CUE_N`, its finite-`N` corrections, and compares it directly with very-high Riemann-zero data through an effective matrix size `N_e(T)`. The zeta two-gap joint density agrees with the displayed effective-CUE prediction through the `O(N_e^-2)` correction, while the gap-ratio statistic removes that CUE correction by symmetry/cancellation and exposes a smaller arithmetic correction at order `O(N_e^-3)` on the zeta side.

**Evidence/status:** `LITERATURE+DERIVED + NEGATIVE/BASELINE`.

The durable Mathia consequence is an information-accounting restriction: **raw adjacent-gap return maps, two-gap histograms, nearest-neighbor anti-correlation, and gap-ratio plots must be treated as established finite-size spectral-statistics baselines.** A surviving visual candidate must isolate a residual beyond the appropriate finite-size CUE/arithmetic prediction or retain genuinely higher-order/nonlocal information.

## Literature bridge

Forrester and Mays (2015) and Bornemann–Forrester–Mays (2017) already place finite-height zeta spacing deviations inside a finite-size circular-ensemble framework rather than treating every departure from the infinite sine-kernel limit as new arithmetic structure.

Nishigaki (2026) sharpens this specifically for consecutive spacings. For `CUE_N`, the joint density `P_c(a,b)` of two consecutive spacings has a leading `O(N^-2)` correction to its sine-kernel limit. The gap-ratio distribution `P_r(r)`, however, has vanishing `O(N^-2)` correction and its first CUE finite-size correction is `O(N^-4)`.

For Riemann zeros near height `T`, the comparison uses an effective finite size

`N_e(T) = (1/sqrt(12 Lambda)) log(T/(2 pi))`,

where `Lambda` is an arithmetic constant arising from prime sums. Using Odlyzko high-zero datasets, the paper reports excellent agreement of the joint distribution of two adjacent unfolded zeta gaps with the analytic `CUE_{N_e}` prediction through the displayed `O(N_e^-2)` correction. Because the CUE ratio correction at that order cancels, the zeta gap-ratio deviation instead reveals the known arithmetic mismatch entering at `O(N_e^-3)`.

The CUE statements are analytic finite-`N` results. The zeta comparison is a literature-backed asymptotic/empirical model supported by very large high-zero datasets; this finding does not upgrade it to a theorem about all zeta zeros.

## What this closes

The accepted multiscale clue left open a source-sensitive higher-order statistic of the zero configuration after local analytic and phase channels were removed. The first obvious move is to draw a return map

`g_n -> g_{n+1}`

of unfolded consecutive gaps, estimate its two-dimensional density, measure its adjacent anti-correlation, or compress it to a ratio `g_{n+1}/g_n` and look for a characteristic ridge or forbidden region.

Those views are now a **baseline, not a discovery surface**. Their structured geometry already belongs to the standard random-matrix/finite-size analysis of zeta zeros. In particular:

- a visible negative relation between neighboring gaps is not by itself an arithmetic signature;
- a non-Poisson two-gap cloud is far too weak a control, because CUE already supplies correlated consecutive spacings;
- deviation from the infinite sine-kernel limit is also too weak, because finite-`N_e` corrections are expected and quantitatively modeled;
- a gap-ratio anomaly must be compared with the known cancellation structure and the zeta `O(N_e^-3)` arithmetic correction before it can be interpreted as new organization.

This closes only the **standalone two-consecutive-gap channel**. It does not close higher-order blocks of gaps, long-lag spacing covariance, conditioned statistics, nonstationary scale coupling, topology of residual processes, or statistics designed explicitly to subtract the known finite-size and arithmetic terms.

## Visual consequence

No new PNG is retained for this result. The candidate was killed at the prior-art gate before a new return-map rendering could carry research value. Rendering another adjacent-gap scatter or ratio histogram would reproduce a standard object whose relevant finite-size geometry is already explicitly studied in the literature.

This is intentional under the Visual Research no-churn rule: once a representation is known to be a canonical baseline, a new image is warranted only when it documents a residual or control not already accounted for by that baseline.

## Prior art and novelty assessment

Primary anchors are recorded in `research/visual_exploration/SOURCES.md`:

- Forrester–Mays (2015), DOI `10.1098/rspa.2015.0436`;
- Bornemann–Forrester–Mays (2017), DOI `10.1111/sapm.12160`;
- Nishigaki (2026), DOI `10.1093/ptep/ptag006`.

No novelty is claimed for CUE spacing laws, finite-size corrections, effective matrix-size modeling, the high-zero comparisons, or the gap-ratio correction. The Mathia contribution is the **visual falsification boundary**: these observables are now explicitly excluded as independent evidence for a new mesoscopic/fractal zeta geometry unless the known baseline is first removed.

## Boundary conditions and falsification

This finding must not be overread as saying that all zero-spacing information is random-matrix universal. The 2026 comparison itself contains arithmetic finite-height corrections, and earlier zeta spectral-statistics work is specifically concerned with non-universal arithmetic terms.

Nor does agreement of low-order distributions imply equality of point processes. A candidate may remain live if it uses information not determined by the joint law of two adjacent gaps — for example three-or-more-gap structure, long-lag correlations, height-coupled residuals, or a statistic conditioned on another arithmetic observable — provided it is tested against controls that preserve the already-known low-order laws.

A future two-gap visual candidate is admissible only if it defines an explicit residual relative to the finite-size baseline and shows that the residual is not merely the known arithmetic correction already present in the literature. Otherwise it should be rejected before rendering.

## Research consequence

`CLUE-zeta-critical-strip-multiscale-geometry` should now treat ordinary adjacent-gap return maps, two-gap densities, adjacent-gap anti-correlation, and raw gap-ratio geometry as closed baseline channels. The live zero-configuration branch moves one level up: search for **higher-order or nonlocal organization after matching not only local density, gaps, and pair correlation, but also the finite-size consecutive-spacing law and its known arithmetic correction**.

This makes the next decisive control sharper. A visually interesting zero statistic should be compared with a surrogate or model that preserves the known one-gap/two-gap structure; otherwise the experiment risks rediscovering random-matrix finite-size geometry in another coordinate system.
