# MI-035 — Sign-destructive Wang bounds must be repaired at a normalization-invariant interaction interface

**Evidence level:** literature+derived synthesis from [VIS-274](../../findings/VIS-274-wang-fixed-q-rescaled-laplace-limit.md), [VIS-275](../../findings/VIS-275-wang-laplace-null-source-bound-floor.md), [VIS-276](../../findings/VIS-276-wang-source-floor-localizes-to-explicit-remainder-mean.md), [VIS-277](../../findings/VIS-277-wang-remainder-mean-is-log-2pi-normalization.md), and [VIS-278](../../findings/VIS-278-wang-gamma-normalized-source-energy.md). The gamma normalization and Dirichlet-series mean square are classical; the Mathia content is the location of the current fixed-source proof interface and the scale separation it imposes.

At fixed physical `q`, VIS-274 shows that Wang's concentrating main term should be retained and rescaled rather than Taylor-collapsed. A signed Laplace-null packet can then remove the leading source functional. VIS-275 shows why the current absolute proof interface cannot certify a further improvement: after the same rescaling, the dominant available bound contains

`O((1/log T) int |h(q)| e^(-4pi q)dq)`.

Once the proof has replaced the residual by this absolute envelope, additional signed packet moments cannot recover the discarded cancellation.

VIS-276 located the apparent lost sign in Wang's decomposition `A=-D+B+E` through the remainder mean `M_T(x)`. VIS-277 evaluates that quantity as

`M_T(x)=-log(2*pi)+O_K(H^-1+T^-1)`.

The nonzero mean is a decomposition-dependent gamma normalization, not a new arithmetic residual. Recentring can make that particular remainder mean vanish only by moving the same contribution into the explicit term.

VIS-278 supplies the correct invariant source interface. Define

`R_x(t)=x(B_x(t)+E_x(t))-log(t/(2*pi))`.

Uniformly on compact fixed-source windows,

`R_x(t)=zeta'/zeta(3/2-it)+O_K(t^-1)`.

Its short-interval mean tends to zero, but its mean square does not:

`(1/H) int |R_x(t)|^2 dt = C_Lambda+o_K(1)`,

`C_Lambda=sum_(n>=2) Lambda(n)^2/n^3=sum_p (log p)^2/(p^3-1)>0`.

Thus normalization repair does not make the source residual small; it separates its deterministic baseline from a classical positive prime-power energy. Crucially, under the fixed-`q` scaling this pure source-energy correction contributes only at `L^(-2)`. It cannot be the origin of the larger `L^(-3/2)` theorem-level frontier that still limits the current argument.

The reusable lesson is therefore stronger than “estimate the signed residual before taking absolute values.” **First form an invariant combined quantity, then locate the interaction sector at the actual limiting scale, and preserve that sector's sign/covariance until the destination estimate is applied.** A convention-dependent signed term can be a false target, while a genuine invariant source energy can sit at too small an order to explain the proof bottleneck.

The next fixed-source target is the signed, normalization-invariant **non-source interaction or cross term** responsible for `L^(-3/2)`. If it admits an asymptotic or cancellation theorem before Wang's absolute majorization, packet design may again matter. If the limiting sector is itself positive/sign-blind or universal, the route must move to a different observable rather than adding moments to the already closed pure-source sector.

**Boundary.** VIS-278 closes only the standalone gamma-normalized `|B+E|^2` sector in the fixed-source short-interval regime. It does not identify the full `L^(-3/2)` interaction, analyze moving source windows, or prove a favorable signed asymptotic for any cross term. The positive constant `C_Lambda` is not a new RH discriminator. Weil-inertia-style covariance obstructions remain mathematically distinct; the shared principle is only that destination-relevant sign cannot be reconstructed after a lossy interface and that invariant scale bookkeeping must precede cancellation claims.