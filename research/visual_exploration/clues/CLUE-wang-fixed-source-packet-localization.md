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
  - research/visual_exploration/findings/VIS-293-wang-source-dirichlet-rh-half-plane.md
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

`VIS-292` isolates the exact symmetric smoothing. With `u=log x`,

`S(e^u)=K*mu`, `K(v)=e^(-2|v|)`,

where

`mu=sum_n [Lambda(n)^2/n] delta_(log n)`.

The filter is distributionally invertible and its log-Fourier/Mellin multipliers have no zeros, so a sharper remainder cannot come from an exact blind frequency manufactured by the window.

`VIS-293` now audits the analytic source itself. For

`D(s)=sum_n Lambda(n)^2 n^(-s)`,

one has in `Re(s)>1/2`

`D(s)=(log zeta)''(s)+A(s)`

with `A` holomorphic. Thus after removing the pole at `s=1`, holomorphy of `D` throughout `Re(s)>1/2` is equivalent to RH. The nonvanishing Wang Mellin multiplier preserves every off-critical pole. Therefore a proposed fixed-power escape based on simply proving a zero-free continuation for `D` is not cheaper source structure; it is RH itself in source coordinates.

## Research question

Is there a **real-axis** arithmetic property of the weighted source `mu`, weaker than RH-equivalent half-plane holomorphy, that forces `S(x)-log x` below the generic Korobov–Vinogradov envelope and still survives Wang's complete remaining error budget?

Alternatively, can a source family approaching a true boundary not covered by one fixed exponent panel — `beta(T)->0`, a regime approaching the admissible source ceiling, or deliberately singular packet normalization — produce information not already contained in the compact-source and fixed-power controls?

## Why it may matter

The source-localization thread has progressively removed the obvious ways to manufacture gain. Compact localization is a bounded projection, the isolated source profile has no endpoint singularity after forced baselines are removed, and the complete fixed-power statistic satisfies the unconditional Korobov–Vinogradov-scale envelope on every pre-fixed compact exponent panel inside `(0,theta)`.

The two most tempting structural explanations are now also controlled. `VIS-292` rules out exact cancellation created by the symmetric filter, while `VIS-293` shows that the first continuation half-plane of the remaining source transform already carries the zeta zero divisor itself. A useful fixed-power result must therefore be genuinely quantitative and weaker than merely assuming or proving the RH-equivalent analytic continuation one wants to exploit. The conceptually distinct alternative remains a moving boundary where the compact-panel theorem no longer supplies uniform control.

## Decisive test

Choose **one** remaining regime before inspecting its signal.

For the fixed-power branch, state a concrete real-axis estimate or secondary expansion for

`S(x)-log x`

and derive it from arithmetic information that is not simply the assertion that `D(s)-1/(s-1)^2` is holomorphic on `Re(s)>1/2`. Determine explicitly what zero-free region or continuation statement the proposed estimate would imply. Then propagate the estimate together with every `D_x`, `B_x`, `E_x`, localization, and cross-term error in Wang's proof. A source-dependent term is interesting only if it survives the complete sharpened envelope uniformly on one predeclared compact `beta` panel and is not a repackaging of the gamma/prime-power diagonal baselines.

Kill the fixed-power route if the proposed gain is only another generic PNT substitution, follows only from high-frequency attenuation, assumes the RH-equivalent pole exclusion of `VIS-293`, is swallowed by another Wang error, or requires an unproved prime-counting improvement.

For a boundary test, state the source law and normalization explicitly and verify that it lies outside the compact exponent panel proved in `VIS-287`–`VIS-293`. Do not let Wang's fixed theorem parameter `lambda<theta` drift with `T` without a new uniformity proof. At `q->0`, retain the exact `VIS-285` baseline; near the source ceiling, rederive the load-bearing localization and mean-value errors rather than extrapolating the compact-panel formula.

Kill the direction if the proposed effect is reproduced by the known linear source main term, the explicit gamma term, the Korobov–Vinogradov PNT envelope, the nonvanishing symmetric smoothing, RH-equivalent source holomorphy, or packet-norm amplification. A surviving effect must either improve the complete fixed-power envelope for a strictly identified weaker arithmetic reason or occupy a boundary regime not covered by `VIS-283`–`VIS-293`.

## Evidence boundary

`VIS-283`–`VIS-286` establish the compact-source diagonal/cross controls and both isolated-profile endpoint baselines. `VIS-287` establishes the leading normalized complete-statistic asymptotic on fixed exponent panels. `VIS-288` localizes the previously unresolved theorem floor to `O(H)`. `VIS-289` sharpens that fixed-panel residual to `o(H)`. `VIS-290` derives a de la Vallée Poussin quantitative envelope, `VIS-291` sharpens it to the standard Korobov–Vinogradov PNT scale, and `VIS-292` proves that the symmetric Green/Mellin filter has no blind frequency.

`VIS-293` proves only an exact analytic reduction: in `Re(s)>1/2`, the source transform is `(log zeta)''` plus a holomorphic remainder, so full pole exclusion there is RH-equivalent. It does **not** prove that the Korobov–Vinogradov real-axis envelope is optimal, classify all weaker source estimates, or rule out a useful bound that implies less than RH. None of these findings controls a theorem with `beta=beta(T)` approaching a boundary or packet families whose total variation diverges.

## Research disposition

Outcome so far: **narrowed**.

The fixed-interior mechanism, both isolated diagonal endpoint singularities, the compact fixed-power branch through the strongest standard Korobov–Vinogradov-shaped PNT envelope, an exact blind-frequency explanation from Wang's smoothing, and an unpriced appeal to source-transform holomorphy are closed. Continued fixed-power investigation is justified only by a precisely quantified real-axis source estimate whose analytic cost is explicitly weaker than the RH-equivalent condition in `VIS-293` and which survives Wang's full error budget. Otherwise the remaining route is a true moving boundary where one fixed uniform exponent panel no longer applies.