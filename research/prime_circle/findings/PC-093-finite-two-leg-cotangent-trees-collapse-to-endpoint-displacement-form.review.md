---
type: adversarial-review
target: research/prime_circle/findings/PC-093-finite-two-leg-cotangent-trees-collapse-to-endpoint-displacement-form.md
---

# Adversarial review

## Adversary

The branch-message reduction is sound, but the final endpoint-displacement conclusion is stated under a weaker shell-disjointness hypothesis than PC-092 actually proves. PC-093's Prime-Circle setup requires only distinct exact orders along adjacent vertices. After contracting off-path branches, the exposed path can therefore revisit the same exact-order shell at nonadjacent internal vertices.

PC-092's serial closure theorem, however, is stated for paths through pairwise distinct exact-order shells. Its weighted two-hop identity requires the intermediate shell to be disjoint from the endpoint shells, with only the special direct return `A=C` treated separately. Adjacent disjointness in PC-093 does not ensure those hypotheses at every inductive reduction once an internal shell is revisited. Thus the implication

`finite two-leg tree -> PC-092 serial class -> endpoint displacement`

does not follow for the full Prime-Circle class currently claimed.

This is not merely a formal concern: PC-094 now explicitly adopts pairwise-disjoint exact-order shells and lists reused nonadjacent shells as an unproved repeated-pole/coincidence boundary. The two findings should not simultaneously treat that repeated-shell case as both covered and outside the clean reduction.

The objection is resolved if PC-093 is restricted to pairwise distinct shell sets along the exposed path (or globally, if that is the intended class), or if a separate derivation extends PC-092 to arbitrary repeated internal exact-order shells and proves the same endpoint-displacement closure through the resulting return/overlap configurations.