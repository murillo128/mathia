# XF-027 — normalized block discriminant has square production and affine exterior cancellation

**Status:** `EXACT-DERIVED` + `CLASSICAL-STIELTJES-STRUCTURE` + `CANDIDATE-BARRIER` + `STRUCTURAL/BOUNDARY`. XF-026 shows that the repeated collision poles of fixed ordered-gap mean removers are not intrinsic to logarithmic repulsion: a root-symmetric observable can have a much better wall structure. There is an exact finite-block functional that removes both translation and scale without introducing a fixed reference spacing. Its internal log-repulsion production is a perfect square, and its coupling to the exterior is blind not only to constant drift but to the entire affine part of the exterior field.

For a block `I` of `n>=2` distinct real roots, write

\[
m=\frac1n\sum_{i\in I}x_i,
\qquad
y_i=x_i-m,
\qquad
V=\sum_{i\in I}y_i^2,
\qquad
N=\binom n2,
\]

and define the scale-free log discriminant

\[
\boxed{
\mathcal J_I
:=
\log\prod_{i<j\in I}(x_i-x_j)^2
-N\log V.
}
\]

Let

\[
b_i:=\sum_{\substack{j\in I\\j\ne i}}\frac1{x_i-x_j},
\qquad
\alpha:=\frac NV,
\qquad
q_i:=b_i-\alpha y_i.
\]

If the full zero velocity is decomposed as

\[
x_i'=2(b_i+e_i),
\]

where `e_i` is the field of roots outside `I`, then

\[
\boxed{
\mathcal J_I'
=4\sum_{i\in I}q_i^2
+4\sum_{i\in I}q_i e_i.
}
\]

The shape gradient `q` satisfies the two exact moment cancellations

\[
\boxed{
\sum_iq_i=0,
\qquad
\sum_i y_iq_i=0.
}
\]

Consequently only the non-affine part of the exterior field contributes. If

\[
\bar e=\frac1n\sum_i e_i,
\qquad
\beta=\frac{\sum_i y_i e_i}{V},
\qquad
e_i^\perp=e_i-\bar e-\beta y_i,
\]

then

\[
\boxed{
\mathcal J_I'
=4\left\|q+\frac12e^\perp\right\|_2^2
-\|e^\perp\|_2^2
\ge -\|e^\perp\|_2^2.
}
\]

Thus an exactly affine exterior field leaves the finite-block monotonicity intact. A single distant exterior root contributes only at cubic order after the two canceled moments: for `z` outside the block,

\[
\boxed{
\sum_i\frac{q_i}{x_i-z}
=
\frac1{(m-z)^2}
\sum_i\frac{q_i y_i^2}{x_i-z}.
}
\]

This is a sharper localization interface than raw endpoint velocity or centered-gap leakage. It does **not** yet give an upper bound for `Lambda`: a root immediately outside a hard block can still create a negative singular flux. The gain is that the far field enters only through its curvature across the block, while constant and linear components cancel exactly.

## 1. The scale-free discriminant is a shape observable

Let `I` contain `n>=2` real distinct roots. Set

\[
\Delta_I^2:=\prod_{i<j\in I}(x_i-x_j)^2.
\tag{1}
\]

Under an affine change `x_i -> a x_i+b`, `a\ne0`, one has

\[
\Delta_I^2\mapsto |a|^{2N}\Delta_I^2,
\qquad
V\mapsto a^2V.
\]

Therefore

\[
\boxed{\mathcal J_I=\log\Delta_I^2-N\log V}
\tag{2}
\]

is invariant under translation and nonzero rescaling. Unlike the centered gap energies of XF-021--XF-025, it does not choose a reference gap, a fixed index taper, or a preferred physical length. It is symmetric under every permutation of the roots inside `I`.

The price is deliberate singularity: if two roots inside `I` collide, `\mathcal J_I -> -\infty`. Thus this is not in the smooth `C^2` class of XF-026. It belongs to the other escape class identified there: a symmetric collision barrier whose singularity has a controlled sign rather than a smooth removable pole.

