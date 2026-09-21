# MI-052 — Restricted inverse conditioning counts only after global extension

**Evidence level:** exact response-space synthesis from [FD-255](../../findings/FD-255-global-mobius-rows-collapse-exact-omission-reachability.md), reconciling the restricted incidence-conditioning branch FD-248--FD-254 with the global Möbius envelope from FD-244.

A large inverse norm on the active-support or companion subsystem is not the inverse norm of the full exact-omission problem. FD-249--FD-254 correctly show that restricted divisor-incidence matrices can have polynomially bad directions, but FD-255 proves that those directions need not extend to coefficient data satisfying the global envelope `|b_n|<=C_b n` on every divisor row.

For an exact omission response with `K` omitted locations, let `g=mu*b=Delta Y` and `D=supp(g)`. Then `|D|<=2K`, and every active coordinate obeys the global Möbius-row constraint

`|g(d)|/d <= C_b sigma_{-1}(d)`.

Combining this with the sparse reciprocal-divisor estimate already proved in FD-244 gives, with `eta=min(1,2K/H)` and `Phi(eta)=eta log(e+log(1/eta))`,

`sum_(d in D) |g(d)|/d << C_b H Phi(eta)`

and hence

`sum_(n<=H) |b_n| << C_b H^2 Phi(eta)`.

Therefore every sublinear exact-omission family `K=o(H)` has vanishing normalized coefficient mass at the macroscopic `H^2` scale. In the polynomial regime `K=H^(alpha+o(1))`, every `alpha<1` is response-side coercive up to the sparse double-log factor. This strictly dominates the earlier companion-only exponent windows.

The mechanism is an **extension constraint**. The active or companion subsystem permits arbitrary bounded row data that maximize its inverse norm, but an actual exact-omission sequence must simultaneously satisfy all omitted divisor rows. Those extra rows remove the polynomial extremizers: FD-255 even exhibits the finite parity companion extremizer from FD-254 violating a discarded start-side coefficient bound.

The reusable distinction is between an ambient/restricted inverse norm and the norm on the **globally extendable image**. A bad singular direction is evidence only after it is shown to extend through every source-side row constraint that the original problem imposes.

**Boundary.** FD-255 is a signed response-space theorem. It does not impose source positivity, finite prime-reservoir capacity, squarefree realization or other physical arithmetic admissibility, and it does not prove the double-log upper factor is sharp for the fully realizable map. The exact-zero sublinear response branch is closed; positive-density omissions and source-side realization remain separate questions.