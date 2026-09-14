# MI-018 — Stretched Volterra amplitude selection is an endpoint matching problem

**Evidence level:** exact consequence of [PL-310](../../findings/PL-310-stretched-fractional-green-limit-is-a-volterra-plus-diagonal-fixed-profile.md) and [PL-311](../../findings/PL-311-stretched-volterra-endpoint-range-obstruction.md). The endpoint range condition and coordinate compression are exact. No finite-`s` matched asymptotic expansion, nonzero source boundary value, amplitude formula or RH consequence is claimed.

PL-310 shows that the small-order fractional Green geometry has a universal fixed-`r` limit. After stretching the right boundary by

`x_s(r)=1-2e^(-r/s)`, 

the limiting Green operator is

`(TF)(r)=e^(-2r)F(r)+e^(-r) integral_0^r e^(-q)F(q)dq`,

and its nonzero fixed profiles form the one-dimensional cone

`F(r)=C/sqrt(e^(2r)-1)`.

The principal shape is therefore universal. Source information can only enter through the scalar amplitude or lower-order matching data.

PL-311 identifies an exact obstruction to selecting that amplitude by an ordinary perturbation on the same outer scale. If `f` is locally integrable at the stretched endpoint, `(I-T)f=h`, and `h` is continuous at `r=0`, then

`h(0)=0`.

In particular `e^(-r)` is not in the endpoint-integrable range of `I-T`. This matters because a lower-order source with a nonzero fixed-`r` boundary limit contributes precisely an `e^(-r)` forcing after application of `T`. Unless another finite-`s` correction cancels its endpoint value, no regular first-order outer correction can absorb it.

The missing compensation has a canonical geometric location. Every fixed physical point `x in (-1,1)` satisfies

`r_s(x)= -s log((1-x)/2)=O(s)`.

Thus the full macroscopic physical bulk collapses into a shrinking `r=O(s)` corner of the stretched coordinate. The fixed-`r>0` limit forgets exactly the region in which bulk source information remains spatially resolved.

This changes the interpretation of the free amplitude `C`. It is not simply an integration constant waiting to be determined by evaluating the outer equation one order further. Its selection is a **solvability/matching problem between two scales**: the compressed physical bulk at `r=O(s)` and the universal fixed-`r` outer profile. A source-sensitive boundary functional can reach the outer amplitude only through that overlap or through an equivalent endpoint cancellation in the finite-`s` equation.

The next theorem should therefore quantify `T_s-T` uniformly across the corner/outer overlap and derive the resulting compatibility condition for `C`, or recover the same condition from a uniformly convergent weak/virial identity. Ordinary bulk convergence is too coarse, while the limiting outer operator by itself has already forgotten the source coordinate needed to select the amplitude.

**Boundary.** PL-311 gives only a necessary range condition for endpoint-integrable corrections; it does not prove surjectivity when `h(0)=0`, does not identify the actual completed-Weil source limit, and does not exclude a finite-`s` kernel correction that cancels the forbidden endpoint term. More singular corrections may also signal an additional layer. The durable conclusion is narrower: source selection of the universal stretched profile is intrinsically a corner-to-outer matching problem, not a regular fixed-scale perturbation problem.