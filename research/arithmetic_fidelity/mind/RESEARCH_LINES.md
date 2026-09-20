# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Exploit source-law certificates once observation rank exceeds latent support and weight freedom

**Linked intuitions:** `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`, `MI-005-test-family-fidelity-has-scale-and-dimension-gates`, and `MI-007-stable-fidelity-is-distance-from-collision`.

AF-416--AF-438 separate left-tail scaling, source selection, exact carrier choice and downstream transport. AF-439 shows that fixed finite moment data are locally noninjective on a movable positive Stieltjes class, while AF-440 proves the complementary rigid-support theorem: on the exact reciprocal-square skeleton with a separated finite mark alphabet, one sufficiently deep moment can determine a linearly deep prefix. AF-441 identifies realized support provenance as the resource that preserves this fidelity under controlled jitter.

AF-442--AF-443 make the dimensional obstruction explicit. One latent support coordinate can absorb one high-moment constraint, and `K` independently movable support coordinates can absorb `K` reciprocal-power moment constraints through a full-rank generalized-Vandermonde map. Shell labels alone do not remove that local fibre.

AF-444 gives the sharp structured repair for positive **unit-weight** atoms: the first `K+1` consecutive power moments separate every `K`-atom multiset from every `(K+1)`-atom multiset, with the top Newton--Girard coefficient as the exact certificate. AF-445 now shows that the threshold moves when the amplitudes are also latent. For positive atoms with unknown positive weights and locations, `K` nuisance atoms carry `2K` continuous parameters; the first `2K` positive moments can still locally absorb a remote added atom, while the first `2K+1` moments globally separate measures with at most `K` distinct positive atoms from a `(K+1)`-atom alternative through the shifted Hankel determinant. Thus the relevant rank is the effective source dimension, not merely the number of support locations.

After the sharp threshold is crossed, the remote-mark margin remains linear in the disappearing atom coordinate, hence `Theta(m^-2)` in the reciprocal-square shell specialization. The live gate is therefore **effective latent dimension -> source-law certificate -> quantitative destination margin**. The next useful classification is which constrained weight/support/relational source laws lower the required observation count or improve the margin without smuggling the target into the assumptions.

## Keep source class, provenance, latent dimension, exact identifiability and robustness separate

AF-439--AF-445 give a concrete ladder: rigid support can make a high moment mark-separating; realized support provenance can preserve that separation under controlled jitter; equal observation rank and latent dimension can leave a local fibre; a unit-weight cardinality law needs only one surplus consecutive moment; allowing unknown positive weights doubles the generic finite-atomic parameter count and shifts the sharp certificate to `2K+1` moments.

The exact thresholds do not by themselves solve stable recovery. Both the Newton and shifted-Hankel certificates can remain nonzero for every positive extra atom while the two admissible observation classes approach each other as that atom disappears. Future claims should therefore state the admissible source class, count its effective latent freedom, identify the exact source law converting surplus observations into an invariant, prove target-purity, and only then price conditioning and transport.