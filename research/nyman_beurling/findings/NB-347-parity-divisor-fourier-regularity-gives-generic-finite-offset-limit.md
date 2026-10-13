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


**Positive-measure source nonvanishing.** Put
\[
\mu=\frac{5\pi^2}{1152},\qquad
M_0^2=\frac{\pi^2(27200-521\pi^2)}{31334400},\qquad
p_0=\frac{\mu^2}{4M_0^2}>0.066.
\]
There is a measurable set \(\mathcal A\subset(-1/2,1/2)\) of
Lebesgue measure at least \(p_0\), consisting of differentiability
phases of \(\mathfrak D\), on which
\(\mathcal L(t)\le-\mu/2<0\). Hence **without assuming pointwise
nonvanishing** of the limit, for every \(t\in\mathcal A\), every
sequence of integers \(a_q\ge2\), and every \(n_q\ge q\),
\[
\boxed{\displaystyle
\liminf_{q\to\infty}\frac{m_q\sqrt{\log q}}q
\|E_{n_q,m_q}\|
\ge\frac{5\pi^2}{2304}\sqrt{\frac2{\log2}}>0.}
\tag{4a}
\]
This is a positive-measure statement, not an assertion of nonvanishing
at every irrational or almost every phase.


**Local two-sided essential range.** The finite almost-everywhere
coefficient is not locally essentially bounded: for **every**
nonempty open interval \(I\subset(-1/2,1/2)\),
\[
\boxed{\displaystyle
\operatorname*{ess\,sup}_{t\in I}\mathcal L(t)=+\infty,
\qquad
\operatorname*{ess\,inf}_{t\in I}\mathcal L(t)=-\infty.}
\tag{4b}
\]
Each strict level set \(\{t\in I:\mathcal L(t)>K\}\) and
\(\{t\in I:\mathcal L(t)<-K\}\) has positive measure for
every \(K>0\), interpreted at differentiability phases.
The statement is compatible with \(\mathcal L\in L^2\).

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

## Positive-measure phase certificate

The conditional nonzero-limit consequence (4) is realized on a
quantitatively positive measure of phases. The proof requires only
the exact Fourier energy above and the already-established physical
witness estimate; it does not require any assumed differentiability
at rational cusps.

By (1), \(\mathfrak D\) has mean \(H\) on the circle. It is even
and periodic, and direct evaluation gives
\[
\mathfrak D(1/2)=\frac14\sum_{\substack{k\ge1\\k\ {\rm odd}}}
\frac1{k^2}=\frac{\pi^2}{32},\qquad
\Delta:=\mathfrak D(1/2)-H=\frac{5\pi^2}{288}.
\tag{11a}
\]
Integrating by parts on \([-1/2,1/2]\), using the absolutely
continuous representative furnished by (2), shows
\[
\int_{-1/2}^{1/2} t\mathfrak D'(t)\,dt
=\mathfrak D(1/2)-H=\Delta,\qquad
\int_{-1/2}^{1/2}\mathcal L(t)\,dt
=-\frac{\Delta}{4}=-\mu.
\tag{11b}
\]

The full variance of the periodic profile also has a closed form:
\[
V:=\int_{-1/2}^{1/2}(\mathfrak D(t)-H)^2\,dt
=\frac1{2\pi^4}\sum_{j\ge1}\frac{\sigma_{\pm}(j)^2}{j^4}
=\frac{371\pi^4}{6609600}.
\tag{11c}
\]
To evaluate the absolutely convergent Dirichlet series, use
\(\sigma_{\pm}(2^a u)=(a-1)\tau(u)\) for \(u\) odd, as in (6).
At exponent \(4\), replacing the ordinary divisor-square Euler
factor at \(2\) multiplies
\(\zeta(4)^4/\zeta(8)\) by
\[
\frac{\sum_{a\ge0}(a-1)^2/16^a}
{\sum_{a\ge0}(a+1)^2/16^a}
=\frac{53}{68}.
\]
Parseval then gives (11c), including its exact normalization.

