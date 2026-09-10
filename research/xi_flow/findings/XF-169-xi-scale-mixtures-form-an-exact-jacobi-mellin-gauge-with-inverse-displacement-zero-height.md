---
type: negative
research_line: xi_flow
finding_id: XF-169
status: canonical
---

# XF-169 — Xi scale mixtures form an exact Jacobi–Mellin gauge with inverse displacement zero height

**Evidence classification:** `EXACT-DERIVED + CLASSICAL-TRANSFORM`. The Mellin scaling and Fourier translation identities used below are classical. The durable line-specific result is the exact classification of the Xi log-scale shift mixtures that preserve the normalized Riemann/Jacobi functional equation, the identification of their entire Mellin multiplier with the time-zero zero multiplier, and the resulting inverse law between the explicit support displacement of XF-167 and the height at which its first added nonreal zero appears. No claim is made that the general transform identities themselves are new.

## Statement

XF-167 exhibited one three-point positive mixture of translated Xi sources that preserves positivity, complete monotonicity and real-axis Jacobi reciprocity while introducing nonreal zeros. XF-168 then showed that exact support on the single lattice `pi n^2` removes all coefficient freedom by Hamburger rigidity. The missing quantitative issue is what happens between these endpoints when the square lattice is moved by a small multiplicative amount.

There is an exact gauge behind the XF-167 construction.

Let

\[
F_\Xi(x)=\sum_{n\ge1}e^{-\pi n^2x},
\qquad
S_\Xi(u)=e^uF_\Xi(e^{4u}),
\qquad
\Phi(u)=\frac18(S_\Xi''(u)-S_\Xi(u)).
\tag{1}
\]

For a finite positive compactly supported measure `nu` on `R`, define

\[
S_\nu(u):=\int S_\Xi(u+a)\,d\nu(a),
\tag{2}
\]

\[
F_\nu(x):=x^{-1/4}S_\nu\!\left(\frac14\log x\right)
=\int e^aF_\Xi(e^{4a}x)\,d\nu(a),
\tag{3}
\]

and `Theta_nu(x)=1+2F_nu(x)`. Its Mellin multiplier is

\[
\boxed{
M_\nu(s):=\int e^{(1-2s)a}\,d\nu(a).
}
\tag{4}
\]

Within this Xi shift-mixture class, the following are equivalent:

1. `Theta_nu` satisfies the standard Jacobi law
   \[
   \Theta_\nu(x)=x^{-1/2}\Theta_\nu(1/x);
   \tag{5}
   \]
2. the completed Mellin transform has the standard Riemann symmetry and residue normalization;
3. `nu` is even and
   \[
   \boxed{\int\cosh a\,d\nu(a)=1.}
   \tag{6}
   \]

For every such normalized even `nu`, the associated source

\[
\rho_\nu(u):=\int\Phi(u+a)\,d\nu(a)
\tag{7}
\]

is even and positive, `F_nu` is completely monotone, and the completed Mellin transform factorizes exactly as

\[
\boxed{
\mathcal Z_\nu(s)=M_\nu(s)\mathcal Z(s),
\qquad
\mathcal Z(s):=\pi^{-s/2}\Gamma(s/2)\zeta(s).
}
\tag{8}
\]

The functional equation sees only the self-reciprocity

\[
\boxed{M_\nu(s)=M_\nu(1-s),\qquad M_\nu(0)=M_\nu(1)=1.}
\tag{9}
\]

At time zero, however, exactly the same multiplier controls the added zero geometry. With the source extended evenly to the real line,

\[
\boxed{
H_0^{(\nu)}(z)
=m_\nu(z)H_0(z),
\qquad
m_\nu(z):=\int\cos(az)\,d\nu(a)
=M_\nu\!\left(\frac12+\frac{iz}{2}\right).
}
\tag{10}
\]

Thus the freedom invisible to the normalized Riemann functional equation is not spectrally inert: zeros of the self-reciprocal entire factor `M_nu` transfer directly to zeros of the time-zero Xi-flow transform.

For the explicit XF-167 family

\[
\nu_c=\frac12\delta_0+
\frac{1}{4\cosh c}(\delta_c+\delta_{-c}),
\qquad c>0,
\tag{11}
\]

one obtains

\[
\boxed{
M_c(s)
=\frac{\cosh c+\cosh(c(1-2s))}{2\cosh c}
}
\tag{12}
\]

and

