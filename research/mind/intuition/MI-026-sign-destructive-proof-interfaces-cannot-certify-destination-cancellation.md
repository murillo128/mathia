# MI-026 — Sign-destructive or scale-mismatched proof interfaces cannot certify destination cancellation

**Evidence level:** supported cross-line synthesis from [VIS-275](../../visual_exploration/findings/VIS-275-wang-laplace-null-source-bound-floor.md) through [VIS-281](../../visual_exploration/findings/VIS-281-wang-fixed-source-localization-power-small.md), and [WI-334](../../weil_inertia/findings/WI-334-fixed-order-gowers-uniformity-does-not-force-bow-variance-cancellation.md)--[WI-338](../../weil_inertia/findings/WI-338-hypercontractive-cube-concentration-closes-all-start-gowers-gap.md). The results concern different analytic objects; the common statement is about whether an intermediate retains the signed information, physical scale and destination coupling actually required.

Two current frontiers fail for related structural reasons: the desired improvement is a **signed cancellation statement**, while an available intermediate either forgets the needed sign/covariance, is evaluated in a parameter regime larger than the destination actually uses, or saturates at a source-imposed diagonal contribution before it can determine the destination.

In the fixed-window Wang channel, a signed Laplace-null packet removes the leading main term exactly. VIS-275 shows that the dominant available remainder certificate then contains

`(1/log T) int |h(q)| e^(-4pi q)dq`.

Once the proof has replaced the residual by this absolute envelope, additional signed packet moments cannot improve the certified exponent for any fixed nonzero packet.

VIS-276 localized a pre-majorization signed coordinate to the remainder mean, but VIS-277 shows why signed is not enough: in Wang's original split that coordinate tends to `-log(2*pi)`, a classical gamma normalization that can be moved between `B` and `E` without changing the full source. VIS-278 then constructs the invariant combined residual

`R_x(t)=x(B_x(t)+E_x(t))-log(t/(2*pi))`.

Its mean tends to zero but its mean-square tends to the positive classical constant `C_Lambda=sum_(n>=2)Lambda(n)^2/n^3`. Under the fixed-source pullback this pure source-energy term contributes only at `L^-2`.

VIS-279 adds a parameter-regime audit: the `D_x`--`E_x` cross drops to `L^-2` when Wang's exact mean-square theorem is specialized to fixed physical source before rescaling. The previously quoted `L^-3/2` contribution came from a uniform-in-growing-`x` `L^2` estimate, not from the compact `q` regime consumed by the packet.

VIS-280 completes the direct prime/source audit. Wang's explicit `D_x`--`B_x` cross estimate becomes `O_K(1/(HL))` after fixed-source packet normalization, hence is power-small in `T`. Therefore the entire direct interaction `D_x` against `B_x+E_x` is excluded as a compulsory `L^-3/2` mechanism.

VIS-281 shows that the same scale mismatch can occur in a theorem-level replacement step rather than an individual decomposition term. Wang's `A_I -> A` zero-window localization costs `O(xL^3)` uniformly over a much larger moving source range. On the fixed physical packet, `x` is bounded; after `dq/L` pullback and `1/(HL)` normalization the complete localization loss is only `O_K(L/H)`, below every fixed inverse power of `L`. The missing object is therefore not “some better cancellation inside the source cross or localization error”; the remaining proof must first exhibit an exact sector that genuinely survives at the claimed logarithmic scale.

In the Weil-inertia bow, the lost datum is two-point rather than one-point sign. WI-334 constructs sequences whose local `U^s` norms are power-small throughout any fixed finite hierarchy while sliding variance stays at the full diagonal scale. WI-335 extends the countermodel to growing order. WI-336 then shows that diagonal zero-increment cubes force high-order `U^s` to become non-small once `R_s=2^s loglog N/log K` reaches the natural threshold.

WI-337 brought density-one random-sign countermodels to every fixed margin below `R_s=2`. WI-338 closes the remaining all-start gap: whenever `R_s<=2-delta_N` with `delta_N loglog N->infinity`, one matched-energy realization is `U^s=o(1)` simultaneously on **every** bow-scale interval and all retained orders while still carrying the full diagonal sliding variance. In the complementary `delta_N loglog N=O(1)` boundary layer, the deterministic diagonal floor already prevents ordinary `U^s=o(1)` for every comparable-energy source. Thus there is no ordinary-Gowers window left for a stronger start quantifier or higher order to exploit.

The shared lesson is more precise than “use a stronger norm.” **An intermediate is useful only if it preserves the destination-sensitive sign/covariance, survives harmless normalization freedom, is evaluated at the same physical scale consumed by the destination, and has not saturated on a diagonal/source-universal component before the destination sign is visible.** Signed moments do not act on an absolute remainder; a normalization-dependent signed coordinate is not intrinsic; a theorem-uniform exponent or localization loss can disappear after source specialization; and an ordinary Gowers hierarchy can be squeezed exactly between generic countermodels below a diagonal wall and deterministic non-smallness at that wall.

There are three honest ways across such a boundary. Recover and estimate the destination-sensitive structure before majorization or norm compression; replace the intermediate by a normalization-invariant or diagonally renormalized statistic that directly controls the needed covariance; or sharpen/reformulate the upstream theorem in the exact physical regime so that it retains the source-specific relation rather than only an ordinary norm or uniform replacement error already known to be slack there. Stacking more constraints inside an already lossy, scale-mismatched or diagonally saturated summary is useful only when the new information can be proved to couple to the actual destination observable.

**Boundary.** VIS-281 does not prove the entire fixed-source Wang remainder is `O(L^-2)` or exclude a different genuine `L^-3/2` sector. WI-338 does not describe the actual von Mangoldt covariance, construct an arithmetic counterexample with the prime singular series, or rule out a diagonal-free/renormalized higher-order statistic. In both cases a stronger source-specific theorem may expose the needed structure. The synthesis is only that sign, normalization, physical scaling, theorem-level replacement losses and diagonal content must be audited before an intermediate is credited with destination-level cancellation.
