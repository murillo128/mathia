# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Require observation rank to outrun latent support freedom before pricing joint pole recovery

**Linked intuitions:** `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class` and the current shell-carrier/derivative-depth intuitions.

AF-416--AF-438 separate left-tail scaling, source selection, exact carrier choice and downstream transport. AF-439 shows that fixed finite moment data are locally noninjective on a movable positive Stieltjes class, while AF-440 proves the complementary rigid-support theorem: on the exact reciprocal-square skeleton with a separated finite mark alphabet, one sufficiently deep moment can determine a linearly deep prefix. AF-441 identifies realized support provenance as the resource that preserves this fidelity under controlled jitter.

AF-442 shows that shell/cell identity alone does not protect a later mark from one earlier latent support coordinate when only one high moment is observed. AF-443 removes the obvious repair: for any fixed `K` reciprocal-power moments, `K` independently movable earlier support coordinates give a full-rank generalized-Vandermonde moment map, so the implicit-function theorem produces a local fibre that can absorb an arbitrarily remote mark flip while all shell labels remain unchanged. The compensating motions even tend to zero with the target depth.

The live gate is therefore dimensional and structural. Merely adding finitely many moments does not create fidelity when the admissible latent support dimension grows with the observation rank. A credible lift must produce an observation rank strictly beyond the effective latent deformation dimension, constrain that deformation by source-derived relations, retain enough realized/relational support data to reconstruct it, or let the observation family grow in a way that outruns the admitted nuisance freedom. Only after the finite observation fibre is proved target-pure should Padé, Stieltjes continued fractions, Hankel/Prony or another joint inverse be compared by conditioning at the shell depth consumed downstream.

## Keep source class, provenance, observation rank, identifiability, conditioning and destination transport separate

Exact analytic continuation from the complete moment sequence is not finite-prefix recovery, and removing the AF-437 peeling cascade does not prove a stable inverse. AF-439--AF-443 now separate four regimes: rigid support can make a high moment strongly mark-separating; marked realized support can preserve that separation under controlled jitter; one latent coordinate defeats one high moment even with cell provenance; and `K` latent coordinates defeat any fixed `K`-moment family under the full-rank local model.

The reusable warning is that nominal measurement richness is not the same as source identifiability. Increasing moment order can strengthen separation on a fixed skeleton while making latent compensation smaller; increasing the number of moments can still leave an equal-dimensional nuisance fibre. Future claims should state the admissible source class and retained provenance, compare observation rank with effective latent dimension, prove or refute target-purity on that class, and only then price inverse conditioning and destination transport. Rank surplus is at most a necessary escape from AF-443, not by itself a sufficient recovery theorem.