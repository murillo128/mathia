# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Find a source-visible ancestry law whose information budget is coercive without reconstructing the source

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-018-additive-coordinate-dimension-is-not-an-information-capacity-bound`.

FD-117--FD-129 classify the reversible Farey skeleton, common-source horizon coherence, sparse multiplicative escape and the circular reconstruction boundary. FD-130--FD-137 then show that counting means, rankwise means, fixed-prime convergence and harmonic physical-scale balancing can all miss a macroscopic source defect; exact multiplicative-rank conditioning exposes one hidden wall but does not make the method generically coercive.

FD-138--FD-140 rotate the wall into transverse additive prime colors. Even conditioning on the complete exact vector of prime-factor counts in every reduced residue class modulo an arbitrary fixed modulus `Q` leaves a finer coprime quadratic coloring whose boundary has only `O((loglog T)^(-1/2))` conditional mass. Thus no fixed congruence-periodic coordinate alphabet is coefficient-coercive by itself.

FD-141 now closes the tempting dimensional extrapolation of that obstruction. A single fixed real strongly additive coordinate

`F(n)=sum_(p_j|n) 3^(-j)`

is injective on squarefree integers and therefore encodes every prime-color wall exactly. Its cost is precision: the minimum spacing through height `T` is of order `3^(-pi(T))`, so stable resolution of all states requires `Theta(pi(T))` bits. **Coordinate dimension is therefore not an information-capacity bound.**

The live coefficient-side theorem must price an admissible information resource, not merely add or count coordinates. Candidate positive laws must be source-native and sufficiently stable to rule out the FD-138--FD-140 walls without becoming an exact recoding of the Möbius prefix. Candidate negative theorems must constrain precision, entropy/covering number, alphabet growth, regularity/description complexity of prime weights, or another quantitative resolving capacity; arbitrary exact real coordinates are too expressive for a finite-dimensional no-go.

A destination-side Fourier-skeleton coercivity theorem remains a distinct route because it could bypass coefficient recovery entirely.

## Determine the first genuinely different regime between fixed alphabets and infinite-precision source encoding

**Linked intuitions:** `MI-015-local-ancestry-has-an-exact-rough-core-rigidity-threshold`, `MI-016-harmonic-scale-balancing-still-misses-the-moving-rank-interface`, `MI-017-finite-rank-localization-can-miss-an-orthogonal-additive-prime-factor-coordinate`, `MI-018-additive-coordinate-dimension-is-not-an-information-capacity-bound`.

The frontier is now bracketed on both sides. Fixed periodic alphabets are under-resolved by FD-140, while unrestricted exact nonperiodic coordinates can be completely source-reconstructing by FD-141. The useful regime must sit between those endpoints.

One route is a modulus/alphabet/precision budget growing with `T` slowly enough that central conditioned cells retain enough mass and a uniform multivariate local law survives, yet fast enough to prevent a fresh transverse coloring from escaping. A second is a finite or slowly growing family of nonperiodic **source-intrinsic** prime weights with a quantified stability/precision modulus. A third is a theorem that the physical admissible source cannot realize the matched half-space colorings, avoiding the need to observe every possible prime coordinate.

For any such proposal the decisive quantity is the number of source states that remain distinguishable at the precision and scale actually available. A condition that becomes injective on the squarefree prefix is already source reconstruction; a condition whose effective alphabet stays bounded is vulnerable to refinement. The missing theorem must identify a noncircular intermediate capacity and prove that it is enough for the Farey endpoint.

## Keep information equivalence, horizon entropy, scale visibility, coordinate visibility, precision and target recovery separate

The obstruction chain shows that “more arithmetic breadth” is not a scalar resource. A coercive law must specify which prime coordinates remain visible, how physical scales are weighted, how narrow the conditioning cells are, what numerical/analytic precision is retained, and how much source freedom remains before the condition simply reconstructs Möbius.

FD-140 says exact localization in a maximal fixed congruence vector can still be too coarse. FD-141 says one exact scalar can instead be maximally fine. The difference is not dimension but **resolving capacity**. Future ancestry claims should therefore state both the coordinate family and the information budget under which it is observed.