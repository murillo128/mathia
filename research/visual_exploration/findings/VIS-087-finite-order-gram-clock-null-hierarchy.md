# VIS-087 — every fixed sublinear Gram power scale has a finite-order clock null

## Claim

Let `g_n` be the sufficiently large Gram points defined by

`theta(g_n)=pi n`,

up to the harmless conventional integer shift, and let `G(u)` denote the eventual smooth inverse of

`theta(G(u))=pi u`.

Fix an integer `m>=1`. For `0<=h<=H_n`, put

`Delta_(n,h)=g_(n+h)-g_n`

and define the degree-`m` inverse-theta Taylor arc

`T_(m,n)(h)=sum_(j=1)^m G^(j)(n) h^j/j!`.

For primes `p<=P_n`, define the corrected prime-phase residual

`R_(m,n,h)(p)`
` = exp(-i log p [Delta_(n,h)-T_(m,n)(h)]).`

Then, with the implied constant depending only on the fixed order `m`,

`max_(h<=H_n) max_(p<=P_n) |R_(m,n,h)(p)-1|`
` <<_m H_n^(m+1) log P_n / [g_n^m (log g_n)^(m+2)]`.

Consequently, whenever

`H_n^(m+1) log P_n = o(g_n^m (log g_n)^(m+2))`,

the degree-`m` corrected prime-phase field collapses uniformly to the identity.

For fixed prime support this includes every

`H_n=o(g_n^(m/(m+1)) (log g_n)^((m+2)/(m+1)))`,

while for polynomial support `P_n<=g_n^A` with fixed `A` it includes every

`H_n=o(g_n^(m/(m+1)) log g_n)`.

In particular, for polynomial prime support, **every fixed sublinear power scale is eventually covered by some fixed finite-order deterministic Gram-clock null**: given any fixed `alpha<1` and fixed real `B`, choose `m` with `alpha<m/(m+1)`; then

`H_n=O(g_n^alpha (log g_n)^B)`

lies inside the degree-`m` collapse corridor.

Thus the successive linear and quadratic controls in `VIS-085` and `VIS-086` are the first two members of a general finite-order hierarchy. Merely moving a Gram/prime-phase visualization to a larger but fixed sublinear power-law block cannot by itself escape deterministic sampling geometry.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-RIEMANN-SIEGEL-ASYMPTOTICS COROLLARY + NEGATIVE/CONTROL + NO-NOVELTY-CLAIM`.

No statement is made for order `m=m(n)` growing with height, nearly linear blocks such as `g_n/log g_n`, genuinely nonlocal Gram sampling, growing-dimensional Haar laws, zeta approximation, prime/zero independence, or RH.

## 1. The theta derivatives have a uniform classical scale

The classical Riemann-Siegel theta asymptotic expansion gives

`theta'(t) asymp log t`

for large `t`. Differentiating the fixed-order asymptotic expansion gives, for every fixed integer `r>=2`,

`theta^(r)(t)=O_r(t^(1-r))`.

The first cases are the estimates already used in `VIS-085` and `VIS-086`:

`theta''(t)=1/(2t)+O(t^(-3))`,
`theta'''(t)=-1/(2t^2)+O(t^(-4))`.

Richard P. Brent's rigorous remainder bounds for the Riemann-Siegel theta expansion and R. B. Paris's refined theta asymptotics are sufficient classical anchors for these fixed-order derivative scales. Nothing in the present argument needs a new theta expansion.

Since `theta'` is eventually positive, `G` is smooth on a final half-line.

## 2. Inverse-theta derivatives form a fixed-order hierarchy

Differentiating

`theta(G(u))=pi u`

once gives

`G'(u)=pi/theta'(G(u))=O(1/log G(u))`.

For every fixed `r>=2`,

`G^(r)(u)=O_r(G(u)^(1-r) (log G(u))^(-(r+1))).`

This follows inductively from the ordinary Faà di Bruno formula. After differentiating the inverse identity `r` times, isolate

`theta'(G) G^(r)`.

Every remaining monomial has the form

`theta^(k)(G) product_(j=1)^(r-1) (G^(j))^(m_j)`

with `k>=2`,

`sum_j m_j=k`,
`sum_j j m_j=r`.

Use

`theta^(k)(G)=O_k(G^(1-k))`,
`G'=O((log G)^(-1))`,

and the inductive bound for every `G^(j)`, `j>=2`. The powers of `G` in each monomial combine exactly to `G^(1-r)`. Its logarithmic factor is at most `(log G)^(-r)`; terms containing a higher inverse derivative are smaller in this bookkeeping. Dividing by `theta'(G) asymp log G` gives the displayed bound for `G^(r)`.

The cases `r=2` and `r=3` recover the derivative scales underlying the linear and quadratic remainders in `VIS-085` and `VIS-086`.

## 3. Taylor inversion gives the uniform block remainder

For fixed `m`, Taylor's theorem applied to the real smooth inverse `G` gives, for each `h>=0`,

`Delta_(n,h)-T_(m,n)(h)`
` = G^(m+1)(xi_(n,h)) h^(m+1)/(m+1)!`

for some `xi_(n,h)` between `n` and `n+h`.

Because `G` is increasing and `xi_(n,h)>=n`, the fixed-order inverse-derivative estimate gives uniformly for all `h>=0`

`|G^(m+1)(xi_(n,h))|`
` <<_m 1/[g_n^m (log g_n)^(m+2)].`

