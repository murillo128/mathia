# MI-026 — Sign-destructive proof interfaces cannot certify destination cancellation

**Evidence level:** supported cross-line synthesis from [VIS-275](../../visual_exploration/findings/VIS-275-wang-laplace-null-source-bound-floor.md) through [VIS-277](../../visual_exploration/findings/VIS-277-wang-remainder-mean-is-log-2pi-normalization.md), and [WI-334](../../weil_inertia/findings/WI-334-fixed-order-gowers-uniformity-does-not-force-bow-variance-cancellation.md). The results concern different analytic objects; the common statement is about where their proof interfaces retain or destroy the signed information required by the destination.

Two current frontiers fail for the same structural reason: the desired improvement is a **signed cancellation statement**, while an available intermediate bound has already forgotten the sign/covariance needed to certify it.

In the fixed-window Wang channel, a signed Laplace-null packet removes the leading main term exactly. VIS-275 shows that the dominant available remainder certificate then contains

`(1/log T) int |h(q)| e^(-4pi q)dq`.

Once the proof has replaced the residual by this absolute envelope, additional signed packet moments cannot improve the certified exponent for any fixed nonzero packet.

VIS-276 localized the pre-majorization quantity to the signed remainder mean `M_T(x)=(x/H) Re int E_x(t)dt`. VIS-277 then shows why even this refinement must respect normalization: in Wang's original split,

`M_T(x) = -log(2*pi) + O_K(H^-1+T^-1)`.

The mean does not vanish; its leading value is the classical gamma-factor normalization. Recentring the decomposition makes the remainder mean `o(1)`, but the same `log(2*pi)` contribution moves into the explicit `B_x^2` term and leaves the full `1/log T` source correction unchanged. The correct signed object is therefore not an arbitrary decomposition piece but the first **normalization-invariant** residual of the combined source after the classical baseline has been removed consistently.

In the Weil-inertia bow, the lost datum is two-point rather than one-point sign. WI-334 constructs sequences whose local `U^s` norms are power-small on every bow-scale interval simultaneously for every order in an arbitrary fixed finite hierarchy, yet whose sliding variance against a prescribed carrier remains at the full diagonal scale. Fixed-order Gowers uniformity records many additive patterns, but not the negative off-diagonal covariance required to cancel the positive diagonal.

The shared lesson is more precise than “use a stronger norm.” **A proof interface cannot be strengthened by manipulating information it has already quotiented out, and a signed intermediate variable is useful only if it is invariant under harmless normalization choices.** Signed moment constraints do not act on an absolute remainder; more fixed-order one-point uniformity does not determine a missing covariance sign; moving a deterministic constant between two decomposition terms does not create cancellation in their sum.

There are only two honest ways across such a boundary. Recover and estimate the destination-sensitive signed structure before majorization or norm compression, in a normalization-invariant formulation, or replace the interface by a theorem that directly controls that structure. Merely stacking more constraints inside the already lossy summary cannot supply the missing information.

**Boundary.** VIS-277 does not compute the next normalization-invariant fixed-source residual, and WI-334 does not describe the actual von Mangoldt covariance. In both cases a stronger source theorem may expose the needed sign. The synthesis is only that the new information must enter before or instead of the lossy interface and must survive the natural gauge/normalization freedom of the representation.