# MI-056 — Colliding Wang centers matter only when the pooled rescaled Gram degenerates

**Evidence level:** exact fixed-depth sampling synthesis from [VIS-360](../../findings/VIS-360-pooled-rescaling-colliding-center-floor.md), extending the one-cluster and separated-multicluster laws in VIS-358--VIS-359.

Put a compact Wang bank into its outer collision coordinate `x_j=c+rho t_j`, with fixed asymptotic depth `q`, bounded normalized locations `|t_j|<=T`, and the current unweighted Euclidean coefficient norm. Let `S` be the polynomial sampling matrix with columns `1,t,...,t^(q-1)`. If

`lambda_min((1/N) S^*S) >= gamma > 0`,

then the smallest fixed-depth Wang singular value has the exact scale

`s_q(A) asymp sqrt(N) rho^(q-1)`.

The proof uses one Taylor block at the outer scale. Once all points are written in the same normalized coordinate, the decomposition into nominal subclusters disappears; the pooled moment Gram is the only remaining fixed-depth geometry. In particular, if the empirical normalized cloud converges to a measure whose support contains at least `q` distinct points, its degree-`q-1` moment Gram is positive definite and the same law follows eventually.

Hence shrinking separation between cluster centers is not itself a new conditioning resource. If the pooled outer-scale Gram remains nondegenerate, colliding centers reduce to the ordinary one-cluster occupancy-width law already priced by `sqrt(N) rho^(q-1)`. A genuinely new compact regime begins only when the pooled Gram loses an eigenvalue after the correct rescaling.

That failure specifies the next object rather than a generic “multicluster” loophole: rescale the deficient polynomial directions at finer widths and track the occupancies or weights that survive there. A hierarchical escape must exhibit degeneration at successive normalized sampling scales; merely exhibiting small pairwise center separation or bad square minors does not establish it.

**Boundary.** VIS-360 is fixed-depth, compact, unweighted and Euclidean. It does not classify a hierarchy of degenerating pooled Grams, nonuniform column weights, changing coefficient norms, growing `q`, scale escape or infinite-dimensional topologies.