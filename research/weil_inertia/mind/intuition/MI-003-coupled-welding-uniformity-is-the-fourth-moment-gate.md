# MI-003 — Scalarizing the Yang lock moves the hard part into signed finite-window Ramanujan leakage, where rank is not metric cancellation

**Evidence level:** supported for the exact source reductions, positive/unweighted scalar-energy obstructions, Ramanujan projector decomposition, alias quotient, pairwise rank classification, and metric-overlap bounds; the remaining signed many-modulus/source-weighted analytic bridge is open

## Core intuition

The unresolved Yang--Yang fourth-moment obstruction is a source-faithful representation problem with a conservation law. Freeing physical shifts produces a power-sparse two-dimensional selector; scalar LCM projection removes that sparsity but produces a near-linear, maximally additively energetic positive family; and using signs does not help inside the existing positive large-sieve interface. After scalarization, genuine sign cancellation can occur only through finite-window interaction among otherwise orthogonal Ramanujan subspaces.

The new pairwise theory adds a crucial warning: a large **rank defect** in that interaction is not a large metric coupling. The sharp close-prime one-third rank loss is highly localized and can coexist with only `O(1)` total whitened squared overlap. Rank deficiency alone therefore cannot supply the extensive signed Hilbert--Schmidt cancellation needed by the fourth-moment route.

## Strongest justified principle

WI-068--WI-078 establish the source/positive boundary. Two-dimensional source fidelity costs sparse incidence in every fixed finite `L^p`, whereas scalar LCM projection yields near-linear density and maximal positive additive energy even after pruning a subpolynomial fraction of source mass. Positive support/energy reduction is therefore not the missing theorem.

WI-079--WI-080 identify the surviving signed interface. Before positivity, the scalar operator is the Toeplitz Ramanujan sum `R_omega(h)=sum_m omega_m c_m(h)`. On complete common periods the modulus blocks are pairwise orthogonal projections, so signs change block signs but cannot cancel operator/Schatten/rank mass. Every cross-modulus signed gain is created by finite-window truncation.

WI-081--WI-087 classify the first leakage geometry. Pairwise cross-Gram rank is controlled by the distance to the nearest LCM period and is usually maximal once the boundary exceeds the smaller Ramanujan dimension; only a close-prime residual strip has extra defect. Exact aliasing is even stronger: WI-084--WI-085 show that every arbitrary-modulus scalar law on an `N`-window factors through exactly `N` divisor/tail coordinates and has a unique subwindow alias. The scalar representation has already forgotten most modulus provenance.

WI-088--WI-091 close the residual prime-pair rank question quantitatively. In the genuinely residual regime the defect is universally at most one third of the smaller prime space, and the Loewner--Bezout family attains that ceiling. But the sharp scale is confined to one boundary quotient; exact positive ceiling cases are precisely opposite nonzero residue classes modulo `3`, form a matching at fixed observation length, and sit at the apex of an exact triangular boundary layer whose defect drops by one per boundary step.

WI-092--WI-093 then show why even that sharp rank phenomenon is not a cancellation mechanism by itself. Throughout the extremal triangular layer the whitened projector overlap satisfies `tr(Pi_p Pi_q)<4`, independent of prime size, so only `O_eta(1)` principal directions can have correlation at least a fixed `eta`. More generally, any residual prime-pair rank defect with positive density `tau/p -> theta>0` forces only bounded total squared canonical overlap, with average surviving squared correlation `O(1/p)`. Extensive rank loss and strong metric alignment are almost orthogonal notions here.

## What remains possible

The viable scalar route must use the **actual centered signed Yang coefficients** and prove a many-modulus cancellation theorem in a norm or quadratic form sensitive to the source weights, not merely exhibit pairwise rank deficiency. Candidate mechanisms include coherent dependencies across many weakly overlapping blocks, a source-specific restriction inside the exact `N`-coordinate alias quotient, or a weighted incidence theorem that couples the pairwise metric overlaps before absolute values are taken.

Distinct source-faithful alternatives remain: a labelled transform retaining reduced slopes, a direct weighted two-dimensional incidence theorem, the base-aggregated multivariate polynomial representation, or a genuinely non-scalar finite-window object formed before Ramanujan scalarization.

## Status / novelty

Ramanujan sums/subspaces, additive-energy inequalities, large-sieve positivity, Vandermonde/Loewner rank, principal angles, and projector-overlap identities are classical. The persisted Mathia content is the exact placement of the Yang source inside these models and the new separation between **algebraic rank leakage** and **metric coupling strength**. The remaining theorem must exploit source-specific many-body structure beyond both.

## Falsification criterion

Find a source-independent power-saving interface from pairwise rank defect alone despite WI-092--WI-093, or prove that the exact Yang coefficients generate extensive signed cancellation from the bounded-overlap pair graph. A positive result must quantify the actual weighted finite-window operator rather than substitute support, rank, or unweighted coherence.

## Lean-formalizable core

- Positive weighted-energy lower bounds on interval-supported measures.
- Ramanujan-projector orthogonality on common periods.
- Exact finite-window alias quotient.
- Residual prime-pair one-third rank ceiling and triangular boundary profile.
- Projector-overlap/canonical-correlation identities and bounded-overlap consequences.