\[
M_c(s)=0
\iff
s\in
\left\{-\frac{(2k+1)\pi i}{2c},
1-\frac{(2k+1)\pi i}{2c}:k\in\mathbb Z\right\}.
\tag{13}
\]

The corresponding time-zero added zeros are exactly

\[
\boxed{
z=\frac{(2k+1)\pi}{c}\pm i.}
\tag{14}
\]

Meanwhile the inverse-Laplace support is displaced from `pi n^2` by log-scale amounts `0,+4c,-4c`. If

\[
\delta:=4c,
\tag{15}
\]

is the maximal nonzero logarithmic lattice displacement, the first added zero has real height

\[
\boxed{T_{\rm zero}=\frac\pi c=\frac{4\pi}{\delta}.}
\tag{16}
\]

So arbitrarily small support displacement is compatible with an `O(1)` violation of real-rootedness, but the violation is forced out to inverse-displacement height in this exact stress family. This is the scale sensitivity that any quantitative strengthening of XF-168 must see.

## 1. Shift averaging is multiplicative convolution in the theta variable

Put `x=e^(4u)`. From `(1)`,

\[
x^{-1/4}S_\Xi(u+a)
=e^aF_\Xi(e^{4a}x),
\tag{17}
\]

which proves `(3)`. Expanding `F_Xi` gives

\[
F_\nu(x)
=\sum_{n\ge1}\int
 e^a e^{-\pi n^2e^{4a}x}\,d\nu(a).
\tag{18}
\]

Hence `F_nu` is a positive Laplace superposition and is completely monotone. Its representing measure is the push-forward mixture

\[
\mu_\nu
=\sum_{n\ge1}\int
 e^a\,\delta_{\pi n^2e^{4a}}\,d\nu(a).
\tag{19}
\]

This formula makes the support geometry explicit: translation by `a` in the Xi source coordinate is multiplicative displacement by `e^(4a)` of every square-lattice atom.

For `Re(s)>1`, the Mellin transform of `(17)` gives

\[
\begin{aligned}
\mathcal Z_\nu(s)
&:=\int_0^\infty F_\nu(x)x^{s/2}\,\frac{dx}{x}\\
&=\int e^{(1-2s)a}\,d\nu(a)
   \int_0^\infty F_\Xi(y)y^{s/2}\,\frac{dy}{y}\\
&=M_\nu(s)\mathcal Z(s),
\end{aligned}
\tag{20}
\]

proving `(8)` first in the half-plane of absolute convergence and then meromorphically. This is just the classical Mellin scaling rule, but here it identifies exactly what the scaled-lattice contamination does to the completed zeta factor.

## 2. The normalized functional equation classifies the shift measure

Suppose first that `nu` is even. Then

\[
M_\nu(1-s)
=\int e^{(2s-1)a}\,d\nu(a)
=M_\nu(s),
\tag{21}
\]

and

\[
M_\nu(0)=M_\nu(1)
=\int\cosh a\,d\nu(a).
\tag{22}
\]

Thus `(6)` implies `(9)`. Since `mathcal Z(s)=mathcal Z(1-s)`, equation `(8)` gives the standard completed functional equation and the residue at `s=1` remains one.

The same conditions also give Jacobi reciprocity directly. The Xi prekernel identity from XF-166 is

\[
S_\Xi(v)-S_\Xi(-v)=-\sinh v.
\tag{23}
\]

Evenness of `nu` lets us write

\[
\begin{aligned}
S_\nu(u)-S_\nu(-u)
&=\int\bigl(S_\Xi(u+a)-S_\Xi(-u-a)\bigr)\,d\nu(a)\\
&=-\int\sinh(u+a)\,d\nu(a)\\
&=-\sinh u,
\end{aligned}
\tag{24}
\]

where `(6)` supplies the final coefficient and the odd `sinh a` moment vanishes. The standard change `x=e^(4u)` converts `(24)` into `(5)`.

Conversely, suppose a compact positive shift measure produces the normalized completed Riemann functional equation. Using `(8)` and the nonvanishing of `mathcal Z` on the real half-line `s>1`, analytic continuation gives

\[
M_\nu(s)=M_\nu(1-s)
\qquad(s\in\mathbb C).
\tag{25}
\]

Set `t=1-2s`. Then `(25)` says that the bilateral Laplace transform of `nu` is even:

\[
\int e^{ta}\,d\nu(a)=\int e^{-ta}\,d\nu(a)
\qquad(t\in\mathbb C).
\tag{26}
\]

