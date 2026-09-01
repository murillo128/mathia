# PC-116 — joint two-prime Hardy corrector has a zero-free Gaussian determinant

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` + `DECISIVE-BOUNDARY`. PC-114 classified the one-new-prime Hardy microlocal corrector `G_{p,q}` when `p -> infinity` with `q` fixed, and PC-115 then showed that the resulting model has a zero-free Gaussian determinant when `q -> infinity`. PC-115 explicitly left arbitrary simultaneous paths `p,q -> infinity` open because no uniform-in-`q` version of the PC-114 two-scale operator limit had been established. That gap can be closed directly at the **finite corrector** level, without proving any uniform two-scale convergence theorem.

For distinct odd primes `p,q`, define `G_{p,q}` exactly as in PC-113. There is a universal triangular Riemann sum `B_N`, independent of primality, such that

\[
\boxed{\|G_{p,q}\|_{\mathcal S_2}^2=B_{pq}+(q-2)B_p.}
\]

Moreover

\[
B_N\longrightarrow c:=\gamma-4+5\log2,
\]

so along **every** joint path `p,q -> infinity` through distinct odd primes,

\[
\boxed{
\left\|\frac{G_{p,q}}{\sqrt{q-1}}\right\|_{\mathcal S_2}^2
\longrightarrow c.
}
\]

At the same time the unscaled correctors are uniformly bounded in operator norm, hence

\[
\boxed{
\left\|\frac{G_{p,q}}{\sqrt{q-1}}\right\|
\longrightarrow0.
}
\]

Consequently both the Hilbert--Schmidt regularized determinant and the ordinary Fredholm determinant converge locally uniformly to the same zero-free Gaussian entire function,

\[
\boxed{
\det_2\!\left(I-z\frac{G_{p,q}}{\sqrt{q-1}}\right)
\longrightarrow
\exp\!\left(-\frac c2z^2\right),
}
\]

\[
\boxed{
\det\!\left(I-z\frac{G_{p,q}}{\sqrt{q-1}}\right)
\longrightarrow
\exp\!\left(-\frac c2z^2\right).
}
\]

Thus the scalar-normalized finite two-prime Hardy corrector cannot recover a Riemann-zero divisor by exploiting a coupled conductor limit. The remaining Hardy boundary is genuinely narrower: a surviving mechanism must use non-scalar conductor-dependent organization, nonlinear operations before the PC-113 split, or another intrinsic operator family rather than the scalar determinant of `G_{p,q}`.

No theorem-level historical novelty is claimed for Ramanujan sums, triangular Riemann sums, trace ideals, `det_2`, or Gaussian determinant limits under infinitesimal operator norm. The durable Prime-Circle content is the exact finite identity for the canonical two-prime corrector and the resulting closure of the simultaneous-conductor escape left open by PC-115.

## 1. Finite two-prime corrector and the off-origin block norm

PC-113 gives, for `p` prime with `p` not dividing `q`, after writing a residue modulo `pq` as

\[
R=pa+r,
\qquad
0\le a<q,
\qquad
0\le r<p,
\]

the exact decomposition

\[
R_{pq}=J_p\otimes R_q+G_{p,q}.
\]

Flattening `(a,r)` to `R=pa+r`, and similarly `(b,s)` to `S=pb+s`, the corrector block is

\[
\boxed{
(G_{p,q})_{R,S}
=
\frac{c_q(R+S+1)}{pq}
D^\circ_{(R+S+1)/(pq)},
}
\]

where `D^\circ_\alpha` is the generalized-Hilbert defect with only the Hardy `(0,0)` entry deleted. Put

\[
F(\alpha):=
\|D^\circ_\alpha\|_{\mathcal S_2}^2.
\]

Because only the `(0,0)` coordinate is removed, grouping Hardy pairs by `m=a+b>=1` gives the exact scalar formula

\[
\boxed{
F(\alpha)
=
\sum_{m\ge1}(m+1)
\left(
\frac1{m+\alpha}-\frac1{m+1}
\right)^2.
}
\]

Equivalently,

\[
F(\alpha)
=(1-\alpha)^2
\sum_{m\ge1}
\frac{m+1}{(m+\alpha)^2(m+1)^2}.
\]

PC-113 proves the stronger `\mathcal S_2`-Lipschitz continuity of `\alpha -> D^\circ_\alpha` on `[0,2]`; in particular `F` is continuous and bounded there. Also

\[
\boxed{F(1)=0.}
\]

That zero is what removes the exceptional prime Ramanujan anti-diagonal in the one-prime case and is again essential below.

## 2. A universal triangular Riemann sum

For every integer `N>=2`, define

\[
m_N(t):=\min(t,2N-t),
\qquad 1\le t\le2N-1,
\]

and

\[
\boxed{
B_N:=
\frac1{N^2}
\sum_{t=1}^{2N-1}
 m_N(t)F(t/N).
}
\]

The factor `m_N(t)` is exactly the number of ordered pairs `(R,S)` with

\[
0\le R,S<N,
\qquad
R+S+1=t.
\]

Writing the sum as

\[
B_N
=
\frac1N
\sum_{t=1}^{2N-1}
\frac{m_N(t)}N F(t/N),
\]

shows directly, by continuity of `F`, that it is the Riemann sum for

\[
\int_0^2\min(x,2-x)F(x)\,dx.
\]

The PC-109 microlocal kernel `\mathcal K` has precisely the off-origin generalized-Hilbert defect `D^\circ_{x+y}` at `(x,y) in [0,1]^2`. Therefore

\[
\begin{aligned}
\int_0^2\min(x,2-x)F(x)\,dx
&=
\int_0^1\int_0^1
\|D^\circ_{x+y}\|_{\mathcal S_2}^2\,dx\,dy\\
&=
\|\mathcal K\|_{\mathcal S_2}^2.
\end{aligned}
\]

PC-108/PC-109 evaluated this universal norm exactly as

\[
\boxed{
c:=\gamma-4+5\log2.}
\]

Hence, with no primality assumption on `N`,

\[
\boxed{B_N\longrightarrow c.}
\]

For a prime `p`, `c_p(t)^2=1` except at `t=p`, where the discrepancy multiplies `F(1)=0`. Thus the prime off-origin remainder satisfies the useful exact identity

\[
\boxed{\|R_p\|_{\mathcal S_2}^2=B_p.}
\]

## 3. Exact finite Hilbert--Schmidt identity for `G_{p,q}`

Let now `p,q` be distinct odd primes and put `N=pq`. From the flattened block formula,

\[
\|G_{p,q}\|_{\mathcal S_2}^2
=
\frac1{p^2q^2}
\sum_{t=1}^{2pq-1}
 m_{pq}(t)c_q(t)^2F(t/(pq)).
\]

For prime `q`, the Ramanujan sum is `-1` away from multiples of `q` and `q-1` on multiples of `q`, hence exactly

\[
\boxed{
c_q(t)^2
=1+q(q-2)\mathbf1_{q\mid t}.}
\]

The baseline `1` contributes exactly `B_{pq}`. For the spike term write `t=qh`, `1<=h<=2p-1`. Then

\[
m_{pq}(qh)=q\,m_p(h),
\qquad
F\!\left(\frac{qh}{pq}\right)=F(h/p).
\]

Therefore

\[
\begin{aligned}
&\frac{q(q-2)}{p^2q^2}
\sum_{q\mid t}
 m_{pq}(t)F(t/(pq))\\
&\qquad=
\frac{q(q-2)}{p^2q^2}
\sum_{h=1}^{2p-1}
 q\,m_p(h)F(h/p)\\
&\qquad=
(q-2)B_p.
\end{aligned}
\]

Thus the finite identity is

\[
\boxed{
\|G_{p,q}\|_{\mathcal S_2}^2
=B_{pq}+(q-2)B_p.
}
\]

This formula has two important consistency checks. First, with `q` fixed and `p -> infinity`,

\[
\|G_{p,q}\|_{\mathcal S_2}^2
\longrightarrow
c+(q-2)c
=(q-1)c
=\varphi(q)c,
\]

which exactly recovers the hidden Hilbert--Schmidt mass found in the PC-114 fixed-`q` model `S_q\otimes\mathcal K`. Second, no ratio `p/q` occurs anywhere in the exact formula.

Now let both primes tend to infinity along an arbitrary joint path. Then

\[
\begin{aligned}
\frac{\|G_{p,q}\|_{\mathcal S_2}^2}{q-1}
&=
\frac{B_{pq}}{q-1}
+
\frac{q-2}{q-1}B_p\\
&\longrightarrow c.
\end{aligned}
\]

Hence for

\[
\boxed{X_{p,q}:=\frac{G_{p,q}}{\sqrt{q-1}}}
\]

we have the path-independent second-moment law

\[
\boxed{
\|X_{p,q}\|_{\mathcal S_2}^2\longrightarrow c.
}
\]

This conclusion is finite-level and bypasses the missing uniform-in-`q` two-scale convergence estimate identified in PC-115.

## 4. The same normalization kills operator norm uniformly

To turn the second-moment law into a determinant classification we need to exclude a hidden finite number of order-one eigenvalues. The required bound follows from the exact Hardy dilation calculus, without a new asymptotic estimate.

PC-079 gives

\[
\Gamma_q=(\mathfrak D_q-I)\Gamma_1
\]

for prime `q`, and

\[
\Gamma_{pq}
=(\mathfrak D_p-I)(\mathfrak D_q-I)\Gamma_1
\]

for distinct primes. Since

\[
\|\Gamma_1\|=\pi,
\qquad
\|\mathfrak D_d\Gamma_1\|=\pi
\]

by the exact residue-split tensor representation `\mathfrak D_d\Gamma_1\cong J_d\otimes\Gamma_1`, the finite expansions give

\[
\boxed{\|\Gamma_q\|\le2\pi,}
\qquad
\boxed{\|\Gamma_{pq}\|\le4\pi.}
\]

PC-075 writes, after residue splitting,

\[
W_n\Gamma_nW_n^*
=-\frac1nC_n\otimes H+T_n.
\]

For `n>2`, `\|C_n/n\|=1` and `\|H\|=\pi`, hence

\[
\|T_q\|\le3\pi,
\qquad
\|T_{pq}\|\le5\pi.
\]

The off-origin operator `R_n` is obtained from `T_n` by deleting its lowest-Hardy compression. If `Q_n` denotes that orthogonal compression,

\[
R_n=T_n-Q_nT_nQ_n,
\]

so

\[
\|R_n\|\le2\|T_n\|.
\]

Consequently

\[
\|R_q\|\le6\pi,
\qquad
\|R_{pq}\|\le10\pi.
\]

Finally PC-113 gives the exact decomposition

\[
G_{p,q}=R_{pq}-J_p\otimes R_q,
\]

with `\|J_p\|=1`. Therefore, uniformly in the distinct odd primes,

\[
\boxed{\|G_{p,q}\|\le16\pi.}
\]

The canonical scalar normalization therefore satisfies

\[
\boxed{
\|X_{p,q}\|
\le\frac{16\pi}{\sqrt{q-1}}
\longrightarrow0.
}
\]

Thus the finite joint-conductor family has exactly the combination needed for a Gaussian determinant law: nonzero limiting `\mathcal S_2` mass but vanishing maximal eigenvalue.

## 5. The `det_2` limit is Gaussian and zero-free on every joint path

Every `G_{p,q}` is self-adjoint: the finite residue kernel depends symmetrically on `R+S`, the prime Ramanujan sums are real, and each `D^\circ_\alpha` is self-adjoint. Also `G_{p,q}` is trace class at every finite pair because PC-113 expresses it as the difference of the trace-class operators `R_{pq}` and `J_p\otimes R_q`.

For a Hilbert--Schmidt operator `X`, the standard regularized determinant has, whenever `|z|\|X\|<1`, the trace expansion

\[
\log\det_2(I-zX)
=-\sum_{k\ge2}\frac{z^k}{k}\operatorname{Tr}(X^k).
\]

For `X=X_{p,q}`, self-adjointness gives

\[
\operatorname{Tr}(X_{p,q}^2)
=\|X_{p,q}\|_{\mathcal S_2}^2
\longrightarrow c.
\]

For every `k>=3`, the trace-ideal estimate

\[
\left|\operatorname{Tr}(X_{p,q}^k)\right|
\le
\|X_{p,q}\|^{k-2}
\|X_{p,q}\|_{\mathcal S_2}^2
\]

forces the higher traces to zero. Since the operator norms tend to zero and the `\mathcal S_2` norms stay bounded, the tail estimate is uniform on every compact `z`-set. Therefore

\[
\boxed{
\det_2(I-zX_{p,q})
\longrightarrow
\exp\!\left(-\frac c2z^2\right)
}
\]

locally uniformly on `\mathbb C`, along every simultaneous path `p,q -> infinity` through distinct odd primes.

The limit has no zeros. Hence allowing the two conductors to grow simultaneously does not resurrect a Riemann-zero divisor that was absent from the iterated limit in PC-115.

## 6. The ordinary Fredholm determinant has the same limit

Because every finite `G_{p,q}` is trace class, the ordinary determinant is also defined. It remains to check that the scalar trace does not survive the normalization.

Let

\[
g(\alpha):=\operatorname{Tr}D^\circ_\alpha
=
\sum_{a\ge1}
\left(
\frac1{2a+\alpha}-\frac1{2a+1}
\right).
\]

The series converges uniformly on `[0,2]`, so

\[
M:=\sup_{0\le\alpha\le2}|g(\alpha)|<\infty.
\]

Taking the residue diagonal `R=S` gives

\[
\operatorname{Tr}G_{p,q}
=
\frac1{pq}
\sum_{R=0}^{pq-1}
 c_q(2R+1)
 g\!\left(\frac{2R+1}{pq}\right).
\]

Because `q` is odd, multiplication by `2` is invertible modulo `q`. Among `R=0,...,pq-1`, exactly `p` values satisfy `q\mid(2R+1)`. Hence

\[
\sum_{R=0}^{pq-1}|c_q(2R+1)|
=p(q-1)+(pq-p)
=2p(q-1).
\]

Therefore

\[
\boxed{
|\operatorname{Tr}G_{p,q}|
\le2M\frac{q-1}{q}
\le2M,
}
\]

and so

\[
\boxed{
\operatorname{Tr}X_{p,q}\longrightarrow0.
}
\]

For trace-class `X`, the standard relation is

\[
\det_2(I-zX)
=
\det(I-zX)e^{z\operatorname{Tr}X}.
\]

Combining it with the `det_2` limit yields

\[
\boxed{
\det(I-zX_{p,q})
\longrightarrow
\exp\!\left(-\frac c2z^2\right)
}
\]

locally uniformly as well.

Thus neither the ordinary determinant nor its Hilbert--Schmidt regularization produces a nontrivial zero set in the simultaneous two-prime limit.

## 7. Scalar normalizations are exhausted at the finite-corrector level

The exact second-moment formula also classifies the scalar scale. Along any joint path,

\[
\|G_{p,q}\|_{\mathcal S_2}^2
\sim c(q-1).
\]

Therefore any scalar normalization `a_{p,q}` for which `a_{p,q}G_{p,q}` has finite nonzero limiting Hilbert--Schmidt mass must have

\[
|a_{p,q}|\asymp q^{-1/2}.
\]

But the uniform operator bound then forces

\[
\|a_{p,q}G_{p,q}\|\longrightarrow0.
\]

If, along a subsequence, `a_{p,q}^2(q-1) -> \lambda`, the same trace expansion gives the only possible nontrivial regularized determinant limit

\[
\boxed{
\exp\!\left(-\frac{\lambda c}{2}z^2\right),
}
\]

again zero-free. Thus changing only the scalar normalization cannot recover a hidden discrete divisor from the finite two-prime corrector.

This statement is deliberately about scalar normalization. A conductor-dependent non-scalar conjugation or unfolding can alter operator-norm geometry and remains outside this argument.

## 8. Falsification checks

The derivation has several independent finite tests.

1. Compute `F(\alpha)` by truncating the Hardy indices and verify `F(1)=0` and continuity on `[0,2]`.
2. For finite distinct primes, compute the Hilbert--Schmidt norm directly from the flattened blocks and compare it with `B_{pq}+(q-2)B_p`. Numerical truncation at 5000 Hardy anti-diagonals gives, for `(p,q)=(5,7)`, `0.3062664337958673` directly versus `0.3062664337958677` from the factorized formula, and for `(11,13)`, `0.548447635075969` versus `0.5484476350759668`.
3. At fixed `q`, verify that the norm tends to `(q-1)c`, matching PC-114.
4. Along joint prime paths with very different ratios `p/q`, verify that `\|G_{p,q}\|_2^2/(q-1)` tends to the same constant `c≈0.0429515677012593`.
5. The operator-norm bound can be falsified entirely from existing exact identities: expand `\Gamma_q` and `\Gamma_{pq}` into at most two and four Hilbert dilations, use the PC-075 channel norm, then apply the PC-113 decomposition.
6. For the trace bound, count solutions of `2R+1=0 mod q`; there must be exactly `p` in one complete set of `p` residue cycles modulo `q`.

These checks target the coefficient, the prime spike multiplicity, the normalization, and the determinant trace term independently.

## 9. Prior-art and novelty audit

The general analytic ingredients are classical and already lie in the audit surface anchored by PC-075, PC-107, and PC-115.

1. The prime formula `c_q(t)=q-1` on multiples of `q` and `-1` otherwise is elementary Ramanujan-sum theory. Finite matrices built from Ramanujan sums and their Fourier spectra are established territory; Ushiroya's 2018 work is already the relevant source anchor used by PC-115.
2. The operator-ideal inequalities, Fredholm determinant, modified determinant `det_2`, and trace-log expansion are standard trace-ideal theory; Barry Simon's *Trace Ideals and Their Applications* is already the canonical source anchor used in PC-107/PC-115.
3. The passage from a triangular lattice sum to `\int_0^1\int_0^1F(x+y)dxdy` is an ordinary Riemann-sum argument. The constant `c` and the Carleman--Hilbert defect are not new here; they were derived and classified in PC-108--PC-110.
4. Directed searches for Ramanujan-sum Hankel matrices, Hilbert--Schmidt regularized determinants, and Gaussian determinant limits found the surrounding classical matrix/trace-ideal mechanisms but no source making this exact finite `G_{p,q}` identity or using it as an RH construction. Absence of that formulation is not evidence of historical priority.

Accordingly the result should not be read as a new general determinant theorem. Its research value is a **boundary closure internal to Prime-Circle**: the simultaneous finite two-prime corrector that PC-115 had to leave open is forced, under every scalar Hilbert--Schmidt normalization, into the same zero-free Gaussian universality class.

## 10. Consequence for the research boundary

PC-115 could only conclude after the iterated route

\[
p\to\infty\text{ with }q\text{ fixed},
\qquad
q\to\infty.
\]

The exact finite identity above removes that order-of-limits escape for the canonical corrector:

\[
\boxed{
(p,q)\to(\infty,\infty)
\text{ arbitrarily}
\quad\Longrightarrow\quad
\text{scalar-normalized }G_{p,q}
\text{ has zero-free Gaussian determinant.}
}
\]

This does **not** show that all simultaneous semiprime Hardy structure is trivial. In particular it does not classify:

- conductor-dependent non-scalar conjugations or microlocalizations performed before taking a determinant;
- nonlinear operations applied before the PC-113 decomposition;
- operator families other than the canonical cyclotomic-log Hardy/Hankel coupling;
- global uniformization/monodromy or other Prime-Circle branches outside this Hardy operator family.

What is closed is the specific natural escape left by PC-115: **arbitrary simultaneous growth of the two prime conductors does not save the scalar Fredholm or `det_2` spectralization of the finite PC-113 corrector.**