# PC-121 — cyclotomic Toeplitz sections are finite-period quasipolynomials

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` + `PRIOR-ART-REDIRECTION`. The exact cyclotomic finite-section formula and its quasipolynomial consequence are derived below. Heine--Szegő/unitary-group characteristic-polynomial averages, Fisher--Hartwig asymptotics, and general Toeplitz determinant theory are classical. No theorem-level novelty is claimed for those frameworks.

PC-075 showed that the canonical Hardy interior/exterior coupling of the **logarithmic** cyclotomic field has universal Hilbert channels, but it deliberately left nonlinear uses of the full boundary potential outside its scope. A particularly natural nonlinear repair is to exponentiate the intrinsic potential back to the nonnegative boundary weight

\[
w_n(e^{it})=e^{2U_n(e^{it})}=|\Phi_n(e^{it})|^2
\]

and study the finite Toeplitz compression of multiplication by this weight. Toeplitz determinants are genuinely nonlocal finite-section objects and sit next to integrable/Riemann--Hilbert machinery, so this is a stronger test than a scalar evaluation of `U_n`.

For the prime-circle symbol, however, the entire section-size dependence is exactly a finite-period quasipolynomial. Its leading coefficient is only the classical cyclotomic discriminant, and its ordinary generating function is rational with poles at roots of unity. Thus the canonical single-shell Toeplitz/Fisher--Hartwig route does not produce a new zeta divisor, functional equation, spectral parameter, or critical line.

## 1. Intrinsic Toeplitz object

Let

\[
\Phi_n(z)=\prod_{a\in(\mathbb Z/n\mathbb Z)^\times}(z-\alpha_a),
\qquad
\alpha_a=e^{2\pi i a/n},
\qquad
m=\varphi(n).
\]

On the unit circle set

\[
w_n(z)=|\Phi_n(z)|^2.
\]

With normalized Haar measure `dmu(z)=|dz|/(2 pi)`, write

\[
\widehat w_n(k)=\int_{\mathbb T}w_n(z)z^{-k}\,d\mu(z)
\]

and define the `N x N` Toeplitz section

\[
T_N(w_n)=\bigl(\widehat w_n(j-k)\bigr)_{0\le j,k<N},
\qquad
D_{n,N}:=\det T_N(w_n),
\]

with `D_{n,0}=1`.

This construction uses no external scale or spectral parameter. It is the standard Hardy compression of the geometry-forced nonnegative density `exp(2U_n)`.

## 2. Exact Christoffel/CUE kernel formula

The Heine--Szegő integral, equivalently Andréief's identity applied to the monomial Gram matrix, gives

\[
D_{n,N}
=\frac1{N!}\int_{\mathbb T^N}
\prod_{\ell=1}^N w_n(z_\ell)
|\Delta(z_1,\ldots,z_N)|^2
\prod_{\ell=1}^N d\mu(z_\ell).
\]

Because every primitive root lies on `T`,

\[
\prod_{\ell=1}^Nw_n(z_\ell)
|\Delta(z_1,\ldots,z_N)|^2
=
\frac{|\Delta(z_1,\ldots,z_N,\alpha_1,\ldots,\alpha_m)|^2}
{|\Delta(\alpha_1,\ldots,\alpha_m)|^2}.
\]

The remaining integral is exactly the `m`-point determinantal correlation kernel of `N+m` Haar-unitary points. Therefore, with

\[
K_M(z,w)=\sum_{k=0}^{M-1}(z\overline w)^k,
\qquad M=N+m,
\]

one obtains the finite identity

\[
\boxed{
D_{n,N}
=
\frac{
\det\bigl(K_{N+m}(\alpha_a,\alpha_b)\bigr)_{a,b\in U(n)}
}
{|\Delta(\alpha_a:a\in U(n))|^2}.
}
\]

Since `Phi_n` is monic with simple roots,

\[
|\Delta(\alpha_a:a\in U(n))|^2
=|\operatorname{disc}\Phi_n|.
\]

The identity can also be viewed as a product-of-characteristic-polynomials average in the CUE. That surrounding determinant technology is classical; the role here is to specialize it exactly to the primitive root shell.

## 3. Root-of-unity periodicity makes the finite determinant a quasipolynomial

For `a=b`,

\[
K_M(\alpha_a,\alpha_a)=M.
\]

For `a\ne b`, put $q=\alpha_a\overline{\alpha_b}$. Then $q$ is a nontrivial `n`-th root of unity, so if

\[
M=Qn+r,\qquad 0\le r<n,
\]

for some integer $Q\ge0$, the complete `n`-blocks cancel and

\[
K_M(\alpha_a,\alpha_b)
=
\sum_{k=0}^{r-1}(\alpha_a\overline{\alpha_b})^k.
\]

Define the fixed `m x m` matrix `B_{n,r}` by zero diagonal and

\[
(B_{n,r})_{ab}
=
\sum_{k=0}^{r-1}(\alpha_a\overline{\alpha_b})^k,
\qquad a\ne b.
\]

Then the Toeplitz determinant is **exactly**

\[
\boxed{
D_{n,N}
=
\frac{\det\bigl((N+m)I_m+B_{n,r}\bigr)}
{|\operatorname{disc}\Phi_n|},
\qquad
r\equiv N+m\pmod n.
}
\]

For every fixed residue class of `N mod n`, the right-hand side is a polynomial in `N` of degree `m=phi(n)`. Hence

\[
\boxed{
N\longmapsto D_{n,N}
\text{ is an exact quasipolynomial of period dividing }n
\text{ and degree }\varphi(n).
}
\]

Its leading coefficient on every residue class is

\[
\boxed{
D_{n,N}
=
\frac{N^{\varphi(n)}}{|\operatorname{disc}\Phi_n|}
+O_n(N^{\varphi(n)-1}).
}
\]

There is an especially transparent residue class. Whenever `N+m` is divisible by `n`, all off-diagonal geometric sums vanish and

\[
\boxed{
D_{n,N}
=
\frac{(N+\varphi(n))^{\varphi(n)}}{|\operatorname{disc}\Phi_n|}.
}
\]

Thus even an infinite subsequence of exact section determinants contains no hidden spectral complication at all.

## 4. The section-size generating function is rational

A quasipolynomial of period dividing `n` and degree `m` has rational ordinary generating function. Therefore

\[
\mathcal D_n(t):=\sum_{N\ge0}D_{n,N}t^N
\]

satisfies

\[
\boxed{
\mathcal D_n(t)\in\mathbb Q(t),
\qquad
\operatorname{den}(\mathcal D_n)
\mid (1-t^n)^{\varphi(n)+1}
}
\]

after cancellation.

The rationality over `Q` also follows directly because `w_n` is a Laurent polynomial with integer Fourier coefficients, so each `D_{n,N}` is an integer; the root-of-unity formula above provides the finite-period polynomial description.

Consequently the only possible poles of this canonical generating function are roots of unity. There is no nontrivial complex zero/pole divisor comparable to the Riemann zeros, and no distinguished `Re(s)=1/2` or `s <-> 1-s` symmetry is generated by the section variable.

## 5. Exact stress tests

Direct Toeplitz determinants from the Laurent coefficients of `|Phi_n|^2` agree with the kernel formula. For `N=1,2,...`, the first values include

\[
\begin{array}{c|l}
n & D_{n,N}\\ \hline
2 & 2,3,4,5,6,7,\ldots\\
3 & 3,5,8,12,16,21,27,33,\ldots\\
4 & 2,4,6,9,12,16,20,25,\ldots\\
5 & 5,9,16,28,48,80,112,156,\ldots\\
8 & 2,4,8,16,24,36,54,81,\ldots\\
9 & 3,9,27,45,75,125,200,320,\ldots\\
12& 3,9,15,25,40,64,96,144,\ldots
\end{array}
\]

The exact `n <-> 2n` rotation collapse for odd `n` is also visible: `Phi_{2n}(z)=Phi_n(-z)` implies the same Toeplitz determinant sequence, e.g. `n=3` and `6`, or `n=5` and `10`.

A particularly sharp audit hook is the zero-remainder class above. For `n=5`, `m=4`, `|disc Phi_5|=125`; at `N=1,6,...` one has `N+m` divisible by `5`, and the formula gives `5^4/125=5`, `10^4/125=80`, matching the direct determinants.

## 6. Prior-art and novelty audit

The mechanism sits inside classical Toeplitz/random-matrix theory rather than defining a new operator class.

1. Daniel Bump and Alex Gamburd, **On the averages of characteristic polynomials from classical groups**, *Communications in Mathematical Physics* 265 (2006), 227--274, DOI `10.1007/s00220-006-1503-1`, give exact classical-group averages of products and ratios of characteristic polynomials using Weyl/Littlewood identities. The kernel determinant above is an elementary CUE/Christoffel specialization of that same finite-`N` framework.
2. Percy Deift, Alexander Its and Igor Krasovsky, **Asymptotics of Toeplitz, Hankel, and Toeplitz+Hankel determinants with Fisher--Hartwig singularities**, *Annals of Mathematics* 174 (2011), 1243--1299, DOI `10.4007/annals.2011.174.2.12`, prove the general Fisher--Hartwig asymptotics for Toeplitz determinants with root singularities. Here every primitive vertex is a root singularity with exponent `alpha=1`; their leading Fisher--Hartwig law specializes to the same `N^m/|Delta|^2` scale found exactly above.
3. Estelle Basor and Peter J. Forrester, **Formulas for the Evaluation of Toeplitz Determinants with Rational Generating Functions**, *Mathematische Nachrichten* 170 (1994), 5--18, DOI `10.1002/mana.19941700102`, are a direct classical anchor for exact rational/polynomial-symbol Toeplitz evaluations. The cyclotomic symbol is an especially rigid polynomial case because all zeros are roots of unity.

A directed search for cyclotomic Toeplitz determinants, root-of-unity Christoffel modifications, product characteristic-polynomial averages, and Fisher--Hartwig root singularities found the surrounding exact/asymptotic machinery but not this specific `Phi_n` quasipolynomial statement under that wording. That absence is **not** a novelty claim. The durable result for this project is the exact classification of a natural Prime-Circle candidate and the resulting obstruction.

The result also reconnects to earlier line findings rather than opening a new arithmetic source. PC-005 already identified `|disc Phi_n|` as the same-shell Vandermonde/self-energy invariant. The leading Toeplitz asymptotic recovers precisely that classical discriminant. PC-075 studied a different object -- the off-diagonal Hardy/Hankel coupling of `log Phi_n` -- so the present nonlinear Toeplitz compression is not covered by its Hilbert-channel theorem, but it collapses for an independent reason.

## 7. Why this is a decisive negative for the canonical Toeplitz route

Toeplitz determinants are a tempting repair because they are simultaneously nonlinear in the potential, nonlocal in Fourier space, finite-dimensional spectral determinants, and naturally connected to integrable/Riemann--Hilbert methods. For the geometry-forced symbol `exp(2U_n)=|Phi_n|^2`, however, the full answer is already finite root-of-unity algebra:

\[
\boxed{
\text{primitive shell}
\to |\Phi_n|^2
\to \text{Toeplitz finite sections}
\to \text{period-}n\text{ quasipolynomial in }N.
}
\]

There is no section-size mechanism from which a Riemann-zero divisor could emerge. Mellin- or Dirichlet-transforming the quasipolynomial sequence could of course manufacture combinations of zeta/Hurwitz-zeta functions, but that would be another transform imposed after the exact finite-size collapse, not a spectral feature generated by the Toeplitz geometry itself.

This is stronger than merely observing the standard Fisher--Hartwig asymptotic: the **entire finite-`N` sequence** is classified. Oscillatory finite-size corrections do not hide a new divisor; they repeat with finite period and polynomial dependence.

## 8. Boundary of the obstruction

The finding is intentionally limited to the canonical **single-shell scalar symbol** `|Phi_n|^2` and its ordinary Toeplitz sections.

It does not rule out:

- matrix-valued Toeplitz symbols that couple several shells before compression;
- cross-level limits in which `n` itself varies and the root-of-unity period is part of the operator rather than a fixed conductor;
- another nonlinear function of `U_n` forced independently by the geometry;
- a non-integer Fisher--Hartwig exponent if such an exponent is derived from the Prime-Circle construction rather than introduced as a free spectral wrapper;
- the extensive old/new cotangent coupling isolated after PC-047;
- the nonlinear uniformization/monodromy branch rooted in PC-017.

Conversely, taking a fixed shell, replacing the logarithmic field by its canonical positive weight, and interpreting Toeplitz section determinants or their large-`N` Fisher--Hartwig behavior as a new RH mechanism is ruled out.

## 9. Falsification surface

The result can be audited at five exact points.

1. **Heine--Szegő step:** direct expansion of the Toeplitz determinant must equal the stated `N`-fold Vandermonde integral.
2. **Vandermonde insertion:** multiplying by `prod_l |Phi_n(z_l)|^2` must turn the `N`-point Vandermonde into the combined `(N+m)`-point Vandermonde divided by `|Delta(alpha)|^2`.
3. **Kernel determinant:** Andréief/Cauchy--Binet must give `det K_{N+m}(alpha_a,alpha_b)` for the pinned primitive roots.
4. **Root-of-unity cancellation:** every off-diagonal kernel entry must depend only on `(N+m) mod n`, while every diagonal entry is exactly `N+m`.
5. **Direct arithmetic check:** determinants built from the integer Laurent coefficients of `|Phi_n|^2` must match the quasipolynomial formula for sample composite and prime-power levels.

Failure of any one invalidates the conclusion. If all hold, rationality of the section generating function and the finite-period obstruction follow algebraically.

## Research consequence

A canonical nonlinear/nonlocal lift of the cyclotomic boundary potential has now been tested and classified exactly:

\[
\boxed{
D_{n,N}=\det T_N(|\Phi_n|^2)
\text{ carries only cyclotomic-discriminant data plus finite root-of-unity periodic corrections.}
}
\]

The Prime-Circle search should therefore not spend further effort on fixed-shell scalar Toeplitz/Fisher--Hartwig sections of `|Phi_n|^2`. Any viable Toeplitz-like continuation must preserve genuinely cross-level or matrix-valued information before the finite-section determinant is taken.
