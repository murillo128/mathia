---
id: CLUE-visual-wang-phase-anchored-small-values
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-416-wang-bandwidth-normalized-balance-radius.md
  - research/visual_exploration/findings/VIS-417-beat-scale-defeats-coarse-amplitude-controls.md
  - research/visual_exploration/findings/VIS-418-time-translation-defeats-fixed-height-small-value-controls.md
  - research/visual_exploration/findings/VIS-419-wang-shell-translation-orbit-prime-torus-haar.md
  - research/visual_exploration/findings/VIS-420-finite-window-haar-small-divisor-cost.md
  - research/visual_exploration/findings/VIS-421-wang-generic-start-no-distinguished-height-selector.md
  - research/visual_exploration/findings/VIS-422-gram-points-prime-torus-haar-null.md
  - research/visual_exploration/findings/VIS-423-gram-block-character-small-divisor-tariff.md
  - research/visual_exploration/findings/VIS-424-normalized-wang-amplitude-moment-tariff.md
  - research/visual_exploration/findings/VIS-425-fixed-radius-wang-persistence-moment-tariff.md
  - research/visual_exploration/findings/VIS-427-growing-window-path-average-no-radius-tariff.md
  - research/visual_exploration/findings/VIS-428-fixed-shell-growing-supremum-uniform-saturation.md
  - research/visual_exploration/findings/VIS-429-target-rarity-forces-pre-saturation-hitting-tail.md
  - research/visual_exploration/findings/VIS-430-target-autocorrelation-hitting-upper-bound.md
  - research/visual_exploration/findings/VIS-431-bernstein-smoothing-finite-depth-hitting-control.md
  - research/visual_exploration/findings/VIS-432-binomial-tail-smoothing-logarithmic-rarity-depth.md
  - research/visual_exploration/findings/VIS-433-chernoff-balanced-bernstein-hitting-depth.md
  - research/visual_exploration/findings/VIS-434-chernoff-arcsine-buffer-geometry.md
---

# Does an independently justified arithmetic height selector align with Wang quiet regions beyond each shell's own translation orbit?

## Observation

`VIS-416` isolates normalized shell amplitude after removing the generic reciprocal-bandwidth scale. `VIS-417` and `VIS-418` show that beat scales and global time translation can manufacture long quiet regions while preserving coarse spectral data, so fixed-height smallness must be calibrated against the exact shell orbit rather than against loose random-sum controls.

`VIS-419` supplies that exact fixed-shell null: a finite Wang shell is a Laurent polynomial on its base-prime torus, and long translation is its Haar pushforward. `VIS-420` quantifies finite-window character-polynomial calibration through prime-log small divisors. `VIS-421` then separates selector provenance from Wang's source interface: Wang's generic interval start does not itself choose a sparse distinguished-height panel.

For ordinary Gram points, the escape route has narrowed repeatedly. `VIS-422` proves fixed finite prime-phase vectors are asymptotically Haar. `VIS-423` gives a quantitative tariff for changing Laurent-polynomial observables. `VIS-424` reduces normalized pointwise amplitude to fixed scalar moment tariffs plus Haar anti-concentration.

`VIS-425` removes the remaining ambiguity for **fixed-radius persistence** in the canonical strict near-band shells. Their frequency radius is uniformly below `log 2`, so Bernstein's inequality turns every fixed path window into a finite offset mesh at arbitrary fixed accuracy. Mixed offset moments pay the same `VIS-423` character tariff, with a structural divisor that for a dyadic shell of arithmetic height `Y_N` satisfies

`delta^*_(N,R) >= (2Y_N)^(-2R)`.

Thus fixed-radius local suprema are not an independent nonlinear escape once the strengthened mixed-moment tariffs and Haar boundary-mass condition pass.

`VIS-427` closes a different growing-path loophole. For every fixed power `q`, the normalized path average

`J_(N,q)=(1/(2rho_N)) int_(-rho_N)^(rho_N) X_(N,u)^q du`

pays **no additional radius tariff**, even when `rho_N -> infinity`: Fubini expands each fixed moment into the same shifted Laurent characters, while the offset-box volume cancels against the path-length normalization. Therefore merely increasing the observation radius cannot create a Gram/Haar anomaly for normalized fixed-power path averages when the existing Wiener/frequency/small-divisor tariffs pass.

