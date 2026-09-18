# MI-036 — A uniform theorem exponent can disappear after specializing to the physical source regime

**Evidence level:** literature+derived synthesis from [VIS-272](../../findings/VIS-272-wang-green-potential-dictionary.md), [VIS-274](../../findings/VIS-274-wang-fixed-source-leading-profile.md), [VIS-278](../../findings/VIS-278-wang-gamma-normalized-source-energy.md), [VIS-279](../../findings/VIS-279-wang-fixed-source-removes-l32-floor.md), [VIS-280](../../findings/VIS-280-wang-db-cross-power-small.md), and [VIS-281](../../findings/VIS-281-wang-fixed-source-localization-power-small.md). Wang's mean-square, cross-term and localization estimates are prior art; the Mathia content is the fixed-source rescaling audit and its consequence for the apparent theorem frontier.

The Wang channel is consumed by a fixed physical source packet `x=e^(2 pi q)` with `q` in a compact set while `L=log T` grows. A theorem stated uniformly for a much larger moving range of `x` can therefore carry an error exponent that is not intrinsic to this destination regime.

VIS-279 makes this explicit for the `D_x`--`E_x` cross term. Wang's exact mean-square identity gives, for fixed `x`,

`int |D_x(t)|^2 dt = H log x + O(H + x log^2(...))`,

so on a compact fixed-source window `||D_x||_2=O(sqrt H)` rather than the `O(sqrt(HL))` scale obtained by inserting a worst-case growing-`x` bound. Together with `||E_x||_2=O(sqrt H/x)`, the cross term is only `O(H/x)`. After the fixed-source `dq/L` pullback and the theorem normalization `1/(HL)`, its contribution is `O(L^-2)`.

VIS-280 removes the other direct prime/source cross as a candidate source of `L^-3/2`. Wang's explicit bound

`|int D_x(t) overline(B_x(t)) dt| << L/sqrt(x)`

is `O_K(L)` on a compact fixed-source packet. After the same `dq/L` pullback and `1/(HL)` normalization, the full `D_x`--`B_x` packet is `O_K(1/(HL))`, hence smaller than every fixed negative power of `L` when `H=T^theta` with fixed `theta>0`.

VIS-281 shows that the same principle applies one level higher in the proof architecture. Wang's zero-window localization step replaces the interval-restricted field by the full explicit-formula field with error `O(x L^3)`. For compact fixed `q`, `x` is bounded, so this is only `O_K(L^3)` before the physical pullback. The extra `dq/L` factor and `1/(HL)` normalization reduce the entire localization loss to

`O_K(L/H)`.

Since `H=T^theta`, this is smaller than every fixed inverse power of `L`. Thus a theorem-level error that is material over the full moving range `x<=T^lambda` can become invisible to **every logarithmic frontier** after specialization to the destination's fixed physical source coordinate.

Together with VIS-278, the current audit excludes all obvious source/direct-cross and localization sectors as compulsory `L^-3/2` mechanisms: the gamma-normalized pure source energy is `L^-2`, the `D_x`--`E_x` cross is at most `L^-2`, the `D_x`--`B_x` cross is power-small, and the `A_I -> A` localization loss is power-small. The previously visible `L^-3/2` scale is therefore not forced by any of these sectors.

The reusable lesson is stronger than “use a sharper estimate.” **Before assigning mathematical meaning to a limiting exponent, re-specialize every theorem input and every proof-loss term to the physical source scaling actually used by the destination, and decompose the remainder until an exact sector genuinely realizes that exponent.** A bound optimized for a larger parameter range may create an apparent frontier that vanishes when the source window is fixed. Packet cancellation should target an exact signed term at the destination scale, not a slack envelope or localization loss inherited from unused uniformity.

This also changes the search order. The next task is not to engineer cancellation inside the direct prime/source cross or the zero-window localization step. It is to inspect the remaining truncation/replacement sectors at fixed physical `q` and identify the actual largest surviving term. If some exact sector really remains at `L^-3/2`, preserve its sign/covariance and test cancellation there. If every compact-source sector falls to `L^-2` or below, the advance is a sharper fixed-source transfer theorem rather than another cancellation packet.

**Boundary.** VIS-281 does not prove that the complete fixed-source theorem has remainder `O(L^-2)`, identify every remaining proof-loss sector, improve Wang's uniform theorem globally in `x`, or imply RH. It closes the zero-window localization boundary in addition to the direct cross terms. A genuine `L^-3/2` contribution may still occur elsewhere and must be exhibited explicitly before it is treated as the destination bottleneck.
