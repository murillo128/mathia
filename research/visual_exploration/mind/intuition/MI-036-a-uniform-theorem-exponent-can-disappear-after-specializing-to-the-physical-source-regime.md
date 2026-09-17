# MI-036 — A uniform theorem exponent can disappear after specializing to the physical source regime

**Evidence level:** literature+derived synthesis from [VIS-272](../../findings/VIS-272-wang-green-potential-dictionary.md), [VIS-274](../../findings/VIS-274-wang-fixed-source-leading-profile.md), [VIS-278](../../findings/VIS-278-wang-gamma-normalized-source-energy.md), and [VIS-279](../../findings/VIS-279-wang-fixed-source-removes-l32-floor.md). Wang's mean-square estimate is prior art; the Mathia content is the fixed-source rescaling audit and its consequence for the apparent theorem frontier.

The Wang channel is consumed by a fixed physical source packet `x=e^(2 pi q)` with `q` in a compact set while `L=log T` grows. A theorem stated uniformly for a much larger moving range of `x` can therefore carry an error exponent that is not intrinsic to this destination regime.

VIS-279 makes this explicit for the first non-source cross term. Wang's exact mean-square identity gives, for fixed `x`,

`int |D_x(t)|^2 dt = H log x + O(H + x log^2(...))`,

so on a compact fixed-source window `||D_x||_2=O(sqrt H)` rather than the `O(sqrt(HL))` scale obtained by inserting a worst-case growing-`x` bound. Together with `||E_x||_2=O(sqrt H/x)`, the `D_x`--`E_x` cross term is only `O(H/x)`. After the fixed-source `dq/L` pullback and the theorem normalization `1/(HL)`, its contribution is `O(L^-2)`.

Thus the previously visible `L^-3/2` scale is not forced by this cross interaction. It came from retaining a uniform-in-growing-source estimate after the destination had already specialized to fixed physical `q`. VIS-278 had separately shown that the gamma-normalized pure source energy is also `L^-2`. Two natural candidate sectors therefore fail to produce an intrinsic fixed-source `L^-3/2` obstruction.

The reusable lesson is stronger than “use a sharper estimate.” **Before assigning mathematical meaning to a limiting exponent, re-specialize every theorem input to the physical source scaling actually used by the destination.** A bound optimized for a larger parameter range may create an apparent frontier that vanishes when the source window is fixed. Packet cancellation should target an exact signed term at the destination scale, not a slack exponent inherited from an unused uniformity regime.

This also changes the search order. One should first decompose the full fixed-source theorem and determine whether any sector genuinely survives at `L^-3/2`. Only if such a term exists should its sign/covariance be engineered. If every exact compact-source sector is `O(L^-2)` or smaller, the right advance is a sharper fixed-source transfer theorem rather than another cancellation packet.

**Boundary.** VIS-279 does not prove that the full fixed-source remainder is `O(L^-2)`, identify every interaction sector, or improve Wang's theorem globally in `x`. It closes only the `D_x`--`E_x` candidate and shows that the old `L^-3/2` attribution was not justified in the fixed-source regime. A genuine `L^-3/2` contribution may still occur elsewhere and must be exhibited explicitly before it is treated as the destination bottleneck.
