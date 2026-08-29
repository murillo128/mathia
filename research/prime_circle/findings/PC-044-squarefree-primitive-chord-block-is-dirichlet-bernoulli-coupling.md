# PC-044 — the squarefree primitive chord block is a finite Dirichlet–Bernoulli coupling matrix

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-REDIRECTION` + `NEGATIVE` for treating the first genuinely multi-prime single-level case of the grounded inverse-square chord operator as an unexplained new analytic spectrum. The result does **not** give a closed formula for every eigenvalue and therefore is not a no-go for all cross-level or nonlinear uses of these blocks.

PC-033 showed that prime powers are still derivative spectra after Bloch decomposition and isolated squarefree radicals with at least two prime factors as the first deletion patterns not covered by that argument. This finding computes that squarefree frontier in the natural multiplicative-character basis. The matrix is not diagonal, so a genuine finite mixing problem remains; however, every matrix coefficient reduces exactly to primitive Gauss sums, Ramanujan factors, and generalized Bernoulli values `L(-1,eta)`. The raw single-level operator therefore contains no hidden free spectral parameter or unclassified transcendental kernel.

## 1. Squarefree primitive block and additive Fourier spectrum

Let `n>1` be squarefree, let

\[
U(n)=(\mathbb Z/n\mathbb Z)^\times,
\]

and retain the inverse-square chord Laplacian from PC-032/033,

\[
(\mathcal L_n f)_a
=
\sum_{b\ne a}
\frac{f_a-f_b}{|e^{2\pi ia/n}-e^{2\pi ib/n}|^2}.
\]

Its normalized additive Fourier modes have the exact classical eigenvalues

\[
\boxed{\lambda_k=\frac{k(n-k)}2,\qquad 0\le k<n.}
\]

Ground every nonprimitive vertex and retain only the birth vertices:

\[
\boxed{A_n:=\mathcal L_n[U(n),U(n)].}
\]

For a multiplicative character `chi` of `U(n)`, extended by zero to a Dirichlet character modulo `n`, put

\[
e_\chi(a)=\frac{\chi(a)}{\sqrt{\varphi(n)}}
\qquad(a\in U(n)).
\]

These `e_chi` form an orthonormal basis of the primitive-coordinate space.

Define the additive Fourier transform of the extended character by

\[
G_\chi(k)
:=
\sum_{a\in U(n)}\chi(a)e^{2\pi i ka/n}.
\]

Inserting the additive spectral resolution of `mathcal L_n` gives the exact compression formula

\[
\boxed{
\langle e_\chi,A_ne_\psi\rangle
=
\frac1{n\varphi(n)}
\sum_{k=0}^{n-1}
\lambda_k\,G_{\overline\chi}(k)G_\psi(-k).
}
\]

Thus the entire squarefree problem is the interaction between additive Fourier modes of the regular polygon and multiplicative characters of the reduced residues.

## 2. CRT turns every imprimitive Fourier transform into Gauss × Ramanujan data

Let `chi` be induced by the primitive character `chi*` of conductor `f|n`, and write

\[
q=\frac nf.
\]

Because `n` is squarefree,

\[
(f,q)=1.
\]

The Chinese remainder theorem factors the additive character modulo `n` into its `f` and `q` components. The primitive `f`-component is the ordinary Gauss transform, while the principal `q`-component is a Ramanujan sum. With

\[
\tau_f(\chi^*)
:=
\sum_{a\bmod f}\chi^*(a)e^{2\pi ia/f},
\]

one obtains exactly

\[
\boxed{
G_\chi(k)
=
\chi^*(q)\,\tau_f(\chi^*)\,
\overline{\chi^*(k)}\,c_q(k).
}
\]

Here `chi*` is extended by zero on nonunits modulo `f`, and `c_q` is the classical Ramanujan sum. For `f=1` this reduces to `G_{chi_0}(k)=c_n(k)`.

So the apparent irregularity of the reduced-residue subset has already split into two standard pieces:

\[
\boxed{
\text{primitive conductor}
\to\text{Gauss character phase},
\qquad
\text{missing Euler factors}
\to\text{Ramanujan weight}.
}
\]

## 3. Exact off-diagonal formula: only `L(-1,eta)` remains

Take distinct characters `chi != psi`. Let their primitive ancestors have conductors `f,g`, put

\[
q=\frac nf,
\qquad
r=\frac ng,
\qquad
\ell=\operatorname{lcm}(f,g),
\qquad
t=\frac n\ell,
\]

and define the quotient character on modulus `ell`

\[
\eta:=\chi^*\overline{\psi^*}.
\]

Because `chi != psi`, `eta` is nonprincipal. Let

\[
\delta
:=
\omega(f)+\omega(g)-2\omega(\gcd(f,g)),
\]

so `delta` counts the primes lying in exactly one of the two conductors. Finally set

\[
\boxed{
K_{\chi,\psi}
:=
\overline{\chi^*(q)}\,
\psi^*(r)\,
\overline{\psi^*(-1)}\,
\tau_f(\overline{\chi^*})\,
\tau_g(\psi^*).
}
\]

On the support of `eta`, each prime in the conductor symmetric difference contributes a fixed Ramanujan factor `-1`, while primes in `t` occur in both complementary Ramanujan sums. Since `t` is squarefree,

\[
c_t(k)^2
=
\prod_{p\mid t}
\left(1+p(p-2)\,\mathbf 1_{p\mid k}\right).
\]

Hence

\[
c_q(k)c_r(k)
=
(-1)^\delta c_t(k)^2
\qquad\text{whenever }\eta(k)\ne0.
\]

The remaining weighted quadratic sum has a particularly simple exact evaluation. For every `d|t`, periodicity modulo `ell` and the generalized Bernoulli identity give

\[
\boxed{
\sum_{\substack{1\le k<n\\d\mid k}}
\lambda_k\eta(k)
=
dn\,\eta(d)L(-1,\eta).
}
\]

One direct verification is to write `k=dm`, set `N=n/d`, split the `N` terms into complete periods modulo `ell`, and use

\[
L(-1,\eta)=-\frac12 B_{2,\eta}.
\]

Expanding `c_t(k)^2` over divisors and resumming multiplicatively therefore yields

\[
\boxed{
\sum_{k=0}^{n-1}
\lambda_k\eta(k)c_q(k)c_r(k)
=
(-1)^\delta nL(-1,\eta)
\prod_{p\mid t}
\left(1+p^2(p-2)\eta(p)\right).
}
\]

Substitution into the compressed Fourier formula gives the complete off-diagonal entry:

\[
\boxed{
\langle e_\chi,A_ne_\psi\rangle
=
\frac{(-1)^\delta K_{\chi,\psi}}{\varphi(n)}
L(-1,\eta)
\prod_{p\mid t}
\left(1+p^2(p-2)\eta(p)\right),
\qquad \chi\ne\psi.
}
\]

Thus every nontrivial coupling is an algebraic special value at the **fixed negative integer `-1`**, multiplied by explicit local conductor factors. No variable `s` is generated by the squarefree deletion pattern.

A useful immediate selection rule is

\[
\boxed{
\eta(-1)=-1
\Longrightarrow
L(-1,\eta)=0
\Longrightarrow
\langle e_\chi,A_ne_\psi\rangle=0.
}
\]

So the operator is exactly block diagonal under even/odd multiplicative parity. This is also forced geometrically by the half-turn symmetry `a -> -a` of the chord kernel.

## 4. The diagonal depends only on the conductor

When `chi=psi`, let `f` be its conductor and put `q=n/f`. The Gauss factors simplify using

\[
\tau_f(\chi^*)\tau_f(\overline{\chi^*})
=\chi^*(-1)f.
\]

The remaining principal-character sums are elementary reduced-residue moments. After the same squarefree divisor expansion one obtains

\[
\boxed{
\langle e_\chi,A_ne_\chi\rangle
=
\frac{n^2}{12}
-
\frac{f\mu(f)}{12\varphi(q)}
\prod_{p\mid q}
\left(1+p^2(p-2)\right).
}
\]

This includes the principal character (`f=1`). In particular the diagonal knows only the conductor, not which primitive character of that conductor was chosen.

For the first odd two-prime example `n=15`, the four possible conductor classes give the exact diagonal values

\[
\boxed{
D_1=\frac{65}{6},
\qquad
D_3=\frac{47}{2},
\qquad
D_5=\frac{125}{6},
\qquad
D_{15}=\frac{35}{2}.
}
\]

Direct construction of the `8 x 8` primitive block reproduces these values; all remaining entries are given by the off-diagonal `L(-1,eta)` formula above.

## 5. Galois audit: the characteristic polynomial is rational

There is an independent exact control which does not use characters. The entries of `A_n` lie in the maximal real cyclotomic field. For every `u in U(n)`, the Galois automorphism

\[
\sigma_u:\zeta_n\mapsto\zeta_n^u
\]

sends the chord weight between `a,b` to the chord weight between `ua,ub`. Multiplication by `u` permutes `U(n)`, hence

\[
\boxed{
\sigma_u(A_n)=P_uA_nP_u^{-1}
}
\]

for a permutation matrix `P_u`. Therefore

\[
\boxed{
\det(xI-A_n)\in\mathbb Q[x].
}
\]

This rationality in fact holds for every `n`, not only squarefree `n`. It is a useful falsification check on any numerical experiment: irrational-looking coefficients of the characteristic polynomial are numerical error, even though individual eigenvalues can lie in nontrivial algebraic extensions.

## 6. Research consequence: the squarefree frontier is real, but it is finite classical mixing

PC-033 was correct that squarefree radicals with at least two primes are the first place where the derivative-of-one-cofactor argument stops. The present calculation shows what replaces it.

The primitive block is **not** a multiplicative convolution and therefore is not diagonalized by Dirichlet characters. Genuine mixing remains. But that mixing is completely finite and its natural matrix coordinates are already

\[
\boxed{
\text{Gauss sums}
\;\times\;
L(-1,\text{quotient character})
\;\times\;
\text{explicit Ramanujan/conductor factors}.
}
\]

The `L(-1,eta)` values are generalized Bernoulli numbers: algebraic special values with no free analytic parameter. Their parity zeros are the standard trivial parity zeros. Consequently the route

\[
\boxed{
\text{squarefree primitive deletion}
\to
1/\text{chord}^2\text{ single-level matrix}
\to
\text{an unexplained new zeta/critical-line spectrum}
}
\]

is strongly classicalized. Merely observing a complicated eigenvalue pattern for `A_{pq}` is not evidence of a new RH mechanism; it is the eigenvalue problem of an explicitly known finite Dirichlet–Bernoulli coupling matrix.

This is intentionally **not** a claim that the whole squarefree branch is dead. The formulas do not provide a closed expression for all eigenvalues or prove that their variation across `n` has no interesting asymptotics. A surviving mechanism would have to use something beyond the raw single-level coefficient algebra, for example:

- a cross-level operation whose composition is not reconstructible from the individual matrices;
- a nonlinear invariant of several squarefree levels with a control showing it is not generic finite character mixing;
- a canonical limiting operator obtained from the family before introducing a Mellin/Dirichlet transform;
- or the global primitive-only uniformization/monodromy defect of PC-017.

## 7. Prior-art and novelty audit

The analytic ingredients are classical and already anchored in `research/prime_circle/SOURCES.md`:

- Calogero–Perelomov supplies the `csc^2` regular-polygon spectrum `lambda_k=k(n-k)/2` used in PC-032;
- primitive Dirichlet characters have the standard finite Fourier/Gauss transform, while a principal complementary modulus contributes the classical Ramanujan sum;
- generalized Bernoulli numbers satisfy `L(1-m,chi)=-B_{m,chi}/m`; Szmidt–Urbanowicz–Zagier is the existing source anchor for the `m=2` specialization used here;
- conductor decomposition, CRT, character parity, and Ramanujan divisor formulas are standard finite harmonic analysis.

Directed searches for reduced-residue principal blocks of the `csc^2` matrix, cosecant-squared matrices combined with Dirichlet characters, and conductor/Ramanujan decompositions did not locate this exact compressed-matrix formula. That absence is not evidence of historical priority. No novelty claim is made for the Gauss, Ramanujan, or generalized-Bernoulli identities themselves.

The durable prime-circle contribution is the **classification of the first unresolved multi-prime deletion pattern**: once expressed in the basis forced by the multiplicative labels of primitive vertices, its complete coefficient algebra is finite classical Dirichlet data rather than a new analytic zeta family.

## 8. Exact falsification tests

The result is finite-dimensional and can be checked without fitting:

1. verify the compressed additive-Fourier formula for `A_n` from the full circulant spectral resolution;
2. use CRT at squarefree `n=fq` to check `G_chi(k)=chi*(q) tau_f(chi*) conjugate(chi*(k)) c_q(k)`;
3. for distinct `chi,psi`, check the prime-by-prime reduction `c_q(k)c_r(k)=(-1)^delta c_t(k)^2` on the support of `eta`;
4. expand `c_t(k)^2` and verify `sum_{d|k} lambda_k eta(k)=dn eta(d)L(-1,eta)` for each `d|t`;
5. recover the displayed off-diagonal Euler product;
6. evaluate the principal periodic moments to recover the conductor-only diagonal formula;
7. for `n=15`, verify the four exact diagonal values above;
8. apply every cyclotomic Galois automorphism `zeta_n -> zeta_n^u` and check conjugacy by the permutation `a -> ua`, forcing a rational characteristic polynomial.

Failure of the CRT Gauss–Ramanujan factorization, the weighted `L(-1)` identity, or the diagonal formula would invalidate the main classification. No claim is made that the eigenvalues themselves have a closed formula, that this package is historically new, or that it settles any part of RH.