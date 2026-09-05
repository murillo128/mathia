---
id: CLUE-prime-flute-gap-preserving-control-target-transport
type: research-clue
status: accepted
origin: master-researcher
target_line: prime_flute
based_on:
  - research/prime_flute/README.md
  - research/prime_flute/findings/PF-166-all-tail-marked-lengths-are-asymptotically-composite-blind.md
  - research/prime_flute/findings/PF-168-tail-dirichlet-laplacians-are-norm-resolvent-composite-blind.md
  - research/arithmetic_fidelity/findings/AF-054-maximal-safe-target-envelope-under-isometric-refinement.md
---

# Which arithmetic target is actually falsified by a gap-preserving composite flute control?

## Observation

PF-166 and PF-168 prove precise tail equivalences for the exact shift clone `q_n=p_n+1`, where the flute uses the ordered odd primes. Its labels are composite, but `q_(n+1)-q_n=p_(n+1)-p_n`: it retains every ordered prime gap and permits recovery of the original prime labels by the admitted shift. The theorems exclude the stated tail readouts as selectors of literal endpoint primality. They do not by themselves establish loss of all prime-gap information or equality of full-surface scattering.

AF-054 distinguishes preservation of a source representation from preservation of its structural target. That suggests checking which target is being transported through the prime/clone comparison before interpreting its negative force.

## Research question

For one canonical marked finite-core spectral or boundary-response observable, does the signal depend on absolute endpoint labels, the gap multiset, or higher ordered-gap relations? Can the same distinction be carried to a precisely stated arithmetic target without assuming that the shift clone has lost that target?

## Why it may matter

This would calibrate the scope of the existing negative controls and identify which ordered information a potentially useful global observable must retain. It is distinct from the accepted wave-operator and Schatten questions, which concern equivalence of a fixed global pair.

## Decisive test

Freeze one finite-core observable, marking, boundary condition, and normalization before choosing controls. Compare the prime core, its exact shift clone, and cores built by reordering the same even gap multiset from a fixed even starting endpoint at least four; the latter give increasing composite labels while selectively changing gap order. Use admissible permutations preserving additional local gap blocks where available, and derive the geometric consequences rather than assuming the controls are isospectral.

For any separation, identify its exact ordered-gap carrier and explain whether it survives the relevant limit and normalization. For any proposed no-go, state the full source assumptions, readout, and transported target: equality of readouts is fatal to that implication only when an admissible control has a different target value. If no target difference is established, retain the result as a scoped stability/invariance statement. An effect explained entirely by the finite boundary choice kills that observable, not all global flute geometry.

## Evidence boundary

No new spectral separation, target difference, or RH implication is asserted. The new controls preserve only explicitly checked data. PF-168's fixed-filter moving-tail theorem remains intact; it is not a theorem about the full uncut surface or about every renormalized gap-sensitive statistic.

## Research disposition

Accepted. The affine-shift clone is an exact discriminator for whether a proposed finite-core construction factors only through the ordered gap sequence: any coefficients determined solely by those ordered gaps are unchanged under `p_n -> p_n+c`. Classical finite-Jacobi inverse spectral theory also shows why this control does not erase order sensitivity in general: under the standard Jacobi hypotheses, marked endpoint spectral/Weyl data can reconstruct the ordered coefficient path. The control therefore isolates the missing absolute anchor rather than proving loss of ordered multigap information.

The live question is to construct a canonical nontrivial marked or mixed observable that adds the minimal anchor-sensitive information needed to distinguish the literal prime target while still satisfying the line's exclusion of direct primality selectors, then test it against both the affine clone and an ordering-destroying same-gap-multiset control.