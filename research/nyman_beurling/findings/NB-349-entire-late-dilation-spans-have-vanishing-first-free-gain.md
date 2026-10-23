# NB-349 — Entire late dilation spans have vanishing first-free gain

- **Status:** proved (author derivation; independent adversarial review pending)
- **Research line:** `nyman_beurling`
- **Depends on:** NB-284, NB-290, NB-292, NB-298, NB-299
- **Classification:** EXACT-DERIVED + COLLECTIVE-DILATION-OBSTRUCTION + FIRST-FREE-TARGET-BOUND + FIXED-PACKET + CLASSICAL-HARDY-INGREDIENTS

## Claim and scope

NB-299 makes one far-dilated finite source section sample-null. Smallness of individual blocks alone does not control their combined normalized span: arbitrarily many weak, correlated columns can recover a strong direction. Here the **entire closed span** of late dilations obeys a cardinality-independent bound. The source sections being dilated may have arbitrary size, and their coefficients need no bound.

Use the Hardy space
\[
\mathscr H=H^2(\Re s>1/2),\qquad
\|F\|^2=\frac1{2\pi}\int_{\mathbb R}|F(1/2+it)|^2\,dt,
\]
and the unitary Mellin map from \(L^2(0,1)\),
\(\mathcal Mf(s)=\int_0^1 f(x)x^{s-1}\,dx\).
Fix a nonempty finite packet of distinct actual zeta zeros
\[
Z=\{\rho_j=1/2+\delta_j+it_j:1\le j\le N\},
\qquad 0<\delta_j<1/2,
\]
with their actual multiplicities included in its finite Blaschke product \(B_Z\). This is a conditional setup, not an assertion that such a packet exists. Put
\[
g_j(x)=\{1/(jx)\}-j^{-1}\{1/x\},\quad
V_{r,Z}=\operatorname{span}\{(\mathcal Mg_j)/B_Z:2\le j\le r\},
\quad U=V_{n-1,Z},\quad n\ge3.
\]
The quotients are Hardy functions because the selected zero multiplicities divide the canonical Mellin sources. Let
\[
LF=(F(\rho_1),\ldots,F(\rho_N)),\qquad K=LP_UL^*.
\]
Assume \(L|_U\) is onto, so \(K\succ0\). Throughout this finding, \(L\) is defined on the **ambient** \(\mathscr H\), and
\[
C_Z=LL^*,\qquad (C_Z)_{jk}=\frac1{\rho_j+\overline{\rho_k}-1}.
\tag{1}
\]
This ambient Cauchy Gram is not the sampling Gram of the closed arithmetic source.

For real \(a\ge1\) define
\[
S_aF(s)=a^{1/2-s}F(s),\qquad
D_a=\operatorname{diag}(a^{1/2-\rho_j}),\qquad LS_a=D_aL.
\]
Let \(M\ge2\) be an integer and let \(W\) be **any closed subspace** of \(S_M\mathscr H\). In particular one may take
\[
W=\overline{\operatorname{span}}\{S_mV_{r_m,Z}:m\in\mathcal I\},
\quad \mathcal I\subseteq\{M,M+1,\ldots\},
\tag{2}
\]
with no bound on the cardinality of \(\mathcal I\) or the source cutoffs \(r_m\). One may also use all of the closed arithmetic source at each dilation. The inclusion follows from \(S_m=S_MS_{m/M}\), where the second factor is an ambient Hardy isometry; no noninteger invariance of the arithmetic source is assumed.

Use the explicit finite source constant from NB-299:
\[
G_n=(\langle g_j,g_k\rangle)_{2\le j,k<n},\qquad
C_n^2=\frac{\sum_{j=2}^{n-1}(1+1/j)^2}{\lambda_{\min}(G_n)},
\qquad b=\frac{C_n}{\sqrt M}.
\tag{3}
\]
For \(M>C_n^2\), the image
\[
R_W=(I-P_U)W=(U+W)\ominus U
\]
is closed. Its baseline-free sample Gram satisfies
\[
\boxed{\displaystyle
\|\Xi_W\|\le B_M:=
\frac{\bigl(\sqrt{\|C_Z\|}\,M^{-\delta_-}+
\sqrt{\|K\|}\,b\bigr)^2}{1-b^2},\qquad
\Xi_W=LP_{R_W}L^*,\quad \delta_-=\min_j\delta_j.}
\tag{4}
\]
At fixed \(n,Z\), this is \(O_{n,Z}(M^{-2\delta_-})\), **uniformly over all such closed subspaces \(W\)**. In particular it controls the infinitely generated space in (2), not the sum of separate block Grams.

