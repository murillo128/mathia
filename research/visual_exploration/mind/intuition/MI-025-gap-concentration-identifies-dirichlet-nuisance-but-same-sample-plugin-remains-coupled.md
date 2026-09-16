# MI-025 — The log-product quotient has an exact three-coordinate Gibbs kernel, but global calibration remains a separate gate

**Evidence level:** exact symmetric-Dirichlet nuisance analysis from [VIS-244](../../findings/VIS-244-empirical-gap-concentration-identifies-dirichlet-alpha.md), [VIS-245](../../findings/VIS-245-gap-concentration-tent-covariance-beta-moments.md), [VIS-246](../../findings/VIS-246-concentration-conditioning-retains-dirichlet-alpha.md), sharpened by the exact coarea disintegration/nondegeneracy witness [VIS-247](../../findings/VIS-247-log-product-conditioning-alpha-free-coarea-law.md), the exact three-gap audit law [VIS-248](../../findings/VIS-248-three-gap-log-product-discriminant-audit.md), and the reversible block-kernel/tangent-spanning result [VIS-249](../../findings/VIS-249-three-coordinate-log-product-gibbs-kernel.md).

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

VIS-249 removes the remaining *structural* sampler gap. Conditioning on all coordinates outside any triple fixes that block's sum and product; after normalizing by its sum, its full conditional is exactly the VIS-248 law. Therefore a random-scan heat-bath that chooses triples with fixed state-independent positive probabilities and resamples from this conditional is reversible and invariant for the full `Lambda=lambda` target.

The same finding proves that these three-coordinate moves have full local directional rank. At every regular point, choosing `a,b` with `1/x_a != 1/x_b` yields `m-2` linearly independent tangent vectors supported on `{a,b,k}` that satisfy both linearized constraints. Thus the admissible block directions span the entire tangent space of the conditioned surface. The candidate kernel is therefore neither missing an exact conditional distribution nor trapped by an infinitesimal rank defect.

What remains is genuinely global/computational rather than another local representation problem: global irreducibility, Harris recurrence, spectral gap or useful mixing time, numerical realization of the one-dimensional conditionals, and error control at the actual frozen `m,lambda`. Reproducing the VIS-248 law is a necessary implementation audit, not evidence that a long high-dimensional chain has converged. Only after stationarity/mixing from separated starts and numerical uncertainty are controlled below the residual scale can the predeclared `bar T` comparison test whether a prime-specific residual survives.

**Boundary.** The exact quotient and Gibbs construction apply to the one-parameter symmetric Dirichlet family and regular log-product levels. Full tangent spanning is local, not global ergodicity. None of VIS-247--VIS-249 establishes fidelity of the Dirichlet family as a final prime-gap null, a prime residual, or an RH mechanism. A surviving residual would still need an independent bridge back to the signed prime-phase destination.
