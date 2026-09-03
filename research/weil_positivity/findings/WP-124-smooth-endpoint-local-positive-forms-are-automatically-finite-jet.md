# WP-124 — Smooth endpoint-local positive forms are automatically finite-jet

**Status:** `LITERATURE+DERIVED + DECISIVE-NEGATIVE + DISTRIBUTIONAL-LOCALITY + AUTOMATIC-FINITE-JET + PRIME-CIRCLE-BRIDGE + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION`.

`WP-123` proves that every fixed **finite-order** positive endpoint-jet geometry for the canonical Gamma--Schoenberg increment

\[
u_t(y)=
\begin{pmatrix}
\cos(ty)-1\\
\sin(ty)
\end{pmatrix}
\]

fails the critical prime-shell Cauchy test, but deliberately leaves infinite-order analytic/Gevrey jet spaces outside its theorem. There is a sharper locality boundary: **inside the ordinary smooth/distributional category, an endpoint-local continuous quadratic form cannot be genuinely infinite-order at all.**

Let

\[
B:C_c^\infty(\mathbb R;\mathbb R^2)\times C_c^\infty(\mathbb R;\mathbb R^2)\to\mathbb R
\]

be a continuous symmetric positive-semidefinite bilinear form, and assume it is supported only at the endpoint in each argument: `B(g,h)=0` whenever either `g` or `h` vanishes on a neighborhood of `0`. The Schwartz kernel theorem represents `B` by a matrix-valued distribution on `R^2`; the support assumption forces that kernel to be supported at the single point `(0,0)`. The classical structure theorem for point-supported distributions then forces

\[
\boxed{
B(g,h)=
\sum_{0\le j,k\le m}
 g^{(j)}(0)^T C_{jk}h^{(k)}(0)
}
\tag{1}
\]

for some **finite** `m`. Positivity makes the finite block matrix `C=(C_{jk})` positive semidefinite. Thus every ordinary smooth endpoint-local positive geometry is already a finite jet form of exactly the class killed in `WP-123`.

Consequently, if such a form sees any nonzero Gamma--Schoenberg prime channel, its exact critical shell energy fails to tend to zero; if its highest visible derivative order is `r>=1`, the `WP-123` endpoint calculation gives growth of order

\[
\boxed{X(\log X)^{2r}}
\tag{2}
\]

on multiplicative prime shells. If only the value trace is seen, then the form vanishes on every `u_t` because `u_t(0)=0` and therefore discards the finite-prime carrier.

So the apparent infinite-order **local** escape after `WP-123` is not available in standard smooth geometry. A genuine survivor must change category: use an analytic/Gevrey or hyperfunction topology not continuous on ordinary smooth test functions, use a nonlocal/fractional kernel with support away from the endpoint point, keep a cutoff-dependent family rather than one fixed form, or alter the finite--archimedean object before the endpoint norm is formed.

This does not prove Weil positivity or RH. The distribution-theoretic classification is classical; the Mathia-specific content is the consequence that the `WP-117`--`WP-123` boundary-layer program has **no hidden infinite-order endpoint-local positive completion in the standard smooth category**.

## 1. Endpoint locality turns the quadratic form into a point-supported distribution kernel

Write

\[
\mathcal D=C_c^\infty(\mathbb R;\mathbb R^2).
\]

Assume `B` is jointly continuous in the ordinary test-function topology, symmetric, and positive semidefinite:

\[
B(g,g)\ge0
\qquad(g\in\mathcal D).
\tag{3}
\]

The endpoint-locality condition is

\[
\boxed{
B(g,h)=0
\quad\text{if either }g\text{ or }h
\text{ vanishes on some neighborhood of }0.
}
\tag{4}
\]

This is the natural fixed-limit meaning of a quadratic geometry supported purely at the endpoint. It is stronger than having a kernel concentrated merely *near* zero, and it is exactly the category suggested when a shrinking boundary layer converges to a boundary trace rather than retaining finite width.

By the Schwartz kernel theorem, each scalar component of `B` is represented by a distribution kernel. Equivalently there is a `2 x 2` matrix-valued distribution

\[
K\in\mathcal D'(\mathbb R^2;M_2(\mathbb R))
\tag{5}
\]

such that

\[
B(g,h)=\langle K,\,g\otimes h\rangle
\tag{6}
\]

with the component contraction understood.

Condition (4) forces

