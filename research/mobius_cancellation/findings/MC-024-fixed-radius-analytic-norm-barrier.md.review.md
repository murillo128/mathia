---
type: adversarial-review
target: research/mobius_cancellation/findings/MC-024-fixed-radius-analytic-norm-barrier.md
---

# Adversarial review

## Adversary

The one-step exponent ledger in (8)--(10) is correct, but the stronger claim that even a strict contraction factor below `1` "changes only the multiplicative constant under repeated squaring" is not valid for an actually iterable same-norm recurrence. For example, if `N_{k+1}=N_k^2` and

\[
x_{k+1}\le c\,x_k^2,\qquad 0<c<1,
\]

with `x_0=N_0^{-\alpha}`, iteration gives

\[
x_k\le c^{2^k-1}N_0^{-\alpha 2^k}
=c^{-1}N_k^{-\left(\alpha-\frac{\log c}{\log N_0}\right)}.
\]

Since `\log c<0`, the repeated contraction has become a strictly larger power exponent along the square-scale tower. More generally, from `x_0\le C N_0^{-\alpha}` the same effect occurs whenever the normalized factor `cC<1`.

This does not establish an exponent bootstrap for the actual Huxley--Watt system: the nested-disk estimate in (6) loses radius, square-scale control must be made uniform enough to iterate, and the additive residual in (7) can create a nonzero normalized floor. Those may indeed block the mechanism. But they are additional obstructions; homogeneity plus `N\mapsto N^2` alone does not justify the stated repeated-squaring no-go, nor the broader conclusion that a genuinely iterable analytic contraction can only improve constants.

Please either restrict the exponent-neutrality conclusion to the one-step/global `O(N^{-\alpha})` bookkeeping actually proved by (8)--(10) (with the residual/norm-loss hypotheses made explicit), or supply the missing argument showing why an iterable subunit contraction cannot convert into a power gain in this scale-doubling system.