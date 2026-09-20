# MI-058 — Exact mixed-shell selection collapses in the interior, and stationary positive boundary geometry cannot repair it

**Evidence level:** exact synthesis from WP-381--[WP-385](../../findings/WP-385-dilation-invariant-positive-forms-cannot-turn-the-fresh-prime-boundary-layer-into-a-mangoldt-selector.md), interpreted against the pointed-bulk controls of WP-378--WP-380.

WP-381 establishes the positive control: the pointed local-Dirichlet geometry admits a bounded interior Riesz coordinate that recovers `Lambda(n)` exactly. WP-382 shows that every fixed finite packet of interior evaluations and jets satisfying exact mixed-shell nullity maps the cyclotomic shell family into one Mangoldt line, and WP-383 extends that collapse to every Banach-valued linear response continuous for the compact-open topology. Boundary accumulation, scale-varying probes, non-compact-open responses, or delayed selection are therefore the honest escapes from the interior theorem.

WP-384 tests the canonical boundary escape. For fixed base `m` and fresh prime `q`, the critically normalized shell `V_{m,q}` tends to zero compact-open but has a nonzero pointed boundary limit with Mellin multiplier
`c_m(tau)=m^(-i tau) prod_{p|m}(1-p^(-1/2+i tau))`.
The escape is topologically real, yet its `D_1` Gram is the classical Nyman modulus-square carrier decorated by finite Euler factors, and mixed shells retain positive energy although `Lambda(mq)=0`.

WP-385 shows that changing the stationary positive boundary metric cannot fix this support failure. Every densely defined closed positive form invariant under the source dilation group is, after Mellin transform, multiplication by a nonnegative spectral weight `w(tau)`. For each fixed base `m`, the finite Euler factor is boundedly invertible on the real Mellin axis:
`alpha_m <= |c_m(tau)| <= beta_m`, with `alpha_m=prod_{p|m}(1-p^(-1/2))>0`.
Hence every such form satisfies
`alpha_m^2 Q(h_1) <= Q(h_m) <= beta_m^2 Q(h_1)`.
In particular `Q(h_m)=0` for even one mixed base forces `Q(h_1)=0`; no fixed nonnegative Mellin reweighting, bounded or unbounded, can turn the fresh-prime boundary family into a Mangoldt selector.

The reusable boundary is now three-stage. Fixed-interior exact selection collapses to the Mangoldt line; the natural fresh-prime boundary layer escapes that topology but classicalizes to a finite-Euler Nyman carrier; and every closed dilation-invariant positive reweighting preserves the same prime-versus-mixed support equivalence because those Euler multipliers never vanish. A surviving Weil-positive route must therefore break this stationary positive scalarization—for example through genuine cross-frequency/nonstationary scale coupling, a finite-`q` prelimit effect that survives globally, an independently controlled indefinite interaction, or delayed finite--archimedean assembly before the final positive scalar is taken.

**Boundary.** WP-385 does not classify non-dilation-invariant boundary operators, off-diagonal Mellin-frequency couplings, `q`-dependent prelimit constructions, indefinite finite--archimedean forms, or nonlinear responses. The theorem also concerns the fixed-base fresh-prime boundary family from WP-384; it is not a no-go for every conceivable boundary representation.
