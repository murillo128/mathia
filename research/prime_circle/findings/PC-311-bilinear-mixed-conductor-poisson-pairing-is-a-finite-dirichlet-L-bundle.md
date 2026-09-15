# PC-311 — bilinear mixed-conductor Poisson pairing is a finite Dirichlet L-bundle

**Status:** `EXACT-DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the most direct bilinear mixed-conductor harmonic escape left after PC-310.

PC-310 shows that the mesh-scale Poisson boundary layer of one prime-level source is an invertible cyclic filter: at one conductor it can recover the centered source, but that recovery is only a one-level decoder and does not create a new RH mechanism. A natural next step is therefore to couple two distinct prime levels *before* separately decoding them and ask whether the common harmonic field creates a genuinely mixed-conductor spectral carrier.

For the canonical bilinear coupling, the answer is exact and negative. Let `q,r` be distinct primes and let

\[
f:\mathbb Z/q\mathbb Z\to\mathbb C,
\qquad
g:\mathbb Z/r\mathbb Z\to\mathbb C
\]

be arbitrary centered sources. This includes the centered prime-support sources of PC-306--PC-310. Extend each source harmonically into the disk with the ordinary Poisson kernel, place the two fields at independent radial depths, and take their common-circle sesquilinear pairing. Then:

1. the two depths collapse exactly to their sum;
2. the cross-level pairing is exactly one cyclic Poisson convolution on the common refinement `Z/(qr)Z`, acting between two sparse lifted source vectors;
3. after Mellinization, the coefficient sequence is periodic modulo `qr` and supported on the units;
4. hence the entire spectralized object is a **finite linear combination of ordinary Dirichlet `L(s,chi)` functions**, evaluated only in the single variable `s+t`;
5. under CRT the coefficients of that `L`-bundle factor into separate one-level character transforms, with only the even composite-character sector surviving the two-sided Poisson pairing.

Thus the first bilinear cross-level repair of the PC-310 one-conductor boundary really does mix the two conductors geometrically, but it does not produce a new analytic species, a genuinely two-variable spectral parameter, a new functional equation, or a critical-line mechanism.

## 1. Two centered Poisson fields couple through one Fourier index

For `0<rho<1`, write the circle Poisson kernel as

\[
P_\rho(\theta)
=\frac{1-\rho^2}{1-2\rho\cos\theta+\rho^2}
=\sum_{k\in\mathbb Z}\rho^{|k|}e^{ik\theta}.
\tag{1}
\]

Use the unnormalized finite Fourier transform

\[
\widehat f(h)
:=\sum_{u\bmod q}f(u)e^{-2\pi ihu/q},
\qquad
\widehat g(j)
:=\sum_{v\bmod r}g(v)e^{-2\pi ijv/r}.
\tag{2}
\]

Since the sources are centered,

\[
\widehat f(0)=\widehat g(0)=0.
\tag{3}
\]

At radial depths `x,y>0`, define the two harmonic fields

\[
\mathcal P_{q,f}(x,\theta)
:=\sum_{u\bmod q}
f(u)P_{e^{-x}}\!\left(\theta-\frac{2\pi u}{q}\right),
\tag{4}
\]

and analogously `mathcal P_{r,g}(y,theta)`. Absolute convergence of (1) gives

\[
\boxed{
\mathcal P_{q,f}(x,\theta)
=\sum_{k\in\mathbb Z}
 e^{-|k|x}\widehat f(k\bmod q)e^{ik\theta}.
}
\tag{5}
\]

The canonical same-circle cross-level pairing is

\[
\mathcal B_{q,r}^{f,g}(x,y)
:=\frac1{2\pi}
\int_0^{2\pi}
\mathcal P_{q,f}(x,\theta)
\overline{\mathcal P_{r,g}(y,\theta)}\,d\theta.
\tag{6}
\]

Parseval orthogonality forces the same integer Fourier index on the two legs:

\[
\boxed{
\mathcal B_{q,r}^{f,g}(x,y)
=\sum_{k\in\mathbb Z}
 e^{-|k|(x+y)}
\widehat f(k\bmod q)
\overline{\widehat g(k\bmod r)}.
}
\tag{7}
\]

The `k=0` term vanishes by (3). Equation (7) already gives the first obstruction: two independent radial depths do not survive as two harmonic variables. The Poisson semigroup and angular Haar pairing reduce them exactly to `x+y` before any Mellin transform is taken.

## 2. The mixed-conductor geometry is one common-refinement circulant

Put

\[
N:=qr,
\qquad
\tau:=e^{-(x+y)}.
\tag{8}
\]

Lift the two source vectors sparsely to `Z/NZ` by

\[
F_N(ru):=f(u),
\qquad
G_N(qv):=g(v),
\tag{9}
\]

and set them to zero away from the indicated multiples. Then

\[
\widehat{F_N}(t)=\widehat f(t\bmod q),
\qquad
\widehat{G_N}(t)=\widehat g(t\bmod r).
\tag{10}
\]

The Poisson semigroup identity also gives a direct vertex-space form of (6):

\[
\boxed{
\mathcal B_{q,r}^{f,g}(x,y)
=\sum_{a,b\bmod N}
F_N(a)\overline{G_N(b)}
P_\tau\!\left(\frac{2\pi(a-b)}{N}\right).
}
\tag{11}
\]

Indeed, for `a=ru` and `b=qv`, the angular difference in (11) is exactly `2pi(u/q-v/r)`. Thus the direct bilinear interaction between the two levels is not a new two-conductor operator family. It is one ordinary `N`-cyclic convolution kernel restricted to the two geometry-forced sparse subspaces.

The sampled Poisson circulant can be diagonalized exactly. For `0<=t<N`, define

\[
A_{N,\tau}(t)
:=\sum_{m\in\mathbb Z}\tau^{|t+mN|}
=\frac{\tau^t+\tau^{N-t}}{1-\tau^N}.
\tag{12}
\]

For `t=0`, this reads `(1+tau^N)/(1-tau^N)`. Finite Fourier inversion of (11) gives

\[
\boxed{
\mathcal B_{q,r}^{f,g}(x,y)
=\sum_{t=0}^{N-1}
A_{N,\tau}(t)
\widehat f(t\bmod q)
\overline{\widehat g(t\bmod r)}.
}
\tag{13}
\]

Because `N=qr`, every nonunit residue `t mod N` is divisible by `q` or by `r`. Equation (3) therefore kills every nonunit term in (13):

\[
\boxed{
\mathcal B_{q,r}^{f,g}(x,y)
=\sum_{t\in(\mathbb Z/N\mathbb Z)^\times}
A_{N,\tau}(t)
\widehat f(t\bmod q)
\overline{\widehat g(t\bmod r)}.
}
\tag{14}
\]

So a genuine product conductor appears, but all source dependence is carried by the CRT tensor of the two one-level Fourier packets and all radial geometry is carried by the universal sampled Poisson multiplier `A_{N,tau}`.

## 3. Double Mellinization is a finite ordinary Dirichlet-L bundle

For `k>=1`, put

\[
c(k)
:=\widehat f(k\bmod q)
\overline{\widehat g(k\bmod r)}
\tag{15}
\]

and

\[
d(k):=c(k)+c(-k).
\tag{16}
\]

Equation (7) becomes

\[
\boxed{
\mathcal B_{q,r}^{f,g}(x,y)
=\sum_{k\ge1}d(k)e^{-k(x+y)}.
}
\tag{17}
\]

The sequence `d` is periodic modulo `N=qr`. Moreover, if `q|k`, then `widehat f(k mod q)=widehat f(0)=0`; if `r|k`, the corresponding `g` factor vanishes. Hence

\[
\boxed{
d(k)=0\quad\text{whenever }(k,N)>1.}
\tag{18}
\]

Thus `d` is simply a complex-valued function on the finite group `U(N)=(Z/NZ)^times`, extended by zero to nonunits. Dirichlet characters modulo `N` are the Fourier basis of this group, so there are unique coefficients

\[
\alpha_\chi
=\frac1{\varphi(N)}
\sum_{a\in U(N)}d(a)\overline{\chi(a)}
\tag{19}
\]

such that

\[
d(a)=\sum_{\chi\bmod N}\alpha_\chi\chi(a).
\tag{20}
\]

Consequently, in `Re u>1`,

\[
\boxed{
D_{f,g}(u)
:=\sum_{k\ge1}\frac{d(k)}{k^u}
=\sum_{\chi\bmod N}\alpha_\chi L(u,\chi).
}
\tag{21}
\]

For `Re s>0`, `Re t>0`, and `Re(s+t)>1`, termwise double Mellin integration in (17) gives

\[
\boxed{
\begin{aligned}
\mathcal M_2\mathcal B_{q,r}^{f,g}(s,t)
&:=\int_0^\infty\int_0^\infty
x^{s-1}y^{t-1}
\mathcal B_{q,r}^{f,g}(x,y)\,dx\,dy\\
&=\Gamma(s)\Gamma(t)
\sum_{\chi\bmod qr}
\alpha_\chi L(s+t,\chi).
\end{aligned}}
\tag{22}
\]

This is the decisive spectral classification. The bilinear mixed-conductor harmonic channel does not produce a genuinely two-variable `L`-object: all arithmetic zero data enter through ordinary Dirichlet `L`-functions in the single variable

\[
u=s+t.
\tag{23}
\]

The separate factors `Gamma(s)Gamma(t)` record only the two Laplace/Mellin integrations. They do not supply a new involution relating `s` and `1-s` or `t` and `1-t`. A principal-character term, when present, is just `zeta(u)` with the finite Euler factors at `q` and `r` removed.

## 4. CRT shows that even the L-bundle coefficients separate by source

The finite `L`-bundle in (22) could still look like a new mixed arithmetic coefficient system. CRT shows that the direct bilinear channel is more rigid.

Every character modulo `N=qr` is uniquely a product

\[
\chi_N(a)\leftrightarrow\chi_q(a\bmod q)\psi_r(a\bmod r).
\tag{24}
\]

First expand the positive-frequency coefficient `c` of (15). Define

\[
A_f(\chi)
:=\frac1{q-1}
\sum_{a\in U(q)}
\widehat f(a)\overline{\chi(a)},
\tag{25}
\]

and

\[
C_g(\psi)
:=\frac1{r-1}
\sum_{b\in U(r)}
\overline{\widehat g(b)}\overline{\psi(b)}.
\tag{26}
\]

Since `U(N)=U(q)times U(r)` under CRT, the character coefficient of `c` factorizes exactly:

\[
\boxed{
\alpha^+_{\chi,\psi}
=A_f(\chi)C_g(\psi).
}
\tag{27}
\]

The negative-frequency contribution is just the simultaneous inversion `(a,b)->(-a,-b)`. Since every Dirichlet character has parity `chi(-1)=+/-1`, equation (16) gives

\[
\boxed{
\alpha_{\chi,\psi}
=\bigl(1+\chi(-1)\psi(-1)\bigr)
A_f(\chi)C_g(\psi).
}
\tag{28}
\]

Thus only the **even composite-character sector** survives, and each surviving coefficient is a product of one `q`-source transform and one `r`-source transform. There is no new nonlinear mixed coefficient hidden in the bilinear harmonic coupling.

For the canonical prime source

\[
P_q=\{\ell:2<\ell<q,\ \ell\text{ prime}\},
\qquad
f_q=|P_q|^{-1}\mathbf1_{P_q}-q^{-1}\mathbf1,
\tag{29}
\]

we have, for `a!=0 mod q`,

\[
\widehat f_q(a)
=\frac1{|P_q|}
\sum_{\ell\in P_q}e^{-2\pi ia\ell/q}.
\tag{30}
\]

For every nonprincipal character `chi mod q`, the standard Gauss identity gives

\[
\boxed{
A_{f_q}(\chi)
=\frac{\tau(\overline\chi)}{(q-1)|P_q|}
\sum_{\ell\in P_q}\chi(-\ell).
}
\tag{31}
\]

The principal coefficient is `A_{f_q}(1)=-1/(q-1)`. Hence even for the actual growing Prime-Circle source, the bundle weights reduce to Gauss factors times finite Dirichlet-character sums over the primes below the conductor. Those coefficients may contain difficult arithmetic, but the analytic family in which they sit is already the ordinary finite Dirichlet-`L` family.

## 5. Relation to earlier Prime-Circle classifications

This result is consistent with, but not identical to, PC-199. PC-199 starts from individual primitive-shell **multiplicative-character** Cauchy--Poisson fields and proves that one sesquilinear pairing collapses to a single composite character packet `L(s+t,chi bar psi)`. The present calculation starts instead from the **arbitrary centered cyclic source** that became the live object in PC-296--PC-310, including the canonical prime-support law. The character packet is not selected in advance; equations (18)--(28) prove that the complete bilinear mixed-conductor source pairing decomposes into a finite sum of those classical character channels, with factorized CRT weights.

PC-201 already shows that fixed finite nonlinear Haar fusion can preserve several independent Fourier indices, but then lands in classical Mordell--Tornheim multiple `L`-data. PC-212 likewise shows that a different common-refinement construction, based on primitive cyclotomic coefficient masks, is coprime-flat after centering. The present obstruction is specifically for the post-PC-310 Poisson/source carrier: **the first direct cross-level bilinear harmonic coupling is one common-refinement circulant and one finite periodic Dirichlet series.**

The result therefore closes a concrete part of the current mixed-conductor frontier without claiming that every cross-level construction is exhausted.

## 6. Prior-art and novelty audit

The analytic target in (21)--(22) is classical periodic-Dirichlet-series theory. Makoto Ishibashi and Shigeru Kanemitsu, **Dirichlet series with periodic coefficients**, *Results in Mathematics* 35 (1999), 70--88, DOI `10.1007/BF03322023`, develops Dirichlet series attached to periodic arithmetic functions in a framework containing Dirichlet characters and ordinary Dirichlet `L`-functions. Tapas Chatterjee and M. Ram Murty, **Non-vanishing of Dirichlet series with periodic coefficients**, *Journal of Number Theory* 145 (2014), 1--21, DOI `10.1016/j.jnt.2014.05.010`, explicitly records the standard Hurwitz-zeta representation and character decomposition for periodic coefficients.

There is also literature showing why a functional equation of a specially engineered periodic Dirichlet series would not itself establish a new Prime-Circle mechanism. Takashi Nakamura, **Dirichlet Series with Periodic Coefficients, Riemann's Functional Equation, and Real Zeros of Dirichlet L-Functions**, *Mathematica Slovaca* 73:5 (2023), 1145--1152, DOI `10.1515/ms-2023-0084`, constructs periodic-coefficient combinations of Dirichlet `L`-functions satisfying Riemann-type functional equations. Thus a functional equation obtained only after choosing coefficients in the classical periodic-series space must be audited as classical analytic structure, not counted as geometry-forced novelty.

No novelty is claimed for the Poisson Fourier expansion, the semigroup identity, CRT, finite-group character orthogonality, Gauss sums, or periodic Dirichlet series. The proof above is self-contained; the references are novelty/context anchors rather than load-bearing theorem dependencies, so no `SOURCES.md` update is required.

The project-local mathematical delta is the exact source-to-target classification after PC-310: **coupling two arbitrary centered prime-level Poisson source fields through their most intrinsic bilinear common-circle interaction produces a unit-supported periodic coefficient on the product conductor, whose Mellin image is a factorized finite ordinary Dirichlet-`L` bundle.**

## 7. Falsification controls and surviving boundary

Every identity has finite controls. For arbitrary centered vectors `f` and `g`, equation (11) can be checked directly against angular quadrature or the Fourier series (7); equation (13) must agree with both after alias summation. A numerical audit at `q=5`, `r=7`, `x=0.31`, `y=0.47` with generic complex centered vectors made the infinite Fourier sum, the direct common-refinement Poisson kernel, and the finite alias formula agree to about `1.4e-14`. This is only a normalization/sign check; the persisted result rests on the exact derivation.

There are also decisive structural controls. The entire architecture works for arbitrary centered cyclic sources, not specifically the prime-support source, so the analytic species is not a prime discriminator. Replacing either source by a matched non-prime law changes only the finite coefficients `A_f` or `C_g`; it does not change the common-refinement Poisson operator or the Dirichlet-`L` target family. Likewise, allowing independent radial depths does not create two spectral variables because equation (7) sees only `x+y`.

What remains outside this finding is precisely where a stronger mixed-conductor mechanism would have to live. The result does **not** classify nonlinear coupling performed before same-index Haar/Parseval contraction, cross-level operators retaining two or more independent Fourier indices, non-circulant pointed interactions, shell-dependent matrix-valued kernels, singular growing-conductor normalizations that are not controlled by the fixed bilinear form above, or a separately justified zero-sensitive destination theorem. A viable next construction must preserve cross-level information that cannot be reduced to the CRT tensor of one-level Fourier packets followed by an ordinary periodic Dirichlet series.

Accordingly the closed route is

\[
\boxed{
\text{two centered prime-level Poisson fields}
\xrightarrow{\text{bilinear same-circle pairing}}
\text{one }qr\text{-cyclic convolution}
\xrightarrow{\text{double Mellin}}
\text{finite ordinary Dirichlet-}L(s+t)\text{ bundle}.
}
\tag{32}
\]

This is a classification/boundary result, not an RH bridge. It supplies no new Euler product, no source-derived self-adjoint zero operator, no positivity theorem, and no intrinsic mechanism selecting `Re(s)=1/2`.