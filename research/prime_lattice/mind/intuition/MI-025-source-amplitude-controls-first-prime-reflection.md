# MI-025 — Source amplitude, not spectral continuity, controls first-prime reflection at the sharp square-root-log scale

**Evidence level:** exact/source-selected synthesis from [PL-326](../../findings/PL-326-fixed-aperture-endpoint-laws-do-not-orient-the-first-prime-crossing.md), [PL-327](../../findings/PL-327-critical-half-log-boundary-regularity-does-not-orient-first-prime-reflection.md), [PL-329](../../findings/PL-329-first-prime-reflection-sharp-source-amplitude-threshold.md), and [PL-330](../../findings/PL-330-first-prime-norm-resolvent-graph-topology.md).

The first-prime activation isolates a shrinking reflected correlation

`H_delta(g)=int_0^(2delta) g(t)g(2delta-t) dt`

whose positive critical profile is only of size `delta/L_delta`, with `L_delta=log(a_delta/delta) -> infinity`. PL-326--PL-327 show that fixed-aperture endpoint asymptotics and the canonical half-log regularity scale do not determine its sign: an antisymmetric residual of state amplitude `L_delta^(-1/2)` on the moving layer can reverse the reflection while remaining small in the natural endpoint norms.

PL-329 shows that the **exact source equation** sees that residual at a reciprocal scale. If `S_delta=sup_Q |F_delta(Q)|` is the exact endpoint-source amplitude, integrating the source equation selects `C_delta` and yields

`|g_delta(Q)-C_delta Q^(-1/2)| <= K(1+S_delta)/Q + K exp(-eta(Q-R))`.

On the newly active layer this gives

`||r_delta||_(L^2(0,2delta)) << sqrt(delta) ((1+S_delta)/L_delta + exp(-eta L_delta))`,

while the critical profile has norm `asymp |C_delta| sqrt(delta/L_delta)`. Hence the reflected correlation keeps its positive leading sign whenever

`(1+S_delta)/(|C_delta| sqrt(L_delta)) -> 0`.

The threshold is sharp within the PL-327 counterfamily. Its sign-reversing residual has state amplitude `L_delta^(-1/2)` on a fixed-width layer in `Q-L_delta`; the coercive `2Qm` term magnifies it into source amplitude `S_delta asymp sqrt(L_delta)` when `C_delta` stays nonzero.

PL-330 shows that this source-amplitude gate cannot be replaced by ordinary spectral continuity. The raw first-prime edge flip has operator norm one at every positive overlap but converges strongly to zero as the overlap closes. Compact resolvent of the threshold localized-Weil operator converts that strong convergence into **norm-resolvent continuity of the full family**, with norm-continuous isolated spectral projections and graph-continuous simple eigenbranches across the activation.

That is still not enough. The PL-327 hostile perturbation can be chosen so that both `||r_delta||_2` and `||T r_delta||_2` tend to zero for the fixed logarithmic principal operator `T`, while its reflected contribution remains large enough relative to the much smaller `delta/L_delta` sign reserve to reverse the crossing. Graph-smallness is therefore compatible with destination-sign failure.

The hierarchy is now explicit. Bounded-operator norm is too strong and mistakes a shrinking-support source event for a discontinuity; norm-resolvent and graph topology are strong enough to transport the spectral branch; but the **moving destination margin is finer still**. The exact source equation supplies the needed relative control because it magnifies precisely the dangerous antisymmetric layer to the square-root-log forcing scale.

The remaining question is no longer whether the actual eigenbranch exists continuously through the first-prime event: PL-330 supplies that spectral continuity under the stated localized-Weil setup. The live problem is whether the transported **actual completed-Weil branch** obeys the PL-329 source-amplitude gate uniformly, including control preventing `C_delta` from collapsing. Proving that would make the first crossing source-selected rather than topologically imposed.

**Boundary.** PL-329 is a sufficient sharp criterion for the first-prime reflection, while PL-330 is a topology refinement for the first activation. Neither proves the source-amplitude condition for the actual branch, orients later prime-power channels, or implies global Weil positivity/RH. The square-root-log threshold remains relative to `|C_delta|`; if the leading coefficient degenerates, the criterion must be re-evaluated.
