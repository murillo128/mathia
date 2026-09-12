# NB-079 — q-adic refinement cancels a common prediction mode, leaving residual discovery versus screening

**Status:** `EXACT-DERIVED + Q-ADIC-RESIDUAL-CHANNEL + COMMON-MODE-CANCELLATION + CONDITIONAL-MUTUAL-INFORMATION + STABLE-TAIL-OBSTRUCTION + METHOD-ADVANCE`.

`NB-078` turns the stable-tail obstruction into a scale-by-scale competition on an exact `q`-adic refinement ray. If

\[
\ell=
\mathfrak L_{qR}-\mathfrak L_R
\]

is the new raw continuation information and

\[
c=
\mathfrak C_{qR,\,q(N+1)-1}-\mathfrak C_{R,N}
\]

is the new cross-cut prediction information, then both are nonnegative and the uncancelled charge changes by

\[
\mathfrak J_{qR,\,q(N+1)-1}-\mathfrak J_{R,N}
=\ell-c.
\]

The remaining weakness is that `ell` and `c` can both be large for the same benign reason: after refinement, the newly resolved past coordinates may already be predictable from the **coarse** future. Estimating that common contribution twice is unnecessary.

The present finding removes it exactly. For every refinement step there are three nonnegative information charges

\[
\boxed{\mathfrak G_{q;R,N}\ge0,\qquad
\mathfrak P_{q;R,N}\ge0,\qquad
\mathfrak S_{q;R,N}\ge0}
\]

such that

\[
\boxed{
\ell=\mathfrak G_{q;R,N}+\mathfrak P_{q;R,N},
\qquad
c=\mathfrak G_{q;R,N}+\mathfrak S_{q;R,N}.
}
\tag{1}
\]

Hence the common prediction mode cancels identically:

\[
\boxed{
\mathfrak J_{qR,\,q(N+1)-1}-\mathfrak J_{R,N}
=
\mathfrak P_{q;R,N}-\mathfrak S_{q;R,N}.
}
\tag{2}
\]

The two surviving charges have direct meanings. `mathfrak P` is the **residual discovery charge**: continuation information revealed by the newly resolved fine past after the coarse future has already been conditioned out. `mathfrak S` is the **future screening charge**: the amount of that fine-prefix continuation information removed when the future branch contrasts are admitted. The third charge `mathfrak G` measures predictability of the newly resolved fine past from the coarse future; it can be arbitrarily large, but it is irrelevant to stable-tail growth because it appears with exactly the same coefficient on both sides of the `NB-078` ledger.

Along any exact `q`-adic refinement ray this gives

\[
\boxed{
\mathfrak J_m
=
\mathfrak J_0+
\sum_{r=1}^{m}
\bigl(\mathfrak P_r-\mathfrak S_r\bigr).
}
\tag{3}
\]

A nonzero stable tail therefore forces

\[
\boxed{
\sum_{r=1}^{m}
(\mathfrak P_r-\mathfrak S_r)
\longrightarrow+\infty.
}
\tag{4}
\]

Conversely, it is enough on one unbounded refinement ray to prove

\[
\mathfrak P_r\le \mathfrak S_r+e_r,
\qquad
\sum_r e_r<\infty,
\tag{5}
\]

to rule out the stable tail. This is algebraically equivalent to the sufficient condition in `NB-078`, but it removes an entire nonnegative common mode before any arithmetic estimate is attempted. The live source problem is consequently smaller: compare **new continuation that remains after coarse-future conditioning** with **new screening supplied by the future contrasts**, rather than comparing two raw refinement budgets.

## 1. The uncancelled continuation charge is itself a conditional Gaussian information channel

Fix integers

\[
q\ge2,
\qquad
2\le R\le N,
\]

and abbreviate

\[
R^+=qR,
\qquad
N^+=q(N+1)-1.
\tag{6}
\]

At the fine cutoff `R^+`, split every prefix innovation as

