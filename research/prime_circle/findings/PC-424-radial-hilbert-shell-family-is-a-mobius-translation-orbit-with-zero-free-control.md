# PC-424 — radial Hilbert shell family is a Möbius translation orbit with a zero-free selector-matched control

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE for the finite noncommutative-word escape left by PC-423 when the arithmetic is supposed to come from primitive-shell Möbius extraction, log-scale translation covariance, Mangoldt support, or prime-power positivity. The whole PC-421 primitive-shell commutator family is an invertible Möbius re-basing of relative translation-conjugates of one regularized Bose seed. An explicit noncyclotomic control has the same shell selectors and the same finite incidence/translation architecture while its Mellin transforms are zero-free throughout the open critical strip.

This does not rule out a genuinely seed-sensitive invariant of the actual Bose commutator, shell-dependent domains/kernels, angular or old-new coupling, or an infinite divisor-family limit in which the finite basis equivalence fails to extend.

## 1. A regularized Bose seed on the critical strip

PC-179 gives

\[
\rho_n(x)=-\sum_{d\mid n}\mu(n/d)\frac{d}{e^{dx}-1}.
\]

Set

\[
r(x):=\frac1{e^x-1}-\frac1x.
\]

Since \(\sum_{d\mid n}\mu(n/d)=0\) for \(n>1\),

\[
\boxed{\rho_n(x)=-\sum_{d\mid n}\mu(n/d)d\,r(dx).}
\tag{1}
\]

The endpoint expansions are

\[
r(x)=-\frac12+\frac{x}{12}+O(x^3),\qquad
r(x)=-\frac1x+O(e^{-x}).
\tag{2}
\]

For \(0<\Re s<1\),

\[
\boxed{\int_0^\infty r(x)x^{s-1}\,dx=\Gamma(s)\zeta(s).}
\tag{3}
\]

One obtains (3) directly from the standard continued Bose Mellin integral by splitting at \(1\): subtract \(1/x\) on \((0,1)\), retain the continuation term \(1/(s-1)\), and use
\(\int_1^\infty x^{s-2}dx=-1/(s-1)\)
to subtract the same \(1/x\) on \((1,\infty)\).

For \(0<\sigma<1\), define

\[
b_\sigma(u)=e^{\sigma u}r(e^u).
\]

Equation (2) gives \(b_\sigma\in H^1(\mathbb R)\cap C_0(\mathbb R)\), and with the PC-421 Fourier normalization

\[
\boxed{\widehat b_\sigma(t)=(2\pi)^{-1/2}\Gamma(\sigma-it)\zeta(\sigma-it).}
\tag{4}
\]

Thus the seed already contains the classical Gamma-zeta Mellin carrier.

## 2. Primitive commutators are an operator-valued Möbius basis

Let \(H\) be the real-line Hilbert transform and

\[
B_\sigma=[H,M_{b_\sigma}].
\]

By the same commutator criterion/norm identity used in PC-421, \(B_\sigma\) is Hilbert--Schmidt. Let
\((\tau_a f)(u)=f(u+a)\)
and define

\[
B_{d,\sigma}
=
d^{1-\sigma}\tau_{\log d}B_\sigma\tau_{-\log d}.
\tag{5}
\]

Because \(H\) commutes with translations,

\[
B_{d,\sigma}
=
[H,M_{d^{1-\sigma}b_\sigma(\cdot+\log d)}],
\]

and
\(d^{1-\sigma}b_\sigma(u+\log d)=d e^{\sigma u}r(de^u)\).
Therefore, with the PC-421 shell operator
\(C_{n,\sigma}=[H,M_{e^{\sigma u}\rho_n(e^u)}]\),

\[
\boxed{C_{n,\sigma}=-\sum_{d\mid n}\mu(n/d)B_{d,\sigma}.}
\tag{6}
\]

Put \(E_{d,\sigma}=B_{d,\sigma}-B_{1,\sigma}\) for \(d>1\). The vanishing Möbius sum removes the \(d=1\) coordinate:

\[
\boxed{
C_{n,\sigma}
=
-\sum_{\substack{d\mid n\\d>1}}\mu(n/d)E_{d,\sigma}.
}
\tag{7}
\]

Let \(D\) be a finite nontrivial-divisor-closed shell set and
\(M_D(n,d)=\mu(n/d)\mathbf1_{d\mid n}\).
Ordered increasingly, \(M_D\) is unit lower triangular, so \(\det M_D=1\). Hence

\[
\boxed{C_D=-M_DE_D}
\tag{8}
\]

is an invertible operator-valued basis change. In particular,

\[
\boxed{
\operatorname{Alg}\{C_{n,\sigma}:n\in D\}
=
\operatorname{Alg}\{E_{d,\sigma}:d\in D\},
}
\tag{9}
\]

and the same holds for their unital norm-closed or C*-algebras.

For every fixed multilinear functional \(F\),

\[
F(C_{n_1,\sigma},\ldots,C_{n_k,\sigma})
=
(-1)^k
\sum_{\substack{d_j\mid n_j\\d_j>1}}
\left(\prod_j\mu(n_j/d_j)\right)
F(E_{d_1,\sigma},\ldots,E_{d_k,\sigma}).
\tag{10}
\]

Thus products, commutators, iterated commutators, and trace tensors of any fixed finite degree transform by the tensor power of the same invertible incidence matrix. PC-423 is the bilinear trace/Gram shadow of (8)--(10). Moving multiplication before trace can retain more seed information, but it cannot make primitive Möbius extraction itself into a new carrier.

## 3. A zero-free control preserving the shell selectors

Define

\[
\boxed{
r_0(x)
=
-\frac{1-e^{-x}}x+\frac12e^{-x}.
}
\tag{11}
\]

