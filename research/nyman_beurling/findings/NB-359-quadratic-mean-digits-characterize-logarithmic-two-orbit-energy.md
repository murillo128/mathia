# NB-359 — Quadratic-mean digits characterize logarithmic two-orbit energy

- **Status:** proved (classical continued-fraction estimates plus author derivation; independent adversarial review pending)
- **Research line:** `nyman_beurling`
- **Depends on:** NB-354 for the real-orbit spaces and projected target; NB-355 and NB-357 for the two-cutoff physical-energy bracket
- **Classification:** LITERATURE+DERIVED + EXACT-ENDPOINT-CLASSIFICATION

## Claim and scope

The logarithmic endpoint left outside NB-358's positive-power classification is governed by the **quadratic mean** of the continued-fraction digits of the seed log ratio. Bounded digits are sufficient but not necessary. This is a specialization of classical reciprocal-sum geometry to the physical component cost of the projected Nyman target, not a new Diophantine theorem.

In \(H=L^2(0,1;dx)\), set
\[
e=1,\quad g_j(x)=\{1/(jx)\}-j^{-1}\{1/x\},\quad
A_af(x)=\sqrt a f(ax)\mathbf1_{x\le1/a},\quad
\mathcal C_j=\overline{\operatorname{span}}\{A_ag_j:a\ge1\text{ real}\}.
\]
Fix real seeds \(p,q>1\) with irrational \(\alpha=\log p/\log q\). Let \(\mathcal N\) be the full continuous Nyman space, \(t=P_{\mathcal N}e\), and \(b=B(1)>0\) its normalized Burnol factor. Write
\[
\mathcal E(\varepsilon)=\inf\{\|u\|^2+\|v\|^2:
 u\in\mathcal C_q,\ v\in\mathcal C_p,\ \|t-u-v\|\le\varepsilon\}.
\tag{1}
\]
For the regular continued fraction \(\alpha=[a_0;a_1,a_2,\ldots]\), define
\(S_m=\sum_{j=1}^m a_j^2\). Then
\[
\boxed{\mathcal E(\varepsilon)\asymp\log(1/\varepsilon)
\quad\Longleftrightarrow\quad
\sup_{m\ge1}\frac{S_m}{m}<\infty.}
\tag{2}
\]
Equivalently, the upper bound \(O(\log(1/\varepsilon))\) alone characterizes the same digit class; NB-355 supplies the universal matching lower bound. Constants may depend on the fixed seeds and \(b\).

The condition strictly contains badly approximable ratios. Conversely, the explicit ratio
\(\alpha_*=[0;1,2,3,4,\ldots]\), realized by \(p=q^{\alpha_*}\) for any fixed \(q>1\), has
\[
\boxed{\mathcal E(\varepsilon)\asymp
\left(\frac{\log(1/\varepsilon)}{\log\log(1/\varepsilon)}\right)^3.}
\tag{3}
\]
Thus a subpolynomial energy law need not have logarithmic order. These assertions concern complete real-dilation orbit vectors and squared physical norms, not finite generator counts or discrete Nyman sections.

## 1. The physical-energy reduction retains both cutoff scales

Put
\[
\delta_n=\|n\alpha\|_{\mathbb R/\mathbb Z},\qquad
W(X)=\sum_{1\le n\le X}\frac1{n^2\delta_n^2}.
\]
NB-355 and NB-357 give, for all sufficiently small positive \(\varepsilon\),
\[
c_1 W(c_2/\varepsilon)
\le\mathcal E(\varepsilon)
\le C_1\bigl(1+W(\lceil C_2/\varepsilon^2\rceil)\bigr),
\tag{4}
\]
with fixed positive constants. In particular,
\[
\mathcal E(\varepsilon)=O(\log(1/\varepsilon))
\quad\Longleftrightarrow\quad W(X)=O(\log X).
\tag{5}
\]
For necessity set \(\varepsilon=c_2/X\) in the lower bound. For sufficiency apply the upper bound and \(\log\lceil C_2/\varepsilon^2\rceil\asymp\log(1/\varepsilon)\). No equivalence between the two cutoffs for an arbitrary irrational is asserted.

The full-norm content of (4) matters. In the unitary Mellin model,
\[
\mathcal M\mathcal C_j=B\Theta_jH^2,\qquad
\Theta_j(s)=\frac{s}{s-1}\frac1{\sqrt j}
\frac{1-j^{1-s}}{1-j^{-s}},\qquad \mathcal Mt=Bb/s.
\]
At \(s_\ell=1+2\pi i\ell/\log q\), \(\ell\ne0\), the first component vanishes after removing \(B\), while the target and the second factor have magnitudes comparable to \(|\ell|^{-1}\) and \(\delta_{|\ell|}\). Bounded lattice sampling gives the lower bound in (4). The upper bound interpolates the required samples up to \(K\) and lifts the omitted target samples with an independent Hardy right inverse. That lift has squared norm at most \(C/K\), and both component norms are priced; choosing \(K\asymp\varepsilon^{-2}\) gives (4). All nonzero zeros of \(\Theta_q\) are canceled before division. The removable point \(s=1\) is not a zero.

