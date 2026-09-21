# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Separate logarithmic aggregate coercivity from the actual Hardy quadratic bridge

**Linked intuitions:** `MI-062-the-critical-ford-mark-is-a-growing-moment-observable`, `MI-063-demodulated-ford-energy-is-bandlimited-at-the-window-scale`, `MI-064-signed-scalar-coherence-shrinks-only-by-paying-total-variation`, `MI-065-signed-carrier-cost-must-be-measured-after-quotienting-unresolved-microscopic-dipoles`, `MI-066-resolved-carrier-channels-can-amortize-hilbert-cancellation-at-j-two-thirds`, `MI-067-critical-hardy-zero-sampling-is-logarithmically-displaced-from-the-real-ford-axis`, `MI-068-a-critical-ford-notch-exports-the-scalar-carrier-into-a-depth-ladder`, `MI-069-near-full-positive-carriers-export-the-ford-obstruction-to-a-shrinking-boundary-layer`, `MI-070-a-cheap-signed-boundary-notch-exports-its-conditioning-into-a-ford-scale-side-lobe`, `MI-071-positive-depth-strip-suppression-is-noncoercive-with-unpriced-conditioning`, `MI-072-polynomial-rank-coupled-ford-coverage-recovers-the-euler-anchor`, `MI-073-nonquasianalytic-cutoffs-push-euler-anchor-recovery-through-any-fixed-iterated-log-loss`, `MI-074-rank-adaptive-compact-cutoffs-reach-the-logarithmic-ford-coverage-endpoint-in-aggregate`, `MI-075-logarithmic-ford-mesh-mass-does-not-force-diagonal-quadratic-energy`.

NB-261--NB-263 move the scalar problem to the shallow depth `u~log(J/K)` and expose a quantifier split: a strip chosen before the eventual rank can be flattened at vanishing resolved Hilbert cost when conditioning and later rank are free.

NB-264--NB-267 couple coverage to rank under bounded resolved `ell^2` cost and push exact Euler-anchor reconstruction down to the pure logarithmic endpoint. With a rank-dependent `N_K asymp log K` compact cutoff, NB-267 forces

`sum_(|n Delta_m|<=C log K) |D_n| >= c m`.

This is a genuine aggregate linear obstruction, but NB-268 shows that it is not yet a quadratic Hardy obstruction. The legal uniform carrier `c_j=1/K` has a sinc-type mesh profile with `sum |D_n|^2 asymp m`; after the live damping `e^(-u) asymp 1/m`, its diagonal quadratic diagnostic satisfies

`e^(-2u) sum |D_n|^2 asymp 1/m -> 0`,

while the same carrier retains the `Omega(m)` aggregate `ell^1` response. The loss from aggregate mass to diagonal energy can therefore occur inside the admissible carrier class.

The primary destination question is now the exact Hardy/Nyman Gram form on this explicit uniform carrier. If its projected quadratic norm also vanishes, the family becomes a serious escape candidate from the source-side obstruction. If the exact norm remains `Omega(1)`, the off-diagonal/Gram term responsible for that lower bound identifies the missing coercivity mechanism. Refining the Ford cutoff further is secondary until this bridge is resolved.

The separate source-side question of whether `O(log K)` aggregate coverage is minimal remains open, but a smaller coercive radius would still not by itself solve the target problem: aggregate linear response, diagonal sample energy and projected Hardy quadratic energy must remain distinct quantities.

## Keep preassigned strips, rank-coupled coverage, certificate complexity and target norm distinct

NB-263 and NB-264--NB-268 are complementary. The former fixes the strip before rank and can export conditioning; the latter tie coverage to eventual rank and assume bounded resolved Hilbert cost. The known aggregate coercive radius reaches `O(log K)`, but NB-268 supplies a concrete warning that neither a pointwise order-one atom nor diagonal quadratic energy follows from that aggregate statement.

A future theorem must therefore state the order of quantifiers and every bounded resource, and must use the actual target quadratic form rather than substitute a diagonal proxy without proof. Growing coefficient norm, total variation, rank-adaptive cutoff order, dual reconstruction variation, off-diagonal Gram coherence and final Hardy/Nyman distance are separate currencies.