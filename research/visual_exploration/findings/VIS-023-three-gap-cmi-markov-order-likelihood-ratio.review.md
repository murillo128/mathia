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