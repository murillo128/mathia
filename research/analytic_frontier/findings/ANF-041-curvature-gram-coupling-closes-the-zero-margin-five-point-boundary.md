# ANF-041 — curvature Gram coupling closes the zero-margin five-point boundary

**Status:** `EXACT-DERIVED + POSITIVE-DEFINITE-GRAM + FIVE-POINT-COMPLEX-LOCAL-CLOSURE + SHARP-EQUALITY-BOUNDARY`. `ANF-040` reduces the last genuinely coupled cardinality-five geometry to two conjugate pairs plus one real point and proves that the curvature margin

\[
m_5(J):=2K_J(0)+3\inf_{t\in\mathbb R}K_J(t),
\qquad
K_J(t):=\int_{-B}^{B}\alpha^2J(\alpha)\cos(2\pi\alpha t)\,d\alpha
\tag{1}
\]

is sharp when its sign is strict: `m_5(J)>0` gives a uniform small-height collapse neighborhood, while `m_5(J)<0` produces genuine two-pair reversals arbitrarily close to the real axis. The equality case was left open because the mixed quartic term need not have a favorable sign by itself.

That boundary is nevertheless stable. Let `J` be a nonzero continuous even nonnegative function with compact support, and let `H_J(y_1,y_2;t_1,t_2)` be the exact two-pair defect of `ANF-040`, so that

\[
E_F(W)-E_F(R(W))=4H_J
\tag{2}
\]

for

\[
W=\{x_1\pm iy_1,x_2\pm iy_2,r\},
\qquad
t_j=x_j-r.
\]

Then

\[
\boxed{
m_5(J)\ge0
\quad\Longleftrightarrow\quad
\exists\,\varepsilon_J>0:\
H_J(y_1,y_2;t_1,t_2)>0
}
\tag{3}
\]

for every `t_1,t_2 in R` and every genuinely two-pair split `y_1,y_2>0` with `y_1^2+y_2^2<\varepsilon_J^2`, with the reverse implication understood in the local-nonnegativity sense: if `m_5(J)<0`, every neighborhood contains a negative defect. Equivalently,

\[
\boxed{
m_5(J)\ge0
\iff
G_{2,2,1;J}(y_1,y_2)\ge0
\text{ throughout some punctured neighborhood of }(0,0),
}
\tag{4}
\]

where `G_{2,2,1;J}=\inf_{t_1,t_2}H_J` as in `ANF-040`.

The new ingredient is not another Taylor coefficient. Because `\alpha^2J(\alpha)\,d\alpha` is a positive measure, the curvature kernel `K_J` is positive definite. Its **three-point Gram constraint couples the two quadratic brackets** that `ANF-040` bounded independently. At the borderline `m_5(J)=0`, this coupling forces a definite quadratic penalty whenever both heights have comparable size; if one height becomes asymptotically negligible, the pure quartic self-energy of the larger pair has a uniform positive coefficient and dominates the mixed quartic term. Thus the only apparent equality loophole closes.

## 1. The curvature kernel carries a three-point Gram constraint

Put

\[
K_0:=K_J(0)=\int\alpha^2J(\alpha)\,d\alpha>0,
\qquad
k_*:=\inf_tK_J(t).
\tag{5}
\]

For arbitrary real `u_0,u_1,u_2` and real coefficients `c_0,c_1,c_2`, direct Fourier expansion gives

\[
\begin{aligned}
\sum_{i,j=0}^2c_ic_jK_J(u_i-u_j)
&=\int\alpha^2J(\alpha)
\left|\sum_{j=0}^2c_je^{-2\pi i\alpha u_j}\right|^2d\alpha\\
&\ge0.
\end{aligned}
\tag{6}
\]

Hence every three-point translation matrix of `K_J` is positive semidefinite. Apply this at the points `0,t_1,t_2`, write

\[
d:=t_1-t_2,
\qquad
a:=\frac{K_J(d)}{K_0},
\qquad
b:=\frac{K_J(t_1)}{K_0},
\qquad
c:=\frac{K_J(t_2)}{K_0},
\tag{7}
\]

and obtain

\[
\boxed{
\begin{pmatrix}
1&b&c\\
b&1&a\\
c&a&1
\end{pmatrix}\succeq0.
}
\tag{8}
\]

Representing this Gram matrix by unit vectors `v_0,v_1,v_2`,

\[
b+c
=\langle v_0,v_1+v_2\rangle
\ge-\|v_1+v_2\|
=-\sqrt{2+2a}.
\tag{9}
\]

