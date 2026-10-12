# NB-340 — Interior phase routing blocks faster mixing throughout bounded quadratic windows

- **Status:** proved (author derivation; independent adversarial review pending)
- **Research line:** nyman_beurling
- **Depends on:** NB-304, NB-314, NB-331, NB-332, NB-333, NB-338
- **Classification:** EXACT-DERIVED + SOURCE-SIDE + UNIFORM-QUADRATIC-WINDOW + INTERIOR-ADJACENT-ROUTING + NON-TARGET-AWARE + PRIOR-ART-AUDITED

## Claim

Keep the actual ambient Nyman section and compressed dilation of NB-314:
\[
U_n=\operatorname{span}\{g_2,\ldots,g_n\},\quad
T_{n,m}=P_{U_n}A_m|_{U_n},\quad
E_{n,m}=\sqrt m\,T_{n,m}-R_n.
\]
For every **fixed** \(B>0\), a constant \(c_B>0\) exists such that
\[
\boxed{\liminf_{n\to\infty}\sqrt{\log n}\,
\inf_{\substack{m\in\mathbb Z\\n\le m\le Bn^2}}
\|E_{n,m}\|\ \ge c_B.}
\tag{1}
\]
In fact each sufficiently large \(n\) and each such \(m\) admits a
specific **interior** adjacent witness
\(\nu_q=g_q-(q-1)g_{q-1}/q\), with
\(c'_Bn\le q\le n\), satisfying
\[
\left|\left\langle E_{n,m}g_2,\nu_q\right\rangle\right|
\ge \frac{a_B}{q}
\tag{2}
\]
for some \(a_B,c'_B>0\) independent of \(m,n\).

This closes, at the **source/operator** level, the integer critical nodes
which remained after NB-334--NB-339: a zero at one specified critical
adjacent index is not a zero after optimization over all admissible
interior indices. It does not supply a target-distance estimate,
first-free Ford target occupation, a nonvanishing limiting norm gap, or
a consequence for RH.

## 1. The exact critical phase difference is a discrete derivative

As in NB-332 and NB-338, put
\[
\mathfrak D(x)=\sum_{k\ge1}\frac{\|kx\|_{\mathbb Z}^{\,2}}{k^2},
\qquad
\nu_q=g_q-\frac{q-1}{q}g_{q-1},
\qquad 8\le q\le n.
\]
Uniform convergence makes \(\mathfrak D\) continuous, even, and
1-periodic. Its two distinguished values are
\[
\mathfrak D(0)=0,\qquad
\mathfrak D(1/2)=\frac14\sum_{k\ {\rm odd}}\frac1{k^2}
=\frac{\pi^2}{32}=:D_* >0.
\tag{3}
\]

The uniform finite-section expansion of NB-338, with \(m=dq+r\),
\(0\le r\le d\) and \(d/q\) confined to a fixed compact subset of
\((0,\infty)\), becomes the particularly simple identity
\[
\boxed{\
q\langle E_{n,m}g_2,\nu_q\rangle
=\frac{\mathfrak D(m/q)-\mathfrak D(m/(q-1))}{4(d/q)}
+O(q^{-1}).\
}
\tag{4}
\]
Indeed the two exact phases in NB-338 are
\(u=d+r/q=m/q\) and
\(v=d+(d+r)/(q-1)=m/(q-1)\);
periodicity removes their integer parts. The error in (4) is uniform
in the ambient \(n\ge q\), in \(r/d\in[0,1]\), and in the declared
compact interval for \(d/q\). No phase regularity or differentiation
of \(\mathfrak D\) is used.

Thus a nontrivial change of \(\mathfrak D(m/q)\) along a short string
of consecutive admissible indices forces an order-\(1/q\) source
coefficient. The key is to place that string at a critical aspect
ratio whose fractional part is a small fixed rational number.

## 2. A finite rotation-grid lemma

Choose a positive integer \(M\ge4\) so large that continuity and (3)
give
\[
\sup_{\|t\|_{\mathbb Z}\le 1/M}\mathfrak D(t)<D_*/8,
\quad
\inf_{\|t-1/2\|_{\mathbb Z}\le1/M}\mathfrak D(t)>7D_*/8.
\tag{5}
\]
Such a **fixed** \(M\) exists by uniform continuity. We do not send
\(M\) to infinity with \(n\).

Suppose, for some integers \(Q=Q_n\asymp n\), that
\[
\frac{m}{Q^2}=\delta+O(n^{-1}),\qquad
\delta=K+\frac1M
\quad(K\in\mathbb Z_{\ge2}),
\tag{6}
\]
where \(m=O(n^2)\) and \(K,M\) are fixed. For \(0\le j\le M\), let
\(x_j=m/(Q+j)\). For each consecutive pair,
\[
x_j-x_{j+1}
=\frac{m}{(Q+j)(Q+j+1)}
=\delta+O_{K,M}(n^{-1}).
\tag{7}
\]
Consequently on the circle \(\mathbb R/\mathbb Z\),
\[
x_j\equiv x_0-\frac jM+O_{K,M}(n^{-1}),
\qquad 0\le j\le M.
\tag{8}
\]
The error is uniform in \(j\) because \(M\) is fixed. For every
starting phase \(x_0\), the grid
\(x_0-j/M\), \(0\le j<M\), includes a point within \(1/(2M)\)
of \(0\) and another within \(1/(2M)\) of \(1/2\). For all
sufficiently large \(n\), (8) places the corresponding actual
phases within \(1/M\) of these two points. By (5),
\[
\max_{0\le j<M}\mathfrak D(x_j)
-\min_{0\le j<M}\mathfrak D(x_j)\ge D_*/2.
\tag{9}
\]
Telescoping along the chain of at most \(M\) consecutive positions
now forces an index \(1\le j\le M\) with
\[
\boxed{
|\mathfrak D(m/(Q+j))-\mathfrak D(m/(Q+j-1))|
\ge \frac{D_*}{2M}.
}
\tag{10}
\]
This is deterministic: it uses neither equidistribution nor
Erdős--Turán or van der Corput estimates. The discrepancy between
the actual phases and the finite rational rotation grid is
\(O_{K,M}(n^{-1})\) in this fixed-length test.

## 3. Uniform construction at and below quadratic scale

Fix \(B>0\) and put
\[
\varepsilon=\frac{\log2}{1000},\qquad
K=\lceil B\rceil+2,\qquad \delta=K+1/M>B.
\tag{11}
\]
Split the admitted integers \(n\le m\le Bn^2\) into two ranges.

**Smaller dilations, \(m\le\varepsilon n^2\).**
Use the explicit quotient witness from NB-331:
\[
d=\lceil m/n\rceil,\quad q=\lfloor m/d\rfloor,\quad r=m-dq.
\]
Then \(0\le r<d\), \(n/2-1\le q\le n\), and for all sufficiently
large \(n\), uniformly throughout this range,
\(d/q\le3\varepsilon\).
The exact NB-331 finite bound gives
\[
\left|q\langle E_{n,m}g_2,\nu_q\rangle
+\frac{\log2}{4}\right|
\le28d/q\le84\varepsilon<\frac{\log2}{8}.
\]
Therefore
\[
|q\langle E_{n,m}g_2,\nu_q\rangle|
\ge\frac{\log2}{8}.
\tag{12}
\]
This is a uniform finite-scale use of NB-331, not an illicit
application of its asymptotic \(m=o(n^2)\) statement to a fixed
quadratic fraction.

**Critical dilations, \(\varepsilon n^2<m\le Bn^2\).**
Take
\[
Q=\operatorname{round}\!\sqrt{m/\delta}.
\tag{13}
\]
The bounds on \(m\) and the strict inequality \(\delta>B\)
give
\[
\sqrt{\varepsilon/\delta}\,n+O(1)\le Q
\le \sqrt{B/\delta}\,n+O(1)<n-M
\]
for all sufficiently large \(n\). In particular the entire string
\(Q+1,\ldots,Q+M\) lies within the **original ambient section**
and \(Q\asymp_{B}n\), uniformly in \(m\). Rounding gives
\(m/Q^2=\delta+O_B(n^{-1})\), so the lemma applies.

For the \(q=Q+j\) selected by (10), set
\(d=\lfloor m/q\rfloor\), \(r=m-dq\). Then
\[
0\le r<q\le d,\qquad
d/q=\delta+O_B(n^{-1}),\qquad q\asymp_B n.
\tag{14}
\]
The inequality \(q\le d\) follows from \(\delta>2\) and
large \(n\). Thus (4) applies uniformly with \(r/d\le1\),
and (10) implies, after absorbing its \(O(q^{-1})\) error,
\[
|q\langle E_{n,m}g_2,\nu_q\rangle|
\ge \frac{D_*}{16\delta M}
=\frac{\pi^2}{512\delta M}.
\tag{15}
\]
Combining (12) and (15), take
\[
a_B=\min\left\{\frac{\log2}{8},
\frac{\pi^2}{512\delta M}\right\}>0,
\tag{16}
\]
which proves (2) with an interior index bounded below by a
positive \(B\)-dependent multiple of \(n\).

Finally NB-304 supplies the genuine Hilbert norm estimates
\[
\|\nu_q\|_2^2\le
\frac{2H_{q-2}+1+\pi^2/18}{q^2},
\qquad \|g_2\|_2=\frac{\sqrt{\log2}}2.
\tag{17}
\]
Cauchy--Schwarz and (2), uniformly for \(q\le n\), give
\[
\|E_{n,m}\|
\ge \frac{a_B}{(\sqrt{\log2}/2)
\sqrt{2H_{n-2}+1+\pi^2/18}},
\tag{18}
\]
hence (1), for example with
\[
\boxed{c_B=a_B\sqrt{2/\log2}>0.}
\tag{19}
\]
The displayed constant is intentionally weak; sharp optimization
over the rotation phase, test length, or source/test-vector norms
is not claimed.

## 4. Falsification, novelty and the exact boundary

- **Critical-node control.** NB-334--NB-339 correctly identify zeros
  and microscopic sign reversals at a *fixed* critical adjacent
  index. Here \(q\) may move by an order-\(n\) fraction relative to
  an initial boundary index, and the method deliberately targets
  \(\delta=K+1/M\), not an integer. This does not contradict
  NB-335's persistence result for sublinear reindexings.
- **Consecutive-denominator control.** Formula (4) keeps the exact
  denominators \(q,q-1\). Replacing them by a common denominator
  would erase the discrete derivative and invalidate the proof.
- **Arithmetic-quotient control.** The critical choice has
  \(d\ge q>r\); this verifies the \(0\le r\le d\) domain used in
  NB-338. An unrestricted remainder \(r<q\) without \(d\ge q\)
  would not be sufficient.
- **Uniformity control.** \(M,K,\varepsilon,B\) are fixed before
  \(n\to\infty\). The same sufficiently large \(n\) works for
  **all** admitted integers \(m\). Rounding contributes
  \(O_B(n^{-1})\), not an uncontrolled phase defect.
- **Matched generic control.** The phase-routing lemma itself is
  topological and applies to any continuous 1-periodic profile
  separating two points. Arithmetic content enters through the
  actual Nyman coefficient identity (4), its admissibility
  restrictions, and the witness norms (17). No specifically
  zeta-theoretic coercivity follows from the generic lemma.

The prior-art neighborhood includes Báez-Duarte, Balazard,
Landreau and Saias, *Notes sur la fonction zêta de Riemann, 3*
(Adv. Math. 149 (2000), 130–144, DOI 10.1006/aima.1999.1861),
and Balazard--Martin, *Sur l'autocorrélation multiplicative de la
fonction partie fractionnaire et une fonction définie par J. R.
Wilton* (arXiv:1305.4395), which establish the natural
approximation/autocorrelation context. The periodic phase and
finite-grid arguments are elementary rather than claimed new
external theorems. The line-local contribution is the uniform
passage from the NB-338 microscopic finite-section difference
to an **all-integer bounded quadratic-window** operator bound,
without a discrepancy theorem. No claim of bibliographic
originality is made; no external estimate is load-bearing, so
the existing SOURCES.md needs no change.

**Remaining boundary.** The rate in (1) remains
\(c_B/\sqrt{\log n}\to0\); it does not preclude ordinary rank-one
operator convergence. More importantly, the test is a source
direction and one adjacent observer. It does not quantify the
projection of the physical first-free Ford target onto that
observer, nor the conditioning and off-critical contraction
required by the Nyman--Beurling approximation problem. No
claim about the Nyman distance or RH follows.
