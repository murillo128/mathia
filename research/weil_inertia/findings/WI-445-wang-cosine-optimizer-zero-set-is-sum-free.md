# WI-445 — Wang's cosine optimizer has sum-free Fourier zeros and forbids orthogonal real triples

**Status:** EXACT-DERIVED + PRIMARY-SOURCE-SPECIALIZATION + FINITE-GRAM-OBSTRUCTION + PRIOR-ART-AUDIT + NON-RH + NO-NOVELTY-CLAIM

**Primary source:** Biao Wang, *Simple critical zeros and distinct zeros of the Riemann zeta function in short intervals*, arXiv:2609.07918v2 (6 October 2026), Proposition 4.1 and Proposition 5.1, https://arxiv.org/html/2609.07918v2.

**Local mathematical dependency:** WI-442 (the exact real-multiset specialization of Wang's integer rank/trace defect). This finding addresses the zero geometry of Wang's *specific optimizing Fourier kernel*, not arbitrary compactly supported kernels or the full off-critical indefinite form.

## Claim

For every fixed \(0<\lambda\leq1\), let
\[
a=\lambda/2,\qquad c=\lambda/\sqrt2\in(0,1/\sqrt2],\qquad
f_\lambda(u)=\frac{\cos(\sqrt2u)}{\sqrt2\sin c}\mathbf1_{[-a,a]}(u),
\qquad K_\lambda(\xi)=\int f_\lambda(u)e^{-2\pi i\xi u}\,du.
\tag{1}
\]
Wang's Proposition 4.1 identifies \(f_\lambda\) as the unique normalized real \(L^2\) optimizer of its pair-energy functional. It is positive on its support, integrates to one, and its transform is real and even on the real axis.

**Exact zero-set rigidity.** Write \(t=\pi\lambda\xi\) and \(b=c\tan c>0\). The positive real zeros of \(K_\lambda\) are precisely
\[
t_k=k\pi+\delta_k\quad (k=1,2,\ldots),\qquad
0<\delta_k<\pi/2,\qquad
(k\pi+\delta_k)\tan\delta_k=b,
\tag{2}
\]
where the root \(\delta_k\) is unique and \(\delta_{k+1}<\delta_k\). They are **sum-free**: for all \(m,n\geq1\),
\[
K_\lambda\!\left(\frac{t_m+t_n}{\pi\lambda}\right)\ne0.
\tag{3}
\]
Consequently no three distinct real points \(x_1,x_2,x_3\) can have all three Gram overlaps \(K_\lambda(x_i-x_j)\) equal to zero. An orthogonal family of real-frequency exponentials in \(L^2(f_\lambda(u)\,du)\) contains at most **two** members. This maximum is attained: choose two frequencies separated by any positive zero.

**Finite packed-triple rigidity.** For every fixed \(R>0\),
\[
\kappa_{\lambda,R}:=
\min_{\substack{r,s\geq0\\r+s\leq R}}
\big(K_\lambda(r)^2+K_\lambda(s)^2+K_\lambda(r+s)^2\big)>0.
\tag{4}
\]
For \(n\) ordered distinct real locations \(x_1<\cdots<x_n\), with span \(X=x_n-x_1\), one therefore has
\[
\boxed{\quad
\sum_{i<j} K_\lambda(x_j-x_i)^2
\ \geq\ \frac{\kappa_{\lambda,R}}3
\big(n-2-2X/R\big)_+.\quad}
\tag{5}
\]
This gives a strictly positive extensive Gram charge in regimes with sufficiently many real points per unit span; it is *not* uniform over configurations allowed to spread arbitrarily far apart.

## 1. Explicit Fourier transform and exclusion of a removable root

Put \(\beta=2\pi\xi\), \(t=\beta a\), and \(c=\sqrt2a\). Direct integration of the cosine product yields, initially when \(\beta^2\ne2\),
\[
K_\lambda(\xi)=
\frac{2\beta\cos c\,\sin t-2\sqrt2\sin c\,\cos t}
 {(\beta^2-2)\sqrt2\sin c}.
\tag{6}
\]
At \(\beta=\pm\sqrt2\), the singularity in (6) is removable, and
\[
K_\lambda(\pm\sqrt2/(2\pi))
=\frac1{\sqrt2\sin c}\int_{-a}^a\cos^2(\sqrt2u)\,du>0.
\tag{7}
\]
In particular the apparent solution \(t=c\) of the numerator equation is **not a zero** of the Fourier transform. Also \(K_\lambda(0)=1\).

At any other possible zero with \(\xi>0\), the numerator of (6) vanishes. Since \(0<c<\pi/2\), the equation cannot hold where \(\cos t=0\), and division gives
\[
\beta\tan t=\sqrt2\tan c,\quad\text{equivalently}\quad
t\tan t=c\tan c=b.
\tag{8}
\]
On \((0,\pi/2)\), \(t\tan t\) increases strictly from zero to infinity; its unique solution is \(t=c\), already excluded by (7). On every interval \((k\pi,k\pi+\pi/2)\), \(k\geq1\), the left side of (8) again increases strictly from zero to infinity and gives exactly one solution \(t_k\). On the intervening half-periods it is negative; no other positive roots exist.

For \(k\geq1\), the function \(F_k(\delta)=(k\pi+\delta)\tan\delta\) increases strictly for \(0<\delta<\pi/2\), while \(F_{k+1}(\delta)>F_k(\delta)\). Therefore the unique roots of \(F_k(\delta_k)=b\) satisfy \(\delta_{k+1}<\delta_k\).

## 2. Sum-freeness and the precise equality obstruction

For positive roots \(t_m,t_n\),
\[
t_m+t_n=(m+n)\pi+(\delta_m+\delta_n),
\qquad 0<\delta_m+\delta_n<\pi.
\tag{9}
\]
If \(\delta_m+\delta_n\geq\pi/2\), this sum lies outside the positive-root half of the relevant period (including its nonzero midpoint). Otherwise it lies in \(((m+n)\pi,(m+n+1/2)\pi)\), but
\[
\delta_m+\delta_n>\delta_{m+n},
\tag{10}
\]
since each \(\delta_k>0\) and the sequence decreases. Thus it cannot coincide with the only root \(t_{m+n}\) in that half-period. This proves (3).

For \(x_1<x_2<x_3\), set \(r=x_2-x_1>0\), \(s=x_3-x_2>0\). Pairwise orthogonality of the corresponding exponentials is exactly \(K_\lambda(r)=K_\lambda(s)=K_\lambda(r+s)=0\), which contradicts (3).

To connect this result to Wang's integer-multiset bound, let \(m_i\geq1\) be the multiplicities of distinct real locations \(x_i\); write \(N=\sum m_i\), \(D=n\), and \(S=\sum_{i,j}m_im_jK_\lambda(x_i-x_j)^2\). For every integer \(q\geq1\), direct diagonal/off-diagonal expansion gives the *exact* identity
\[
\boxed{\quad
S-(2q+1)N+q(q+1)D
=\sum_i(m_i-q)(m_i-q-1)
+2\sum_{i<j}m_im_jK_\lambda(x_i-x_j)^2.\quad}
\tag{11}
\]
Both contributions on the right are nonnegative (integer \(m_i\)). Equality requires every multiplicity in \(\{q,q+1\}\) and every pairwise Fourier overlap to vanish. By (3), **equality is impossible for \(D\geq3\)** at the exact cosine optimizer, while one- and two-location examples attain equality with allowed multiplicities and a positive Fourier zero. This sharpens the *finite real-only equality characterization* already implicit in WI-442 without claiming any new unconditional zeta proportion.

## 3. Uniform three-point gap at bounded span

The summands defining \(\kappa_{\lambda,R}\) are continuous on the compact triangle \(\{(r,s):r,s\geq0,\ r+s\leq R\}\). They cannot all vanish, since for \(r=0\) or \(s=0\) a term is \(K_\lambda(0)^2=1\), and for positive \(r,s\) their simultaneous vanishing contradicts the sum-free zero set. Hence (4) is strictly positive.

For \(x_1<\cdots<x_n\), put \(d_i=x_{i+2}-x_i\) for \(1\leq i\leq n-2\). Every adjacent gap contributes to at most two of these spans, so
\[
\sum_{i=1}^{n-2}d_i\leq2X.
\tag{12}
\]
There are at most \(2X/R\) starting indices with \(d_i>R\), leaving at least \((n-2-2X/R)_+\) good consecutive triples. Greedily selecting the leftmost remaining good triple and discarding its at-most-two later overlapping starts gives at least one disjoint triple for every three good starts. Each selected triple contributes at least \(\kappa_{\lambda,R}\) to the distinct unordered pair sum, and disjoint triples spend no pair twice. This proves (5), including the \(n<3\) convention where the right side is zero.

Because \(m_i m_j\geq1\), (11) and (5) also imply the finite integer defect bound
\[
\boxed{\quad
S-(2q+1)N+q(q+1)D\geq
\sum_i(m_i-q)(m_i-q-1)+
\frac{2\kappa_{\lambda,R}}3(n-2-2X/R)_+.\quad}
\tag{13}
\]
The inequality is meaningful only when the distribution of *real* locations supplies an independently established density/packing input. It cannot be applied to a conjugation-invariant complex divisor by discarding the off-line indefinite blocks.

## 4. Stability for source-admissible smooth windows

Wang's optimizer (1) is not itself smooth across its support endpoints. The source's Proposition 4.1 constructs real, even, nonnegative, normalized \(C_c^\infty\) probability densities \(f_\varepsilon=\eta_\varepsilon^2\) on the same interval such that
\(\|f_\varepsilon-f_\lambda\|_{L^1}\to0\). Fourier transforms then satisfy, uniformly for real \(\xi\),
\[
|K_\varepsilon(\xi)-K_\lambda(\xi)|
\leq\|f_\varepsilon-f_\lambda\|_1=:\epsilon_\varepsilon.
\tag{14}
\]
Both transforms have absolute value at most one, so the squared three-overlap sum changes by at most \(6\epsilon_\varepsilon\). Consequently for each fixed \(\lambda,R\) and sufficiently small fixed \(\varepsilon\),
\[
\min_{r,s\geq0,\ r+s\leq R}
\big(K_\varepsilon(r)^2+K_\varepsilon(s)^2+
K_\varepsilon(r+s)^2\big)
\geq\kappa_{\lambda,R}/2>0.
\tag{15}
\]
Thus **the bounded-span packing obstruction survives smooth approximation**. This does not imply global sum-freeness of every perturbed kernel, nor does it justify a \(T\)-dependent approximation in Wang's short-interval theorem. The original zeta passage first holds a smooth test fixed as \(T\to\infty\), then takes approximation/support limits.

## 5. Controls, prior art, and RH boundary

**Rectangular-window falsification control.** A uniform probability density on \([-\lambda/2,\lambda/2]\) has Fourier transform \(K_{\rm box}(\xi)=\sin(\pi\lambda\xi)/(\pi\lambda\xi)\), whose nonzero real zeros lie at \(k/\lambda\), \(k\in\mathbb Z\setminus\{0\}\). These zeros *are* closed under appropriate sums, and the frequencies \(j/\lambda\) form arbitrarily large orthogonal families. Therefore compact interval support alone does not imply the obstruction; the cosine optimizer's nonzero taper is essential. As \(\lambda\downarrow0\), the normalized cosine window approaches a box after rescaling, and no gap uniform in the degenerate parameter \(\lambda=0\) is claimed.

**Unbounded-span control.** The Riemann–Lebesgue lemma gives \(K_\lambda(u)\to0\) as \(|u|\to\infty\). For three points at \(0,L,2L\), the off-diagonal term in (11) tends to zero as \(L\to\infty\). Thus failure of exact equality at \(D\geq3\) must not be mistaken for an unconditional size-independent stability gap. Formula (5) explicitly retains the required span/density constraint.

**Literature and provenance.** The cosine optimizer and its variational optimality are Wang's Proposition 4.1, while the integer-parameter finite-multiset inequality is Wang's Proposition 5.1 and the exact real-only residual was recorded in WI-442. Exponential orthogonality as vanishing Fourier differences, the sinc lattice for a uniform interval, and elementary transform-zero localization belong to classical harmonic analysis. A targeted check of the source and neighboring Fourier-zero/spectral-measure literature did not establish whether the specific sum-free zero-set specialization has appeared before; **no discovery priority or independent zeta theorem is claimed**. The contribution here is the explicit algebraic zero classification and its source-specific finite equality/packing consequence.

**Falsification tests.** Verify (6) against direct quadrature, explicitly check the removable point \(t=c\), check the root count in each tangent half-period, and test both regimes in (9) including a possible half-period crossing. Numerical diagnostics at \(\lambda=1\) give \(b\approx0.6042301211\), \(t_1\approx3.321537712\), \(t_2\approx6.377645239\), with \(K_\lambda(t_k/(\pi\lambda))\) consistent with zero to floating precision while \(K_\lambda(2t_1/(\pi\lambda))\approx0.03364549\ne0\). Numerics support checks only; (6)–(10) prove the assertion.

**Exact RH-facing boundary.** The argument concerns the positive-definite Gram matrix of *real* frequencies for one optimal window. Wang's actual zero multiset is conjugation-invariant in \(\mathbb C\), and the off-critical conjugate blocks of the Weil form are indefinite. Nothing here proves that their contribution cannot compensate real Gram packing costs, nor supplies an independently source-controlled lower bound on the number/density of real frequencies in the needed configuration. The short-interval moment bound by itself gives no individual off-line-zero coercivity or strict bootstrap. No improvement to Wang's unconditional bound, no claim that zeta extremizes the kernel, and **no proof of RH** follows.

## Consequence for the line

The all-real equality configuration allowed by the *abstract* integer rank/trace inequality cannot occur with three or more distinct real locations for Wang's actual cosine optimizer. The compact triple-gap version survives fixed smooth approximations and pinpoints a concrete structural cost that a truly source-compatible, non-scalar Gram argument might retain. The remaining missing implication is a source-justified way to preserve this positive real Gram cost after the off-line indefinite components and asymptotic localization are included, rather than inferring zero exclusion from a finite real-only obstruction.