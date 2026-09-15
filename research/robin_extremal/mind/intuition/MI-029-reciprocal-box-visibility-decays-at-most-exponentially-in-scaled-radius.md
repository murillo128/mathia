# MI-029 — Reciprocal-box visibility is exponentially sharp for pure vertical escape on the proved one-sided window

**Evidence level:** exact positive-measure visibility lower bound from [RE-145](../../findings/RE-145-reciprocal-box-visibility-has-an-exponential-scaled-radius-floor.md), with one-sided functional-order sharpness supplied by the corrected matched control [RE-151](../../findings/RE-151-one-sided-vertical-product-packets-isolate-reciprocal-escape.md).

For a normalized positive empirical Robin packet confined to a reciprocal-scale box of radius `R`, RE-145 gives a cardinality-free local floor

`sup_I |F_mu| >= c_kappa exp(-C_kappa R)`.

Thus `R(U)=o(log U)` still forces a `U^(-o(1))` normalized visibility floor, although it need not give a fixed positive margin.

RE-151 shows that exponential deterioration can be realized without horizontal drift. A matched simple finite-edge packet can place every active atom at the same real part as the target, keep the target scale-maximal, and use only vertical subset-product phase geometry. With scaled vertical radius `R_j`, its contribution on the **one-sided** relative window

`u in [(1-kappa)U_j,U_j]`

can be suppressed by `exp(-c R_j)` relative to the target, while `R_j` tends to infinity as slowly as prescribed and the off-critical packet population remains sparse.

This is the corrected scope of the sharpness statement. The earlier symmetric-window formulation was invalid: the product contraction used for RE-151 is guaranteed only before the anchor time. No matching obstruction has been proved on the upper half `[U_j,(1+kappa)U_j]`.

The reusable lesson is therefore two-sided. Horizontal localization and upper population counts cannot improve the **proved one-sided** visibility exponent by themselves; an actual-zeta input must constrain vertical occupancy/phase geometry there. But a symmetric Robin-window theorem may still gain information from the post-anchor half, so the one-sided matched control must not be silently promoted to a symmetric no-go.

**Boundary.** RE-151 is a matched-control spectrum, not an actual-zeta construction. It preserves the relevant finite-edge symmetry and sparse counting but not Euler-product or other source-specific zero laws. Its sharpness is one-sided in observation time.