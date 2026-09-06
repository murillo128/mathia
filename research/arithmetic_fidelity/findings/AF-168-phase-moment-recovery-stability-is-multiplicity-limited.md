# AF-168 — Phase-moment zero recovery is globally Hölder and multiplicity-limited

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `QUANTITATIVE-RECOVERY`, `PHASE/ORIENTATION`, `NO-NOVELTY-CLAIM`

## Claim

AF-167 proves exact recovery of a degree-`n` finite Blaschke zero divisor from the degree together with the first `n` positive Fourier coefficients of the boundary phase derivative. Exact recoverability is not the same as stable recoverability. In the natural moment coordinates supplied by AF-167, the inverse map is globally only Hölder in the worst case, and the optimal local Hölder exponent is controlled by root multiplicity.

Let an unordered degree-`n` divisor in the closed unit disk be

\[
A=\{a_1,\ldots,a_n\},
\qquad |a_j|\le 1,
\]

with multiplicity, and define its retained phase-moment vector

\[
M_n(A)=(p_1(A),\ldots,p_n(A)),
\qquad
p_k(A)=\sum_{j=1}^n a_j^k.
\tag{1}
\]

For finite Blaschke products this is, up to complex conjugation, exactly the first `n` positive Fourier coefficients of the phase derivative in AF-167. Put

\[
\delta(A,B)=\max_{1\le k\le n}|p_k(A)-p_k(B)|
\tag{2}
\]

and use the bottleneck matching distance on unordered divisors,

\[
d(A,B)=\min_{\sigma\in S_n}\max_j |a_j-b_{\sigma(j)}|.
\tag{3}
\]

Then:

1. **Global recovery is `1/n`-Hölder.** There is a constant `C_n<\infty`, depending only on `n`, such that for all degree-`n` divisors in the closed unit disk,

\[
\boxed{
 d(A,B)\le C_n\,\delta(A,B)^{1/n}.
}
\tag{4}
\]

2. **The global exponent is sharp.** No estimate

\[
d(A,B)\le C\,\delta(A,B)^\alpha
\tag{5}
\]

with a uniform finite `C` can hold on the full degree-`n` class for any `\alpha>1/n`.

3. **Multiplicity gives the optimal local exponent.** If `A` has maximum root multiplicity `m`, then in a sufficiently small neighborhood of `A` there is a constant `C_A` such that

\[
\boxed{
 d(A,B)\le C_A\,\delta(A,B)^{1/m}.
}
\tag{6}
\]

For an interior divisor containing an `m`-fold root, this exponent cannot in general be improved beyond `1/m`.

4. **Simple divisors are locally Lipschitz.** If all roots of `A` are distinct, then after local labeling the Jacobian of the moment map is

\[
J_{k j}=k a_j^{k-1},
\]

with determinant

\[
\boxed{
\det J
=n!\prod_{1\le i<j\le n}(a_j-a_i).
}
\tag{7}
\]

Hence the moment map is locally invertible with a locally Lipschitz, indeed analytic after labeling, inverse exactly away from the collision locus. The Vandermonde factor identifies root collision as the intrinsic singular set for these coordinates.

Thus AF-167's finite exact recovery profile has a sharp quantitative refinement: the first `n` phase-gradient moments retain the full divisor, but the retained representation becomes progressively ill-conditioned near multiple or nearly colliding zeros. Exact fidelity alone is therefore insufficient for an asymptotic arithmetic application unless the relevant multiplicity/separation geometry is also controlled.

## Derivation

### Newton reconstruction is Lipschitz on the bounded moment domain

Newton--Girard identities express the elementary symmetric coefficients `e_k` of

\[
Q_A(z)=\prod_{j=1}^n(z-a_j)
=z^n-e_1z^{n-1}+\cdots+(-1)^n e_n
\tag{8}
\]

as triangular polynomials in `p_1,\ldots,p_k`. Since `|a_j|\le1`, every moment satisfies `|p_k|\le n`. On the compact moment box containing all such divisors, the polynomial map

\[
(p_1,\ldots,p_n)\mapsto(e_1,\ldots,e_n)
\tag{9}
\]

