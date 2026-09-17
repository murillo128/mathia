# MI-026 — Sign-destructive or scale-mismatched proof interfaces cannot certify destination cancellation

**Evidence level:** supported cross-line synthesis from [VIS-275](../../visual_exploration/findings/VIS-275-wang-laplace-null-source-bound-floor.md) through [VIS-279](../../visual_exploration/findings/VIS-279-wang-fixed-source-removes-l32-floor.md), and [WI-334](../../weil_inertia/findings/WI-334-fixed-order-gowers-uniformity-does-not-force-bow-variance-cancellation.md)--[WI-336](../../weil_inertia/findings/WI-336-matched-energy-diagonal-cubes-squeeze-gowers-escape-to-one-order-window.md). The results concern different analytic objects; the common statement is about whether an intermediate retains the signed information and physical scale required by the destination.

Two current frontiers fail for related structural reasons: the desired improvement is a **signed cancellation statement**, while an available intermediate either forgets the needed sign/covariance or is being evaluated in a parameter regime larger than the destination actually uses.

In the fixed-window Wang channel, a signed Laplace-null packet removes the leading main term exactly. VIS-275 shows that the dominant available remainder certificate then contains

`(1/log T) int |h(q)| e^(-4pi q)dq`.

Once the proof has replaced the residual by this absolute envelope, additional signed packet moments cannot improve the certified exponent for any fixed nonzero packet.

VIS-276 localized a pre-majorization signed coordinate to the remainder mean, but VIS-277 shows why signed is not enough: in Wang's original split that coordinate tends to `-log(2*pi)`, a classical gamma normalization that can be moved between `B` and `E` without changing the full source. VIS-278 then constructs the invariant combined residual

`R_x(t)=x(B_x(t)+E_x(t))-log(t/(2*pi))`.

Its mean tends to zero but its mean-square tends to the positive classical constant `C_Lambda=sum_(n>=2)Lambda(n)^2/n^3`. Under the fixed-source pullback this pure source-energy term contributes only at `L^-2`.

VIS-279 adds a second audit: the first obvious non-source cross term also drops to `L^-2` when Wang's exact mean-square theorem is specialized to fixed physical source before rescaling. The previously quoted `L^-3/2` contribution came from a uniform-in-growing-`x` `L^2` estimate, not from the compact `q` regime consumed by the packet. The missing object is therefore not merely “some signed `L^-3/2` term”; the full fixed-source decomposition must first demonstrate that an intrinsic `L^-3/2` sector exists at all.

In the Weil-inertia bow, the lost datum is two-point rather than one-point sign. WI-334 constructs sequences whose local `U^s` norms are power-small throughout any fixed finite hierarchy while sliding variance stays at the full diagonal scale. WI-335 extends the countermodel to growing order. WI-336 then closes the opposite side: diagonal zero-increment cubes force high-order `U^s` to become non-small once `2^s loglog N/log K` crosses the complementary threshold. Since raising `s` by one doubles this ratio, ordinary Gowers smallness is squeezed to at most one critical order window. Below it the norm is too weak to force covariance cancellation; above it the source's own diagonal energy prevents smallness.

The shared lesson is more precise than “use a stronger norm.” **An intermediate is useful only if it preserves the destination-sensitive sign/covariance, survives harmless normalization freedom, and is evaluated at the same physical scale and parameter regime consumed by the destination.** Signed moments do not act on an absolute remainder; a normalization-dependent signed coordinate is not intrinsic; a theorem-uniform exponent can disappear after source specialization; more ordinary Gowers orders do not manufacture the missing covariance and eventually become diagonal-dominated themselves.

There are three honest ways across such a boundary. Recover and estimate the destination-sensitive structure before majorization or norm compression; replace the intermediate by a normalization-invariant or diagonally renormalized statistic that directly controls the needed covariance; or sharpen the upstream theorem in the exact physical regime so that an apparent limiting scale is removed rather than canceled. Stacking more constraints inside an already lossy or scale-mismatched summary is useful only when the new information can be proved to couple to the actual destination observable.

**Boundary.** VIS-279 does not prove the entire fixed-source Wang remainder is `O(L^-2)` or exclude a different genuine `L^-3/2` sector. WI-336 does not describe the actual von Mangoldt covariance or rule out a critical-order/diagonal-free statistic. In both cases a stronger source-specific theorem may expose the needed structure. The synthesis is only that sign, normalization and physical scaling must be audited before an intermediate is credited with destination-level cancellation.
