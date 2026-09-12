# NB-075 — future Schur elimination resolves prediction volume into a partial-correlation cancellation budget

**Status:** `EXACT-DERIVED + FINITE-SCHUR-CHAIN + PARTIAL-CORRELATION-BUDGET + INFINITE-FUTURE-CORE + STABLE-TAIL-OBSTRUCTION + SOURCE-ONLY-SCALARIZATION + METHOD-ADVANCE`.

`NB-074` replaces the growing-dimensional continuation problem by the nonnegative renormalized prediction-volume charge

\[
\mathfrak J_{R,N}
=
\log\frac{\det S_{R,N}}{\det A_R},
\qquad N\ge R,
\tag{1}
\]

where `A_R` is the visible Gram matrix before `log R` and `S_(R,N)` is the prefix Gram after optimally eliminating the finite future `D_R,...,D_N`. A persistent stable tail forces (1) to diverge for every finite horizon schedule. The remaining source-facing difficulty is that (1) is still a determinant of an `(R-1) x (R-1)` matrix.

The present finding gives an exact scalar elimination chain in the **future-horizon direction**. Before any future correction, define the raw continuation-volume charge

\[
\boxed{
\mathfrak L_R
:=
\log\frac{\det H_{<R}}{\det A_R},
}
\tag{2}
\]

where `H_(<R)` is the global Gram matrix of `D_1,...,D_(R-1)`. Since global norm splits into visible plus tail norm,

\[
H_{<R}=A_R+B_R,
\qquad B_R\succeq0,
\tag{3}
\]

so `mathfrak L_R>=0`.

For each `n>=R`, residualize the new innovation `D_n` and the old prefix against the already admitted future `D_R,...,D_(n-1)`. The squared multiple correlation of that residualized `D_n` with the residualized prefix is a scalar

\[
0\le \beta_{R,n}<1.
\tag{4}
\]

Then the finite charge has the exact chain rule

\[
\boxed{
\mathfrak J_{R,N}
=
\mathfrak L_R
-
\sum_{n=R}^{N}
\bigl[-\log(1-\beta_{R,n})\bigr].
}
\tag{5}
\]

Thus every added future innovation removes a **nonnegative scalar amount** of raw continuation volume, and nothing else. Letting `N->infinity` gives

\[
\boxed{
\mathfrak J_{R,\infty}
:=
\lim_{N\to\infty}\mathfrak J_{R,N}
=
\mathfrak L_R
-
\sum_{n=R}^{\infty}
\bigl[-\log(1-\beta_{R,n})\bigr]
\ge0.
}
\tag{6}
\]

The series converges for every fixed `R`. More importantly, if `0!=t in T_infinity`, then

\[
\boxed{
\mathfrak J_{R,\infty}
\ge
\log\!\left(
1+\frac{\|J_Rt\|^2}{\|(I-J_R)t\|^2}
\right)
\longrightarrow\infty.
}
\tag{7}
\]

A stable tail therefore requires a divergent **uncancelled future-volume core**. It is not enough for the raw prefix tails to be large: after every later innovation has been allowed to explain them sequentially, a divergent amount of volume must still remain.

Conversely, (5) produces a purely scalar sufficient criterion. If there are unbounded `R_k`, finite horizons `N_k>=R_k`, and `C<infinity` such that

\[
\boxed{
\sum_{n=R_k}^{N_k}
\bigl[-\log(1-\beta_{R_k,n})\bigr]
\ge
\mathfrak L_{R_k}-C,
}
\tag{8}
\]

then `mathfrak J_(R_k,N_k)<=C`, and `NB-074` forces

\[
\boxed{\mathcal T_\infty=\{0\}.}
\tag{9}
\]

Since `-log(1-x)>=x` on `[0,1)`, the stronger but simpler source target

\[
\boxed{
\sum_{n=R_k}^{N_k}\beta_{R_k,n}
\ge
\mathfrak L_{R_k}-C
}
\tag{10}
\]

already suffices. This allows `mathfrak L_R` itself to diverge. The route is to show that actual later Nyman innovations cancel essentially all of that raw continuation budget.

## 1. One future innovation is a rank-one Schur update

Fix `R>=2`. For `n>=R`, put

\[
\mathcal F_{R,n-1}
:=
\operatorname{span}\{D_R,\ldots,D_{n-1}\},
\tag{11}
\]

with the convention `F_(R,R-1)={0}`, and let `P_(R,n-1)` denote its orthogonal projector. For the prefix indices `i<R`, define

\[
u_i^{(n)}
:=(I-P_{R,n-1})D_i,
\qquad
w_n^{(R)}
:=(I-P_{R,n-1})D_n.
\tag{12}
\]

The Gram matrix of the residualized prefix vectors is exactly the previous Schur complement,