Hence

`max_(h<=H_n) |Delta_(n,h)-T_(m,n)(h)|`
` <<_m H_n^(m+1)/[g_n^m (log g_n)^(m+2)].`

This is a one-sided deterministic estimate. It does not require first assuming that `H_n` is logarithmic or a small fixed power of `g_n`; the useful scale is determined by whether the resulting normalized remainder tends to zero.

## 4. Prime phases add only the logarithmic support factor

For real `y`,

`|exp(-iy)-1|<=|y|`.

Therefore every prime `p<=P_n` satisfies

`|R_(m,n,h)(p)-1|`
` <= log p |Delta_(n,h)-T_(m,n)(h)|`
` <<_m H_n^(m+1) log P_n/[g_n^m(log g_n)^(m+2)].`

Taking maxima proves the main bound.

For polynomial support `P_n<=g_n^A`, `log P_n=O(log g_n)`, so collapse follows from

`H_n^(m+1)=o(g_n^m (log g_n)^(m+1))`,

which is equivalent to

`H_n=o(g_n^(m/(m+1)) log g_n)`.

Now fix any `alpha<1` and any fixed real `B`. Choose a fixed integer `m` with

`alpha<m/(m+1)`.

Then

`g_n^alpha (log g_n)^B / [g_n^(m/(m+1)) log g_n] -> 0`,

so every block `H_n=O(g_n^alpha(log g_n)^B)` is swallowed by that finite-order null.

## 5. What this closes and what remains open

`VIS-084` showed local freezing and the first linear Gram arc. `VIS-085` showed that first-order inverse-theta subtraction collapses the prime-phase residual through the square-root corridor for polynomial support. `VIS-086` pushed the same deterministic explanation through the two-thirds-power corridor by subtracting quadratic clock curvature.

The present result shows that those are not isolated thresholds. For each fixed order, the deterministic clock Taylor polynomial pushes the coordinatewise null to the next exponent `m/(m+1)`, and the exponents approach one.

This kills an entire family of visual false positives: if a proposed Gram/prime-phase pattern lives on a block of fixed scale `g_n^alpha` with `alpha<1` (even with any fixed logarithmic factor) and uses only polynomially many prime frequencies, failure of a lower-order correction is not evidence of arithmetic structure. A sufficiently high but still fixed inverse-theta correction forces the phase residual to collapse.

The result does **not** justify sending `m` to infinity with `n`; the constants in the fixed-order derivative bounds are not controlled uniformly in `m`. It also does not control nearly linear or linear Gram blocks, nonlocal rearrangements of Gram indices, observables whose sensitivity grows with the prime dimension, or any additional analytic coordinate such as `Z(g_n)`, Gram occupancy, zero locations, or derivatives.

Those are genuinely different frontiers rather than automatic continuations of the finite-order local-clock argument.

## Prior art and novelty assessment

The Riemann-Siegel theta expansion, its rigorous remainder control, and coarse inversion for Gram points are classical. Richard P. Brent, **On the Accuracy of Asymptotic Approximations to the Log-Gamma and Riemann-Siegel Theta Functions**, *Journal of the Australian Mathematical Society* 107:3 (2019), 319-337, DOI `10.1017/S1446788718000393`, gives rigorous theta asymptotic error bounds. R. B. Paris, **Refined asymptotics of the Riemann-Siegel theta function**, *Bulletin of Kerala Mathematics Association* 16:2 (2020), 17-27, gives a refined large-`t` expansion. Standard Gram-point computation inverts `theta(g_n)=pi n`, often using the leading Lambert-`W` approximation and Newton refinement.

The derivative induction above is ordinary inverse-function/Faà di Bruno calculus applied to those classical asymptotics. A targeted search for higher-order Gram-point and inverse-theta asymptotics found no basis for presenting the displayed hierarchy as a new general theorem. **No novelty is claimed for the analytic asymptotic statement.**

The durable Mathia result is the control interpretation: the entire family of fixed sublinear power-law Gram/prime-phase visual scales with polynomial prime support is contained in finite-order deterministic sampling geometry.

## Boundary and falsification

For each fixed `m`, the collapse conclusion requires

`H_n^(m+1) log P_n=o(g_n^m(log g_n)^(m+2))`.

Outside that corridor the estimate gives no lower bound. In particular, it does not show that a residual survives at the boundary or beyond it.

Falsify the claim by breaking the fixed-order theta derivative bounds, the inverse-derivative induction, the Taylor remainder estimate, or the elementary phase chord inequality. A counterexample would need to invalidate one of those deterministic steps; a visually nonzero finite-height residual is not enough.

## Visual consequence

No canonical PNG is retained. The theorem classifies the whole finite-order family more sharply than any finite set of rendered Gram blocks. A plot at one chosen order or height would risk making an artificial corridor boundary look structurally distinguished when the point of the result is that every fixed finite order has another deterministic successor.

## Research consequence

The accepted `CLUE-zeta-prime-phase-recursive-geometry` should no longer treat a general finite-order inverse-theta hierarchy as an open escape test. For polynomial prime support, any purely local Gram/prime-phase route on a fixed sublinear power scale must first quotient the appropriate finite-order sampling clock and will then collapse coordinatewise.

A surviving route must instead reach a genuinely different regime: nearly linear/nonlocal Gram sampling with a separately justified null, an observable whose growing-dimensional sensitivity escapes the coordinatewise metric, or an independently informative analytic coordinate/source law.