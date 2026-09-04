# XF-033 — finite-range scale-invariant shape assemblies have geometric-ramp bulk null modes

**Status:** `EXACT-DERIVED` + `NEGATIVE/OBSTRUCTION` + `CLASSICAL-PATCH-TEST-STRUCTURE` + `STRUCTURAL/BOUNDARY`. XF-032 shows that the normalized three-root discriminant has an exact nonlinear bulk null family: geometric gap progressions `g_i=C r^i`, equivalently affine profiles in `y_i=log g_i`. That phenomenon is not special to triples. It is forced by finite-range locality, translation-invariant sliding, and scale invariance of the local shape observable.

Let `m>=1`, let

\[
H:(0,\infty)^{m+1}\to\mathbb R
\]

be `C^1`, and assume common-scale invariance

\[
H(cg_0,\ldots,cg_m)=H(g_0,\ldots,g_m)
\qquad(c>0).
\tag{1}
\]

For positive gaps `g_i`, define translated local energies

\[
E_j=H(g_j,\ldots,g_{j+m})
\]

and, for any finitely supported weights `a_j`,

\[
\mathcal K_a=\sum_j a_jE_j.
\tag{2}
\]

Put `y_i=log g_i`. Suppose that on every gap touched by the active windows one has the exact geometric ramp

\[
\boxed{g_i=C r^i},
\qquad C>0,\quad r>0.
\tag{3}
\]

Then there are coefficients `c_0(r),...,c_m(r)`, depending only on the local observable and on `r`, such that

\[
\boxed{
\mathcal K_a'
=\sum_i\left(\sum_{s=0}^m c_s(r)a_{i-s}\right)y_i'
}
\tag{4}
\]

along **any** differentiable gap evolution, and scale invariance forces

\[
\boxed{\sum_{s=0}^m c_s(r)=0.}
\tag{5}
\]

Consequently the entire coefficient in (4) is a discrete derivative of the taper. If

\[
C_s(r):=\sum_{t=0}^s c_t(r),
\qquad 0\le s\le m-1,
\]

then

\[
\boxed{
\sum_{s=0}^m c_s(r)a_{i-s}
=\sum_{s=0}^{m-1}C_s(r)\bigl(a_{i-s}-a_{i-s-1}\bigr).
}
\tag{6}
\]

In particular, wherever the block-start weights are constant on the relevant finite neighborhood, the first variation of the assembled energy with respect to `y_i` vanishes exactly. A constant-weight plateau has **no interior production at all on a geometric ramp**; its instantaneous derivative is supported only within `m` sites of the taper transitions/endpoints.

This generalizes the null mode of XF-032 from the normalized triple discriminant to every finite-range scale-invariant local shape energy. In particular, merely replacing three-root normalized discriminants by fixed `n`-root normalized discriminants, or by another fixed-range scale-free symmetric block observable, cannot make the mean logarithmic contrast into a bulk-coercive mode. A viable continuation must break at least one of the hypotheses: introduce a genuinely nonlocal/global term, use source-justified index/height dependence, retain an endpoint/global anchor, or abandon scale invariance in a controlled way.

## 1. Log-gap coordinates turn scale invariance into translation symmetry

Define

\[
G(u_0,\ldots,u_m)
:=H(e^{u_0},\ldots,e^{u_m}).
\tag{7}
\]

Equation (1) is equivalent to

\[
G(u+t\mathbf 1)=G(u)
\qquad(t\in\mathbb R).
\tag{8}
\]

Differentiating (8) gives two facts. First,

\[
\nabla G(u+t\mathbf 1)=\nabla G(u),
\tag{9}
\]

so the local gradient is unchanged by a common additive shift of all log gaps. Second,

\[
\boxed{
\sum_{s=0}^m\partial_sG(u)=0
}
\tag{10}
\]

for every `u`.

On the geometric ramp (3), write `B=log r` and `A=log C`. The log-gap window beginning at `j` is

\[
(y_j,\ldots,y_{j+m})
=(A+Bj)\mathbf 1+B(0,1,\ldots,m).
\tag{11}
\]

By (9), every translated window therefore has the **same slot gradient**. Define

\[
\boxed{
c_s(r):=
\partial_sG\bigl(0,B,2B,\ldots,mB\bigr).
}
\tag{12}
\]

The choice of zero for the first component is harmless because of (9). Equation (10) at this window is exactly (5).

Thus the null mode comes from symmetry before any Xi-flow equation is used: affine profiles in `y=log g` are homogeneous states for any translation-invariant sliding local shape functional.

## 2. Exact tapered derivative and the first-difference factorization

Differentiate (2) along an arbitrary differentiable positive-gap evolution. The block beginning at `j` contributes

\[
E_j'
=\sum_{s=0}^m c_s(r)y_{j+s}'
\tag{13}
\]

at the geometric-ramp configuration. Summing with weights and collecting the coefficient of `y_i'` gives

\[
\begin{aligned}
\mathcal K_a'
&=\sum_j a_j\sum_{s=0}^m c_s(r)y_{j+s}'\\
&=\sum_i\left(\sum_{s=0}^m c_s(r)a_{i-s}\right)y_i',
\end{aligned}
\tag{14}
\]

which is (4).

Now put `C_{-1}=0` and `C_m=0`; the latter equality is (5). Since

