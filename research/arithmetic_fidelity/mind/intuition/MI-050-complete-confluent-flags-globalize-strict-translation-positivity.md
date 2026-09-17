# MI-050 — Complete confluent flags globalize strict translation total positivity

**Evidence level:** exact/classical synthesis from [AF-403](../../findings/AF-403-complete-confluent-flags-globalize-strict-translation-total-positivity.md). The implication is exact for fixed order; the ECT/oscillation mechanism is classical and no novelty claim is made.

For a smooth positive translation profile `f`, local same-point derivative data can be a complete global certificate when the **entire initial confluent flag** is retained. Write

`H_m(t)=(-1)^(m(m-1)/2) det(f^(i+j)(t))_(i,j=0)^(m-1)`.

AF-403 shows that if `H_m(t)>0` for every `t` and every `m<=r`, then the translation kernel `K_f(x,y)=f(x-y)` is strictly totally positive through order `r` for arbitrary strictly ordered source and destination points. The proof passes through extended complete Chebyshev systems: the complete confluent flag gives the one-sided derivative-collocation signs, and the ECT collocation theorem then globalizes them to arbitrary placements.

This changes the locality ledger. For **strict interior** total positivity at fixed order, there is no additional hidden placement/topology datum once the complete flag is positive. Earlier low-order examples in which local analytic signs had to be supplemented by a global connectedness condition belong to the degenerate/nonstrict boundary where some confluent minor can vanish; topology enters through how those zero strata split the domain, not as an independent strict-interior resource.

The reusable rule is therefore to distinguish an incomplete local jet test from a complete confluent flag. Failure of a small stencil or a few low-order conditions does not imply that local analytic data can never globalize. Conversely, an all-order claim requires an unbounded hierarchy of confluent signs; no finite initial flag certifies total positivity of every order.

**Boundary.** AF-403 does not classify what happens when some `H_m` vanishes, does not show that sparse arithmetic sampling can verify the complete flag, and does not give a finite certificate for all-order total positivity. The live arithmetic question is whether the needed flag can be controlled at the physical source scales available to the prime/logarithmic mesh, and which finite global data survive on the nonstrict strata.