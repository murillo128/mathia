# MI-040 — Finite point-supported Mellin singularities collapse to the von Mangoldt endpoint

**Evidence level:** exact synthesis from PC-179, PC-335, [PC-336](../../findings/PC-336-endpoint-mellin-distributions-are-generalized-von-mangoldt-jets.md), and [PC-337](../../findings/PC-337-finite-point-mellin-selectors-collapse-to-von-mangoldt-endpoint.md), together with classical point-support and exponential-polynomial facts. No new zero theorem is claimed.

The singular endpoint `s=1` is not an unlimited escape from the bounded Mellin no-go, and PC-337 shows that moving to finitely many nonendpoint singular frequencies does not help either.

For the exact prime-circle radial flux, every finite Taylor jet at `s=1` is related by an invertible universal lower-triangular transformation to the generalized von Mangoldt hierarchy `Lambda_1,...,Lambda_(K+1)`. The vanishing order `ord_(s=1) R_n(s)=omega(n)-1` therefore exposes successive almost-prime strata, but only through a classical arithmetic jet.

Now let `T` be any finite point-supported distribution on one fixed Mellin line `Re(s)=sigma>0`, and let `L_T(n)` be its shell response. If

`L_T(pq)=0`

for every pair of distinct primes, then PC-337 gives the complete finite-point classification:

- for `sigma!=1`, `L_T(n)=0` for every shell `n>1`;
- for `sigma=1`, `L_T(n)=c Lambda(n)` for one constant `c`.

The nonendpoint mechanism is rigid. Because the radical factor satisfies `A_(pq)=A_p A_q`, fixing one prime and varying the other turns the response into a finite exponential polynomial in `x=log q`. Such a nonzero function has only `O(R)` zeros in a disk of radius `R`, while prime logarithms contribute exponentially many candidate zeros in that coordinate. Hence every nonendpoint component that survives multiplication by the universal zeta envelope must vanish; components killed by the envelope are invisible to all shells anyway. At the endpoint, semiprime nulling eliminates every generalized von Mangoldt jet except `Lambda_1=Lambda`.

This makes the finite singular boundary sharper than “endpoint jets are classical.” **Every finite point-supported semiprime-null Mellin selector is either shell-invisible or the original von Mangoldt endpoint channel.** Adding finitely many deltas, delta derivatives, nonendpoint frequencies or support at zeta zeros cannot create a new exact prime-power selector.

**Boundary.** The classification does not cover infinite or continuous Mellin support, generalized analytic functionals beyond ordinary finite point-supported distributions, shell-dependent singular symbols/order, nonlinear radial constructions, or genuinely cross-shell coupling before scalarization. Leaving the finite-point class is only an architectural escape from this no-go; it still supplies no functional equation, critical-line positivity or zero-sensitive destination theorem.