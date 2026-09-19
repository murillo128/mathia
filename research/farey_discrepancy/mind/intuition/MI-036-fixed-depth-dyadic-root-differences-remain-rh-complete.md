# MI-036 — Fixed-depth signed dyadic root differences remain RH-complete

**Evidence level:** exact synthesis from [FD-206](../../findings/FD-206-root-aligned-lowbit-anchor-is-an-rh-equivalent-dyadic-mertens-criterion.md) and [FD-207](../../findings/FD-207-fixed-depth-dyadic-root-differences-remain-rh-equivalent-at-critical-random-cost.md), interpreted against the lowbit geometry of FD-204--FD-205.

FD-206 identifies the root-aligned Farey sensor

`Delta(n)=M(2n)-M(n)`

as a destination-complete scalar coordinate: square-root control of `Delta` reconstructs square-root control of arbitrary `M(N)` through binary prefixes. This already shows why a positive energy containing `|Delta(n)|^2` has not lowered the RH theorem surface even when the surrounding lowbit graph has logarithmic resistance and a near-critical random benchmark.

FD-207 asks whether cancellation can be restored by differencing root sensors across scales **before** positivity. Let `T` be dyadic dilation, `(TF)(n)=F(2n)`, and for fixed `q>=0` define

`C_q(n)=(T-I)^q Delta(n)`.

Every `C_q` is an exact signed combination of the root-aligned Farey sensors at `n,2n,...,2^q n`. The literal standalone root anchor has disappeared for `q>=1`, and the squarefree-Rademacher comparator still pays only the critical random scale: `E|C_q^f(n)|^2=Theta_q(n)`.

But the pointwise analytic difficulty has not changed. The physical Möbius source has a bounded odd-step defect. That defect reconnects dyadic orbits and lets a critical bound on `C_q` be inverted one finite difference at a time along binary prefixes. For every fixed `q`,

`C_q(n)=O_epsilon(n^(1/2+epsilon))`

is therefore equivalent to RH, and more generally an `n^(1/2)L(n)` bound propagates back to the same square-root scale for `M(N)` up to a logarithmic correction.

The reusable distinction is between **placing sign before positivity** and **creating noninvertible signed leverage**. A finite signed transform can remove the visible hard coordinate while preserving an exact bounded inverse on the physical source class. In that case the representation looks more cancellative and can even retain a favorable random benchmark, but its pointwise critical estimate is still destination-complete.

A genuine Farey escape must break that fixed-depth inversion. Natural possibilities left open by FD-207 are a depth `q=q(n)` growing with scale, an aggregate signed inequality across many root edges that does not first control each coefficient at the critical pointwise scale, or an observable whose recovery uses additional Farey geometry rather than a fixed polynomial in dyadic dilation.

**Boundary.** The fixed-depth hypothesis is essential. The inversion constants depend on `q`, so FD-207 does not classify growing-depth transforms or collective nonpointwise estimates. The random comparator is only a cost calibration and supplies no deterministic Möbius cancellation. The result does not invalidate the lowbit tree; it isolates the point at which its current positive/root architecture becomes analytically circular.