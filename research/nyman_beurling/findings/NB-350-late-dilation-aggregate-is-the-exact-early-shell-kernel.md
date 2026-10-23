# NB-350 — The late dilation aggregate is the exact early-shell kernel

- **Status:** proved (author derivation; independent adversarial review pending)
- **Research line:** `nyman_beurling`
- **Depends on:** NB-034, NB-039, NB-284, NB-298, NB-349
- **Classification:** EXACT-DERIVED + ARITHMETIC-SPAN-IDENTIFICATION + FINITE-CODIMENSION + FULL-EXCESS-SATURATION + CLASSICAL-DILATION-INGREDIENTS

## Claim and consequence

NB-349 bounds the absolute first-free gain of an arbitrary late dilation aggregate. Its comparison with the **remaining finite-section excess** has a different answer: the maximal arithmetic aggregate can recover that excess exactly. The decisive structure is an equality of source subspaces, independent of any assumption about zeta zeros.

In \(L^2(0,1)\), put
\[
g_j(x)=\{1/(jx)\}-j^{-1}\{1/x\},\qquad
V_N=\operatorname{span}(g_2,\ldots,g_N),\qquad
\mathcal V=\overline{\bigcup_{N\ge2}V_N}.
\]
All source and dilation indices below are integers. Let
\[
A_mf(x)=\sqrt m\,f(mx)\mathbf1_{(0,1/m]}(x),\qquad
I_t=(1/(t+1),1/t].
\]
Every element of \(\mathcal V\) is constant almost everywhere on each \(I_t\). For an integer \(M\ge2\), define the bounded observation map
\[
R_Mf=(f|_{I_1},\ldots,f|_{I_{M-1}})\in\mathbb C^{M-1}.
\]
The coordinates mean cell values, equivalently cell averages; they are not point evaluations on arbitrary \(L^2\) functions.

Then
\[
\boxed{\begin{aligned}
\mathcal W_M
&:=\overline{\operatorname{span}}\{A_mg_j:m\ge M,\ j\ge2\}\\
&=\overline{\operatorname{span}}\{A_mg_j:m\ge M,\ 2\le j\le m+1\}\\
&=\overline{\operatorname{span}}\{k g_k-(k+1)g_{k+1}:k\ge M\}\\
&=\ker(R_M|_{\mathcal V})
=\{f\in\mathcal V:f=0\text{ a.e. on }(1/M,1]\}.
\end{aligned}}\tag{1}
\]
Thus the aggregate already uses finite source sections growing only linearly with the dilation. It has **exact codimension \(M-1\) in the arithmetic closure**. No identification of that closure with the full step space or ambient Hardy space is used.

For every \(n\ge3\),
\[
\boxed{\operatorname{codim}_{\mathcal V}(V_{n-1}+\mathcal W_M)
=\max\{0,M-n+1\}.}\tag{2}
\]
In particular,
\[
\boxed{V_{n-1}+\mathcal W_M=\mathcal V
\quad\Longleftrightarrow\quad M\le n-1.}\tag{3}
\]
These are equalities of closed subspaces, not just dense algebraic sums. Section 4 transfers them isometrically to first-free sampling and proves exact saturation of the entire finite-section excess in the regime (3).

## 1. Two neighboring dilation blocks recover each weighted edge

The classical integer-dilation identity is
\[
A_mg_j=\sqrt m\,(g_{mj}-j^{-1}g_m).
\tag{4}
\]
For \(x\le1/m\), it follows by substituting the fractional-part definitions. For \(x>1/m\), the expression on the right vanishes because both \(1/(mx)\) and \(1/(mjx)\) lie below one. Thus (4) includes the support cutoff, not just a formal Mellin identity.

Put \(\widehat h_k=k g_k-(k+1)g_{k+1}\). Telescoping gives
\[
A_mg_j=-\frac1{j\sqrt m}\sum_{k=m}^{mj-1}\widehat h_k.
\tag{5}
\]
Conversely, eliminating the common coefficient at \(k(k+1)\) gives
\[
\boxed{\widehat h_k
=k\sqrt{k+1}\,A_{k+1}g_k
-(k+1)\sqrt k\,A_kg_{k+1}.}\tag{6}
\]
Both source indices obey \(j\le m+1\). Equations (5)--(6) prove the first three equalities in (1), even at the level of algebraic spans before taking closure.

