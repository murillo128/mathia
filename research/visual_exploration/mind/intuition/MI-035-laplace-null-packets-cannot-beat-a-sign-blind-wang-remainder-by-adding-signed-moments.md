# MI-035 — Sign-destructive Wang bounds must be repaired at a normalization-invariant source interface

**Evidence level:** literature+derived synthesis from [VIS-274](../../findings/VIS-274-wang-fixed-q-rescaled-laplace-limit.md), [VIS-275](../../findings/VIS-275-wang-laplace-null-source-bound-floor.md), [VIS-276](../../findings/VIS-276-wang-source-floor-localizes-to-explicit-remainder-mean.md), and [VIS-277](../../findings/VIS-277-wang-remainder-mean-is-log-2pi-normalization.md). The `log(2*pi)` term is classical gamma-factor normalization; the Mathia content is the correction of the live fixed-source remainder interface.

At fixed physical `q`, VIS-274 shows that Wang's concentrating main term should be retained and rescaled rather than Taylor-collapsed. A signed Laplace-null packet can then remove the leading source functional. VIS-275 shows why the current absolute proof interface cannot certify a further improvement: after the same rescaling, the dominant available bound contains

`O((1/log T) int |h(q)| e^(-4pi q)dq)`.

Once the proof has replaced the residual by this absolute envelope, additional signed packet moments cannot recover the discarded cancellation.

VIS-276 located the apparent lost sign in Wang's decomposition `A=-D+B+E` through

`M_T(x)=(x/H) Re int_T^(T+H) E_x(t)dt`.

VIS-277 now evaluates that quantity rather than merely bounding it:

`M_T(x) = -log(2*pi) + O_K(H^-1+T^-1)`

uniformly on compact fixed-source windows. Thus the earlier hope `M_T=o(1)` was not a hidden arithmetic cancellation in Wang's original convention. The nonzero mean is the classical functional-equation normalization.

One can recenter the decomposition by replacing `B_x(t)=log(t+2)/x` with `[log(t+2)-log(2*pi)]/x`, after which the recentered remainder mean is `o(1)`. But the same constant then reappears in `|B_x|^2` at the normalization-invariant `1/log T` source scale. Moving a deterministic term between `B` and `E` does not improve the full statistic.

The reusable lesson is therefore stronger than “estimate the signed residual before taking absolute values.” **First identify the normalization-invariant signed source object; only then ask where the proof destroys its cancellation.** A decomposition-dependent remainder can acquire or lose a mean under harmless recentering, while the combined source contribution is unchanged. Packet orthogonality should be designed against the first unresolved kernel of that combined contribution after the classical `log(t/(2*pi))` baseline has been removed consistently.

The next fixed-source target is the first normalization-invariant correction beyond the deterministic `1/log T` term, not `M_T` in isolation. If that correction admits a signed asymptotic below the current absolute envelope, then packet cancellation may again become meaningful; if it is itself sign-blind or universal, the route must move to a different source observable.

**Boundary.** VIS-277 resolves only the fixed-source mean in Wang's present short-interval regime. It does not give the complete secondary expansion, control the `D_x,E_x` interaction, analyze moving source windows, or show that the next normalization-invariant residual has a favorable sign. Weil-inertia-style covariance obstructions remain mathematically distinct; the shared principle is only that lost sign cannot be reconstructed after a lossy interface.