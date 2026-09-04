# MI-011 — Coherent exact description has an entropy and atomicity gate that pointwise tolerance complexity can miss

**Evidence level:** supported by AF-116--AF-119; exact for the stated countable-mark and nested-partition models, with classical coding/entropy inputs

## Core intuition

Finite repair at every positive tolerance is weaker than finite information cost for one exact coherent representation. Rare states can be discarded separately at each tolerance, so every fixed-error codebook may stay finite even while the cumulative exact description requires infinite expected information.

The correct resource is therefore not only how many labels are needed at one scale, but whether the **same coherent refinement hierarchy** accumulates a summable amount of new information. Once the hierarchy genuinely generates the source, bounded terminal entropy is possible exactly for finite-entropy atomic sources.

## Strongest justified principle

AF-116 separates label count, worst-case bits, and probability-weighted description length. AF-117 identifies the one-shot mean-bit endpoint: finite Shannon entropy is exactly the finiteness gate for countable prefix-coded repair, up to the universal one-bit coding gap. Finite entropy implies finite-alphabet repair after arbitrarily small extra error, but the extra tolerance cannot be removed uniformly at zero error.

AF-118 converts the whole tolerance profile of one fixed mark into an exact resource statistic. If `K_p(epsilon)` is the minimal retained probability rank, then

`integral_0^1 log_2 K_p(epsilon) d epsilon = E[log_2 J]`,

and this log-rank area is finite if and only if the mark has finite Shannon entropy, with uniform comparison over families. Pointwise finiteness of `K_p(epsilon)` is therefore insufficient; its logarithmic growth must be integrable as tolerance tends to zero.

AF-119 closes the coherence gap. For nested generating partitions, the partition entropies increase to the entropy of the full measured source. Their supremum is finite if and only if the source is purely countably atomic with finite atom entropy. Equivalently, the cumulative conditional-entropy innovation budget is finite exactly in that regime. A nonatomic source cannot be encoded exactly by a generating refinement tower with uniformly bounded entropy even if each positive tolerance admits a finite quantizer.

## What remains possible

This is an information-budget theorem, not a provenance theorem. A low-entropy auxiliary mark can still be arbitrary, target-tuned, or noncanonical. Conversely, a source application may require only a declared positive tolerance or a non-generating statistic, in which case the exact atomicity obstruction need not apply.

A positive arithmetic application should identify the actual terminal sigma-field or target quotient that must be generated, then prove both the entropy budget and the naturality of the mark from the source rather than choosing a code after seeing the target.

## Status / novelty

Kraft--McMillan, Shannon entropy, ranked probabilities, partition entropy, and generating quantizers are classical. The synthesis is the multiscale fidelity gate: **per-tolerance finite repair does not imply a finite coherent exact description; exact bounded-information generation forces finite-entropy atomicity**.

## Falsification criterion

Exhibit a nonatomic standard probability source with an exactly generating nested partition hierarchy of uniformly bounded entropy, or a countable mark with finite integrated log-rank area but infinite Shannon entropy under the AF-118 hypotheses. A destination that does not require exact generation lies outside the claim.

## Lean-formalizable core

- Entropy versus mean prefix length.
- Tolerance-rank log-area identity and entropy finiteness equivalence.
- Monotone entropy of refining partitions.
- Finite terminal entropy iff finite-entropy atomicity.
