---
type: classical
research_line: xi_flow
finding_id: XF-168
status: canonical
---

# XF-168 — Single-square-lattice Jacobi reciprocity is Hamburger-rigid

**Evidence classification:** literature-backed exact reduction. The rigidity theorem used below is Hamburger's classical converse theorem for the Riemann zeta functional equation. The line-specific contribution is to identify it as the exact answer to the coefficient-level source gate left by XF-167 and to derive its hypotheses directly from the weighted theta representation. No novelty is claimed for Hamburger rigidity itself.

## Statement

XF-167 showed that positivity, real-axis Jacobi reciprocity, cusp normalization, and complete monotonicity still permit a positive de Bruijn–Newman transition once the inverse-Laplace spectrum is allowed to split into several scaled square lattices. If the Laplace support is fixed back to the **single** Xi square lattice, however, the apparent freedom to reweight those atoms disappears completely.

Let `(a_n)_{n>=1}` be a complex sequence such that

\[
A(s):=\sum_{n\ge1}a_n n^{-s}
\tag{1}
\]

converges absolutely for every `Re(s)>1`. Define

\[
F_a(x):=\sum_{n\ge1}a_n e^{-\pi n^2x},
\qquad
\Theta_a(x):=1+2F_a(x),
\qquad x>0.
\tag{2}
\]

Assume the exact Jacobi reciprocity law

\[
\boxed{
\Theta_a(x)=x^{-1/2}\Theta_a(1/x)
}
\qquad(x>0).
\tag{3}
\]

Then

\[
\boxed{A(s)=\zeta(s)}
\tag{4}
\]

and hence, by uniqueness of absolutely convergent Dirichlet series,

\[
\boxed{a_n=1\quad\text{for every }n\ge1.}
\tag{5}
\]

No positivity assumption on the coefficients is needed. In the source language of XF-166--XF-167: once the inverse-Laplace atoms are constrained to occur exactly at `pi n^2`, the real-axis Jacobi law and the standard constant term already force the Xi weights. Therefore **weight deformation on the fixed square lattice is not a surviving source-side escape route**. The nontrivial escape in XF-167 genuinely comes from support contamination by scaled lattices.

## 1. The theta law produces the Riemann completed functional equation

Absolute convergence of `(1)` at, say, `s=2` implies `|a_n|=O(n^2)`. Thus the series `(2)` converges absolutely for every `x>0`, and for `x>=1`

\[
F_a(x)=O(e^{-\pi x})
\tag{6}
\]

up to a harmless polynomial factor absorbed by the exponential.

Equation `(3)` is equivalent to

\[
F_a(x)
=
 x^{-1/2}F_a(1/x)
+\frac{x^{-1/2}-1}{2}.
\tag{7}
\]

For `Re(s)>1`, termwise Mellin transformation gives

\[
\Lambda_a(s)
:=
\pi^{-s/2}\Gamma\!\left(\frac s2\right)A(s)
=
\int_0^\infty F_a(x)x^{s/2}\,\frac{dx}{x}.
\tag{8}
\]

Split at `x=1`, apply `(7)` on `(0,1)`, and substitute `x=1/y` in the reflected term. One obtains the exact continuation formula

\[
\boxed{
\Lambda_a(s)
=
\frac1{s-1}-\frac1s
+
\int_1^\infty
F_a(x)
\left(x^{s/2}+x^{(1-s)/2}\right)
\frac{dx}{x}.
}
\tag{9}
\]

The integral in `(9)` is entire in `s` by `(6)`, so `Lambda_a` is meromorphic on `C` with possible poles only at `0` and `1`. The right-hand side is invariant under `s -> 1-s`; consequently

\[
\boxed{\Lambda_a(s)=\Lambda_a(1-s).}
\tag{10}
\]

Thus the real-axis theta reciprocity has already recreated the completed Riemann functional equation for the Dirichlet series carried by the square-lattice weights.

## 2. The continuation automatically lies in Hamburger's finite-order class

