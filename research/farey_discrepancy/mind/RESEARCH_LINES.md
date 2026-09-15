# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Find a source-visible ancestry law whose information budget is coercive without reconstructing the source

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-018-additive-coordinate-dimension-is-not-an-information-capacity-bound`.

FD-117--FD-129 classify the reversible Farey skeleton, common-source horizon coherence, sparse multiplicative escape and the circular reconstruction boundary. FD-130--FD-137 then show that counting means, rankwise means, fixed-prime convergence and harmonic physical-scale balancing can all miss a macroscopic source defect; exact multiplicative-rank conditioning exposes one hidden wall but does not make the method generically coercive.

FD-138--FD-140 rotate the wall into transverse additive prime colors. Even conditioning on the complete exact vector of prime-factor counts in every reduced residue class modulo an arbitrary fixed modulus `Q` leaves a finer coprime quadratic coloring whose boundary has only `O((loglog T)^(-1/2))` conditional mass. Thus no fixed congruence-periodic coordinate alphabet is coefficient-coercive by itself.

FD-141 shows that coordinate dimension does not control resolving power: one fixed exact strongly additive scalar can encode the full squarefree prime support. FD-142 sharply improves the capacity audit. The fixed coordinate

`L(n)=sum_(p|n) log p = log rad(n)`

is already injective on squarefree `n<=T`, has minimum spacing `>1/T`, and remains injective after uniform quantization using only `log_2 T+log_2 log T+O(1)` bits. Any injective encoding of the whole squarefree prefix needs `Omega(log T)` bits, so full source reconstruction is possible at essentially the ambient source-identity scale, not only with exponentially fine precision.

FD-143 supplies the first genuinely growing lower-bound regime between those extremes. For arbitrary source-independent partitions of central squarefree parent domains, let `K_T` be the number of active primes and `M_T` the maximum number of cells per prime. If

`K_T M_T = o(sqrt(loglog T))`,

then one fixed infinite prime coloring has a subsequence on which every observed conditional ancestry defect tends to zero, while one fixed orientation of the same source remains wrong on at least half of a fixed active-prime parent domain up to `o(1)`. The cells need not come from congruences, additive coordinates or any regular partition. The obstruction is therefore an observation-budget effect, not merely a fixed-alphabet artifact.

The live coefficient-side theorem must now cross this sub-root-rank anti-concentration barrier without jumping all the way to source identity. Candidate resources include larger but still sub-reconstructive effective alphabets, entropy/covering budgets, source-native derivability from the Farey observable, controlled prime-weight complexity, or a theorem excluding the matched prime-color half-spaces for the physical source. Merely counting coordinates, specifying polynomial precision or allowing a slowly growing arbitrary alphabet is not enough.

A destination-side Fourier-skeleton coercivity theorem remains a distinct route because it could bypass coefficient recovery entirely.

## Determine the first genuinely different regime between fixed alphabets and source reconstruction

**Linked intuitions:** `MI-015-local-ancestry-has-an-exact-rough-core-rigidity-threshold`, `MI-016-harmonic-scale-balancing-still-misses-the-moving-rank-interface`, `MI-017-finite-rank-localization-can-miss-an-orthogonal-additive-prime-factor-coordinate`, `MI-018-additive-coordinate-dimension-is-not-an-information-capacity-bound`.

The frontier is now quantitatively bracketed. Fixed periodic alphabets are under-resolved by FD-140. FD-143 extends the no-go to arbitrary growing source-independent observation schemes with total prime-cell complexity `o(sqrt(loglog T))` in the central rank regime, using one common source along a subsequence. At the opposite end, FD-142 shows that one fixed strongly additive scalar observed with only `Theta(log T)` bits can already be source-reconstructing on the squarefree prefix.

A useful middle regime must therefore live above the elementary Rademacher anti-concentration budget while remaining genuinely below the squarefree identity scale. One route is to push the hidden-wall theorem to much larger alphabets by exploiting structure beyond the union budget. A second is a finite or slowly growing family of source-intrinsic prime weights whose admissibility follows from the Farey/Fourier construction and whose resolving capacity can be priced without directly labeling `n`. A third is a theorem that the physical source cannot realize the matched half-space colorings, avoiding the need to observe every prime coordinate.

For every proposal the decisive audit is whether the observation has become an indirect label for the squarefree parent. If it can distinguish essentially every parent state, the ancestry dilution problem has been bypassed by reconstruction rather than solved by a weaker coercive law. Conversely, being noninjective is not sufficient: FD-143 now gives one concrete range in which a growing noninjective observation is still provably noncoercive.

## Keep information equivalence, horizon entropy, scale visibility, coordinate visibility, precision, provenance and target recovery separate

The obstruction chain shows that “more arithmetic breadth” is not a scalar resource. A coercive law must specify which prime coordinates remain visible, how physical scales are weighted, how narrow the conditioning cells are, how many source states remain distinguishable at the available precision, how many active prime-cell constraints are imposed, where the observable came from, and how much source freedom remains before the condition simply reconstructs Möbius.

FD-140 says exact localization in a maximal fixed congruence vector can still be too coarse. FD-141 says one exact scalar can instead be maximally fine. FD-142 shows that this does not require exotic infinite precision: `Theta(log T)` source-identity bits already suffice in one fixed additive coordinate. FD-143 adds a different resource law: below `sqrt(loglog T)` total prime-cell constraints, even arbitrary source-independent partitions cannot uniformly expose every transverse prime-color wall. Future ancestry claims should therefore state both their resolving capacity and why that capacity is noncircular for the Farey endpoint.