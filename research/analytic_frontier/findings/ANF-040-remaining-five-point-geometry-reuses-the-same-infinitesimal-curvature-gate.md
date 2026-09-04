# ANF-040 — the remaining five-point geometry reuses the same infinitesimal curvature gate

**Status:** `EXACT-DERIVED + FIVE-POINT-COMPLEX-REDUCTION + SHARP-INFINITESIMAL-GATE + STRUCTURAL-BOUNDARY`. `ANF-039` closes, at every height, the five-point geometry consisting of one conjugate pair and three real anchors whenever the curvature margin

\[
m_5(J):=2K_J(0)+3\inf_{t\in\mathbb R}K_J(t),
\qquad
K_J(t):=\int_{-B}^{B}\alpha^2J(\alpha)\cos(2\pi\alpha t)\,d\alpha
\]

is nonnegative. The only genuinely coupled cardinality-five geometry left there is two conjugate pairs plus one real point. Its exact defect is two-dimensional rather than the one-dimensional Fourier minimum of `ANF-037`, but its infinitesimal boundary contains **no new quadratic obstruction**: the same `m_5(J)` controls every simultaneous small-height splitting.

Let

\[
F(z)=\widehat J(z)
=\int_{-B}^{B}J(\alpha)e^{-2\pi i\alpha z}\,d\alpha,
\qquad J\ge0,
\tag{1}
\]

with `J` real, even, continuous and compactly supported. Consider

\[
W
=\{x_1+iy_1,x_1-iy_1,x_2+iy_2,x_2-iy_2,r\},
\qquad y_1,y_2>0,
\tag{2}
\]

and its real-part collapse

\[
R(W)=\{x_1,x_1,x_2,x_2,r\}.
\tag{3}
\]

Put

\[
t_1:=x_1-r,
\qquad
t_2:=x_2-r,
\qquad
d:=t_1-t_2=x_1-x_2,
\tag{4}
\]

and retain from `ANF-037`

\[
c_y(\alpha):=\cosh(2\pi\alpha y),
\tag{5}
\]

\[
A_y:=\int J(\alpha)(c_y(\alpha)^2-1)\,d\alpha,
\tag{6}
\]

\[
L_y(t):=\int J(\alpha)(c_y(\alpha)-1)
\cos(2\pi\alpha t)\,d\alpha.
\tag{7}
\]

The new coupled transform is

\[
\boxed{
M_{y_1,y_2}(t)
:=\int J(\alpha)
\bigl(c_{y_1}(\alpha)c_{y_2}(\alpha)-1\bigr)
\cos(2\pi\alpha t)\,d\alpha.
}
\tag{8}
\]

Then the complete energy defect is

\[
\boxed{
E_F(W)-E_F(R(W))
=4H_J(y_1,y_2;t_1,t_2),
}
\tag{9}
\]

where

\[
\boxed{
H_J
=A_{y_1}+A_{y_2}
+2M_{y_1,y_2}(t_1-t_2)
+L_{y_1}(t_1)+L_{y_2}(t_2).
}
\tag{10}
\]

Thus for fixed heights the remaining five-point collapse gate is exactly

\[
\boxed{
G_{2,2,1;J}(y_1,y_2)
:=\inf_{t_1,t_2\in\mathbb R}
H_J(y_1,y_2;t_1,t_2).
}
\tag{11}
\]

A negative value gives a genuine two-pair five-point energy reversal. If the three real centers `x_1,x_2,r` are pairwise distinct, `W` and `R(W)` have the same total cardinality and exactly the same simple-real-point count, namely one. Hence such a reversal is also a strictly stronger constraint at the universal affine-counting level.

## 1. Exact two-pair defect

Pair energy is translation invariant, so set `r=0`. At frequency `alpha` write

\[
z_j=e^{-2\pi i\alpha t_j},
\qquad
c_j=c_{y_j}(\alpha).
\]

The two structure factors are

\[
S_W=1+2c_1z_1+2c_2z_2,
\qquad
S_{R(W)}=1+2z_1+2z_2.
\tag{12}
\]

A direct expansion gives

\[
\begin{aligned}
\frac{|S_W|^2-|S_{R(W)}|^2}{4}
={}&(c_1^2-1)+(c_2^2-1)\\
&+2(c_1c_2-1)\cos(2\pi\alpha(t_1-t_2))\\
&+(c_1-1)\cos(2\pi\alpha t_1)\\
&+(c_2-1)\cos(2\pi\alpha t_2).
\end{aligned}
\tag{13}
\]

Integrating against the nonnegative spectrum `J` proves (9)--(10).

The coupled term also has a direct Fourier--Laplace form. The identity

\[
\cosh u\cosh v
=\frac{\cosh(u+v)+\cosh(u-v)}2
\]

