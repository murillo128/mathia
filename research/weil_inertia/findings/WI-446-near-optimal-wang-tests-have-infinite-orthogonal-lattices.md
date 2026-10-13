# WI-446 — Near-optimal smooth Wang tests admit infinite orthogonal frequency lattices

**Status:** EXACT-DERIVED + CLASSICAL-POISSON-SPECIALIZATION + NEGATIVE/OBSTRUCTION + NO-NOVELTY-CLAIM + NON-RH

**Primary source:** Biao Wang, *Simple critical zeros and distinct zeros of the Riemann zeta function in short intervals*, arXiv:2609.07918v2, Proposition 4.1 (variational optimizer and admissible smooth approximation) and Proposition 5.1 (integer multiset inequality), https://arxiv.org/html/2609.07918v2.

**Local dependencies:** WI-442 (integer multiset inequality and real-only defect identity); WI-445 (sum-free Fourier zeros at Wang's *exact* optimizer, with a bounded-span stability gap).

## Exact statement

Fix \(0<\lambda\leq1\), put \(a=\lambda/2\), and use the Fourier convention
\[
\widehat f(\xi)=\int_{\mathbb R}f(u)e^{-2\pi i\xi u}\,du.
\]
Let
\[
f_\lambda(u)=
\frac{\cos(\sqrt2u)}{\sqrt2\sin(\lambda/\sqrt2)}
\mathbf1_{[-a,a]}(u),
\qquad
C(f)=\int f(u)^2\,du+
\iint |u-v|f(u)f(v)\,du\,dv,
\]
and \(C_\lambda=C(f_\lambda)=\lambda/2+
2^{-1/2}\cot(\lambda/\sqrt2)\).

**Theorem (near-optimal smooth orthogonal lattices).** For every
\(\varepsilon>0\) there exist a real even
\(\eta\in C_c^\infty((-a,a))\) with \(\int\eta^2=1\), and a period
\(p>0\), such that \(f=\eta^2\) satisfies
\[
\boxed{\quad 0<C(f)-C_\lambda<\varepsilon,\qquad
\widehat f(k/p)=0\quad(k\in\mathbb Z\setminus\{0\}).\quad}
\tag{1}
\]
Consequently \(\{e^{2\pi iju/p}:j\in\mathbb Z\}\) is an
**infinite orthonormal family** in \(L^2(\mathbb R,f(u)\,du)\).

For any finite number \(n\) of distinct real frequencies \(x_j=j/p\)
and any integer multiplicities \(m_j\in\{q,q+1\}\), \(q\geq1\),
the corresponding *real-only abstract finite multiset* attains exact
equality in Wang's Proposition 5.1:
\[
S=(2q+1)N-q(q+1)D,\qquad
D=n,\quad N=\sum_{j=1}^n m_j,\quad
S=\sum_{i,j=1}^n m_i m_j\widehat f(x_i-x_j)^2.
\tag{2}
\]
Thus the exact-optimizer prohibition of orthogonal real triples
(WI-445) has **no global counterpart uniform over all admissible
smooth near-minimizers and unbounded frequency spans**. This is a
finite-model obstruction, not a realization by zeta zeros.

## Construction and proof

**Step 1: positive smooth approximation.** As in Wang's Proposition
4.1, choose an even smooth cutoff \(\chi_\delta\), equal to one on
\([-a+\delta,a-\delta]\), and set
\[
\eta_0(u)=
\frac{\chi_\delta(u)\sqrt{f_\lambda(u)}}
{\left(\int\chi_\delta^2 f_\lambda\right)^{1/2}},
\qquad f_0=\eta_0^2.
\tag{3}
\]
Then \(\eta_0\in C_c^\infty((-a,a))\) is even,
\(\int f_0=1\), \(f_0\geq0\), and
\(\|f_0-f_\lambda\|_{L^2}\to0\) as \(\delta\downarrow0\).
There is a \(b>0\) such that \(f_0>0\) on \((-b,b)\).

**Step 2: flatten the periodization exactly.** For any \(0<p<2b\)
define the smooth \(p\)-periodic function
\[
G_p(u)=p\sum_{\ell\in\mathbb Z}f_0(u+\ell p).
\tag{4}
\]
Every residue class modulo \(p\) meets \((-b,b)\), so \(G_p>0\)
everywhere. Since \(f_0\) is even, \(G_p\) is even. Put
\[
\eta_p(u)=\frac{\eta_0(u)}{\sqrt{G_p(u)}},
\qquad f_p(u)=\eta_p(u)^2=\frac{f_0(u)}{G_p(u)}.
\tag{5}
\]
The test \(\eta_p\) remains real, even and compactly supported
smoothly inside \((-a,a)\).

By periodicity, a *pointwise* identity holds:
\[
p\sum_{\ell\in\mathbb Z} f_p(u+\ell p)
=\frac{p\sum_\ell f_0(u+\ell p)}{G_p(u)}=1.
\tag{6}
\]
Integrating over one period gives \(\int_{\mathbb R}f_p=1\),
so \(f_p=\eta_p^2\) is admissible without any further scaling.
For each integer \(k\), unfolding that same period gives
\[
\begin{aligned}
\widehat f_p(k/p)
&=\int_0^p e^{-2\pi iku/p}
    \sum_{\ell\in\mathbb Z}f_p(u+\ell p)\,du\\
&=\frac1p\int_0^p e^{-2\pi iku/p}\,du
=\mathbf1_{\{k=0\}} .
\end{aligned}
\tag{7}
\]
The exact reciprocal-lattice Fourier zeros therefore hold for
*all* nonzero integers \(k\), not just a prescribed finite range.

**Step 3: proximity to the unique optimizer.** Fourier-series
periodization (equivalently Poisson summation) gives
\[
G_p(u)=\sum_{k\in\mathbb Z}
\widehat f_0(k/p)\,e^{2\pi iku/p},
\qquad\widehat f_0(0)=1.
\tag{8}
\]
Because \(f_0\in C_c^\infty\), its Fourier transform decreases faster
than any inverse power. Hence for each fixed \(r\geq0\) and
\(M>0\),
\[
\|G_p-1\|_{C^r}=O_{f_0,r,M}(p^M)\qquad(p\downarrow0).
\tag{9}
\]
For fixed \(f_0\), this gives \(f_p\to f_0\) in \(L^2\)
and \(\eta_p\to\eta_0\) smoothly. Choose the cutoff \(\delta\)
first and the period \(p\) second: \(\|f_p-f_\lambda\|_2\)
can then be made arbitrarily small.

For \(h=f_p-f_\lambda\) (of integral zero), Wang's exact
variation identity states, with \(P(u)=\int_{-a}^{u}h(v)\,dv\),
\[
C(f_p)-C_\lambda=\|h\|_2^2-2\|P\|_2^2,
\quad
\left(1-\frac{2\lambda^2}{\pi^2}\right)\|h\|_2^2
\le C(f_p)-C_\lambda\le\|h\|_2^2 .
\tag{10}
\]
The strict positive lower bound follows because \(f_p\) is smooth
and cannot equal Wang's endpoint-discontinuous minimizer
\(f_\lambda\) almost everywhere. Taking \(\delta,p\) sufficiently
small proves (1).

**Step 4: finite-multiset equality.** For real distinct locations,
the exact identity in WI-442/WI-445 is
\[
\begin{aligned}
&S-(2q+1)N+q(q+1)D\\
&=\sum_j(m_j-q)(m_j-q-1)
+2\sum_{i<j}m_i m_j\widehat f(x_i-x_j)^2.
\end{aligned}
\tag{11}
\]
Take \(x_j=j/p\) and \(m_j=q\) or \(q+1\).
The first sum vanishes termwise by integrality, and the second
by (7). This proves (2), for arbitrary finite \(n\).
There is no claim that the selected frequencies obey the ordinate
spacing or arithmetic statistics of actual zeta zeros.

## Matched controls and exact boundary

**The exact optimizer is different.** WI-445 proves that
\(\widehat f_\lambda\) has a sum-free positive zero set, so at most
two real-frequency exponentials are mutually orthogonal for the
nonsmooth, unique minimizer. Equations (1) and (7) do not contradict
that statement: the cost approaches the optimal value while the
reciprocal lattice escapes to arbitrarily large frequency spacing
\(1/p\). In particular the family is *not* uniformly compact in
the frequency variables.

**The bounded-span result survives.** WI-445 gives a strictly
positive triple-overlap minimum for frequencies in every fixed
span \(R\), stable under a sufficiently close \(L^1\) smoothing.
Here the nearest distinct lattice frequencies are \(1/p\) apart.
For each fixed \(R\), sufficiently small \(p\) leaves no pair of
lattice frequencies within \(R\). Thus this example does **not**
disprove the compact packing bound or an improvement that has a
separate source-proved spatial-density hypothesis.

**Admissibility and exactness.** The positivity condition \(p<2b\)
prevents zero denominators; the evenness of \(f_0\) and \(G_p\)
preserves the even real test class; (6) proves exact probability
normalization; (7) is exact rather than an approximate numerical
cancellation. A falsification check may compute the periodization
and lattice Fourier coefficients for a fixed smooth cutoff, then
independently verify (10); the proof does not rely on numerics.

**Literature and novelty.** The minimizer, functional, and
smooth-test admissibility are Wang's source results, not Mathia's.
Periodization, Poisson summation, and vanishing of nonconstant
Fourier coefficients for a constant periodic function are classical
harmonic analysis; see, for example, E. M. Stein and R. Shakarchi,
*Fourier Analysis: An Introduction*, Princeton Lectures in
Analysis I (2003), for Fourier series and Poisson summation.
The only line-specific consequence assembled here is the
near-optimal admissible-smooth countermodel to a *uniform global*
extrapolation from WI-445. No original-method or priority claim
is made.

## Implication for Weil inertia and RH

This closes a specific potential shortcut: a theorem that uses
only Wang-window near-optimality, smoothness, nonnegativity and
compact support cannot assert a universal bound of two on the
size of orthogonal real-frequency families, nor a strictly
positive global Gram-defect floor for *arbitrary* configurations.
Any surviving coercivity must retain a quantitative spatial
packing constraint, source-fixed test family, or genuinely new
arithmetic information.

Wang's zeta application holds each admissible smooth test
fixed before taking \(T\to\infty\). The construction makes no
uniform assertion with \(p=p(T)\), supplies no information on
where the actual zeta frequencies lie, and does not address the
indefinite blocks arising from off-critical conjugate pairs.
It gives neither a sharper unconditional zero proportion
nor an individual off-line-defect certificate, and **does not
prove RH**.
