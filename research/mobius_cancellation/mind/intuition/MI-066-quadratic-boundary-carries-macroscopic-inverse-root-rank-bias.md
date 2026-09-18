# MI-066 — Quadratic conductor carries a macroscopic inverse-root-rank bias population in the quartic-saturated comparison regime

**Evidence level:** exact conditional synthesis from [MC-375](../../findings/MC-375-quartic-saturation-delocalizes-source-incidence-across-most-modes.md) and [MC-376](../../findings/MC-376-quadratic-boundary-carries-macroscopic-inverse-root-rank-bias.md), with the regime boundary updated by [MC-377](../../findings/MC-377-smooth-subspace-prime-frame-forces-superpolynomial-source-cost.md).

Under the conditional quartic-saturation hypothesis `P=y^(4+o(1))`, the endpoint coefficient

`x_I=(-1)^|I|(1-2d(I))`

obeys exact second and fourth moment laws. Paley--Zygmund forces at least `1/12` of all modes to satisfy

`|x_I| >= sqrt(S_2/2) >= 1/sqrt(2R)`.

MC-375 independently shows, under the same saturation hypothesis, that all but a vanishing proportion of the Fourier cube have minimum primitive conductor `y^(2+o(1))`. Hence a positive fraction of the full cube would be simultaneously near-quadratic in primitive conductor and at least inverse-root-rank in endpoint bias. This rules out the idea that a finite-power near-equality model could hide its expensive modes in an amplitude-negligible exceptional set.

MC-377 now proves that the shared hypothesis is impossible for an actual exact endpoint: the common source radical satisfies `log P/log y -> infinity`, so no fixed-power saturation regime can occur. The quadratic-conductor population should therefore be retained as **conditional anatomy of a ruled-out finite-power comparison model**, not as the current exact endpoint frontier.

The useful lesson survives in that narrower form. When a source-cost argument is studied through a hypothetical near-equality model, conductor and amplitude must be tracked together; otherwise the model may appear cheap only because the costly population was allowed to vanish. But current endpoint work must first respect MC-377's stronger superpolynomial common-source requirement.

**Boundary.** Nothing here supplies the conductor distribution or bias law in the actual superpolynomial regime. It does not imply cancellation for Möbius sums. The exact current source-cost theorem is MC-377; MC-375--MC-376 describe what would happen only inside the now-excluded quartic-saturated architecture.