# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Quarantine the main zeta background while pricing the resource used to simplify the residual

**Linked intuition:** `MI-018-signed-complexity-only-transfers-through-sign-regular-observations`.

AF-217--AF-220 show that the relevant observation theorem is finite-order sign regularity, not all-order total positivity. AF-338 removes the artificial quadratic harmonic-depth bill: for fixed requested order `r`, spacing `h`, multiplicative window `q_j in [P,AP]`, and `sigma>r-1`, the full Euler-log sampling matrix is eventually strictly sign-regular through order `r`, with relative minor error `O(P^-(sigma-(r-1)))`.

AF-339--AF-341 isolate the source-side cost. After pole cancellation, the prime layer alone remains an RH-complete right-half-plane pole discriminator and has `Theta(P/log P)` ordered sign variation; higher prime powers are holomorphic in `Re(s)>1/2` and do not carry the relevant zero poles. AF-342 shows that an arbitrary baseline can lower this sign variation only by reacting on a prime-scale set of prime or prime-adjacent sites, while AF-343 proves that fixed periodic or more generally syndetic positive-composite backgrounds cannot do so.

AF-344 closes the inference that this exceptional geometry must itself be arithmetically complicated. For every fixed `k>=2`, the prime-independent perfect-`k`th-power background

`b_k(m^k)=k m^(k-1)`, `b_k(n)=0` otherwise,

has Dirichlet transform `k(\zeta(ks-k+1)-1)`, hence residue one at `s=1` and no zeta-zero poles in `Re(s)>1/2`. The residual still carries the RH pole discriminator, but on every fixed multiplicative window its zero-deleted sign variation is only `O(P^(1/k))`. The price has moved into a sparse support of size `asymp P^(1/k)` with amplitudes `asymp P^(1-1/k)` and total mass `asymp P`.

So ordered sign variation by itself is not a conserved source-complexity currency. A fixed short algebraic rule can preserve the zero discriminator while trading prime-scale sign density for dynamic range and support gaps. The live bridge is now to identify a **joint source certificate** actually consumed by the observation theorem—sign order together with amplitude, local concentration, support-gap geometry or another norm—or to prove a growing-order observation theorem that prices the resource into which AF-344 moves the source. Description complexity and exceptional-site cardinality alone are no longer viable lower bounds.

## Price the actual target metric before calling a representation compressed

**Linked intuitions:** `MI-019-faithful-translation-lifts-are-affine`, `MI-020-prime-tail-localization-has-an-information-conservation-law`.

Localization, contraction and lifting can move information without making it cheaper in the metric used by the final theorem. A useful compression claim needs both a genuinely smaller target geometry and a theorem that the downstream argument consumes only that target rather than the hidden source detail used to construct it. AF-342--AF-344 sharpen the warning: exceptional-set cardinality, syndeticity and ordered sign count can all be reduced or rearranged while another resource such as amplitude concentration grows. Any claimed source compression must audit the full resource bundle used by the destination.

## Build cancellation-coherent source access to the Li root-rate class

**Linked intuitions:** `MI-021-coarse-rh-endpoints-can-still-require-deep-source-access`, `MI-022-prefix-truncation-must-respect-cancellation-orbits`.

The RH root-rate endpoint tolerates large output error but is highly sensitive to breaking its binomial cancellation orbit upstream. The remaining bridge must assemble the required cancellation coherently before taking the root-rate quotient; ordinary prefix accuracy is the wrong resource.

## Replace the conditional Schanuel codimension budget by an unconditional joint-dependence obstruction

**Linked intuitions:** `MI-023-local-completeness-can-preserve-a-root-rate-discriminator-at-zero-density`, `MI-024-periodic-completeness-turns-li-cancellation-into-profinite-leakage`, `MI-025-regular-sampling-separates-aliasing-from-finite-window-stability`, `MI-026-zero-count-fidelity-is-distance-to-the-boundary-zero-discriminant`, `MI-027-one-sided-source-constraints-replace-nullspace-rank-by-reachable-cone-geometry`, `MI-028-exact-zero-incidence-is-thinner-than-stable-access`, `MI-029-prime-phase-character-rank-exhausts-the-small-polygon-obstruction-at-the-pentagon`, `MI-030-five-prime-harmonic-rigidity-constrains-recurrence-not-first-incidence`, `MI-031-two-harmonics-recover-five-point-zero-fiber-except-torsion`, `MI-032-six-point-zero-shapes-cross-the-one-complex-coordinate-threshold`, `MI-033-parity-controls-minimal-harmonic-recovery`, `MI-035-fixed-prime-conditioning-has-zero-uniform-gap-but-a-polynomial-finite-height-modulus`, `MI-036-varying-prime-supports-fill-finite-phase-space-at-fixed-time`, `MI-037-support-height-and-time-height-form-a-two-resource-conditioning-window`, `MI-038-exponential-algebraic-gate-is-pointwise-not-stable`, `MI-039-exceptional-time-does-not-make-the-phase-point-algebraic`, `MI-040-unitary-zero-incidence-spends-two-algebraic-codimensions`.

AF-320--AF-329 separate exact recovery, conditioning, support-union geometry and exact incidence. AF-330 forces any exact eight-prime hit to have exponentially algebraic common parameter `-it`; AF-331 shows that exceptional real-time set is countable but dense, so it has no stability content. AF-332 proves that at nonzero real time at most two distinct prime phases can be algebraic.

AF-333 gives the first joint algebraic-dimension closure, but conditionally on Schanuel: a common-time tuple from multiplicatively independent algebraic bases has algebraic codimension at most one, whereas a unitary zero `e_1=0` forces the independent reciprocal relation `e_(n-1)=0`, consuming at least two codimensions. AF-335 fixes the information budget on the weaker even middle-singular branch, and AF-336 closes the maximally singular consecutive-half-spectrum endpoint.

The actual target `e_1=e_4=0` is weaker than half-spectrum vanishing and still retains the one-real fidelity defect isolated by AF-335. The unconditional theorem remains: rule out the required independent polynomial relations on the common prime-phase tuple without Schanuel, or find another prime-source theorem strong enough to exclude the middle-singular fibre.

## Derive an equicoercive quartic profile restriction from source structure

**Linked intuition:** `MI-034-a-sub-boundary-profile-cap-makes-quartic-euler-minimization-equicoercive`.

AF-319 closes the optimizer-transfer problem once one assumes a homogeneous profile cap `Q<=C<3`: the cap is projectively compact, the normalized full Euler objective converges uniformly to the quartic homogeneous objective with `O(delta)` error, and its minimizers converge to the unique certified homogeneous optimizer. The unrestricted problem still admits escaping source shapes.

The remaining question is provenance of the non-escape resource. Can the arithmetic/source construction force a cap below the certified boundary level, or another condition strong enough to give projective equicoercivity, without inserting that restriction solely to recover the desired optimizer?

## Keep observation order, sign density, amplitude concentration, main-term isolation and destination slack as different currencies

Finite sign order, exact algebraic recovery, conditioning, support-union geometry, common-time incidence, main-term cancellation and destination sensitivity are distinct resources. AF-338 improves the observation-side bill by preserving collision geometry. AF-339--AF-343 show that pole isolation leaves a prime-scale sign burden against broad low-amplitude/syndetic baseline classes. AF-344 then proves that a sparse high-amplitude zero-pole-blind background can collapse that burden to `O(P^(1/k))` without learning the prime set. Any next source theorem must therefore state which combination of sign order, amplitude, concentration, support geometry or other norm is genuinely conserved and transported to the destination.