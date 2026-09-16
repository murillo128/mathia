# PC-322 — canonical Green slice is classical Hilbert criticality

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the most natural finite intermediate Mordell–Tornheim exponent left open by PC-321.

PC-316 identifies the canonical nonlinear cross-level Poisson product with the three-variable packet

\[
Z_{q,r}^{f,g}(s,t,u)
=\sum_{k,l\ge1}\frac{a(k)b(l)}{k^s l^t(k+l)^u}.
\tag{1}
\]

PC-319/PC-320 show that small positive `u` retains off-critical zeros, while PC-321 proves that the canonical `(5,7)` packet is zero-free on the full right `(s,t)` polyhalf-plane once `Re(u)>=5`. That leaves finite intermediate `u` as a possible escape, but it also raises a sharper question: is any intermediate exponent distinguished by the original Poisson geometry rather than chosen after inspecting zeros?

There is one particularly canonical candidate. Integrating the downstream Poisson depth with **no extra weight** applies the ordinary Green/resolvent of the positive-frequency radial generator and selects exactly `u=1`. At this value the additive kernel is the classical Hilbert matrix. Moreover, `u=1` is the exact operator-theoretic transition on `ell^2`: for real `u>1` the kernel is Hilbert–Schmidt, at `u=1` it is bounded and noncompact, and for `0<u<1` it is unbounded.

The same slice also produces the number `1/2`, but in a way that is decisively non-arithmetic. The source vectors `a(k)k^{-s}` and `b(l)l^{-t}` belong to `ell^2` exactly for `Re(s)>1/2` and `Re(t)>1/2`; this threshold is shared by every nonzero periodic source. Hence the canonical Green slice does contain an intrinsic **Hilbert-space critical boundary at one half**, but it is the standard Hardy-space-of-Dirichlet-series boundary, not a Riemann-zero selection law. It supplies no reason for zeros to lie on that boundary.

## 1. The coefficient-free downstream Green operator selects `u=1`

Use the PC-316 anchored field

\[
H_{q,r}^{f,g}(x,y,z)
=\sum_{k,l\ge1}a(k)b(l)e^{-kx-ly-(k+l)z}.
\tag{2}
\]

On each output Fourier mode, the positive radial generator has eigenvalue `k+l`. Therefore the coefficient-free Green operation

\[
\mathcal G H(x,y)
:=\int_0^\infty H(x,y,z)\,dz
\tag{3}
\]

gives, by absolute convergence for `x,y>0`,

\[
\boxed{
\mathcal G H(x,y)
=\sum_{k,l\ge1}
\frac{a(k)b(l)}{k+l}e^{-kx-ly}.
}
\tag{4}
\]

Mellinizing the two remaining input depths in any safe right half-plane yields

\[
\boxed{
\int_0^\infty\!\int_0^\infty
x^{s-1}y^{t-1}\mathcal G H(x,y)\,dx\,dy
=\Gamma(s)\Gamma(t)Z_{q,r}^{f,g}(s,t,1).
}
\tag{5}
\]

Thus `u=1` is not selected by fitting a zero pattern: it is the ordinary inverse of the downstream number generator. More generally, the Mellin factor `(k+l)^{-u}` is the fractional Green family

\[
(k+l)^{-u}
=\frac1{\Gamma(u)}\int_0^\infty z^{u-1}e^{-(k+l)z}\,dz,
\qquad \Re u>0,
\tag{6}
\]

so `u=1` is the unweighted, first inverse rather than an arbitrary fractional power. This does not make it unique among all conceivable nonlocal operators, but it makes it the cleanest source-independent intermediate slice to test after PC-321.

## 2. `u=1` is exactly the classical Hilbert-matrix threshold

For real `u>0`, let

\[
(K_u)_{kl}:=\frac1{(k+l)^u},
\qquad k,l\ge1.
\tag{7}
\]

There is an exact phase change at `u=1`.

For `u>1`,

\[
\|K_u\|_{\mathcal S_2}^2
=\sum_{k,l\ge1}(k+l)^{-2u}
=\sum_{n\ge2}(n-1)n^{-2u}<\infty,
\tag{8}
\]

so `K_u` is Hilbert–Schmidt and therefore compact.

At `u=1`, reindexing `k=j+1`, `l=m+1` gives

\[
(K_1)_{jm}=\frac1{j+m+2},
\qquad j,m\ge0,
\tag{9}
\]

which is the generalized Hilbert matrix `H_2`. Classical Hilbert inequality makes it bounded on `ell^2`. PC-075 already records the exact trace-class comparison `H_alpha-H_1 in S_1` for every `alpha>0`, while Magnus/Rosenblum give the noncompact absolutely continuous Hilbert channel for `H_1`. Consequently

