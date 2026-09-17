# MI-051 — Finite-Laplace source capacity grows only logarithmically with the transform rectangle at fixed precision

**Evidence level:** exact conditioning synthesis from [RE-190](../../findings/RE-190-shrinking-euler-sampling-windows-collapse-to-reciprocal-mass-rank-one.md)--[RE-193](../../findings/RE-193-dyadic-laplace-compression-makes-euler-stable-dimension-logarithmic.md). Generic finite-Laplace compactness and low-rank approximation are prior-art territory; the Mathia content is the precision-aware dyadic compression bound for the exact ordinary-prime Euler channel.

RE-192 identified the mixed scale

`R=U log(Q_+/Q_-)`

for a source packet supported on `[Q_-,Q_+]` and observed on `1<=s<=1+U`. A single global Taylor expansion gave a rank budget proportional to `R`, suggesting that `R->infinity` might be the first scalar regime with substantially growing robust capacity.

RE-193 shows that this global polynomial view is far from optimal. After the exact prime-power reduction, the first-harmonic channel is the positive finite-Laplace kernel `e^{-ux}` on `0<=u<=U`, `0<=x<=log(Q_+/Q_-)`. Splitting the source coordinate dyadically and using a source-scale-dependent spectral cutoff yields, for tolerance `epsilon` above the explicit `O(Q_-^-1)` floor, a finite-rank approximation with

`rank = O((1+log(1+R))(1+log(1/epsilon)))`.

The geometry explains the logarithm. A source coordinate at distance `x` matters only in the spectral boundary layer `u=O(1/x)` before `e^{-ux}` becomes exponentially small. Each dyadic source scale therefore consumes only `O(log(1/epsilon))` separated directions, and the number of relevant scales is only `O(log(1+R))`.

Consequently fixed `U>0` with polynomially separated support `Q_-=p^A`, `Q_+=p^B` has at most `O_epsilon(loglog p)` robust scalar Euler dimension at fixed precision, even though `R=Theta(log p)`. Exact continuum identification by analyticity can coexist with extremely small finite-precision capacity. Merely enlarging the Euler rectangle is not a monotone route to many usable source coordinates.

The reusable capacity test is therefore precision-aware. A claim of `K` robust independent scalar Euler coordinates can evade the current upper bound only if roughly

`log(1+R) >= K/(1+log(1/epsilon))`.

At fixed tolerance, the transform rectangle must be exponential in the desired dimension. If the destination genuinely provides a tolerance `epsilon_p` shrinking rapidly with the source scale, that precision can buy more effective rank; the residual scale must be derived from the Robin mechanism rather than chosen for convenience.

**Boundary.** RE-193 is an upper bound, not a matching singular-value asymptotic or a constructive `{0,1,2}` matched control. It concerns a one-sided real scalar Euler channel; vertical complex sampling, joint observables or nonlocal invariants may have different geometry. The next useful question is to insert the actual source-native Robin tolerance into the logarithmic-capacity law and compare it with the number of independent source constraints a rigidity argument really needs.
