# ANF-075 — arbitrarily narrow central notches escape every fixed real-support cap

**Status:** `EXACT-DERIVED + REAL-MULTIPLICITY + FINITE-SUPPORT-UNIFORM + SUPPORT-CARDINALITY-ESCAPE + ONE-PAIR-SIX-POINT-COROLLARY`. `ANF-073` exposed real multiplicity as the first obstruction missed by the minimum-slack central-notch normalization, and `ANF-074` showed that amplitude reoptimization absorbs every positive-spectrum multiplicity pattern supported on at most two distinct real sites. The apparent next gate was therefore three distinct real support sites. That gate is not fundamental. A crude but uniform energy estimate shows that, after paying a support-count-dependent normalization slack of order `beta eta`, the same central-notch family beats Montgomery--Taylor on **every prescribed finite real-support cap**. The price grows only linearly with the number of distinct support sites, while the pair-functional gain is order `beta`; narrowing the notch makes every fixed cap affordable.

More precisely, fix an integer `R>=1` and define

\[
\eta_R
:=3R-\sqrt{9R^2-3}
=\frac{3}{3R+\sqrt{9R^2-3}}.
\tag{1}
\]

For every

\[
\boxed{0<\eta<\eta_R,\qquad 0<s<1,}
\tag{2}
\]

use the central-notch profile of `ANF-034`/`ANF-074`,

\[
J_s=J_{\rm MT}-s\phi_\eta,
\qquad
\beta:=s b_\eta,
\qquad
\varepsilon:=\beta\eta,
\qquad
F_s=\widehat J_s.
\tag{3}
\]

Then every finite real multiset `Z` supported on at most `R` distinct real sites satisfies the deterministic affine inequality

\[
\boxed{
s(Z)\ge A_R|Z|-E_{F_s}(Z),
\qquad
A_R:=2-2R\varepsilon.
}
\tag{4}
\]

The corresponding normalization slack is

\[
\boxed{
\delta_R
:=1+F_s(0)-A_R
=(2R-1)\varepsilon,
}
\tag{5}
\]

and the exact BGSST objective obeys

\[
\boxed{
M(F_s)+\delta_R
=
m_{\rm MT}
-\beta\left(
1-2R\eta+\frac{\eta^2}{3}
\right)
<m_{\rm MT}.
}
\tag{6}
\]

Thus no argument based on real multiplicity patterns with a **fixed a priori bound on the number of distinct support sites** can kill the central-notch shape family. For any such cap one can narrow the notch and retain a strict Montgomery--Taylor improvement after paying enough deterministic slack to cover the entire capped class.

## 1. The notch has an exact global negative floor

`ANF-074` records the two identities needed here:

\[
F_s(0)=1-\beta\eta=1-\varepsilon
\tag{7}
\]

and, because `R_MT>=0` while the removed sinc-square profile lies between zero and `b_eta eta`,

\[
\boxed{
F_s(t)\ge-\beta\eta=-\varepsilon
\qquad(t\in\mathbb R).
}
\tag{8}
\]

No positive-semidefinite optimization is needed below. Equation (8) is deliberately much cruder than the exact positive-spectrum Gram geometry used in `ANF-074`; its advantage is that it scales uniformly with an arbitrary fixed number of support sites.

Let the distinct support sites of a real multiset be `x_1,...,x_r`, where `1<=r<=R`, and let their positive integer multiplicities be `k_1,...,k_r`. Put

\[
N:=\sum_{i=1}^r k_i=|Z|,
\qquad
\sigma:=s(Z)=\#\{i:k_i=1\}.
\tag{9}
\]

Using (7) on the diagonal and (8) on every off-diagonal support pair,

\[
\begin{aligned}
E_{F_s}(Z)
&=
(1-\varepsilon)\sum_i k_i^2
+
2\sum_{i<j}k_i k_j F_s(x_i-x_j)\\
&\ge
(1-\varepsilon)\sum_i k_i^2
-
2\varepsilon\sum_{i<j}k_i k_j\\
&=
\boxed{
\sum_i k_i^2-\varepsilon N^2.
}
\end{aligned}
\tag{10}
\]

This is the only energy input in the finite-support theorem.

## 2. Exact multiplicity bookkeeping closes every support cap

Insert the lower bound (10) into the affine slack at the intercept `A_R` from (4):

