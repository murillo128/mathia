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

## Owner

The objection is correct for a maximum over the full `Z_ctl`, but that is not the domain used by the construction. The intended quantity in (5) is the maximum over exactly the strict-subedge positive-frequency index set of (4),

`{rho in Z_ctl : sigma_0 <= Re rho < Theta, Im rho > 0}`,

and the same restricted quantity is the normalizing scale in (6). The fixed quartet on `Re rho = Theta` is included only to make the formal right edge attained and is explicitly outside both (4) and this packet maximum.

With that domain, the proof already gives the claimed asymptotic: (30) gives the empty-subset atom `(1+o(1))U_j^{-A}`; (31) makes every nonempty atom in stage `j` smaller by `r^{|S|}(1+o(1))`; and (36) makes every strict-subedge atom from all other stages `o(U_j^{-A})` on the relevant window. Thus the restricted maximum is `(1+o(1))U_j^{-A}`, while the edge quartet has no role in either the hiding estimate or its normalization.

So this is a domain-specification defect in (5), not a change to the matched-control construction or its attained-edge claim. If this defense is accepted, the same-claim persistence needed in the canonical finding is to replace the bare `max_rho` in (5) by the explicit strict-subedge domain and state that (6) uses that same packet maximum.