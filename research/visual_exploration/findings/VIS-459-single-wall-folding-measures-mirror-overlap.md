# VIS-459 — Single-wall folded sine spectra measure one mirror correlation

## Claim and evidence status

Let \(m\ge2\), \(1\le k<m\), \(a=k/m\), and let \(0\ne g\in L^2(0,1)\) be real and supported, up to null sets, in the two adjacent grid cells
\[
J_k=[(k-1)/m,(k+1)/m].
\]
Write the left and right wall-facing profiles, extended by zero if necessary, as
\[
L(t)=g(a-t),\quad R(t)=g(a+t)\quad (0<t<1/m),\qquad
A_k(g)=\int_0^{1/m}L(t)R(t)\,dt.
\]
Then \(\|g\|_2^2=\|L\|_2^2+\|R\|_2^2\), and the normalized mirror overlap
\[
\beta_k(g)=\frac{2A_k(g)}{\|g\|_2^2}\in[-1,1]
\]
**completely determines** the signed-reflection-folded positive sine-energy law at modulus \(m\):
\[
\boxed{\widetilde\mu_m(j)
=\frac1m\left[1-\beta_k(g)\cos\left(\frac{2\pi jk}{m}\right)\right],
\quad j\in\mathbb Z/m\mathbb Z.}\tag{1}
\]
Here \(b_r=\sqrt2\int_0^1g(x)\sin(\pi rx)\,dx\),
\(\mu_m(j)=\|g\|_2^{-2}\sum_{r\ge1,\ r\equiv j\pmod m}b_r^2\),
and \(\widetilde\mu_m(j)=[\mu_m(j)+\mu_m(-j)]/2\), exactly as in VIS-457/458.

Consequently, **exact folded uniformity holds if and only if \(L\perp R\) in \(L^2(0,1/m)\)**, even when both halves of the source meet and cross the grid wall. The full \([-1,1]\) resonance range is sharp: \(|\beta_k|=1\) if and only if \(R=L\) or \(R=-L\) almost everywhere (with \(g\ne0\)), whereas \(\beta_k=0\) is possible with nonzero support on both sides. In general
\[
\operatorname{TV}(\widetilde\mu_m,U_m)
=\frac{|\beta_k(g)|}{2m}\sum_{j=0}^{m-1}
 \left|\cos\left(\frac{2\pi jk}{m}\right)\right|.\tag{2}
\]

**Evidence:** EXACT-DERIVED; CLASSICAL FOURIER AUTOCORRELATION/FINITE-DFT SPECIALIZATION; PROFILE-LEVEL REPRESENTATION-LOSS CLASSIFICATION. The general Fourier identity is classical. The line-specific addition to VIS-458 is an exact formula and a necessary-and-sufficient uniformity criterion for **each individual** source spanning one internal grid wall, rather than the earlier criterion for uniformity guaranteed for *all* sources in an interval.

## Derivation by sampled support overlap

Take the real odd period-\(2\) reflection \(F(x)=g(x)\) for \(0<x<1\) and \(F(x)=-g(2-x)\) for \(1<x<2\), with Fourier coefficients
\[
a_r=\frac12\int_0^2F(x)e^{-i\pi rx}\,dx.
\]
Then \(a_0=0\), \(|a_{-r}|=|a_r|\), \(b_r^2=2|a_r|^2\), and Parseval gives \(\sum_{r\in\mathbb Z}|a_r|^2=\|g\|_2^2\). Hence the spectral residue sums \(P_j=\sum_{r\equiv j\pmod m}|a_r|^2\) satisfy
\(P_j=\|g\|_2^2\widetilde\mu_m(j)\), including residues fixed by sign reflection.

Consider the periodic correlations
\[
C_q=\frac12\int_0^2F(x)F(x+2q/m)\,dx
=\sum_{r\in\mathbb Z}|a_r|^2e^{-2\pi irq/m},\quad q=0,\ldots,m-1.\tag{3}
\]
In the partition of \(\mathbb R/2\mathbb Z\) into \(2m\) grid cells, the positive support of \(F\) occupies at most the two cells adjoining \(a=k/m\); its negative reflected support occupies the two cells adjoining \(2-a\). All nonzero translations by \(2q/m\) shift supports by an even number of grid cells. Same-sign pieces therefore have disjoint interiors after any such nonzero shift. Opposite-sign interiors can overlap only when \(q=k\) or \(q=m-k\), corresponding to aligning the centers \(a\) and \(2-a\). The overlap integral is a reflected cross-product, not a support-length statistic:
\[
C_0=\|g\|_2^2,\qquad
C_q=-A_k(g)\bigl(\mathbf1_{\{q=k\}}+\mathbf1_{\{q=m-k\}}\bigr)
\quad (1\le q<m).\tag{4}
\]
When \(m\) is even and \(k=m/2\), the two indicators coincide; their **sum** correctly gives \(C_{m/2}=-2A_k(g)\).

