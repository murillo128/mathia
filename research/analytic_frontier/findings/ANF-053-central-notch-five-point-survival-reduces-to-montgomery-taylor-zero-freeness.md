# ANF-053 — central-notch five-point survival reduces to Montgomery--Taylor zero-freeness

**Status:** `EXACT-DERIVED + SIGNED-NOTCH-ASYMPTOTIC + UNIFORM-FAMILY-COMPACTNESS + ZERO-SET-DICHOTOMY + STRUCTURAL-REDUCTION`. `ANF-052` proves that a narrow central notch changes the two-conjugate-pair five-point defect only by `O(s b_eta eta^3)` on bounded heights, but that absolute estimate leaves open whether the cubic perturbation helps or hurts near a small Montgomery--Taylor margin. The sign is in fact universal. On every bounded geometry box, the notch decreases the defect at cubic order by an amount depending only on the total squared conjugate height; all horizontal phase and anti-phase geometry first enters two powers later.

For the central-notch family

\[
J_{\eta,s}=J_{\rm MT}-s\phi_\eta,
\qquad
\phi_\eta(\alpha)=b_\eta\left(1-\frac{|\alpha|}{\eta}\right)_+,
\qquad 0<s\le1,
\tag{1}
\]

let `H_{eta,s}` be the two-pair defect of `ANF-040` and let `H_MT` denote the same defect for `J_MT`. For every fixed `Y,T<infinity`, uniformly on

\[
0<y_1,y_2\le Y,
\qquad
|t_1|,|t_2|\le T,
\]

one has

\[
\boxed{
H_{\eta,s}-H_{\rm MT}
=-\frac53\pi^2 s b_\eta
(y_1^2+y_2^2)\eta^3
+O_{Y,T}(s b_\eta\eta^5).
}
\tag{2}
\]

More precisely, if `d=t_1-t_2`, the first horizontal dependence appears in the `eta^5` coefficient. Consequently every genuine zero of the Montgomery--Taylor two-pair defect is **immediately destabilized** by every sufficiently narrow nontrivial central notch.

Conversely, if `H_MT` has no genuine zero for `y_1,y_2>0`, then the entire narrow-notch family admits one common obstruction box, and `H_MT` has a positive minimum on that box. Uniform convergence from `ANF-052` then transfers positivity to all sufficiently narrow notches. Thus the remaining five-point question for the explicit separator ray is equivalent to one base-profile question:

\[
\boxed{
\begin{aligned}
&H_{\rm MT}(y_1,y_2;t_1,t_2)\ne0
\quad\text{for all }y_1,y_2>0,\ t_1,t_2\in\mathbb R\\
&\qquad\Longleftrightarrow\\
&\exists\eta_*>0\ \forall\,0<\eta<\eta_*\ \forall\,0<s\le1:\
H_{\eta,s}(y_1,y_2;t_1,t_2)>0
\quad\text{for all }y_1,y_2>0,\ t_1,t_2\in\mathbb R.
\end{aligned}
}
\tag{3}
\]

The left side is automatically a strict-positivity statement: if `H_MT` were negative anywhere, the uniform small-height positivity from `ANF-040` and continuity along a vertical scaling path would force an intervening genuine zero.

## 1. The central-frequency expansion has a universal positive quadratic coefficient

Retain the exact pointwise integrand from `ANF-040`--`ANF-052`,

\[
H_J=\int J(\alpha)h_\alpha\,d\alpha,
\tag{4}
\]

where

\[
\begin{aligned}
h_\alpha={}&(c_1^2-1)+(c_2^2-1)
+2(c_1c_2-1)\cos(2\pi\alpha d)\\
&+(c_1-1)\cos(2\pi\alpha t_1)
+(c_2-1)\cos(2\pi\alpha t_2),
\end{aligned}
\tag{5}
\]

and

\[
c_j=\cosh(2\pi\alpha y_j),
\qquad d=t_1-t_2.
\tag{6}
\]

On a bounded geometry box the Taylor expansions are uniform. At the central frequency,

\[
c_j-1
=2\pi^2y_j^2\alpha^2+O_Y(\alpha^4),
\tag{7}
\]

\[
c_j^2-1
=4\pi^2y_j^2\alpha^2+O_Y(\alpha^4),
\tag{8}
\]

\[
c_1c_2-1
=2\pi^2(y_1^2+y_2^2)\alpha^2+O_Y(\alpha^4),
\tag{9}
\]

