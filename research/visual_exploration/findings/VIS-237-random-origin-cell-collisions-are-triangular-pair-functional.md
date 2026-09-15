# VIS-237 — random-origin cell collisions are exactly a triangular pair-gap functional

## Claim

Let

`x_1 < x_2 < ... < x_m`

be any finite ordered set of distinct real points and let `ell>0`. For a grid origin `U in [0,ell)`, partition the line into half-open cells

`I_j(U)=[U+j ell, U+(j+1)ell)`, `j in Z`,

let `N_j(U)` be the number of points in cell `I_j(U)`, and define the same-cell collision count

`S(U)=sum_j binom(N_j(U),2)`.

Then the origin average has the exact finite identity

`(1/ell) integral_0^ell S(U) dU`
` = sum_(1<=a<b<=m) (1-|x_b-x_a|/ell)_+`,

where `(t)_+=max(t,0)`.

Thus randomizing the origin of an ordered interval grid does not create a new categorical or Markov null. It quotients the arbitrary grid phase exactly and turns the collision statistic into the triangular/tent-kernel two-point functional of the underlying ordered point configuration.

Applied to the critical prime-coordinate cells inherited from `VIS-225`--`VIS-227`, every shifted grid remains an ordered-interval representation and therefore preserves the monotone support obstruction of `VIS-236`. At the critical scale, where the inherited cell width is `ell=Theta(log y)`, the origin-averaged collision statistic depends only on prime-pair gaps shorter than `ell`, with linearly decreasing weight.

**Evidence/status:** `EXACT-DERIVED + REPRESENTATION-MATCHED ORIGIN CONTROL + CLASSICAL TENT-KERNEL REDUCTION + NO-NOVELTY-CLAIM`.

No prime-gap theorem, stochastic model for primes, prime-specific residual, new hashing theorem, new point-process theorem, or RH consequence is claimed.

## 1. Same-cell collisions are a pair-indicator sum

For fixed `U`, every unordered pair contributes once to `S(U)` exactly when its two points lie in the same grid cell. Hence

`S(U)=sum_(a<b) 1_{x_a,x_b lie in the same I_j(U)}`.

This rewrites the occupancy statistic without introducing any probabilistic assumption about the point set. The only quantity being averaged is the nuisance grid origin.

## 2. A single pair has a tent collision law

Fix a pair `x_a<x_b` and write

`d=x_b-x_a`.

If `d>=ell`, the two points cannot lie in the same length-`ell` cell except for irrelevant boundary coincidences of zero `U`-measure, so its origin-averaged contribution is zero.

If `0<d<ell`, vary `U` modulo `ell`. The pair fails to share a cell precisely when one grid boundary falls in the interval `(x_a,x_b]`. The set of such origins has Lebesgue measure `d`; the complementary set of origins has measure `ell-d`. Therefore

`P_U(pair shares a cell)=1-d/ell`.

Equivalently,

`(1/ell) integral_0^ell 1_{same cell} dU = (1-d/ell)_+`.

Summing this exact identity over all unordered pairs gives the claimed formula. The half-open cell convention only decides the measure-zero set of origins at which a point is exactly on a boundary.

## 3. The origin quotient stays inside the actual representation support

`VIS-236` showed that the critical prime-coordinate cell labels are nondecreasing because increasing primes are quantized by ordered intervals. Generic categorical or Markov controls can revisit earlier labels and therefore leave that geometric support; the exact first-order type of the actual label path is in fact a singleton.

Origin translation avoids that defect. For every `U`, the cells remain ordered intervals on the same real coordinate and the source points remain in their original increasing order. Occupancies change when a boundary crosses a point, but the label sequence remains monotone. The random-origin family is therefore a genuine nuisance transformation of the existing representation rather than an enlarged path space invented to manufacture null variability.

The exact average also shows what information survives the quotient. It is not a higher-order label statistic: it is the short-range pair-gap measure smoothed by

`K_ell(r)=(1-r/ell)_+`.

