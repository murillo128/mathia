# NB-066 — persistent tail is a fixed locally natural mode with divergent causal extension cost

**Status:** `EXACT-DERIVED + FIXED-STABLE-MODE + LOCAL-NATURAL-TRACE-CHARACTERIZATION + DIVERGENT-EXTENSION-COST + UNFILTERED-MEMORY-BUDGET + FLAT-CONTROL + METHOD-ADVANCE`.

`NB-064` and `NB-065` show that, if the collective late-quotient defect persists, the normalized visible target must keep moving into weaker and weaker singular sectors of the one-cell forward-memory maps

\[
\Gamma_R:\mathcal G_R\to\mathcal X_R^\circ.
\tag{1}
\]

That description still makes the obstruction look like a sequence of scale-dependent directions. The present finding shows that the geometry is substantially more rigid. The moving visible target converges in the ambient Hilbert space to one **fixed nonzero stable-tail mode**, and every finite truncation of that mode is exactly a natural finite-window trace.

Retain

\[
\mathcal D=\mathcal A^\perp,
\qquad
\mathcal K_R=\mathcal E_R\ominus\mathcal G_R,
\qquad
\mathcal T_R=\mathcal K_R^\perp\cap\mathcal D,
\tag{2}
\]

and put

\[
\mathcal T_\infty:=\bigcap_{R\ge2}\mathcal T_R
=\mathcal D\ominus\mathcal K_{\rm fin}.
\tag{3}
\]

Then

\[
\boxed{
\mathcal T_\infty
=
\{t\in\mathcal D:J_Rt\in\mathcal G_R\text{ for every }R\ge2\}.
}
\tag{4}
\]

Thus a stable-tail vector is globally orthogonal to the natural Nyman space while looking **exactly natural on every finite Paley--Wiener window**.

For the canonical residual `h_*=Qe`, define

\[
t_*:=P_{\mathcal T_\infty}h_*.
\tag{5}
\]

The decreasing-subspace projection theorem and the `NB-061` decomposition give

\[
\boxed{
P_{\mathcal T_R}h_*
=(I-J_R)h_*+p_R
\longrightarrow t_*,
\qquad
p_R:=P_{\mathcal G_R}J_Rh_*\longrightarrow t_*.
}
\tag{6}
\]

Hence

\[
\boxed{
\delta_\infty=\|t_*\|.
}
\tag{7}
\]

If the collective defect persists, `delta_infinity>0`, the normalized directions from `NB-064/065` do not wander arbitrarily:

\[
\boxed{
\frac{p_R}{\|p_R\|}
\longrightarrow
\frac{t_*}{\|t_*\|}
\quad\text{strongly in }H^2.
}
\tag{8}
\]

There is a second, quantitatively sharper consequence. For `t in T_infinity`, define the least future energy required to extend its finite trace by a genuine natural vector,

\[
\mathfrak E_R(t)
:=
\inf\left\{
\|(I-J_R)a\|:
 a\in\mathcal A,
\ J_Ra=J_Rt
\right\}.
\tag{9}
\]

The set is nonempty by (4) and `G_R=J_R A`. If `0!=t in T_infinity`, then every admissible extension satisfies the exact orthogonality constraint

\[
\langle (I-J_R)t,(I-J_R)a\rangle
=-\|J_Rt\|^2,
\tag{10}
\]

so

\[
\boxed{
\mathfrak E_R(t)\,\|(I-J_R)t\|
\ge
\|J_Rt\|^2.
}
\tag{11}
\]

Since `J_Rt -> t` and `(I-J_R)t -> 0`, every nonzero stable-tail mode forces

\[
\boxed{
\mathfrak E_R(t)\longrightarrow\infty.
}
\tag{12}
\]

Thus persistence is not merely bad one-cell conditioning. It requires a vector whose finite traces are all perfectly natural but whose **global natural continuation cost blows up without bound**.

This can be made source-only. Let

\[
\Lambda_R
:=
\sup_{0\ne g\in\mathcal G_R}
\frac{1}{\|g\|}
\inf\left\{
\|(I-J_R)a\|:
 a\in\mathcal A,
\ J_Ra=g
\right\}.
\tag{13}
\]

Each `Lambda_R` is finite because every `g in G_R` already has an extension in the finite causal span from `NB-062`. If `T_infinity` contains any nonzero vector, then (11) gives

