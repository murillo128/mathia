# MI-029 — Reciprocal-box visibility is exponentially sharp even for pure vertical escape

**Evidence level:** exact positive-measure visibility lower bound from [RE-145](../../findings/RE-145-reciprocal-box-visibility-has-an-exponential-scaled-radius-floor.md), with functional-order sharpness strengthened by [RE-149](../../findings/RE-149-zero-horizontal-spread-product-packets-isolate-vertical-escape.md).

For a normalized positive empirical Robin packet confined to a reciprocal-scale box of radius `R`, RE-145 gives a cardinality-free local floor

`sup_I |F_mu| >= c_kappa exp(-C_kappa R)`.

Thus `R(U)=o(log U)` still forces a `U^(-o(1))` normalized visibility floor, although it need not give a fixed positive margin.

RE-149 shows that the exponential dependence cannot be blamed on horizontal drift. For every fixed relative observation window one can construct matched simple finite-edge packets whose active atoms all have **exactly the same real part** as the target. The target is the unique scale-maximal coefficient, while vertical offsets alone form a subset-product phase pattern. With scaled vertical radius `R_j`,

`sup_I |packet| <= C exp(-c R_j) |target|`,

and `R_j` may tend to infinity as slowly as prescribed. The normalized positive-measure version has the same exponential suppression.

So the `exp(-O(R))` lower theorem and `exp(-Omega(R))` controls match in functional order even on a vertical line. Horizontal localization, one-sided shell estimates and upper population counts do not by themselves improve this local floor. The missing actual-zeta input must constrain **vertical occupancy/phase geometry** or introduce another source relation that the abstract positive-measure model lacks.

This also clarifies the role of packet complexity. Actual-zero counting can prevent arbitrarily many modes in a fixed absolute ordinate band, but it does not forbid scaled vertical radius from diverging with the observation scale. Radius and count are related only after the source theorem specifies the relevant absolute/scaled conversion.

**Boundary.** RE-149 is a matched-control theorem, not a construction inside the actual zeta zero set. It preserves finite-edge symmetry and sparse one-level counts but not Euler-product, pair-correlation or other source-specific zero laws. The conclusion is sharpness of the representation-level visibility rate, not existence of the bad packet for zeta.