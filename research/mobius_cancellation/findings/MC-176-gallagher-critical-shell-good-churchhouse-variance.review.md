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

## Owner

The endpoint objection is correct as stated. Condition (2) alone gives only `X_beta/T_beta^2 = exp(o(1/beta))` at `tau=1/8`, so it does not imply the displayed uniform `O(1)` comparison.

The substantive critical-shell claim does not require an arbitrary dyadic sequence satisfying (2); it only needs one dyadic shell at the positive Gaussian saddle. Fix it canonically by taking

`k_beta = round(1/(4 beta log 2))` and `X_beta = 2^(k_beta)`.

Then

`log X_beta = 1/(4 beta) + O(1)`, hence still `beta log X_beta -> 1/4`, but now

`X_beta/T_beta^2 = exp((1/4-2 tau)/beta + O(1))`.

For every `tau >= 1/8` this is `O(1)` (and tends to zero for `tau>1/8`). Therefore the error terms in (16)--(18) are uniformly `O(1)` on `y in [X_beta,2X_beta]`, so (5) follows for this canonical nearest-dyadic saddle, including the endpoint `tau=1/8`. The later `L^2` comparison and exponential-type consequence (6), and hence the `H_beta = X_beta^(1-4 tau+o(1))` necessary variance statement and the `tau=1/8` square-root-scale specialization, are unchanged.

This is a shell-selection precision error rather than a change in the mathematical claim identity: the finding asserts a necessary critical-shell projection of the global positive Gallagher energy, and existence of the canonical saddle shell is sufficient for that projection. If this repair is accepted, the durable correction should strengthen (2) to the nearest-dyadic condition `log X_beta = 1/(4 beta)+O(1)` and adjust the surrounding explanation so (19) supplies boundedness rather than merely subexponential control.

## Adversary

The repair is mathematically sufficient: the nearest-dyadic choice gives `log X_beta = 1/(4 beta)+O(1)`, hence `X_beta/T_beta^2 = exp((1/4-2 tau)/beta+O(1))`, which is uniformly bounded for `tau>=1/8`. This preserves the same necessary critical-shell claim and restores the stated `O(1)` comparison at the endpoint.

Closure is pending durable persistence. Please strengthen the canonical shell selection from the limit-only condition (2) to the nearest-dyadic condition `log X_beta = 1/(4 beta)+O(1)` (or an equivalent bounded-offset choice) and update the use of (19) accordingly; the sidecar should remain until that correction is present in the finding.

## Owner

Persisted the accepted repair in the canonical finding. The shell is now the nearest-dyadic saddle with `log X_beta = 1/(4 beta)+O(1)`, and equation (19) now gives `X_beta/T_beta^2=O(1)` uniformly for `tau>=1/8`, including the endpoint. The mathematical claim and finding identity are unchanged.