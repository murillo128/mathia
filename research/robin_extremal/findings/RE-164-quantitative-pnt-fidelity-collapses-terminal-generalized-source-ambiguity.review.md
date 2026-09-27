---
type: adversarial-review
target: research/robin_extremal/findings/RE-164-quantitative-pnt-fidelity-collapses-terminal-generalized-source-ambiguity.md
---

# Adversarial review

## Adversary

Equation (24) claims that the bounded-terminal-shell estimate (23) already gives
[
b\kappa_A\ge \frac12
\quad\Longrightarrow\quad
\mathcal A_p(Q_1)-\mathcal A_p(Q_2)=o(1).
]
The equality case is not justified by the stored asymptotics.

Writing (x=\log p) and (y=\log\log p), the canonical horizon has
[
\log U_A=A x^{5/3}y^{1/3}.
]
For bounded (L) and (T=U_Ae^{-L}), direct expansion of the very function used in (12),
[
V(T)=\frac{(\log T)^{3/5}}{(\log\log T)^{1/5}},
]
gives
[
V(T)
=
\kappa_A x
\left(
1-\frac{\log y+3\log A}{25y}
+o\!\left(\frac1y\right)
\right).
]
Thus at the asserted boundary (b\kappa_A=1/2),
[
p^{1/2}e^{-bV(T)}
=
\exp\!\left(
\frac{x(\log y+3\log A)}{50y}
+o\!\left(\frac{x}{y}\right)
\right),
]
so the subpower factor hidden by the (p^{o(1)}) in (23) is not controlled by the displayed polylogarithmic denominator. In fact, the available local-shell majorant obtained from (17) does not tend to zero at equality. More simply, even the stated form
[
p^{1/2-b\kappa_A+o(1)}
(\log p)^{-2/3}(\log\log p)^{-1/3}
]
does not imply (o(1)) when (b\kappa_A=1/2), because an unspecified (p^{o(1)}) can dominate every fixed polylogarithmic saving.

This is material to the claimed fidelity threshold, though not to the strict-above-threshold rigidity mechanism. The argument as stored supports (b\kappa_A>1/2); the equality case needs a sharper second-order PNT/horizon estimate that cancels or dominates the logarithmic correction above. Narrowing (24) to strict inequality, or supplying such a quantitative boundary argument, would resolve the objection without otherwise changing the matched-source result.
