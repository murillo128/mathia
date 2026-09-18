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
  - research/visual_exploration/findings/VIS-286-wang-large-source-diagonal-linearizes.md
  - research/visual_exploration/findings/VIS-287-wang-fixed-power-source-escape-linear.md
  - research/visual_exploration/findings/VIS-288-wang-fixed-power-residual-h-frontier.md
---

# Does Wang packet localization preserve the fixed-source diagonal profile without manufacturing strip gain?

## Observation

`VIS-283` isolates the fixed-source coefficient-scale field energy after the exact gamma baseline is retained. On compact fixed physical-source windows, the signed prime/source cross is power-small after packet normalization, while the surviving `L^-2` arithmetic profile before packet projection is the positive diagonal quantity

`Q_gamma(x)=S_D(x)+C_Lambda/x^2`,

with `x=e^(2*pi*q)`.

`VIS-284` resolves the fixed-interior packet interface. Uniformly `L^1`-bounded packets are bounded projections of that profile, while Laplace-null localization loses arithmetic response linearly with support width unless total variation grows at least inversely with the width.

`VIS-285` and `VIS-286` close the two obvious isolated-profile endpoint escapes: the left endpoint is analytic, while the large-source profile is the universal linear baseline `2*pi*q+o(1)` after prime-number-theorem partial summation.

`VIS-287` closes the leading complete-statistic fixed-power escape. For every fixed compact exponent panel

`0<beta_0<=beta<=beta_1<theta`, `x=T^beta`,

Wang's Proposition 2.6 gives uniformly

`(2*pi/(H L)) F_I(T^beta)=beta+o(1)`.

`VIS-288` now extracts the next scale from the same complete error budget. After subtracting Wang's full main term,

`R_beta(T)=F_I(T^beta)-(H/(2*pi))(L^2 T^(-2 beta)+beta L)=O(H)`

uniformly on every such panel, and all explicit source-dependent error terms are actually `o(H)`. Since the `L^2 T^(-2 beta)` main term is itself `o(H)`, one also has

`F_I(T^beta)-(H beta L)/(2*pi)=O(H)`.

Therefore every fixed-power residual scale strictly between `H` and `HL` is already excluded by the published theorem. The first unresolved fixed-power scale is `H` itself.

## Research question

Can the bare `O(H)` remainder in Wang's fixed-power formula be sharpened enough to expose or eliminate a genuine source-dependent `H`-scale profile after the linear baseline is removed?

Alternatively, can a source family approaching a true boundary not covered by one fixed exponent panel — `beta(T)->0`, a regime approaching the admissible source ceiling, or deliberately singular packet normalization — produce information not already contained in the compact-source and fixed-power controls?

## Why it may matter

The source-localization thread has now removed the obvious ways to manufacture a gain and has also removed an entire range of possible residual scales. Compact localization is a bounded projection, the isolated source profile has no endpoint singularity after forced baselines are removed, the complete statistic is linear at `HL` scale on fixed power panels, and every remaining fixed-power deviation is at most `O(H)`.

A positive result must therefore refine the actual theorem floor or enter a genuinely nonuniform boundary regime. Replotting, renormalizing, or packet-reweighting the same fixed-power statistic cannot create a mesoscopic `H a(T)` signal with `a(T)->infinity` that Wang's estimate already rules out.

## Decisive test

Choose **one** remaining regime before inspecting its signal.

For the fixed-power branch, identify the source of the bare `O(H)` term in Wang's proof and determine whether its contribution to

`F_I(T^beta)-(H beta L)/(2*pi)`

admits a uniform `o(H)` estimate or a source-dependent `H`-scale asymptotic on one predeclared compact `beta` panel. A useful positive result must produce a term not already swallowed by the current `O(H)` bound; a useful negative result should show that the load-bearing `O(H)` contribution is source-independent or can be sharpened below `H`.

For a boundary test, state the source law and normalization explicitly and verify that it lies outside the compact exponent panel proved in `VIS-287`–`VIS-288`. Do not let Wang's fixed theorem parameter `lambda<theta` drift with `T` without a new uniformity proof. At `q->0`, retain the exact `VIS-285` baseline; near the source ceiling, rederive the load-bearing localization and mean-value errors rather than extrapolating the compact-panel formula.

Kill the direction if the proposed effect is reproduced by the known linear source main term, the explicit gamma term, Wang's `O(H)` theorem floor, or packet-norm amplification. A surviving effect must either sharpen that floor or occupy a boundary regime not covered by `VIS-283`–`VIS-288`.

## Evidence boundary

`VIS-283`–`VIS-286` establish the compact-source diagonal/cross controls and both isolated-profile endpoint baselines. `VIS-287` establishes the leading normalized complete-statistic asymptotic on fixed exponent panels. `VIS-288` establishes only the consequence that the remaining fixed-power residual is uniformly `O(H)` and therefore cannot occupy any asymptotic scale strictly between `H` and `HL`.

None of these findings gives an `o(H)` remainder, an `H`-scale limiting profile, a theorem with `beta=beta(T)` approaching a boundary, or control for packet families whose total variation diverges. No source-threshold theorem, new pair-correlation theorem, off-critical-strip gain, RH criterion, or new arithmetic invariant is established here.

## Research disposition

Outcome so far: **narrowed**.

The fixed-interior mechanism, both isolated diagonal endpoint singularities, the leading fixed-power escape, and every intermediate fixed-power residual scale above `H` are closed. Continued investigation is justified only at the theorem's `H`-scale remainder itself or at a true moving boundary where one fixed uniform exponent panel no longer applies.