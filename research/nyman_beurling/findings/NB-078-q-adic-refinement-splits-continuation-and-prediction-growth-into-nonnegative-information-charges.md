# NB-078 — q-adic refinement splits continuation and prediction growth into nonnegative information charges

**Status:** `EXACT-DERIVED + Q-ADIC-REFINEMENT + CONDITIONAL-MUTUAL-INFORMATION + BRANCH-CONTRAST-LEDGER + STABLE-TAIL-OBSTRUCTION + METHOD-ADVANCE`.

`NB-077` proves that exact integer branching transports both the raw continuation volume

\[
\mathfrak L_R
=\log\frac{\det H_{<R}}{\det A_R}
\]

and every finite cross-cut prediction charge

\[
\mathfrak C_{a\mid R\mid b}
=\log\frac{\Delta_{a,R-1}\Delta_{R,b}}{\Delta_{a,b}}
\]

monotonically under dilation. Its remaining limitation is that the two monotonicities are separate: they do not explain **where the increase created by refinement lives**, and therefore do not compare the scale-by-scale growth of `mathfrak L` with the scale-by-scale growth of the cancellation charge.

The present finding resolves that refinement step exactly. Fix an integer `q>=2`. Inside every descendant block

\[
I_j^{(q)}=\{qj,\ldots,q(j+1)-1\}
\]

choose any orthogonal coefficient transform whose first coordinate is the normalized block average

\[
q^{-1/2}(1,\ldots,1).
\]

Exact branching identifies this average with

\[
\overline D_j^{(q)}
=q^{-1/2}\sum_{k\in I_j^{(q)}}D_k
=U_{\log q}D_j.
\]

The remaining `q-1` coordinates are the **branch contrasts**. Passing from all fine descendants to the coarse averages is therefore not an opaque compression: it discards a concrete contrast subspace on each side of the causal cut.

For a finite rectangle `a<R<=b`, let `Y_- ,Y_+` denote the Gaussian coordinate blocks associated with the coarse averages on the past and future sides, and let `Z_-,Z_+` denote all corresponding branch contrasts. Using the same real-Gaussian determinant representation as `NB-077`, the refinement gain has the exact chain rule

\[
\boxed{
\begin{aligned}
&\mathfrak C_{qa\mid qR\mid q(b+1)-1}
-\mathfrak C_{a\mid R\mid b}\\
&=2I(Y_-;Z_+\mid Y_+)
 +2I(Z_-;Y_+\mid Y_-)
 +2I(Z_-;Z_+\mid Y_-,Y_+).
\end{aligned}
}
\tag{1}
\]

Every term is nonnegative. Thus the inequality of `NB-077` is the shadow of a stronger statement: **all predictive dependence gained by integer refinement is carried by three explicit conditional-information channels involving the branch contrasts**. Signed fine-scale Gram cancellation cannot hide this gain, because the conditioning has already been performed before the three nonnegative terms are formed.

There is an exactly parallel decomposition for the raw continuation volume. Write

\[
H_{<R}=A_R+B_R,
\qquad B_R\succeq0,
\]

where `A_R` is the visible Gram and `B_R` is the Gram of the unseen tails. Introduce independent real Gaussian vectors `X_R,Z_R` with covariances `B_R,A_R` and output `W_R=X_R+Z_R`. Then

\[
\mathfrak L_R=2I(X_R;W_R).
\]

At scale `qR`, first remove the edge coordinates `1,...,q-1`, then apply the same block-average/contrast transform to the descendants `q,...,qR-1`. The branch averages of both the visible and unseen parts are exactly the shifted coarse variables because the Paley--Wiener cutoff intertwines branching. Hence

\[
\boxed{
\mathfrak L_{qR}-\mathfrak L_R
=\mathfrak E^{\rm cont}_{q,R}
 +\mathfrak K^{\rm cont}_{q,R},
}
\tag{2}
\]

where both terms are nonnegative sums of conditional mutual informations: `mathfrak E^(cont)` is the information lost when the initial edge coordinates are discarded, and `mathfrak K^(cont)` is the information lost when all branch contrasts are discarded. No determinant remainder of indeterminate sign is left.

For the standard prefix/future charge

\[
\mathfrak C_{R,N}
:=\sum_{1\le j<R\le n\le N}\kappa_{j,n},
\]

the fine prefix contains the same extra edge `1,...,q-1`. Thus its refinement is likewise exact:

\[
\boxed{
\mathfrak C_{qR,\,q(N+1)-1}-\mathfrak C_{R,N}
=\mathfrak E^{\rm pred}_{q,R,N}
 +\mathfrak K^{\rm pred}_{q,R,N},
}
\tag{3}
\]

with nonnegative edge and branch-contrast conditional-information charges. Equations (2)--(3) give a genuine multiscale ledger for the `NB-075/076` competition.

Along a `q`-adic descendant ray

\[
R_m=q^mR_0,
\qquad
N_m=q^m(N_0+1)-1,
\qquad N_0\ge R_0,
\]

put