\[
D_k=J_{R^+}D_k+(I-J_{R^+})D_k,
\qquad k<R^+.
\tag{7}
\]

Let `A_(R^+)` be the visible prefix Gram and let the tail pieces in (7), together with the future innovations `D_(R^+),...,D_(N^+)`, be represented by a centered real Gaussian vector after realification if necessary. Write

\[
X^+
\]

for the fine prefix-tail block. Independently introduce a Gaussian visible-noise block `V^+` with covariance `A_(R^+)` and put

\[
W^+=X^++V^+.
\tag{8}
\]

Then `W^+` has the full fine-prefix Gram covariance. Because every future innovation starts at or after `log R^+`, it is orthogonal to the visible part `V^+`; all cross-cut covariance is carried by `X^+`.

Now perform the canonical average/contrast transform from `NB-078` on every descendant block

\[
I_j^{(q)}=\{qj,\ldots,q(j+1)-1\}.
\]

On the future side write

\[
(Y_+,Z_+)
\]

for the transformed coordinates, where `Y_+` contains the block averages and `Z_+` the branch contrasts. On the past side the average coordinates of the descendant blocks give compressed variables

\[
X=T_qX^+,
\qquad
W=T_qW^+,
\tag{9}
\]

where `T_q` also discards the initial fine edge `1,...,q-1` and all past branch contrasts. Exact branching and cutoff intertwining identify `(X,W,Y_+)`, up to the isometry `U_(log q)`, with the Gaussian channel at the coarse pair `(R,N)`.

The additive-noise construction gives the Markov chains

\[
Y_+\;\longrightarrow\;X\;\longrightarrow\;W
\]

and

\[
(Y_+,Z_+)\;\longrightarrow\;X^+\;\longrightarrow\;W^+.
\tag{10}
\]

Therefore the identities `mathfrak J=mathfrak L-mathfrak C` from `NB-075/076` sharpen to

\[
\boxed{
\frac12\mathfrak J_{R,N}
=I(X;W\mid Y_+),
}
\tag{11}
\]

and

\[
\boxed{
\frac12\mathfrak J_{R^+,N^+}
=I(X^+;W^+\mid Y_+,Z_+).
}
\tag{12}
\]

Indeed, for a Markov chain `Y -> X -> W`,

\[
I(X;W)=I(Y;W)+I(X;W\mid Y),
\tag{13}
\]

while `2I(X;W)=mathfrak L` and `2I(Y;W)=mathfrak C`. Thus the renormalized Schur determinant is not only a difference of two information volumes: it is exactly the conditional information of the unresolved tail signal through the visible prefix channel after the admitted future has been conditioned out.

## 2. One common nonnegative charge appears in both raw refinement budgets

Define

\[
\boxed{
\mathfrak G_{q;R,N}
:=
2\bigl[
I(W^+;Y_+)-I(W;Y_+)
\bigr].
}
\tag{14}
\]

Because `W` is a deterministic linear compression of `W^+`, conditional on no extra variable, data processing gives

\[
\mathfrak G_{q;R,N}\ge0.
\tag{15}
\]

This charge measures how much better the **same coarse future averages** predict the prefix once the initial edge and past branch contrasts are restored. It is precisely the common mode that was not isolated in `NB-078`.

Next define the residual-discovery charge

\[
\boxed{
\mathfrak P_{q;R,N}
:=
2\bigl[
I(X^+;W^+\mid Y_+)
-
I(X;W\mid Y_+)
\bigr].
}
\tag{16}
\]

The pair `(X,W)` is obtained by deterministic linear compression of `(X^+,W^+)`, while the conditioning block `Y_+` is unchanged. Conditional data processing therefore gives

\[
\mathfrak P_{q;R,N}\ge0.
\tag{17}
\]

Use (13) at fine and coarse resolution, but condition both decompositions only on `Y_+`. Then

