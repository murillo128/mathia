---
type: theorem
research_line: xi_flow
finding_id: XF-179
status: canonical
---

# XF-179 — Complexity-matched Jacobi cusp jets exactly resolve finite atom surgery

**Evidence classification:** `CLASSICAL-ALGEBRA + EXACT-DERIVED + SHARP-COMPLEXITY-THRESHOLD`. XF-176 gives exact Jacobi rigidity, while XF-177--XF-178 show that fixed real-axis norms can be made arbitrarily insensitive to remote finite atom surgery. The present finding separates that instability from genuine nonidentifiability. If exactly `m` positive unit-mass atom pairs of the integer theta comb are moved, then the first `m` derivatives at the Jacobi cusp `x=0` determine whether the surgery is trivial. This depth is sharp: for every choice of `m` distinct reference atoms there are arbitrarily small nontrivial `m`-atom surgeries whose first `m-1` cusp derivatives vanish exactly. Thus the finite-surgery obstruction admits an exact complexity-adaptive inverse, with required jet depth equal to the number of independently moved atom pairs. The argument is Newton--Girard algebra after an exact Jacobi-to-moment bridge; no specialized external theorem is load-bearing.

## Statement

Let

\[
1\le n_1<\cdots<n_m
\tag{1}
\]

be distinct positive integers and let

\[
0<r_1<\cdots<r_m
\tag{2}
\]

be distinct positive replacement radii. Form the even positive unit-mass finite surgery of the integer comb

\[
\rho
:=
\delta_{\mathbb Z}
-
\sum_{j=1}^m(\delta_{n_j}+\delta_{-n_j})
+
\sum_{j=1}^m(\delta_{r_j}+\delta_{-r_j}).
\tag{3}
\]

Define

\[
\Theta_\rho(x)
:=
\langle\rho,e^{-\pi x(\cdot)^2}\rangle,
\qquad x>0,
\tag{4}
\]

and its Jacobi residual

\[
\boxed{
\mathcal J_\rho(x)
:=
\Theta_\rho(x)-x^{-1/2}\Theta_\rho(1/x).
}
\tag{5}
\]

Then `mathcal J_rho` extends smoothly to `x=0` with

\[
\mathcal J_\rho(0)=0
\tag{6}
\]

and, for every integer `ell>=1`,

\[
\boxed{
\mathcal J_\rho^{(\ell)}(0)
=
2(-\pi)^\ell
\left(
\sum_{j=1}^m r_j^{2\ell}
-
\sum_{j=1}^m n_j^{2\ell}
\right).
}
\tag{7}
\]

Consequently,

\[
\boxed{
\mathcal J_\rho^{(\ell)}(0)=0
\quad(1\le\ell\le m)
\Longrightarrow
\{r_1,\ldots,r_m\}
=
\{n_1,\ldots,n_m\}.
}
\tag{8}
\]

Since both lists are increasingly ordered, `(8)` gives `r_j=n_j` for every `j`; the surgery is trivial.

The depth `m` is best possible. For every reference set `(1)` and every sufficiently small neighborhood of it, there exists a nontrivial positive ordered replacement set `(2)` inside that neighborhood such that

\[
\boxed{
\mathcal J_\rho^{(\ell)}(0)=0
\quad(1\le\ell\le m-1),
}
\tag{9}
\]

while

\[
\boxed{
\mathcal J_\rho^{(m)}(0)\ne0.
}
\tag{10}
\]

In particular, if the replacements are required to remain in the Xi cells

\[
|r_j-n_j|<\frac14,
\tag{11}
\]

the sharpness construction can be chosen to satisfy `(11)`. Hence positivity, unit masses, uniform separation, eventual exact agreement with the Xi comb, and arbitrarily small atom motion do not reduce the worst-case cusp-jet depth below the moved-atom count.

## 1. A finite Jacobi surgery has a smooth cusp residual

The integer comb satisfies the Jacobi identity exactly. Therefore only the moved atoms contribute to `(5)`. Put

\[
D(x)
:=
2\sum_{j=1}^m
\left(e^{-\pi r_j^2x}-e^{-\pi n_j^2x}\right).
\tag{12}
\]

Then

\[
\boxed{
\mathcal J_\rho(x)
=
D(x)-x^{-1/2}D(1/x).
}
\tag{13}
\]

Equal cardinality gives `D(0)=0`. Since every `n_j` and `r_j` is strictly positive, for some `c>0`

\[
x^{-1/2}D(1/x)
=
O\!\left(x^{-1/2}e^{-c/x}\right)
\qquad(x\downarrow0).
\tag{14}
\]