is Lipschitz. Therefore there is `K_n<\infty` such that

\[
\max_k |e_k(A)-e_k(B)|
\le K_n\,\delta(A,B).
\tag{10}
\]

Classical polynomial-root perturbation bounds of Ostrowski type imply that the roots of two monic degree-`n` polynomials with bounded coefficients can be matched with displacement bounded by a constant times the `1/n` power of the coefficient perturbation. Combining that bound with `(10)` gives `(4)`.

This establishes a genuine recovery modulus, not merely continuity: the finite phase-moment mark is stable on each fixed-degree class, but only with the worst-case exponent `1/n`.

### Root-of-unity splitting makes the global exponent sharp

Let

\[
A_0=\{0,\ldots,0\}
\]

and, for `0<\varepsilon<1`, let

\[
A_\varepsilon
=\{\varepsilon,\varepsilon\omega,\ldots,
\varepsilon\omega^{n-1}\},
\qquad
\omega=e^{2\pi i/n}.
\tag{11}
\]

Then for `1\le k<n`, root-of-unity cancellation gives

\[
p_k(A_\varepsilon)=0=p_k(A_0),
\tag{12}
\]

while

\[
p_n(A_\varepsilon)=n\varepsilon^n,
\qquad
p_n(A_0)=0.
\tag{13}
\]

Hence

\[
\delta(A_0,A_\varepsilon)=n\varepsilon^n,
\qquad
d(A_0,A_\varepsilon)=\varepsilon.
\tag{14}
\]

If `(5)` held with `\alpha>1/n`, then

\[
\varepsilon
\le C n^\alpha \varepsilon^{n\alpha},
\]

which fails as `\varepsilon\to0`. Thus the exponent `1/n` cannot be improved uniformly on the full degree-`n` divisor class.

### The same control localizes the obstruction to multiplicity

Suppose `A` contains a root `a` of multiplicity exactly `m`. For sufficiently small `\varepsilon`, replace only that cluster by

\[
a+\varepsilon,
a+\varepsilon\omega_m,\ldots,
 a+\varepsilon\omega_m^{m-1},
\qquad
\omega_m=e^{2\pi i/m},
\tag{15}
\]

and leave all other roots fixed. For every `k`,

\[
\sum_{j=0}^{m-1}(a+\varepsilon\omega_m^j)^k-ma^k
=
\sum_{\ell=1}^{k}
\binom{k}{\ell}a^{k-\ell}\varepsilon^\ell
\sum_{j=0}^{m-1}\omega_m^{j\ell}.
\tag{16}
\]

The inner root-of-unity sum vanishes unless `m\mid\ell`. Therefore all retained moment differences vanish for `k<m`, while at `k=m`,

\[
\Delta p_m=m\varepsilon^m.
\tag{17}
\]

For fixed `n` and `A`, every retained moment difference is `O(\varepsilon^m)`, whereas the divisor matching distance is exactly `\varepsilon` for sufficiently small perturbations. Thus

\[
\delta(A,A_\varepsilon)=\Theta(\varepsilon^m),
\qquad
d(A,A_\varepsilon)=\varepsilon,
\tag{18}
\]

so no local exponent larger than `1/m` can hold in general at an `m`-fold root.

Conversely, classical continuity-of-roots results sharpened by multiplicity state that a root of multiplicity `m` is locally Hölder of order `1/m` as a function of the polynomial coefficients. Since Newton reconstruction `(9)` is locally Lipschitz in the retained moments, this gives `(6)`. Taking the maximum multiplicity handles the unordered divisor as a whole.

### Simple roots recover the ordinary Lipschitz regime

For locally labeled distinct roots, differentiate

\[
p_k=\sum_{j=1}^n a_j^k.
\]

The Jacobian is

\[
J_{kj}=k a_j^{k-1}.
\]

Factoring `k` from row `k` leaves the ordinary Vandermonde matrix, proving `(7)`. Therefore the inverse-function theorem gives a local analytic inverse whenever all roots are distinct.

The determinant formula should not be misread as a complete condition-number estimate: small Vandermonde products certify approach to singularity, but quantitative conditioning depends on the full inverse matrix, not only its determinant. What is exact here is the singular locus and the multiplicity-dependent Hölder barrier.

