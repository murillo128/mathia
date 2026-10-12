# WI-442 — Wang's integer multiset inequality certifies distinct zeros at every fixed power scale

**Status:** PRIMARY-SOURCE-AUDIT + LITERATURE+DERIVED + RECENT-UNREFEREED-PREPRINT + EXACT-FINITE-INEQUALITY + PRIOR-ART-REDIRECT + NON-RH + NO-NOVELTY-CLAIM

Source: Biao Wang, *Simple critical zeros and distinct zeros of the Riemann zeta function in short intervals*, arXiv:2609.07918v2 (posted 6 October 2026; manuscript dated 8 October 2026), https://arxiv.org/abs/2609.07918. Theorem 1.2 and Proposition 5.1, Section 5.

Related finding: WI-226 (its September v1 distinctness threshold is superseded, while its simple-critical and bow-reservoir obstruction remains).

## Claim and exact source status

Let \(H=T^\theta\), where \(0<\theta<1\) is **fixed**, let \(N(T,H)\) count nontrivial zeta zeros by multiplicity in \((T,T+H]\), and let \(N^d(T,H)\) count distinct zeros there irrespective of horizontal position. Define
\[
C_\theta=\frac{\theta}{2}+\frac1{\sqrt2}\cot\frac{\theta}{\sqrt2},
\quad q_\theta=\lfloor C_\theta\rfloor\ge1,
\quad
D(C)=\frac{2\lfloor C\rfloor+1-C}{\lfloor C\rfloor(\lfloor C\rfloor+1)}.
\tag{1}
\]
Wang's new Theorem 1.2 proves unconditionally, for each fixed \(0<\theta<1\),
\[
\boxed{\liminf_{T\to\infty}
  \frac{N^d(T,T^\theta)}{N(T,T^\theta)}
  \ge D(C_\theta)\ge C_\theta^{-1}>0.}
\tag{2}
\]
The positivity persists at arbitrarily small **fixed** power exponents. This **supersedes the September v1 distinct-zero estimate**
\[
d_{\mathrm{v1}}(\theta)=\tfrac32-\tfrac12 C_\theta,
\tag{3}
\]
whose right-hand side is nonpositive for \(\theta\le0.346658926139761\ldots\). It does **not** alter Wang's simple-critical theorem, whose coefficient \(c(\theta)=2-C_\theta\) is positive only for \(\theta>0.550193964744154\ldots\).

Equation (2) is literature evidence from the *unrefereed v2 preprint*, not an independently established new zeta theorem of Mathia. The finite-dimensional algebra and the bow-scale specialization below are independently reconstructed here.

## 1. Exact finite-multiset mechanism

Let \(\mathcal Z\) be a finite multiset of complex numbers invariant under conjugation, with multiplicities \(m_z\); choose a real, even, compactly supported \(L^2\) test \(\eta\), normalized by \(\widehat{\eta^2}(0)=1\). Put
\[
K(w)=\widehat{\eta^2}(w),\quad
N=\sum_{z\in\mathcal Z}m_z,\quad
S=\sum_{z,s\in\mathcal Z}K(z-s)^2,\quad
D=\#\operatorname{supp}\mathcal Z.
\tag{4}
\]
All sums in \(S\) include multiplicity. In this conjugate-symmetric setting \(S\) is real and nonnegative even though its individual complex summands need not be.

For any integer \(q\ge1\), Wang's Proposition 5.1 establishes the **exact** inequality
\[
\boxed{S\ge(2q+1)N-q(q+1)D},
\qquad
D\ge\frac{(2q+1)N-S}{q(q+1)}.
\tag{5}
\]
In particular \(q=1\) recovers the earlier Lamzouri distinct-count inequality \(D\ge(3N-S)/2\). The simple rank/trace estimate \(N^2\le DS\) already gives a positive \(D/N\) when \(S/N\) is uniformly bounded; the integer family (5) improves that quantitative conversion.

