---
type: adversarial-review
target: research/mobius_cancellation/findings/MC-027-analytic-scale-doubling-iteration-threshold.md
---

# Adversarial review

## Adversary

Equation (10) does not follow from (8)–(9). Convergence of `S` does not imply every finite partial sum is at most `S`. In the finding’s own constant model `a_k=c<1`, `y_0=1`, one has `S=\log c` and `\eta=-\log c`, while the exact iterated bound is `y_k\le c^{2^k-1}`, not `c^{2^k}=e^{-\eta 2^k}`. Thus the displayed exact exponent misses a finite prefactor (or needs an additional tail-monotonicity/sign hypothesis). The qualitative conclusion can be recovered, e.g. for every `0<\eta'<\eta` one eventually has `y_k\le e^{-\eta'2^k}`, but the exact statement and any downstream use of `\eta` as written need repair.
