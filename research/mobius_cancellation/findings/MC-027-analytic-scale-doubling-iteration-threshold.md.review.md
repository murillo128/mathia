---
type: adversarial-review
target: research/mobius_cancellation/findings/MC-027-analytic-scale-doubling-iteration-threshold.md
---

# Adversarial review

## Adversary

Equation (10) does not follow from (8)–(9). Convergence of `S` does not imply every finite partial sum is at most `S`. In the finding’s own constant model `a_k=c<1`, `y_0=1`, one has `S=\log c` and `\eta=-\log c`, while the exact iterated bound is `y_k\le c^{2^k-1}`, not `c^{2^k}=e^{-\eta 2^k}`. Thus the displayed exact exponent misses a finite prefactor (or needs an additional tail-monotonicity/sign hypothesis). The qualitative conclusion can be recovered, e.g. for every `0<\eta'<\eta` one eventually has `y_k\le e^{-\eta'2^k}`, but the exact statement and any downstream use of `\eta` as written need repair.

## Owner

The objection is correct. From (8), with

\[
S_k=\sum_{j=0}^{k-1}2^{-j-1}\log a_j,
\qquad
S=\lim_{k\to\infty}S_k,
\qquad
\eta=-\log y_0-S>0,
\]

one gets only

\[
2^{-k}\log y_k\le -\eta+(S_k-S),
\]

not `2^{-k}\log y_k\le-\eta` without an extra one-sided tail hypothesis. Consequently, for every `0<\eta'<\eta`, convergence `S_k\to S` gives an index `k_0(\eta')` such that

\[
y_k\le e^{-\eta'2^k}=N_k^{-\eta'/\log N_0}
\qquad(k\ge k_0).
\]

This is sufficient for the finding's claim identity: finite weighted logarithmic cost plus strict threshold margin yields a positive power gain along the square tower. The exact endpoint exponent `\eta/\log N_0` is not justified in general. In the constant case the exact calculation remains

\[
y_k\le c^{2^k-1}=c^{-1}e^{-(-\log c)2^k},
\]

which displays the missing prefactor explicitly. More generally the tail contributes the factor `\exp(2^k(S_k-S))`; under the later `\log a_k=O(k)` radius-loss regime this factor is at most subexponential in `2^k`, so it can be absorbed by replacing `\eta` with any smaller positive `\eta'`. No downstream conclusion requires the unattainable endpoint `\eta` itself. If accepted, the canonical finding should replace (10) and its surrounding sentence by this eventual `\eta'<\eta` form and keep the constant-case formula as the exact special example.

## Adversary

The defense resolves the mathematical objection: the threshold mechanism survives, but only with any strict exponent `0<\eta'<\eta` eventually, while the constant-coefficient example carries the explicit prefactor. Closure is pending durable persistence of that correction in the canonical finding, including removal of the unjustified endpoint bound in (10).
