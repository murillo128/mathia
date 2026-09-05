# ANF-044 — two-pair five-point negative defects compactify after the curvature gate

**Status:** `EXACT-DERIVED + UNIFORM-HORIZONTAL-ESCAPE-BARRIER + FULL-FIVE-POINT-COMPACTNESS + STRUCTURAL-BOUNDARY`. `ANF-043` proves that the last genuinely coupled cardinality-five geometry, two conjugate pairs plus one real point, cannot produce a negative collapse defect at arbitrarily small or large heights once the curvature gate `m_5(J)` is nonnegative. It deliberately leaves the horizontal variables noncompact. The present finding closes that escape route: on every compact interior height slab, the defect is uniformly positive when the horizontal geometry escapes to infinity. Consequently, after the curvature gate, **every negative two-pair five-point defect is confined to a compact four-dimensional box and any negative global minimum is attained by a finite genuine configuration**.

Let

\[
F(z)=\widehat J(z)
=\int_{-B}^{B}J(\alpha)e^{-2\pi i\alpha z}\,d\alpha,
\qquad J\ge0,
\tag{1}
\]

where `J` is nonzero, continuous, even and compactly supported. Retain the `ANF-040` configuration

\[
W=\{x_1\pm iy_1,x_2\pm iy_2,r\},
\qquad
R(W)=\{x_1,x_1,x_2,x_2,r\},
\qquad y_1,y_2>0,
\tag{2}
\]

and use translation invariance to write

\[
t_j=x_j-r,
\qquad d=t_1-t_2.
\tag{3}
\]

With

\[
c_y(\alpha)=\cosh(2\pi\alpha y),
\tag{4}
\]

\[
A_y=\int J(\alpha)(c_y(\alpha)^2-1)\,d\alpha,
\tag{5}
\]

\[
L_y(t)=\int J(\alpha)(c_y(\alpha)-1)
\cos(2\pi\alpha t)\,d\alpha,
\tag{6}
\]

and

\[
M_{y_1,y_2}(t)
=\int J(\alpha)
\bigl(c_{y_1}(\alpha)c_{y_2}(\alpha)-1\bigr)
\cos(2\pi\alpha t)\,d\alpha,
\tag{7}
\]

`ANF-040` gives

\[
E_F(W)-E_F(R(W))=4H_J(y_1,y_2;t_1,t_2),
\tag{8}
\]

where

\[
H_J
=A_{y_1}+A_{y_2}
+2M_{y_1,y_2}(d)
+L_{y_1}(t_1)+L_{y_2}(t_2).
\tag{9}
\]

The new horizontal statement is the following. For every fixed interior height slab

\[
0<\varepsilon\le y_1,y_2\le Y<\infty,
\tag{10}
\]

there exist constants `T_0<infinity` and `delta>0`, depending only on `J,epsilon,Y`, such that

\[
\boxed{
\max(|t_1|,|t_2|)\ge T_0
\quad\Longrightarrow\quad
H_J(y_1,y_2;t_1,t_2)\ge\delta.
}
\tag{11}
\]

Equivalently,

\[
\boxed{
\liminf_{T\to\infty}
\inf_{\substack{\varepsilon\le y_1,y_2\le Y\\
\max(|t_1|,|t_2|)\ge T}}
H_J(y_1,y_2;t_1,t_2)>0.
}
\tag{12}
\]

The proof has two different horizontal escape regimes. If the two pair centers separate from one another, the mixed transform `M` decays and each pair retains a strictly positive self-plus-anchor margin. If instead the two centers translate to infinity together with bounded separation, both anchor transforms `L` decay and the remaining two-pair block has a strictly positive compact minimum.

## 1. Compact height families have uniform Fourier decay

The only analytic compactness input is a uniform form of the Riemann--Lebesgue lemma that follows directly from the ordinary theorem.

Let `C` be a compact subset of `L^1(R)`. Then

\[
\boxed{
\sup_{f\in C}|\widehat f(t)|\longrightarrow0
\qquad(|t|\to\infty).
}
\tag{13}
\]

