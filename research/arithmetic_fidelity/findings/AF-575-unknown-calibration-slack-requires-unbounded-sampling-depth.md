# AF-575 — Unknown calibration slack requires unbounded sampling depth

## Status and question

EXACT-DERIVED · LITERATURE+DERIVED · ARITHMETIC-FIDELITY · ADAPTIVE-STOPPING · MATCHED-CONTROL · NO-GENERAL-NOVELTY-CLAIM

AF-572–AF-574 choose the sampling geometry using a **known** smooth-calibration budget. Replace that knowledge by the promise that the budget is strictly below the exact alias threshold, without a supplied distance from the threshold. This changes the observation problem: no uniformly bounded number of adaptive value queries suffices, even without noise. Nevertheless, one sequential procedure identifies every admissible noiseless input after finitely many queries. Its stopping depth is not uniform over the promised class.

This is a distinction between a finite query bound and input-dependent finite termination. It is not a claim that the known-budget results fail, or that adaptive numerical differentiation is new.

## Experiment and theorem

Fix an integer \(n\ge1\), a known finite set \(S=\{p_1<\cdots<p_m\}\), \(m\ge2\), of sufficiently large rational-prime edit locations, and a sufficiently small fixed window \(0<a\le A\). Retain
\[
 P(s)=\sum_{\ell\ {\rm prime}}\ell^{-s},\qquad
 h_p(s)=p^{-s}-(p+1)^{-s},\qquad
 \Phi_p(a)=(P-h_p)^{-1}(E_1(a)),\qquad
 E_1(a)=\int_a^\infty e^{-u}\frac{du}{u}.
\tag{1}
\]
Put \(\sigma=(-1)^{n-1}\), \(F_i=\sigma\Phi_{p_i}\), and \(g_i=F_{i+1}-F_i\). AF-571/572 give a window, independent of any calibration slack, on which
\[
 g_i^{(n)}(a)>0,\qquad g_i^{(n+1)}(a)<0,
 \qquad d:=\min_i g_i^{(n)}(0)>0.
\tag{2}
\]
The sign change of the entire observation is known and preserves all nuisance and noise norms. We therefore write the observation directly as
\[
 y(a)=F_i(a)+b(a)+\eta(a),\qquad
 b\in\mathcal B^\circ:=\{b\in C^n[0,A]:\|b^{(n)}\|_\infty<d/2\},
 \qquad |\eta(a)|\le\varepsilon.
\tag{3}
\]
One function \(b\) is shared by all queries in an experiment; competing hypotheses may have different functions. Lower polynomial coefficients are unrestricted. The source set, curves, \(n,A,d\), and, when present, the noise bound are known. The actual
\[
 L=\|b^{(n)}\|_\infty<d/2,\qquad \delta=d-2L>0
\tag{4}
\]
are **not** supplied to the procedure. This is the union of AF-572's subcritical budget classes, not one fixed known budget class.

The following statements hold in the exact real-valued query model.

1. For every finite \(N\), no deterministic policy using at most \(N\) positive-coordinate value queries identifies every input in (3), even when \(\varepsilon=0\). This includes policies choosing each coordinate from earlier responses.
2. A single procedure, independent of \(L\), identifies every noiseless input after finitely many queries. It uses prescribed geometrically shrinking blocks and response-dependent stopping. For fixed sources and order, its sufficient stopping depth is \(O(1+\log_+(KA/\delta))\), where
   \[
   K=\max_i\|g_i^{(n+1)}\|_{C[0,A]}>0.
   \tag{5}
   \]
   Here \(\log_+x=\max(0,\log x)\). This is an upper bound for this procedure, not an optimal query-complexity law.
3. For every fixed \(\varepsilon>0\), even the full observation curve has an ambiguity somewhere in the promised class. Its uniform deterministic-noise identification radius is zero.
4. A noise-aware version of the same stopping certificate is still valid on every input. It is guaranteed to terminate when a scale \(h=A2^{-j}\) satisfies
   \[
   Kh+2\kappa_n\varepsilon h^{-n}<\delta/2,
   \qquad \kappa_n=[2(n+1)]^n.
   \tag{6}
   \]
   In particular, in the near-threshold regime \(0<\delta\le4KA\), a sufficient condition is
   \[
   \boxed{\displaystyle
   \varepsilon<\frac{\delta^{n+1}}{8^{n+1}\kappa_n K^n}.}
   \tag{7}
   \]
   The constants are not claimed sharp. Without such separation, the procedure need not terminate. Statement 3 rules out a positive noise guarantee uniform over all unknown slacks.

## A common transcript defeats every finite query bound

