# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Push quantitative prime-extension rigidity beyond deletion-only sources

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-028-sparse-midpoint-rigidity-comes-from-cross-coordinate-multiplicativity-not-coefficient-fidelity`.

The observation geometry is sharply source-class relative. Complete Farey fields and consecutive midpoint histories are exactly invertible over unrestricted formal sources. Sparse geometric horizons become target-rigid inside the bounded squarefree multiplicative cone, while FD-175--FD-179 construct permanent deletion-only controls that match every dyadic midpoint despite agreeing with Möbius through essentially the whole squarefree-rank range.

FD-180 now turns the previously qualitative missing relation into an exact rate threshold for that deletion-only class. If the deleted set `S` is subpolynomial and primes remain physical, its prime-extension defect boundary satisfies

`B_a(x)=(C_S+o(1))x/log x`,  `C_S=sum_(n in S)1/n`.

Normalized over all squarefree prime-extension edges, the finite-`L^q` multiplicativity defect is therefore

`((zeta(2)C_S+o(1))/(log x loglog x))^(1/q)`.

Hence an `o((log x loglog x)^(-1/q))` relation defect forces `S` empty, whereas merely requiring average multiplicativity to vanish still permits the exact dyadic-null control. The line has therefore found a weaker-than-full-multiplicativity separator, but only in a narrow source fibre.

The live source question is to preserve this quantitative boundary principle under a broader admissible class: signed perturbations, compensating edits, or sources whose prime coordinates are not fixed can cancel or relocate the simple edge defect. A useful next relation should still force every sparse midpoint repair to expose a non-negligible relational boundary for an arithmetic reason, not merely because deletion-only errors cannot cancel.

Inside the genuinely multiplicative cone, the finite certification bound for geometric ladders remains quantitatively crude and may admit sharper orbit-hitting estimates. Pairwise sparse inversion also remains distinct from one-target rigidity.

## Apply information budgets only after fixing source class, observation family and destination

The same midpoint coordinate can encode the full source when observed through changing consecutive horizons, become sparse-target-rigid under multiplicativity, and retain a permanent kernel under deletion-only sources that are coordinatewise indistinguishable from Möbius outside an `o(first-correction)` extremal cap. FD-180 adds that even the phrase “approximately multiplicative” is meaningless without a rate and a relation graph: the dyadic-null source has vanishing average prime-extension defect, but exactly at the non-rigid boundary scale.

Any lower bound should first declare whether it concerns unrestricted recovery, one-target testing, pairwise recovery or quotient recovery; whether changing horizon counts as a new operator; the source class and its cross-coordinate laws; the relation graph and normalization; and the observation/noise topology. Only then do rank, sample count, inverse modulus or information capacity become meaningful currencies.

## Keep source coercivity and the Franel--Landau destination separate

The results above concern recovery or non-rigidity of the coefficient source. They do not prove the RH-critical discrepancy estimate. Even a source condition that kills every sparse midpoint repair must still be shown to control the nonlocal Franel--Landau norm with the required scale and conditioning. Conversely, failure of coordinatewise sparse rigidity does not by itself rule out a destination theorem that uses a genuinely different source-native relation.