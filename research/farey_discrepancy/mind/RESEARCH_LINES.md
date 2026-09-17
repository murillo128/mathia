# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Push quantitative prime-extension rigidity to its real sparsity boundary

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-028-sparse-midpoint-rigidity-comes-from-cross-coordinate-multiplicativity-not-coefficient-fidelity`.

The observation geometry is sharply source-class relative. Complete Farey fields and consecutive midpoint histories are exactly invertible over unrestricted formal sources. Sparse geometric horizons become target-rigid inside the bounded squarefree multiplicative cone, while FD-175--FD-179 construct permanent deletion-only controls that match every dyadic midpoint despite agreeing with Möbius through essentially the whole squarefree-rank range.

FD-180 identified the first quantitative cross-coordinate separator for those deletion-only controls. FD-181 now removes the fragile parts of that statement. For an arbitrary squarefree-supported source `a`, put `delta=a-mu`, let `S` be the support of `delta`, and define the true prime-extension energy

`M_(a,q)(x)=sum_((n,pn) in E_x) |a(pn)-a(p)a(n)|^q`.

If `S(x)=o(x/log x)`, with arbitrary signed amplitudes and even allowing prime coordinates themselves to move, then

`liminf_(x->infinity) (log x/x) M_(a,q)(x) >= sum_(n in S) |delta(n)|^q/n`.

Consequently an `o((log x loglog x)^(-1/q))` normalized finite-`L^q` relation defect still forces `a=mu`. On the bounded subpolynomial fibre with physical primes, the lower bound is an exact first-order asymptotic and recovers FD-180 with the weighted reciprocal perturbation mass in place of deletion count.

The live source question has therefore moved to the actual prime-fan scale. Is `S(x)=o(x/log x)` close to optimal? At support size comparable to `x/log x`, a source has enough changed coordinates in principle to corrupt an entire prime fan. Constructing a dyadic-null control there with subcritical relation energy, or proving that some stronger arithmetic obstruction survives, would identify the true cardinal threshold. Dense but tiny-amplitude perturbations require a weighted replacement for support sparsity and are a separate escape.

More importantly, prime-extension energy is still an added source-faithfulness observable. The Farey program needs a source-native bridge showing that a natural Farey observation family controls a cross-coordinate relation at the required rate. Without such a bridge, FD-180--FD-181 are coercivity results for an augmented source model, not Franel--Landau estimates.

Inside the genuinely multiplicative cone, the finite certification bound for geometric ladders remains quantitatively crude and may admit sharper orbit-hitting estimates. Pairwise sparse inversion also remains distinct from one-target rigidity.

## Apply information budgets only after fixing source class, observation family and destination

The same midpoint coordinate can encode the full source when observed through changing consecutive horizons, become sparse-target-rigid under multiplicativity, and retain a permanent kernel under deletion-only sources that are coordinatewise indistinguishable from Möbius outside an `o(first-correction)` extremal cap. FD-180--FD-181 add that even the phrase “approximately multiplicative” is meaningless without a rate, a relation graph and a source sparsity model: exact dyadic-null sources can have vanishing average prime-extension defect, yet any `o(x/log x)` perturbation support is rigid once the defect beats the explicit `(log x loglog x)^(-1/q)` boundary.

Any lower bound should first declare whether it concerns unrestricted recovery, one-target testing, pairwise recovery or quotient recovery; whether changing horizon counts as a new operator; the source class and its cross-coordinate laws; the relation graph and normalization; and the observation/noise topology. Only then do rank, sample count, inverse modulus or information capacity become meaningful currencies.

## Keep source coercivity and the Franel--Landau destination separate

The results above concern recovery or non-rigidity of the coefficient source. They do not prove the RH-critical discrepancy estimate. Even a source condition that kills every sparse midpoint repair must still be shown to control the nonlocal Franel--Landau norm with the required scale and conditioning. Conversely, failure of coordinatewise sparse rigidity does not by itself rule out a destination theorem that uses a genuinely different source-native relation.