Choose an adjacent pair attaining \(g^{(n)}(0)=d\), and let \(M=(F_i+F_{i+1})/2\). Feed a policy the responses \(M(a)\) at its queried coordinates. Consider any finite nonempty prefix, and let \(u>0\) be its smallest queried coordinate. Define
\[
 J_u(a)=
 \begin{cases}
 \displaystyle\sum_{r=0}^n\frac{g^{(r)}(u)}{r!}(a-u)^r,&0\le a\le u,\\
 g(a),&u\le a\le A.
 \end{cases}
\tag{8}
\]
All derivatives through order \(n\) match at \(u\). Positivity and strict decrease in (2) give
\[
 J_u\in C^n[0,A],\qquad
 \|J_u^{(n)}\|_\infty=g^{(n)}(u)<d.
\tag{9}
\]
Thus \(b_i=J_u/2\) and \(b_{i+1}=-J_u/2\) are both in \(\mathcal B^\circ\), and their observations equal \(M\) at every coordinate in the prefix. These are fixed functions realizing the whole prefix; the nuisance is not changed between its queries.

If the policy stops on this prefix, it is wrong on one of these two admissible inputs. If it has not stopped after \(N\) responses, either admissible realization violates a claimed uniform \(N\)-query bound. The empty-prefix case is immediate. The full midpoint curve itself is a critical-budget observation and is excluded from the strict promise. That exclusion permits an input-dependent terminating procedure while forcing it to continue forever along the hypothetical midpoint transcript. The witness may depend on the finite prefix, which suffices for the worst-case lower bound; one subcritical witness for the entire infinite transcript is neither asserted nor needed.

This proof also covers a guarantee required for every realization of a randomized policy by fixing its random seed. It does not establish lower bounds for weaker probabilistic success guarantees.

## A finite stopping certificate without the missing budget

For a scale \(h\le A\), query the \(n+1\) distinct positive nodes
\[
 t_r=\frac{r+1}{n+1}h\quad(0\le r\le n),\qquad
 D_hv=n!\sum_{r=0}^n
 \frac{v(t_r)}{\prod_{s\ne r}(t_r-t_s)}.
\tag{10}
\]
The classical divided-difference mean-value theorem says that \(D_hv=v^{(n)}(\xi)\) for some \(\xi\) between the extreme nodes when \(v\in C^n\). In particular,
\[
 |D_hb|\le L,
 \qquad D_hg_i\ge g_i^{(n)}(0)-Kh\ge d-Kh.
\tag{11}
\]
The coefficient norm in (10) is exactly
\[
 \|D_h\|=n!\left(\frac{n+1}{h}\right)^n
 \sum_{r=0}^n\frac1{r!(n-r)!}
 =\kappa_n h^{-n}.
\tag{12}
\]
This identity also bounds arbitrary, possibly discontinuous, observation noise: no differentiability of \(\eta\) is assumed.

Compute \(z_h=D_hy\), the known centers \(c_i(h)=D_hF_i\), and \(B_h=\kappa_n\varepsilon h^{-n}\). Retain the candidate set
\[
 I_h=\{i:|z_h-c_i(h)|<d/2+B_h\}.
\tag{13}
\]
The strict inequality is justified because the actual nuisance norm is strictly below \(d/2\). The true source always belongs to \(I_h\). Whenever this set is a singleton, stop and report its source; otherwise query the next scale \(h/2\). Keeping intersections with earlier sets is optional and is not used in the proof.

The centers are strictly ordered by (2) and (10). At a scale with \(Kh<d\), every distinct pair of centers has separation at least \(d-Kh\), since a nonadjacent difference is a sum of positive adjacent differences. If the true index is \(i\), then for every other \(j\),
\[
 |z_h-c_j(h)|
 \ge d-Kh-L-B_h
 =d/2+\delta/2-Kh-B_h.
\tag{14}
\]
Condition (6) makes this larger than \(d/2+B_h\), so every false candidate is excluded. For zero noise, eventually \(Kh<\delta/2\), proving finite termination. At most \((n+1)(j+1)\) queries have been used by block \(j\); repeated nodes may be reused. For example, any integer \(j>\log_2(2KA/\delta)\), with \(j\ge0\), is sufficient.

For (7), take the first dyadic scale with \(h\le\delta/(4K)\). Under \(\delta\le4KA\), it lies in
\[
 \delta/(8K)<h\le\delta/(4K).
\]
Then \(Kh\le\delta/4\), and (7) gives \(2B_h<\delta/4\), proving (6). The procedure does not need to know which block has this property. The construction uses a classical differentiation contrast; its function here is an honest finite exclusion certificate against the entire unknown-budget class.

## Why the full curve has no uniform positive noise margin

For the weakest pair used in (8), choose \(0<\alpha<1\). The two nuisances
\[
 b_i=\alpha g/2,\qquad b_{i+1}=-\alpha g/2
\tag{15}
\]
have norm \(\alpha d/2<d/2\). Their noiseless curves differ by \((1-\alpha)g\). Choose \(\alpha\) close enough to one that \((1-\alpha)\|g\|_\infty/2\le\varepsilon\). Adding opposite errors \(\pm(1-\alpha)g/2\) makes both full observations exactly \(M\). Therefore no full-curve rule can identify every input at that positive noise level.