Every derivative of the right-hand side of `(14)` is again a polynomial in `x^{-1}` times `e^{-c/x}`, hence tends to zero. Thus the reciprocal Jacobi image is **flat at the cusp**. Extending it by zero at `x=0` makes it `C^infinity`, and `(13)` gives

\[
\mathcal J_\rho^{(\ell)}(0)=D^{(\ell)}(0).
\tag{15}
\]

Termwise differentiation of the finite sum `(12)` now yields exactly `(7)`.

This point is structurally different from the fixed-`x` estimates in XF-175 and the weighted sup norms in XF-177--XF-178. Remote Gaussian atoms are weak at any prescribed positive heat scale, but the full boundary jet at `x=0` records their algebraic moments before the reciprocal image can contribute.

## 2. The first `m` cusp coefficients recover `m` unit atoms

Set

\[
\lambda_j:=n_j^2,
\qquad
\mu_j:=r_j^2.
\tag{16}
\]

If the first `m` derivatives in `(8)` vanish, `(7)` says that the first `m` power sums agree:

\[
\sum_{j=1}^m\mu_j^\ell
=
\sum_{j=1}^m\lambda_j^\ell,
\qquad
1\le\ell\le m.
\tag{17}
\]

Let `e_k(lambda)` and `e_k(mu)` denote the elementary symmetric polynomials. The Newton--Girard identities recursively determine `e_k` from the power sums through order `k`. Hence `(17)` gives

\[
e_k(\mu)=e_k(\lambda)
\qquad(1\le k\le m).
\tag{18}
\]

Therefore the two monic polynomials

\[
\prod_{j=1}^m(z-\mu_j)
\quad\text{and}\quad
\prod_{j=1}^m(z-\lambda_j)
\tag{19}
\]

have identical coefficients and are equal. Their root multisets coincide, so positivity gives the equality of radii claimed in `(8)`.

The atom count is doing real work. General finite-moment reconstruction with unknown masses belongs to the classical Prony/moment-problem framework and carries more unknown parameters. Here every moved pair has known unit mass, so the only unknowns are the `m` squared radii; exactly `m` power sums are enough.

## 3. Constant-term deformation proves that depth `m-1` is insufficient

The sharpness statement has an explicit algebraic normal form. Start from

\[
P(z)
:=
\prod_{j=1}^m(z-\lambda_j)
=
z^m-e_1z^{m-1}+e_2z^{m-2}-\cdots+(-1)^m e_m,
\tag{20}
\]

where `e_k=e_k(lambda)`. For real `tau` define

\[
\boxed{
P_\tau(z)
:=
P(z)+(-1)^m\tau.
}
\tag{21}
\]

Because the roots `lambda_j` are positive and simple, for every sufficiently small real `tau` the polynomial `P_tau` has `m` positive simple real roots

\[
\mu_1(\tau)<\cdots<\mu_m(\tau)
\tag{22}
\]

with `mu_j(tau)->lambda_j` as `tau->0`. This follows directly by the implicit-function theorem at each simple root. Put

\[
r_j(\tau):=\sqrt{\mu_j(\tau)}.
\tag{23}
\]

For small enough nonzero `tau`, the replacements are nontrivial and can be made to satisfy `(11)`.

Equation `(21)` changes only the constant coefficient of the monic root polynomial. Thus

\[
e_k(\mu(\tau))=e_k(\lambda)
\qquad(1\le k\le m-1),
\tag{24}
\]

while

\[
e_m(\mu(\tau))=e_m(\lambda)+\tau.
\tag{25}
\]

Newton--Girard now gives equality of the power sums through order `m-1`, hence `(9)`. At order `m`, subtracting the two Newton identities gives

\[
\sum_{j=1}^m\mu_j(\tau)^m
-
\sum_{j=1}^m\lambda_j^m
=
(-1)^{m+1}m\tau.
\tag{26}
\]

Combining `(7)` and `(26)`,

\[
\boxed{
\mathcal J_\rho^{(m)}(0)
=
2(-\pi)^m(-1)^{m+1}m\tau,
}
\tag{27}
\]

which is nonzero for `tau!=0`. Thus the complexity threshold is exact, not merely an upper bound obtained from a generic finite moment theorem.

For `m=1`, the statement says the zeroth cusp value is always blind because equal cardinality forces `mathcal J(0)=0`, while the first derivative detects the moved squared radius. For `m=2`, a one-parameter deformation can preserve the sum of the two squared radii exactly, but the second derivative detects the changed product. The same coefficient mechanism persists for every `m`.

