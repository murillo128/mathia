---
id: RG-reflected-defect-erasure-and-energy-identifiability
type: research-graph-relation
derived: true
---

# Reflected Farey defects: erasure recovery and energy-conditioned spectra

[[research/farey_discrepancy/graph/farey-discrepancy|Farey Discrepancy]]

[[research/farey_discrepancy/findings/FD-331-joint-farey-defect-ranks-and-values-invert-all-excursion-permutations|FD-331]] gives exact inversion from the complete ordered defective ranks and values, with the prime and genuine positive excursion lengths supplied. It includes a realization check; neither ranks alone nor values alone are substituted for that record.

[[research/farey_discrepancy/findings/FD-344-reflection-makes-three-farey-defect-erasures-recoverable-four-need-not-be|FD-344]] uses equal mirror values and a zero half-checksum in the explicitly reflected permutation class. Any three known-position value erasures are recoverable when the complete exact ranks remain. Four can hide different energies at order seven. The more general sufficient pattern is at most one completely missing mirror pair; this is not a classification of every two-pair erasure.

FD-344 §4 specializes [[research/farey_discrepancy/findings/FD-333-one-quantum-fixed-rank-farey-spectral-instability|FD-333]] to primes `p=7 mod 12`, `p>=19`. Its reflected `BACRH` and `HACRB` orders have the same six exact defective ranks and retain the same two values `7/p` after erasing two specified mirror pairs. Their full energies tend to `19/(24pi²)` and `211/(288pi²)`, leaving gap `17/(288pi²)>0`. Every scalar energy estimator from this common erased record therefore has liminf worst-pair error at least `17/(576pi²)`. The source proves the limits from its PNT-based rank asymptotics and exact transport identity; finite examples alone do not establish them.

This asymptotic obstruction uses unequal energies. Supplying exact energy distinguishes the pair for sufficiently large primes, so it does not answer the stronger matched-energy question below. It is an explicit specialization of FD-333's existing construction, not a separate frontier episode or a claim that every two-pair erasure is ambiguous.

[[research/farey_discrepancy/findings/FD-345-exact-energy-does-not-repair-four-reflected-farey-defect-erasures|FD-345]] settles the stronger record with exact positive full discrepancy energy also supplied. A balanced excursion reversal has `D'(r+a)=C-D(r+ell-a)` with `C=0` when `N(2t+1)=p(2r+ell)`, preserving the full energy. Its order-617 certificate has identical sixteen defective ranks and retained values outside two erased mirror pairs, identical directed-edge inventory and equal positive energy. Yet the squared Dirichlet second-difference norms differ by `-11577/141348948592544`. Since `sum_m lambda_m^2 pi_m=||KD||^2/||D||^2`, at least one normalized even-mode intensity differs. Equality of the first spectral moment also survives; unequal vectors alone are not the separation argument.

Thus exact energy does not repair universal spectral identification after four erasures. The three-erasure inverse remains intact. This is one additional obstruction for an enriched observation record, not a contradiction of full-signature injectivity. The energy-matched FD-345 example establishes no fixed-low-mode gap, asymptotic separation or minimal prime. Its localized upper bound below now limits the single-pair mechanism.

## Necessary balance and the localized spectral limit

FD-345, equations (4a)–(4e), now proves that balance is necessary for a nontrivial **single mirrored excursion-pair exchange**. Its full-energy increment is `2 C A_j`, where `A_j=(ell-1)/p-2 sum_a y_a`. The genuine interior fractions have denominators coprime to p, and `p A_j` has residue `(ell-1)(2j+1)` modulo p. Since `1<=ell-1<p`, only the central, self-reflected excursion has zero skew; exchanging that label does nothing. Exact energy equality for a nontrivial pair therefore requires `N(2t+1)=p(2r+ell)`, hence `p|N` and even ell at a left noncentral slot. Those necessary arithmetic conditions neither realize the rank nor ensure the defective ranks survive.

Only `2(ell-1)` discrepancy coordinates can change, each by at most `1/p`. For equal positive energy E, FD-345 (15)–(16) gives `TV(pi(D'),pi(D)) <= sqrt(2(ell-1)/(p² E)) < sqrt(2/(pE))`. Thus `pE -> infinity` forces convergence of the full normalized spectra, including at positive limiting energy. A fixed separation at least delta requires `E<=2/(delta² p)`; no family attaining that regime is proved. Several exchanges can compensate energy increments, and whole-block moves need not obey this support bound. The statement does not close general four-erasure spectral separation or weaken the finite order-617 certificate.

This narrows the existing energy-conditioned-erasure episode rather than adding another event. The probability-metric step is classical square-root-density/Cauchy–Schwarz stability, as acknowledged in FD-345; the prime-denominator and realization restrictions are retained explicitly.

These sources concern artificial inherited-label whole-excursion reassemblies with exact auxiliary inputs, not alternative genuine Farey sequences. Coding checksums, reversal isometries and Dirichlet spectral calculus are classical; the sources claim a local realizable certificate, not external priority or improved Franel/RH bounds. No Atlas territory is closed by this control example.
