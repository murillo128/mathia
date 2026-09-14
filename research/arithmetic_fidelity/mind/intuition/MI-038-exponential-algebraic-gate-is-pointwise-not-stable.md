# MI-038 — Exponential-algebraic incidence is a pointwise gate, not a stability margin

**Evidence level:** exact consequence of [AF-330](../../findings/AF-330-exact-prime-algebraic-incidence-forces-exponentially-algebraic-time.md) and [AF-331](../../findings/AF-331-exponential-algebraic-exceptional-time-gate-is-countable-dense.md). No exact eight-prime incidence or non-incidence theorem is claimed.

AF-330 turns an exact middle-singular hit into an arithmetic restriction on the **common exponent parameter**: if the prime-phase orbit reaches any proper algebraic target then `-it` must lie in `ecl_C(empty)`. This is exponential algebraicity of the parameter, not algebraicity of `e^{it}` or of the individual phase coordinates.

That exceptional class is thin but not locally separating. AF-331 proves that the real set `E_R={t:-it in ecl_C(empty)}` is countable and dense; it contains `2*pi*Q`, while its complement is also dense, has full Lebesgue measure and is comeager.

Therefore the gate has **no positive geometric margin**. Its distance from every real time is zero, no open time interval avoids it, and arbitrarily small near-hit windows can contain both exponentially algebraic and exponentially transcendental parameters. Measure-zero or genericity language cannot be converted into a neighborhood exclusion for the exact common-zero problem.

The reusable distinction is between a **pointwise arithmetic restriction** and a **stable discriminant**. AF-325--AF-327 provide finite-height quantitative separation from rank-loss boundaries; AF-330--AF-331 instead isolate an exact exceptional class whose topology gives no quantitative help. These are different currencies and cannot be substituted for one another.

The live theorem must use internal arithmetic of an exponentially algebraic pure-imaginary parameter together with the prime logarithms, or another exact invariant of the common-zero equations. A proof that merely shows the exceptional set is small, nongeneric, or approximated poorly at finite precision cannot decide incidence.

**Boundary.** AF-331 does not show that the prime-log orbit ever hits the exceptional locus at the required algebraic variety, nor that it never does. Countable density is a statement about the ambient parameter set, not about the simultaneous equations defining the eight-prime target.
