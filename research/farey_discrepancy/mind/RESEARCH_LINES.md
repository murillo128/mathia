# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Find a source-visible ancestry law that cannot rotate its hidden wall into another additive coordinate

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-017-finite-rank-localization-can-miss-an-orthogonal-additive-prime-factor-coordinate`.

FD-117--FD-129 classify the reversible Farey skeleton, common-source horizon coherence, sparse multiplicative escape and the circular reconstruction boundary. FD-130--FD-136 then show that counting means, rankwise means, fixed-prime convergence and harmonic physical-scale balancing can all miss a macroscopic source defect.

FD-137 proves that the surviving FD-132 witness is not hiding across physical scales. Inside every factor-two shell its defects occupy an `o(sqrt(loglog T))` central `omega(n)` strip, so mean ancestry still vanishes over a broad growing prime family. Exact conditioning on the exceptional rank, however, exposes a maximal defect wall. This identifies the hidden coordinate of that witness rather than proving a general coercive law.

FD-138 moves the sign wall into the additive prime-color coordinate `D(n)=sum_(q|n) chi_4(q)`, and FD-139 shows that even exact central `omega=m` conditioning leaves that transverse wall asymptotically invisible in mean. The local mechanism is codimension: fixing the rank fixes essentially the sum of the two mod-4 prime-color populations, while the difference retains square-root fluctuations.

FD-140 lifts this from one missing coordinate to every **fixed congruence-periodic coordinate alphabet**. For any fixed modulus `Q`, condition on the entire exact vector of prime-factor counts in all reduced residue classes modulo `Q`. A quadratic character modulo a new prime `ell` coprime to `Q` refines every coarse class into two equal prime populations. The full mod-`Q` vector fixes their sums but leaves one signed difference with `Theta(loglog T)` variance, so the two-value sign wall has only `O((loglog T)^(-1/2))` conditional mass in every central exact vector cell. Thus no fixed finite family of additive prime coordinates whose weights factor through one fixed modulus can be coefficient-coercive by itself.

The live positive theorem must therefore use structure stronger than fixed congruence resolution. Can the admissible Farey/Möbius source itself forbid transverse additive half-space walls, or is there a nonperiodic source-native coordinate family whose joint localization is coercive without already reconstructing the Möbius prefix? Any proposed law must survive the FD-140 refinement test and stay below the exact rough-core reconstruction threshold of FD-135. A destination-side Fourier-skeleton coercivity theorem remains a distinct route because it could bypass coefficient recovery entirely.

## Determine the first genuinely different regime beyond fixed coordinate alphabets

**Linked intuitions:** `MI-015-local-ancestry-has-an-exact-rough-core-rigidity-threshold`, `MI-016-harmonic-scale-balancing-still-misses-the-moving-rank-interface`, `MI-017-finite-rank-localization-can-miss-an-orthogonal-additive-prime-factor-coordinate`.

FD-137--FD-140 separate localization strength from coordinate completeness. Exact conditioning is effective only when the source transition is measurable in the visible coordinates. Enlarging a fixed periodic alphabet all the way to the complete residue-class count vector modulo `Q` still does not close the problem, because a coprime modulus supplies a finer independent coloring.

The next coefficient-side question is therefore no longer which additional **fixed** congruence coordinate to add. Three regimes remain genuinely open. First, can a modulus or coordinate dimension grow with `T` slowly enough that central exact cells remain populated and a uniform multivariate local law survives, yet fast enough to prevent the FD-140 refinement escape? Second, can a finite set of nonperiodic/source-intrinsic prime weights be justified from the actual Farey/Möbius representation and shown to exclude transverse sign walls? Third, can one prove directly that the physical admissible source cannot realize the matched half-space colorings used by the negative controls, without attempting to observe every possible prime coordinate?

For the growing-alphabet route the quantitative bottleneck is now explicit: determine the joint range in which a dimension/modulus `D(T)` may increase while exact central vector cells still have enough mass and sufficiently uniform Selberg--Delange/local-limit control to support a coercive ancestry estimate. A negative result in that regime would need a diagonal refinement construction whose new color remains unresolved faster than the visible alphabet grows.

## Keep information equivalence, horizon entropy, scale visibility, coordinate visibility, local rigidity and target recovery separate

The current obstruction chain shows that “more arithmetic breadth” is not a scalar resource. A coercive law must specify which prime coordinates and additive factor statistics remain visible after normalization, how physical scales are weighted, how narrow the conditioning cells are, and how much source freedom remains before the condition simply reconstructs Möbius.

FD-140 sharpens the warning from FD-139: even exact localization in a maximal fixed congruence coordinate vector does not help if the source can retain a finer transverse fluctuation. The next condition must therefore be justified from actual source geometry or must grow in arithmetic resolution with scale, not chosen merely because it kills the previous counterexample.