\[
\boxed{
\Lambda_R
\ge
\frac{\|J_Rt\|}{\|(I-J_R)t\|}
\longrightarrow\infty.
}
\tag{14}
\]

Consequently, a bounded causal-extension constant on any unbounded sequence of windows would force

\[
\boxed{\mathcal T_\infty=\{0\}.}
\tag{15}
\]

That criterion is stronger than a target-specific statement: it would eliminate the stable tail for every defect vector at once.

Finally, the fixed mode has a stronger one-cell transmission law than the filtered budget in `NB-065`. Put

\[
g_R:=J_Rt,
\qquad
x_R^{(t)}:=(J_{R+1}-J_R)t.
\tag{16}
\]

Since both `g_R in G_R` and `J_(R+1)t in G_(R+1)`, the graph decomposition of `NB-063` forces

\[
\boxed{
x_R^{(t)}=\Gamma_Rg_R+\beta_RC_R}
\tag{17}
\]

for a scalar `beta_R`, with the two terms orthogonal. Therefore

\[
\boxed{
\sum_{R\ge2}
\left(
\|\Gamma_RJ_Rt\|^2
+|\beta_R|^2\|C_R\|^2
\right)
=
\|(I-J_2)t\|^2.
}
\tag{18}
\]

For nonzero `t`, normalizing `w_R=J_Rt/||J_Rt||` for large `R` gives

\[
\boxed{
\sum_R\|\Gamma_Rw_R\|^2<\infty,
\qquad
\|\Gamma_Rw_R\|\to0.
}
\tag{19}
\]

So a persistent mode is itself an **unfiltered square-summable approximate-kernel trajectory**. The pathology needed for persistence is pushed beyond the immediate next cell: although each one-cell continuation becomes weak in square-sum, every exact global natural extension of the same finite trace must develop an exploding far-future tail by (11)--(12).

## 1. Stable-tail vectors are exactly the locally natural traces

`NB-058` and `NB-060` identify

\[
\mathcal T_R=\mathcal D\ominus\mathcal K_R,
\qquad
\mathcal T_\infty
=\mathcal D\ominus\overline{\bigcup_R\mathcal K_R}.
\tag{20}
\]

For `t in D`, the truncation `J_Rt` lies in `E_R`. By `NB-061`,

\[
\mathcal E_R=\mathcal K_R\oplus\mathcal G_R.
\tag{21}
\]

If `t in T_infinity`, then `t` is orthogonal to `K_R` for every `R`. Since every vector of `K_R` is supported before `log R`, this is equivalent to

\[
J_Rt\perp\mathcal K_R.
\tag{22}
\]

Equation (21) then gives `J_Rt in G_R`. Conversely, if every `J_Rt` belongs to `G_R`, then `t` is orthogonal to every `K_R`, hence to their closed union, so `t in T_infinity`. This proves (4).

The characterization is an inverse-limit statement, not a closure statement. A vector in `T_infinity` agrees on every finite window with some natural vector, but it need not be the norm limit of those natural vectors. Equation (12) shows exactly why a nonzero one cannot be.

## 2. The canonical moving projection converges to one fixed mode

For arbitrary `h in D`, projection onto `K_R` can be performed entirely inside the early window. From (21),

\[
P_{\mathcal K_R}h
=J_Rh-P_{\mathcal G_R}J_Rh.
\tag{23}
\]

Hence

\[
\boxed{
P_{\mathcal T_R}h
=h-P_{\mathcal K_R}h
=(I-J_R)h+P_{\mathcal G_R}J_Rh.
}
\tag{24}
\]

The spaces `T_R` are decreasing closed subspaces with intersection `T_infinity`. Orthogonal projections onto a decreasing family converge strongly to the projection onto the intersection, so

\[
P_{\mathcal T_R}h_*	o P_{\mathcal T_\infty}h_*=t_*.
\tag{25}
\]

Since `||(I-J_R)h_*||->0`, equation (24) gives (6). Taking norms and using `delta_R=||P_(T_R)h_*||` proves (7). If `delta_infinity>0`, normalization is continuous near the nonzero limit and yields (8).

This strengthens the interpretation of `NB-064`. The approximate-kernel directions produced there may be selected spectrally at each scale, but the canonical visible target itself has a fixed ambient limit. Persistence therefore cannot be explained by indefinite rotation through unrelated bad singular directions.

