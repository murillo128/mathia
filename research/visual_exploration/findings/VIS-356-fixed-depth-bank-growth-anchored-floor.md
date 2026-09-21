# VIS-356 — fixed-depth Wang scale-bank growth cannot lower an anchored quotient floor

## Claim

Fix a finite asymptotic depth `q>=1` and one translation fiber of the Wang tail-coefficient map from `VIS-354`. For a bank with `N>=q` active inverse scales `x_j=a_j^(-1)>0`, write

`V_N=(x_j^k)_(1<=k<=q,1<=j<=N)`

and let `D_beta=diag(beta_1,...,beta_q)` be the fixed invertible Wang tail matrix. Suppose that among the active columns there is a `q`-column anchor `W_N` whose Wang moment matrix remains uniformly nonsingular:

`s_min(D_beta W_N) >= sigma > 0`.

A sufficient concrete condition is that the anchor consists of `q` distinct inverse scales in a fixed compact interval `[r,R] subset (0,infinity)` with pairwise separation at least `eta>0`.

Then adding any number of further scales cannot reduce the smallest nonzero singular value of the full fixed-depth moment map. More precisely,

`s_q(D_beta V_N) >= sigma`,

and hence for every coefficient vector `c in C^N`,

`||D_beta V_N c||_2 >= sigma dist(c,ker V_N)`.

This remains true when the additional scales and coefficients are chosen adaptively from the arithmetic source, provided the uniformly conditioned anchor survives.

Therefore **growing the number of active Wang scales at fixed asymptotic depth is not by itself a new conditioning escape**. Extra columns may enlarge the exact moment-cancellation kernel, but after quotienting that already-known kernel they cannot manufacture an additional small tail-coefficient vector while a uniformly conditioned `q`-scale anchor remains present.

Combined with `VIS-343`, the consequence is sharper: scale-count growth becomes an asymptotic resource only when it is used to increase the cancellation depth/order, or when every possible `q`-scale anchor itself degenerates through scale collision, escape, approach to zero, or another explicitly charged geometry. Merely appending more scales at fixed `q` does not weaken the quotient floor.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL PSD/EIGENVALUE MONOTONICITY + STRUCTURAL NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This finding does not rule out growing tail depth `q`, banks in which all `q`-column anchors degenerate, changing coefficient norms, infinite-dimensional limits with a different topology, or genuinely new signed information about the arithmetic source.

## 1. Column augmentation only adds positive semidefinite Gram mass

After reordering columns, write

`V_N = [W_N  Z_N]`,

where `W_N` is the chosen `q x q` anchor and `Z_N` contains all remaining scales. Then

`(D_beta V_N)(D_beta V_N)^*`
` = (D_beta W_N)(D_beta W_N)^*`
`   + (D_beta Z_N)(D_beta Z_N)^*`.

The second term is positive semidefinite. Hence, in Loewner order,

`(D_beta V_N)(D_beta V_N)^* >= (D_beta W_N)(D_beta W_N)^*`.

By the standard monotonicity of eigenvalues under addition of a positive semidefinite matrix,

`lambda_min((D_beta V_N)(D_beta V_N)^*)`
` >= lambda_min((D_beta W_N)(D_beta W_N)^*)`
` >= sigma^2`.

Because the anchor is nonsingular, the full `q x N` map has row rank `q`. Its `q` positive singular values are the square roots of the eigenvalues of the Gram matrix above, so

`s_q(D_beta V_N) >= sigma`.

No separation, compactness, or source-independence is required for the **added** columns. Those hypotheses are needed only to guarantee a uniformly conditioned anchor.

## 2. The quotient inequality survives arbitrary extra scales

For any full-row-rank matrix `A`, singular-value decomposition gives

`||A c||_2 >= s_min^+(A) dist(c,ker A)`,

where `s_min^+(A)` is its smallest positive singular value. Applying this to `A=D_beta V_N` and using `ker(D_beta V_N)=ker V_N` gives

`||D_beta V_N c||_2 >= sigma dist(c,ker V_N)`.

