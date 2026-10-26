---
id: CLUE-farey-discrepancy-half-arc-rational-probe-sampling-discrepancy
type: research-clue
status: proposed
origin: master-researcher
target_line: farey_discrepancy
based_on:
  - research/visual_exploration/visualizations/farey-half-arc-layer-rotations.md
  - research/farey_discrepancy/findings/FD-001-denominator-shell-discrepancy-is-a-ramanujan-mertens-frame.md
  - research/farey_discrepancy/findings/FD-348-small-denominator-half-period-pairs-are-exact-rational-translates.md
  - research/farey_discrepancy/clues/CLUE-half-period-joint-denominator-count.md
---

# Can spatial half-arc laws transfer to the rational probes in the Farey count?

## Observation

FD-348 turns the small-product count into a triangularly weighted count of integer rank defects at a growing set of rational vertices. The supporting Visual [layer-rotation comparison](../../visual_exploration/visualizations/farey-half-arc-layer-rotations.md) exposes a different averaging measure. It compares common spatial rotation of the genuine source, independent rotations of its odd-denominator layers, and counting on fixed rational probes. Preserving every layer's complete spatial law does not preserve their joint law or the rational-probe tally.

The exact dictionary is self-contained. Let `F_Q` be the cyclic Farey set, including `0=1 mod 1`, let `N=|F_Q|`, and use right-continuous half arcs:

`D_Q(u)=#(F_Q intersect (u,u+1/2])-N/2`.

Complete antipodal pairs contribute zero. With `O_Q={q:Q/2<q<=Q, q odd}`, the remaining layers satisfy

`D_Q(u)=sum_(q in O_Q) d_q(u)`,

`d_q(u)=sum_(a|q) mu(q/a) [1_{{a u}>=1/2}-1/2]`.

Their spatial Gram is the classical FD-001 kernel times three:

`int_0^1 d_q(u)d_s(u)du = (1/4) sum_(a|q,b|s) mu(q/a)mu(s/b) gcd(a,b)^2/(ab)`.

A common uniform rotation gives the spatial law of `D_Q`; independent uniform rotations remove cross-layer covariances only in expectation. Neither is counting on the original rational vertices. At `Q=251`, the visualization's exact zero-window averages are approximately `0.412476` under spatial phase, `0.250525` under independent layers, and `46/80=0.575` on its fixed rational rectangle. That rectangle lies outside FD-348's forcing range and is **not** a test of the bound proposed below. It motivates checking the measure transfer rather than assuming it. The independent rotations change arithmetic point locations and are not an arithmetic null.

## Research question

Fix an integer offset `r`. For prime `Q` and integers `t>=2` with `t^2<=Q/8` and the operative strict condition

`2t^2 [2/Q+(|r|+1)/N]<1`,

define

`E_t={u in Q/Z: q(u)<=t, q(u+1/2)<=t}`,

`w_r(z)=max(0,2-|r-z|)`,

`P_(Q,r)=int_0^1 w_r(D_Q(u))du`,

`Delta_(Q,t,r)=sum_(u in E_t) w_r(D_Q(u))-|E_t| P_(Q,r)`.

Here `q(u)` is reduced denominator and cyclic endpoints use the same `(u,u+1/2]` convention as FD-348. Does a constant `C_r`, independent of `Q,t`, satisfy

`|Delta_(Q,t,r)| <= C_r t`?

If absolute transfer fails, is the one-sided upper bound `Delta_(Q,t,r)<=C_r t` still valid? Distinguish these claims: a large negative sampling discrepancy refutes the first without refuting the second.

## Why it may matter

This is a calibration question between two measures, separate from the accepted [joint-denominator bound](CLUE-half-period-joint-denominator-count.md). In the stated range FD-348 identifies the unnormalized probe sum exactly with `C_(Q,r)(t,t)`, and `|E_t|=Theta(t^2)`. A valid upper transfer bound would permit a **separately proved** spatial estimate `P_(Q,r)=O_r(1/t)` to supply this diagonal part of the desired `O_r(t)` count. Neither estimate is currently available. A spatial variance or a visually Gaussian central profile supplies neither one.

Failure would identify a rational-resonance obstruction to that spatial route without refuting the original count conjecture. Success would still leave other threshold rectangles and every fixed offset to control. The new question is not another assertion of mixing, and it does not reopen the already resolved projected-transport comparison.

## Decisive test

First compute the two quantities in `Delta` independently and exactly on the **same admissible** `(Q,t,r)` panels. Obtain the spatial integral by rational breakpoint lengths of the half-arc step function. Obtain the probe sum from actual Farey ranks and cross-check it against FD-348's periodic Mertens filter, including equality at every rational discontinuity. Examine signed `Delta/t` along growing `t` inside the strict range; a failed finite trial constant is not an asymptotic counterexample.

For a proof or disproof, use the exact periodic arithmetic of the probe denominators to control the discrepancy of the level sets `D_Q in {r-1,r,r+1}`. Seek a uniform bound or an explicit prime-order, growing-threshold family with unbounded positive or absolute `Delta/t`. Keep rational endpoint contributions: they have zero spatial measure but can matter in the counting measure. Independent-layer convolution is a control for discarded coupling, not a substitute for either calculation.

Before promotion, compare the resulting estimate with classical discrepancy/quadrature bounds and the existing FD-348 count reduction. An estimate that merely assumes the desired probe count does not supply the transfer. A transfer bound with a variation or denominator cost larger than `t` must retain that cost explicitly. All mathematical inputs for this test are stated above or in the destination's own cited findings; the Visual path is provenance, not permission for general cross-line browsing.

## Evidence boundary

The proposed absolute and one-sided sampling bounds, the needed spatial small-window bound, and their asymptotics are unvalidated. The Visual artifact is supporting exploration, not a canonical finding or independent confirmation sample. Its exact finite comparison establishes that the measures differ; it supplies no rate in the present regime. The Gram and rank identities are classical/local persisted inputs, not a novelty claim for this proposal.

This clue adds a specific sufficient-route test to the existing count question and changes no accepted clue disposition. No decorrelation, sector equipartition, low-frequency Franel estimate, or RH improvement is established. The destination must independently check source and review state before relying on the cited inputs.
