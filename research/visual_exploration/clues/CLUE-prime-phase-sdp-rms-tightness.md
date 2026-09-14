---
id: CLUE-visual_exploration-prime-phase-sdp-rms-tightness
type: research-clue
status: resolved
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
  - research/visual_exploration/findings/VIS-225-coherent-prime-blocks-force-divergent-ising-scale.md
---

# Can the symmetric-taper prime sign Hamiltonian stay at Haar-RMS scale?

## Observation

`VIS-218` closes the normalized magnetic-ground-state relaxation throughout the strictly subcritical regime, and `VIS-220` closes the fractional simple-cycle packing relaxation by a universal envelope ceiling. `VIS-221` then identifies the full correlation SDP as a strictly stronger static interaction certificate,

`U_abs(A)=max_(X>=0,diag(X)=1)|Tr(A X)|`.

`VIS-222` removes the unbounded-relaxation ambiguity through the complex symmetric Grothendieck inequality. `VIS-223` uses midpoint symmetry of the canonical tapers to gauge the prime coefficient matrix to a real symmetric signed ratio-shell matrix `B`. `VIS-224` finally shows that

`I_abs(B)=max_(epsilon_i in {+1,-1}) |epsilon^T B epsilon|`

has the same bounded-versus-divergent scale as the exact torus objective and real correlation SDP up to a universal factor.

`VIS-225` now supplies the missing prime-specific lower bound. Partitioning the top-half primes into Fourier-unresolved ratio cells makes every within-cell centered-taper coupling positive. Choosing one Rademacher sign per cell and averaging over the cell signs cancels cross-cell terms while preserving all positive within-cell mass. The same PNT occupancy mechanism used in `VIS-218` then gives

`I_abs(B_(y,H)) >>_(alpha,v) y/(H log y)`

throughout

`H->infinity`, `H log y/y ->0`.

Since `VIS-192` gives `R_v(y,H) asymp 1/H`,

`I_abs(B_(y,H))/sqrt(R_v(y,H))`
` >>_(alpha,v) y/(sqrt(H) log y)`
` -> infinity`.

## Research question

For the canonical centered real signed prime matrices `B_(y,H)` in the strictly subcritical regime, what is the asymptotic scale of

`I_abs(y,H)=max_(epsilon_p in {+1,-1}) |epsilon^T B_(y,H) epsilon|`?

Does `I_abs=O(sqrt(R_v))` hold in any nontrivial growing strictly subcritical regime, or must the normalized ratio diverge?

## Why it may matter

By `VIS-224`, this binary sign question decides the coarse bounded-versus-divergent scale of the exact continuous-phase worst-start objective and the real-elliptope SDP. A divergent binary certificate means continuous phases and higher-rank SDP correlations are not creating the obstruction: the symmetric-taper prime Hamiltonian already has a coarse real-sign organization that exceeds Haar RMS.

This also sharpens the matched-control problem. A useful control for further quantitative work should preserve the coupling magnitudes and real signed-shell representation while perturbing the prime organization; arbitrary independent complex edge phases are not representation-matched.

## Decisive test

The decisive test was to obtain a representation-matched analytic lower bound for the signed ratio-shell kernel in the complete strictly subcritical regime.

`VIS-225` does this by grouping top-half primes into cells of additive width `asymp y/H`, on which `H log(q/p)` stays inside the positive neighborhood of the centered taper response. One shared sign per cell preserves every such positive edge, while independent signs across cells annihilate all other terms in expectation. PNT cell occupancy then forces total retained coupling mass `>> y/(H log y)`.

Together with `R_v asymp 1/H`, this proves normalized divergence and passes the decisive test.

## Evidence boundary

`VIS-225` proves only the bounded-versus-divergent scale in the strictly subcritical regime. It does not identify the exact maximizing sign pattern, the sharp asymptotic constant, the critical transition `H asymp y/log y`, supercritical behavior, or the one-parameter time needed for the physical prime-log orbit to approach a near-maximizing torus point.

Those are separate research questions. The resolved clue is not evidence beyond the linked canonical finding.

## Research disposition

Outcome: supported

Resolved by:
- [[research/visual_exploration/findings/VIS-225-coherent-prime-blocks-force-divergent-ising-scale]]

The accepted alternative is decided: throughout the stated strictly subcritical regime,

`I_abs(B_(y,H))/sqrt(R_v(y,H)) -> infinity`.

By `VIS-224`, the exact torus worst-start objective and real correlation SDP diverge on the same normalized scale up to universal multiplicative constants. Critical/supercritical behavior and access time remain separate frontier questions rather than unfinished parts of this clue.