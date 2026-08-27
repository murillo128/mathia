# PF-085 — the canonical Grunsky–Schiffer completion is trace-class and does not carry the quarter-plane threshold

**Status:** `EXACT-BRIDGE` + `DECISIVE-NEGATIVE` for the most direct interior/exterior Fredholm realization of PF-084. The exact prime-circle/projective-reference deformation has a canonical classical Grunsky–Schiffer kernel whose rectangle integrals recover the exact finite-block geodesic-length defect. However, its prime-cell compression is trace class and its all-block interaction is absolutely summable. Therefore the `Re s = 1/4` threshold of PF-084 does **not** come from the canonical conformal/potential-theoretic Fredholm operator. Any operator realization of PF-084 must contain genuinely dynamical long-block propagation in addition to endpoint conformal distortion.

## 1. The exact endpoint map is an exterior univalent map

Recall the exact endpoint map

\[
V(z)=\pi\cot\frac{\pi}{z}.
\]

It has the expansion at infinity

\[
V(z)=z-\frac{\pi^2}{3z}-\frac{\pi^4}{45z^3}+O(z^{-5}).
\]

All finite poles of `V` occur at `z=1/k`. Moreover,

\[
V(z_1)=V(z_2)
\quad\Longrightarrow\quad
\frac1{z_1}-\frac1{z_2}\in\mathbb Z.
\]

Hence `V` is holomorphic and univalent on every exterior domain `|z|>R` with `R>2`. In particular the tail of the prime endpoint sequence lies inside a standard exterior-univalent setting; finitely many initial endpoints are irrelevant to the summability statements below.

Thus the exact-vs-projective comparison has a canonical classical Grunsky object. Define

\[
F_V(z,w)
:=
\log\frac{V(w)-V(z)}{w-z}
\]

and its mixed derivative

\[
\boxed{
\mathcal K_V(z,w)
:=
\partial_z\partial_wF_V(z,w)
=
\frac{V'(z)V'(w)}{(V(w)-V(z))^2}
-
\frac1{(w-z)^2}.
}
\]

This is the standard Grunsky/Schiffer kernel measuring deviation from a Möbius map.

## 2. For `V=pi cot(pi/z)` the kernel is explicit and positive

For real `x,y>2`, put

\[
\delta=\pi\left(\frac1x-\frac1y\right).
\]

The cotangent difference identity and

\[
V'(x)=\frac{\pi^2}{x^2}\csc^2\frac{\pi}{x}
\]

give the exact formula

\[
\boxed{
\mathcal K_V(x,y)
=
\frac{\pi^2}{x^2y^2}
\left(
\csc^2\delta-\frac1{\delta^2}
\right).
}
\]

The bracket has the continuous value `1/3` at `delta=0`. Since for `x,y>2` one has `|delta|<pi/2`,

\[
0<\csc^2\delta-\delta^{-2}\le C.
\]

Consequently

\[
\boxed{
0<\mathcal K_V(x,y)\le\frac{C}{x^2y^2}.
}
\]

On the diagonal,

\[
\boxed{
\mathcal K_V(x,x)
=\frac{\pi^2}{3x^4}
=\frac16 S(V)(x),
}
\]

exactly matching the Schwarzian found in PF-082.

There is also a useful exact factorization before differentiating:

\[
\frac{V(y)-V(x)}{y-x}
=
\frac{\pi/x}{\sin(\pi/x)}
\frac{\pi/y}{\sin(\pi/y)}
\frac{\sin\delta}{\delta}.
\]

The first two factors are one-endpoint terms. Only the last factor survives a mixed derivative or a four-endpoint cross-ratio. This isolates the genuinely relational part of the exact-circle defect.

## 3. Rectangle integrals are exactly finite-block geodesic defects

Take

\[
a<b<c<d
\]

and define the reference cross-ratio used by the prime-flute block separator

\[
\chi_0
=
\frac{(c-b)(d-a)}{(b-a)(d-c)},
\qquad
L_0=4\operatorname{arsinh}\sqrt{\chi_0}.
\]

Let `chi_E,L_E` be the same quantities after replacing every endpoint by `V(endpoint)`.

Define the complementary cross-ratio

\[
r
:=
\frac{(d-b)(c-a)}{(d-a)(c-b)}.
\]

