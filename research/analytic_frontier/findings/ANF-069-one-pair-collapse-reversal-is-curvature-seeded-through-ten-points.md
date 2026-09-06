# ANF-069 — one-pair collapse reversal is curvature-seeded through ten points

**Status:** `EXACT-DERIVED + ALL-ORDER-HEIGHT-EXPANSION + LARGER-CONFIGURATION-BOUNDARY + CURVATURE-COMPLETE-THROUGH-TEN-POINTS + MONTGOMERY-TAYLOR-HEIGHT-COMPACTIFICATION + STRUCTURAL-REDUCTION`. `ANF-067` shows that the Montgomery--Taylor real-collapse comparison first reverses infinitesimally at six points, while `ANF-068` proves that the resulting negative-second-variation class cannot consume the available affine slack in a sufficiently small-height neighborhood. That leaves open whether a genuinely new **finite-height** one-pair collapse reversal can appear independently of the curvature sign.

It cannot, and the reason is coefficientwise. For every nonzero continuous even compactly supported spectrum `J>=0`, one conjugate pair together with at most eight real anchors has an exact height expansion whose coefficients above quadratic order are nonnegative. Equivalently, through total cardinality ten, the normalized real-collapse defect

\[
y\longmapsto \frac{E_F(W_y)-E_F(R(W_y))}{y^2}
\]

is strictly increasing for every fixed horizontal configuration. Therefore a one-pair real-collapse reversal occurs at some positive height **if and only if its quadratic curvature coefficient is already negative**. When it is negative there is exactly one positive crossing height: collapse reversal holds below that height and fails above it.

For the Montgomery--Taylor six-point geometry of `ANF-067`, this gives a certified global height restriction. Every one-pair/four-anchor collapse reversal satisfies

\[
\boxed{y<0.267431<0.268.}
\]

Thus the finite-height part of the six-point frontier is not a second collapse mechanism. It is the continuation of the same curvature-seeded descent found in `ANF-067`. A six-point affine obstruction may still occur because that descent could consume the real-collapse affine margin, or because the notch perturbation changes the affine balance, but it cannot be produced by a new higher-height sign reversal with nonnegative second variation.

## 1. Exact all-order expansion for one pair and `m` real anchors

Let

\[
F(z)=\widehat J(z)
=\int_{-B}^{B}J(\alpha)e^{-2\pi i\alpha z}\,d\alpha,
\qquad J\ge0,
\tag{1}
\]

with `J` nonzero, continuous, real, even and compactly supported. Put one conjugate pair at `+-iy` after translating its real center to zero, and let `t_1,...,t_m` be the real-anchor displacements. As in `ANF-037`, define

\[
W_y=\{iy,-iy,t_1,\ldots,t_m\},
\qquad
R(W_y)=\{0,0,t_1,\ldots,t_m\},
\tag{2}
\]

\[
L_y(t)
=\int J(\alpha)
\bigl(\cosh(2\pi\alpha y)-1\bigr)
\cos(2\pi\alpha t)\,d\alpha,
\tag{3}
\]

and

\[
A_y
=\int J(\alpha)
\bigl(\cosh^2(2\pi\alpha y)-1\bigr)
\,d\alpha.
\tag{4}
\]

Then

\[
E_F(W_y)-E_F(R(W_y))
=4Q_m(y;T),
\qquad
Q_m(y;T):=A_y+\sum_{j=1}^mL_y(t_j).
\tag{5}
\]

For `n>=1` introduce the even spectral moments

\[
M_n(t)
:=\int_{-B}^{B}\alpha^{2n}J(\alpha)
\cos(2\pi\alpha t)\,d\alpha.
\tag{6}
\]

Compact support makes the hyperbolic-cosine series entire and permits termwise integration. Using

\[
\cosh^2u-1=\frac{\cosh(2u)-1}{2},
\tag{7}
\]

one obtains the exact expansion