\[
\boxed{K_1\text{ is bounded and noncompact, with }\sigma_{\rm ess}(K_1)=[0,\pi].}
\tag{10}
\]

For `0<u<1`, take the normalized positive vector

\[
x^{(N)}_k=N^{-1/2}\mathbf1_{1\le k\le N}.
\tag{11}
\]

Then

\[
\begin{aligned}
\langle x^{(N)},K_ux^{(N)}\rangle
&=\frac1N\sum_{1\le k,l\le N}(k+l)^{-u}\\
&\ge 2^{-u}N^{1-u}\longrightarrow\infty.
\end{aligned}
\tag{12}
\]

Hence `K_u` is unbounded on `ell^2` for every real `0<u<1`. Therefore

\[
\boxed{
0<u<1:\ \text{unbounded},
\qquad
u=1:\ \text{bounded noncompact Hilbert},
\qquad
u>1:\ \text{Hilbert--Schmidt}.
}
\tag{13}
\]

Here the middle symbol is the real exponent `u=1`; equation (13) is an operator classification, not a claim about zeros of (1).

## 3. The Green slice is a Hilbert matrix coefficient of Dirichlet-series source vectors

Define the source vectors

\[
v_a(s):=(a(k)k^{-s})_{k\ge1},
\qquad
v_b(t):=(b(l)l^{-t})_{l\ge1}.
\tag{14}
\]

Let `B(x,y):=\sum_k x_k(K_1y)_k`, the bounded complex-bilinear form induced by the Hilbert matrix. Whenever `v_a(s),v_b(t) in ell^2`,

\[
\boxed{
Z_{q,r}^{f,g}(s,t,1)
=B(v_a(s),v_b(t)).
}
\tag{15}
\]

In the safe region `Re(s)>1`, `Re(t)>1`, this is just the absolutely convergent series (1). Since the vector-valued maps in (14) are holomorphic wherever their `ell^2` norms converge, (15) gives a canonical holomorphic continuation of the `u=1` slice to the corresponding product half-plane.

For a nonzero periodic sequence `a`, put

\[
\mu_a:=\frac1q\sum_{h=1}^{q}|a(h)|^2>0
\tag{16}
\]

for any period `q`. Then

\[
\|v_a(s)\|_2^2
=\sum_{k\ge1}|a(k)|^2 k^{-2\Re s}.
\tag{17}
\]

Because `|a(k)|^2` is periodic with positive mean, its Dirichlet series has a simple pole at exponent `1` with residue `mu_a`. Therefore

\[
\boxed{
v_a(s)\in\ell^2\iff\Re s>\frac12,}
\tag{18}
\]

and, as `sigma downarrow 1/2`,

\[
\boxed{
\|v_a(\sigma+i\tau)\|_2^2
\sim\frac{\mu_a}{2\sigma-1}.
}
\tag{19}
\]

The same statements hold for `b`. Thus (15) gives

\[
\boxed{
Z_{q,r}^{f,g}(s,t,1)
\text{ a bounded-Hilbert-form realization for }
\Re s>\tfrac12,\ \Re t>\tfrac12.
}
\tag{20}
\]

For the canonical pair `(5,7)`, PC-319 gives the exact source packets. Parseval for the unnormalized finite Fourier transform gives

\[
\mu_{a_5}=\frac45,
\qquad
\mu_{b_7}=\frac5{14},
\tag{21}
\]

so both source norms really diverge at the same one-half boundary.

## 4. Why the appearance of `1/2` is a false RH positive

Equation (20) looks superficially suggestive: the same real part `1/2` that defines the Riemann critical line is the natural Hilbert-space boundary of the canonical Green slice. The matched control is decisive, however.

For **every** nonzero periodic coefficient sequence `c(k)`, regardless of whether it comes from primes, roots of unity, an arbitrary residue mask, or a matched non-prime control,

\[
(c(k)k^{-s})_{k\ge1}\in\ell^2
\iff \Re s>\frac12.
\tag{22}
\]

The number `1/2` therefore comes from square summability of power weights, not from Prime-Circle arithmetic. This is exactly the classical Hardy/Hilbert space of Dirichlet series introduced by Hedenmalm--Lindqvist--Seip: square-summable Dirichlet coefficients naturally define analytic functions on `Re(s)>1/2`, with the boundary determined by Cauchy--Schwarz and the zeta reproducing kernel. The Prime-Circle source changes the vector inside that universal space, not the location of its Hilbert-space boundary.