This explains why (5) is a statement about the actual physical budget rather than about a list of small samples. Also,
\[
\|e-u-v\|^2=1-b^2+\|t-u-v\|^2
\tag{6}
\]
throughout: the Burnol floor remains.

## 2. Continued-fraction blocks price the reciprocal sum

Use the standard indexing
\[
P_m/Q_m=[a_0;a_1,\ldots,a_m],\qquad
Q_{-1}=0,\quad Q_0=1,\quad Q_{m+1}=a_{m+1}Q_m+Q_{m-1}.
\]
For \(j\ge1\), the elementary best-approximation facts are
\[
\frac1{Q_{j+1}+Q_j}<\delta_{Q_j}<\frac1{Q_{j+1}},\qquad
\delta_n\ge\delta_{Q_j}\quad(1\le n<Q_{j+1}).
\tag{7}
\]
These also cover \(a_1=1\); the duplicate initial denominators \(Q_0=Q_1=1\) will never be counted twice. The denominators \(Q_1,Q_2,\ldots\) are strictly increasing.

The points \(0,n\alpha\pmod1\), \(1\le n<Q_{j+1}\), are pairwise separated by more than \((2Q_{j+1})^{-1}\), because every nonzero index difference is less than \(Q_{j+1}\). On each side of zero, the \(r\)-th nearest point is therefore at distance at least \(r/(2Q_{j+1})\). Consequently
\[
\sum_{1\le n<Q_{j+1}}\delta_n^{-2}
\le 8\zeta(2)Q_{j+1}^2,
\]
and hence
\[
\sum_{Q_j\le n<Q_{j+1}}\frac1{n^2\delta_n^2}
\le8\zeta(2)\left(\frac{Q_{j+1}}{Q_j}\right)^2
\le32\zeta(2)a_{j+1}^2.
\tag{8}
\]
Conversely, the single term at \(n=Q_j\) is at least
\[
\frac1{Q_j^2\delta_{Q_j}^2}
\ge\left(\frac{Q_{j+1}}{Q_j}\right)^2\ge a_{j+1}^2.
\tag{9}
\]
Sum (8) over \(1\le j<m\), and (9) over the distinct denominators in that range. The finitely many terms \(1\le n<Q_1\) contribute a fixed constant \(C_\alpha\ge0\). For every \(m\ge2\),
\[
\boxed{S_m-a_1^2\le W(Q_m-1)
\le C_\alpha+32\zeta(2)S_m.}
\tag{10}
\]
For any real \(X\) with \(Q_m\le X<Q_{m+1}\), monotonicity similarly gives
\[
S_m-a_1^2\le W(X)\le C_\alpha+32\zeta(2)S_{m+1}.
\tag{11}
\]
The one-digit difference is intentional. At an arbitrary cutoff, the next digit can be large, so (11) is not being replaced by a universal common-index asymptotic.

## 3. Exact logarithmic endpoint

Suppose \(S_m\le A m\) for every \(m\). Since \(Q_m\ge F_{m+1}\), with \(F_k\) the Fibonacci numbers, \(m\ll\log Q_m\) for \(m\ge2\). Choose \(m\) with \(Q_m\le X<Q_{m+1}\). Equation (11) yields
\[
W(X)\le C_\alpha+32\zeta(2)A(m+1)\ll\log X.
\]
This implication needs an average bound on all initial digit segments, not a uniform bound on each digit.

Conversely suppose \(W(X)\ll\log X\). By (10), for all sufficiently large \(m\),
\[
S_m\ll_\alpha\log Q_m.
\tag{12}
\]
Here the fixed \(a_1^2\) has been absorbed since \(Q_m\to\infty\). The recurrence gives \(Q_m\le\prod_{j=1}^m(a_j+1)\). Thus
\[
\log Q_m\le\sum_{j=1}^m\log(a_j+1)
\le\sum_{j=1}^m a_j\le\sqrt{mS_m}.
\tag{13}
\]
Equations (12)--(13) imply \(S_m\ll m\); the finitely many initial segments are harmless. This proves the digit equivalence in (5). Combining it with NB-355's \(W(X)\gg\log X\) proves (2).

