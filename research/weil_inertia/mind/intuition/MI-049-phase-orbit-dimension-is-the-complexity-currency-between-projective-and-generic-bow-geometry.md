# MI-049 — Phase-orbit complexity remains priced under controlled charge tails

**Evidence level:** exact synthesis from [WI-347](../../findings/WI-347-projective-bow-compression-costs-linear-source-resolution.md) through [WI-352](../../findings/WI-352-lipschitz-equivariance-automatically-controls-only-the-first-charge-moment.md), together with the standard compact-abelian character decomposition audited in WI-350--WI-352.

The gap between projective compression and generic phase-sensitive bow geometry is controlled by the complexity of the phase-cyclic output orbit. WI-350 makes this exact for finite charge support. If a height-independent `U(1)`-equivariant feature is `L`-Lipschitz, has transmission floor `mu`, and every centered output activates at most `D` independent phase characters, then

`r_tau(G) <= D (1 + H Delta L/(4 mu sqrt(tau)))`.

Thus bounded phase complexity restores the linear resolution obstruction: extensive effective rank costs `L/mu=Omega(r_tau/D)`. The generic `Omega(sqrt(r_tau))` tariff of WI-348--WI-349 can be approached under equivariance only by allowing phase complexity itself to grow.

WI-351 closes the obvious soft-tail escape in which infinitely many charge sectors are allowed but most carry tiny amplitude. Let

`B_s=sup_U (sum_q |q|^(2s)||P_q F(z_U)||^2)^(1/2)`

be a uniform charge-Sobolev moment. Truncating the charge tail below the destination resolution reduces the problem to WI-350. In the generic sharp regime `L/mu=O(sqrt(r_tau))`, realizing effective rank `r_tau` forces

`B_s/mu = Omega(r_tau^(s/2))`

up to fixed geometric/threshold constants.

WI-352 then shows that the first soft moment is not an independent currency. On the normalized phase-saturated source orbit, `U(1)` equivariance and the same `L`-Lipschitz hypothesis give directly

`B_1<=L`,

and hence `B_s<=L` for every `0<s<=1`. Inserting `B_1<=L` into the WI-351 effective-rank bound yields, with `x=L/(mu sqrt(tau))` and `h=H Delta`,

`r_tau(G) <= (1+4x)(1+hx/2)`.

At natural aperture `h<=1`, inversion recovers only the generic square-root scale

`L/mu = Omega(sqrt(r_tau))`.

First-order angular charge complexity is therefore already paid by the ordinary Lipschitz sensitivity budget; counting it again does not produce a second obstruction.

The threshold at one angular derivative is sharp. WI-352 constructs a Lipschitz equivariant phase orbit with finite `B_1` but infinite `B_(1+epsilon)` for every `epsilon>0`. Ordinary Lipschitz control therefore cannot silently upgrade the soft-tail argument to the stronger moments that would be needed to beat the generic square-root tariff.

The reusable lesson is that **formal complexity currencies must be audited for dependency before being counted as independent resources**. Infinite charge support becomes useful only when enough tail survives destination resolution, and the first Sobolev charge moment becomes useful only if it contains information not already forced by the continuity constant. A stronger charge-tail obstruction begins strictly beyond the regularity supplied for free by Lipschitz equivariance.

For the physical bow problem, a feature capable of distinguishing `Lambda` from `Lambda^sharp` must therefore do more than retain phase or carry a finite `B_1`. It must prove genuinely source-specific higher angular regularity, explain why the distinguished arithmetic covariance forces the necessary high-charge growth, use a different non-equivariant/source-specific mechanism, or directly establish the required signed off-diagonal covariance. Charge complexity supplies capacity, not the sign.

**Boundary.** WI-352 uses Lipschitz control on the full phase-saturated source domain, a strongly continuous unitary `U(1)` representation, scalar phase action and the normalized centered carrier. It does not constrain maps controlled only along the physical height curve, non-equivariant maps, higher regularity supplied by an independent arithmetic theorem, uncontrolled heavy charge tails, explicit height dependence, growing aperture or direct covariance identities. The result is a feature-complexity dependency theorem, not a proof of distinguished-twist cancellation, zero simplicity or RH.