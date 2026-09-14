# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Quarantine the main zeta background while pricing a source resource stronger than prime-gap concentration

**Linked intuition:** `MI-018-signed-complexity-only-transfers-through-sign-regular-observations`.

AF-217--AF-220 identify finite-order sign regularity, rather than total positivity, as the relevant observation mechanism. AF-338 removes the earlier artificial quadratic harmonic-depth bill: for every fixed requested order `r`, spacing `h`, multiplicative window `q_j in [P,AP]`, and `sigma>r-1`, the full Euler-log sampling matrix is eventually strictly sign-regular through order `r`.

AF-339--AF-344 isolate the source-side escape. After pole cancellation the prime layer alone retains the RH-complete right-half-plane pole discriminator and has `Theta(P/log P)` ordered sign variation, yet fixed prime-independent perfect-power backgrounds remain residue-one and zero-pole-blind while reducing the residual sign variation to `O(P^(1/k))`.

AF-345 identifies the exact statistic being reduced. For every nonnegative background below prime height, zero-deleted sign variation is exactly twice the number `J_b` of consecutive-prime gaps carrying positive composite background mass:

`V = 2 J_b`.

If `M=sum m_j` is the retained composite gap mass and `S_q=sum m_j^q`, then

`V^(q-1) S_q >= 2^(q-1) M^q`.

AF-346 now proves that this concentration law is itself quantitatively sharp for an explicit arithmetic-faithful escape family. For every fixed `k>=3`, the weighted `k`-th-power background has, on fixed multiplicative windows,

`V asy X^(1/k)`, `M asy X`, `S_q asy X^(q-(q-1)/k)`.

Thus it lies exactly on the AF-345 exponent line, and on thin multiplicative windows its Holder ratio approaches the sharp constant. The family remains prime-independent, residue-one and zero-pole-blind. Consequently neither sign variation nor the concentration exponent forced by AF-345 can be strengthened into the missing source certificate under the present hypotheses.

The live source question is therefore more selective: find a **stronger normalized locality/concentration profile** that excludes these power backgrounds and is actually consumed by the destination theorem, or prove a growing-order observation theorem whose constants charge the full concentration geometry rather than only `V` and one mass moment. The `k=2` square background remains a separate boundary because unconditional prime-gap theory does not presently separate every sufficiently large pair of consecutive squares.

## Price the actual target metric before calling a representation compressed

**Linked intuitions:** `MI-019-faithful-translation-lifts-are-affine`, `MI-020-prime-tail-localization-has-an-information-conservation-law`.

Localization, contraction and lifting can move information without making it cheaper in the metric used by the final theorem. AF-342--AF-346 make this explicit: exceptional-set cardinality, support size, sign count and even the sharp prime-gap mass-moment tradeoff can all be reduced or saturated while the RH pole discriminator survives. Any claimed source compression must identify the complete resource bundle that the destination actually charges.

## Build cancellation-coherent source access to the Li root-rate class

**Linked intuitions:** `MI-021-coarse-rh-endpoints-can-still-require-deep-source-access`, `MI-022-prefix-truncation-must-respect-cancellation-orbits`.

The RH root-rate endpoint tolerates large output error but is highly sensitive to breaking its binomial cancellation orbit upstream. The remaining bridge must assemble the required cancellation coherently before taking the root-rate quotient; ordinary prefix accuracy is the wrong resource.

## Replace the conditional Schanuel codimension budget by an unconditional joint-dependence obstruction

**Linked intuitions:** `MI-023-local-completeness-can-preserve-a-root-rate-discriminator-at-zero-density`, `MI-024-periodic-completeness-turns-li-cancellation-into-profinite-leakage`, `MI-025-regular-sampling-separates-aliasing-from-finite-window-stability`, `MI-026-zero-count-fidelity-is-distance-to-the-boundary-zero-discriminant`, `MI-027-one-sided-source-constraints-replace-nullspace-rank-by-reachable-cone-geometry`, `MI-028-exact-zero-incidence-is-thinner-than-stable-access`, `MI-029-prime-phase-character-rank-exhausts-the-small-polygon-obstruction-at-the-pentagon`, `MI-030-five-prime-harmonic-rigidity-constrains-recurrence-not-first-incidence`, `MI-031-two-harmonics-recover-five-point-zero-fiber-except-torsion`, `MI-032-six-point-zero-shapes-cross-the-one-complex-coordinate-threshold`, `MI-033-parity-controls-minimal-harmonic-recovery`, `MI-035-fixed-prime-conditioning-has-zero-uniform-gap-but-a-polynomial-finite-height-modulus`, `MI-036-varying-prime-supports-fill-finite-phase-space-at-fixed-time`, `MI-037-support-height-and-time-height-form-a-two-resource-conditioning-window`, `MI-038-exponential-algebraic-gate-is-pointwise-not-stable`, `MI-039-exceptional-time-does-not-make-the-phase-point-algebraic`, `MI-040-unitary-zero-incidence-spends-two-algebraic-codimensions`.

AF-320--AF-336 separate exact recovery, conditioning, support-union geometry and exact incidence. The unconditional target remains to rule out the required independent polynomial relations on the common prime-phase tuple without Schanuel, or find another prime-source theorem strong enough to exclude the middle-singular fibre.

## Derive an equicoercive quartic profile restriction from source structure

**Linked intuition:** `MI-034-a-sub-boundary-profile-cap-makes-quartic-euler-minimization-equicoercive`.

AF-319 closes optimizer transfer once a homogeneous profile cap `Q<=C<3` is assumed. The remaining question is provenance: derive a non-escape condition of that strength from the arithmetic/source construction rather than insert it solely to recover the desired optimizer.

## Keep observation order, sign density, gap occupancy, concentration profile and destination slack as different currencies

AF-346 closes one more shortcut: the AF-345 concentration inequality is not merely necessary but exponent-sharp on simple zero-pole-blind power backgrounds. A future source theorem must therefore say which stronger combination of observation order, prime-gap occupancy, normalized mass concentration/locality and destination norm is genuinely conserved and transported. Treating sign count or one Holder moment as source complexity is now closed.