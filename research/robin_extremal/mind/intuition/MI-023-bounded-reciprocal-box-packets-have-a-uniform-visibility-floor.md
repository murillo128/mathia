# MI-023 — Reciprocal-box visibility decays exponentially with scaled radius, and that rate is sharp

**Evidence level:** exact reciprocal-box visibility theorem from [RE-135](../../findings/RE-135-fixed-reciprocal-box-packets-have-a-cardinality-free-visibility-floor.md), quantitatively sharpened by [RE-136](../../findings/RE-136-reciprocal-box-visibility-has-a-sharp-exponential-radius-law.md)

RE-135 removes occupancy as an escape mechanism. For any fixed scaled reciprocal box around a target strict-subedge zero, an arbitrary finite local Robin packet has a cardinality-free visibility floor because its normalized local spectrum is a probability measure on one compact set and its Fourier--Laplace transform satisfies `F(0)=1`.

RE-136 prices the only remaining local noncompactness. For normalized positive-measure transforms supported in a scaled box of radius `R`, a fixed relative interval has visibility at least

`exp(-C_kappa R)`.

The order is sharp: matched subset-product packets achieve residual `exp(-c_kappa R)`. Thus hiding by a factor `epsilon` costs scaled radius `Omega(log(1/epsilon))`; the deterioration of the compactness constant is not merely a proof artifact.

The same quantitative floor transfers to the physical Robin packet for radii `R(U)` up to a sufficiently small constant multiple of `log U`:

`sup_((1-kappa)U<=u<=U)|S_(C_U,K)(u)| >= exp(-C_*R(U)) #C_U |a_(rho_0,K)(U)|`.

So the surviving attained-edge problem is no longer qualitative reciprocal-scale tightness. It is a **competition of exponents**: source information about the actual exterior packet must make the mass available beyond scaled radius `R` decay faster than the local visibility floor `exp(-C R)`, at least over the logarithmic radius window where the transfer is valid.

This turns concentration--compactness into a quantitative budget. Local cardinality is irrelevant; radius buys cancellation only exponentially; and the formal matched class shows that this exchange rate cannot be improved without additional zeta-specific information.

**Boundary.** RE-136 does not prove reciprocal-scale tightness for actual zeros or control the exterior mass. The exponential floor is a local visibility theorem and matched formal packets show sharpness only in the admitted formal class. The nonattained edge and `Theta=1` branches remain separate.