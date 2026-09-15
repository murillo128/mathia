# MI-033 — Current endpoint capacities are jointly satisfiable; the missing coupling is prime localization

**Evidence level:** exact matched critical-scale compatibility construction from [MC-306](../../findings/MC-306-near-shell-singleton-source-profile-saturates-current-capacities.md), testing the radical/energy/occupancy constraints of `MC-296` and `MC-301`--`MC-305`

At critical rank `2^R=kappa log y`, the currently persisted scalar constraints do not contradict one another. MC-306 chooses `R` distinct odd primes `p_i in [z,2z]`, `z=y^(1/R)`, and the independent quadratic characters modulo those primes. Their common radical

`P=prod_i p_i`

satisfies

`y <= P <= kappa y log y`, `phi(P)/P -> 1`,

while every nontrivial subset character has primitive conductor at least `z`, above the current Page source scale after fixing the audited constant.

The same model simultaneously fits the other endpoint budgets. The reciprocal one-defect law has selected Fourier energy

`E_X=2^R/R = kappa log y/R`,

which fits well inside the fixed-radical capacity `(1-o(1))log y`. The quotient map `(Z/PZ)^* -> {±1}^R` is onto, every sign cell has `phi(P)/2^R` residue classes, and each of the `R` endpoint cells contains far more residue classes than the balanced shell multiplicity would require.

Thus the factor-`R` energy slack, near-shell radical lower bound and quotient-support count are not three fragments of an eventual contradiction: **there is a single critical-scale source profile satisfying all of them at once.** Further algebraic recombination of those same scalar inequalities cannot close the endpoint.

What the matched profile deliberately does not realize is the target arithmetic localization. Actual primes in `(y,2y]`, with the required congruence restriction, would have to land with the endpoint multiplicities in prescribed one-defect Legendre sign cells for a modulus `P=y^(1+o(1))`. Residue-class cardinality does not imply such dyadic prime occupancy. A second possible source-specific discriminator is the full shell source-cost minimization: a lower-prime representative could conceivably realize the same finite shell functional more cheaply than the constructed primitive conductor profile.

The reusable lesson is that capacity accounting can become complete without becoming coercive. Once rank, conductor scale, common ramification, totient density, Fourier energy and quotient state count admit one matched model, the next theorem must couple the source to **where target primes actually occur**, or introduce an invariant absent from that model.

**Boundary.** MC-306 does not construct an arithmetic endpoint realization and gives no Mertens estimate. It does not rule out a theorem on prime localization in simultaneous quadratic-sign cells, unexpectedly cheap ambient source representatives, finer conductor correlations or another source-specific invariant.