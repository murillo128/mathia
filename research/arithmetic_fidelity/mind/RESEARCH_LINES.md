# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Compress a zero-sensitive source without hiding the complexity that makes it zero-sensitive

**Linked intuition:** `MI-018-signed-complexity-only-transfers-through-sign-regular-observations`.

AF-217--AF-220 show that the relevant observation theorem is finite-order sign regularity, not all-order total positivity. AF-337 supplied an explicit full-Euler modulus but paid a quadratic sufficient depth by bounding higher-harmonic determinants independently of the first-harmonic collision structure.

AF-338 removes that artificial quadratic bill. For fixed requested order `r`, spacing `h`, multiplicative window `q_j in [P,AP]`, and

`sigma > r-1`,

the full Euler-log sampling matrix is eventually strictly sign-regular through order `r`, uniformly over the allowed integer source sets. Quantitatively the relative error of every full-Euler minor against its first-harmonic generalized Vandermonde minor is `O(P^-(sigma-(r-1)))`.

The decisive accounting identity is that a higher-harmonic tuple loses a first-harmonic pairwise collision factor only when the two column harmonic labels differ. If `X(m)` counts those unequal-label pairs and `S(m)=sum_j(m_j-1)` is the extra-harmonic order, then

`X(m) <= (k-1) S(m)`.

Thus each unit of harmonic tail can destroy at most `k-1` collision factors; the observation-side depth budget is linear in the requested sign order and independent of `h` at exponent level.

AF-339 now closes the most canonical source-side shortcut. The zero-sensitive discrepancy `d_n=Lambda(n)-1` has

`sum_(n>=2) d_n n^-s = -zeta'(s)/zeta(s)-zeta(s)+1`,

so its meromorphic continuation retains the zeta zero divisor, but on every fixed multiplicative window `[P,AP]` its ordered sign variation is

`V=(2(A-1)+o(1)) P/log P`.

Therefore the raw zero-sensitive source eventually lies outside every fixed-order AF-216/AF-338 sign budget. AF-338 cannot be extrapolated to growing `r` without a new uniform theorem.

The remaining bridge is now precise: find an **intrinsic recoding/grouping of a zero-sensitive source whose effective ordered complexity is bounded or otherwise cheaply certifiable while the zero-divisor discriminator remains recoverable**, prove a joint growing-order observation theorem strong enough for the raw source, or replace ordered sign variation by another source-complexity invariant with a finite certificate that survives toward the zero-sensitive destination. Compression counts only if the destination information lost in buying the simpler source geometry is audited explicitly.

## Price the actual target metric before calling a representation compressed

**Linked intuitions:** `MI-019-faithful-translation-lifts-are-affine`, `MI-020-prime-tail-localization-has-an-information-conservation-law`.

Localization, contraction and lifting can move information without making it cheaper in the metric used by the final theorem. A useful compression claim needs both a genuinely smaller target geometry and a theorem that the downstream argument consumes only that target rather than the hidden source detail used to construct it.

## Build cancellation-coherent source access to the Li root-rate class

**Linked intuitions:** `MI-021-coarse-rh-endpoints-can-still-require-deep-source-access`, `MI-022-prefix-truncation-must-respect-cancellation-orbits`.

The RH root-rate endpoint tolerates large output error but is highly sensitive to breaking its binomial cancellation orbit upstream. The remaining bridge must assemble the required cancellation coherently before taking the root-rate quotient; ordinary prefix accuracy is the wrong resource.

## Replace the conditional Schanuel codimension budget by an unconditional joint-dependence obstruction

