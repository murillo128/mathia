---
id: CLUE-weil-inertia-kernel-checked-c2330-source-surplus
type: research-clue
status: proposed
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

The pinned environment was Lean `4.33.0-rc2`, Mathlib `51e6992efd06126df61a496bebf8f49482a4e129`, and Zeta23 `3635e74826a4c1fcece7d1cd2b6fa75e43a00510`. The completed checks were:

- `.venv/bin/python hunts/ainta_seven_point/four_point_preflight.py`: 1516 cell lemmas, 11863 leaves, 220 chunks, 13 boxes, 64 dispatch cases, zero problems.
- From the candidate package, `lake exe cache get`, `lake build Zeta23Ext.Bridge.Main`, and `lake build FourPoint.Base` succeeded. Native Lake then found competing `FourPoint.Base` modules before cell elaboration.
- The same pinned compiler completed all 48 candidate source modules using explicit candidate import maps, with commands of the form `lean -j8 -M20000 --setup=/tmp/mathia-119/direct-<module>.setup.json -o .lake/build/lib/lean/<module-path>.olean <module-path>.lean`. Each setup retained the successful Base setup's upstream import map and compiler options, changed its module name, and mapped checked candidate imports to their own package's artifacts. Cells0 completed with the same compiler and `--setup=/tmp/mathia-119/cells0.setup.json`, without the explicit resource flags. No Lean source or package configuration was edited; all frozen source hashes remained unchanged.
- Main actually printed the axiom dependencies of `Zeta23Ext.Bridge.FourPoint.F4_eq`, `cover1`, `four_point_cert`, `Phi_four`, `four_point_bound`, and `four_point_bound_ratio`: every list was exactly `[propext, Classical.choice, Quot.sound]`. The pinned workflow's forbidden-token check also passed on all 48 candidate Lean files.

Thus the result is **PASS — complete kernel check**, including the downstream declarations. The preflight's floating-point cell screen is diagnostic only; the mathematical evidence is the completed exact Lean proof.

## Research question

Does the checked artifact, after Research Watch verifies its correspondence to the actual MT kernel, common gap-pressure ledger and intended simple-critical zero counts, discharge WI-172's missing premise and establish its strict improvement over WI-036?

The exact proposed transfer is

\[
B_{2330}=\frac{14400000H_{\rm MT}-17240}{14366681},
\qquad
B_{2330}-B_{36}
=\frac{400365625H_{\rm MT}-97878440}{23068277981399}>0.
\]

WI-172 already derives this comparison using `H_MT>2/3`; no decimal approximation is needed. This return concerns that completed finite gate. The accepted kernel-constrained clue retains ownership of its broader optimal-resource question.

## Why it may matter

The checked source functional has a uniform margin of at least `20/10^6` above the `2310/10^6` input used in WI-166. Its actual MT pair weights depend on the same additive gaps as its pressure; WI-171's generic Gram witness cannot substitute for that coupling. The checked m=432 bridge gives `0.672860358838866...`, compared with WI-036's `0.672852930121184...`. The new evidence therefore changes the candidate's mathematical status and the supported strict-proportion frontier, subject to the owning watch's evidence integration.

## Decisive test

Reconstruct the formal-to-mathematical correspondence from the pinned `F4_eq`, `four_point_cert` and downstream statements, retaining pressure coefficient `1/2500`, the actual kernel definitions, and the intended zero counts. Check the existing admissibility identity `c(432-3)=999570/10^6<1` and WI-172's exact comparison above. Accept the finite transfer only if those links and the completed proof provenance agree; otherwise identify the precise mismatch. This test requires no alternate parameters, certificate generation or proof-tree modification.

## Evidence boundary

The external declarations have completed kernel checking, but this proposed handoff is not a canonical Mathia finding or a durable Mathia Lean formalization. Research Watch still owns correspondence review and integration of the result into persisted mathematical claims. The constant, emitted certificate and bridge are attributed external work; no novelty is claimed. This fixed-certificate improvement does not establish the optimal MT-constrained resource, improve arbitrary positive-cover architectures, defeat the single-profile ceiling discussed in WI-172, identify the exceptional complement, or imply RH.
