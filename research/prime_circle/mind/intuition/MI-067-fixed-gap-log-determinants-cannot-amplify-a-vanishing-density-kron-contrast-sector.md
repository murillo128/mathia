# MI-067 — Thin positive Kron contrast cannot create extensive mass, and summable deleted-layer coupling kills its unscaled outliers

**Evidence level:** exact/asymptotic spectral synthesis from [PC-392](../../findings/PC-392-fixed-gap-log-determinants-cannot-amplify-the-thin-multi-deletion-contrast-sector.md), [PC-393](../../findings/PC-393-complete-survivor-connectivity-closes-the-singular-normalized-determinant-edge.md), and [PC-394](../../findings/PC-394-summable-deleted-layer-coupling-closes-the-kron-outlier-window.md), sharpening the exceptional-observable escape left by PC-391.

PC-391 isolates the irreducible simultaneous-deletion correction as a positive semidefinite contrast operator `Delta_T` of rank at most `k-1`. PC-392 shows that positive-regularized determinant ratios reduce exactly to this thin sector and cannot create an extensive normalized log-determinant. PC-393 closes the apparent singular loophole: the common constant zero mode lies outside the contrast carrier, complete survivor connectivity gives a mean-zero spectral floor, and the same normalized determinant conclusion persists through the exact pseudodeterminant endpoint.

PC-394 removes the most immediate nonextensive escape in the natural summable-tail phase. Writing the simultaneous correction as

`Delta_T=P Q P^*`, with `0<=Q<=K`,

where `K` is the internal deleted-layer Laplacian and the columns of `P` are normalized incidence profiles, gives the exact contraction

`||Delta_T||_op <= tr K`.

At a successive primorial step the deleted vertices are all multiples of the new prime `q`, so their mutual separations live on a coarse `q`-lattice. For inverse-power chord conductances with exponent `alpha>1/2` and window `H=p^u`, Buchstab counting plus summability of the internal tail yields

`||Delta_T||_op = O(p^(u-1-2 alpha)/log p)`.

Hence throughout `2<u<=1+2 alpha` the entire irreducible simultaneous-deletion correction tends to zero in operator norm. Every eigenvalue of the true Kron response is then `o(1)` from the independent-star baseline. For the canonical inverse-square interaction, this closes persistent unscaled outliers through the full first higher-boundary range `2<u<=3`.

The reusable distinction is between **thin rank**, **determinant amplification**, and **operator amplitude**. A vanishing-rank carrier can in principle support an exceptional eigenvalue, so normalized determinant control alone does not close outliers. Here the source-forced coarse spacing of the deleted layer supplies the extra amplitude estimate that does.

The positive linear-Kron branch therefore survives only in regimes not covered by this amplitude collapse: longer windows `u>1+2 alpha`, nonsummable tails, renormalized exceptional observables, cross-level orientation/evolution of the contrast subspaces, or signed/indefinite/nonlinear operators where the positive Schur and conductance bounds no longer apply.

**Boundary.** The operator-norm conclusion uses positive regularized inverse-power chord conductances, fixed polynomial primorial windows and `alpha>1/2`. The threshold `u=1+2 alpha` is a proof boundary, not evidence for a phase transition. PC-394 does not rule out rescaled outliers, longer windows, signed kernels or cross-level state information, and none of the Kron results supplies a zeta-zero mechanism.