**Linked intuitions:** `MI-023-local-completeness-can-preserve-a-root-rate-discriminator-at-zero-density`, `MI-024-periodic-completeness-turns-li-cancellation-into-profinite-leakage`, `MI-025-regular-sampling-separates-aliasing-from-finite-window-stability`, `MI-026-zero-count-fidelity-is-distance-to-the-boundary-zero-discriminant`, `MI-027-one-sided-source-constraints-replace-nullspace-rank-by-reachable-cone-geometry`, `MI-028-exact-zero-incidence-is-thinner-than-stable-access`, `MI-029-prime-phase-character-rank-exhausts-the-small-polygon-obstruction-at-the-pentagon`, `MI-030-five-prime-harmonic-rigidity-constrains-recurrence-not-first-incidence`, `MI-031-two-harmonics-recover-five-point-zero-fiber-except-torsion`, `MI-032-six-point-zero-shapes-cross-the-one-complex-coordinate-threshold`, `MI-033-parity-controls-minimal-harmonic-recovery`, `MI-035-fixed-prime-conditioning-has-zero-uniform-gap-but-a-polynomial-finite-height-modulus`, `MI-036-varying-prime-supports-fill-finite-phase-space-at-fixed-time`, `MI-037-support-height-and-time-height-form-a-two-resource-conditioning-window`, `MI-038-exponential-algebraic-gate-is-pointwise-not-stable`, `MI-039-exceptional-time-does-not-make-the-phase-point-algebraic`, `MI-040-unitary-zero-incidence-spends-two-algebraic-codimensions`.

AF-320--AF-329 separate exact recovery, conditioning, support-union geometry and exact incidence. AF-330 forces any exact eight-prime hit to have exponentially algebraic common parameter `-it`; AF-331 shows that exceptional real-time set is countable but dense, so it has no stability content. AF-332 proves that at nonzero real time at most two distinct prime phases can be algebraic.

AF-333 gives the first joint algebraic-dimension closure, but conditionally on Schanuel: a common-time tuple from multiplicatively independent algebraic bases has algebraic codimension at most one, whereas a unitary zero `e_1=0` forces the independent reciprocal relation `e_(n-1)=0`, consuming at least two codimensions. For the eight-prime target, Schanuel already forbids `e_1=0`.

AF-335 fixes the information budget on the weaker even middle-singular branch. Near a regular `2m`-gon, `e_m=0` removes one real source degree while the low-harmonic image loses two; adjoining the product phase `E in S^1` is therefore dimension-minimal as a continuous exact lift. AF-336 closes the maximally singular consecutive-half-spectrum endpoint: `s_1=...=s_floor(n/2)=0` forces a rotated regular `n`-gon, and a nonzero prime-time tuple cannot realize that fibre. For every shorter consecutive block, positive shape dimension remains after rotation.

The actual target `e_1=e_4=0` is weaker than half-spectrum vanishing and still retains the one-real fidelity defect isolated by AF-335. The unconditional theorem remains: rule out the required independent polynomial relations on the common prime-phase tuple without Schanuel, or find another prime-source theorem strong enough to exclude the middle-singular fibre.

## Derive an equicoercive quartic profile restriction from source structure

**Linked intuition:** `MI-034-a-sub-boundary-profile-cap-makes-quartic-euler-minimization-equicoercive`.

AF-319 closes the optimizer-transfer problem once one assumes a homogeneous profile cap `Q<=C<3`: the cap is projectively compact, the normalized full Euler objective converges uniformly to the quartic homogeneous objective with `O(delta)` error, and its minimizers converge to the unique certified homogeneous optimizer. The unrestricted problem still admits escaping source shapes.

The remaining question is provenance of the non-escape resource. Can the arithmetic/source construction force a cap below the certified boundary level, or another condition strong enough to give projective equicoercivity, without inserting that restriction solely to recover the desired optimizer?

## Keep incidence, source resources and destination slack as different currencies

Finite sign order, exact algebraic recovery, conditioning, support-union geometry, common-time incidence and destination sensitivity are distinct resources. AF-338 shows why this accounting matters on the observation side: preserving the actual collision geometry changes a quadratic apparent transport bill into a linear one. AF-339 supplies the complementary source-side warning: direct zero sensitivity may come with a sign budget that diverges like `P/log P`. Neither improvement supplies the other currency for free.