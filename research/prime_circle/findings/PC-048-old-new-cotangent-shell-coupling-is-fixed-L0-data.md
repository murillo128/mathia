# PC-048 — old/new cotangent shell coupling is fixed `L(0)` data

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-REDIRECTION` + `NEGATIVE` for interpreting the raw old/new cotangent carrier at one odd squarefree level as a new analytic or critical-line spectrum. PC-047 proves that this carrier can have maximal rectangular rank. The present result shows that maximal rank does not come from an unexplained analytic kernel: after decomposing the inherited vertices by their exact birth order and using multiplicative characters on both sides, every coefficient is either forced to vanish by parity or is an explicit Gauss/Ramanujan factor times the fixed generalized-Bernoulli value `L(0,eta)`.

This is intentionally narrower than a no-go for nonlinear or cross-level use of the old/new coupling. Singular values of the assembled rectangular matrix need not have a simple closed form, and a Lewis–Zagier-type cross-scale Gram/dilation construction is outside the claim.

## 1. The old sector splits canonically into exact birth shells

Let `n>1` be odd and squarefree and write

\[
U(n)=(\mathbb Z/n\mathbb Z)^\times.
\]

As in PC-045/PC-047, use the intrinsic oriented cotangent kernel on the full regular `n`-gon,

\[
H_n^{\rm full}(a,b)=
\begin{cases}
i\cot\!\left(\dfrac{\pi(a-b)}n\right),&a\ne b,\\[2mm]
0,&a=b.
\end{cases}
\]

The primitive rows are indexed by `U(n)`. Every inherited root has a unique exact order `d|n`, `d<n`. If

\[
m=\frac nd,
\]

then the exact-order `d` roots inside the `n`-gon are indexed by `mc` with `c in U(d)`. Define the primitive-to-order-`d` block

\[
\boxed{
B_{n,d}(a,c)
=i\cot\!\left(\frac{\pi(a-mc)}n\right),
\qquad a\in U(n),\ c\in U(d).
}
\]

For `d=1` this is the single column coupling the primitive shell to the common anchor `1`. With the exact-order decomposition of the old roots,

\[
\boxed{
B_n=\bigl[\,B_{n,d}\,\bigr]_{d\mid n,\ d<n},
}
\]

where `B_n=H_n^{full}[U,O]` is the old/new matrix of PC-047. Thus there is no arbitrary partition: the columns are grouped by the same primitive/birth layers that define prime-circle geometry.

## 2. Additive Fourier resolution converts a shell block into two finite character transforms

For a character `chi` of `U(n)` and a character `psi` of `U(d)`, use normalized vectors

\[
e_\chi(a)=\frac{\chi(a)}{\sqrt{\varphi(n)}},
\qquad
e_\psi(c)=\frac{\psi(c)}{\sqrt{\varphi(d)}}.
\]

For a Dirichlet character `alpha` modulo a squarefree modulus `N`, extended by zero away from the units, put

\[
G_\alpha^{(N)}(k)
=\sum_{a\in U(N)}\alpha(a)e^{2\pi iak/N}.
\]

The full cotangent circulant has additive Fourier eigenvalues

\[
\lambda_0=0,
\qquad
\lambda_k=N-2k\quad(1\le k<N).
\]

Embedding the order-`d` shell into the `n`-gon therefore gives the exact rectangular compression formula

\[
\boxed{
\langle e_\chi,B_{n,d}e_\psi\rangle
=
\frac{1}{n\sqrt{\varphi(n)\varphi(d)}}
\sum_{k=0}^{n-1}
(n-2k)\,
G_{\overline\chi}^{(n)}(k)
G_\psi^{(d)}(-k).
}
\]

Let `chi*` and `psi*` be the primitive ancestors of `chi` and `psi`, of conductors

\[
f\mid n,
\qquad
g\mid d,
\]

and set

\[
q=\frac nf,
\qquad
r=\frac dg.
\]

Squarefreeness gives the same CRT Gauss–Ramanujan factorization used in PC-044/PC-045:

\[
\boxed{
G_\alpha^{(N)}(k)
=\alpha^*(N/f_\alpha)\,
\tau_{f_\alpha}(\alpha^*)\,
\overline{\alpha^*(k)}\,
c_{N/f_\alpha}(k),
}
\]

where `tau` is the primitive Gauss sum and `c_j` the Ramanujan sum. Consequently all nontrivial structure in the shell coupling reduces to one quotient character and the product `c_q(k)c_r(k)`.

## 3. Reflection forces an exact parity selection rule

Let reflection act by `a -> -a` on `U(n)` and `c -> -c` on `U(d)`. Oddness of cotangent gives

\[
\boxed{
R_n B_{n,d}R_d^{-1}=-B_{n,d}.
}
\]

Characters are reflection eigenvectors,

\[
R_ne_\chi=\chi(-1)e_\chi,
\qquad
R_de_\psi=\psi(-1)e_\psi.
\]

Hence

\[
\boxed{
\chi(-1)\psi(-1)=+1
\quad\Longrightarrow\quad
\langle e_\chi,B_{n,d}e_\psi\rangle=0.
}
\]

Only opposite-parity characters can couple. This already shows that the large rank found in PC-047 is assembled from chiral channels rather than arbitrary dense mixing.

For the remaining case define the quotient character on

\[
\ell=\operatorname{lcm}(f,g)
\]

by

\[
\eta=\chi^*\overline{\psi^*}.
\]

Opposite parity implies `eta(-1)=-1`, so `eta` is nonprincipal and the fixed special value `L(0,eta)` is well-defined through the first generalized Bernoulli number.

## 4. The Ramanujan product has only two local factors

Define

\[
f_d=\gcd(f,d)
\]

and the two disjoint prime sets

\[
\mathcal A
=\{p:p\mid d,\ p\nmid fg\},
\]

\[
\mathcal B
=\{p:p\mid n/d,\ p\nmid f\}.
\]

Also put

\[
\delta
=\omega(g)+\omega(f_d)-2\omega(\gcd(f,g)),
\]

which counts the primes in the symmetric difference between `g` and the part of `f` lying in `d`.

On the support of `eta`, the prime-by-prime Ramanujan factors are exact:

- if a prime occurs in exactly one of `q` and `r` while also lying in `ell`, it contributes `-1`;
- for `p in mathcal A`, it occurs in both complementary Ramanujan sums and contributes
  \[
  c_p(k)^2=1+p(p-2)\mathbf 1_{p\mid k};
  \]
- for `p in mathcal B`, it occurs only in `q` and contributes
  \[
  c_p(k)=-1+p\mathbf 1_{p\mid k}.
  \]

Therefore

\[
\boxed{
c_q(k)c_r(k)
=(-1)^\delta
\prod_{p\in\mathcal A}
\left(1+p(p-2)\mathbf1_{p\mid k}\right)
\prod_{p\in\mathcal B}
\left(-1+p\mathbf1_{p\mid k}\right)
}
\]

whenever `eta(k) != 0`.

The only analytic-looking sum that remains is the first Bernoulli moment. If `e` is supported on `mathcal A union mathcal B`, then `(e,ell)=1`, and periodicity of the nonprincipal character gives

\[
\boxed{
\sum_{\substack{1\le k<n\\e\mid k}}
(n-2k)\eta(k)
=2n\eta(e)L(0,\eta).
}
\]

Indeed, writing `k=ej` and `N=n/e`, the constant term vanishes because `sum eta=0`, while

\[
\sum_{j=1}^{N}j\eta(j)=-N L(0,\eta),
\qquad
L(0,\eta)=-B_{1,\eta}.
\]

No analytic continuation or limiting operation is being used here; this is a finite periodic identity.

## 5. Exact shellwise coupling formula

Collect the fixed Gauss/conductor phase

\[
\boxed{
C_{\chi,\psi}^{n,d}
=
\overline{\chi^*(q)}\,
\psi^*(r)\,
\overline{\psi^*(-1)}\,
\tau_f(\overline{\chi^*})\,
\tau_g(\psi^*).
}
\]

Expanding the two finite local products in the previous section and applying the Bernoulli moment term by term yields, for opposite parity,

\[
\boxed{
\begin{aligned}
\langle e_\chi,B_{n,d}e_\psi\rangle
={}&
\frac{2(-1)^\delta C_{\chi,\psi}^{n,d}}
{\sqrt{\varphi(n)\varphi(d)}}
L(0,\eta)\\
&\times
\prod_{p\in\mathcal A}
\left(1+p(p-2)\eta(p)\right)
\prod_{p\in\mathcal B}
\left(p\eta(p)-1\right).
\end{aligned}
}
\]

Together with the same-parity zero rule, this gives **every multiplicative-character coefficient of every exact-order old/new block** for odd squarefree `n`.

The common anchor is included rather than treated separately. For `d=1`, use the trivial one-dimensional character, `g=1`, `tau_1=1`, and `varphi(1)=1`; the formula becomes the ordinary cotangent character coordinate of the anchor profile. Thus the pointed channel and all higher inherited birth shells belong to one fixed `L(0)` package.

## 6. Maximal rank and classical coefficient algebra are compatible

PC-047 established

\[
\operatorname{rank}B_n
=\min(\varphi(n),n-\varphi(n))
\]

away from the balanced power-of-two exception, and in particular full row rank for every even squarefree composite level and for many odd squarefree levels such as `n=105`.

The present result explains why that does **not** imply a new analytic spectrum. A matrix assembled from many algebraic special-value channels can have maximal rank. Here every shellwise channel is built from

\[
\boxed{
\text{Gauss sums}
\;\times\;
L(0,\text{odd quotient character})
\;\times\;
\text{explicit local Ramanujan factors}.
}
\]

There is no free complex parameter `s`, no gamma completion, no intrinsic `s <-> 1-s` symmetry, and no critical-line localization at this stage. The nontriviality found in PC-047 is therefore an **information-capacity statement**, not evidence that the raw rectangular coupling already contains a Hilbert–Pólya-type object.

As finite checks, normalized direct construction gives, with the quadratic character modulo `3` on the primitive rows:

- at `(n,d)=(15,5)` against the quadratic character modulo `5`, the coefficient is `i sqrt(30)/2`;
- at `(n,d)=(105,15)` against the same conductor-`5` character, the extra prime-`7` local factor gives `-2 i sqrt(10)`;
- at `(n,d)=(15,1)` the common-anchor coefficient is `i sqrt(6)`.

These checks exercise respectively the bare Gauss/Bernoulli term, a nontrivial one-sided Ramanujan factor, and the anchor convention.

## 7. Prior-art and novelty audit

The ingredients sit in well-established cotangent/character theory.

- Kurt Girstmair, **Cotangent power sums and character coordinates**, *Integers* 25 (2025), A63, treats `i cot(pi k/n)` as a cyclotomic Galois orbit and organizes cotangent data in Dirichlet-character coordinates, Gauss sums, and generalized Bernoulli numbers.
- Matthias Beck and Mary Halloran, **Finite Trigonometric Character Sums Via Discrete Fourier Analysis**, *International Journal of Number Theory* 6 (2010), 51–67, place character-weighted cotangent and related sums in the classical finite-Fourier/class-number framework.
- Liwen Gao and Xuejun Guo, **Trigonometric determinants via special values of Dirichlet L-functions**, *Linear and Multilinear Algebra* 74:7 (2026), 916–933, give a modern spectral/determinantal treatment of trigonometric matrices through Dirichlet `L`-values and Gauss sums.
- John Lewis and Don Zagier, **Cotangent sums, quantum modular forms, and the generalized Riemann hypothesis**, *Research in the Mathematical Sciences* 6 (2019), Article 4, is the essential boundary: a different cross-scale family of rational-cotangent matrices does encode a GRH criterion through Gram/dilation and Beurling-type structure.

Those sources are already anchored in `research/prime_circle/SOURCES.md`. No novelty claim is made for cotangent character sums, Gauss/Ramanujan factorization, generalized Bernoulli values, or the finite Fourier method. Directed searches did not locate this exact rectangular **primitive-shell to exact-order inherited-shell** formula, but absence of an exact wording match is not evidence of historical priority.

The durable prime-circle contribution is instead the structural classification forced by its birth decomposition: **the full-rank carrier reopened by PC-047 decomposes shell by shell into fixed classical `L(0)` channels.** This materially narrows what any surviving use of `B_n` must exploit.

## 8. Boundaries and exact falsification tests

The result assumes `n` is odd and squarefree. Repeated prime powers require additional local multiplicities, and the even case has its own `n <-> 2n` degeneracies. Neither is silently covered by the displayed formula.

The result also does not claim:

- a closed formula for singular values or eigenvectors of the assembled `B_n`;
- that nonlinear invariants of several blocks reduce to one `L(0)` value;
- that cross-level composition before character decomposition is classicalized;
- that Lewis–Zagier-type dilation/Gram constructions are ruled out;
- or that the global primitive-only uniformization/monodromy direction of PC-017 is affected.

The exact claim can be falsified without asymptotics:

1. decompose the nonprimitive roots into exact-order shells `d|n`, `d<n`, and verify the block formula for `B_{n,d}`;
2. insert the additive Fourier resolution of `H_n^{full}` and check the rectangular coefficient identity;
3. verify the squarefree CRT formula for each finite character transform;
4. check reflection and the same-parity zero rule;
5. inspect each prime of `c_q(k)c_r(k)` and recover the `mathcal A`, `mathcal B`, and `delta` factors;
6. prove the finite Bernoulli moment for every divisor supported on `mathcal A union mathcal B`;
7. expand the local products and recover the boxed `L(0,eta)` coefficient formula;
8. compare with direct exact matrices at small squarefree levels, including the common-anchor case `d=1`.

Failure of the prime-by-prime Ramanujan decomposition, the Bernoulli moment, or any one of these finite matrix comparisons would invalidate the classification. Maximal rank itself remains exactly as in PC-047; what is ruled out here is only the interpretation of the **raw single-level shellwise coefficient algebra** as a new analytic RH mechanism.
