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
  - research/visual_exploration/findings/VIS-291-wang-fixed-power-korobov-vinogradov-envelope.md
  - research/visual_exploration/findings/VIS-292-wang-symmetric-smoothing-green-resolvent.md
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

`VIS-288` confined every fixed-power residual above the linear source law to `O(H)`, `VIS-289` sharpened that to `o(H)`, and `VIS-290` made the improvement quantitative with a de la Vallée Poussin remainder.

`VIS-291` propagates the stronger Korobov–Vinogradov prime-number-theorem scale through the same symmetric squared-von-Mangoldt coefficient sum and Wang's complete error budget. For some `c_0>0`, uniformly on every pre-fixed compact exponent panel,

`F_I(T^beta)-(H beta L)/(2*pi)`
` = O(H exp(-c_0 L^(3/5)(log L)^(-1/5)))`.

This scale is inherited from generic unconditional prime-counting accuracy; it is not a detected residual of the pair-correlation statistic.

`VIS-292` now isolates the exact structure of the symmetric smoothing itself. With `u=log x`,

`S(e^u)=K*mu`, `K(v)=e^(-2|v|)`,

where

`mu=sum_n [Lambda(n)^2/n] delta_(log n)`.

Distributionally,

`(4-d^2/du^2)S(e^u)=4mu`,

and the log-Fourier multiplier is `4/(4+xi^2)`, strictly positive for every real `xi`. Equivalently the Mellin multiplier is `4/(4-w^2)` on `-2<Re(w)<2`. The smoothing therefore has no exact blind log/Mellin frequency: it attenuates source modes but does not annihilate any of them.

The fixed compact-power route is consequently narrowed one step further. A sharper remainder cannot be explained merely by an exact spectral null manufactured by the symmetric `min(n/x,x/n)^2` kernel. It must use non-generic arithmetic cancellation or analytic structure in the weighted source itself, or leave the fixed compact-power regime.

## Research question

Does the weighted source measure

`mu=sum_n [Lambda(n)^2/n] delta_(log n)`

or its Dirichlet transform

`D(s)=sum_n Lambda(n)^2 n^(-s)`

have arithmetic structure that, after multiplication by the nonvanishing Green/Mellin kernel, forces `S(x)-log x` below the generic Korobov–Vinogradov envelope in a way that survives the **complete** remaining Wang error budget?

Alternatively, can a source family approaching a true boundary not covered by one fixed exponent panel — `beta(T)->0`, a regime approaching the admissible source ceiling, or deliberately singular packet normalization — produce information not already contained in the compact-source and fixed-power controls?

## Why it may matter

The source-localization thread has progressively removed the obvious ways to manufacture gain. Compact localization is a bounded projection, the isolated source profile has no endpoint singularity after forced baselines are removed, and the complete fixed-power statistic now satisfies the unconditional estimate

`F_I(T^beta)=(H beta L)/(2*pi)`
` + O(H exp(-c_0 L^(3/5)(log L)^(-1/5)))`

on every pre-fixed compact exponent panel inside `(0,theta)`.

`VIS-292` also rules out a tempting purely filter-theoretic explanation for an extra gain: Wang's symmetric coefficient kernel has no exact null frequency on logarithmic scale and is distributionally invertible by `4-d^2/du^2`. Thus a positive fixed-power result has to expose something genuinely arithmetic in the source, not just a cancellation forced by the symmetric window. The conceptually distinct alternative remains a moving boundary where the compact-panel theorem no longer supplies uniform control.

## Decisive test

Choose **one** remaining regime before inspecting its signal.

For the deeper fixed-power branch, derive an independently justified analytic or arithmetic property of `D(s)` or `mu` that implies a bound or secondary expansion for

`S(x)-log x`

strictly sharper than the generic Korobov–Vinogradov envelope. The gain must come from the source rather than an exact zero of the smoothing multiplier, because `VIS-292` proves that no such zero exists. Propagate the resulting estimate together with every `D_x`, `B_x`, `E_x`, localization, and cross-term error in Wang's proof. A candidate source-dependent term is interesting only if it survives the complete sharpened envelope uniformly on one predeclared compact `beta` panel and is not a repackaging of the explicit gamma or prime-power diagonal baselines.

Kill the fixed-power route if the proposed gain is only another generic PNT substitution, follows only from high-frequency attenuation without a new source estimate, is swallowed by another Wang error, or requires an unproved prime-counting improvement. In particular, do not count the nonvanishing Green/Mellin filter itself as a cancellation mechanism.

For a boundary test, state the source law and normalization explicitly and verify that it lies outside the compact exponent panel proved in `VIS-287`–`VIS-292`. Do not let Wang's fixed theorem parameter `lambda<theta` drift with `T` without a new uniformity proof. At `q->0`, retain the exact `VIS-285` baseline; near the source ceiling, rederive the load-bearing localization and mean-value errors rather than extrapolating the compact-panel formula.

Kill the direction if the proposed effect is reproduced by the known linear source main term, the explicit gamma term, the Korobov–Vinogradov PNT envelope, the nonvanishing symmetric smoothing, or packet-norm amplification. A surviving effect must either beat the complete fixed-power envelope for a source-specific arithmetic reason or occupy a boundary regime not covered by `VIS-283`–`VIS-292`.

## Evidence boundary

`VIS-283`–`VIS-286` establish the compact-source diagonal/cross controls and both isolated-profile endpoint baselines. `VIS-287` establishes the leading normalized complete-statistic asymptotic on fixed exponent panels. `VIS-288` localizes the previously unresolved theorem floor to `O(H)`. `VIS-289` sharpens that fixed-panel residual to `o(H)`. `VIS-290` derives a de la Vallée Poussin quantitative envelope, and `VIS-291` sharpens it to the standard Korobov–Vinogradov PNT scale. `VIS-292` identifies the exact log-scale Green/Mellin kernel and proves that its multiplier has no zero, so the symmetric window does not create an exact blind frequency.

`VIS-292` does **not** prove that the Korobov–Vinogradov envelope is optimal, that smoothing cannot improve a remainder through arithmetic cancellation, or that `D(s)` lacks exploitable analytic structure. None of these findings gives a theorem with `beta=beta(T)` approaching a boundary or control for packet families whose total variation diverges. No source-threshold theorem, new pair-correlation theorem, off-critical-strip gain, RH criterion, or new arithmetic invariant is established here.

## Research disposition

Outcome so far: **narrowed**.

The fixed-interior mechanism, both isolated diagonal endpoint singularities, the compact fixed-power branch through the strongest standard Korobov–Vinogradov-shaped PNT envelope, and an exact blind-frequency explanation from Wang's symmetric smoothing are now closed. Continued fixed-power investigation is justified only by a source-specific arithmetic/analytic property of `mu` or `D(s)` that beats the generic PNT transfer and survives Wang's full error budget. Otherwise the remaining route is a true moving boundary where one fixed uniform exponent panel no longer applies.