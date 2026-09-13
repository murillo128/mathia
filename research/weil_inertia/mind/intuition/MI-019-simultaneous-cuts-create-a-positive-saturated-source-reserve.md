# MI-019 — Hilbert cut orientation helps, but generic arbitrary-shift covariance still cannot break the scalar wall

**Evidence level:** exact at a hypothetical attained first unrestricted Suzuki crossing through [WI-274](../../findings/WI-274-simultaneous-cuts-create-a-positive-saturated-source-reserve.md)--[WI-279](../../findings/WI-279-hilbert-cut-covariance-yields-a-bottom-toeplitz-reserve-but-does-not-break-the-scalar-profile-wall.md), with the arbitrary noncommensurate-shift obstruction [WI-280](../../findings/WI-280-noncommensurate-cut-mixtures-cannot-break-the-scalar-profile-wall-generically.md). Prime-overlap remains conditional on a one-signed null mode, and source-specific compatibility of the actual Suzuki cut path remains open.

WI-275 exhausts complementary mass information through the sharp harmonic reserve. WI-276 retains one cross-cut correlation. WI-277 combines several commensurate shifts after scalarizing the cut path. WI-279 shows that this scalarization loses real information: keeping the oriented Hilbert cut vectors gives the exact covariance identity `F_v(r)=S_v-C(2r)` and a bottom-Toeplitz reserve that can be strictly stronger than the scalarized top-spectrum bound.

That improvement is sharp for abstract PSD null-partition geometry, and WI-278 already shows why it does not finish the RH-facing budget: as long as the numerator is only a positive combination of `r lambda_r`, every such reserve is bounded by the same scalar-profile ceiling `sup r lambda_r`, which the admissible counterprofile keeps below `K_+`.

WI-280 removes the apparent escape of choosing arbitrary noncommensurate shifts. For any finite radii `r_j` with nonnegative weights `alpha_j`, a compact two-pulse null-partition path can be arranged so that one selected covariance is `-S/2` and all other selected covariances vanish. Therefore any lower bound

`sum_j alpha_j C(2r_j) >= eta S`

valid for the whole generic PSD cut class must have `eta<0`—indeed `eta<=-alpha_j/2` for each selected witness. The resulting reserve is then strictly below the weighted scalar average and hence cannot exceed `sup r lambda_r`.

The durable distinction is now three-layered. **Scalarization loses information; restoring generic Hilbert orientation recovers some of it; but noncommensurability and generic covariance geometry still do not create the source-specific constraint needed to cross the scalar budget.** A positive result must shrink the admissible cut-path class using the actual Suzuki source/eigenfunction equation, not merely enrich the list of shifts.

Concrete surviving mechanisms include a source law forcing positive weighted covariance for the actual null mode, a stronger source-conditioned numerator than `r lambda_r`, nodal/regularity restrictions excluding two-pulse anti-covariance, or a nonlinear joint invariant not reducible to a positive linear covariance mixture. Each would use information absent from the WI-280 matched generic countermodel.

The sign gate remains separate. All these reserve statements are sign-independent, whereas the prime-overlap tariff is currently one-signed. A stronger source-specific reserve does not by itself control a sign-changing first mode.

**Boundary.** WI-280 does not show that the actual Suzuki cut path realizes the two-pulse geometry. It proves only that PSD/null-partition support geometry, even with arbitrary finite noncommensurate shifts, cannot rule it out. A theorem excluding that countergeometry from the true source class would be exactly the missing new information.