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
  - research/visual_exploration/findings/VIS-290-wang-fixed-power-classical-pnt-envelope.md
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

`VIS-288` confined every fixed-power residual above the linear source law to `O(H)`, and `VIS-289` removed that apparent floor by replacing the coarse coefficient estimate `sum a_n^2=log x+O(1)` with the standard two-term squared-von-Mangoldt asymptotic, giving

`F_I(T^beta)-(H beta L)/(2*pi)=o(H)`

uniformly on compact exponent panels.

`VIS-290` makes this quantitative. Retaining the classical de la Vallee Poussin prime-number-theorem remainder through the same symmetric coefficient square and Wang's complete error budget yields, for some `c_0>0`,

`F_I(T^beta)-(H beta L)/(2*pi)=O(H exp(-c_0 sqrt(log T)))`

uniformly for `beta in [beta_0,beta_1]`. The stretched-exponential factor is inherited from ordinary prime-counting accuracy; it is an unconditional envelope, not a claimed intrinsic residual scale.

The fixed compact-power branch is therefore closed not only through the `H` scale but through every residual asymptotically larger than this classical-PNT envelope. Any surviving mechanism must resolve a still smaller term or leave the fixed compact exponent regime.

## Research question

Can a fixed-power residual below the classical-PNT envelope be isolated with a sharper quantitative input and shown to carry source-dependent arithmetic information, or does the compact fixed-power statistic continue to collapse to the universal linear source law as the arithmetic remainder is sharpened?

Alternatively, can a source family approaching a true boundary not covered by one fixed exponent panel — `beta(T)->0`, a regime approaching the admissible source ceiling, or deliberately singular packet normalization — produce information not already contained in the compact-source and fixed-power controls?

## Why it may matter

The source-localization thread has progressively removed the obvious ways to manufacture gain. Compact localization is a bounded projection, the isolated source profile has no endpoint singularity after forced baselines are removed, and the complete fixed-power statistic now satisfies the explicit unconditional estimate

`F_I(T^beta)=(H beta L)/(2*pi)+O(H exp(-c_0 sqrt(log T)))`

on every pre-fixed compact exponent panel inside `(0,theta)`.

A positive fixed-power result must therefore improve on a complete quantitative error budget rather than merely display a smaller normalized deviation. Because the current envelope is inherited from a generic prime-number-theorem remainder, a genuine mechanism would need either a sharper arithmetic expansion whose candidate term survives all of Wang's other errors or a regime in which the fixed-panel argument ceases to apply.

## Decisive test

Choose **one** remaining regime before inspecting its signal.

For a deeper fixed-power test, replace the classical de la Vallee Poussin input by an explicitly stronger quantitative asymptotic for

`sum_n a_n^2-log x`

and propagate it together with every `D_x`, `B_x`, `E_x`, localization, and cross-term error in Wang's proof. A candidate source-dependent term is interesting only if it dominates the **complete** sharpened error envelope uniformly on one predeclared compact `beta` panel and is not a repackaging of the explicit gamma or prime-power diagonal baselines. Kill the route if the apparent term is swallowed by the improved arithmetic remainder or another existing Wang error.

For a boundary test, state the source law and normalization explicitly and verify that it lies outside the compact exponent panel proved in `VIS-287`–`VIS-290`. Do not let Wang's fixed theorem parameter `lambda<theta` drift with `T` without a new uniformity proof. At `q->0`, retain the exact `VIS-285` baseline; near the source ceiling, rederive the load-bearing localization and mean-value errors rather than extrapolating the compact-panel formula.

Kill the direction if the proposed effect is reproduced by the known linear source main term, the explicit gamma term, the `O(H exp(-c_0 sqrt(log T)))` classical-PNT envelope, or packet-norm amplification. A surviving effect must occupy a quantitatively resolved smaller fixed-power scale or a boundary regime not covered by `VIS-283`–`VIS-290`.

## Evidence boundary

`VIS-283`–`VIS-286` establish the compact-source diagonal/cross controls and both isolated-profile endpoint baselines. `VIS-287` establishes the leading normalized complete-statistic asymptotic on fixed exponent panels. `VIS-288` localizes the previously unresolved theorem floor to `O(H)`. `VIS-289` sharpens that fixed-panel residual to `o(H)`. `VIS-290` retains a classical quantitative prime-number-theorem remainder and derives the explicit stretched-exponential upper envelope above.

`VIS-290` does **not** establish a nonzero residual at that scale, prove that the envelope is optimal, or show that stronger prime-counting estimates cannot improve it. None of these findings gives a theorem with `beta=beta(T)` approaching a boundary or control for packet families whose total variation diverges. No source-threshold theorem, new pair-correlation theorem, off-critical-strip gain, RH criterion, or new arithmetic invariant is established here.

## Research disposition

Outcome so far: **narrowed**.

The fixed-interior mechanism, both isolated diagonal endpoint singularities, and the compact fixed-power branch down to the classical-PNT stretched-exponential envelope are closed. Continued investigation is justified only by a quantitatively sharper sub-envelope expansion or a true moving boundary where one fixed uniform exponent panel no longer applies.