For any nonzero first-free datum \(y\), let
\[
\mathcal G_W(y)=y^*\bigl[K^{-1}-(K+\Xi_W)^{-1}\bigr]y,
\qquad \mathcal C_U(y)=y^*K^{-1}y.
\]
Then
\[
\boxed{\displaystyle
0\le\sup_W\sup_{y\ne0}\frac{\mathcal G_W(y)}{\mathcal C_U(y)}
\le\min\{1,\|K^{-1}\|B_M\}\longrightarrow0.}
\tag{5}
\]
There is also a sharp target-dependent boundary. If \(S_MU\subseteq W\subseteq S_M\mathscr H\), and \(n,Z,y\) are fixed, put
\[
h=K^{-1}y,\qquad \delta(y)=\min_{h_j\ne0}\delta_j.
\]
Uniformly over all choices of the intervening space \(W=W_M\),
\[
\boxed{\mathcal G_W(y)=\Theta_{n,Z,y}(M^{-2\delta(y)}).}
\tag{6}
\]
Thus adding any number of later copies, even of much larger source sections, cannot improve the fixed-datum decay exponent supplied by the first retained copy. Constants and oscillating leading coefficients are not asserted equal.

This includes the canonical first-free datum \(y_j=c_Z/\rho_j\), \(|c_Z|=1\), from NB-284. Its least occupied depth must still be read from \(K^{-1}y\); the theorem does not assume that every coordinate of that transformed datum is nonzero.

## Uniform angle control against the whole shifted Hardy space

The important strengthening of the single-copy argument is
\[
\|P_US_M\|\le C_nM^{-1/2}=b,
\tag{7}
\]
with domain all of \(\mathscr H\), rather than just \(U\).
For \(u\in U\), write \(B_Zu=\mathcal Mf\), where
\(f\in\operatorname{span}(g_2,\ldots,g_{n-1})\). Since
\(|g_j|\le1+1/j\), finite Gram positivity and Cauchy--Schwarz give
\(\|f\|_\infty\le C_n\|f\|_2=C_n\|u\|\).
For any \(v\in\mathscr H\), inner multiplication is isometric and commutes with \(S_M\), so
\[
|\langle u,S_Mv\rangle|
=|\langle B_Zu,S_MB_Zv\rangle|
\le\|1_{(0,1/M]}f\|_2\,\|v\|
\le b\|u\|\|v\|.
\tag{8}
\]
The support assertion used here is exact: Mellin inversion sends \(S_M\) to
\(A_Mf(x)=\sqrt M f(Mx)1_{(0,1/M]}(x)\). No pointwise estimate on a Blaschke-divided inverse Mellin function is required.

Every \(w\in W\subseteq S_M\mathscr H\) therefore satisfies
\[
\|P_Uw\|\le b\|w\|,\qquad
\|(I-P_U)w\|^2\ge(1-b^2)\|w\|^2.
\tag{9}
\]
When \(b<1\), this bounded-below map on the closed space \(W\) has closed range. It is injective, and \(U+W=U\oplus R_W\) is closed. This justifies both the orthogonal projector and all subsequent normalization, even for infinitely many highly dependent generating columns.

## Bounding the normalized collective sampler

For \(w=S_Mv\in W\), isometry and the covariance give
\[
\|Lw\|\le\sqrt{\|D_MC_ZD_M^*\|}\,\|w\|
\le\sqrt{\|C_Z\|}M^{-\delta_-}\|w\|.
\]
Also \(\|LP_Uw\|\le\sqrt{\|K\|}\,b\|w\|\). Hence
\[
\frac{\|L(I-P_U)w\|}{\|(I-P_U)w\|}
\le\frac{\sqrt{\|C_Z\|}M^{-\delta_-}+\sqrt{\|K\|}b}
{\sqrt{1-b^2}}.
\]
Taking the operator norm on \(R_W\) and squaring proves (4).
The Cauchy matrix (1) follows directly from the Mellin evaluation kernel
\(x^{\overline{\rho_j}-1}\); integrating its pairings gives (1), so no zero-sampling theorem is imported.

