# NB-345 — Near common-divisibility dilations preserve the finite normalization residue

- **Status:** proved (author derivation; independent adversarial review pending)
- **Research line:** nyman_beurling
- **Depends on:** NB-304, NB-314, NB-334, NB-337, NB-338, NB-339, NB-344
- **Classification:** EXACT-DERIVED + SOURCE-SIDE + MOVING-NEAR-DIVISIBILITY + UNIFORM-IN-DILATION + FINITE-NORMALIZATION-RESIDUE + NON-TARGET-AWARE + PRIOR-ART-AUDITED

## Claim

For the canonical Nyman finite section and projected integer dilation, put
\[
U_n=\operatorname{span}\{g_2,\ldots,g_n\},\quad
T_{n,m}=P_{U_n}A_m|_{U_n},\quad E_{n,m}=\sqrt m\,T_{n,m}-R_n,\quad
\nu_q=g_q-\frac{q-1}{q}g_{q-1}.
\]
Let \(n\ge q\ge8\), \(a\ge2\) be integers and \(h\) be an integer with \(|h|\le q/2\). Define
\[
m=a q(q-1)+h,\qquad \mathcal F_{n;q,m}=\langle E_{n,m}g_2,\nu_q\rangle.
\]
Then, with a single absolute constant independent of \(a,n,q,h\),
\[
\boxed{
\left|m\mathcal F_{n;q,m}+\frac{\pi^2}{144}\right|
\le C\left[\frac1q+\frac{|h|}{q}
\log\left(\frac{e q^2}{\max(1,|h|)}\right)\right].
}\tag{1}
\]
In particular, for arbitrary integer sequences \(a_n\ge2\) and \(h_n=o(n/\log n)\), with \(m_n=a_n n(n-1)+h_n\),
\[
\boxed{
m_n\langle E_{n,m_n}g_2,\nu_n\rangle\longrightarrow-\frac{\pi^2}{144},
\qquad
\liminf_{n\to\infty}\frac{m_n\sqrt{\log n}}n\|E_{n,m_n}\|
\ge\frac{\pi^2}{144}\sqrt{\frac2{\log2}}>0.
}\tag{2}
\]
No upper growth bound on \(a_n\) is imposed: the result applies also when \(m_n\) grows faster than every polynomial. For \(q=n\), \(m_n\ge n^2\) for all sufficiently large \(n\). At \(h=0\) this recovers the leading exact-divisibility residue from NB-344; the new content is *uniform stability under nonzero, moving integer perturbations*, even at arbitrary dilation scales.

## Exact reduction and uniform Bernoulli error

The exact NB-338 adjacent-selector identity is
\[
q\mathcal F_{n;q,m}
=\frac{qu}{2}\sum_{k\ge1}(-1)^{k+1}[F(ku)-F(kv)],
\quad
u=\frac mq,\quad v=\frac m{q-1},\quad
c=\frac{q-1}{q},\quad cv=u,
\tag{3}
\]
where \(F(x)=\int_x^\infty(\{t\}-1/2)t^{-2}\,dt\). The present \(m\) satisfies \(u\ge 2(q-1)-1/2\ge q\), and \(v>u\), even if \(a\) diverges. The exact adjacent-cell selector is admissible for either sign of \(h\): writing \(m=dq+r\) with \(0\le r<q\) gives \(d\ge q\) and \(r\le d\).

Use the periodic Bernoulli expansion (NB-339), uniform across integer folds,
\[
F(x)=-\frac{B_2(x)}{2x^2}-\frac{B_3(x)}{3x^3}+O(x^{-4}),\quad x\ge1,
\]
and define the absolutely convergent series
\[
S_j(x)=\sum_{k\ge1}\frac{(-1)^{k+1}B_j(kx)}{k^j}\quad(j=2,3).
\]
NB-338 identifies \(S_2(x)=H-\mathfrak D(x)\), where
\[
H=\frac{\pi^2}{72},\qquad
\mathfrak D(x)=\sum_{k\ge1}\frac{\|kx\|_{\mathbb Z}^2}{k^2}.
\]
Substituting the Bernoulli expansion in (3) and summing the absolute errors yields
\[
q\mathcal F_{n;q,m}
=\frac q{4u}[c^2S_2(v)-S_2(u)]
+\frac q{6u^2}[c^3S_3(v)-S_3(u)]
+O(q/u^3).
\tag{4}
\]
All constants are absolute and the estimate makes no assumption that \(u/q\) is bounded. Multiply by \(m/q=u\):
\[
m\mathcal F_{n;q,m}
=\frac q4[c^2S_2(v)-S_2(u)]
+\frac q{6u}[c^3S_3(v)-S_3(u)]
+O(q/u^2).
\tag{5}
\]

## Moving integer phases

Because \(m=a q(q-1)+h\),
\[
u=a(q-1)+\frac hq,\quad
v=aq+\frac h{q-1},\quad
v-u=a+\frac{h}{q(q-1)}.
\tag{6}
\]
Thus the *relative* displacement modulo one is \(\delta=h/[q(q-1)]\), **independent of \(a\)**.

