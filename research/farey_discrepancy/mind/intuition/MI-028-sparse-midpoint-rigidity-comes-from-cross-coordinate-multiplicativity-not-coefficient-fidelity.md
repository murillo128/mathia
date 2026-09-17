# MI-028 — Sparse midpoint rigidity comes from cross-coordinate multiplicativity, not near-maximal coefficient fidelity

**Evidence level:** exact synthesis from [FD-170](../../findings/FD-170-consecutive-midpoint-history-inverts-the-entire-source.md) through [FD-179](../../findings/FD-179-dyadic-midpoint-null-defects-fit-inside-an-o-first-correction-rank-cap.md).

The midpoint sequence is a changing linear observation of the source. Consecutive horizons invert it exactly, while sparse geometric horizons become target-rigid inside the genuinely multiplicative squarefree source class. FD-175--FD-179 show that this rigidity is not explained by knowing primes, signs, low multiplicative ranks, or even coordinatewise agreement through essentially the entire squarefree-rank range.

For the dyadic ladder, deletion-only sources `a(n) in {0,mu(n)}` can match every sampled midpoint while agreeing with Möbius on all but an exceptionally thin high-rank shell. FD-177 protects every fixed subextremal fraction of the maximal rank scale; FD-178 pushes protection through the leading extremal scale and its first explicit correction.

FD-179 sharpens this to the exact maximal-rank geometry. If

`R(x)=max_(n<=x) omega(n)`

and

`g(x)=(log x)^(2/3)(loglog x)^(-1/3) logloglog x`,

then a permanent exact dyadic-midpoint repair can be arranged so that every sufficiently large squarefree `n` with

`omega(n) <= R(n)-2g(n)`

is untouched. The defect set lies in a rank cap of thickness `(1+o(1))g(n)`, which is `o(log n/(loglog n)^2)`, hence smaller than the first correction scale in the maximal-order expansion. Its counting function remains subpolynomial.

The reusable lesson is stronger than “coordinate depth is not relational rigidity.” **Even correctness up to the exact maximum minus an `o(first-correction)` cap does not recover the cross-coordinate product law.** Rare extremal coordinates can still absorb every sparse observation debt when they remain independently editable. Full multiplicativity prevents that by coupling repair coordinates to earlier prime data; the open structural question is how much weaker a compatibility can already kill the repair freedom.

A prospective information lower bound should therefore price the relation that couples coordinates, not the number or extremal rank of individually correct coefficients. The natural next discriminator is a source law whose violation cannot be confined to a vanishing near-maximal shell, or an observation family whose equations directly test such compatibility.

**Boundary.** FD-179 does not prove full squarefree-rank fidelity, a sharp minimal cap thickness, pairwise sparse inversion, or the Franel--Landau destination estimate. It shows that the remaining coordinatewise escape can be compressed below the first extremal correction scale; what remains missing is genuinely relational source information.