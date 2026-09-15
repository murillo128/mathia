---
type: adversarial-review
target: research/nyman_beurling/findings/NB-141-selberg-density-makes-polynomial-confluence-cells-rare-but-not-forbidden.md
---

# Adversarial review

## Adversary

The general rarity statement (5) has a boundary mismatch in the Selberg reduction. Under the stated hypothesis `Delta_G <= a/2`, a zero in the cell is only guaranteed to satisfy `beta >= 1/2 + a/2` by (11), while the counting function in (12) is defined with the strict condition `beta > sigma`. At the endpoint `Delta_G = a/2`, zeros with `beta = 1/2 + a/2` contribute to `m_G(t)` but are absent from `N_>(sigma_a,3G)`, so the first inequality in (18) does not follow as written.

The polynomial application `Delta_G = G^{-B}` is eventually strictly smaller than `a/2`, so this does not attack the intended asymptotic conclusion (7). But the boxed theorem (5) is stated for the larger `<=` domain. Closure requires either narrowing the hypothesis to `Delta_G < a/2` (with a fixed strict margin sufficient for the chosen Selberg threshold), replacing the strict counting function by a non-strict one with a justified density bound, or otherwise accounting for boundary-line zeros explicitly.