# NB-347 — Parity-divisor Fourier regularity gives a generic finite rational-offset limit

- **Status:** proved (author derivation; independent adversarial review pending)
- **Research line:** nyman_beurling
- **Depends on:** NB-304, NB-338, NB-339, NB-344, NB-345, NB-346
- **Classification:** EXACT-DERIVED + SOURCE-SIDE + PARITY-DIVISOR-FOURIER + EXACT-SOBOLEV-ENERGY + ALMOST-EVERYWHERE-OFFSET-LIMIT + UNBOUNDED-DILATION-UNIFORMITY + NON-TARGET-AWARE + PRIOR-ART-AUDITED

## Claim

Let \(f(x)=\|x\|_{\mathbb Z}^2\) and retain the periodic Diophantine profile from NB-332--NB-346,
\[
\mathfrak D(x)=\sum_{k\ge1}\frac{f(kx)}{k^2},
\qquad H=\frac{\pi^2}{72}.
\]
Define the signed parity-divisor count
\[
\sigma_{\pm}(j)=\sum_{d\mid j}(-1)^d.
\]
Then the **absolutely and uniformly convergent** Fourier expansion and its weak derivative are
\[
\boxed{\displaystyle
\mathfrak D(x)=H+\frac1{\pi^2}\sum_{j\ge1}
 \frac{\sigma_{\pm}(j)}{j^2}\cos(2\pi jx),}
\tag{1}
\]
\[
\boxed{\displaystyle
\mathfrak D'(x)=-\frac2\pi\sum_{j\ge1}
 \frac{\sigma_{\pm}(j)}j\sin(2\pi jx)
 \quad\text{in }L^2(\mathbb T),\qquad
 \int_0^1|\mathfrak D'(x)|^2\,dx=\frac{\pi^2}{18}.}
\tag{2}
\]
Consequently \(\mathfrak D\in H^1(\mathbb T)\), has an absolutely continuous representative (the already-defined continuous function), and is differentiable at Lebesgue-almost-every phase. It need not be differentiable at rational cusps.

For **every** differentiability phase \(t\in(-1/2,1/2)\), let \(q\to\infty\) range over all positive integers, choose a nearest integer \(h_q\) to \(qt\), arbitrary integers \(a_q\ge2\), and arbitrary finite-section sizes \(n_q\ge q\). Define
\[
m_q=a_q q(q-1)+h_q,\quad
U_n=\operatorname{span}\{g_2,\ldots,g_n\},\quad
E_{n,m}=\sqrt m\,P_{U_n}A_m|_{U_n}-R_n,
\quad \nu_q=g_q-\frac{q-1}{q}g_{q-1},
\]
\[
\mathcal F_q=\langle E_{n_q,m_q}g_2,\nu_q\rangle.
\]
Then, with **no upper bound on the growth of \(a_q\) or \(n_q\)**,
\[
\boxed{\displaystyle
m_q\mathcal F_q\longrightarrow
\mathcal L(t):=-\frac12[H-\mathfrak D(t)]
-\frac t4\mathfrak D'(t).}
\tag{3}
\]
Thus the normalized adjacent source coefficient is finite for almost every limiting offset, in contrast to the logarithmic divergence at fixed even-denominator rational offsets in NB-346. If \(\mathcal L(t)\ne0\), NB-304's physical-norm certificate further gives
\[
\boxed{\displaystyle
\liminf_{q\to\infty}
\frac{m_q\sqrt{\log q}}q\,\|E_{n_q,m_q}\|
\ge\sqrt{\frac2{\log2}}\,|\mathcal L(t)|>0.}
\tag{4}
\]
This does **not** assert that \(\mathcal L(t)\ne0\) for every differentiability phase.

## Parity-divisor spectrum and exact Sobolev energy

NB-339(5) records the classical absolutely convergent Fourier series
\[
f(x)=\frac1{12}+\frac1{\pi^2}
\sum_{\ell\ge1}\frac{(-1)^\ell\cos(2\pi\ell x)}{\ell^2}.
\tag{5}
\]
The doubly indexed series obtained by inserting (5) into
\(\sum_{k\ge1}k^{-2}f(kx)\) is absolutely summable. Collecting the
frequency \(j=k\ell\) gives (1), since \(1/(k^2\ell^2)=1/j^2\).
The constant is \(\zeta(2)/12=H\). No differentiation of a conditionally
convergent series is used.

Write \(j=2^a u\) with \(u\) odd, \(a\ge0\). There are \(\tau(u)\)
odd divisors and \(a\tau(u)\) even divisors, so
\[
\sigma_{\pm}(2^a u)=(a-1)\tau(u).
\tag{6}
\]
The standard Euler product, here used only for an absolutely
convergent sum at \(s=2\), is
\[
\sum_{j\ge1}\frac{\tau(j)^2}{j^s}
 =\frac{\zeta(s)^4}{\zeta(2s)},\qquad s>1.
\]
At the prime \(2\), the local factor is
\(\sum_{a\ge0}(a+1)^2/4^a=80/27\); replacing it using (6) gives
\(\sum_{a\ge0}(a-1)^2/4^a=32/27\). Therefore
\[
\begin{aligned}
\sum_{j\ge1}\frac{\sigma_{\pm}(j)^2}{j^2}
&=\frac{32}{80}\frac{\zeta(2)^4}{\zeta(4)}
 =\frac{\pi^4}{36}<\infty.
\end{aligned}
\tag{7}
\]
The coefficient sequence of the formal derivative of (1) is therefore
square summable. Fourier--Sobolev theory yields the derivative series
in \(L^2\), and Parseval gives
\[
\|\mathfrak D'\|_{L^2(\mathbb T)}^2
=\frac2{\pi^2}\sum_{j\ge1}\frac{\sigma_{\pm}(j)^2}{j^2}
=\frac{\pi^2}{18}.
\]
In one dimension \(H^1(\mathbb T)\) has an absolutely continuous
representative and almost-everywhere ordinary derivative, proving (2).
The exact norm is a property of the intrinsic arithmetic phase profile,
not a Nyman target norm.

## Uniform moving-offset reduction

Put \(t_q=h_q/q\), \(c=(q-1)/q\), and
\[
u=\frac{m_q}{q}=a_q(q-1)+t_q,\qquad
v=\frac{m_q}{q-1}=a_q q+t_q+\frac{t_q}{q-1}.
\]
Modulo integers, their phases are \(t_q\) and
\(t_q+\delta_q\), with \(\delta_q=t_q/(q-1)\), independent of \(a_q\).
For \(|t|<1/2\) and large \(q\), \(|h_q|\le q/2\) and \(u\ge q\),
so the exact adjacent selector and Bernoulli expansion of NB-345 apply.
With its \(S_2=H-\mathfrak D\) and globally Lipschitz periodic \(S_3\),
equation NB-345(5) reads
\[
m_q\mathcal F_q
=\frac q4[c^2S_2(v)-S_2(u)]
+\frac q{6u}[c^3S_3(v)-S_3(u)]
+O(q/u^2).
\tag{8}
\]
Here \(v-u=a_q+\delta_q\). The \(S_3\) difference is \(O(q^{-1})\);
its contribution and the last error are \(O(q^{-1})\) uniformly over
all \(a_q\ge2\), \(n_q\ge q\), and \(t\in(-1/2,1/2)\).

Retain the finite normalization \(q(c^2-1)/4=-1/2+1/(4q)\).
The global modulus from NB-337,
\[
|\mathfrak D(x+s)-\mathfrak D(x)|
\ll |s|\log(e/|s|),\quad |s|\le1/2,
\]
controls the \(c^2\)-to-\(1\) replacement uniformly, yielding
\[
\boxed{\displaystyle
m_q\mathcal F_q
=-\frac q4[\mathfrak D(t_q+\delta_q)-\mathfrak D(t_q)]
-\frac12[H-\mathfrak D(t_q)]
+O\!\left(\frac{\log(2q)}q\right).}
\tag{9}
\]
The implied constant is absolute, independent of \(a_q,n_q,t\).
In particular the formula remains valid for superpolynomial and
factorial-size dilations, just as NB-345--NB-346 require.

If \(\mathfrak D\) is differentiable at \(t\), then
\[
t_q-t=O(q^{-1}),\quad
\delta_q=\frac tq+O(q^{-2}),\quad
\mathfrak D(t+s)=\mathfrak D(t)+s\mathfrak D'(t)+o(|s|).
\]
Apply the last expansion separately at
\(s=t_q+\delta_q-t\) and \(s=t_q-t\), both \(O(q^{-1})\).
Subtracting gives
\[
q[\mathfrak D(t_q+\delta_q)-\mathfrak D(t_q)]
\longrightarrow t\mathfrak D'(t),
\]
even though \(t_q\) itself varies over rational grid points. By
continuity \(\mathfrak D(t_q)\to\mathfrak D(t)\), and (9) proves (3).

A useful unsampled control is the strong mean-square limit
\[
q\left[\mathfrak D\!\left(t+\frac{t}{q-1}\right)
-\mathfrak D(t)\right]
\longrightarrow t\mathfrak D'(t)
\quad\text{in }L^2(-1/2,1/2).
\tag{10}
\]
Indeed absolute continuity represents the quotient as
\[
\frac q{q-1}t\int_0^1
\mathfrak D'\!\left(\left(1+\frac{s}{q-1}\right)t\right)\,ds.
\]
Composition with these near-identity affine maps is uniformly
\(L^2\)-bounded on the interval and converges strongly to the identity
for each \(L^2\) function, first for continuous functions and then by
density. Thus (10) independently checks the generic finite-scale
interpretation; it is **not** an assertion of \(L^2\) convergence for
the discontinuously rounded sampled phases \(t_q\).

## Physical norm, boundary checks, and novelty

NB-304 supplies
\[
\|g_2\|_2=\frac{\sqrt{\log2}}2,\qquad
\|\nu_q\|_2^2\le
\frac{2H_{q-2}+1+\pi^2/18}{q^2}.
\]
Consequently
\[
\|E_{n_q,m_q}\|\ge
\frac{2q|\mathcal F_q|}
{\sqrt{\log2}\sqrt{2H_{q-2}+1+\pi^2/18}},
\]
and \(H_{q-2}/\log q\to1\) proves (4). If
\(\mathcal L(t)=0\), the inequality yields no positive floor. It is
not a bound for the Nyman--Beurling approximation distance.

Two sharp controls rule out a uniform-in-phase reading of (3).
At fixed reduced **even-denominator rational** \(t=p/B\),
the NB-336 cusp makes the coefficient grow as
\(|p|\log q/(4B^2)\) when \(B\mid q\), by NB-346.
At reduced **odd-denominator rational** phases the NB-339 term
\((\log2/B)|s|\) yields distinct one-sided derivatives, so (3)
cannot be applied merely by inserting a formal Fourier derivative.
At \(t=0\), rounding gives \(h_q=0\) and the separate exact-divisibility
limit \(-H/2=-\pi^2/144\) from NB-344, despite the cusp there.
The almost-everywhere quantifier cannot be promoted to every
irrational phase without additional Diophantine analysis.

As an arithmetic consistency check, the finite sum
\(\sum_{j\le200000}\sigma_{\pm}(j)^2/j^2\) is approximately
\(2.70510018\), approaching the exact value
\(\pi^4/36\approx2.70580808\). This tests the sign, parity, and
normalization in (6)--(7), but the proof is the Euler-product
calculation and Parseval.

The Fourier series for \(f\) is already present in NB-339. Nearby
primary literature includes Balazard--Martin, *Sur l'autocorrélation
multiplicative de la fonction partie fractionnaire et une fonction
définie par J. R. Wilton*, arXiv:1305.4395 (differentiability and
divisor-weighted fractional-part series), and Patkowski,
*A generalized Davenport expansion*, Proc. Edinburgh Math. Soc.
(2021), DOI 10.1017/S0013091521000468 (related Davenport-type
Fourier expansions). These are prior-art boundaries, **not**
theorems invoked to prove (1)--(4), and no bibliographic priority
or independence claim is made. All load-bearing ingredients are
classical Fourier/Sobolev identities or exact local NB derivations;
no SOURCES.md extension is required.

## Research consequence

NB-346's even/odd rational dichotomy is not a generic dichotomy
between all arithmetic and non-arithmetic offsets. The intrinsic
profile has an **exact finite Sobolev derivative energy**, and the
physical adjacent operator coefficient has a finite explicit
normalized limit at almost every irrational limiting offset, with
no cap on the dilation multiple. Rational logarithmic resonances
remain genuine but exceptional. This is a source/observer
classification only: it supplies neither target occupation,
inverse-section conditioning, an asymptotic bound on
\(\operatorname{dist}(\mathbf1,U_n)\), nor an RH implication.
