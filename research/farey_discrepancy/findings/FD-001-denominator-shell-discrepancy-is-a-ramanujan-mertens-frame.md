# FD-001 — denominator-shell Farey discrepancy is an exact Ramanujan--Mertens frame

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + MULTISCALE-DECOMPOSITION + RAMANUJAN-FOURIER + MOBIUS-COLLAPSE + STRUCTURAL-BOUNDARY`. The Farey counting discrepancy has a canonical decomposition by exact denominator. Each denominator shell has an explicit Fourier spectrum given by Ramanujan sums, and the complete cross-scale `L^2` Gram matrix is an elementary divisor kernel. Summing shells through order `N` then collapses every Fourier mode to a finite divisor transform of the Mertens function.

This gives the Farey line a precise multiscale object, but also a sharp boundary: **linear harmonic information carried only by exact-denominator counting shells does not create an arithmetic channel independent of familiar Möbius summatory data.** Any genuinely additional Farey-order mechanism must use information not exhausted by these shell coefficients, such as ordered adjacency/refinement relations before they are collapsed to the cumulative counting function, or must prove a quantitatively stronger estimate for the same Möbius-controlled object.

## 1. Exact denominator-shell decomposition

For `q>=2`, let

\[
A_q(x):=\#\left\{1\le a\le q:\ (a,q)=1,\ \frac aq\le x\right\},
\qquad 0\le x\le1,
\]

and define the centered exact-denominator discrepancy

\[
e_q(x):=A_q(x)-\varphi(q)x.
\tag{1}
\]

Using interior Farey fractions avoids endpoint bookkeeping. Put

\[
\mathcal F_N^\circ
:=\left\{\frac aq:1\le a<q\le N,\ (a,q)=1\right\},
\qquad
C_N:=\sum_{q=2}^N\varphi(q),
\]

and

\[
D_N(x)
:=\#\{y\in\mathcal F_N^\circ:y\le x\}-C_Nx.
\tag{2}
\]

Partitioning by the reduced denominator gives the exact identity

\[
\boxed{D_N(x)=\sum_{q=2}^N e_q(x).}
\tag{3}
\]

A denominator-level decomposition of Farey local discrepancy is already explicit in García (2025); (3) is therefore not a novelty claim. The point here is to retain the complete shell family and derive its exact harmonic and Gram structure.

Möbius inversion gives, for every `q>=2`,

\[
A_q(x)
=\sum_{d\mid q}\mu(d)\left\lfloor\frac{qx}{d}\right\rfloor.
\tag{4}
\]

Since

\[
\varphi(q)=\sum_{d\mid q}\mu(d)\frac qd,
\]

we obtain the exact sawtooth expansion

\[
\boxed{
e_q(x)
=\sum_{d\mid q}\mu(d)
\left(\left\lfloor\frac{qx}{d}\right\rfloor-\frac{qx}{d}\right)
=\sum_{m\mid q}\mu(q/m)(\lfloor mx\rfloor-mx).
}
\tag{5}
\]

Thus the denominator-shell decomposition is already a finite Möbius combination of elementary fractional-part waves.

## 2. Each shell has Ramanujan Fourier coefficients

For `q>1`, the reduced residues occur in complementary pairs `a` and `q-a`, so

\[
\sum_{\substack{1\le a\le q\\(a,q)=1}}a
=\frac{q\varphi(q)}2.
\]

Consequently

\[
\int_0^1e_q(x)\,dx=0.
\tag{6}
\]

In the distributional sense,

\[
e_q'
=\sum_{\substack{1\le a\le q\\(a,q)=1}}
\delta_{a/q}-\varphi(q).
\tag{7}
\]

Use the Fourier convention

\[
\widehat f(k)=\int_0^1f(x)e^{-2\pi ikx}\,dx.
\]

For `k ne 0`, the Fourier coefficient of the atomic term in (7) is the classical Ramanujan sum

\[
c_q(k)
:=\sum_{\substack{1\le a\le q\\(a,q)=1}}
 e^{-2\pi i k a/q}.
\tag{8}
\]

Because Ramanujan sums are real and even in `k`, differentiation gives

\[
\boxed{
\widehat e_q(0)=0,
\qquad
\widehat e_q(k)=\frac{c_q(k)}{2\pi i k}\quad(k\ne0).
}
\tag{9}
\]

Ramanujan's 1918 paper is the classical source boundary for `c_q(k)` and its divisor formula

\[
\boxed{
c_q(k)=\sum_{d\mid(q,k)}d\,\mu(q/d).
}
\tag{10}
\]

Equation (9) is therefore an immediate specialization of classical Fourier arithmetic to the Farey denominator shell, not a claim that Ramanujan sums themselves are new.

## 3. The complete cross-scale Gram kernel is explicit

Parseval and (9) give, for `q,r>=2`,

\[
\langle e_q,e_r\rangle_{L^2(0,1)}
=\frac1{2\pi^2}
\sum_{k\ge1}\frac{c_q(k)c_r(k)}{k^2}.
\tag{11}
\]

Insert (10) and interchange the finite divisor sums with the absolutely convergent `k^{-2}` series. The condition `d|k` and `e|k` is equivalent to `lcm(d,e)|k`, so

\[
\begin{aligned}
\sum_{k\ge1}\frac{c_q(k)c_r(k)}{k^2}
&=\zeta(2)
\sum_{d\mid q}\sum_{e\mid r}
\mu(q/d)\mu(r/e)
\frac{de}{\operatorname{lcm}(d,e)^2}\\
&=\zeta(2)
\sum_{d\mid q}\sum_{e\mid r}
\mu(q/d)\mu(r/e)
\frac{\gcd(d,e)^2}{de}.
\end{aligned}
\tag{12}
\]

Since `zeta(2)=pi^2/6`,

\[
\boxed{
\langle e_q,e_r\rangle
=\frac1{12}
\sum_{d\mid q}\sum_{e\mid r}
\mu(q/d)\mu(r/e)
\frac{\gcd(d,e)^2}{de}.
}
\tag{13}
\]

The right-hand side is multiplicative in the pair `(q,r)`. If `a=v_p(q)` and `b=v_p(r)`, its local factor is

\[
G_p(a,b)
=(1+\mathbf1_{a,b\ge1})p^{-|a-b|}
-\mathbf1_{a\ge1}p^{-|a-b-1|}
-\mathbf1_{b\ge1}p^{-|a-b+1|}.
\tag{14}
\]

Useful special cases are

\[
G_p(a,a)=2(1-p^{-1})\qquad(a\ge1),
\tag{15}
\]

\[
G_p(a,0)=-(p-1)p^{-a}\qquad(a\ge1),
\tag{16}
\]

and, for `a>b>=1`,

\[
G_p(a,b)=-(p-1)^2p^{-(a-b+1)}.
\tag{17}
\]

In particular the shell norm is independent of prime-power depth:

\[
\boxed{
\|e_q\|_2^2
=\frac1{12}\prod_{p\mid q}2(1-p^{-1}).
}
\tag{18}
\]

For example `||e_2||_2^2=||e_4||_2^2=1/12`, while cross-shell entries can be negative; (13) gives `\langle e_2,e_4\rangle=-1/48`. There is no contradiction with positivity because the full matrix is a Gram matrix by construction.

Equation (13) is the exact cross-scale covariance object suggested by the Farey mandate: no sampling, asymptotic replacement, or geometric visualization is needed to define it.

## 4. Summing the shells collapses modewise to Mertens

The key arithmetic boundary appears after summing in `q`. From (10),

\[
\begin{aligned}
\sum_{q=1}^N c_q(k)
&=\sum_{q\le N}\sum_{d\mid(q,k)}d\mu(q/d)\\
&=\sum_{\substack{d\mid k\\d\le N}}
 d\sum_{m\le N/d}\mu(m).
\end{aligned}
\]

Writing `M(x)=sum_{m<=x} mu(m)`, this is

\[
\boxed{
\sum_{q=1}^N c_q(k)
=\sum_{\substack{d\mid k\\d\le N}}
 d\,M(\lfloor N/d\rfloor).
}
\tag{19}
\]

The `q=1` shell contributes the endpoint convention; for the interior discrepancy (3),

\[
\boxed{
\widehat D_N(k)
=\frac1{2\pi i k}
\left[
\sum_{\substack{d\mid k\\d\le N}}
 d\,M(\lfloor N/d\rfloor)-1
\right],
\qquad k\ne0.
}
\tag{20}
\]

The first mode is especially transparent:

\[
\boxed{
2\pi i\,\widehat D_N(1)=M(N)-1.
}
\tag{21}
\]

Finally,

\[
\boxed{
\|D_N\|_2^2
=\frac1{2\pi^2}
\sum_{k\ge1}\frac1{k^2}
\left|
\sum_{\substack{d\mid k\\d\le N}}
 d\,M(\lfloor N/d\rfloor)-1
\right|^2.
}
\tag{22}
\]

Thus the complete linear Fourier spectrum of the cumulative denominator-shell counting discrepancy is an exact finite divisor transform of Mertens values. The multiscale shell frame is mathematically real, but at this level its arithmetic content has not escaped the classical Möbius channel.

## 5. Consequence for the Farey research frontier

This result distinguishes two questions that should not be conflated.

First, denominator strata do provide an exact signed multiscale geometry: the shells `e_q` have nontrivial positive and negative cross-correlations given by (13), and prime-power depth leaves the diagonal shell norm unchanged while changing off-diagonal coupling. This structure can be useful for reorganizing estimates.

Second, **linear harmonic observables of the cumulative shell discrepancy are not a new source of arithmetic information**. Equation (20) expresses every Fourier mode through the familiar Mertens function. A proposed Farey mechanism that only changes basis, diagonalizes the shell Gram matrix, or selects Fourier bands after forming `D_N` must therefore show a quantitatively stronger estimate; it cannot claim an independent arithmetic carrier merely because the denominator-shell representation looks multiscale.

This does not kill ordered-gap, mediant-ancestry, refinement-path, or other pre-cumulative information. Those objects can retain relations that are erased when each denominator level is reduced to the scalar counting function `e_q`. It also does not show that a nonlinear functional of the shell family is reducible to one scalar Mertens value. The precise obstruction is the modewise linear/cumulative interface (19)--(22).

## 6. Prior art and audit boundary

García, *New Analytical Formulas for the Rank of Farey Fractions and Estimates of the Local Discrepancy*, Mathematics **13** (2025), 140, DOI `10.3390/math13010140`, explicitly decomposes Farey local discrepancy into exact-denominator/totient-level discrepancies and derives Mertens-based formulas. That makes the denominator-level viewpoint itself prior art.

Ramanujan, *On Certain Trigonometrical Sums and Their Applications in the Theory of Numbers*, Trans. Cambridge Philos. Soc. **22** (1918), 259--276, is the classical source for the sums `c_q(k)` and their elementary arithmetic. Codecà--Perelli, *On the uniform distribution (mod 1) of the Farey fractions and l^p spaces*, Math. Ann. **279** (1988), 413--422, DOI `10.1007/BF01456278`, is a neighboring harmonic-analysis boundary for Farey uniform distribution and RH-sensitive estimates.

A targeted search did not establish that formulas (13) and (18) have not appeared elsewhere; they follow elementarily from classical Ramanujan-sum identities and should be treated as a derived organization, not a theorem-level novelty claim. The substantive Mathia delta is the exact **boundary statement** obtained by composing the denominator-shell decomposition with Ramanujan Fourier analysis: before pursuing more shell-only spectral geometry, one can see explicitly which part is already a divisor transform of Mertens and where genuinely ordered Farey information would have to enter.

The result concerns the continuous counting discrepancy `D_N` in (2), not directly the discrete Franel quadratic sum over rank positions. Transferring an estimate between those norms requires its own quantitative argument. No RH estimate, improved discrepancy exponent, or new bound on `M(N)` is proved here.
