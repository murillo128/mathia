# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Separate logarithmic aggregate coercivity from the actual Hardy quadratic bridge

**Linked intuitions:** `MI-062-the-critical-ford-mark-is-a-growing-moment-observable`, `MI-063-demodulated-ford-energy-is-bandlimited-at-the-window-scale`, `MI-064-signed-scalar-coherence-shrinks-only-by-paying-total-variation`, `MI-065-signed-carrier-cost-must-be-measured-after-quotienting-unresolved-microscopic-dipoles`, `MI-066-resolved-carrier-channels-can-amortize-hilbert-cancellation-at-j-two-thirds`, `MI-067-critical-hardy-zero-sampling-is-logarithmically-displaced-from-the-real-ford-axis`, `MI-068-a-critical-ford-notch-exports-the-scalar-carrier-into-a-depth-ladder`, `MI-069-near-full-positive-carriers-export-the-ford-obstruction-to-a-shrinking-boundary-layer`, `MI-070-a-cheap-signed-boundary-notch-exports-its-conditioning-into-a-ford-scale-side-lobe`, `MI-071-positive-depth-strip-suppression-is-noncoercive-with-unpriced-conditioning`, `MI-072-polynomial-rank-coupled-ford-coverage-recovers-the-euler-anchor`, `MI-073-nonquasianalytic-cutoffs-push-euler-anchor-recovery-through-any-fixed-iterated-log-loss`, `MI-074-rank-adaptive-compact-cutoffs-reach-the-logarithmic-ford-coverage-endpoint-in-aggregate`, `MI-075-logarithmic-ford-mesh-mass-does-not-force-diagonal-quadratic-energy`, `MI-076-resolved-center-spikes-force-rank-growing-destination-strength`, `MI-077-target-pairings-change-mismatch-not-source-gram-strength`.

NB-264--NB-267 force `Omega(m)` aggregate mesh response down to `O(log K)` rank-coupled coverage under bounded resolved cost. NB-268 then shows that this linear aggregate obstruction does not force diagonal quadratic energy: the legal uniform carrier keeps the aggregate mass while its damped diagonal diagnostic vanishes.

NB-269 resolves the actual Hardy-projected multi-shell diagnostic for the explicit matched packet. The resolved shell bands are disjoint after projection, so full-line Plancherel diagonalizes the shell index exactly. For the uniform positive carrier `c_j=1/K`, the projected energy is `Theta(1/K)` even though the center value remains order one on a spike of width `Theta(1/K)`. Thus the hard-window quadratic form itself can vanish; generic off-diagonal shell terms do not rescue this carrier.

NB-270 classifies every positive band-diagonal repair. If shell `j` is charged by `q_j`, the Euler anchor `sum c_j=1` has a rank-uniform quadratic floor exactly when `sum_j q_j^(-1)` remains bounded. Sobolev weights have the sharp threshold `s>1/2`; the critical `s=1/2` endpoint still leaks as `1/log K`, with the exact logarithmic refinement determined by reciprocal summability. The ordinary Hardy norm is the leaking `s=0` case.

NB-271 removes the generic off-diagonal loophole at the same abstraction level. For a positive Gram matrix `A_K`, the optimal anchored energy is `1/(1^* A_K^dagger 1)` when the anchor lies in the range, and zero if an anchor-visible null direction exists. Testing the uniform anchored vector shows that any rank-uniform positive floor requires operator strength at least `Theta(K)` relative to the canonical resolved Hardy norm. Uniformly bounded, finite-band or summably decaying positive corrections therefore cannot repair the leak.

NB-272 sharpens the remaining target-sensitive loophole by an exact finite-section identity. For source Gram `R_K=S_K^*S_K`, target pairing `b_K=S_K^*g`, and Euler anchor `e_K^*c=1`, the constrained residual splits into

`delta_K^2 + |mu_K|^2/(e_K^*R_K^(-1)e_K)`,

where `delta_K=dist(g,ran S_K)` and `mu_K=1-e_K^*R_K^(-1)b_K`. The target cross term changes the unconstrained projection and anchor mismatch but does not modify the source-source Hessian `R_K`; it cannot itself be the `Theta(K)` positive Gram repair sought after NB-271. In the resolved regime `R_K asymp I`, the mismatch penalty is `Theta(|mu_K|^2/K)`, so only a nonvanishing section defect, a `sqrt(K)`-scale anchor mismatch, or genuinely new source-source quadratic geometry can provide an order-one target-side obstruction.

The live destination question is therefore a concrete fork. Estimate the actual canonical-target quantities `delta_K` and `mu_K` in the same rank-coupled resolved regime, or identify the smallest exact source component outside the NB-269 channel whose relative Gram has `Omega(K)` strength and passes the inverse-Gram anchor test. Merely invoking target cross terms, generic off-diagonal coherence, diagonal reweighting or local/summable corrections is closed at this abstraction level.

The separate source-side question of whether `O(log K)` aggregate coverage is minimal remains open, but improving that radius cannot by itself overcome the destination leak. Aggregate response, projected Hardy energy, target projection defect, anchor mismatch, inverse-Gram conditioning and the full Nyman norm are distinct currencies.

## Realize the Ford divisor through a legal mechanism without hiding the singularity in the source

