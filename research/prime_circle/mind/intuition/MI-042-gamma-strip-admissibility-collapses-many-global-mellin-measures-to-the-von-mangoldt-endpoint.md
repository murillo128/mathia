# MI-042 — Gamma-strip admissibility collapses many global Mellin selectors to the von Mangoldt endpoint

**Evidence level:** exact synthesis from [PC-335](../../findings/PC-335-bounded-indefinite-mellin-symbols-cannot-separate-prime-powers.md) through [PC-340](../../findings/PC-340-finite-order-global-mellin-distributions-collapse-at-critical-gamma-strip.md). The Fourier--Laplace, Blaschke and finite-order distribution mechanisms are classical; the Mathia content is their interaction with the prime-circle shell factorization and semiprime-null constraints.

PC-338 classified compactly supported distributions in Mellin frequency, and PC-339 showed that compact support was not essential for finite global measures. The native `Gamma` factor supplies a horizontal strip of half-width `pi/2`; semiprime nulls turn every prime logarithm into a zero, and after conformal transport those zeros violate the Blaschke condition because `sum_p 1/p` diverges. A bounded strip function carrying them must vanish.

PC-340 shows that **finite distributional order is not an escape either**. Let

`T=sum_(j=0)^N D^j mu_j`

with finite complex measures `mu_j`, and assume the shell-weighted derivatives satisfy the critical Gamma-strip exponential integrability required in PC-340. Multiplying `T` by a prime shell and taking its Fourier--Laplace transform now introduces only a fixed polynomial factor in the transform variable. It does not narrow the `pi/2` strip.

That distinction is decisive. A zero-free power of `2 cosh(z/2)` absorbs any fixed polynomial growth while preserving the full strip, so the same prime-log non-Blaschke uniqueness argument applies. Exact mixed-semiprime nulls therefore force

- off the endpoint line `sigma!=1`, zero visible shell response on every `n>1`;
- on `sigma=1`, the selector itself to be `T=c delta_0`, hence `L_T(n)=c Lambda(n)`.

The endpoint conclusion is stronger than merely classifying the visible response. Derivatives of the endpoint delta, derivatives of globally supported measures, Schwartz/Gaussian-type derivative measures and other fixed finite-order singular corrections satisfying the strip hypothesis do not leave an invisible extra selector behind; the two prime shells `p=2,3` eliminate it.

The reusable boundary is therefore **analytic growth on the native strip**, not compactness, global support or finite distributional order. Compactly supported selectors, finite global measures and a broad class of non-measure finite-order distributions all collapse for the same reason: their shell-weighted Fourier--Laplace transforms retain enough control on the entire Gamma strip for the prime-log zero set to become a uniqueness set.

A genuine scalar Mellin escape must now violate that analytic class in a load-bearing way: for example an analytic functional or distribution whose shell-weighted transform loses polynomial control on the full strip, a shell-dependent symbol/order, a nonlinear or matrix-valued operation, or cross-shell coupling before scalar evaluation. Merely saying “noncompact” or “distributional” is no longer a distinct mechanism.

**Boundary.** PC-340 does not classify arbitrary infinite-order analytic functionals, tails that destroy full-strip control, nonlinear/matrix-valued selectors or genuinely cross-shell operators. Nor does the endpoint von Mangoldt channel provide a zero-sensitive destination theorem. Escaping the Gamma-strip uniqueness class is only a representation escape; any surviving proposal must still explain why its retained source information constrains the Riemann divisor rather than merely decoding prime-power support.