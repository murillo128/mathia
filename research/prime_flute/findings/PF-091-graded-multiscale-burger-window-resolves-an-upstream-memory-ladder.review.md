---
type: adversarial-review
target: research/prime_flute/findings/PF-091-graded-multiscale-burger-window-resolves-an-upstream-memory-ladder.md
---

# Adversarial review

## Adversary

PF-091 writes the upstream resistance using the shorthand

\[
R_j=e_j^T L^+e_j.
\]

For the connected path Laplacian, the invariant source is instead

\[
q=e_j-\frac1j\mathbf 1.
\]

The shorthand agrees with the gauge-invariant quantity \(q^TL^+q\) only when \(L^+\) is the Moore--Penrose inverse with \(L^+\mathbf 1=0\). Without that convention the displayed expression is under-specified; in particular, the corresponding uncentered potential equation is not solvable because the source has nonzero total mass.

This does not challenge the finite upstream-memory coefficient. It challenges only whether PF-091 records the exact zero-mode convention needed to reuse the resistance identity safely. The objection is resolved if the finding states the centered source, the Moore--Penrose convention, and the equality between the shorthand and the centered quadratic form explicitly.
