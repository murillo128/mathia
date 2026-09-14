---
type: adversarial-review
target: research/weil_inertia/findings/WI-286-growing-prime-screening-hits-a-square-root-gap-threshold.md
---

# Adversarial review

## Adversary

The square-root threshold argument itself survives, but the finding's claim that Baker--Harman--Pintz with `theta=21/40=0.525` is the **best/currently established** short-interval input is no longer adequately supported by the current literature.

Runbo Li, *The number of primes in short intervals and numerical calculations for Harman's sieve*, arXiv:2308.04458 (current 2025 version), proves that `[X-X^0.52,X]` contains a prime for all sufficiently large `X`, explicitly sharpening Baker--Harman--Pintz. This also supplies the forward form required by equation (5): for example, taking `X=x+2x^0.52`, one has `X-X^0.52>x` for all sufficiently large `x`, so a prime lies in `[x,x+2x^0.52]`. Thus the same argument applies with `theta=0.52` and a fixed constant `C`.

Consequently the best currently claimed quantitative input changes the necessary width exponent from `1-21/40=19/40=0.475` to `1-0.52=0.48`, and changes the residual pole-growth exponent from `21/40-1/2=1/40=0.025` to `0.52-1/2=0.02`. The qualitative conclusion is unchanged: this remains on the wrong side of the strict `theta<1/2` threshold. But statements that the established theorem misses the spectral transition **exactly by `1/40`**, or that `0.525` is the current best established exponent, are stale unless the finding intentionally restricts its evidence class to a narrower published/accepted literature and says so explicitly.

To resolve the objection, either audit and incorporate Li's `0.52` result and update the current quantitative frontier while preserving the abstract `theta<1/2` theorem, or explicitly scope the words "best established/currently established" to a narrower evidence class and justify that scope. This objection concerns the prior-art/evidence classification and the exact current margin, not the validity of the weaker Baker--Harman--Pintz deductions or the square-root threshold mechanism itself.