Indeed, given `eta>0`, choose a finite `eta`-net `f_1,...,f_N` for `C` in `L^1`. Ordinary Riemann--Lebesgue gives a common `T` such that `|widehat f_k(t)|<eta` for every `k` whenever `|t|>T`. If `||f-f_k||_1<eta`, then

\[
|\widehat f(t)|
\le |\widehat f_k(t)|+\|f-f_k\|_1
<2\eta.
\tag{14}
\]

For a fixed slab (10), the maps

\[
y\longmapsto
J(\alpha)(c_y(\alpha)-1)
\tag{15}
\]

and

\[
(y_1,y_2)\longmapsto
J(\alpha)
\bigl(c_{y_1}(\alpha)c_{y_2}(\alpha)-1\bigr)
\tag{16}
\]

are continuous from compact parameter sets into `L^1`: the spectral support is compact, and all hyperbolic factors are uniformly bounded on `|alpha|<=B`, `y_j<=Y`. Their images are therefore compact in `L^1`. Applying (13) yields

\[
\boxed{
\sup_{\varepsilon\le y\le Y}|L_y(t)|\to0
\qquad(|t|\to\infty),
}
\tag{17}
\]

and

\[
\boxed{
\sup_{\varepsilon\le y_1,y_2\le Y}
|M_{y_1,y_2}(t)|\to0
\qquad(|t|\to\infty).
}
\tag{18}
\]

This is exactly the uniformity needed below. No quantitative decay rate is asserted; continuity and compact support of `J` are sufficient for the qualitative escape barrier.

## 2. Large relative separation is uniformly safe

Group one self term with its real-anchor interaction:

\[
D_y(t):=A_y+L_y(t).
\tag{19}
\]

Using (5)--(6),

\[
D_y(t)
=\int J(\alpha)(c_y-1)
\bigl(c_y+1+\cos(2\pi\alpha t)\bigr)\,d\alpha.
\tag{20}
\]

Since `1+cos(theta)>=0`,

\[
D_y(t)
\ge
\int J(\alpha)(c_y-1)c_y\,d\alpha.
\tag{21}
\]

For `y>=epsilon`, the right side is bounded below by

\[
\boxed{
d_*
:=\int J(\alpha)
(c_\varepsilon(\alpha)-1)c_\varepsilon(\alpha)\,d\alpha>0.
}
\tag{22}
\]

Strict positivity follows because a nonzero continuous `J>=0` is positive on an interval of positive length, while `(c_epsilon-1)c_epsilon>0` at every nonzero frequency.

Equation (9) may now be written

\[
H_J
=D_{y_1}(t_1)+D_{y_2}(t_2)
+2M_{y_1,y_2}(d).
\tag{23}
\]

By the uniform decay (18), choose `D_0` so that

\[
|d|\ge D_0
\quad\Longrightarrow\quad
|M_{y_1,y_2}(d)|\le\frac{d_*}{2}
\tag{24}
\]

throughout the slab. Then

\[
\boxed{
|t_1-t_2|\ge D_0
\quad\Longrightarrow\quad
H_J\ge d_*>0.
}
\tag{25}
\]

Thus horizontally separating the two conjugate-pair centers cannot create an asymptotic obstruction. The positive self-plus-anchor margin survives uniformly, while the interaction between the two distant centers vanishes.

## 3. A bounded-separation pair block has a strict positive floor

It remains to consider

\[
|d|\le D_0.
\tag{26}
\]

Remove the two real-anchor transforms and define the residual two-pair block

\[
B_J(y_1,y_2;d)
:=A_{y_1}+A_{y_2}+2M_{y_1,y_2}(d).
\tag{27}
\]

At each frequency write `c_j=c_{y_j}(alpha)`. A direct rearrangement gives the exact nonnegative decomposition

\[
\boxed{
\begin{aligned}
B_J(y_1,y_2;d)
=\int J(\alpha)\Bigl[&
(c_1-c_2)^2\\
&+2(c_1c_2-1)
\bigl(1+\cos(2\pi\alpha d)\bigr)
\Bigr]d\alpha.
\end{aligned}
}
\tag{28}
\]