\[
\ell_m:=\mathfrak L_{R_m}-\mathfrak L_{R_{m-1}}\ge0,
\qquad
c_m:=\mathfrak C_{R_m,N_m}-\mathfrak C_{R_{m-1},N_{m-1}}\ge0.
\]

Then the uncancelled continuation charge has the exact telescoping form

\[
\boxed{
\mathfrak J_{R_m,N_m}
=\mathfrak J_{R_0,N_0}
 +\sum_{r=1}^{m}(\ell_r-c_r).
}
\tag{4}
\]

A nonzero stable tail therefore forces

\[
\boxed{
\sum_{r=1}^{m}(\ell_r-c_r)\longrightarrow+\infty
}
\tag{5}
\]

on **every** such integer-refinement ray. Conversely, if on one unbounded ray

\[
\ell_m\le c_m+e_m,
\qquad
\sum_{m\ge1}e_m<\infty,
\tag{6}
\]

then `mathfrak J_(R_m,N_m)` is bounded and `NB-074` forces

\[
\boxed{\mathcal T_\infty=\{0\}.}
\tag{7}
\]

The live source problem can therefore be attacked scale by scale: one does not need to compare two large determinants at the final scale. It is enough to show that the **new** continuation information created by each integer refinement is matched, up to summable total loss, by the **new** cross-cut prediction information created by the same refinement.

## 1. Cross-cut refinement is exactly branch-contrast conditional information

Fix `a<R<=b` and consider the fine descendant family

\[
D_{qa},D_{qa+1},\ldots,D_{q(b+1)-1}.
\]

Its Gram matrix is positive definite by the finite independence of the causal innovations. As in `NB-077`, represent this Gram matrix as the covariance of a centered real Gaussian vector after realification if necessary. Split the coordinates at `qR` into fine past and future blocks.

Inside every `q`-coordinate descendant block apply an orthogonal transform `W_q` whose first row is

\[
q^{-1/2}(1,\ldots,1).
\]

The first transformed coordinate of block `j` is the coefficient-space average corresponding to `overline D_j^(q)`. Because

\[
\overline D_j^{(q)}=U_{\log q}D_j
\]

and `U_(log q)` is an isometry, the covariance matrix of all first coordinates is exactly the coarse Gram matrix of `D_a,...,D_b`.

Write the transformed past coordinates as `(Y_-,Z_-)`, where `Y_-` collects the averages and `Z_-` all contrasts, and similarly `(Y_+,Z_+)` on the future side. Mutual information is invariant under invertible transformations performed separately on the two sides, so

\[
\frac12\mathfrak C_{qa\mid qR\mid q(b+1)-1}
=I(Y_-,Z_-;Y_+,Z_+),
\tag{8}
\]

while

\[
\frac12\mathfrak C_{a\mid R\mid b}
=I(Y_-;Y_+).
\tag{9}
\]

The ordinary chain rule gives

\[
\begin{aligned}
I(Y_-,Z_-;Y_+,Z_+)
={}&I(Y_-;Y_+)\\
&+I(Y_-;Z_+\mid Y_+)\\
&+I(Z_-;Y_+\mid Y_-)\\
&+I(Z_-;Z_+\mid Y_-,Y_+),
\end{aligned}
\tag{10}
\]

which proves (1).

The individual contrast coordinates depend on the orthonormal basis chosen inside the codimension-one zero-sum coefficient space, but the grouped conditional mutual informations in (10) do not: an invertible change of basis inside `Z_-` or `Z_+` leaves them unchanged. The refinement ledger therefore depends only on the canonical average direction and its canonical contrast subspace, not on a decorative contrast basis.

For the prefix charge, apply (10) to the descendant coordinates `q,...,q(N+1)-1`. The complete fine past also contains

\[
E_q:=\{1,\ldots,q-1\}.
\]

Adding this past edge contributes exactly

\[
2I(E_q;F_{\rm desc}\mid P_{\rm desc})\ge0,
\tag{11}
\]

where `P_desc` and `F_desc` are the descendant past and future coordinate blocks. Combining (10)--(11) gives (3), with `mathfrak E^(pred)` equal to (11) and `mathfrak K^(pred)` equal to the three contrast terms.

## 2. Raw continuation refinement has the same multiresolution decomposition

For the fine prefix at cutoff `qR`, write

\[
H_{<qR}=A_{qR}+B_{qR}.
\]

Choose independent real Gaussian vectors

\[
X\sim N(0,B_{qR}),
\qquad
Z\sim N(0,A_{qR}),
\qquad
W=X+Z.
\]

The standard additive-Gaussian determinant formula gives

\[
2I(X;W)
=\log\frac{\det(A_{qR}+B_{qR})}{\det A_{qR}}
=\mathfrak L_{qR}.
\tag{12}
\]

Restrict both `X` and `W` to the descendant coordinate set `q,...,qR-1`, then apply the same block transform `W_q` to both. The coarse average of a descendant innovation is `U_(log q)D_j`, and the cutoff intertwines exactly:

\[
J_{qR}U_{\log q}D_j
=U_{\log q}J_RD_j.
\tag{13}
\]

Therefore the averaged visible covariance is `A_R`, while the averaged unseen covariance is

\[
H_{<R}-A_R=B_R.
\]

