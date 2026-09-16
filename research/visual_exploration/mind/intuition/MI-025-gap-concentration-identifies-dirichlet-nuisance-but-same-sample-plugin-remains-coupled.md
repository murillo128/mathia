# MI-025 — The log-product quotient has one global exact Gibbs communication class; quantitative calibration is the remaining gate

**Evidence level:** exact symmetric-Dirichlet nuisance analysis from [VIS-244](../../findings/VIS-244-empirical-gap-concentration-identifies-dirichlet-alpha.md), [VIS-245](../../findings/VIS-245-gap-concentration-tent-covariance-beta-moments.md), [VIS-246](../../findings/VIS-246-concentration-conditioning-retains-dirichlet-alpha.md), sharpened by the exact coarea disintegration/nondegeneracy witness [VIS-247](../../findings/VIS-247-log-product-conditioning-alpha-free-coarea-law.md), the exact three-gap audit law [VIS-248](../../findings/VIS-248-three-gap-log-product-discriminant-audit.md), the reversible block-kernel/tangent-spanning result [VIS-249](../../findings/VIS-249-three-coordinate-log-product-gibbs-kernel.md), and the global accessibility/irreducibility theorem [VIS-250](../../findings/VIS-250-triple-gibbs-global-accessibility.md).

For symmetric cyclic Dirichlet gaps, the concentration statistic `C=m sum_i X_i^2-1` identifies the nuisance parameter `alpha`, but VIS-246 proves that conditioning on `C` does not eliminate it for `m>=3`: the conditional slice density still carries `(prod_i X_i)^(alpha-1)`. Identification and elimination are different operations.

The exact sufficient coordinate is

`Lambda(X)=sum_i log X_i=log(prod_i X_i)`.

VIS-247 makes the resulting regular conditional law explicit. On a level `Lambda=lambda<-m log m`, let

`J(x)^2=sum_i x_i^(-2)-(1/m)(sum_i x_i^(-1))^2`.

Then

`P_alpha(dx | Lambda=lambda)=Z(lambda)^(-1) J(x)^(-1) d sigma_lambda(x)`.

The exponential-family factor `exp((alpha-1)lambda)` is constant on the level and cancels under normalization, so the conditional surface law is exactly independent of `alpha`. VIS-247 also gives an exact same-product pair with different `bar T`, so this nuisance quotient does not structurally force the tent statistic to collapse.

VIS-248 turns the `m=3` quotient into a complete one-dimensional audit law. For `P=X_1X_2X_3=p` and `Q=X_1X_2+X_2X_3+X_3X_1`, the unordered triple is recovered from `t^3-t^2+Qt-p`, while

`f(q | p)=Z(p)^(-1) Delta_p(q)^(-1/2)`

on the discriminant interval. The cosine parametrization removes the endpoint singularities, giving deterministic quadrature and an exact full-distribution benchmark.

VIS-249 removes the local sampler gap. Conditioning on all coordinates outside any triple fixes that block's sum and product; after normalizing by its sum, its full conditional is exactly the VIS-248 law. A random-scan heat bath that chooses triples with fixed state-independent positive probabilities and resamples from this conditional is reversible and invariant for the full `Lambda=lambda` target. At every regular point its three-coordinate sum/product-preserving tangent directions span the entire `(m-2)`-dimensional conditioned tangent space.

VIS-250 upgrades that local statement to a global one. The regular level

`S_lambda={x_i>0: sum_i x_i=1, sum_i log x_i=lambda}`

is the boundary of a compact convex superlevel set around the barycenter and is homeomorphic to `S^(m-2)`, hence connected. The triple-fiber vector fields span the tangent space everywhere, so their local accessibility classes are open; connectedness forces one global deterministic accessibility class. Because every exact block conditional has positive density on every regular fiber arc, the random-scan heat-bath chain is `mu_lambda`-irreducible. There is therefore **no hidden disconnected component or communication-class obstruction** in the exact mathematical kernel.

What remains is strictly quantitative/computational: conductance, spectral gap or another useful mixing bound; metastable bottlenecks; numerical realization of the one-dimensional conditionals; and Monte Carlo error at the actual frozen `m,lambda`. Irreducibility can coexist with impractically slow mixing. Reproducing the VIS-248 law is still a necessary implementation audit, but the next structural question is no longer whether the chain can reach the full conditioned surface—it can.

Only after separated initial states give quantitatively consistent samples and total numerical/Monte Carlo error is below the predeclared residual scale can `bar T` be compared with the prime configuration. A residual then remains a point-process statement, not an RH mechanism; it must still translate through the signed prime-phase kernel and survive the earlier representation/amplitude controls.

**Boundary.** VIS-247--VIS-250 apply to the one-parameter symmetric Dirichlet family, regular levels `lambda<-m log m`, exact block conditionals, and fixed state-independent positive triple-selection probabilities. VIS-250 proves irreducibility, not a spectral gap, geometric ergodicity, practical burn-in, or correctness of a floating-point implementation. It also does not establish that the symmetric-Dirichlet family is the final prime-gap null or that any surviving residual controls RH.