\[
\boxed{
Q_m(y;T)
=
\sum_{n=1}^{\infty}
\frac{(2\pi y)^{2n}}{(2n)!}
\left[
2^{2n-1}M_n(0)
+\sum_{j=1}^mM_n(t_j)
\right].
}
\tag{8}
\]

The `n=1` bracket is exactly the curvature coefficient from `ANF-037` and `ANF-067`,

\[
\boxed{
D_m(T)
:=2K(0)+\sum_{j=1}^mK(t_j),
\qquad K=M_1.
}
\tag{9}
\]

No Montgomery--Taylor-specific fact has entered yet.

## 2. Spectral positivity makes every higher coefficient nonnegative through ten points

Because `J>=0`,

\[
|M_n(t)|\le M_n(0)
\qquad(n\ge1,\ t\in\mathbb R).
\tag{10}
\]

Hence the order-`2n` bracket in (8) obeys

\[
\boxed{
2^{2n-1}M_n(0)+\sum_{j=1}^mM_n(t_j)
\ge
\bigl(2^{2n-1}-m\bigr)M_n(0).
}
\tag{11}
\]

If `m<=8`, then for every `n>=2`,

\[
2^{2n-1}-m\ge8-m\ge0.
\tag{12}
\]

Moreover for every `m<=8`, the `n=3` coefficient is strictly positive because

\[
2^5-m\ge24
\tag{13}
\]

and `M_3(0)>0` for every nonzero continuous `J>=0`. Thus all orders above the quadratic one are nonnegative, with at least one strictly positive higher coefficient.

Put `r=y^2`. Dividing (8) by `r` gives

\[
\boxed{
\frac{Q_m(\sqrt r;T)}{r}
=
2\pi^2D_m(T)
+
\sum_{n=2}^{\infty}
\frac{(2\pi)^{2n}}{(2n)!}
B_n(T)r^{n-1},
}
\tag{14}
\]

where every `B_n(T)>=0` for `m<=8`, and `B_3(T)>0`. Therefore the right side is **strictly increasing** for `r>0` and tends to `+infinity` as `r->infinity`.

This proves the complete sign classification:

\[
\boxed{
D_m(T)\ge0
\quad\Longrightarrow\quad
Q_m(y;T)>0
\quad\text{for every }y>0,
}
\tag{15}
\]

while

\[
\boxed{
D_m(T)<0
\quad\Longrightarrow\quad
\exists!\,y_c(T)>0:
\begin{cases}
Q_m(y;T)<0,&0<y<y_c(T),\\
Q_m(y_c(T);T)=0,\\
Q_m(y;T)>0,&y>y_c(T).
\end{cases}
}
\tag{16}
\]

Consequently, for every one-pair configuration with at most eight real anchors,

\[
\boxed{
\exists y>0:\ E_F(W_y)<E_F(R(W_y))
\quad\Longleftrightarrow\quad
D_m(T)<0.
}
\tag{17}
\]

The infinitesimal curvature test is therefore not merely necessary near height zero; it is **complete for the existence of any finite-height collapse reversal** through total cardinality `m+2<=10`.

The coefficientwise protection first stops being automatic at nine real anchors, total cardinality eleven. At `m=9`, the quartic lower bound in (11) becomes `-M_2(0)`. This does not prove a curvature-independent eleven-point reversal; it identifies the first cardinality at which spectral positivity alone no longer forbids such a higher-order mechanism.

## 3. A quartic floor compactifies every six-point Montgomery--Taylor reversal in height

For `m<=7`, the `n=2` instance of (11) gives the quantitative lower bound

\[
B_2(T)\ge(8-m)M_2(0).
\tag{18}
\]

Keeping only the quadratic and quartic terms in (8),

\[
\boxed{
Q_m(y;T)
\ge
2\pi^2D_m(T)y^2
+
\frac23\pi^4(8-m)M_2(0)y^4.
}
\tag{19}
\]

Hence any collapse reversal with `D_m(T)<0` must satisfy

