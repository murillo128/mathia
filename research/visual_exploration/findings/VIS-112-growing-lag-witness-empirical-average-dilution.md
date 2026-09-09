# VIS-112 — the VIS-111 growing-lag witness dilutes under empirical averaging

## Claim

Let `x_r,y_r` be the exact order-`r` Markov-type pair from `VIS-111`, with

`N_r=4r+6`, `k_r=r+1`, and `l_r=2r+3=N_r/2`.

For the raw third-order correlation

`C_z(k,l)=sum_(j=0)^(N-1-l) z_j z_(j+k) z_(j+l)`,

`VIS-111` proves

`C_(x_r)(k_r,l_r)-C_(y_r)(k_r,l_r)=1`.

Now form the empirical average over all admissible starts,

`A_z(k,l)=C_z(k,l)/(N-l)`.

Then exactly

`A_(x_r)(k_r,l_r)-A_(y_r)(k_r,l_r)=1/(2r+3)=2/N_r`,

and therefore

`A_(x_r)(k_r,l_r)-A_(y_r)(k_r,l_r) -> 0`.

More generally, for any positive normalization `a_r -> infinity` applied linearly to this displayed raw coefficient difference,

`[C_(x_r)(k_r,l_r)-C_(y_r)(k_r,l_r)]/a_r = 1/a_r -> 0`.

Thus the `VIS-111` family proves **information admission beyond every fixed block quotient**, but it does not supply a macroscopic-amplitude witness under empirical or other diverging normalization. Non-factorization and asymptotically nonvanishing effect size are separate requirements.

**Evidence/status:** `EXACT-DERIVED + NEGATIVE AMPLITUDE/SCALE BOUNDARY + CLASSICAL HIGHER-ORDER-MOMENT NORMALIZATION + NO-SOURCE-SPECIFICITY + NO-NOVELTY-CLAIM`.

No statement is made about centered third-order cumulants, bicoherence, optimal normalization, null fluctuation scale, statistical power, zeta/CUE separation, or RH.

## 1. Exact dilution of the `VIS-111` coefficient

For the `VIS-111` pair, the second lag is

`l_r=2r+3`.

Since `N_r=4r+6`, the number of admissible starts in the triple-product sum is

`N_r-l_r = 2r+3 = N_r/2`.

The raw coefficient difference is exactly one, so dividing by the number of admissible starts gives

`Delta A_r = 1/(N_r-l_r) = 1/(2r+3) = 2/N_r`.

No probability model, asymptotic approximation, rendering, or source data enter this calculation.

The distinction is therefore sharp. The two assemblies remain distinguishable for every finite `r`, and no fixed finite block inventory determines the chosen coefficient uniformly in `r`; nevertheless, the displayed empirical-average separation shrinks to zero at rate `N_r^(-1)`.

## 2. Information capacity does not determine effect scale

`VIS-110` and `VIS-111` answer an information question. A bounded-lag statistic factors through a bounded block inventory, while the displayed growing-lag family does not factor through any uniformly fixed block length.

That answer alone does not determine how large the surviving information channel is after a normalization appropriate to comparing different observation lengths. The synthetic `VIS-111` words contain only six ones, independent of `r`, and the separating triple occurs only once. Their raw separation is therefore `O(1)` while the admissible-start count is `Theta(N_r)`.

This does not weaken the exact non-factorization theorem. It changes what that theorem licenses downstream. The family is a valid **information-admission witness**, but it is not evidence that a normalized growing-lag bispectral or third-moment observable should retain an `O(1)` source effect at large window size.

Conversely, a vanishing absolute normalized difference does not by itself imply statistical undetectability. If an appropriate null fluctuates on a still smaller scale, a shrinking effect may remain detectable. That is a separate source-and-null question and must be calibrated rather than inferred from the synthetic witness.

## 3. Consequence for a source-specific growing-scale test

A future zeta-zero test should therefore freeze two independent design choices before confirmation data are inspected:

