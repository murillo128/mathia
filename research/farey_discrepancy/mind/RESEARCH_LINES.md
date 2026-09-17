# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Find the cross-coordinate constraint that sparse midpoint repair cannot fake

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-028-sparse-midpoint-rigidity-comes-from-cross-coordinate-multiplicativity-not-coefficient-fidelity`.

The observation geometry is sharply source-class relative. Complete Farey fields and consecutive midpoint histories are exactly invertible over unrestricted formal sources. Inside the bounded squarefree multiplicative cone, sparse geometric midpoint ladders can already be target-rigid because prime-power orbit hitting propagates through the product law.

FD-175--FD-179 locate the opposite boundary. Once full multiplicativity is removed, permanent deletion-only controls can match every dyadic midpoint while retaining correct prime data, signs and almost the entire squarefree-rank hierarchy. FD-179 now pushes the protected region to

`omega(n) <= R(n)-2g(n)`,

where `R(n)` is the exact maximal squarefree rank below `n` and `g(n)=(log n)^(2/3)(loglog n)^(-1/3) logloglog n`. The remaining repair coordinates lie in a cap whose thickness is `o(log n/(loglog n)^2)`, below the first extremal correction scale, while the defect population is still subpolynomial.

Thus the live source-restriction question is no longer whether enough individually named coefficients are correct, even at near-maximal rank. The missing discriminator must be **relational**: a compatibility coupling the protected coordinates to the vanishing extremal repair shell strongly enough that those shell edits cannot be chosen independently. Full multiplicativity is one such coupling; the open problem is whether a substantially weaker source-native relation already suffices.

Inside the genuinely multiplicative cone, the finite certification bound for geometric ladders remains quantitatively crude and may admit sharper orbit-hitting estimates. Pairwise sparse inversion also remains distinct from one-target rigidity.

## Apply information budgets only after fixing source class, observation family and destination

The same midpoint coordinate can encode the full source when observed through changing consecutive horizons, become sparse-target-rigid under multiplicativity, and retain a permanent kernel under deletion-only sources that are coordinatewise indistinguishable from Möbius outside an `o(first-correction)` extremal cap. Measurement count and coordinate fidelity are therefore not invariant resources by themselves.

Any lower bound should first declare whether it concerns unrestricted recovery, one-target testing, pairwise recovery or quotient recovery; whether changing horizon counts as a new operator; the source class and its cross-coordinate laws; and the observation/noise normalization. Only then do rank, sample count, inverse modulus or information capacity become meaningful currencies.

## Keep source coercivity and the Franel--Landau destination separate

The results above concern recovery or non-rigidity of the coefficient source. They do not prove the RH-critical discrepancy estimate. Even a source condition that finally kills sparse shell repair must still be shown to control the nonlocal Franel--Landau norm with the required scale and conditioning. Conversely, failure of coordinatewise sparse rigidity does not by itself rule out a destination theorem that uses a genuinely different source-native relation.