There is a finite realization with a stated support cost. For \(N\ge M\), every vector of
\[
\widehat W_{M,N}=\operatorname{span}(\widehat h_M,\ldots,\widehat h_{N-1})
\]
is a linear combination of the \(2(N-M)\) displayed columns in (6), with \(M\le m\le N\), source indices at most \(N\), and resulting canonical indices at most \(N(N-1)\). Individual columns need not belong to \(V_N\); their higher-index terms cancel in (6). This is a quadratic upper bound on the largest resulting index, not an optimal bound or a coefficient-conditioning estimate. The cancellation coefficients in (6) grow like \(k^{3/2}\).

## 2. The closure step preserves the kernel

On \(I_t\), the exact cell formula is \(g_j=\{t/j\}\). Every weighted edge with \(k\ge M\) therefore vanishes on the first \(M-1\) cells. Conversely, the finite identity proved in NB-034 is
\[
\ker(R_M|_{V_N})=\widehat W_{M,N}\qquad(N\ge M).
\tag{7}
\]
Its rank argument can be recovered directly. If
\(\sum_{j=2}^M c_j\{t/j\}=0\) for \(1\le t<M\), set
\(a=\sum_{j=2}^M c_j/j\). The first equation gives \(a=0\). Successive differences use
\[
\{t/j\}-\{(t-1)/j\}=j^{-1}-\mathbf1_{j\mid t}
\]
to force \(c_2,\ldots,c_{M-1}=0\) in order, and then \(c_M=0\). Hence \(R_M|_{V_M}\) is an isomorphism onto \(\mathbb C^{M-1}\). The same argument at cutoff \(N\) proves independence of \(g_2,\ldots,g_N\); the independent \(N-M\) weighted edges then exhaust the kernel in (7).

Taking a closure of finite kernels requires a correction argument. Let
\[
J_M=(R_M|_{V_M})^{-1}:\mathbb C^{M-1}\longrightarrow V_M.
\]
For fixed \(M\), this is bounded because its domain is finite-dimensional. Given \(f\in\mathcal V\) with \(R_Mf=0\), choose \(f_\ell\in V_{N_\ell}\), \(N_\ell\ge M\), with \(f_\ell\to f\). Then
\[
f_\ell-J_MR_Mf_\ell\in\widehat W_{M,N_\ell},\qquad
f_\ell-J_MR_Mf_\ell\longrightarrow f.
\tag{8}
\]
This proves the last equalities in (1). It also shows
\[
\mathcal V=V_M\mathbin{\dotplus}\mathcal W_M,
\tag{9}
\]
where the direct sum need not be orthogonal. No uniform bound on \(J_M\) as \(M\to\infty\) is asserted here.

## 3. Exact source deficit after adjoining an old section

The quotient map \(R_M\) identifies \(\mathcal V/\mathcal W_M\) with \(\mathbb C^{M-1}\). The image of \(V_{n-1}\) has rank
\[
\operatorname{rank}(R_M|_{V_{n-1}})=\min\{M-1,n-2\}.
\tag{10}
\]
If \(n-1\ge M\), it contains the onto section \(V_M\). If \(n-1<M\), its restriction to the first \(n-2\) cells is already injective by the preceding rank argument. This proves (2)--(3). Closedness follows either from the quotient description or because a finite-dimensional space plus a closed subspace is closed.

For \(M\le n-1\le N\), equations (7) and (9) also give the exact finite containment
\[
V_N=V_M+\widehat W_{M,N}
\subseteq V_{n-1}
+\operatorname{span}\{A_{k+1}g_k,A_kg_{k+1}:M\le k<N\}.
\tag{11}
\]
Thus recovery of each finite section has an explicit finite realization. Letting \(N\to\infty\) recovers the source closure, but supplies no rate for approximating its optimal interpolant or the RH target.

## 4. First-free sampling: when the aggregate attains all remaining excess

Conditionally fix a finite packet \(Z\) of actual zeta zeros in \(1/2<\Re s<1\), including their actual multiplicities in \(B_Z\), as in NB-284 and NB-349. Define the isometry
\[
\mathcal D_Zf=\frac{\mathcal Mf}{B_Z},\qquad
\mathcal H_Z=\mathcal D_Z\mathcal V,
\quad U=\mathcal D_ZV_{n-1},\quad
W=\mathcal D_Z\mathcal W_M.
\]
The map is defined on the whole closure: the Mellin sources lie in the closed subspace \(B_ZH^2\), and division there is isometric. It intertwines integer dilation with \(S_mF(s)=m^{1/2-s}F(s)\). Consequently \(W\) is precisely the aggregate in (1) with \(A_mg_j\) replaced by \(S_m\mathcal D_Zg_j\), and (2)--(3) transfer unchanged.

