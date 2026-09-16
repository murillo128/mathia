# MI-030 — Low-frequency arithmetic jets are physical moments

**Evidence level:** exact/literature-bridged synthesis from [VIS-259](../../findings/VIS-259-cusp-adapted-packet-ladder-is-uniform-approximation-duality.md), [VIS-260](../../findings/VIS-260-rodgers-fixed-margin-error-pays-cusp-packet-conditioning.md), and [VIS-261](../../findings/VIS-261-bk-low-frequency-jet-is-physical-moment.md). The pair-correlation theorem and Bogomolny--Keating prediction are inherited from the audited sources in VIS-260--VIS-261.

Once the sine-kernel cusp and lower even nuisance moments have been cancelled, the remaining low-frequency arithmetic coefficient has a direct source representation. If `D_T(u)` is the physical-space Bogomolny--Keating-minus-matched-GUE kernel and `R_T(alpha)` its Fourier transform, then

`R_T^(2j)(0)=(-1)^j log(T)^(2j) M_(2j)(T)`,

where `M_(2j)(T)=int u^(2j)D_T(u)du`; all odd derivatives vanish. The first surviving arithmetic jet is therefore exactly the first nonzero even physical-space moment of the kernel difference.

VIS-259 supplies the sharp observation needed to extract that jet. An order-`2m` cusp-adapted packet with normalized retained moment has total variation `E_m^(-1)b^(-2m)`. VIS-261 shows that pairing it with `R_T` returns the `2m`-th Taylor coefficient plus a remainder bounded by

`E_m^(-1)b^2 sup_(|alpha|<=b)|R_T^(2m+2)(alpha)|/(2m+2)!`.

VIS-260 supplies a second, logically independent error: transferring the actual zeta statistic to the arithmetic prediction costs `O(T^(-delta)E_m^(-1)b^(-2m))` in Rodgers' fixed-margin regime.

A candidate carrier must therefore beat **two different conditioning bills**. The source moment must be large enough that the packet resolves its Taylor jet, and the rigorous theorem must approximate the pair statistic accurately enough after multiplication by the packet norm. Neither a formal nonzero derivative nor a decaying scalar theorem error is sufficient by itself.

The most economical next test is the quadratic moment `M_2(T)` for one frozen even weight. Only if it vanishes or fails the two quantitative gates for a derived reason should the quartic moment be considered. Higher packet order is not a free search dimension because every step pays both `b^(-2m)` theorem amplification and a separate Taylor-resolution requirement.

**Boundary.** This synthesis is fixed-margin and two-level. It does not prove any `M_(2j)(T)` is nonzero or large, does not provide moving-edge uniformity, and does not supply the four-level covariance needed by the original edge--edge statistic. Fourier moment identities are standard; the substantive content is the exact source/packet/theorem accounting in the persisted normalization.