while every cosine in (5) equals `1+O_T(alpha^2)`. Therefore

\[
\boxed{
h_\alpha
=10\pi^2(y_1^2+y_2^2)\alpha^2
+O_{Y,T}(\alpha^4).}
\tag{10}
\]

The coefficient `10` has a direct decomposition. The two self terms contribute `4`, the coupled two-pair term contributes another `4`, and the two real-anchor terms contribute `2`, all multiplied by `pi^2(y_1^2+y_2^2)alpha^2`. In particular, the common horizontal phase, relative separation, and anti-phase tube are invisible at this first nonzero central order.

For auditability, the next coefficient can also be written explicitly. One has

\[
\boxed{
\begin{aligned}
h_\alpha={}&10\pi^2r^2\alpha^2
+\pi^4\mathcal Q_4\alpha^4
+O_{Y,T}(\alpha^6),\\
r^2:={}&y_1^2+y_2^2,
\end{aligned}}
\tag{11}
\]

with

\[
\boxed{
\begin{aligned}
\mathcal Q_4={}&
\frac{22}{3}(y_1^4+y_2^4)
+8y_1^2y_2^2\\
&-4t_1^2y_1^2-4t_2^2y_2^2
-8(y_1^2+y_2^2)(t_1-t_2)^2.
\end{aligned}}
\tag{12}
\]

Thus horizontal coherence genuinely enters only through the quartic frequency coefficient.

## 2. Exact tent moments make the cubic notch drift strictly negative

Because the defect is linear in the spectrum,

\[
H_{\eta,s}-H_{\rm MT}
=-s\int\phi_\eta(\alpha)h_\alpha\,d\alpha.
\tag{13}
\]

`ANF-052` records the exact tent moments

\[
\int\phi_\eta(\alpha)\alpha^2\,d\alpha
=\frac{b_\eta\eta^3}{6},
\qquad
\int\phi_\eta(\alpha)\alpha^4\,d\alpha
=\frac{b_\eta\eta^5}{15}.
\tag{14}
\]

Combining (10), (13), and (14) gives (2). Using the explicit quartic term gives the sharper expansion

\[
\boxed{
H_{\eta,s}-H_{\rm MT}
=-s b_\eta\left[
\frac53\pi^2r^2\eta^3
+\frac{\pi^4}{15}\mathcal Q_4\eta^5
+O_{Y,T}(\eta^7)
\right].
}
\tag{15}
\]

The load-bearing sign is now visible: for every genuine shape `r^2>0`, the coefficient of `s b_eta eta^3` is strictly negative. The fifth-order correction may depend on the anti-phase geometry, but it cannot change the sign for sufficiently narrow notches at any fixed shape.

This sharpens the scale hierarchy of `ANF-052`. The five-point response is not merely cubic in magnitude; its leading cubic direction is universally **toward lower defect**, while horizontal discrimination begins only at quintic order in the notch width.

## 3. Every genuine Montgomery--Taylor zero is perturbatively fatal

Suppose

\[
H_{\rm MT}(y_1,y_2;t_1,t_2)=0
\tag{16}
\]

at some fixed `y_1,y_2>0`. Evaluating (15) at that shape gives

\[
H_{\eta,s}
=-s b_\eta\eta^3
\left[
\frac53\pi^2(y_1^2+y_2^2)+O(\eta^2)
\right].
\tag{17}
\]

Since `b_eta>0` and `s>0`, the bracket is positive for all sufficiently small `eta`. Hence

\[
\boxed{
H_{\rm MT}=0\text{ at a genuine shape}
\quad\Longrightarrow\quad
H_{\eta,s}<0
}
\tag{18}
\]

at the **same shape** for every sufficiently narrow nontrivial central notch.

This is stronger than saying that a small perturbation might expose a nearby negative point. No movement in heights or horizontal phases is required. An exact Montgomery--Taylor zero is itself the finite witness after the notch is introduced.

A negative Montgomery--Taylor point also implies the existence of such a zero. Fix its horizontal geometry and scale both positive heights by `lambda in (0,1]`. `ANF-040`, together with `m_5(J_MT)>0`, gives strict positivity for all sufficiently small positive `lambda`, uniformly in the horizontal variables. If the value at `lambda=1` is negative, continuity forces a zero at some intermediate `lambda`. Therefore

\[
\boxed{
H_{\rm MT}\text{ has no genuine zero}
\quad\Longrightarrow\quad
H_{\rm MT}>0\text{ everywhere on the genuine two-pair domain}.}
\tag{19}
\]

