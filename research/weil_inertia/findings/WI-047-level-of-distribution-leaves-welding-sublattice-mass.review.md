---
type: adversarial-review
target: research/weil_inertia/findings/WI-047-level-of-distribution-leaves-welding-sublattice-mass.md
---

# Adversarial review

## Adversary

The prior-art boundary used in the finding is stale. The text calls Lichtman's `66/107` result the strongest currently located unconditional level in the triply-well-factorable prime setting, but Alexandru Pascadi, *On the exponents of distribution of primes and smooth numbers* (arXiv:2505.00653, 2025), states an unconditional level `5/8-o(1)` for primes with triply-well-factorable weights, explicitly removing the Selberg-eigenvalue assumption from the earlier `5/8` result. Thus equations (35) onward and the surrounding `LITERATURE+DERIVED` / `PRIOR-ART-REDIRECTION` discussion do not currently test against the strongest known unconditional comparison.

This does not appear to invalidate the geometric obstruction itself: the formulae (1)--(2) are stated for every fixed `theta<1`, and the box (29) still fails both necessary AP inequalities at `theta=5/8` (for example the worst lower corner gives `0.39+(5/8)0.39=0.63375>0.625`). But the canonical finding should update the literature claim/source bridge and re-run its explicit strongest-known control at `theta=5/8`, rather than presenting `66/107` as the current record. A direct check against Pascadi's precise weighted theorem hypotheses should also preserve the existing caveat that this is not a generic black-box AP theorem.