\[
\begin{aligned}
\frac12\bigl(
\mathfrak L_{R^+}-\mathfrak L_R
\bigr)
={}&
I(X^+;W^+)-I(X;W)\\
={}&
I(W^+;Y_+)-I(W;Y_+)\\
&+
I(X^+;W^+\mid Y_+)-I(X;W\mid Y_+).
\end{aligned}
\]

Hence

\[
\boxed{
\ell
=
\mathfrak G_{q;R,N}
+
\mathfrak P_{q;R,N}.
}
\tag{18}
\]

So the raw continuation gain splits into a part already exposed to the coarse future and a genuinely residual part that remains after that coarse future has been used.

## 3. The same common charge reappears in prediction growth, and future contrasts supply the screening term

Define

\[
\boxed{
\mathfrak S_{q;R,N}
:=
2I(W^+;Z_+\mid Y_+)
\ge0.
}
\tag{19}
\]

The fine cross-cut prediction charge is

\[
\frac12\mathfrak C_{R^+,N^+}
=I(W^+;Y_+,Z_+),
\tag{20}
\]

while the coarse charge is

\[
\frac12\mathfrak C_{R,N}
=I(W;Y_+).
\tag{21}
\]

The mutual-information chain rule therefore gives

\[
\begin{aligned}
\frac12 c
={}&
I(W^+;Y_+,Z_+)-I(W;Y_+)\\
={}&
I(W^+;Y_+)-I(W;Y_+)\\
&+I(W^+;Z_+\mid Y_+),
\end{aligned}
\]

so

\[
\boxed{
c
=
\mathfrak G_{q;R,N}
+
\mathfrak S_{q;R,N}.
}
\tag{22}
\]

Equations (18) and (22) prove (1)--(2). In particular,

\[
\boxed{
0\le\mathfrak G\le\min\{\ell,c\},
\qquad
\mathfrak P=\ell-\mathfrak G,
\qquad
\mathfrak S=c-\mathfrak G.
}
\tag{23}
\]

Thus potentially dominant refinement growth which is already visible as coarse-future predictability need never be estimated in the stable-tail comparison.

The term `mathfrak S` has a second exact interpretation which makes the word *screening* literal. From (10),

\[
I(W^+;Z_+\mid X^+,Y_+)=0.
\tag{24}
\]

The conditional interaction identity therefore yields

\[
\boxed{
\frac12\mathfrak S_{q;R,N}
=
I(X^+;W^+\mid Y_+)
-
I(X^+;W^+\mid Y_+,Z_+).
}
\tag{25}
\]

So admitting the future branch contrasts can only reduce the continuation information remaining in the fine prefix, and the reduction is **exactly** `mathfrak S/2`. Combining (16) and (25) gives a direct path from the coarse residual channel to the fine one:

\[
I(X;W\mid Y_+)
\xrightarrow{\text{refine past}}
I(X^+;W^+\mid Y_+)
\xrightarrow{\text{refine future}}
I(X^+;W^+\mid Y_+,Z_+),
\tag{26}
\]

where the first step increases by `mathfrak P/2` and the second decreases by `mathfrak S/2`.

## 4. The stable-tail criterion now compares only unresolved fine structure

Take the exact refinement ray from `NB-078`,

\[
R_m=q^mR_0,
\qquad
N_m=q^m(N_0+1)-1.
\tag{27}
\]

Apply (2) at every level and abbreviate the corresponding charges by `mathfrak P_m`, `mathfrak S_m`, and `mathfrak G_m`. Then

\[
\boxed{
\mathfrak J_{R_m,N_m}
=
\mathfrak J_{R_0,N_0}
+
\sum_{r=1}^{m}
(\mathfrak P_r-\mathfrak S_r).
}
\tag{28}
\]

`NB-074` says that a nonzero stable tail forces the left side to diverge for every finite horizon schedule. Hence (4) follows.

