# MI-049 — Abel cubic singular-series asymptotics isolate an RH-equivalent zero layer at model level

**Evidence level:** exact/literature-based synthesis from [PL-403](../../findings/PL-403-abel-cubic-singular-series-rh-equivalence.md), refining the zero-sensitive Mellin layer of PL-402. The RH equivalence is a line-specific smooth consequence of the classical Goldston--Suriajaya continuation/Riesz theory, not a new independent RH criterion.

The unregularized cubic kernel of PL-402 has the right nonzero Mellin response at every zeta-zero pole but insufficient vertical decay for naive full half-line inversion. PL-403 inserts Abel damping in the same cubic variable,

`w_eta(u)=exp(-eta u^3) sin(pi u^3/6)/u`, `eta>0`,

whose Mellin transform has genuine exponential vertical decay and remains nonzero at every `s_rho=rho/2-1`. The regulator therefore fixes the inversion problem without deleting the zero layer.

For the Hardy--Littlewood pair singular series, the normalized cubic average has the asymptotic

`A_eta(H)=phi_eta/3 - [Gamma(2/3) R_eta^(1/3) sin(phi_eta/3)]/(2H) + O_(eta,epsilon)(H^(-7/4+epsilon))`.

For every fixed `eta>0`, this estimate for all `epsilon>0` is equivalent to RH. The leading `H^0` term is the Gallagher mean, the deterministic `H^-1` term is explicit, and the nontrivial-zero poles begin at `H^(rho/2-2)`; on RH their real exponent is `-7/4`. A parity-only control keeps the leading cubic mass but has neither the `H^-1` singular-series layer nor the zeta-zero layer, so the subleading hierarchy is genuinely arithmetic rather than a cubic-phase artifact.

The durable route correction is that **the regularization and deterministic-layer problems are solved at the singular-series model level**. The unresolved Prime-Lattice step is no longer to show that the cubic kernel can see the zeta divisor; it is to transfer this regulated asymptotic to the actual incomplete-gamma continuation observable with aggregate error below the `H^-7/4` scale.

**Boundary.** PL-403 is a statement about the classical pair singular series, not about actual `Lambda(r)Lambda(r+d)` correlations. Its converse uses the known meromorphic continuation of the singular-series Dirichlet series. The remaining transfer requires a new uniform comparison theorem for the exact Prime-Lattice statistic; the model-level RH equivalence cannot be promoted across that bridge by analogy.