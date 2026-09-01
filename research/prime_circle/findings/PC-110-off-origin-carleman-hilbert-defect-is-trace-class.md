# PC-110 — off-origin Carleman–Hilbert defect is trace class

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` + `DECISIVE-BOUNDARY`. PC-109 identifies the canonical prime-conductor microlocal residual with the universal Hilbert–Schmidt operator

\[
\mathcal K=\mathcal D-P_0\mathcal DP_0,
\qquad
\mathcal D=C-VHV^*,
\]

where `C` is the Carleman operator on `L^2(R_+)`, `H` is the Hilbert matrix embedded as a unit-cell step operator, and `P_0` is multiplication by `1_[0,1)`. PC-109 leaves `det_2(I-z\mathcal K)` as a legitimate regularized determinant, although already prime-blind. The remaining trace-ideal question has a stronger exact answer:

\[
\boxed{\mathcal K\in\mathcal S_1.}
\]

In fact

\[
\boxed{\operatorname{Tr}\mathcal K
=1-\log2-\frac\gamma2.}
\]

Consequently the `det_2` zero divisor of the canonical compact microlocal residual is again nuclear: `det_2(I-z\mathcal K)=det(I-z\mathcal K)e^{z\operatorname{Tr}\mathcal K}`, so its zeros have absolutely summable reciprocal moduli and counting function `o(R)`. The Hilbert--Schmidt regularization therefore does **not** escape the PC-107 Riemann-zero-density obstruction after the canonical PC-109 microlocal recentering. The only non-trace-class part of the continuum defect is the singular lowest cell `P_0\mathcal DP_0`, which is already universal and noncompact.

No theorem-level historical novelty is claimed for trace ideals, Carleman/Hilbert operators, rank-one integral factorizations, or regularized determinants. The durable Prime-Circle result is the exact trace-class classification of the specific off-origin defect produced by PC-109 and the resulting closure of its `det_2` escape.

## 1. Exact cell model from PC-109

Use the PC-109 identification

\[
L^2(0,1)\otimes\ell^2(\mathbb Z_{\ge0})
\cong L^2(\mathbb R_+),
\qquad
u=a+x,
\]

with `a>=0` and `0<=x<1`. The kernel of

\[
\mathcal D=C-VHV^*
\]

between cells `a,b` is

\[
\boxed{
 d_{ab}(x,y)
=
\frac1{a+b+x+y}-\frac1{a+b+1}.
}
\]

Let `P=P_0` be the projection onto the cell `a=0` and `Q=I-P`. Then

\[
\boxed{
\mathcal K=\mathcal D-P\mathcal DP
=P\mathcal DQ+Q\mathcal DP+Q\mathcal DQ.
}
\]

Thus every matrix block retained by `\mathcal K` has at least one positive cell index. This single missing `(0,0)` block is exactly what changes the trace ideal.

## 2. The continuum/discrete difference has a rank-two integral representation

For `0<t<1`, define vectors in

\[
\mathscr H=L^2(0,1)\otimes\ell^2(\mathbb Z_{\ge0})
\]

by

\[
f_t(a,x)=t^{a+x-1/2},
\qquad
g_t(a,x)=t^a.
\]

Then pointwise in the cell variables,

\[
\int_0^1 f_t(a,x)f_t(b,y)\,dt
=
\frac1{a+b+x+y},
\]

while

\[
\int_0^1 g_t(a,x)g_t(b,y)\,dt
=
\frac1{a+b+1}.
\]

Hence, first as a weak identity on compactly supported cell vectors,

\[
\boxed{
\mathcal D
=
\int_0^1
\bigl(|f_t\rangle\langle f_t|-|g_t\rangle\langle g_t|\bigr)\,dt.
}
\]

Put `h_t=f_t-g_t`. The integrand can be written in cancellation-preserving form as

\[
A_t
:=|f_t\rangle\langle f_t|-|g_t\rangle\langle g_t|
=|h_t\rangle\langle f_t|+|g_t\rangle\langle h_t|.
\]

After deleting the singular lowest-cell compression,

\[
\begin{aligned}
K_t&:=A_t-PA_tP\\
&=|Qh_t\rangle\langle f_t|
 +|Ph_t\rangle\langle Qf_t|\\
&\quad+|Qg_t\rangle\langle h_t|
 +|Pg_t\rangle\langle Qh_t|.
\end{aligned}
\]

Every `K_t` is therefore a sum of four rank-one operators. It remains only to check that its trace norm is integrable in `t`.

## 3. Removing the origin cell makes the rank-one integral nuclear

The relevant norms are explicit:

\[
\|g_t\|^2=\frac1{1-t^2},
\qquad
\|Qg_t\|^2=\frac{t^2}{1-t^2},
\qquad
\|Pg_t\|=1,
\]

and

\[
\boxed{
\|f_t\|^2=-\frac1{2t\log t},
\qquad
\|Qf_t\|^2=-\frac{t}{2\log t},
\qquad
\|Pf_t\|^2=-\frac{1-t^2}{2t\log t}.
}
\]

For `0<t<=1/2`, the triangle inequality gives

\[
\|Qh_t\|
\le \|Qf_t\|+\|Qg_t\|
=O\!\left(\sqrt{\frac{t}{|\log t|}}+t\right),
\]

while

\[
\|h_t\|,\|Ph_t\|
=O\!\left(\frac1{\sqrt{t|\log t|}}+1\right).
\]

Using the rank-one identity `|| |u><v| ||_1=||u|| ||v||`, the four terms above therefore satisfy

\[
\boxed{
\|K_t\|_1
\le
C\left(
\frac1{|\log t|}
+\sqrt{\frac{t}{|\log t|}}
+t
\right),
\qquad 0<t\le\frac12,
}
\]

and the right-hand side is integrable at zero.

At the opposite endpoint write

\[
f_t(a,x)=g_t(a,x)t^{x-1/2}.
\]

Uniformly for `x in [0,1]`,

\[
|t^{x-1/2}-1|\le C(1-t)
\qquad\left(\frac12\le t<1\right).
\]

Since `||f_t||,||g_t||,||Qf_t||,||Qg_t||=O((1-t)^{-1/2})`, this yields

\[
\|h_t\|,\|Qh_t\|=O((1-t)^{1/2}),
\qquad
\|Ph_t\|=O(1-t).
\]

Therefore

\[
\boxed{
\|K_t\|_1=O(1)
\qquad(t\to1^-).
}
\]

Combining the two endpoint estimates gives

\[
\int_0^1\|K_t\|_1\,dt<\infty.
\]

The Bochner integral of the rank-one decomposition therefore converges in trace norm and has exactly the PC-109 kernel outside the deleted origin block. Hence

\[
\boxed{
\mathcal K=\int_0^1K_t\,dt\in\mathcal S_1.
}
\]

This is strictly stronger than the `\mathcal S_2` conclusion needed in PC-109.

## 4. The trace is an explicit universal constant

Because the preceding integral converges in trace norm, the trace may be taken termwise. An equivalent absolutely convergent cell expansion is

\[
\operatorname{Tr}\mathcal K
=
\sum_{a=1}^\infty
\int_0^1
\left(
\frac1{2a+2x}-\frac1{2a+1}
\right)dx.
\]

Thus

\[
\operatorname{Tr}\mathcal K
=
\sum_{a=1}^\infty
\left[
\frac12\log\frac{a+1}{a}
-
\frac1{2a+1}
\right].
\]

The `N`-th partial sum is

\[
1+rac12\log(N+1)+\frac12H_N-H_{2N+1},
\]

so the standard harmonic-number asymptotic gives

\[
\boxed{
\operatorname{Tr}\mathcal K
=1-\log2-\frac\gamma2
=0.018244986989\ldots .
}
\]

Together with PC-109,

\[
\|\mathcal K\|_2^2
=\gamma-4+5\log2,
\]

this supplies two exact universal trace-ideal invariants of the escaped prime-conductor mass. Neither contains any conductor or primitive-root datum.

## 5. The canonical `det_2` escape collapses back to the PC-107 nuclear zero law

Let the nonzero eigenvalues of the self-adjoint trace-class operator `\mathcal K` be `\mu_j`, repeated with multiplicity. Then

\[
\sum_j|\mu_j|<\infty.
\]

For a trace-class operator, the Hilbert--Carleman determinant and the ordinary Fredholm determinant satisfy the standard identity

\[
\boxed{
\det{}_2(I-z\mathcal K)
=
\det(I-z\mathcal K)
\exp\!\bigl(z\operatorname{Tr}\mathcal K\bigr).
}
\]

The exponential factor never vanishes. Consequently both determinants have the same nonzero zero divisor,

\[
z_j=\mu_j^{-1},
\]

and therefore

\[
\boxed{
\sum_j\frac1{|z_j|}
=
\sum_j|\mu_j|<\infty.
}
\]

Exactly as in PC-107, monotonic rearrangement of the summable eigenvalue moduli gives

\[
\boxed{N_{\det_2}(R)=o(R).}
\]

The Riemann--von Mangoldt zero count is of order `R log R`, so this canonical compact microlocal residual cannot directly realize the Riemann-zero ordinate divisor under an asymptotically linear spectral normalization. Passing from `det` to `det_2` changes nothing because the operator itself has fallen back inside `\mathcal S_1`.

This is a stronger analytic obstruction than prime-blindness alone. Even if one ignored the fact that `\mathcal K` is universal, its trace ideal already places its regularized determinant in the wrong zero-density class.

## 6. Prior-art and novelty audit

The surrounding operator theory is classical. Magnus and Rosenblum give the Hilbert-matrix spectral model already used in PC-075. The continuous/discrete Hankel correspondence and Carleman/Hilbert comparison lie in the classical Hankel framework represented in the line's source anchors by Pushnitski--Yafaev and the Yafaev continuous/discrete representation used in PC-109. Trace-class ideals, Fredholm determinants, and the identity relating `det_2` to `det` are standard trace-ideal theory already invoked in PC-107.

Directed searches for Carleman/Hilbert continuous-discrete comparison, trace-class perturbations, and discretization defects found established general frameworks, not a basis for a historical novelty claim about the analytic ingredients. The claim retained here is deliberately line-specific: **after the exact PC-109 conductor scaling and deletion of its unique non-Hilbert--Schmidt origin cell, the remaining Prime-Circle continuum defect is not merely Hilbert--Schmidt but trace class**.

The proof above is self-contained and uses the exact PC-109 kernel, so the result does not depend on identifying a literature theorem with precisely this step-function embedding.

## 7. Consequence for the surviving Hardy/Hankel boundary

The PC-107--PC-110 chain now reads

\[
\text{fixed conductor }T_n\in\mathcal S_1
\longrightarrow
\text{prime conductor blowup}
\longrightarrow
\text{universal Hilbert corner}
\longrightarrow
\text{Carleman--Hilbert microlocal defect}.
\]

The singular origin cell is noncompact and universal; after removing it, the recovered compact mass is again nuclear:

\[
\boxed{
\mathcal D
=P_0\mathcal DP_0+\mathcal K,
\qquad
\mathcal K\in\mathcal S_1.
}
\]

Thus the canonical affine conductor microlocalization does not merely lose prime arithmetic; its compact remainder also returns to the same trace-ideal zero-density obstruction that PC-107 established at fixed conductor. A surviving Hardy/Hankel mechanism must retain arithmetic **before** this universal single-conductor scaling, for example through a genuinely joint cross-level operator or a geometry-forced multiscale/non-affine recentering whose limiting compact part is not trace class. Those possibilities remain open boundaries, not positive evidence.