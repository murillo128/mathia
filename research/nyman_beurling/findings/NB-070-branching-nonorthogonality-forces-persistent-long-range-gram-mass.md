# NB-070 — branching nonorthogonality forces persistent long-range Gram mass

**Status:** `EXACT-DERIVED + BRANCHING-MASS-TRANSFER + UNIFORM-SCHUR-TAIL-RIGIDITY + MATCHED-CONTROL-RESTRICTION + METHOD-ADVANCE`.

`NB-069` shows that the exact integer-dilation branching law of the canonical Nyman innovations rules out every uniformly bounded nonorthogonal source with a fixed finite Gram bandwidth. That still leaves an apparently broad escape route: replace the finite-band boundary chain by a long-range Gram matrix whose off-diagonal entries decay rapidly enough that distant interactions remain negligible.

The branching law sharply restricts that escape as well. For a Hilbert-space sequence `{E_j}_{j>=1}` satisfying, for one fixed integer `m>=2`,

\[
W E_j=\frac1{\sqrt m}\sum_{k=mj}^{m(j+1)-1}E_k
\tag{1}
\]

for an isometry `W`, let

\[
G_{ij}:=\langle E_i,E_j\rangle.
\tag{2}
\]

For `q=m^r`, define the dilation block

\[
I_j^{(q)}:=\{qj,qj+1,\ldots,q(j+1)-1\}.
\tag{3}
\]

Iteration of (1) gives the exact block identity already isolated in `NB-069`,

\[
G_{ij}
=\frac1q
\sum_{k\in I_i^{(q)}}
\sum_{\ell\in I_j^{(q)}}G_{k\ell}.
\tag{4}
\]

The first consequence is an absolute-mass transfer law requiring no decay or boundedness hypothesis:

\[
\boxed{
\sum_{k\in I_i^{(q)}}
\sum_{\ell\in I_j^{(q)}}|G_{k\ell}|
\ge q\,|G_{ij}|.
}
\tag{5}
\]

Thus every nonzero coarse correlation forces at least linear absolute Gram mass in every pair of its descendant blocks. Branching cannot dilute a nonzero correlation into a vanishing total interaction merely by spreading it over more indices.

To make the long-range content precise, set

\[
\omega(L)
:=
\sup_{k\ge1}
\sum_{\substack{\ell\ge1\\ |\ell-k|\ge L}}
|G_{k\ell}|,
\qquad L\ge0.
\tag{6}
\]

This is the uniform Schur row-tail of the Gram matrix. If `omega(0)<infinity`, then the sequence is uniformly bounded because `||E_k||^2=G_(kk)<=omega(0)`. The main rigidity statement is

\[
\boxed{
\omega(L)\longrightarrow0
\quad\Longrightarrow\quad
G_{ij}=0\ \text{for every }i\ne j.
}
\tag{7}
\]

Equivalently, under exact branching, **a uniformly Schur-localized Gram matrix is necessarily diagonal**. More quantitatively, every fixed off-diagonal entry satisfies

\[
\boxed{
|G_{ij}|
\le
\lim_{L\to\infty}\omega(L).
}
\tag{8}
\]

Consequently any bounded nonorthogonal exact-branching source has a macroscopic far tail:

\[
\boxed{
\lim_{L\to\infty}\omega(L)>0.
}
\tag{9}
\]

The long-range escape left by `NB-069` is therefore not merely "nonzero entries arbitrarily far from the diagonal." It must fail uniform absolute row localization. A nonzero coarse correlation has to be replenished at arbitrarily large index separations with an order-one amount of aggregate absolute Gram mass.

This still does **not** prove that the Nyman stable tail vanishes. The absolute mass in (5)--(9) may contain strong sign/phase cancellation, while the `NB-067` continuation certificate is a Schur complement and depends on the signed positive-semidefinite geometry. The result instead closes a natural intermediate loophole: a branch-compatible matched obstruction cannot preserve nonorthogonality while replacing the `NB-068` nearest-neighbor chain by a uniformly summable decaying Gram tail.

## 1. Branching transports absolute correlation mass to every scale

Iterating (1) gives

\[
W^rE_j
=q^{-1/2}\sum_{k\in I_j^{(q)}}E_k,
\qquad q=m^r.
\tag{10}
\]

Taking inner products and using that `W^r` is an isometry proves (4). Applying the triangle inequality to (4) immediately yields