To audit the indefinite/off-line part of (5), represent each \(z\) by the vector
\(f_z(u)=\eta(u)e^{-2\pi iuz}\) and each nonreal conjugate pair by the real/imaginary combinations \(g_z=(f_z+f_{\bar z})/2\), \(h_z=(f_z-f_{\bar z})/(2i)\). On their finite span, the self-adjoint operator
\[
A=\sum_{x\in\mathcal R}m_x f_x\otimes f_x+
  2\sum_{j=1}^k m_{z_j}(g_{z_j}\otimes g_{z_j}-h_{z_j}\otimes h_{z_j})
\tag{6}
\]
has \(\operatorname{tr}A=N\) and \(\operatorname{tr}(A^2)=S\). The **minus sign** in the nonreal \(h\)-block is retained, rather than assuming positivity or RH.

Partition the distinct real locations into \(\mathcal R_1=\{m_x\le q\}\) and \(\mathcal R_2=\{m_x\ge q+1\}\), of sizes \(n,r\). Set \(L=\sum_{\mathcal R_1}m_x\), \(H_*=\sum_{\mathcal R_2}m_x\), \(M=2\sum_{j=1}^k m_{z_j}\), so \(N=L+H_*+M\) and \(D=n+r+2k\). With \(U=\operatorname{span}\{g_{z_j},f_x:x\in\mathcal R_2\}\), \(V=\operatorname{span}\{U,f_x:x\in\mathcal R_1\}\), and orthogonal projections \(P_U,P_V\), the conjugate-block signs still give
\[
\operatorname{tr}(P_U A)\ge H_*+M,\qquad
\operatorname{tr}(P_V A)\ge N.
\tag{7}
\]
For \(B=qP_V+P_U\),
\[
\operatorname{tr}(AB)\ge qN+H_*+M,\qquad
\operatorname{tr}(B^2)\le(q+1)^2(r+k)+q^2n.
\tag{8}
\]
Since \(A-B\) is self-adjoint, \(\operatorname{tr}(A-B)^2\ge0\), giving
\[
S\ge2qN+2(H_*+M)-(q+1)^2(r+k)-q^2n.
\tag{9}
\]
Subtracting the right side of the first inequality in (5) from the lower bound (9) leaves
\[
M+(q^2-1)k+
  \sum_{x\in\mathcal R_2}(m_x-q-1)+
  \sum_{x\in\mathcal R_1}(q-m_x)\ge0.
\tag{10}
\]
Thus (5) correctly charges conjugate nonreal blocks; its positivity is an operator-square inequality, not assumed Weil positivity. The scalar control \((m-q)(m-q-1)\ge0\) for integer \(m\ge1\) explains why adjacent multiplicities \(q,q+1\) naturally saturate the multiplicity part of the bound.

## 2. Short-interval deduction and optimized integer threshold

Wang's unconditional short-interval pair-correlation theorem, combined with its rational-weight removal, gives for every fixed Fourier support \(0<\lambda<\theta\) and admissible even test profile \(f\)
\[
\limsup_{T\to\infty}\frac{S}{N}
\le C(f).
\tag{11}
\]
Here the standard rescaling \(z_\rho=i(\rho-\tfrac12)\log T/(2\pi)\) turns the **correct** same-height functional-equation pairing \(\rho\mapsto1-\bar\rho\) into conjugation \(z_\rho\mapsto\bar z_\rho\). Merely using \(\rho\mapsto\bar\rho\) would wrongly leave the positive-ordinate interval; the former is the required invariance.

The source's variational optimizer has
\[
\inf_f C(f)=C_\lambda=
\frac\lambda2+\frac1{\sqrt2}\cot\frac\lambda{\sqrt2}.
\tag{12}
\]
Apply (5), first let \(T\to\infty\) with fixed \(\lambda<\theta\), then let \(\lambda\uparrow\theta\). For every fixed integer \(q\ge1\),
\[
\liminf\frac{N^d(T,T^\theta)}{N(T,T^\theta)}
\ge\frac{2q+1-C_\theta}{q(q+1)}.
\tag{13}
\]
Choosing \(q=\lfloor C_\theta\rfloor\) yields (2), and
\[
D(C)-\frac1C=
\frac{(C-q)(q+1-C)}{Cq(q+1)}\ge0,\quad q=\lfloor C\rfloor.
\tag{14}
\]
Both fixedness of \(\theta\) and the order of the limits are material. Neither a microscopic short-interval bound nor uniformity as \(\theta=\theta(T)\downarrow0\) follows.