`VIS-428` sharpens the remaining growing-window **supremum** route. For every fixed nonzero shell and every fixed threshold `t<1`, the closed target `{A_N>=t}` contains the nonempty open set `{A_N>t}` in the shell's prime torus. Minimality of the prime-log Kronecker flow plus compactness gives a finite shell-specific cover radius `R_N(t)` such that every initial phase reaches `{A_N>=t}` within `|u|<=R_N(t)`. Hence

`Q_(N,rho)(z)>=t`

for every phase `z` once `rho>=R_N(t)`, and fixed-shell path suprema converge uniformly to one as the window grows.

`VIS-429` adds the missing pre-saturation rarity control. If

`mu_N(t)=m_H{A_N>=t}`

and `eta>0`, the `VIS-425` orbit-Lipschitz certificate gives

`m_H{H_(N,t+eta)>rho}`
` >= max(0,1-(1+rho Omega_N/eta) mu_N(t))`.

Thus a rare high-amplitude target forces long quiet windows for a large Haar fraction even before any arithmetic selector is introduced. In particular, when `0<mu_N(t)<1`,

`R_N(t+eta) >= (eta/Omega_N)(1/mu_N(t)-1)`.

So `rho_N->infinity` by itself is not a residual mechanism for suprema, and neither is a large absolute hitting/cover time. A nontrivial changing-shell effect must live **before universal saturation and beyond the target-rarity floor**: the prescribed radius `rho_N` must be anomalous relative to the shell's exact Haar hitting profile after accounting for `mu_N(t)`, `Omega_N`, and the threshold buffer.

A surviving Gram-point anomaly must now expose a quantified tariff failure, nonuniform Haar concentration, a selector with a genuinely non-Haar finite-prime phase law, or an atypical pre-saturation hitting-time profile that is not already forced by target rarity. Unqualified growing radius or long quiet intervals are no longer escapes.

`VIS-430`--`VIS-433` now close much of the complementary upper-tail representation cost. Occupation variance converts finite Fourier control into a hitting bound; buffered Bernstein smoothing makes the hard target finite-depth; thresholded binomial tails make fixed-buffer rarity cost only logarithmic depth in `1/mu_b`; and Chernoff balancing gives the optimal exponent inside that separator family. `VIS-434` further shows that, for a fixed interior amplitude threshold and small buffer, the local Chernoff cost is governed by the Fisher/arcsine amplitude coordinate. The extra `t^(-2)` factor in the coarse raw-squared-amplitude Hoeffding certificate is therefore not an intrinsic shrinking-buffer resource.

## Research question

Fix, before inspecting shell values, a deterministic arithmetic height selector `S={T_j}` with explicit provenance and a pre-specified rule transporting the Wang shell family across those heights. Do the selected heights exhibit unusually small normalized amplitudes or unusually persistent quiet regions relative to each corresponding shell's exact translation/Haar self-null, after bandwidth normalization and without scanning the selector, shell scale, shift, persistence radius, moment order, threshold, or statistic to favor the observed values?

For ordinary Gram points and strict near-band Wang shells, do the **actual transported source coefficients** violate the combined `VIS-424`/`VIS-425`/`VIS-427` sufficient null through excessive normalized Wiener mass, unexpectedly small fixed-order product-ratio divisors, or nonuniform Haar concentration? If a growing-window supremum remains the intended diagnostic, does the selected phase have an atypically long hitting time into the shell superlevel target **after** the `VIS-429` target-rarity lower bound is priced and before the universal saturation radius `R_N(t)` exposed by `VIS-428`?

## Why it may matter

The control hierarchy now preserves essentially all fixed-shell arithmetic character structure while removing generic explanations one by one. Deterministic selector sparsity is insufficient (`VIS-422`); growing dimension alone is insufficient below the character tariff (`VIS-423`); scalar modulus is insufficient below the moment tariff (`VIS-424`); a fixed local supremum is insufficient when uniform bandwidth and mixed-moment tariffs hold (`VIS-425`); a normalized fixed-power path average cannot escape merely by widening its observation window (`VIS-427`); a fixed shell's growing-window supremum eventually saturates for every phase (`VIS-428`); and a rare superlevel target itself forces a long pre-saturation Haar hitting tail (`VIS-429`).

A positive residual would therefore have to identify a concrete source resource rather than hide behind generic nonlinearity, finite-window beating, path dependence, radius growth, or rare-target geometry. For a supremum, the source-sensitive object is the same-shell pre-saturation hitting-time tail **after target rarity is accounted for**, not the existence of a large window. A negative result is equally useful because it can close the current Gram selector branch at the level of the actual Wang transport rather than by simulation.

