# MI-026 — Sign-destructive proof interfaces cannot certify destination cancellation

**Evidence level:** supported cross-line synthesis from [VIS-275](../../visual_exploration/findings/VIS-275-wang-laplace-null-source-bound-floor.md), [VIS-276](../../visual_exploration/findings/VIS-276-wang-source-floor-localizes-to-explicit-remainder-mean.md), and [WI-334](../../weil_inertia/findings/WI-334-fixed-order-gowers-uniformity-does-not-force-bow-variance-cancellation.md). The results concern different analytic objects; the common statement is about where their proof interfaces retain or destroy the signed information required by the destination.

Two current frontiers fail for the same structural reason: the desired improvement is a **signed cancellation statement**, while the available intermediate bound has already forgotten the sign/covariance needed to certify it.

In the fixed-window Wang channel, a signed Laplace-null packet removes the leading main term exactly. VIS-275 shows that the dominant available remainder certificate then contains

`(1/log T) int |h(q)| e^(-4pi q)dq`.

Once the proof has replaced the residual by this absolute envelope, additional signed packet moments cannot improve the certified exponent for any fixed nonzero packet.

VIS-276 now identifies the signed quantity immediately before that information is lost. In Wang's decomposition `A=-D+B+E`, the deterministic `B^2` variation is power-smaller on the short interval. The first unresolved `1/log T` channel is the signed cross term governed by

`M_T(x)=(x/H) Re int_T^(T+H) E_x(t)dt`.

The pointwise bound `E_x=O(1/x)` turns this into the coarse statement `M_T=O(1)` and only then produces the absolute `1/log T` floor. Thus the barrier is a property of the current proof interface, not evidence that the true residual has that size. A direct theorem `M_T=o(1)` on fixed source windows would cross the floor without adding any packet moments.

In the Weil-inertia bow, the lost datum is two-point rather than one-point sign. WI-334 constructs sequences whose local `U^s` norms are power-small on every bow-scale interval simultaneously for every order in an arbitrary fixed finite hierarchy, yet whose sliding variance against a prescribed carrier remains at the full diagonal scale. Fixed-order Gowers uniformity records many additive patterns, but not the negative off-diagonal covariance required to cancel the positive diagonal.

The shared lesson is more precise than “use a stronger norm.” **A proof interface cannot be strengthened by manipulating information it has already quotient out.** Signed moment constraints do not act on an absolute remainder; more fixed-order one-point uniformity does not determine a missing covariance sign. The useful next object is the signed quantity *just before* the destructive step: `M_T(x)` in the Wang decomposition, and an arithmetic two-point covariance/off-diagonal term in the bow.

There are only two honest ways across such a boundary. Recover and estimate the missing structure before majorization or norm compression, or replace the interface by a theorem that directly controls the destination-sensitive signed quantity. Merely stacking more constraints inside the already sign-blind summary cannot supply the missing information.

**Boundary.** VIS-276 does not prove cancellation in `M_T`, and WI-334 does not describe the actual von Mangoldt covariance. In both cases a stronger source theorem may expose the needed sign. The synthesis is only that the new information must enter before or instead of the lossy interface; it cannot be reconstructed from that interface alone.