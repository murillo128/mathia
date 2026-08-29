---
type: adversarial-review
target: research/prime_flute/findings/PF-091-graded-multiscale-burger-window-resolves-an-upstream-memory-ladder.md
---

# Adversarial review

## Adversary

PF-091 identifies the upstream resistance as

\[
R_j=e_j^T L_{\{1,\ldots,j\}}^+e_j
=\frac1{j^2}\sum_{m=1}^{j-1}\frac{m^2}{w_m},
\]

but does not state the zero-mode convention that makes the first expression a
gauge-invariant resistance.  For the connected path Laplacian, the invariant
source is

\[
q=e_j-\frac1j\mathbf 1.
\]

The displayed shorthand is equal to \(q^TL^+q\) when \(L^+\) is the
Moore--Penrose inverse, because \(L^+\mathbf 1=0\).  Without that convention,
the notation is under-specified; in particular, \(Lx=e_j\) is not a solvable
potential equation.  The gauge-explicit Lean artifact at
[murillo128/qwen-lean#103](https://github.com/murillo128/qwen-lean/pull/103),
reviewed at `ca9902e052904391ad403d16c2b0b7f680ed6b6d`, proves the centered weak
equation and energy identity rather than relying on this shorthand.

This does not challenge the finite coefficient, but it does challenge whether
PF-091 currently records the exact formal-to-informal boundary needed to reuse
that coefficient safely.  The objection is resolved if the canonical finding
makes the Moore--Penrose convention and the equivalence with the centered-source
quadratic form explicit; no weakening of the theorem is required.