Two elementary estimates, also used in NB-337, are
\[
\mathfrak D(x)\ll|x|\quad(|x|\le1/2),\qquad
|\mathfrak D(x+\delta)-\mathfrak D(x)|
\ll|\delta|\log(e/|\delta|)\quad(0<|\delta|\le1/2).
\tag{7}
\]
For the first, split the defining sum at \(k=1/|x|\) and use
\(\|kx\|^2\le\min(k^2x^2,1/4)\). For the second, the periodic function
\(t\mapsto\|t\|_{\mathbb Z}^2\) is globally Lipschitz, so its \(k\)-th term
changes by at most \(C k^{-2}\min(k|\delta|,1)\); summing gives (7).
This avoids unjustified differentiation at rational cusps.

Periodicity and (6)--(7) imply
\[
|S_2(u)-H|\ll |h|/q,
\quad
|S_2(v)-S_2(u)|
\ll \frac{|h|}{q(q-1)}
\log\frac{e q(q-1)}{|h|},
\tag{8}
\]
with the second bound read as zero for \(h=0\). The periodic polynomial
\(B_3\) is globally Lipschitz; the \(1/k^3\) weights make \(S_3\) globally Lipschitz as well. Hence
\[
|c^3S_3(v)-S_3(u)|
\ll\frac1q+\frac{|h|}{q(q-1)}.
\tag{9}
\]
Since \(u\ge q\), the second term and remainder in (5) are \(O(1/q)\).
For its leading term, retain the exact normalization
\[
\frac q4(c^2-1)=-\frac12+\frac1{4q}.
\tag{10}
\]
Equations (8)--(10) give
\[
\begin{aligned}
m\mathcal F_{n;q,m}
&=-\frac12S_2(u)+O\left(\frac1q+q|S_2(v)-S_2(u)|\right)\\
&=-\frac H2+
O\left[\frac1q+\frac{|h|}{q}
\log\frac{e q^2}{\max(1,|h|)}\right].
\end{aligned}
\tag{11}
\]
As \(H/2=\pi^2/144\), this is (1). It is uniform in **arbitrarily large \(a\)**, because the periodic arguments differ only by an integer and a controlled \(\delta\), while all Bernoulli errors decrease as \(u\) grows. The hypothesis \(h_n=o(n/\log n)\) makes (11)'s error \(o(1)\) with \(q=n\), proving the first statement in (2).

## Physical Hilbert bound

For the genuine source and adjacent witness, NB-304 and NB-344 establish
\[
\|g_2\|_2=\frac{\sqrt{\log2}}2,\qquad
\|\nu_n\|_2^2\le
\frac{2H_{n-2}+1+\pi^2/18}{n^2}.
\]
Cauchy--Schwarz therefore gives
\[
\|E_{n,m}\|\ge
\frac{2n|\mathcal F_{n;n,m}|}
{\sqrt{\log2}\sqrt{2H_{n-2}+1+\pi^2/18}}.
\tag{12}
\]
Use (11) at \(q=n\) and \(H_{n-2}/\log n\to1\) to prove the second assertion in (2), with the exact constant from NB-344. This is the physical operator norm, not an unweighted coefficient proxy.

## Prior art, falsification, and scientific boundary

The fractional-part correlation and discrete Nyman semigroup are anchored by Báez-Duarte, Bagchi, Báez-Duarte--Balazard--Landreau--Saias, and Balazard--Martin in this line's SOURCES.md. Bernoulli primitives and the elementary modulus estimates are classical, with the exact selector/finite-expansion derivations recorded in NB-338 and NB-339. NB-344 proves the center point \(h=0\). The **line-local mathematical delta** is the explicit moving-neighborhood estimate (1) *uniform in the arbitrarily growing multiple*, with its physical consequence (2). A targeted structural literature comparison did not identify precisely this operator estimate; no bibliographic priority or independent novelty is claimed. No additional external theorem or SOURCES.md edit is needed.

The width \(o(n/\log n)\) is sufficient, not asserted optimal. For \(|h|\asymp n/\log n\), the right side of (1) is merely \(O(1)\); it cannot justify either convergence or a counterexample. Rational cusps forbid treating \(\mathfrak D\) as globally differentiable. A finite sign check using (3) and NB-344's integer harmonic-tail formula (with a direct one-cell integral for fractional starts) gives \(m\mathcal F\approx-0.06320,-0.06591,-0.06723\) at \(a=2,h=1,q=40,80,160\), compared with \(-\pi^2/144\approx-0.06854\). These checks are not the proof.

**RH boundary.** The estimate is on a selected operator/source-observer channel. It does not bound \(d_n=\operatorname{dist}(\mathbf1,U_n)\), force occupation by the actual first-free Ford datum, or control inverse-section conditioning or off-critical-zero contraction. Within the polynomial and specified superpolynomial windows NB-342/343 give stronger phase-routed source estimates; (1) instead survives *without any upper dilation cutoff* near divisibility centers. Even (2) yields only a decaying unweighted lower bound \(n/(m_n\sqrt{\log n})\), not a positive operator-norm gap or any implication for RH.

## Research consequence

The finite normalization residue at exact common multiples is **stable in a moving integer neighborhood**: failures of exact divisibility by offsets \(o(n/\log n)\) preserve its universal signed coefficient even for arbitrarily rapid dilation growth. This closes a robustness question for the NB-344 source mechanism; it does not supply the missing target-sensitive approximation-distance bridge.
