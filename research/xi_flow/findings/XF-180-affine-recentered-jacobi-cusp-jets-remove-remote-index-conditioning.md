---
type: theorem
research_line: xi_flow
finding_id: XF-180
status: canonical
---

# XF-180 — Affine-recentered Jacobi cusp jets remove remote-index conditioning but expose a complexity barrier

**Evidence classification:** `EXACT-DERIVED + LOCAL-STABILITY + SHARP-COMPLEXITY-OBSTRUCTION`. XF-179 shows that the first `m` Jacobi cusp derivatives exactly identify an `m`-pair positive unit-mass finite surgery, but leaves open whether the resulting Newton/Vandermonde inverse becomes unusably ill-conditioned merely because the packet is remote. The present finding separates absolute location from intrinsic packet complexity. After an exact affine recentering of the cusp differential operator, the local inverse problem depends only on the normalized geometry of the moved squared radii. For a consecutive Xi packet `((N+1)^2,...,(N+m)^2)` with `N>=m`, the inverse Jacobian has an explicit upper bound depending on `m` but not on `N`. However, the same normalized power-moment coordinates have an inverse norm at least `(m-1)^(m-1)/(m-1)!`, hence exponentially large in `m`. Remote index is therefore not the intrinsic finite-packet obstruction once centered normalized cusp jets are supplied; packet complexity is. The remaining unresolved conditioning can instead enter when the centered cusp jets themselves must be estimated from finite positive heat scales.

## Statement

Retain the finite unit-mass surgery notation of XF-179. Put

\[
\lambda_j:=n_j^2,
\qquad
\mu_j:=r_j^2,
\qquad 1\le j\le m,
\tag{1}
\]

and let `mathcal J_rho` be its Jacobi residual. For any real center `A`, any scale `R>0`, and every integer `ell>=1`, define the centered normalized cusp datum

\[
\boxed{
\mathcal C_\ell(A,R)
:=
\frac{1}{2(-\pi R)^\ell}
\left[(\partial_x+\pi A)^\ell\mathcal J_\rho(x)\right]_{x=0}.
}
\tag{2}
\]

Then

\[
\boxed{
\mathcal C_\ell(A,R)
=
\sum_{j=1}^m v_j^\ell
-
\sum_{j=1}^m u_j^\ell,
}
\tag{3}
\]

where

\[
u_j:=\frac{\lambda_j-A}{R},
\qquad
v_j:=\frac{\mu_j-A}{R}.
\tag{4}
\]

Thus `(2)` converts the Jacobi cusp residual exactly into **dimensionless centered power-sum differences**.

Assume the reference normalized nodes satisfy

\[
0\le u_1<\cdots<u_m\le1,
\qquad
\delta:=\min_{j\ne k}|u_j-u_k|>0.
\tag{5}
\]

For a local perturbation `v_j=u_j+h_j`, set

\[
q_\ell:=\mathcal C_\ell(A,R),
\qquad
s_k:=\frac{q_{k+1}}{k+1},
\qquad 0\le k\le m-1.
\tag{6}
\]

The differential of the map `h -> (s_0,...,s_{m-1})` at `h=0` is the Vandermonde map

\[
\boxed{
s_k=\sum_{j=1}^m u_j^k h_j+O_m(\|h\|_\infty^2).
}
\tag{7}
\]

Its inverse in `ell^infinity` obeys

\[
\boxed{
\|V(u)^{-1}\|_{\infty\to\infty}
\le
\left(\frac{2}{\delta}\right)^{m-1}.
}
\tag{8}
\]

Consequently the normalized moment map is locally invertible, with a local inverse modulus depending on the packet only through its normalized geometry `(m,delta)`, not through the absolute center `A` or scale `R`.

For the consecutive Xi squared-lattice packet

\[
\lambda_j=(N+j)^2,
\qquad 1\le j\le m,
\tag{9}
\]

choose

\[
A=(N+1)^2,
\qquad
R=(N+m)^2-(N+1)^2
=(m-1)(2N+m+1).
\tag{10}
\]

If `N>=m>=2`, then

\[
\boxed{
\delta\ge\frac{1}{2(m-1)},
}
\tag{11}
\]

so

\[
\boxed{
\|V(u)^{-1}\|_{\infty\to\infty}
\le
\bigl(4(m-1)\bigr)^{m-1},
}
\tag{12}
\]

uniformly in the remote index `N`.

This removal of `N` does **not** make the hierarchy uniformly well-conditioned in complexity. For the same consecutive normalized packet, the first Lagrange row gives

\[
\boxed{
\|V(u)^{-1}\|_{\infty\to\infty}
\ge
\frac{(m-1)^{m-1}}{(m-1)!}
\sim
\frac{e^{m-1}}{\sqrt{2\pi(m-1)}}.
}
\tag{13}
\]

Hence exponential deterioration in `m` is already intrinsic to these power-moment coordinates, even after absolute remote location has been normalized away.

## 1. Centering the Jacobi cusp jet is exact

XF-179 writes the finite-surgery residual as

