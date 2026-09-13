# MI-029 — Prime phase character rank exhausts the small-polygon obstruction at the pentagon

**Evidence level:** proved for common-time phases of distinct rational primes through AF-310. Exact prime-support zero incidence remains open for saturated supports of size `k>=5`.

For distinct primes `p_1,...,p_k` at a common nonzero time, normalize by the last phase and write `u_j=(p_j/p_k)^(-it)`. The integer character-relation lattice

`L_(p,t)={a in Z^(k-1): product_j u_j^(a_j)=1}`

injects into `Z` by its winding number. Prime-log rational independence makes the winding map injective, so `L_(p,t)` is cyclic and has rank at most one. This bound is sharp: choosing the time can force one prescribed nontrivial character relation, but two independent relations cannot coexist.

That rank bound exactly explains the small-support exclusions. Every normalized three-phase zero is an equilateral triangle and forces two independent torsion relations; every normalized four-phase zero splits into two antipodal pairs and again forces relation rank at least two. Hence the same character theorem excludes exact prime hits for `k=3,4`.

The mechanism reaches its natural boundary at `k=5`. The normalized equilateral-pentagon zero locus is a connected genus-four surface, and the subset on which two independent integer characters vanish is meagre. A dense residual set of pentagon zero configurations therefore has relation rank at most one, exactly the range permitted by the prime orbit. The prime phase point also cannot lie in any torsion coset of codimension at least two, so a hypothetical `k>=5` hit must be genuinely nontorsion.

The next exact-incidence theorem must therefore use arithmetic finer than monomial/torsion rank: the special placement of the prime-log direction inside the nontorsion polygon-zero cone. Adding more generic topology, density, root-of-unity comparison, or integer-character constraints cannot by itself recover the `k=3,4` contradiction.

**Boundary.** Compatibility is not existence. The residual pentagon statement concerns the ambient zero manifold and supplies no prime-support hit, measure lower bound, Diophantine rate, or RH implication. The cyclic character bound also allows one exact relation, so rank zero is false without an additional restriction on the time.