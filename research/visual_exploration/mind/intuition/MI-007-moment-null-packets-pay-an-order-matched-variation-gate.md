# MI-007 — Moment-null shrinking packets are limited by conditioning and by nonanalytic destination cusps

**Evidence level:** exact synthesis from the finite-window moment/capacity chain VIS-145--VIS-147 and the sine-kernel cusp obstruction [VIS-256](../../findings/VIS-256-finite-moments-do-not-beat-sine-kernel-cusp.md).

Vanishing moments are useful only relative to the regularity of the function they are asked to annihilate. In the smooth finite-window regime, VIS-145 shows that a zero second frequency moment removes the entire common quadratic centered-cosine response, not only the CUE part. The first possible deterministic distinction then moves to quartic or higher order.

That shift has an exact conditioning bill. VIS-146 gives `|m_(2j)(nu_b)| <= b^(2j)||nu_b||_TV`; retaining an order-one `2j`-th moment on bandwidth `b` therefore costs at least `b^(-2j)` total variation. Any uncertainty controlled linearly by the same variation is amplified in lockstep. Packet rescaling cannot create signal-to-error separation; the post-calibration source coefficient must beat an error gate at the same order.

VIS-256 shows that this Taylor-order picture is not even the right abstraction when the limiting destination is nonsmooth. The centered sine-kernel/CUE form-factor increment is `T(q)=min(|q|,1)`, so near zero the destination is the cusp `|q|`. For every fixed `n` there is an explicit symmetric finite signed measure with bounded-in-`b` total variation that annihilates every ordinary moment through degree `2n-1`, yet after dilation to `[-b,b]` satisfies

`int T(q) dnu_b(q) = c_n b`, with `c_n != 0`.

Thus **no fixed finite number of polynomial moments forces an improvement from `O(b)` to `o(b)` against the sine-kernel cusp**. Moment cancellation can eliminate a finite Taylor jet, but `|q|` is not represented by such a jet. This obstruction is logically different from the total-variation price of smooth high-order cancellation: here even keeping the normalization bounded does not remove the linear response.

The combined design principle is to inspect destination regularity before choosing moment constraints. For a uniformly smooth kernel, moments can suppress successive derivatives but the conditioning cost must be paid. For a cusp or other nonanalytic feature, polynomial moments may be the wrong dual coordinates altogether; one needs direct control of a cusp-adapted functional such as `int |q| dnu_b`, a packet architecture that annihilates the actual singular profile, or a theorem giving a uniform finite-window smoothing scale before the asymptotic limit is taken.

For the support-edge zeta/CUE route, adding zero mass, symmetry or more fixed ordinary moments to the low-frequency companion is therefore not a legitimate claim of stronger null suppression. The source-specific arithmetic residual, theorem/transfer error, normalization and covariance still have to be propagated through whatever extra mechanism actually controls the cusp.

**Boundary.** The VIS-256 construction is a sharpness obstruction for deductions from bounded total variation plus any *fixed finite* set of ordinary moments. It does not say every moment-balanced packet has linear cusp response, and it does not provide a uniform finite-`N` lower bound: at fixed finite source window the profile can be smoother on sufficiently tiny scales. If cancellation order grows with the asymptotic parameter, total variation and conditioning again become part of the problem. Nothing here proves a zeta-specific arithmetic residual or finite-height transfer theorem.
