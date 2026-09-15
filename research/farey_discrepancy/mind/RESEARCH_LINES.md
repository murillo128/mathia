# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Find a source-visible ancestry law whose information budget is coercive without reconstructing the source

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-018-additive-coordinate-dimension-is-not-an-information-capacity-bound`.

FD-117--FD-129 classify the reversible Farey skeleton, common-source horizon coherence, sparse multiplicative escape and the circular reconstruction boundary. FD-130--FD-137 then show that counting means, rankwise means, fixed-prime convergence and harmonic physical-scale balancing can all miss a macroscopic source defect; exact multiplicative-rank conditioning exposes one hidden wall but does not make the method generically coercive.

FD-138--FD-140 rotate the wall into transverse additive prime colors. Even conditioning on the complete exact vector of prime-factor counts in every reduced residue class modulo an arbitrary fixed modulus `Q` leaves a finer coprime quadratic coloring whose boundary has only `O((loglog T)^(-1/2))` conditional mass. Thus no fixed congruence-periodic coordinate alphabet is coefficient-coercive by itself.

FD-141 shows that coordinate dimension does not control resolving power: one fixed exact strongly additive scalar can encode the full squarefree prime support. FD-142 sharply improves the capacity audit. The fixed coordinate

`L(n)=sum_(p|n) log p = log rad(n)`

is already injective on squarefree `n<=T`, has minimum spacing `>1/T`, and remains injective after uniform quantization using only `log_2 T+log_2 log T+O(1)` bits. Any injective encoding of the whole squarefree prefix needs `Omega(log T)` bits, so full source reconstruction is possible at essentially the ambient source-identity scale, not only with exponentially fine precision.

Therefore neither finite dimension, finite precision nor inverse-polynomial precision defines a noncircular intermediate ancestry regime. The live coefficient-side theorem must price an admissible resource that stays genuinely below source identity or excludes direct source labeling by provenance/regularity. Candidate restrictions include sublinear effective alphabet, entropy/covering number, source-native derivability from the Farey observable, controlled prime-weight complexity, or another stable resolving capacity. Merely requiring `o(T)` states prevents injectivity but does not prove a hidden wall or coercivity.

A destination-side Fourier-skeleton coercivity theorem remains a distinct route because it could bypass coefficient recovery entirely.

## Determine the first genuinely different regime between fixed alphabets and source reconstruction

**Linked intuitions:** `MI-015-local-ancestry-has-an-exact-rough-core-rigidity-threshold`, `MI-016-harmonic-scale-balancing-still-misses-the-moving-rank-interface`, `MI-017-finite-rank-localization-can-miss-an-orthogonal-additive-prime-factor-coordinate`, `MI-018-additive-coordinate-dimension-is-not-an-information-capacity-bound`.

The frontier is now bracketed more tightly than by FD-141 alone. Fixed periodic alphabets are under-resolved by FD-140, while FD-142 shows that one fixed strongly additive scalar observed with only `Theta(log T)` bits can already be source-reconstructing on the squarefree prefix. Polynomially fine resolution is therefore not an intermediate regime by itself.

A useful middle regime must constrain the **effective number of source states distinguishable at the actual observation precision and provenance**. One route is an alphabet/entropy budget provably below the squarefree identity scale while still growing enough to defeat every fixed congruence refinement. A second is a finite or slowly growing family of source-intrinsic prime weights whose admissibility follows from the Farey/Fourier construction rather than from an arbitrary encoding of `n`. A third is a theorem that the physical source cannot realize the matched half-space colorings, avoiding the need to observe every prime coordinate.

For every proposal the decisive audit is whether the observation has become an indirect label for the squarefree parent. If it can distinguish essentially every parent state, the ancestry dilution problem has been bypassed by reconstruction rather than solved by a weaker coercive law.

## Keep information equivalence, horizon entropy, scale visibility, coordinate visibility, precision, provenance and target recovery separate

The obstruction chain shows that “more arithmetic breadth” is not a scalar resource. A coercive law must specify which prime coordinates remain visible, how physical scales are weighted, how narrow the conditioning cells are, how many source states remain distinguishable at the available precision, where the observable came from, and how much source freedom remains before the condition simply reconstructs Möbius.

FD-140 says exact localization in a maximal fixed congruence vector can still be too coarse. FD-141 says one exact scalar can instead be maximally fine. FD-142 shows that this does not require exotic infinite precision: `Theta(log T)` source-identity bits already suffice in one fixed additive coordinate. Future ancestry claims should therefore state both their resolving capacity and why that capacity is noncircular for the Farey endpoint.