## 2. Its gradient is the non-affine part of the internal Stieltjes field

Define the internal logarithmic field

\[
b_i:=\sum_{\substack{j\in I\\j\ne i}}\frac1{x_i-x_j}.
\tag{3}
\]

Differentiating the two pieces of (2) gives

\[
\frac{\partial}{\partial x_i}\log\Delta_I^2=2b_i,
\qquad
\frac{\partial V}{\partial x_i}=2y_i,
\tag{4}
\]

so with `\alpha=N/V`,

\[
\boxed{
\frac12\nabla\mathcal J_I=q,
\qquad
q_i=b_i-\alpha y_i.
}
\tag{5}
\]

Two pairwise identities now remove the translation and dilation directions. First,

\[
\sum_i b_i=0
\tag{6}
\]

because each pair contributes opposite reciprocals. Second,

\[
\begin{aligned}
\sum_i y_i b_i
&=\sum_{i<j}\frac{y_i-y_j}{x_i-x_j}\\
&=\sum_{i<j}1
=N.
\end{aligned}
\tag{7}
\]

Since `\sum_i y_i=0` and `\alpha V=N`, equations (5)--(7) give

\[
\boxed{
\langle q,\mathbf 1\rangle=0,
\qquad
\langle q,y\rangle=0.
}
\tag{8}
\]

So `q` is literally the shape component of the internal reciprocal field after projecting away the two affine symmetry directions.

## 3. Pure internal log repulsion produces an exact square

First take the finite matched control in which the block is the entire real-rooted polynomial system, so there is no exterior field. The backward-heat root flow is

\[
x_i'=2b_i.
\tag{9}
\]

Using (5),

\[
\mathcal J_I'
=\sum_i 2q_i\,2b_i
=4\langle q,b\rangle.
\tag{10}
\]

But `b=q+\alpha y`, and `q\perp y` by (8). Hence

\[
\boxed{
\mathcal J_I'=4\|q\|_2^2\ge0.
}
\tag{11}
\]

This is stronger than a sign estimate: the production is exactly the squared shape-gradient norm. The radial expansion of the cloud contributes nothing to the scale-free entropy.

Equality has the classical Hermite/Stieltjes form. If `q=0`, then

\[
b_i=\alpha y_i
\qquad(i\in I).
\tag{12}
\]

For the monic polynomial `P(z)=\prod_i(z-y_i)`, the standard root identity gives