Set \(x=K^{-1/2}y\) and \(A=K^{-1/2}\Xi_WK^{-1/2}\). Minimum-norm interpolation in the closed orthogonal sum \(U\oplus R_W\) gives
\[
\mathcal G_W(y)=x^*A(I+A)^{-1}x.
\tag{10}
\]
As \(0\preceq A(I+A)^{-1}\preceq\min\{1,\|A\|\}I\) and
\(\|A\|\le\|K^{-1}\|B_M\), equation (5) follows.

## Target-sensitive two-sided certificate

For \(h=K^{-1}y\) define
\[
H_h=h^*Kh,\qquad
J_K(M)=h^*D_MKD_M^*h,\qquad
J_C(M)=h^*D_MC_ZD_M^*h,
\quad \eta_M=\|K^{-1}\|B_M.
\]
Whenever \(b<1\) and \(S_MU\subseteq W\subseteq S_M\mathscr H\),
\[
\boxed{\displaystyle
\frac{[\sqrt{J_K(M)}-b\sqrt{H_h}]_+^2}{1+\eta_M}
\le\mathcal G_W(y)
\le\frac{(\sqrt{J_C(M)}+b\sqrt{H_h})^2}{1-b^2}.}
\tag{11}
\]
Here \([a]_+=\max(a,0)\). For the upper bound, the scalar functional
\(w\mapsto h^*Lw\) on \(S_M\mathscr H\) has norm \(\sqrt{J_C(M)}\), while
\[
|h^*LP_Uw|\le\|P_UL^*h\|\,\|P_Uw\|
\le b\sqrt{H_h}\,\|w\|.
\]
Use (9) to bound its norm on \(R_W\), then use
\(\mathcal G_W(y)\le h^*\Xi_Wh\).

For the lower bound, restrict to vectors
\(r=(I-P_U)S_Mu\) with \(u\in U\). They lie in \(R_W\) and have \(\|r\|\le\|u\|\). On the unit sphere of \(U\), the scalar functional \(h^*LS_Mu\) has norm \(\sqrt{J_K(M)}\). Its correction \(h^*LP_US_Mu\) has norm at most \(b\sqrt{H_h}\), by (7). The reverse triangle inequality therefore gives
\[
h^*\Xi_Wh\ge[\sqrt{J_K(M)}-b\sqrt{H_h}]_+^2.
\]
Finally (10) yields
\(\mathcal G_W(y)\ge h^*\Xi_Wh/(1+\|A\|)\), proving (11).

Since \(K\succ0\),
\[
\lambda_{\min}(K)\|D_M^*h\|^2
\le J_K(M),\qquad
J_C(M)\le\|C_Z\|\|D_M^*h\|^2,
\]
and \(\|D_M^*h\|^2=\sum_j|h_j|^2M^{-2\delta_j}
=\Theta_{Z,h}(M^{-2\delta(y)})\).
Because \(\delta(y)<1/2\), the subtraction \(b\sqrt{H_h}=O(M^{-1/2})\) is asymptotically smaller than \(\sqrt{J_K(M)}\). Also \(\eta_M\to0\). This proves (6) without any phase-separation assumption or commutation of \(K\) and \(D_M\).

## Arithmetic closure, moving parameters, and controls

