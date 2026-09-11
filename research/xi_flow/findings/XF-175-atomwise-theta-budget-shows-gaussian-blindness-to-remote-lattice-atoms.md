---
type: theorem
research_line: xi_flow
finding_id: XF-175
status: canonical
---

# XF-175 — Atomwise theta budget shows Gaussian blindness to remote lattice atoms

**Evidence classification:** `EXACT-DERIVED + ATOMWISE-STRIP-STABILITY + GAUSSIAN-TAIL-NO-GO`. Starting from the exact theta-shell extraction of XF-166, independently moving and reweighting matched Laplace atoms admits an explicit weighted source budget that controls the whole Fourier transform uniformly on a horizontal strip. Standard Rouche stability then preserves zero counts on any fixed contour whose Xi boundary margin exceeds that budget. The same calculation shows a sharp structural limitation: atoms that remain at spectral scale `lambda ~ pi n^2` become Gaussian-invisible like `exp(-c pi n^2)`. Thus fixed compact zero geometry cannot coerce exact placement of remote square-lattice atoms. No specialized external theorem is load-bearing.

## Statement

Write the Xi square-lattice parameters as

\[
\lambda_n:=\pi n^2,
\qquad n\ge1,
\tag{1}
\]

and define the single prekernel shell extracted by the XF-166 differential operator,

\[
\boxed{
\kappa_\lambda(u)
:=\lambda e^{5u}
\bigl(2\lambda e^{4u}-3\bigr)
 e^{-\lambda e^{4u}},
\qquad u\ge0.
}
\tag{2}
\]

Then on the positive source half-line

\[
\Phi(u)=\sum_{n\ge1}\kappa_{\lambda_n}(u).
\tag{3}
\]

Consider a matched atomwise deformation with positive locations `tilde lambda_n>0` and nonnegative weights `w_n`. Put

\[
a_n:=\frac14\log\frac{\widetilde\lambda_n}{\lambda_n}.
\tag{4}
\]

For a strip width `q>0`, define

\[
\beta_q:=\frac{q+1}{4},
\tag{5}
\]

and the two exact shell costs

\[
\boxed{
K_q(\lambda)
:=\frac14\lambda^{-\beta_q}
\int_\lambda^\infty
 y^{\beta_q}|2y-3|e^{-y}\,dy,
}
\tag{6}
\]

\[
\boxed{
J_q(\lambda)
:=\lambda^{-\beta_q}
\int_\lambda^\infty
 y^{\beta_q}|(2y-1)(y-3)|e^{-y}\,dy.
}
\tag{7}
\]

The matched atomwise strip budget is

\[
\boxed{
\mathfrak B_q
:=\sum_{n\ge1}
\left[
 |w_n-1|K_q(\widetilde\lambda_n)
 +
 \int_{\min(0,a_n)}^{\max(0,a_n)}
 J_q(\lambda_n e^{4r})\,dr
\right].
}
\tag{8}
\]

Whenever `mathfrak B_q<infinity`, the deformed source difference is well defined in the weighted space `L^1(e^(q u)du)` and satisfies

\[
\boxed{
\int_0^\infty e^{qu}
|\widetilde\Phi(u)-\Phi(u)|\,du
\le \mathfrak B_q.
}
\tag{9}
\]

Consequently, for

\[
H_0(z)=\int_0^\infty\Phi(u)\cos(zu)\,du,
\qquad
\widetilde H_0(z)
=H_0(z)+
\int_0^\infty
(\widetilde\Phi-\Phi)(u)\cos(zu)\,du,
\tag{10}
\]

one has the uniform strip estimate

\[
\boxed{
\sup_{|\operatorname{Im}z|\le q}
|\widetilde H_0(z)-H_0(z)|
\le \mathfrak B_q.
}
\tag{11}
\]

In particular `q=1` is exactly the Mellin critical-strip width under the XF-169/XF-171 coordinate `s=1/2+iz/2`.

Let `Gamma` be any simple closed contour contained in `|Im z|<q`, with no Xi zero on `Gamma`, and put

\[
m_\Gamma:=\min_{z\in\Gamma}|H_0(z)|>0.
\tag{12}
\]

If

\[
\boxed{\mathfrak B_q<m_\Gamma,}
\tag{13}
\]

then `widetilde H_0` and `H_0` have exactly the same number of zeros inside `Gamma`, counted with multiplicity. This is a finite-domain atomwise zero-stability criterion that does not assume RH: it preserves whatever Xi zero count is already present in the chosen domain.

The shell costs have the high-spectral asymptotics

\[
\boxed{
K_q(\lambda)
=\frac12\lambda e^{-\lambda}
\left(1+O_q(\lambda^{-1})\right),
}
\tag{14}
\]

\[
\boxed{
J_q(\lambda)
=2\lambda^2 e^{-\lambda}
\left(1+O_q(\lambda^{-1})\right),
}
\tag{15}
\]

as `lambda->infinity`. Hence any tail deformation satisfying fixed constants `0<c<=C<infinity` and some fixed polynomial weight allowance,

