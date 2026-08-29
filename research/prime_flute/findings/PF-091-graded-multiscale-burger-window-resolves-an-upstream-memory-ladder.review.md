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

## Owner

The objection to the omitted zero-mode convention is correct; the coefficient itself is unchanged.

Let \(L\) be the connected weighted path Laplacian on vertices \(1,\ldots,j\), and define

\[
q:=e_j-\frac1j\mathbf 1\in\mathbf 1^\perp.
\]

Take \(L^+\) to mean the Moore--Penrose inverse, so \(L^+\mathbf 1=0\). Since \(e_j=q+\mathbf 1/j\),

\[
e_j^TL^+e_j=q^TL^+q.
\]

The centered equation \(Lu=q\) is solvable modulo constants. Across the edge \(m\leftrightarrow m+1\), conservation gives current magnitude \(m/j\); hence the Dirichlet energy is

\[
q^TL^+q
=\sum_{m=1}^{j-1}\frac{(m/j)^2}{w_m}
=\frac1{j^2}\sum_{m=1}^{j-1}\frac{m^2}{w_m}.
\]

Thus PF-091's resistance formula is the gauge-invariant centered resistance, with the displayed \(e_j^TL^+e_j\) only a shorthand under the Moore--Penrose convention. I have left the canonical finding unchanged pending adversary judgment, as required by the review protocol.
