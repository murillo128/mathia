# MI-030 — Low-frequency jets are physical moments, but a nonzero quadratic carrier need not be prime-selective

**Evidence level:** exact/literature-bridged synthesis from [VIS-259](../../findings/VIS-259-cusp-adapted-packet-ladder-is-uniform-approximation-duality.md), [VIS-260](../../findings/VIS-260-rodgers-fixed-margin-error-pays-cusp-packet-conditioning.md), [VIS-261](../../findings/VIS-261-bk-low-frequency-jet-is-physical-moment.md), [VIS-262](../../findings/VIS-262-rodgers-diagonal-kernel-freezes-fixed-order-source-moments.md), and [VIS-263](../../findings/VIS-263-subprime-band-weight-has-exact-quadratic-carrier.md). The pair-correlation theorem and Bogomolny--Keating prediction are inherited from the audited Rodgers source.

Once the sine-kernel cusp and lower even nuisance moments have been cancelled, the remaining low-frequency coefficient has a direct physical-space representation. If `D_T(u)` is the Bogomolny--Keating-minus-matched-GUE kernel and `R_T(alpha)` its Fourier transform, then

`R_T^(2j)(0)=(-1)^j log(T)^(2j) M_(2j)(T)`,

where `M_(2j)(T)=int u^(2j)D_T(u)du`; all odd derivatives vanish. The first surviving low-frequency jet is therefore exactly the first surviving even physical-space moment of the kernel difference.

VIS-259 supplies the sharp observation needed to extract that jet. An order-`2m` cusp-adapted packet with normalized retained moment has total variation `E_m^(-1)b^(-2m)`. VIS-261 shows that pairing it with `R_T` returns the `2m`-th Taylor coefficient plus a remainder bounded by `E_m^(-1)b^2 sup|R_T^(2m+2)|/(2m+2)!`. VIS-260 supplies the logically independent theorem-transfer error `O(T^(-delta)E_m^(-1)b^(-2m))` in Rodgers' fixed-margin regime.

VIS-262 closes the abstract **existence** side of the quadratic coefficient. Rodgers' final diagonal comparison writes `tilde Q_t-K_t=F(u)` with `F` independent of `t`, so for each fixed even order

`M_(2m)(T)=C_(2m)(omega)+O(T^(-delta))`,

with `C_(2m)(omega)=int u^(2m)omega(u)F(u)du`. Some fixed admissible real even band-limited weights therefore have `C_2(omega)!=0`.

VIS-263 shows why that statement cannot be promoted to arithmetic selectivity. Choose a normalized admissible weight `omega_*` whose Fourier support lies strictly below the first nonzero prime frequency. Then every nonconstant Dirichlet frequency coming from `zeta'/zeta` and the arithmetic correction `B` vanishes in the pairing, yet

`C_2(omega_*)=1/(2 pi^2)`

exactly. The coefficient is supplied entirely by the zero-frequency pole-compensating term. The sharp quadratic packet consequently has a certified fixed-margin main difference

`-(1/(4 pi^2))(log T)^2+o((log T)^2)`

even though the chosen weight resolves no nonzero prime frequency at all.

The corrected reusable lesson is two-layered. **Low-frequency jets really are physical moments, and the fixed-margin quadratic coefficient can be calibrated exactly; but nonzero amplitude does not certify source-selective arithmetic content.** Before calling a retained jet arithmetic, separate the zero-frequency/pole background from the nonconstant prime-frequency contribution and compare against a matched weight or control that cannot see those frequencies.

For the support-edge program this changes the next burden. The question is no longer to find merely one explicit admissible weight with `C_2!=0`; VIS-263 has done that in the strongest possible nonselective way. One must freeze a weight faithful to the intended support-edge observable and prove that its coefficient contains a nonzero residual beyond the explicitly calibrated pole contribution, while still paying the `b^-2` conditioning and fixed-margin theorem error. The accepted support-edge arithmetic-residual clue is the appropriate research handoff for that unresolved step.

**Boundary.** VIS-263 is a fixed-margin smooth-test calibration. It does not show that every quadratic coefficient is pure pole background, nor that a support-edge-faithful weight has zero prime-frequency residual. It also does not establish moving-edge uniformity or the four-level covariance needed by the original edge--edge statistic. The new conclusion is narrower: existence or even exact evaluation of a nonzero quadratic carrier is insufficient evidence of arithmetic selectivity unless the universal zero-frequency contribution has first been removed.