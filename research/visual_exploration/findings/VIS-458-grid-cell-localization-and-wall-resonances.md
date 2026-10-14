# VIS-458 — Grid-cell localization and sharp wall resonances in folded sine spectra

## Claim and evidence status

Fix an integer \(m\ge2\). For real \(0\ne g\in L^2(0,1)\), use the positive sine-energy law and signed-reflection folding from VIS-457:
\[
b_r=\sqrt2\int_0^1g(x)\sin(\pi r x)\,dx,\qquad
\mu_m(j)=\|g\|_2^{-2}\sum_{r\ge1,\ r\equiv j\ (\mathrm{mod}\ m)}b_r^2,\quad
\widetilde\mu_m(j)=\tfrac12[\mu_m(j)+\mu_m(-j)].
\]
The endpoint strip in VIS-457 is **not necessary** for exact folding. If \(g\) is supported, up to null sets, inside **any one cell**
\[
I_k=[k/m,(k+1)/m],\qquad 0\le k<m,
\]
then, for every \(j\in\mathbb Z/m\mathbb Z\),
\[
\boxed{\widetilde\mu_m(j)=1/m.}\tag{1}
\]
This is a sharp *profile-independent support-interval* characterization: for an open interval \(J\subset(0,1)\), equation (1) holds for **every** nonzero real \(g\in L^2(0,1)\) supported in \(J\) if and only if \(J\) contains no interior grid wall \(k/m\), \(1\le k<m\). Thus the universal null consists of entire grid cells, not only the right endpoint cell.

Moreover, for a translated rectangular profile
\[
g_{a,\varepsilon}=\mathbf1_{(a-\varepsilon,a+\varepsilon)},\qquad
0<\varepsilon<1/(2m),\quad \varepsilon<a<1-\varepsilon,
\]
let \(k\in\{1,\ldots,m-1\}\) be the unique index with \(|a-k/m|<\varepsilon\), if it exists, and set \(\rho=1-|a-k/m|/\varepsilon\); otherwise set \(\rho=0\). Then the complete folded residue law is
\[
\boxed{\widetilde\mu_{m,a,\varepsilon}(j)
=\frac1m\left[1-\rho\cos\left(\frac{2\pi jk}{m}\right)\right]}\tag{2}
\]
when \(\rho>0\), and \(\widetilde\mu=1/m\) when \(\rho=0\). In particular, at a grid wall \(a=k/m\), \(\widetilde\mu(0)=0\), whereas even an arbitrarily close translated box becomes perfectly uniform as soon as its support clears the wall. The total-variation resonance is exactly
\[
\operatorname{TV}(\widetilde\mu_{m,a,\varepsilon},U_m)
=\frac{\rho}{2m}\sum_{j=0}^{m-1}|\cos(2\pi jk/m)|.\tag{3}
\]

**Evidence:** EXACT-DERIVED; CLASSICAL FOURIER AUTOCORRELATION/FINITE-DFT SPECIALIZATION; EXACT REPRESENTATION-ARTIFACT CLASSIFICATION. No new general Fourier theorem, genuine Farey-order assertion, or RH consequence is claimed.

## Proof of grid-cell universality and sharpness

Form the real, odd-reflected, period-\(2\) extension \(F(x)=g(x)\) for \(0<x<1\) and \(F(x)=-g(2-x)\) for \(1<x<2\). The Fourier coefficients \(a_r=\tfrac12\int_0^2F(x)e^{-\pi irx}\,dx\) satisfy \(a_0=0\), \(a_{-r}=\overline{a_r}\), and \(b_r^2=2|a_r|^2\). Therefore
\[
P_j:=\sum_{r\equiv j\ (\mathrm{mod}\ m)}|a_r|^2
=\|g\|_2^2\widetilde\mu_m(j).
\]
By period-\(2\) Parseval, the \(m\)-point Fourier transform of \(P_j\) is
\[
C_q=\frac12\int_0^2F(x)F(x+2q/m)\,dx
=\sum_{r\in\mathbb Z}|a_r|^2e^{-2\pi irq/m},\qquad 0\le q<m.\tag{4}
\]
If \(g\) occupies cell \(I_k\), the two support cells of \(F\), in the period-\(2\) partition into \(2m\) cells of length \(1/m\), have indices \(k\) and \(2m-k-1\). These indices have opposite parity. Translation by \(2q/m\) moves an **even** number of cells, preserving parity; for \(1\le q<m\) it cannot send either support cell to itself or to the other support cell. Hence \(C_q=0\) for every \(q\ne0\), while \(C_0=\|g\|_2^2\). Inverse finite DFT yields \(P_j=\|g\|_2^2/m\), proving (1).