At zero noise the full classes are disjoint: the order-\(n\) endpoint derivative of a difference of two admitted nuisances has absolute value strictly less than \(d\), while every distinct signed source gap has that derivative at least \(d\). The uniform norm closures nevertheless meet at the midpoint. Thus exact separation, finite certification, bounded query count, and a uniform noise margin are four distinct assertions in this same source family.

## Arithmetic realization, controls, and limits

The source input (2) is the all-order alternating boundary-jet law already derived in AF-571 by integrating the positive real-edit sensitivity, not by subtracting uncontrolled asymptotic errors:
\[
 [a^r](\Phi_q-\Phi_p)
 =(-1)^{r-1}\frac{c^r}{(r-1)!}\Delta_{p,q}(\log p)^{r-1}
 [1+O_r(1/\log p)],\quad
 c=e^{B_1},\quad \Delta_{p,q}=\frac1{p(p+1)}-\frac1{q(q+1)}>0.
\tag{16}
\]
Here \(B_1\) is the Meissel–Mertens constant. For fixed \(n\), applying (16) at orders \(n,n+1\), then fixing a finite sufficiently remote \(S\) and shrinking \(A\), gives precisely (2) and finite \(K\). For a pair, the critical derivative and its initial decrease are
\[
 d=n c^n\Delta_{p,q}(\log p)^{n-1}[1+O_n(1/\log p)],\qquad
 -g^{(n+1)}(0)=(n+1)c^{n+1}\Delta_{p,q}(\log p)^n
 [1+O_n(1/\log p)].
\tag{17}
\]
Consequently the promise and the finite-transcript witnesses are realized on the registered prime-edit construction, rather than only on abstract function classes. As in AF-572, all source thresholds and window choices precede the unknown-slack experiment. No simultaneous prime/order/window/slack asymptotic is claimed.

An exact analytic control is \(F_0=0\), \(F_1=a^n/n!-a^{n+1}/(n+1)!\) on \([0,1/2]\). Here \(d=K=1\), \(g^{(n)}=1-a\), and
\[
 D_hg=1-\frac{n+2}{2(n+1)}h.
\tag{18}
\]
For the true source \(F_0\) with \(b=(1-\delta)a^n/(2n!)\), \(0<\delta\le1\), and no noise, the singleton test occurs exactly when \(h\le\delta(n+1)/(n+2)\). Equality excludes the false candidate because (13) uses an open interval. The Taylor extension (8) has derivative norm \(1-u\), verifying the strict-slack ambiguity directly. Exact rational arithmetic checked (10)–(12), (18), the Taylor join, and 420 extreme-sign noise cases for \(n=1,2,3,4\) over seven slack scales satisfying (7). These are controls of the formulas; the arbitrary-order and prime statements rest on the derivations above.

The procedure assumes exact source constants and exact noiseless real observations in statements 1–2. Numerical source-evaluation error, finite arithmetic precision, input-coordinate uncertainty, or a minimum accessible coordinate require additional error bounds. In particular, keeping all queries above a fixed \(u>0\) leaves the exact ambiguity (8). Equation (12) makes the precision cost of endpoint access explicit.

## Prior art and consequence

The distinction between fixed and response-dependent information cardinality is classical: [Wasilkowski (1986), §§1–3, *Information of varying cardinality*](https://doi.org/10.1016/0885-064X(86)90002-6), studies termination functions and worst-case/average-case information in linear Banach-space problems. Its general setting is different from this discrete source label on a union of translated open nuisance classes; its linear-problem optimality results are not invoked as a theorem for this experiment. [De Boor (2005), §§8–9, *Divided Differences*](https://arxiv.org/abs/math/0502036) supplies the classical normalized derivative, positivity, and coefficient formulas behind (10)–(12). No novelty is claimed for adaptive stopping, differentiation, or interpolation adversaries.

The source-specific delta is a precise limit on transporting AF-572–AF-574's known-budget finite-probe conclusions to an **unknown strictly subcritical** calibration class. Exact identification survives with input-dependent finite stopping; every uniform finite query bound fails, and the full-curve uniform positive noise radius disappears. The noise-aware certificate also identifies a sufficient slack/precision regime without learning the nuisance norm first. Its \(\delta^{n+1}\) sufficient power agrees with the sharp quadratic and cubic known-budget margin powers at \(n=1,2\), but no sharp higher-order margin or optimal stopping rate is asserted.

These are generalized-prime matched controls indexed by rational-prime edits. The result supplies neither an ordinary-prime discriminator nor an RH implication. A physical representation still needs to provide the stated common coordinate, known source class and critical threshold, and the calibration law and precision needed for the certificate.