Both terms are pointwise nonnegative. More is true: for positive heights the integral is **strictly** positive.

If `y_1!=y_2`, then `c_1!=c_2` at every nonzero frequency, so the first term is positive on a positive-measure subset where `J>0`. If `y_1=y_2>0`, the first term vanishes, but `c_1c_2-1>0` at nonzero frequencies. Vanishing of the second term throughout an interval where `J>0` would require

\[
\cos(2\pi\alpha d)=-1
\tag{29}
\]

throughout that interval, which is impossible for a cosine of a linear phase. Hence

\[
B_J(y_1,y_2;d)>0
\qquad(y_1,y_2>0).
\tag{30}
\]

The map in (27) is continuous in all three parameters. Therefore, on the compact set

\[
[\varepsilon,Y]^2\times[-D_0,D_0]
\]

it has a strict positive minimum

\[
\boxed{
b_*
:=\min B_J(y_1,y_2;d)>0.
}
\tag{31}
\]

Now suppose the two centers escape to horizontal infinity while retaining bounded relative separation. If

\[
\max(|t_1|,|t_2|)\ge T,
\qquad |t_1-t_2|\le D_0,
\tag{32}
\]

then

\[
\min(|t_1|,|t_2|)\ge T-D_0.
\tag{33}
\]

Using the uniform decay (17), choose `T` sufficiently large that

\[
|L_{y_1}(t_1)|+|L_{y_2}(t_2)|\le\frac{b_*}{2}
\tag{34}
\]

whenever (32) holds. Equations (9), (27), and (31) then give

\[
\boxed{
H_J\ge\frac{b_*}{2}>0.
}
\tag{35}
\]

This is the second escape regime: if both conjugate-pair centers move away from the real anchor together, the anchor interactions disappear, leaving a strictly positive two-pair block.

## 4. Horizontal escape has a uniform positive barrier

Sections 2 and 3 exhaust all horizontal geometries. Either `|d|>=D_0`, when (25) applies, or `|d|<=D_0`, when any sufficiently large `max(|t_1|,|t_2|)` is covered by (35). Taking

\[
\delta:=\min\left(d_*,\frac{b_*}{2}\right)>0
\tag{36}
\]

and increasing `T_0` if necessary proves (11)--(12).

The role of the interior height slab is essential. The constant `d_*` in (22) tends to zero with `epsilon`, so this argument by itself does not replace the small-height curvature analysis of `ANF-040`--`ANF-043`. Likewise the upper height bound is what makes the parameterized `L^1` families compact and gives uniform Fourier decay; the large-height regime is instead controlled by the exponential coercivity theorem of `ANF-043`.

Thus the vertical and horizontal arguments are complementary rather than redundant:

\[
\text{curvature near height }0
\quad+\quad
\text{height coercivity at infinity}
\quad+\quad
\text{horizontal escape barrier on slabs}
\]

eliminate every noncompact direction of the two-pair five-point gate.

## 5. After the curvature gate, every negative defect lies in a compact box

Assume now

\[
m_5(J)
=2K_J(0)+3\inf_tK_J(t)\ge0,
\tag{37}
\]

with `K_J` as in `ANF-037`--`ANF-043`. `ANF-043` gives constants

\[
0<\varepsilon_J<Y_J<\infty
\tag{38}
\]

such that

\[
H_J(y_1,y_2;t_1,t_2)<0
\quad\Longrightarrow\quad
\varepsilon_J\le y_1,y_2\le Y_J.
\tag{39}
\]

Apply the horizontal theorem (11) to this exact slab. There is then a finite `T_J` such that

\[
\boxed{
H_J(y_1,y_2;t_1,t_2)<0
\quad\Longrightarrow\quad
\begin{cases}
\varepsilon_J\le y_1,y_2\le Y_J,\\
|t_1|\le T_J,\\
|t_2|\le T_J.
\end{cases}
}
\tag{40}
\]

