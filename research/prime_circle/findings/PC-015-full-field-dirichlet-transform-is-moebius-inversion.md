# PC-015 — Dirichlet scale transforms of the full primitive-shell field are Möbius inversion, not a new zeta mechanism

**Status:** `DECISIVE-NEGATIVE` + `LITERATURE+DERIVED` + `EXACT-DERIVED`.

## Claim

The most canonical linear way to retain the full interior prime-circle field while introducing a complex scale variable is to Dirichlet-transform the primitive-shell potentials over the polygon level. That construction does encode every zero of the Riemann zeta function as a singularity of the transformed field, but the encoding is not an independently derived spectral mechanism: the factor `1/zeta(s)` is exactly the Dirichlet-series form of Möbius inversion between full root-of-unity layers and primitive/cyclotomic layers.

Moreover, the exact circle inversion `z -> 1/conj(z)` acts only on the spatial variable. After the same scale transform it leaves `s` unchanged and contributes the classical totient Dirichlet series `zeta(s-1)/zeta(s)`. Therefore the intrinsic prime-circle interior/exterior duality does **not** by itself induce the zeta functional equation `s <-> 1-s`.

This closes two natural but misleading branches:

1. keeping the complete harmonic field `U_n(z)` and then applying the standard `n^{-s}` scale transform does not escape classical Ramanujan/Möbius inversion;
2. identifying spatial circle inversion with the functional-equation reflection requires additional structure not present in the exact geometry.

## 1. Exact analytic primitive-shell field

For `|z|<1`, define

\[
\widehat\Phi_1(z)=1-z,
\qquad
\widehat\Phi_n(z)=\Phi_n(z)\quad(n\ge2),
\]

and take the unique holomorphic branch

\[
L_n(z)=\Log\widehat\Phi_n(z),
\qquad L_n(0)=0.
\]

Its real part is the logarithmic potential of the primitive `n`-th root shell, including the harmless sign normalization at `n=1`:

\[
\Re L_n(z)=U_n(z).
\]

Since the primitive roots are exactly the Fourier support of the Ramanujan sum,

\[
c_n(m)=\sum_{\substack{1\le a\le n\\(a,n)=1}}e^{2\pi i am/n},
\]

we have the exact interior expansion

\[
\boxed{
L_n(z)=-\sum_{m\ge1}\frac{c_n(m)}{m}z^m.
}
\]

This is already the analytic form of the full two-dimensional primitive-shell potential: the angular/radial dependence has not yet been collapsed to the common vertex.

## 2. The complete Dirichlet scale transform factors through `1/zeta(s)`

For `Re(s)>1`, define

\[
\mathcal L(s,z)
:=\sum_{n\ge1}\frac{L_n(z)}{n^s}.
\]

For fixed `|z|<1`, the exponential decay in the Fourier index justifies exchanging the sums. The classical Ramanujan Dirichlet series

\[
\sum_{n\ge1}\frac{c_n(m)}{n^s}
=\frac{\sigma_{1-s}(m)}{\zeta(s)}
\]

then gives

\[
\boxed{
\mathcal L(s,z)
=-\frac1{\zeta(s)}
\sum_{m\ge1}\frac{\sigma_{1-s}(m)}{m}z^m.
}
\]

Expanding the divisor sum `sigma_{1-s}(m)` and writing `m=dk` yields the equivalent field-level identity

\[
\boxed{
\mathcal L(s,z)
=\frac1{\zeta(s)}
\sum_{d\ge1}\frac{\Log(1-z^d)}{d^s}.
}
\]

This is precisely the logarithmic form of the weighted infinite-cyclotomic-product identity proved from Ramanujan sums by Bal (Theorem 2.2 and Remark 2.4 of the corrected v2).

The factorization also follows directly from the cyclotomic decomposition

\[
1-z^n=\prod_{d\mid n}\widehat\Phi_d(z).
\]

Taking logarithms, primitive-shell extraction is Möbius inversion on the divisor lattice. Dirichlet transformation turns convolution with the Möbius function into multiplication by

\[
\sum_{n\ge1}\frac{\mu(n)}{n^s}=\frac1{\zeta(s)}.
\]

So the appearance of reciprocal zeta is forced algebraically before any spectral interpretation is attempted.

## 3. Zeta zeros really are poles of the field — but tautologically

For each fixed `|z|<1`, put

\[
N(s,z):=\sum_{d\ge1}d^{-s}\Log(1-z^d).
\]

Because `Log(1-z^d)=O(z^d)`, the series for `N(s,z)` converges locally uniformly for every complex `s`; hence `N` is entire in `s`. Therefore

\[
\mathcal L(s,z)=\frac{N(s,z)}{\zeta(s)}
\]

provides a meromorphic continuation of the transformed field.

