# VIS-357 — compact Wang anchor degeneration is exactly q-point packing collapse

## Claim

Fix an asymptotic depth `q>=2`, a compact inverse-scale interval `[r,R] subset (0,infinity)`, and the invertible Wang tail matrix

`D_beta=diag(beta_1,...,beta_q)`.

For a finite active inverse-scale set `X={x_1,...,x_N} subset [r,R]`, `N>=q`, define its best `q`-point packing separation by

`delta_q(X)=max_(J subset X, |J|=q) min_(x!=y in J) |x-y|`,

and its best fixed-depth Wang anchor quality by

`alpha_q(X)=max_(J subset X, |J|=q) s_min(D_beta W_J)`,

where `W_J=(x_j^k)_(1<=k<=q, x_j in J)`.

Put `M=q(q-1)/2`, `beta_-=min_k |beta_k|`, `beta_+=max_k |beta_k|`,

`B=max(R,R^q)`,

and

`L_q(R)=(sum_(k=1)^q k^2 R^(2k-2))^(1/2)`.

Then every such finite scale set satisfies the two-sided estimate

`[beta_- r^q/(qB)^(q-1)] delta_q(X)^M <= alpha_q(X) <= [beta_+ L_q(R)/sqrt(2)] delta_q(X)`.

Consequently, for any sequence of compact scale banks `X_T subset [r,R]`,

`alpha_q(X_T) -> 0  iff  delta_q(X_T) -> 0`.

Equivalently, loss of **every** uniformly conditioned fixed-depth `q`-scale anchor inside a fixed compact interval occurs exactly when the scale set loses every `q`-point separated configuration. In packing/covering language, this is equivalent to the following collapse: for every `epsilon>0`, all sufficiently large `T` admit an `epsilon`-net for `X_T` with at most `q-1` centers. Thus the compact anchor-loss branch left open by `VIS-356` is not diffuse growing-bank complexity; it is asymptotic concentration into at most `q-1` shrinking inverse-scale clusters.

For `q=1` there is no compact anchor-degeneration branch at all: `s_min(D_beta W_{x})=|beta_1|x >= |beta_1|r`.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL VANDERMONDE/PACKING GEOMETRY + STRUCTURAL NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This finding classifies degeneration of the **best square `q`-column anchor**. It does not assert that the smallest positive singular value of the full rectangular bank map degenerates when `alpha_q(X_T)->0`: growing cluster multiplicity can add positive-semidefinite Gram mass and may compensate shrinking within-cluster separation. That multiplicity-versus-width problem is a separate quantitative question.

## 1. A separated q-tuple forces a uniform anchor floor

Choose a `q`-point subset `J={x_1,...,x_q}` that realizes `delta=delta_q(X)`. Its truncated Wang moment matrix is

`W_J=(x_j^k)_(1<=k,j<=q)`.

Because the rows start at power one rather than zero,

`det W_J = (prod_(j=1)^q x_j) prod_(1<=i<j<=q)(x_j-x_i)`.

Every `x_j>=r` and every pair in `J` is separated by at least `delta`, so

`|det W_J| >= r^q delta^M`.

Also every matrix entry has modulus at most `B`, hence

`||W_J||_2 <= ||W_J||_F <= qB`.

If `s_1>=...>=s_q>0` are the singular values of `W_J`, then

`|det W_J|=prod_i s_i <= ||W_J||_2^(q-1) s_q`.

Therefore

`s_min(W_J) >= r^q delta^M/(qB)^(q-1)`.

Left multiplication by the fixed invertible diagonal matrix gives

`s_min(D_beta W_J) >= beta_- s_min(W_J)`.

Since `alpha_q(X)` is the maximum over all `q`-column anchors, this proves the lower bound.

The estimate is intentionally crude. Its role is structural: any one `q`-tuple that remains uniformly separated inside `[r,R]` supplies the stable anchor required by `VIS-356`.

## 2. A collapsing best packing forces every anchor to collapse

For any `q`-point subset `J`, let

`d(J)=min_(x!=y in J)|x-y|`.

Choose a closest pair `x_i,x_j` in `J` and the unit coefficient vector

`z=(e_i-e_j)/sqrt(2)`.

Writing `w(x)=(x,x^2,...,x^q)^T`,

`s_min(D_beta W_J) <= ||D_beta W_J z||_2`
` = ||D_beta(w(x_i)-w(x_j))||_2/sqrt(2)`.

On `[r,R]`, the derivative of `w` has norm at most

`L_q(R)=(sum_(k=1)^q k^2 R^(2k-2))^(1/2)`.

The mean-value estimate therefore gives

`s_min(D_beta W_J) <= [beta_+ L_q(R)/sqrt(2)] d(J)`.

Taking the maximum over `J` yields

`alpha_q(X) <= [beta_+ L_q(R)/sqrt(2)] delta_q(X)`.

Together with the determinant lower bound, this proves

`alpha_q(X_T)->0 iff delta_q(X_T)->0`.

Thus, inside fixed compact scale geometry, there is no third mechanism by which all fixed-depth anchors can disappear: either some separated `q`-tuple survives and supplies a floor, or the best `q`-point packing scale itself collapses.

## 3. Packing collapse is the same as at most q-1 shrinking clusters

The quantity `delta_q(X)` is the largest separation scale at which `X` contains `q` mutually separated points.