## 3. Global orthogonality forces every exact extension to blow up

Fix `0!=t in T_infinity`. By (4), `J_Rt in G_R=J_RA`, so admissible extensions in (9) exist. Let `a in A` satisfy

\[
J_Ra=J_Rt.
\tag{26}
\]

Because `t in D=A^perp`,

\[
0=\langle t,a\rangle.
\tag{27}
\]

Splitting at the orthogonal Paley--Wiener cutoff gives

\[
0
=
\langle J_Rt,J_Ra\rangle
+
\langle(I-J_R)t,(I-J_R)a\rangle
=
\|J_Rt\|^2
+
\langle(I-J_R)t,(I-J_R)a\rangle,
\tag{28}
\]

which is (10). Cauchy--Schwarz yields

\[
\|J_Rt\|^2
\le
\|(I-J_R)t\|\,\|(I-J_R)a\|.
\tag{29}
\]

Taking the infimum over admissible `a` proves (11).

The denominator in (11) cannot vanish for a nonzero stable mode. If `(I-J_R)t=0`, then `t in E_R intersect D`; because `J_Rt in G_R` and `K_R=E_R ominous G_R`, one would have simultaneously `t in G_R` and `t in D`, hence `t=0` after using `G_R=J_RA` together with (28). More directly, (28) would give `||t||^2=0`. Thus (11) is meaningful at every finite `R`.

As `R->infinity`,

\[
\|J_Rt\|\to\|t\|>0,
\qquad
\|(I-J_R)t\|\to0,
\tag{30}
\]

and (12) follows. Dividing (11) by `||J_Rt||` and taking the supremum over all local traces gives (14).

The contrapositive is the useful source criterion. If `Lambda_R` is bounded on an unbounded sequence `R_k`, then no nonzero `t in T_infinity` can satisfy (14), so `T_infinity={0}`. No target pairing is needed for this conclusion.

## 4. The causal basis makes the locally natural mode explicit

`NB-062` gives

\[
\mathcal G_R
=\operatorname{span}\{J_RD_j:1\le j<R\}
\tag{31}
\]

with those vectors linearly independent. Thus for `t in T_infinity` there is a unique finite causal interpolant

\[
s_R\in\operatorname{span}\{D_1,\ldots,D_{R-1}\}
\subseteq\mathcal A
\tag{32}
\]

such that

\[
J_Rs_R=J_Rt.
\tag{33}
\]

Compatibility of the truncations forces

\[
\boxed{
s_{R+1}-s_R=a_RD_R}
\tag{34}
\]

for a scalar `a_R`: the difference lies in `span{D_1,...,D_R}` and vanishes under `J_R`, whose kernel on that finite span is exactly `span{D_R}` by the causal independence proved in `NB-062`.

Consequently a stable-tail mode has a unique locally finite formal natural expansion

\[
t\sim\sum_{j\ge1}a_jD_j,
\tag{35}
\]

in the precise sense that every finite Paley--Wiener truncation is eventually reproduced exactly by the partial sums. But the series cannot converge to a nonzero `t` in the ambient `H^2` norm, because every partial sum belongs to `A` whereas `t in A^perp`. Applying (11) to `s_R` gives the quantitative failure:

\[
\boxed{
\|(I-J_R)s_R\|
\ge
\frac{\|J_Rt\|^2}{\|(I-J_R)t\|}
\longrightarrow\infty.
}
\tag{36}
\]

So the obstruction is not failure of finite-window synthesis. Finite-window synthesis is exact at every scale. The obstruction is that the compatible natural continuations become violently nonuniform in the unseen future.

## 5. The fixed mode has an exact unfiltered one-cell budget

Take `t in T_infinity` and put `g_R=J_Rt`. Equation (4) gives

\[
g_R\in\mathcal G_R,
\qquad
J_{R+1}t\in\mathcal G_{R+1}.
\tag{37}
\]

The `NB-063` orthogonal graph decomposition is

\[
\mathcal G_{R+1}
=
\{g+\Gamma_Rg:g\in\mathcal G_R\}
\oplus\operatorname{span}\{C_R\}.
\tag{38}
\]

Restriction by `J_R` fixes the graph coordinate uniquely, so the graph coordinate of `J_(R+1)t` must be exactly `g_R`. Therefore

