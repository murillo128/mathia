# MI-026 — Sign-destructive or scale-mismatched proof interfaces cannot certify destination cancellation

**Evidence level:** supported cross-line synthesis from [VIS-275](../../visual_exploration/findings/VIS-275-wang-laplace-null-source-bound-floor.md) through [VIS-280](../../visual_exploration/findings/VIS-280-wang-db-cross-power-small.md), and [WI-334](../../weil_inertia/findings/WI-334-fixed-order-gowers-uniformity-does-not-force-bow-variance-cancellation.md)--[WI-337](../../weil_inertia/findings/WI-337-almost-all-gowers-countermodels-reach-diagonal-threshold.md). The results concern different analytic objects; the common statement is about whether an intermediate retains the signed information, start quantifier and physical scale required by the destination.

Two current frontiers fail for related structural reasons: the desired improvement is a **signed cancellation statement**, while an available intermediate either forgets the needed sign/covariance, is evaluated in a parameter regime larger than the destination actually uses, or is asserted under a start quantifier too weak to determine the distinguished destination.

In the fixed-window Wang channel, a signed Laplace-null packet removes the leading main term exactly. VIS-275 shows that the dominant available remainder certificate then contains

`(1/log T) int |h(q)| e^(-4pi q)dq`.

Once the proof has replaced the residual by this absolute envelope, additional signed packet moments cannot improve the certified exponent for any fixed nonzero packet.

VIS-276 localized a pre-majorization signed coordinate to the remainder mean, but VIS-277 shows why signed is not enough: in Wang's original split that coordinate tends to `-log(2*pi)`, a classical gamma normalization that can be moved between `B` and `E` without changing the full source. VIS-278 then constructs the invariant combined residual

`R_x(t)=x(B_x(t)+E_x(t))-log(t/(2*pi))`.

Its mean tends to zero but its mean-square tends to the positive classical constant `C_Lambda=sum_(n>=2)Lambda(n)^2/n^3`. Under the fixed-source pullback this pure source-energy term contributes only at `L^-2`.

VIS-279 adds a parameter-regime audit: the `D_x`--`E_x` cross drops to `L^-2` when Wang's exact mean-square theorem is specialized to fixed physical source before rescaling. The previously quoted `L^-3/2` contribution came from a uniform-in-growing-`x` `L^2` estimate, not from the compact `q` regime consumed by the packet.

VIS-280 completes the direct prime/source audit. Wang's explicit `D_x`--`B_x` cross estimate becomes `O_K(1/(HL))` after fixed-source packet normalization, hence is power-small in `T`. Therefore the entire direct interaction `D_x` against `B_x+E_x` is excluded as a compulsory `L^-3/2` mechanism. The missing object is not “some better cancellation inside the source cross”; the remaining fixed-source proof must first exhibit an exact sector that genuinely survives at `L^-3/2`.

In the Weil-inertia bow, the lost datum is two-point rather than one-point sign. WI-334 constructs sequences whose local `U^s` norms are power-small throughout any fixed finite hierarchy while sliding variance stays at the full diagonal scale. WI-335 extends the countermodel to growing order. WI-336 then closes the high-order side: diagonal zero-increment cubes force high-order `U^s` to become non-small once `2^s loglog N/log K` reaches the complementary threshold, leaving at most one binary-order window for an all-start theorem.

WI-337 shows that even this window disappears for the **density-one/almost-all black-box interface**. A matched-energy Rademacher realization can be simultaneously `U^s=o(1)` on a density-one set of intervals for every order with `R_s<=2-eta`, while those same good intervals retain asymptotically the entire diagonal sliding variance. Above `R_s>=2+eta`, comparable-energy ordinary smallness is impossible. Thus an almost-all ordinary-Gowers theorem cannot manufacture the missing bow covariance by moving to higher order; the generic countermodel reaches the same diagonal threshold from below.

The shared lesson is more precise than “use a stronger norm.” **An intermediate is useful only if it preserves the destination-sensitive sign/covariance, survives harmless normalization freedom, is evaluated at the same physical scale and parameter regime consumed by the destination, and carries the start quantifier required by the destination.** Signed moments do not act on an absolute remainder; a normalization-dependent signed coordinate is not intrinsic; a theorem-uniform exponent can disappear after source specialization; and almost-all ordinary Gowers smallness can remain compatible with full destination variance all the way to the diagonal wall.

There are three honest ways across such a boundary. Recover and estimate the destination-sensitive structure before majorization or norm compression; replace the intermediate by a normalization-invariant or diagonally renormalized statistic that directly controls the needed covariance; or sharpen the upstream theorem in the exact physical regime and start quantifier so that an apparent limiting scale or exceptional-set gap is removed rather than rhetorically canceled. Stacking more constraints inside an already lossy, scale-mismatched or quantifier-mismatched summary is useful only when the new information can be proved to couple to the actual destination observable.

**Boundary.** VIS-280 does not prove the entire fixed-source Wang remainder is `O(L^-2)` or exclude a different genuine `L^-3/2` sector. WI-337 does not describe the actual von Mangoldt covariance, settle the exact `R_s=2` boundary, close the all-start critical window, or rule out a diagonal-free statistic. In both cases a stronger source-specific theorem may expose the needed structure. The synthesis is only that sign, normalization, physical scaling and start quantifier must be audited before an intermediate is credited with destination-level cancellation.
