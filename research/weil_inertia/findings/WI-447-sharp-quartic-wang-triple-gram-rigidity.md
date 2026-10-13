# WI-447 — Sharp quartic span decay of Wang's triple-Gram rigidity and its smooth-test price

**Status:** EXACT-DERIVED + PRIMARY-SOURCE-SPECIALIZATION + SHARP-RATE/OBSTRUCTION + CLASSICAL-FOURIER-TOOLS + NON-RH + NO-PRIORITY-CLAIM

**Primary source:** Biao Wang, *Simple critical zeros and distinct zeros of the Riemann zeta function in short intervals*, arXiv:2609.07918v2, Proposition 4.1 (unique cosine variational optimizer, admissible smooth tests) and Proposition 5.1 (integer-multiset bound), https://arxiv.org/html/2609.07918v2.

**Local mathematical dependencies:** WI-442 (real-only exact finite-multiset defect), WI-445 (sum-free optimizer Fourier zero set and positive bounded-span triple cost), WI-446 (smooth near-minimizers can admit arbitrarily large orthogonal families when frequency span escapes).

## Exact results

Fix \(0<\lambda\le1\), let \(a=\lambda/2\), \(c=\lambda/\sqrt2\), and set
\[
 f_*(t)=\frac{\cos(\sqrt2t)}{\sqrt2\sin c}\mathbf1_{[-a,a]}(t),
 \quad K(x)=\int_{\mathbb R}f_*(t)e^{-2\pi ixt}\,dt.
\]
The unique Wang variational minimizer is \(f_*\). Its exact triple-Gram floor at frequency span at most \(R\) is
\[
 \kappa_\lambda(R)
 =\min_{\substack{r,s\ge0\\r+s\le R}}
     \left\{K(r)^2+K(s)^2+K(r+s)^2\right\}.
\]
WI-445 proves \(\kappa_\lambda(R)>0\) at every finite \(R\), but does not quantify its decay.

**Theorem A (sharp decay with universal leading constant).** For every fixed \(0<\lambda\le1\),
\[
 \boxed{\displaystyle
       \lim_{R\to\infty}R^4\kappa_\lambda(R)=\frac{3}{2\pi^4}.}
 \tag{1}
\]
In particular, the positive bounded-span obstruction cannot be promoted to a uniform-in-span floor, and its optimal large-span rate is exactly \(R^{-4}\). The leading constant is independent of \(\lambda\), but no uniformity as \(\lambda\downarrow0\) is claimed.

Define the admissible smooth-test class
\[
 \mathcal F_\lambda=
 \{\eta^2:\eta\in C_c^\infty((-a,a);\mathbb R),\
       \eta\ \text{even},\ \int\eta^2=1\}
\]
and Wang's functional
\[
 C(f)=\int_{\mathbb R} f(t)^2\,dt+
       \iint_{\mathbb R^2}|t-v|f(t)f(v)\,dt\,dv,
 \qquad C_\lambda=C(f_*).
\]
Let \(E_\lambda(R)\) be the infimum of \(C(f)-C_\lambda\) over \(f\in\mathcal F_\lambda\) for which *some* three distinct real frequencies \(x_1<x_2<x_3\), of span \(x_3-x_1\le R\), obey
\[
 \widehat f(x_2-x_1)=\widehat f(x_3-x_2)
 =\widehat f(x_3-x_1)=0.
\]
The infimum over the empty feasible set is \(+\infty\).

**Theorem B (sharp variational exponent).** For fixed \(0<\lambda\le1\), the feasible set is nonempty for all sufficiently large \(R\) and
\[
 \boxed{E_\lambda(R)=\Theta_\lambda(R^{-4}).}
 \tag{2}
\]
More explicitly, setting \(\sigma_\lambda=1-2\lambda^2/\pi^2>0\),
\[
 E_\lambda(R)\ge
 \frac{\sigma_\lambda}{3\lambda}\,\kappa_\lambda(R)
 =\left(\frac{\sigma_\lambda}{2\pi^4\lambda}+o(1)\right)R^{-4}.
 \tag{3}
\]
The matching upper bound uses even, nonnegative, smooth compactly supported probability densities of the exact source-admissible form \(f=\eta^2\), with **exact** three-frequency orthogonality; approximate Fourier zeros alone do not suffice.

## 1. Exact transform and addition identity

