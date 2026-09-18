# MI-036 — Fixed-source specialization reveals a diagonal `L^-2` arithmetic profile and removes spurious larger exponents

**Evidence level:** literature+derived synthesis from [VIS-272](../../findings/VIS-272-wang-green-potential-dictionary.md), [VIS-274](../../findings/VIS-274-wang-fixed-source-leading-profile.md), and [VIS-278](../../findings/VIS-278-wang-gamma-normalized-source-energy.md) through [VIS-283](../../findings/VIS-283-wang-fixed-source-cross-frequency-separation.md). Wang's decomposition, mean-square and localization estimates are prior art; the Mathia content is the fixed-source rescaling audit, exact coefficient-scale source profile and signed frequency-separation recombination.

The Wang channel is consumed by a compact physical source window `x=e^(2 pi q)` while `L=log T` grows. A theorem uniform in a much larger moving range of `x` can therefore carry an error exponent that is not intrinsic to the destination regime. VIS-279--VIS-281 show this directly: the apparent direct-cross and localization losses drop to `L^-2` or become power-small after specializing before rescaling.

VIS-282 sharpens the fixed-source Dirichlet sector instead of treating its `O(H)` contribution as anonymous uncertainty. With

`a_n(x)=Lambda(n)/sqrt(n) min(n/x,x/n)`, 

the exact diagonal energy is

`S_D(x)=x^(-2) sum_(n<=x) n Lambda(n)^2 + x^2 sum_(n>x) Lambda(n)^2/n^3`,

and

`int_I |D_x(t)|^2 dt = H S_D(x)+O_K(1)`.

The profile is continuous and piecewise smooth with derivative jumps `-4 Lambda(m)^2/m^2` at prime powers. Thus a coarse `O(H)` estimate was hiding arithmetic structure precisely at the `L^-2` coefficient scale.

VIS-283 resolves the recombination that was previously open. The combined source has

`x(B_x+E_x)=log(t/(2*pi))+zeta'/zeta(3/2-it)+O_K(t^-1)`.

After conjugation, the absolutely convergent zeta residual and `D_x` carry the same negative temporal-frequency orientation, so their product contains frequencies `-log(mn)` and no zero-frequency diagonal. This gives

`int_I D_x overline(E_x) dt = O_K(1)`

and

`int_I D_x overline(B_x+E_x) dt = O_K(L)`,

where the larger term comes only from the slowly varying classical gamma baseline. After the fixed-source pullback the complete signed prime/source cross is `O_K(1/(HL))`, below every fixed inverse power of `L`.

The field energy therefore separates through constant order:

`(1/H) int_I |A(x,t)|^2 dt = S_D(x)+x^(-2)[log(T/(2*pi))^2+C_Lambda]+o_K(1)`.

If the exact gamma baseline is retained, the normalization-invariant coefficient-scale arithmetic remainder is

`Q_gamma(x)=S_D(x)+C_Lambda/x^2`.

This is a positive diagonal sum before packet projection. The prime-power kinks in `S_D` are not erased by an equal-scale source cross because no such resonant cross exists in the fixed-source representation.

The reusable lesson is stronger than “use a sharper estimate.” **Specialize to the physical source scale before converting structured terms into uniform errors, and audit frequency orientation before expecting signed cancellation between surviving sectors.** A theorem-uniform exponent can disappear entirely, while an apparently harmless mean-square term can contain the whole destination-scale arithmetic coefficient.

The next unresolved step is downstream of the field-level recombination: determine whether the admissible packet/test projection preserves a nontrivial component of `Q_gamma(e^(2 pi q))`, projects it away, or exposes another exact transform; in parallel, audit any remaining truncation/replacement term that could genuinely exceed `L^-2`.

**Boundary.** VIS-283 is restricted to fixed compact source and does not prove a complete pair-correlation remainder theorem of order `L^-2`. It proves that the direct source recombination cannot supply a larger logarithmic frontier and that the coefficient-scale field profile is diagonal before packet projection. Growing-source regimes require a new uniformity audit.