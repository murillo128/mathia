# MI-069 — Stabilizer symmetry exhausts the centered Gaussian qutrit nuisance covariance

**Evidence level:** exact representation-theoretic synthesis from VIS-389--VIS-391 and [VIS-392](../../findings/VIS-392-source-stabilizer-gaussian-null-is-sector-scaled.md) for a generic rank-one qutrit source with distinct eigenvalues.

VIS-391 introduced a three-sector centered Gaussian nuisance family with independent isotropic root-plane blocks and arbitrary sector variances. VIS-392 shows that this family is not merely a convenient control. For a generic qutrit source, the stabilizer torus acts independently by rotations on the three real root planes `H_12`, `H_13`, and `H_23`. A centered Gaussian law is invariant under the full stabilizer if and only if its covariance has the block form

`sigma_12^2 I_2 direct-sum sigma_13^2 I_2 direct-sum sigma_23^2 I_2`.

Cross-sector covariance and within-sector ellipticity break stabilizer symmetry. Because Gaussian laws are determined by their covariance, the sector-scaled family of VIS-391 is therefore the **maximal centered Gaussian nuisance class compatible with the exact source stabilizer**.

This strengthens the meaning of the calibrated residual `v=F_lambda(u|m_1)`. Once the three variance ratios are fixed independently, a deviation from the calibrated law cannot be explained by some further hidden stabilizer-invariant Gaussian covariance. The remaining source-free alternatives must leave the Gaussian-covariance class: non-Gaussian higher-order dependence, nonlinear admissibility effects, symmetry breaking, mixture structure, or another mechanism not encoded by a centered stabilizer-invariant covariance.

The reusable principle is that a nuisance family becomes substantially more informative when it is classified by the exact symmetry rather than chosen parametrically. The right null is the full fiber allowed by the retained invariance. Only after that fiber is exhausted does residual structure justify moving to higher-order or symmetry-breaking explanations.

**Boundary.** Exhausting the stabilizer-invariant centered Gaussian covariance class does not make a residual arithmetic. Non-Gaussian stabilizer-invariant laws and source-free admissibility mechanisms remain possible, the nuisance variances still must not be fitted adaptively to the candidate residual, and no destination-level Wang gain follows from rejecting this Gaussian null alone.