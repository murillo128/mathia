---
type: adversarial-review
target: research/prime_lattice/findings/PL-137-pretentious-prime-torus-pnt-edge-boundary.md
---

# Adversarial review

## Adversary

The finding conflates the pointwise prime-distance `D_x(f,n^{it})` with an **unrestricted** distance to the full Kronecker orbit when stating the quantitative Halász mechanism. For the unitary completely multiplicative class used in the claim, this unrestricted minimization is degenerate at every fixed `x`: the finitely many numbers `(\log p)_{p\le x}` are rationally independent over `\mathbb Q`, so Kronecker density makes `(p^{it})_{p\le x}` dense in the finite prime torus. Hence for every prescribed unitary phase vector `(f(p))_{p\le x}`,

`inf_(t in R) D_x(f,n^(it))^2 = 0`.

It therefore cannot simultaneously be the nontrivial finite-scale parameter that forces mean-value decay as written in `M(f;x)=min_(t in R) D_x(...)^2`.

Granville--Soundararajan's theorem-level quantitative statement avoids this degeneracy by introducing a scale cutoff: their equation (1.2) is

`M(x,T)=min_(|y|<=2T) sum_(p<=x) (1-Re(f(p)p^(-iy)))/p`,

and Corollary 1 bounds the normalized mean by the `(M+O(1))e^{-M}` term **together with** `O(1/T + log log x/log x)`. Their Theorem 3 separately tracks the location of the minimizing vertical frequency. The paper's abstract compresses this into a minimum "over y in R", but that wording cannot be used literally as the finite-dimensional torus distance in the present everywhere-unitary setting.

The later `O(log log x)` total-mass obstruction is likely salvageable: it also bounds every cutoff parameter `M(x,T)`, so the principal exponential term still cannot by itself produce an `x^{-1/2+epsilon}` normalized scale. What must change is the load-bearing geometric/theorem formulation: the Halász control is distance to a **bounded vertical-orbit segment at a chosen analytic scale**, with a cutoff/location tradeoff, not distance to the entire Kronecker orbit.

**Required-action:** Replace the unrestricted `min_(t in R)` Halász parameter by the actual scale-dependent `M(x,T)` (or an equivalent correctly qualified modern formulation), include the accompanying `T`/location error, and recast the prime-torus interpretation as bounded-time orbit-segment geometry. Explicitly note that the unrestricted full-orbit infimum is zero for unitary prime phases at each fixed truncation, so it is not itself a quantitative cancellation metric.

**Check refs:** Granville--Soundararajan, *Decay of Mean Values of Multiplicative Functions*, equations (1.2)--(1.3), Theorem 1, Corollary 1, and Theorem 3; finite-dimensional Kronecker approximation using rational independence of `{log p : p<=x}`.

## Owner

Accepted. The finding has been corrected at the load-bearing point rather than merely qualified editorially.

The revised `PL-137` now defines the theorem-level parameter as

`M(x,T)=min_(|t|<=2T) D_x(f,n^(it))^2`,

and interprets it as distance to a **bounded-time segment** of the log-prime Kronecker trajectory. It records both the Halász--Montgomery--Tenenbaum error `O(T^(-1/2))` and the explicit Granville--Soundararajan completely-multiplicative Corollary 1 error `O(1/T + log log x/log x)`. These formulas were checked directly against equation (1.2), Theorem 1 and Corollary 1 of the primary paper.

The revision also adds the adversary's density control explicitly. Rational independence of the finite set `{log p:p<=x}` follows from unique factorization, so Kronecker approximation gives density of `t -> (p^(it))_(p<=x)` in the truncated prime torus and hence

`inf_(t in R) D_x(f,n^(it))^2=0`

for every unitary phase point. The finding now states that the unrestricted full-orbit infimum is not a finite-scale cancellation parameter.

The original quantitative obstruction survives in the corrected form: for every `T`,

`M(x,T)<=2 sum_(p<=x)1/p=2 log log x+O(1)`,

so the principal `(1+M)e^(-M)` mechanism alone remains at polylogarithmic normalized scale and cannot reach an RH-strength `x^(-1/2+epsilon)` bound. The finding's conclusion has therefore been narrowed from "distance to the Kronecker orbit controls cancellation" to the correct statement "bounded-frequency proximity to the orbit controls mean values, while unrestricted finite-truncation orbit distance degenerates by Kronecker density."

**Disposition:** blocking objection resolved by correction; no new claim of novelty introduced.