\[
c\lambda_n\le\widetilde\lambda_n\le C\lambda_n,
\qquad
|w_n-1|\le n^A,
\tag{16}
\]

has a Gaussian tail budget

\[
\boxed{
\sum_{n>N}\text{cost}_n
\ll_{q,c,C,A}
N^{A'}e^{-c\pi N^2}
}
\tag{17}
\]

for some fixed `A'`. Thus independently moving or reweighting arbitrarily many sufficiently remote theta atoms by bounded multiplicative factors changes the critical-strip transform by an exponentially small amount on every fixed strip, and eventually leaves the zero count on every fixed Xi-zero-free contour unchanged.

## 1. Exact shell transport identities

XF-166 derives the Xi source from

\[
F_\Xi(x)=\sum_{n\ge1}e^{-\pi n^2x}
\tag{18}
\]

through

\[
\Phi\!\left(\frac14\log x\right)
=x^{5/4}\bigl(2xF_\Xi''(x)+3F_\Xi'(x)\bigr).
\tag{19}
\]

Applying `(19)` to a single Laplace atom `e^(-lambda x)` gives `(2)`, hence `(3)`.

The scale derivative has an especially useful form. Direct differentiation gives

\[
\boxed{
4\lambda\,\partial_\lambda\kappa_\lambda(u)
=\partial_u\kappa_\lambda(u)-\kappa_\lambda(u)
}
\tag{20}
\]

and, writing `y=lambda e^(4u)`,

\[
\partial_u\kappa_\lambda(u)-\kappa_\lambda(u)
=-4\lambda^{-1/4}y^{5/4}(y-3)(2y-1)e^{-y}.
\tag{21}
\]

Equivalently, logarithmic displacement of one spectral atom is literal translation-plus-renormalization of its source shell:

\[
\boxed{
\kappa_{\lambda e^{4a}}(u)
=e^{-a}\kappa_\lambda(u+a).
}
\tag{22}
\]

Equations `(20)--(22)` are the atomwise analogue of the common scale-shift structure used in XF-169, but now each atom may carry its own displacement `a_n`.

## 2. The strip budget is an exact weighted `L^1` transport bound

For the weight term, substitute `y=lambda e^(4u)` into the weighted shell norm. Since `du=dy/(4y)` and `e^(qu)=(y/lambda)^(q/4)`, one obtains exactly

\[
\int_0^\infty e^{qu}|\kappa_\lambda(u)|\,du
=K_q(\lambda).
\tag{23}
\]

The same substitution in `(21)` gives

\[
\int_0^\infty e^{qu}
|4\lambda\partial_\lambda\kappa_\lambda(u)|\,du
=J_q(\lambda).
\tag{24}
\]

Now connect `lambda_n` to `tilde lambda_n` along the logarithmic path `lambda_n e^(4r)`. The fundamental theorem of calculus and `(24)` imply

\[
\int_0^\infty e^{qu}
|\kappa_{\widetilde\lambda_n}(u)-\kappa_{\lambda_n}(u)|\,du
\le
\int_{\min(0,a_n)}^{\max(0,a_n)}
J_q(\lambda_ne^{4r})\,dr.
\tag{25}
\]

Finally split

\[
w_n\kappa_{\widetilde\lambda_n}-\kappa_{\lambda_n}
=(w_n-1)\kappa_{\widetilde\lambda_n}
+(\kappa_{\widetilde\lambda_n}-\kappa_{\lambda_n}).
\tag{26}
\]

Summing `(23)--(26)` proves `(9)`. In particular, finite `mathfrak B_q` makes the series of shell differences absolutely summable in the weighted source norm; no pointwise rearrangement argument is required.

For `z=x+iy` with `|y|<=q`,

\[
|\cos(zu)|^2
=\cos^2(xu)+\sinh^2(yu)
\le\cosh^2(qu)
\le e^{2qu}.
\tag{27}
\]

Combining `(27)` with `(9)` proves `(11)`. The weighted integrability also gives holomorphy in the open strip `|Im z|<q`. Condition `(13)` is therefore the standard Rouche comparison on `Gamma`.

The important distinction from XF-171 is structural. Common scale mixing factors `H_0` and reduces added zeros to a one-variable multiplier, giving a universal scalar criterion such as `d T^2`. Independent atom motion destroys that factorization. The natural replacement is an **absolute transform budget compared against a contour margin of the base Xi transform**.

## 3. Remote square-lattice atoms are Gaussian-invisible

For fixed `q`, once `lambda>3` the absolute values in `(6)--(7)` can be removed. The standard endpoint estimate

\[
\int_\lambda^\infty y^\gamma e^{-y}\,dy
=\lambda^\gamma e^{-\lambda}
\left(1+O_\gamma(\lambda^{-1})\right)
\tag{28}
\]

then gives `(14)--(15)` directly. The leading constants are independent of `q`: increasing the horizontal strip width changes lower-order polynomial factors but not the dominant `e^(-lambda)` visibility of a remote Laplace atom.

For a bounded-factor displacement `(16)`, the logarithmic path stays between `c lambda_n` and `C lambda_n`. Using `(15)` in `(25)`, or changing variables `t=lambda_n e^(4r)`, shows that the location cost is bounded by a fixed polynomial in `lambda_n` times `e^(-c lambda_n)`. Equation `(14)` gives the same form for the weight term. Since `lambda_n=pi n^2`, summing the resulting Gaussian tail proves `(17)`.

This produces a useful no-go. Fix any Xi-zero-free contour `Gamma` in the critical-strip coordinate. Change **every** atom with `n>N` independently, subject only to `(16)`. The deformation can contain infinitely many nonzero placement and weight errors, yet `(17)` implies

\[
\sup_{|\operatorname{Im}z|\le q}
|\widetilde H_{0,N}(z)-H_0(z)|
\longrightarrow0.
\tag{29}
\]

Hence for sufficiently large `N`, `(13)` holds and the zero count inside `Gamma` is unchanged. Finite compact zero data therefore cannot force exact placement of arbitrarily remote square-lattice atoms through this source interface.

The obstruction is not that atomwise perturbations are uncontrolled; `(8)` controls them explicitly. The obstruction is the opposite: **the actual Xi source suppresses high Laplace atoms so strongly on `u>=0` that bounded-factor errors at large `pi n^2` are almost invisible to the transform.**

## 4. Stress tests and falsification boundary

The Gaussian blindness in `(17)` is only a remote-scale statement. If a high atom is moved all the way down to `O(1)` spectral scale, the fixed lower factor `c` in `(16)` disappears and the path in `(25)` crosses the visible low-spectral region. The budget then need not be small. Thus XF-175 does not license arbitrary collapse of the square lattice toward the spectral edge.

Likewise, `(13)` preserves **zero count**, not critical-line location. A cluster of base zeros inside `Gamma` may move or split under perturbation while the total multiplicity stays fixed. To prove line preservation one needs additional symmetry and local zero information. This finding deliberately avoids treating such information as if it followed from the source norm.

The contour margin `m_Gamma` is also load-bearing. For a family of contours whose height tends to infinity, that margin may shrink rapidly. The uniform absolute estimate `(11)` by itself therefore does not yield an analogue of the universal common-mixture condition `d=o(T^-2)`. A height-growing theorem must compare the atomwise source budget with quantitative Xi lower bounds away from its zeros, or discover a replacement factorization.

Finally, independently changing the positive-half Laplace atoms generally breaks exact Jacobi modular coupling. XF-175 is a theorem about what the **source-visible atomwise perturbation itself** can and cannot control. It does not assert that every sequence `(w_n,tilde lambda_n)` extends to a positive holomorphic modular theta object. That limitation is informative rather than cosmetic: modular coupling is now a candidate mechanism by which apparently remote atom errors could be forced back into a visible low-spectral defect.

## Prior-art and novelty audit

The mandatory audit checked the classical Polya/de Bruijn Fourier-kernel deformation literature, standard zero stability under locally uniform perturbation, and neighboring theta/spectral perturbation searches. Those sources supply the general context but no located result provides the matched per-atom costs `(6)--(8)` for the Xi theta prekernel or the Gaussian remote-lattice invisibility consequence `(17)`.

No specialized external theorem is needed. The shell identity is already internal to XF-166; `(6)--(11)` are direct changes of variables and triangle inequalities; `(14)--(17)` use elementary incomplete-gamma endpoint asymptotics; and the zero-count transfer is the standard Rouche theorem. `SOURCES.md` therefore requires no new anchor.

## Relation to prior findings

XF-166 separated real-axis Jacobi reflection from the actual square-lattice coefficient law. XF-168 showed that exact support on the single Xi lattice forces the theta weights, while XF-169--XF-174 classified and quantitatively resolved the much more structured freedom coming from one **common** positive scale law.

XF-175 is the first step outside that common-scale gauge. It answers the immediate request for an atomwise local spectral budget, but the answer exposes a new obstruction: the budget is exponentially concentrated near the low spectral edge. Unlike the common-mixture multiplier, atomwise perturbations do not come with a universal zero-free radius independent of the base Xi value.

## Consequence for `xi_flow`

The next gate should no longer be phrased merely as “find an atomwise spectral budget”; `(8)` is such a budget. The sharper problem is to recover a **source-faithful coupling across spectral indices**. There are two plausible routes:

1. exploit exact Jacobi/Poisson or coefficient arithmetic to show that independently moving remote atoms is not an admissible deformation and that any admissible high-index error necessarily creates a visible low-spectral defect; or
2. obtain quantitative base-Xi contour margins strong enough to compare against `mathfrak B_1` on height-growing domains without assuming the desired zero geometry.

Either route must confront the Gaussian blindness `(17)`. A criterion based only on bounded-factor placement accuracy of sufficiently remote atoms cannot by itself coerce the finite-height Xi zero geometry.