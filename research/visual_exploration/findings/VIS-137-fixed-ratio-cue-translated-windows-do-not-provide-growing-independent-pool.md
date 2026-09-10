# VIS-137 — fixed-ratio translated CUE tents do not supply a growing independent source-window pool

## Claim

Continue the bounded-source CUE support-edge construction of `VIS-130`--`VIS-136`. Let

`a_alpha(theta)=(1-|theta|/(pi alpha))_+`,

with fixed `alpha in (0,1)`, and let `b_alpha` be its Fourier coefficient function

`b_alpha(xi)=(1/(2 pi)) integral a_alpha(theta) exp(-i xi theta) dtheta`.

For two source centers `c,d` whose tent supports lie in one common non-wrapping chart, put `delta=d-c`, let

`t_(N,v)=N+rho_N v`,  `rho_N=N/L -> rho>0`,

and define the locally phased translated amplitude

`Z_(N,v,c)=sum_j a_(alpha_N)(theta_j-c) exp(i t_(N,v)(theta_j-c))`,

where `alpha_N=M/N -> alpha`. With `H_2=M/3` and

`X_(N,v,c)=[Z_(N,v,c)-E Z_(N,v,c)]/sqrt(H_2)`,

remove the irrelevant carrier gauge by

`Y_(N,v,c)=exp(i N c) X_(N,v,c)`.

Then, for fixed `v,w,c,d`,

`E[Y_(N,v,c) overline{Y_(N,w,d)}] -> K_(alpha,rho,delta)(v,w)`,

where

`K_(alpha,rho,delta)(v,w)`
` = (3/alpha) sum_(n in Z) b_alpha(n-rho v)b_alpha(n-rho w) exp(i n delta)`

and, under the same common-chart condition,

`K_(alpha,rho,delta)(v,w)`
` = [3 exp(i rho(v+w)delta/2)/(2 pi alpha)]`
`   * integral_R a_alpha(x+delta/2)a_alpha(x-delta/2)`
`       `exp(i rho(v-w)x) dx`.

Thus the leading cross-window covariance is the Fourier transform of the **actual overlap of the two translated source tents**. In particular,

`K_(alpha,rho,delta)(v,w)=0`

whenever the two tent supports are disjoint, equivalently `|delta|>=2 pi alpha` in the common chart.

The bounded-determinantal cumulant estimate used in `VIS-135` applies unchanged to any fixed finite collection of translated windows. Hence the translated terminal packets are jointly proper complex Gaussian in the same finite-dimensional sense, and their centered intensity covariance satisfies

`Cov(I_(N,c)(v), I_(N,d)(w)) -> |K_(alpha,rho,delta)(v,w)|^2`,

where `I_(N,c)(v)=|X_(N,v,c)|^2-E|X_(N,v,c)|^2`. The same conclusion passes through the fixed Montgomery/Laplace smoothing. Therefore pairwise-disjoint translated tents are asymptotically decorrelated at the leading order of the frozen finite-CUE null.

However, each tent occupies angular length `2 pi alpha`. A single CUE circle can contain at most

`floor(1/alpha)`

pairwise-disjoint such supports. With `alpha_N -> alpha>0`, this bound stays `O(1)` as `N,L -> infinity`. Consequently, **one fixed-ratio CUE realization cannot provide the growing `m`-window asymptotic required by `VIS-136` merely by translating the same source taper around the circle**.

To obtain `m -> infinity`, one must instead shrink the source fraction `alpha_N -> 0`, use additional independent CUE realizations, or introduce a separate cross-height/cross-window model for the zeta process. Each choice changes the null or scaling regime and requires its own covariance/transfer argument.

**Evidence/status:** `EXACT-DERIVED + ASYMPTOTIC CUE TRANSLATION CONTROL + NEGATIVE AVERAGING CONTROL + CLASSICAL TRACE/CUMULANT INGREDIENTS + NO-NOVELTY-CLAIM`.

This result does not determine the covariance law of separated Riemann-zero height windows and does not show that zeta windows are independent, mixing, stationary, or finite-CUE distributed at the `1/L` scale.

## 1. Translation only adds a Fourier phase to the terminal packet

For the translated local-phase test function

`f_(N,v,c)(theta)=a_(alpha_N)(theta-c) exp(i t_(N,v)(theta-c))`,

the Fourier coefficient at integer `k` is

`hat f_(N,v,c)(k)=exp(-i k c) b_(alpha_N)(k-t_(N,v))`.

The exact CUE trace covariance used in `VIS-133` therefore gives

`Cov(Z_(N,v,c), overline{Z_(N,w,d)})`
` = sum_(k in Z, k!=0) min(N,|k|)`
`     `b_(alpha_N)(k-t_(N,v)) b_(alpha_N)(k-t_(N,w)) exp(i k delta)`.

