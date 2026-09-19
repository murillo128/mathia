# MI-050 — Any fixed finite Hilbertization preserves reciprocal similarity

**Evidence level:** exact operator-theoretic synthesis from [PC-355](../../findings/PC-355-free-fock-completion-preserves-reciprocal-parity.md) through [PC-358](../../findings/PC-358-arbitrary-fixed-finite-hilbertizations-preserve-reciprocal-similarity.md).

PC-355 shows that the canonical full-Fock signature multiplier of the reciprocal control is unitarily conjugate to the source multiplier when the Hilbert structure is parity-compatible. PC-356 shows that a source-dependent radial Gram metric does not help when recomputed covariantly on the control: the metric is transported by parity and source/control remain isometric.

PC-357 freezes one parity-breaking one-particle metric on both source and control. Unitarity can fail, but after whitening the reciprocal law still becomes an exact nonunitary similarity, with depth-dependent singular/resolvent distortion bounded by the tensor condition number.

PC-358 removes the tensor-product assumption. On the finite word space `V_N`, the algebraic reciprocal identity is

`L~_N = P_N L_N P_N`, `P_N^2=I`.

Equip `V_N` with **any** fixed positive Hermitian metric `G_N>0`, allowing arbitrary word, shell and degree couplings. With `R_N=G_N^(1/2)`, the Euclidean representatives satisfy

`A~_N = S_N A_N S_N^(-1)`, `S_N=R_N P_N R_N^(-1)`.

Hence every fixed finite-dimensional Hilbertization leaves ordinary spectrum, Jordan form and rational functional-calculus data exactly control-blind. Metric-sensitive quantities may differ, but their separation is bounded by the single static distortion `Delta_N=kappa_2(S_N)=||P_N||_(G_N)^2`. The earlier tensor law `kappa_H(J)^N` is only one special case of this general similarity budget.

The same principle extends to infinite depth whenever the algebraic parity extends boundedly to the chosen Hilbert completion and the multipliers extend boundedly. In that case the source and control remain boundedly similar. Therefore a **metric-only** escape must make parity genuinely unbounded in the completion, or change the domain/operator/control law so the algebraic conjugacy no longer induces a bounded similarity.

The reusable audit is to solve the algebraic reciprocal intertwining relation before attributing spectral leverage to a chosen norm. Nonfactorizing geometry, cross-degree coupling and shell-dependent metrics do not create source information at finite depth when they merely change the condition number of the same involution.

**Boundary.** PC-358 does not classify completions where parity is unbounded, source-forced domains not preserved by parity, genuinely different operators or asymmetric couplings inserted before the reciprocal quotient. It produces no zero-sensitive spectral parameter and implies no RH statement.
