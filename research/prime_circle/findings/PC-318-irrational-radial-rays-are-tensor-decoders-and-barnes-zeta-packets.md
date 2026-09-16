# PC-318 — irrational radial rays are exact tensor decoders and Barnes-zeta packets

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-NEGATIVE` for the remaining irrational one-parameter radial escape from PC-317.

PC-316 showed that multiplying two oriented prime-level Poisson/Hardy fields before scalar angular compression preserves two independent Fourier indices. PC-317 then proved that every **rational** one-parameter radial ray collapses those indices into eventually quasipolynomial coefficient data and hence a finite Hurwitz-zeta packet. The complementary case is an irrational ratio of the two effective radial rates.

That case does avoid the rational collision pattern, but in the opposite way from a useful compression: it is exactly lossless. Periodicity lets one strip off two known geometric denominators and obtain a finite exponential polynomial whose `qr` frequencies are all distinct when the rate ratio is irrational. A Vandermonde inversion therefore recovers the complete residue tensor `a(i)b(j)`. For the canonical normalized Prime-Circle sources, the row and column sums then recover both one-level Fourier packets separately, hence both original cyclic sources.

The Mellin transform is also classical. Splitting the two periodic indices into residue classes writes it as a finite linear combination of Barnes double zeta functions with positive periods. Thus the dichotomy for **every positive one-parameter radial ray** of the PC-316 construction is now exact: rational rate ratio gives the finite Hurwitz/quasipolynomial collapse of PC-317; irrational rate ratio gives a lossless two-index decoder whose one-variable Mellin image is a finite Barnes double-zeta packet.

This closes the proposed irrational-ray escape as a nonreconstructive scalar invariant. It does not rule out a future theorem about zeros of the particular canonical Barnes combination, but such a theorem would have to add an independent zero-selection mechanism; the radial restriction itself supplies no intermediate information quotient.

## 1. Irrational radial restriction

Use the PC-316 notation. At the common anchor,

\[
H_{q,r}^{f,g}(x,y,z)
=\sum_{k,l\ge1}a(k)b(l)e^{-kx-ly-(k+l)z},
\tag{1}
\]

where `q,r` are distinct primes and

\[
a(k)=\widehat f(k\bmod q),\qquad
b(l)=\widehat g(l\bmod r)
\tag{2}
\]

are periodic sequences of periods `q` and `r`.

Restrict to a positive radial ray

\[
x=\alpha t,\qquad y=\beta t,\qquad z=\gamma t,
\qquad t>0,
\tag{3}
\]

and define the effective rates

\[
\lambda:=\alpha+\gamma>0,\qquad
\mu:=\beta+\gamma>0.
\tag{4}
\]

Then

\[
\boxed{
R(t):=H_{q,r}^{f,g}(\alpha t,\beta t,\gamma t)
=\sum_{k,l\ge1}a(k)b(l)e^{-(\lambda k+\mu l)t}.
}
\tag{5}
\]

Equivalently, by the PC-316 semigroup factorization,

\[
R(t)=A_{q,f}(\lambda t,0)B_{r,g}(\mu t,0).
\tag{6}
\]

The unresolved case of PC-317 is

\[
\boxed{\lambda/\mu\notin\mathbb Q.}
\tag{7}
\]

## 2. Periodicity exposes a finite residue tensor

Write

\[
a_i:=a(i),\quad 1\le i\le q,
\qquad
b_j:=b(j),\quad 1\le j\le r.
\tag{8}
\]

Periodicity gives the exact geometric-series identities

\[
\sum_{k\ge1}a(k)e^{-\lambda kt}
=\frac{\sum_{i=1}^{q}a_i e^{-\lambda i t}}
{1-e^{-q\lambda t}},
\qquad
\sum_{l\ge1}b(l)e^{-\mu lt}
=\frac{\sum_{j=1}^{r}b_j e^{-\mu j t}}
{1-e^{-r\mu t}}.
\tag{9}
\]

Therefore, after multiplying the observed ray by the two known denominators,

\[
\boxed{
E(t):=(1-e^{-q\lambda t})(1-e^{-r\mu t})R(t)
=\sum_{i=1}^{q}\sum_{j=1}^{r}
C_{ij}e^{-\rho_{ij}t},
}
\tag{10}
\]

where

\[
C_{ij}:=a_i b_j,
\qquad
\rho_{ij}:=\lambda i+\mu j.
\tag{11}
\]

Thus the infinite one-parameter signal is equivalent to a finite exponential polynomial carrying exactly the `q x r` residue tensor.

If two frequencies coincide,

\[
\lambda i+\mu j=\lambda i'+\mu j',
\tag{12}
\]

then

\[
\frac{\lambda}{\mu}(i-i')=-(j-j').
\tag{13}
\]

Under (7), the right-hand side can equal the left only when

\[
i=i',\qquad j=j'.
\tag{14}
\]

Hence all `qr` frequencies in (10) are pairwise distinct.

## 3. The ray reconstructs the complete two-index coefficient array

Distinct real exponentials are linearly independent, but here the reconstruction can be written as a finite exact Vandermonde system. Let

\[
M:=qr
\tag{15}
\]

and enumerate the distinct frequencies in (10) as `rho_1,...,rho_M`, with corresponding coefficients `C_1,...,C_M`. At any fixed `t_0>0`, the first `M` derivatives satisfy

\[
(-1)^mE^{(m)}(t_0)
=\sum_{\nu=1}^{M}C_\nu\rho_\nu^m e^{-\rho_\nu t_0},
\qquad 0\le m<M.
\tag{16}
\]

The coefficient matrix is a Vandermonde matrix times a nonzero diagonal matrix. Its determinant is, up to the usual sign,

\[
\boxed{
\det V(t_0)
=e^{-t_0\sum_\nu\rho_\nu}
\prod_{1\le \nu<\eta\le M}(\rho_\eta-\rho_\nu)
\neq0.
}
\tag{17}
\]

Consequently the germ of `E`, hence the original ray signal `R`, determines every coefficient

\[
\boxed{C_{ij}=a_i b_j.}
\tag{18}
\]

Because `a` and `b` are periodic, (18) determines the entire infinite PC-316 coefficient array

\[
(k,l)\longmapsto a(k)b(l).
\tag{19}
\]

There is therefore no nontrivial information quotient at the two-index level: irrationality removes the additive collisions precisely by making the one-dimensional frequency encoding injective.

For the canonical Prime-Circle prime-support sources of PC-306--PC-317, finite Fourier orthogonality gives

\[
\sum_{i=1}^{q}a_i=qf_q(0)=-1,
\qquad
\sum_{j=1}^{r}b_j=rg_r(0)=-1.
\tag{20}
\]

Hence the tensor itself separates its two factors without even a scalar ambiguity:

\[
\boxed{
a_i=-\sum_{j=1}^{r}C_{ij},
\qquad
b_j=-\sum_{i=1}^{q}C_{ij}.}
\tag{21}
\]

The inverse finite Fourier transforms then recover `f_q` and `g_r`, and therefore the complete normalized prime-support measures used to construct the two fields. For these canonical sources the irrational radial trace is not merely tensor-injective: it is an exact decoder of both input cyclic sources.

## 4. The one-variable Mellin image is a Barnes double-zeta packet

Since `a,b` are bounded, (5) has the usual two-dimensional counting growth near `t=0`, so for `Re(s)>2` termwise Mellin integration is absolutely valid:

\[
\boxed{
\int_0^\infty t^{s-1}R(t)\,dt
=\Gamma(s)D_{\lambda,\mu}(s),
}
\tag{22}
\]

with

\[
D_{\lambda,\mu}(s)
:=\sum_{k,l\ge1}
\frac{a(k)b(l)}{(\lambda k+\mu l)^s}.
\tag{23}
\]

Split

\[
k=i+qm,\qquad l=j+rn,
\qquad
1\le i\le q,\ 1\le j\le r,
\quad m,n\ge0.
\tag{24}
\]

Using (18),

\[
\boxed{
D_{\lambda,\mu}(s)
=\sum_{i=1}^{q}\sum_{j=1}^{r}
C_{ij}
\zeta_2\!\left(
 s,\lambda i+\mu j\mid q\lambda,r\mu
\right),
}
\tag{25}
\]

where the Barnes double zeta is

\[
\zeta_2(s,w\mid \omega_1,\omega_2)
:=\sum_{m,n\ge0}
(w+m\omega_1+n\omega_2)^{-s},
\qquad \Re s>2.
\tag{26}
\]

This is exactly the classical Barnes family for positive `w,omega_1,omega_2`; no commensurability of the periods is required. Ruijsenaars' standard treatment, **On Barnes' multiple zeta and gamma functions**, *Advances in Mathematics* 156:1 (2000), 107--132, DOI `10.1006/aima.2000.1946`, gives the classical multiple-zeta framework and meromorphic continuation for positive parameters.

Thus irrationality does not create a new analytic species. It prevents the further one-dimensional lattice folding used in PC-317, leaving the established Barnes double-zeta object instead. When `lambda/mu` is rational, the same double lattice becomes commensurate and PC-317 gives the stronger finite Hurwitz/quasipolynomial reduction.

## 5. Exact inversion is not uniformly well-conditioned across growing levels

For fixed `q,r,lambda,mu`, (17) is a finite-dimensional exact inversion. That should not be confused with a uniform stable carrier as the polygon levels grow.

Put `theta=lambda/mu`, assumed irrational. By ordinary Diophantine approximation there are positive integers `h,k` with arbitrarily large `h` such that

\[
|\theta h-k|\longrightarrow0.
\tag{27}
\]

Choose prime levels larger than the corresponding `h` and `k`. Then the residue rectangles contain two distinct index pairs whose differences are `(h,-k)`, and their frequencies differ by

\[
\delta=\mu|\theta h-k|\longrightarrow0.
\tag{28}
\]

On any fixed observation interval `0\le t\le T`, two basis atoms with gap `delta` satisfy

\[
\sup_{0\le t\le T}
|e^{-\rho t}-e^{-(\rho+\delta)t}|
\le T\delta.
\tag{29}
\]

Therefore the inverse map from the full coefficient tensor to a finite-window ray signal has no level-uniform lower bound: its conditioning can diverge along growing conductors. This is a secondary boundary, not the main no-go. The decisive point is already exact injectivity: the irrational ray avoids PC-317's compression by retaining the full source packet.

## 6. Prior-art and novelty audit

No novelty is claimed for finite exponential-polynomial uniqueness, Vandermonde reconstruction, generalized Dirichlet-series uniqueness, Barnes multiple zeta functions, or their meromorphic continuation. The reconstruction in (16)--(17) is elementary and self-contained. The analytic destination in (25) is visibly the classical Barnes double zeta of Barnes/Ruijsenaars, including for irrational positive period ratios.

A directed literature search found the expected general Barnes multiple-zeta theory and general Dirichlet-series framework but not the exact Prime-Circle statement obtained by stripping the two source periods from the PC-316 radial trace. That absence is not a historical novelty claim. The line-specific durable content is the exact information classification: the irrational ray is injective on the full periodic cross-level tensor, and the canonical Prime-Circle normalization fixes the factorization so that both source packets are individually recoverable.

The Barnes classification also prevents an analytic overclaim. Meromorphic continuation or special-function status of (25) is inherited background, not a new bridge to the Riemann critical line. A future source-specific theorem about the zeros of the exact canonical linear combination in (25) is not excluded, but it would have to be proved as an additional theorem and tied independently to the RH target.

## 7. Research consequence

PC-317 and PC-318 together exhaust the positive one-parameter radial restrictions of the canonical PC-316 nonlinear Poisson product by the elementary dichotomy

\[
\lambda/\mu\in\mathbb Q
\quad\text{or}\quad
\lambda/\mu\notin\mathbb Q.
\tag{30}
\]

In the rational case, additive collisions force quasipolynomial coefficients and a finite Hurwitz packet. In the irrational case, collisions disappear, the ray exactly reconstructs the full two-index residue tensor, and its Mellin transform is a finite Barnes double-zeta packet. There is no third one-dimensional radial regime supplying a genuinely compressed but nonclassical invariant.

Accordingly the route

\[
\text{PC-316 two-index nonlinear field}
\longrightarrow
\text{one positive radial parameter}
\longrightarrow
\text{new nonreconstructive RH carrier}
\]

is closed for this construction. Any surviving mechanism must retain genuinely multivariable geometry, introduce a source-forced coupling not equivalent to the additive radial frequencies, or prove a new zero-selection theorem for the exact source-specific classical packet rather than treating the scalarization itself as progress.

## 8. Audit tests

The result has direct falsification checks:

1. Verify (9) by splitting each periodic sequence into residue classes modulo its prime period.
2. Multiply by the two geometric denominators and check the finite exponential polynomial (10).
3. Under `lambda/mu` irrational, test any alleged frequency collision and recover (13)--(14).
4. Form the derivative system (16) and verify the nonzero Vandermonde determinant (17).
5. For the canonical source, use the exact sums in (20) to recover each factor by (21), then invert the finite DFT.
6. Split (23) by residue classes and compare term by term with the Barnes definition (26).
7. As a control, restore a rational rate ratio and verify that frequency collisions reappear, consistent with PC-317's rational generating-function/Hurwitz classification.