\[
q|G_{ij}|
\le
\sum_{k\in I_i^{(q)}}
\sum_{\ell\in I_j^{(q)}}|G_{k\ell}|,
\tag{11}
\]

which is (5).

This point is stronger than the finite-band argument of `NB-069`. There the descendant blocks eventually separated enough that every term vanished. Here no entry is assumed to vanish. Equation (11) instead says that any mechanism retaining one coarse correlation must continually manufacture enough fine-scale absolute correlation to compensate the `1/q` normalization in the branching identity.

For nonadjacent coarse indices the forced mass is automatically far from the diagonal. Suppose `j>=i+2`. Every pair

\[
k\in I_i^{(q)},\qquad \ell\in I_j^{(q)}
\]

satisfies

\[
\ell-k
\ge
q(j-i-1)+1.
\tag{12}
\]

Therefore, with

\[
L_q:=q(j-i-1)+1,
\tag{13}
\]

we have

\[
\sum_{k\in I_i^{(q)}}
\sum_{\ell\in I_j^{(q)}}|G_{k\ell}|
\le
q\,\omega(L_q).
\tag{14}
\]

Combining (11) and (14),

\[
\boxed{|G_{ij}|\le\omega(L_q).}
\tag{15}
\]

Since `L_q->infinity`, every separated nonzero coarse correlation already forces a nonvanishing uniform far tail.

## 2. Adjacent correlations also force a far tail

The only subtle case is `j=i+1`, because the two descendant blocks share a boundary. Their closest fine indices remain adjacent for every dilation scale, so the argument from (12) cannot simply push the entire block to large distance.

Assume `omega(0)<infinity` and put

\[
M^2:=\sup_k\|E_k\|^2\le\omega(0).
\tag{16}
\]

Fix an integer `L>=1` and take `q>L`. Split the pairs

\[
(k,\ell)\in I_i^{(q)}\times I_{i+1}^{(q)}
\]

into those with `|ell-k|<L` and the remaining pairs. Across a common block boundary, the number of pairs at distance `d` is exactly `d` for `1<=d<=q`. Hence the near-boundary set contains at most

\[
C_L:=\sum_{d=1}^{L-1}d=\frac{L(L-1)}2
\tag{17}
\]

pairs. Cauchy--Schwarz gives

\[
|G_{k\ell}|\le\|E_k\|\,\|E_\ell\|\le M^2,
\tag{18}
\]

so the near contribution is at most `C_L M^2`.

For the far contribution, every fixed row `k in I_i^(q)` contributes at most `omega(L)`. There are exactly `q` such rows, so

\[
\sum_{\substack{k\in I_i^{(q)},\ \ell\in I_{i+1}^{(q)}\\|\ell-k|\ge L}}
|G_{k\ell}|
\le q\,\omega(L).
\tag{19}
\]

Equations (4), (17)--(19) therefore give

\[
|G_{i,i+1}|
\le
\frac{C_LM^2}{q}+\omega(L).
\tag{20}
\]

Letting `q=m^r->infinity` with `L` fixed yields

\[
\boxed{|G_{i,i+1}|\le\omega(L)\qquad(L\ge1).}
\tag{21}
\]

Then `L->infinity` proves the adjacent case of (8). Hermitian symmetry treats `i>j`.

Combining (15) and (21) proves (8) for every off-diagonal entry. In particular, if `omega(L)->0`, all off-diagonal entries vanish and (7) follows.

## 3. This is a uniform compressibility obstruction, not merely an infinite-band requirement

Fixed bandwidth is the special case in which `omega(L)=0` for all sufficiently large `L`, so `NB-069` is recovered immediately. But (7) rules out much more. For example, if a bounded exact-branching source satisfied any uniform summable envelope

\[
|G_{k\ell}|\le a_{|k-\ell|},
\qquad
\sum_{d\ge0}a_d<\infty,
\tag{22}
\]

then

\[
\omega(L)
\le
2\sum_{d\ge L}a_d
\longrightarrow0,
\tag{23}
\]

so its Gram matrix would have to be diagonal.

Thus polynomial or exponential off-diagonal decay with a summable, index-uniform envelope is incompatible with **nonorthogonal** exact branching. The same is true for any stronger notion that implies convergence to zero of the uniform absolute row tails. A branch-compatible stable-tail control can certainly be infinite-band, but if it is nonorthogonal and bounded it cannot be uniformly compressible in this Schur-row sense.

This is the relevant strengthening of the `NB-069` frontier. That finding left "long-range Gram interaction" as one escape. The present result separates two meanings of long range:

\[
\text{arbitrarily distant small entries}
\quad\text{versus}\quad
\text{persistent aggregate far mass}.
\tag{24}
\]

Only the second can support bounded nonorthogonality under exact branching.

## 4. Relation to the finite Schur certificates

`NB-067` asks for a finite horizon `N=N(R)` on an unbounded sequence such that

\[
S_{R,N(R)}\preceq C^2A_R,
\tag{25}
\]

where `S_(R,N)` is the Schur complement after eliminating future innovations and `A_R` is the visible finite-window Gram matrix. `NB-069` showed that a cheap nearest-neighbor boundary chain cannot be a matched obstruction once branching is imposed. Equations (5)--(9) now show that a bounded nonorthogonal replacement cannot hide in a uniformly summable weak tail either.

There is, however, no valid direct implication from (9) to either divergence or boundedness of the Schur certificates. The quantity `omega(L)` uses absolute values, whereas block branching in (4) and the Schur complement in (25) retain signs/phases and positive-semidefinite cancellation. Large absolute far mass may cancel almost completely in the normalized block sums. Conversely, poor Schur conditioning need not be visible from a single row-tail statistic.

Therefore this finding does **not** replace the finite-certificate target of `NB-067`. It narrows what a counterexample to that target must look like. Under bounded innovation norms, any branch-compatible nonorthogonal obstruction must combine its global continuation pathology with nonvanishing absolute Gram mass at arbitrarily large index separation. A proof of (25) may consequently need to exploit the signed block-renormalization identities rather than approximate the canonical Gram matrix uniformly by a banded or absolutely localized matrix.

## 5. Controls, prior art, and failure modes

The flat `O=1` Nyman control remains consistent. Its innovations occupy disjoint Paley--Wiener cells, so `G` is diagonal and `omega(L)=0` for every `L>=1`. Exact branching and perfect localization coexist precisely in the orthogonal case allowed by (7).

The theorem is conditional on uniform Schur localization. If `omega(0)=infinity`, or if `omega(L)` fails to tend to zero, the proof gives no contradiction; those are exactly the escape regimes it is designed to expose. The boundedness assumption is used only in the adjacent-block argument, where the `O(L^2)` entries near the moving block boundary must become negligible after division by `q`. A more general source could replace `omega(0)<infinity` by any local-growth condition making that normalized boundary strip vanish, but no such weakening is needed for the present classification.

The refinement-equation and wavelet literature has long related dilation/refinement identities, autocorrelation, and orthogonality; for example, Lawton--Lee--Shen characterize orthonormality of refinable-function shifts through an autocorrelation transition operator. No novelty is claimed for that general theme. A targeted search did not locate the specific abstract implication (7)--(9) for the consecutive-block isometric branching law (1), and no priority claim is made for the elementary estimate.

The closest recent Nyman Gram-decay work found in the audit is Hugh Carvill's 2025 preprint `arXiv:2510.18132`, which proves polynomial off-diagonal decay and block-compressibility after Mellin smoothing on a two-prime ladder. That does not contradict (7): the smoothed ladder family and its ladder-distance Gram matrix are not the canonical causal innovation sequence obeying (1). The result here instead marks a warning boundary: a summable uniform decay envelope cannot be transferred to the exact branching innovations while retaining nonorthogonality without checking which operation has changed the branching structure.

No external theorem is load-bearing for (5)--(23), so `SOURCES.md` requires no new anchor.

## 6. Consequence for the live frontier

After `NB-068`, a persistent stable tail could be imagined as a cheap nearest-neighbor boundary condition. `NB-069` forced any bounded matched replacement to become infinite-range. The present result makes that requirement quantitative:

\[
\boxed{
\text{bounded + exact branching + nonorthogonal}
\Longrightarrow
\lim_{L\to\infty}\omega(L)>0.
}
\tag{26}
\]

So the remaining negative mechanism must carry **order-one aggregate absolute correlation arbitrarily far from the Gram diagonal**, or else leave the bounded-source regime. Merely sprinkling rapidly decaying long-range entries is not enough.

This is still a structural restriction rather than an RH estimate. The next live problem remains the signed one: determine whether the exact block averages in (4), together with positive-semidefiniteness and the causal Schur geometry of `NB-067`, force enough cancellation/control to bound `Xi_(R,N)` on an unbounded sequence, or whether a branch-compatible nonlocal Gram mechanism can preserve the order-one far mass required by (26) while still sustaining a stable boundary mode.