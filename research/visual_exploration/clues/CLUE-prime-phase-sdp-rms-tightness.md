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
  - research/visual_exploration/findings/VIS-223-midpoint-symmetric-taper-real-elliptope.md
  - research/visual_exploration/findings/VIS-224-midpoint-symmetric-taper-ising-constant-factor-equivalence.md
---

# Can the symmetric-taper prime sign Hamiltonian stay at Haar-RMS scale?

## Observation

`VIS-218` closes the normalized magnetic-ground-state relaxation throughout the strictly subcritical regime, and `VIS-220` closes the fractional simple-cycle packing relaxation by a universal envelope ceiling. `VIS-221` then identifies the full correlation SDP as a strictly stronger static interaction certificate,

`U_abs(A)=max_(X>=0,diag(X)=1)|Tr(A X)|`.

`VIS-222` removes the unbounded-relaxation ambiguity through the complex symmetric Grothendieck inequality:

`M_abs(A)<=U_abs(A)<=K_gamma^C M_abs(A)`,

where `M_abs(A)` is the exact fixed-modulus torus objective from `VIS-213`.

`VIS-223` then uses midpoint symmetry of the canonical tapers to remove the observation-origin phase. After diagonal switching,

`A_(y,H)=D_H^* B_(y,H) D_H`

with `B_(y,H)` real symmetric, and the full complex correlation SDP collapses exactly to the real elliptope.

`VIS-224` adds the final representation reduction needed for coarse asymptotic scale. Define

`I_abs(B)=max_(epsilon_i in {+1,-1}) |epsilon^T B epsilon|`.

The real symmetric Grothendieck inequality gives the pointwise chain

`I_abs(B) <= M_abs(A) <= U_abs^R(B) <= K_gamma^R I_abs(B)`,

with `K_gamma^R<=sqrt(2)(8/pi-1)<2.188`.

Therefore the binary Ising sign optimum, exact continuous-phase torus optimum, and real correlation SDP all have the same bounded-versus-divergent RMS-normalized asymptotic scale up to a universal factor. Continuous vertex phases are no longer necessary to decide that coarse scale in the midpoint-symmetric branch.

## Research question

For the canonical centered real signed prime matrices `B_(y,H)` in the strictly subcritical regime, what is the asymptotic scale of

`I_abs(y,H)=max_(epsilon_p in {+1,-1}) |epsilon^T B_(y,H) epsilon|`?

Does

`I_abs(y,H)=O(sqrt(R_v(y,H)))`

hold in any nontrivial growing regime, or does

`I_abs(y,H)/sqrt(R_v(y,H)) -> infinity`?

By `VIS-224`, this is equivalent up to a fixed universal factor to the same bounded-versus-divergent question for the exact prime-torus worst-start supremum and for the full real-elliptope SDP value.

## Why it may matter

The live static question is now combinatorial rather than intrinsically continuous-phase. For midpoint-symmetric tapers the coefficients form an explicit real signed ratio-shell kernel, and the binary hypercube already captures the exact worst-start objective scale within a universal factor.

This substantially sharpens the matched-control problem. A useful control should preserve the coupling magnitudes and the real signed-shell class while perturbing the arithmetic organization; injecting arbitrary independent complex edge phases is no longer representation-matched to the canonical symmetric taper.

A bounded sign/RMS ratio would prove Haar-RMS-scale worst starts immediately through `VIS-224`. A divergent sign/RMS ratio would itself force divergent exact worst starts. There is no remaining loophole in which continuous phases or high-rank SDP correlations alone create the asymptotic scale separation.

## Decisive test

Freeze a growing family of canonical `(y,H)` values and study the exact signed quadratic form

`epsilon^T B_(y,H) epsilon`, `epsilon_p in {+1,-1}`,

normalized by `sqrt(R_v(y,H))`.

The decisive mathematical outcomes are:

1. prove `I_abs/sqrt(R_v)=O(1)` in a stated growing regime; `VIS-224` then gives the same bounded scale for the exact torus/worst-start objective and the real SDP;
2. prove `I_abs/sqrt(R_v)->infinity`; the binary sign assignments themselves then witness divergent worst-start scale;
3. derive a representation-matched analytic upper/lower comparison for the signed ratio-shell kernel that survives controls preserving edge magnitudes and shell-sign statistics while perturbing prime arithmetic organization.

For the quadratic taper, use the centered coupling

`B_(p,q)=Q_y^(-1)p^(-alpha)q^(-alpha) r_w(H log(q/p))`,

where

`r_w(u)=12[2 sin(u/2)-u cos(u/2)]/u^3`.

Its coupling signs are deterministic multiplicative ratio shells. A finite numerical Ising/SDP panel may guide which regime to attack, but it remains exploratory until converted into a durable analytic bound or exact certificate. Do not interpret a generic complex-phase scramble as a matched null for this symmetric-taper question.

## Evidence boundary

`VIS-221` proves the SDP hierarchy and exact rank-one stress certificate. `VIS-222` proves a universal constant-factor comparison between the complex correlation SDP and exact unit-modulus quadratic optimum. `VIS-223` proves that midpoint-symmetric tapers gauge the canonical coefficient matrix to a real signed matrix and collapse the SDP to the real elliptope. `VIS-224` proves the additional real symmetric-Grothendieck comparison with the binary sign hypercube.

None of these results estimates the prime-specific asymptotic value of `I_abs(B_(y,H))/sqrt(R_v(y,H))`. The clue therefore remains open. What is now closed is the need to distinguish the coarse asymptotic scale of the continuous torus, binary signs, and real SDP in the midpoint-symmetric branch: they differ by at most a universal multiplicative constant.

One-parameter prime-log access time to near-maximizing torus regions remains a separate simultaneous-Diophantine issue and is not addressed by the sign reduction.

## Research disposition

Accepted. The unresolved static problem is now the arithmetic scale of the centered real signed prime Hamiltonian. The binary sign optimum is the simplest representation-matched proxy whose boundedness or divergence already decides the exact worst-start/RMS scale up to a universal constant.