# VIS-168 — growing support forces a collision-null mass barrier

## Claim

Keep the anchored held-out-prime Haar control of `VIS-164`. For retained support dimension `d>=1`, write

`R(X)=sqrt(sum_(j=1)^d sin^2(pi X_j))`,

`N(Y)=|sin(pi Y)|`,

`C=N(Y)/R(X)`,

with `X` Haar-uniform on `T^d`, `Y` Haar-uniform on `T`, and

`mu_d(L)=P(C>L)`.

Let

`v_d = pi^(d/2)/Gamma(d/2+1)`

be the volume of the Euclidean unit ball in `R^d`. Then for every `d>=1` and every threshold `L>=1`,

`(2/3) v_d (2 pi L)^(-d) <= mu_d(L) <= v_d (2L)^(-d)`.

Consequently, as `d->infinity`, uniformly for arbitrary `L=L_d>=1`,

`log mu_d(L) = -(d/2) log d - d log L + O(d)`.

Thus a growing-support collision experiment has a population-mass gate before any Diophantine-discrepancy issue appears. If `Q` anchored indices are available, define the matched Haar exceedance mass

`H_Q(d,L)=Q mu_d(L)`.

Then:

1. for every fixed `gamma>0`, if `d=d(Q)->infinity` and `L(Q)=Q^gamma`,

   `H_Q(d(Q),L(Q)) -> 0`;

   hence no relative empirical law of the form

   `F_Q(L(Q)) ~ mu_(d(Q))(L(Q))`

   can hold along all sufficiently large `Q`;

2. for fixed `L>=1` and

   `d(Q) ~ c log Q/log log Q`, `c>0`,

   `log H_Q = (1-c/2+o(1)) log Q`;

   so the matched Haar mass diverges for `c<2` and vanishes for `c>2`;

3. more generally, if

   `L(Q)=Q^(kappa/d(Q))`

   and `d(Q) ~ c log Q/log log Q`, then

   `log H_Q = (1-kappa-c/2+o(1)) log Q`.

Therefore the natural positive-power collision scale under growing support is not `Q^gamma` with fixed `gamma>0`; its exponent must shrink on the order of `1/d`, with an additional high-dimensional volume penalty when `d` approaches `log Q/log log Q`.

**Evidence/status:** `EXACT-DERIVED + HIGH-DIMENSIONAL-MATCHED-NULL + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This is a Haar-population theorem. It is not a growing-dimensional discrepancy theorem for the deterministic prime-log orbit, an extreme-value limit, a source-sensitive zeta separation, or an RH consequence.

## 1. Uniform collision bounds from elementary torus geometry

Represent each torus coordinate by its signed representative `u_j in [-1/2,1/2]`. On this interval,

`2|u_j| <= |sin(pi u_j)| <= pi |u_j|`.

The upper bound follows because `N(Y)<=1`. If `C>L`, then

`R(X)<1/L`.

The lower sine inequality gives

`2 ||u||_2 <= R(X) < 1/L`,

so `u` lies in the Euclidean ball of radius `1/(2L)`. Since `L>=1`, that ball lies inside the signed torus cube. Therefore

`mu_d(L) <= v_d (2L)^(-d)`.

For the lower bound, restrict the held-out coordinate to

`|sin(pi Y)| >= 1/2`,

which has Haar measure `2/3`. If simultaneously

`||u||_2 < 1/(2 pi L)`,

then the upper sine inequality gives

`R(X) <= pi ||u||_2 < 1/(2L)`.

Hence `L R(X)<1/2<=N(Y)`, so `C>L`. The corresponding product set has measure

`(2/3) v_d (2 pi L)^(-d)`.

This proves the two-sided estimate without taking `L->infinity` first and without using the fixed-dimensional tail asymptotic from `VIS-164`.

## 2. High-dimensional volume supplies the dominant support penalty

Stirling's formula gives the standard unit-ball asymptotic

`v_d = (2 pi e/d)^(d/2) / sqrt(pi d) * (1+O(1/d))`.

Taking logarithms in the two-sided collision bounds yields

`log mu_d(L)`
` = -(d/2) log d - d log L + O(d)`

uniformly for `L>=1`. The constants hidden in `O(d)` differ between the upper and lower geometric comparisons but do not depend on `L`.

The `-(d/2) log d` term is separate from the familiar `-d log L` tail penalty. It is the volume cost of asking all `d` retained phases to enter one small Euclidean collision neighborhood at once.

As a consistency check, the fixed-`d`, large-`L` tail coefficient from `VIS-164`,

`c_d = Gamma((d+1)/2)/(pi^((d+1)/2) Gamma(d/2+1)^2)`,

itself satisfies

`c_d ~ [sqrt(2)/(pi d)] [2e/(pi d)]^(d/2)`.

This has the same `-(d/2) log d+O(d)` support penalty. The present joint bound does not rely on exchanging the `L->infinity` and `d->infinity` limits.

## 3. Fixed positive-power thresholds disappear under any unbounded support growth

Take `L(Q)=Q^gamma` with fixed `gamma>0` and `d(Q)->infinity`. Since the unit ball is contained in the cube `[-1,1]^d`, one has `v_d<=2^d`. The upper collision bound therefore gives

`H_Q = Q mu_d(Q^gamma)`
` <= Q v_d (2 Q^gamma)^(-d)`
` <= Q^(1-gamma d)`.

Because `d(Q)->infinity`, the right-hand side tends to zero.

This is stronger than saying that the fixed-support exponent in `VIS-165` deteriorates when support changes. Even an ideal Haar population contains asymptotically less than one exceedance at any threshold `Q^gamma` with fixed positive `gamma` once the support dimension diverges.

There is also an integer-granularity obstruction to a relative empirical tail law in this regime. If

`F_Q(L)=Q^(-1) #{q<=Q:C_q>L}`

