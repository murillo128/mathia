# PC-317 — common-radial Poisson product is affine-periodic Hurwitz data

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for one-parameter radial scalarizations of the nonlinear cross-level Poisson product of PC-316.

PC-316 is deliberately not a scalar no-go: multiplying two oriented prime-level Hardy/Poisson fields before angular compression preserves the two independent Fourier indices `(k,l)`, and an additional downstream Poisson depth supplies the genuinely coupled coordinate `k+l`. Mellinizing the three depths independently therefore lands in a finite bundle of classical Mordell–Tornheim double `L`-functions rather than collapsing immediately to a one-variable Dirichlet series.

A natural next test is whether a **geometrically distinguished one-parameter radial slice** of that three-depth field retains a special source-specific analytic object. The most symmetric choice is the common-radial diagonal `x=y=z=t`. It does not. For arbitrary centered prime-level sources, the resulting additive-convolution coefficients satisfy an exact affine-periodicity law with period `qr`; for the canonical Prime-Circle prime-support sources the drift is exactly `+1` per period. Consequently the diagonal Mellin transform is one universal shifted Riemann-zeta term plus a finite rational-shift Hurwitz packet.

More generally, every rational one-parameter radial ray of the PC-316 construction has a rational generating function with only root-of-unity poles of order at most two. Its coefficient sequence is therefore eventually quasipolynomial of degree at most one, and its Mellin transform again lies in a finite span of rational-shift `zeta(s,alpha)` and `zeta(s-1,alpha)` terms plus a finite Dirichlet polynomial.

Thus the genuinely two-index Mordell–Tornheim information of PC-316 survives only while at least two independent radial variables are retained. Collapsing those depths onto any rational one-dimensional radial ray restores classical finite Hurwitz data.

## 1. Common-radial restriction turns the two-index field into additive convolution

Use the notation of PC-316. Let `q` and `r` be distinct primes, let

\[
f:\mathbb Z/q\mathbb Z\to\mathbb C,
\qquad
g:\mathbb Z/r\mathbb Z\to\mathbb C
\]

be centered sources, and define the periodic Fourier sequences

\[
a(k):=\widehat f(k\bmod q),
\qquad
b(l):=\widehat g(l\bmod r).
\tag{1}
\]

PC-316 gives, at the common anchored vertex,

\[
H_{q,r}^{f,g}(x,y,z)
=\sum_{k,l\ge1}a(k)b(l)e^{-kx-ly-(k+l)z}
=A_{q,f}(x+z,0)B_{r,g}(y+z,0).
\tag{2}
\]

On the symmetric common-radial diagonal `x=y=z=t`,

\[
\boxed{
H_{q,r}^{f,g}(t,t,t)
=A_{q,f}(2t,0)B_{r,g}(2t,0)
=\sum_{k,l\ge1}a(k)b(l)e^{-2(k+l)t}.
}
\tag{3}
\]

Group terms by `n=k+l`. With

\[
c(n):=\sum_{k=1}^{n-1}a(k)b(n-k),
\qquad c(1):=0,
\tag{4}
\]

we obtain the exact one-variable expansion

\[
\boxed{
H_{q,r}^{f,g}(t,t,t)
=\sum_{n\ge1}c(n)e^{-2nt}.
}
\tag{5}
\]

The question is therefore no longer the full two-index analytic structure of PC-316, but the arithmetic retained by this source-forced additive convolution.

## 2. CRT gives an exact affine-periodicity law

Put

\[
N:=qr,
\qquad
S_a:=\sum_{h=1}^{q}a(h),
\qquad
S_b:=\sum_{j=1}^{r}b(j).
\tag{6}
\]

Because `N` is a period of both coefficient sequences,

\[
\begin{aligned}
c(n+N)-c(n)
&=\sum_{k=n}^{n+N-1}a(k)b(n+N-k).
\end{aligned}
\tag{7}
\]

As `k` runs through any `N=qr` consecutive integers, the Chinese remainder theorem makes

\[
k\longmapsto (k\bmod q,\ n-k\bmod r)
\]

a bijection from `Z/NZ` to `(Z/qZ)\times(Z/rZ)`. Hence the new block in (7) factorizes exactly:

\[
\boxed{
c(n+N)-c(n)=S_aS_b.}
\tag{8}
\]

This identity holds for every `n>=1` and for arbitrary periodic sequences of coprime periods `q` and `r`; no asymptotic argument is involved.

Finite Fourier orthogonality identifies the drift directly in source space. With the unnormalized transform convention of PC-316,

\[
\sum_{h\bmod q}\widehat f(h)=qf(0),
\qquad
\sum_{j\bmod r}\widehat g(j)=rg(0).
\tag{9}
\]

The ranges in (6) traverse every residue once, including the zero residue represented by `q` or `r`. Therefore

\[
\boxed{S_a=qf(0),\qquad S_b=rg(0),}
\tag{10}
\]

and the affine drift is

\[
\boxed{c(n+qr)-c(n)=qr\,f(0)g(0).}
\tag{11}
\]