gives

\[
\boxed{
M_{y_1,y_2}(t)
=\frac12\Bigl(
\Re F(t+i(y_1+y_2))
+\Re F(t+i(y_1-y_2))
\Bigr)-F(t).
}
\tag{14}
\]

Equation (11) is therefore a completely explicit two-variable Fourier--Laplace minimization. If desired it can be written as nested one-dimensional minima by fixing `d=t_1-t_2` and minimizing `L_{y_1}(t)+L_{y_2}(t-d)` over `t`, but no further exact scalar collapse is asserted here.

## 2. The boundary axes reduce to the already-closed one-pair gate

The coupled formula has the correct degeneration. If `y_2=0`, then

\[
A_0=L_0=0,
\qquad
M_{y_1,0}=L_{y_1},
\]

so

\[
H_J(y_1,0;t_1,t_2)
=A_{y_1}
+2L_{y_1}(t_1-t_2)
+L_{y_1}(t_1).
\tag{15}
\]

Every `L_{y_1}` term is at least its global infimum. Hence

\[
\boxed{
H_J(y_1,0;t_1,t_2)
\ge A_{y_1}+3\inf_tL_{y_1}(t)
=G_J(y_1),
}
\tag{16}
\]

where `G_J` is exactly the one-pair-plus-three-real quantity of `ANF-037`--`ANF-039`. The same statement holds with the indices exchanged.

Therefore, whenever `m_5(J)>=0`, `ANF-039` implies

\[
H_J(y_1,0;t_1,t_2)\ge0,
\qquad
H_J(0,y_2;t_1,t_2)\ge0
\tag{17}
\]

for all horizontal positions and all heights. If `m_5(J)>0`, its quantitative bound gives strict positivity on either axis whenever the other height is nonzero. Thus the unresolved two-pair geometry is not hiding a new obstruction on a one-pair boundary face.

## 3. Uniform small-height expansion

The genuinely new question is whether coupling two positive heights creates a stricter instability immediately after leaving the real axis. It does not at quadratic order.

Compact spectral support makes the `cosh` Taylor expansions uniform under the integral and, because every oscillatory factor has absolute value at most one, uniform in `t_1,t_2`. As `y_1,y_2->0`,

\[
A_y
=4\pi^2y^2K_J(0)+O_J(y^4),
\tag{18}
\]

\[
L_y(t)
=2\pi^2y^2K_J(t)+O_J(y^4)
\quad\text{uniformly in }t,
\tag{19}
\]

and

\[
M_{y_1,y_2}(d)
=2\pi^2(y_1^2+y_2^2)K_J(d)
+O_J\bigl((y_1^2+y_2^2)^2\bigr)
\tag{20}
\]

uniformly in `d`. Substitution in (10) gives

\[
\boxed{
\begin{aligned}
H_J
={}&2\pi^2y_1^2
\bigl(2K_J(0)+2K_J(d)+K_J(t_1)\bigr)\\
&+2\pi^2y_2^2
\bigl(2K_J(0)+2K_J(d)+K_J(t_2)\bigr)\\
&+O_J\bigl((y_1^2+y_2^2)^2\bigr),
\end{aligned}
}
\tag{21}
\]

uniformly in the horizontal geometry.

Let

\[
k_*:=\inf_{t\in\mathbb R}K_J(t).
\]

Each quadratic bracket in (21) obeys

\[
2K_J(0)+2K_J(d)+K_J(t_j)
\ge2K_J(0)+3k_*
=m_5(J).
\tag{22}
\]

Consequently there is a finite constant `C_J` and a neighborhood of the origin such that, with

\[
r^2:=y_1^2+y_2^2,
\]

\[
\boxed{
H_J(y_1,y_2;t_1,t_2)
\ge2\pi^2m_5(J)r^2-C_Jr^4
}
\tag{23}
\]

uniformly in `t_1,t_2`.

This is the main structural point: **the remaining five-point geometry has no quadratic gate beyond `m_5(J)`**. The two independent vertical fibers share the same curvature threshold already forced by the one-pair geometry.

## 4. The strict curvature sign is sharp for the local two-pair problem

If

\[
m_5(J)>0,
\]

then (23) gives an `epsilon_J>0` such that

\[
\boxed{
G_{2,2,1;J}(y_1,y_2)>0
\qquad
\text{whenever }
0<y_1^2+y_2^2<\epsilon_J^2.
}
\tag{24}
\]

Thus every two-pair-plus-one-real five-point configuration sufficiently close to its real collapse is uniformly harmless, regardless of the horizontal positions.

The opposite strict sign is also sharp. Suppose `m_5(J)<0`. Given `delta>0`, choose real `p,q` with

\[
K_J(p)<k_*+\delta,
\qquad
K_J(q)<k_*+\delta.
\tag{25}
\]

