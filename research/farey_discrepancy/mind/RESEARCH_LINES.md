# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Find a source-visible ancestry law that cannot rotate its hidden wall into another additive coordinate

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-017-finite-rank-localization-can-miss-an-orthogonal-additive-prime-factor-coordinate`.

FD-117--FD-129 classify the reversible Farey skeleton, common-source horizon coherence, sparse multiplicative escape and the circular reconstruction boundary. FD-130--FD-136 then show that counting means, rankwise means, fixed-prime convergence and harmonic physical-scale balancing can all miss a macroscopic source defect.

FD-137 proves that the surviving FD-132 witness is not hiding across physical scales. Inside every factor-two shell its defects occupy an `o(sqrt(loglog T))` central `omega(n)` strip, so mean ancestry still vanishes over a broad growing prime family. Exact conditioning on the exceptional rank, however, exposes a maximal defect wall. This identifies the hidden coordinate of that witness rather than proving a general coercive law.

FD-138 supplies the next matched obstruction. A new common source moves the sign wall into the additive prime-color coordinate `D(n)=sum_(q|n) chi_4(q)`. Even after restricting to one factor-two shell and a fixed positive-Gaussian-mass central rank window, the mean defect tends to zero uniformly over all primes while coefficient disagreement stays positive-density.

FD-139 closes the exact-rank escape for that new source. Squarefree Sathe--Selberg keeps every central exact `omega=m` parent cell at scale `T/sqrt(loglog T)` even after excluding the active prime, while the joint local law for the two mod-4 prime colors puts the fixed boundary `D in {-1,0}` at scale only `T/loglog T`. Hence the same one global source has vanishing mean ancestry uniformly over all primes **inside every exact central rank in a fixed CLT band** while remaining a positive-density distance from Möbius. Exact rank is therefore not intrinsically coercive; FD-137 succeeded only because its earlier witness placed the wall in the rank coordinate itself.

The live theorem must now use **source-native multidimensional structure** rather than finer localization of `omega`. Can the admissible Farey/Möbius source be shown to forbid transverse additive half-space walls, or can one identify a finite family of prime-factor coordinates whose joint localization is coercive without already reconstructing the Möbius prefix? Any proposed law must survive the FD-139 exact-rank rotation test and stay below the exact rough-core reconstruction threshold of FD-135. A destination-side Fourier-skeleton coercivity theorem remains a distinct route because it could bypass coefficient recovery entirely.

## Determine whether any finite source-native coordinate family is complete enough

**Linked intuitions:** `MI-015-local-ancestry-has-an-exact-rough-core-rigidity-threshold`, `MI-016-harmonic-scale-balancing-still-misses-the-moving-rank-interface`, `MI-017-finite-rank-localization-can-miss-an-orthogonal-additive-prime-factor-coordinate`.

FD-137 and FD-139 separate two notions that had been conflated. Exact conditioning kills a source only when the source transition is measurable in the conditioned coordinate. The mod-4 witness survives exact `omega` because `omega` records essentially the sum of the two prime-color populations while `D` records their difference, whose conditional fluctuation remains of square-root size.

The next coefficient-side question is therefore finite-dimensional rather than one-dimensional: if one conditions on several exact additive prime-factor coordinates simultaneously, can a matched source always rotate its wall into another transverse coordinate, or is there a natural finite family fixed by the Farey/Möbius representation that closes all such directions? A useful positive law must justify that family from source geometry rather than adding coordinates adversarially until a chosen witness disappears. Conversely, a strong negative result would show that every fixed finite congruence/additive coordinate family admits a further common-source coloring with a codimension-one boundary of vanishing conditional mass.

## Keep information equivalence, horizon entropy, scale visibility, coordinate visibility, local rigidity and target recovery separate

The current obstruction chain shows that “more arithmetic breadth” is not a scalar resource. A coercive law must specify which prime coordinates and additive factor statistics remain visible after normalization, how physical scales are weighted, how narrow the conditioning cells are, and how much source freedom remains before the condition simply reconstructs Möbius.

FD-139 sharpens the warning from FD-138: even exact localization in a visible coordinate does not help if the source can retain a transverse fluctuation. The next condition must therefore be justified from the actual source geometry, not chosen merely because it kills the previous counterexample.