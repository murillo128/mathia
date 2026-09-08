# VIS-095 — step-two signatures of fixed delay paths collapse to local block sums plus boundary

## Claim

Let

`a=(a_1,...,a_N)`

be a finite real sequence and fix `1<=m<N`. Write

`w_i=(a_i,...,a_(i+m-1)) in R^m`, `1<=i<=M=N-m+1`,

and let `X_a` be the ordinary piecewise-linear path that visits

`w_1,w_2,...,w_M`

in chronological order, with **no appended time/index coordinate**. Let `S^(1)` and `S^(2)` denote the first two tensor levels of its iterated-integral signature.

Then the complete step-two signature `(1,S^(1),S^(2))` is determined by only:

1. the first and last delay windows `w_1,w_M`; and
2. the **unordered multiset of length-`(m+1)` blocks**

`u_i=(a_i,...,a_(i+m))`, `1<=i<=N-m`.

More explicitly,

`S^(1)=w_M-w_1`.

The shuffle identity gives

`Sym S^(2) = (1/2) S^(1) tensor S^(1)`,

so the symmetric second level contains no information beyond the endpoint displacement.

For coordinates `1<=r<s<=m`, define the antisymmetric second-level component

`A_(r,s)=(1/2)(S^(2)_(r,s)-S^(2)_(s,r))`.

For the polygonal delay path,

`A_(r,s)`
` = (1/2) [ sum_(i=1)^(N-m) (a_(i+r-1) a_(i+s) - a_(i+s-1) a_(i+r))`
`             + a_(N-m+r) a_s - a_(N-m+s) a_r ]`.

Equivalently, if `u_i=(u_(i,1),...,u_(i,m+1))`, then

`A_(r,s)`
` = (1/2) [ sum_i (u_(i,r) u_(i,s+1) - u_(i,s) u_(i,r+1))`
`             + (w_M^r w_1^s - w_M^s w_1^r) ]`.

The interior term is therefore an additive function of the unordered `(m+1)`-block multiset, and the only remaining datum is an endpoint correction. Thus any deterministic statistic, visualization, classifier, or filtration that factors only through the **unaugmented step-two signature** of a fixed-`m` delay path cannot distinguish two sequences having the same `(m+1)`-block multiset and the same first/last `m`-windows.

The collision from `VIS-094` already witnesses strict loss. For `m=2`,

`a=(1,1,2,1,1,1,1)`,

`b=(1,1,1,2,1,1,1)`

have the same length-three block multiset and the same initial/final two-windows `(1,1)`, hence identical signatures through level two, while their length-four block multisets differ. Their common signed area component is `A_(1,2)=-1/2`.