satisfied `F_Q(L(Q))/mu_(d(Q))(L(Q))->1`, then the integer exceedance count

`Q F_Q(L(Q))`

would be asymptotic to `H_Q->0`. It would therefore be zero eventually, forcing the ratio to be zero rather than one. Thus a fixed positive collision exponent cannot be transported uniformly to unbounded support by any refinement of the discrepancy estimate alone.

## 4. Fixed thresholds have a `2 log Q/log log Q` support-mass boundary

Now keep `L>=1` fixed and suppose

`d(Q) ~ c log Q/log log Q`.

Then

`d log L = o(log Q)`,

`O(d)=o(log Q)`,

and

`(d/2) log d = (c/2+o(1)) log Q`.

Hence

`log H_Q`
` = log Q + log mu_d(L)`
` = (1-c/2+o(1)) log Q`.

For `c<2`, the matched Haar exceedance mass tends to infinity. This does not prove a deterministic prime-log frequency theorem, but event-count granularity does not obstruct one.

For `c>2`, the matched Haar mass tends to zero. In that regime even a fixed collision threshold becomes too sparse for a relative-frequency approximation to the Haar law. The critical scale `c=2` needs finer terms and is not classified here.

## 5. Dimension-rescaled thresholds expose the correct first-order joint scale

Let

`L(Q)=Q^(kappa/d(Q))`.

Then

`d log L = kappa log Q`.

If again

`d(Q) ~ c log Q/log log Q`,

the uniform logarithmic estimate gives

`log H_Q = (1-kappa-c/2+o(1)) log Q`.

Thus the first-order population-mass boundary is

`kappa + c/2 = 1`.

When `d=o(log Q/log log Q)`, this reduces to the familiar dimension-rescaled extreme scale `L approximately Q^(1/d)` at first order. When support approaches the high-dimensional threshold, the shrinking volume of the collision neighborhood consumes part of that exponent budget.

This identifies a better null coordinate for any future growing-support comparison: freeze either the Haar mass `Q mu_d(L)` itself or the dimension-rescaled threshold exponent `kappa=d log L/log Q`, rather than comparing raw collision thresholds across changing support.

## 6. Prior art and novelty boundary

The ingredients are classical and elementary: the chord bounds for `sin`, Euclidean ball volume, and Stirling's formula. High-dimensional small-ball decay and the volume asymptotic of the Euclidean unit ball are standard facts; no new probability or geometry theorem is claimed.

The Mathia-specific content is the specialization to the anchored held-out-prime collision null of `VIS-164` and the resulting experimental-design obstruction. `VIS-165`--`VIS-167` established quantitative fixed-support discrepancy, tail, and capped-moment transfer. The present result shows that before trying to make those estimates uniform in support, the Haar target itself changes regime: fixed positive-power thresholds become empty, and even fixed thresholds cross a population-mass wall near `2 log Q/log log Q` retained dimensions.

No prior-art novelty claim is made for the asymptotic threshold. It is retained because it materially changes how the accepted prime-phase clue must formulate any growing-support test.

## 7. Boundaries and falsification

The bounds use the exact anchored collision observable and the chordal Euclidean denominator from `VIS-162`--`VIS-164`. A different metric, anchor, or singularity geometry can change the dimension penalty and must be recalibrated.

`H_Q=Q mu_d(L)` is a matched Haar population mass, not the actual deterministic exceedance count. `H_Q->infinity` is only a necessary statistical room condition for a stable relative-frequency comparison, not a discrepancy theorem. Uniform deterministic control still has to overcome the changing dimension, prime-log Diophantine constants, and boundary complexity identified in `VIS-165`--`VIS-167`.

The vanishing-mass conclusions are stronger: when `H_Q->0`, a relative empirical law `F_Q~mu_d` is impossible by integer granularity, regardless of how strong the deterministic discrepancy machinery becomes.

Falsify the geometric bound by finding a signed torus point violating `2|u|<=|sin(pi u)|<=pi|u|` on `[-1/2,1/2]`, or by showing that the collision event does not imply the stated Euclidean small-ball containment. Falsify the phase calculations by exhibiting an error in the unit-ball Stirling asymptotic or in the substitution of the proposed support/threshold scales.

## Research consequence

Growing support does not preserve the fixed-support collision scale. Any future zeta-versus-held-out-prime experiment must first pass a **null-mass gate**: choose support and threshold growth so that the matched Haar collision mass is not already asymptotically empty.

In particular, fixed positive-power thresholds `Q^gamma` are ruled out once support grows without bound. The natural first-order normalization is dimension-rescaled, with thresholds on the scale `Q^(kappa/d)` and an additional support-volume penalty near `d approximately 2 log Q/log log Q`. Only after this population gate is satisfied does it make sense to spend effort on uniform prime-log discrepancy or a source-sensitive zeta separation.