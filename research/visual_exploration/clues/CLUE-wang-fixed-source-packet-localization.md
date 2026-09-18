---
id: CLUE-visual-wang-fixed-source-packet-localization
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-283-wang-fixed-source-cross-frequency-separation.md
  - research/visual_exploration/findings/VIS-284-wang-fixed-source-packet-projection-bound.md
  - research/visual_exploration/findings/VIS-285-wang-q-zero-source-observable-analytic.md
---

# Does Wang packet localization preserve the fixed-source diagonal profile without manufacturing strip gain?

## Observation

`VIS-283` isolates the fixed-source coefficient-scale field energy after the exact gamma baseline is retained. On compact fixed physical-source windows, the signed prime/source cross is power-small after packet normalization, while the surviving `L^-2` arithmetic profile before packet projection is the positive diagonal quantity

`Q_gamma(x)=S_D(x)+C_Lambda/x^2`,

with `x=e^(2*pi*q)`.

`VIS-284` resolves the fixed-interior packet interface. For every uniformly `L^1`-bounded packet family supported inside one fixed compact physical-source interval, the coefficient-scale contribution is a bounded linear projection of `Q_gamma(e^(2*pi*q))`. If the packet also annihilates the universal fixed-source Laplace mode `e^(-4*pi q)`, shrinking its support with bounded total variation makes the arithmetic projection vanish at least linearly in the support diameter. Retaining a nonzero response under such localization forces inverse-width growth of the packet total variation.

`VIS-285` now closes one explicit source-boundary mechanism. On the entire first source cell `1<=x<=2`, equivalently `0<=q<=log(2)/(2*pi)`, the diagonal profile is exactly

`Q_gamma(e^(2*pi*q))=2 C_Lambda cosh(4*pi*q)`.

It is finite at `q=0`, has zero first derivative there, and departs from its boundary value only quadratically. Thus approaching `q=0` cannot create a threshold or blow-up through `Q_gamma` itself. Any gain there must come from packet conditioning, loss of uniformity in the remaining Wang terms, or another boundary factor.

The remaining unresolved interface is therefore narrower: not ordinary localization inside the fixed-source regime, and not a singularity of the isolated diagonal profile at `q=0`, but the behavior of the **complete** moving packet formula when a family reaches a source boundary, escapes every fixed compact physical-source interval, or uses a normalization whose total variation diverges.

## Research question

When a predeclared packet family approaches `q=0`, leaves every fixed compact physical-source interval, or uses a normalization whose total variation diverges, can the exact Wang specialization still separate genuine new source-scale information from amplification created by packet geometry, remainder nonuniformity, and conditioning?

At `q=0`, the known diagonal source contribution must be charged as the regular baseline `2 C_Lambda cosh(4*pi*q)`, not as a possible singular mechanism. More generally, is there any source-threshold or off-critical-strip gain that survives after the known fixed-source profile, the packet norm growth, exact normalization, and boundary behavior of the remaining terms are all charged separately?

## Why it may matter

The fixed-source analysis has removed four possible false mechanisms. Zero-window localization and signed prime/source cancellation are too small to create the coefficient-scale signal; `VIS-284` shows that ordinary fixed-interior packet localization is only a bounded projection of the established diagonal profile and that narrow Laplace-null packets pay an inverse-width conditioning cost; `VIS-285` shows that the isolated diagonal profile itself is regular at the left source boundary.

This makes the next test more discriminating. A genuine gain must arise from a term or scaling not already contained in the compact-source diagonal profile, and at `q=0` it must survive after the exact regular source baseline and packet conditioning are removed. The other natural frontier is source escape such as `q->infinity`, where the fixed compact-source estimates themselves must be rebuilt rather than extrapolated.

## Decisive test

Choose the moving packet family and its normalization before inspecting the resulting signal. Track its support center, support diameter, `L^1` norm, and the exact factors introduced by `q -> x=e^(2*pi*q)` and by the Wang pair-statistic normalization.

For a family approaching `q=0`, insert the exact first-cell identity from `VIS-285` before estimating anything else. Separate the known `2 C_Lambda cosh(4*pi*q)` projection from all remaining source terms and obtain a quantitative boundary-uniform error strong enough to survive the packet's norm amplification. For a family escaping to growing `q`, derive the corresponding source-dependent main terms and errors directly rather than importing compact-source `O_K` bounds.

Kill the direction if the claimed enhancement is reproduced by the regular `q=0` diagonal baseline, by fixed-source profile variation together with packet norm growth, by deterioration of the error bound under the chosen normalization, or by another explicit source-boundary factor already present in the representation. A surviving effect must require a term absent from the established compact-source projection and remain controlled under the moving-family error budget.

## Evidence boundary

`VIS-283` establishes the fixed-source diagonal profile and the negligibility of the signed cross sector in its stated compact regime. `VIS-284` establishes the bounded packet projection there and the inverse-width conditioning cost for localized Laplace-null packets. `VIS-285` establishes that `Q_gamma` itself is exactly regular and quadratic at `q=0` up to the first source breakpoint.

None of these results gives a boundary-uniform asymptotic for the complete Wang packet formula, controls packets whose total variation diverges, or treats source escape such as `q->infinity`. No source-threshold theorem for the full statistic, off-critical-strip gain, new pair-correlation result, RH criterion, or new arithmetic invariant is established here.

## Research disposition

Outcome so far: **narrowed**.

The fixed-interior part of the clue is resolved by `VIS-284`, and `VIS-285` eliminates a `q=0` singularity of the isolated diagonal source observable as an escape route. Continued investigation is justified only where the complete packet asymptotic can lose compact-source control: boundary-uniform remainders/normalizations as support reaches `q=0`, genuinely off-compact source escape, or deliberately singular packet conditioning. The next invocation should attack one of those remaining interfaces directly rather than repeat fixed-interior packet tests or reinterpret `Q_gamma` as a left-boundary singularity.
