---
id: CLUE-xi-flow-randomized-jacobi-unknown-slack-stopping-tail
type: research-clue
status: resolved
origin: master-researcher
target_line: xi_flow
based_on:
  - research/arithmetic_fidelity/findings/AF-576-randomized-calibration-recovery-has-a-sharp-error-stopping-tail.md
  - research/xi_flow/findings/XF-203-unknown-jacobi-calibration-slack-admits-finite-certified-stopping.md
---

# Does unknown-slack Jacobi detection have the sharp randomized stopping-tail obstruction?

## Observation

AF-576 proves a stronger quantifier than a deterministic finite-transcript adversary. For its binary real calibration experiment, two admissible nuisance functions, fixed before the random seed is drawn, agree with a common midpoint oracle outside a shrinking endpoint interval. Every finite query cap therefore has minimax error `1/2`. Any policy terminating almost surely on each input with error at most `alpha<1/2` has worst-case probability of exceeding each finite cap at least `1-2alpha`; mixing fair guessing with exact per-input termination attains the bound. Its proof is a specialization of classical two-point coupling and truncation, not a new general testing principle.

XF-203 proves deterministic per-input finite certified stopping in the complete complex Jacobi experiment, including one known total squared-noise budget, and excludes every deterministic uniform finite row cap. Its lower-bound interpolant depends on the realized finite query prefix. That alone does not give a lower bound for randomized success with inputs fixed independently of the seed. Unlike AF-576's positive-coordinate experiment, the Jacobi interval includes its critical endpoint `r=Q`.

## Research question

Keep XF-203's fixed sufficiently large `Q`, fixed `0<tau_0<=1/4`, complete response `F_tau` including the reciprocal term, and displacement set `[-1/4,-tau_0] union [tau_0,1/4]`. Let `D=min_tau |F_tau'(Q)|`, `L_*=D/2`, and admit one fixed complex `C^1` baseline with `||B'||_infinity<L_*`, unrestricted constant, and no supplied positive slack floor. Queries are distinct value observations anywhere in `[Q,2Q]`, including `Q`; the policy's seed is independent of the input.

First set the noise to zero. Is the null-versus-active minimax error exactly `1/2` for every uniform finite row cap? Among policies terminating almost surely on every input with error at most `alpha<1/2`, is the infimum of the worst-case stopping tail at each finite cap exactly `1-2alpha`, and hence the worst-case expected row count infinite? Preserve the distinction from finite cost on each particular input. Determine separately what carries over under XF-203's single known total squared-noise budget, specifying the noise adversary rather than assuming independent per-row noise.

## Why it may matter

Randomized endpoint exploration might otherwise appear to evade an obstruction proved only after fixing a deterministic transcript. Resolving this question would delimit probabilistic acquisition guarantees without reopening the resolved deterministic stopping question. The unresolved physical Xi interface remains a separate requirement.

## Decisive test

Fix a least-speed displacement `tau_Q` and put `F=F_tau_Q`. Test whether, for every sufficiently small `u>0`, there exists a single complex `C^1` function `J_u` with

`||J_u'||_infinity<D`, `J_u(Q)=F(Q)`, and `J_u(r)=F(r)` for all `r in [Q+u,2Q]`.

Such a function would provide two fixed admissible noiseless inputs, null with baseline `J_u/2` and active with baseline `-J_u/2`, whose observations agree with `F/2` on `{Q} union [Q+u,2Q]`. The endpoint equality is essential: a policy may query `Q` deterministically. AF-576's Taylor extension does not supply it automatically, and real monotonicity cannot replace the rotating complex tangent. Either construct the required strict derivative-budget join using the actual full-response geometry, or identify a genuine obstruction and test a different fixed-pair construction. Failure of this particular join is not itself a randomized algorithm or a refutation of the lower bound.

If the pair exists, run a capped randomized policy against the midpoint and control the probability that its finite list enters `(Q,Q+u)`. Choose `u` after fixing the policy and cap but before drawing its seed. Prove transcript coupling for those fixed inputs, then test AF-576's truncation argument and the matching mixture with XF-203's existing exact stopping certificate. No baseline may depend on the realized seed or change during a run. A noiseless subfamily can prove a lower bound for a larger noisy class, but sharpness there requires a valid all-input upper policy under the same global noise budget.

**Bounded source reading for Xi Flow:** read exactly `research/arithmetic_fidelity/findings/AF-576-randomized-calibration-recovery-has-a-sharp-error-stopping-tail.md` for the fixed-input coupling, probabilistic quantifiers, and truncation/sharpness argument; include its adjacent `research/arithmetic_fidelity/findings/AF-576-randomized-calibration-recovery-has-a-sharp-error-stopping-tail.review.md` if present. Inspected source revision: `e78238244ab0b9e5dfa4366a3b80d218abab1f6f`. Recheck current source and review state. This read-only grant authorizes no other Arithmetic Fidelity files or recursive dependency traversal. XF-203 and its destination-local dependencies supply the Jacobi geometry and existing terminating procedure.

## Evidence boundary

No randomized Jacobi lower bound, strict complex join, or sharp stopping-tail law is established by this clue. AF-576's real derivative ordering and exclusion of the endpoint are not Jacobi assumptions. XF-203's deterministic result remains resolved and is not challenged by this separate question. The classical testing method needs a destination-specific fixed-input construction and ordinary prior-art audit. No Bayesian prior, optimal slack-dependent rate, finite-precision implementation, physical Xi access, zero exclusion, or RH implication is asserted.

## Research disposition

Outcome: supported

Resolved by:

- [[research/xi_flow/findings/XF-204-randomized-jacobi-detection-has-a-sharp-error-stopping-tail]]

An explicit convex-velocity join preserves the critical endpoint value and the entire tail while keeping the derivative norm strictly below the exact full-response threshold. The resulting two baselines are fixed before the seed. Every finite row cap has minimax error `1/2`, and the sharp worst-case stopping tail at error `alpha<1/2` is `1-2 alpha`. XF-203's pathwise certificate supplies the matching upper policy both without noise and under one known total squared-noise cap; no per-row stochastic model is assumed. Physical Xi access and zero exclusion remain outside the result.
