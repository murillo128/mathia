# PC-191 — inversion-even reciprocal cyclotomic amplitudes have strictly positive Fourier spectrum

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-NEGATIVE` for the canonical inversion-even pure-exponential centering of fixed positive-integer reciprocal cyclotomic amplitudes. The resulting real Fourier transform is strictly positive at every frequency, so this natural functional-equation-style completion cannot produce a real spectral zero set, let alone a critical-line mechanism. This does not classify minimally renormalized differences, non-integer powers, signed combinations, shell-dependent matrix kernels, cross-level couplings, or global uniformization routes.

PC-190 showed that fixed integer reciprocal powers of the local amplitude `Phi_n(e^{-x})` have eventually quasipolynomial coefficient dynamics and Mellinize to finite rational-shift Hurwitz/Barnes data. A different possible escape is to use cyclotomic reciprocity itself as an intrinsic inversion symmetry: extend the positive radial variable to the full logarithmic line, apply the unique pure exponential centering that makes the raw amplitude even under `x <-> -x`, and then read its Fourier spectrum. The symmetry is exact, but its integer reciprocal powers are more rigid than expected: their Fourier transforms are everywhere strictly positive.

## 1. Cyclotomic reciprocity fixes a unique inversion-even centering

Let `n>1`, put

\[
\phi:=\varphi(n),
\qquad
C_n(x):=e^{\phi x/2}\Phi_n(e^{-x}),
\qquad x\in\mathbb R.
\tag{1}
\]

For `n>1`, cyclotomic polynomials are self-reciprocal:

\[
\Phi_n(z)=z^{\phi}\Phi_n(z^{-1}).
\tag{2}
\]

Therefore

\[
C_n(-x)
=e^{-\phi x/2}\Phi_n(e^x)
=e^{-\phi x/2}e^{\phi x}\Phi_n(e^{-x})
=C_n(x).
\tag{3}
\]

Moreover this half-growth factor is forced among pure exponential gauges. If

\[
C_{n,a}(x):=e^{ax}\Phi_n(e^{-x})
\]

is even for all real `x`, then (2) gives

\[
C_{n,a}(-x)=e^{(\phi-a)x}\Phi_n(e^{-x}),
\]

so equality with `C_{n,a}(x)` requires

\[
\boxed{a=\phi/2.}
\tag{4}
\]

Thus (1) is not a tunable completion chosen to manufacture a spectrum: it is the unique pure exponential centering of the raw cyclotomic amplitude compatible with the intrinsic inversion `z <-> z^{-1}`.

For a fixed integer `m>=1`, define the reciprocal amplitude

\[
H_{n,m}(x):=C_n(x)^{-m}
=e^{-m\phi x/2}\Phi_n(e^{-x})^{-m}.
\tag{5}
\]

Because `C_n` is positive on the real logarithmic line, even, and grows like `exp(phi |x|/2)` at infinity, `H_{n,m}` is positive, even, continuous, and belongs to `L^1(R)`.

## 2. Primitive-root pairing turns the reciprocal amplitude into strip Poisson factors

Assume first `n>2`. Pair the primitive roots as

\[
e^{\pm i\theta_1},\ldots,e^{\pm i\theta_r},
\qquad
0<\theta_j<\pi,
\qquad
r=\phi/2.
\]

For one conjugate pair,

\[
(e^{-x}-e^{i\theta})(e^{-x}-e^{-i\theta})
=2e^{-x}(\cosh x-\cos\theta).
\tag{6}
\]

Multiplying all pairs and applying the centering in (1) yields the exact factorization

\[
\boxed{
C_n(x)=\prod_{j=1}^{r}2(\cosh x-\cos\theta_j).
}
\tag{7}
\]

Hence

\[
H_{n,1}(x)=\prod_{j=1}^{r}g_{\theta_j}(x),
\qquad
g_\theta(x):=\frac{1}{2(\cosh x-\cos\theta)}.
\tag{8}
\]

The elementary factor `g_theta` is, after rescaling, exactly the Poisson kernel of a horizontal strip. With Fourier convention

\[
\widehat f(t)=\int_{\mathbb R}f(x)e^{-itx}\,dx,
\tag{9}
\]

the classical strip-Poisson transform gives

\[
\boxed{
\widehat g_\theta(t)
=\frac{\pi}{\sin\theta}
\frac{\sinh((\pi-\theta)t)}{\sinh(\pi t)},
\qquad 0<\theta<\pi,
}
\tag{10}
\]

with the continuous value

\[
\widehat g_\theta(0)=\frac{\pi-\theta}{\sin\theta}.
\tag{11}
\]

Every quantity on the right of (10) has the same sign in numerator and denominator for nonzero real `t`, while (11) is positive. Therefore

\[
\boxed{\widehat g_\theta(t)>0\quad\text{for every }t\in\mathbb R.}
\tag{12}
\]

The factors also have exponentially decaying Fourier transforms, so the product/convolution theorem applies without a distributional subtlety. From (8),

\[
\widehat H_{n,1}
=(2\pi)^{1-r}\,
\widehat g_{\theta_1}*\cdots*\widehat g_{\theta_r}.
\tag{13}
\]

A convolution of continuous functions that are strictly positive everywhere is strictly positive everywhere. Thus

\[
\boxed{
\widehat H_{n,1}(t)>0
\qquad(n>2,\ t\in\mathbb R).
}
\tag{14}
\]

For integer `m>=1`, `H_{n,m}=H_{n,1}^m`, so another application of the product/convolution theorem gives

\[
\widehat H_{n,m}
=(2\pi)^{1-m}\underbrace{\widehat H_{n,1}*\cdots*\widehat H_{n,1}}_{m\text{ factors}},
\tag{15}
\]

and consequently

\[
\boxed{
\widehat H_{n,m}(t)>0
\quad\text{for all }n>2,\ m\in\mathbb N,\ t\in\mathbb R.
}
\tag{16}
\]

## 3. The exceptional two-point shell is positive as well

For `n=2`, `Phi_2(z)=1+z` and `phi(2)=1`, so

\[
C_2(x)=e^{x/2}(1+e^{-x})=2\cosh(x/2).
\tag{17}
\]

Therefore

\[
H_{2,1}(x)=\frac{1}{2\cosh(x/2)}
\]

and the classical hyperbolic-secant transform gives

\[
\boxed{
\widehat H_{2,1}(t)=\frac{\pi}{\cosh(\pi t)}>0.
}
\tag{18}
\]

Integer powers again preserve strict Fourier positivity by convolution. Combining (16) and (18) proves the exact all-level statement

\[
\boxed{
\widehat H_{n,m}(t)>0
\quad\text{for every }n>1,\ m\in\mathbb N,\ t\in\mathbb R.
}
\tag{19}
\]

## 4. Matched prime and mixed-prime controls

The smallest nontrivial examples show that the effect is geometric rather than a prime-power selector.

For `n=3`, the primitive pair has `theta=2pi/3`, and (10) gives

\[
\boxed{
\widehat H_{3,1}(t)
=\frac{2\pi}{\sqrt3}
\frac{\sinh(\pi t/3)}{\sinh(\pi t)}>0.
}
\tag{20}
\]

For the mixed-prime level `n=6`, the primitive pair has `theta=pi/3`, giving

\[
\boxed{
\widehat H_{6,1}(t)
=\frac{2\pi}{\sqrt3}
\frac{\sinh(2\pi t/3)}{\sinh(\pi t)}>0.
}
\tag{21}
\]

The `n=2` control (18) is positive as well. Thus strict positivity is not selecting primes, prime powers, or mixed-prime shells; it is forced by the Poisson-factor geometry of every reciprocal cyclotomic amplitude after the canonical inversion-even centering.

Direct numerical quadrature at several nonzero frequencies for `n=2,3,6` agrees with (18), (20), and (21), providing an independent normalization check on the `pi` factors in the Fourier convention (9).

## 5. Prior art and novelty audit

The analytic ingredient is classical strip potential theory, not a new transform identity.

Thiago Carvalho Corso, **A Generalized Three Lines Lemma in Hardy-like Spaces**, *Complex Analysis and Operator Theory* **20**, article 146 (2026), DOI `10.1007/s11785-026-01997-3`, Appendix B, writes the strip Poisson kernel

\[
\mathscr P_y(u)=\frac12\frac{\sin(\pi y)}{\cosh(\pi u)-\cos(\pi y)}
\]

and proves its explicit Fourier transform. Taking `y=theta/pi`, rescaling `x=pi u`, and using the convention (9) gives exactly (10). The same appendix cites D. V. Widder, **Functions harmonic in a strip**, *Proceedings of the American Mathematical Society* **12** (1961), 67--72, DOI `10.1090/S0002-9939-1961-0132838-8`, for the classical strip Poisson representation.

Searches against the exact transform, cyclotomic polynomials evaluated at `e^{-x}`, positive-definite cyclotomic amplitudes, and combinations of `cyclotomic`, `cosh`, and `Fourier transform` did not locate a reference packaging (7)--(19) as a cyclotomic/RH statement. No novelty is claimed for self-reciprocity, the strip kernel, Fourier product/convolution, or positivity. The durable contribution is the **Prime-Circle boundary theorem**: once the geometry itself forces the unique half-growth inversion gauge, all fixed positive-integer reciprocal amplitudes land inside a strictly positive-definite strip-Poisson product class and therefore have no real Fourier spectral zeros.

This also prevents a misleading analogy with a zeta functional equation. The symmetry `x <-> -x` is genuine, but its canonical scalar spectral readout is positivity, not a critical zero locus. Neither the gamma factor nor a distinguished `1/2` in a complex spectral parameter is generated by (19); the half in (1) is simply half the polynomial degree forced by reciprocal centering.

## 6. What this rules out and what remains open

The exact obstruction is the route

\[
\text{integer reciprocal cyclotomic amplitude}
\longrightarrow
\text{unique inversion-even half-growth completion}
\longrightarrow
\text{real Fourier zero spectrum}
\longrightarrow
\text{RH mechanism}.
\tag{22}
\]

Equation (19) kills this route at the spectral step: the real Fourier zero set is empty. Increasing the positive integer reciprocal power does not help, because multiplication in physical space only convolves already positive spectra.

The theorem is deliberately narrower than all possible inversion constructions. It does **not** classify the minimally renormalized even difference `Phi_n(e^{-|x|})^{-m}-1`; that subtraction destroys the direct positive-product argument. It does not prove strict Fourier positivity for fractional or other non-integer reciprocal powers, nor for signed linear combinations. It also does not address shell-dependent or matrix-valued nonlocal kernels, cross-level/all-shell couplings, singular boundary domains, or the global uniformization/monodromy sector.

The distinction from PC-029 is important. PC-029 used a minimally renormalized logarithmic potential whose even radial continuation removes the asymptotic constant before scalarization. Here the object is the **raw amplitude**, and the factor `exp(phi x/2)` is the unique pure exponential gauge making that amplitude reciprocal-even. For the even continuation one may equivalently write

\[
\log C_n(x)
=\log\Phi_n(e^{-|x|})+\frac{\phi}{2}|x|.
\tag{23}
\]

This is a different normalization question and therefore a genuine new boundary relative to the earlier log-potential analysis.

## 7. Falsification and audit checks

The claim is exact and can be audited without any RH assumption.

- Verify cyclotomic reciprocity (2) and check that an arbitrary pure exponential gauge is even only at `a=phi/2`.
- Pair conjugate primitive roots and recover (7) exactly; failure of a factor `2` or the half-growth cancellation falsifies the normalization.
- Rescale the standard strip Poisson transform to obtain (10), then check the `t=0` limit (11).
- Numerically Fourier-transform `H_{2,1}`, `H_{3,1}`, and `H_{6,1}` and compare with (18), (20), and (21).
- Search for a real zero of `widehat H_{n,m}` at any tested `n,m`; one genuine zero would falsify (19), because the proof claims strict positivity, not merely nonnegativity.

## Research consequence

PC-190 left open non-polynomial Fourier/spectral uses of the reciprocal amplitude even after its Mellin coefficients classicalized. PC-191 closes the most canonical inversion-symmetric version of that escape: **cyclotomic reciprocity does provide an intrinsic full-line completion, but integer reciprocal powers become products of strip Poisson kernels and have strictly positive Fourier spectrum**.

A surviving functional-equation or spectral-zero route must therefore introduce structure that breaks this positive product class before Fourier scalarization: a genuinely signed/renormalized observable, a geometry-forced non-integer operation with independent significance, shell-dependent nonlocal mixing, cross-level coupling, or a global operator/uniformization mechanism. Merely centering the reciprocal amplitude by its intrinsic inversion symmetry cannot produce the desired zero geometry.