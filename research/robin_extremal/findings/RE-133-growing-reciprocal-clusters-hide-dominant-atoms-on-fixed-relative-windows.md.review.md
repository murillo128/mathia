---
type: adversarial-review
target: research/robin_extremal/findings/RE-133-growing-reciprocal-clusters-hide-dominant-atoms-on-fixed-relative-windows.md
---

# Adversarial review

## Adversary

Equation (5) is incompatible with the finding's attained-edge claim as currently quantified. The theorem defines

`M_K^{ctl}(U_j) := max_ρ |a_{ρ,K}(U_j)| = (1+o(1)) U_j^{-A}`

while also requiring a finite attained right edge `Re ρ = Θ`. Section 2 says such an attained edge may be supplied by a fixed finite quartet. For any fixed right-edge member `ρ_*` with `Re ρ_* = Θ`, the exponential factor in (3) is exactly one and

`a_{ρ_*,K}(u) -> 1/[ρ_*(1-ρ_*)] != 0`

as `u -> infinity`. Hence a maximum over the full `Z_ctl` is bounded below by a positive constant and cannot be asymptotic to `U_j^{-A} -> 0`.

The construction later proves dominance only inside the strict-subedge packet (4), where the added edge quartet is explicitly absent. The objection is resolved if the maximum in (5), and every use of it in (6), is genuinely intended to range only over the strict-subedge packet and that domain is made mathematically explicit; alternatively the attained-edge requirement would have to change. As written, the displayed global maximum and the finite attained edge cannot both hold.