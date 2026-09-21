# MI-072 — Polynomial rank-coupled Ford coverage recovers the Euler anchor

**Evidence level:** exact Fourier-reconstruction synthesis from [NB-264](../../findings/NB-264-fixed-power-carrier-locked-shallow-meshes-recover-the-euler-anchor-at-bounded-hilbert-cost.md), locating the rank-coupled boundary left open by NB-263.

For an Euler-normalized resolved carrier with `J=mK` and bounded coefficient `ell^2` norm, the anchor `sum c_j=1` admits an exact absolutely summable reconstruction from carrier-locked shallow Ford samples. The reconstruction coefficients have total mass `O(1)`, individual size `O(1/m)`, and rapidly decaying frequency tails.

Consequently, on every fixed-power rank-coupled mesh radius `B_K=K^delta`, `delta>0`,

`sum_(|n Delta_m|<=K^delta) |D_n| >= c m`

for large `K`; in particular the carrier cannot converge uniformly to zero on that mesh at bounded Hilbert cost. At the live depth `u=log m+O(1)`, a cone-aligned matched subpacket inside this still-`o(J)` central window recovers order-one residue mass.

This resolves the quantifier gap in NB-263. Preassigned or sufficiently slow-growing strips can be flattened by choosing rank afterward, but bounded-cost suppression cannot extend to any fixed polynomial power of the eventual rank. A suppressing bounded-cost sequence must keep the covered carrier-locked radius in the subpolynomial regime `K^(o(1))`.

**Boundary.** The theorem is a matched source/destination-interface obstruction, not a statement that actual zeta zeros occupy the reconstructed mesh. It also leaves the subpolynomial rank-coupled window and exact Hardy-projected consequences open. The relevant next scale is therefore between preassigned/subpolynomial coverage and fixed-power coverage, with variation and final projection still charged.