Write `k=N+n`. Because `b_alpha(xi)=O((1+|xi|)^-2)`, the same dominated-convergence argument as in `VIS-133` isolates the terminal packet. After division by `N` and removal of the carrier phase `exp(i N delta)`,

`N^-1 exp(-i N delta)`
` Cov(Z_(N,v,c), overline{Z_(N,w,d)})`
` -> sum_(n in Z) b_alpha(n-rho v)b_alpha(n-rho w) exp(i n delta)`.

Since `H_2~alpha N/3`, this proves the first formula for `K`.

The translation does not create a new stochastic degree of freedom. It rotates the same terminal Fourier packet by the deterministic phase `exp(i n delta)`.

## 2. Poisson summation turns the packet covariance into tent overlap

Insert

`b_alpha(n-rho v)`
` = (1/(2 pi)) integral a_alpha(theta)`
`     `exp(-i(n-rho v)theta) dtheta`

and the corresponding expression for `w`. Summing over `n` gives the periodic Dirac comb. Under the common non-wrapping chart assumption only the central copy intersects both compact tent supports, so

`sum_n b_alpha(n-rho v)b_alpha(n-rho w) exp(i n delta)`
` = [exp(i rho w delta)/(2 pi)]`
`   `integral a_alpha(theta)a_alpha(delta-theta)`
`      `exp(i rho(v-w)theta) dtheta`.

Because the tent is even, shift `theta=x+delta/2` to obtain

`= [exp(i rho(v+w)delta/2)/(2 pi)]`
`  `integral a_alpha(x+delta/2)a_alpha(x-delta/2)`
`     `exp(i rho(v-w)x) dx`.

At `delta=0` this reduces exactly to the covariance kernel `R_(alpha,rho)(v-w)` of `VIS-133`. For nonzero separation it has an immediate geometric interpretation: only the overlap of the translated source tapers contributes at leading order.

If `|delta|>=2 pi alpha`, the supports of `a_alpha(x+delta/2)` and `a_alpha(x-delta/2)` are disjoint, so the integral vanishes identically for every fixed `v,w`. The boundary case has only measure-zero contact and gives the same zero integral.

## 3. Joint Gaussianity propagates the overlap law to the quadratic statistic

The proof of `VIS-135` uses only that the CUE correlation operator has rank `N`, the relevant test functions are uniformly bounded, and `H_2=Theta(N)`. Translating the tent preserves all three properties. Therefore every fixed mixed cumulant of order `p>=3` for a finite collection of translated normalized amplitudes is still

`O(N^(1-p/2))`.

The cross-window pseudocovariance remains `o(1)` for the same terminal-frequency reason as in `VIS-135`: the two nonconjugated high-frequency packets cannot simultaneously meet the same CUE trace mode at order `N`.

Hence the finite translated packet is asymptotically proper complex Gaussian with conjugate covariance `K`. Wick's rule then gives

`Cov(I_(N,c)(v),I_(N,d)(w)) -> |K_(alpha,rho,delta)(v,w)|^2`.

For the Montgomery-smoothed field

`J_(N,c)(v)=integral exp(-2|u|) I_(N,c)(v+u) du`,

dominated convergence gives the cross-window limit

`integral integral exp(-2|u|-2|s|)`
`  `|K_(alpha,rho,delta)(v+u,w+s)|^2 du ds`.

