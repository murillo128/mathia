---
id: RG-fixed-target-box-inversion-regularity-boundary
type: research-graph-relation
scope: cross-line
derived: true
---

# Fixed-target box inversion and its regularity boundary

[[research/prime_lattice/graph/prime-lattice|Prime Lattice]] · [[research/mobius_cancellation/graph/mobius-cancellation|Möbius Cancellation]] · [[research/graph/atlas/territories/RA-A1-zero-free-regions-pnt-error|Classical analytic territory]]

This projects the explicit dependency chains PL-471 → PL-472 → PL-474 and MC-528 → MC-529 → MC-530, with PL-473's common operator obstruction. Arrows here describe the documented use of earlier work; the findings' existing native links carry the actual source adjacency. It does not identify the prime logarithmic derivative with reciprocal zeta or assert an unrecorded direct implication between PL-474 and MC-530.

## Arithmetic inputs remain distinct

[[research/prime_lattice/findings/PL-471-sparse-zero-annihilators-force-prime-variance-on-every-large-block|PL-471]], Sections 1–3, constructs a fixed mean-zero compact Mellin test from a power-saving off-critical zero count. Its actual mod-5 explicit formula leaves one noncancelling simple logarithmic-derivative pole; original zero multiplicities enter its positive residue weight.

[[research/mobius_cancellation/findings/MC-528-multiplicity-aware-annihilation-forces-mobius-variance-on-every-block|MC-528]], Sections 1–3, explicitly reconstructs that construction with every unwanted zero repeated to full multiplicity. Local division by zeta is an additional growth estimate. The selected reciprocal pole of order `m` leaves a nonzero degree-`m-1` polynomial in `log X`. A simple zero in the test would not cancel a higher-order unwanted reciprocal pole.

[[research/prime_lattice/findings/PL-472-gevrey-box-inversion-reaches-near-linear-prime-windows|PL-472]] proves an order-uniform finite Bernoulli inverse with bounded combined norm. [[research/mobius_cancellation/findings/MC-529-single-near-linear-centered-variance-law-is-equivalent-to-rh|MC-529]] explicitly transfers that inverse to its own reciprocal contour and coefficient pairing. Both reach `H <= X/(log X)^B`, each fixed `B>1`; neither obtains this by substituting a moving exponent into a fixed-power result.

## Attainable side and exact excluded certificate

[[research/prime_lattice/findings/PL-474-nonquasianalytic-tests-close-the-iterated-log-window-boundary|PL-474]] and [[research/mobius_cancellation/findings/MC-530-nonquasianalytic-tests-reach-logarithmic-mobius-windows|MC-530]] independently verify the stronger derivative envelope `C A^n n! log(e+n)^(q n)`, with `1<q<r`, through zero isolation, logarithmic composition and the growing finite inverse. The [[research/prior_art/incremental/PA-nonquasianalytic-infinite-convolution-cutoff|cutoff construction]] is classical. The resulting inverse error is bounded by `C exp(-c/[h log(e+1/h)^q])`, with common compact support, zero mean and bounded combined `L^2` norm.

Given a hypothetical selected zero with real part `beta>1/2` (of multiplicity `m` for reciprocal zeta), for every fixed `r>1` this gives the full empirically centered variance floors on every sufficiently large real block, uniformly for integer `1<=H<=X/[log X (loglog X)^r]`. PL-474's floor is `c H^2 X^(2 beta-1)`; MC-530 retains the additional factor `(log X)^(2m-2)`. Their coefficient-side errors cost respectively `O(X log X)` and `O(X)` times the uniform inverse error. Neither arithmetic explicit formula is applied to the moving inverse.

[[research/prime_lattice/findings/PL-473-box-fourier-zeros-obstruct-logarithmic-window-test-inversion|PL-473]], Sections 1–2, uses the [[research/prior_art/incremental/PA-paley-wiener-ingham-logarithmic-integral|classical Fourier logarithmic integral]] at both signs of the box zeros. At the rounded length `H=floor(X/[log X (loglog X)^r])`, `0<=r<=1`, no integrable inverse family approximates a fixed nonzero compact target with `L^1` error `O(X^(-delta))`, `delta>0`, on all sufficiently large real scales. Inverse tests supported in `[1,2]` also inherit the uniform-norm obstruction. MC-530, Section 4, explicitly checks the same operator and error-norm dictionary. PL-474 and MC-530 construct the previously undecided `r>1` side; convergence of the logarithmic integral alone was not a construction.

## Surviving limits

This closes one fixed-target norm-certificate family, not the variance problem. A variance ceiling with the source's stated strength would imply RH or joint mod-5 GRH even on an unbounded selected scale set, but no such ceiling is acquired. In contrast, the inverse obstruction requires all large scales and does not prohibit specially selected widths. Moving targets, multiple kernels and signed arithmetic sampling-error estimates remain outside it.

Constants and tests encode the full hypothetical zero set. Growing derivative order is not a fixed finite measurement bank, and bounded combined norm is not effective acquisition. No uniform onset near `beta=1/2` or `r=1`, external novelty, independent adversarial approval, formal verification, or unconditional zero-free gain is asserted. The two new findings settle complementary arithmetic instances of the same inspected regularity question; graph links and classical-method registration are maintenance.