\[
\operatorname{Gram}\{u_i^{(n)}:i<R\}
=S_{R,n-1},
\tag{13}
\]

where for the empty-future case we set

\[
S_{R,R-1}:=H_{<R}.
\tag{14}
\]

Let

\[
\sigma_{R,n}^2:=\|w_n^{(R)}\|^2>0
\tag{15}
\]

and let `q_(R,n) in C^(R-1)` be the cross-Gram vector

\[
(q_{R,n})_i
:=
\langle u_i^{(n)},w_n^{(R)}\rangle.
\tag{16}
\]

Finite independence of the innovations implies `sigma_(R,n)>0` and `S_(R,n-1)>0`. Adding `D_n` to the future elimination gives the standard rank-one Schur update

\[
\boxed{
S_{R,n}
=
S_{R,n-1}
-
\frac{q_{R,n}q_{R,n}^*}{\sigma_{R,n}^2}.
}
\tag{17}
\]

Define

\[
\boxed{
\beta_{R,n}
:=
\frac{
q_{R,n}^*S_{R,n-1}^{-1}q_{R,n}
}{\sigma_{R,n}^2}.
}
\tag{18}
\]

The block Gram matrix of the residualized prefix together with `w_n^(R)` is positive definite, so its scalar Schur complement is positive and therefore

\[
0\le\beta_{R,n}<1.
\tag{19}
\]

Geometrically, if

\[
\mathcal W_{R,n}
:=
\operatorname{span}\{u_i^{(n)}:i<R\},
\tag{20}
\]

then the usual projection formula gives

\[
\boxed{
\beta_{R,n}
=
\frac{
\|P_{\mathcal W_{R,n}}w_n^{(R)}\|^2
}{
\|w_n^{(R)}\|^2
}.
}
\tag{21}
\]

Thus `beta_(R,n)` is not a raw pairwise correlation. It is the squared multiple correlation of the genuinely new part of `D_n` with the genuinely unresolved part of the old prefix, **after** the previously admitted future has been removed from both.

## 2. Determinant volume becomes an additive scalar cancellation budget

Applying the matrix determinant lemma to (17) yields

\[
\det S_{R,n}
=
\det S_{R,n-1}
\left(1-\beta_{R,n}\right).
\tag{22}
\]

Taking logarithms and iterating from the empty future (14) gives

\[
\log\frac{\det S_{R,N}}{\det A_R}
=
\log\frac{\det H_{<R}}{\det A_R}
+
\sum_{n=R}^{N}\log(1-\beta_{R,n}),
\tag{23}
\]

which is exactly (5).

`NB-067` proves that `S_(R,N)` decreases in Loewner order to a positive matrix `S_R>=A_R`. Consequently `mathfrak J_(R,N)` decreases to a finite nonnegative limit for every fixed `R`. Equation (5) then shows that

\[
\sum_{n=R}^{\infty}-\log(1-\beta_{R,n})
\le
\mathfrak L_R<\infty,
\tag{24}
\]

and proves (6). No interchange of the limits `R->infinity` and `N->infinity` is used.

The first step has a familiar interpretation. For `n=R` there is no previously admitted future, so

\[
\beta_{R,R}
=
\frac{\|P_{\operatorname{span}(D_1,\ldots,D_{R-1})}D_R\|^2}{\|D_R\|^2}.
\tag{25}
\]

Hence

\[
-\log(1-\beta_{R,R})
=
\log
\frac{\|D_R\|^2}
{\operatorname{dist}(D_R,\operatorname{span}\{D_1,\ldots,D_{R-1}\})^2}.
\tag{26}
\]

Equation (5) at `N=R` therefore reproduces the one-step determinant formula of `NB-074`: the difference between the raw prefix charge and the one-step unseen charge is exactly the global backward-predictability charge of the newest innovation.

## 3. A persistent tail survives complete future cancellation

`NB-074` proves for every finite `N>=R` and every nonzero `t in T_infinity` that

\[
\mathfrak J_{R,N}
\ge
\log\!\left(
1+\frac{\|J_Rt\|^2}{\|(I-J_R)t\|^2}
\right).
\tag{27}
\]

The right side is independent of `N`. Taking the monotone limit in `N` proves (7). Since `J_Rt->t!=0` while `(I-J_R)t->0`, the lower bound diverges.

Combining (6) and (7) gives a sharper falsification picture than raw-tail growth:

\[
\boxed{
0\ne\mathcal T_\infty
\Longrightarrow
\mathfrak L_R
-
\sum_{n=R}^{\infty}-\log(1-\beta_{R,n})
\longrightarrow\infty.
}
\tag{28}
\]

Thus a stable mode cannot be manufactured merely by large prefix tails or by poor finite conditioning. It requires a growing portion of the raw continuation volume that the **entire** later innovation sequence fails to explain through its exact conditional correlations.

