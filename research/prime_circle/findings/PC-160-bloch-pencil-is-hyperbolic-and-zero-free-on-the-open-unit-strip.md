# PC-160 — Bloch pencil is hyperbolic and zero-free on the open unit strip

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-NEGATIVE` for interpreting the analytically continued PC-156/PC-159 Bloch coordinate as a Riemann-like spectral variable. PC-159 proved the exact reflection `t <-> 1-t` and showed that it is universal Bloch time reversal rather than arithmetic. The stronger statement is that the same intrinsic quadratic pencil has **no determinant zeros anywhere in the open strip `0 < Re(t) < 1`**. In fact every polynomial eigenvalue is real and lies in `(-infinity,0] union [1,infinity)`.

Fix `d>=2` and any nonempty finite subset

\[
X\subseteq \mathbb Z/d\mathbb Z.
\]

As in PC-159, define on `C^X` the induced inverse-square chord Laplacian

\[
(L_Xf)(a)=\sum_{\substack{b\in X\\b\ne a}}
\frac{f(a)-f(b)}{4\sin^2(\pi(a-b)/d)},
\]

the Hermitian cotangent matrix

\[
H_X(a,b)=
\begin{cases}
i\cot\!\left(\dfrac{\pi(a-b)}d\right),&a\ne b,\\0,&a=b,
\end{cases}
\]

and

\[
C_X:=H_X+J_X.
\]

The universal Bloch pencil is

\[
\boxed{
\mathcal P_X(t)
=\frac1{d^2}\left(L_X+\frac t2 C_X-\frac{t^2}{2}I\right).
}
\tag{1}
\]

Then for every real `0<=sigma<=1`,

\[
\boxed{
\mathcal P_X(\sigma)
\succeq
\frac{\sigma(1-\sigma)}{2d^2}I.
}
\tag{2}
\]

Consequently, for `t=sigma+i tau` with `0<sigma<1`,

\[
\boxed{
\operatorname{Re}\mathcal P_X(t)
\succeq
\frac{\sigma(1-\sigma)+\tau^2}{2d^2}I
\succ0,
}
\tag{3}
\]

so the pencil is strictly accretive throughout the entire open unit strip. In particular,

\[
\boxed{
\det\mathcal P_X(t)\ne0
\qquad(0<\operatorname{Re}t<1).
}
\tag{4}
\]

This holds before imposing primitiveness, coprimality, prime birth, or any other arithmetic condition on `X`.

## 1. Complete cyclic lifts force a positive gap on the real Bloch interval

Let `m>=2` and form the complete cyclic lift of `X`,

\[
S_{X,m}:=
\{a+rd\pmod{dm}:a\in X,\ r\in\mathbb Z/m\mathbb Z\}.
\tag{5}
\]

Translation by `d` is an exact order-`m` symmetry of this root set. Let `M_{X,m}` be the inverse-square chord Laplacian induced on `S_{X,m}`, normalized by `(dm)^{-2}`. The same complete-fiber Fourier calculation used in PC-156, and requiring no arithmetic property of `X`, gives for the `k`-th fiber sector

\[
\boxed{
M_{X,m}^{(k)}
\simeq
\mathcal P_X(k/m),
\qquad 0\le k<m,
}
\tag{6}
\]

up to the harmless diagonal root-of-unity gauge already used in PC-156/PC-159.

Now split the weighted graph on `S_{X,m}` into edges joining points in the same fiber and edges joining different fibers. Both edge Laplacians are positive semidefinite and both commute with the fiber translation, so their individual Fourier blocks are positive semidefinite.

Inside one fiber the chord difference is `d(r-s)`, hence its conductance is exactly

\[
\frac1{4\sin^2(\pi(r-s)/m)}.
\]

The same-fiber graph is therefore the full regular `m`-gon inverse-square Laplacian. Its classical Fourier eigenvalue in sector `k` is

\[
\lambda_k^{(m)}=\frac{k(m-k)}2.
\tag{7}
\]

After the `(dm)^{-2}` normalization, the same-fiber part of the `k`-th block is the scalar

\[
\frac{k(m-k)}{2d^2m^2}I
=
\frac{t(1-t)}{2d^2}I,
\qquad t=\frac{k}{m}.
\tag{8}
\]

The cross-fiber block is positive semidefinite. Equations (6)--(8) therefore prove

\[
\mathcal P_X(k/m)
\succeq
\frac{(k/m)(1-k/m)}{2d^2}I.
\tag{9}
\]

Rational Bloch points are dense in `[0,1]`, and both sides depend continuously on the real parameter. The positive cone is closed, so (9) extends to every real `sigma in [0,1]`, proving (2).

The bound is structural rather than an estimate obtained from the explicit matrix entries: the positive gap is exactly the energy of motion **within each complete lift fiber**. Any additional interaction between distinct coarse roots can only increase the quadratic form.

## 2. Analytic continuation is strictly accretive in the whole strip

For real `sigma`, `L_X` and `C_X` are Hermitian. If

\[
t=\sigma+i\tau,
\]

then taking the Hermitian part of (1) gives the exact identity

\[
\boxed{
\frac{\mathcal P_X(t)+\mathcal P_X(t)^*}{2}
=
\mathcal P_X(\sigma)
+\frac{\tau^2}{2d^2}I.
}
\tag{10}
\]

Combining (10) with (2) gives (3). Hence for every vector `v`,

\[
\operatorname{Re}\langle v,\mathcal P_X(t)v\rangle
\ge
\frac{\sigma(1-\sigma)+\tau^2}{2d^2}\|v\|^2.
\tag{11}
\]

A matrix with strictly positive Hermitian part cannot have a kernel. More quantitatively,

\[
\boxed{
\|\mathcal P_X(t)^{-1}\|
\le
\frac{2d^2}{\sigma(1-\sigma)+\tau^2},
\qquad 0<\sigma<1.
}
\tag{12}
\]

On the visually tempting midpoint line this becomes

\[
\boxed{
\|\mathcal P_X(1/2+i\tau)^{-1}\|
\le
\frac{8d^2}{1+4\tau^2}.
}
\tag{13}
\]

Thus the exact PC-159 reflection center is not merely unsupported as a zero-localizing line: the intrinsic pencil is uniformly separated from singularity there.

## 3. Every polynomial eigenvalue is real and lies outside `(0,1)`

There is an independent direct hyperbolicity check. Suppose

\[
\mathcal P_X(t)v=0,
\qquad v\ne0.
\]

Set

\[
\ell:=\langle v,L_Xv\rangle\ge0,
\qquad
c:=\langle v,C_Xv\rangle\in\mathbb R,
\qquad
r:=\|v\|^2>0.
\]

Taking the scalar product with `v` in (1) yields

\[
r t^2-c t-2\ell=0.
\tag{14}
\]

Its discriminant is

\[
\boxed{
c^2+8r\ell\ge0,}
\tag{15}
\]

so every matrix-polynomial eigenvalue `t` is real. Moreover (2) is positive definite for every real `0<t<1`, excluding that interval. Therefore

\[
\boxed{
\det\mathcal P_X(t)=0
\Longrightarrow
 t\in(-\infty,0]\cup[1,\infty).
}
\tag{16}
\]

After multiplying (1) by `-1`, this is exactly the real-rooted Hermitian quadratic situation called a hyperbolic/definite matrix polynomial in the classical matrix-polynomial literature. The Prime-Circle geometry does not produce a hidden cloud of nonreal Bloch eigenparameters waiting to be organized by the PC-159 reflection; it produces the opposite spectral geometry.

## 4. Prior-art and novelty audit

The ingredients used here are deliberately classical. The full regular-polygon `csc^2` eigenvalue (7) is the Calogero--Perelomov identity already anchored in `research/prime_circle/SOURCES.md`. PC-156 supplied the exact complete-fiber inverse-square/cotangent pencil, and PC-159 showed that the same pencil and its `t <-> 1-t` antiunitary reflection hold for arbitrary root subsets.

The abstract matrix-polynomial classification is also established theory. Nicholas J. Higham, D. Steven Mackey and Françoise Tisseur, **Definite Matrix Polynomials and their Linearization by Definite Pencils**, *SIAM Journal on Matrix Analysis and Applications* 31:2 (2009), 478--502, DOI `10.1137/080721406`, treats hyperbolic/definite Hermitian matrix polynomials and their real spectral structure. The elementary scalar-compression argument (14)--(15) is sufficient here; no new general theorem about matrix polynomials is claimed.

Directed searches across root-of-unity `csc^2`/cotangent Bloch pencils, hyperbolic quadratic matrix polynomials, and inverse-square chord operators did not locate the exact lower bound (2) or strip statement (3)--(4) for this Prime-Circle pencil. That absence is not evidence of historical priority. The durable content is the line-specific classification obtained by combining the complete root lift with the standard definite-polynomial viewpoint: the exact Bloch variable supplied by the intrinsic chord geometry has a **definiteness interval equal to the whole candidate critical strip on the real axis and a strictly accretive analytic continuation across the corresponding complex strip**.

## 5. RH consequence and surviving boundary

PC-159 already ruled out reading the universal reflection `t <-> 1-t` as zeta's functional equation. Equations (3), (4), and (16) sharpen that obstruction decisively. If one analytically continues the *intrinsic* Bloch coordinate supplied by PC-156, then the region corresponding formally to Riemann's critical strip is exactly where the Prime-Circle determinant cannot vanish. In particular the midpoint line `Re(t)=1/2` is a quantitative resolvent region rather than a candidate zero locus.

This rules out the route

\[
\boxed{
\text{complete-fiber inverse-square/cotangent Bloch pencil}
\to
\text{analytic continuation in }t
\to
\text{PC-159 half-reflection}
\to
\text{Riemann-like critical-strip zeros}.
}
\]

The statement is intentionally narrow. It does **not** classify nonlinear functions of the pencil, determinants after coupling different conductors, zero-mean new-prime puncture sectors not representable by the complete cyclic lift, growing-support limits, or the global uniformization/monodromy branch. A surviving mechanism would have to introduce genuinely arithmetic information that breaks the universal complete-lift positivity, rather than reinterpret this finite Bloch parameter itself as `s`.

The result is directly falsifiable. One finite root subset `X`, one `d`, and one `t` with `0<Re(t)<1` for which `det P_X(t)=0` falsifies (3)--(4); one nonreal polynomial eigenvalue falsifies (14)--(16); and one rational `k/m` violating the same-fiber lower bound (9) falsifies the geometric proof at its source.
