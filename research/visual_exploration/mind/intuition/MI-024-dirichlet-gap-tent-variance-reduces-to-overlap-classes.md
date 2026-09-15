# MI-024 — Dirichlet-gap tent variance reduces exactly to cyclic overlap classes

**Evidence level:** exact-derived calibration from [VIS-242](../../findings/VIS-242-dirichlet-gap-tent-variance-overlap-classes.md), building on the fixed-count Dirichlet null of VIS-240 and endpoint-phase quotient of VIS-241.

Normalize the circle to length `1`, let cyclic gaps `X` have the symmetric `Dirichlet(alpha,...,alpha)` law, and let `S_(i,r)` be the mass of the oriented arc of `r` consecutive gaps starting at `i`. For the cut-averaged tent statistic,

`bar T = (1/2) sum_(i,r) q_u(S_(i,r))`,

where `q_u` is the complement-symmetric piecewise quadratic pair kernel.

For two oriented arcs of lengths `r,s`, their joint law depends only on the overlap size `k`. Partitioning the gaps into intersection, first-only, second-only and remainder gives at most four aggregated masses with Dirichlet parameters

`(k alpha,(r-k)alpha,(s-k)alpha,(m-r-s+k)alpha)`.

Therefore every covariance term is one low-dimensional expectation `M_(r,s,k)`, and cyclic stationarity gives the exact finite formula

`Var_G(bar T) = (m/4) sum_(r,s,d) [M_(r,s,k_(r,s)(d))-mu_r mu_s]`.

The dimensionality of the probability integral does not grow with the number of points. The only `m`-dependence outside the Dirichlet parameters is deterministic cyclic-overlap combinatorics. Because `q_u` is piecewise quadratic, the expectations reduce to truncated Dirichlet polynomial moments; Monte Carlo is not mathematically required.

At `alpha=1`, rotated symmetric Dirichlet gaps are exactly spacings of `m` iid uniform circle points. Translation invariance makes pair terms sharing one endpoint uncorrelated, so the U-statistic variance collapses to

`Var(bar T)=binom(m,2)[2u/3-4u^2/3+11u^3/15-u^4/9]`.

This is a mandatory audit identity for any implementation of the general overlap formula.

The substantive consequence is that the representation-matched dependence null no longer has an unresolved variance obstacle. Once `alpha` and endpoint semantics are fixed independently, the tent statistic has an exact calibration. Any subsequent prime residual is therefore a separate empirical/source question rather than an artifact of uncomputed null covariance.

**Boundary.** The Dirichlet family is a chosen dependence control, not a theorem about prime gaps. A residual against it is only a point-process statement until it survives stronger predeclared controls and is translated through the signed prime-phase kernel. Fitting `alpha` on the same confirmation statistic destroys the intended test.