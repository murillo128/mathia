---
type: adversarial-review
target: research/robin_extremal/findings/RE-150-global-gue-statistics-are-blind-to-lacunary-vertical-escape.md
---

# Adversarial review

## Adversary

The global-correlation blindness calculation in (6), (15)--(20) is independent and appears intact, but the stronger combined claim that the same control spectrum retains the `RE-149` Robin hiding conclusion inherits the unresolved window mismatch in `RE-149`. This finding repeatedly states that the scale-maximal Robin atom remains exponentially hidden and that the `RE-149` hiding estimate is unchanged, while `RE-149` currently states its main suppression on `|u-U_j| <= kappa U_j` but only proves the product contraction on the one-sided window `u in [(1-kappa)U_j,U_j]`.

Nothing in the GUE graft repairs that missing upper half of the Robin window: sections 1--3 here only make the exceptional stages sparse, and section 4 controls the added critical-line background by the lower endpoint `(1-kappa)U_j`; it does not supply a new product estimate on `[U_j,(1+kappa)U_j]`. Thus the correlation-invisibility theorem can survive, but the advertised conjunction `global GUE statistics + RE-149 symmetric-window Robin hiding` is not established at the current strength.

This objection is resolved if the canonical statement is explicitly scoped to the one-sided Robin window actually proved in `RE-149` (with the correlation-blindness conclusion otherwise unchanged), or if the upstream review is resolved by a valid symmetric-window hiding construction and that construction is shown compatible with the sparsification used here.