\[
\mathcal J_\rho(x)=D(x)-x^{-1/2}D(1/x),
\tag{14}
\]

with

\[
D(x)=2\sum_{j=1}^m
\left(e^{-\pi\mu_jx}-e^{-\pi\lambda_jx}\right).
\tag{15}
\]

The reciprocal term is flat at `x=0`: every finite derivative tends to zero there. Applying any fixed finite-order differential operator therefore leaves only the cusp derivatives of `D`.

For a single exponential,

\[
(\partial_x+\pi A)e^{-\pi\lambda x}
=-\pi(\lambda-A)e^{-\pi\lambda x}.
\tag{16}
\]

Iterating `(16)` and evaluating at zero gives

\[
\left[(\partial_x+\pi A)^\ell\mathcal J_\rho(x)\right]_{x=0}
=2(-\pi)^\ell
\left[
\sum_j(\mu_j-A)^\ell
-
\sum_j(\lambda_j-A)^\ell
\right].
\tag{17}
\]

Dividing by `2(-pi R)^ell` proves `(3)`. This is more than a cosmetic change of variables: the observable itself is centered before inversion, so the algebraic data do not contain powers of the remote absolute location.

The construction is compatible with the exact depth law of XF-179. Translation and nonzero scaling of the atom coordinate give a triangular invertible change among power sums through order `m`, so the first `m` centered normalized cusp data remain exactly identifying for an `m`-atom unit-mass surgery.

## 2. The local inverse is a normalized Vandermonde problem

Write `v_j=u_j+h_j`. Expanding `(3)` gives

\[
q_\ell
=\ell\sum_j u_j^{\ell-1}h_j
+O_m(\|h\|_\infty^2),
\qquad 1\le\ell\le m.
\tag{18}
\]

After the normalization `(6)`, the linear term is exactly

\[
s_k=\sum_j u_j^k h_j,
\qquad 0\le k\le m-1.
\tag{19}
\]

Let

\[
L_j(t)=
\prod_{i\ne j}\frac{t-u_i}{u_j-u_i}
=\sum_{k=0}^{m-1}c_{jk}t^k
\tag{20}
\]

be the Lagrange cardinal polynomial. Then `L_j(u_i)=delta_{ij}`, hence

\[
h_j=\sum_{k=0}^{m-1}c_{jk}s_k
\tag{21}
\]

at the linearized level. Because every `u_i` lies in `[0,1]`, the coefficient `ell^1` norm of the numerator polynomial satisfies

\[
\left\|\prod_{i\ne j}(t-u_i)\right\|_{\ell^1(\mathrm{coeff})}
\le
\prod_{i\ne j}(1+|u_i|)
\le2^{m-1}.
\tag{22}
\]

The denominator obeys

\[
\prod_{i\ne j}|u_j-u_i|
\ge\delta^{m-1}.
\tag{23}
\]

Equations `(20)--(23)` prove `(8)`. Since the Jacobian is nonsingular, the inverse-function theorem then gives a genuine local nonlinear inverse around the reference packet. The allowed neighborhood and Lipschitz constant can depend on `(m,delta)`, but **not on `A` or `R` once the centered normalized data `(2)` are treated as the measured coordinates**.

This qualification matters. The theorem does not say that ordinary uncentered cusp derivatives, nor finite-`x` samples from which `(2)` might be estimated, are uniformly conditioned in a remote index. It says that the *moment inversion stage itself* has no unavoidable remote-index penalty after the exact affine normalization.

## 3. Consecutive Xi packets have remote-index-uniform normalized separation

For `(9)--(10)`,

\[
u_1=0,
\qquad
u_m=1,
\tag{24}
\]

and adjacent gaps are

\[
u_{j+1}-u_j
=
\frac{2N+2j+1}{(m-1)(2N+m+1)}.
\tag{25}
\]

The minimum occurs at `j=1`, so

\[
\delta
=
\frac{2N+3}{(m-1)(2N+m+1)}.
\tag{26}
\]

When `N>=m`,

\[
\frac{2N+3}{2N+m+1}\ge\frac12,
\tag{27}
\]

which proves `(11)` and then `(12)`.

This directly sharpens the conditioning caveat left in XF-179. A packet does not become intrinsically harder to invert merely because all its atoms are translated far out along the Xi square lattice. For fixed `m`, the normalized local inverse remains bounded as `N->infinity`. In fact the normalized nodes converge to the equally spaced configuration

\[
u_j\longrightarrow\frac{j-1}{m-1}.
\tag{28}
\]

The bad parameter is therefore not remote location by itself; it is increasing packet complexity or collapsing normalized separation.

## 4. Complexity still produces an exponential inverse barrier

The upper bound `(12)` is deliberately elementary and not claimed sharp. More importantly, no refinement can make the monomial moment inverse uniformly benign as `m` grows.

Consider the endpoint Lagrange polynomial `L_1`. Since `u_1=0`, its leading coefficient has absolute value

\[
\frac{1}{\prod_{k=2}^m u_k}.
\tag{29}
\]

For the consecutive square-lattice packet,