Applied to a zeta-zero gap sequence, the first path-signature escape left open by `VIS-094` therefore does **not** yet provide genuinely nonlocal order at signature level two. Its new antisymmetric information is a sum of local `(m+1)`-block edge areas plus a boundary term.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-SIGNATURE/LEVY-AREA SPECIALIZATION + NEGATIVE INFORMATION-LOSS CONTROL + NO-NOVELTY-CLAIM`.

No claim is made about signature levels three and above, time-augmented or lead-lag signatures, growing signature depth, or the full signature. Those constructions can retain genuinely richer ordered-path information and require separate audits.

## 1. The first level is only endpoint displacement

For a bounded-variation path, the first signature level is the ordinary increment. Hence for the polygonal path through the delay windows,

`S^(1)=integral dX = w_M-w_1`.

This already removes any possibility that level one records the interior visitation order. It depends only on the first and last `m`-windows.

At level two, the standard shuffle relation gives, coordinatewise,

`S^(2)_(r,s)+S^(2)_(s,r)=S^(1)_r S^(1)_s`.

The diagonal components satisfy

`S^(2)_(r,r)=(1/2)(S^(1)_r)^2`.

Therefore all genuinely new second-level information is contained in the antisymmetric coordinates `A_(r,s)`.

## 2. The antisymmetric level is the chord-closed polygonal area

For a piecewise-linear path with vertices `w_1,...,w_M`, the antisymmetric second signature in coordinates `(r,s)` is the signed Levy area of the projected polygonal path closed by the chord from `w_M` back to `w_1`:

`A_(r,s)`
` = (1/2) [ sum_(i=1)^(M-1) (w_i^r w_(i+1)^s - w_i^s w_(i+1)^r)`
`             + w_M^r w_1^s - w_M^s w_1^r ]`.

This identity may also be checked directly from polygonal increments `v_i=w_(i+1)-w_i`:

`A_(r,s)=(1/2) sum_(i<j) (v_i^r v_j^s-v_i^s v_j^r)`.

The two formulas are the standard equivalence between the antisymmetric second iterated integral and signed area.

For the delay path,

`w_i^r=a_(i+r-1)`, `w_(i+1)^s=a_(i+s)`.

Thus every edge contribution is

`a_(i+r-1) a_(i+s) - a_(i+s-1) a_(i+r)`.

That quantity is a function of the single length-`(m+1)` block

`u_i=(a_i,...,a_(i+m))`,

namely

`f_(r,s)(u_i)=u_(i,r)u_(i,s+1)-u_(i,s)u_(i,r+1)`.

Summing over the path edges therefore forgets their chronology: it retains only the sum of `f_(r,s)` over the unordered block multiset. The chord correction depends only on `w_1,w_M`.

This proves the claimed information bound for every antisymmetric coordinate and hence for the complete step-two signature.

## 3. The `VIS-094` collision also defeats step-two signatures

For

`a=(1,1,2,1,1,1,1)`,

`b=(1,1,1,2,1,1,1)`,

`VIS-094` proves equality of the length-three block multisets at `m=2`:

- `(1,1,1)` occurs twice;
- `(1,1,2)` occurs once;
- `(1,2,1)` occurs once;
- `(2,1,1)` occurs once.

Both delay paths start and end at `(1,1)`. The first signature level is therefore zero for each, the symmetric second level is zero, and the area formula gives the same antisymmetric coordinate `-1/2`.

Yet the four-block multisets differ. Thus the step-two signature has not recovered the next ordering layer that the static transition graph of `VIS-094` also misses.

This is stronger than reversal invariance: the two sequences are not simply reversals of one another. They genuinely differ in how the same local transition inventory is assembled.

## 4. Prior art and novelty assessment

Path signatures are classical iterated-integral invariants. Ben Hambly and Terry Lyons, **Uniqueness for the signature of a path of bounded variation and the reduced path group**, *Annals of Mathematics* 171:1 (2010), 109–167, DOI `10.4007/annals.2010.171.109`, gives the standard finite-variation signature framework and the tree-like equivalence boundary for full-signature uniqueness.

The fact that the antisymmetric second level is signed area is also standard signature theory. Joscha Diehl, Terry Lyons, Rosa Preiß, and Jeremy Reizenstein, **Areas of areas generate the shuffle algebra**, arXiv `2002.02338`, explicitly uses the classical fact that the information added by signature level two relative to level one is equivalent to the area between path components.

No novelty is claimed for the signature, shuffle, or Levy-area identities. The Mathia-specific contribution is the elementary specialization to a **sliding-window delay path**, where every projected edge-area contribution becomes a function of one `(m+1)`-block. That specialization closes the first path-aware escape explicitly left open by `VIS-094` at the weakest nontrivial signature depth.

## Boundary and falsification

The theorem concerns the ordinary unaugmented polygonal signature **truncated after level two** at fixed delay dimension `m`.

It does not classify:

- signature levels `k>=3` or higher log-signature brackets;
- the full signature, which can retain path information far beyond level two up to the standard tree-like equivalence;
- a time/index coordinate appended to the delay path;
- lead-lag transforms or other lifts that deliberately add coordinates before taking signatures;
- occurrence-labelled vertices or another carrier that directly retains chronology;
- signature depth, delay dimension, or memory order growing materially with observation scale;
- independent analytic marks such as `Z(g_n)`, derivatives, zero multiplicity, or another field coordinate.

Those are legitimate next candidates. Their additional information must still be audited rather than credited automatically to a visually richer path representation.

The result also does not say that the level-two signature contains only one-gap information. At fixed `m` it can aggregate genuine `(m+1)`-block geometry. The obstruction is specifically to interpreting that aggregation as **nonlocal ordering beyond the local block inventory plus endpoints**.

Falsify the claim by producing two fixed-`m` delay paths with the same first/last `m`-windows and the same unordered `(m+1)`-block multiset but different signatures through level two, or by finding an antisymmetric second-level coordinate that cannot be written as the displayed local block sum plus endpoint correction.

## Visual consequence

No canonical PNG is retained. This is an exact pre-render information audit. Plotting the step-two area tensor or a low-dimensional embedding of it could produce a visually discriminating statistic across datasets, but for a fixed delay dimension its mathematical carrier is already bounded by the local `(m+1)`-block inventory and boundary windows.

## Research consequence

`CLUE-zeta-critical-strip-multiscale-geometry` should narrow the path-signature escape: **unaugmented signature depth two is not yet a genuinely nonlocal channel for a fixed-window scalar delay path**. A live path-aware route now has to use genuinely higher iterated order, an independent time/analytic mark, a growing-memory regime, or another construction whose value cannot be reduced to fixed local block counts plus endpoints.