Elementary cross-ratio algebra gives

\[
r=\frac{1+\chi}{\chi}
=\coth^2\frac L4.
\]

Integrating the mixed derivative over the two endpoint intervals gives

\[
\begin{aligned}
\int_a^b\int_c^d\mathcal K_V(x,y)\,dy\,dx
&=F_V(b,d)-F_V(a,d)-F_V(b,c)+F_V(a,c)\\
&=\log\frac{r_E}{r_0}.
\end{aligned}
\]

Therefore

\[
\boxed{
\int_a^b\int_c^d\mathcal K_V(x,y)\,dy\,dx
=
2\log
\frac{\tanh(L_0/4)}{\tanh(L_E/4)}.
}
\]

This is an exact bridge between the original prime-circle endpoint deformation and an actual closed-geodesic observable of the hyperbolic flute.

Because `K_V>0`, it also gives the global inequality

\[
\boxed{L_E<L_0}
\]

for every ordered four-endpoint block in the tail. Thus the exact cotangent geometry shortens every canonical block separator relative to its projective tangent reference, not merely asymptotically.

## 4. The canonical prime-cell compression is trace class

Let

\[
I_n=[p_n,p_{n+1}],
\qquad
g_n=p_{n+1}-p_n,
\]

and use the normalized cell indicators

\[
e_n=g_n^{-1/2}\mathbf 1_{I_n}.
\]

Compress the real Schiffer kernel to this canonical prime partition:

\[
A_{mn}
:=
\langle e_m,\mathcal K_V e_n\rangle
=
\frac1{\sqrt{g_mg_n}}
\int_{I_m}\int_{I_n}\mathcal K_V(x,y)\,dy\,dx.
\]

The pointwise bound above implies

\[
|A_{mn}|
\le
C
\frac{\sqrt{g_mg_n}}{p_m^2p_n^2}.
\]

Bertrand gives `g_n<p_n`, hence

\[
\sum_n\frac{\sqrt{g_n}}{p_n^2}
\le
\sum_n p_n^{-3/2}
<\infty.
\]

Therefore

\[
\boxed{
\sum_{m,n}|A_{mn}|<\infty,
}
\]

so the compressed operator is trace class on `ell^2`. In particular

\[
\det(I+zA)
\]

is an ordinary entire Fredholm determinant in the auxiliary coupling `z`; no regularization or convergence wall is needed.

The unnormalized all-block rectangle interactions are even more directly summable. From

\[
\left|
\int_{I_m}\int_{I_n}\mathcal K_V
\right|
\le
C\frac{g_mg_n}{p_m^2p_n^2}
\]

and Bertrand,

\[
\frac{g_n}{p_n^2}
\le
2\left(\frac1{p_n}-\frac1{p_{n+1}}\right),
\]

so

\[
\boxed{
\sum_n\frac{g_n}{p_n^2}<\infty
}
\]

by telescoping, and hence the double sum of all rectangle defects converges absolutely.

## 5. Why this kills the most direct Fredholm explanation of PF-084

PF-084 found a sharp ordinary-Euler-product threshold

\[
\operatorname{Re}s=\frac14
\]

for

\[
\mathcal R_{\rm rel}^{\rm block}(s)
=
\prod_{m<n}
\frac{1-e^{-sL^E_{m,n}}}
     {1-e^{-sL^0_{m,n}}}.
\]

For fixed left endpoint and a far right endpoint,

\[
L_E-L_0\to\text{nonzero constant},
\]

so at the boundary `s=1/4` the Ruelle logarithm has the slow decay

\[
\asymp e^{-L_0/4}
\asymp
\frac{\sqrt{g_n}}{p_n},
\]

which is large enough to contain the divergent prime harmonic tail.

The canonical Grunsky/Schiffer interaction behaves differently. Since

\[
r=\coth^2(L/4)=1+\frac1\chi,
\]

the rectangle defect has long-block decay of order

\[
\boxed{
\log(r_E/r_0)=O(\chi^{-1})=O(e^{-L_0/2}).
}
\]

For a fixed left cell this is

\[
O\left(\frac{g_n}{p_n^2}\right),
\]

which is summable.

Thus the two mechanisms differ by exactly the decay that matters:

\[
\boxed{
\begin{array}{rcl}
\text{canonical conformal/Schiffer coupling}
&:& e^{-L/2}\quad\text{(summable)},\\[1mm]
\text{PF-084 boundary Ruelle weight}
&:& e^{-L/4}\quad\text{(critical/non-summable)}.
\end{array}
}
\]

Therefore the quarter-plane threshold cannot be attributed to the canonical Grunsky/Schiffer Fredholm operator associated with the exact endpoint map, nor to its natural prime-cell compression.

This does **not** rule out every possible Fredholm realization of PF-084. It rules out the most direct one suggested by the exact circle/projective-reference deformation and the interior/exterior harmonic duality. If PF-084 has an intrinsic operator realization, the missing ingredient must be a dynamical propagator or branching mechanism that contributes the slower `e^{-sL}` long-block weight; endpoint conformal distortion alone is too trace-class.

## 6. Interior/exterior duality is preserved, not discarded

This negative result does not arise by quotienting away the ambient two-sided geometry. The Grunsky/Schiffer kernel is precisely a classical potential-theoretic object coupling the two conformal sides of a boundary, and its definition is Möbius/projectively natural.

The rectangle identity is entirely in cross-ratios. Applying the ambient inversion that exchanges the two orthogonal-circle sides conjugates the same kernel/cross-ratio data and leaves the block defect unchanged.

So the failure is informative: **even the canonical operator that most faithfully packages the interior/exterior projective defect is too regular to generate PF-084's nontrivial abscissa.**

## 7. Prior-art / novelty audit

The general operator theory here is classical, not a new Mathia construction:

- Grunsky coefficients are defined from `log((f(z)-f(w))/(z-w))`, and the mixed derivative above is the standard Grunsky/Schiffer kernel.
- Schiffer, Grunsky and later operator-theoretic formulations connect these kernels with interior/exterior potential theory.
- Takhtajan--Teo prove Hilbert--Schmidt properties for Grunsky operators in the Weil--Petersson class and identify the universal Liouville action with a Fredholm determinant associated with the quasicircle.
- Johansson and later work relate Grunsky Fredholm determinants to planar spectral/conformal functionals.
- Fan--Viklund--Wang (2026) construct an operator directly from Fourier coefficients of `log |(phi(z)-phi(w))/(z-w)|`, relate it to single-layer potential/composition operators, characterize the Weil--Petersson class by Hilbert--Schmidt behavior, and express Loewner energy by Fredholm determinants.

Therefore no novelty is claimed for the existence of a Grunsky/Schiffer/Fredholm formalism itself. The project-specific exact content is the specialization to

\[
V(z)=\pi\cot(\pi/z),
\]

the closed form for `K_V`, the exact rectangle-to-prime-flute-length identity, the positivity/shortening statement, and the trace-class summability comparison with PF-084.

The main research value is negative: **known canonical conformal Fredholm machinery absorbs the exact-circle defect too efficiently and therefore cannot explain the new `1/4` Ruelle threshold.**

## 8. Research consequence

Do not identify PF-084 with a Grunsky, Schiffer, Kerzman--Stein, single-layer, Loewner-energy, or directly associated conformal Fredholm determinant merely because all of them are built from the same endpoint map and cross-ratio distortion. Their natural kernel has `e^{-L/2}` long-block decay and is trace-class after prime compression.

The remaining meaningful operator-realization question is narrower:

\[
\boxed{
\text{Can a geometrically forced relative dynamical/transfer operator}
\text{ combine the trace-class endpoint defect with }e^{-sL}
\text{ propagation, without reintroducing the PF-035/PF-075 divergence?}
}
\]

A positive answer would genuinely go beyond classical conformal Fredholm theory. A negative answer would demote PF-084 to a canonical but selected geometric Euler-product sector.

## Lean / symbolic candidates

1. Formalize the cotangent divided-difference factorization.
2. Prove the explicit kernel identity and diagonal limit `K_V(x,x)=S(V)(x)/6`.
3. Formalize the rectangle mixed-derivative identity and `r=coth(L/4)^2`.
4. Deduce `L_E<L_0` from positivity of `csc(delta)^2-delta^-2`.
5. Formalize the Bertrand telescoping estimate `g_n/p_n^2 <= 2(1/p_n-1/p_{n+1})` and the resulting absolute summability.