Put
\[
 b=c\tan c>0,\qquad A=c\cot c>0,\qquad
 H(u)=u\sin u-b\cos u,\qquad u=\pi\lambda x.
\]
Direct cosine integration (as in WI-445) gives
\[
 k(u):=K\left(\frac{u}{\pi\lambda}\right)
 =A\frac{H(u)}{u^2-c^2},\qquad Ab=c^2=\lambda^2/2,
 \tag{4}
\]
with continuous extension at \(u=\pm c\); \(k(0)=1\). Write \(w=u+v\). For all \(u,v>0\), elementary trigonometric addition and
\(\sin u=(H(u)+b\cos u)/u\) yield the **exact identity**
\[
\begin{aligned}
H(w)={}&\left(\frac wu+\frac{b^2}{uv}\right)H(u)\cos v
       +\left(\frac wv+\frac{b^2}{uv}\right)H(v)\cos u\\
 &+b\left(\frac wu+\frac wv-1+\frac{b^2}{uv}\right)
      \cos u\cos v
       +\frac b{uv}H(u)H(v).
\end{aligned}
\tag{5}
\]
No approximation or assumption that \(H(u)\) vanishes is used here. This identity is the quantitative residual behind the sum-free zero set: three simultaneously tiny \(H\)-values must finance the strictly nonzero cosine term.

## 2. Upper bound and attainment of the sharp coefficient

Write \(L=\pi\lambda R\). For large \(L\), choose an integer
\[
 n=\left\lfloor\frac{L}{2\pi}\right\rfloor-1\ge1,
 \qquad u=v=n\pi+\frac{3b}{4n\pi}.
\]
For all sufficiently large \(L\), \(w=2u\le L\), and \(u/L\to1/2\). Taylor expansion at integer multiples of \(\pi\) gives
\[
 H(u)=(-1)^n\left(-\frac b4+O_\lambda(n^{-2})\right),
 \qquad H(2u)=2b+O_\lambda(n^{-2}).
\]
Consequently,
\[
 L^4[2k(u)^2+k(2u)^2]\longrightarrow
 2(Ab)^2+(2Ab)^2=6A^2b^2.
 \tag{6}
\]
Thus \(\limsup_{L\to\infty}L^4\kappa_\lambda(L/(\pi\lambda))
 \le6A^2b^2\).

## 3. Matching lower bound; no hidden boundary minimizers

Choose any sequence \(L_j\to\infty\) and actual minimizers
\(u_j,v_j\ge0\), \(w_j=u_j+v_j\le L_j\). The compact minimum exists. Equation (6) forces
\[
 |k(u_j)|+|k(v_j)|+|k(w_j)|=O_\lambda(L_j^{-2}).
 \tag{7}
\]
Since \(k(0)=1\), the minimizing points are eventually strictly positive.

First **both \(u_j,v_j\to\infty\)**. Indeed, if their sum remained bounded, the positive compact triple gap WI-445 would contradict (7). If, say, \(u_j\to u_*<\infty\) while \(v_j\to\infty\), then \(k(u_*)=0\), so \(u_*>0\). Formula (4) and (7), using \(v_j,w_j\le L_j\), imply \(H(v_j),H(w_j)=O(1)\) and thus \(\sin v_j,\sin w_j\to0\). The sine addition formula then implies \(\sin u_*=0\), which contradicts \(H(u_*)=0\) because \(b>0\). The other case is symmetric.

Next **neither \(u_j/w_j\) nor \(v_j/w_j\) can tend to zero**. For example, if \(u_j/w_j\to0\), (4) and (7) give \(H(u_j)=O(u_j^2/L_j^2)=o(1)\), while \(H(v_j),H(w_j)=O(1)\). Since all three arguments diverge, \(\cos u_j,\cos v_j=\pm1+o(1)\). In (5) the forcing term
\(b(w_j/u_j+w_j/v_j-1+b^2/(u_jv_j))\cos u_j\cos v_j\)
has magnitude asymptotic to \(bw_j/u_j\to\infty\); the first remaining term is \(O(w_ju_j/L_j^2)=o(1)\), the second \(O(1)\), and the last \(o(1)\). Contradiction.

Pass to a subsequence where
\(\alpha_j=u_j/w_j\to\alpha\in(0,1)\),
\(\beta_j=v_j/w_j\to\beta=1-\alpha\), and \(d_j=w_j/L_j\to d\in[0,1]\). If \(d=0\), (4) and (7) give
\(H(u_j),H(v_j),H(w_j)\to0\). Formula (5) would then require
\(b(1/\alpha+1/\beta-1)\cos u_j\cos v_j\to0\), impossible because the coefficient is strictly positive and the cosine product has limiting absolute value one. Hence \(d>0\).

