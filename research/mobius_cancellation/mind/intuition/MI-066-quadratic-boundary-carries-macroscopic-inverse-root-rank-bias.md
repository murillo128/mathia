# MI-066 — Quadratic conductor carries a macroscopic inverse-root-rank bias population

**Evidence level:** exact synthesis from [MC-375](../../findings/MC-375-quartic-saturation-delocalizes-source-incidence-across-most-modes.md) and [MC-376](../../findings/MC-376-quadratic-boundary-carries-macroscopic-inverse-root-rank-bias.md). The moment/Paley--Zygmund step is elementary; the Mathia content is its coupling to the previously established primitive-conductor saturation.

The near-quadratic primitive-conductor obstruction is not supported only by modes whose endpoint coefficients vanish too quickly to matter. For the endpoint coefficient

`x_I=(-1)^|I|(1-2d(I))`,

MC-376 gives exact cube moments `E|x|^2=S_2` and `E|x|^4=3S_2^2-2S_4<=3S_2^2`. Paley--Zygmund therefore forces at least `1/12` of all modes to satisfy

`|x_I| >= sqrt(S_2/2) >= 1/sqrt(2R)`.

MC-375 independently shows that, in the quartic-saturated regime, all but a vanishing proportion of the Fourier cube have minimum primitive conductor `y^(2+o(1))`. The two statements overlap: asymptotically a positive fraction of the full cube is simultaneously near-quadratic in primitive conductor and at least inverse-root-rank in endpoint bias.

This changes the target theorem. It is no longer enough to show that cheap primitive representatives are rare, or to control one exceptional expensive mode. A successful reverse-discrimination mechanism must either suppress/control a **macroscopic population** of near-quadratic-conductor modes at a bias scale `R^(-1/2)`, or avoid an architecture that requires resolving those modes individually.

The amplitude scale is also stronger than a fixed-positive-threshold statement. In the natural source budget `R=O(log y)`, the forced bias is still only slowly decaying, of order at least `(log y)^(-1/2)` up to constants. Treating the quadratic boundary as negligible therefore requires an actual cancellation theorem at this moving amplitude, not qualitative smallness.

**Boundary.** The result is tied to the endpoint coefficient law and the quartic-saturated source-incidence regime established in the preceding findings. It does not prove cancellation for Möbius sums, identify an optimal source theorem at quadratic conductor, or show that every destination must resolve these modes separately. It fixes the size and population of the obstruction that such a destination would face.