Accordingly, scanning many cell origins and treating them as independent confirmation statistics would only repeatedly interrogate different discretizations of the same two-point geometry. The analytically averaged quantity is the natural origin-invariant version.

## 4. Point-process calibration boundary

The same identity identifies the correct baseline language for any stochastic ordered-point control. For a stationary simple point process on the line with intensity `rho` and pair-correlation function `g(r)` in the usual second-factorial-moment convention, the expected origin-averaged collision functional per unit length is

`rho^2 integral_0^ell (1-r/ell) g(r) dr`.

For a homogeneous Poisson process, `g(r)=1`, so this becomes

`rho^2 ell/2`.

These are standard Campbell/factorial-moment consequences, not statements about primes. In the prime application they only expose what a representation-matched null has to account for: local intensity and short-range pair-gap structure at the chosen `ell`. A prime residual can be claimed only after a null for that geometry is specified independently and audited for the relevant scale.

This also separates two questions that were previously entangled. Grid-origin instability is an exactly removable representation nuisance. Departure of the triangular pair-gap functional from an independently justified ordered-point baseline is a mathematical/statistical question about the source points themselves.

## Prior art and novelty boundary

Random-offset equal-width bucket collisions are classical. Datar, Immorlica, Indyk, and Mirrokni, **Locality-sensitive hashing scheme based on p-stable distributions**, *Proceedings of the Twentieth Annual Symposium on Computational Geometry* (2004), 253–262, DOI `10.1145/997817.997857`, use random bucket offsets as part of locality-sensitive hashing; the one-dimensional fixed-distance bucket-overlap calculation underlying the tent collision probability is standard geometry in that setting.

The point-process expectation above is standard second-factorial-moment/Campbell calculus; an authoritative general reference is S. N. Chiu, D. Stoyan, W. S. Kendall, and J. Mecke, **Stochastic Geometry and Its Applications**, 3rd ed., Wiley (2013), DOI `10.1002/9781118658222`.

No novelty is claimed for random grid shifts, the triangular/Bartlett kernel, pair-count U-statistics, or Campbell formulas. The Mathia-specific contribution is the compatibility reduction: after `VIS-236` rules out generic Markov-type randomization for the ordered prime cells, origin averaging supplies a nondegenerate transformation that stays inside the actual representation support and reveals exactly which two-point statistic it measures.

## Boundaries and falsification

The finite identity holds for any distinct real points and any `ell>0`; it assumes neither stationarity nor randomness of the points. The point-process formula in Section 4 is a separate expectation statement requiring the stated stationary second-order model.

The origin average removes only the arbitrary phase of an equal-width interval grid. It does not remove sensitivity to the cell width, to the source coordinate, to endpoint truncation of the observed point set, or to the point configuration itself. It does not prove that Poisson, renewal, Cramér-like, or any other stochastic model is a faithful null for primes.

At critical prime scale, the fact that `ell=Theta(log y)` merely places the kernel on the same order as the mean prime spacing. It does not establish a prime-specific excess or deficit relative to any control.

Falsify the deterministic claim by giving a finite ordered configuration and width `ell` for which the exact origin integral differs from the displayed triangular pair sum. Falsify the representation consequence by exhibiting an allowed translated interval grid for which increasing source points produce a decreasing cell-label step.

## Research consequence

The cell-origin robustness part of `CLUE-prime-phase-critical-logarithmic-occupancy` no longer needs an empirical sweep of arbitrary origins: its mean collision response is known exactly. Future confirmation work should use the triangular pair-gap functional directly, or compare origin-specific deviations only when the deviation itself has a predeclared mathematical role.

The live question is now narrower. Freeze the critical width rule and a representation-matched ordered-point null independently of confirmation data, calibrate the tent-weighted short-gap functional under that null, and ask whether the prime configuration has a stable residual across growing scales. A residual is not informative merely because it survives grid shifts; it must survive the local-intensity/gap structure already encoded by the null. Only then should the result be translated back through the signed prime-phase kernel.