\[
\boxed{\operatorname{supp}K\subseteq\{(0,0)\}.}
\tag{7}
\]

Indeed, if a support point had first coordinate different from zero, one could test it with a first-factor bump supported away from zero, contradicting (4); the same argument applies to the second coordinate.

The use of the full real line is only notational. The Gamma jump coordinate is naturally written for `y>0`, but every `u_t` extends smoothly through `0`; a one-sided endpoint form has the same finite one-sided jet classification after any fixed smooth extension across the endpoint.

## 2. Point support forces finite order

A classical theorem of Schwartz distribution theory states that every distribution supported at one point is a finite linear combination of derivatives of the Dirac mass. Applied componentwise to (5)--(7), there is a finite integer `m` and matrices `A_{jk}` such that

\[
K=
\sum_{0\le j,k\le m}
A_{jk}\,
\partial_x^j\partial_y^k
\bigl(\delta_0\otimes\delta_0\bigr).
\tag{8}
\]

After absorbing the conventional derivative signs into the coefficients, (8) is exactly (1):

\[
B(g,h)=
\sum_{j,k=0}^m
 g^{(j)}(0)^T C_{jk}h^{(k)}(0).
\tag{9}
\]

There is therefore no continuous distributional functional at a point that depends on arbitrarily high derivatives. Compact point support automatically implies finite order before positivity or arithmetic enters.

To identify the sign structure, let