The contrapositive is the source-facing criterion (5). It is equivalent in truth value to the `ell_m-c_m` criterion of `NB-078`, but not equivalent in **proof burden**: the common charge `mathfrak G_m` has already disappeared algebraically. In particular, a source estimate may allow both `ell_m` and `c_m` to be large because the coarse future strongly predicts newly exposed fine coordinates. Such growth is harmless. Only the portion `mathfrak P_m` that remains after coarse-future conditioning can feed the stable-tail obstruction, and only the future-detail charge `mathfrak S_m` needs to match it.

The new past details consist exactly of the fixed initial edge `1,...,q-1` together with the past branch-contrast subspaces. Therefore `mathfrak P_m` can, if useful, be split further by the ordinary conditional-information chain rule into nonnegative edge and past-contrast discovery terms. Likewise `mathfrak S_m` depends only on the future branch-contrast subspace. These grouped quantities are invariant under a change of orthonormal basis inside any contrast space. No decorative Haar basis is required.

This identifies a sharper arithmetic target than the raw ledger:

\[
\boxed{
\text{control the continuation information of edge/past contrasts}
\text{ after coarse-future conditioning,}
}
\]

and compare it with the screening supplied by the future contrasts at the same refinement level. Mesoscopic additive localization remains optional rather than built into the criterion.

## 5. Stress tests and strict boundary

For the unit-outer control `O=1`, every innovation is supported on its own logarithmic cell. The prefix has no unseen tail signal, so `X=X^+=0`; the future is orthogonal to the prefix. Consequently

\[
\mathfrak G=\mathfrak P=\mathfrak S=0
\]

at every refinement step, and (2) is the identity `0=0`.

The exact-branching inner-factor controls of `NB-071/072` remain valid counterexamples to any source-free conclusion. If such a control has a nonzero stable tail, then (28) forces its residual discovery to outrun future screening by an unbounded cumulative amount. The present theorem therefore does not smuggle outerness, Nyman arithmetic, or RH-strength information into a generic information inequality. It only removes the common mode which cannot contribute to the net obstruction.

The net increment in (2) can have either sign. Neither `mathfrak P` nor `mathfrak S` is asserted to dominate at a single scale, and no summability is automatic. In particular, the fixed edge contribution to `mathfrak P` is not declared summable merely because it involves finitely many indices; such a claim would require additional tail regularity of the actual source. Likewise, `mathfrak S` need not be localized to bounded additive distance from the cut.

The Gaussian variables are again only exact representations of finite positive-definite Gram data. No stochastic model for the Nyman functions is assumed. Degenerate tail covariances can be handled by the standard positive-noise regularization implicit in the determinant formulas; the visible Gram is positive definite by the causal finite-window independence of `NB-062`.

## 6. Prior-art boundary and consequence for the line

The mutual-information chain rule, data processing, the Markov identity (13), and additive-Gaussian log-determinant formulas are classical. No novelty is claimed for those identities. A targeted audit of recent Nyman--Beurling Gram work again found Werner Ehm's explicit Gram/reciprocity program (`arXiv:2405.06349`) and Hugh Carvill's Mellin-smoothed multiscale/block-compressibility analysis (`arXiv:2510.18132`). The search did not locate the present specialization: using exact Báez--Duarte integer branching to identify the **same nonnegative coarse-future prediction gain** inside both the continuation-refinement and cross-cut-prediction increments, cancel it exactly, and leave a residual discovery-versus-screening ledger for the stable-tail Schur charge. No priority claim is made.

No specialized external estimate is load-bearing, so `SOURCES.md` remains unchanged.

The mathematical delta over `NB-078` is not another refinement monotonicity. It is an exact cancellation before estimation. The previous live target

\[
\ell_m\lesssim c_m
\]

can contain an arbitrarily large common component `mathfrak G_m`. The actual obstruction is now isolated as

\[
\boxed{
\mathfrak P_m-\mathfrak S_m,
}
\]

where `mathfrak P_m` is unresolved continuation created by the newly resolved past **after** the coarse future is known, and `mathfrak S_m` is exactly the amount screened by the new future contrasts. Any source-specific theorem proving summable positive excess for this smaller residual pair rules out the stable tail, without controlling the common prediction growth at all.