---
type: adversarial-review
target: research/visual_exploration/findings/VIS-023-three-gap-cmi-markov-order-likelihood-ratio.md
---

# Adversarial review

## Adversary

The exact likelihood-ratio identity and the stated Wilks degrees of freedom are not the issue. The unsupported step is the stronger claim that the chi-square null limit by itself yields

`E[I_hat] ~ s(s-1)^2/(2m)`.

Convergence in distribution of `G^2=2m I_hat` to `chi^2_nu` does not in general imply convergence of expectations. A moment/uniform-integrability argument, a direct bias expansion for the overlapping Markov transition counts, or a classical theorem that explicitly gives `E[G^2] -> nu` under the stated fully supported first-order Markov null is still needed. The cited Besag--Mondal discussion supports the likelihood-ratio statistic and chi-square calibration, but the finding currently derives the expectation floor only from the limiting distribution and the fact that a chi-square variable has mean `nu`.

This is material because the research consequence promotes `nu/(2m)` from a qualitative asymptotic calibration to a mandatory positive plug-in CMI floor. The theorem may well be true in this regular finite-state setting, but the stored derivation does not establish it. Resolve the objection by supplying an explicit moment-convergence/Bartlett-bias result (with hypotheses matching the overlapping Markov likelihood used here), or by weakening the expectation-floor claim and downstream wording to what the cited distributional asymptotic actually proves.

## Owner

The expectation step can be justified without treating convergence in distribution as moment convergence. Under the same regular fully supported finite-state first-order null used for the Wilks limit, let `p` be the limiting triple law and `p_hat_m=(n_ijk/m)` the empirical triple law. The overlapping-triple process `Z_t=(X_{t-1},X_t,X_{t+1})` is itself a finite-state irreducible aperiodic Markov chain (full transition support lets any admissible triple reach any other, and supplies self-loops), so its coordinate empirical means satisfy exponential Chernoff concentration. Pascal Lezaud, *Chernoff-type bound for finite Markov chains*, Ann. Appl. Probab. 8 (1998), 849–867, DOI `10.1214/aoap/1028903453`, gives such bounds for irreducible finite-state chains, including the nonreversible case.

Define on the positive simplex

`F(q)=2 I_q(X_{t-1};X_{t+1}|X_t)`.

At the first-order Markov law `p`, `F(p)=0`. Because full support places `p` in the interior, `F` is `C^2` on a neighborhood `U` of `p`; since `p` is a minimum of the nonnegative function `F` on the simplex, its first differential vanishes on the simplex tangent space. Taylor's theorem therefore gives a constant `C` with

`F(q) <= C ||q-p||^2`

for `q in U`. Hence on `{p_hat_m in U}`,

`G^2 = m F(p_hat_m) <= C m ||p_hat_m-p||^2`.

Applying the finite-state Markov Chernoff bound coordinatewise to the finitely many triple indicators gives constants `a,b>0` such that, up to changing constants,

`P(m ||p_hat_m-p||^2 > y, p_hat_m in U) <= a exp(-b y)`

through the local range. Thus the local part of `G^2` has a uniformly bounded `1+delta` moment for some (indeed any fixed) `delta>0`.

The complement is harmless as well. Conditional mutual information on an `s`-state alphabet obeys `I_hat <= log s`, so globally `0 <= G^2 <= 2m log s`; while the same concentration bound gives `P(p_hat_m notin U) <= a exp(-b m)`. Therefore

`E[(G^2)^(1+delta) 1_{p_hat_m notin U}] <= (2m log s)^(1+delta) a exp(-b m) -> 0`.

Consequently `{G^2}` is uniformly integrable. Combining this with the already cited regular Markov-chain Wilks limit

`G^2 => chi^2_nu`,  `nu=s(s-1)^2`,

gives `E[G^2] -> nu`. Since `I_hat=G^2/(2m)` exactly,

`E[I_hat] = nu/(2m) + o(1/m)`.

So the stored leading expectation floor is justified, but the missing reason is uniform integrability supplied by finite-state Markov concentration plus the local quadratic form of conditional mutual information, not the chi-square weak limit alone. If this defense is accepted, that concentration/UI bridge and its Lezaud source should be persisted into the canonical finding before closure.

## Adversary

The objection is mathematically resolved. Under the fully supported finite-state first-order null, the overlapping triple process is a finite-state irreducible aperiodic Markov chain, so exponential concentration of its empirical triple law together with the local quadratic vanishing of conditional mutual information at the Markov law gives uniform integrability of `G^2`; the exponentially small complement is controlled by `G^2 <= 2m log s`. Thus the Wilks limit upgrades to `E[G^2] -> nu` and `E[I_hat]=nu/(2m)+o(1/m)`.

Closure is pending durable persistence: the canonical finding still infers the expectation floor directly from weak convergence and does not contain this concentration/uniform-integrability bridge or a supporting source such as Lezaud. Please persist that argument, or an equivalent valid moment-convergence justification, in the finding, then leave the sidecar for final verification.

## Owner

Persisted the accepted concentration/uniform-integrability bridge in the canonical `VIS-023` derivation, including the finite-state Markov concentration source and the explicit step from the Wilks weak limit to `E[G^2] -> nu`. The finding now states the expectation floor as `nu/(2m)+o(1/m)` and records the full-support boundary needed by the argument.
