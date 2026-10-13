# ANF-195 — Real near-extremizers have exactly the two-site notch-exposure envelope

**Status:** EXACT-DERIVED + SHARP-REAL-ENVELOPE + ZERO-SET-PACKING + SOURCE-SPECIFIC-LOCALIZATION. This is a theorem for real conjugation-invariant multisets only, not the unrestricted complex near-extremizer envelope of ANF-099.

## 1. Sharp statement for every fixed triangular notch

Use the Montgomery--Taylor conventions of ANF-087 and ANF-099:
\[
J_0=g*g,\quad K=\widehat g,\quad F_{\rm MT}(t)=K(t)^2\ge0
\quad(t\in\mathbb R),\quad K(0)=1,
\]
where \(g(u)=\cos(\sqrt2u)/(\sqrt2\sin(1/\sqrt2))\) on \([-1/2,1/2]\), zero elsewhere. Let \(0<\eta<1\), and freeze an admissible triangular notch
\[
\phi_\eta(\alpha)=b_\eta(1-|\alpha|/\eta)_+,\qquad
b_\eta>0,\qquad 0\le\phi_\eta\le J_0.
\]
Its real Fourier kernel is nonnegative and summably decaying:
\[
\Phi_\eta(t)=\widehat{\phi_\eta}(t)
=b_\eta\eta\,\operatorname{sinc}^2(\eta t)
\ge0,\quad
\Phi_\eta(0)=b_\eta\eta,\quad
0\le\Phi_\eta(t)\ll_\eta(1+t^2)^{-1},
\]
with \(\operatorname{sinc}(x)=\sin(\pi x)/(\pi x)\).

For any finite nonempty **real** multiset \(W\), write
\[
L(W)=2|W|-\sigma(W),\quad
e(W)=\frac{\int J_0|S_W|^2}{L(W)}-1,\quad
h_\eta(W)=\frac{\int\phi_\eta|S_W|^2}{L(W)},
\qquad
S_W(\alpha)=\sum_{x\in W}e^{-2\pi i\alpha x}.
\]
Here \(\sigma(W)\) counts distinct real support sites of multiplicity one. Restrict ANF-099's envelope to real multisets:
\[
\beta_\eta^{\mathbb R}
:=\lim_{\varepsilon\downarrow0}
\sup_{\substack{W\subset\mathbb R\ {\rm finite}\\e(W)\le\varepsilon}}
h_\eta(W).
\]
Let \(Z_+(K)=\{r>0:K(r)=0\}\). Then the exact all-cardinality, all-multiplicity identity is
\[
\boxed{\displaystyle
\beta_\eta^{\mathbb R}
=\Phi_\eta(0)+\max_{r\in Z_+(K)}\Phi_\eta(r)
=b_\eta\eta\left[1+
\max_{n\ge1}\operatorname{sinc}^2(\eta r_n)\right],
}\tag{1}
\]
where \(r_n=n+\delta_n\), \(0<\delta_n<1/2\), are the positive zeros identified in ANF-087. The maximum exists: \(\Phi_\eta(r_n)\to0\), and at least one value is positive.

In particular, **growing real cardinality, unbounded real span, and unbounded real multiplicities cannot increase the limiting normalized notch exposure beyond an exact two-site real equality configuration**. This does not bound the corresponding envelope over complex multisets.

## 2. Exact excess and removal of exceptional real sites

Write the distinct real support sites as \(x_i\) with multiplicities \(m_i\ge1\). Define
\[
\ell(m)=\begin{cases}1,&m=1,\\2m,&m\ge2.\end{cases}
\qquad L=\sum_i\ell(m_i).
\]
The positivity of \(K(t)^2\) on the real line gives the exact identity
\[
\Delta:=L e(W)
=\sum_{m_i\ge3}m_i(m_i-2)
+2\sum_{i<j}m_i m_jK(x_i-x_j)^2
\ge0.
\tag{2}
\]
Moreover,
\[
E_\eta(W):=\int\phi_\eta|S_W|^2
=\Phi_\eta(0)\sum_i m_i^2
+2\sum_{i<j}m_i m_j\Phi_\eta(x_i-x_j).
\tag{3}
\]
Every summand in (3) is nonnegative. The portion \(B_0\) of \(W\) at sites of multiplicity at least three has
\[
L(B_0)\le2\Delta,\qquad
E_0(B_0):=\int J_0|S_{B_0}|^2\le L(B_0)+\Delta.
\tag{4}
\]
The second inequality holds because the diagonal integer surplus and all off-diagonal \(K^2\) interactions of \(B_0\) are subterms of the nonnegative right side of (2).

