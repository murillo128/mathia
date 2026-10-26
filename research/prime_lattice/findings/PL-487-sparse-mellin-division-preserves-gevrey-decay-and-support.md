# PL-487 — Sparse Mellin division preserves Gevrey decay and the support interval

**Evidence/status:** LITERATURE+DERIVED / EXACT ANALYTIC REDUCTION;
CLASSICAL MINIMUM-MODULUS AND PALEY–WIENER INGREDIENTS;
NO FIXED-BOX INTERPOLANT EXISTENCE OR EXTERNAL NOVELTY CLAIM.

## Claim and consequence for the fixed-box question

Let \(\mathcal D\) be a discrete multiset of nonzero complex numbers,
with no finite accumulation point, whose multiplicity-counted function satisfies
\[
n(R)\le C(1+R)^a,\qquad 0<a<1.
\tag{1}
\]
For \(c\ne0\), put
\[
P(s)=c\prod_{\lambda\in\mathcal D}(1-s/\lambda).
\tag{2}
\]
The empty and finite products are allowed. Fix \(1<q<1/a\) and write
\(b=1/q>a\). Here \(G_c^q(\mathbb R)\) means compactly supported
functions satisfying \(\|k^{(j)}\|_\infty\le C_k A_k^j(j!)^q\).
Suppose \(k\in G_c^q(\mathbb R)\) and
\[
F(s)=\int_{\mathbb R}k(t)e^{st}\,dt
\]
vanishes at each point of \(\mathcal D\) to at least its specified
multiplicity. Then \(G=F/P\) is entire and, on every fixed closed vertical
strip \(I+i\mathbb R\),
\[
\boxed{|G(\sigma+i\tau)|\le C_I e^{-c_I|\tau|^b}\quad(\sigma\in I).}
\tag{3}
\]
Moreover, there is a unique \(g\in G_c^q(\mathbb R)\) such that
\[
G(s)=\int g(t)e^{st}\,dt,\qquad k=P(-\partial_t)g.
\tag{4}
\]
The differential series in (4) converges in every smooth norm. If
\(k\ne0\), the closed convex hulls of \(\operatorname{supp}g\) and
\(\operatorname{supp}k\) coincide. Equality of their possibly disconnected
supports is **not** asserted. Constants need not be uniform over multisets,
nearby selected points, or \(a\uparrow b\).

For the
[[research/prime_lattice/clues/CLUE-single-box-range-sparse-mellin-interpolation|single-box clue]],
take its multiset of unwanted zeros, including their prescribed
multiplicities, and add the point \(1\) once. Its product
\((s-1)\prod_{\lambda\ne\rho_0}(1-s/\lambda)^{m_\lambda}\)
has exactly the form (2), with \(c=-1\).
If an interpolant \(f\in G_c^q(J)\), \(1<q<1/a\), exists in that
clue, the requested stretched-exponential decay of
\(\Phi_{h,f}/P\) follows automatically, with \(b=1/q\).
Thus **within this Gevrey class, quotient decay is not an additional
existence constraint beyond mean-zero Hermite interpolation**.

The remaining constraint is still substantial: construct the interpolant
inside the prescribed single-box range. A merely \(C_c^\infty\)
interpolant has not been shown to belong to any such Gevrey class. This
result neither constructs it nor upgrades a smooth solution to Gevrey.

## 1. A local-circle lower bound needs no zero separation

From (1), \(\sum_{\lambda\in\mathcal D}|\lambda|^{-1}<\infty\).
The genus-zero product converges locally uniformly, with the prescribed
zero multiplicities and no other zeros. The argument in
[[research/prime_lattice/findings/PL-471-sparse-zero-annihilators-force-prime-variance-on-every-large-block|PL-471]]
also gives \(|P(s)|\le C_0\exp(C_0|s|^a)\).

