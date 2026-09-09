---
type: adversarial-review
target: research/mobius_cancellation/findings/MC-176-gallagher-critical-shell-good-churchhouse-variance.md
---

# Adversarial review

## Adversary

The uniform `O(1)` comparison in (5) is not justified at the endpoint `tau=1/8` from the stated shell condition (2). Equations (16)--(18) leave an error of order `1+y/T_beta^2`; on `y asymp X_beta`, (19) gives only

`beta log(X_beta/T_beta^2) -> 0`

when `tau=1/8`. That is merely subexponential control, not boundedness. For example, a dyadic choice with `log X_beta = 1/(4 beta) + beta^{-1/2} + O(1)` still satisfies (2), but has `X_beta/T_beta^2 = exp(beta^{-1/2}+O(1))`, so the displayed argument cannot yield (5).

The main exponential-type consequence (6) may still survive with the weaker `exp(o(1/beta))` comparison, since `1/4-tau>0`, and the advertised `O(1)` statement can also be recovered by explicitly choosing the nearest dyadic saddle so that `log X_beta = 1/(4 beta)+O(1)`. But one of those repairs is needed. As written, the finding claims (5) for a dyadic shell specified only by (2), and the boundary case `tau=1/8` used for the square-root conclusion (9) does not support that claim.