# MI-018 — Stretched Volterra amplitude selection reduces to one endpoint cancellation plus singular-mode matching

**Evidence level:** exact consequence of [PL-310](../../findings/PL-310-stretched-fractional-green-limit-is-a-volterra-plus-diagonal-fixed-profile.md)--[PL-312](../../findings/PL-312-volterra-regular-range-right-inverse.md). The limiting regular range and right inverse are exact. No finite-`s` matched asymptotic expansion, actual completed-Weil endpoint forcing, amplitude formula or RH consequence is claimed.

PL-310 shows that the small-order fractional Green geometry has a universal fixed-`r` limit. After stretching the right boundary by

`x_s(r)=1-2e^(-r/s)`, 

the limiting Green operator is

`(TF)(r)=e^(-2r)F(r)+e^(-r) integral_0^r e^(-q)F(q)dq`,

and its nonzero fixed profiles form the one-dimensional cone

`F(r)=C/sqrt(e^(2r)-1)`.

The principal shape is therefore universal. Source information can only enter through the scalar amplitude or lower-order matching data.

PL-311 identifies the endpoint obstruction: if `f` is endpoint-integrable, `(I-T)f=h`, and `h` is continuous at `0`, then `h(0)=0`. A nonzero constant endpoint forcing cannot be absorbed by an ordinary regular outer correction.

PL-312 proves that, in the continuous correction gauge, there is **no further smooth solvability obstruction hidden behind that condition**. Writing `D(r)=1-e^(-2r)`, one has

`Ran((I-T):C([0,R])->C([0,R])) = {h: h(0)=0, lim_(r->0) h(r)/r exists}`,

and the unique regular preimage is

`Rh = h/D + e^(-r)/sqrt(D) integral_0^r e^(-q)h(q)/D(q)^(3/2)dq`.

For `h in C^1`, solvability is equivalent simply to `h(0)=0`, with `(Rh)(0)=h'(0)`. Thus once the constant endpoint mismatch is cancelled, the remainder is automatically and uniquely absorbed by the regular outer inverse.

The homogeneous equation supplies exactly one excluded mode:

`f_C(r)=C/sqrt(e^(2r)-1) ~ C/sqrt(2r)`.

It is endpoint-integrable but not continuous. This is precisely the PL-310 amplitude profile. Restricting the correction to `C([0,R])` therefore gauges out the amplitude direction rather than determining it.

The missing compensation has a canonical geometric location. Every fixed physical point `x in (-1,1)` satisfies `r_s(x)=O(s)`, so the full macroscopic bulk collapses into a shrinking `r=O(s)` corner. The fixed-`r>0` limit forgets exactly the region in which bulk source information remains spatially resolved.

This makes the finite-`s` matching obligation scalar and explicit. A valid overlap expansion must determine the total first-order outer forcing `h_tot`, enforce

`h_tot(0)=0`,

and simultaneously select the coefficient `C` of the singular homogeneous profile. Once that cancellation holds, no additional family of regular outer Fredholm conditions remains to be solved. Any further difficulty must come from deriving the finite-`s` forcing uniformly, controlling a more singular correction class, or extracting the arithmetic sign of the selected amplitude.

The next theorem should therefore quantify `T_s-T` across the corner/outer overlap or derive an equivalent endpoint cancellation from a uniformly convergent weak/virial identity. Another inversion of the limiting outer operator is no longer useful: PL-312 has completed that problem.

**Boundary.** The exact right inverse applies to the limiting operator and continuous corrections; more singular forcing/corrections occupy a larger class. PL-312 does not prove that the finite-`s` completed-Weil equation has a first-order expansion in this gauge or that the corner term supplies the needed cancellation. The durable conclusion is narrower: for regular outer data, source selection is a one-scalar endpoint matching problem plus the separate singular amplitude mode.