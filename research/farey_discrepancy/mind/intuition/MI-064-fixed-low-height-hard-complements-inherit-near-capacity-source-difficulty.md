# MI-064 — Fixed low-height hard complements inherit near-capacity source difficulty

**Evidence level:** supported by [FD-298](../../findings/FD-298-low-height-hard-complements-are-near-capacity-equivalent-to-the-block-mertens-field.md) together with the rigidity regime isolated in FD-297.

FD-298 separates the block Mertens field into the explicit central term, a low-height spectral packet, and the remaining hard complement,

`G_N = C_N + G_(T,N) + R_(T,N)`.

At the near-capacity scale tested in the current Farey route, the central term and every fixed low-height packet are lower order. Consequently the normalized hard complement `R_(T,N)` and the original source field `G_N` differ by an asymptotically negligible amount. Removing finitely much low-height spectral information therefore does not soften the source at the scale where the capacity obstruction is tested.

Combined with the FD-297 rigidity regime, this means that a low-height hard-complement strategy cannot obtain a near-capacity gain merely by peeling off a fixed packet of easy zeros. Whenever the original block field is already forced into the rigid source geometry, its fixed-height hard complement inherits the same difficulty up to the relevant normalization. In the extreme sub-first-zero regime the nonpacket complement simply coincides with the source contribution after the explicit deterministic pieces are removed.

The useful distinction is between **spectral decomposition** and **capacity reduction**. A decomposition can isolate visually or analytically simpler components without reducing the norm scale that the final argument must beat. To create a genuinely easier residual, a moving cutoff would need a quantitative theorem showing that the removed packet carries a non-negligible fraction of the near-capacity obstruction, rather than merely increasing the amount of explicitly represented spectral data.

**Boundary.** The equivalence is a near-capacity statement for fixed, or otherwise sufficiently controlled, low-height packets in the proved rigidity regime. It does not rule out a moving-height decomposition whose removed packet is shown independently to capture a macroscopic part of the relevant norm, nor does it supply cancellation beyond the established normalization.