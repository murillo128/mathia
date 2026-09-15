# PC-314 — Fourier-symmetrized canonical packet has off-critical zeros

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-NEGATIVE` for using the universal finite-Fourier eigensectors of PC-313 as an RH-like scalar repair after the canonical mixed-conductor Prime-Circle packet has already been compressed to one periodic coefficient sequence.

PC-313 showed that for every even periodic coefficient `d`, the universal symmetrizations

\[
a_+:=d+\mathcal F_Nd,
\qquad
a_-:=d-\mathcal F_Nd
\]

are finite-Fourier eigenvectors and therefore their completed periodic Dirichlet series satisfy scalar `+` and `-` Riemann-type functional equations. That result already showed that the functional equation itself is universal rather than Prime-Circle-specific, but it left open a weaker hope: perhaps the **canonical source-generated** eigensectors still have an unusually good zero set.

The smallest admissible canonical mixed pair `(q,r)=(5,7)` rules that out decisively. For both eigensectors, the periodic coefficient sequence is not of the exceptional form whose Dirichlet series is a Dirichlet polynomial times one Dirichlet `L`-function. A theorem of Saias and Weingartner then implies linearly many zeros in every fixed vertical strip sufficiently close to `Re(s)=1`, including strips lying strictly in `Re(s)>1`. Thus both exact scalar functional-equation sectors produced by the canonical Prime-Circle packet have infinitely many zeros **inside their half-plane of absolute convergence**, far to the right of the critical line.

This is stronger than saying that Fourier symmetrization is an arbitrary wrapper. In a fully source-native admissible instance, the wrapper provably produces scalar functions whose zero geometry is incompatible with an RH-type confinement statement.

## 1. The canonical `(5,7)` mixed coefficient

Take the canonical centered prime-support sources of PC-310--PC-312. For `q=5`,

\[
P_5=\{3\},
\]

so for every nonzero residue `h mod 5`,

\[
\widehat f_5(h)=e^{-2\pi i3h/5}.
\tag{1}
\]

For `r=7`,

\[
P_7=\{3,5\},
\]

and for every nonzero residue `j mod 7`,

\[
\widehat g_7(j)
=\frac12\left(e^{-2\pi i3j/7}+e^{-2\pi i5j/7}\right).
\tag{2}
\]

Put `N=35` and `zeta=e^{2\pi i/35}`. On the unit classes modulo `35`, the PC-312 positive-frequency coefficient

\[
c(k)=\widehat f_5(k)\overline{\widehat g_7(k)}
\]

therefore becomes

\[
\boxed{
c(k)=\frac12\left(\zeta^{-6k}+\zeta^{4k}\right).
}
\tag{3}
\]

The real even coefficient entering the two-sided Poisson pairing is

\[
d(k)=c(k)+c(-k),
\]

hence

\[
\boxed{
d(k)=\cos\frac{8\pi k}{35}+\cos\frac{12\pi k}{35}
\qquad ((k,35)=1).
}
\tag{4}
\]

Write

\[
d_1:=d(1),
\qquad d_2:=d(2).
\tag{5}
\]

PC-312 gives the normalized finite Fourier dual directly from the original source values:

\[
(\mathcal F_{35}d)(n)
=\sqrt{35}\,[
 f_5(-3n)g_7(3n)+f_5(3n)g_7(-3n)],
\tag{6}
\]

with residues taken in the appropriate moduli. Since

\[
f_5(3)=\frac45,
\qquad f_5(x)=-\frac15\quad(x\ne3),
\]

and

\[
g_7(3)=g_7(5)=\frac5{14},
\qquad g_7(y)=-\frac17\quad(y\notin\{3,5\}),
\]

equation (6) gives the exact values

\[
\boxed{
(\mathcal F_{35}d)(1)=-\frac{13\sqrt{35}}{70},
\qquad
(\mathcal F_{35}d)(2)=\frac{2\sqrt{35}}{35}.
}
\tag{7}
\]

Thus the two scalar functional-equation coefficients from PC-313 satisfy

\[
\boxed{
\begin{aligned}
a_\pm(1)&=d_1\mp\frac{13\sqrt{35}}{70},\\
a_\pm(2)&=d_2\pm\frac{2\sqrt{35}}{35}.
\end{aligned}}
\tag{8}
\]

No numerical approximation enters these identities.

## 2. A periodic `P(s)L(s,chi)` coefficient must have constant modulus on unit classes

Let `a` be any nonzero periodic sequence of period `N`, and suppose

\[
D_a(s):=\sum_{n\ge1}\frac{a(n)}{n^s}
=P(s)L(s,\chi),
\tag{9}
\]

where

\[
P(s)=\sum_{m\le M}b_m m^{-s}
\tag{10}
\]

is a Dirichlet polynomial and `chi` is a Dirichlet character. Comparing absolutely convergent Dirichlet coefficients in `Re(s)>1` gives

\[
a(n)=\sum_{\substack{m\mid n\\m\le M}}b_m\chi(n/m).
\tag{11}
\]

For every prime `ell>M` not dividing the conductor of `chi`, only the divisor `m=1` contributes, so

\[
\boxed{a(\ell)=b_1\chi(\ell).}
\tag{12}
\]

Now fix any unit class `u mod N`. Dirichlet's theorem supplies infinitely many primes `ell congruent u mod N`; after discarding finitely many primes dividing the conductor and those at most `M`, equation (12) and periodicity imply

\[
\boxed{|a(u)|=|b_1|\qquad((u,N)=1).}
\tag{13}
\]

If `b_1=0`, equation (13) says that all unit-class values vanish. Therefore a necessary condition for a periodic Dirichlet series to be a Dirichlet polynomial times one Dirichlet `L`-function is:

\[
\boxed{|a(u)|\text{ is constant on }(\mathbb Z/N\mathbb Z)^\times.}
\tag{14}
\]

This elementary criterion is only a necessary test; it is sufficient here because the canonical eigensectors fail it exactly.

## 3. Both canonical Fourier eigensectors fail the constant-modulus test exactly

The coefficients `a_+` and `a_-` are real. If either had equal modulus at the unit residues `1` and `2`, then

\[
a_\pm(1)^2-a_\pm(2)^2=0.
\tag{15}
\]

Using (8), write

\[
K:=\mathbb Q(\zeta_{35})
\]

and note that `d_1,d_2 in K`. A direct expansion gives

\[
\boxed{
a_\pm(1)^2-a_\pm(2)^2
=A\mp\frac{\sqrt{35}}{35}(13d_1+4d_2),
}
\tag{16}
\]

where

\[
A=d_1^2-d_2^2+\frac{153}{140}\in K.
\tag{17}
\]

The coefficient of `sqrt(35)` in (16) is nonzero. Indeed,

\[
d_1
=\cos\frac{8\pi}{35}+\cos\frac{12\pi}{35}
>\cos\frac\pi4
=\frac{\sqrt2}{2},
\tag{18}
\]

because `8pi/35<pi/4` and `12pi/35<pi/2`, while trivially `d_2>=-2`. Hence

\[
13d_1+4d_2
>\frac{13\sqrt2}{2}-8
>0.
\tag{19}
\]

Also

\[
\boxed{\sqrt{35}\notin K.}
\tag{20}
\]

A quick exact reason is ramification: the cyclotomic field `Q(zeta_35)` is ramified only at `5` and `7`, whereas `Q(sqrt(35))` has discriminant `140`, so `2` ramifies in that quadratic field. It therefore cannot be a subfield of `Q(zeta_35)`.

If (15) held, (16) with the nonzero coefficient (19) would force `sqrt(35) in K`, contradicting (20). Therefore

\[
\boxed{|a_\pm(1)|\ne|a_\pm(2)|.}
\tag{21}
\]

By the necessary condition (14), for **both signs**

\[
\boxed{
D_{a_\pm}(s)\ne P(s)L(s,\chi)
}
\tag{22}
\]

for every Dirichlet polynomial `P` and every Dirichlet character `chi`.

This is an exact algebraic certificate. The choice `(5,7)` is not a numerical search for a bad example; it is the smallest admissible pair of distinct primes in the canonical PC-310 source family.

## 4. Saias--Weingartner forces infinitely many zeros with `Re(s)>1`

Eric Saias and Andreas Weingartner, **Zeros of Dirichlet series with periodic coefficients**, *Acta Arithmetica* 140:4 (2009), 335--344, DOI `10.4064/aa140-4-4`, arXiv:`0807.0783`, prove the following classification consequence. If a periodic Dirichlet series `F_a(s)` is not of the exceptional form

\[
P(s)L(s,\chi),
\]

then there exists `eta=eta(a)>0` such that, for every

\[
\frac12<\sigma_1<\sigma_2<1+\eta,
\]

the number of zeros in

\[
\sigma_1<\Re s<\sigma_2,
\qquad |\Im s|\le T
\]

is bounded above and below by positive constant multiples of `T` for all sufficiently large `T`.

Applying this theorem to (22), there are positive `eta_+` and `eta_-` with this property for the two canonical eigensectors. In particular choose

\[
1<\sigma_1<\sigma_2<1+\eta_\pm.
\]

Then

\[
\boxed{
D_{a_+}\text{ and }D_{a_-}
\text{ each have infinitely many zeros with }\Re s>1.
}
\tag{23}
\]

These zeros lie in the ordinary half-plane of absolute convergence of the original Dirichlet series. No continuation artifact, gamma-factor pole, or boundary ambiguity is involved.

PC-313 simultaneously gives the exact scalar completed functional equations

\[
\Lambda_{a_+}(1-s)=\Lambda_{a_+}(s),
\qquad
\Lambda_{a_-}(1-s)=-\Lambda_{a_-}(s).
\tag{24}
\]

The completion factors are nonzero for `Re(s)>1`, so the zeros in (23) remain zeros of the completed eigensectors. Therefore these canonical source-generated functions provide an especially sharp internal control:

\[
\boxed{
\text{exact Riemann-type functional equation}
\not\Rightarrow
\text{critical-line zero confinement}.
}
\tag{25}
\]

Here the failure is not merely possible; it occurs with positive vertical density in strips strictly to the right of `Re(s)=1`.

## 5. Prior art and novelty audit

The zero theorem is classical and no novelty is claimed for it. Saias--Weingartner's 2009 theorem is the load-bearing prior-art result. Booker and Thorne, **Zeros of L-functions outside the critical strip**, *Algebra & Number Theory* 8:9 (2014), 2027--2042, DOI `10.2140/ant.2014.8.2027`, extends the same general philosophy to broader automorphic settings: absence of an Euler-product eigenform structure can force zeros in the region of absolute convergence. Nakamura's 2023 periodic-series constructions, already audited in PC-312, independently emphasize that Riemann-type functional equations exist well beyond zeta and Dirichlet `L`-functions.

The Mathia-specific contribution is narrower. Equations (1)--(8) derive the **actual canonical Prime-Circle** `(5,7)` coefficient and its finite-Fourier dual. Equations (13)--(22) then give an exact source-specific certificate that both PC-313 scalar eigensectors fall on the generic Saias--Weingartner side rather than the exceptional `P(s)L(s,chi)` side. The resulting off-critical zeros are therefore a theorem about this canonical Prime-Circle repair, not a heuristic analogy with Davenport--Heilbronn-type examples.

No historical novelty is claimed for periodic Dirichlet series, finite Fourier functional equations, Dirichlet's theorem, cyclotomic ramification, or the Saias--Weingartner zero-density result.

## 6. Boundary and falsification controls

The result is a decisive counterexample to a **general mechanism claim** about the universal Fourier symmetrization of PC-313. It does not assert that every pair of canonical primes `(q,r)` has the same zero distribution. One admissible source-native pair is sufficient to falsify the idea that the finite-Fourier eigensector construction itself enforces RH-like zero confinement.

The use of `(5,7)` is load-bearing only for the short exact coefficient certificate. A broader theorem for all `(q,r)` would require proving that their `a_+` and `a_-` sequences never fall into the exceptional `P(s)L(s,chi)` class; that stronger classification is not claimed here.

The Saias--Weingartner theorem is also load-bearing. If its exceptional-class statement were inapplicable to one of these periodic series, or if (22) failed, then the off-critical-zero conclusion would need withdrawal. Equations (9)--(22) isolate the exact checks needed to audit that bridge.

Finally, (23) says nothing negative about the individual classical Dirichlet `L`-components inside the PC-311 character expansion. It says that the **source-forced linear combination after universal Fourier eigensymmetrization** is not an RH surrogate.

## 7. Consequence for the Prime-Circle search

PC-312 and PC-313 can now be sharpened into a complete negative statement for the post-compression finite-Fourier repair:

\[
\text{canonical mixed Poisson packet}
\longrightarrow
\text{one periodic sequence }d
\longrightarrow
(d,\mathcal F_Nd)
\longrightarrow
 d\pm\mathcal F_Nd
\]

produces exact scalar functional equations, but those equations do not carry a critical-line mechanism. The smallest canonical mixed pair already yields infinitely many zeros in `Re(s)>1` in both scalar eigensectors.

Therefore a surviving Prime-Circle route cannot obtain its RH content merely by closing the compressed periodic packet under finite Fourier/Hurwitz duality. It must add source-forced structure **before** that universal compression or derive an independently constrained arithmetic/operator mechanism whose zero control is stronger than functional-equation symmetry alone.