This already shows that the nonperiodic part of the common-radial coefficient sequence is controlled only by the two source values at the distinguished anchor residue.

## 3. The canonical Prime-Circle source forces a universal `+1` ramp

For the canonical prime-support source of PC-306--PC-310, at a prime level `q>3`,

\[
\nu_q(x)=\frac{1}{M_q}\mathbf 1_{\{x\in P_q\}},
\qquad
P_q=\{p:2<p<q,\ p\text{ prime}\},
\qquad
f_q(x)=\nu_q(x)-\frac1q.
\tag{12}
\]

The anchored residue `x=0` is not in `P_q`, so

\[
f_q(0)=-\frac1q.
\tag{13}
\]

Thus for two canonical sources at distinct prime levels `q,r`, equations (10)--(11) give

\[
S_a=S_b=-1
\]

and therefore the particularly rigid recurrence

\[
\boxed{c(n+qr)=c(n)+1.}
\tag{14}
\]

Define

\[
d(n):=c(n)-\frac{n}{qr}.
\tag{15}
\]

Then (14) is equivalent to

\[
\boxed{d(n+qr)=d(n)}
\tag{16}
\]

for every `n>=1`. Hence the complete common-radial coefficient sequence is exactly

\[
\boxed{c(n)=\frac{n}{qr}+d(n),}
\tag{17}
\]

where `d` is a bounded `qr`-periodic sequence.

The interpretation matters. The affine ramp does **not** encode the internal prime support of `P_q` or `P_r`; its coefficient `1/(qr)` is forced solely by the values `f_q(0)=-1/q` and `f_r(0)=-1/r` introduced when the normalized prime-support measures are centered against the uniform measure. All finer arithmetic can survive only in the bounded periodic residual `d`.

## 4. Diagonal Mellinization is one shifted zeta plus a finite Hurwitz packet

Since `a` and `b` are bounded, (4) gives `c(n)=O(n)`. Therefore for `Re(s)>2`, termwise Mellin integration of (5) is absolutely valid:

\[
\begin{aligned}
\mathcal M_{\mathrm{diag}}(s)
&:=\int_0^\infty t^{s-1}H_{q,r}^{f_q,f_r}(t,t,t)\,dt\\
&=\Gamma(s)2^{-s}\sum_{n\ge1}\frac{c(n)}{n^s}.
\end{aligned}
\tag{18}
\]

Substituting (17) yields

\[
\boxed{
\mathcal M_{\mathrm{diag}}(s)
=\Gamma(s)2^{-s}
\left[
\frac1{qr}\zeta(s-1)+D_{q,r}(s)
\right],
}
\tag{19}
\]

where

\[
D_{q,r}(s):=\sum_{n\ge1}\frac{d(n)}{n^s}.
\tag{20}
\]

Because `d` is exactly `N=qr` periodic, splitting into residue classes gives the finite Hurwitz decomposition

\[
\boxed{
D_{q,r}(s)
=N^{-s}\sum_{a=1}^{N}d(a)
\zeta\!\left(s,\frac{a}{N}\right).
}
\tag{21}
\]

Equations (19)--(21) are the decisive collapse. The common-radial slice no longer has the Mordell–Tornheim denominator `k^s l^t(k+l)^u` of PC-316. Its entire analytic continuation is inherited from one universal shifted Riemann zeta and finitely many rational-shift Hurwitz zeta functions.

The `zeta(s-1)` term is not an RH mechanism. It is a source-independent ramp forced by centering at the omitted anchor residue. In particular, importing the nontrivial zeros of `zeta(s-1)` merely shifts the ordinary critical line to `Re(s)=3/2`; it supplies no independent reason for the zeros of `zeta(s)` to lie on `Re(s)=1/2`. The periodic residual likewise inherits the universal finite-Fourier/Hurwitz duality already classified in PC-313. No zero-selection property is implied by (21).

## 5. Every rational one-parameter radial ray has the same classical destination

The common diagonal is the strongest exact recurrence, but the collapse is not special to the equality `x=y=z`. Restrict (2) to a one-parameter ray

\[
x=\alpha t,\qquad y=\beta t,\qquad z=\gamma t,
\tag{22}
\]

with positive effective rates

\[
\lambda_1:=\alpha+\gamma>0,
\qquad
\lambda_2:=\beta+\gamma>0.
\tag{23}
\]

If `lambda_1/lambda_2` is rational, rescaling `t` lets us write the rates as positive integers `A,B`. The restricted field then has generating function

\[
G(z)
:=\sum_{k,l\ge1}a(k)b(l)z^{Ak+Bl}
=\left(\sum_{k\ge1}a(k)z^{Ak}\right)
 \left(\sum_{l\ge1}b(l)z^{Bl}\right).
\tag{24}
\]

Periodicity gives finite numerators `P_a,P_b` with

\[
\sum_{k\ge1}a(k)z^{Ak}
=\frac{P_a(z)}{1-z^{Aq}},
\qquad
\sum_{l\ge1}b(l)z^{Bl}
=\frac{P_b(z)}{1-z^{Br}}.
\tag{25}
\]

Hence