On the imaginary axis this is equality of the Fourier transforms of `nu` and its reflection. Uniqueness of Fourier transforms of finite measures forces `nu` to be even. The standard residue at `s=1` is one, so `(8)` gives

\[
M_\nu(1)=\int e^{-a}\,d\nu(a)=1.
\tag{27}
\]

Evenness converts `(27)` into `(6)`. Finally, exact Jacobi reciprocity implies the same normalized completed functional equation by the Mellin calculation used in XF-168, so `(5)` also forces `(6)` and evenness. This proves the equivalence.

The conclusion is an exact classification **inside the Xi scale-mixture class**. It is not a classification of all functions satisfying the Riemann functional equation.

## 3. The Mellin gauge and the time-zero zero multiplier are the same entire function

Because `Phi` and `rho_nu` are even when `nu` is even, their cosine transforms are half of their full Fourier transforms. Translation under the full Fourier transform gives

\[
\int_{\mathbb R}\rho_\nu(u)e^{izu}\,du
=\left(\int e^{-iaz}\,d\nu(a)\right)
 \int_{\mathbb R}\Phi(u)e^{izu}\,du.
\tag{28}
\]

Evenness of `nu` makes the first factor `m_nu(z)=int cos(az)dnu(a)`, yielding `(10)`. Substitution into `(4)` gives the second equality in `(10)` exactly.

This dictionary is the central obstruction. Multiplying the completed zeta transform by any `M_nu` from the normalized even shift cone preserves the functional equation because `M_nu` is self-reciprocal. On the critical coordinate used by the Xi flow, however, `M_nu` is literally the multiplier of `H_0`. Functional-equation symmetry therefore cannot distinguish a harmless factor from one carrying new nonreal zeros unless additional arithmetic information excludes the factor.

Hamburger rigidity in XF-168 supplies precisely such additional information by requiring a Dirichlet series on the **single** square lattice. The scale mixture `(19)` leaves that class as soon as nonzero shift mass is present, so no contradiction arises.

## 4. XF-167 gives an exact inverse displacement–zero-height stress law

For `(11)`, direct substitution into `(4)` gives `(12)`. Solving

\[
\cosh(c(1-2s))=-\cosh c
\tag{29}
\]

gives `(13)`, and the coordinate `s=1/2+iz/2` gives `(14)`. Equations `(18)`--`(19)` show at the same time that the three spectral copies are displaced by log amounts `0,+4c,-4c`, proving `(16)`.

The same family quantifies why fixed-height perturbative control is misleading. From `(12)`,

\[
M_c(s)-1
=\frac{\cosh(c(1-2s))-\cosh c}{2\cosh c}.
\tag{30}
\]

Using `|cosh w-1| <= |w|^2 e^{|w|}/2`, for `|1-2s|<=T` one obtains

\[
\boxed{
|M_c(s)-1|
\le
\frac{c^2}{4}
\left(T^2e^{cT}+e^c\right).
}
\tag{31}
\]

In particular, for every fixed Mellin window the normalized completed transform differs from Xi only by `O(c^2)`. More generally,

\[
cT_c\to0
\quad\Longrightarrow\quad
\sup_{|1-2s|\le T_c}|M_c(s)-1|\to0.
\tag{32}
\]

Yet the first zeros of `M_c` occur at imaginary height `pi/(2c)` on the lines `Re(s)=0,1`, and the corresponding nonreal `H_0^(c)` zeros occur at real height `pi/c`. The small-`c` expansion makes the second-order invisibility explicit:

\[
\boxed{
M_c(s)=1+c^2s(s-1)+O_c\bigl(c^4(1+|s|)^4\bigr)
}
\tag{33}
\]

locally uniformly in `s`, equivalently

\[
m_c(z)=1-\frac{c^2}{4}(1+z^2)+O(c^4(1+|z|)^4)
\tag{34}
\]

on fixed `z`-sets. Symmetric support contamination cancels to first order, while its first new zero is only encountered when the observation height reaches the inverse displacement scale.

Equation `(16)` is therefore a falsification boundary for any proposed quantitative source-rigidity theorem: a norm or defect estimate that treats support displacement `delta -> 0` without tracking zero height cannot yield uniform global zero control. To control the transform through a height `T` by such a support-stability principle, this family forces the theorem to resolve at least the regime `delta*T = O(1)`; a purely scale-blind `delta=o(1)` hypothesis is insufficient. This is a necessary sensitivity exposed by the example, not a sufficient condition for real-rootedness.