Conversely, suppose an open interval \(J\) contains an internal wall \(k/m\). Choose \(\varepsilon>0\) small enough that \((k/m-\varepsilon,k/m+\varepsilon)\subset J\), and choose the real symmetric rectangular \(g\) supported on that interval. Every sine coefficient with frequency \(r=m\ell\) vanishes by antisymmetry about \(x=k/m\), since
\(\sin(\pi m\ell(k/m+t))=(-1)^{k\ell}\sin(\pi m\ell t)\).
Thus \(\mu_m(0)=\widetilde\mu_m(0)=0\ne1/m\). Every interval not contained in a single grid cell contains such an internal wall; this proves the stated sharp characterization **for a guarantee over all profiles**, not a necessity condition for each individual profile.

## Exact triangular wall law and numerical audit

For the rectangular profile, \(\|g\|_2^2=2\varepsilon\). With \(2\varepsilon<1/m\), the same-sign translated pieces of \(F\) never overlap at nonzero sampled shifts. Opposite-sign pieces can overlap only when the box straddles a unique wall \(k/m\). Write \(d=|a-k/m|<\varepsilon\). In the correlation (4), each of the shifts \(q=k\) and \(q=m-k\) contributes \(- (\varepsilon-d)\); when \(k=m/2\), these are the same shift and both contributions are included there. All remaining nonzero correlations vanish. Dividing by \(C_0=2\varepsilon\) and inverting the \(m\)-point DFT gives (2), including the \(m\)-even self-opposite case, and then (3).

An independent finite-sine-sum check used
\[
b_r=\frac{2\sqrt2}{\pi r}\sin(\pi r a)\sin(\pi r\varepsilon)
\]
for \(m=3,4,7,8\), centers at and away from grid walls, and \(r\le70{,}000\). The largest absolute disagreement from (2) among those checks was below \(1.5\times10^{-5}\); the uncounted positive spectral mass is bounded by \(4/(\pi^2\varepsilon R)\) for cutoff \(R\), and the observed missing mass at \(m=7,\varepsilon=1/35\) was about \(5.1\times10^{-5}\).

## Prior art, mathematical delta, and boundaries

The derivation is standard Fourier autocorrelation, support-overlap geometry, and finite-DFT inversion; consult Stein–Shakarchi, *Fourier Analysis: An Introduction* (2003), already recorded in this line's SOURCES.md, and the general autocorrelation framework in VIS-457. A targeted audit of Fourier spectral aliasing and autocorrelation literature found no basis for claiming novelty in the underlying general method. The **line-specific delta** is the sharp *all-profiles interval criterion* and the explicit triangular loss-of-uniformity law at cell boundaries. VIS-457 proved the endpoint strip sufficient and showed one off-endpoint counterexample; neither gave this interior-cell classification or the quantitative boundary resonance.

FD-327's fixed-parameter continuum step \(g_m\) lies in the final cell and therefore satisfies (1), but **so do infinitely many other interior-cell profiles with unrelated cuts and shapes**. A folded-modulus-\(m\) flat spectrum by itself therefore cannot locate the cut or identify genuine Farey order; a resonance near a wall can be produced solely by moving an artificial support. This concerns continuum profiles, not a uniform estimate for finite-prime rank transport when \(m=m(p)\) grows. It does not settle the accepted source-natural cut/orientation discriminator, transfer a source-prime error rate, improve Franel–Landau, or bear on RH.