So the relevant base-profile alternative is exactly **zero-free strict positivity versus existence of a zero**; there is no third negative-but-zero-free case.

## 4. All sufficiently narrow notches share one compact obstruction box

To prove the converse direction in (3), pointwise strict positivity of `H_MT` is not enough by itself because the domain is noncompact and the defect tends to zero as the heights approach the real axis. The compactification of `ANF-043`--`ANF-044` can, however, be made uniform over the entire narrow-notch family.

First choose `eta_0>0` so small that

\[
\frac56\eta_0^3<\frac12\,m_5(J_{\rm MT}).
\tag{20}
\]

Since `0<s b_eta<=1`, the curvature estimate of `ANF-038` gives

\[
\boxed{
m_5(J_{\eta,s})
\ge\frac12m_5(J_{\rm MT})>0
}
\tag{21}
\]

for every `eta<eta_0` and `0<s<=1`. The small-height expansion in `ANF-040` has a remainder controlled by compact spectral support and finitely many moments of `J`. Because

\[
0\le J_{\eta,s}\le J_{\rm MT},
\tag{22}
\]

those remainder constants are bounded uniformly by constants depending only on `J_MT`. Equations (21)--(22) therefore give a common `epsilon>0` such that

\[
\boxed{
0<y_1^2+y_2^2<\varepsilon^2
\quad\Longrightarrow\quad
H_{\eta,s}>0
}
\tag{23}
\]

for every sufficiently narrow notch and every horizontal geometry.

At the opposite vertical boundary, `ANF-052` already proves a family-level result: choose one positive-frequency interval

\[
I=[\beta,\gamma]\subset(1/2,1)
\tag{24}
\]

outside the central notch. For `eta_0<beta`, every family member agrees with `J_MT` on `I`, while removing nonnegative central mass can only decrease the global negative floor used in the coercivity estimate. Hence one common `Y<infinity` satisfies

\[
\boxed{
\max(y_1,y_2)\ge Y
\quad\Longrightarrow\quad
H_{\eta,s}>0.}
\tag{25}
\]

It remains to make horizontal compactness uniform on the slab `epsilon<=y_1,y_2<=Y`. The proof of `ANF-044` has exactly the required robustness. Its positive self-plus-anchor margin

\[
D_y(t)
\ge\int J(\alpha)(c_y-1)c_y\,d\alpha
\tag{26}
\]

may be restricted to the unchanged interval `I`, giving one common positive lower bound for the family. The Montgomery--Taylor transforms `L_MT` and `M_MT` decay uniformly over the compact height slab by the finite-net Riemann--Lebesgue argument of `ANF-044`. The notch corrections satisfy, uniformly on that slab,

\[
\left|L_{\phi_\eta,y}(t)\right|
\le C_Y b_\eta\eta^3,
\qquad
\left|M_{\phi_\eta,y_1,y_2}(t)\right|
\le C_Y' b_\eta\eta^3,
\tag{27}
\]

because every hyperbolic amplitude has a double zero at `alpha=0`. Shrinking `eta_0` makes these residual terms smaller than any fixed fraction of the common outer-interval margin.

For the bounded-relative-separation regime, the residual block from `ANF-044` is

\[
B_J
=\int J(\alpha)\Bigl[
(c_1-c_2)^2
+2(c_1c_2-1)(1+\cos(2\pi\alpha d))
\Bigr]d\alpha.
\tag{28}
\]

Its integrand is nonnegative. Restricting (28) to the unchanged interval `I` gives a strictly positive continuous function of `(y_1,y_2,d)`; on every compact slab and bounded `d` interval it therefore has a common positive minimum independent of the notch. Repeating the two escape cases of `ANF-044` with these common margins yields a single `T<infinity` such that

\[
\boxed{
H_{\eta,s}<0
\quad\Longrightarrow\quad
\varepsilon\le y_1,y_2\le Y,
\qquad
|t_1|,|t_2|\le T
}
\tag{29}
\]

for every `0<eta<eta_0` and every `0<s<=1`.

Thus the obstruction box does not drift as the notch narrows or as its depth varies. This uniformity is the missing compactness input needed to turn the pointwise perturbation estimate into a global theorem.

## 5. Zero-free Montgomery--Taylor implies five-point survival for every narrow notch