There is also no Hilbert--Pólya statement hidden in (15). `Z(s,t,1)` is a **matrix coefficient** of a fixed classical Hilbert operator between parameter-dependent vectors. Its zeros are not eigenvalues of `K_1`; boundedness of the form supplies neither a functional equation nor any theorem confining those zeros to the boundary where the vectors cease to lie in `ell^2`. In fact the literal Hilbert-space realization breaks down on `Re(s)=1/2`; reaching that boundary requires a separate limiting or analytic-continuation prescription.

The distinction is structural:

\[
\boxed{
\text{Hilbert-space threshold at }\Re s=\tfrac12
\neq
\text{zero-selection theorem on }\Re s=\tfrac12.
}
\tag{23}
\]

Consequently the coincidence of the two numbers cannot itself count as an RH bridge.

## 5. Prior-art and novelty audit

All load-bearing analytic ingredients are classical and already anchored in `research/prime_circle/SOURCES.md`.

- Hilbert's inequality and the spectral theory of the Hilbert matrix are classical; Magnus (1950) and Rosenblum (1958) provide the standard noncompact continuous Hilbert channel used already in PC-075.
- PC-075 proves within Prime Circle that every generalized block `H_alpha` differs from the standard Hilbert matrix by trace class, so the reindexed `H_2` in (9) carries the same universal essential band.
- Hedenmalm, Lindqvist and Seip (1997) introduce the Hilbert space of Dirichlet series with square-summable coefficients and the natural right half-plane `Re(s)>1/2`; this is already the prior-art anchor for the same functional-analytic threshold elsewhere in the line.
- Brevig, Perfekt, Seip, Siskakis and Vukotic (2016) give an additional RH-adjacent warning: zeta/Dirichlet-series structure can coexist with a Hilbert-type operator and the classical continuous band without producing a Riemann-zero spectral realization.

A directed literature search also returned modern generalized-Hilbert-operator work and the standard `H^2` Dirichlet-series reproducing-kernel boundary at `Re(s)=1/2`. No novelty is claimed for either threshold separately or for Hilbert-matrix boundedness. The durable Prime-Circle content is the exact identification of the **coefficient-free PC-316 downstream Green slice** with this classical critical Hilbert form, together with the matched-source proof that its apparent one-half line is universal rather than arithmetic.

## 6. Research consequence and boundary

PC-321 left finite intermediate Mordell--Tornheim exponents open and required any useful proposal to explain why a particular intermediate regime is geometrically selected. PC-322 tests the strongest immediate candidate: the ordinary downstream Green inverse selects `u=1` without fitting a parameter.

The result is informative but negative for RH zero selection. The selected kernel is exactly classical Hilbert criticality, and the accompanying `Re(s)=Re(t)=1/2` boundary is forced by square summability for every nonzero periodic source. Thus the route

\[
\text{canonical Poisson product}
\longrightarrow
\text{ordinary downstream Green inverse }(u=1)
\longrightarrow
\text{Hilbert-space boundary at }1/2
\longrightarrow
\text{RH critical-line mechanism}
\]

fails at its last implication: the half-line is a universal functional-analytic threshold and contains no source-specific zero-selection theorem.

This does **not** prove that the actual function `Z_{5,7}(s,t,1)` has off-critical zeros, nor that it is zero-free, nor that every intermediate `0<u<5` slice is useless. It also does not rule out determinants or quotients built from several coupled packets, a source-forced operator whose kernel is not a fractional power of `k+l`, or a genuinely growing-level construction. What it closes is the tempting interpretation that the most canonical intermediate Green slice has discovered the Riemann critical line merely because both its operator and its Dirichlet source vectors become critical at familiar Hilbert-space thresholds.

## 7. Audit and falsification tests

The result has six exact checks:

1. integrate (2) in the downstream depth and verify the Green denominator `(k+l)^{-1}`;
2. reindex `K_1` to the generalized Hilbert matrix `H_2`;
3. verify the Hilbert--Schmidt sum (8) for `u>1` and the block-vector lower bound (12) for `0<u<1`;
4. reconstruct (15) as a bounded Hilbert matrix coefficient on `ell^2`;
5. for any nonzero periodic source, verify (18)--(19) from the positive mean of `|a(k)|^2`;
6. apply a matched arbitrary periodic source and check that the same one-half boundary persists without any prime arithmetic.

Failure of any of these bridges would invalidate the stated classicalization. Passing all six establishes only the operator/representation boundary above; it deliberately makes no theorem-level claim about the zero set of the `u=1` Mordell--Tornheim slice itself.
