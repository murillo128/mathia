# MI-026 — Sign-destructive proof interfaces cannot certify destination cancellation

**Evidence level:** supported cross-line synthesis from [VIS-275](../../visual_exploration/findings/VIS-275-wang-laplace-null-source-bound-floor.md) through [VIS-278](../../visual_exploration/findings/VIS-278-wang-gamma-normalized-source-energy.md), and [WI-334](../../weil_inertia/findings/WI-334-fixed-order-gowers-uniformity-does-not-force-bow-variance-cancellation.md)--[WI-335](../../weil_inertia/findings/WI-335-growing-gowers-hierarchy-still-does-not-force-bow-variance.md). The results concern different analytic objects; the common statement is about where their proof interfaces retain or destroy the signed information required by the destination.

Two current frontiers fail for the same structural reason: the desired improvement is a **signed cancellation statement**, while an available intermediate summary has already forgotten the sign/covariance needed to certify it.

In the fixed-window Wang channel, a signed Laplace-null packet removes the leading main term exactly. VIS-275 shows that the dominant available remainder certificate then contains

`(1/log T) int |h(q)| e^(-4pi q)dq`.

Once the proof has replaced the residual by this absolute envelope, additional signed packet moments cannot improve the certified exponent for any fixed nonzero packet.

VIS-276 localized a pre-majorization signed coordinate to the remainder mean, but VIS-277 shows why signed is not enough: in Wang's original split that coordinate tends to `-log(2*pi)`, a classical gamma normalization that can be moved between `B` and `E` without changing the full source. VIS-278 then constructs the correct invariant combined residual

`R_x(t)=x(B_x(t)+E_x(t))-log(t/(2*pi))`.

Its mean tends to zero but its mean-square tends to the positive classical constant

`C_Lambda=sum_(n>=2) Lambda(n)^2/n^3`.

Under the fixed-source pullback this pure source-energy term contributes only at `L^(-2)`, so it cannot explain the still larger `L^(-3/2)` theorem-level frontier. The missing signed object must therefore be sought in another interaction sector at the actual limiting scale, not in a decomposition-dependent remainder or in the already closed standalone source energy.

In the Weil-inertia bow, the lost datum is two-point rather than one-point sign. WI-334 constructs sequences whose local `U^s` norms are power-small on every bow-scale interval for every order in an arbitrary fixed finite hierarchy, while the sliding variance against a prescribed carrier remains at the full diagonal scale. WI-335 tracks the order dependence and extends the obstruction to every hierarchy satisfying

`2^(S_N) log log N=o(log K)`,

including `S_N=(1-o(1))log_2 log K`. Increasing the number of generic uniformity constraints almost to the log-log complexity scale still does not determine the negative off-diagonal covariance required to cancel the positive diagonal.

The shared lesson is more precise than “use a stronger norm.” **A proof interface cannot be strengthened by manipulating information it has already quotiented out, and an intermediate variable is useful only if it both preserves the destination-sensitive sign/covariance and is intrinsic under the representation's harmless normalization freedom.** Signed moments do not act on an absolute remainder; more Gowers orders do not manufacture a missing covariance sign; moving a deterministic baseline between decomposition terms does not create cancellation in their invariant sum; and an invariant positive energy at the wrong asymptotic order is not the missing limiting interaction.

There are only two honest ways across such a boundary. Recover and estimate the destination-sensitive structure before majorization or norm compression, in a normalization-invariant formulation at the actual limiting scale, or replace the interface by a theorem that directly controls that structure. Stacking more constraints inside an already lossy summary is useful only when the new information can be proved to couple to the missing destination observable.

**Boundary.** VIS-278 does not identify the `L^(-3/2)` interaction or prove its sign; WI-335 does not describe the actual von Mangoldt covariance and gives no sufficiency theorem at `s~log log K`. In both cases a stronger arithmetic/source theorem may expose the needed structure. The synthesis is only that the information must enter before or instead of the lossy interface, must survive natural normalization/gauge freedom, and must live at the asymptotic scale consumed by the destination theorem.