The mutual information of the retained average input/output pair is consequently exactly `mathfrak L_R/2`.

Now use the same mutual-information chain rule twice. The first compression discards the initial edge coordinates and contributes a sum of three nonnegative conditional mutual informations involving their input/output variables. The second compression discards the descendant contrast subspaces and contributes another sum of three nonnegative conditional mutual informations. Their doubled total is precisely

\[
\mathfrak L_{qR}-\mathfrak L_R.
\tag{14}
\]

This proves (2). In particular, the monotonicity `mathfrak L_R<=mathfrak L_(qR)` from `NB-077` contains no hidden signed determinant effect: its entire refinement gain can be resolved into ordinary nonnegative information channels just as the cross-cut charge can.

## 3. The stable-tail obstruction becomes a scale-by-scale imbalance

Set

\[
\mathfrak J_{R,N}=\mathfrak L_R-\mathfrak C_{R,N}
\]

as in `NB-075/076`. The descendant choice

\[
R_m=q^mR_0,
\qquad
N_m=q^m(N_0+1)-1
\]

ensures that each level is exactly the full `q`-fold refinement of the previous prefix/future rectangle. Subtracting consecutive values gives

\[
\mathfrak J_{R_m,N_m}-\mathfrak J_{R_{m-1},N_{m-1}}
=\ell_m-c_m,
\tag{15}
\]

and summing proves (4).

`NB-074` states that if `0!=mathcal T_infinity`, then `mathfrak J_(R,N(R))->infinity` for every finite future schedule. The present `N_m` is such a schedule along the unbounded sequence `R_m`, so (5) follows.

Equation (5) is stronger as an interpretation than saying separately that `mathfrak L` and `mathfrak C` are increasing. A stable-tail mechanism must repeatedly create enough **new continuation-channel information not matched by new branch-refinement prediction information** that the cumulative excess diverges. It cannot survive merely because both budgets are large, because cross-cut information sits at long additive distance, or because signs cancel in raw Gram entries.

The contrapositive (6)--(7) gives a source-facing sufficient criterion with a summable error budget. It allows finitely many bad refinement levels and arbitrarily large individual values of `mathfrak L_R`; only the cumulative unmatched refinement matters.

## 4. Stress tests and strict boundary

The unit-outer control has mutually orthogonal cell innovations. There are no unseen continuation tails, no cross-cut partial correlations, and therefore

\[
\mathfrak L_R=\mathfrak C_{R,N}=0
\]

at every scale. All edge and contrast charges in (1)--(3) vanish, and (4) is identically zero.

The exact-branching inner-factor controls of `NB-071/072` provide the opposite calibration. They can have good global Gram conditioning and a nonzero stable tail. The present theorem does not remove them; instead `NB-074` and (5) force their `q`-adic continuation-refinement ledger to develop an unbounded cumulative excess over the corresponding prediction-refinement ledger. Thus the result is compatible with the known counterexample class and identifies what that class must pay at the multiscale information level.

The result also does **not** prove finite-additive-band localization. A contrast subspace belongs to one descendant block in coefficient space, but its correlations across the causal cut may still involve descendant rectangles whose additive widths grow with scale. Equation (1) explains the information introduced by refinement; it does not show that this information lies within `O(1)` or even `o(R)` distance from the cut. The localization problem stated after `NB-077` remains open.

Nor is a Gaussian stochastic model being asserted for the Nyman functions. Gaussian vectors are only an exact representation of positive-definite determinant ratios. Every quantity in (1)--(4) is determined by finite Gram matrices of the actual deterministic innovations.

## 5. Prior-art boundary and consequence for the line

The chain rule and nonnegativity of conditional mutual information, the Gaussian log-determinant formula, and invariance under invertible coordinate transforms are classical information theory. No novelty is claimed for them. `NB-077` already uses the corresponding data-processing inequality to prove coarse-to-fine monotonicity.

A targeted audit of Nyman--Beurling Gram work found the recent explicit Gram and reciprocity program of Werner Ehm and the Mellin-smoothed multiscale/block-compressibility analysis of Hugh Carvill, as well as contemporary finite Gram-spectral studies already anchored in `SOURCES.md`. The search did not locate the present specialization: resolving exact Báez--Duarte integer branching into average/contrast coordinates and using the mutual-information chain rule to obtain a nonnegative **refinement ledger for both** the raw continuation channel and the cross-cut conditional-prediction channel. No priority claim is made. No specialized external estimate is load-bearing, so `SOURCES.md` remains unchanged.

The mathematical delta over `NB-077` is the replacement of two unrelated monotonicities by a common multiresolution currency. The next arithmetic target can now be stated locally in scale:

\[
\boxed{
\text{control }\ell_m-c_m
\text{ along one integer-refinement ray, with summable positive excess.}
}
\tag{16}
\]

Such a theorem would rule out the stable tail without requiring bounded raw continuation volume, bounded global condition number, or direct finite-band localization. If instead the actual Nyman source exhibits a persistent positive refinement excess, (1)--(3) identify whether it enters through the initial edge or through the branch-contrast channels, giving a sharper location for the remaining arithmetic obstruction.