The contrapositive is the useful source route. Equation (8) asks only for a scalar lower bound on the amount of raw volume removed by a chosen finite future schedule. It is strictly more permissive than trying to prove `mathfrak L_R=O(1)`: `mathfrak L_R` may grow without obstruction if the future-cancellation budget tracks it to within `O(1)`.

## 4. Stress tests: raw continuation volume is not itself an obstruction

The unit-outer control from `NB-056/062/067` has disjoint cell innovations. Then `B_R=0`, so

\[
\mathfrak L_R=0,
\qquad
\beta_{R,n}=0,
\qquad
\mathfrak J_{R,N}=0
\tag{29}
\]

for every admissible `R,n,N`, as required.

A two-coordinate control shows why the subtraction in (5) is load-bearing. Let the early window be `span{e_0}` and take

\[
D_1=e_0+Me_1,
\qquad
D_2=e_1,
\tag{30}
\]

with `M>0`. At `R=2`, the visible Gram is `A_2=[1]`, while the raw global prefix Gram is `[1+M^2]`. Therefore

\[
\mathfrak L_2=\log(1+M^2),
\tag{31}
\]

which can be arbitrarily large. But

\[
\beta_{2,2}=\frac{M^2}{1+M^2},
\qquad
-\log(1-\beta_{2,2})=\log(1+M^2),
\tag{32}
\]

so the single future innovation removes the entire raw charge and

\[
\boxed{\mathfrak J_{2,2}=0.}
\tag{33}
\]

Large raw tail energy, a large raw determinant ratio, or a nearly perfect old/new correlation is therefore not evidence for a stable tail. The relevant quantity is the **uncancelled** budget after future elimination.

This also explains why replacing `beta_(R,n)` by unconditioned pairwise correlations is invalid. The same future direction can correlate with many prefix directions before residualization, and summing those raw correlations double-counts removable volume. Equations (18)--(21) condition on all already admitted future directions and count exactly the new cancellation once.

## 5. Boundaries and prior-art audit

The chain rule is exact finite-dimensional Hilbert-space algebra. Rank-one Schur updates, the matrix determinant lemma, and the identification of (18) with a squared multiple correlation are classical; no novelty is claimed for those ingredients. The line-local advance is the application to the `NB-067/074` causal Nyman continuation matrices, including the visible-Gram renormalization and the stable-tail implication (7)--(10).

A targeted literature audit checked recent Nyman--Beurling Gram work. Werner Ehm's `arXiv:2405.06349` develops explicit Nyman Gram formulae, reciprocity relations, and quadratic-form decompositions. Hugh Carvill's `arXiv:2510.18132` develops Mellin-smoothed Gram decay and block compressibility. Alouges--Darses--Hillion, `arXiv:2006.02953`, study generalized Nyman--Beurling approximation and associated Gram structures. The audit did not locate the specific future-horizon factorization (5), the residualized partial-correlation variables (18), or the stable-tail cancellation criterion (8)--(10). No priority claim is made.

No specialized external estimate is load-bearing here, so `SOURCES.md` remains unchanged.

Several limitations are essential. First, divergence of `mathfrak J_(R,infinity)` is necessary for a stable tail but is not sufficient in a general growing-dimensional causal family: many moderate generalized eigenvalues can make a log determinant diverge while the worst continuation singular value remains bounded. Second, (8) is only useful if the `beta_(R,n)` can be controlled from the actual arithmetic source; defining them does not supply that estimate. Third, all finite numerical tests must preserve positive definiteness and conditional residualization rigorously; unstable floating-point regressions can manufacture `beta` values close to one. Finally, the order of future elimination matters for the individual `beta` values even though their total logarithmic cancellation in (5) is fixed by the chosen future span.

## 6. Consequence for the live Nyman frontier

After `NB-074`, the immediate source target was to keep a renormalized determinant charge bounded on an unbounded sequence of windows. Equation (5) replaces that single opaque determinant task by a scalar budget with two independently meaningful pieces:

\[
\boxed{
\text{raw prefix continuation volume}
\;\mathfrak L_R
\quad\text{minus}\quad
\text{future partial-correlation cancellation}.
}
\tag{34}
\]

The next arithmetic question is therefore more specific: **do the exact later Nyman innovations recover essentially all of the raw continuation volume generated by the earlier innovations?** It is enough to prove this to `O(1)` accuracy along an unbounded sequence and at any finite horizon schedule. The simple sufficient form (10) asks for a lower bound on a sum of squared conditional projection coefficients rather than an upper bound on a growing determinant.

If that scalar cancellation mechanism fails, (28) identifies what a genuine stable-tail obstruction must look like: a divergent amount of prefix continuation volume that remains invisible to every later innovation even after exact sequential residualization. This is now the source-facing distinction to test, rather than generic Gram conditioning or raw tail size.