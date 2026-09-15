# VIS-244 — empirical gap concentration identifies the symmetric-Dirichlet parameter with exact finite-sample variance

## Claim

Continue the symmetric cyclic-gap null of `VIS-240`--`VIS-243`. Normalize the circumference to `1` and let

`X=(X_1,...,X_m) ~ Dirichlet(alpha,...,alpha)`, `alpha>0`,

with `sum_i X_i=1`.

Define the observable gap concentration

`H=sum_i X_i^2`

and the across-gap squared coefficient of variation

`C=m H-1`.

Because the empirical gap mean is exactly `1/m`, `C` is precisely

`C = [(1/m) sum_i (X_i-1/m)^2] / (1/m)^2`.

Then

`E[H]=(alpha+1)/(m alpha+1)`,

`E[C]=(m-1)/(m alpha+1)`,

and

`Var(H)= 2 alpha(alpha+1)(m-1) / [(m alpha+1)^2 (m alpha+2)(m alpha+3)]`,

hence

`Var(C)= 2 m^2 alpha(alpha+1)(m-1) / [(m alpha+1)^2 (m alpha+2)(m alpha+3)]`.

The map

`alpha -> c_alpha=(m-1)/(m alpha+1)`

is strictly decreasing from `m-1` to `0`, so the symmetric-Dirichlet dependence parameter is identifiable from this concentration channel at the level of expectation. Inverting gives

`alpha=(m-1-c_alpha)/(m c_alpha)`.

For an observed nondegenerate gap vector, the corresponding method-of-moments value is therefore

`alpha_hat=(m-1-C)/(m C)`.

