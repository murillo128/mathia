# MI-044 — Honest multiplicity prices early repair by deletion support

**Evidence level:** exact synthesis from [RE-173](../../findings/RE-173-mertens-normalization-does-not-rigidify-an-infinite-prime-tail.md), [RE-175](../../findings/RE-175-euler-boundary-jets-detect-remote-compensators.md), [RE-179](../../findings/RE-179-two-jet-matching-forces-a-kv-weighted-reset-budget.md), and [RE-180](../../findings/RE-180-honest-prime-multiplicities-force-a-selector-scale-deletion-tariff.md).

RE-179 prices delayed two-jet repair by a location-sensitive KV reset budget, but it deliberately allows relaxed signed integer coefficients. In that relaxation, a large negative repair can be concentrated into a small number of atoms, so the branch that pays the debt near the selector remains unpriced in source support.

RE-180 restores the honest ordinary-prime multiplicity constraint `m_Q(q)>=0`. Relative to the baseline multiplicity one, every negative coefficient is then exactly `-1`: an ordinary prime can be deleted once, but it cannot carry an arbitrarily large negative atom. Two exact Euler boundary coordinates force a Robin-scale amount of negative centered repair, while every repair prime beyond the protected multiplicative gap contributes only `O(1/p)` centered leverage. Therefore any honest repair must use

`N_del(infinity) = Omega(sqrt(p)/log p)`

distinct deleted primes, the same cardinality scale as the original selector deletion packet.

With the KV envelope the discrete and continuous costs combine. For a cutoff `Y`, the negative repair satisfies schematically

`N_del(Y)/p + R_b^-(Y) + ell_KV(Y) exp(-bV(Y)) >> d_p`,

where `d_p asymp 1/(sqrt(p) log p)` is the selector-scale debt. Thus avoiding a substantial remote weighted reset budget forces selector-scale many early deletions. Conversely, using `o(sqrt(p)/log p)` early deletions leaves a remote reset bill of order `d_p`.

This sharpens the source-fidelity principle. A continuous capacity bound can correctly price *where* compensating mass must appear while still discarding the atomic one-sided granularity of the actual source. Restoring that source constraint converts an apparently free early branch into a support-complexity tariff. The useful resource is therefore hybrid: location-weighted transport for remote oscillation plus discrete deletion cardinality where the source has bounded negative multiplicity.

The theorem prices rather than eliminates the early branch. A fixed multiplicative interval at scale `p` contains many more ordinary primes than `sqrt(p)/log p`, so a highly interlaced local repair is not ruled out. What is ruled out is representing that repair as a cheap scalar negative mass once the source architecture only permits one deletion per prime.

**Boundary.** The first Euler slope remains additional source information rather than a consequence of Robin's criterion, and the protected multiplicative gap is load-bearing. Positive multiplicities have no analogous support lower bound without an upper duplication cap. RE-180 does not prove that genuine CA/Robin selectors forbid the required second deletion set; it identifies the source-faithful combinatorial price that any such repair must pay.