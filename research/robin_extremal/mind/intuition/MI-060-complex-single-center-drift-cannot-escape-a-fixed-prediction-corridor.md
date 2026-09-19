# MI-060 — Single-center drift must pay Wiener cost; the inverse-center exception was only a proof artifact

**Evidence level:** exact synthesis from [RE-229](../../findings/RE-229-bounded-complex-single-center-vanishing-arcs-have-divergent-wiener-rate.md)--[RE-236](../../findings/RE-236-full-arc-contraction-eliminates-the-inverse-center-exception.md).

RE-229--RE-231 identify the microscopic transition: bounded complex drift and subcritical large-center load leave residual delay, while positive-real load past the unit threshold can flatten the local `u=m theta` profile. RE-232--RE-234 show that crossing this gate does not buy a competitive global predictor at finite load: the fixed arc can be predicted, but the normalized Wiener cost stays above the best existing separated construction.

RE-235 pushes the same audit into the super-broad regime `tau=N/(m|a|)->infinity`. Outside the inverse-center layer it proves that bounded normalized Wiener rate forces the observed arc to shrink exponentially in `tau`. Its apparent exception `|a| sin(alpha)<1` came from a coarse phase estimate used to control the DC normalizer.

RE-236 shows that this exception is not geometrically real. Full contraction on the symmetric arc implies

`1-|1-1/a| > sin(alpha)/(sqrt(3)|a|)`,

so the exact coefficient lower bound applies with no condition relating `alpha` to `1/|a|`. Every contracting super-broad single-center predictor with bounded normalized rate is forced into the same exponentially thin destination regime, with `sin(alpha)` bounded essentially by `tau^(-1) 2^(-tau)` up to the explicit finite-`m` factors.

The reusable audit has four currencies: local normal-form threshold, effective predictive load, macroscopic destination width and global coefficient/Wiener cost. Parameter drift counts as a new mechanism only if it improves destination-visible approximation without paying the same or a worse global cost. The inverse-center split failed this test because it was created by an information-losing estimate, not by a new source geometry.

**Boundary.** RE-236 still assumes a contracting symmetric arc and the single-center truncated negative-binomial representation. It does not rule out the genuinely coupled exponentially thin-arc scaling, noncontracting constructions, multi-center/minimax predictors, rational predictors or other bases, and it does not improve the universal separated constant by itself. Its exact contribution is to close the artificial inverse-center branch.