It has the same load-bearing endpoint terms,

\[
r_0(x)=-\frac12+\frac{x^2}{12}+O(x^3),
\qquad
r_0(x)=-\frac1x+O(e^{-x}).
\tag{12}
\]

For \(0<\Re s<1\), integration by parts gives

\[
\int_0^\infty(1-e^{-x})x^{s-2}dx=\frac{\Gamma(s)}{1-s},
\]

hence

\[
\boxed{
Z_0(s):=\int_0^\infty r_0(x)x^{s-1}dx
=
-\frac{1+s}{2(1-s)}\Gamma(s).
}
\tag{13}
\]

This has no zeros in the open critical strip and has a simple pole at \(s=1\) with residue \(1\), just like \(\Gamma(s)\zeta(s)\).

Assemble shells by the same primitive rule,

\[
\widetilde\rho_n(x)
=
-\sum_{d\mid n}\mu(n/d)d\,r_0(dx).
\tag{14}
\]

Then

\[
\boxed{
\widetilde{\mathcal R}_n(s)
=
\frac{1+s}{2(1-s)}\Gamma(s)
A_n(s),
\quad
A_n(s)=n^{1-s}\prod_{p\mid n}(1-p^{s-1}).
}
\tag{15}
\]

For \(0<\Re s<1\), every factor in (15) is nonzero, so

\[
\boxed{\widetilde{\mathcal R}_n(s)\ne0\quad(0<\Re s<1).}
\tag{16}
\]

Nevertheless the control keeps the exact source-side selectors. From (12),

\[
\boxed{\widetilde\rho_n(0+)=\frac{\varphi(n)}2.}
\tag{17}
\]

From the pole-zero cancellation at \(s=1\),

\[
\boxed{\int_0^\infty\widetilde\rho_n(x)\,dx=\Lambda(n).}
\tag{18}
\]

Prime powers are again exactly the pointwise-positive shells. Put

\[
f_0(x)=-r_0(x)=\frac{1-e^{-x}}x-\frac12e^{-x}.
\]

For \(n=p^a\) and \(y=p^{a-1}x\),

\[
\widetilde\rho_{p^a}(x)
=
p^{a-1}\bigl[p f_0(py)-f_0(y)\bigr],
\]

with

\[
p f_0(py)-f_0(y)
=
\frac{e^{-y}(1+y/2)-e^{-py}(1+py/2)}{y}.
\tag{19}
\]

Since \(g(y)=e^{-y}(1+y/2)\) satisfies
\(g'(y)=-(1+y)e^{-y}/2<0\),
(19) is strictly positive. If \(n\) is not a prime power, (18) is zero while (17) is positive and the profile is nonzero, so it must change sign. Therefore

\[
\boxed{
\widetilde\rho_n(x)>0\ \forall x>0
\iff
n\text{ is a prime power}.
}
\tag{20}
\]

The control hence has the common-anchor value, exact Mangoldt total flux, and strict prime-power positivity, but no critical-strip Mellin zeros.

## 4. The same finite Hilbert incidence architecture survives in the control

Define
\(\widetilde b_\sigma(u)=e^{\sigma u}r_0(e^u)\)
and
\(\widetilde B_\sigma=[H,M_{\widetilde b_\sigma}]\).
By (12), \(\widetilde b_\sigma\in H^1\cap C_0\) for \(0<\sigma<1\). Repeating (5)--(8) gives

\[
\boxed{
\widetilde C_D=-M_D\widetilde E_D,
\qquad
\operatorname{Alg}(\widetilde C_D)
=
\operatorname{Alg}(\widetilde E_D).
}
\tag{21}
\]

Thus every structural statement that uses only finite Möbius incidence, the common log-scale translation action, the anchor value, Mangoldt total flux, or prime-power positivity survives after the zeta zero set is removed. Concrete seed-dependent spectra need not agree; that is exactly the remaining place where a viable mechanism would have to live.

## 5. Prior-art and novelty audit

The analytic ingredients are classical. NIST DLMF §25.5 is an authoritative source for the Bose Mellin representation of \(\Gamma(s)\zeta(s)\) and its analytic continuation by subtraction of singular terms. Hilbert-transform/singular-integral commutators and their Schatten/Besov classification are classical; Janson--Wolff is a standard source for that framework. Möbius incidence on divisor-closed sets is elementary and already appears line-locally in PC-027 and PC-423.

No novelty is claimed for those ingredients, for the Gamma calculation (13), or for the monotonicity in (19). The line-local contribution is the exact scope classification: the PC-421 shell family is an operator-valued Möbius basis of one regularized translation orbit, and the strongest elementary shell selectors survive in an explicit zero-free matched family.

Directed searches for regularized Bose Mellin kernels, zeta/Hilbert commutators, and Möbius/dilation operator constructions found the expected classical Mellin, commutator, and dilation frameworks, not a new theorem forcing a zeta interpretation of (8)--(21).

## 6. Consequence and falsification boundary

This closes the finite-family route

\[
\boxed{
\text{PC-421 primitive Hilbert commutators}
\to
\text{fixed finite noncommutative words}
\to
\text{primitive incidence/selectors}
\to
\text{new RH mechanism}.
}
\tag{22}
\]

A surviving route must instead produce a seed-sensitive finite invariant that fails the control (11)--(21), a shell-dependent domain/kernel, angular or old-new data coupled before radial scalarization, or an infinite/renormalized divisor-family limit in which the finite unitriangular equivalence does not extend boundedly.

The result is falsified by any failure of (1), (3), (6)--(10), (13), or (17)--(21). In particular, (19) is an elementary exact check of the positivity claim, and (16) is an exact zero-free check from the finite Euler factor. A later genuinely seed-sensitive operator theorem would cross the stated boundary rather than contradict this finding.