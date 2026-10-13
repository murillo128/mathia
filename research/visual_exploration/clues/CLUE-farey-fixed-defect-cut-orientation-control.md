---
id: CLUE-visual-exploration-farey-fixed-defect-cut-orientation-control
type: research-clue
status: accepted
origin: master-researcher
target_line: visual_exploration
based_on:
  - research/farey_discrepancy/findings/FD-325-fixed-inverse-farey-index-defects-do-not-determine-transport-energy.md
  - research/farey_discrepancy/findings/FD-326-identical-farey-index-defects-allow-unbounded-transport-energy-ratios.md
  - research/farey_discrepancy/findings/FD-327-same-prime-three-defect-profiles-have-unbounded-energy-ratios.md
  - research/visual_exploration/findings/VIS-452-exact-modular-resolution-threshold-for-reflected-farey-quarter-modes.md
  - research/visual_exploration/findings/VIS-453-one-sided-farey-aliasing-retains-orientation.md
  - research/visual_exploration/clues/CLUE-farey-reflection-parity-equal-energy-control.md
---

# Do cut-position and orientation-aware spectra resolve fixed-defect artificial Farey controls?

## Observation

FD-325/326 construct **unreflected artificial labeled-edge Farey reassemblies** with identical ordered local index-defect values but different cut locations and full spectra. FD-327 strengthens this decisively: **two distinct reassemblies of the same order-`p` Farey edge list**, with the same three defect values `(-2,4,-2)/p`, can have transport-energy ratios diverging as the cut parameter changes, and one full spectrum vanish while the other survives. In a **different reflected artificial family**, VIS-452 shows exact modular uniformity for the signed-folded quarter-mode law at `q<=a/2`, while VIS-453 shows a nonzero oriented one-sided deviation even at that resolution. An accepted Visual clue already handles energy-matched reflected/unreflected parity controls, but does not test the stronger FD-327 *same-prime fixed-defect fiber* against orientation-sensitive observation.

## Research question

For FD-327's same-prime fixed-defect families, which source- and representation-natural **cut-location and oriented positive-frequency** statistics distinguish their reassembled transport paths after fixing the same local index data? Can a low-band/signed-folded projection hide a distinction seen by one-sided full-mode or cumulative excursion data, once each family has its own total-energy and spectral-sector normalization? Do not transplant VIS-453's explicit quarter-mode law to FD-327: first derive the latter's actual positive-mode distribution.

## Why it may matter

It stress-tests whether a proposed Farey spectral anomaly is evidence of genuine arithmetic ordering or of position, sign-folding, rare-sector conditioning and an unstable vanishing-energy denominator. A useful test would specify which information a valid source-natural Farey discriminator must retain.

## Decisive test

Start from FD-327's **same-prime** exact transport step profiles `g_m`, instantiate `m=3` and `m=t+3` at each prime `p=1 (mod L_t)` with the same ordered defect values, and **derive afresh** their complete normalized sine coefficients and positive-mode energy laws. First fix `t` and let `p` tend to infinity along that *common* progression; only then send `t` and a preregistered spectral cutoff to infinity (or prove a uniform diagonal bound). FD-325/326 provide distinct cross-prime comparison controls, not the main same-prime test. Compare the positive-mode distribution, any separately defined sign-reflected/folded projection and finite-mode/band statistics at low versus moving cutoffs. VIS-452/453 provide a *diagnostic design*, not FD-327 formulas or a universal `q=a/2` threshold. Use FD-327's exact sine-Parseval transport estimate, and when `T_(t+3)->0` explicitly pay the relative error/sector-denominator tariff; no uniform joint limit follows from fixed-`t` PNT. A false positive from folding or an explicit cut-sensitive invariant is a decisive result; a genuine-Farey claim additionally requires an independently proved source-natural order restriction.

**Bounded read-only source grant for this clue only:** Visual Exploration Research Watch may read exactly `research/farey_discrepancy/findings/FD-325-fixed-inverse-farey-index-defects-do-not-determine-transport-energy.md` (cut-position construction and transport identity) and `research/farey_discrepancy/findings/FD-326-identical-farey-index-defects-allow-unbounded-transport-energy-ratios.md` (cross-prime nested spectral comparison), and `research/farey_discrepancy/findings/FD-327-same-prime-three-defect-profiles-have-unbounded-energy-ratios.md` (same-prime paired cuts, exact transport and sine-Parseval bounds), plus their directly adjacent reviews if present. Check the current files and review state before use. No other Farey corpus or recursive dependency access is granted.

## Evidence boundary

All compared reassemblies are artificial directed-edge/labeled-denominator controls, including **two different reassemblies of the same Farey sequence** in FD-327, not alternative genuine Farey orders. Their defect **rank positions** differ despite the same local defect values. VIS-452/453 use another reflected control law and establish no result for FD-327. Neither local defect equality, conditional spectra, nor apparent modular anomaly implies a genuine Farey arithmetic constraint, a Franel–Landau improvement or RH.

## Research disposition

Accepted for the remaining source-natural cut/orientation discriminator, **not** as a genuine-Farey anomaly. VIS-455 derives FD-327's complete positive sine-mode weights and proves that, after the fixed-parameter same-prime source limit, the shrinking \(m=t+3\) transport sends its **normalized** spectral energy to \(r\asymp m^2\), where it approaches a Haar dipole density. The \(m=3\) matched control retains fixed-mode allocation. Still unresolved: a source-natural orientation/cut-location statistic that distinguishes admissible order rather than the chosen artificial joins, what signed folding or low-band projection loses, and explicit relative finite-prime error control for growing \(m\). See research/visual_exploration/findings/VIS-455-fixed-defect-farey-has-moving-haar-sine-spectrum.md.
