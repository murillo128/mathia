# MI-026 — Sign-destructive proof interfaces cannot certify destination cancellation

**Evidence level:** supported cross-line synthesis from [VIS-275](../../visual_exploration/findings/VIS-275-wang-laplace-null-source-bound-floor.md) and [WI-334](../../weil_inertia/findings/WI-334-fixed-order-gowers-uniformity-does-not-force-bow-variance-cancellation.md). The two results concern different analytic objects; the common statement is about which information their current proof interfaces retain, not a transfer of either theorem to the other line.

Two current frontiers fail for the same structural reason: the desired destination improvement is a **signed cancellation statement**, while the available intermediate bound has already forgotten the sign/covariance needed to certify it.

In the fixed-window Wang channel, a signed Laplace-null packet removes the leading main term exactly. But the dominant remainder exposed by the present proof is controlled by

`(1/log T) int |h(q)| e^(-4pi q)dq`.

Once the remainder has been replaced by this absolute envelope, adding further signed moments cannot improve the certified exponent for any fixed nonzero packet. The orthogonality acts on a sign structure that the bound no longer contains.

In the Weil-inertia bow, the lost datum is two-point rather than one-point sign. WI-334 constructs sequences whose local `U^s` norms are power-small on every bow-scale interval simultaneously for every order in an arbitrary fixed finite hierarchy, yet whose sliding variance against a prescribed carrier remains at the full diagonal scale. Fixed-order Gowers uniformity records many additive patterns, but not the negative off-diagonal covariance required to cancel the positive diagonal.

The shared lesson is more precise than “use a stronger norm.” **A proof interface cannot be strengthened by manipulating information it has already quotient out.** Signed moment constraints do not act on an absolute remainder; more fixed-order one-point uniformity does not determine a missing covariance sign. Before iterating an orthogonality, smoothing or pseudorandomness argument, identify whether the destination quantity depends on phase/sign data that the current inequality or norm has discarded.

There are only two honest ways across such a boundary. Recover the missing structure before the destructive step—for example a signed asymptotic for the Wang remainder or an arithmetic two-point identity for the bow source—or replace the interface by a theorem that directly controls the destination-sensitive signed quantity. Merely stacking more constraints inside the already sign-blind summary cannot supply the missing information.

**Boundary.** VIS-275 does not prove the true Laplace-null residual is of order `1/log T`, and WI-334 does not describe the actual von Mangoldt covariance. In both cases a stronger theorem may expose the missing sign. The synthesis is that such new signed information must enter *before or instead of* the lossy interface; it cannot be reconstructed from that interface alone.