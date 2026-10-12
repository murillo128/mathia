# PF-345 — a growing exterior edge strip has exponentially small transition-shorted trace mass

**Status:** EXACT-DERIVED + FINITE-SECTION-VARIATIONAL-SHORTING + NEGATIVE-BINOMIAL-EXTRAPOLATION + RELATIVE-TRACE-CLASS-BOUND + NORMALIZED-ANGLE-OPEN.

PF-344 establishes exponential suppression of the **two individual edge modes** after a fixed positive-width physical transition band is eliminated from the complete positive seam form. Its qualitative weighted-completeness argument does not control coefficient growth for arbitrary exterior modes. Here an explicit negative-binomial extrapolator extends its quantitative trial to a **growing-dimensional, physically positive-width strip on each side of the transition**. The trace-norm statement below concerns a positive compression of the *unnormalized finite-section Schur complement*. It is not a trace-ideal theorem for the diagonally normalized low/high angle.

## Precise claim

Retain the strictly positive canonical finite-section seam form \(M=Q+\Lambda_E>0\), the zero-twist symmetric seam-parity cosine basis, and the exact transition-sector Schur complement \(S=M^{/\mathcal T}\) from PF-344. Fix \(0<\kappa_-<\kappa_+<\infty\), with \(\eta=\kappa_+-\kappa_->0\). Write \(L=L_n\), \(h=2\pi/L\), and

\[
D=D_n=L^{-1}(s_{n-1}^{-1}+s_n^{-1}),\qquad
D_n\ge c e^{(19/80)L_n}/L_n
\tag{1}
\]

as in PF-344 (25). Choose the fixed positive constants

\[
0<a<\min\{10^{-3},\eta/(8\pi),\kappa_-/(8\pi)\},
\qquad b=a/100,\qquad
m=\lfloor aL\rfloor,\quad R=\lfloor bL\rfloor.
\tag{2}
\]

Let \(\tau_-\) be the lowest positive transition frequency and \(\tau_+\) the highest, both on the Fourier lattice. For \(1\le r\le R\), define the normalized exterior cosine modes

\[
\ell_r(t)=\sqrt{2/L}\cos((\tau_--rh)t),\qquad
h_r(t)=\sqrt{2/L}\cos((\tau_++rh)t).
\tag{3}
\]

For sufficiently large \(n\), the \(2R\) vectors in (3) lie respectively in the retained low and high sectors, are orthonormal in the seam Fourier metric, and are supported on one cuff in the symmetric two-face parity channel. The choices in (2) ensure that all \(m\) successive frequencies inward from either transition edge remain inside the **actual eliminated transition sector**. Let \(E_n\) denote their span, and \(P_{E_n}\) the orthogonal projection in that Fourier metric.

There are constants \(C,\gamma>0\), independent of \(n\), the index \(r\), and the containing canonical finite section, such that

\[
\boxed{\quad
0\le\langle c,Sc\rangle\le C D_n e^{-\gamma L_n}
\quad\text{for every basis vector }c\in
\{\ell_r,h_r:1\le r\le R\}.\quad}
\tag{4}
\]

Consequently, possibly reducing \(\gamma>0\),

\[
\boxed{\quad
\|P_{E_n}SP_{E_n}\|_{\mathcal S_1}
=\operatorname{Tr}(P_{E_n}SP_{E_n})
\le C D_n e^{-\gamma L_n},
\qquad \dim E_n=2\lfloor bL_n\rfloor=\Theta(L_n).
\quad}
\tag{5}
\]

The trace identity in (5) uses positivity of the **compressed shorted form**; it does not assert that arbitrary cross-sector blocks are positive.

## 1. A transition-only negative-binomial extrapolator

The same explicit construction works for either edge and every \(r\). Put \(\alpha=\tau_--rh\), \(\sigma=+1\) at the lower edge; put \(\alpha=\tau_++rh\), \(\sigma=-1\) at the upper edge. Let

\[
z=e^{i\sigma ht},\qquad
B_{r,m}(z)=\sum_{j=0}^{m-1}
\binom{r+j-1}{j}(1-z)^j,
\tag{6}
\]

and use the real normalized trial trace

\[
f_{r,m}(t)=\sqrt{2/L}\,
\operatorname{Re}\bigl(e^{i\alpha t}[1-z^rB_{r,m}(z)]\bigr).
\tag{7}
\]

Because \(z^rB_{r,m}(z)\) is a polynomial involving only powers \(z^r,\ldots,z^{r+m-1}\), the exterior Fourier component of (7) is **exactly** the selected unit mode, and all its remaining components have frequencies

\[
\alpha+\sigma(r+j)h\quad(0\le j<m),
\tag{8}
\]

which are the first \(m\) positive transition frequencies inward from the corresponding edge. Thus (7) is admissible in PF-344's *full* finite-section Schur minimum. It does not discard a transition variable or assume any bound on \(M_{TT}^{-1}\).

For the \(\ell^1\) sum of the Fourier cosine coefficients of (7), the elementary hockey-stick identity and \(\|(1-z)^j\|_{\ell^1}=2^j\) give

\[
A_{r,m}\le1+\sum_{j=0}^{m-1}\binom{r+j-1}{j}2^j
\le1+2^m\binom{r+m-1}{m-1}
\le 2^{2m+r+1}.
\tag{9}
\]

The estimate deliberately overcounts cancellations and is valid for both signs of \(\sigma\). All trial frequencies remain in the same fixed bounded physical window needed for PF-344 (13), despite \(r,m\) growing with \(L\).

## 2. Exponential weighted cancellation with explicit coefficient cost

Let \(\delta=1/(8\pi)\). When \(|t|\le\delta L\), \(|1-z|\le h|t|\le1/4\). The classical negative-binomial identity

