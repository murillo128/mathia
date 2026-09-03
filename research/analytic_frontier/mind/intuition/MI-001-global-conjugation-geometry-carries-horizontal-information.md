# MI-001 — Horizontal zero information can survive in global conjugation geometry even when local positive extraction is screened

**Evidence level:** supported by ANF-001--ANF-002 and the audited support-one pair-correlation inputs

## Core intuition

Support-one pair data are not intrinsically blind to horizontal displacement. What fails is a narrower extraction architecture: fixed-scale estimates can lose their exponent at microscopic depth, and termwise-positive local kernels can be screened. A global quadratic inequality that retains conjugation symmetry can still convert the same pair-correlation information into an unconditional horizontal-zero statement.

The useful distinction is therefore between **information present in the global pair geometry** and information recoverable by a particular local positive decomposition.

## Strongest justified principle

ANF-001 gives the scale gate. A bound with a fixed-`sigma` power saving does not automatically remain coercive when `sigma-1/2` is only `O(1/log T)`; the exponent improvement can shrink to a constant-factor effect. Any RH-relevant near-line argument must carry a quantitative uniformity statement to the microscopic scale.

ANF-002 gives the complementary positive mechanism. Lamzouri's use of the unconditional BGSST support-one pair theorem together with a global Hilbert inequality yields horizontal information without demanding nonnegativity of each individual cross-height term. The conjugation/global quadratic structure retains a relation that termwise screening arguments deliberately discard.

Thus the support threshold by itself does not classify the information content. One must also specify the aggregation geometry and whether signs/cross-height coupling are retained.

## Evidence synthesis and boundaries

This does not say support one is sufficient for RH, nor that every global quadratic form avoids screening. ANF-002 reaches a substantial unconditional simple-critical proportion, not zero localization, and ANF-001 warns that a fixed-depth theorem can still fail at the scale required for RH.

The durable boundary is sharper: a negative result for one positive-kernel extraction cannot be promoted to a no-go for the entire pair-correlation information class unless it also matches the global conjugation/coupling used by the competing method.

## Status / novelty

The pair-correlation theorem and Hilbert inequality are literature; the scale computation is exact. The synthesis is the separation between local positivity bandwidth and globally retained horizontal information.

## Falsification criterion

Either prove that a proposed global support-one quadratic observable factors through a screened local-positive quotient, or exhibit a source-faithful microscopic estimate whose coercive gain remains uniform as the horizontal depth is `O(1/log T)`.

## Lean-formalizable core

- Exponent-budget evaluation under `sigma-1/2 = a/log T`.
- Conjugation-pair bookkeeping.
- Logical separation between termwise positivity and positivity of a global quadratic form.
