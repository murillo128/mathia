---
id: CLUE-visual-wang-fixed-source-packet-localization
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-283-wang-fixed-source-cross-frequency-separation.md
  - research/visual_exploration/findings/VIS-284-wang-fixed-source-packet-projection-bound.md
---

# Does Wang packet localization preserve the fixed-source diagonal profile without manufacturing strip gain?

## Observation

`VIS-283` isolates the fixed-source coefficient-scale field energy after the exact gamma baseline is retained. On compact fixed physical-source windows, the signed prime/source cross is power-small after packet normalization, while the surviving `L^-2` arithmetic profile before packet projection is the positive diagonal quantity

`Q_gamma(x)=S_D(x)+C_Lambda/x^2`,

with `x=e^(2*pi*q)`.

`VIS-284` now resolves the fixed-interior packet interface. For every uniformly `L^1`-bounded packet family supported inside one fixed compact physical-source interval, the coefficient-scale contribution is a bounded linear projection of `Q_gamma(e^(2*pi*q))`. If the packet also annihilates the universal fixed-source Laplace mode `e^(-4*pi q)`, shrinking its support with bounded total variation makes the arithmetic projection vanish at least linearly in the support diameter. Retaining a nonzero response under such localization forces inverse-width growth of the packet total variation.

The remaining unresolved interface is therefore not ordinary localization inside the fixed-source regime. It is the transition to a source boundary, escaping source scale, or singular packet normalization where the compact bounded-projection argument no longer applies.

## Research question

When a predeclared packet family approaches the relevant source boundary, leaves every fixed compact physical-source interval, or uses a normalization whose total variation diverges, can the exact Wang specialization still separate genuine variation of the source profile from amplification created by packet geometry and conditioning?

In particular, is there any source-threshold or off-critical-strip gain that survives after the known fixed-source profile, the packet norm growth, and the exact normalization are all charged separately?

## Why it may matter

The fixed-source analysis has now removed three possible false mechanisms. Zero-window localization and signed prime/source cancellation are too small to create the coefficient-scale signal, and `VIS-284` shows that ordinary fixed-interior packet localization is only a bounded projection of the already established diagonal profile. A visually or numerically strong signal produced by narrowing a Laplace-null packet can therefore be explained by its conditioning unless a new source regime is actually entered.

This sharpens the next test. A genuine gain must arise at a mathematically identifiable boundary of the fixed-source representation rather than from the freedom to choose a narrower or more highly normalized test function inside it.

## Decisive test

Choose the moving packet family and its normalization before inspecting the resulting signal. Track its support center, support diameter, `L^1` norm, and the exact factors introduced by `q -> x=e^(2*pi*q)` and by the Wang pair-statistic normalization.

Derive the contribution directly from the exact source representation. First subtract or match the already established `Q_gamma` projection and the universal Laplace mode. Then determine whether the residual gain remains after charging the packet's norm amplification and the quantitative remainder required to justify that amplification.

Kill the direction if the claimed enhancement is reproduced by the fixed-source diagonal profile together with packet norm growth, by the source-boundary factor already present in the representation, or by a normalization singularity. A surviving effect must require a term that is absent from the established compact-source projection and remains controlled under the moving-family error budget.

## Evidence boundary

`VIS-283` establishes the fixed-source diagonal profile and the negligibility of the signed cross sector in its stated compact regime. `VIS-284` establishes the bounded packet projection there and the inverse-width conditioning cost for localized Laplace-null packets. Neither result gives a uniform asymptotic for packets whose support approaches a source boundary, escapes the compact fixed-source regime, or whose total variation diverges. No source-threshold theorem, off-critical-strip gain, new pair-correlation result, RH criterion, or new arithmetic invariant is established here.

## Research disposition

Outcome so far: **narrowed**.

The fixed-interior part of the clue is resolved by `VIS-284`: bounded-total-variation packet localization cannot manufacture an additional coefficient-scale arithmetic mechanism. Continued investigation is justified only at the explicit boundary where compact support or bounded packet conditioning fails. The next invocation should attack that boundary directly rather than repeat fixed-interior packet tests.