\[
z^{-r}=(1-(1-z))^{-r}
=\sum_{j=0}^{\infty}\binom{r+j-1}{j}(1-z)^j
\tag{10}
\]

holds in this region. Its remainder after \(m\) terms has ratio of successive absolute terms

\[
\frac{r+j}{j+1}|1-z|\le\frac{1+r/m}{4}<\frac12
\quad(j\ge m),
\tag{11}
\]

for all large \(n\), since \(r\le R\le m/100+O(1)\). Hence

\[
|1-z^rB_{r,m}(z)|
\le2\binom{r+m-1}{m}4^{-m}
\le2^{r-m}.
\tag{12}
\]

Outside \(|t|\le\delta L\), (9) gives the coarse but global bound
\(|1-z^rB_{r,m}(z)|\le A_{r,m}\le 2^{2m+r+1}\).
Together with \(\operatorname{sech}t\le2e^{-|t|}\) and
\(\int_{\mathbb R}\operatorname{sech}t\,dt=\pi\), these estimates yield

\[
\boxed{\quad
\int_{\mathbb R}
\left|\sqrt{L/2}\,f_{r,m}(t)\right|^2
\operatorname{sech}t\,dt
\le C\left(4^{r-m}+16^m4^r e^{-\delta L}\right).
\quad}
\tag{13}
\]

We emphasize that the coefficient penalty is simultaneously controlled: \(A_{r,m}^2\le C16^m4^r\). Applying the **actual complete two-pant trial bound** PF-344 (13), followed by the positive variational Schur minimum PF-344 (3), gives

\[
\frac{\langle c,Sc\rangle}{D}
\le C\left[
4^{r-m}
+16^m4^r e^{-\delta L}
+\frac{(1+w_n)16^m4^r}{D}
\right]
\tag{14}
\]

for either exterior cosine basis vector \(c\) in (3). This is the essential point: the nonsingular chart and seam energies are paid with the **same exponentially growing coefficient mass** that appears in the weighted approximation.

Now use \(r\le bL\), \(m\le aL\), \(m\ge aL-1\), and (1). Each right-hand term of (14) is \(O(e^{-\gamma L})\) for any sufficiently small

\[
0<\gamma<
\frac12\min\left\{
(a-b)\log4,\quad
\delta-a\log16-b\log4,\quad
\frac{19}{80}-a\log16-b\log4
\right\}.
\tag{15}
\]

All three quantities are strictly positive because \(b=a/100\) and \(a<10^{-3}\); the factor \(L\) from \(D^{-1}\) is absorbed by the spare exponent. This proves (4).

## 3. Positive trace mass of the growing edge subspace

The compression \(P_{E_n}SP_{E_n}\) is a positive finite-rank operator, regardless of couplings to modes outside \(E_n\). In the orthonormal Fourier basis (3), its trace is exactly the sum of the \(2R\) diagonal shorted energies. Thus (4) implies

\[
\|P_{E_n}SP_{E_n}\|_{\mathcal S_1}
\le2RC D_n e^{-\gamma L_n}
\le C' D_n e^{-\gamma' L_n}
\quad(0<\gamma'<\gamma),
\tag{16}
\]

since \(R=O(L_n)\). The two physical edge-strip widths tend to the same **positive constant** \(2\pi b\); only the subspace dimension grows. The result is uniform across containing canonical finite sections, as in PF-344.

The statement does not use a separate orthogonality assumption in the *energy* metric. Positivity and Fourier orthonormality alone suffice for the trace identity. It does not imply that the off-diagonal block has a small **canonical correlation** after dividing by its simultaneously shorted diagonal energies.

## Prior art, provenance, and novelty

The negative-binomial series (10), the binomial-coefficient bounds, and finite-band superoscillatory extrapolation are classical. Related wider approximation schemes are treated by Karmakar and Jordan, *Beyond Superoscillation: General Theory of Approximation with Bandlimited Functions*, arXiv:2306.03963 (S22); this finding neither attributes (6) to them nor uses their results as an unproved input. The positive Schur minimum is the classical shorted-form identity in PF-344, with Dirichlet-to-Neumann references already cited there. The arithmetic input (1) is the established Baker--Harman--Pintz prime-gap bound (S6), via PF-344.

The **project-specific derivation** is the simultaneous control of extrapolation error and coefficient amplification in the canonical prime-flute corridor trial, followed by the positive finite-section shorting and a growing-rank trace estimate. Equations (6)--(16) are explicit and auditable, but no independent review or broad novelty claim is asserted.

## Exact boundaries and falsification controls

This is a local finite-section, symmetric cosine-parity, **unnormalized** result. It uses the fixed positive transition width and the unconditional prime-specific lower growth (1) of the raw corridor scale. If either fails, the coefficient penalty in (14) may defeat the estimate. The conclusion need not hold for the antisymmetric seam channel, arbitrary exterior packets, all low modes, the unbounded high-frequency sector, or an infinite-section Schur limit.

Most importantly, \(D_n e^{-\gamma L_n}\) need not tend to zero, and both shorted diagonal energies can shrink along with the mixed entries. Equation (5) does **not** prove compactness, Hilbert--Schmidt membership, or weak trace class for the **diagonally normalized** low/high angle. Nor does it prove the global reassembly bounds demanded by PF-318/PF-320. The remaining decisive test is a *two-sided* estimate for the shorted diagonal energy and its mixed canonical correlation, uniformly under canonical finite-section assembly.

A falsification could show that PF-344's trial bound (13) fails uniformly for bounded-frequency sums with the coefficient mass (9), that the Fourier/seam normalization used in (3) is not the claimed orthonormal symmetric channel, or that the exact Schur minimum excludes the full set of transition modes in (8). None of the trace bounds here substitutes for checking those geometric inputs.