Let \(LF=(F(\rho_j))_j\) on ambient \(H^2(\Re s>1/2)\), and suppose \(L|_U\) is onto. Put
\[
K=LP_UL^*\succ0,\quad K_\infty=LP_{\mathcal H_Z}L^*,\quad
R=(U+W)\ominus U,\quad \Xi=LP_RL^*.
\]
Then the unsupplied future sampling Gram has the exact form
\[
\boxed{K_\infty-K-\Xi
=LP_{\mathcal H_Z\ominus(U+W)}L^*\succeq0,\qquad
\operatorname{rank}(K_\infty-K-\Xi)\le\max\{0,M-n+1\}.}\tag{12}
\]
The codimension is exact for source spaces; the sampling-rank bound need not be attained.

In particular, for \(M\le n-1\),
\[
\boxed{\Xi=K_\infty-K,\qquad
\mathcal G_W(y):=y^*[K^{-1}-(K+\Xi)^{-1}]y
=\mathfrak A_U(y):=y^*[K^{-1}-K_\infty^{-1}]y.}\tag{13}
\]
This holds for every datum \(y\), including the canonical first-free datum \(y_j=c_Z/\rho_j\). Whenever \(\mathfrak A_U(y)>0\), the gain divided by the full finite-section excess is **exactly one**. The onto assumption makes both inverses legitimate; the minimum-norm interpolation formula yields (13).

This does not contradict NB-349. At a fixed packet, \(\mathfrak A_U(y)\to0\) as \(n\to\infty\). Thus with \(M\le n-1\) tending to infinity, exact relative saturation can coexist with vanishing absolute gain. At fixed \(n\) and \(M\to\infty\), the saturation condition eventually fails and the source codimension in (2) grows. The theorem neither amplifies the fixed-packet gain nor supplies a new uniform moving-packet estimate.

## Boundaries, controls, and prior art

The source identity is unconditional. The off-critical packet application is conditional on such zeros existing and on the stated finite-section surjectivity. The argument does not infer zeros, RH, or an approximation rate from a finite rank calculation.

Allowing the source index to grow is essential to this proof. Equation (6) is unavailable in an aggregate \(\overline{\operatorname{span}}\{A_mV_r:m\ge M\}\) with a fixed \(r\); no claim of saturation is made for that different family. Likewise a finite collection of dilations cannot silently replace the closed infinite aggregate. Formula (11) gives a finite support cost, but no uniformly stable coefficients or stopping rule for a desired interpolation error.

Deflation preserves the source identities, not physical step values of the deflated inverse Mellin functions. The early observation in the quotient is \(R_M\mathcal D_Z^{-1}\); it must not be replaced by raw cell evaluation after division by \(B_Z\). Nor is \(W\) identified with \(S_M\mathcal H_Z\), or with the entire shifted ambient Hardy space. The latter remains only an admissible upper enlargement in NB-349.

For an endpoint control, at \(M=2,n=3\) the aggregate has codimension one in \(\mathcal V\), and adjoining \(g_2\) recovers all of \(\mathcal V\). At \(M=n\) the missing source dimension is exactly one, even though its image under a particular sampler could vanish. These checks distinguish the exact source statement from any stronger target claim.

Bagchi, *On Nyman, Beurling and Baez-Duarte's Hilbert space reformulation of the Riemann hypothesis*, Proc. Indian Acad. Sci. Math. Sci. 116 (2006), 137--146, [Theorem 7 and its proof](https://arxiv.org/pdf/math/0607733), supplies the classical step-space and integer-dilation framework. Burnol, *A note on Nyman's equivalent formulation of the Riemann Hypothesis*, [Section 2](https://arxiv.org/pdf/math/9910055), supplies the Mellin/Hardy and inner-factor setting for the **continuous** family; its closure identification is not imported for the discrete arithmetic source. Both are already anchored in SOURCES.md.

The external comparison covered tail dilation spans, finite-codimension source restrictions, discrete versus continuous closure, and Gram formulations; Ehm's [*On certain Gram matrices and their associated series*](https://arxiv.org/abs/2405.06349) addresses Gram formulae and quadratic-form decompositions. No external theorem beyond the stated classical framework is needed for the proof. There is no priority claim for the elementary span and quotient arguments.

The line-local delta is the converse to NB-039's single-copy containment: neighboring integer copies recover **every** weighted tail edge, and the corrected closure argument identifies exactly what the full aggregate omits. This links NB-034's early-shell kernel to NB-349's aggregate and upgrades NB-298's subblock inequality to equality in the regime (3), with a finite-rank deficit elsewhere. It changes the relative-excess interpretation without resolving the source-access or approximation-rate problem. The evidence is an analytic proof, not numerical evidence or a Lean verification.
