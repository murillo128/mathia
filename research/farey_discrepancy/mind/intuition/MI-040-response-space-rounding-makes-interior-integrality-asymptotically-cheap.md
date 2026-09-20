# MI-040 — Response-space rounding makes interior integrality asymptotically cheap

**Evidence level:** exact finite-dimensional synthesis from [FD-237](../../findings/FD-237-interior-real-reservoir-profiles-admit-uniformly-switched-stable-integer-lifts.md). The conclusion applies to interior real reservoir profiles with sufficient capacity margin; it does not construct such a positive profile or settle the finer-topology obstruction from FD-236.

For the divisor-response matrix `A_D`, the finite map from coefficient cells to responses is lower triangular with unit diagonal, hence unimodular. If `y=A_D a`, round each response coordinate to an integer `q(m)` and pull back with the exact inverse

`(A_D^-1 q)(n)=sum_(d|n) (q(d)-q(d-1))`.

The resulting occupancy is integral. Because each response coordinate moves by at most `1/2`, the coefficient perturbation is bounded by `tau(n)`. For the switched rows currently used in the Farey construction, whose difference orders are `1` or `4`, the induced response error is uniformly bounded; after the physical prime-flip normalization the same statement remains an absolute-constant error.

That changes the role of integrality. At reservoir scales `K_n asymp n L_N` with `L_N->infinity`, the `tau(n)` perturbation is negligible relative to the cell capacities, provided the real profile sits at least that far from each capacity face. Likewise any switched normalization tending to infinity absorbs the bounded response error. Integer realization is therefore not a separate macroscopic bulk barrier once an interior real lift has been found.

The boundary qualifier is essential. A real lift that relies on cells within `O(tau(n))` of zero or saturation can be destroyed by quantization, and a newly refined response topology may assign non-negligible cost to the otherwise bounded rounding error. Exact source-side coherence can also impose constraints not encoded by the finite divisor-response lattice.

**Boundary.** FD-237 is a quantization theorem, not a positivity theorem. It does not produce a real nonnegative lift, prove capacity margin, determine the correct response topology below `L_N 4^j`, or show that all arithmetic source constraints are preserved. It isolates the remaining discrete difficulty at capacity boundaries and coherence rather than in interior integrality itself.