\[
c_s=C_s-C_{s-1},
\]

a finite telescoping gives

\[
\begin{aligned}
\sum_{s=0}^m c_sa_{i-s}
&=\sum_{s=0}^{m-1}C_sa_{i-s}
-\sum_{s=0}^{m-1}C_sa_{i-s-1}\\
&=\sum_{s=0}^{m-1}C_s(a_{i-s}-a_{i-s-1}),
\end{aligned}
\tag{15}
\]

which proves (6).

For a hard plateau `a_j=1` on `j=L,...,R` and zero elsewhere, every coefficient in (14) vanishes whenever all starts `i,i-1,...,i-m` lie in the plateau or all lie outside it. Hence

\[
\boxed{
\left(\sum_{j=L}^R E_j\right)'
\text{ depends only on }y_i'\text{ with }i\text{ within }m\text{ sites of }L\text{ or }R.
}
\tag{16}
\]

For `m=1`, (15) reduces to one taper difference and reproduces the structure of XF-032 for a triple observable `F(y_{j+1}-y_j)`.

## 3. Fixed larger normalized discriminants do not remove the mean-contrast blind spot

Take the XF-027 normalized discriminant on `n>=3` consecutive roots. It is a `C^1` function of the `n-1` positive internal gaps away from collisions. Under common scaling of all those gaps, the Vandermonde term gains `2N log c` while the variance term `N log V` gains the same `2N log c`; hence the normalized block observable is exactly scale invariant.

Therefore the theorem applies with

\[
m=n-2.
\]

On a geometric gap progression, any constant-weight sliding sum of fixed `n`-root normalized discriminants has zero interior Euler coefficient in log-gap coordinates. Increasing the block size can change the endpoint stencil and can add more internal shape directions, but it **cannot by itself create bulk sensitivity to the affine log-gap slope**.

The same conclusion holds for any finite linear combination of finitely many translated local scale-invariant shape observables: each component has a zero-sum slot gradient on an affine log-gap profile, so the assembled interior coefficient still vanishes.

This sharpens the escape clause left open in XF-032. A larger fixed block may help control fluctuations transverse to the geometric-ramp family, but it does not solve the missing mean logarithmic contrast unless some additional nonlocal, inhomogeneous, scale-sensitive, or boundary information is introduced.

## 4. What the theorem does and does not say

The result is a statement about the **first variation of the assembled functional**, not about the numerical value of each local block energy. A local shape energy can depend strongly on `r`; for example, every triple discriminant on a non-arithmetic geometric ramp has a nonzero shape deficit and positive internal square production. Equation (16) says that, after translation-invariant overlap, those local productions can be cancelled by the remaining interactions so that the total instantaneous derivative is boundary-supported. This is exactly the phenomenon already exhibited concretely by XF-032.

Nor does the theorem say that geometric ramps are preserved by the Xi flow. The identity is instantaneous and kinematic: it holds at the ramp configuration for any differentiable evolution. It therefore cannot be evaded by changing details of the logarithmic-repulsion conductances while keeping the same local observable and assembly symmetry.

A long fixed-ratio ramp is also not asserted to be source-admissible for Xi. As XF-032 notes, `g_{j+M}/g_j=r^M` can have enormous dynamic range. The theorem is instead a **coercivity obstruction**: no proof may claim that a finite-range scale-free translation-invariant block energy controls the mean log-gap slope through interior production alone. Xi-specific information may still exclude the null family or control its endpoint mode.

Finally, a slow taper does not automatically make the total boundary term small. Equation (6) makes the coefficient proportional to taper differences, but the factors `y_i'` may be large or singular near collisions. The collision-coverage mechanism of XF-028 and the finite-gap estimates sought after XF-031 remain necessary.

## 5. Prior-art and novelty boundary

The algebra behind (5)--(16) is an elementary discrete Euler--Lagrange symmetry cancellation. In neighboring atomistic/discrete-variational language, the requirement that homogeneous deformations create no spurious interior force is the classical **patch-test / ghost-force consistency** principle. A targeted literature audit found this broad mechanism explicitly in the atomistic-to-continuum patch-test literature; it is not treated here as a new general variational theorem.

No external theorem is load-bearing in the proof above. The Mathia-specific durable consequence is the specialization to `y_i=log g_i`: **geometric gap ramps are an unavoidable bulk-null family for every finite-range, translation-invariant assembly of common-scale-invariant local gap-shape observables**. This places the XF-032 mean-contrast obstruction at the level of the whole local shape-energy design class rather than one triple formula.

## 6. Consequence for `xi_flow`

The active overlap/discriminant program should no longer treat “use a larger fixed normalized block” as a way to make affine log-gap profiles acquire bulk cost. The missing mode survives every such finite-range scale-free translation-invariant assembly.

The positive options are correspondingly sharper. One may keep the collision-safe local shape carrier but add a genuinely nonlocal/global observable that anchors the mean contrast; exploit source-valid height dependence or endpoint information; or prove that Xi-specific counting/spacing constraints make the geometric-ramp endpoint mode quantitatively harmless on the super-mesoscopic buffer. Any proposed local replacement that still satisfies the three hypotheses above should be rejected immediately as a solution to the mean-contrast problem, even if its internal block algebra looks different from the triple discriminant.