## Decisive test

Before numerical evaluation, freeze the selector provenance, the shell-family transport rule, the Wang parameters, bandwidth normalization, amplitude/persistence statistic, persistence-radius law, threshold law, panel aggregation, moment orders used by any path-average statistic, and numerical approximation rule.

For an ordinary-Gram strict near-band shell

`F_N=sum_a b_(N,a) z^a`,

compute or rigorously bound

`W_N=(sum_a |b_(N,a)|)/||F_N||_infinity`

and the dyadic shell height `Y_N`. For every fixed total moment order `R` relevant to the intended test, use the structural divisor

`delta^*_(N,R)=min |sum_(j=1)^R(lambda_(a_j)-lambda_(c_j))|`

over nonzero values. `VIS-425` gives the source-independent bound

`delta^*_(N,R) >= (2Y_N)^(-2R)`

for the strict near-band ratio shells.

Attempt the explicit sufficient tariff

`W_N^(2R) [ 1/N + R/log N + (log N)(2Y_N)^(2R)/N ] -> 0`

for every fixed `R`, or replace the elementary divisor floor by a sharper proved bound when available. If these mixed-moment tariffs pass, `VIS-425` forces every fixed continuous pointwise-amplitude and fixed-radius persistence diagnostic to its Haar self-null. For a fixed low-tail threshold, additionally require the corresponding Haar boundary mass to vanish uniformly in shrinking neighborhoods of that threshold.

For any normalized growing-window path average of a **fixed** power, do not add a radius penalty: `VIS-427` shows that the same fixed-order character tariff controls its moments for arbitrary `rho_N`. Treat an observed dependence on growing radius in such an averaged statistic as a reason to audit normalization, coefficient transport, moment order, or tariff failure rather than as a new mechanism by itself.

For a growing-window **supremum**, choose fixed `t<1` and a pre-specified buffer `eta>0` with `t+eta<=1`. Use the exact closed-target hitting variable

`H_(N,t)(z)=inf{|u| : A_N(z tau_N(u))>=t}`.

`VIS-428` gives

`Q_(N,rho)(z)<t  iff  H_(N,t)(z)>rho`

and a finite fixed-shell cover radius

`R_N(t)=sup_z H_(N,t)(z)`.

Before interpreting an observed long hitting time, compute or rigorously bound the exact-shell Haar target mass

`mu_N(t)=m_H{A_N>=t}`.

Then apply `VIS-429`:

`m_H{H_(N,t+eta)>rho}`
` >= max(0,1-(1+rho Omega_N/eta) mu_N(t))`.

When this lower bound is already large at the chosen `rho_N`, a quiet selected phase is generically expected under Haar and cannot support an arithmetic anomaly. Likewise, when `0<mu_N(t)<1`, the cover radius necessarily satisfies

`R_N(t+eta) >= (eta/Omega_N)(1/mu_N(t)-1)`.

Only after this rarity gate fails to explain the selected quiet interval should the test pursue an upper-tail certificate. `VIS-430` reduces that task to occupation variance. For a buffered amplitude target, `VIS-431` first replaces the hard indicator by finite Laurent depth. `VIS-432` gives the universal Hoeffding separator, while `VIS-433` supplies the sharper Chernoff-balanced certificate. With `a=t^2`, `b=(t+eta)^2`, `mu_b=mu_N(t+eta)`, use

`d > log((1+mu_b)/mu_b)/C_Ber(a,b)`

whenever the exact Chernoff information is available; the `VIS-432` coefficient `2/(b-a)^2` remains a universal coarse fallback.

For fixed interior `t in (0,1)` and a small pre-registered amplitude buffer `eta`, `VIS-434` gives

`C_Ber(t^2,(t+eta)^2)=eta^2/[2(1-t^2)] + O_t(eta^3)`.

Thus the optimized leading depth coefficient is `2(1-t^2)/eta^2`, not the coarse `1/(2t^2 eta^2)` obtained by applying Hoeffding directly to the squared-amplitude gap. Interpret this only locally at fixed interior `t`; if `t=t_N` approaches an endpoint together with `eta_N`, audit that coupled endpoint regime separately.

