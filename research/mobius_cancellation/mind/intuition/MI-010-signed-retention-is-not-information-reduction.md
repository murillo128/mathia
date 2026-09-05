# MI-010 — Signed retention is not information reduction when generic complement recovery reconstructs Mertens

**Evidence level:** supported through MC-087 by exact parity controls, annular identities, Fourier/physical reconstruction equivalences, and arbitrary-subset support budgets

## Core intuition

A useful Möbius carrier must pass two distinct gates. It must retain signed arithmetic that unsigned divisor-density surrogates erase, and it must discard enough target information that controlling the carrier is genuinely easier than controlling Mertens. Passing the first gate does not imply the second, and neither proper truncation nor selective geometry proves under-resolution.

The annular results now make the second gate representation-independent across a broad class. If an omitted Fourier tail or physical-space complement can already be restored below the target power scale by a generic absolute estimate, then the retained source-coupled statistic remains quantitatively equivalent to the Mertens target.

## Strongest justified principle

MC-082 constructs a matched control showing that unsigned local divisor-density data can miss Liouville parity completely. MC-083--MC-084 then show that direct parity restoration and the exact Huxley--Watt sawtooth coupling retain the sign but reconstruct Mertens.

MC-085 proves the same for a proper low-frequency Fourier truncation once its generic omitted tail is below the desired target scale. MC-086 gives the physical-space analogue for initial reciprocal slabs with the same power threshold. MC-087 removes the geometry entirely: for any omitted annular subset `E_N`, if `#E_N=O(N^{2 beta})` then boundedness of the source sawtooth gives a target-subordinate complement and the retained coupled statistic is equivalent to `M(x)=O(x^beta)`.

Thus the useful discriminator is **signed information plus genuine information deficit**. A selective mask or partial statistic becomes interesting only when its discarded contribution is too large to restore generically and a new arithmetic mechanism controls it, or when the coupled recurrence closes without reconstructing the complement at all.

## What remains possible

A live annular route may omit supercritical pair mass and prove signed Möbius cancellation in that complement from independently weaker input, use a sparse/source-forced family for which retained and omitted pieces are estimated jointly before absolute values, or derive a strict scale contraction that never restores the full Huxley--Watt residual.

The evidence does not say that every signed partial statistic is Mertens-equivalent. It says that parity sensitivity, exact source origin, properness, sparsity, and selectivity are not sufficient evidence of information reduction when a generic complement bound already restores the target at the claimed resolution.

## Status / novelty

Liouville parity, sawtooth expansions, Fourier truncation, hyperbola counting, and support bounds are classical ingredients. The persisted synthesis is the information gate: **a Möbius residual is useful only if it retains signed source structure while crossing the resolution at which generic complement recovery reconstructs Mertens**.

## Falsification criterion

Produce a covered MC-083--MC-087 carrier at the stated generic-restoration resolution whose bound is strictly weaker than the corresponding Mertens bound, or construct a source-forced signed residual with supercritical omitted information whose complement is independently controlled or never reconstructed while a strict contraction closes.

## Lean-formalizable core

- Liouville-parity matched controls.
- Exact source-coupled annular recovery identities.
- Fourier and reciprocal-slab reconstruction thresholds.
- Arbitrary omitted-subset support bound and Mertens equivalence.
