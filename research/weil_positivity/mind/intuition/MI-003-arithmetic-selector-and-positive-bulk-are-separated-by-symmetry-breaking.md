# MI-003 — Positive finite selectors survive, but canonical cover/refinement assembly gives either no repeated increment or an extensive one

**Evidence level:** supported by exact positive selectors, cover-Jensen controls, and repeated-prime full-chord stationarity/reduction/trace theorems

## Core intuition

Positivity does not by itself erase arithmetic. Finite pointed covers and related operators can carry exact `log n` or prime-power information. The obstruction is the **assembly law**: a positive carrier may become universal, singular, stationary, reducing, or extensive when levels are glued, so the depth-independent increment required by the Weil prime-power comb is absent.

In the canonical normalized full-chord positive geometry, repeated-prime refinement now exhibits both sides of this mismatch. The coarse channel has exactly zero increment and zero fine-mode self-energy; fixed continuous nonnegative traces of the complete fine spectrum are instead either zero or linear in deck multiplicity. Neither behavior produces the constant repeated Mangoldt birth `log p`.

## Strongest justified principle

WP-081--WP-106 show the cover-side boundary. Positive finite selectors and a positive logarithmic Jensen cocycle exist, but regular bulk/trace scalarizations classicalize; exact `log n` occurs only at a singular endpoint that generic cover Markov dynamics already forces. Prime-power support still needs additional signed structure.

WP-134 supplies the coarse refinement obstruction. For the normalized full inverse-square primitive-shell chord Laplacian, repeated-prime refinement satisfies exactly `J^*A_{Np}J=A_N`. The canonical coarse increment is zero for every repeated power while `Lambda(p^k)=log p` remains nonzero.

WP-135 closes the coarse/fine response escape. The complete repeated-prime operator decomposes into fiber Fourier sectors with the coarse sector reducing. Hence the Feshbach/Schur self-energy vanishes and fixed spectral functional calculus followed by coarse compression remains exactly stationary.

WP-136 closes the natural full-fiber positive-trace escape. PC-156 writes the full fine spectrum as samples of one fixed Hermitian pencil `P_d(k/m)`. For every fixed continuous nonnegative spectral function `Phi`,

`Tr Phi(A_dm) = sum_{k=0}^{m-1} Tr Phi(P_d(k/m))`.

The normalized Riemann sum converges to a nonnegative integral. Thus the trace is either identically zero or `I_Phi m + o(m)`. Along `m=p^r` it is extensive in prime-power depth; after division by `m`, successive increments vanish. A fixed positive continuous full-spectrum trace cannot yield a nonzero depth-independent `log p` shell birth.

## Evidence synthesis and boundaries

The theorem is narrow but decisive for this carrier. Singular or depth-dependent spectral functions, nonlinear joint observables, determinant phases, provenance-sensitive cross-level couplings, and finite--archimedean constructions formed before the positive scalar trace remain possible. Their normalization must be source-forced rather than chosen to subtract the extensive term after seeing the target.

Any successful repeated-prime mechanism must explain how it escapes the exact trichotomy already seen here: stationary coarse response, zero coarse/fine self-energy, or extensive regular full-spectrum positive response.

## Status / novelty

Positive graph Laplacians, cyclic fiber decompositions, Schur complements, Riemann sums, Jensen inequalities, and functional calculus are classical. The persisted synthesis is the selector/assembly boundary: **regular positive assembly naturally produces zero or extensive depth response, while the explicit formula needs a nonzero intensive repeated-prime birth**.

## Falsification criterion

Produce a nonzero repeated-prime coarse/Feshbach increment in the exact geometry or a fixed continuous nonnegative full-fiber spectral trace with a nonzero depth-independent asymptotic increment, contradicting WP-134--WP-136. A singular/depth-dependent pre-compression carrier would evade rather than falsify the intuition.

## Lean-formalizable core

- Repeated-prime coarse stationarity and reducing-subspace identity.
- Vanishing Feshbach/Schur self-energy.
- Full-fiber sampling identity over the fixed quadratic pencil.
- Zero-versus-extensive dichotomy for continuous nonnegative spectral traces.
