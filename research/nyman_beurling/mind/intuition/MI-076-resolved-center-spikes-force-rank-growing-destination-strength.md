# MI-076 — Resolved center spikes force rank-growing destination strength

**Evidence level:** exact destination-side synthesis from [NB-269](../../findings/NB-269-resolved-multi-shell-hardy-projection-compresses-a-shallow-matched-ford-residue-into-a-1-over-k-center-spike.md), [NB-270](../../findings/NB-270-reciprocal-shell-weight-summability-is-the-exact-rank-uniform-band-diagonal-coercivity-threshold.md), and [NB-271](../../findings/NB-271-inverse-gram-anchor-criterion-forces-k-scale-operator-growth-for-any-off-diagonal-ford-channel-repair.md).

A resolved multi-shell carrier can retain an order-one center residue while its canonical Hardy energy vanishes because the residue narrows as rank grows. NB-269 makes this exact: after legal Hardy projection the shell-frequency cells are disjoint, the uniform positive Euler carrier `c_j=1/K` has full-line and fixed-window energy `Theta(1/K)`, yet the current stays order one on a center interval of width `Theta(1/K)`.

The missing destination resource is therefore not generic off-diagonal coherence; it is enough strength in the anchor direction. NB-270 shows that a diagonal shell weight `q_j` gives a rank-uniform floor exactly when `sum q_j^(-1)` is uniformly bounded. Ordinary Hardy weighting leaks as `1/K`, the critical half-derivative weight still leaks as `1/log K`, and only reciprocal-summable weights are coercive.

NB-271 gives the invariant form of the same statement. For any positive Gram matrix `A_K`, the anchored minimum is governed by `1^*A_K^dagger 1`; if the nullspace is visible to the Euler anchor, the minimum is zero. Testing the uniform carrier also gives the unavoidable scale law

`anchored floor <= ||A_K||_op / K`.

Hence a uniform positive floor requires `Theta(K)` operator growth relative to the canonical resolved channel. Fixed-band, summably decaying or uniformly `H^2`-continuous positive corrections cannot restore coercivity.

The reusable audit is to measure **evaluation concentration and anchor-aligned Gram strength together**. Pointwise residue is not quadratic mass when bandwidth grows, and off-diagonal structure is useful only if its inverse Gram remains controlled on the anchor while its strength grows at the rank scale demanded by the uniform carrier.

**Boundary.** These results classify positive quadratic observables on the resolved projected Ford channel, not the complete Nyman--Beurling distance. The full target may contain additional components, constraints or cross terms not uniformly controlled by that channel. The matched packet is a compatibility control rather than a statement about actual zeta zeros.