# MI-080 — Escaping anchors cancel known degree at constant noise cost

**Evidence level:** supported synthesis of [AF-581](../../findings/AF-581-known-polynomial-degree-restores-sharp-full-ray-adaptive-recovery.md). Interpolation, quotient duality and the approximation ingredients are classical. The sharp budget is for a known finite source list, shared polynomial calibration of known degree, unrestricted finite positive query coordinates and absolute bounded errors; it is not an arithmetic discriminator.

Observe \(y(a)=F_i(a)+b(a)+\eta(a)\), \(a>0\), with \(b\in\Pi_r\), \(r\ge0\) known, unrestricted coefficients and \(|\eta|\le\varepsilon\). For \(m\ge2\) known continuous sources, suppose the adjacent gaps \(G_i=F_{i+1}-F_i\) are positive, bounded and vanish at both ends. Set \(d=\min_i\sup G_i>0\). For \(i<j\), a nonconstant polynomial is unbounded on the ray, so
\[
\operatorname{dist}_\infty(F_j-F_i,\Pi_r)
=\tfrac12\sup(F_j-F_i),\qquad
\varepsilon_{\rm full}^{[r]}=d/4.
\]
These are supremal identification radii: the closest shifted pair has a midpoint alias at the endpoint. The same full-curve distance holds for unknown unbounded degree, where [AF-580](../../findings/AF-580-positive-noise-destroys-finite-stopping-under-unknown-polynomial-calibration.md) nevertheless excludes reliable finite noisy return. The degree promise changes finite acquisition, not this global distance.

Fix a finite informative set \(K\subset(0,\infty)\). Take \(r+1\) anchors
\[
t_0=L,\quad 0<L<\min K,\qquad t_k=kR\quad(1\le k\le r),
\]
and let \(l_k(a)\) be their Lagrange weights. At every finite \(R>\max K\), they reproduce every \(b\in\Pi_r\) exactly. For fixed \(L,r,K\), uniformly on \(K\) as \(R\to\infty\),
\[
l_0(a)\to1,\quad l_k(a)=O(R^{-1})\ (k\ge1),\quad
\Lambda(a):=\sum_{k=0}^r|l_k(a)|\to1.
\]
Thus the contrast and source centers
\[
Z(a)=y(a)-\sum_kl_k(a)y(t_k),\qquad
z_i(a)=F_i(a)-\sum_kl_k(a)F_i(t_k)
\]
satisfy
\[
|Z-z_i|\le\varepsilon(1+\Lambda),\qquad
z_{i+1}-z_i=G_i(a)-G_i(L)+o_R(1).
\]
First take \(L\) small, then \(R\) large. The source correction vanishes and the absolute-error multiplier tends to two, for every fixed degree. For \(r=0\), the sole anchor has weight one. For higher degree the remote weights may be negative: replacing \(\Lambda\) by one at finite \(R\) is invalid. Small weights still cancel large polynomial moments; no moment convergence or finite-precision guarantee follows.

If one known locator \(a_*\) has \(\gamma=\min_iG_i(a_*)>d/2\), then every strict noise allowance \(\varepsilon<d/4\) is attainable with **\(r+3\) adaptive values**. Choose one near-peak coordinate for each adjacent gap and include them with \(a_*\) in \(K\). Tune the anchors so the contrast-error bound \(E\) is close to \(2\varepsilon\), adjacent locator centers are separated by more than \(E\), and each selected pair peak exceeds \(2E\). The locator leaves at most two adjacent compatible labels; a single pair-specific follow-up separates them. Reused-anchor errors may be correlated, but these marginal interval exclusions suffice. AF-581 verifies the locator premise for every sufficiently remote finite prime-edit set, without a cardinality or logarithmic-diameter restriction.

With only \(r+2\) values, adaptivity gives no improvement over a fixed bank. The first \(r+1\) distinct values are compatible with every source by interpolation; the last test is a one-dimensional polynomial quotient. For its annihilator \(\lambda\), normalized by \(\sum|\lambda_k|=1\),
\[
\sum_k\lambda_ka_k^j=0\quad(0\le j\le r),\qquad
\varepsilon_{\rm bank}=\tfrac12\min_{i<j}
\left|\sum_k\lambda_k(F_j-F_i)(a_k)\right|.
\]
Arbitrary node placement does not remove its sharp worst-family deficit. Put
\[
f(x)=xe^{1-x},\quad g(x)=f(3x/2),\quad
x_*=2\log(3/2),\quad \rho=f(x_*)=\frac{8e}{9}\log(3/2)<1.
\]
AF-581 proves that every finite signed measure with zero total mass and total variation one satisfies \(\min\{|\mu(f)|,|\mu(g)|\}\le\rho/2\). Same-sign integrals are controlled by a convex combination of \(f,g\) with maximum \(\rho\); opposite signs are controlled by \(\|f-g\|_\infty\le\log(3/2)<\rho\). The certificate applies to all polynomial-annihilating banks, regardless of higher moment constraints, coalescing nodes or escape.

The non-arithmetic family \(F=(0,f,3f+2g,3f+3g)\) has \(d=1\) and locator \(x_*\). For every fixed known \(r\), its exact radii are
\[
\varepsilon_{r+2}^{[r],\rm ad}=\varepsilon_{r+2}^{[r]}=\rho/4
<1/4=\varepsilon_{r+3}^{[r],\rm ad}=\varepsilon_{\rm full}^{[r]}.
\]
AF-581's four-prime matched-control families give the same sharp asymptotic ratio for the prime-edit curves. This demonstrates a degree-independent **relative** loss at the first informative contrast; absolute prime-edit margins still vanish along remote families.

Fix the finite source set, degree and strict noise slack before selecting finite anchors. The construction supplies no uniform coordinate bound, bounded-window theorem, relative-error tolerance or arithmetic precision cost. Unknown degree restores AF-580's exact compact-window matching; full-ray access and absolute error control are essential to the positive result here.
