# MI-028 — Empty-side moving Julia reduction has a universal logarithmic boundary layer

**Evidence level:** exact moving-node scaling-limit obstruction from [WP-314](../../findings/WP-314-empty-side-moving-julia-boundary-layer-is-universal-logarithmic-control.md), extending the fixed-node and stable-limit boundaries WP-312--WP-313

WP-312 closes every finite fixed-real-node Julia--Nevanlinna repair and WP-313 closes infinite fixed-node chains whenever the relevant high-energy discriminator passes to the limit. WP-314 tests the canonical nonuniform loophole: move a regular boundary node to `X->infinity` on the empty positive side of the reflected Mangoldt support and observe on the node scale `z=X zeta`.

After the canonical unit-log normalization, the reduced Pick function converges locally uniformly to

`J_*(zeta)=((zeta-1) Log zeta)/((zeta-1)-Log zeta)`.

This limit is exactly the Julia reduction of the synthetic unit-density logarithmic control `Log zeta`. The arithmetic remainder in the Mangoldt counting law disappears completely. On fixed spectral compacta the same family degenerates instead to a constant.

Thus noncommutation of the moving-node and high-energy limits is real, but it is not automatically an arithmetic escape. At the natural empty-side scale the source has density one, so rescaling sees Lebesgue measure and the moving Julia layer becomes universal before the Gamma curvature discriminator is reached. The universal layer even changes the logarithmic shape itself rather than revealing the desired archimedean correction.

The surviving scalar question is therefore narrower: a moving boundary operation must be tied to a **source-specific fluctuation scale**, not merely to the bulk location of a regular node. It must preserve Pick positivity while magnifying a nonuniversal part of the Mangoldt measure strongly enough that the unit-density tangent no longer dominates, and it must still match the Gamma asymptotic hierarchy after rescaling.

**Boundary.** WP-314 treats the canonical empty-side regular-node scaling `z~X`. It does not close moving nodes near the reflected arithmetic support, different source-dependent scalings, matrix/operator-valued reductions, noninvertible operations, or explicit finite--archimedean couplings.