\[
\boxed{
G(z)=
\frac{P_a(z)P_b(z)}
{(1-z^{Aq})(1-z^{Br})}.
}
\tag{26}
\]

Let `L=lcm(Aq,Br)`. Multiplying each denominator into `1-z^L` rewrites (26) as

\[
\boxed{G(z)=\frac{Q(z)}{(1-z^L)^2}}
\tag{27}
\]

for a polynomial `Q`. It follows by elementary root-of-unity partial fractions, equivalently by expanding `(1-z^L)^{-2}`, that the coefficient sequence of `G` is eventually quasipolynomial of degree at most one and period dividing `L`.

Therefore the Mellin/Dirichlet transform of **every rational one-parameter radial ray** is a finite linear combination of rational-shift Hurwitz functions of the forms

\[
\zeta\!\left(s,\frac{a}{L}\right),
\qquad
\zeta\!\left(s-1,\frac{a}{L}\right),
\tag{28}
\]

plus a finite Dirichlet polynomial accounting for any initial exceptional coefficients. The exact common diagonal is stronger because (14)--(17) identify the affine drift from the Prime-Circle source itself and hold from the first coefficient onward.

## 6. Prior art and novelty audit

No novelty is claimed for the analytic machinery behind (21), (27), or (28). PC-190 already records Makoto Ishibashi and Shigeru Kanemitsu, **Dirichlet series with periodic coefficients**, *Results in Mathematics* 35 (1999), 70--88, DOI `10.1007/BF03322023`, as prior art for periodic-coefficient Dirichlet series and explicitly derives finite rational-shift Hurwitz decompositions from periodic/quasipolynomial coefficients. PC-190 also uses the same standard rational-generating-function mechanism for denominators `(1-z^n)^m`: root-of-unity poles of bounded order force periodic/quasipolynomial coefficient data.

PC-313 independently shows that the finite Hurwitz/Fourier functional-equation swap of a periodic Dirichlet series is universal and therefore cannot be credited to the arithmetic source. PC-316 supplies the other side of the comparison: before one-parameter radial scalarization, the same two source indices really do produce a classical Mordell–Tornheim multiple-`L` bundle.

A directed prior-art search found the expected classical literature on periodic Dirichlet series, rational generating functions/quasipolynomials, and Mordell–Tornheim series, but did not locate the exact line-specific statement (14) for the centered Prime-Circle source. That absence is **not** a historical novelty claim. Equation (14) is an elementary consequence of finite Fourier orthogonality, the Chinese remainder theorem, and the particular anchor value of the canonical source.

The durable Mathia contribution is therefore narrower and exact: the canonical PC-316 common-radial slice has the source-forced recurrence `c(n+qr)=c(n)+1`, and the whole rational one-parameter radial family is thereby located on the classical quasipolynomial/Hurwitz side of the research boundary.

## 7. Research consequence

PC-316 remains a genuine information-retention result: with independent depths, the pair `(k,l)` survives and the nonlinear field reaches the established but genuinely multivariable Mordell–Tornheim class. PC-317 identifies exactly what is lost when those depths are collapsed onto a single rational radial parameter.

The chain

\[
\text{two prime-level oriented fields}
\longrightarrow
\text{pointwise product}
\longrightarrow
\text{one rational radial parameter}
\longrightarrow
\text{one Mellin variable}
\]

cannot be counted as a new RH mechanism. Its coefficients are affine-periodic/quasipolynomial and its analytic continuation is a finite Hurwitz packet, with a universal `zeta(s-1)` term in the symmetric canonical case.

This does **not** close PC-316's full multivariable bundle, irrational radial rays, nonlinear observables that retain a genuinely two-dimensional index geometry, source-dependent non-additive couplings, matrix/tensor-valued cross-level states, or growing-level limits. In particular it does not prove anything about a source-specific zero-selection property of the full Mordell–Tornheim coefficient vector. It only rules out obtaining such a property by first collapsing the canonical additive geometry onto a rational one-dimensional radial ray.

## 8. Audit and falsification tests

The finding can be checked without any RH assumption:

1. Expand PC-316 on `x=y=z=t` and verify directly that the coefficient of `e^{-2nt}` is the convolution (4).
2. For arbitrary periodic test sequences of coprime periods `q,r`, compute `c(n+qr)-c(n)` and verify the CRT factorization (8).
3. Verify finite Fourier orthogonality (9), then substitute the canonical centered prime-support value `f_q(0)=-1/q` to recover the exact `+1` recurrence (14).
4. Check that `d(n)=c(n)-n/(qr)` is exactly `qr`-periodic from the first coefficient; any violation falsifies (17).
5. Numerically Mellin-transform the common-radial field in `Re(s)>2` and compare with the right side of (19)--(21).
6. For a rational ray with integer rates `A,B`, expand the two periodic generating functions and verify (26)--(27); the coefficient tail must be affine on each residue class modulo `L`.
7. Retain two independent radial variables instead of one. The quasipolynomial classification must then fail in general and the two-index Mordell–Tornheim structure of PC-316 must reappear, confirming that PC-317 is a scalarization boundary rather than a contradiction of PC-316.