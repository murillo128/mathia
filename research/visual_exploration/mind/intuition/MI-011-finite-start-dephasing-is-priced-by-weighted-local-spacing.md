# MI-011 — Finite-start dephasing is priced by coefficient-weighted local spacing, not the worst prime-ratio gap

**Evidence level:** exact deterministic weighted-Hilbert reduction through VIS-194, combined with the VIS-192 Cesaro variance law. No arithmetic improvement `D_v=o(y^2)` or optimality of `D_v` is proved.

VIS-192 writes the signed prime-ratio observable as a finite exponential polynomial with distinct frequencies `lambda=+/-log(q/p)` and coefficient energy

`R_v(y,H)=sum_lambda |c_lambda|^2`.

Its infinite-start variance is `asymp 1/H` in the relevant diverging subcritical regime. VIS-193 transfers this to every deterministic start interval once the window length is `O(y^2)`, but that scale comes from the single smallest gap in the entire frequency set.

VIS-194 applies the weighted Montgomery--Vaughan Hilbert inequality instead. Give each frequency its own nearest-neighbor spacing `delta_lambda` and define

`W_v=sum_lambda |c_lambda|^2/delta_lambda`,

`D_v=W_v/R_v`.

Then uniformly in the start `T0`,

`|R_(v,L)(T0;y,H)-R_v(y,H)| <= (3 pi D_v/L) R_v(y,H)`.

Thus the deterministic observation horizon is controlled by an **energy-weighted inverse local spacing**. A near collision with negligible coefficient mass should not price the whole experiment. `L>=C D_v` suffices for the same `O(1/H)` cancellation, while `L/D_v->infinity` gives uniform asymptotic recovery of the Cesaro variance.

The old `y^2` scale remains a rigorous universal ceiling because every `delta_lambda^(-1)<=y^2+1`. The gain is conceptual and quantitative only if arithmetic/taper structure makes the weighted average much smaller. VIS-194 supplies a pair-dependent floor as well, but does not by itself prove such concentration avoidance.

The next source theorem is therefore a weighted multiplicative-collision statement: estimate how much tapered coefficient energy can sit on densely packed prime ratios. This is a different resource from the worst rational spacing and from the absolute `y/log y` resolution threshold.

**Boundary.** `D_v` is the sufficient horizon produced by this classical weighted Hilbert inequality; it is not proved necessary or optimal. No pointwise-in-start cancellation is asserted below this scale, and no improvement over `y^2` follows without a new arithmetic estimate on the weighted near-collision geometry.