To use Hamburger's theorem one must not silently assume its growth hypothesis. Here it follows from `(9)`.

For `|s|<=R`, `(6)` bounds the entire integral in `(9)` by an expression of the form

\[
\int_1^\infty e^{-c x}x^{R/2+C}\,dx
\le
\exp\!\bigl(O(R\log(R+2))\bigr)
\tag{11}
\]

for fixed positive constants `c,C`. Hence the pole-cleared completion has finite order. Since `1/Gamma(s/2)` is entire of finite order and `pi^(s/2)` has exponential type,

\[
A(s)
=
\frac{\pi^{s/2}}{\Gamma(s/2)}\Lambda_a(s)
\tag{12}
\]

extends meromorphically with at most a simple pole at `s=1`, and

\[
\boxed{(s-1)A(s)\text{ is entire of finite order}.}
\tag{13}
\]

At `s=0` the pole of `Lambda_a` is cancelled by the zero of `1/Gamma(s/2)`; at the negative even integers the same reciprocal-gamma factor causes no new pole. Thus `(13)` contains no hidden regularity assumption beyond `(1)` and `(3)`.

## 3. Hamburger leaves only zeta, and the cusp normalization fixes the scalar

Hamburger's converse theorem, in the standard formulation recalled explicitly by Kaczorowski--Molteni--Perelli, says that if Dirichlet series `f,g` converge absolutely for `Re(s)>1`, `(s-1)f` and `(s-1)g` are entire of finite order, and

\[
\pi^{-s/2}\Gamma\!\left(\frac s2\right)f(s)
=
\pi^{-(1-s)/2}\Gamma\!\left(\frac{1-s}{2}\right)g(1-s),
\tag{14}
\]

then `f=g=c zeta` for some constant `c`.

Apply the theorem with `f=g=A`. Equations `(1)`, `(10)`, and `(13)` verify exactly its hypotheses, so

\[
A(s)=c\zeta(s).
\tag{15}
\]

Formula `(9)` has residue `1` at `s=1`. Because

\[
\pi^{-1/2}\Gamma(1/2)=1,
\tag{16}
\]

`A` itself also has residue `1` there. Since `zeta` has residue `1`, `(15)` forces `c=1`, proving `(4)`. Uniqueness of Dirichlet coefficients in the half-plane of absolute convergence then gives `(5)`.

This is precisely the conductor-one one-dimensional rigidity singled out by Hamburger's theorem. The literature also explicitly relates Hamburger uniqueness to uniqueness properties of Poisson summation, so the appearance of the theorem at the present theta-source gate is structural rather than accidental.

## 4. Stress tests against the current controls

### XF-167 does not contradict the theorem

The completely monotone control of XF-167 has inverse-Laplace measure

\[
\mu_c
=
\frac12\sum_{n\ge1}\delta_{\pi n^2}
+
\frac{e^c}{4\cosh c}\sum_{n\ge1}\delta_{\pi e^{4c}n^2}
+
\frac{e^{-c}}{4\cosh c}\sum_{n\ge1}\delta_{\pi e^{-4c}n^2}.
\tag{17}
\]

For every `c>0`, the down-scaled lattice contains atoms away from `{pi n^2}`; even when one scale happens to map a subsequence of squares into the base lattice, its reciprocal scale introduces off-lattice atoms. Hence XF-167 escapes `(5)` through **support displacement**, not through a nontrivial coefficient sequence on the fixed support.

### Positivity and complete monotonicity are irrelevant to the rigidity step

The proof never uses `a_n>=0`. Consequently strengthening complete monotonicity or coefficient positivity cannot produce additional freedom once exact square support and exact Jacobi reciprocity are already imposed. Those properties were useful classifier candidates before XF-167, but at fixed support they are logically downstream of a stronger uniqueness mechanism.

### Approximate reciprocity is not covered

The conclusion is exact. A small Jacobi defect does not automatically imply `a_n` is close to `1`, and Hamburger's theorem is not a quantitative stability theorem. Likewise, support points merely close to `pi n^2` fall outside the Dirichlet-series reduction. These are genuine surviving directions rather than technical omissions.

