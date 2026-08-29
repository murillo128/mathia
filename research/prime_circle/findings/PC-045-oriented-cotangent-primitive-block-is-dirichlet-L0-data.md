# PC-045 — the oriented primitive cotangent block is fixed `L(0)` / Bernoulli mixing

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-REDIRECTION` + `DECISIVE-NEGATIVE` for the natural **single-level oriented/chiral repair** in which the primitive shell is coupled by the intrinsic cotangent/Cauchy kernel. This does not rule out the quite different cross-scale cotangent constructions already known to encode GRH criteria, nor nonlinear/cross-level prime-circle operators.

PC-044 showed that the first genuinely multi-prime primitive compression of the inverse-square chord Laplacian is a finite Dirichlet–Bernoulli coupling matrix at the fixed value `L(-1,eta)`. A natural escape is to retain the orientation that `|z_a-z_b|^{-2}` discards. The canonical circle kernel for that purpose is the periodic Cauchy/Hilbert kernel `cot`, equivalently the oriented ratio of two roots of unity.

For odd squarefree levels the escape also classicalizes completely: in multiplicative-character coordinates every off-diagonal coefficient is an explicit Gauss/Ramanujan factor times the fixed special value `L(0,eta)`. Reflection makes the matrix exactly bipartite between even and odd characters, and its characteristic polynomial is rational by cyclotomic Galois symmetry. No free spectral parameter, completed functional equation, or unexplained critical-line spectrum is generated.

## 1. Intrinsic oriented cotangent operator

Let

\[
z_a=e^{2\pi ia/n},\qquad a\in\mathbb Z/n\mathbb Z.
\]

Define the full oriented cotangent operator by

\[
\boxed{
H_n^{\rm full}(a,b)=
\begin{cases}
i\cot\!\left(\dfrac{\pi(a-b)}n\right),&a\ne b,\\[2mm]
0,&a=b.
\end{cases}}
\]

Since `cot` is real and odd, `H_n^{full}` is Hermitian. The kernel is intrinsic to the oriented root-of-unity configuration because, for `r != 0 mod n`,

\[
\boxed{
i\cot\frac{\pi r}{n}
=\frac{1+\zeta_n^r}{1-\zeta_n^r}.}
\]

Thus it is a cyclotomic Cauchy kernel depending only on the oriented ratio `z_a/z_b`, not on an externally chosen coordinate lift.

Retain only the primitive/new vertices:

\[
U(n)=(\mathbb Z/n\mathbb Z)^\times,
\qquad
\boxed{H_n:=H_n^{\rm full}[U(n),U(n)].}
\]

Unlike the inverse-square kernel of PC-044, this operator remembers chirality: reversing the circle changes its sign.

## 2. The full polygon already has an elementary linear spectrum

Let

\[
f_k(a)=n^{-1/2}e^{2\pi ika/n},\qquad 0\le k<n.
\]

The finite cotangent transform gives

\[
\sum_{r=1}^{n-1}
\cot\frac{\pi r}{n}
 e^{-2\pi i kr/n}
=-i(n-2k),
\qquad 1\le k<n,
\]

while the `k=0` sum vanishes by oddness. Therefore

\[
\boxed{
H_n^{\rm full}f_k=\lambda_k f_k,
\qquad
\lambda_0=0,
\qquad
\lambda_k=n-2k\ (1\le k<n).}
\]

So before the primitive compression the entire oriented operator is just a circulant with a linear additive-Fourier spectrum.

At prime level this already closes the route. Since `U(p)` is the full polygon with one vertex removed, all principal cofactors are equal and, if

\[
P_p(t)=\det(tI-H_p^{\rm full}),
\]

then

\[
\boxed{
\det(tI-H_p)=\frac1pP_p'(t).}
\]

Thus the prime-level pointed spectrum is again derivative data of a completely explicit circulant, exactly as in the general pointed-circulant mechanism of PC-038. The genuinely new test begins at composite primitive subsets.

## 3. Exact compression in multiplicative-character coordinates

Assume now that `n>1` is odd and squarefree. For a character `chi` of `U(n)`, extended by zero to a Dirichlet character modulo `n`, put

\[
e_\chi(a)=\frac{\chi(a)}{\sqrt{\varphi(n)}}
\qquad(a\in U(n)).
\]

Define its additive Fourier transform

\[
G_\chi(k)
:=\sum_{a\in U(n)}\chi(a)e^{2\pi iak/n}.
\]

Compressing the additive spectral resolution from the full polygon gives exactly

\[
\boxed{
\langle e_\chi,H_ne_\psi\rangle
=
\frac1{n\varphi(n)}
\sum_{k=0}^{n-1}
\lambda_k\,G_{\overline\chi}(k)G_\psi(-k).}
\]

Let `chi` be induced by its primitive ancestor `chi*` of conductor `f|n`, and write `q=n/f`. The squarefree CRT factorization used in PC-044 gives

\[
\boxed{
G_\chi(k)
=
\chi^*(q)\tau_f(\chi^*)
\overline{\chi^*(k)}\,c_q(k),}
\]

where `tau_f` is the primitive Gauss sum and `c_q` the Ramanujan sum. Hence the only new analytic ingredient relative to PC-044 is the **linear** weight `lambda_k=n-2k` in place of the quadratic weight `k(n-k)/2`.

## 4. The squarefree off-diagonal coupling is exactly `L(0,eta)`

Take distinct characters `chi != psi`. Let their primitive ancestors have conductors `f,g`, and put

\[
q=\frac nf,
\qquad
r=\frac ng,
\qquad
\ell=\operatorname{lcm}(f,g),
\qquad
t=\frac n\ell.
\]

On modulus `ell` define the nonprincipal quotient character

\[
\eta:=\chi^*\overline{\psi^*},
\]

and set

\[
\delta
:=
\omega(f)+\omega(g)-2\omega(\gcd(f,g)).
\]

As in PC-044, define the explicit Gauss phase

\[
\boxed{
K_{\chi,\psi}
:=
\overline{\chi^*(q)}\,
\psi^*(r)\,
\overline{\psi^*(-1)}\,
\tau_f(\overline{\chi^*})\,
\tau_g(\psi^*).}
\]

On the support of `eta`, squarefreeness gives

\[
c_q(k)c_r(k)=(-1)^\delta c_t(k)^2,
\]

and

\[
c_t(k)^2
=
\prod_{p\mid t}
\left(1+p(p-2)\mathbf 1_{p\mid k}\right).
\]

The decisive weighted identity is now the first Bernoulli moment. For every `d|t`, write `n=dN`. Since `(d,ell)=1` and `N` is a multiple of `ell`, periodicity of the nonprincipal character gives

\[
\sum_{m=1}^{N}\eta(m)=0,
\qquad
\sum_{m=1}^{N}m\eta(m)=-N L(0,\eta),
\]

using the standard generalized-Bernoulli identity

\[
L(0,\eta)=-B_{1,\eta}
=-\frac1\ell\sum_{a=1}^{\ell}a\eta(a).
\]

Therefore

\[
\boxed{
\sum_{\substack{1\le k<n\\d\mid k}}
(n-2k)\eta(k)
=2n\eta(d)L(0,\eta).}
\]

Expanding `c_t(k)^2` over divisors and resumming yields

\[
\boxed{
\sum_{k=0}^{n-1}
\lambda_k\eta(k)c_q(k)c_r(k)
=
2(-1)^\delta nL(0,\eta)
\prod_{p\mid t}
\left(1+p(p-2)\eta(p)\right).}
\]

Substitution into the compressed Fourier formula gives the complete off-diagonal entry:

\[
\boxed{
\langle e_\chi,H_ne_\psi\rangle
=
\frac{2(-1)^\delta K_{\chi,\psi}}{\varphi(n)}
L(0,\eta)
\prod_{p\mid t}
\left(1+p(p-2)\eta(p)\right),
\qquad \chi\ne\psi.}
\]

Thus the first genuinely multi-prime primitive compression does not create a new analytic spectral family. Its complete coefficient algebra is finite Gauss/Ramanujan data times the fixed Dirichlet special value `L(0,eta)`, equivalently a generalized Bernoulli number.

## 5. Chirality becomes exact parity bipartiteness

Let `P` be reflection on the primitive shell,

\[
(Pf)(a)=f(-a).
\]

Because the cotangent kernel is odd,

\[
\boxed{PH_nP^{-1}=-H_n.}
\]

Every multiplicative character is a reflection eigenvector:

\[
Pe_\chi=\chi(-1)e_\chi.
\]

Hence

\[
\boxed{
\chi(-1)\psi(-1)=+1
\Longrightarrow
\langle e_\chi,H_ne_\psi\rangle=0.}
\]

This agrees exactly with the special-value formula: for distinct same-parity characters the quotient `eta` is even and the standard trivial-parity zero gives `L(0,eta)=0`.

For `n>2`, evaluation at `-1` splits the character group equally into even and odd characters, so in parity-ordered coordinates

\[
\boxed{
H_n=
\begin{pmatrix}
0&B_n\\
B_n^*&0
\end{pmatrix}.}
\]

Consequently the spectrum is symmetric under

\[
\boxed{\lambda\longleftrightarrow-\lambda.}
\]

The apparent chiral structure is therefore real, but its matrix coefficients are already the standard `B_1/L(0)` character package rather than a new critical-line symmetry.

## 6. Galois audit and the factor `2`

The matrix entries lie in the cyclotomic field:

\[
H_n(a,b)
=
\frac{1+\zeta_n^{a-b}}{1-\zeta_n^{a-b}}.
\]

For every `u in U(n)`, the Galois automorphism `sigma_u:zeta_n -> zeta_n^u` is implemented on primitive coordinates by the permutation `a -> ua`. Thus

\[
\boxed{\sigma_u(H_n)=P_uH_nP_u^{-1},}
\]

and therefore, for every `n>2`, not only squarefree `n`,

\[
\boxed{\det(xI-H_n)\in\mathbb Q[x].}
\]

So numerical irrationality of characteristic coefficients is a falsification signal, not arithmetic structure.

There is also no new even squarefree branch. For odd `n`, primitive `2n`-th roots are exactly the rotation by `-1` of primitive `n`-th roots:

\[
\zeta_{2n}^{n+2a}=-\zeta_n^a.
\]

The oriented ratio/difference kernel is invariant under this common rotation, and the relabeling `a -> n+2a` gives

\[
\boxed{H_{2n}\simeq H_n.}
\]

Thus adjoining the prime `2` contributes no new single-level chiral spectrum at all.

## 7. Prior art: cotangent arithmetic is already deeply classical and can even encode GRH in other constructions

The ingredients and the broader cotangent/L-function landscape are not new.

- Kurt Girstmair, *Cotangent power sums and character coordinates*, **Integers 25** (2025), A63, arXiv:2504.08330, explicitly treats `i cot(pi k/n)` as a cyclotomic Galois orbit and explains cotangent character sums through character coordinates, Gauss sums and generalized Bernoulli numbers. This is the closest direct prior-art warning for the `L(0)`/Bernoulli character content used here.
- Matthias Beck and Mary Halloran, *Finite Trigonometric Character Sums Via Discrete Fourier Analysis*, **International Journal of Number Theory 6** (2010), 51–67, DOI `10.1142/S1793042110002806`, place character-weighted cotangent and related finite trigonometric sums in the classical discrete-Fourier/class-number framework.
- Wiktor Ejsmont and Franz Lehner, *The Trace Method for Cotangent Sums*, **Journal of Combinatorial Theory, Series A 177** (2021), 105324, DOI `10.1016/j.jcta.2020.105324`, realize cotangent values as spectra of finite self-adjoint matrices and derive classical cotangent power-sum/zeta consequences. Their matrix is not the primitive-shell compression above, but it is strong neighboring prior art against reading a finite cotangent spectrum as intrinsically new.
- Liwen Gao and Xuejun Guo, *Trigonometric determinants via special values of Dirichlet L-functions*, **Linear and Multilinear Algebra 74:7** (2026), 916–933, DOI `10.1080/03081087.2026.2654025`, derive cotangent/tangent/cosecant/sine determinant formulas from spectral decompositions and Dirichlet `L`-values. Their multiplicative trigonometric matrices are different from the additive-difference compression `H_n`, but they reinforce the same novelty boundary.
- Most importantly, John Lewis and Don Zagier, *Cotangent sums, quantum modular forms, and the generalized Riemann hypothesis*, **Research in the Mathematical Sciences 6** (2019), article 4, DOI `10.1007/s40687-018-0159-8`, prove that an asymptotic determinant property of a different family of matrices built from finite rational cotangent sums is equivalent to GRH for an odd Dirichlet `L`-series. Their mechanism uses a cross-scale Gram/dilation construction and Beurling-type functional analysis; it is **not** the single-level primitive block `H_n`.

This last source is an important boundary on the negative conclusion. One must not infer that “cotangent matrices cannot be RH-relevant.” Some can be, by known theory. The result here is narrower: the most intrinsic **single-level oriented pair kernel on the primitive root shell** has no unexplained analytic parameter after exact harmonic decomposition.

Directed searches for a principal compression of the additive-difference matrix `i cot(pi(a-b)/n)` to the reduced residues, followed by its full multiplicative-character matrix, did not locate the exact displayed squarefree coefficient formula. That absence is not evidence of historical priority, and no novelty claim is made for the finite Fourier, Gauss, Ramanujan, generalized-Bernoulli, or cotangent-character ingredients.

## 8. Research consequence

The natural route

\[
\boxed{
\text{oriented primitive-root geometry}
\to
\text{cotangent/Cauchy/Hilbert pair kernel}
\to
\text{single-level chiral spectrum}
\to
\text{new RH mechanism}
}
\]

is closed under the hypotheses above. At primes it is a derivative spectrum of an elementary circulant; at odd squarefree composite levels its complete character-basis coefficient algebra is fixed `L(0)` / generalized-Bernoulli data; adjoining `2` does not change the primitive block.

The result does **not** close:

- cross-level cotangent Gram/dilation constructions of the Lewis–Zagier type;
- an operator coupling several birth levels simultaneously before any character decomposition;
- nonlinear functionals of several primitive blocks whose composition is not reconstructible from their individual coefficient matrices;
- shell-dependent kernels carrying an independently derived continuous parameter;
- the primitive-only composite uniformization/monodromy defect of PC-017.

A viable oriented prime-circle route must therefore obtain its extra structure **before** the single-level cotangent block is diagonalized/compressed; changing from an unoriented chord kernel to this canonical chiral kernel alone is not enough.

## 9. Exact audit and falsification tests

The claim is finite-dimensional and directly checkable:

1. diagonalize `H_n^{full}` by additive Fourier modes and verify `lambda_0=0`, `lambda_k=n-2k`;
2. compress the additive spectral resolution to `U(n)` and recover the displayed `G_bar{chi}(k)G_psi(-k)` formula;
3. for squarefree `n`, insert the CRT Gauss–Ramanujan transform from PC-044;
4. for each `d|t`, verify the exact first-moment identity `sum_{d|k}(n-2k)eta(k)=2n eta(d)L(0,eta)`;
5. expand `c_t(k)^2` and recover the Euler product in the off-diagonal coefficient;
6. verify directly that reflection anticommutes with `H_n`, forcing the even/odd bipartite form;
7. apply every `sigma_u` and check conjugacy by `a -> ua`, forcing a rational characteristic polynomial;
8. for odd `n`, relabel primitive `2n`-th roots by `a -> n+2a` and verify exact unitary/permutation equivalence `H_{2n} ~= H_n`.

Failure of the linear full spectrum, the squarefree `L(0)` reduction, or the reflection/Galois symmetries would invalidate the classification. No claim is made that all cotangent-derived matrices are RH-blind, that the displayed finite mixing has a closed eigenvalue formula at every composite level, or that the cross-level/nonlinear boundaries above are exhausted.