\[
\boxed{
y^2<
-\frac{3D_m(T)}{\pi^2(8-m)M_2(0)}.
}
\tag{20}
\]

Specialize now to the Montgomery--Taylor profile and four real anchors. Write

\[
D(T)=2K_0+\sum_{j=1}^4K(t_j),
\qquad
D_*:=2K_0+4k_*.
\tag{21}
\]

Since `K(t)>=k_*`, every horizontal configuration satisfies `D(T)>=D_*`. The already-canonical interval inputs give

\[
K_0>0.1549985926411760,
\tag{22}
\]

from `ANF-059`, and

\[
k_*>-0.091274161151487458117
\tag{23}
\]

from `ANF-066`. Therefore

\[
\boxed{D_*>-0.055099459323598.}
\tag{24}
\]

For the quartic moment, `ANF-038` writes

\[
M_2(0)
=\int_{-1}^{1}\alpha^4J_{\rm MT}(\alpha)\,d\alpha
=W_2
=
\frac{31-19\cos\sqrt2-20\sqrt2\sin\sqrt2}
{2(1-\cos\sqrt2)}.
\tag{25}
\]

Substitution of the outward enclosures already displayed in that finding gives

\[
\boxed{M_2(0)>0.05854458579969.}
\tag{26}
\]

Using `pi>3.14159265358`, equations (20), (24), and (26) imply that every Montgomery--Taylor one-pair/four-anchor collapse reversal satisfies

\[
 y^2<0.071519113,
\qquad
\boxed{y<0.267431.}
\tag{27}
\]

No search over height is involved. The bound is an exact consequence of spectral positivity plus the previously certified curvature minimum and exact fourth moment.

## 4. What this changes in the six-point frontier

`ANF-067` found the sign change by inspecting only the quadratic coefficient, so it left logically open the possibility that a different six-point horizontal geometry might have nonnegative curvature but become collapse-reversing later at finite height. Equations (15)--(17) remove that possibility completely. In the one-pair/four-anchor category, **every** finite-height reversal is the continuation of a negative Montgomery--Taylor second variation.

This sharpens the interpretation of `ANF-068`. Its small-height screening did not merely eliminate one local rational witness. It screened the germ of the only possible collapse-reversal branch. What remains is quantitative rather than topological: determine whether the curvature-seeded branch can ever descend far enough, before its unique crossing below `y=0.267431`, to consume the affine slack of the real collapse or of a sufficiently small central-notch perturbation.

The same theorem also prevents wasted work at the next few one-pair cardinalities. Adding real anchors up through eight anchors may make the curvature coefficient more negative, but it does not create an independent finite-height instability. A genuinely new higher-height one-pair mechanism can first become possible, by this coefficient budget, only from nine real anchors onward.

## 5. The remaining six-point affine question reduces to a one-dimensional profile tradeoff

There is a useful profile-specific reduction for the base Montgomery--Taylor six-point layer. Define the curvature deficit below the `ANF-059` exterior threshold by

\[
r(t):=\left(-\frac{K_0}{3}-K(t)\right)_+.
\tag{28}
\]

Suppose one can certify a constant `c>0` such that

\[
\boxed{F_{\rm MT}(t)\ge c\,r(t)\qquad(t\in\mathbb R).}
\tag{29}
\]

For four anchors with `D(T)<0`, write `e(t)=(K(t)+K_0/3)_+`. The identity

\[
K(t)=-\frac{K_0}{3}-r(t)+e(t)
\]

gives

\[
\sum_{j=1}^4r(t_j)
=\frac{2K_0}{3}+\sum_{j=1}^4e(t_j)-D(T)
\ge\frac{2K_0}{3}-D(T).
\tag{30}
\]

The collapsed Montgomery--Taylor six-point affine slack from `ANF-068` is

\[
\mathcal S_{\rm MT}(R_T)
=4\sum_jF_{\rm MT}(t_j)
+2\sum_{j<k}F_{\rm MT}(t_j-t_k).
\tag{31}
\]