We need a lower bound on a surrounding curve, not a false lower bound
at every point. Given \(s\in\mathbb C\), set \(R=4+|s|\),
\(N=n(2R)\), and \(\delta=1/[8(N+1)]\). Exclude from \([1,2]\)
the intervals of radius \(\delta\) around each number
\(|\lambda-s|\) with \(|\lambda|\le2R\). Their total length is at
most \(2N\delta<1/4\), even when multiplicities are counted. Choose
a radius \(r_s\in[1,2]\) outside them. On the whole circle
\(|z-s|=r_s\),
\[
|z-\lambda|\ge\delta\quad(|\lambda|\le2R),\qquad |z|<R.
\]
The finite part of the product therefore satisfies
\[
\sum_{|\lambda|\le2R}\log|1-z/\lambda|
\ge-N\log(2R/\delta)\ge-C_1 R^a\log R.
\tag{5}
\]
For the remaining factors, \(|z/\lambda|<1/2\), so
\(\log|1-z/\lambda|\ge-2|z|/|\lambda|\). Partial summation
using (1) gives
\[
\sum_{|\lambda|>2R}|\lambda|^{-1}\ll R^{a-1}.
\]
Consequently, uniformly on this circle,
\[
\boxed{|P(z)|\ge C_2\exp(-C_3R^a\log R).}
\tag{6}
\]
All constants can depend on the full product. Close clusters and large
finite multiplicities only enter the count \(N\); no lower spacing bound
has been assumed. This elementary special-case minimum-modulus estimate
is the load-bearing division step.

## 2. Exact cancellation transports the strip decay

For \(\sigma\) in a fixed compact interval, the functions
\(e^{\sigma t}k(t)\) have a common compact support and derivative bounds
\(C_I A_I^j(j!)^q\). Integration by parts \(j\) times yields
\[
|F(\sigma+i\tau)|\le C_I A_I^j(j!)^q|\tau|^{-j}.
\]
Choosing \(j\) proportional to \(|\tau|^{1/q}\) proves
\[
|F(\sigma+i\tau)|\le C_I' e^{-c_I'|\tau|^b}.
\tag{7}
\]
This is the usual Gevrey Fourier estimate, here written in the bilateral
Laplace convention.