In particular, an unusually large next digit cannot be hidden by the large denominator it creates: its quadratic contribution dominates its logarithmic contribution in (13). This is the step that makes a bound in \(\log Q_m\) force a bound per continued-fraction digit.

## 4. Two explicit boundary controls

**Unbounded digits with logarithmic energy.** Define an irrational \(\alpha=[0;a_1,a_2,\ldots]\) by
\[
a_j=\begin{cases}2^k,&j=4^k,\ k\ge1,\\1,&\text{otherwise}.\end{cases}
\]
For each \(m\),
\[
S_m\le m+\sum_{4^k\le m}4^k\le\tfrac73m.
\]
The digits are unbounded, but (2) gives logarithmic energy for the real seeds \(q>1,p=q^\alpha\). This ratio is not badly approximable: at the preceding denominator,
\(Q_{4^k-1}\delta_{Q_{4^k-1}}<1/a_{4^k}=2^{-k}\).
Thus replacing the criterion in (2) by bounded partial quotients would falsely exclude admissible logarithmic-cost pairs.

**Regular digit growth with larger energy.** For \(\alpha_*=[0;1,2,3,\ldots]\),
\[
S_m=\frac{m(m+1)(2m+1)}6\asymp m^3,\qquad
m!\le Q_m\le(m+1)!.
\tag{14}
\]
The denominator bounds follow by iterating \(mQ_{m-1}\le Q_m\le(m+1)Q_{m-1}\). If \(Q_m\le X<Q_{m+1}\), factorial estimates give
\(\log X\asymp m\log m\), hence \(m\asymp\log X/\log\log X\). Equation (11) now has matching orders on both sides:
\[
W(X)\asymp\left(\frac{\log X}{\log\log X}\right)^3.
\tag{15}
\]
For every fixed \(r,c>0\), the right-hand scale at \(X=c\varepsilon^{-r}\) is comparable to that at \(X=\varepsilon^{-1}\). Substitution into the two distinct cutoffs in (4) proves (3). No asymptotic constant for the physical optimum follows from this comparison. In particular (3) is smaller than every positive inverse power of \(\varepsilon\), but larger than logarithmic energy.

## Prior art, mathematical delta, and boundaries

Borda, *On the theorem of Davenport and generalized Dedekind sums*, J. Number Theory 172 (2017), 1--20, [Section 4, Theorem 3 and Proposition 5](https://arxiv.org/pdf/1606.07946), treats the same reciprocal-power sums through continued fractions. Equations (7)--(11) reconstruct only their coarse comparison; they are classical in mechanism.

The closer endpoint precedent is Borda, *Optimal and typical L2 discrepancy of 2-dimensional lattices*, Ann. Mat. Pura Appl. 203 (2024), 2157--2184, [Theorem 1 and its proof in Section 2.2](https://link.springer.com/article/10.1007/s10231-024-01440-4). It characterizes optimal symmetrized-lattice discrepancy by bounded quadratic-mean digits, using the same denominator-growth argument. The scalar criterion and that argument are prior art. The present consequence is (2) for the **Nyman physical two-component energy**, via the full-norm bracket (4). Neither a new scalar criterion nor a new discrepancy theorem is claimed.

Locally, NB-357 established logarithmic energy under bounded digits, and NB-358 classified positive power bounds while explicitly leaving the logarithmic endpoint unresolved. Equation (2) completes that endpoint and the controls distinguish it from both bounded type and general subpolynomial cost. This settles one rate boundary; it does not provide a new route to eliminate the common zeta-zero obstruction.

- All seed parameters and \(b\) are fixed before \(\varepsilon\downarrow0\). The constructions make no assertion about the digit statistics of any specified integer log ratio, including \(\log2/\log3\).
- The cost is the sum of squared norms of the two grouped physical orbit vectors, after all cancellations within each orbit. Both may require arbitrarily many real dilations. No dilation-resolution, coefficient-size, or canonical discrete-section rate is supplied.
- Equation (6) retains the unknown Burnol floor. The target projection and the underlying upper construction involve \(B\); this does not compute that projection without zero information and does not prove RH.
- Rational ratios are excluded. Interchanging the two seeds leaves the physical conclusion unchanged; the criterion therefore describes the reciprocal ratio as well, despite changing the continued-fraction indexing.
- The strict cutoff \(Q_m-1\), distinct indices beginning at \(Q_1\), and the next digit in (11) prevent double counting or silently assuming bounded denominator jumps.

Evidence is the analytic proof and the inspected primary literature. The decisive audit points are the norm/error powers in (4), best-approximation separation for all index differences in (8), the converse absorption in (12)--(13), and the all-cutoff factorial comparison in (15). No numerical optimization, Lean verification, independent adversarial approval, exact physical asymptotic constant, or arithmetic finite-section improvement is asserted.
