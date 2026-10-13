# VIS-453 — the one-sided Farey quarter-mode spectrum retains orientation erased by signed aliasing

## Claim and evidence

Fix odd \(a\ge5\) and first take the fixed-\(a\) continuum/source-prime limit of the artificial reflected Farey transport from VIS-451. Its quarter-mode-conditioned positive-frequency weights are
\[
p_a(\ell)=a^{-1}f(\ell/a),\qquad
f(x)=\frac{(1-\cos 2\pi x)^2}{\pi^2x^2},\quad f(0)=0,\quad
\sum_{\ell\ge1}p_a(\ell)=1. \tag{1}
\]
For \(q\ge1\), retain the original positive orientation:
\[
\mu_{a,q}(r)=\sum_{\ell\ge1:\,\ell\equiv r\ (q)}p_a(\ell),
\quad r\in\mathbb Z/q\mathbb Z. \tag{2}
\]
VIS-452 proves that the **signed-folded** law
\(\nu_{a,q}(r)=\frac12[\mu_{a,q}(r)+\mu_{a,q}(-r)]\)
is exactly \(1/q\) whenever \(2q\le a\). The **unfolded** law need not be uniform, even asymptotically within that exact signed-uniform regime.

For \(c>0\), define the continuous, endpoint-periodic half-line periodization
\[
G_c(y)=c\sum_{n\ge0}f(c(n+y)),\qquad 0\le y\le1. \tag{3}
\]
It is a probability density on the unit circle, and for every admissible \(a,q,r\),
\[
\boxed{q\mu_{a,q}(r)=G_{q/a}(r/q).} \tag{4}
\]
For all \(0<c\le1/2\), the even full-line Poisson formula gives
\[
\boxed{G_c(y)+G_c(1-y)=2.} \tag{5}
\]
Thus folding cancels an **antisymmetric orientation signal**, not necessarily an aliasing error small in absolute variation.

If odd \(a\to\infty\), \(q=q(a)\in\mathbb N\), and \(q/a\to c\in(0,1/2)\), then
\[
\boxed{\operatorname{TV}(\mu_{a,q},U_q)\to
D(c)=\frac12\int_0^1|G_c(y)-1|\,dy>0.} \tag{6}
\]
Indeed, with
\[
A(c)=\frac2\pi\sum_{n=2}^\infty
\frac{(2c)^{2n-1}-2c^{2n-1}}{2n(2n-1)},\qquad 0<c<\tfrac12 ,
\tag{7}
\]
every summand is positive and
\[
\boxed{D(c)\ge\frac12 A(c)\ge\frac{c^3}{2\pi}.} \tag{8}
\]
There is also an **additional, sequential** fine-resolution limit:
\[
G_c(y)=1-\frac{4\pi^2}{3}c^3B_3(y)+O(c^5),
\quad B_3(y)=y^3-\frac32y^2+\frac12y, \tag{9}
\]
uniformly in \(y\in[0,1]\) as \(c\downarrow0\); hence
\[
\boxed{D(c)=\frac{\pi^2}{48}c^3+O(c^5).} \tag{10}
\]

**Evidence:** EXACT-DERIVED; CLASSICAL POISSON/FOURIER/BERNOULLI SPECIALIZATION; NEGATIVE REPRESENTATION CONTROL. The additional content relative to VIS-452 is the *one-sided* exact residue profile, its persistent mesoscopic nonuniformity while the folded law is exactly uniform, and the sharp cubic small-resolution law. Neither a novel general Fourier theorem, arithmetic ordering anomaly, nor RH implication is claimed.

## Derivation: exact periodization and mesoscopic limit

For \(r=0,\ldots,q-1\), write all positive indices in its residue class as \(r+nq\), \(n\ge0\). The extra zero term when \(r=0\) vanishes because \(f(0)=0\); inserting (1) proves (4). Since \(f\) is continuous, \(O(x^{-2})\) at infinity, and \(f(0)=0\), the series (3) converges locally uniformly for \(c>0\), agrees at \(y=0,1\), and integrates over successive cells to \(\int_0^\infty f=1\).

Extend \(f\) evenly. VIS-452 derived its exactly band-limited Fourier transform
\[
\widehat f(t)=2\Lambda(t)-\Lambda(t-1)-\Lambda(t+1),
\quad\Lambda(t)=(1-|t|)_+,\quad\widehat f(0)=2,
\tag{11}
\]
supported on \([-2,2]\) and zero at the endpoints. For \(c\le1/2\),
\[
c\sum_{n\in\mathbb Z}f(c(n+y))
=\sum_{j\in\mathbb Z}\widehat f(j/c)e^{2\pi i jy}
=\widehat f(0)=2. \tag{12}
\]
Evenness identifies this full-line sum with \(G_c(y)+G_c(1-y)\), proving (5) and independently recovering \(\nu_{a,q}=U_q\) for \(q/a\le1/2\).

If \(q/a\to c\in(0,1/2)\), then \(q\to\infty\). The common \(O(n^{-2})\) tail of (3) on compact positive-\(c\) intervals gives \(G_{q/a}\to G_c\) uniformly. Therefore the exact identity
\[
\operatorname{TV}(\mu_{a,q},U_q)
=\frac1{2q}\sum_{r=0}^{q-1}|G_{q/a}(r/q)-1|
\tag{13}
\]
converges by Riemann sums to (6). This by itself does not yet prove \(D(c)>0\).