Since `F_MT>=0`, (29)--(30) imply

\[
\mathcal S_{\rm MT}(R_T)
\ge4c\left(\frac{2K_0}{3}-D(T)\right).
\tag{32}
\]

Meanwhile minimizing the quadratic-plus-quartic floor (19) for `m=4` over all heights yields

\[
4Q_4(y;T)
\ge-\frac{3D(T)^2}{2M_2(0)}.
\tag{33}
\]

Therefore the full six-point slack on the entire collapse-reversing branch obeys

\[
\boxed{
\mathcal S_{\rm MT}(W_{y,T})
\ge
4c\left(\frac{2K_0}{3}-D(T)\right)
-
\frac{3D(T)^2}{2M_2(0)}.
}
\tag{34}
\]

As `D(T)` ranges over `[D_*,0)`, a sufficient condition for the right side to remain positive is

\[
c>
\frac{3D_*^2}
{8M_2(0)(2K_0/3-D_*)}.
\tag{35}
\]

Using `2K_0/3-D_*=4(-K_0/3-k_*)=4\Delta`, together with the certified `Delta>0.0396079636044282` from `ANF-066` and (24), (26), gives the explicit sufficient threshold

\[
\boxed{c>0.122743.}
\tag{36}
\]

Thus the clean one-dimensional inequality

\[
\boxed{
F_{\rm MT}(t)
\ge
\frac18\left(-\frac{K_0}{3}-K(t)\right)_+
\qquad(t\in\mathbb R)
}
\tag{37}
\]

would, if certified, screen the **entire** Montgomery--Taylor one-pair six-point collapse-reversal branch with a fixed positive affine margin. `ANF-059` already confines the positive part on the right side to `0.545<|t|<1.01`, and `ANF-030` gives both `F_MT` and `K` in explicit rational-trigonometric form. The remaining test (37) is therefore one-dimensional and compact.

Equation (37) is a proposed decisive gate, not a claim of this finding. No sampled evaluation of its ratio is treated as evidence.

## 6. Prior art, stress test, and evidence boundary

A fresh literature check revisited Buescu--Paixão--Symeonides on holomorphic positive-definite strip functions and the current Montgomery--Taylor / Lamzouri pair-correlation framework. The former supplies the classical Fourier--Laplace representation underlying (1), while the latter supplies the number-theoretic setting and extremal profile. No source located in the targeted search states the finite-anchor coefficient threshold (11)--(17), the ten-point curvature completeness, or the Montgomery--Taylor height bound (27). No publication-level novelty claim is made. All relevant external frameworks are already anchored in `SOURCES.md`, so no source-file change is required.

The all-order theorem is exact and does not use the computer-assisted Montgomery--Taylor certificates. Its audit points are only the factor `2^(2n-1)` in the expansion of `cosh^2u-1`, the elementary characteristic-function bound `|M_n(t)|<=M_n(0)`, and the anchor count `m<=8`. A missing factor in (8) would change the cardinality threshold immediately, so (7)--(8) are the primary algebraic check.

The numerical constant in (27) has a different evidence tier: it uses only outward-certified intervals already canonical in `ANF-038`, `ANF-059`, and `ANF-066`, followed by monotone rational arithmetic. Ordinary floating-point optimization is not used. The inequality (37) remains unproved and is explicitly excluded from the finding's evidence.

Finally, this result concerns **real-collapse energy** for one conjugate pair. It does not prove the universal affine inequality, does not control configurations with two or more nonreal fibers, and does not show that a central-notch perturbation survives six points. Its structural conclusion is narrower: through ten total points, one-pair finite-height collapse reversal contains no hidden instability beyond the quadratic curvature sign. For the current six-point program, the next useful work is therefore the profile tradeoff (37) or an equivalent direct affine-margin comparison, not an unconstrained search for a curvature-independent finite-height reversal.
