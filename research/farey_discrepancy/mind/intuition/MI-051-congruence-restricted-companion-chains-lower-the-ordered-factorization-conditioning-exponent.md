# MI-051 — Congruence-restricted companion chains lower the ordered-factorization conditioning exponent

**Evidence level:** exact/asymptotic paired-coefficient synthesis from [FD-254](../../findings/FD-254-congruence-restricted-chain-entropy-extends-paired-dilation-coercivity.md), sharpening the companion-image reduction in FD-253.

For pure-dilation isolated omissions `E=LD`, the companion set is `C=LD+1`. FD-253 moved the relevant inverse problem from the potentially terrible full support `E union C` to the divisibility geometry of `C`. FD-254 shows that this geometry has its own smaller ordered-factorization entropy because every companion lies in the congruence class `1 mod L`.

Let `rho_L>1` be the unique solution of

`sum_(j>=1) (1+jL)^(-rho_L)=1`.

Then, up to every fixed `H^epsilon` loss,

`kappa(C) <<_(epsilon,L) H^(rho_L-1+epsilon)`,

and the exact paired coefficient mass is bounded by

`sum_(n<=H) |b_n| << C_b K H^(rho_L+epsilon)`,

where `K=|D|`. Thus a family with `K<=H^(alpha+o(1))` cannot hide macroscopic `H^2` coefficient mass whenever `alpha<2-rho_L`. In the parity case `L=2`, `rho_2=1.377785...`, so the protected omission-density window extends to `alpha<0.622214...`, far beyond the unrestricted support threshold inherited from `zeta(rho_*)=2`.

The mechanism is structural rather than a lucky parity estimate. A divisibility chain among numbers `1 mod L` can only grow through factors that are themselves `1 mod L`, so its ordered-factorization branching starts at `L+1` instead of at `2`. The companion image therefore has less chain entropy than a free divisor support even when it is not an antichain.

The remaining paired question is now quantitative: can the **actual** paired inverse, including all non-companion rows, realize a positive-power fraction of this congruence-restricted entropy ceiling, or do those extra rows impose another polynomial loss? FD-254's odd-primorial construction shows that parity companions can still have super-polylogarithmic conditioning, so the problem is not reduced to a polylogarithmic bound.

**Boundary.** The exponent is an upper bound for fixed `L` pure-dilation companion geometry, not a sharp asymptotic for every paired omission family. It does not prove that the full paired inverse attains `H^(rho_L-1)`, and it does not address the independent source-side positivity, squarefree realization, finite reservoir or arithmetic-coherence constraints.