After choosing `d`, apply the `VIS-430` variance formula together with the depth-`d` Wang Wiener/small-divisor tariff. Fixed-buffer rarity still costs only logarithmically growing Laurent depth; the live question is whether the actual Wang coefficient geometry controls the **Chernoff-priced** depth. A failure of this sufficient bound is not an anomaly by itself.

The `VIS-429` bound remains one-sided, so passing beyond its forced scale does **not** establish atypicality; it only makes the upper-tail certificate or sharper same-shell hitting-time comparison informative.

Also determine whether the chosen `rho_N` is already at or beyond the universal saturation scale. If `rho_N>=R_N(t+eta)` eventually, the strict low-supremum event is empty for every phase and the test is dead. A threshold `t_N->1` is admissible only when its shrinking-target law, buffer rule, and target-mass estimation are frozen in advance and audited separately.

Only a quantified failure of these gates should remain live. A failed sufficient bound is **not** evidence of an anomaly: identify which resource causes the failure and test whether it is specific to the Wang source rather than a generic property of comparable finite character polynomials. Likewise, a large `R_N(t)` is not itself a source anomaly; `VIS-429` shows that rare targets force large generic hitting scales even before source selection.

For a different external selector, first audit whether its finite prime-phase vectors or the relevant changing observables are already forced to the same Haar null. Independent randomization of ratio-mode phases is not an admissible substitute for the base-prime Haar control.

Kill the direction if no non-arbitrary selector with defensible provenance can be frozen, if the relevant selector is already Haar in the tested regime and the combined amplitude/persistence/path-average tariffs pass, if a growing-window supremum is already beyond its shell cover radius, if the selected quiet interval lies in a regime where `VIS-429` already forces a large Haar avoidance probability, if the selected phases are typical under the sharper exact pre-saturation hitting-time self-null, or if an apparent effect disappears under the pre-registered transport/scaling rules or can be recreated by post-selection.

## Evidence boundary

`VIS-419` proves fixed-shell Haar calibration; `VIS-420` gives finite-window small-divisor costs; `VIS-421` separates Wang's generic source height from an external selector; `VIS-422` closes ordinary Gram points for fixed shells; `VIS-423` controls changing Laurent-polynomial observables; `VIS-424` reduces pointwise amplitude to scalar moments; `VIS-425` extends that reduction to fixed-radius persistence under a uniform frequency bound and stronger mixed-frequency divisor; `VIS-427` shows that normalized fixed-power path averages acquire no additional growing-radius tariff; `VIS-428` gives fixed-shell uniform saturation; `VIS-429` gives the target-rarity lower tail; `VIS-430` gives the complementary occupation-variance upper-tail route; `VIS-431` converts buffered hard targets to finite Laurent depth; `VIS-432` reduces the fixed-buffer rarity cost to logarithmic depth; `VIS-433` optimizes the thresholded-Bernstein exponent by Bernoulli Chernoff information; and `VIS-434` identifies its fixed-interior small-buffer Fisher/arcsine geometry and the coordinate looseness in the raw squared-amplitude Hoeffding coefficient.

None of these findings proves that the actual transported Wang growing family satisfies the sufficient tariffs, proves uniform Haar anti-concentration at a chosen threshold, gives an upper bound or asymptotic law for `R_N(t)`, or establishes a source-sensitive anomaly when a tariff fails. `VIS-429` is only a one-sided generic lower bound: a selected phase beyond that forced scale may still be entirely typical under the exact Haar hitting-time law.

No current result identifies a selector with an anomalous Wang-shell phase law, establishes a source-sensitive low-tail excess, produces an RH mechanism, or turns an external selector into part of Wang's theorem.

## Research disposition

Accepted, further narrowed through `VIS-434`. **For ordinary Gram points, pointwise amplitude, fixed-radius persistence, normalized fixed-power path averages, fixed-shell large-radius suprema, and buffered pre-saturation hitting now have explicit lower- and upper-tail control routes.** Fixed-buffer target rarity costs only logarithmic separator depth, and the recommended coefficient is the exact Bernoulli Chernoff information rather than the coarse squared-gap Hoeffding constant. For fixed interior amplitude threshold and small buffer, the local cost is governed by the arcsine/Fisher amplitude coordinate; the extra low-`t` penalty of the raw squared-amplitude Hoeffding certificate is not intrinsic. Continue only with a quantified Wang tariff failure at that Chernoff-priced growing depth, a genuinely endpoint-coupled shrinking-buffer/target regime, a selector whose prime-phase law is not driven to the same self-null, or another destination observable not reduced by the current character machinery.