# MI-050 — Fixed Euler windows have factorial stable rank on selector shells

**Evidence level:** exact conditioning synthesis from [RE-190](../../findings/RE-190-shrinking-euler-sampling-windows-collapse-to-reciprocal-mass-rank-one.md) and [RE-191](../../findings/RE-191-fixed-euler-temperature-windows-are-factorially-compressible.md). The finite Laplace approximation mechanism is classical; the Mathia content is its uniform reduction from the exact Euler-factor channel on a multiplicative selector shell.

Let a signed ordinary-prime packet be supported on `Ap<=q<=Bp`, and sample the exact Euler discrepancy throughout a fixed one-sided interval `s=1+u`, `0<=u<=U`. After multiplying by `p^u`, the source channel is uniformly

`sum_q (c_q/q) exp(-u log(q/p)) + O_A(p^-1 ||c||_(p,1))`.

The logarithmic source coordinate `alpha=log(q/p)` lies in a fixed compact interval. Taylor separation of `exp(-u alpha)` therefore gives a rank-`m` approximation with error

`e^(UM) (UM)^m/m! + O_A(p^-1)`.

Thus a fixed constant-distance spectral interval escapes the rank-one collapse of RE-190 but not by acquiring robust continuum-dimensional source information. Its approximation numbers decay at least factorially, and at fixed source-scale tolerance the stable rank is bounded independently of both `p` and the number of selector-shell primes. To accuracy `epsilon` above the `p^-1` floor, only about `log(1/epsilon)/loglog(1/epsilon)` reciprocal log-location moments are needed.

This cleanly separates **exact source identification from stable source information**. A whole exact interval determines a finite Euler packet by analyticity, but recovering the higher source coordinates requires resolving factorially small residuals. Dense exact samples are therefore not equivalent to many usable coordinates unless the arithmetic theorem controls them at the required precision.

RE-190 is the `U=o(1)`, rank-one endpoint of the same geometry. The available escapes are correspondingly structural rather than denser sampling: let the spectral span `U` grow, enlarge the logarithmic source diameter by coupling separated prime scales, prove source-native precision down to the factorial tail, or introduce a joint/nonlocal invariant tied more directly to the Robin destination.

**Boundary.** The factorial estimate is an upper bound on stable rank, not a matching asymptotic for singular values. The null directions used in the rank argument are relaxed real signed coefficient directions, not necessarily honest `{0,1,2}` multiplicity controls. Exact analyticity remains fully rigid, and neither growing spectral windows nor multiscale source support is covered by the fixed-rectangle theorem.