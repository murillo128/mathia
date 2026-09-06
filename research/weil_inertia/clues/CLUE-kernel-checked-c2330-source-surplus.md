---
id: CLUE-weil-inertia-kernel-checked-c2330-source-surplus
type: research-clue
status: resolved
origin: research-watch
target_line: weil_inertia
based_on:
  - research/weil_inertia/findings/WI-172-c2330-four-point-candidate-awaits-kernel-check.md
  - research/weil_inertia/findings/WI-036-multiscale-span-packing-recovers-full-m515-constant.md
  - research/weil_inertia/findings/WI-166-four-point-positive-cover-relaxation-is-sharp.md
  - research/weil_inertia/findings/WI-171-four-point-saturation-witness-is-uniformly-gram-realizable.md
  - research/weil_inertia/clues/CLUE-kernel-constrained-positive-cover-escape.md
---

# Does the checked c2330 certificate discharge WI-172's strict source-surplus gate?

## Observation

Independent compute execution of [issue #119](https://github.com/murillo128/mathia/issues/119) completed the previously missing kernel check of [the preserved external candidate](https://github.com/teal-sea/zeta-lab/blob/d28df5f992479cd32751cb90c8c88551550582a3/hunts/ainta_seven_point/lean-four-point/FourPoint/Main.lean), at exact commit `d28df5f992479cd32751cb90c8c88551550582a3`: `n=4`, `c=2330/1000000`, `p=2500`, `m=432`.

The pinned environment was Lean `4.33.0-rc2`, Mathlib `51e6992efd06126df61a496bebf8f49482a4e129`, and Zeta23 `3635e74826a4c1fcece7d1cd2b6fa75e43a00510`. The preserved preflight reproduced 1516 cell lemmas, 11863 leaves, 220 chunks, 13 boxes, 64 dispatch cases, and zero problems. After the frozen checkout's native-Lake `FourPoint.Base` name collision, the same pinned compiler completed all 48 candidate source modules with explicit import maps and no source or package-configuration edit. The principal axiom reports were exactly `[propext, Classical.choice, Quot.sound]`, and the forbidden-token audit passed all candidate Lean files.

## Research question

Does the checked artifact, after Research Watch verifies its correspondence to the actual MT kernel, common gap-pressure ledger and intended simple-critical zero counts, discharge WI-172's missing premise and establish its strict improvement over WI-036?

The exact proposed transfer is

\[
B_{2330}=\frac{14400000H_{\rm MT}-17240}{14366681},
\qquad
B_{2330}-B_{36}
=\frac{400365625H_{\rm MT}-97878440}{23068277981399}>0.
\]

## Evidence boundary

The external constant, emitted certificate and bridge are prior art; no novelty is claimed. A complete exact-source kernel replay establishes the finite formal gate, but the owning Research Watch must still check that the theorem is about the intended Montgomery--Taylor kernel and `N0simple/Ncount` objects before promoting the clue to canonical evidence.

This fixed-certificate improvement does not establish the optimal MT-constrained resource, improve arbitrary positive-cover architectures, defeat the single-profile ceiling, identify the exceptional complement, or imply RH.

## Research disposition

Outcome: supported

Resolved by:
- [[research/weil_inertia/findings/WI-172-c2330-four-point-candidate-awaits-kernel-check.md]]

Research Watch independently reconstructed the frozen formal interface. `Zeta23Ext.Bridge.Defs` defines the actual Montgomery--Taylor overlap kernel `K`, its normalized square `w`, and the common gap-pressure functional `F`; `FourPoint.F4_eq` unfolds the checked certificate to the six MT pair interactions at the additive distances of three nonnegative gaps; `four_point_cert` proves `2330/10^6 <= F 4 2500`; and the generic `n_point_bound` theorem consumes exactly that certificate plus the finite side conditions to conclude an eventual lower bound for `N0simple/Ncount`.

At `m=432`, the load-bearing cap is exact:

\[
\frac{2330}{10^6}(432-3)=\frac{999570}{10^6}<1.
\]

The frozen downstream declarations compile and give

\[
B_{2330}
=
\frac{14400000H_{\rm MT}-17240}{14366681}
=
0.6728603588388666595\ldots,
\]

which exceeds WI-036 by the exact positive expression above. WI-172 has therefore been strengthened from a conditional candidate-status finding to the canonical kernel-checked result. The broader `CLUE-kernel-constrained-positive-cover-escape` remains accepted because this resolves only its first bounded source-surplus test.
