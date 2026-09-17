# MI-030 — Low-frequency jets are physical moments, but source selectivity begins only after pole subtraction

**Evidence level:** exact/literature-bridged synthesis from [VIS-259](../../findings/VIS-259-cusp-adapted-packet-ladder-is-uniform-approximation-duality.md), [VIS-260](../../findings/VIS-260-rodgers-fixed-margin-error-pays-cusp-packet-conditioning.md), [VIS-261](../../findings/VIS-261-bk-low-frequency-jet-is-physical-moment.md), [VIS-262](../../findings/VIS-262-rodgers-diagonal-kernel-freezes-fixed-order-source-moments.md), [VIS-263](../../findings/VIS-263-subprime-band-weight-has-exact-quadratic-carrier.md), and [VIS-264](../../findings/VIS-264-quadratic-carrier-prime-power-curvature-sampler.md). The pair-correlation theorem and Bogomolny--Keating prediction are inherited from the audited Rodgers source.

Once the sine-kernel cusp and lower even nuisance moments have been cancelled, the remaining low-frequency coefficient has a direct physical-space representation. If `D_T(u)` is the Bogomolny--Keating-minus-matched-GUE kernel and `R_T(alpha)` its Fourier transform, then

`R_T^(2j)(0)=(-1)^j log(T)^(2j) M_(2j)(T)`,

where `M_(2j)(T)=int u^(2j)D_T(u)du`; all odd derivatives vanish. The first surviving low-frequency jet is therefore exactly the first surviving even physical-space moment of the kernel difference.

VIS-259 supplies the sharp observation needed to extract that jet. An order-`2m` cusp-adapted packet with normalized retained moment has total variation `E_m^(-1)b^(-2m)`. VIS-261 shows that pairing it with `R_T` returns the `2m`-th Taylor coefficient plus a controlled higher-order remainder, while VIS-260 supplies the logically independent fixed-margin theorem-transfer error `O(T^(-delta)E_m^(-1)b^(-2m))`.

VIS-262 closes the abstract existence side of the quadratic coefficient. Rodgers' final diagonal comparison freezes each fixed even moment to a functional `C_(2m)(omega)+O(T^(-delta))`, and some admissible weights have `C_2(omega)!=0`. VIS-263 shows why this cannot be promoted directly to arithmetic selectivity: one may choose `omega` with Fourier support strictly below the first nonzero prime frequency and still obtain

`C_2(omega)=1/(2pi^2)`

exactly. That carrier comes entirely from the zero-frequency pole-compensating term.

VIS-264 now gives the exact decomposition that the previous boundary demanded:

`C_2(omega)=hat omega(0)/(2pi^2) - (1/(8pi^4)) sum_p sum_(m>=1) (log p)^2 p^(-m) hat omega''(m log p/(2pi))`.

Because `hat omega` is compactly supported, the prime-power sum is finite. The first term is the universal DC/pole background. The second is the genuinely source-dependent coordinate: a **prime-power curvature sampler**. If the support lies below `log 2/(2pi)`, the sampler vanishes identically and VIS-263 is recovered. If the support crosses prime frequencies, arithmetic access becomes possible but nonzero response is still not automatic: the sampled curvature may vanish or different prime-power terms may cancel.

The corrected reusable lesson is therefore three-layered. **Low-frequency jets are physical moments; a nonzero total carrier need not contain any prime-frequency information; and after explicit pole subtraction the remaining quadratic coordinate is a finite linear functional of prime-power Fourier curvature.** Arithmetic selectivity begins at this residual, not at the existence of the total coefficient.

For the support-edge program the next burden is exact. Freeze a weight faithful to the intended edge observable and show that its prime-power curvature sampler is nonzero at the required normalization while still paying the `b^-2` packet conditioning and theorem-transfer error. That would establish a source-selective fixed-margin quadratic carrier. Moving-edge uniformity and the four-level covariance needed by the original edge--edge statistic remain separate gates.

**Boundary.** VIS-264 does not prove that a support-edge-faithful weight has nonzero prime-power residual, and the residual formula itself is not a zero-selection theorem. It also does not establish moving-edge uniformity or four-level covariance. The gain is sharper: pole/background subtraction is now explicit, so source selectivity of the quadratic carrier can be tested by one concrete finite prime-power curvature functional rather than inferred from nonzero amplitude.