\[
u_k
=
\frac{(k-1)(2N+k+1)}{(m-1)(2N+m+1)},
\tag{30}
\]

and therefore

\[
\frac{1}{\prod_{k=2}^m u_k}
=
\frac{(m-1)^{m-1}}{(m-1)!}
\prod_{k=2}^m
\frac{2N+m+1}{2N+k+1}.
\tag{31}
\]

Every factor in the final product is at least one. Since the coefficient `ell^1` norm of `L_1` is at least the magnitude of its leading coefficient, `(31)` proves the lower bound `(13)`. Stirling's formula gives the final asymptotic.

Thus the affine normalization cleanly separates two effects:

\[
\boxed{
\text{remote index }N
\quad\text{is removable at the normalized moment-inversion stage,}
}
\tag{32}
\]

while

\[
\boxed{
\text{packet complexity }m
\quad\text{already forces exponential conditioning in power-moment coordinates.}
}
\tag{33}
\]

This lower bound is intentionally scoped. It is a barrier for the normalized cusp-jet / monomial power-moment inverse map used here, not a theorem that every conceivable source-side representation must suffer the same exponential constant. Orthogonalized or otherwise preconditioned moment coordinates may alter numerical conditioning, although they still need enough independent information to defeat the `m-1` exact cancellation from XF-179.

## 5. Stress tests and boundaries

For `m=2`, the normalized nodes are exactly `{0,1}` for every `N`, so the centered inverse has constant conditioning independent of how remote the two atoms are. This is the simplest sanity check that raw powers of `N` in uncentered Newton coordinates are a coordinate effect rather than an unavoidable information loss.

For fixed `m` and `N->infinity`, `(28)` gives a nondegenerate limiting configuration, again confirming that no new inverse singularity is created by remote translation. Conversely, when `m` grows, `(13)` shows that the normalized monomial inverse becomes exponentially sensitive even though all nodes remain in `[0,1]` and are regularly ordered.

The finite-surgery and known-reference-window hypotheses remain load-bearing. An infinite deformation has no finite depth `m`, and an unknown collection of moved atoms requires model selection before `(A,R,m)` are available. The local stability conclusion also assumes the moved nodes remain close enough to the reference normalized packet for the inverse-function neighborhood to apply; `(3)` itself is exact globally, but the quantitative inverse estimate is local.

Most importantly, `(2)` is a cusp observable. If the only available information is `mathcal J_rho(x)` at positive `x`, estimating `(partial_x+pi A)^ell mathcal J_rho(0)` may require cancellations involving coefficients of size comparable to powers of `A/R`. Such an estimator can reintroduce remote-index dependence. XF-180 therefore removes the remote index only from the **algebraic reconstruction stage once the centered normalized cusp jet is supplied**. Building a finite-scale, noise-stable estimator of those data remains open and is now a more sharply isolated problem.

## Prior-art and novelty audit

Finite atomic reconstruction from moments is classical Prony theory, and conditioning of Vandermonde inverses in terms of node geometry is classical numerical analysis. Representative references include Walter Gautschi, *On inverses of Vandermonde and confluent Vandermonde matrices*, Numerische Mathematik 4 (1962/63), 117--123, and Stefan Kunis, Thomas Peter, Tim Roemer and Ulrich von der Ohe, *A multivariate generalization of Prony's method*, Linear Algebra and its Applications 490 (2016), 31--47, DOI `10.1016/j.laa.2015.10.023`. Modern Vandermonde conditioning work likewise emphasizes node separation and basis choice rather than absolute translation as the natural variables.

No novelty is claimed for Lagrange inversion, Vandermonde conditioning, affine normalization of polynomial coordinates, or the inverse-function theorem. The Xi-flow contribution is the exact source bridge `(2)--(3)`: the centered operator `(partial_x+pi A)^ell` applied to the Jacobi cusp residual produces normalized moments of the moved **squared theta atoms** without contamination from the reciprocal term. Combining that bridge with the Xi square-lattice geometry yields the remote-index-uniform bound `(12)` and isolates the exponential complexity obstruction `(13)` inside the exact adaptive hierarchy opened by XF-179. The derivation is self-contained; no new external theorem is load-bearing, so no new durable source anchor is required.

## Consequence for the Xi-flow frontier

XF-178 ruled out every fixed-complexity real-axis power topology on arbitrary remote finite packets. XF-179 answered that no-go with an exact hierarchy whose depth tracks the moved-atom count. XF-180 now shows that, for finite consecutive Xi packets, the hierarchy need not also pay an unavoidable price merely because the packet is remote: after affine recentering, the local inverse depends on normalized geometry and is uniform in `N` for fixed `m`.

The live obstruction is therefore narrower. A transition-relevant source theorem must either control an **effective packet complexity** small enough that an adaptive hierarchy remains usable, replace monomial moments by a better-conditioned complexity-matched representation, or construct a finite-positive-scale estimator of centered cusp information whose error remains below the zero-sensitive tolerance. Merely citing remote index as the reason cusp-jet inversion fails is no longer justified; the unresolved quantitative burden is complexity growth plus the extraction of those centered jets from non-singular source data.