# MI-036 — A uniform theorem exponent can disappear after specializing to the physical source regime

**Evidence level:** literature+derived synthesis from [VIS-272](../../findings/VIS-272-wang-green-potential-dictionary.md), [VIS-274](../../findings/VIS-274-wang-fixed-source-leading-profile.md), and [VIS-278](../../findings/VIS-278-wang-gamma-normalized-source-energy.md) through [VIS-282](../../findings/VIS-282-wang-fixed-source-dirichlet-profile.md). Wang's mean-square, cross-term and localization estimates are prior art; the Mathia content is the fixed-source rescaling audit and the exact coefficient-scale source profile exposed by specializing before discarding structure.

The Wang channel is consumed by a fixed physical source packet `x=e^(2 pi q)` with `q` in a compact set while `L=log T` grows. A theorem stated uniformly for a much larger moving range of `x` can therefore carry an error exponent that is not intrinsic to this destination regime.

VIS-279 makes this explicit for the `D_x--E_x` cross term. Wang's exact mean-square identity gives `||D_x||_2=O_K(sqrt H)` on a compact fixed-source window, not the `O(sqrt(HL))` scale obtained from a worst-case growing-`x` estimate. Together with `||E_x||_2=O_K(sqrt H)`, the cross contributes only `O(L^-2)` after the fixed-source pullback.

VIS-280 removes the direct `D_x--B_x` cross as a logarithmic bottleneck: Wang's explicit estimate becomes `O_K(1/(HL))` after packet normalization and is power-small because `H=T^theta`. VIS-281 does the same one level higher for the zero-window replacement `A_I -> A`; its theorem-uniform `O(xL^3)` loss becomes `O_K(L/H)` on the actual compact source packet, below every fixed inverse power of `L`.

VIS-282 sharpens the remaining `D_x` mean square instead of treating its fixed-source `O(H)` term as anonymous uncertainty. With Wang's coefficients

`a_n(x)=Lambda(n)/sqrt(n) min(n/x,x/n)`, 

the exact diagonal energy is

`S_D(x)=x^(-2) sum_(n<=x) n Lambda(n)^2 + x^2 sum_(n>x) Lambda(n)^2/n^3`,

and fixed-source Montgomery--Vaughan gives

`int_I |D_x(t)|^2 dt = H S_D(x) + O_K(1)`.

Writing `C_D(x)=S_D(x)-log x`, the whole `H C_D(x)` term survives at the same `L^-2` packet scale as `H log x`; the genuine mean-value remainder is power-small after normalization. Moreover `C_D` is continuous and piecewise smooth with derivative jumps

`C_D'(m+)-C_D'(m-)=-4 Lambda(m)^2/m^2`

at every prime power `m`. Thus the coarse replacement `S_D=log x+O(1)` was hiding a deterministic prime-power profile precisely at the coefficient scale one would want to resolve.

This changes the fixed-source audit in an important way. The apparent `L^-3/2` frontier has not been realized by the direct source cross terms or localization loss, while one exact `L^-2` sector is now known in considerably more detail: it carries source arithmetic rather than featureless theorem error. The next coherent calculation is therefore to recombine the exact `D_x` profile with the `B_x+E_x` sector and the remaining signed cross/replacement terms at `L^-2`, and determine whether that prime-power profile survives, combines with another exact contribution, or cancels.

The reusable lesson is stronger than “use a sharper estimate.” **Specialize to the physical source scale before converting structured terms into uniform errors.** A theorem-uniform exponent may vanish entirely, while an apparently harmless `O(H)` may contain the whole destination-scale arithmetic coefficient. One must preserve exact diagonal/source structure through the pullback before deciding which sector deserves cancellation engineering.

**Boundary.** VIS-282 does not prove that the complete fixed-source pair statistic has remainder `O(L^-2)`, that the prime-power kinks survive the final recombination, or that no different sector produces a genuine `L^-3/2` term. It identifies the exact `D_x` contribution and removes its averaging remainder as an uncertainty. Any larger surviving logarithmic frontier still has to be exhibited in a specific signed sector rather than inferred from a theorem-uniform envelope.