By the multiplicity hypothesis, all apparent poles of \(G=F/P\) are
removable. On the circle from §1 about \(s=\sigma+i\tau\), its real
part stays in the strip enlarged by 2 and its imaginary part differs
from \(\tau\) by at most 2. Equations (6)–(7) give
\[
|G(z)|\le C\exp\{-c(|\tau|-2)_+^b+C'(4+|s|)^a\log(4+|s|)\}.
\]
Because \(a<b\), the positive term is absorbed into half the negative
term at sufficiently large height. The maximum-modulus principle for
the **entire quotient** on the disk proves (3), including its removable
values at product zeros. The compact remaining heights are absorbed
into \(C_I\). In particular no bound on \(1/P\) at a zero was used.

## 3. Division preserves the support interval and Gevrey order

Assume \(k\ne0\), and let \([\ell,r]\) be its support's closed convex
hull. Define
\[
H(\sigma)=\sup_{t\in[\ell,r]}\sigma t,
\qquad c_0=(\ell+r)/2,\qquad d=(r-\ell)/2.
\]
The elementary support bound is \(|F(s)|\le\|k\|_1e^{H(\Re s)}\).
Using it on the same circles, whose radii are at most 2, and applying
the maximum-modulus principle again gives
\[
|G(s)|\le C\exp\{H(\Re s)+C'(4+|s|)^a\log(4+|s|)\}.
\tag{8}
\]
The bounded change in \(H\) around the circle is absorbed in \(C\).
Since \(H(\sigma)-c_0\sigma=d|\sigma|\), (8) implies, for every
\(\epsilon>0\),
\[
|e^{-c_0s}G(s)|\le C_\epsilon e^{(d+\epsilon)|s|}.
\tag{9}
\]
Equation (3) puts \(G(i\tau)\) in \(L^2(\mathbb R)\). The classical
\(L^2\) Paley–Wiener theorem applied to (9), with the Fourier variable
rotated by \(s=i\tau\), gives an inverse supported in
\([\ell-\epsilon,r+\epsilon]\). Fourier uniqueness makes it the same
inverse for every \(\epsilon\); intersecting these intervals gives
support in \([\ell,r]\). A precise version of the theorem with the
radial exponential-type hypothesis used here is Rainer, *Real Analysis*,
Theorem 8.18 (source 158); its \(2\pi\) normalization is rescaled here.

The inverse has the absolutely convergent representation
\[
g(t)=\frac1{2\pi}\int_{\mathbb R}G(i\tau)e^{-i\tau t}\,d\tau.
\]
Differentiating it and using (3) yields
\[
\|g^{(j)}\|_\infty\le C\int_0^\infty x^je^{-cx^b}\,dx
=\frac Cb c^{-(j+1)/b}\Gamma((j+1)/b)
\le C_4A_4^j(j!)^q.
\tag{10}
\]
The last inequality follows from Stirling's formula, absorbing
polynomial factors into \(A_4^j\). Thus \(g\in G_c^q\).

Writing \(P(s)=\sum p_js^j\), the optimized Cauchy estimate gives
\(|p_j|\le CB^j/(j!)^{1/a}\), as in PL-471. The derivative series
\(\sum p_j(-1)^jg^{(j)}\) converges in every smooth norm because
\(q<1/a\). More precisely, using
\((j+m)!\le2^{j+m}j!m!\), its \(m\)-th derivative is bounded by
\[
C A^m(m!)^q\sum_{j\ge0}\frac{B_1^j}{(j!)^{1/a-q}}.
\]
It is again Gevrey of order \(q\), and has support contained in
\(\operatorname{supp}g\). Its Laplace transform is \(PG=F\), by
termwise integration by parts. Fourier uniqueness proves (4).
Hence \(\operatorname{supp}k\subseteq\operatorname{supp}g\); combined
with the support inclusion already proved, this proves equality of
the closed convex hulls. When \(k=0\), the unique inverse is simply zero.

## 4. The exact box-range consequence and its boundary

For \(h>0\), \(J\Subset(0,\infty)\), and \(f\in G_c^q(J)\), set
\[
\varphi(u)=A_hf(u)=h^{-1}\int_0^hf(u-v)\,dv,
\quad k(t)=\varphi(e^t),
\quad \Phi(s)=\int\varphi(u)u^{s-1}\,du.
\]
Box averaging preserves the Gevrey derivative bounds. The logarithmic
change of variables preserves their order on the fixed positive compact
support: expand \((u\partial_u)^j\) in ordinary derivatives, use
\({j\brace m}\le{j\choose m}m^{j-m}\), and
\(m^{j-m}m!\le j!\). This gives
\(\|\partial_t^j k\|_\infty\le C A^j(j!)^q\), as in
[[research/prime_lattice/findings/PL-486-subunit-order-mellin-filters-cannot-preserve-a-fixed-box-range|PL-486]].
Also \(\Phi(s)=\int k(t)e^{st}dt\) exactly, including the Jacobian.

Mean zero gives \(\Phi(1)=0\); the unwanted Hermite conditions give
the other zeros of \(P\). Thus (3) is precisely the optional quotient
bound in the clue. If \(\Phi(\rho_0)=1\), then
\(G(\rho_0)=1/P(\rho_0)\ne0\), since the selected point was excluded
from the product. No assumption on the selected pole's order is needed
for this nonvanishing statement.

With \(\psi(u)=g(\log u)\), equation (4) becomes
\[
\varphi=P(-u\partial_u)\psi.
\tag{11}
\]
The support interval of \(\psi\) equals that of \(\varphi\), and
\(\psi\) has the same Gevrey order. Equation (11) is a necessary
factorization of an **already existing** interpolant. It does not say
that \(\psi\) is itself a box average, or that arbitrary filtered
\(\psi\) belongs to the required box range. It therefore does not
evade PL-486's universal range-preservation obstruction.

## Prior art, checks and research consequence

Entire-function division with growth control and infinite-order
differential operators are classical. Berenstein–Gay–Vidras (1994),
Introduction, Theorem 1.1 and Lemma 1.2 (source 157), use minimum-modulus
estimates in a substantially broader division framework. The local-circle
proof above supplies the particular \(O(R^a\log R)\) loss needed here
directly from the multiplicity count; no general theorem from that paper
is imported without its hypotheses. Gevrey Fourier decay and the
\(L^2\) Paley–Wiener support theorem are also classical. This finding
claims a local reduction of the pending fixed-box test, not a new
general division theorem.

The audit checks are analytic rather than finite numerical evidence:
the product tail uses \(a<1\), decay absorption uses the stronger
\(a<1/q\), and removal of quotient singularities uses **every required
Hermite order**. Simple zeros of \(F\) at unwanted multiple poles do
not meet the premise. The circle selection handles arbitrarily close
clusters, and the support conclusion uses all \(\epsilon>0\), not a
single enlarged interval. Finite products, the empty product, and the
zero function satisfy the stated conclusions. No uniform constants,
critical case \(a=1/q\), or optimal exponent is asserted.

The optional reciprocal version of the single-box clue consequently
has one fewer obligation if a sufficiently regular interpolant can be
built: its quotient decay comes for free. Infinite fixed-box Hermite
feasibility remains unresolved, as does the original smooth simple-value
problem. No new prime-window floor, variance ceiling, arithmetic
cancellation, RH/GRH progress, Lean verification, or independent
adversarial approval follows from this analytic reduction.
