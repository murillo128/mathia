# VIS-088 — polynomial-sensitivity observables inherit the finite-order Gram-clock null

## Claim

Use the notation of `VIS-087`. For fixed `m>=1`, let

`R_(m,n,h)(p)=exp(-i log p [g_(n+h)-g_n-T_(m,n)(h)])`

for `0<=h<=H_n` and primes `p<=P_n`, and regard the whole corrected block as one point

`R_(m,n)=(R_(m,n,h)(p))_(h,p)`

in the finite product torus. Give that product the chord sup metric

`d_infty(z,w)=max_(h,p) |z_(h,p)-w_(h,p)|`.

Let `E_n` be any normed space and let

`F_n : (S^1)^({0,...,H_n} x {p<=P_n}) -> E_n`

be a possibly `n`-dependent observable with Lipschitz constant `Lambda_n` for `d_infty`:

`||F_n(z)-F_n(w)|| <= Lambda_n d_infty(z,w)`.

Then `VIS-087` immediately lifts from coordinatewise phase collapse to the full observable:

`||F_n(R_(m,n))-F_n(1)||`
` <<_m Lambda_n H_n^(m+1) log P_n / [g_n^m (log g_n)^(m+2)].`

Consequently, the observable collapses to its deterministic clock-null value whenever

`Lambda_n H_n^(m+1) log P_n`
` = o(g_n^m (log g_n)^(m+2)).`

For polynomial prime support `P_n<=g_n^A`, take fixed real exponents `alpha<1`, `B`, `kappa>=0`, and `D`, and suppose

`H_n=O(g_n^alpha (log g_n)^B)`,
`Lambda_n=O(g_n^kappa (log g_n)^D)`.

Choose any fixed integer `m` satisfying

`m(1-alpha) > alpha+kappa`.

Then

`||F_n(R_(m,n))-F_n(1)|| -> 0`.

Thus **polynomial growth of the observable's total sensitivity does not escape the finite-order Gram-clock hierarchy on any fixed sublinear power-law block**. Raising the prime dimension, block dimension, or an unnormalized aggregation by a fixed polynomial amount can be absorbed by choosing a sufficiently high but still fixed clock order.

**Evidence/status:** `EXACT-DERIVED + ELEMENTARY-LIPSCHITZ COROLLARY OF VIS-087 + NEGATIVE/CONTROL + NO-NOVELTY-CLAIM`.

This does not cover nearly linear/nonlocal Gram blocks, observables with super-polynomial Lipschitz sensitivity, discontinuous threshold/binning rules without a separation margin, growing Taylor order `m=m(n)`, additional analytic source coordinates, zeta approximation, or RH.

## 1. Coordinatewise collapse controls any Lipschitz block observable

`VIS-087` proves, for every fixed `m`,

`d_infty(R_(m,n),1)`
` <<_m H_n^(m+1) log P_n/[g_n^m(log g_n)^(m+2)].`

No additional number theory is required to pass from this metric statement to an observable. By the definition of the Lipschitz constant,

`||F_n(R_(m,n))-F_n(1)||`
` <= Lambda_n d_infty(R_(m,n),1)`.

Substituting the `VIS-087` bound gives the claimed estimate.

The point is that `Lambda_n` records exactly the loophole left open by coordinatewise convergence. If an observable combines more coordinates as height grows, its sensitivity to a uniform coordinate perturbation may also grow. The relevant question is therefore not dimension by itself but whether that total sensitivity can outrun the deterministic phase-collapse rate.

## 2. Every fixed polynomial sensitivity budget is swallowed on a fixed sublinear power scale

Assume `P_n<=g_n^A`, so `log P_n=O(log g_n)`. Under

`H_n=O(g_n^alpha(log g_n)^B)`

and

`Lambda_n=O(g_n^kappa(log g_n)^D)`,

the observable error is

`O_m(g_n^(kappa+alpha(m+1)-m)`
`      (log g_n)^(D+B(m+1)-m-1)).`

The exponent of `g_n` is

`kappa+alpha-m(1-alpha)`.

For fixed `alpha<1` and fixed `kappa`, choose a fixed `m` with

`m(1-alpha)>alpha+kappa`.

The power of `g_n` is then strictly negative, so it dominates every fixed logarithmic factor and the observable error tends to zero.

This strengthens the interpretation of `VIS-087`. There, increasing dimension was left as a formal possibility because coordinatewise convergence alone does not control arbitrary functions of a growing vector. The present estimate shows that **ordinary polynomial sensitivity is not enough**. A genuine escape through dimension must either have sensitivity growing faster than every fixed polynomial allowed by the chosen scale, or leave the Lipschitz regime in a mathematically consequential way.