## Relation to prior findings

XF-162--XF-165 removed tail asymptotics, finite source jets, and heat-origin gauges as coercive source data. XF-166 showed that exact real-axis Jacobi reflection can be synthesized for arbitrary suitable even sources through a Green lift. XF-167 then strengthened the negative result by constructing a positive, analytic, completely monotone Jacobi-reflecting prekernel with `0<Lambda_c<=1/2`; its inverse-Laplace measure is a positive mixture of three scaled square lattices.

XF-168 closes the immediate coefficient-weight branch left by XF-167. The phrase in XF-167 that the surviving rigidity must retain “the single square-lattice support and its exact weights” can now be sharpened: **inside the classical Dirichlet-series class, the weights are forced automatically once the single support and exact Jacobi reciprocity are fixed**. The only nontrivial spectral freedom in that package is therefore movement, splitting, or enlargement of the support (or weakening the exact reciprocal law/growth class).

## Prior-art and novelty audit

This finding is a classicalization, not a novelty claim. Hamburger's 1921 converse theorem characterizes the Riemann zeta function by its functional equation inside the relevant finite-order Dirichlet-series class. Kaczorowski, Molteni and Perelli give a modern peer-reviewed statement of precisely the version used here and note its connection with uniqueness of Poisson summation. A targeted search for weighted square-lattice theta reciprocity therefore redirects the apparent coefficient problem to this classical theorem rather than supporting a new uniqueness claim.

The derivation `(7)`--`(13)` is included because it is the load-bearing dictionary for `xi_flow`: it verifies that the weighted prekernel contemplated after XF-167 actually lands in Hamburger's hypotheses, rather than merely resembling zeta formally. The external theorem is now anchored in `SOURCES.md`.

## Falsification boundary

XF-168 does **not** show that coefficient-level theta rigidity implies `Lambda=0`. Once `(5)` is reached, one has simply identified the source as the genuine Xi theta prekernel; proving the required zero statement is again the original RH/de Bruijn--Newman problem. Source identification is not source-to-transition coercivity.

The theorem also does not provide stability. It gives no estimate converting an `epsilon`-sized displacement of the spectral atoms, an approximate Jacobi law, or a small coefficient defect into a quantitative bound on `Lambda`. XF-167 is especially important here: for arbitrarily small `c>0`, its three square lattices are multiplicatively close to the Xi lattice on relative scale, while the time-zero transform still acquires nonreal zeros (at heights moving to infinity as `c->0`). Any useful quantitative rigidity theorem must therefore keep track of the coupling between spectral error scale and the zero height at which the defect becomes visible.

Finally, the finite-order hypothesis is not being smuggled in as an extra source axiom: under the exact weighted-theta representation and absolute Dirichlet convergence, `(9)` supplies the required continuation and finite-order growth. If one leaves that representation or permits substantially wilder coefficient objects/distributions, Hamburger's conclusion need not apply.

## Consequence for `xi_flow`

Do not spend further passes searching for a nontrivial reweighting of the exact atoms `pi n^2` that preserves the standard Jacobi law: Hamburger rigidity rules it out in the natural Dirichlet-series class.

The next meaningful coefficient-level gate is **quantitative support stability**, not exact identification. One needs a theorem or counterexample for spectra

\[
\lambda_n=\pi n^2 e^{\varepsilon_n}
\tag{18}
\]

(or finite positive mixtures of such nearby spectra) that measures how a Jacobi/modular defect and the displacement profile `(epsilon_n)` propagate into high-zero geometry or into a bound for the de Bruijn--Newman transition. XF-167 supplies the first stress family: a symmetric multiplicative displacement `epsilon=±4c` can be arbitrarily small while creating a nonreal seam at real height `asymp 1/c`. A useful stability principle must therefore be scale-sensitive in height; a norm that ignores where the spectral error is observed will be too weak.