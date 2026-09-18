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
  - research/visual_exploration/findings/VIS-289-wang-fixed-power-residual-o-h.md
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

`VIS-288` first confined every fixed-power residual above the linear source law to `O(H)`. `VIS-289` identifies the apparent bare `O(H)` floor in Wang's proof: it comes from the coarse estimate `sum a_n^2=log x+O(1)`. Standard prime-number-theorem precision gives instead

`sum a_n^2=log x+o(1)`,

so all remaining proof terms are `o(H)` on a fixed compact power panel. Therefore

`F_I(T^beta)-(H beta L)/(2*pi)=o(H)`

uniformly for `beta in [beta_0,beta_1]`.

The fixed-power branch is consequently closed through the `H` scale. Any residual mechanism must either live strictly below `H` or leave the fixed compact exponent regime.

## Research question

Can a genuinely smaller-than-`H` fixed-power residual be isolated with a quantitative refinement that carries source-dependent arithmetic information, or does the fixed-power statistic collapse completely to the known linear source law at every useful scale?

Alternatively, can a source family approaching a true boundary not covered by one fixed exponent panel — `beta(T)->0`, a regime approaching the admissible source ceiling, or deliberately singular packet normalization — produce information not already contained in the compact-source and fixed-power controls?

## Why it may matter

The source-localization thread has removed the obvious ways to manufacture a gain and progressively closed the complete fixed-power statistic from its leading `HL` profile through the `H` scale. Compact localization is a bounded projection, the isolated source profile has no endpoint singularity after forced baselines are removed, and the complete statistic satisfies

`F_I(T^beta)=(H beta L)/(2*pi)+o(H)`

on every pre-fixed compact exponent panel inside `(0,theta)`.

A positive result must therefore refine the theorem substantially below `H` or enter a genuinely nonuniform boundary regime. Replotting, renormalizing, or packet-reweighting the same fixed-power statistic cannot resurrect an `H`-scale source signal already removed by the strengthened mean-square input.

## Decisive test

Choose **one** remaining regime before inspecting its signal.

For a sub-`H` fixed-power test, derive an explicit quantitative remainder for

`sum_n a_n^2-log x`

and propagate it together with every `D_x`, `B_x`, `E_x`, localization, and cross-term error in Wang's proof. A candidate source-dependent term is interesting only if it dominates the complete resulting error envelope uniformly on one predeclared compact `beta` panel and is not a repackaging of the explicit gamma or prime-power diagonal baselines.

For a boundary test, state the source law and normalization explicitly and verify that it lies outside the compact exponent panel proved in `VIS-287`–`VIS-289`. Do not let Wang's fixed theorem parameter `lambda<theta` drift with `T` without a new uniformity proof. At `q->0`, retain the exact `VIS-285` baseline; near the source ceiling, rederive the load-bearing localization and mean-value errors rather than extrapolating the compact-panel formula.

Kill the direction if the proposed effect is reproduced by the known linear source main term, the explicit gamma term, the sharpened `o(H)` fixed-power remainder, or packet-norm amplification. A surviving effect must occupy a quantitatively resolved sub-`H` scale or a boundary regime not covered by `VIS-283`–`VIS-289`.

## Evidence boundary

`VIS-283`–`VIS-286` establish the compact-source diagonal/cross controls and both isolated-profile endpoint baselines. `VIS-287` establishes the leading normalized complete-statistic asymptotic on fixed exponent panels. `VIS-288` localizes the previously unresolved theorem floor to `O(H)`. `VIS-289` uses standard prime-number-theorem precision inside Wang's own mean-square step to sharpen that fixed-panel residual to `o(H)`.

None of these findings supplies a quantitative best sub-`H` rate, a nonzero sub-`H` limiting profile, a theorem with `beta=beta(T)` approaching a boundary, or control for packet families whose total variation diverges. No source-threshold theorem, new pair-correlation theorem, off-critical-strip gain, RH criterion, or new arithmetic invariant is established here.

## Research disposition

Outcome so far: **narrowed**.

The fixed-interior mechanism, both isolated diagonal endpoint singularities, and the complete fixed-power branch through the `H` scale are closed. Continued investigation is justified only by a quantitatively controlled sub-`H` refinement or a true moving boundary where one fixed uniform exponent panel no longer applies.