The three \(H\)-values are now bounded. Pass to a further subsequence with their limits and with
\(\cos u_j\to\epsilon_u\in\{\pm1\}\) and
\(\cos v_j\to\epsilon_v\in\{\pm1\}\).
Define
\[
 x=\lim\epsilon_u H(u_j),\quad
 y=\lim\epsilon_v H(v_j),\quad
 z=\lim\epsilon_u\epsilon_v H(w_j).
\]
The exact identity (5), with \(uv\to\infty\), yields
\[
 z=\frac x\alpha+\frac y\beta+
        b\left(\frac1{\alpha\beta}-1\right).
 \tag{8}
\]
Meanwhile (4) shows
\[
 \lim_j L_j^4\left[k(u_j)^2+k(v_j)^2+k(w_j)^2\right]
 =\frac{A^2}{d^4}
  \left(\frac{x^2}{\alpha^4}+
        \frac{y^2}{\beta^4}+z^2\right).
 \tag{9}
\]
Completing squares (or a two-variable weighted Cauchy--Schwarz inequality) under (8) gives
\[
\begin{aligned}
 \frac{x^2}{\alpha^4}+\frac{y^2}{\beta^4}+z^2
 &\ge
 \frac{b^2(\frac1{\alpha\beta}-1)^2}
          {1+\alpha^2+\beta^2}\\
 &=\frac{b^2(1-\alpha\beta)}{2(\alpha\beta)^2}
 \ \ge\ 6b^2,
\end{aligned}
\tag{10}
\]
because \(0<\alpha\beta\le1/4\) and
\((1-t)/t^2\) strictly decreases for \(0<t\le1/4\).
Since \(d\le1\), every minimizing subsequential limit in (9)
is at least \(6A^2b^2\). This matches (6) and proves the
scaled form
\[
 \lim_{L\to\infty}L^4
 \kappa_\lambda\left(\frac{L}{\pi\lambda}\right)
 =6A^2b^2.
\]
Using \(Ab=\lambda^2/2\) gives exactly (1).

## 3a. Rigidity of every asymptotically sharp triple

**Theorem A' (near-extremizer classification).** Fix \(0<\lambda\le1\) and write \(L_j=\pi\lambda R_j\to\infty\). Suppose \(u_j,v_j\ge0\), \(w_j=u_j+v_j\le L_j\), and
\[
 L_j^4\big(k(u_j)^2+k(v_j)^2+k(w_j)^2\big)
 \longrightarrow 6A^2b^2.
 \tag{10a}
\]
Then
\[
 \frac{w_j}{L_j}\to1,\qquad
 \frac{u_j}{L_j}\to\frac12,\qquad
 \frac{v_j}{L_j}\to\frac12.
 \tag{10b}
\]
Furthermore, there are positive integers \(n_j,m_j\to\infty\) such that
\[
 \boxed{\quad
 u_j=n_j\pi+\frac{3b}{4n_j\pi}+o(L_j^{-1}),\qquad
 v_j=m_j\pi+\frac{3b}{4m_j\pi}+o(L_j^{-1}).\quad}
 \tag{10c}
\]
Thus the two gaps of every asymptotically optimal triple are almost equal, fill the available span, and have the same first-order phase shift relative to their nearest multiples of \(\pi\). The result applies to *any* asymptotically sharp family, not only to exact minimizers of the compact problem.

**Proof.** The compactness and boundary-exclusion argument in Section 3 uses only the bound in (7), not exact minimization. It therefore applies to the family in (10a): along every subsequence one can extract limits \(\alpha,\beta,d,x,y,z\) satisfying (8)--(9), with \(\alpha,\beta>0\), \(\alpha+\beta=1\) and \(0<d\le1\). Put \(t=\alpha\beta\), \(B=b(t^{-1}-1)\), and
\[
 P=\left(\frac{x}{\alpha^2},\frac{y}{\beta^2},z\right),
 \qquad a=(-\alpha,-\beta,1).
\]
Equation (8) says \(a\cdot P=B\). Orthogonal projection onto the normal \(a\) gives the *exact* Pythagorean identity
\[
 \|P\|^2=
 \frac{B^2}{1+\alpha^2+\beta^2}
 +\left\|P-\frac{B}{1+\alpha^2+\beta^2}a\right\|^2
 =
 \frac{b^2(1-t)}{2t^2}
 +\left\|P-\frac{B}{1+\alpha^2+\beta^2}a\right\|^2.
 \tag{10d}
\]
Because \(0<t\le1/4\), the first term is at least \(6b^2\), with equality *only* at \(t=1/4\). Inserting (10d) into (9) and comparing with the assumed sharp limit (10a) forces simultaneously \(d=1\), \(\alpha=\beta=1/2\), and vanishing of the orthogonal remainder. At those parameters \(B=3b\) and \(1+\alpha^2+\beta^2=3/2\), so \(P=(-b,-b,2b)\). Hence \(x=y=-b/4\) and \(z=2b\).

