# MI-025 — Source amplitude controls first-prime reflection at the sharp square-root-log scale

**Evidence level:** exact/source-selected synthesis from [PL-326](../../findings/PL-326-fixed-aperture-endpoint-laws-do-not-orient-the-first-prime-crossing.md), [PL-327](../../findings/PL-327-critical-half-log-boundary-regularity-does-not-orient-first-prime-reflection.md), and [PL-329](../../findings/PL-329-first-prime-reflection-sharp-source-amplitude-threshold.md).

The first-prime activation isolates a shrinking reflected correlation

`H_delta(g)=int_0^(2delta) g(t)g(2delta-t) dt`

whose positive critical profile is only of size `delta/L_delta`, with `L_delta=log(a_delta/delta) -> infinity`. PL-326--PL-327 show that fixed-aperture endpoint asymptotics and the canonical half-log regularity scale do not determine its sign: an antisymmetric residual of state amplitude `L_delta^(-1/2)` on the moving layer can reverse the reflection while remaining small in the natural endpoint norms.

PL-329 shows that the **exact source equation** sees that residual at a reciprocal scale. For a family satisfying the critical envelope, let

`S_delta = sup_Q |F_delta(Q)|`

be the amplitude of the exact endpoint source. Integrating the source equation first selects a coefficient `C_delta` from the family itself. After subtracting `C_delta Q^(-1/2)`, the positive comparison argument yields

`|g_delta(Q)-C_delta Q^(-1/2)| <= K(1+S_delta)/Q + K exp(-eta(Q-R))`

on a fixed tail, uniformly in `delta` apart from the displayed source amplitude.

On the newly active physical layer, where `Q>=L_delta`, this becomes

`||r_delta||_(L^2(0,2delta)) << sqrt(delta) ((1+S_delta)/L_delta + exp(-eta L_delta))`.

The critical profile itself has norm `asymp |C_delta| sqrt(delta/L_delta)`. Therefore the reflected correlation keeps its positive leading sign whenever

`(1+S_delta)/(|C_delta| sqrt(L_delta)) -> 0`.

This is exactly the moving-layer scale that the generic argument was missing. The condition does not demand a supercritical Hölder exponent; it asks instead that the **source forcing** be small enough relative to the selected critical coefficient.

The threshold is sharp within the PL-327 counterfamily. Its sign-reversing residual has endpoint-state amplitude `L_delta^(-1/2)` on a fixed-width layer in `Q-L_delta`. The coercive term `2Qm` multiplies that state by `Q~L_delta`, producing a source perturbation of size `sqrt(L_delta)`. All other source terms are lower order there. Thus the known sign-reverser necessarily pays

`S_delta asymp sqrt(L_delta)`

when `C_delta` stays nonzero. Sub-square-root-log forcing excludes it; square-root-log forcing can sustain it.

This gives a useful source/destination transducer: the shrinking reflected sign is too fine for the natural endpoint state norm, but the exact logarithmic-Laplacian source equation magnifies precisely the dangerous antisymmetric layer. A source bound can therefore orient a destination quantity that generic regularity leaves undecided.

The remaining question is no longer “which regularity assumption would suffice?” It is whether the **actual completed-Weil eigenbranch/source family** obeys the source-amplitude gate uniformly through the first-prime activation, including control preventing `C_delta` from collapsing. Proving that would make first-crossing orientation source-selected rather than imposed.

**Boundary.** PL-329 is a sufficient criterion for the first-prime reflection and a sharp calibration against the known critical counterfamily. It is not yet proved for the actual eigenbranch, does not orient later prime-power channels, and does not imply global Weil positivity or RH. The square-root-log threshold is relative to `|C_delta|`; if the leading coefficient degenerates, the criterion must be re-evaluated.