Assume now that `H_MT` has no genuine zero. By (19), it is strictly positive throughout the genuine domain. In particular, on the common compact box from (29),

\[
\mathcal K
=[\varepsilon,Y]^2\times[-T,T]^2,
\tag{30}
\]

continuity gives a positive margin

\[
\boxed{
\mu:=\min_{\mathcal K}H_{\rm MT}>0.}
\tag{31}
\]

`ANF-052` gives, for the same height ceiling `Y`, an absolute perturbation bound independent of the horizontal variables and bounded above uniformly for `0<s<=1` by

\[
\sup_{\mathcal K}|H_{\eta,s}-H_{\rm MT}|
\le C_Y\eta^3
\tag{32}
\]

for all sufficiently small `eta`. Choose `eta_*<=eta_0` so that the right side of (32) is less than `mu/2`. Then

\[
H_{\eta,s}\ge\frac\mu2>0
\tag{33}
\]

throughout `K` for every `0<eta<eta_*` and every `0<s<=1`. Outside `K`, the uniform small-height, high-height, and horizontal escape barriers from Section 4 already give strict positivity. This proves the forward implication in (3).

The reverse implication is (18): if `H_MT` has a genuine zero, then every sufficiently narrow notch with any positive depth has a negative defect at that same finite configuration. Hence (3) is an exact dichotomy.

For the explicit separator program this has a useful corollary. `ANF-034` allows the notch width to be chosen arbitrarily small and then permits a sufficiently small positive `s` with strict finite-real separation. Therefore, **if the Montgomery--Taylor two-pair defect is zero-free, one can choose an `ANF-034` separator that simultaneously beats the Montgomery--Taylor finite-real ratio and clears every cardinality-five two-pair complex collapse test.** If a Montgomery--Taylor zero exists, the same central-notch direction is killed at cardinality five no matter how small the nonzero notch depth is once the width is sufficiently narrow.

## 6. Prior art, falsification, and evidence boundary

No new external theorem is load-bearing. The exact Montgomery--Taylor extremizer remains anchored through Carneiro--Chandee--Littmann--Milinovich, and the positive Fourier--Laplace framework remains anchored through Buescu--Paixão--Symeonides in `SOURCES.md`. A targeted literature check around those extremal and strip-positive-definite frameworks found no theorem identifying the present two-pair five-point perturbation, its signed central-notch cubic term, or the zero-set dichotomy (3). Recent configuration-level improvements that retain multiple profiles or local state change the information carrier and do not supply this scalar perturbation argument. No publication-level novelty claim is made, and no `SOURCES.md` update is required.

The signed asymptotic can be falsified directly by expanding (5): the `alpha^2` coefficient must be exactly `10 pi^2(y_1^2+y_2^2)`, and the horizontal variables must first appear in the coefficient (12). Equations (14)--(15) then use exact tent moments, so no numerical evidence enters the sign claim. The uniform compactness step can be audited against the three noncompact directions already isolated in `ANF-043`--`ANF-044`: positive curvature controls the real-axis boundary, the fixed outer interval controls large height, and the same untouched interval plus small `O(eta^3)` central corrections controls horizontal escape.

This finding does **not** prove that `H_MT` is zero-free. It therefore does not yet prove that the central-notch separator survives all cardinality-five complex tests. It also does not address conjugation-invariant multisets of cardinality greater than five, nor does it establish the full universal affine counting inequality of `ANF-005`. The theorem instead identifies an exact necessary-and-sufficient base-profile gate for the entire sufficiently narrow central-notch family.

## 7. Consequence for the next gate

`ANF-044`--`ANF-052` progressively reduced the unresolved two-pair problem to a compact balanced-height anti-phase coherence tube. The present result removes the notch itself from the next mathematical decision. There is no need to optimize a sequence of ever-narrower notched profiles first. One should decide the exact zero question

\[
\boxed{
H_{\rm MT}(y_1,y_2;t_1,t_2)=0,
\qquad y_1,y_2>0.
}
\tag{34}
\]

for the explicit Montgomery--Taylor profile.

A proof that (34) has no solution immediately transfers, by (3), to every sufficiently narrow notch and therefore clears the last cardinality-five gate for an explicit finite-real separator. A single genuine solution of (34) is equally decisive in the opposite direction: the signed cubic law turns it into an explicit negative witness for every narrow nontrivial central notch. The residual research problem is therefore no longer a perturbative sign estimate but the **exact zero geometry of one fixed, explicit Montgomery--Taylor defect**.