\[
\begin{aligned}
\mathcal S_R(Z)
&:=
\sigma-A_RN+E_{F_s}(Z)\\
&\ge
\sum_i k_i^2-2N+\sigma
+\varepsilon N(2R-N).
\end{aligned}
\tag{11}
\]

The first term has the exact multiplicity decomposition

\[
\boxed{
P(k)
:=
\sum_i k_i^2-2N+\sigma
=
\sum_{k_i\ge2}k_i(k_i-2)
\ge0.
}
\tag{12}
\]

If `N<=2R`, both terms on the right side of (11) are nonnegative and the claim is immediate.

Suppose instead that `N>2R`. Cauchy gives

\[
\sum_i k_i^2
\ge\frac{N^2}{r}
\ge\frac{N^2}{R},
\tag{13}
\]

hence

\[
P(k)
\ge
\frac{N^2}{R}-2N
=
\frac{N(N-2R)}{R}.
\tag{14}
\]

The width in (1) automatically satisfies

\[
\eta_R
=
\frac{3}{3R+\sqrt{9R^2-3}}
<\frac1R.
\tag{15}
\]

Since `0<s<1` and `0<b_eta<=1`, equations (2)--(3) imply

\[
0<\varepsilon<\eta<\frac1R.
\tag{16}
\]

Combining (14) and (16),

\[
P(k)
>
\varepsilon N(N-2R),
\tag{17}
\]

which cancels the negative second term in (11). Therefore

\[
\boxed{\mathcal S_R(Z)\ge0}
\tag{18}
\]

for every finite real multiset supported on at most `R` distinct sites, proving (4).

Several stress tests are built into this bookkeeping. All-simple sets have `P=0` but `N=r<=R`, so they lie in the safe `N<=2R` branch. Uniform doubles on `R` sites have `N=2R` and `P=0`, exactly the boundary where the support-count term vanishes. Large multiplicities move into the `N>2R` branch, where the quadratic diagonal growth in (14) dominates the worst possible accumulated negative pair contribution. No assumption of equal multiplicities, separated sites, generic positions, or attained spatial minima enters the proof.

## 3. The exact support-width tradeoff still beats Montgomery--Taylor

By `ANF-074` the central notch has

\[
M(F_s)
=
m_{\rm MT}
-\beta a(\eta),
\qquad
a(\eta)
=
1-\eta+\frac{\eta^2}{3}.
\tag{19}
\]

Using (5),

\[
\begin{aligned}
M(F_s)+\delta_R
&=
m_{\rm MT}
-\beta a(\eta)
+(2R-1)\beta\eta\\
&=
m_{\rm MT}
-\beta\left(
1-2R\eta+\frac{\eta^2}{3}
\right).
\end{aligned}
\tag{20}
\]

The small root of

\[
1-2R\eta+\frac{\eta^2}{3}=0
\tag{21}
\]

is exactly `eta_R` from (1). Therefore (2) makes the bracket in (20) strictly positive and proves (6).

This recovers a familiar boundary at `R=1`:

\[
\eta_1=3-\sqrt6,
\tag{22}
\]

the same width already isolated in `ANF-046`. For `R=2` the present argument is intentionally nonsharp: `ANF-074` uses positive-spectrum Gram structure and keeps the much larger full `R=1` width range. The point of (1) is not optimality at small `R`; it is the scalable statement

\[
\eta_R
=
\frac{1}{2R}+O(R^{-3}),
\tag{23}
\]

which shows that the admissible notch width only needs to shrink like the reciprocal of the support cap.

A convenient conservative corollary is

\[
0<\eta\le\frac1{4R}
\quad\Longrightarrow\quad
1-2R\eta+\frac{\eta^2}{3}\ge\frac12,
\tag{24}
\]

so in this range

\[
\boxed{
M(F_s)+\delta_R
\le m_{\rm MT}-\frac{\beta}{2}.
}
\tag{25}
\]

The gain is therefore not merely qualitative.

## 4. Consequence for the current three-support frontier

At `R=3`,

\[
\eta_3
=
9-\sqrt{78}
=
0.1682391336\ldots.
\tag{26}
\]

Every central notch with `0<eta<eta_3` and `0<s<1` therefore survives **all** real multisets supported on at most three distinct sites, including mixed simple/repeated patterns such as `(2,1,1)` and `(2,2,1)`, arbitrary larger multiplicities, and the no-simple class proposed as the next gate in `ANF-074`.

