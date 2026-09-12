# MI-011 — Finite-start dephasing is equivalent at top scale to weighted bounded-determinant crowding

**Evidence level:** exact deterministic weighted-Hilbert reduction through VIS-195, combined with the VIS-192 Cesaro variance law. No estimate proving `D_v=o(y^2)` or optimality of `D_v` is established.

VIS-192 writes the signed prime-ratio observable as a finite exponential polynomial with frequencies `lambda=+/-log(q/p)` and coefficient energy `R_v=sum |c_lambda|^2`. Its infinite-start variance is `asymp 1/H` in the relevant diverging subcritical regime. VIS-193 transfers this to every deterministic start once the window length is `O(y^2)`, but that scale comes from the single smallest gap in the entire frequency set.

VIS-194 replaces the worst gap by the weighted local-spacing resource

`D_v = [sum_lambda |c_lambda|^2/delta_lambda] / R_v`.

Uniformly in the start `T0`, a window `L` pays only `O(D_v/L)` relative mean-square error. Thus a rare tiny gap matters only in proportion to the coefficient energy carried by the corresponding frequency.

VIS-195 identifies the remaining arithmetic content exactly. Prime parity gives the universal spacing floor

`b_y=log(1+2/y^2)`,

and if `C(A)` is the coefficient-energy mass on frequencies with `delta_lambda<=A b_y`, then

`b_y D_v = integral_1^infinity C(A) A^(-2) dA`.

Hence

`D_v=o(y^2)  <=>  C(A)->0 for every fixed A>1`.

At fixed `A`, every dangerous collision eventually comes from top-scale odd prime products satisfying one of

`qr-ps=h`,  `qs-pr=h`,

where `h` belongs to a fixed finite set of nonzero even integers and every participating prime is a positive proportion of `y`. Conversely any such bounded-determinant collision at macroscopic product scale lies in a fixed normalized-crowding class. Therefore `D_v=o(y^2)` is equivalent to vanishing **weighted** mass on every fixed top-scale bounded-determinant incidence family.

The dephasing problem is no longer “prove typical prime ratios are separated.” It is to show that the taper-generated coefficient measure avoids the finitely thin determinant surfaces strongly enough. Unweighted incidence counts are only useful insofar as they control that weighted mass; a spectacularly close ratio carrying negligible coefficient energy is harmless.

**Boundary.** The equivalence concerns the sufficient Hilbert resource `D_v`; it does not prove that `D_v` is the optimal deterministic observation horizon. VIS-195 also gives only the universal constant-factor fallback `D_v<=y^2/2+O(1)`. A genuine subquadratic gain still requires new arithmetic control of the weighted determinant incidences.