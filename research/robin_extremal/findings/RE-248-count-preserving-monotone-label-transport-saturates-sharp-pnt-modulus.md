# RE-248 — Count-preserving monotone label transport saturates the sharp terminal PNT modulus

**Status:** EXACT-DERIVED + QUANTITATIVE-PNT-FIDELITY + RANK-PRESERVING-TRANSPORT + SHARP-MATCHED-SOURCE-OBSTRUCTION + PRIOR-ART-BOUNDED.

**Parent findings:** RE-153, RE-155, RE-156, RE-238, RE-246, RE-247.

RE-247 proved that the maximal terminal ambiguity of the normalized Robin-kernel source functional, among discrete generalized-prime sources with a common unit Korobov–Vinogradov Chebyshev envelope and an identical prefix, is \((2+o(1))B_{p,b,U}\). Its saturating sources place fresh labels against prescribed monotone Chebyshev targets and *need not retain the original number of labels in the terminal shell*. The cardinality freedom is not necessary. The same sharp constant is attained by two **order-preserving transports of the very same indexed prime-like labels**, supported strictly inside the shell, retaining the exact shell cardinality and the logarithmic scale of every neighboring gap.

## 1. Statement and the strengthened control class

Fix \(b>0\), \(0<\alpha<3/4\), and let \(p\to\infty\), \(U=U(p)\), \(U/p\to\infty\). Put
\[
T=e^{-2}U,\qquad V(t)=\frac{(\log t)^{3/5}}{(\log\log t)^{1/5}},
\qquad E(t)=t e^{-bV(t)},\qquad
B_{p,b,U}=\frac{\sqrt p\log p}{\log U}e^{-bV(U)}.
\tag{1}
\]
Use the exact functional and normalization of RE-247:
\[
h(t)=\frac{-\log(1-t^{-1})}{\log t},\quad
Z_{p,U}=\sqrt p\log p\int_{p+p^\alpha}^{U}\sqrt t\,(-h'(t))dt=2+o(1),
\]
\[
\mathcal A_{p,U}(Q)
=\frac{\sqrt p\log p}{Z_{p,U}}
 \int_{p+p^\alpha}^{U}(t-\vartheta_Q(t))(-h'(t))dt,\quad
\vartheta_Q(t)=\sum_{q\in Q,\ q\le t}\log q.
\tag{2}
\]
Here a source is a strictly increasing, unbounded sequence of distinct real labels \(q>1\); no assertion is made about its generalized-integer counting function.

**Theorem (sharp modulus with fixed rank and gap scale).** There exist a fixed generalized-prime source \(Q_*=\{q_j\}_{j\ge1}\), a fixed \(t_0=t_0(b)\), and, for every sufficiently large \(p\), sources
\(Q_p^+=\{q_{p,j}^+\}_{j\ge1}\) and \(Q_p^-=\{q_{p,j}^-\}_{j\ge1}\) such that:

1. \(q_{p,j}^\pm=q_j\) whenever \(q_j\notin(T,U)\). Every other label is moved *within* \((T,U)\), and the map \(q_j\mapsto q_{p,j}^\pm\) preserves the full order and indexing. Thus both sources have exactly the same number of labels as \(Q_*\) in \((T,U)\), and their exterior label sets coincide exactly.
2. All sources satisfy the same **unit**, all-height Chebyshev envelope
   \[
   |\vartheta_Q(t)-t|\le E(t)\quad(t\ge t_0),
   \qquad Q\in\{Q_*,Q_p^+,Q_p^-\}.
   \tag{3}
   \]
3. Both transports are uniformly bi-Lipschitz in label position: for all consecutive labels, once \(p\) is large,
   \[
   \frac45\le\frac{q_{p,j+1}^\pm-q_{p,j}^\pm}{q_{j+1}-q_j}\le\frac43.
   \tag{4}
   \]
   In particular, gaps in the terminal shell remain comparable to \(\log U\), with no densely concentrated label packet.
4. Nevertheless,
   \[
   \boxed{
   \mathcal A_{p,U}(Q_p^-)-\mathcal A_{p,U}(Q_p^+)
     =(2+o(1))B_{p,b,U}.
   }
   \tag{5}
   \]

Let \(\Delta_{p,b,U}^{\mathrm{tr}}\) be the supremum in RE-247 restricted to pairs produced from this fixed \(Q_*\) by order-preserving, shell-supported transports satisfying (3) and (4). RE-247's upper bound and (5) therefore give
\[
\boxed{\Delta_{p,b,U}^{\mathrm{tr}}
       =(2+o(1))B_{p,b,U}
       =\Delta_{p,b,U}(1+o(1)).}
\tag{6}
\]
Thus the exact rigidity criterion and the rescaled critical-horizon limit of RE-247 remain sharp even after fixing shell cardinality, individual label ranks, all exterior labels, and the local separation scale. The transports *do not* preserve the counting function at each intermediate point of the shell, nor do they produce ordinary primes.

## 2. Fixed baseline and monotone rank transport

Take the fixed source used in RE-246 and RE-247:
\[
q_1=2,\qquad q_{j+1}-\log q_{j+1}=q_j.
\tag{7}
\]
The function \(x-\log x\) is strictly increasing for \(x>1\), so (7) defines an increasing unbounded sequence. Summation gives
\[
\vartheta_{Q_*}(q_j)=q_j-(2-\log2),\qquad
\vartheta_{Q_*}(t)=t+O(\log t).
\tag{8}
\]
Each gap at height \(t\) is \(\asymp\log t\). In the shell the number \(N\) of baseline labels satisfies \(N=O(U/\log U)\): their logarithmic weights are at least \(\log T\), whereas the difference of the two Chebyshev steps in (8) is \(U-T+O(\log U)=O(U)\).

Set
\[
\delta=(\log U)^{-1/2},\quad a=1-\delta,\quad w=8E(U),
\]
\[
\phi(t)=\min\left\{\frac{t-T}{w},\,1,\,\frac{U-t}{w}\right\}
\quad(T\le t\le U),\qquad
H_\pm(t)=t\pm a\phi(t)E(t).
\tag{9}
\]
Because \(E(U)/U=e^{-bV(U)}\to0\), the ramps fit disjointly inside the shell, their total length is \(2w=o(U)\), and \(\phi(T)=\phi(U)=0\). The derivative of the envelope is
\[
E'(t)=e^{-bV(t)}(1-btV'(t))=o(1)
\quad\text{uniformly on }[T,U],
\tag{10}
\]
since \(tV'(t)=o(1)\) and \(V(T)=V(U)+o(1)\). Where differentiable,
\[
|H_\pm'(t)-1|
\le a\left(\frac{E(U)}w+\sup_{[T,U]}|E'|\right)
=\frac18+o(1).
\tag{11}
\]
In particular \(3/4\le H_\pm'\le5/4\) for large \(U\). Extend \(H_\pm\) as the identity outside \([T,U]\). Each extension is a continuous increasing homeomorphism of \([2,\infty)\), fixes \(T,U\), and is globally bi-Lipschitz with the same bounds.

Define the transported labels by the explicit **index-by-index** rule
\[
\boxed{q_{p,j}^\pm=H_\pm^{-1}(q_j)\quad(j\ge1).}
\tag{12}
\]
The inverse maps are increasing, so they preserve strict order, and identity outside the shell gives the exact exterior matching and cardinality statement. Taking inverse Lipschitz constants in (11) proves (4), even for gaps crossing \(T\) or \(U\).

## 3. Quantitative Chebyshev control despite changed logarithmic weights

The key point is to control *both* displacement of jump locations and the fact that a generalized prime at its new position carries weight \(\log q_{p,j}^\pm\), not the old weight \(\log q_j\).

For \(t\in[T,U]\), put \(H=H_\pm\). Since \(H(t)\in[T,U]\) and the exterior labels are fixed, the Chebyshev steps satisfy the exact identity
\[
\vartheta_{Q_p^\pm}(t)
=\vartheta_{Q_*}(H(t))
+\sum_{\substack{q_j\in(T,H(t)]}}
\log\frac{H^{-1}(q_j)}{q_j}.
\tag{13}
\]
The maximum shift of any shell label is at most \(aE(U)\), because if \(r=H^{-1}(q)\), then \(|r-q|=|r-H(r)|\le aE(U)\). Since \(r,q\ge T\),
\[
\left|\log\frac rq\right|
\le\frac{|r-q|}{T}\le\frac{E(U)}{T}.
\tag{14}
\]
Together with \(N=O(U/\log U)\) and \(T=e^{-2}U\), this yields the **uniform** bound
\[
\sum_{q_j\in(T,U)}
\left|\log\frac{H^{-1}(q_j)}{q_j}\right|
=O\!\left(\frac{E(U)}{\log U}\right).
\tag{15}
\]
Combining (8), (9), (13), and (15),
\[
\vartheta_{Q_p^\pm}(t)
=t\pm a\phi(t)E(t)
+O\!\left(\log U+\frac{E(U)}{\log U}\right)
\quad(T\le t\le U),
\tag{16}
\]
with an error uniform in \(t\) and the sign.

Throughout the fixed multiplicative shell, \(E(t)\asymp E(U)\) (indeed \(E(t)/E(U)=t/U+o(1)\) uniformly). Moreover \(E(U)/\log U\to\infty\), while
\[
\frac{\log U+E(U)/\log U}{\delta E(t)}
=O((\log U)^{-1/2})+o(1)\to0.
\tag{17}
\]
Thus the margin \(\delta E(t)\) from \(a=1-\delta\) absorbs every error in (16), proving the unit envelope (3) inside \([T,U]\), including both ramps and their endpoints.

For \(t<T\) the sources are identical to \(Q_*\). Choose \(t_0=t_0(b)\) once so that \(|\vartheta_{Q_*}(t)-t|\le E(t)/4\) for every \(t\ge t_0\), possible by (8). For \(t\ge U\), the entire transported shell has been passed and
\[
\vartheta_{Q_p^\pm}(t)-\vartheta_{Q_*}(t)
=\sum_{q_j\in(T,U)}
\log\frac{H_\pm^{-1}(q_j)}{q_j}
=O\!\left(\frac{E(U)}{\log U}\right).
\tag{18}
\]
The function \(E(t)\) is eventually increasing, so the last error is \(o(E(t))\) uniformly for \(t\ge U\); the baseline occupies at most one quarter of the unit envelope. Therefore (3) holds on the **entire ray** with the same \(t_0\) and envelope constant for both transports and the fixed baseline.

## 4. Exact asymptotic Robin-kernel separation

RE-247's exact matched-source subtraction identity, applicable because both sources coincide through \(T\), gives
\[
\mathcal A_{p,U}(Q_p^-)-\mathcal A_{p,U}(Q_p^+)
=\frac{\sqrt p\log p}{Z_{p,U}}
 \int_T^U
 (\vartheta_{Q_p^+}(t)-\vartheta_{Q_p^-}(t))(-h'(t))dt.
\tag{19}
\]
Subtract (16):
\[
\vartheta_{Q_p^+}(t)-\vartheta_{Q_p^-}(t)
=2a\phi(t)E(t)
+O\!\left(\log U+\frac{E(U)}{\log U}\right).
\tag{20}
\]
The exact positive kernel obeys
\[
-h'(t)
=\frac1{t(t-1)\log t}
 +\frac{-\log(1-t^{-1})}{t(\log t)^2}
=\frac{1+o(1)}{t^2\log t}
\quad(T\le t\le U).
\tag{21}
\]
Consequently
\[
W_{p,U}:=\int_T^U E(t)(-h'(t))dt
=(2+o(1))\frac{e^{-bV(U)}}{\log U},
\quad
\int_T^U(-h'(t))dt=O\!\left(\frac1{U\log U}\right).
\tag{22}
\]
Only the two ramps, of combined length \(2w=16E(U)=o(U)\), have \(\phi\ne1\). Their missing weighted mass is
\[
0\le W_{p,U}-\int_T^U\phi(t)E(t)(-h'(t))dt
=O\!\left(\frac{wE(U)}{U^2\log U}\right)
=O\!\left(\frac{e^{-2bV(U)}}{\log U}\right)
=o(W_{p,U}).
\tag{23}
\]
The integrated error in (20) is likewise
\[
O\!\left(\frac1U+\frac{e^{-bV(U)}}{(\log U)^2}\right)
=o(W_{p,U}).
\tag{24}
\]
Putting (19)--(24) together and using \(a\to1\), \(Z_{p,U}\to2\),
\[
\mathcal A_{p,U}(Q_p^-)-\mathcal A_{p,U}(Q_p^+)
=\frac{\sqrt p\log p}{2+o(1)}
\,2(1+o(1))\,
\frac{(2+o(1))e^{-bV(U)}}{\log U}
=(2+o(1))B_{p,b,U}.
\tag{25}
\]
The upper bound of RE-247 applies to this more restrictive subclass, proving (6). In particular the critical layer \( \log U=v_*(\log p)+s\,v_*(\log p)/\log p+o(v_*/\log p)\) still has transport-limited ambiguity tending to \(2e^{-3s/10}\), with \(v_*\) defined precisely in RE-247.

## 5. Scope, prior art, and decisive checks

The mathematical delta from RE-247 is not a stronger unconstrained upper bound: it is the **exact persistence of the upper constant after adding rank, shell-cardinality, exterior-matching, and bounded-gap-distortion constraints**. The earlier monotone-target discretization attained the full envelope by adjusting the number of shell labels. Formula (12) replaces that freedom by a monotone quantile transport, while (13)--(18) prove that the altered logarithmic jump weights do not consume the necessary Chebyshev margin. RE-155 and RE-246 previously used equal-cardinality deletions and insertions, but neither saturated the *unit quantitative PNT* modulus while preserving each label's rank and gap scale.

Monotone transport of ordered point sequences and discrete approximation of increasing distribution functions are elementary general mechanisms. The general flexibility of Beurling generalized primes is classical (for context: W.-B. Zhang, *Normalization of Beurling generalized primes with Riemann Hypothesis*, Ann. Univ. Sci. Budapest. Sect. Comput. 39 (2013), DOI 10.71352/ac.39.459; H. Diamond and W.-B. Zhang, *Optimality of Chebyshev bounds for Beurling generalized numbers*, Acta Arith. 160 (2013), 259–275, DOI 10.4064/aa160-3-3). Those works concern generalized-prime systems and their counting properties, not an imported theorem asserting this Robin-kernel constrained sharpness. The proof uses no new external analytic estimate; the Korobov–Vinogradov background and its role in the ordinary-prime comparison are already anchored in SOURCES.md.

Essential falsification checks are: (i) the maps must fix *both* shell endpoints, or shell cardinality and exterior rank matching could fail; (ii) the transported log weights in (13) cannot be replaced silently by old weights; (iii) the uniform error (15), including the \(t\ge U\) residual, must fit the **same unit envelope**; (iv) every transported gap, including those straddling a shell endpoint, must remain comparable to its original gap; (v) the two boundary ramps must occupy \(o(U)\), while their derivatives remain bounded, for (23) to hold; and (vi) the complete endpoint-subtracted kernel and \(Z_{p,U}\to2\) are needed for the constant in (25).

Nothing here forces the *ordinary* prime sequence to admit such deformations, controls the intermediate counting staircase pointwise, or establishes a generalized-CA extremal state satisfying Robin's hypotheses. The result concerns the exact information content of a matched generalized-prime PNT envelope and a truncated source observable, not a new inequality for actual divisor sums. A positive Robin theorem must use additional ordinary-prime/source-selector information beyond this constrained source class; RH is not proved.