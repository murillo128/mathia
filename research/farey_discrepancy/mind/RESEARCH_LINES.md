# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Separate source-side rigidity from the exact observation threshold

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-033-matched-horizon-mode-dilation-is-divisor-transport-not-new-arithmetic-information`.

Prime-extension energy is the exact source-side relation currency. For a squarefree-supported source `a`, with `delta=a-mu`, the quantities `D_(a,q)` and `M_(a,q)` measure coefficient displacement and prime-extension inconsistency. FD-187--FD-188 show that on the physical-prime fibre, subcritical relation energy plus sublinear coefficient mass forces `a=mu`; source-side arithmetic rigidity is therefore available once the observation exposes those currencies.

FD-189--FD-194 make the dyadic signed-Fourier observation threshold exact. At a geometric horizon `H=B^m`, modes through `k<=c sqrt(H)` cover every sufficiently large source coordinate exactly when `c>=sqrt(B)`. For dyadic horizons the sharp constant is `sqrt(2)`. Below that constant there are permanent quotient holes; at and above it there is an explicit cumulative inverse.

FD-191 closes the formerly open power endpoint under strong coordinatewise Möbius fidelity: at `alpha=1/2`, dyadic Fourier bands still admit exact null perturbations on composite squarefree coordinates even when all primes and all nonsquarefree coordinates are fixed. Together with FD-190, every `alpha<=1/2` remains noninjective in that class. FD-192 strengthens the consequence: such square-root-and-below nulls can hide order-one coefficient discrepancies and critical prime-extension energy of order `x/log x`. Coordinatewise fidelity alone therefore cannot recover the relation currency needed by FD-187--FD-188.

FD-193--FD-194 provide the complementary positive theorem. For geometric horizons, `c>=sqrt(B)` is not merely a coverage condition: the cumulative source has an explicit inverse with uniform error control. Under raw Fourier `l_infinity` noise, cumulative reconstruction has amplification at most one and coefficient increments at most two; below the threshold no inverse exists. The square-root transition is therefore a geometry/injectivity threshold rather than a conditioning pathology.

FD-195 adds a topology-sensitive warning at exactly this point. For the classical Franel/GCD quadratic energy, the dual cost of one geometric quotient witness is `C_(H,k)=Theta(1)`, even though the raw signed-Fourier inverse row for the same witness contracts like `2^omega(k)/k=n^(-1+o(1))`. Stable coordinate recovery and scalar quadratic-energy duality therefore price the same source direction differently. At the geometric horizon `H~n^2`, generic one-horizon Franel duality reaches only the `M(n)=O(n^(1+epsilon))` scale; square-root Mertens would require substantially stronger Franel energy than the RH-equivalent bound supplies.

FD-196 makes that loss exact across the weighted Fourier family `E_(H,sigma)`: a square-root band with energy exponent `gamma` recovers `M(n)=O(n^(gamma+sigma-1+epsilon))`, so the RH-facing line is `gamma+sigma<=3/2`. Classical Franel transfer stays on `gamma+sigma=2` for every `0<=sigma<=1`; changing Sobolev weight alone never recovers the missing half power.

FD-197 shows that the same noncritical line is the exact logarithmic second-moment baseline of a squarefree Rademacher random multiplicative source. On `K~sqrt(H)`, `E E_(H,sigma)^f(K)=H^(2-sigma+o(1))`; in particular the half-Sobolev energy has mean `H^(3/2+o(1))`, not the `H^(1+epsilon)` needed by the FD-196 recovery theorem.

FD-198 sharpens the interpretation of that missing half power. For primes `K/2<p<=K`, the exact centered row identity

`B_H(p)-B_H(1)=p M(floor(H/p))`

puts `Theta(K/log K)` distinct Mertens samples of size `Theta(K)` inside the same positive half-Sobolev budget. If `E_(H,1/2)(K)=H^(gamma+o(1))`, their RMS is `<<K^(gamma-1+o(1))`. Thus the FD-196 critical budget `H^(1+epsilon)` would force subpower RMS on the whole reciprocal-prime shell, whereas the FD-197 random-multiplicative baseline `gamma=3/2` gives the natural square-root RMS. The positive energy is therefore not merely lossy relative to raw inversion: at the RH-facing exponent it is simultaneously much more coercive than the pointwise RH target on a growing sparse family.

FD-199 extends that shell audit across the full weighted family and exposes a genuine centering transition at `sigma=1/2`. For the prime shell, the map from the raw coordinates `(B_H(1),B_H(p))` to the centered rows `B_H(p)-B_H(1)` has exact measurement-space squared norm `1+S_sigma(K)`, where `S_sigma(K)=sum_(K/2<p<=K) p^(-2sigma)`. PNT gives `S_sigma=o(1)` exactly for `sigma>=1/2` (with `S_(1/2)~log(2)/log K`) and `S_sigma~K^(1-2sigma)/log K` below it. Consequently every FD-196 critical energy on `gamma+sigma=3/2` with `sigma>=1/2` forces subpower reciprocal-prime RMS, while for `sigma<1/2` the direct raw-energy comparison gives only `K^(1/2-sigma+o(1))` because the common base row dominates. The exact norm is sharp only in unrestricted measurement-coordinate space; it is not asserted as a source-realizable lower bound.

FD-200 rules out the simplest matched cross-horizon escape. For every cumulative source, not just Möbius, simultaneous prime dilation obeys

`B_(pH)(pk)=B_(pH)(k)+p B_H(k)-p 1_(p|k)B_H(k/p)`.

Along a coprime divisor-closed composite dilation family, matched coordinates and fixed-mode horizon coordinates are related by an invertible Dirichlet convolution. In particular `(B_(pH)(p)-B_(pH)(1))/p=B_H(1)`, so on the physical source every matched ridge `(pH,p)` simply repeats `M(H)`. Cross-horizon information can still matter through common-source incompatibility, but a matched horizon-mode residual carries no Möbius-specific cancellation by itself.

FD-201 tests the complementary fixed-mode direction. For any fixed integer `r>=2` and prime `p`, the cross-horizon difference `D_(r,H)(k)=B_(rH)(k)-B_H(k)` satisfies

`D_(r,H)(p)-D_(r,H)(1)=p[M(floor(rH/p))-M(floor(H/p))]`.

So unlike FD-200, fixed-mode comparison is genuinely source-sensitive and exposes a Möbius sum over a fixed-ratio multiplicative interval. But compressing these differences into the positive half-Sobolev energy `Dcal_(r,H)(K)=sum_(k<=K)|D_(r,H)(k)|^2/k`, with `K~sqrt(H)`, recreates the shellwide tariff: `Dcal_(r,H)(K)=O_epsilon(H^(1+epsilon))` forces subpower RMS for the `Theta(K/log K)` reciprocal-prime interval increments. A squarefree Rademacher multiplicative control already contributes `H^(3/2+o(1))` from the prime shell alone. Fixed-mode cross-horizon information is therefore real, but positive diagonal squaring still erases the sign/correlation structure needed to beat the half-power baseline.

The live question has therefore narrowed further. Positive diagonal weights at or above half-Sobolev inherit shellwide overcoercion on the RH-facing line; weights below half-Sobolev pay a growing rank-one tariff merely to remove `B_H(1)`. Matched horizon-mode dilation is universal divisor transport, while fixed-mode horizon differencing becomes source-sensitive but remains overcoercive after positive diagonal compression. A plausible route should now preserve signs or correlations **before squaring**: signed cross-mode/cross-horizon covariance, a targeted projection with unmatched quotient coordinates, order-sensitive/nonlinear coupling, or another Möbius-specific destination statistic whose gain survives both the universal divisor cocycle and the reciprocal-prime shell benchmark.

## Apply information budgets only after fixing source class, observation family and destination norm

The same Farey representation can be complete, target-rigid or permanently noninjective depending on the source class, observation family and destination norm. Above the geometric square-root constant, stable cumulative inversion is available; below it, exact null directions remain. FD-195--FD-201 show that even above threshold the contraction visible in the raw coordinate inverse need not survive compression to quadratic Farey energy, that the RH-facing positive weighted budgets from half-Sobolev upward simultaneously overcontrol reciprocal-prime Mertens shells, that multiplying horizon and mode together can create only algebraic copies rather than independent source constraints, and that fixed-mode horizon differencing does not remove the same overcoercion once its source-sensitive increments are squared diagonally.

Sample count and algebraic injectivity are not the invariants. What matters is quotient coverage, which cross-coordinate relations the source class forces, whether nominally new coordinates survive exact algebraic transport, the source covariance beyond generic multiplicativity, whether the destination norm preserves sign/cross-mode/cross-horizon structure, and what simultaneous family of source coordinates that norm controls.

Any lower bound should therefore declare whether it concerns unrestricted recovery, one-target testing, pairwise recovery or quotient recovery; the source class and relation graph; the observation/noise topology; and whether support count, weighted amplitude, relation energy, scale coverage, covariance structure or quadratic-energy dual cost is the relevant currency. Only then do bandwidth, rank or inverse modulus have mathematical meaning.

## Keep source coercivity, coordinate inversion and the Franel--Landau destination separate

Stable source recovery above the square-root threshold still does not prove the RH-critical discrepancy estimate. Conversely, FD-187--FD-188 say what a relation-sensitive observation would have to expose: enough control of `D_q` and `M_q` to force the Möbius source without reconstructing every coordinate. FD-195--FD-201 rule out treating the scalar Franel energy, a Sobolev reweighting, generic random multiplicativity, one-row dual recovery, matched horizon-mode replication, or fixed-mode positive cross-horizon energy as a lossless proxy for the contractive raw inverse on geometric quotient witnesses.

The high-value frontier is therefore a deterministic Möbius-specific suppression mechanism with a credible simultaneous interpretation, a signed destination-relevant relation statistic, or cross-horizon structure that compares genuinely different quotient coordinates **without immediately squaring away their correlations**. A wider positive band or more matched copies are not progress by themselves: their source consequences and exact algebraic redundancy must be audited collectively, and below half-Sobolev the common-mode centering cost must also be accounted for.
