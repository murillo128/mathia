# MI-015 — Diffuse one-profile averaging suppresses local square-root bands and fixes the total Hilbert--Schmidt mass

**Evidence level:** unconditional classicalization from PC-282--PC-285, conditional RH sharpening through [PC-290](../../findings/PC-290-count-matched-l2-transport-reaches-square-root-boundary.md), unconditional square-root boundary results [PC-291](../../findings/PC-291-microscopic-resonance-band-is-spectrally-invisible-at-square-root-resolution.md)--[PC-294](../../findings/PC-294-boundary-log-hilbert-schmidt-mass-is-source-universal.md). The count-matched control is deliberately given the scalar source cardinality `M_q`; no full prime-versus-control collapse of spectral shape at `B~sqrt(q)` is claimed.

After selector subtraction, the complete-domain remainder is a classical logarithmic/digamma Green symbol. Prime dependence in this branch survives only through source placement inside the finite section. PC-285 reproduces that placement with a matched Li-grid control through the unconditional Vinogradov--Korobov range, while PC-287--PC-290 show under RH that the normalized one-profile singular-spectrum laws collapse for every `B=o(sqrt(q))` once total source count is matched.

PC-291 tests the first denominator-microscopic relations at `B~sqrt(q)` and shows narrow local bands remain destination-negligible. PC-292 proves the local invisibility threshold sharp in worst case: a fixed same-source pair already has order-one normalized operator norm on a band `T~N/log q`.

PC-293 separates that worst-case transition from the observable actually averaged over source pairs. For a source law `mu`,

`E ||K^(<=T)/N||_F^2 <= ||mu||_infty E_q(T) + (log q)^2/N^2`.

When `N~sqrt(q)` and `||mu||_infty=O(log q/q)`, every local band `T=O(N)` is `o(1)` in the averaged normalized singular-spectrum law. Both the uniform prime source and the count-matched Li-grid control satisfy this diffuseness scale.

PC-294 then removes the possibility that the missing signal simply lives in the aggregate energy of the nonlocal complement. For the full normalized boundary-log operator,

`|E(mu)-E(u_q)| <= 2(log q)^2 sqrt(q ||mu||_infty/N)`.

At square-root resolution this is `o(1)` for both prime and matched diffuse controls, and the common benchmark tends to `pi^2/12`. Thus the total squared singular-value mass is source-universal at the exact scale where local worst-case residue geometry becomes order one.

The conceptual boundary is now five-way: **microscopic resonance, worst-case local amplitude, source-averaged local amplitude, total spectral mass and spectral shape are different gates**. A one-profile source can have an order-one fixed-pair Hankel mechanism while its local averaged contribution and its full Hilbert--Schmidt mass are both universal.

Any surviving prime-specific one-profile signal must therefore redistribute a fixed asymptotic mass. Candidate destinations are higher spectral moments, top-edge behavior, small-singular-value statistics, or another nonlocal shape observable that is not determined by the Hilbert--Schmidt norm. If those also classicalize, the source information was discarded before one-profile singular-value compression and a richer architecture is required.

The reusable lesson is to test a proposed extremizer against both the **source aggregation** and the **spectral functional** used by the destination. An order-one fixed-pair effect cannot explain an averaged endpoint after diffuse incidence suppresses it, and a nonlocal remainder cannot be called source-specific merely because it contains most of the matrix energy when that total energy is universal.

**Boundary.** PC-290 remains RH-conditional and gives the control `M_q`. PC-293--PC-294 are unconditional and use diffuseness plus the exact residue decomposition. They do not determine higher spectral moments or the full singular-value law at square-root resolution. Measures with large atoms, fixed exceptional pairs, non-averaged observables and richer multi-level summaries remain outside these suppression statements.