As `N` grows, the kernel dimension can grow from `N-q`. That is real exact freedom, but it is exactly the first-`q` moment-null space already identified in `VIS-343` and `VIS-354`. The new columns do not create a second conditioning channel after this null space is quotiented out.

Thus a coefficient vector with a small fixed-depth Wang tail has only two possibilities under the anchor hypothesis: it is close to the known moment kernel, or its coefficient norm is small in the chosen normalization. Increasing `N` alone does not change that dichotomy.

## 3. Source-adaptive bank growth does not change the pointwise bound

Let the arithmetic source choose any additional columns and coefficients,

`G -> (Z_N(G),c(G))`,

while the selected bank still contains an anchor satisfying the same lower bound `sigma`. The Gram identity is deterministic for each realized bank, so the same inequality holds pointwise:

`||D_beta V_N(G)c(G)||_2 >= sigma dist(c(G),ker V_N(G))`.

Therefore source-adaptive **bank enlargement** is no more powerful than the bounded adaptive selection closed by `VIS-355` unless it also destroys the anchor condition, increases the tail depth, changes the functional setting, or injects a genuinely new arithmetic estimate.

## 4. What growing scale count can actually buy

`VIS-343` shows that an `N`-dilate combination can cancel at most `N-1` successive inverse-frequency moments and that achieving larger polynomial tail order requires correspondingly more moment constraints. The present result separates that order-growth mechanism from mere dimensional growth.

At fixed `q`, extra scales only give more ways to enter the same first-`q` moment kernel. They do not reduce the quotient conditioning if one uniformly stable `q`-scale subbank remains. Consequently, a claimed asymptotic gain from `N=N(X)->infinity` must identify at least one additional resource:

- the effective cancellation depth `q=q(X)` also grows;
- every candidate `q`-scale anchor becomes ill-conditioned because the scale geometry degenerates or escapes;
- the coefficient norm/topology changes in a way that invalidates the finite Euclidean quotient estimate;
- or the source supplies a new signed/nonlinear estimate outside the passive moment map.

This rules out treating raw scale count as an independent asymptotic resource once the fixed-depth moment kernel has already been charged.

## Prior-art audit

The matrix step is classical. For matrices `A` and `B`, appending columns gives `[A B][A B]^*=AA^*+BB^*`, and `BB^*` is positive semidefinite. Monotonicity of Hermitian eigenvalues under positive-semidefinite addition is a standard consequence of the min-max/Weyl theory; see Roger A. Horn and Charles R. Johnson, **Matrix Analysis**, 2nd ed., Cambridge University Press, 2012, DOI `10.1017/CBO9781139020411`.

The Wang specialization is bounded by the existing prior-art audits in `VIS-343`--`VIS-355`: Richardson/Vandermonde moment cancellation is classical, and compact-family quotient conditioning is ordinary singular-value/pseudoinverse theory. No novelty is claimed for Gram matrices, Weyl monotonicity, singular values, Vandermonde systems, or column augmentation.

The Mathia-specific content is the frontier bookkeeping consequence: **the previously open “growing scale count” escape is not independent at fixed tail depth if a uniformly conditioned `q`-scale anchor survives**.

## Dependencies

- `VIS-343`: scale count bounds attainable moment-cancellation order.
- `VIS-354`: the Wang tail-coefficient map is the truncated inverse-scale Vandermonde moment map.
- `VIS-355`: bounded source-adaptive selection cannot evade a compact quotient floor.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue narrowed by this result.

## Research consequence

The accepted Wang clue can be narrowed once more. **Growing the number of scales while keeping the asymptotic depth fixed is not a separate conditioning resource when the bank retains one uniformly conditioned `q`-scale anchor.** Additional scales only enlarge the already-known moment kernel; on the quotient, the lower singular-value floor can only improve under column augmentation.

Future work should therefore not list raw scale count and tail depth as interchangeable escapes. A viable growing-bank mechanism must either use the extra scales to make the effective cancellation depth grow, quantify why every fixed-depth anchor degenerates, change the functional topology, or introduce genuinely new arithmetic information that survives the Wang destination audit.