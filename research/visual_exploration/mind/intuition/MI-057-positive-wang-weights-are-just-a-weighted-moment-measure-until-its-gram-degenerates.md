# MI-057 — Positive Wang weights are just a weighted moment measure until its Gram degenerates

**Evidence level:** exact fixed-depth weighted-sampling synthesis from [VIS-361](../../findings/VIS-361-weighted-pooled-moment-gram-floor.md), extending the unweighted pooled-Gram boundary in VIS-360.

Put a compact fixed-depth Wang bank in the outer collision coordinate `x_j=c+rho t_j`, with positive coefficient weights `w_j>0`, total mass `M=sum_j w_j`, and coefficient norm `sum_j |a_j|^2/w_j`. After the Hilbert coordinate change `a=W^(1/2)z`, the bank is ordinary polynomial sampling against the positive discrete measure with masses `w_j`.

Let `S` have columns `1,t,...,t^(q-1)` and define the normalized weighted moment Gram

`G_w = M^(-1) S^* W S`.

If `lambda_min(G_w)>=gamma>0`, then the smallest fixed-depth Wang singular value has the sharp scale

`s_q(A_w) asymp sqrt(M) rho^(q-1)`.

Thus unequal positive diagonal weights are not an independent cancellation resource. They change the effective mass and the normalized sampling measure, but create no new compact singular exponent while all `q` polynomial modes remain stably visible. In particular, if the normalized weighted empirical measures converge weakly to a probability measure whose support contains at least `q` distinct points, the limiting moment Gram is positive definite and the same law eventually applies.

The genuinely new weighted regime starts exactly when the normalized weighted Gram loses an eigenvalue. At that point the deficient polynomial directions must be rescaled at a finer geometric width and their surviving weighted mass tracked. Merely concentrating some individual weights, or making weights highly unequal, is not evidence of extra Wang cancellation if `G_w` stays uniformly nondegenerate.

**Boundary.** This applies to fixed asymptotic depth, compact positive centers, and positive diagonal coefficient metrics. Signed or indefinite weights, non-diagonal coefficient geometry, growing depth, scale escape, infinite-dimensional limits, or source-dependent signed arithmetic estimates are outside the reduction.