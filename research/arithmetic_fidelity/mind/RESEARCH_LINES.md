# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Exploit source-law certificates once observation rank exceeds latent support freedom

**Linked intuitions:** `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`, `MI-005-test-family-fidelity-has-scale-and-dimension-gates`, and `MI-007-stable-fidelity-is-distance-from-collision`.

AF-416--AF-438 separate left-tail scaling, source selection, exact carrier choice and downstream transport. AF-439 shows that fixed finite moment data are locally noninjective on a movable positive Stieltjes class, while AF-440 proves the complementary rigid-support theorem: on the exact reciprocal-square skeleton with a separated finite mark alphabet, one sufficiently deep moment can determine a linearly deep prefix. AF-441 identifies realized support provenance as the resource that preserves this fidelity under controlled jitter.

AF-442 shows that shell/cell identity alone does not protect a later mark from one earlier latent support coordinate when only one high moment is observed. AF-443 generalizes the obstruction: for any fixed `K` reciprocal-power moments, `K` independently movable earlier support coordinates give a full-rank generalized-Vandermonde moment map, so a local fibre can absorb an arbitrarily remote mark flip while all shell labels remain unchanged.

AF-444 identifies a sharp positive boundary for a much more rigid source class. For positive **unit-weight** atoms, the first `K+1` consecutive power moments separate every `K`-atom multiset from every `(K+1)`-atom multiset. The top Newton--Girard coefficient is an exact discriminator: padding the `K`-atom side by zero forces `e_(K+1)=0`, while the side carrying the extra positive atom has `e_(K+1)>0`. On compact positive nuisance intervals the class separation is `Theta(y)` in the disappearing atom coordinate `y`, hence `Theta(m^-2)` in the reciprocal-square shell specialization.

The live gate is therefore not raw rank surplus but **rank surplus plus a source law that turns it into a target-sensitive invariant**. The next useful classification is which constrained weight/cardinality/relational source laws admit such a certificate, how many additional observations they require, and whether the resulting exact separation remains quantitatively usable at the destination scale. Only after target-purity is established should Padé, Stieltjes continued fractions, Hankel/Prony or another joint inverse be compared by conditioning.

## Keep source class, provenance, observation rank, identifiability, conditioning and destination transport separate

AF-439--AF-444 now give a concrete ladder. Rigid support can make a high moment strongly mark-separating; marked realized support can preserve that separation under controlled jitter; one latent coordinate defeats one high moment; `K` latent coordinates defeat `K` moment constraints locally; but a unit-atom cardinality law plus one consecutive surplus moment creates a global Newton certificate.

The last step is also a warning against collapsing exact and stable recovery. AF-444 restores exact target purity for every `y>0`, yet the two observation classes approach each other linearly as `y->0`. In the shell model the exact discriminator therefore becomes only `Theta(m^-2)` separated at depth `m`.

Future claims should state the admissible source class and retained provenance, compare observation rank with effective latent dimension, identify the source law that converts any rank surplus into an invariant, prove or refute target-purity, and only then price inverse conditioning and destination transport. Equal rank can leave a fibre; surplus rank can still be useless without structure; and exact separation can coexist with vanishing robustness.