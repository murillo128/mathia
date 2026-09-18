# MI-026 — Sign-destructive or scale-mismatched proof interfaces cannot certify destination cancellation

**Evidence level:** supported cross-line synthesis from [VIS-275](../../visual_exploration/findings/VIS-275-wang-laplace-null-source-bound-floor.md) through [VIS-282](../../visual_exploration/findings/VIS-282-wang-fixed-source-dirichlet-profile.md), and [WI-334](../../weil_inertia/findings/WI-334-fixed-order-gowers-uniformity-does-not-force-bow-variance-cancellation.md) through [WI-339](../../weil_inertia/findings/WI-339-diagonal-deleted-gowers-still-misses-bow-variance.md). The results concern different analytic objects; the common statement is about whether an intermediate retains the signed information, physical scale and destination coupling actually required.

Two current frontiers fail for related structural reasons: the desired improvement is a **signed destination statement**, while an available intermediate either forgets the needed covariance, is evaluated in a larger parameter regime than the destination uses, or removes a generic self-term without adding the source-specific relation that the destination consumes.

In the fixed-window Wang channel, VIS-275 shows that once the residual has been replaced by a sign-blind absolute envelope, extra signed packet moments cannot improve the certified exponent. VIS-276--VIS-278 then separate convention-dependent gamma normalization from an invariant combined residual whose standalone energy lives at `L^-2`.

VIS-279--VIS-281 expose a second failure mode: theorem-uniform errors can disappear after specialization to the physical fixed-source coordinate. The `D_x--E_x` cross drops to `L^-2`, the direct `D_x--B_x` cross is power-small, and the zero-window localization error is also power-small after the actual pullback. None realizes the apparent `L^-3/2` frontier.

VIS-282 shows why merely labeling the remaining fixed-source `D_x` mean-square uncertainty as `O(H)` is also destructive. The exact diagonal energy is

`S_D(x)=x^(-2) sum_(n<=x)n Lambda(n)^2 + x^2 sum_(n>x)Lambda(n)^2/n^3`,

with

`int_I |D_x(t)|^2 dt = H S_D(x)+O_K(1)`.

The difference `S_D(x)-log x` contributes at `L^-2` and has derivative jumps `-4 Lambda(m)^2/m^2` at prime powers. The anonymous `O(H)` was therefore hiding destination-scale arithmetic structure, while the genuine averaging error was much smaller. The correct next step is exact recombination at the physical coefficient scale, not another cancellation imposed on a coarse uniform remainder.

In Weil Inertia, ordinary Gowers smallness loses the needed two-point sign in a different way. WI-338 squeezes the ordinary hierarchy exactly against its deterministic zero-increment diagonal wall: below the wall generic matched-energy signs can be Gowers-small on every bow interval while preserving full sliding variance; at the wall the source energy prevents smallness.

WI-339 tests the literal diagonal-free repair. Removing every zero-increment cube is exactly centering the Rademacher cube chaos. This moves the all-interval countermodel frontier from `R_s=2` to the much higher curve `R_s=(s+1)`, but the matched-energy source can still have small diagonal-deleted amplitude while retaining `(1+o(1))NK log N` bow variance. **Subtracting a generic self-energy does not manufacture the distinguished negative covariance.**

The shared lesson is therefore sharper than “preserve sign” or “renormalize the diagonal.” An intermediate is useful only if it preserves the destination-sensitive relation, is evaluated at the same physical scale, and keeps exact source structure until one knows which terms really survive there. A normalization-invariant quantity can still be too coarse; a diagonal-free statistic can still be source-blind; and a uniform theorem bound can still hide both a smaller true error and a structured coefficient-scale term.

There are three honest ways across such a boundary. Recover and estimate the destination-sensitive structure before majorization or norm compression; define a renormalization whose subtraction is itself tied to the source/carrier relation rather than only to generic degeneracy; or re-specialize the upstream theorem so that exact structured terms survive through the physical coordinate map. More constraints inside an already sign-destructive, scale-mismatched or source-blind summary do not help unless they can be shown to control the actual destination observable.

**Boundary.** VIS-282 does not prove that the full fixed-source Wang theorem has remainder `O(L^-2)` or that its prime-power profile survives final recombination. WI-339 leaves a top growing-order strip and does not rule out source-dependent, carrier-dependent or relative-linear-forms renormalizations. The synthesis does not identify those two problems mathematically; it states the common interface test: subtraction or specialization counts as progress only when the information retained after it is the information the destination actually needs.