This elementary inequality is the coupling missing from the independent lower bounds in `ANF-040`.

## 2. Nonnegative `m_5` forces a simultaneous quadratic margin

The quadratic expansion in `ANF-040` is

\[
H_J
=2\pi^2y_1^2B_1
+2\pi^2y_2^2B_2
+O_J\bigl((y_1^2+y_2^2)^2\bigr),
\tag{10}
\]

where

\[
B_1:=2K_0+2K_J(d)+K_J(t_1),
\qquad
B_2:=2K_0+2K_J(d)+K_J(t_2).
\tag{11}
\]

If `m_5(J)>=0`, then

\[
k_*\ge-\frac23K_0,
\tag{12}
\]

and therefore each bracket is individually nonnegative:

\[
B_j\ge2K_0+3k_*=m_5(J)\ge0.
\tag{13}
\]

The Gram constraint gives more. From (9), (12), and `a>=k_*/K_0>=-2/3`,

\[
\begin{aligned}
\frac{B_1+B_2}{K_0}
&=4+4a+b+c\\
&\ge4+4a-\sqrt{2+2a}.
\end{aligned}
\tag{14}
\]

The right side is increasing for `a>=-2/3`, so

\[
\boxed{
B_1+B_2
\ge c_{\rm Gram}K_0,
\qquad
c_{\rm Gram}:=\frac43-\sqrt{\frac23}
=0.5168367524\ldots>0.
}
\tag{15}
\]

Thus the two quadratic brackets cannot flatten simultaneously, even at `m_5(J)=0`.

If, for example, `0<y_2<=y_1`, then (13)--(15) imply

\[
y_1^2B_1+y_2^2B_2
\ge y_2^2(B_1+B_2)
\ge c_{\rm Gram}K_0y_2^2.
\tag{16}
\]

So whenever the two heights remain comparable, the coupled geometry has a strict quadratic margin despite the vanishing one-pair curvature margin.

## 3. The fourth-order term closes the only remaining asymmetric regime

It remains to control sequences in which one height is much smaller than the other. For this the complete fourth-order expansion has a useful sign that is invisible if the mixed term is inspected alone.

Let

\[
M_4:=\int\alpha^4J(\alpha)\,d\alpha>0.
\tag{17}
\]

Writing `d=t_1-t_2`, uniform Taylor expansion of the exact integrand in `ANF-040` gives

\[
H_J=Q_2+Q_4+O_J\bigl((y_1^2+y_2^2)^3\bigr),
\tag{18}
\]

where `Q_2` is the quadratic expression in (10)--(11), and

\[
\begin{aligned}
Q_4
=\frac{(2\pi)^4}{24}\int\alpha^4J(\alpha)
\Bigl[&y_1^4\bigl(8+2\cos(2\pi\alpha d)+\cos(2\pi\alpha t_1)\bigr)\\
&+y_2^4\bigl(8+2\cos(2\pi\alpha d)+\cos(2\pi\alpha t_2)\bigr)\\
&+12y_1^2y_2^2\cos(2\pi\alpha d)
\Bigr]d\alpha.
\end{aligned}
\tag{19}
\]

The pure fourth-order coefficient of either pair is uniformly positive:

\[
8+2\cos u+\cos v\ge5.
\tag{20}
\]

Therefore

\[
\boxed{
Q_4
\ge
\frac{(2\pi)^4M_4}{24}
\left[5(y_1^4+y_2^4)-12y_1^2y_2^2\right].
}
\tag{21}
\]

Now assume `m_5(J)=0` and suppose, for contradiction, that arbitrarily small genuinely two-pair splits can have nonpositive defect. Choose a sequence with

\[
y_{1,n}\ge y_{2,n}>0,
\qquad
y_{1,n}\to0,
\qquad
H_{J,n}\le0,
\tag{22}
\]

and put

\[
\lambda_n:=\frac{y_{2,n}^2}{y_{1,n}^2}\in(0,1].
\tag{23}
\]

If a subsequence has `lambda_n>=lambda_0>0`, then (16) makes `Q_2` at least a positive constant times `y_{1,n}^2`, while all remaining terms are `O_J(y_{1,n}^4)`. This contradicts (22). Hence any putative bad sequence must satisfy

\[
\lambda_n\to0.
\tag{24}
\]

But then (21) gives

\[
\frac{Q_4}{y_{1,n}^4}
\ge
\frac{(2\pi)^4M_4}{24}
\left(5+5\lambda_n^2-12\lambda_n\right)
\longrightarrow
\frac{5(2\pi)^4M_4}{24}>0.
\tag{25}
\]

