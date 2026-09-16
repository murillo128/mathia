# MI-038 — High-temperature Euler rigidity is exact but exponentially conditioned

**Evidence level:** exact synthesis from [RE-173](../../findings/RE-173-infinite-prime-supported-exact-mertens-compensation-survives-kv-fidelity.md) and [RE-174](../../findings/RE-174-unbounded-euler-temperature-samples-restore-infinite-prime-source-rigidity.md), using classical uniqueness of absolutely convergent Dirichlet series.

RE-173 shows that one exact Mertens boundary charge plus ordinary-prime support, bounded integer multiplicity and arbitrarily strong fixed KV fidelity leaves a noncompact null direction: an infinite delete/duplicate tail can repay the global debt after producing an order-one transient Robin excursion.

RE-174 shows that this ambiguity disappears completely if the observation family is strengthened from one boundary charge to an unbounded sequence of exact Euler temperatures. For multiplicity defects `c_p=m_p-1`,

`D_Q(sigma)=log Z_Q(sigma)-log zeta(sigma)`

is an absolutely convergent Dirichlet series whose prime-power coefficients are `c_p/k`. Equality `D_Q(sigma_j)=0` on any sequence `sigma_j->infinity` therefore forces every coefficient, hence every `c_p`, to vanish.

The direct asymptotic makes the mechanism and its cost sharper. If `P` is the smallest modified prime, then

`D_Q(sigma)=c_P P^(-sigma)(1+o(1))`.

High temperature triangularizes the infinite source from the **smallest** defect outward. This is the infinite-support dual of RE-172, where a finite perturbation is triangularized from the largest changed prime by unique factorization.

Exact source identification is therefore not the missing theorem. The high-temperature germ already identifies the complete bounded-multiplicity prime source. What is missing is a **well-conditioned selector-sensitive invariant**: detecting a defect near prime `P` at temperature `sigma` requires resolving a signal of size `P^(-sigma)`, exponentially smaller than the Robin-scale displacement one wants to control.

The next useful falsification target lies between the two extremes. Test whether finitely many fixed Euler temperatures, or another economically conditioned finite family of Euler summaries, can still be matched by a KV-faithful infinite delete/duplicate control. If they can, exact analytic identifiability should not be mistaken for robust selector control.

**Boundary.** RE-174 is a source-identification theorem entirely in `Re s>1`; it does not estimate the Robin functional, improve prime-distribution bounds or imply RH. Its exact rigidity depends on an unbounded observation hierarchy, while its first-defect asymptotics explicitly warn that approximate recovery is badly conditioned.