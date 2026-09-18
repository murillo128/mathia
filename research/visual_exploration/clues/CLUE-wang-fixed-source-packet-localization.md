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
---

# Does Wang packet localization preserve the fixed-source diagonal profile without manufacturing strip gain?

## Observation

`VIS-283` isolates the fixed-source coefficient-scale field energy after the exact gamma baseline is retained. On compact fixed physical-source windows, the signed prime/source cross is power-small after packet normalization, while the surviving `L^-2` arithmetic profile before packet projection is the positive diagonal quantity

`Q_gamma(x)=S_D(x)+C_Lambda/x^2`,

with `x=e^(2*pi*q)`.

`VIS-284` resolves the fixed-interior packet interface. For every uniformly `L^1`-bounded packet family supported inside one fixed compact physical-source interval, the coefficient-scale contribution is a bounded linear projection of `Q_gamma(e^(2*pi*q))`. If the packet also annihilates the universal fixed-source Laplace mode `e^(-4*pi q)`, shrinking its support with bounded total variation makes the arithmetic projection vanish at least linearly in the support diameter. Retaining a nonzero response under such localization forces inverse-width growth of the packet total variation.

`VIS-285` closes the left endpoint of the isolated diagonal profile: on the first source cell it is exactly `2 C_Lambda cosh(4*pi*q)`, finite and quadratic at `q=0`.

`VIS-286` closes the opposite isolated-profile escape. Classical prime-number-theorem partial summation gives

`Q_gamma(e^(2*pi*q))=2*pi*q+o(1)` as `q->infinity`,

and bounded-total-variation packets translating to large source cannot retain a nonzero response after that linear baseline is subtracted.

`VIS-287` now closes the first **complete-statistic** moving-source regime. For every fixed exponent panel

`0<beta_0<=beta<=beta_1<theta`, `x=T^beta`,

Wang's Proposition 2.6 gives uniformly

`(2*pi/(H L)) F_I(T^beta)=beta+o(1)`.

Thus, at the natural `HL` scale, every fixed power-law source escape strictly below the short-interval exponent has only the known linear `log x=beta L=2*pi*q` leading profile. Wang's localization, remaining sectors, and cross terms are all lower order there.

The unresolved interface has therefore moved again. It is no longer fixed-interior localization, an endpoint singularity of `Q_gamma`, or a leading-order fixed-power source effect. Any surviving mechanism must be genuinely finer or boundary-sensitive.

## Research question

After subtracting the known linear source main term in the complete Wang statistic, is there a **second-order moving-source residual** that remains nontrivial and uniformly controlled, or can every such candidate be absorbed by Wang's explicit remainder budget and packet conditioning?

Alternatively, can a source family approaching a true boundary not covered by one fixed exponent panel — `beta(T)->0`, a regime approaching the admissible source ceiling, or deliberately singular packet normalization — produce information not already contained in the fixed-source and fixed-power controls?

## Why it may matter

The visual/source thread has now removed the obvious ways to manufacture a source gain. Compact localization is a bounded projection, both ends of the isolated diagonal profile are regular after their forced baselines are removed, and the complete statistic itself is asymptotically linear throughout every fixed power-law source panel below `theta`.

A positive result now has to identify a genuinely new asymptotic scale or boundary interaction rather than reinterpret a known main term. Conversely, proving that Wang's remainder structure also kills the relevant second-order or boundary regimes would close the packet-localization route cleanly.

## Decisive test

Choose **one** remaining regime before inspecting its signal.

For a second-order fixed-power test, fix `beta in (0,theta)` and subtract Wang's full main term

`(H/(2*pi))(L^2 T^(-2 beta)+beta L)`.

Then derive, rather than numerically infer, the strongest residual scale supported by the `D_x`, `B_x+E_x`, localization, and cross-term estimates. A candidate is interesting only if it survives after the entire explicit error envelope and packet norm are charged.

For a boundary test, state the source law and normalization explicitly and verify that it lies outside the compact exponent panel proved in `VIS-287`. Do not let Wang's fixed theorem parameter `lambda<theta` drift with `T` without a new uniformity proof. At `q->0`, retain the exact `VIS-285` baseline; near the source ceiling, rederive the load-bearing localization and mean-value errors rather than extrapolating the compact-panel formula.

Kill the direction if the proposed effect is reproduced by the known linear source main term, by the explicit gamma term, by Wang's remainder envelope, or by packet-norm amplification. A surviving effect must occupy a scale or boundary regime not already covered by `VIS-283`–`VIS-287`.

## Evidence boundary

`VIS-283`–`VIS-286` establish the compact-source diagonal/cross controls and both isolated-profile endpoint baselines. `VIS-287` establishes only the **leading normalized asymptotic** for the complete statistic on fixed exponent panels bounded away from `0` and `theta`.

None of these findings gives a second-order expansion after subtracting the complete main term, a theorem with `beta=beta(T)` approaching a boundary, or control for packet families whose total variation diverges. No source-threshold theorem, new pair-correlation theorem, off-critical-strip gain, RH criterion, or new arithmetic invariant is established here.

## Research disposition

Outcome so far: **narrowed**.

The fixed-interior mechanism, both isolated diagonal endpoint singularities, and the leading-order fixed power-law source escape are closed. Continued investigation is justified only at a finer residual scale or a true moving boundary where one of the hypotheses used in `VIS-287` no longer provides a single fixed uniform source panel.