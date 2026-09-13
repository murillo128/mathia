# MI-012 — Averaging local-factor mass removes the pointwise log-log loss but leaves the dimension-four dephasing scale

**Evidence level:** exact as a refinement of the VIS-197--VIS-200 proof architecture through VIS-201, using the cited Henriot/Nair--Tenenbaum discriminant-uniform polynomial average. It is a sufficient dephasing bound, not a lower bound on the true horizon or collision energy.

VIS-200 showed that scalar cutoff tuning cannot beat the four-form pointwise threshold. Splitting at `X=(y/H)L` leaves a pointwise singular-series factor `B(y)=(1+log log(3+y))^4` in the sieve term, while taper decay forces `L` large enough that optimizing the cutoff changes only lower-order logarithms.

VIS-201 attacks the ingredient that VIS-200 identified rather than retuning the split. On each nondegenerate top-scale four-prime fiber, the local conductor reduces to three primitive affine polynomial values. Henriot's discriminant-uniform Nair--Tenenbaum bound, with the corrected non-monic discriminant factor, gives an arithmetic majorant `G_A(d_0)` whose first mean is bounded: `sum_(n<=D) G_A(n) <<_A D`.

Averaging the local factors over the second-gap fiber **before** the first-gap sum therefore removes the pointwise `B(y)` loss. With the generalized cutoff the normalized collision energy becomes

`O((log y)^2/log(H/L)^4 + (log y)^2/L^3 + H/(y log y))`.

Taking `L=log y` reduces the sufficient horizon condition to `sqrt(log y)=o(log H)` together with `H log y/y -> 0`. The earlier extra `log log y` multiplier was thus an artifact of pointwise local-factor maximization, not of the dephasing resource itself.

The remaining barrier is more structural. The present argument still uses a dimension-four upper-bound sieve and the weighted local-spacing resource `D_v`, so it does not reach the critical scale `log H=Theta(sqrt(log y))`, polylogarithmic horizons, or arbitrarily slow horizons. Further progress must improve joint fiber incidence/cancellation, strengthen the fourth-prime use, or replace `D_v`; scalar cutoff tuning and pointwise singular-series bounds are no longer the live bottlenecks.

**Boundary.** The averaging theorem is used only for fixed crowding multiplier `A` and nondegenerate four-form fibers. The conductor-zero three-prime branch remains separate. VIS-201 proves sufficiency for the existing dephasing architecture, not necessity or sharpness of its remaining `sqrt(log y)` scale.