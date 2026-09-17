# MI-023 — Unbounded exact Farey horizons rigidify a permanent source

**Evidence level:** exact synthesis from [FD-164](../../findings/FD-164-one-farey-horizon-leaves-dense-coefficient-orientations-undetermined.md), [FD-165](../../findings/FD-165-polylogarithmically-many-farey-horizons-still-leave-dense-orientations-undetermined.md), and [FD-166](../../findings/FD-166-unbounded-exact-farey-horizons-rigidify-a-permanent-source.md), with the quantitative continuation isolated separately in `MI-024` from FD-167.

Finite-cutoff and permanent-source ambiguity are different questions. FD-164 shows that one complete Farey discrepancy field can be matched exactly while changing a dense fraction of squarefree Möbius orientations. FD-165 extends this to large finite horizon bundles: whenever `J_T M_beta(T)=o(T)`, one source chosen for that finite bundle can still retain a dense high-coordinate orientation kernel.

FD-166 shows why those controls cannot converge to a distinct permanent exact source. The quotient set exposed by one complete horizon `H` contains every consecutive integer through `floor(sqrt(H))`. Exact equality of complete fields therefore forces `A(r)=M(r)` and `a(r)=mu(r)` for every `r<=floor(sqrt(H))`.

If one fixed source matches the physical complete field on any unbounded set of horizons, however sparse, these forced prefixes exhaust every finite coordinate and the source is exactly Möbius. Equivalently, a permanent source whose first defect is at `n_0` cannot match any complete field once `H>=n_0^2`.

The finite-bundle kernels of FD-164--FD-165 are therefore **noncompact in source coordinates**. Their altered orientations must migrate outward as the cutoff grows. More horizons help only when the compatibility requirement binds them to one permanent latent source; no critical density of exact complete horizons is needed once the hierarchy is unbounded.

FD-167 subsequently shows that this exact rigidity is not merely a brittle equality phenomenon for the complete field: the square-root prefix also has an `H`-independent `L^2` inverse modulus. That quantitative statement belongs to `MI-024`; the reusable point here is the compactness change created by requiring one permanent source across unbounded horizons.

**Boundary.** Exact permanent-source rigidity does not imply that a partial, sampled or coarsened observation family retains a growing source prefix, and source recovery does not imply the RH-critical Franel--Landau discrepancy estimate. Those are separate conditioning and destination gates.