For an actual aggregate (2), integer dilation invariance puts \(W\) in the closed arithmetic quotient source \(\mathcal H_Z^\infty\). For every \(M\), the sum \(U+W\) is closed because \(U\) is finite-dimensional and \(W\) is closed; hence \(R_W=(U+W)\ominus U\) remains defined even when the sufficient angle bound \(b<1\) is unavailable. Thus NB-298's other bound still applies:
\[
0\preceq\Xi_W\preceq
E_{n-1,Z}:=L(P_{\mathcal H_Z^\infty}-P_U)L^*.
\tag{12}
\]
At fixed packet this tends to zero in norm as \(n\to\infty\), uniformly over every aggregate. Combining (12) with (4) for each of the finitely many smaller \(n\) gives joint vanishing uniformly over aggregates as \(\max(n,M)\to\infty\), once \(n\ge n_0\) with an onto old section. The same holds for gain divided by old cost, since \(K_{n-1,Z}\succeq K_{n_0-1,Z}\succ0\). The finite-rectangle argument does not require \(M>C_n^2\) on the deep-section part.

This conclusion does not apply to every late quotient construction. In particular NB-058 projects against an infinite natural closure, where there is no finite-section estimate (7) bounded away from one. Its collective compact-time defect question is not resolved here.

Further boundaries are essential:

- The ambient enlargement \(W=S_M\mathscr H\) is allowed for the upper bound, but is not asserted to be arithmetically realizable. Formula (12) is reserved for \(W\subseteq\mathcal H_Z^\infty\).
- Arbitrarily large coefficients and near dependencies do not evade (4): the proof bounds the actual closed subspace with its inherited Hilbert norm, not a coefficient norm or a sum of single-copy bounds.
- An empty or sample-null subspace need not attain the sharp rate. The lower bound requires \(S_MU\subseteq W\). Enlarging such a space may change the leading coefficient, but cannot change the fixed-datum exponent.
- Critical-line evaluation is not a bounded functional on this Hardy space. One cannot substitute \(\delta_j=0\) in this theorem. Already \((C_Z)_{jj}=1/(2\delta_j)\) shows why approaching the boundary requires a new uniform analysis.
- In a moving packet/section regime, (4)--(5) remain finite valid inequalities whenever \(b<1\). A sufficient collapse gate is \(\|K^{-1}\|B_M\to0\). This explicitly prices the ambient sampling Gram, the source constant and the horizontal zero depths; failure of this sufficient gate proves no positive occupation.
- These are first-free interpolation gains relative to the fixed ordinary source baseline. They neither estimate the full Nyman target distance nor compare the gain to a full finite-section excess that may itself be shrinking.

## Prior art and mathematical delta

The dilation semigroup is classical: Bagchi, *On Nyman, Beurling and Baez-Duarte's Hilbert space reformulation of the Riemann hypothesis*, Proc. Indian Acad. Sci. Math. Sci. 116 (2006), 137--146, [Theorem 7 and its proof](https://arxiv.org/pdf/math/0607733), gives the integer isometries and their canonical source covariance. Burnol, *A note on Nyman's equivalent formulation of the Riemann Hypothesis*, [Section 2](https://arxiv.org/pdf/math/9910055), gives the Mellin/Hardy and invariant-subspace framework. Both are already in SOURCES.md. Their general Hilbert-space ingredients, the nesting of shifted Hardy spaces, and minimum-norm interpolation are not new claims.

The neighboring interpolation literature includes Jacob--Partington--Pott, *Weighted interpolation in Paley--Wiener spaces and finite-time controllability*, J. Funct. Anal. 259 (2010), 2424--2436, [DOI 10.1016/j.jfa.2010.06.014](https://doi.org/10.1016/j.jfa.2010.06.014). Its published abstract concerns transferring Hardy interpolation to finite-time model spaces; no theorem from it is used here. Ehm's [*On certain Gram matrices and their associated series*](https://arxiv.org/abs/2405.06349) concerns explicit Nyman Gram kernels and quadratic-form decompositions. These are related source boundaries, not evidence of priority for the present consequence.

The delta from NB-299 is a uniform bound on a **whole arbitrarily generated late span**, including copies of unboundedly larger source sections. The support estimate (8) holds against the entire shifted ambient Hardy space, so poor conditioning among the dilated generators cannot supply hidden amplification after orthogonal normalization. Equation (11) also shows that an aggregate retaining its first copy has exactly the same target-selected power as that copy. This closes the many-copy rescue at fixed packet and ordinary baseline; it introduces no new arithmetic cancellation estimate or RH implication. The proof is analytic, with no numerical experiment or formal verification claimed, and remains pending independent adversarial review.
