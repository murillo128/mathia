# MI-044 — Honest multiplicity prices early repair, but support cardinality alone does not rigidify it

**Evidence level:** exact synthesis from [RE-173](../../findings/RE-173-mertens-normalization-does-not-rigidify-an-infinite-prime-tail.md), [RE-175](../../findings/RE-175-euler-boundary-jets-detect-remote-compensators.md), [RE-179](../../findings/RE-179-two-jet-matching-forces-a-kv-weighted-reset-budget.md), [RE-180](../../findings/RE-180-honest-prime-multiplicities-force-a-selector-scale-deletion-tariff.md), and [RE-181](../../findings/RE-181-exact-two-jet-matching-remains-nonrigid-under-bounded-prime-multiplicity.md).

RE-179 prices delayed two-jet repair by a location-sensitive KV reset budget, but it deliberately allows relaxed signed integer coefficients. In that relaxation, a large negative repair can be concentrated into a small number of atoms, so the branch that pays the debt near the selector remains unpriced in source support.

RE-180 restores the honest ordinary-prime multiplicity constraint `m_Q(q)>=0`. Relative to the baseline multiplicity one, every negative coefficient is then exactly `-1`: an ordinary prime can be deleted once, but it cannot carry an arbitrarily large negative atom. Two exact Euler boundary coordinates force a Robin-scale amount of negative centered repair, while every repair prime beyond the protected multiplicative gap contributes only `O(1/p)` centered leverage. Therefore any honest repair must use

`N_del(infinity) = Omega(sqrt(p)/log p)`

distinct deleted primes, the same cardinality scale as the original selector deletion packet.

With the KV envelope the discrete and continuous costs combine. For a cutoff `Y`, the negative repair satisfies schematically

`N_del(Y)/p + R_b^-(Y) + ell_KV(Y) exp(-bV(Y)) >> d_p`,

where `d_p asymp 1/(sqrt(p) log p)` is the selector-scale debt. Thus avoiding a substantial remote weighted reset budget forces selector-scale many early deletions. Conversely, using `o(sqrt(p)/log p)` early deletions leaves a remote reset bill of order `d_p`.

RE-181 proves that this lower tariff can actually be paid. It builds an ordinary-prime-supported source with multiplicities in `{0,1,2}`, a protected initial region, an explicit second deletion packet of the required size, and geometrically separated repair shells. The resulting source matches both the boundary value and first Euler slope exactly, stays inside every fixed KV envelope, yet preserves a transient Robin-scale excursion before the compensating shells arrive.

This changes the interpretation of RE-180. Honest one-sided granularity converts an unpriced scalar negative mass into a large support bill, but **a large bill is not a discriminator when the admissible source class can realize it**. The missing resource is no longer deletion cardinality itself. It is a source constraint on the *placement and joint geometry* of the second deletion set and later duplications: genuine CA/Robin selector structure, a joint moment/integrality law, or another invariant that forbids the shell arrangement while still following from the arithmetic source.

The reusable principle is that resource lower bounds and source rigidity are different statements. A theorem may prove that every escape must pay a selector-scale combinatorial cost; a matched construction can still show that this cost is affordable inside the declared source class. Only a source-native restriction that makes the required payment impossible or destination-inert closes the branch.

**Boundary.** RE-181 establishes nonrigidity for the stated ordinary-prime `{0,1,2}` source class with exact two-jet matching and KV fidelity. It does not prove that actual colossally abundant/Robin selector geometry admits the same repair placement, preserve multiplicity one, or automatically extend to arbitrarily high exact Euler jets. Those are now the load-bearing distinctions; the RE-180 cardinality tariff by itself is not.