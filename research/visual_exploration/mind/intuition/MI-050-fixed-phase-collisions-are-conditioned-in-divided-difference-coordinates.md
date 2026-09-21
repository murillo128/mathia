# MI-050 — Fixed phase collisions are conditioned in divided-difference coordinates

**Evidence level:** literature/derived structural synthesis from [VIS-351](../../findings/VIS-351-divided-difference-cluster-conditioning.md), refining the norming question isolated by VIS-350. Generalized exponential divided differences and their Riesz-basis conditioning are classical; the line-specific content is the accounting correction for Wang phase clusters.

For a fixed multiplicity `r` and nodes `mu_0,...,mu_r` in a bounded cluster, replace the raw exponentials by generalized divided differences

`phi_k(x)=[mu_0,...,mu_k](lambda -> exp(-i lambda x))`.

On every fixed interval of positive length, the Gram matrix of this basis has a uniformly positive smallest eigenvalue, uniformly as any subset of the nodes collide and uniformly in the absolute cluster center. At complete confluence the basis simply becomes the derivative modes `exp(-ibx), x exp(-ibx), ..., x^r exp(-ibx)` up to nonzero constants.

Thus raw Vandermonde blow-up near a phase collision is a coordinate singularity, not automatically a small-function resource. In the two-phase model, coefficients may diverge like `1/h` while the stable divided-difference coordinate `h c_1` remains finite and the represented function stays uniformly normed.

Applied after MI-049, a finite Wang bank cannot explain a small reference norm merely by citing near-coalescing phases at fixed multiplicity. Each bounded cluster must first be expressed in stable divided-difference coordinates. Any genuine collapse must then occur in the map from Wang moments to those cluster-adapted coefficients, through growing cluster multiplicity/radius, cancellation among distinct cluster subspaces, growing global cluster density, or another source/frequency-dependent mechanism.

**Boundary.** VIS-351 is local in cluster complexity. It does not give a global lower frame bound for arbitrarily many moving clusters and does not control the original Wang moment-to-divided-difference map. Inter-cluster cancellation and growing effective dimension remain real quantitative questions.