\[
J_mg(0)=
\bigl(g(0),g'(0),\ldots,g^{(m)}(0)\bigr)
\in\mathbb R^{2(m+1)}.
\tag{10}
\]

Finite jet interpolation allows every vector in this space to be realized by a compactly supported smooth function. Hence (3) implies

\[
\boxed{C=(C_{jk})_{0\le j,k\le m}\succeq0,}
\tag{11}
\]

and

\[
\boxed{B(g,g)=J_mg(0)^T C J_mg(0).}
\tag{12}
\]

Thus the general continuous endpoint-local positive form is not merely analogous to the finite-jet class in `WP-123`; it **is** that class.

## 3. The exact critical Gamma carrier is therefore already covered by WP-123

For `q>1`, define the critical multiplicative prime-shell vector

\[
F_{X,q}(y)
:=
\sum_{X<p\le qX}
\frac{\log p}{\sqrt p}\,u_{\log p}(y).
\tag{13}
\]

The endpoint derivatives of the canonical increment have the exact form

\[
u_t^{(j)}(0)=t^jv_j,
\qquad j\ge1,
\tag{14}
\]

where `v_j` is a fixed signed coordinate vector depending only on the parity of `j`. Therefore

\[
F_{X,q}^{(j)}(0)
=
B_{X,j,q}v_j,
\qquad
B_{X,j,q}:=
\sum_{X<p\le qX}
\frac{(\log p)^{j+1}}{\sqrt p}.
\tag{15}
\]

The prime-number-theorem asymptotic used in `WP-123` gives

\[
\boxed{
B_{X,j,q}
=
2(\sqrt q-1)\sqrt X\,(\log X)^j(1+o(1)).
}
\tag{16}
\]

If (12) is nonzero on the canonical carrier, let `r>=1` be the largest derivative order whose parity vector is seen by the positive block matrix. Positivity eliminates invisible higher rows exactly as in the endpoint argument of `WP-123`, so the highest visible order dominates and

\[
\boxed{
B(F_{X,q},F_{X,q})
\asymp
X(\log X)^{2r}
}
\tag{17}
\]

with a positive leading constant. In particular the shell tail does not tend to zero, so the critical ordered prime series cannot be Cauchy in this geometry.

If no derivative order `j>=1` is seen, the form is supported only on the value trace as far as the carrier is concerned. But

\[
\boxed{u_t(0)=0,}
\tag{18}
\]

so then `B` vanishes on every finite-prime increment and cannot produce the finite Weil term.

This gives the dichotomy

\[
\boxed{
\text{smooth endpoint-local positive geometry}
\Longrightarrow
\begin{cases}
\text{critical prime-shell divergence},&\text{if it sees the carrier},\\
0,&\text{if it does not.}
\end{cases}}
\tag{19}
\]

There is no third, genuinely infinite-order distributional endpoint case.

## 4. Why analytic/Gevrey infinite jets are a genuine category change, not a counterexample

The point-support theorem is specific to the standard smooth test-function topology. An infinite series of endpoint derivatives may define a continuous functional on a much smaller space of analytic or Gevrey germs while failing to define any distribution on `C_c^infty`.

For example, on functions admitting holomorphic continuation one may form

\[
L_a(g):=g'(ia)
=
\sum_{r\ge0}
\frac{(ia)^r}{r!}\,g^{(r+1)}(0),
\qquad a>0,
\tag{20}
\]

and the rank-one form

\[
\mathcal E_a(g)=|L_a(g)|^2\ge0.
\tag{21}
\]

This is a genuinely infinite-jet positive form. On the canonical exponential increment,

\[
L_a(e^{ity}-1)=it\,e^{-at},
\tag{22}
\]

so it damps large positive frequencies exponentially. At the critical prime amplitudes, the corresponding coherent coefficient is

\[
\sum_p
\frac{(\log p)^2}{p^{a+1/2}},
\tag{23}
\]

which converges for `a>1/2`.

This is an important matched falsifier: **positivity by itself does not forbid an infinite-order regularization.** What fails is ordinary smooth endpoint locality. The functional (20) is not defined on a generic compactly supported smooth function because it demands analytic continuation to a nonreal point, and the parameter `a` introduces a distinguished length scale. No current Mathia construction independently forces such an analytic topology or such a scale, and (21) supplies neither the finite/archimedean explicit-formula decomposition nor an independent global Weil sign theorem.

The example therefore marks the exact surviving boundary rather than reopening the local smooth route.

## 5. Matched controls and scope boundary

**Nonlocal fractional forms.** A negative/fractional Sobolev form couples values at distinct jump coordinates or has a Fourier multiplier of noninteger order. Its distribution kernel is not supported only at `(0,0)`, so (7) fails. Such forms remain outside this finding; the separate prime-torus spectral obstructions `WP-109`--`WP-116` are not being imported as a theorem about the Gamma jump coordinate.

**Finite-width endpoint layers.** A fixed kernel supported in a neighborhood of zero rather than at the endpoint point is not covered by the point-support theorem. `WP-122` handles broad zero-order positive Radon geometries of this type, while `WP-123` handles finite-order local differential versions.

**Cutoff-synchronized layers.** A family whose width continues to shrink as `1/log X` while the tested prime shell moves to `X` is not one fixed bilinear form and is outside the premise, exactly as in `WP-123`.

**Analytic/Gevrey or hyperfunction topology.** These categories can support infinite-order point-local functionals because they are not ordinary distributions on smooth tests. They are genuine remaining categories, but adopting one requires an independently forced Mathia analytic structure and a new sign/domain theorem; merely writing an infinite derivative series is not inherited geometric positivity.

**Off-critical attenuation.** As in `WP-123`, for fixed derivative order and `sigma>1` the multiplicative shell coefficient decays. The critical failure is therefore not a tautology of endpoint support alone; it comes from combining the automatic finite-order classification with the exact `sigma=1/2` prime density.

## 6. Prior-art and novelty audit

No theorem-level novelty is claimed for the analytic classification. The Schwartz kernel theorem is the classical bridge from continuous bilinear forms on test functions to distribution kernels. The structure theorem that a distribution supported at one point is a finite sum of derivatives of the Dirac mass is classical; a standard reference is Lars Hörmander, *The Analysis of Linear Partial Differential Operators I*, Springer, 2nd ed., Theorem 2.3.4. The familiar distinction between point-supported distributions and larger analytic/hyperfunction categories is precisely why infinite-order point functionals require stronger test-function topologies.

A targeted literature search found the standard kernel and point-support theorems, but no external result that turns an infinite-order analytic endpoint functional of the Gamma--Schoenberg carrier into the global Weil quadratic form with an RH-independent sign theorem. The abstract distributional step is therefore classical. The Mathia-specific durable consequence is narrower and exact:

\[
\boxed{
\text{ordinary smooth endpoint locality}
+\text{continuity}
+\text{positivity}
\Longrightarrow
\text{finite jet}
\xRightarrow{\mathrm{WP\text{-}123}}
\text{critical obstruction}.
}
\tag{24}
\]

This materially narrows the live boundary after `WP-123`: a purported infinite-order **local** rescue must first justify why Mathia has left ordinary smooth/distributional geometry at all. Nonlocal fractional kernels, analytically forced scales, and genuinely nonseparable finite--archimedean structures remain open and require separate tests.