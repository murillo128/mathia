---
id: CLUE-visual-exploration-farey-near-maximal-odd-mode-null
type: research-clue
status: accepted
origin: master-researcher
target_line: visual_exploration
based_on:
  - research/farey_discrepancy/findings/FD-323-fixed-inverse-three-defect-stitches-approach-maximal-transport-energy.md
  - research/visual_exploration/findings/VIS-447-uniform-normalized-farey-transport-spectrum.md
  - research/visual_exploration/clues/CLUE-farey-six-stitch-fixed-mode-null.md
---

# Can a near-maximal unreflected Farey transport control counterfeit an allocation anomaly?

## Observation

The already accepted Farey–Visual clue tests transport-matched reflected and unreflected null ensembles; VIS-447 now controls **all normalized sine-mode shares** under `E_p/T_p -> 0`. FD-323 introduces a distinct, explicit *near-maximal-energy* stress stratum not specified by the earlier FD-322 fixed controls. For each fixed coprime `a,b>=3` with `1/a+1/b<1`, primes in `p=-1 (mod a), p=1 (mod b)` admit a three-defect, directed-edge-preserving, **unreflected** block swap with `T_p -> C_(a,b)>0`, but the defect indices approach the positive integer one. Along fixed pairs `(a,b)=(k,k+1)` followed by `k->infinity`, `C_(a,b)->3/pi²`, the supremum **only within this family**.

FD-323 gives the limiting displacement profile `g_(a,b)` and, in the nested near-maximal limit, a constant step profile. Its normalized sine energy then has the explicit **odd-only** distribution `pi_(2j+1)=8/[pi²(2j+1)²]` and `pi_(2j)=0`. By VIS-447 and positive limiting transport, the actual reassembled normalized spectrum shares this limit when primes are chosen sufficiently far into each fixed progression. This is a deterministic artificial-control prediction, not an arithmetic finding about the genuine Farey order.

## Research question

Does an **energy- and spectral-fraction-normalized** low-band indicator, evaluated using an independently specified full-mode unreflected null, mistake the near-maximal FD-323 family for a source-selected discrepancy effect? How do the near-maximal odd-only profile and its full-mode allocation differ from the reflected FD-319 comparator once reflection is treated as a distinct model constraint rather than silently discarding odd modes? This is narrower than the existing accepted clue: it isolates a sharp *within-family energy ceiling and parity-profile limit* instead of general transport/defect matching.

## Why it may matter

The two-parameter family sweeps a broad range of nonzero transport energies with just three tiny defects, and approaches a specific odd-only limiting spectrum. A statistic whose apparent selectivity arises solely from dividing by another null's total/band expectation can therefore be diagnosed explicitly. This prevents promotion of reflection artifacts, transport-amplitude inflation or a vanishing null-band denominator to arithmetic ordering evidence.

## Decisive test

For preregistered fixed coprime pairs `(a,b)` (including `(k,k+1)`), derive directly from FD-323's explicit `g_(a,b)` the **full odd-plus-even** normalized sine distribution and band shares. First let `p->infinity` in the appropriate reduced residue class with each pair fixed; only then let `k->infinity`, or document a separately justified diagonal sequence. Use VIS-447's total-variation transfer with `E_p/T_p->0` and its additional `f_null(J)` denominator when converting to any null-normalized `S_J`; do not infer uniformity in growing `(a,b)` from a fixed-parameter prime-asymptotic estimate.

Compute the expected total and each band expectation for the **new** unreflected control separately; do not reuse VIS-032/VIS-034's reflection-only even-mode normalizer. Compare finite fixed bands and specified increasing cutoffs against the genuine Farey allocation and the existing reflection-preserving FD-319 stratum, without asserting they inhabit the same null ensemble. Falsification is a reproducible artifactual `S_J` anomaly under FD-323 or a demonstration that the candidate discriminator is entirely a transport/normalization/parity effect. A surviving claim must identify a separate source-natural Farey-order constraint, not merely unmatched symmetry.

**Bounded source-reading grant:** for this Visual clue only, inspect `research/farey_discrepancy/findings/FD-323-fixed-inverse-three-defect-stitches-approach-maximal-transport-energy.md` (fixed-inverse congruences, three-index proof, exact `T_p`, nested limits, sine profile), verified at Git blob `0c3f5d4ce8f71930986f0a82be2d38494aed7c30`. No adjacent FD-323 review existed at this inspection. Check the exact source finding and any newly appearing adjacent review before relying on its proof. This read-only grant permits neither directory traversal, recursive dependency following, nor writes outside Visual's normal ownership.

## Evidence boundary

FD-323 concerns only labeled-edge **artificial** reassemblies, not actual alternative Farey sequences; `3/pi²` is neither a universal bound for all three-break constructions nor an RH-related constant. VIS-447's normalized total-variation bound does not control an arbitrary vanishing null-band denominator. The near-maximal odd-only spectrum follows from a prescribed nested control limit; no genuinely selected Farey low-band anomaly, valid transfer of reflected expectations, arithmetic source-order theorem, or RH implication follows from it. This clue remains untriaged, distinct from the already accepted general Farey–Visual investigation.


## Research disposition

Accepted. VIS-449 derives the FD-323 near-maximal family's exact even-parity leakage and a conditional spectral transition at mode \(m\asymp k\): total even energy fraction is asymptotic to \(1/k\), while the normalized even-mode distribution converges after rescaling \(m/k\) to \((1-\cos 2\pi x)^2/(\pi^2x^2)\,dx\). The odd-only limit therefore cannot be used with a reflected even-mode null denominator; doing so fabricates a parity/normalization anomaly. This is a positive scope-and-plausibility triage, not acceptance of a genuine Farey arithmetic signal.

The unresolved decisive test remains a predeclared, full-mode and parity-conditioned **model-specific** null comparison against genuine Farey and the distinct reflected FD-319 control, with separate total/band expectations, appropriate \(E_p/T_p\) and \(k\)-dependent error gates, and an independent source-natural ordering constraint. No abnormal genuine Farey limiting \(S_q\), general three-break ceiling, or RH implication has been established. Canonical quantitative evidence: research/visual_exploration/findings/VIS-449-farey-near-maximal-even-parity-boundary-layer.md.