## Derivation: a positive missing sine coefficient and the cubic profile

The first Fourier coefficient of (3) is the half-line transform
\[
\widehat G_c(1)=\int_0^\infty f(x)e^{-2\pi ix/c}\,dx. \tag{14}
\]
For \(c<1/2\), its real part is \(\widehat f(1/c)/2=0\) by (11). To compute its imaginary part, let \(\omega=2\pi/c>4\pi\) and
\[
J(\omega,b)=\int_0^\infty
\frac{(1-\cos bx)\sin(\omega x)}{x^2}\,dx .
\]
The cosine-difference/Frullani integral, with regularization if differentiating under the improper integral, gives
\[
J'(\omega,b)=\frac12\log(1-b^2/\omega^2),\quad
\lim_{\omega\to\infty}J(\omega,b)=0,\quad
J(\omega,b)=\sum_{n\ge1}\frac{b^{2n}}{2n(2n-1)\omega^{2n-1}}
\quad(\omega>b). \tag{15}
\]
Using \((1-\cos bx)^2=2(1-\cos bx)-\tfrac12(1-\cos2bx)\), with \(b=2\pi\), we obtain
\[
-\int_0^\infty f(x)\sin(\omega x)\,dx
=\frac{\frac12J(\omega,4\pi)-2J(\omega,2\pi)}{\pi^2}
=A(c)>0. \tag{16}
\]
The \(n=1\) terms cancel, while each \(n\ge2\) contribution in (7) is positive. Hence \(\widehat G_c(1)=iA(c)\neq0\). Testing a probability difference against the unit-modulus character \(e^{2\pi iy}\) gives \(2D(c)\ge|\widehat G_c(1)|\); retaining the first positive term of (7) yields (8).

More generally, \(\widehat G_c(j)=iA(c/j)\) for every \(j\ge1\). Since \(A(c/j)=O(j^{-3})\), the Fourier series converges absolutely and uniformly:
\[
G_c(y)=1-2\sum_{j\ge1}A(c/j)\sin(2\pi jy). \tag{17}
\]
The series (7) gives, uniformly for \(0<c\le c_0<1/2\),
\(A(c/j)=c^3/(\pi j^3)+O(c^5/j^5)\).
The classical Bernoulli identity
\[
\sum_{j\ge1}\frac{\sin(2\pi jy)}{j^3}
=\frac{2\pi^3}{3}B_3(y)
\]
proves (9). Finally \(B_3(y)=y(y-\frac12)(y-1)\) has opposite signs on the two halves of the unit interval, and \(\int_0^1|B_3(y)|\,dy=1/32\). Integrating the uniform error term proves (10).

## Controls, attribution, and limits

A direct positive-index sum to \(\ell=10^6\), independently compared with Fourier evaluation of (17), gives one-sided total variations approximately \(0.003547\) for \((a,q)=(101,25)\), \(0.009871\) for \((303,101)\), and \(0.056010\) for \((1001,490)\). All satisfy \(2q\le a\), so each signed-folded law is **exactly** uniform. The missing mass in each truncated direct sum is at most \(4a/(\pi^2 10^6)\), since \(p_a(\ell)\le4a/(\pi^2\ell^2)\). Separately, Fourier evaluation of the limiting profiles gives \(D(0.1)\simeq0.00020977\), \(D(1/3)\simeq0.00987224\), and \(D(0.49)\simeq0.05644738\), and the small-\(c\) ratio approaches \(\pi^2/48\simeq0.205617\). The exploratory plot of \(G_c\) exposed the reflection-odd profile; the proof rests on exact formulae, not visual appearance. No PNG is retained.

Poisson periodization, half-line sine/cosine transforms, and Bernoulli Fourier coefficients are classical; compare Stein and Shakarchi, *Fourier Analysis: An Introduction* (Princeton, 2003), and NIST DLMF §24.8(i), both already anchored in this line's SOURCES.md. The quantitative distinction here is a specialization to the **exact artificial** VIS-451 source law, not a new sampling or Euler–Maclaurin theorem.

The positive \(\ell\) indices, their artificial signed copies, and their residue quotients are **different observables**. Equations (6)–(10) concern the nested order: source-prime \(\to\infty\) at fixed odd \(a\), then \(a\to\infty\) with \(q/a\to c\), followed by \(c\downarrow0\) only for (9)–(10). They do not provide a uniform simultaneous prime/\(a\)/\(q\) limit. Such a transfer would need the finite transport approximation and the projected rare-sector stability budget of VIS-450.

## Research consequence

The exact signed-uniformity threshold of VIS-452 **cannot** be used to certify that an oriented positive-frequency null has no residue structure. Matching Farey spectra must fix sign folding, conditioning, modulus growth, and each model's own energy normalizer before labeling a residual arithmetic. This strengthens the representation-artifact warning for the accepted reflection/parity clue but leaves its source-natural order discriminator open. No genuine-Farey anomaly, Franel–Landau improvement, or RH consequence follows.