## 3. Consequence at the live source-compatible bow scale

WI-226 and WI-202 identify the still-live count-saturating fixed-power bow range
\[
0<\vartheta\le\vartheta_*=\frac{3943}{12011}
=0.3282824077928565\ldots .
\tag{15}
\]
At its upper endpoint, direct substitution gives
\[
C_{\vartheta_*}=3.1553876542760326\ldots,\quad
q_{\vartheta_*}=3,\quad
D(C_{\vartheta_*})=0.320384362143664\ldots.
\tag{16}
\]
Thus the **v2** distinctness certificate is about **32.0384%** there; WI-226's old conclusion that *both v1 proportion bounds* are vacuous is no longer a statement about the current paper. The simple-critical bound remains negative at this endpoint, \(c(\vartheta_*)=-1.155387654276\ldots\).

The same extension from exact \(H=T^\vartheta\) to a *fixed-exponent* \(H=T^{\vartheta+o(1)}\) follows from WI-226's explicit error bookkeeping when \(0<\lambda<\vartheta\) is fixed: the local pair formula has relative error
\[
O_g\left((\log T)^{-1}+
  \frac{T^\lambda\log T}{H}\right)=o(1),
\tag{17}
\]
and the finite-multiset step (5) is independent of interval length. This is a Mathia **derived extension of the published v2 result**, not a claim that Wang's Theorem 1.2 explicitly states it. No exact endpoint \(\lambda=\vartheta\) is assumed for logarithmically shortened intervals.

**Crucial countercontrol:** distinctness is not critical-line occupancy. A mirror-closed configuration of simple off-line zeros can have \(N^d/N=1\), satisfy (2) with ample slack, and contain *no* simple critical-line zeros. Therefore (16) supplies neither the complementary critical-line reservoir needed to contradict the surviving bow nor an individual-off-line-defect certificate. It also cannot exclude a finite or zero-density exceptional divisor: both affect normalized fractions by \(o(1)\).


### Full finite defect and joint short-interval stability

The source's inequalities (7)–(10) admit an **exact, nonnegative defect decomposition**, not merely the discarded lower bound (10). Since \(\eta\) is nonzero on a set of positive measure, distinct complex exponentials are linearly independent after multiplication by \(\eta\); consequently the spans in (7) have \(\dim U=r+k\), \(\dim V=n+r+k\). Define \(Q_U=I-P_U\), \(Q_V=I-P_V\), \(B=qP_V+P_U\), and the projection losses
\[
\begin{aligned}
\varepsilon_U
&:=\operatorname{tr}(P_U A)-(H_*+M)
 =\sum_{x\in\mathcal R_1}m_x\|P_Uf_x\|^2
  +2\sum_{j=1}^k m_{z_j}\|Q_Uh_{z_j}\|^2,\\
\varepsilon_V
&:=\operatorname{tr}(P_V A)-N
 =2\sum_{j=1}^k m_{z_j}\|Q_Vh_{z_j}\|^2 .
\end{aligned}\tag{18}
\]
Both are nonnegative. The self-adjoint square identity
\(S=2\operatorname{tr}(AB)-\operatorname{tr}(B^2)+\|A-B\|_{\rm HS}^2\),
combined with the **exact** projection traces above, gives
\[
\boxed{\begin{aligned}
&S-(2q+1)N+q(q+1)D\\
&\quad=M+(q^2-1)k+
\sum_{x\in\mathcal R_2}(m_x-q-1)
+\sum_{x\in\mathcal R_1}(q-m_x)\\
&\qquad\quad+\|A-B\|_{\rm HS}^2
   +2\varepsilon_U+2q\varepsilon_V .
\end{aligned}}\tag{19}
\]
Every summand is nonnegative for integer \(m_x\), \(q\ge1\). This is a strengthening **of the recorded proof audit for the same claim**, derived from Wang's projection argument, not a new analytic input or a separately certified zeta theorem. For a single real location of multiplicity \(m\), (19) reduces exactly to \((m-q)(m-q-1)\); this checks both branches of the adjacent-integer multiplicity split.