At the same time `Q_2>=0` by (13), and the remainder in (18) is `o(y_{1,n}^4)`. Thus `H_{J,n}>0` for all sufficiently large `n`, again contradicting (22).

This proves that the equality case `m_5(J)=0` has a uniform punctured neighborhood in which every genuine two-pair split is collapse-dominated. The mixed quartic term can indeed be negative, but it can matter only when both heights are active; exactly there the positive-definite curvature Gram matrix supplies the missing quadratic margin. When one height disappears fast enough to evade that margin, the larger pair's pure quartic coefficient is uniformly at least `5` and wins instead.

## 4. The local criterion is now exact, including equality

For `m_5(J)>0`, local positivity is `ANF-040`. Section 3 adds the missing case `m_5(J)=0`. Conversely, `ANF-040` proves that if `m_5(J)<0`, then for arbitrarily small `epsilon>0` one can choose horizontal positions and the asymmetric heights

\[
y_1=\epsilon,
\qquad
y_2=\epsilon^2
\tag{26}
\]

so that `H_J<0` while both conjugate pairs remain genuinely nonreal. Hence (3)--(4) are sharp.

The resulting boundary now exactly parallels `ANF-039` at infinitesimal scale: **nonnegative `m_5` is the complete local five-point curvature criterion for both irreducible cardinality-five geometries**. The mechanisms differ. The one-pair geometry of `ANF-039` is controlled coefficient-by-coefficient at every height; the two-pair geometry needs positive-definite coupling between three horizontal curvature samples plus a fourth-order fallback in the strongly asymmetric regime.

This distinction is important: the present argument is local. It does not upgrade the two-pair geometry to the all-height theorem proved for one pair in `ANF-039`.

## 5. Consequence for the Montgomery--Taylor and central-notch profiles

`ANF-038` already gives the strict margins

\[
m_5(J_{\rm MT})>0.0078
\]

and, for a compatible central notch `J_s=J_{\rm MT}-s\phi_\eta`,

\[
m_5(J_s)>0.0003.
\]

Those profiles were therefore already inside the strict side of `ANF-040`; the new theorem does not improve their numerical local radius. Its value is structural: the previously unresolved equality face contains **no hidden five-point instability**. Any deformation of a positive spectrum that drives `m_5` exactly to zero remains locally safe for both five-point complex geometries.

Accordingly, the finite-real separator program no longer needs to treat `m_5=0` as a special unresolved branch. Within cardinality five, the only surviving complex question is still the genuinely finite-height two-pair gate

\[
\inf_{y_1,y_2>0}G_{2,2,1;J}(y_1,y_2),
\tag{27}
\]

away from the local neighborhood closed here and the one-pair boundary axes already closed globally by `ANF-039`.

## 6. Prior art and evidence boundary

The positive-definite step (6) is classical Fourier/Gram structure: a Fourier transform of a positive measure has positive semidefinite finite translation matrices. A targeted prior-art check found the standard Bochner/positive-definite-function framework and the already anchored strip version of Buescu--Paixão--Symeonides, but no external theorem is needed for (6)--(16), which are proved directly from the nonnegative density `alpha^2 J(alpha)`.

No publication-level novelty claim is made. The durable Mathia contribution here is the specific insertion of the three-point curvature Gram constraint into the `ANF-040` two-pair defect and the resulting closure of its zero-margin case. No new entry in `SOURCES.md` is required because the only general positive-definite framework used is already represented there and the load-bearing inequalities are finite derivations.

The assumptions `J>=0`, compact support, and `J` nonzero are essential to this proof as stated. Nonnegativity gives the Gram matrix; compact support gives the uniform fourth-order expansion; nontriviality gives `K_0,M_4>0`. The result does not address signed spectra, larger conjugation-invariant multisets, the global finite-height two-pair minimum, or the normalization-slack problem of `ANF-005`.

## 7. Consequence for the next gate

The local five-point analysis is now closed without a sign exception. For a positive support-one spectrum satisfying `m_5(J)>=0`, further cardinality-five work should not spend effort on another small-height expansion. A genuinely new five-point obstruction must occur at finite joint height in the two-pair geometry, where the full hyperbolic factors rather than their curvature jets control the sign. The natural next question is whether the same positive-definite coupling can be lifted from `K_J` to height-dependent transforms strongly enough to control that finite-height minimum, or whether an explicit finite-height two-pair witness breaks it.