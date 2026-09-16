# MI-034 — Separated Jordan supports cannot hide the adverse zero reservoir

**Evidence level:** exact source-specific synthesis from [NB-159](../../findings/NB-159-fixed-finite-polynomial-height-samplers-export-a-routine-negative-zero-lobe.md) and [NB-160](../../findings/NB-160-poisson-width-sign-separation-forces-a-routine-adverse-zero-reservoir.md), using the explicit local Riemann--von Mangoldt count already audited in the line.

The failure of the zero-mass exterior selector is not fundamentally about using finitely many atoms. NB-160 upgrades the obstruction to arbitrary finite signed Borel height measures. If the sampler has zero total mass, a positive top atom of size `c_G`, total variation `O(c_G)`, polynomially high support, and its positive and negative Jordan supports are separated by a sufficiently large fixed additive distance, then the target window retains positive order-`c_G` charge while the negative support generates total adverse zero charge `Omega(c_G log G)`.

The mechanism is measure-valued. Each infinitesimal negative mass element sees `Theta(log G)` zeta zeros within one Poisson width. Integrating this local density over the negative Jordan measure preserves an `Omega(c_G log G)` negative contribution. By contrast, the zero-summed tail from the separated positive support is only `O(c_G log G/Delta)`, so a large enough fixed separation cannot cancel the routine reservoir.

Thus **growing cardinality and continuous spreading do not buy selectivity while the two signs remain separated at the Poisson scale**. The geometric resource is overlap of the Jordan signs, not the number of sampler components. A genuinely new signed construction must make positive and negative mass interlace/collapse within `O(1)` widths so the same local zero population sees both signs, accept worsening conditioning or lower-height geometry, or couple signs to source arithmetic before taking absolute Jordan pieces.

This also sharpens the interpretation of moment cancellation. Zero total mass and further completed-Gamma/Stirling moments may remove universal backgrounds, but they do not determine where the compensating sign debt lands. If the debt is geometrically separated, routine zero density dominates independently of how finely it is distributed.

**Boundary.** NB-160 does not exclude interlaced/collapsing sign supports, support extending to heights with `log H_G=o(log G)`, unbounded conditioning, or source-coupled cancellation before Jordan separation. Those are now the precise escapes rather than generic “more sampling heights.”
