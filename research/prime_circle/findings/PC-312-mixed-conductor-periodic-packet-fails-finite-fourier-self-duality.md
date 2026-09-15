# PC-312 — mixed-conductor periodic packet fails finite-Fourier self-duality

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-NEGATIVE` for obtaining a source-native scalar Riemann-type functional equation from the canonical bilinear mixed-conductor Poisson packet of PC-311.

PC-311 proves that the direct bilinear coupling of two centered prime-level Poisson fields produces, after Mellinization, a finite bundle of ordinary Dirichlet `L`-functions in the single variable `u=s+t`. That classification by itself leaves a natural question: although the analytic species is classical, could the **specific periodic coefficient sequence forced by the canonical Prime-Circle prime sources** happen to satisfy the finite-Fourier self-duality that closes such a bundle into a scalar degree-one functional equation?

For the canonical source the answer is exactly no. The periodic coefficient has exact period `N=qr`, but its normalized finite Fourier transform is not proportional to itself. In fact the obstruction is visible at the two nonunit residues `q` and `r`: the original coefficient vanishes there, while its finite Fourier transform is exactly `2/sqrt(N)` at both points. By the classical characterization of periodic Dirichlet series with degree-one functional equation, this rules out a scalar Riemann-type functional equation for the PC-311 mixed packet at its intrinsic product conductor.

The point is not that periodic Dirichlet series cannot satisfy Riemann-type functional equations; many special ones do. The result is source-specific: the actual Prime-Circle coefficient forced by the canonical prime-support source fails the necessary finite-Fourier eigenvector condition.

## 1. Canonical PC-311 coefficient

Let `q,r>3` be distinct primes and put

\[
N:=qr.
\tag{1}
\]

Use the canonical centered prime-support sources from PC-310/PC-311,

\[
f_q(x)=\frac{1}{M_q}\mathbf 1_{P_q}(x)-\frac1q,
\qquad
P_q:=\{\ell:2<\ell<q,\ \ell\text{ prime}\},
\qquad M_q:=|P_q|,
\tag{2}
\]

and analogously `g_r` on `Z/rZ`. Both are real and centered:

\[
\sum_{x\bmod q}f_q(x)=0,
\qquad
\sum_{y\bmod r}g_r(y)=0.
\tag{3}
\]

Use the unnormalized finite Fourier transforms

\[
\widehat f(h)=\sum_{x\bmod q}f_q(x)e^{-2\pi ihx/q},
\qquad
\widehat g(j)=\sum_{y\bmod r}g_r(y)e^{-2\pi ijy/r}.
\tag{4}
\]

PC-311 isolates the positive-frequency mixed coefficient

\[
c(k):=\widehat f(k\bmod q)\,\overline{\widehat g(k\bmod r)}
\tag{5}
\]

and the two-sided Poisson pairing uses the even coefficient

\[
\boxed{
 d(k):=c(k)+c(-k).
}
\tag{6}
\]

Thus `d` is real, even and `N`-periodic. Centering gives

\[
\boxed{
 d(k)=0\qquad\text{whenever }(k,N)>1,
}
\tag{7}
\]

because `q|k` forces `widehat f(0)=0`, while `r|k` forces `widehat g(0)=0`.

The associated one-variable Dirichlet series is

\[
D_d(u):=\sum_{k\ge1}\frac{d(k)}{k^u},
\qquad \Re u>1,
\tag{8}
\]

and PC-311 gives

\[
\mathcal M_2\mathcal B_{q,r}^{f_q,g_r}(s,t)
=\Gamma(s)\Gamma(t)D_d(s+t).
\tag{9}
\]

The question is therefore whether `D_d` itself can acquire the missing scalar degree-one functional equation from the special arithmetic shape of `d`.

## 2. Exact finite Fourier transform returns the original source tensor

Let

\[
\bar r\,r\equiv1\pmod q,
\qquad
\bar q\,q\equiv1\pmod r,
\tag{10}
\]

and use the normalized finite Fourier transform on `Z/NZ`,

\[
(\mathcal F_Nd)(n)
:=\frac1{\sqrt N}\sum_{k\bmod N}d(k)e^{-2\pi ink/N}.
\tag{11}
\]

CRT writes a residue `k mod N` as

\[
k\equiv k_q r\bar r+k_rq\bar q\pmod N.
\tag{12}
\]

Consequently the additive character factors into its `q`- and `r`-parts. Finite Fourier inversion gives

\[
\sum_{h\bmod q}\widehat f(h)e^{-2\pi i ah/q}
=qf_q(-a),
\tag{13}
\]

while, because `g_r` is real,

\[
\sum_{j\bmod r}\overline{\widehat g(j)}e^{-2\pi i bj/r}
=rg_r(b).
\tag{14}
\]

Applying (13)--(14) first to `c(k)` and then to `c(-k)` yields the exact identity

\[
\boxed{
(\mathcal F_Nd)(n)
=\sqrt N\Bigl[
 f_q(-n\bar r\bmod q)g_r(n\bar q\bmod r)
 +f_q(n\bar r\bmod q)g_r(-n\bar q\bmod r)
\Bigr].
}
\tag{15}
\]

Thus finite Fourier duality does not return another opaque mixed packet. It exchanges the Fourier-side product in (5) with the symmetrized CRT tensor of the **original source values**. This is the exact source/frequency duality hidden inside the periodic Dirichlet-series representation of PC-311.

## 3. The canonical prime source violates self-duality at `q` and `r`

For `q>3`, none of `0,1,-1 mod q` belongs to `P_q`: `0` and `1` are not prime and `-1=q-1` is even and greater than `2`. Hence

\[
f_q(0)=f_q(1)=f_q(-1)=-\frac1q,
\tag{16}
\]

and similarly

\[
g_r(0)=g_r(1)=g_r(-1)=-\frac1r.
\tag{17}
\]

Equation (7) immediately gives

\[
\boxed{d(q)=d(r)=0.}
\tag{18}
\]

At `n=q`, however, `q\bar r=0 mod q` and `q\bar q=1 mod r`. Substituting (16)--(17) into (15) gives

\[
\boxed{
(\mathcal F_Nd)(q)
=\sqrt N\left(\frac1{qr}+\frac1{qr}\right)
=\frac{2}{\sqrt N}.
}
\tag{19}
\]

The same calculation with `n=r` gives

\[
\boxed{
(\mathcal F_Nd)(r)=\frac{2}{\sqrt N}.
}
\tag{20}
\]

Therefore

\[
\boxed{
\mathcal F_Nd\notin\mathbb C d.
}
\tag{21}
\]

This is a support-level obstruction, not an asymptotic estimate or numerical test: the source-native packet has zeros at the nonunit product-conductor residues precisely where its Fourier dual has fixed nonzero values.

There is no hidden lower period that could evade the product-conductor conclusion. Equation (15) at `n=0` gives

\[
(\mathcal F_Nd)(0)
=2\sqrt N f_q(0)g_r(0)
=\frac{2}{\sqrt N}\neq0,
\tag{22}
\]

so `d` is not identically zero. Any proper period of an `N=qr` periodic sequence must divide `q` or `r`. If `d` had period `q`, then all values on the multiples of `r` would vanish by (7), while those multiples run through every residue modulo `q`; hence `d` would be identically zero. The same argument excludes period `r`, and period `1` is impossible because `d(0)=0` but `d` is nonzero. Thus

\[
\boxed{\operatorname{per}(d)=qr.}
\tag{23}
\]

## 4. Classical functional-equation criterion makes the obstruction decisive

The general analytic continuation of a periodic-coefficient Dirichlet series is classical: it is a finite linear combination of Hurwitz zeta functions. What is special is closure under a scalar degree-one functional equation.

Ernvall-Hytönen, Odžak and Smajlović prove a necessary-and-sufficient coefficient criterion for an even or odd periodic Dirichlet series to lie in the degree-one extended Selberg class with its periodic conductor. In their normalized convention, the criterion is equivalent to the finite Fourier transform of the coefficient vector being a constant unit-modulus multiple of that vector. For a real even coefficient vector, the only possible scalar Fourier eigenvalues are `+1` or `-1`.

The exact-period statement (23) puts `D_d` at conductor `N=qr` in precisely that setting. But (18)--(20) violate the Fourier-eigenvector condition at once. Therefore

\[
\boxed{
D_d\text{ does not satisfy a source-native scalar degree-one Riemann-type functional equation.}
}
\tag{24}
\]

Equivalently, the standard Hurwitz-zeta functional transformation sends the PC-311 coefficient vector `d` to the genuinely different vector `mathcal F_N d`; it does not close on `d` itself. Individual Dirichlet-`L` components in the PC-311 character expansion of course retain their classical functional equations, but the Prime-Circle source weights do not recombine them into a new scalar self-dual object.

This also sharpens a statement in PC-311. Saying that the bilinear mixed-conductor pairing is a finite Dirichlet-`L` bundle shows that no new analytic species appeared; equations (18)--(24) now prove that the **actual canonical bundle does not accidentally acquire the missing degree-one self-duality either**.

## 5. Prior-art and novelty audit

The general periodic-series mechanism is classical and no novelty is claimed for it.

- Makoto Ishibashi and Shigeru Kanemitsu, **Dirichlet series with periodic coefficients**, *Results in Mathematics* 35 (1999), 70--88, DOI `10.1007/BF03322023`, develops Dirichlet series attached to periodic arithmetic functions in a framework containing ordinary Dirichlet characters and `L`-functions.
- Anne-Maria Ernvall-Hytönen, Almasa Odžak and Lejla Smajlović, **On a class of periodic Dirichlet series with functional equation**, *Mathematical Communications* 25 (2020), 35--47, gives the finite-Fourier coefficient characterization used in Section 4. Their Theorem 1 gives the necessary-and-sufficient relation, and Lemma 1 identifies it with finite-Fourier eigenvector behavior for even/odd coefficient vectors.
- Takashi Nakamura, **Dirichlet Series with Periodic Coefficients, Riemann's Functional Equation, and Real Zeros of Dirichlet L-Functions**, *Mathematica Slovaca* 73:5 (2023), 1145--1152, DOI `10.1515/ms-2023-0084`, constructs special periodic-coefficient combinations that do satisfy Riemann's functional equation. This is an important control: periodicity itself is not the obstruction.

The Mathia-specific contribution is narrower and exact: for the canonical two-prime source generated by the Prime-Circle construction, equation (15) identifies the finite Fourier dual explicitly with the symmetrized source tensor, and the values (18)--(20) give an immediate certificate that the required self-duality fails. This appears to be a project-specific specialization/consequence of classical periodic Dirichlet-series theory, not a new theorem about periodic Dirichlet series in general.

## 6. Boundary and surviving mechanisms

The result closes only the most direct functional-equation repair of PC-311:

\[
\text{canonical two-level Poisson pairing}
\longrightarrow
\text{periodic Dirichlet series }D_d(u)
\longrightarrow
\text{scalar degree-one self-dual functional equation}.
\]

It does **not** rule out a vector- or matrix-valued functional equation retaining both `d` and `mathcal F_Nd`, a source-forced operation that acts on that pair before scalarization, genuinely nonlinear cross-level couplings, or a different intrinsic source whose coefficient vector is Fourier self-dual. Nor does it rule out manually replacing `d` by a Fourier symmetrization such as `d+mathcal F_Nd`; that operation would simply require an independent Prime-Circle reason before it could count as source-native progress.

The critical-line lesson is correspondingly narrow. PC-311's product-conductor mixing is genuine, but the canonical arithmetic weights break the finite-Fourier modularity needed for the classical degree-one scalar functional equation. Any surviving route to a critical-line mechanism must therefore add structure **before** this mixed packet is compressed to one periodic scalar Dirichlet series, or prove an independently forced coupling of the packet with its Fourier dual.

## 7. Falsification hooks

This finding should be revised or withdrawn if any of the following occurs:

1. the coefficient `d` in (6) is not the actual two-sided coefficient entering the canonical PC-311 Poisson pairing;
2. the CRT/Fourier calculation (15) has a sign or normalization error that makes `(mathcal F_N d)(q)` or `(mathcal F_N d)(r)` vanish;
3. the canonical prime source includes one of `0,1,-1` under the conventions of PC-310/PC-311, invalidating (16)--(17);
4. `d` is shown to have a proper period despite the nonunit-vanishing argument in Section 3;
5. the cited periodic-Dirichlet-series criterion does not apply to an even exact-period coefficient vector in the stated degree-one setting;
6. an independently source-forced Prime-Circle operation is proved to couple `d` and `mathcal F_Nd` into a scalar self-dual object, in which case the present result remains a no-go only for `D_d` by itself.

Absent such a failure, the direct attempt to extract the missing Riemann-type scalar functional equation from the canonical PC-311 mixed-conductor periodic packet is closed.