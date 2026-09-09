# Robin-extremal source anchors

This file records durable literature dependencies for `research/robin_extremal/`. It is an anchor list, not a search history.

## Core criterion

- [`research/prior_art/robin-criterion.md`](../prior_art/robin-criterion.md). Role: Mathia prior-art anchor for the divisor-sum inequality equivalent to RH and its extremal-number interpretation.
- [`research/prior_art/lagarias-criterion.md`](../prior_art/lagarias-criterion.md). Role: neighboring divisor-sum criterion and boundary against merely translating between known RH-equivalent inequalities.

## Colossally abundant structure

- Leonidas Alaoglu and Paul Erdos, *On highly composite and similar numbers*, Transactions of the American Mathematical Society **56** (1944), 448-469, DOI `10.2307/1990319`; primary scan: `https://www.renyi.hu/~p_erdos/1944-03.pdf`. Role: colossally abundant variational definition, prime-exponent threshold structure, and supporting-slope description used by `RE-001` and `RE-002`.
- Guy Robin, *Grandes valeurs de la fonction somme des diviseurs et hypothese de Riemann*, Journal de Mathematiques Pures et Appliquees **63** (1984), 187-213. Role: Robin's criterion, the colossally abundant envelope for `G(n)=sigma(n)/(n log log n)`, and the CA above/below-threshold behavior used in `RE-001`--`RE-002`.
- Marco Mantovanelli, *Colossally Abundant Numbers, Robin's Inequality, and an Exact Prime-Layer Workload*, preprint, August 2026; public computational/manuscript companion: Zenodo DOI `10.5281/zenodo.22014299`. Role: closest prior art for the tangent parameter `epsilon_X=(X log X)^(-1)`, regular self-tangent CA states, prime-layer event workload, exact packet identity, moment hierarchy, and prime-frontier normal form. This is recent preprint prior art, not an accepted RH result; `RE-001` independently reconstructs the exact identities it uses, while `RE-002` treats the event/workload framework as prior art and adds a local peak-clearance gate.
- Bruce Zimov, *On the Least Colossally Abundant Exception to Robin's Inequality*, arXiv:2510.23889 (2025). Role: neighboring prior art on consecutive-CA transitions and the least hypothetical CA counterexample; it estimates the Robin-ratio change from prime/semiprime consecutive quotients. `RE-002` uses it as a comparison boundary rather than as a load-bearing theorem: the secant-balanced transition-coordinate criterion derived there is a different local statement.

## Expansion rule

Add primary sources when a canonical finding depends on an exact theorem about superabundant/colossally abundant integers, exponent-profile transitions, explicit prime-distribution errors, or extremal divisor-sum bounds. Finite verification records should be cited only when a finding actually depends on their verified range.