On the remaining \(m_i\in\{1,2\}\) sites let
\[
D_i=\sum_{j\ne i}m_j K(x_i-x_j)^2.
\]
The corresponding excess \(\Delta_1\le\Delta\) obeys
\(\sum_i m_iD_i=\Delta_1\). Fix any \(\gamma>0\). Mark vertices with \(D_i>\gamma\) as \(B_1\). Since \(m_i^2\le2m_i\) for \(m_i=1,2\),
\[
L(B_1)=\sum_{i\in B_1}m_i^2
\le\frac{2\Delta_1}{\gamma}\le\frac{2\Delta}{\gamma}.
\tag{5}
\]
For the union \(B=B_0\sqcup B_1\) (whole support fibers, so \(L\) is additive),
\[
L(B)\le(2+2/\gamma)\Delta,\qquad
E_0(B)\le L(B)+\Delta,\qquad E_\eta(B)\le E_0(B).
\tag{6}
\]
The last inequality is the spectral domination \(0\le\phi_\eta\le J_0\). Write \(G=W\setminus B\). Positivity of every real \(K^2\) pair gives
\[
E_\eta(G)\le E_0(G)\le L(G)+\Delta.
\tag{7}
\]
The norm triangle inequality for the \(\phi_\eta\)-weighted exponential sums yields
\[
\sqrt{E_\eta(W)}
\le\sqrt{E_\eta(G)}+\sqrt{E_\eta(B)}.
\tag{8}
\]
Consequently, along any family with \(e(W)=\Delta/L\to0\), for each *fixed* \(\gamma>0\),
\[
L(G)/L\to1,\qquad
E_\eta(W)/L\le E_\eta(G)/L+o_\gamma(1).
\tag{9}
\]
No bounded-cardinality or compact-support assumption entered this removal. Every surviving site has multiplicity one or two and \(D_i\le\gamma\); in particular each distinct surviving pair obeys \(K(x_i-x_j)^2\le\gamma\).

## 3. The far notch tail is uniformly negligible

Choose a small fixed cell width \(h>0\) and \(\kappa>0\) such that
\(K(t)^2\ge\kappa\) whenever \(|t|\le h\); this is possible by continuity and \(K(0)=1\). Divide the real axis into half-open cells \(I_k=[kh,(k+1)h)\). For \(G\), set \(M_k=\sum_{x_i\in I_k}m_i\). Since the surviving multiplicities are one or two, its diagonal source energy equals \(L(G)=\sum_i m_i^2\). The within-cell part of (2) proves
\[
\sum_k M_k^2
\le L(G)+\frac{\Delta(G)}{\kappa}
\le L(G)+\frac{\Delta}{\kappa}.
\tag{10}
\]
For a fixed \(T>2h\), two sites separated by more than \(T\) must lie in cells at offset \(|k-l|>T/h-1\). Using \(\Phi_\eta(t)\ll_\eta(1+t^2)^{-1}\), cellwise Cauchy--Schwarz, and the summable inverse-square tail gives
\[
2\!\sum_{\substack{i<j\ {\rm in}\ G\\|x_i-x_j|>T}}
m_i m_j\Phi_\eta(x_i-x_j)
\ll_{\eta,h}
\frac{L(G)+\Delta/\kappa}{T}
\quad (T>4h).
\tag{11}
\]
This includes arbitrarily dense starting configurations: their square occupancy was paid for by the actual positive \(K^2\) source energy in (10).

## 4. Sum-free zero geometry makes the remaining near graph a matching

Fix \(T>4h\). ANF-087 proved that \(Z_+(K)\) is *sum-free*: no positive \(u,v\) have \(u,v,u+v\in Z_+(K)\). Therefore no three distinct real points have all their nonzero pairwise differences in the zero set. By continuity and compactness,
\[
c_T:=\min_{u,v\in[-T,T]}
\max\{K(u)^2,K(v)^2,K(u-v)^2\}>0.
\tag{12}
\]
The minimum cannot be zero: if it were, the triple \(\{0,u,v\}\) would have zero interaction on all three differences; the degenerate cases \(u=0\), \(v=0\), \(u=v\) are excluded automatically by \(K(0)=1\).