Expand the square of
\(\mathcal L=(\mathfrak D-H)/2-t\mathfrak D'/4\).
The cross term obeys
\[
\int_{-1/2}^{1/2}t(\mathfrak D-H)\mathfrak D'\,dt
=\frac{\Delta^2-V}{2}.
\]
The integration by parts is justified because
\((\mathfrak D-H)^2\) is absolutely continuous. Using
\(|t|\le1/2\) and the exact derivative energy (2) yields
\[
\begin{aligned}
\|\mathcal L\|_{L^2(-1/2,1/2)}^2
&=\frac{3V}{8}-\frac{\Delta^2}{8}
+\frac1{16}\int_{-1/2}^{1/2}t^2|\mathfrak D'(t)|^2\,dt\\
&\le \frac{3V}{8}-\frac{\Delta^2}{8}
+\frac1{64}\frac{\pi^2}{18}
=M_0^2.
\end{aligned}
\tag{11d}
\]
In particular the explicit \(M_0^2\) in the claim is positive;
numerically it is about \(0.006948\), while
\(\mu\) is about \(0.042837\).

Let \(A_0=\{t:\mathcal L(t)\le-\mu/2\}\), with the
inequality interpreted for the almost-everywhere weak derivative.
Since \(\int\mathcal L=-\mu\),
\[
\mu=-\int\mathcal L
\le\int_{A_0}|\mathcal L|+\frac\mu2
\le M_0\sqrt{|A_0|}+\frac\mu2.
\]
Thus \(|A_0|\ge\mu^2/(4M_0^2)=p_0>0.066\).
Intersecting \(A_0\) with the full-measure differentiability set
preserves the bound and defines \(\mathcal A\). Formulae (3)--(4)
now give (4a) for every \(t\in\mathcal A\), with the same freedom
in the dilation sequence as before. The proof does not determine
whether the exceptional zero set of \(\mathcal L\) has positive or
zero measure, and it supplies no target-approximation estimate.

## Every-interval two-sided essential blowup

Fix a nonempty open \(I\subset(-1/2,1/2)\) and \(K>0\).
Choose a **nonzero** reduced rational \(r=a/b\in I\) of
even denominator \(b\); such points are dense, as seen using
fractions with odd numerator and power-of-two denominator.
Keep this rational fixed. NB-336(2) proves the two-sided cusp
\[
\mathfrak D(r+s)-\mathfrak D(r)
=-\frac{|s|}{b}\log\frac1{|s|}+O_b(|s|).
\tag{11e}
\]
The \(H^1\) conclusion (2) gives absolute continuity, so
the fundamental theorem of calculus yields, for \(h\downarrow0\),
\[
\begin{aligned}
\frac1h\int_r^{r+h}\mathfrak D'(t)\,dt
&=-\frac1b\log\frac1h+O_b(1)\longrightarrow-\infty,\\
\frac1h\int_{r-h}^{r}\mathfrak D'(t)\,dt
&=+\frac1b\log\frac1h+O_b(1)\longrightarrow+\infty.
\end{aligned}
\tag{11f}
\]
Therefore, for any \(M>0\) and sufficiently small \(h\),
the right interval contains a positive-measure set where
\(\mathfrak D'<-M\), and the left interval contains one
where \(\mathfrak D'>M\). Otherwise the respective integral
average could not cross its strict threshold. The derivative
exists almost everywhere.

Since \(0\le\mathfrak D(t)\le\zeta(2)/4=\pi^2/24\) and
\(H=\pi^2/72\),
\[
\left|\frac{\mathfrak D(t)-H}{2}\right|
\le C_0:=\frac{\pi^2}{72}.
\tag{11g}
\]
Choose the intervals inside \(I\) and so short that
\(\operatorname{sgn}t=\operatorname{sgn}r\) and
\(|t|\ge|r|/2\). Take
\(M>8(K+C_0)/|r|\). On the above two positive-measure
sets, \(|t\mathfrak D'(t)/4|>K+C_0\), with opposite signs.
Consequently
\(\mathcal L(t)=(\mathfrak D(t)-H)/2-t\mathfrak D'(t)/4\)
exceeds \(K\) on one set and is below \(-K\) on the other
(the sides reverse when \(r<0\)). This proves (4b).

Combining (4b) with (4), for every \(C>0\) and every
open phase interval \(I\), a positive-measure subset
of its differentiability phases has
\[
\liminf_{q\to\infty}
\frac{m_q\sqrt{\log q}}q\,
\|E_{n_q,m_q}\|>C
\]
for **every** integer sequence \(a_q\ge2\) and every
\(n_q\ge q\) in (3). The phase \(t\) is fixed before
\(q\to\infty\). No common convergence onset in \(t\)
is asserted, nor any positive lower density of the
large-level sets as \(C\) grows. The derivation is a
source-side consequence of the fixed-rational NB-336
cusp and absolute continuity; it invokes no outside theorem
or unproved derivative interchange. The nearby
Balazard--Martin rational-singularity literature remains
a prior-art boundary, not an independent novelty claim.

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
remain genuine but exceptional. The coefficient is now proved
nonzero on a set of phases of measure at least 0.066, with a uniform
scaled physical-norm floor, without asserting almost-everywhere
nonvanishing. The finite coefficient is also locally essentially
unbounded of both signs in every open phase interval, furnishing
arbitrarily large normalized source coefficients on positive-measure
subsets while keeping the phase fixed. This is a source/observer
classification only: it supplies neither target occupation,
inverse-section conditioning, an asymptotic bound on
\(\operatorname{dist}(\mathbf1,U_n)\), nor an RH implication.