The boundedness of \(H(u_j),H(v_j)\) together with \(u_j,v_j\to\infty\) gives \(\sin u_j,\sin v_j\to0\). Choose the nearest integer multiples \(n_j\pi,m_j\pi\), and set \(\delta_j=u_j-n_j\pi\), \(\epsilon_j=v_j-m_j\pi\). Then \(\delta_j=O(u_j^{-1})\) and \(\epsilon_j=O(v_j^{-1})\). With the signs removed as in Section 3,
\[
 (-1)^{n_j}H(u_j)
   =u_j\sin\delta_j-b\cos\delta_j
   =u_j\delta_j-b+o(1)\to-b/4,
\]
and analogously \(v_j\epsilon_j\to3b/4\). Since \(u_j,v_j\sim L_j/2\), replacing \(u_j,v_j\) by \(n_j\pi,m_j\pi\) in these denominators incurs only \(o(L_j^{-1})\); this gives (10c). Every convergent subsequence has the same forced limiting parameters, so the full sequence satisfies (10b)--(10c). Conversely, the construction in Section 2 attains this phase-locked geometry and the sharp coefficient.

**Boundary of use.** The rigidity is at the artificially free *finite real-frequency* minimization interface, not a statement that zeta ordinates obey or avoid the displayed phase conditions. Excluding these near-extremizers arithmetically would require an independent source-controlled ordinate-spacing input; the off-line indefinite blocks remain untreated.

## 4. Cost of creating an exact smooth orthogonal triple

**Lower bound.** Wang's exact second-variation identity is
\[
 C(f)-C_\lambda
 =\|f-f_*\|_2^2-
  2\left\|\int_{-a}^{\,t}(f-f_*)(v)\,dv\right\|_2^2
 \ge\sigma_\lambda\|f-f_*\|_2^2,
 \tag{11}
\]
where the endpoint-zero primitive permits the Dirichlet Poincare inequality on an interval of length \(\lambda\).
For any admissible orthogonal triple with gaps \(r,s\),
\(\widehat f(r)=\widehat f(s)=\widehat f(r+s)=0\). Fourier Cauchy--Schwarz on the common support of length \(\lambda\) gives, for each gap \(z\),
\[
 |K(z)|=|\widehat{f_*-f}(z)|
 \le\sqrt\lambda\,\|f-f_*\|_2.
\]
Summing the three squares yields
\(\kappa_\lambda(R)\le3\lambda\|f-f_*\|_2^2\),
so (11) proves (3).

**Constructive matching upper bound.** Take the real frequency gap
\(r_R=u/(\pi\lambda)\) from Section 2 and use the ordered locations
\(0,r_R,2r_R\). Their span is at most \(R\), and (4)--(6) give
\[
 |K(r_R)|+|K(2r_R)|=O_\lambda(R^{-2}).
\]
Choose a smooth even cutoff \(\chi_\delta\), equal to one away from endpoint collars of total width \(O(\delta)\), and vanish smoothly before the endpoints. With \(\delta=R^{-4}\), set
\[
 \eta_0=\frac{\chi_\delta\sqrt{f_*}}
                 {(\int\chi_\delta^2f_*)^{1/2}},
 \qquad f_0=\eta_0^2.
\]
The square root is evaluated only inside \((-a,a)\), where \(f_*\) is smooth and strictly positive. Then \(f_0\in\mathcal F_\lambda\),
\(\|f_0-f_*\|_2=O_\lambda(R^{-2})\), and
\[
 \big(\int f_0-1,\widehat f_0(r_R),
                  \widehat f_0(2r_R)\big)
 =(0,O_\lambda(R^{-2}),O_\lambda(R^{-2})).
\]

