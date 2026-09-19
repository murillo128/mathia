# MI-052 — Proper grade Hamiltonians do not spectralize bounded one-sided source signatures

**Evidence level:** exact synthesis from [PC-361](../../findings/PC-361-proper-grade-hamiltonians-are-spectrally-blind-to-bounded-raising-signatures.md), extending the completion audit of PC-347--PC-360.

Let `H=direct_sum_(m>=0) H_m` with finite-dimensional grades, and let `H_0` be a proper diagonal grade Hamiltonian whose energies `epsilon_m` tend to infinity. If the source signature enters through a bounded operator `Q` that is strictly grade-raising, then `H_0+Q` is closed with compact resolvent, but its spectrum is still exactly the diagonal grade spectrum `{epsilon_m}` with the same algebraic multiplicities.

Thus making the ambient operator unbounded does not by itself cure the spectral blindness found in bounded reciprocal-control models. One-sided bounded raising data are triangular relative to the proper grading; they can change eigenvectors, Riesz projections, Jordan geometry and resolvent norms without moving the eigenvalues that a naive spectralization would read.

The source/control discriminator therefore has to enter a channel that defeats this triangular invariance. Genuine possibilities include same-grade or backward coupling, two-sided interactions, an unbounded signature term whose domain carries source information, nontriangular boundary/domain conditions, or a non-eigenvalue observable such as projection geometry or resolvent growth that is itself tied to the arithmetic destination.

The reusable audit is stronger than “is the operator unbounded?” Ask instead **where the source-dependent term sits relative to the grading and which spectral object is consumed downstream**. A proper unbounded diagonal plus a bounded one-sided triangular perturbation can be spectrally as blind as the compactified bounded models it was meant to escape.

**Boundary.** PC-361 applies to bounded strictly grade-raising perturbations of the stated proper diagonal Hamiltonian. It does not classify unbounded source perturbations, two-sided/domain coupling or non-eigenvalue spectral data, and it does not supply a zeta-zero destination theorem.