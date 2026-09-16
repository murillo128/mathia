# Weil-positivity research lines

This file holds the current mathematical lines of investigation suggested by the durable Weil-positivity intuitions. It is not a roadmap, task queue, status page, or history.

## Find a source-derived sign theorem outside scalar shadows and universal enriched lifts

**Linked intuitions:** `MI-001-positivity-needs-a-sign-producing-global-operation`, `MI-010-source-forced-critical-gram-can-have-the-wrong-weil-orientation` through `MI-042-faithful-exact-law-ucp-readouts-force-multiplicative-domain-rigidity`.

WP-293--WP-328 close broad scalar and enriched semigroup routes: many natural positivity/divisibility structures are either incompatible with the exact source shadow or universal on matched controls. WP-329--WP-330 show that operator-valued enrichment is likewise nonselective when all arithmetic remains in the scalarization state or the readout annihilates the fluctuation ideal.

WP-331--WP-332 give the opposite finite-cutoff rigidity. For a faithful UCP readout preserving the exact second moment of the same self-adjoint source observable, the positive Kadison defect vanishes; the observable lies in the multiplicative domain and its off-diagonal Stinespring coupling disappears.

WP-333--WP-335 expose the nonuniform moving-tail loophole. A support-preserving Markov/UCP map can converge to the identity under strong bounded-observable diagnostics while retaining order-one variance on the growing logarithmic coordinate.

WP-336 identifies the sharp exact-barycentric correction. With escape mass `epsilon_x` and one-sided propagation radii `L_-,L_+`, exact preservation `Psi(X)=X` gives `Q(x)<=epsilon_x L_-L_+` and globally

`||Q|| <= (1/2)||Psi-I|| sup_x L_-(x)L_+(x)`.

WP-337 shows that approximate preservation has an additional independent term. With coordinate bias `beta_x=Psi(X)(x)-x`,

`Q(x) <= epsilon_x L_-L_+ + beta_x(L_+-L_-) - beta_x^2`.

Thus asymptotic rigidity needs control of both **channel error × bidirectional propagation** and **coordinate bias × propagation asymmetry**. An intrinsic dyadic Mangoldt example has vanishing channel error and vanishing coordinate bias but fixed defect because a rare long jump keeps the relevant quadratic scale critical.

WP-338 classifies the obvious transport-topology repair exactly. For the row law `P_x`,

`W_2(P_x,delta_x)^2 = Q(x) + beta_x^2`.

Hence every rowwise `W_p` with `p>=2` controls the Kadison defect, while every fixed `1<=p<2` admits growing-support Markov/UCP maps with `W_p(P_x,delta_x)->0` and order-one defect. The failure persists under exact barycentric preservation on a dyadic prime-power ray and in the intrinsic WP-337 Mangoldt witness. The exponent `2` is sharp.

This closes ordinary rowwise Wasserstein distance as an independent source of rigidity. Subquadratic transport is too weak; quadratic transport works because it is **exactly the second-moment defect plus squared bias**; stronger exponents overpay. A surviving operator-valued route must therefore produce an independent source-side theorem forcing the quadratic transport energy to vanish, abandon the commutative rowwise Markov/UCP category, or expose a genuinely global/noncommutative coupling whose positivity is not just a reformulation of the desired Kadison defect.

## Separate source fingerprint from source-selective sign

Shifted-lattice support, Mangoldt coefficients, prime-power gaps, exact scalar laws and dyadic realizations are source-specific fingerprints. WP-333--WP-338 show that even intrinsic arithmetic support does not make the variance/transport mechanism arithmetic: the sharp propagation inequalities, the `p=2` threshold and their extremizers are generic finite-spectrum probability geometry. Sign provenance must fail on a matched control, not merely carry arithmetic labels.

## Match the topology to the moving observable without restating the target

Normalization, algebraic category, scalar shadows, fluctuation visibility, faithfulness modulus, scalar-law topology, map-level topology, observable scale, barycentric bias and propagation geometry are independent. The WP-337 ledger

`E_R=||Psi_R-I|| sup_x L_(-,R)L_(+,R)`

and

`B_R=||Psi_R(X_R)-X_R|| sup_x |L_(+,R)-L_(-,R)|`

prices two ways of generating second-moment defect. WP-338 identifies the invariant quantity they must ultimately control: rowwise quadratic transport. Future weighted graph/energy norms are useful only if a source theorem forces that quadratic quantity small for a reason stronger than simply assuming `W_2->0`; otherwise the proposed topology is only the conclusion rewritten as a metric.