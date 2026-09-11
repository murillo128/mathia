# MI-001 — Farey occupation is a sparse multiplicative-placement problem, not a growth-exponent problem

**Evidence level:** supported

## Core intuition

The Farey obstruction has been narrowed from generic regularity to a very thin exceptional-set problem. The physical shell source already has the correct zeta-zero power exponent on every fixed row, terminal nonsquarefree occupation is uniformly positive through quotient depth `o(sqrt H)`, and exact dilation relations prevent very small occupation from persisting on a positive amount of logarithmic scale.

A remaining failure must therefore be **subpower, logarithmically sparse, and concentrated in low-row multiplicative placement**. Ordinary smoothness or another average theorem is no longer the right currency.

## Strongest justified claim

FD-031--FD-048 establish the underlying hierarchy. Terminal quotient blocks have positive nonsquarefree density; the physical shell source and Mertens function are inverse floor transforms with the same zero-frontier exponent; fixed nonsquarefree dilation injects a lower-horizon copy of the full energy; and even strong short-interval smoothing does not by itself prevent sparse low-row escape.

FD-049 combines the lower-scale injection with the zero-frontier envelope. For fixed head dimension, if `nu_H` is nonsquarefree occupation and `epsilon_H` the normalized Schur defect, then neither can have a positive polynomial decay exponent beyond `2 Theta-1`. Under RH (`Theta=1/2`), `H^eta nu_H` and `H^eta epsilon_H` diverge for every `eta>0`. Any residual decay is necessarily subpower.

FD-050 turns the same dilation identity into a global logarithmic entropy bound. In the natural `dH/H` measure, the average of `log(1/nu_H)` stays bounded by an explicit dilation constant. Consequently horizons where `nu_H` falls below any threshold tending to zero have vanishing logarithmic density. Sparse bad scales can wander between multiplicative chains, but they cannot occupy a macroscopic fraction of logarithmic scale.

FD-051 removes the earlier cube-root limitation on the source-independent terminal bulk. Finite prime-square sieves recover the full nonsquarefree density constant from below for arbitrary nonnegative shell profiles whenever the quotient depth is `o(sqrt H)`. The square-root block scale is sharp for such profile-independent reasoning because singleton squarefree blocks appear there.

## Synthesis of evidence

The residual obstruction is now highly constrained. It cannot be a missing growth exponent, broad terminal loss, persistent multiplicative-chain deficit, positive-log-density phenomenon, or ordinary short-interval roughness. It must use rare horizons where energy is pushed into the low Jordan rows / long quotient arguments in a way compatible with the exact physical increment law.

A decisive theorem should therefore couple divisibility across neighboring scales, exploit the explicit increment formula, or otherwise show that the physical source cannot realize the remaining low-row exceptional geometry. Conversely, a physical-compatible construction with `nu_H -> 0` on a sparse subpower subsequence would show that even these multiplicative constraints do not suffice.

## Counterevidence / boundary cases

FD-049 permits inverse-logarithmic or other subpower occupation loss. FD-050 permits exceptional horizons of zero logarithmic density. FD-051 controls only the terminal quotient region and explicitly leaves low rows uncontrolled. These gaps overlap rather than disappear.

The smooth synthetic controls used earlier do not satisfy the exact physical increment/divisibility law, so they do not demonstrate that the surviving exceptional regime is realizable by the Farey source.

## Epistemic status

**Supported exceptional-set narrowing:** any remaining occupation collapse must be subpower, globally logarithmically sparse, and carried by low-row arithmetic placement beyond the universal terminal bulk.

## Novelty/prior-art status

No broad novelty claim is made beyond the finding-level audits. This note synthesizes the exact zero-frontier, dilation, logarithmic-average, and finite-square-sieve consequences.

## Falsification criterion

Construct a source obeying the exact physical increment/floor-transform laws with occupation tending to zero on an unbounded subsequence while respecting FD-049--FD-051, or prove those laws force a positive pointwise lower bound. Either outcome resolves the current diagnosis.