Suppose `delta_q(X_T)->0`. Fix `epsilon>0`. For large `T`, no `q` points of `X_T` are pairwise `epsilon`-separated. Take a maximal `epsilon`-separated subset of `X_T`. It therefore has at most `q-1` points. By maximality, those points form an `epsilon`-net of `X_T`.

Conversely, suppose that for every `epsilon>0`, all sufficiently large `T` can be covered by at most `q-1` balls of radius `epsilon`. Any `q` selected points then place two points in the same ball, so their distance is at most `2epsilon`. Hence `delta_q(X_T)<=2epsilon` eventually, and `delta_q(X_T)->0`.

Therefore the compact anchor-loss condition is equivalent, at the level of asymptotic vanishing, to concentration into at most `q-1` clusters whose covering radii tend to zero. The cluster centers may move with `T`; no fixed limiting centers are required.

This converts the qualitative phrase “every anchor degenerates” from `VIS-356` into an explicit geometric resource. Any continuation that remains in `[r,R]` must now pay for shrinking cluster width and whatever multiplicities accumulate inside those clusters.

## 4. What the classification does not close

The result concerns the **best square anchor**, not the full rectangular moment map. This distinction is load-bearing.

If a bank contains many columns inside a shrinking cluster, each individual `q`-column anchor can become ill-conditioned while the full Gram matrix

`(D_beta V_N)(D_beta V_N)^* = sum_j D_beta w(x_j)w(x_j)^* D_beta^*`

receives more positive-semidefinite mass as multiplicity grows. `VIS-356` showed that a stable anchor is sufficient for a uniform full-map floor; the present result characterizes failure of that sufficient condition, but failure of the condition is not itself proof of full-map degeneration.

Accordingly, a proposed compact escape must track at least two quantities together: cluster widths and cluster occupancies/weights. It must show that the gain survives after the full rectangular singular value or the relevant quotient norm is computed. Merely exhibiting pairwise scale collisions is insufficient.

The theorem also does not cover `q=q(T)->infinity`, `r=r(T)->0`, `R=R(T)->infinity`, changing coefficient norms/topologies, infinite-dimensional limits, nonlinear source operations, or direct signed information about `G`. Those remain distinct exits from the fixed compact finite-depth ledger.

Source-adaptive selection does not alter the classification pointwise: if `G` selects `X_T(G) subset [r,R]`, the same packing-versus-anchor inequalities apply to each realized scale set. Any source-specific advantage must enter through the selected cluster geometry, its multiplicities/weights, growing order, scale escape, or an additional arithmetic estimate.

## Prior-art audit

The matrix ingredients are classical. Walter Gautschi's **Norm Estimates for Inverses of Vandermonde Matrices**, *Numerische Mathematik* 23 (1975), 337–347, studies inverse-norm/conditioning behavior of Vandermonde matrices and the effect of node geometry and scaling. Fermín S. V. Bazán, **Conditioning of Rectangular Vandermonde Matrices with Nodes in the Unit Disk**, *SIAM Journal on Matrix Analysis and Applications* 21:2, DOI `10.1137/S0895479898336021`, gives rectangular conditioning bounds depending on matrix size and node separation and explicitly notes that adding columns can improve conditioning in suitable regimes. Dmitry Batenkov, Laurent Demanet, Gil Goldman, and Yosef Yomdin, **Conditioning of Partial Nonuniform Fourier Matrices with Clustered Nodes**, *SIAM Journal on Matrix Analysis and Applications* 41:1 (2020), 199–220, DOI `10.1137/18M1212197`, proves sharp clustered-node smallest-singular-value bounds for the unit-circle/partial-Fourier Vandermonde setting.

Those works establish that node separation, clustering, rectangular oversampling, and singular-value degradation are classical conditioning phenomena. The packing/covering argument above is elementary metric geometry. No novelty is claimed for any of them, for the Vandermonde determinant estimate, or for the mean-value upper bound.

The Mathia-specific delta is only the exact classification of the remaining compact **anchor-loss escape** in the current Wang ledger: after `VIS-356`, “all fixed-depth anchors degenerate” can be replaced by the concrete statement that the inverse-scale bank collapses into at most `q-1` shrinking clusters. The separate full-rectangular multiplicity-versus-width question remains open rather than being silently identified with anchor collapse.

## Dependencies

- `VIS-343`: scale count and attainable moment-cancellation order.
- `VIS-354`: exact block-Vandermonde Wang tail-coefficient map.
- `VIS-355`: compact source-adaptive selection obeys the same quotient floor.
- `VIS-356`: a surviving uniformly conditioned `q`-column anchor prevents fixed-depth bank enlargement from lowering the quotient floor.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue narrowed by this classification.

## Research consequence

The compact fixed-depth branch is narrower again. **If every `q`-scale anchor degenerates while all inverse scales remain in a fixed compact subset of `(0,infinity)`, the bank must asymptotically collapse into at most `q-1` shrinking scale clusters.** There is no additional diffuse compact geometry to investigate at the anchor level.

Future work on this branch should therefore price the actual clustered rectangular map: how cluster widths, occupancies, coefficient normalization, and moment depth jointly control the smallest positive singular value and whether any resulting source-dependent choice survives Wang's unchanged destination derivative tax. Growing `q`, scale escape, infinite topology, nonlinear source dependence, and direct signed arithmetic information remain separate live mechanisms.