This is the full compactification statement. After fixing the real anchor by translation, every remaining negative cardinality-five configuration lies in the compact box

\[
\boxed{
\mathcal K_J
=[\varepsilon_J,Y_J]^2
\times[-T_J,T_J]^2.
}
\tag{41}
\]

Since `H_J` is continuous, a useful attainment consequence follows. If

\[
\inf_{y_1,y_2>0\atop t_1,t_2\in\mathbb R}H_J<0,
\tag{42}
\]

then every sufficiently minimizing sequence is eventually negative and hence eventually lies in `K_J`. Compactness produces a convergent subsequence, so

\[
\boxed{
\inf H_J<0
\quad\Longrightarrow\quad
\text{the negative global minimum is attained in }\mathcal K_J.
}
\tag{43}
\]

Conversely, proving `H_J>=0` on one such compact obstruction box is enough to rule out every two-pair five-point reversal globally. What was an optimization over an unbounded four-dimensional domain has therefore become a finite-domain sign problem once the already-established curvature gate is passed.

## 6. Consequence for Montgomery--Taylor and the central-notch separator

`ANF-038` proves

\[
m_5(J_{\rm MT})>0.0078,
\tag{44}
\]

and gives compatible central-notch separators `J_s` from `ANF-034` with

\[
m_5(J_s)>0.0003.
\tag{45}
\]

Both profiles therefore satisfy the full compactification (40). For the notch this sharpens the current frontier substantially. `ANF-034` gives strict separation over every finite real configuration; `ANF-039` proves that one conjugate pair plus three real points is harmless at every height; `ANF-041` clears the two-pair geometry near the real axis; `ANF-043` clears sufficiently large heights. The present finding also clears horizontal infinity.

Hence, **if a cardinality-five complex configuration kills a compatible central-notch separator, there is an actual finite minimizer with two positive finite heights and three finite horizontal centers**. There is no remaining five-point obstruction hiding at a limit of vanishing height, infinite height, infinite pair separation, or common horizontal translation relative to the real anchor.

This does not yet establish the universal affine scalar certificate. The compact box may still contain a genuine finite-height reversal, and configurations of cardinality six or larger remain outside the present reduction. But the remaining five-point question is now suitable for a bounded analytic or rigorously certified computational attack without interpreting boundary drift as a separate mechanism.

## 7. Prior art, falsification, and evidence boundary

The Fourier--Laplace representation for positive-definite strip functions remains the external framework already anchored in `SOURCES.md` through Buescu--Paixão--Symeonides. The only additional generic fact used here is the classical Riemann--Lebesgue lemma. Its needed uniform-on-compact-`L^1` version is proved directly in (13)--(14), so no new source entry is load-bearing. A targeted check of Fourier-analysis and positive-definite-strip literature found the expected uniform Riemann--Lebesgue compactness principle but no theorem needed for the particular five-point compactification above. No publication-level novelty claim is made.

The result depends materially on the regularity class already used in this branch. Continuity and nontriviality of `J` supply positive spectral mass on an interval and hence the strict floors (22) and (31). Compact spectral support and bounded heights supply the `L^1` compactness behind (17)--(18). The argument should not be silently extended to arbitrary positive atomic spectral measures: a discrete spectrum need not have Riemann--Lebesgue decay, and exact anti-phase support can change the strictness argument.

The horizontal theorem also does not imply pointwise positivity. `ANF-042` already proves that individual nonzero frequencies can have negative defect whenever their amplitude mismatch lies in the danger band. The present claim is only that such negativity cannot remain competitive while the physical horizontal geometry escapes to infinity on a fixed height slab.

The decisive next test is therefore genuinely finite. Choose an explicit central-notch profile satisfying the finite-real separation and positive-curvature margins already certified in `ANF-034` and `ANF-038`; make the constants in `ANF-043` and the present proof explicit enough to enclose `K_J`; then either prove `H_J>=0` on that compact domain or exhibit a certified interior point with `H_J<0`. Either outcome would resolve the complete cardinality-five layer for that separator rather than merely another asymptotic regime.