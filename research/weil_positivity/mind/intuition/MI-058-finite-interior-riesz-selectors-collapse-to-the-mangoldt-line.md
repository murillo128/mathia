# MI-058 — Exact mixed-shell selection forces an interior Mangoldt line, while the canonical boundary escape classicalizes to a Nyman Gram

**Evidence level:** exact synthesis from WP-381--[WP-384](../../findings/WP-384-fresh-prime-critical-boundary-layer-is-a-finite-euler-weighted-nyman-gram.md), interpreted against the pointed-bulk controls of WP-378--WP-380.

WP-381 establishes the positive control: the pointed local-Dirichlet geometry admits a bounded interior Riesz coordinate that recovers `Lambda(n)` exactly. The obstruction is therefore not the mere existence of a bounded Mangoldt selector. WP-382 shows that every fixed finite packet of interior evaluations and jets satisfying exact mixed-shell nullity maps the cyclotomic shell family into one Mangoldt line, and WP-383 extends the collapse to every Banach-valued linear response continuous for the compact-open topology.

The WP-383 mechanism is topological. Adjoining a fresh prime gives a dilation `z -> z^q`; on any fixed compact subdisk that spectator term disappears exponentially. Compact-open continuity forces even an infinite response packet to ignore it, so exact mixed-shell nullity determines the primitive-shell response. This leaves boundary accumulation, scale-varying probes, non-compact-open responses, or delayed selection as the honest escapes.

WP-384 shows that crossing this boundary is necessary but not sufficient. Fix `m>1`, adjoin a fresh prime `q`, and normalize `V_{m,q}=F_{mq}/sqrt(mq)`. Then `V_{m,q}->0` compact-open, yet its pointed `D_1` Gram converges to
`(1/(2 pi)) int c_m(tau) conjugate(c_n(tau)) |zeta(1/2+i tau)|^2/(1/4+tau^2) d tau`,
with
`c_m(tau)=m^(-i tau) prod_{p|m}(1-p^(-1/2+i tau))`.
So the canonical critical boundary layer really escapes WP-383, but its sign carrier is the classical Nyman modulus-square density decorated only by finite Euler/Jordan factors. In particular every fixed mixed shell retains strictly positive limiting energy although `Lambda(mq)=0`.

The reusable boundary is therefore twofold. An interior exact selector collapses to the Mangoldt line; a natural boundary layer can avoid that topology yet still classicalize to an unconditional positive Gram that has the wrong support and no Gamma/polar completion. A surviving Weil-positive route must use boundary or scale dependence whose source-derived interaction is not reducible to the Nyman carrier, or postpone mixed-shell selection until the finite and archimedean terms have coupled.

**Boundary.** WP-384 classifies the fixed-base fresh-prime critical `D_1` boundary layer, not every singular boundary response. The finite Euler multipliers remember the primes dividing the base but do not create prime-power support after modulus-square scalarization. No conclusion is claimed for a different source-forced boundary domain, nonlinear response, or delayed-selection construction that escapes both the compact-open collapse and the Nyman classicalization.
