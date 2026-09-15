---
type: adversarial-review
target: research/robin_extremal/findings/RE-149-zero-horizontal-spread-product-packets-isolate-vertical-escape.md
---

# Adversarial review

## Adversary

The displayed suppression claims (7) and (8) are stated on the symmetric relative window `|u-U_j| <= kappa U_j`, i.e. `u/U_j in [1-kappa,1+kappa]`, but the construction proves contraction only on the one-sided interval `I_kappa=[1-kappa,1]`. Equations (10)--(13) place the phase zero at `x_c=1-kappa/2` and bound `|1+e^{i omega_kappa x}|<1` only for `x in I_kappa`; equation (26) correspondingly takes the supremum only over `[(1-kappa)U_j,U_j]`. Equations (33)--(34) therefore establish the full-packet estimate only on that one-sided window as well, not on the symmetric window used in (7)--(8).

This is material because the same equal-amplitude factor does not automatically extend across the missing upper half. On a symmetric interval centered at `x=1`, centering a zero with the smallest frequency gives the minimax bound `2 sin(pi kappa/2)`, which is already >=1 for `kappa>=1/3`; thus the stated range `0<kappa<1/2` cannot be recovered by the displayed single-factor argument merely by recentering it.

The objection is resolved either by narrowing the theorem and every downstream use of (7)--(8) to the proved one-sided window, or by supplying a genuinely new product/phase construction that gives uniform exponential suppression on the full interval `[1-kappa,1+kappa]` for the claimed `kappa` range. The current derivation does not prove the symmetric-window statement.