1. the **information scale** — the growing lag law or global higher-order functional and the lower-information quotient it is meant to escape;
2. the **amplitude scale** — the normalization and null-calibrated decision statistic used to compare windows or observation lengths.

Passing the first gate does not pass the second. In particular, citing `VIS-111` is insufficient justification for treating a raw unit difference at macroscopic lags as an extensive or scale-stable phenomenon.

For an empirical third-moment continuation, the natural admissible-start average above is one transparent baseline. A different normalization may be scientifically appropriate, including a variance-stabilized or power-normalized statistic, but its scale must be fixed from the mathematical/source model and calibrated under the matched non-arithmetic null. Choosing a normalization after seeing which one preserves the apparent zeta effect would reintroduce the same selection freedom that the visual protocol is meant to remove.

A source-positive result would need to show that the predeclared statistic has a reproducible conditional residual at its declared normalization and that the residual is not reproduced by finite-size CUE or another appropriate non-arithmetic control. The `VIS-111` pair remains useful only as a lower-information admission test unless a stronger synthetic family also supplies the desired amplitude scaling.

## 4. Prior art and novelty assessment

Higher-order moments/cumulants and their Fourier-domain polyspectra are classical signal-processing objects. David R. Brillinger, **An Introduction to Polyspectra**, *Annals of Mathematical Statistics* 36:5 (1965), 1351–1374, develops the higher-order correlation/polyspectral framework. C. L. Nikias and M. R. Raghuveer, **Bispectrum estimation: A digital signal processing framework**, *Proceedings of the IEEE* 75:7 (1987), 869–891, DOI `10.1109/PROC.1987.13824`, is a standard bispectral-estimation reference already used in the current visual line.

A targeted check of third-order-moment and bispectral estimation confirms that averaging/normalization is part of the estimation problem and that other normalizations such as bicoherence are also used. No universal normalization theorem is imported here. The displayed `2/N_r` identity is only the elementary specialization of empirical averaging to the exact `VIS-111` combinatorial witness.

No novelty is claimed for empirical moment normalization, bispectral normalization, or asymptotic effect-size reasoning. The Mathia-specific value is the boundary it imposes on the current visual clue: an exact escape from fixed-memory quotients must still be audited for scale before it can motivate a source-specific multiscale claim.

## Boundary and falsification

The result concerns the exact `VIS-111` pair and the direct empirical-average normalization of its displayed uncentered third-order coefficient, plus the trivial extension to any linearly applied diverging denominator.

It does **not** classify:

- centered third-order moments or cumulants after mean subtraction;
- bicoherence or other nonlinear power normalizations;
- dense exact-type witness families whose raw separating count grows with `N`;
- another growing-lag statistic whose raw difference is `Theta(N)` or otherwise extensive;
- the fluctuation scale of any CUE, zeta, Markov-type, or other null distribution;
- statistical power for a shrinking but low-noise effect;
- whether any zeta-zero statistic is arithmetic-specific.

Falsify the exact claim by finding an `r>=2` for which the `VIS-111` raw coefficient difference is not one, or for which `N_r-l_r` is not `2r+3`. The identities `N_r=4r+6`, `l_r=2r+3`, and the direct correlation calculation in `VIS-111` rule out either failure.

## Visual consequence

No canonical PNG is retained. This is a pre-render scale control. A growing-lag heatmap can contain information absent from every fixed local quotient while its normalized contrast still collapses with observation length. Rendering before fixing the normalization would therefore conflate information capacity with visual amplitude.

## Research consequence

The accepted critical-strip multiscale clue should treat `VIS-111` as an information-admission theorem only. A source-specific continuation now needs an explicit **amplitude/normalization audit** in addition to the existing growing-lag and lower-information audit.

The next source experiment should not inherit the sparse synthetic lag coefficient as though its unit raw separation were scale-stable. It should predeclare a mathematically motivated growing-scale functional, normalization, lower-information conditioning, confirmation windows, and matched non-arithmetic null, then evaluate effect size relative to that frozen null. A stronger synthetic construction with extensive separation would be useful, but it is a new question rather than something established by `VIS-111`.