## Prior art and novelty assessment

The stability ingredients are classical, and no novelty is claimed for root perturbation, Prony/Vandermonde singularities, or multiplicity-dependent Hölder regularity.

- Rajendra Bhatia, Ludwig Elsner, and Gerd Krause, **“Bounds for the variation of the roots of a polynomial and the eigenvalues of a matrix,”** *Linear Algebra and its Applications* 142 (1990), 195--209, DOI `10.1016/0024-3795(90)90267-G`, gives quantitative bounds for matching roots of nearby polynomials from coefficient perturbations.
- David Brink, **“Hölder continuity of roots of complex and p-adic polynomials,”** *Communications in Algebra* 38(5) (2010), 1658--1662, DOI `10.1080/00927870902971320`, proves the multiplicity-refined local statement that a root of multiplicity `m` is locally Hölder of order `1/m` in the coefficients.
- Dmitry Batenkov and Yosef Yomdin, **“Geometry and singularities of the Prony mapping,”** *Journal of Singularities* 10 (2014), 1--25, DOI `10.5427/jsing.2014.10a`, studies collision singularities of moment/Prony inversion and explicitly relates the geometry to Vieta and Vandermonde maps.
- Bernard Beauzamy, **“How the roots of a polynomial vary with its coefficients: a local quantitative result,”** *Canadian Mathematical Bulletin* 42(1) (1999), 3--12, DOI `10.4153/CMB-1999-001-6`, records the classical global `1/n` scale and multiplicity-sensitive local improvement.

The Arithmetic Fidelity contribution is the endpoint-specific assembly with AF-167: the retained phase-gradient moments are not merely an exact minimal lift in a nested Fourier family; their inverse stability has a sharp hierarchy. The full degree-`n` class has worst-case exponent `1/n`, an `m`-fold collision has local exponent `1/m`, and simple divisors recover the Lipschitz regime through the Vandermonde Jacobian. The root-of-unity controls make the exponent loss explicit in exactly the phase-moment coordinates retained by the compression.

## Boundary conditions and falsification checks

- The global estimate is for fixed degree `n`. Its constant `C_n` is not claimed uniform in `n`.
- The divisor metric is the bottleneck matching metric. Other Wasserstein or coefficient metrics require their own constants and may encode different notions of endpoint loss.
- The local `1/m` claim concerns the maximum multiplicity of the reference divisor. It does not assert that every perturbation realizes the worst-case exponent; `(15)--(18)` show only that the exponent cannot be improved uniformly in a neighborhood containing the indicated splitting direction.
- The phase-gradient moments are assumed known as exact complex numbers. Measurement noise in the underlying boundary phase, numerical quadrature, or finite sampling introduces an additional forward-error map not analyzed here.
- Distinct but very close roots are locally in the Lipschitz regime at each fixed divisor, yet the local Lipschitz constant can deteriorate without bound as separation tends to zero. Thus a family of simple divisors can still have no useful uniform Lipschitz modulus.
- Nothing here implies a statement about Riemann-zeta zeros. An arithmetic use must identify an intrinsic finite-divisor or moment model and control how its degree, multiplicities, root separation, and moment error scale in the relevant limit.

## Consequences for the research line

AF-167 closes exact finite-divisor recovery from a sharply truncated phase mark. AF-168 shows why that exact theorem is not enough for a growing or limiting problem. A candidate arithmetic compression that transports only finitely many phase-like moments must now pass two separate gates:

1. **exact gate:** enough moments exist to determine the declared divisor endpoint;
2. **stability gate:** the divisor family has a recovery modulus that remains quantitatively useful as degree grows and roots approach one another.

Multiplicity supplies an exact local obstruction, while the Vandermonde singular locus exposes near-collision as the continuous version of the same failure. Therefore a later RH-facing application cannot cite finite exact recovery alone: it must either prove a separation/multiplicity regime with controlled constants, change the endpoint to one insensitive to individual zero displacement, or retain a stronger witness whose inversion avoids this root-reconstruction bottleneck.