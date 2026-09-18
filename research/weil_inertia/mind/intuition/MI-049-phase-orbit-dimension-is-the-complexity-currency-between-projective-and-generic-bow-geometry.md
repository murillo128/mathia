# MI-049 — Phase-orbit complexity remains priced under controlled charge tails

**Evidence level:** exact synthesis from [WI-347](../../findings/WI-347-projective-bow-compression-costs-linear-source-resolution.md) through [WI-351](../../findings/WI-351-controlled-charge-tails-preserve-the-bow-effective-rank-barrier.md), together with the standard compact-abelian character decomposition audited in WI-350--WI-351.

The gap between projective compression and generic phase-sensitive bow geometry is controlled by the complexity of the phase-cyclic output orbit. WI-350 makes this exact for finite charge support. If a height-independent `U(1)`-equivariant feature is `L`-Lipschitz, has transmission floor `mu`, and every centered output activates at most `D` independent phase characters, then

`r_tau(G) <= D (1 + H Delta L/(4 mu sqrt(tau)))`.

Thus bounded phase complexity restores the linear resolution obstruction: extensive effective rank costs `L/mu=Omega(r_tau/D)`. The generic `Omega(sqrt(r_tau))` tariff of WI-348--WI-349 can be approached under equivariance only by allowing phase complexity itself to grow.

WI-351 closes the obvious soft-tail escape in which infinitely many charge sectors are allowed but most carry tiny amplitude. Let

`B_s=sup_U (sum_q |q|^(2s)||P_q F(z_U)||^2)^(1/2)`

be a uniform charge-Sobolev moment. Truncating to `|q|<=Q` leaves tail norm at most

`T_Q=B_s/(Q+1)^s`.

Whenever `T_Q<mu sqrt(tau)`, the truncated feature still captures every singular direction above the requested threshold after paying the reduced transmission margin, and WI-350 applies with only `2Q+1` active charges. Optimizing `Q` therefore turns the finite-cardinality obstruction into a soft complexity tariff. In the generic sharp regime `L/mu=O(sqrt(r_tau))`, realizing effective rank `r_tau` forces

`B_s/mu = Omega(r_tau^(s/2))`

up to the fixed geometric/threshold constants of the theorem.

Infinitely many microscopic charge sectors are therefore not a free escape from finite phase-orbit dimension. They merely replace a hard support count `D` by a weighted charge-tail resource. To recover generic quadratic packing while retaining controlled transmission, the arithmetic feature must carry a quantitatively growing amount of high-charge mass.

The reusable lesson is that **formal infinite support is not the same as usable orbit complexity**. A representation may contain every character while remaining effectively finite at the destination resolution. The relevant quantity is whichever tail norm controls how many sectors survive above the requested singular-value threshold.

For the physical bow problem, a feature capable of distinguishing `Lambda` from `Lambda^sharp` must now do more than retain phase. It must either violate every relevant controlled charge-moment bound at the rank scale, explain why the distinguished arithmetic covariance forces the necessary growth of `B_s`, or use a different non-equivariant/source-specific mechanism. In every case it must still produce the required signed off-diagonal covariance; charge complexity by itself supplies capacity, not the sign.

**Boundary.** WI-351 assumes `U(1)` equivariance, height-independent Lipschitz control, nonvanishing transmission and a finite `s`-moment bound. It does not constrain non-equivariant maps, uncontrolled heavy charge tails, explicit height dependence, growing aperture or direct arithmetic covariance identities. The result is a feature-complexity obstruction, not a proof of distinguished-twist cancellation, zero simplicity or RH.