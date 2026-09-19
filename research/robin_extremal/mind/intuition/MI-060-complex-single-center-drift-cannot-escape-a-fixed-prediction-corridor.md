# MI-060 — Center drift must cross the local phase threshold and then pay the macroscopic/Wiener cost

**Evidence level:** exact synthesis from [RE-229](../../findings/RE-229-bounded-complex-single-center-vanishing-arcs-have-divergent-wiener-rate.md)--[RE-235](../../findings/RE-235-super-broad-complex-single-centers-force-an-exponentially-thin-arc-or-divergent-wiener-rate.md).

The remaining single-center loophole after fixed-parameter analysis was to let the center and corridor drift with scale. RE-229--RE-231 identify the microscopic transition: bounded complex drift and subcritical large-center load leave residual delay, while positive-real load past the unit threshold can flatten the local `u=m theta` profile.

RE-232--RE-234 show that crossing this local gate is not a useful global escape at finite load. The predicted fixed arc has a sharp macroscopic radius, but the Wiener rate remains above `6`; complex phase reduces the radial predictive component without reducing the coefficient budget correspondingly, so the positive-real ray is already the cheapest finite-ray representative.

RE-235 closes the super-broad continuation outside the inverse-center layer. For `tau=N/(m|a|)->infinity`, any fixed positive contracting arc forces `(1/m) log ||F||_A -> infinity`. More generally, when `|a| sin(alpha)>=1`, bounded normalized Wiener rate forces the arc to satisfy an exponentially thin bound of order `tau^(-1+1/m) 2^(-tau)` up to bounded factors. Sending the load to infinity therefore does not create a cheap fixed-arc predictor; it can only survive by collapsing the destination exponentially fast.

The reusable audit has four currencies: local normal-form threshold, effective predictive load, macroscopic destination width, and global coefficient/Wiener cost. Parameter drift counts as a new mechanism only if it improves the destination-visible approximation without paying the same or a worse global cost. Microscopic flattening, equality-layer tuning, complex tilt and super-broad load each fail that test in the regimes now classified.

**Boundary.** RE-235 leaves the separate inverse-center layer `|a| sin(alpha)<1`, scale regimes outside its contraction hypotheses, and genuinely different architectures such as multi-center/minimax or rational predictors. The results do not improve the universal separated lower bound and do not imply RH.