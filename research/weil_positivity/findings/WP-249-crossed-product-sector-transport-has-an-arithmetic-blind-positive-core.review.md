---
type: adversarial-review
target: research/weil_positivity/findings/WP-249-crossed-product-sector-transport-has-an-arithmetic-blind-positive-core.md
---

# Adversarial review

## Adversary

Section 1 justifies the existence of the product automorphism `alpha` by saying that every quasi-local observable has finite support. That is false for the algebra defined in (1): `A` is the norm closure of the finite-support local algebras, so a general quasi-local element need not have finite prime support; Section 5 itself correctly acknowledges this for nonlocal coefficients.

The main crossed-product obstruction appears repairable, but the `EXACT-DERIVED` setup needs the actual extension argument. The local tensor automorphisms must be shown compatible under the inclusions `A_F -> A_{F'}` and hence define an isometric *-automorphism on the dense local union, which then extends uniquely (with its inverse) to the C*-completion. Please persist that argument, or an equivalent correct construction of `alpha`, while keeping the finite-support claims in (8)--(13) explicitly restricted to local coefficients. This would resolve the objection without changing the mathematical identity of the finding.