\[
J_{R+1}t
=g_R+\Gamma_Rg_R+\beta_RC_R,
\tag{39}
\]

which proves (17). Since `Gamma_Rg_R in X_R^circ` and `C_R` is orthogonal to that space,

\[
\|x_R^{(t)}\|^2
=
\|\Gamma_Rg_R\|^2
+|\beta_R|^2\|C_R\|^2.
\tag{40}
\]

The cells are pairwise orthogonal and partition the tail after `log 2`, so summing (40) gives the exact identity (18).

For nonzero `t`, `||g_R||->||t||`. Hence for all sufficiently large `R`, `||g_R||>=||t||/sqrt2`, and

\[
\sum_R
\left\|
\Gamma_R\frac{g_R}{\|g_R\|}
\right\|^2
<\infty.
\tag{41}
\]

This proves (19). It is stronger than a filtered spectral statement for the stable mode itself: the actual one-cell continuation norm is square-summable.

For the canonical persistent branch, both

\[
\frac{p_R}{\|p_R\|}
\quad\text{and}\quad
\frac{J_Rt_*}{\|J_Rt_*\|}
\tag{42}
\]

converge strongly to `t_*/||t_*||`. One must **not**, however, apply `Gamma_R` to their difference and infer convergence of the images: `||Gamma_R||` may grow without control. This is why the source-visible filtered budget of `NB-065` remains useful even though the hidden stable mode has the stronger unfiltered law (19).

## 6. Flat control and the new mechanism boundary

In the unit-outer control of `NB-056`, every causal innovation `D_j^(0)` is supported entirely in its birth cell. Hence every `g in G_R^(0)` already has a natural extension with zero future tail, and

\[
\Lambda_R^{(0)}=0.
\tag{43}
\]

Equation (15) correctly gives

\[
\mathcal T_\infty^{(0)}=\{0\},
\tag{44}
\]

consistent with the explicit cubic collective-tail decay. The control therefore distinguishes the new obstruction correctly: arithmetic forward memory must accumulate into an unbounded **long-horizon extension cost** before a stable tail can exist.

The converse is false. `Lambda_R -> infinity` does not imply that `T_infinity` is nonzero, and `T_infinity != {0}` does not imply that the canonical target has a nonzero projection onto it. Equations (14)--(15) are one-way source obstructions, while (5)--(8) identify the additional target-specific branch.

Likewise, (36) is not a contradiction with the exact local synthesis of `NB-062`. Local convergence on every finite window is much weaker than convergence in the ambient Hardy norm. A nonzero stable mode can exist only by exploiting precisely that gap.

## 7. Prior-art boundary and next target

Stable ranges, generalized kernels, monotone convergence of nested orthogonal projections, and quotient/right-inverse conditioning are standard Hilbert-space and operator-theoretic ideas. No novelty is claimed for those abstract principles. `NB-060` already identifies `T_infinity` as the stable range complementary to the generalized kernel of the dyadic backward shift, while `NB-061`--`NB-063` supply the line-specific finite-window and causal-graph structure used here.

A targeted literature audit covered the Hardy-space orthogonal-complement work of Calderaro--Manzur--Noor--Santos, contemporary Nyman subspace-angle work, Gram/block-conditioning work, and generalized Nyman approximation papers emphasizing coefficient control. The search did not locate the source-specific combination proved here: the Blaschke-deflated stable tail is exactly the inverse-limit space of finite natural traces, a canonical persistent target converges to one fixed member of that space, and global orthogonality forces the natural continuation cost of every nonzero such member to diverge at least by (11). No priority claim is made.

No specialized external estimate is load-bearing for the derivation, so `SOURCES.md` remains unchanged.

The durable shift in the live frontier is the separation between **one-cell transmission** and **long-horizon continuation**. `NB-065` shows that the canonical visible target has only a finite filtered one-cell transmission budget. The present finding shows that, on a persistent branch, the limiting stable mode has an even stronger square-summable unfiltered one-cell budget, yet its exact natural extensions must blow up arbitrarily far in the future. A useful next source theorem should therefore control the extension constants `Lambda_R`, or an explicit causal upper bound for them, rather than only another local singular-value statistic of `Gamma_R`. A bounded extension subsequence would collapse the entire stable tail by (15).