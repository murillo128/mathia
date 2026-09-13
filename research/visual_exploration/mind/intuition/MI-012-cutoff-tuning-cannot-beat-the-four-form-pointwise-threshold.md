# MI-012 — Averaged four-form dephasing has a sharp square-root-log method threshold

**Evidence level:** exact as a statement about the VIS-201 upper-bound architecture through VIS-202, using the cited Henriot/Nair--Tenenbaum discriminant-uniform polynomial average and the persisted dimension-four sieve/taper decomposition. It is not a lower bound on the true collision energy, `D_v`, or the optimal observation horizon.

VIS-200 showed that scalar cutoff tuning cannot beat the four-form pointwise threshold. VIS-201 then attacks the ingredient that caused the extra loss rather than retuning the split. On each nondegenerate top-scale four-prime fiber, the local conductor reduces to three primitive affine polynomial values; Henriot's discriminant-uniform Nair--Tenenbaum bound gives a bounded-mean arithmetic majorant after averaging over the second-gap fiber.

That averaging removes the pointwise `log log y` loss and leaves the generalized cutoff bound

`C_(y,H)(A) << (log y)^2/log(H/L)^4 + (log y)^2/L^3 + H/(y log y)`

for fixed crowding multiplier `A` under the standing subcritical hypotheses.

VIS-202 identifies the exact cutoff frontier of this majorant. There exists an admissible scalar cutoff `L=L(y)` for which all three positive terms vanish **if and only if**

`log H / sqrt(log y) -> infinity`.

Necessity is forced by the first term because `log(H/L)<=log H`; the taper tail cannot compensate for it. Conversely, `L=log y` makes the tail vanish and preserves `log(H/L)~log H` whenever the displayed ratio diverges. The square-root-log scale is therefore not an artifact of a poor cutoff choice after local-factor averaging: it is the sharp threshold of the current dimension-four fiberwise sieve plus taper-tail proof architecture.

This closes scalar cutoff optimization on both sides of VIS-201. To reach the boundary `log H=Theta(sqrt(log y))` or smaller, one must alter a structural currency: couple determinant fibers before scalarization, exploit cancellation or packing across fibers, lower the effective incidence dimension, strengthen the fourth-prime input, obtain a genuinely sharper tail mechanism, or replace the sufficient resource `D_v`.

**Boundary.** VIS-202 proves a method threshold, not a physical/source threshold. It does not show that `C_(y,H)(A)` stays nonzero at the boundary, that `D_v=o(y^2)` is impossible there, or that no other dephasing statistic can work. The fixed-`A`, nondegenerate four-form and strictly subcritical assumptions remain load-bearing.