## 3. What kinds of visual statistics are covered

The theorem is deliberately stated through a sensitivity budget rather than a particular plot.

A normalized average of corrected coordinates has `Lambda_n=O(1)` in the sup metric. More generally, for a coordinate-separable complex statistic

`F_n(z)=sum_j a_(n,j) f_(n,j)(z_j)`

with each `f_(n,j)` having chord-Lipschitz constant `L_(n,j)`, one may take

`Lambda_n <= sum_j |a_(n,j)| L_(n,j)`.

Hence unnormalized sums are also covered whenever their total coefficient/sensitivity mass grows only polynomially in `g_n`. Since the number of block coordinates is at most

`(H_n+1) P_n`,

it is itself polynomial for polynomial `P_n` and fixed sublinear power-law `H_n`. Any coordinatewise construction with polynomially bounded per-coordinate sensitivity therefore still has a polynomial total sensitivity budget.

The same reasoning applies to vector-valued summaries, filtered images, or finite compositions of maps whenever their operator/Lipschitz constants can be bounded polynomially. What matters is the norm in which the claimed visual or statistical separation is supposed to survive.

A hard threshold, sign, exact bin membership, nearest-neighbor identity, or another discontinuous readout is different. An arbitrarily small phase perturbation can change such an output when the input lies arbitrarily close to the decision boundary. Such a statistic is not rescued merely by being visually striking: it needs a separately proved margin/stability statement before a finite-height difference can be interpreted as information beyond the clock null.

## 4. What remains genuinely open

This result does not close every growing-dimensional route. It closes the broad class for which the whole block observable has a fixed-polynomial Lipschitz sensitivity budget on a fixed sublinear power-law block.

A surviving Gram/prime-phase route must therefore do at least one of the following:

- enter a nearly linear or genuinely nonlocal sampling regime not covered by the fixed-sublinear hierarchy;
- exhibit a super-polynomial sensitivity mechanism and justify why that amplification is mathematically meaningful rather than an unstable threshold artifact;
- prove a non-Lipschitz statistic has a robust separation margin under the relevant null;
- use prime support outside the admitted polynomial regime with its own quantitative control; or
- add an independently informative analytic source coordinate not determined by the corrected prime-phase block.

Failure of the present upper bound outside those conditions is not positive evidence.

## Prior art and novelty assessment

The abstract step used here is the defining metric inequality for a Lipschitz map on a finite product space; controlling a coordinate-separable map by the sum of its coordinate sensitivities is standard elementary analysis. Lipschitz-function spaces and sup product metrics are classical objects, and no novelty is claimed for those facts.

The number-theoretic input is exactly the already audited fixed-order inverse-theta estimate in `VIS-087`. No new asymptotic for Gram points, the Riemann-Siegel theta function, or prime phases is asserted here.

The durable Mathia contribution is the control interpretation obtained by composing these two elementary pieces: the apparent growing-dimensional loophole after `VIS-087` survives only when the observable's sensitivity itself outruns every admitted fixed-polynomial budget, or when the sampling/source law changes.

## Boundary and falsification

The claim is only as strong as the chosen metric and sensitivity bound. To falsify an application, show that the proposed `F_n` is not Lipschitz in the stated norm with the claimed `Lambda_n`, that its actual sensitivity grows faster than assumed, or that the underlying phase block lies outside the `VIS-087` corridor used to obtain `d_infty(R_(m,n),1)`.

A scalar statistic may have a small Lipschitz constant even in very high dimension; conversely, a bounded-valued statistic may be discontinuous. Dimension or output range alone does not determine the sensitivity budget.

The theorem gives an upper bound only. When `Lambda_n d_infty(R_(m,n),1)` does not tend to zero, no surviving signal is implied.

## Visual consequence

No canonical PNG is retained. A finite plot can illustrate accumulation of small coordinate errors, but the theorem classifies the entire polynomial-sensitivity family directly and more reliably than a selected rendering. Retaining a plot would risk making one arbitrary dimension or threshold appear distinguished.

## Research consequence

`CLUE-zeta-prime-phase-recursive-geometry` should no longer treat generic growing-dimensional sensitivity as an open escape from the finite-order Gram-clock null. On fixed sublinear power-law Gram blocks with polynomial prime support, every observable with a fixed-polynomial Lipschitz sensitivity budget is forced to its clock-null value after a sufficiently high fixed-order correction.

The remaining prime-phase frontier is narrower: nearly linear/nonlocal sampling, quantitatively justified super-polynomial or non-Lipschitz amplification, or a genuinely independent analytic coordinate/source law.