Thus disjoint source supports kill the leading same-realization cross-window covariance even after the fixed support-edge smoothing. Overlapping windows, by contrast, share a nonzero terminal packet unless a separately proved contrast cancellation removes it.

## 4. Fixed-ratio packing blocks an asymptotically growing disjoint pool

The previous section might suggest using many translated, pairwise-disjoint CUE source windows to realize the `m`-window average in `VIS-136`. The circle geometry prevents that in the frozen regime.

Each tent support has angular measure `2 pi alpha+o(1)`. If `m_N` source supports are pairwise disjoint, then

`m_N (2 pi alpha_N) <= 2 pi`,

so

`m_N <= 1/alpha_N`.

As `alpha_N -> alpha>0`, the right-hand side stays bounded. There is therefore no sequence of pairwise-disjoint fixed-ratio windows with `m_N -> infinity` inside one CUE realization.

This does not prove that averaging overlapping translations is useless. Dense or structured translation averages can project onto special center-frequency modes and may have cancellation. But that is exactly the kind of nontrivial low-frequency mechanism singled out by `VIS-136`; it must be derived rather than counted as additional independent samples.

Likewise, taking independent CUE matrices makes windows independent by construction, but that changes the experiment from repeated windows of one spectrum to repeated ensemble realizations. It cannot by itself justify the dependence law of height windows cut from the single Riemann-zero sequence.

## Prior-art and novelty assessment

The CUE trace covariance formula for linear eigenvalue statistics is classical and is already anchored for this line by Persi Diaconis and Steven N. Evans, **Linear functionals of eigenvalues of random matrices**, *Transactions of the American Mathematical Society* 353:7 (2001), 2615--2633, DOI `10.1090/S0002-9947-01-02800-8`. `VIS-133` uses precisely that machinery for the unshifted terminal tent packet.

The determinantal cumulant method and Gaussian-limit mechanism are likewise classical and already anchored by Alexander Soshnikov, **Gaussian Limit for Determinantal Random Point Fields**, *Annals of Probability* 30:1 (2002), 171--187, DOI `10.1214/aop/1020107764`, together with the modern cumulant discussion cited in `VIS-135`.

Translation of a test function, Poisson summation, compact-support overlap, and the packing bound are elementary harmonic/geometric consequences. No novelty is claimed for those general ingredients. The Mathia-specific role of this finding is to apply them to the exact fixed-ratio terminal-frequency source convention frozen by `VIS-130`--`VIS-136` and to close a concrete ambiguity in the proposed source-window averaging strategy.

## Boundary and falsification

The asymptotic covariance formula assumes a fixed source fraction `alpha_N -> alpha in (0,1)`, fixed scaled edge coordinates, and translated tents whose relevant pair can be represented in one common non-wrapping chart. If the source fraction shrinks, the centers or edge-coordinate family scale with `N`, or the source window wraps the coordinate cut, the packet/alias calculation must be redone in that regime.

The disjoint-support conclusion is leading-order after normalization. It does not claim exact finite-`N` independence of disjoint CUE arcs; global CUE constraints can leave lower-order dependence. It also does not claim that every overlapping-window average has a positive long-run variance: specially designed translation contrasts may produce center-frequency cancellation and must be analyzed explicitly.

Most importantly, CUE translation is not zeta height translation. A single CUE circle is only the matched finite-size null used by the current support-edge thread. The actual zeta question requires a justified model or theorem for covariance across height windows, including local unfolding, counting-function fluctuations, effective-size drift, overlap, and finite-height transfer at the target `1/L` scale.

## Research consequence

`VIS-136` reduces averaging feasibility to the low-frequency covariance law of the source-window sequence. This finding rules out one easy way of manufacturing that sequence: the fixed-ratio finite-CUE null itself does not contain an asymptotically growing family of pairwise-disjoint translated source windows.

The next coherent gate should therefore specify the **cross-height ensemble** rather than continue slicing one CUE circle. Either derive the covariance of the frozen zeta height-window statistic directly, or introduce a multi-block/random-matrix surrogate with an explicit separation/dependence law and then prove why that surrogate transfers to zeta at the `1/L` scale. Independent CUE realizations may calibrate per-window variance, but they are not evidence for zeta-window independence.