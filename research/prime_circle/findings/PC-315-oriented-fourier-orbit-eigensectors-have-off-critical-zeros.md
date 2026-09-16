# PC-315 — oriented Fourier-orbit eigensectors have off-critical zeros

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-NEGATIVE` for retaining the orientation/chirality discarded by the even PC-311/PC-312 mixed-conductor packet and then closing its full finite-Fourier orbit into scalar functional-equation sectors.

PC-311 starts from the canonical two-prime Poisson coupling and introduces the positive-frequency coefficient

\[
c(k)=\widehat f_q(k\bmod q)\,\overline{\widehat g_r(k\bmod r)}
\]

before the two-sided real Poisson pairing replaces it by the even combination `d(k)=c(k)+c(-k)`. PC-312--PC-314 classify the scalar finite-Fourier repair of that even packet and show, for the smallest canonical mixed pair `(q,r)=(5,7)`, that both even Fourier eigensectors have infinitely many zeros in `Re(s)>1`.

A natural objection remains: the passage `c -> d` discards the oriented odd component before the universal Fourier/Hurwitz closure is applied. Perhaps the chirality already present in the positive-frequency packet supplies the missing source-native structure.

It does not. The odd component

\[
e:=c-c^\vee,\qquad c^\vee(k):=c(-k),
\]

has a two-dimensional Fourier orbit because `F_N^2=-I` on odd sequences. Its two canonical Fourier eigensectors

\[
b_{+i}:=e-i\mathcal F_Ne,
\qquad
b_{-i}:=e+i\mathcal F_Ne
\]

have eigenvalues `+i` and `-i`, so the classical periodic-Dirichlet-series transform gives each an exact scalar degree-one Riemann-type functional equation. For the same canonical `(5,7)` source used in PC-314, however, **both odd eigensectors are outside the exceptional `P(s)L(s,chi)` class**. Saias--Weingartner therefore forces linearly many zeros in strips lying strictly inside `Re(s)>1` for both of them.

Together with PC-314, this classifies **all four scalar eigensectors of the complete finite-Fourier orbit of the oriented canonical packet**: eigenvalues `+1,-1,+i,-i` all occur only through the universal finite-Fourier closure, and all four canonical `(5,7)` scalar sectors have infinitely many zeros in the half-plane of absolute convergence. Retaining orientation before the even symmetrization therefore does not rescue the post-PC-311 Fourier functional-equation route.

## 1. The unsymmetrized packet is the minimal orientation-preserving state

Let `q,r>3` be distinct primes, `N=qr`, and let `f_q,g_r` be the real centered canonical prime-support sources of PC-310--PC-312. With the unnormalized finite Fourier transforms used there, define

\[
\boxed{
 c(k):=\widehat f_q(k\bmod q)\,
       \overline{\widehat g_r(k\bmod r)}.
}
\tag{1}
\]

Centering gives

\[
c(k)=0\qquad\text{if }(k,N)>1,
\tag{2}
\]

and `c` is `N`-periodic. PC-311's real two-sided Poisson pairing uses

\[
d(k)=c(k)+c(-k).
\tag{3}
\]

The information discarded by (3) is exactly

\[
\boxed{
 e(k):=c(k)-c(-k).
}
\tag{4}
\]

Because the sources are real,

\[
c(-k)=\overline{c(k)},
\]

so `e` is purely imaginary and odd:

\[
\boxed{
 e(-k)=-e(k),
 \qquad
 \overline{e(k)}=-e(k).
}
\tag{5}
\]

No extra coefficient or chirality parameter has been inserted. Equation (4) is simply the complementary component of the already source-forced positive-frequency coefficient (1). It is therefore the minimal test of whether the orientation removed by the real Poisson contraction can change the PC-314 conclusion.

Use the normalized finite Fourier transform

\[
(\mathcal F_Na)(n)
:=\frac1{\sqrt N}\sum_{k\bmod N}
a(k)e^{-2\pi ink/N}.
\tag{6}
\]

For every sequence,

\[
\mathcal F_N^2a(k)=a(-k).
\tag{7}
\]

Hence on the odd subspace

\[
\boxed{
\mathcal F_N^2=-I.
}
\tag{8}
\]

The two odd Fourier eigensectors are therefore forced algebraically:

\[
\boxed{
 b_{+i}:=e-i\mathcal F_Ne,
 \qquad
 b_{-i}:=e+i\mathcal F_Ne,
}
\tag{9}
\]

and (8) gives

\[
\boxed{
\mathcal F_Nb_{+i}=i b_{+i},
\qquad
\mathcal F_Nb_{-i}=-i b_{-i}.
}
\tag{10}
\]

Thus retaining orientation enlarges the even `+/-1` sector of PC-313 to the full order-four Fourier representation; it does not yet create a source-dependent transform.

## 2. The finite Fourier dual of the odd component is an antisymmetric source tensor

PC-312 computes the Fourier transform of the positive-frequency coefficient before even symmetrization. Let

\[
\bar r\,r\equiv1\pmod q,
\qquad
\bar q\,q\equiv1\pmod r.
\tag{11}
\]

CRT and finite Fourier inversion give

\[
\boxed{
(\mathcal F_Nc)(n)
=\sqrt N\,
 f_q(-n\bar r\bmod q)
 g_r(n\bar q\bmod r).
}
\tag{12}
\]

Reflection of `c` exchanges the signs in the source tensor, so subtracting the two transforms gives

\[
\boxed{
(\mathcal F_Ne)(n)
=\sqrt N\Bigl[
 f_q(-n\bar r)g_r(n\bar q)
 -f_q(n\bar r)g_r(-n\bar q)
\Bigr].
}
\tag{13}
\]

For real sources the right side is real and odd, exactly as required by (8). Equation (13) is the oriented companion of PC-312's symmetrized source-tensor formula. The finite Fourier transform still merely exchanges the frequency-side product with a source-side CRT tensor; the only new information is the antisymmetric rather than symmetric combination.

This already gives the prior-art warning. A periodic coefficient and its finite Fourier transform are related by the classical Hurwitz functional transformation. For an odd coefficient, the relevant gamma factor is the standard odd degree-one factor, and a finite-Fourier eigenvector with eigenvalue `+i` or `-i` closes to a scalar functional equation. Ernvall-Hytönen--Odžak--Smajlović's finite-Fourier characterization covers exactly these even/odd eigenvector sectors. Thus (10) guarantees functional equations, but by itself says nothing about critical-line confinement.

## 3. Exact canonical `(5,7)` odd packet

Take the same smallest admissible canonical pair used in PC-314:

\[
q=5,\qquad r=7,\qquad N=35.
\tag{14}
\]

The prime-support sets are

\[
P_5=\{3\},
\qquad
P_7=\{3,5\}.
\tag{15}
\]

PC-314 derives, on the unit classes modulo `35`,

\[
 c(k)=\frac12\left(\zeta_{35}^{-6k}+\zeta_{35}^{4k}\right).
\tag{16}
\]

Therefore the oriented odd coefficient is

\[
\boxed{
 e(k)
 =i\left(
 \sin\frac{8\pi k}{35}
 -\sin\frac{12\pi k}{35}
 \right)
 \qquad ((k,35)=1),
}
\tag{17}
\]

and `e(k)=0` on the nonunits.

For the canonical centered source values,

\[
f_5(3)=\frac45,
\qquad
f_5(x)=-\frac15\quad(x\ne3),
\tag{18}
\]

and

\[
g_7(3)=g_7(5)=\frac5{14},
\qquad
g_7(y)=-\frac17\quad(y\notin\{3,5\}).
\tag{19}
\]

The inverses in (11) are

\[
\bar r=3\pmod5,
\qquad
\bar q=3\pmod7.
\tag{20}
\]

Substitution in (13) at `n=1` gives

\[
\begin{aligned}
(\mathcal F_{35}e)(1)
&=\sqrt{35}
\left[
 f_5(2)g_7(3)-f_5(3)g_7(4)
\right]\\
&=\sqrt{35}
\left[-\frac1{14}+\frac4{35}\right],
\end{aligned}
\]

hence

\[
\boxed{
(\mathcal F_{35}e)(1)=\frac{3\sqrt{35}}{70}.
}
\tag{21}
\]

At `n=2` the two source products coincide:

\[
f_5(4)g_7(6)
=f_5(1)g_7(1)
=\frac1{35},
\]

so

\[
\boxed{
(\mathcal F_{35}e)(2)=0.
}
\tag{22}
\]

Write

\[
u_1:=\sin\frac{8\pi}{35}-\sin\frac{12\pi}{35}
=-2\cos\frac{2\pi}{7}\sin\frac{2\pi}{35}<0,
\tag{23}
\]

and

\[
u_2:=\sin\frac{16\pi}{35}-\sin\frac{24\pi}{35}
=2\cos\frac{3\pi}{7}\sin\frac{4\pi}{35}>0.
\tag{24}
\]

Then

\[
e(1)=iu_1,
\qquad
e(2)=iu_2.
\tag{25}
\]

The following coarse rational intervals are enough and can be certified entirely by elementary alternating Taylor bounds:

\[
\boxed{
\frac{222}{1000}<|u_1|<\frac{223}{1000},
\qquad
\frac{156}{1000}<u_2<\frac{157}{1000},
\qquad
\frac{253}{1000}<\frac{3\sqrt{35}}{70}<\frac{254}{1000}.
}
\tag{26}
\]

For an explicit audit of the first two intervals, use

\[
\frac{333}{106}<\pi<\frac{355}{113}
\tag{27}
\]

and, for the positive angles occurring in (23)--(24), the alternating-series enclosures

\[
x-\frac{x^3}{6}+\frac{x^5}{120}-\frac{x^7}{5040}
<\sin x
<x-\frac{x^3}{6}+\frac{x^5}{120},
\tag{28}
\]

\[
1-\frac{x^2}{2}+\frac{x^4}{24}-\frac{x^6}{720}
+\frac{x^8}{40320}-\frac{x^{10}}{3628800}
<\cos x
<1-\frac{x^2}{2}+\frac{x^4}{24}-\frac{x^6}{720}
+\frac{x^8}{40320}.
\tag{29}
\]

They in fact give the tighter enclosures

\[
0.2226509<|u_1|<0.2226635,
\qquad
0.1563724<u_2<0.1564048.
\tag{30}
\]

The square-root bound in (26) follows already from `5.91^2<35<5.92^2`. Thus no floating-point assumption is load-bearing in what follows.

## 4. Both odd Fourier eigensectors fail the exceptional constant-modulus test

Put

\[
A:=\frac{3\sqrt{35}}{70}.
\tag{31}
\]

Equations (9), (21), (22), and (25) give

\[
\begin{aligned}
b_{+i}(1)&=i(u_1-A),
&b_{+i}(2)&=iu_2,\\
b_{-i}(1)&=i(u_1+A),
&b_{-i}(2)&=iu_2.
\end{aligned}
\tag{32}
\]

The signs in (23) and the certified intervals (26) imply `A>|u_1|`. Therefore

\[
|b_{+i}(1)|=A+|u_1|>\frac{475}{1000},
\tag{33}
\]

whereas

\[
|b_{-i}(1)|=A-|u_1|<\frac{32}{1000}.
\tag{34}
\]

At the second unit class,

\[
\boxed{
\frac{156}{1000}
<|b_{+i}(2)|=|b_{-i}(2)|
<\frac{157}{1000}.
}
\tag{35}
\]

Consequently

\[
\boxed{
|b_{+i}(1)|\ne|b_{+i}(2)|,
\qquad
|b_{-i}(1)|\ne|b_{-i}(2)|.
}
\tag{36}
\]

Now use the elementary necessary condition already isolated in PC-314. If a nonzero periodic Dirichlet series

\[
D_a(s)=\sum_{n\ge1}\frac{a(n)}{n^s}
\tag{37}
\]

has the exceptional form

\[
D_a(s)=P(s)L(s,\chi)
\tag{38}
\]

with a Dirichlet polynomial `P`, then comparison of absolutely convergent Dirichlet coefficients shows that, for all sufficiently large primes away from the conductor of `chi`,

\[
a(\ell)=b_1\chi(\ell).
\tag{39}
\]

Dirichlet's theorem in arithmetic progressions and periodicity of `a` then force

\[
\boxed{
|a(u)|=|b_1|
\quad\text{on every unit class }u
\text{ of any period of }a.
}
\tag{40}
\]

If `b_1=0`, all unit-class values must vanish. The exact mismatch (36) therefore proves, for both signs,

\[
\boxed{
D_{b_{+i}}(s)\ne P(s)L(s,\chi),
\qquad
D_{b_{-i}}(s)\ne P(s)L(s,\chi)
}
\tag{41}
\]

for every Dirichlet polynomial `P` and every Dirichlet character `chi`.

This is an exact source-specific certificate. It does not infer nonexceptionality from a numerical search or from genericity of Fourier eigenvectors.

## 5. Saias--Weingartner forces zeros in `Re(s)>1`

Saias and Weingartner, **Zeros of Dirichlet series with periodic coefficients**, *Acta Arithmetica* 140:4 (2009), 335--344, DOI `10.4064/aa140-4-4`, arXiv:`0807.0783`, prove that if a periodic Dirichlet series is not of the form `P(s)L(s,chi)`, then there exists `eta>0` such that for every

\[
\frac12<\sigma_1<\sigma_2<1+\eta
\tag{42}
\]

the number of zeros in

\[
\sigma_1<\Re s<\sigma_2,
\qquad |\Im s|\le T
\tag{43}
\]

is bounded above and below by positive constant multiples of `T` for sufficiently large `T`.

Applying that theorem to (41), each odd eigensector has its own `eta_\pm>0`. Choosing

\[
1<\sigma_1<\sigma_2<1+\eta_\pm
\]

gives

\[
\boxed{
D_{b_{+i}}
\text{ and }
D_{b_{-i}}
\text{ each have infinitely many zeros with }\Re s>1.
}
\tag{44}
\]

At the same time, (10) puts `b_{+i}` and `b_{-i}` in the odd finite-Fourier eigenclasses. The classical Hurwitz transformation therefore supplies the corresponding exact scalar degree-one functional equations, with the standard odd gamma factor and root number determined by the eigenvalue `+i` or `-i`. This is the odd analogue of PC-313's even `+/-1` closure.

The completion factors have no zeros in `Re(s)>1`, so the zeros in (44) remain zeros of the completed eigensectors. Thus the oriented sector gives the same decisive control as PC-314:

\[
\boxed{
\text{exact scalar Fourier/Hurwitz functional equation}
\not\Rightarrow
\text{critical-line zero confinement}.
}
\tag{45}
\]

Here again the failure occurs with positive vertical density in strips strictly to the right of `Re(s)=1`.

## 6. The full Fourier orbit of the canonical oriented packet is now closed

Let `R` denote reflection, `Ra(k)=a(-k)`. Since

\[
R=\mathcal F_N^2,
\tag{46}
\]

the source-generated oriented coefficient has the parity decomposition

\[
c=\frac12(d+e),
\qquad
d=c+Rc,
\qquad e=c-Rc.
\tag{47}
\]

The cyclic Fourier orbit

\[
\operatorname{span}\{c,\mathcal F_Nc,\mathcal F_N^2c,\mathcal F_N^3c\}
\tag{48}
\]

therefore decomposes into the four eigenspaces of `F_N`:

\[
\lambda\in\{+1,-1,+i,-i\}.
\tag{49}
\]

The `+1` and `-1` eigenvectors are exactly the even combinations

\[
d+\mathcal F_Nd,
\qquad
d-\mathcal F_Nd,
\tag{50}
\]

studied in PC-313/PC-314. The `+i` and `-i` eigenvectors are (9). PC-314 proves that both vectors in (50), for the canonical `(5,7)` source, lie outside the Saias--Weingartner exceptional class and have infinitely many zeros in `Re(s)>1`. Equations (41)--(44) prove the same statement for both odd vectors.

Hence, for the smallest canonical mixed conductor,

\[
\boxed{
\textbf{all four scalar finite-Fourier eigensectors of the oriented packet}
\textbf{ have infinitely many zeros in }\Re s>1.
}
\tag{51}
\]

This is stronger than the even-packet statement of PC-314. It rules out the objection that the bad zero geometry was an artifact of symmetrizing away chirality before the Fourier closure.

## 7. Prior-art and novelty audit

The ambient analytic mechanisms are classical and no theorem-level novelty is claimed for them.

- Anne-Maria Ernvall-Hytönen, Almasa Odžak and Lejla Smajlović, **On a class of periodic Dirichlet series with functional equation**, *Mathematical Communications* 25:1 (2020), 35--47, characterizes the relevant even/odd degree-one periodic Dirichlet series by finite-Fourier relations. Their finite Fourier discussion explicitly has eigenvalues `1,-1,i,-i`; the `+/-i` sectors used here are therefore standard odd Fourier eigensectors, not a new functional-equation mechanism.
- Saverio Salerno, Antonio Vitolo and Umberto Zannier, **Functional equations for Dirichlet series with periodic coefficients**, *Ricerche di Matematica* 40 (1991), 209--222, treats the general functional relation between periodic Dirichlet series and their finite transforms. This is the classical transform background for both PC-313 and the odd closure above.
- Eric Saias and Andreas Weingartner, **Zeros of Dirichlet series with periodic coefficients**, *Acta Arithmetica* 140:4 (2009), 335--344, DOI `10.4064/aa140-4-4`, arXiv:`0807.0783`, supplies the load-bearing zero theorem in Section 5.

The closest-prior-art audit therefore classicalizes both ingredients separately: finite-Fourier eigensectors automatically supply degree-one functional equations, while generic periodic series outside the single-`L` exceptional class have many zeros near and to the right of `Re(s)=1`.

The Mathia-specific consequence is narrower and exact. Equations (12)--(22) identify the **actual orientation-odd companion of the canonical PC-311 coefficient**, and (26)--(41) give a finite exact certificate that both of its Fourier eigensectors land on the generic Saias--Weingartner side. Together with PC-314 this closes the complete order-four Fourier orbit of the source-generated `(5,7)` packet. No claim is made that this specialization is historically novel outside the project.

A directed literature search across periodic Dirichlet series, odd/even finite-Fourier eigenvectors, and zeros of periodic-coefficient Dirichlet series found exactly these established general frameworks. Nothing in that literature changes the project-specific calculation, and no absence claim is needed.

## 8. Boundary, falsification controls, and research consequence

The exact route closed by this finding is

\[
\text{canonical positive-frequency mixed packet }c
\longrightarrow
\text{retain even and odd orientation sectors}
\longrightarrow
\text{close the finite-Fourier orbit}
\longrightarrow
\text{scalar Fourier eigensectors as RH surrogates}.
\tag{52}
\]

The result does **not** rule out source-forced structure that acts before the PC-311 same-index/Haar compression, a genuinely nonlinear interaction between separate prime-level indices, a pointed or shell-labelled matrix state not determined by the finite-Fourier orbit of `c`, a noncommutative source-dependent operator whose transform is not conjugate to the universal order-four Fourier action, or an independently proved zero-selection theorem using additional geometry. Those mechanisms change the information carrier rather than retaining one more parity component of the already periodic packet.

This finding should be revised or withdrawn if any of the following occurs:

1. equation (12), already used implicitly in PC-312, has a sign or normalization error;
2. the canonical `(5,7)` source values (18)--(19) are not the source convention of PC-310--PC-314;
3. the exact evaluations (21)--(22) fail;
4. the elementary rational interval certificate (26) is invalid;
5. the constant-modulus necessary condition (40) is not applicable to one of the periodic eigensectors;
6. the Saias--Weingartner exceptional-class theorem does not apply to these complex/purely-imaginary periodic coefficients;
7. the periodic-series functional-equation transform does not close a `+i` or `-i` finite-Fourier eigenvector in the stated odd degree-one class.

The first four items are finite exact checks; the last three are the explicit classical theorem bridges. Absent such a failure, the post-PC-311 universal finite-Fourier repair is now closed even when the orientation discarded by the real Poisson pairing is retained: **chirality enlarges the universal transform orbit from two scalar sectors to four, but it does not supply an RH-like zero-selection mechanism.**