# MI-012 — Low-bias Hamming regularization bottoms out at a positive diagonal floor, and generic reconstruction is ill-conditioned

**Evidence level:** exact source-level and classical approximation results through MC-103

## Core intuition

Moving the source-forced Hamming deformation toward zero bias does reduce its almost-square degree-two amplitude, but this does not approach the signed cancellation mechanism at the Möbius endpoint. Before the crossover the reduction is exactly degree-two damping; at the square-root scale a positive degree-zero diagonal shell takes over and pins the source at linear size. Trying to transport that low-bias gain back to the endpoint by a universal linear reconstruction is worse: the exact Chebyshev extrapolation cost from a shrinking window is superpolynomial at the available degree ceiling.

The relevant lesson is therefore no longer a missing square-root regime. **Low-bias amplitude regularization is fully explained by positive source shells, while any useful transfer to the hard endpoint must exploit arithmetic relations narrower than the class of degree-bounded polynomials.**

## Strongest justified principle

MC-099--MC-101 show that the Hamming path begins with an almost-square positive degree-two shell, develops large negative curvature before the hard endpoint, and throughout every polynomial mesoscopic bias `t=N^{-alpha}`, `0<alpha<1/2`, has the exact degree-two scale `N^{2-2alpha}/log^2 N`.

MC-102 evaluates the previously coarse degree-zero term: `C_{0,N}=c_0N+O(N^{2/3})` with `c_0>0`. It gives a uniform crossover asymptotic in which degree zero and degree two add positively. At `t ~ (log N)/sqrt N` they are both linear, and below that scale the diagonal term supplies a positive `c_0N` floor. The square-root boundary is therefore not a hidden cancellation transition.

MC-103 supplies the optimal degree-only transfer obstruction. Endpoint evaluation from `[0,tau]` has norm `T_K(2/tau-1)` on degree-`K` polynomials, and every exact signed sampling formula pays at least this total-variation cost. For polynomially shrinking Hamming windows, including the square-root scale, that cost is superpolynomial when `K=K_N`; subtracting finitely many known low Taylor shells does not change the diagnosis.

## What remains possible

The actual Hamming polynomial occupies a source-constrained coefficient family much smaller than all degree-bounded polynomials. A signed recurrence using those joint coefficient constraints, a moving interior observable, a non-point functional, or a different deformation can evade the Chebyshev lower bound because it need not reconstruct arbitrary polynomials. Such a route must identify the extra arithmetic relation explicitly and show that its conditioning cost is strictly smaller than the source gain.

## Status / novelty

The asymmetric-divisor expansion and Hamming source asymptotics are persisted line-specific results; Chebyshev/Remez endpoint extrapolation is classical. The durable synthesis is: **shrinking toward zero bias never exposes the endpoint cancellation by amplitude alone, and generic polynomial reconstruction cannot recover it at an acceptable cost.**

## Falsification criterion

Invalidate the positive diagonal asymptotic or the crossover formula of MC-102; produce an exact universal linear reconstruction from a polynomially shrinking low-bias window whose amplification beats the Chebyshev extremal norm; or derive a source-specific recurrence whose hypotheses genuinely hold for the Hamming coefficients and whose conditioning overcomes the established low-bias/endpoint gap.
