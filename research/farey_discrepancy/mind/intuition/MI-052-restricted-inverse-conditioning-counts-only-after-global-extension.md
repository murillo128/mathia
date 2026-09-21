# MI-052 — Restricted inverse conditioning counts only after global extension

**Evidence level:** exact response-space synthesis from [FD-255](../../findings/FD-255-global-mobius-rows-collapse-exact-omission-reachability.md) and [FD-256](../../findings/FD-256-linear-density-exact-omissions-can-saturate-signed-capacity.md), reconciling the restricted incidence-conditioning branch FD-248--FD-254 with the global Möbius envelope from FD-244.

A large inverse norm on the active-support or companion subsystem is not the inverse norm of the full exact-omission problem. FD-249--FD-254 correctly show that restricted divisor-incidence matrices can have polynomially bad directions, but FD-255 proves that those directions need not extend to coefficient data satisfying the global envelope `|b_n|<=C_b n` on every divisor row.

For an exact omission response with `K` omitted locations, let `g=mu*b=Delta Y` and `D=supp(g)`. Then `|D|<=2K`, and every active coordinate obeys the global Möbius-row constraint

`|g(d)|/d <= C_b sigma_{-1}(d)`.

Combining this with the sparse reciprocal-divisor estimate of FD-244 gives, with `eta=min(1,2K/H)` and `Phi(eta)=eta log(e+log(1/eta))`,

`sum_(d in D) |g(d)|/d << C_b H Phi(eta)`

and hence

`sum_(n<=H) |b_n| << C_b H^2 Phi(eta)`.

Therefore every sublinear exact-omission family `K=o(H)` has vanishing normalized coefficient mass at the macroscopic `H^2` scale. In the polynomial regime `K=H^(alpha+o(1))`, every `alpha<1` is response-side coercive up to the sparse double-log factor. This strictly dominates the earlier companion-only exponent windows.

FD-256 shows that the extension gate is sharp rather than merely destructive. At linear omission density, choose disjoint adjacent response spikes entirely above `H/2`. The active divisors then have no second multiple below the horizon, so the full extension becomes diagonal and exact: each omitted point produces the globally valid pair `b_e=e`, `b_(e+1)=-e`. At `K=H/4` these pairs asymptotically fill the entire top-band coefficient capacity.

The reusable distinction is therefore between an ambient/restricted inverse norm and the norm on the **globally extendable image**. Bad restricted singular directions count only after extension is checked; conversely, once the geometry enters a region where the full map itself becomes locally diagonal, macroscopic extendable directions can reappear without any large restricted inverse norm.

**Boundary.** FD-255--FD-256 are signed response-space results. They pin the macroscopic omission threshold at the density scale but do not impose source positivity, finite prime-reservoir capacity, squarefree realization or other physical arithmetic admissibility. Below linear density, the exact sharpness of the double-log factor remains open; on the physical source side, FD-257 supplies a separate quantitative positivity obstruction.