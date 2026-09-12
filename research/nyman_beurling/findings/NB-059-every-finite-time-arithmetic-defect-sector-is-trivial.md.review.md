---
type: adversarial-review
target: research/nyman_beurling/findings/NB-059-every-finite-time-arithmetic-defect-sector-is-trivial.md
---

# Adversarial review

## Adversary

The load-bearing local-Dirichlet step in Section 3 is not supplied by the cited source as written. Equation (9) asserts `N^perp ∩ D_{delta_zeta} = {0}` for every boundary point `zeta in T`, but arXiv:2203.05030v4 states the basic rigidity only at the distinguished point `1`: Theorem 2 gives `N^perp ∩ D_{delta_1} = {0}`, and Theorem 13 extends this to the `D_1^p` scale. In that version, Corollary 10 is instead a zero-free-half-plane consequence and does not provide all-boundary local rigidity.

This matters to the proof, not just the citation. A compact-time half-plane defect may indeed give a Cayley image holomorphic through a finite boundary point, hence membership in `D_{delta_zeta}` at that image, but the natural Nyman space `N` is not shown here to be rotation/automorphism invariant. Therefore rigidity at disk point `1` cannot simply be transported to an arbitrary `zeta` while keeping the same orthogonal complement. Under the usual Cayley normalization, the distinguished disk point `1` is also the boundary pole/infinite half-plane point, whereas the argument deliberately chooses a finite half-plane boundary point where the Blaschke factor extends.

To close the objection, supply one of the missing bridges: a valid source or proof that `N^perp ∩ D_{delta_zeta}={0}` at a finite boundary image relevant to this Cayley realization; a proof that the particular compact-time `Bh` lands in the distinguished `D_{delta_1}` despite the finite-point argument; or an exact conjugacy showing that the required change of Cayley/disk automorphism preserves the natural Nyman span and its orthogonal complement. Until such a bridge is established, the deduction `h=0` and hence (1)--(3) are unsupported.