Thus the `three-distinct-support real-multiplicity envelope` is not a shape-level obstruction. The correct finite-real boundary is support cardinality itself: for a notch of width `eta`, the present certificate handles every real multiset with

\[
R
<
\frac{1+\eta^2/3}{2\eta}.
\tag{27}
\]

As `eta->0`, this protected support cardinality tends to infinity. Equivalently, **no fixed finite-support family of real multiplicity tests can furnish a uniform no-go for the narrowing central-notch ray**.

This does not say that one fixed notch passes all finite real multisets. Equation (27) is a finite-support theorem whose protected cap grows as the notch narrows. A genuine real-multiplicity no-go can still arise from configurations whose number of distinct support sites grows on the `1/eta` scale, or from a global weighted-Gram/stability mechanism that controls all support sizes at once.

## 5. Six-point one-pair consequence at the reoptimized intercept

The result also repairs the real boundary left by `ANF-072` for a concrete narrower regime. A collapsed one-pair six-point configuration

\[
R_T=\{0,0,t_1,t_2,t_3,t_4\}
\tag{28}
\]

has at most five distinct real support sites. Taking `R=5` gives

\[
\eta_5
=
15-\sqrt{222}
=
0.1003355742\ldots,
\tag{29}
\]

and the affine intercept

\[
A_5=2-10\beta\eta.
\tag{30}
\]

Hence (4) proves the complete collapsed real-multiplicity inequality for (28) whenever `eta<eta_5`.

For the exact one-pair class of `ANF-072`, additionally impose its already certified amplitude range `0<s<=1/4000`. On the collapse-reversing branch, `ANF-072` proves positive affine slack at the **harder** intercept `2-2 beta eta`; lowering the intercept to (30) can only increase that slack. On the nonreversing branch, the energy comparison used in `ANF-072` transfers positivity from the collapsed configuration to the one-pair configuration because the relevant cardinality/simple-real bookkeeping is the same in that class. Consequently the central notch satisfies the full one-pair six-point affine inequality at `A_5` throughout

\[
\boxed{
0<\eta<15-\sqrt{222},
\qquad
0<s\le\frac1{4000}.
}
\tag{31}
\]

Its objective still beats Montgomery--Taylor by (6). Thus the six-point one-pair branch is not merely reduced to real multiplicity; after paying the support-cap slack it is completely safe in the explicit regime (31).

This does not extend automatically to two nonreal pairs or to arbitrary cardinality. It also does not contradict `ANF-073`: the minimum-slack intercept `2-2 beta eta` genuinely fails on doubled real sites. The new point is that increasing the slack by only `O(R beta eta)` is cheap compared with the `O(beta)` pair-functional gain when the notch is narrow.

## 6. Prior art, audit, and remaining boundary

The nearest classical language is many-particle stability/superstability: Fisher--Ruelle and Ruelle-type arguments exploit positive short-range self-energy against an accumulated negative pair tail, often producing quadratic occupancy bounds. The present estimate has the same broad flavor, and no novelty is claimed for that principle, Cauchy's inequality, or bounded-below pair-potential bookkeeping. The exact zeta-side statement (4)--(6) is instead a specialization to the Mathia central-notch kernel, its simple-real counting term, and the Montgomery--Taylor objective. A targeted literature check found no external theorem needed for this finite-support specialization. The existing Sütő/Procacci stability anchors in `SOURCES.md` remain sufficient; no new load-bearing source is added.

The load-bearing interfaces are minimal and auditable:

1. `ANF-074` supplies exactly `F_s(0)=1-beta eta`, `F_s(t)>=-beta eta`, and the pair-functional identity (19).
2. Equation (10) uses the worst possible value `-epsilon` independently on every distinct support pair; it does not assume favorable phases or Gram correlations.
3. Equation (12) uses the repository's exact definition of `s(Z)` as the number of multiplicity-one real support points.
4. The only large-multiplicity input is Cauchy (13), with the actual support size `r<=R`.
5. The objective comparison is algebraic; `eta_R` is exactly the first positive root of (21).

The finding does **not** prove the universal affine certificate, improve the unconditional zeta-zero proportion, or imply RH. It changes the next scalar question. Testing isolated three-site multiplicity patterns is no longer decisive. A real-multiplicity obstruction robust against the narrowing notch must either control support cardinalities growing at least on the reciprocal-width scale or supply a support-uniform stability inequality. Complex multi-pair geometry and the cardinality-eleven higher-order one-pair frontier remain outside this finite-real theorem.