**Linked intuitions:** `MI-078-the-ford-current-is-a-singular-mellin-derivative-of-the-canonical-nyman-source`, `MI-079-finite-differentiated-nyman-sources-cannot-carry-interior-divisor-current`, `MI-080-finite-boundary-repair-is-exactly-hardy-zero-sampling-geometry`.

NB-276 gives an exact source identity independent of the proposed/pending NB-273--NB-275 chain. For the canonical Nyman synthesis

`N[P](s)=zeta(s)/s (P(s)-P(1))`

and `P_*(s)=1/zeta(s)`, one has `N[P_*]=1/s`, while differentiation gives

`-s N[P_*'] = zeta'(s)/zeta(s) + zeta(s)`.

Thus the Ford divisor current is encoded as the singular Mellin derivative of the canonical Möbius source. The obstruction is legal realization: differentiation inserts `log k`, multiplication by `s` is unbounded in the Hardy geometry, and the zero poles appear only after meromorphic continuation rather than a norm-continuous `H^2` passage.

NB-277 closes the canonical Abel-shift repair. Replacing `1/zeta(s)` by `1/zeta(s+epsilon)` displaces the Ford depth by `X epsilon`. Preserving Ford depth requires `X epsilon->0`, but then the differentiated coefficients on the shell retain their full `log k~X` size. Strong damping costs a non-negligible or diverging Ford displacement.

NB-278 closes the direct finite differentiated linear-truncation route more strongly. For every finite Dirichlet polynomial `P`, the current `-zeta(s)(P'(s)-P'(1))` is entire and has identically zero interior divisor current. The limiting object `zeta'/zeta+zeta` has nonzero residues at zeta zeros. Distributional continuity of `bar-partial` therefore forbids convergence of these finite currents across any neighborhood containing a zero, regardless of coefficient growth or Hardy-norm blowup.

NB-279 resolves the immediate boundary/contour escape exactly. Every finite legal residual `r_P=1/s-N[P]` satisfies `r_P(rho)=1/rho` at every nonzero zeta zero, so a contour weighted by `s zeta'/zeta` counts the enclosed divisor without making the finite source singular. But the poles have moved into the **dual functional**. In `H^2(C_(1/2))`, the exact content is the reproducing-kernel interpolation bound

`||r_P||_(H^2)^2 >= v^* G^(-1) v`,

with `G_(jk)=1/(rho_j+conj(rho_k)-1)` and `v_j=1/rho_j`.

NB-280 now evaluates that quantity exactly. The canonical vector is the sample vector of the fixed Hardy kernel `k_1(s)=1/s`, so

`v^*G^(-1)v = 1-|B_Z(1)|^2 = 1-product_(rho in Z)(1-(2Re(rho)-1)/|rho|^2)`.

The apparent inverse-Gram conditioning frontier is therefore an internal collision with the finite Burnol/Blaschke target defect already analyzed in NB-114--NB-116. Pairwise spacing and Cauchy-Gram condition number cannot make this canonical point-value certificate large at high ordinate. NB-116 already gives `v^*G^(-1)v=O(1/G)` for every finite packet of actual right-half zeros above height `G`, while the matched Ford packets of NB-231 can retain order-one Ford residue and vanishing point-sampling energy.

The live source-native question has consequently moved **outside the finite point-evaluation span**. A viable boundary mechanism must contain information not equivalent to the same Burnol defect: a genuinely finite arithmetic-section interaction, higher derivative jets at multiple zeros, or another nonlinear/boundary construction with a distinct destination quantity. Better conditioning of the same canonical sampling matrix is no longer a route.

This research line does not promote NB-273--NB-275 and does not use their pending claims as premises. NB-276--NB-280 do not establish `H^2` convergence to the singular current, an order-one Hardy lower bound, or failure of Möbius cancellation; they isolate the exact continued current, close Abel damping and finite interior approximation, identify the finite boundary route with Hardy zero sampling, and then classicalize its canonical inverse-Gram cost as the already-controlled Burnol defect.

## Keep preassigned strips, rank-coupled coverage, certificate complexity, source Gram and target zero Gram distinct

A future theorem must state the order of quantifiers and every bounded resource. NB-269--NB-272 show that an order-one point residue can be hidden in a shrinking width while every positive quadratic observable continuously dominated by the resolved `H^2` channel pays the rank leak, and that the ordinary target pairing does not secretly alter the source Gram. A successful target mechanism must therefore locate either a genuine target mismatch that survives at order one or a new source-source component with the necessary rank-growing strength.

NB-276--NB-280 add a different source-native route rather than repairing that quadratic channel. The exact Ford current is present only after a singular derivative/continuation operation; Abel smoothing cannot preserve Ford depth while removing the derivative tariff; finite differentiated Nyman sources have the wrong interior divisor-current topology; the legal finite boundary repair reduces to forced Hardy evaluations at the zeros; and for the canonical values those evaluations collapse exactly to the finite Burnol/Blaschke defect. Future work must keep finite legal source approximation, singular dual weights, generic Gram conditioning, target-coupled sampling data, higher-jet information, meromorphic continuation and Ford-scale localization distinct rather than treating the exact contour identity or an ill-conditioned Cauchy matrix as extra Nyman coercivity.