At any zeta zero `rho`,

\[
N(\rho,z)=-z+O(z^2)
\qquad(z\to0),
\]

because the `d=1` term is `Log(1-z)=-z+O(z^2)` while all `d>=2` terms start at order `z^2`. Thus for every fixed zero `rho`, all sufficiently small nonzero interior observation points satisfy

\[
N(\rho,z)\ne0,
\]

so `mathcal L(s,z)` has a genuine pole at `s=rho`.

This is an exact geometric representation of the zeros as singularities of a full-field transform, but it is **not independent evidence about their location**: the poles are inherited from the explicit Möbius-inversion denominator `1/zeta(s)`. No self-adjoint operator, positivity statement, or new zero condition has been produced.

At the boundary value `s=1`, the distinction is especially instructive. Analytic continuation makes `1/zeta(s)` vanish at `s=1`, but convergence of the original `sum_n L_n(z)/n` through its natural partial sums is equivalent to the prime number theorem. Bal's corrected v2 proves this using the classical Ramanujan identity rather than an unjustified interchange of conditionally convergent sums.

## 4. Exact spatial inversion does not become the zeta functional equation

PC-003 gives, for the real potential and all `n`,

\[
U_n(z)=\varphi(n)\log|z|+U_n(1/\bar z).
\]

For `|z|>1` and initially `Re(s)>2`, summing with weight `n^{-s}` gives

\[
\mathcal U(s,z)-\mathcal U(s,1/\bar z)
=\log|z|\sum_{n\ge1}\frac{\varphi(n)}{n^s}.
\]

Using the classical totient Dirichlet series,

\[
\sum_{n\ge1}\frac{\varphi(n)}{n^s}
=\frac{\zeta(s-1)}{\zeta(s)},
\]

we obtain

\[
\boxed{
\mathcal U(s,z)-\mathcal U(s,1/\bar z)
=\log|z|\frac{\zeta(s-1)}{\zeta(s)}.
}
\]

The crucial point is structural: circle inversion changes `z` to `1/conj(z)` while leaving the same scale parameter `s` on both sides. It does not produce `s -> 1-s`, the gamma factor, or the `pi^{-s/2}` completion of zeta. The appearance of a zeta ratio is again the classical Dirichlet transform of an arithmetic coefficient, here `phi(n)`.

Therefore the attractive slogan

\[
\text{inside/outside circle duality}
\stackrel?\longleftrightarrow
\text{zeta functional equation}
\]

is false for the exact linear scale transform. Any genuine bridge between the two symmetries must contain an additional operation that acts nontrivially on the scale variable and must be derived rather than chosen to imitate the known functional equation.

## 5. Prior art / novelty audit

The underlying analytic identities are classical or now explicitly in the literature:

- Ramanujan's 1918 work gives the Ramanujan sums and their arithmetic expansions; the Dirichlet generating identity `sum_n c_n(m)n^{-s}=sigma_{1-s}(m)/zeta(s)` is standard.
- Hartosh Singh Bal, *Constancy of an Infinite Cyclotomic Product via Ramanujan Sums*, arXiv:2511.16975v2 (6 Jan 2026; also Integers 25 (2025), A96), defines the same normalized cyclotomic factors `hat Phi_n`, derives `Log hat Phi_n(z)=-sum_m c_n(m)z^m/m`, and proves the weighted product identity whose logarithm is the formula for `mathcal L(s,z)` above. Remark 2.4 explicitly rewrites it as a ratio expression for zeta.
- `sum phi(n)n^{-s}=zeta(s-1)/zeta(s)` is the standard Dirichlet series for Euler's totient.

Accordingly, **no novelty is claimed for the transformed-field identity or its reciprocal-zeta factor**. The program-specific contribution of PC-015 is the negative classification: even preserving the complete interior harmonic field does not rescue the canonical linear Dirichlet-transform route from being Möbius inversion in analytic dress, and the exact spatial inversion does not implement the zeta functional equation.

## 6. What remains alive

PC-015 does not rule out prime-circle mechanisms that use information before this linear collapse. In particular it leaves open:

- nonlinear couplings between Fourier modes or primitive shells;
- genuinely two-dimensional operators whose scale dynamics is not diagonalized by the weight `n^{-s}`;
- boundary-limit phenomena on `|z|=1`, where convergence and singular support differ sharply from the interior;
- a canonically derived transform that acts simultaneously on spatial inversion and logarithmic scale, rather than simply attaching a Dirichlet weight afterward;
- cross-level interactions that are not recoverable from one linearly superposed field.

But future work should treat both `1/zeta(s)` in the linear interior transform and `zeta(s-1)/zeta(s)` in the transformed inversion law as **known Möbius/totient background**, not as evidence for a new RH mechanism.