## Relation to prior findings

XF-162--XF-165 ruled out tail asymptotics and finite source jets as heat-origin anchors. XF-166 showed that real-axis Jacobi inversion and a positive prekernel can be synthesized for unsuitable sources. XF-167 then gave a stronger positive and completely monotone counterexample by mixing three scaled square lattices, while XF-168 proved that exact return to one square lattice restores Hamburger uniqueness of the coefficients.

XF-169 identifies the exact transform mechanism connecting the last two findings. The scaled-lattice freedom is a multiplicative-convolution gauge: log-scale shifts become an entire factor `M_nu`, normalized Jacobi/Riemann symmetry is exactly evenness plus one `cosh` moment in this class, and the critical-coordinate restriction of the same factor transfers its zeros directly into `H_0`. The XF-167 example then turns the qualitative phrase “stability must be height-sensitive” from XF-168 into the exact stress relation `(16)`.

This does **not** solve the source-to-transition bridge. It sharpens what a viable quantitative bridge has to measure.

## Prior-art and novelty audit

The transform ingredients are classical. Mellin transforms diagonalize multiplicative scaling, Fourier transforms diagonalize translation, and the equivalence between zeta functional equations and Poisson/theta reciprocity is the setting of Hamburger's theorem. The existing Kaczorowski--Molteni--Perelli anchor in `SOURCES.md` already records the Hamburger theorem and its connection with uniqueness of Poisson summation. A targeted literature search also located Ehrenpreis--Kawai's 1982 paper *Poisson's Summation Formula and Hamburger's Theorem* and Yoshimoto's generalization, confirming that no novelty should be attributed to the general functional-equation/Poisson viewpoint.

The search did not locate a theorem matching the line-specific package used here: classification of the positive compact Xi log-shift mixtures by the normalized Jacobi/Riemann symmetry, identification of the resulting Mellin factor with the exact time-zero Xi-flow zero multiplier, and the explicit `delta*T_zero=4pi` support-displacement stress law inherited from XF-167. Those consequences are derived elementarily here and need no new external theorem. No new literature item is load-bearing, so `SOURCES.md` is unchanged.

## Falsification boundary

The equivalence above is only for mixtures obtained by translating the Xi prekernel/source in the logarithmic coordinate. There may be other functional-equation-preserving deformations not representable by a positive compact shift measure; XF-169 neither classifies nor excludes them.

The factorization `(10)` is a **time-zero** identity. For positive heat time, multiplication of Fourier transforms does not commute with the backward heat operator, so `H_t^(nu)` is not generally `m_nu H_t`. The finding therefore does not assign a de Bruijn--Newman threshold to a general `nu`. XF-167 remains the explicit member for which a strictly positive threshold was proved using its nonreal seam plus de Bruijn strip contraction.

Equation `(16)` is an exact stress law for the three-point family, not a universal lower bound saying every support perturbation of size `delta` must wait until height `1/delta` to affect zeros. Other perturbations may be better or worse. What the family proves is one-sided: **no scale-blind stability theorem can rule out nonreal zeros globally from small multiplicative support displacement alone.**

Finally, Hamburger rigidity itself remains exact rather than quantitative. Once the support is exactly `pi n^2`, XF-168 identifies the Xi coefficients and the problem returns to RH. The open problem is to find a quantitative hypothesis strong enough to suppress nonconstant self-reciprocal multipliers at the height relevant to the transition without simply assuming the exact Xi source.

## Consequence for `xi_flow`

The next source-side gate should be phrased in a height-dependent form. Instead of asking whether a nearby theta spectrum is globally “close” to the Xi square lattice, seek a bound that couples a spectral displacement/mixture defect to an observation height `T` and then controls the nonconstant multiplier or the corresponding zero geometry through that height. XF-167/XF-169 show that the dimensionless combination `delta*T` is unavoidable for the simplest symmetric contamination.

A promising theorem would therefore have to use more than normalized real-axis Jacobi reciprocity and complete monotonicity: for example, an arithmetic condition that quantitatively suppresses off-lattice mass at resolution `O(1/T)`, or an equivalent complex-modular/Dirichlet constraint whose defect can be propagated to the zero geometry. A theorem depending only on `delta=o(1)` with no height coupling is falsified by `(16)`.