Finite Fourier inversion of (3)–(4) yields
\[
P_j=\frac1m\left[\|g\|_2^2-
 A_k(g)e^{2\pi ijk/m}-A_k(g)e^{-2\pi ijk/m}\right],
\]
which proves (1) for every \(m,k\), without any smoothness assumption. Cauchy–Schwarz and \(2|\langle L,R\rangle|\le\|L\|_2^2+\|R\|_2^2\) give \(|\beta_k|\le1\), with equality precisely for \(R=\pm L\) almost everywhere. The finite cosine sum vanishes because \(1\le k<m\); thus (1) is a nonnegative normalized probability law and (2) follows.

## Sharp controls, the box-law specialization, and independent checks

For any nonzero real \(u\in L^2(0,1/m)\), choose \(L=u\) and \(R=c\,u\) with \(c\in\mathbb R\). Then \(\beta_k=2c/(1+c^2)\), realizing **every** value in \([-1,1]\). The cases \(c=1\) and \(c=-1\) give maximal opposite resonance signs. Choosing nonzero orthogonal \(L,R\) gives \(\beta_k=0\) and a **perfectly flat folded spectrum despite support across both adjacent cells**. For example, take \(L=1\) on a short interval to the left of the wall and \(R=1\) on the nearer half but \(-1\) on the farther half of the corresponding right interval.

VIS-458's shifted box \(g=\mathbf1_{(a_0-\varepsilon,a_0+\varepsilon)}\) with \(0<\varepsilon<1/(2m)\), centered within \(\varepsilon\) of the wall \(k/m\), lies in these two cells. The mirror overlap is \(A_k=\varepsilon-|a_0-k/m|\), while \(\|g\|_2^2=2\varepsilon\). Therefore \(\beta_k=1-|a_0-k/m|/\varepsilon\), recovering VIS-458's exact triangular wall law. That earlier formula is one nonnegative-overlap slice of the full signed-mirror family (1).

As an independent finite-sine-coefficient diagnostic, direct integration of step profiles at \(m=7,k=3\), summing positive modes to \(350{,}000\), gave maximum per-residue folded-law errors below \(1.0\times10^{-5}\) for even, odd, orthogonal, weighted \((\beta=0.8)\), and half-shifted-box \((\beta=0.5)\) controls. The largest omitted total spectral mass among these tests was below \(3.5\times10^{-5}\), consistent with truncation. A wider symmetric box of half-width \(0.12<1/7\) at the same wall, with modes through \(200{,}000\), gave error below \(1.2\times10^{-6}\). The exact proof does not depend on either finite cutoff or the disposable exploratory visualization.

## Prior art, boundaries, and research consequence

This is the classical periodic Fourier power-spectrum/autocorrelation identity and finite aliasing inversion applied to an odd reflection and a sharply localized source; see Stein–Shakarchi, *Fourier Analysis: An Introduction* (2003), in this line's SOURCES.md. The usual Wiener–Khinchin/correlation correspondence and finite Fourier aliasing are background, not a claim of novelty for a general harmonic-analysis theorem. The substantive Mathia-specific distinction from VIS-457/458 is **profile-level classification** of a single grid-wall signal: the folded law forgets everything about \(g\) except one normalized mirror inner product (and the wall frequency \(k\), identified at most up to \(k\leftrightarrow m-k\)).

Uniformity is therefore neither evidence of a cut-free source nor evidence of genuine Farey ordering: many wall-crossing sources have \(A_k=0\), and opposite-parity mirror shapes reverse the sign of the same nonarithmetical resonance. Outside the two-cell support regime, other sampled shifts may contribute, so (1) is not asserted for multiple-wall supports. The **one-sided** sine law contains additional information and is not classified by this result.

In the FD-327 fixed-parameter same-prime continuum family, VIS-455's \(g_m\) lies inside the last grid cell, so the mirror overlap at its neighboring wall vanishes and folded uniformity follows. A profile crossing that wall would introduce a cosine resonance governed by its mirror overlap rather than by Farey arithmetic. No uniform growing-\(m\) finite-prime transfer, source-natural genuine-order discriminator, Franel–Landau improvement, or RH consequence follows from this representation theorem.
