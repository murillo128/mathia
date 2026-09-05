# PC-176 — symmetric valuation-length refinement symbols are classical GCD operators bounded only for `sigma>1`

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-NEGATIVE` for the simplest arithmetic/conductor-decaying escape left open by PC-175. Once exact weak refinement has reduced a normalized first-order boundary form to a multiplicative Toeplitz symbol `Phi(m/l)`, the most canonical inversion-symmetric power-law decay in the intrinsic prime-valuation length is exactly the classical normalized GCD matrix. Its infinite `ell^2(N)` operator is bounded if and only if the decay exponent is strictly greater than `1`; in that bounded region it is uniformly positive and its exact norm is the elementary Euler product `zeta(sigma)^2/zeta(2 sigma)`. Thus the intrinsic half-density exponent `sigma=1/2` of PC-006 is not a bounded PC-174/175 weak-form symbol, and strengthening the decay until boundedness holds produces a classical GCD/Poisson operator whose only zeta dependence is the ordinary Euler product in its half-plane of convergence.

PC-175 proved that a nonzero bounded exact-refinement symbol cannot be a regular function of the ordinary real ratio `m/l`; it must instead be arithmetically sparse or decay with reduced numerator/denominator complexity. The first symmetric repair to test is therefore the valuation length already present in PC-006.

## 1. The canonical symmetric ratio length reproduces the GCD kernel

Write a positive rational in lowest terms as

\[
q=\frac ab,
\qquad (a,b)=1,
\]

and define its weighted prime-valuation length

\[
\boxed{
L(q)
=\sum_p |v_p(q)|\log p
=\log a+\log b
=\log(ab).
}
\tag{1}
\]

This length is intrinsic to the multiplicative refinement group: it is invariant under `q -> q^{-1}`, is proper on rational ratios, and is exactly the global valuation metric that appears in PC-006. Indeed PC-006 wrote

\[
\frac{\gcd(m,l)}{\sqrt{ml}}
=\exp\!\left[-\frac12 L(m/l)\right].
\tag{2}
\]

The simplest inversion-symmetric power-law conductor decay allowed by PC-175 is therefore

\[
\Phi_\sigma(q)=e^{-\sigma L(q)}=(ab)^{-\sigma},
\qquad \sigma>0.
\tag{3}
\]

If `g=gcd(m,l)`, then `m/g` and `l/g` are the reduced numerator and denominator of `m/l`, so the corresponding multiplicative-Toeplitz matrix is

\[
\boxed{
B_\sigma(m,l)
=\Phi_\sigma(m/l)
=\left(\frac{g^2}{ml}\right)^\sigma
=\frac{\gcd(m,l)^{2\sigma}}{(ml)^\sigma}.
}
\tag{4}
\]

Thus the candidate is not merely analogous to a GCD kernel: it is exactly the standard power GCD matrix. At `sigma=1/2`, (4) is the critical kernel of PC-006,

\[
B_{1/2}(m,l)=\frac{\gcd(m,l)}{\sqrt{ml}}.
\tag{5}
\]

This already gives a strong novelty warning: the most natural symmetric denominator-decay completion of PC-175 lands on the same classical GCD/Poisson family that forced the PC-006 downgrade.

## 2. Prime factorization makes the boundedness threshold exact

Let

\[
r_p=p^{-\sigma}.
\]

From (1),

\[
\boxed{
B_\sigma(m,l)
=\prod_p r_p^{|v_p(m)-v_p(l)|}.
}
\tag{6}
\]

For one prime, the local matrix on `ell^2(N_0)` is

\[
T(r)=\bigl(r^{|j-k|}\bigr)_{j,k\ge0}.
\tag{7}
\]

Its Toeplitz symbol is the ordinary Poisson kernel

\[
P_r(e^{it})
=\sum_{k\in\mathbb Z}r^{|k|}e^{ikt}
=\frac{1-r^2}{1-2r\cos t+r^2},
\tag{8}
\]

hence

\[
\boxed{
\|T(r)\|=\frac{1+r}{1-r},
\qquad
\frac{1-r}{1+r}I\le T(r)\le\frac{1+r}{1-r}I.
}
\tag{9}
\]

Now fix a finite set of primes `P` and compress `B_sigma` to the subspace spanned by integers all of whose prime factors lie in `P`. Under prime-exponent coordinates that compression is the tensor product

\[
\bigotimes_{p\in P}T(p^{-\sigma}).
\tag{10}
\]

Therefore every bounded extension of `B_sigma` to `ell^2(N)` would have to satisfy

\[
\|B_\sigma\|
\ge
\prod_{p\in P}\frac{1+p^{-\sigma}}{1-p^{-\sigma}}
\tag{11}
\]

for every finite `P`. Since

\[
\log\frac{1+x}{1-x}=2x+O(x^3),
\]

the right-hand products remain bounded over expanding prime sets exactly when

\[
\sum_p p^{-\sigma}<\infty,
\]

that is, exactly when

\[
\boxed{\sigma>1.}
\tag{12}
\]

Consequently

\[
\boxed{
0<\sigma\le1
\quad\Longrightarrow\quad
B_\sigma\text{ is unbounded on }\ell^2(\mathbb N).
}
\tag{13}
\]

This includes the geometry-derived `sigma=1/2` kernel (5). The PC-006 half-density therefore cannot itself serve as the bounded normalized operator required by the PC-174 weak-form framework.

## 3. In the bounded region the operator is an explicit positive Euler product

For `sigma>1`, the product of Poisson kernels

\[
F_\sigma(z)
=\prod_p P_{p^{-\sigma}}(z_p),
\qquad z\in\mathbb T^\infty,
\tag{14}
\]

converges uniformly because `sum_p p^{-sigma}<infinity`. Its Fourier coefficient at the finite valuation vector `alpha-beta` is exactly the product in (6), so under the standard Bohr identification of `ell^2(N)` with `H^2(T^infinity)`, `B_sigma` is the Toeplitz operator with positive symbol `F_sigma`.

The extreme values of every Poisson factor occur at `z_p=+1` and `z_p=-1`. Hence

\[
\sup F_\sigma
=\prod_p\frac{1+p^{-\sigma}}{1-p^{-\sigma}}
=\prod_p\frac{1-p^{-2\sigma}}{(1-p^{-\sigma})^2}
=\boxed{\frac{\zeta(\sigma)^2}{\zeta(2\sigma)}}.
\tag{15}
\]

Likewise

\[
\inf F_\sigma
=\boxed{\frac{\zeta(2\sigma)}{\zeta(\sigma)^2}}.
\tag{16}
\]

The finite-prime compressions in (10) approach the upper product, so the bound is sharp. Therefore

\[
\boxed{
\|B_\sigma\|
=\frac{\zeta(\sigma)^2}{\zeta(2\sigma)},
\qquad \sigma>1,
}
\tag{17}
\]

and the quadratic form satisfies

\[
\boxed{
\frac{\zeta(2\sigma)}{\zeta(\sigma)^2}I
\le B_\sigma\le
\frac{\zeta(\sigma)^2}{\zeta(2\sigma)}I.
}
\tag{18}
\]

Thus whenever the conductor power law is bounded, it is not near developing a zero mode: it is boundedly invertible with an explicit positive lower spectral bound.

## 4. Prior art already contains the whole ambient mechanism

The matrix (4) is a classical object. Lindqvist and Seip, **Note on some greatest common divisor matrices**, *Acta Arithmetica* 84:2 (1998), 149–154, DOI `10.4064/aa-84-2-149-154`, study exactly

\[
M_\sigma=\left(\frac{\gcd(m,l)^{2\sigma}}{m^\sigma l^\sigma}\right)
\]

and prove for `sigma>1` the sharp finite-section eigenvalue bounds with endpoints

\[
\frac{\zeta(2\sigma)}{\zeta(\sigma)^2}
\quad\text{and}\quad
\frac{\zeta(\sigma)^2}{\zeta(2\sigma)},
\]

while for `1/2<sigma<=1` the smallest and largest finite-section eigenvalues respectively tend to `0` and `infinity`. They explicitly derive the constants from Euler products and the Dirichlet-series/Riesz-basis framework.

Aistleitner, Berkes and Seip, already anchored in `research/prime_circle/SOURCES.md` for PC-006, study the same family for `0<alpha<=1`, identify its GCD sums with Poisson integrals on a polydisc, and obtain spectral-norm estimates, with the critical `alpha=1/2` case singled out. Hilberdink's multiplicative-Toeplitz work already anchored for PC-174 places ratio matrices of precisely this kind inside an established Euler-product/operator theory.

Accordingly no historical novelty is claimed for (4), its Poisson factorization, or the zeta bounds. The Prime-Circle-specific result is the **closure of the PC-175 escape**: once one chooses the most immediate inversion-symmetric valuation-length power law forced by the same metric already visible in PC-006, the candidate is exactly this classical operator and its boundedness threshold lies strictly to the right of `1`.

## 5. Why the zeta factor is not an RH mechanism

Equation (17) contains the Riemann zeta function, but only in the least informative way for the present target. It is the Euler product of independent primewise Poisson norms in the region where that product converges absolutely. No functional equation, gamma factor, critical-line symmetry, or zeta-zero divisor has been generated.

More strongly, the operator exists as a bounded positive fixed-form representative only for `sigma>1`, where `zeta(sigma)` is nonzero and (18) gives a uniform positive lower bound. Formally analytically continuing the scalar expression

\[
\frac{\zeta(\sigma)^2}{\zeta(2\sigma)}
\]

past `sigma=1` would not continue the bounded operator: the finite-prime compressions already force its norm to diverge there. Any zeros or poles seen after scalar meromorphic continuation would therefore belong to an externally continued Euler product, not to the spectrum of the Prime-Circle boundary operator.

The intrinsic `sigma=1/2` appearance from PC-006 is also not a hidden critical-line selector. It is precisely the classical critical GCD kernel, and (13) shows that it falls outside the bounded normalized weak-form class before any spectral determinant can be formed.

## 6. Exact boundary of the negative result

This finding does **not** eliminate all arithmetic symbols surviving PC-175. It rules out the canonical one-parameter family obtained by applying a uniform power law to the symmetric valuation length `L(q)`. Surviving possibilities include symbols supported on genuinely sparse rational sets, prime-dependent or valuation-dependent anisotropic decay, non-power-law arithmetic weights, shell-dependent families, unbounded normalized forms with a separately justified domain, nonlinear constructions, and cross-level operators not represented by one fixed multiplicative-Toeplitz symbol.

Those possibilities face a sharper novelty gate. A prime-dependent weight that merely replaces `p^{-sigma}` by chosen local radii is again an Euler product of one-prime Toeplitz/Poisson factors unless the Prime-Circle geometry forces a new coupling between primes. Likewise, choosing extra decay solely to move from the intrinsic `sigma=1/2` to the bounded region `sigma>1` is a repair parameter, not a derived RH mechanism.

The durable conclusion is therefore:

\[
\boxed{
\text{PC-175 regular-ratio escape}
\;\xrightarrow{\text{symmetric valuation power decay}}\;
\text{classical GCD/Poisson operator},
\qquad
B_\sigma\in\mathcal B(\ell^2)\iff\sigma>1.
}
\]

The zeta ratio in its norm is classical absolute-convergence data, not evidence for a new Prime-Circle route to the critical line.