\[
\frac{P''(y_i)}{P'(y_i)}=2b_i=2\alpha y_i.
\tag{13}
\]

Therefore the polynomial

\[
P''(z)-2\alpha zP'(z)+2\alpha nP(z)
\tag{14}
\]

has degree at most `n-1` and vanishes at all `n` distinct roots, so it is identically zero. After the rescaling `u=\sqrt\alpha\,z`, this is the physicists' Hermite equation. Thus the equality configurations are exactly affine rescalings of the `n` Hermite roots. Conversely those roots satisfy (12).

Equivalently, on the centered fixed-variance shape sphere, `\mathcal J_I` is bounded above and its interior maximizer is the Hermite configuration; collision faces have value `-\infty`. This is the classical Stieltjes--Fekete electrostatic structure, not an Xi-specific discovery.

## 4. In the full system only the non-affine exterior field survives

Return to a finite block inside a larger logarithmic-repulsion system. On an Xi real-simple slice, interpret the root velocities with the same Rodgers--Tao principal-value convention used in XF-014. Write

\[
e_i:=\sum_{k\notin I}'\frac1{x_i-x_k},
\tag{15}
\]

so that

\[
x_i'=2(b_i+e_i).
\tag{16}
\]

The same gradient calculation gives

\[
\begin{aligned}
\mathcal J_I'
&=4\langle q,b+e\rangle\\
&=\boxed{4\|q\|_2^2+4\langle q,e\rangle}.
\end{aligned}
\tag{17}
\]

Now project `e` onto the span of the constant vector and the centered position vector. Define

\[
\bar e=\frac1n\sum_i e_i,
\qquad
\beta=\frac{\langle e,y\rangle}{V},
\qquad
e^\perp=e-\bar e\,\mathbf1-\beta y.
\tag{18}
\]

By (8),

\[
\langle q,e\rangle=\langle q,e^\perp\rangle.
\tag{19}
\]

Completing the square in (17) therefore yields

\[
\boxed{
\mathcal J_I'
=4\left\|q+\frac12e^\perp\right\|_2^2
-\|e^\perp\|_2^2
\ge-\|e^\perp\|_2^2.
}
\tag{20}
\]

This is the main structural gain. The exterior does not enter through its absolute size, its mean drift, or its best linear trend across the block. Only its **failure to be affine on the block** can drive `\mathcal J_I` downward.

In particular, a constant exterior field merely translates the block, while a linear exterior field changes its scale to first order; both are invisible to an affine-invariant shape functional. Equation (20) makes that geometric statement exact for the logarithmic zero flow.

## 5. A distant exterior root has exact cubic leakage

The affine cancellation has an exact one-root form. Let `z` be an exterior root and put `a=m-z`. For `x_i=m+y_i`, the elementary identity

\[
\frac1{a+y_i}
=
\frac1a-\frac{y_i}{a^2}
+\frac{y_i^2}{a^2(a+y_i)}
\tag{21}
\]

combined with (8) gives

\[
\boxed{
\sum_i\frac{q_i}{x_i-z}
=
\frac1{(m-z)^2}
\sum_i\frac{q_i y_i^2}{x_i-z}.
}
\tag{22}
\]

Thus the constant `1/(m-z)` and linear `-(x_i-m)/(m-z)^2` pieces cancel identically. The first surviving multipole is quadratic in the block coordinate.

Let

\[
r:=\max_i|y_i|.
\]

If `|m-z|>=2r`, then `|x_i-z|>=|m-z|/2`, so Cauchy--Schwarz gives

\[
\begin{aligned}
\left|\sum_i\frac{q_i}{x_i-z}\right|
&\le
\frac{2}{|m-z|^3}\sum_i|q_i|y_i^2\\
&\le
\boxed{
\frac{2\|q\|_2 V}{|m-z|^3}
}.
\end{aligned}
\tag{23}
\]

For a collection `Z` of exterior roots all satisfying the same separation,

\[
\boxed{
|\langle q,e_Z\rangle|
\le
2\|q\|_2V
\sum_{z\in Z}\frac1{|m-z|^3}.
}
\tag{24}
\]

The cubic tail is absolutely summable for the Xi zero-location scale `|x_k|\asymp |k|/\log|k|`. This is qualitatively stronger than controlling the raw reciprocal exterior field, which is only principal-value summable. It also meshes with XF-020: once a physical buffer separates the core from the far exterior, the existing global counting law is more than strong enough to estimate the cubic tail. What is **not** yet proved is that the resulting error is small relative to the shape production on every relevant Xi block; the factors `V` and `\|q\|` and the near exterior still matter.

## 6. A hard block still has a real negative boundary spike

The affine cancellation does not remove a root that approaches immediately from outside the selected membership set. There is an exact four-particle counterexample.

Take the full ordered configuration

\[
-\delta<0<1<3,
\qquad \delta>0,
\]

and choose the consecutive three-root block

\[
I=\{0,1,3\}.
\]

For this block,

\[
m=\frac43,
\qquad
V=\frac{14}{3},
\qquad
N=3,
\]

and direct evaluation of (5) gives

\[
q=
\left(-\frac{10}{21},\frac57,-\frac5{21}\right),
\qquad
\|q\|_2^2=\frac{50}{63}.
\tag{25}
\]

The single exterior root `-\delta` contributes

\[
e=
\left(\frac1\delta,
\frac1{1+\delta},
\frac1{3+\delta}\right),
\]

with

\[
\langle q,e\rangle
=-\frac{10}{7\delta(\delta+1)(\delta+3)}.
\tag{26}
\]

Hence (17) becomes

\[
\boxed{
\mathcal J_I'
=
\frac{40(5\delta^3+20\delta^2+15\delta-9)}
{63\delta(\delta+1)(\delta+3)}.
}
\tag{27}
\]

In particular,

\[
\mathcal J_I'
=-\frac{40}{21\delta}+O(1)
\qquad(\delta\downarrow0).
\tag{28}
\]

So a hard membership boundary can still create an arbitrarily large negative derivative. This falsifies the strongest possible interpretation of (11): normalized discriminant is **not** a universal Lyapunov function for arbitrary sub-blocks of a larger system. The improvement is specifically that the dangerous exterior information has been compressed to a non-affine field residual, with cubic decay for distant roots.

## 7. Relation to XF-026 and the previous mean-removal no-go results

XF-021--XF-025 showed that several natural fixed-index centered energies pay for mean removal with collision-positive `1/epsilon` boundary spikes. XF-026 then identified their common coefficient as failure of reflection smoothness at a root-exchange wall and suggested physical-coordinate permutation symmetry or a deliberately singular barrier.

`\mathcal J_I` realizes the second option. Inside the selected block it is fully permutation symmetric and its collision singularity is the logarithmic discriminant itself; under pure internal repulsion, that singularity contributes to the **positive** square production (11). Translation and scale are removed geometrically rather than by subtracting a local gap mean.

The counterexample (27) also pinpoints what has not been solved. The observable is symmetric under permutations **inside** `I`, but a root crossing the membership boundary changes which particles participate in the discriminant. That boundary is not reflection-smooth. Any genuine localization built from `\mathcal J_I` must therefore smooth, average, or cancel membership changes rather than assume that the hard block itself is monotone.

## 8. Prior art and novelty boundary

The Stieltjes electrostatic characterization of Hermite zeros and the Fekete/logarithmic-energy interpretation of classical orthogonal-polynomial zeros are classical. A targeted audit against modern Stieltjes--Fekete literature, including Bertola, Chavez Heredia and Grava, **The Stieltjes--Fekete Problem and Degenerate Orthogonal Polynomials**, *International Mathematics Research Notices* 2024:11 (2024), 9114--9141, DOI `10.1093/imrn/rnae037`, confirms that the Hermite equilibrium aspect belongs to established theory. No novelty is claimed for equations (12)--(14), for scale-normalized Vandermonde optimization, or for viewing logarithmic repulsion as a gradient flow.

No external theorem is load-bearing in this finding. Equations (4)--(24) are finite algebra from the Rodgers--Tao root law already anchored in `SOURCES.md`; the Hermite equality classification is rederived from the polynomial differential equation. The literature audit is used only to set the novelty boundary, so no new source anchor is required for the proof.

The durable contribution for `xi_flow` is the exact **block-flow decomposition** (17)--(20) together with the two-moment exterior cancellation (22). It converts the unresolved mean-removal problem from “control singular centered conductances or endpoint velocities” into the more invariant question “control the non-affine part of the exterior reciprocal field seen by a scale-free symmetric block shape.”

## 9. Consequence for `xi_flow`

This result supplies a new constructive target after XF-026. A promising localization should preserve the internal normalized-discriminant square production while eliminating the hard membership spike of (27), for example through a physical-coordinate symmetric weighting or a signed combination of overlapping blocks. The first audit for such a construction is now exact: verify that constant and linear exterior fields cancel, then quantify only the residual curvature field.

The far exterior is no longer the first-order obstacle. Equation (22) forces a cubic tail after affine projection, so the super-mesoscopic spatial room certified in XF-020 is compatible with strong far-field decay without any pointwise lower-gap hypothesis. The live obstruction is the **near boundary and membership transition**, plus the absence of an Xi-specific lower bound tying the square production `\|q\|_2^2` to the remaining exterior residual.

Accordingly XF-027 does not claim a new bound on `Lambda`, collision exclusion, or an Xi-specific selector. It sharpens the proof obligation: if a future barrier can make block membership reflection-smooth while retaining (20), the only source-facing leakage left is a second-order spatial variation of the exterior zero field rather than its full singular magnitude.