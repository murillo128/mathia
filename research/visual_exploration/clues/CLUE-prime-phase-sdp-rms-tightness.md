---
id: CLUE-visual_exploration-prime-phase-sdp-rms-tightness
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-213-worst-start-prime-phase-torus-optimization.md
  - research/visual_exploration/findings/VIS-216-normalized-magnetic-gap-certificate.md
  - research/visual_exploration/findings/VIS-218-subcritical-effective-edge-density-closes-magnetic-rms.md
  - research/visual_exploration/findings/VIS-220-simple-cycle-packing-universal-envelope-ceiling.md
  - research/visual_exploration/findings/VIS-221-sdp-stress-certificate-retains-torus-interactions.md
  - research/visual_exploration/findings/VIS-222-symmetric-grothendieck-constant-factor-sdp-torus-equivalence.md
---

# Can the full correlation SDP compress prime-phase worst starts to Haar-RMS scale?

## Observation

`VIS-218` closes the normalized magnetic-ground-state relaxation throughout the strictly subcritical regime, and `VIS-220` closes the fractional simple-cycle packing relaxation by a universal envelope ceiling. `VIS-221` then identifies the full correlation SDP as a strictly stronger static interaction certificate:

`U_abs(A)=max_(X>=0,diag(X)=1)|Tr(A X)|`.

`VIS-222` substantially sharpens the interpretation. Friedland--Lim's complex symmetric Grothendieck inequality applies to exactly the Hermitian pair present here and gives

`M_abs(A)<=U_abs(A)<=K_gamma^C M_abs(A)`,

with `K_gamma^C<=8/pi-1`, where

`M_abs(A)=max_(|z_i|=1)|z^*Az|`.

Since `VIS-213` identifies `M_abs(A_(y,H))` with the exact fixed-parameter prime-phase worst-start supremum, the correlation SDP and true torus optimum have the same asymptotic scale up to a universal constant. The relaxation rank can matter for exact optimizer recovery, but no longer creates an unbounded ambiguity in objective scale.

## Research question

For the canonical prime coefficient matrices `A_(y,H)` in the strictly subcritical regime, what is the asymptotic scale of

`U_abs(y,H)=max(U_+(A_(y,H)),U_+(-A_(y,H)))`?

Does

`U_abs(y,H)=O(sqrt(R_v(y,H)))`

hold in any nontrivial growing regime, or does

`U_abs(y,H)/sqrt(R_v(y,H)) -> infinity`?

By `VIS-222`, this is simultaneously the bounded-versus-divergent scale question for the exact fixed-modulus torus optimum and hence for the fixed-parameter worst-start supremum.

## Why it may matter

This is the first post-`VIS-220` route whose asymptotic objective scale transfers both ways to the exact torus problem. A bounded SDP/RMS ratio immediately proves an RMS-scale pointwise upper bound on the true worst-start amplitude. A divergent SDP/RMS ratio now has equally direct content: the exact torus optimum must also exceed RMS by a divergent factor, within the universal symmetric-Grothendieck constant.

Rank-one tightness remains more informative at finite parameters because a PSD stationary stress identifies the exact optimizer and exact value, but it is no longer required to infer the asymptotic objective scale.

## Decisive test

Freeze a growing family of canonical `(y,H)` values and, for both signs of `A_(y,H)`, evaluate or analytically bound

`max Tr(±A X)` subject to `X>=0`, `diag(X)=1`.

Normalize by the exact Haar scale `sqrt(R_v(y,H))`. The decisive mathematical outcomes are now:

1. prove `U_abs/sqrt(R_v)=O(1)` in a stated growing regime; by `VIS-222` this gives the same bounded scale for the exact torus/worst-start objective;
2. prove `U_abs/sqrt(R_v)->infinity`; by `VIS-222` this forces the exact torus/worst-start ratio to diverge as well;
3. at finite parameters, when an SDP optimizer is rank one, certify the corresponding stationary stress as positive semidefinite to recover the exact torus optimizer and value, not merely its universal-factor scale.

Finite numerical SDP panels may guide which analytic regime to attack, but they remain exploratory until converted into a durable analytic bound or exact certificate. When interpreting arithmetic specificity, use matched controls that preserve the weight matrix while varying admissible edge phases rather than controls that change the scale being measured.

## Evidence boundary

`VIS-221` proves the SDP hierarchy and exact rank-one stress certificate. `VIS-222` proves the universal constant-factor comparison between the optimal SDP value and exact unit-modulus quadratic optimum by specializing the classical complex symmetric Grothendieck inequality. Neither result estimates the actual asymptotic SDP value on the canonical prime matrices.

The clue therefore remains an open scale problem. What is no longer open is the interpretation of a large high-rank SDP value: it cannot be attributed solely to an unbounded correlation-relaxation gap. One-parameter prime-log access time to near-maximizing torus regions remains separate from this static objective question.

## Research disposition

Accepted. The symmetric-Grothendieck bridge removes the previous relaxation-gap ambiguity and makes the SDP scale itself a faithful constant-factor proxy for the exact static worst-start scale. The unresolved task is now the prime-specific asymptotic estimate for `U_abs(A_(y,H))/sqrt(R_v(y,H))`.