## 4. Relation to the XF-178 cancellation obstruction

XF-178 shows that a packet with enough matched **offset moments** can defeat any one fixed power-weighted real-axis Jacobi topology. That result correctly rules out a complexity-independent coercive norm. XF-179 shows that this does not mean finite surgery is information-theoretically invisible.

For an `m`-atom unit-mass surgery, the exact cusp data provide a hierarchy whose required depth grows with the packet complexity:

\[
\boxed{
\text{at most }m\text{ moved positive atom pairs}
\quad\Longrightarrow\quad
\text{cusp jet through order }m\text{ is identifying}.
}
\tag{28}
\]

Moreover, `(21)--(27)` show that replacing `m` by `m-1` fails even for arbitrarily small, positive, uniformly separated surgeries. This supplies a precise positive answer to one branch of the complexity-adaptive target left after XF-178: **the finite-surgery class has a sharp atom-count-matched modular resolution law.**

There is no contradiction with the remote-packet no-go. XF-178 measures a residual through fixed positive-scale sup norms; XF-179 takes exact derivatives at the singular modular cusp. The latter is much stronger information and can be violently ill-conditioned under noise. In particular, the theorem gives no bound of the form

\[
\max_j|r_j-n_j|
\le
\omega(\text{small finite-scale Jacobi error})
\tag{29}
\]

with useful constants as `m` or the remote index grows.

## 5. Stress tests and boundaries

The unit-mass hypothesis is load-bearing for the exact depth `m`. If both positions and masses are unknown, the parameter count changes and the natural neighboring theory is Prony reconstruction; XF-179 does not claim that `m` derivatives remain sufficient.

Finite surgery is also load-bearing. An infinite atomwise deformation has no finite complexity parameter `m`, so `(28)` does not produce a finite identifying jet. Likewise, a sequence of finite surgeries with `m->infinity` can outrun every fixed jet depth, exactly in the spirit of XF-178.

The theorem is exact rather than stable. Small cusp derivatives do not by themselves imply small atom displacement without quantitative conditioning of the Newton/Vandermonde inverse. For remote or tightly parameterized packets those constants can deteriorate badly. A route toward a transition-time theorem would need a regularized finite-scale surrogate whose depth grows with effective source complexity while its conditioning remains comparable to a zero-sensitive quantity.

Finally, `(7)` uses the Jacobi **residual of the finite surgery relative to the exact integer comb**. The individual theta trace has the usual modular singular behavior as `x->0`; the smooth cusp jet exists because the integer-comb background cancels and the reciprocal image of the finite perturbation is flat. The statement must not be reinterpreted as termwise differentiation of the full theta comb at `x=0`.

## Prior-art and novelty audit

The algebraic reconstruction step is classical. Newton--Girard identities already imply that `m` equal-weight atoms are determined by their first `m` power sums, and Prony-type methods form the broader finite-atomic moment-reconstruction literature. A representative modern reference is Stefan Kunis, Thomas Peter, Tim Roemer and Ulrich von der Ohe, *A multivariate generalization of Prony's method*, Linear Algebra and its Applications 490 (2016), 31--47, DOI `10.1016/j.laa.2015.10.023`.

No novelty is claimed for Newton identities, finite atomic moment reconstruction, or persistence of simple real roots under a small coefficient perturbation. The durable Xi-flow content is the exact bridge `(7)` from the Jacobi cusp residual to squared-radius moments, the sharp `m` versus `m-1` threshold for positive unit-mass finite theta-comb surgery, and its role in resolving the specific complexity-adaptive escape left by XF-178. The proof is self-contained, so no new load-bearing literature dependency is required in `SOURCES.md`.

## Consequence for `xi_flow`

The source-side frontier is now narrower. XF-176 says exact Jacobi plus asymptotic matching is globally rigid. XF-177--XF-178 say fixed-complexity positive-scale norms are not continuously coercive. XF-179 shows that, on the finite unit-mass surgery class, **complexity-adaptive exact data do recover coercivity in the strongest possible qualitative sense, and the required depth is exactly the moved-atom count.**

The next useful question is therefore not whether some finite packet can hide from every fixed statistic; it can. The sharper question is whether the actual Xi source supplies a bound on effective packet complexity, or whether the exact cusp jet in `(28)` can be replaced by a quantitatively stable finite-scale hierarchy whose depth grows with that complexity. Without such a conditioning bridge, exact source identifiability still does not yield an upper bound on the de Bruijn--Newman transition time.