For each fixed \(0<\theta<1\) put \(q=\lfloor C_\theta\rfloor\), and write \(M_\theta(T)\), \(k_\theta(T)\), \(N_{0,j}(T)\) for the off-line multiplicity mass, number of off-line conjugate pairs, and number of on-line locations of multiplicity \(j\) in \((T,T+T^\theta]\), respectively. Use the same \(N=N(T,T^\theta)\), \(D=N^d(T,T^\theta)\) as in (4). Applying Wang's second-moment upper bound separately for **fixed** admissible supports \(\lambda<\theta\), then taking \(\lambda\uparrow\theta\), yields
\[
\boxed{\;
\frac{M+(q^2-1)k+
\sum_{x\in\mathcal R_2}(m_x-q-1)+
\sum_{x\in\mathcal R_1}(q-m_x)}{N}
\le q(q+1)\left(\frac DN-D(C_\theta)\right)+o(1).
\;}\tag{20}
\]
The result is a **joint** bound: the same distinctness surplus pays simultaneously for all off-line zeros (including simple ones), the distinct off-line pairs, and critical-line multiplicities different from \(q,q+1\). At the fixed bow endpoint \(\theta=\vartheta_*=3943/12011\), \(q=3\), so (20) becomes
\[
\boxed{\;
\frac{M+8k+2N_{0,1}+N_{0,2}+R_{\ge5}}{N}
\le12\left(\frac{N^d}{N}-0.320384362143664\ldots\right)+o(1),
\;}\tag{21}
\]
where \(R_{\ge5}=\sum_{\Re\rho=1/2,\ m_\rho\ge5}(m_\rho-4)\) counts locations in the same short interval. The \(q=3\) calculation charges simple and double on-line locations by 2 and 1, leaves triple/quadruple ones uncharged, and charges higher multiplicities by their excess above four.

If \(D/N\to D(C_\theta)\), each population in (20) has **vanishing relative density**. The squared-operator and projection losses in (19) are controlled in the **iterated** limit of near-optimal fixed tests \(\lambda\uparrow\theta\) after \(T\to\infty\); (11) supplies no uniform statement for a varying test \(\lambda=\lambda(T)\). At no point is equality in Wang's bound established for actual zeta zeros. Even if it were attained in density, (20) would not exclude an individual off-critical zero or a zero-density exceptional family, and the finite-square identity adds no independent prime-side control.


## 4. Prior art, boundaries, and falsification

The analytic pair formula, optimizer, and integer-parameter Proposition 5.1 are **Wang v2 source claims**. Lamzouri's \(q=1\) finite-multiset inequality, the older global pair framework, and the rank/trace estimate are acknowledged prior art. The exact mathematical outcome recorded here is a **source-revision correction and Weil-inertia consequence**, not a new proof of the source theorem or a novelty/priority claim.

Checks against overstatement: \(q=1\) in (5) gives the v1 distinctness conversion; conjugate off-line contributions remain indefinite in (6) but are covered by (7)–(10); (14) proves nonnegative improvement over the rank/trace reciprocal; (16) uses \(q=3\), not the obsolete \(q=1\) bound. A proof claiming all distinct zeros are on the critical line, that \(D(C_\theta)\) bounds simple-critical zeros, or that a fixed positive fraction excludes a sparse exceptional set would fail these controls.

The preprint is unrefereed and should be independently verified before its quantitative conclusions are treated as settled peer-reviewed input. An independent theorem audit should check the conjugation-invariant kernel/trace identity (6), the subspace inequalities (7), the positivity residual (10), and the fixed-support short-interval error (17); failure of any load-bearing step requires correction or withdrawal of the corresponding derived consequence.

## Research consequence

This October source revision closes the *numerical distinctness-vacuity* diagnosis in WI-226, but not its *RH-facing* obstruction. Improved integer rank/trace information detects repeated versus distinct zero locations at every fixed power scale; without an independent observable that separates on-line mass, off-line conjugate blocks, and proof slack, it is not a strict off-line-defect elimination or a bootstrap to RH.
