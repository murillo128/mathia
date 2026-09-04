---
id: CLUE-visual-exploration-zeta-rh-canonical-visual-atlas
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/README.md
  - research/visual_exploration/findings/VIS-021-gram-occupancy-is-discrete-S-increment.md
---

# Which canonical visualizations of zeta and RH should be treated as baseline instruments rather than endpoints?

## Observation
Before inventing exotic representations, the Visual Researcher would benefit from a compact, reproducible baseline atlas of the standard ways ζ and RH are made visible. Canonical views encode different mathematics and can expose whether a supposedly new pattern is already a familiar consequence of zeros, the functional equation, zero counting, phase winding, or prime/zero duality. They are therefore useful both as inspiration and as negative controls against rediscovering known structure in a prettier coordinate system.

The first independence audit already removes one apparent multiplicity of views. `VIS-021` shows exactly that the Gram-sampled zero-counting residual is `S(g_n)` and that the occupancy `C_n` of consecutive Gram intervals satisfies `C_n = 1 + S(g_{n+1})-S(g_n)`. Thus zero-counting residuals, sampled argument residuals, and Gram-interval occupancy maps are algebraically interconvertible up to one initial integer. Repetition across those pictures is not cross-representation corroboration.

## Research question
Can a small set of mathematically independent canonical ζ/RH views be reproduced on matched windows and scales, with their exact constructions documented, and then used to identify cross-view features that survive representation changes **after algebraically recoverable views have been quotiented into one baseline family**?

Candidate baseline families include complex-plane domain/phase coloring of `ζ(s)` or `ξ(s)`; modulus and level-set portraits across the critical strip; Hardy `Z(t)` on the critical line with its zeros; the zero-counting/argument/Gram-occupancy family delimited by `VIS-021`; local zero-spacing/statistics views; and explicit-formula style prime-versus-zero oscillation pictures. The goal is not completeness but a minimal visual grammar for distinguishing intrinsic structure from rendering novelty.

## Why it may matter
A canonical atlas gives the line a reference frame. New visual experiments can be compared against known encodings instead of being judged in isolation, while features repeated across genuinely different representations become better candidates for exact mathematical questions. It can also reveal blind spots: structures that are obvious in one classical view but disappear in another may point directly to what information a representation preserves or forgets.

The independence quotient matters as much as reproduction quality. Without it, several attractive panels can appear to agree while merely restating one argument-principle identity. `VIS-021` supplies the first exact example of how the atlas should collapse such redundancy before using cross-view persistence as a clue generator.

## Decisive test
Perform a focused prior-art survey to select a compact set of canonical visualizations with clear mathematical definitions. Reproduce them over shared regions/heights wherever meaningful, recording normalization, truncation, phase conventions, zero data, and numerical method. Before treating two views as independent, test whether one is algebraically recoverable from the other under the chosen sampling; use `VIS-021` as the baseline example of a family that must be merged.

For several known phenomena — individual zeros, critical-line crossings, zero-counting fluctuations, Gram behavior, local spacing structure, and prime/zero oscillatory correspondence where appropriate — determine which **independent families** show the phenomenon and why. Then test at least one proposed cross-family statistic or correspondence that can be stated without pictures. If the atlas merely reproduces known identities with no reusable control value or new falsifiable question, retain only the minimum useful baseline material and do not promote it to a finding.

## Evidence boundary
The existence of visually similar features across canonical plots does not establish a new invariant, theorem, or RH criterion. The listed families are candidate baseline instruments subject to prior-art verification and careful numerical construction. `VIS-021` proves only an exact redundancy inside the counting/argument/Gram-occupancy family; it does not establish independence of the remaining candidate families. The clue proposes building and auditing that baseline, not claiming novelty for any classical visualization.

## Research disposition
Accepted in independence-audited form. The atlas is worth building as a reusable falsification instrument, but its unit of comparison must be a mathematically non-recoverable representation family rather than a panel count. The next useful step is to reproduce a representative from a genuinely different family and explicitly test whether its proposed cross-view feature survives the exact recoverability controls already exposed by current findings.