Set

\[
d=p,
\qquad
t_1=q,
\qquad
t_2=q-p.
\tag{26}
\]

Then the coefficient multiplying `y_1^2` in (21) is less than

\[
m_5(J)+3\delta.
\tag{27}
\]

Choose `delta` small enough that this is negative, and take for example

\[
y_1=\varepsilon,
\qquad
y_2=\varepsilon^2.
\tag{28}
\]

Both conjugate pairs remain genuinely nonreal, while (21) gives

\[
\frac{H_J(\varepsilon,\varepsilon^2;q,q-p)}{2\pi^2\varepsilon^2}
\longrightarrow
2K_J(0)+2K_J(p)+K_J(q)<0.
\tag{29}
\]

Hence every neighborhood of the real-height origin contains a genuine two-pair five-point energy reversal.

The equality case `m_5(J)=0` is deliberately left open. Unlike the one-pair geometry in `ANF-039`, mixed quartic terms from `cosh(2\pi\alpha y_1)\cosh(2\pi\alpha y_2)` need not have an individually favorable sign after horizontal interference. Therefore the exact all-height equivalence of `ANF-039` must **not** be imported into the two-pair problem merely from the shared quadratic threshold.

## 5. Consequence for Montgomery--Taylor and the central-notch survivor

`ANF-038` proves the rigorous margin

\[
m_5(J_{\rm MT})>0.0078.
\tag{30}
\]

Therefore (24) supplies a uniform neighborhood of the real axis in which **every** remaining two-pair-plus-one-real five-point configuration is collapse-dominated for the exact Montgomery--Taylor spectrum.

More importantly, for the central-notch separator

\[
J_s=J_{\rm MT}-s\phi_\eta
\]

of `ANF-034`, `ANF-038` proves that the compatible choice

\[
s\eta^3<0.009
\]

gives

\[
m_5(J_s)>0.0003.
\tag{31}
\]

Hence that same separator can simultaneously retain its strict finite-real gain, pass the complete one-pair-plus-three-real layer at **all heights** by `ANF-039`, and pass the remaining two-pair-plus-one-real geometry throughout a uniform simultaneous small-height neighborhood by (24).

Combining `ANF-036`, `ANF-039`, and the present result, all genuinely complex cardinality-five geometries are therefore harmless sufficiently close to the real axis for such a chosen notch. Any five-point obstruction that still kills the notch must come from the two-pair-plus-one-real pattern at genuinely non-infinitesimal joint height; it cannot be forced by an immediate simultaneous complex splitting.

This does not yet prove the universal affine scalar certificate. A finite-height two-pair reversal may still exist, and larger coupled multisets remain outside the five-point analysis.

## 6. Prior art and evidence boundary

The only external analytic framework used here is the positive Fourier--Laplace representation already anchored in `SOURCES.md` through Buescu--Paixão--Symeonides and used by `ANF-012` and `ANF-035`--`ANF-039`. A targeted prior-art check found the classical representation of holomorphic positive-definite strip functions as Fourier--Laplace transforms of positive exponentially finite measures, but no separate result is required for the finite five-point identity (13) or the curvature reduction (21)--(23). No publication-level novelty claim is made.

No new source entry is needed. Equations (9)--(14) are finite algebra; equations (18)--(23) use only compact support, `J>=0`, and uniform Taylor remainder bounds. The strict-negative construction (25)--(29) uses the definition of `inf K_J` and an asymmetric positive-height approach, not attainment of the infimum.

The theorem does **not** show `G_{2,2,1;J}(y_1,y_2)>=0` for all heights when `m_5(J)>=0`. In particular the mixed higher-order terms prevent the coefficient argument of `ANF-039` from being reused without a new proof. It also does not address larger complex multisets or the full normalization slack of `ANF-005`.

## 7. Next decisive test

The entire complex cardinality-five question for a fixed positive spectrum is now explicit. The unresolved quantity is

\[
\boxed{
\inf_{y_1,y_2>0}
G_{2,2,1;J}(y_1,y_2)
}
\tag{32}
\]

with `G_{2,2,1;J}` defined by (10)--(11). For the central-notch ray there is no reason to search the simultaneous small-height region after (24), and the axes reduce to `ANF-039` by (16). The cheapest next step is therefore to exploit the actual Montgomery--Taylor/notch spectral shape to derive a finite-height lower bound for (10), or else produce a certified two-pair witness with negative defect and compare its affine cost against the strict finite-real gain of `ANF-034`.

If the two-pair gate can also be proved nonnegative for the chosen notch, then every complex constraint of total cardinality at most five reduces to the already-surviving real/multiplicity envelope. If it fails, (10) gives the exact first unresolved complex mechanism rather than a generic high-dimensional search.