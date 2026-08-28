# MI-003 — Arithmetic significance begins after universal-control subtraction

**Evidence level:** supported

## Core intuition

A striking exponent, singularity, or determinant boundary is not evidence of arithmetic merely because it was discovered on a prime-derived geometry.  Mathia needs a **null-model discipline**: first identify which analytic features are forced by dimension, ordering, density, or the ambient exact map; only the residual that changes when genuinely prime organization is removed can be interpreted as arithmetic signal.

## Strongest justified principle

If a proposed prime-specific spectral feature is reproduced by a featureless control under the same geometric construction, that feature itself belongs to the carrier geometry, not to the primes.  Prime information may still appear in coefficients, subleading terms, ordered fluctuations, or marked responses built on that carrier.

PF-088 is the decisive example.  Replacing the primes by integers while keeping

\[
V(x)=\pi\cot(\pi/x)
\]

and the same ordered flute/scattering construction reproduces the sharp threshold

\[
\operatorname{Re}s=\frac14
\]

both for the direct relative scattering kernel and for the all-block relative Ruelle sector.  The exponent comes from one-dimensional propagation and square summability:

\[
|i-j|^{-2s}\quad\leadsto\quad
\sum_m m^{-4\operatorname{Re}s}.
\]

Primes modify the weights and fluctuations but do not cause the exponent.

The same adversarial lesson appears in milder forms elsewhere.  Prime-circle refinement can collapse to classical cyclotomic/Farey/Bost--Connes structures; the exact Grunsky--Schiffer kernel of `V` is defined before any prime sampling; and scalar low-energy determinants obey a universal matrix-tree identity before prime gap asymptotics are inserted.  The arithmetic question starts **after** these universal pieces are factored out.

## A useful hierarchy of controls

For future candidates, a sequence of increasingly matched controls can separate distinct sources of apparent structure:

1. **regular lattice** (`x_n=n`): tests dimensionality, ordering, and the exact ambient map;
2. **smooth density-matched mesh** (`x_n` with prime-number-theorem scale such as `n log n`): tests whether a phenomenon is only caused by nonuniform mean spacing;
3. **gap-marginal control**: preserve the multiset or empirical distribution of gaps while destroying their order, testing whether the observable sees merely one-gap statistics;
4. **ordered local controls**: preserve short blocks but destroy longer correlations, testing the relational depth of a proposed spectral memory.

A candidate that survives deeper controls has a progressively sharper claim about what arithmetic organization it is detecting.  These controls are diagnostics, not substitutes for proof.

## Evidence against overgeneralization

A universal carrier can still be mathematically essential.  The fact that the `1/4` boundary is non-arithmetic does not make the relative scattering operator useless; prime-specific residues may live inside its trace-class region or in subleading behavior.  Likewise, a classical transform can be the correct coordinate system for new arithmetic information.

The principle therefore forbids only the inference

\[
\text{observed on primes}\Rightarrow\text{caused by primes}.
\]

It does not require every interesting quantity to vanish on controls.

## Status / novelty

The integer-control calculation of PF-088 is proved.  The broader hierarchy of matched controls is a methodological mathematical principle, not a theorem about RH.  Its value is adversarial: it prevents universal geometry from being mistaken for arithmetic structure.

## Falsification criterion

The narrow principle is falsified only if a feature mathematically identical under the prime and control constructions can nevertheless be shown to encode a prime-specific distinction **without any additional residual data**.  For a concrete candidate, the decisive test is to compute the same invariant on progressively matched controls and identify the first level at which it changes.

## Lean-formalizable core

- Integer-control `p`-series criterion giving the `1/4` threshold.
- Abstract lemma: equality of an invariant on two inputs implies that invariant alone cannot distinguish those inputs.
- Finite-sequence permutation tests for observables depending only on a gap multiset versus ordered adjacent pairs/triples.