Fix an even nonnegative nonzero
\(\psi\in C_c^\infty((-a/2,a/2))\).
For \(i,j=0,1,2\) form
\[
 M_{ij}(R)=\int\psi(t)
     \cos(2\pi i r_Rt)\cos(2\pi j r_Rt)\,dt.
\]
By the Riemann--Lebesgue lemma,
\(M(R)\to\mathrm{diag}(J,J/2,J/2)\), \(J=\int\psi>0\);
therefore \(M(R)^{-1}\) is uniformly bounded for large \(R\).
Solve the *exact* linear system
\[
 M(R)a=-
 \big(0,\widehat f_0(r_R),\widehat f_0(2r_R)\big)^{\mathsf T},
 \qquad a_j=O_\lambda(R^{-2}),
\]
and define
\[
 f_R(t)=f_0(t)+\psi(t)\sum_{j=0}^2
          a_j\cos(2\pi j r_Rt).
 \tag{12}
\]
The three equations enforce, exactly,
\(\int f_R=1\), \(\widehat f_R(r_R)=0\), and
\(\widehat f_R(2r_R)=0\). The perturbation is supported in a fixed compact subset where \(f_0\) has a positive lower bound independent of large \(R\), and its uniform size is \(O_\lambda(R^{-2})\). Hence \(f_R\) is nonnegative, is strictly positive on the perturbation support, and can be written \(f_R=\eta_R^2\) with an even real \(\eta_R\in C_c^\infty((-a,a))\): outside that compact set use \(\eta_0\), while on it the positive smooth square root is well-defined and joins smoothly. Finally
\[
 \|f_R-f_*\|_2=O_\lambda(R^{-2}),\qquad
 0<C(f_R)-C_\lambda\le\|f_R-f_*\|_2^2
   =O_\lambda(R^{-4}),
\]
by Wang's upper second-variation identity. The strict inequality follows from uniqueness: a compactly supported smooth \(f_R\) cannot equal the endpoint-discontinuous \(f_*\).
This proves the matching upper bound in (2) with a **genuinely smooth, positive, normalized, exactly orthogonal** test.

## Source boundary, controls, and novelty audit

- **Compact-span falsifier:** At any fixed finite \(R\), (1) does not nullify WI-445; \(\kappa_\lambda(R)>0\). The exact optimizer admits no orthogonal real triple, whereas the smooth tests constructed in (12) pay nonzero positive variational cost.
- **Arithmetic/spacing boundary:** The minimizing near-zero overlaps arise from three real frequencies spread across span comparable with \(R\). Their spacing is constructed freely, and the smooth test itself depends on \(R\). Neither the spacing nor the test family is supplied for the actual zeta ordinates. In Wang's zeta argument, each smooth test is fixed before \(T\to\infty\); no uniform short-interval pair-correlation bound for \(R\)- or \(T\)-dependent tests is inferred.
- **Indefinite-block boundary:** Only the real-frequency positive Gram sector is controlled. Off-critical conjugate blocks contribute indefinite terms and may offset a real-only Gram charge. A new arithmetic source-controlled inequality would be needed before applying this span law to off-line-zero exclusion.
- **Degenerate control:** At \(\lambda\downarrow0\), the normalized cosine window tends after rescaling toward a rectangle, whose sinc-transform zeros admit exact orthogonal lattices; the proof fixes \(\lambda>0\) before sending \(R\to\infty\), and its error constants depend on \(\lambda\).
- **Checkable tests:** Recompute (4) by direct cosine integration including the removable points \(u=\pm c\); verify (5) by the sine/cosine addition formulas; check the coefficient \(3b/(4n\pi)\) and the \(6A^2b^2\) asymptotic; search separately for boundary minimizing sequences with one gap bounded, with one gap sublinear, and with total span sublinear (each is ruled out in Section 3); check invertibility, normalization and positivity in (12).
- **Prior art:** Wang's optimizer, variational identity and admissible smooth class are primary-source results, not Mathia discoveries. Orthogonal exponentials as Fourier zeros, trigonometric addition, finite cosine interpolation and Riemann--Lebesgue are classical Fourier-analysis tools (e.g. Stein--Shakarchi, *Fourier Analysis: An Introduction*, Princeton, 2003). A targeted comparison with neighboring Fourier-zero and spectral-measure literature did not establish independent priority for the **specific** sharp quartic constant. No claim of an original general method, or first publication of this specialization, is made.

## Consequence for Weil inertia and RH

WI-445 gives an exact positive charge for three real optimizer frequencies at every fixed span. WI-446 rules out a uniform global extension over near-optimal admissible smooth windows. The present result resolves the quantitative interface between them: the best optimizer triple charge at span \(R\) is asymptotic to \(3/(2\pi^4R^4)\), and engineering one exactly orthogonal triple into an admissible smooth near-minimizer costs precisely order \(R^{-4}\) in Wang's variational functional. Therefore any proposed Gram-based improvement that relies on bounded-span rigidity must pay explicit attention to the spatial scale, distribution of actual critical-line ordinates, the order of smooth-test limits, and the indefinite off-line blocks.

This finite harmonic-analysis result supplies no new prime-side support, no unconditional increase in the certified simple-critical percentage, no independent individual off-line-zero coercivity, and **does not prove RH**.