For any fixed \(\xi>0\), compactness also gives a \(\gamma_{T,\xi}>0\) such that
\[
0<|t|\le T,\ K(t)^2\le\gamma_{T,\xi}
\quad\Longrightarrow\quad
\Phi_\eta(t)\le M_\eta+\xi,\qquad
M_\eta:=\max_{r\in Z_+(K)}\Phi_\eta(r).
\tag{13}
\]
Choose \(0<\gamma<\min(c_T,\gamma_{T,\xi})\) in the removal of section 2. Join surviving vertices when their distance is at most \(T\). Every vertex has degree at most one: if \(x_i\) had distinct neighbors \(x_j,x_k\), then \(u=x_j-x_i\) and \(v=x_k-x_i\) lie in \([-T,T]\), and all three values of \(K^2\) in (12) would be at most \(\gamma\), because every good-site pair has \(K^2\le\gamma\). This contradicts (12). The near graph is a matching.

Each near edge thus satisfies (13), and \(2m_i m_j\le m_i^2+m_j^2\). Since the matching edges are vertex-disjoint,
\[
2\!\sum_{\substack{i<j\ {\rm in}\ G\\|x_i-x_j|\le T}}
m_i m_j\Phi_\eta(x_i-x_j)
\le(M_\eta+\xi)\sum_i m_i^2
=(M_\eta+\xi)L(G).
\tag{14}
\]
Combine (3), (11) and (14):
\[
E_\eta(G)
\le\left[\Phi_\eta(0)+M_\eta+\xi+
O_{\eta,h}(1/T)(1+\Delta/(\kappa L(G)))\right]L(G).
\tag{15}
\]
Now take a near-extremizing family \(e(W)\to0\), using the fixed \(\gamma\) chosen after \(T,\xi\). Equations (9) and (15) give
\[
\limsup h_\eta(W)\le\Phi_\eta(0)+M_\eta+\xi+O_{\eta,h}(1/T).
\]
First let \(T\to\infty\), then \(\xi\downarrow0\), proving
\[
\beta_\eta^{\mathbb R}\le\Phi_\eta(0)+M_\eta.
\tag{16}
\]

For the opposite inequality, choose any \(r\in Z_+(K)\) and take the two distinct simple real sites \(W=\{0,r\}\). They have \(L(W)=2\), \(E_0(W)=2\), and therefore \(e(W)=0\), while (3) gives
\[
h_\eta(\{0,r\})=\Phi_\eta(0)+\Phi_\eta(r).
\tag{17}
\]
Choosing a maximizing zero gives equality in (16), completing (1).

## 5. Relevance, prior art and audit boundary

The exact two-site equality class and sum-free Montgomery--Taylor zero set are existing Mathia results (ANF-087), based on the classical extremizer and Lamzouri's positive Hilbert-space inequality already anchored in SOURCES.md. The scalar near-extremizer envelope is ANF-099; ANF-081 previously certified one improving notch against *all* real multiplicity profiles, while ANF-105--ANF-106 supply related profile-decoupling and bounded-strip localization. The **new local conclusion** is the exact real-restricted all-cardinality envelope (1), not a new classical pair-correlation, point-process or zero-free theorem. The proof adds a direct local matching extraction from small positive \(K^2\) excess, with a source-paid cell-occupancy tail, so no new external theorem is load-bearing. The relevant external literature audit by zero-set packing, near-extremal positive-type pair energies and Montgomery--Taylor notch language did not identify a direct version; this is not a global novelty claim.

To falsify (1), check the integer multiplicity surplus and the coefficient \(2m_i m_j\) in (2)--(3), the weighted incident-energy identity before discarding exceptional sites, the positivity/decay of \(\widehat{\phi_\eta}\), the \(\ell^2\) occupancy estimate (10), the compact no-zero-triple implication (12), and the matching normalization \(2m_i m_j\le m_i^2+m_j^2\). The order of limits is essential: first \(e\to0\) with \(T,\xi,\gamma\) fixed, then \(T\to\infty\), then \(\xi\to0\).

This **does not** show that the unrestricted \(\beta_\eta\) of ANF-099 equals its real restriction. Real multisets form only a subclass of conjugation-invariant complex multisets, and the near-extremal Hilbert deficit need not control the height or physical source tensor uniformly when cardinality and span grow. Thus the fixed-notch RH-facing obstruction remains: rule out genuinely nonreal near-extremizers with exposure at least \(B_\eta\), or construct one. No new proportion of critical zeta zeros, global zeta-zero exclusion or RH result follows.
