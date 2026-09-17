# MI-030 — Low-frequency arithmetic jets are physical moments, and the quadratic fixed-margin carrier can be nonzero

**Evidence level:** exact/literature-bridged synthesis from [VIS-259](../../findings/VIS-259-cusp-adapted-packet-ladder-is-uniform-approximation-duality.md), [VIS-260](../../findings/VIS-260-rodgers-fixed-margin-error-pays-cusp-packet-conditioning.md), [VIS-261](../../findings/VIS-261-bk-low-frequency-jet-is-physical-moment.md), and [VIS-262](../../findings/VIS-262-rodgers-diagonal-kernel-freezes-fixed-order-source-moments.md). The pair-correlation theorem and Bogomolny--Keating prediction are inherited from the audited Rodgers source.

Once the sine-kernel cusp and lower even nuisance moments have been cancelled, the remaining low-frequency arithmetic coefficient has a direct source representation. If `D_T(u)` is the physical-space Bogomolny--Keating-minus-matched-GUE kernel and `R_T(alpha)` its Fourier transform, then

`R_T^(2j)(0)=(-1)^j log(T)^(2j) M_(2j)(T)`,

where `M_(2j)(T)=int u^(2j)D_T(u)du`; all odd derivatives vanish. The first surviving arithmetic jet is therefore exactly the first nonzero even physical-space moment of the kernel difference.

VIS-259 supplies the sharp observation needed to extract that jet. An order-`2m` cusp-adapted packet with normalized retained moment has total variation `E_m^(-1)b^(-2m)`. VIS-261 shows that pairing it with `R_T` returns the `2m`-th Taylor coefficient plus a remainder bounded by `E_m^(-1)b^2 sup|R_T^(2m+2)|/(2m+2)!`. VIS-260 supplies the logically independent theorem-transfer error `O(T^(-delta)E_m^(-1)b^(-2m))` in Rodgers' fixed-margin regime.

VIS-262 closes the previously open **existence** side of the quadratic source gate. Rodgers' final diagonal comparison writes `tilde Q_t-K_t=F(u)` with `F` independent of `t`, and the admissible smooth band-limited test class is stable under multiplication by any fixed even polynomial. Hence, for every fixed `m`,

`M_(2m)(T)=C_(2m)(omega)+O(T^(-delta))`,

with `C_(2m)(omega)=int u^(2m)omega(u)F(u)du`. Since Rodgers' `F` is not identically zero, one can choose a fixed real even admissible weight, independently of confirmation-zero data, for which `C_2(omega)!=0`.

For such a fixed weight, the sharp quadratic packet therefore produces the nonzero main term `-(C_2(omega)/2)(log T)^2`. Its Taylor error is `O(b^2(log T)^4)`, while the RH-conditional zeta-to-prediction transfer costs `O(T^(-delta)b^(-2))`. With `b=T^(-beta)` and `0<2beta<delta<epsilon/2`, both are `o((log T)^2)`.

The fixed-margin lesson is now stronger than a formal moment dictionary: **the admissible test class actually contains a rigorously calibrated nonzero quadratic arithmetic carrier**. Higher packet order should not be explored merely because it exists. The next burden is to freeze one explicit application weight, evaluate its concrete `C_2`, and prove that the same weight corresponds to the intended support-edge observable rather than to an abstract member of Rodgers' test class.

**Boundary.** The result is fixed-margin, two-level, and RH-conditional only at the final transfer from the Bogomolny--Keating prediction to actual zeta pair statistics. It does not establish moving-edge uniformity, a changing-weight theorem, or the four-level covariance needed by the original edge--edge statistic. Existence of some admissible weight with `C_2!=0` does not imply that any previously chosen application weight has nonzero quadratic carrier.