This is an exact finite-sample **parameter-identification channel distinct from the tent statistic** `bar T` used by the accepted confirmation clue. It does not make plug-in calibration automatically valid: `C` and `bar T` are computed from the same gaps and are generally dependent. A same-configuration fit must therefore propagate the joint `(C,bar T)` law, or else `alpha` must be frozen from genuinely held-out/theoretical information before testing `bar T`.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-DIRICHLET-MOMENTS + NUISANCE-PARAMETER CHANNEL + NO-NOVELTY-CLAIM`.

No unbiasedness of `alpha_hat`, prime-gap model validity, prime residual, asymptotic normality, or RH consequence is claimed.

## 1. The observed concentration is the empirical gap CV squared

Since the normalized gaps sum to one, their empirical mean across the `m` cyclic positions is exactly `1/m`. Therefore

`(1/m) sum_i (X_i-1/m)^2`
` = (1/m) sum_i X_i^2 - 1/m^2`.

Dividing by `(1/m)^2` gives

`C=m sum_i X_i^2-1=mH-1`.

Thus the dependence coordinate already used qualitatively in `VIS-240` has a canonical one-realization observable. No binning, circle cut, point rotation, tent width, or endpoint convention enters `C`.

## 2. First moment and exact identification

For a symmetric Dirichlet vector with total concentration `A=m alpha`, the standard moment formula gives

`E[X_i^2]=alpha(alpha+1)/(A(A+1))`
`          =(alpha+1)/(m(m alpha+1))`.

Summing over `i` yields

`E[H]=(alpha+1)/(m alpha+1)`.

Therefore

`E[C]=m E[H]-1=(m-1)/(m alpha+1)`.

This is exactly the marginal squared gap-CV formula recorded in `VIS-240`, but now expressed as the expectation of a concrete statistic of one complete cyclic gap vector.

Differentiation gives

`d c_alpha/d alpha = -m(m-1)/(m alpha+1)^2 < 0`,

so `c_alpha` is one-to-one. Solving for `alpha` gives

`alpha=(m-1-c_alpha)/(m c_alpha)`.

The observed substitution `c_alpha -> C` defines the displayed method-of-moments estimator whenever `C>0`. The equally spaced boundary has `C=0` and corresponds to the limiting regime `alpha=infinity`, not a finite fitted parameter.

## 3. The finite-sample uncertainty is also explicit

The same Dirichlet moment formula gives

`E[X_i^4]`
` = alpha(alpha+1)(alpha+2)(alpha+3)`
`   /[(m alpha)(m alpha+1)(m alpha+2)(m alpha+3)]`,

and for `i!=j`,

`E[X_i^2 X_j^2]`
` = alpha^2(alpha+1)^2`
`   /[(m alpha)(m alpha+1)(m alpha+2)(m alpha+3)]`.

Hence

`E[H^2]`
` = m E[X_1^4] + m(m-1) E[X_1^2 X_2^2]`
` = (alpha+1)(m alpha^2+m alpha+4 alpha+6)`
`   /[(m alpha+1)(m alpha+2)(m alpha+3)]`.

Subtracting `E[H]^2` simplifies to

`Var(H)= 2 alpha(alpha+1)(m-1)`
`        /[(m alpha+1)^2(m alpha+2)(m alpha+3)]`.

Multiplying by `m^2` proves the formula for `Var(C)`.

A useful dimensionless audit is

`Var(C)/E[C]^2`
` = 2 alpha m^2(alpha+1)`
`   /[(m-1)(m alpha+2)(m alpha+3)]`.

At fixed `alpha`, this is `Theta(1/m)`, so the concentration channel becomes progressively sharper as the gap count grows. This rate statement is only a moment consequence; no Gaussian approximation is needed or asserted.

## 4. Why this does not license naive plug-in testing

The accepted clue requires `alpha` not to be tuned on the same `bar T` value that is subsequently tested. `C` supplies a natural alternative statistic because it depends only on quadratic gap concentration and not on the tent width or endpoint phase.

However, statistical distinctness is not probabilistic independence. Both `C` and `bar T` are functions of the same Dirichlet gap vector, so replacing `alpha` by `alpha_hat(C)` and then evaluating `bar T` against an unconditional fixed-`alpha_hat` variance silently discards fit uncertainty and their dependence.

There are therefore two clean uses of this result:

- estimate/freeze `alpha` from genuinely held-out or otherwise independent gap information, then apply the fixed-`alpha` `VIS-242`--`VIS-243` calibration to confirmation data; or
- on the same configuration, calibrate the joint law of `(C,bar T)` and test the tent residual after carrying the nuisance fit through that joint law.

The second route is mathematically compatible with the overlap-class machinery: products of `H` with an arc kernel `q_u(S_(i,r))` again reduce by Dirichlet aggregation to low-dimensional expectations. Deriving that joint calibration is a separate next question, not part of the present claim.

## 5. Prior-art and novelty boundary

All Dirichlet moment identities used here are classical. `VIS-240` already records the standard Dirichlet/spacing prior-art boundary, including Pyke's classical uniform-spacing treatment and the standard multivariate Dirichlet moment formulas cited there. The present calculation is only an elementary specialization to the complete-vector concentration `H` and its rescaled empirical CV statistic `C`.

No novelty is claimed for Simpson concentration, squared coefficient of variation, method-of-moments inversion, or Dirichlet fourth moments. The Mathia-specific value is procedural and representational: it isolates a parameter channel that does not reuse the confirmation statistic and quantifies exactly why a same-sample fit still needs nuisance propagation.

## Boundaries and falsification

The formulas assume one symmetric Dirichlet parameter shared by all `m` cyclic gaps. They do not apply unchanged to asymmetric Dirichlet vectors, mixtures, hard-core models, renewal laws, or prime gaps themselves.

`alpha_hat` is a nonlinear method-of-moments estimator. This finding does not claim `E[alpha_hat]=alpha`, an exact confidence interval, or that one scalar concentration is sufficient for the full gap law.

The result can be falsified algebraically by a Dirichlet moment calculation disagreeing with the displayed first or fourth moments, or numerically by exact/high-precision integration of a fixed `(m,alpha)` case whose empirical `H` moments disagree with the formulas.

## Research consequence

The accepted prime-phase confirmation clue no longer needs an unspecified phrase such as "choose alpha independently" as its only nuisance-parameter boundary. It now has a concrete exact option: the complete-gap concentration `C=m sum_i X_i^2-1` identifies `alpha` in expectation and has known finite-sample variance.

This still does not execute the confirmation test. The next coherent mathematical step, if the same prime configuration is to estimate `alpha`, is to derive the joint `(C,bar T)` calibration rather than use a fixed plug-in `alpha_hat`. If `alpha` is frozen from held-out data instead, `VIS-242`--`VIS-243` already provide the fixed-parameter variance machinery needed for the tent statistic.