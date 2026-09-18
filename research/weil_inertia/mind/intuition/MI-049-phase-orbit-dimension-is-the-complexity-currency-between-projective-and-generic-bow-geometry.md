# MI-049 — Phase-orbit dimension is the complexity currency between projective and generic bow geometry

**Evidence level:** exact synthesis from [WI-347](../../findings/WI-347-projective-bow-compression-costs-linear-source-resolution.md), [WI-348](../../findings/WI-348-global-phase-sensitivity-still-needs-resolution-collapse.md), [WI-349](../../findings/WI-349-physical-bow-carrier-saturates-the-quadratic-resolution-cost.md), and [WI-350](../../findings/WI-350-bounded-phase-orbit-dimension-restores-linear-bow-resolution-cost.md), together with the standard compact-abelian character decomposition audited in WI-350.

The gap between projective compression and generic phase-sensitive bow geometry is controlled by a concrete algebraic complexity: the dimension of the phase-cyclic output orbit. Let a height-independent feature be `U(1)`-equivariant, `L`-Lipschitz, have transmission floor `mu`, and suppose every centered output activates at most `D` independent phase characters. WI-350 proves

`r_tau(G) <= D (1 + H Delta L/(4 mu sqrt(tau)))`.

Thus bounded phase complexity restores the linear resolution obstruction that was previously visible only in a single projective/fixed-charge sector. Whenever `r_tau(G)>D`,

`L/mu >= (4 sqrt(tau)/(H Delta))(r_tau(G)/D - 1)`.

For fixed aperture and bounded `D`, extensive effective rank costs `L/mu=Omega(r_tau)`. The generic `Omega(sqrt(r_tau))` tariff of WI-348--WI-349 can be approached under equivariance only if the phase-orbit dimension itself grows. In the compact-abelian decomposition, `D` is exactly the number of distinct active charge sectors in the output vector, not the ambient representation dimension.

This converts “phase sensitivity” from a binary label into a priced resource. One active charge reproduces the projective linear obstruction. Boundedly many charges preserve it up to the factor `D`. Unrestricted phase complexity can recover the quadratic ordinary covering law, but only by paying in growing charge support. The apparent escape from projective compression is therefore not free information; its cost is a growing source-to-feature orbit dimension.

For the physical bow problem this sharpens the next test. A natural arithmetic feature capable of distinguishing `Lambda` from `Lambda^sharp` must either have quantitatively controlled phase-orbit dimension, in which case WI-350 supplies a direct rank-resolution obstruction, or explain why the distinguished arithmetic covariance necessarily activates a growing family of charge sectors. Either route must still produce the required signed off-diagonal destination information; phase complexity alone does not create the covariance sign.

**Boundary.** The theorem assumes `U(1)` equivariance, a height-independent feature, Lipschitz control and nonvanishing transmission. It does not restrict non-equivariant maps, growing `D`, collapsing `mu`, growing aperture or explicit height dependence. Most importantly, it is a structural feature-complexity theorem, not a proof of distinguished-twist cancellation, zero simplicity or RH.