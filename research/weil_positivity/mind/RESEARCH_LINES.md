# Weil-positivity research lines

This file holds the current mathematical lines of investigation suggested by the durable Weil-positivity intuitions. It is not a roadmap, task queue, status page, or history.

## Find a source-derived sign theorem outside scalar shadows and universal enriched lifts

**Linked intuitions:** `MI-001-positivity-needs-a-sign-producing-global-operation`, `MI-010-source-forced-critical-gram-can-have-the-wrong-weil-orientation` through `MI-042-faithful-exact-law-ucp-readouts-force-multiplicative-domain-rigidity`.

WP-293--WP-328 close broad scalar and enriched semigroup routes: many natural positivity/divisibility structures are either incompatible with the exact source shadow or universal on matched controls. WP-329--WP-330 show that operator-valued enrichment is likewise nonselective when all arithmetic remains in the scalarization state or the readout annihilates the fluctuation ideal.

WP-331--WP-332 give the opposite finite-cutoff rigidity. For a faithful UCP readout preserving the exact second moment of the same self-adjoint source observable, the positive Kadison defect vanishes; the observable lies in the multiplicative domain and its off-diagonal Stinespring coupling disappears.

WP-333--WP-335 expose the nonuniform moving-tail loophole. A support-preserving martingale UCP map can converge to the identity under weak scalar metrics, every fixed finite divergence, both max-divergences and even ordinary channel norm while retaining an order-one Kadison defect on the growing logarithmic observable. The mechanism is a vanishing escape probability multiplied by a growing squared jump.

WP-336 makes that tradeoff sharp. If `epsilon_x` is the off-diagonal row mass and `L_-(x),L_+(x)` are the one-sided source-coordinate propagation radii, exact barycentric preservation gives

`0 <= Q(x) <= epsilon_x L_-(x)L_+(x)`

for the Kadison defect `Q=Psi(X^2)-X^2`, while

`||Psi-I|| = 2 sup_x epsilon_x`.

Hence

`||Q|| <= (1/2)||Psi-I|| sup_x L_-(x)L_+(x)`.

The WP-335 construction attains equality. Ordinary channel-norm convergence therefore **does** recover asymptotic multiplicative-domain rigidity once the bidirectional propagation product is subcritical relative to the channel error. A fixed surviving defect forces propagation budget at least reciprocal to `||Psi-I||` along a subsequence.

A surviving operator-valued route must consequently pay a critical/supercritical nonlocal propagation bill, abandon exact martingale preservation of the same scalar coordinate, move outside the commutative Markov/UCP setting, or expose another source-forced coupling. Merely invoking a stronger unnamed “energy topology” is no longer enough; in this lane the exact missing resource is quantitatively identified.

## Separate source fingerprint from source-selective sign

Shifted-lattice support, Mangoldt coefficients, prime-power gaps and exact scalar laws are source-specific fingerprints. WP-333--WP-336 show that even exact support preservation and an intrinsic arithmetic ray do not make the UCP variance mechanism arithmetic: the sharp propagation inequality and its extremizer are generic martingale geometry. Sign provenance must fail on a matched control, not merely carry arithmetic labels.

## Match the topology to the moving observable

Normalization, algebraic category, scalar shadows, fluctuation visibility, faithfulness modulus, scalar-law topology, map-level topology, observable scale and propagation geometry are independent. WP-336 identifies the exact scale correction for the current martingale coordinate: bounded-channel convergence is sufficient only after multiplication by

`B_R = sup_x L_(-,R)(x)L_(+,R)(x)`.

The criterion `||Psi_R-I|| B_R -> 0` forces the second-moment/Kadison defect to vanish, while WP-335 sits exactly at the critical product scale. Future constructions should therefore state the norm on the actual moving observable and the propagation/moment budget that turns it into a uniform modulus. Weighted graph/energy norms remain possible reformulations, but they must dominate this concrete critical product rather than merely sound stronger than the sup norm.
