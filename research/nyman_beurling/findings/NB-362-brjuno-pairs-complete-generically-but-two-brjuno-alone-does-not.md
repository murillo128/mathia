# NB-362 — Brjuno pairs complete generically, but 2-Brjuno alone does not

- **Status:** proved (classical theorems plus author derivation; independent adversarial review pending)
- **Research line:** `nyman_beurling`
- **Depends on:** NB-354 and NB-356 for the orbit realization and exact target-membership test; NB-360 for the full component-cost comparison; NB-361 for the universal 2-Brjuno necessary condition
- **Classification:** LITERATURE+DERIVED + EXACT-TARGET-MEMBERSHIP + NEGATIVE/OBSTRUCTION

## Claim and scope

The finite-type hypothesis in NB-360 can be weakened to the ordinary Brjuno condition, admitting some Liouville seed ratios. However, the weaker 2-Brjuno necessary condition in NB-361 does **not** suffice for almost-everywhere third-seed completion. An explicit 2-Brjuno Liouville ratio has infinite physical component cost for almost every third seed.

Fix real seeds \(p,q>1\) with irrational \(\alpha=\log p/\log q\). Let \(P_j/Q_j\) be the regular continued-fraction convergents of \(\alpha\), with \(Q_{-1}=0,Q_0=1\), and put
\[
\mathcal B_k(\alpha)=\sum_{j\ge1}\frac{\log Q_{j+1}}{Q_j^k}.
\tag{1}
\]
In \(H=L^2(0,1;dx)\), define
\[
e=1,\quad g_v(x)=\{1/(vx)\}-v^{-1}\{1/x\},\quad
A_af(x)=\sqrt a f(ax)\mathbf1_{x\le1/a},\quad
\mathcal C_v=\overline{\operatorname{span}}\{A_ag_v:a\ge1\text{ real}\}.
\]
Let \(\mathcal N=\overline{\operatorname{span}}\{g_v:v>1\}\) be the continuous Nyman space and \(t=P_{\mathcal N}e\). Then
\[
\boxed{\mathcal B_1(\alpha)<\infty
\quad\Longrightarrow\quad
t\in\mathcal C_q+\mathcal C_p+\mathcal C_{q^\beta}
\quad\text{for almost every }\beta\in(1,2).}
\tag{2}
\]
Each component is a finite-norm vector from a closed real-dilation orbit space. This is an algebraic-sum statement, not a finite-generator representation.

For a counterexample to replacing \(\mathcal B_1\) by \(\mathcal B_2\) in (2), define one continued fraction recursively by
\[
\alpha_-=[1;2,a_2,a_3,\ldots],\qquad
a_{j+1}=\left\lceil\exp(Q_j^{3/2})\right\rceil\quad(j\ge1).
\tag{3}
\]
Then \(\alpha_-\) is Liouville and \(\mathcal B_2(\alpha_-)<\infty\), but for \(p=q^{\alpha_-}\),
\[
\boxed{t\notin\mathcal C_q+\mathcal C_p+\mathcal C_{q^\beta}
\quad\text{for almost every }\beta\in(1,2).}
\tag{4}
\]
Equation (4) does **not** exclude every exceptional third seed. Whether (3) admits any completing third seed is not settled here. In particular, this does not refute the possible sufficiency of 2-Brjuno for the *existence* of a third seed; it refutes its sufficiency for *almost-everywhere* completion.

## 1. Retain the physical target in the phase test

Write \(\delta_n=\|n\alpha\|_{\mathbb R/\mathbb Z}>0\), and set
\[
S_\alpha(\beta)=\sum_{n\ge1}
\frac1{n^2(\delta_n^2+\|n\beta\|^2)}.
\tag{5}
\]
NB-356 proves, also for real seeds,
\[
t\in\mathcal C_q+\mathcal C_p+\mathcal C_{q^\beta}
\quad\Longleftrightarrow\quad S_\alpha(\beta)<\infty.
\tag{6}
\]
The bridge preserves the common zeta-zero factor. In the unitary Mellin model,
\[
\mathcal M\mathcal C_v=B\Theta_vH^2,\qquad
\mathcal Mt=Bf,\quad f(s)=b/s,\quad b=B(1)>0,
\qquad
\Theta_v(s)=\frac{s}{s-1}\frac1{\sqrt v}
\frac{1-v^{1-s}}{1-v^{-s}}.
\tag{7}
\]
Here \(H^2=H^2(\Re s>1/2)\), with boundary norm \((2\pi)^{-1}\int|F(1/2+iy)|^2dy\). Dividing by \(B\) is isometric on its range. At the nonzero zero-lattice points \(z_\ell=1+2\pi i\ell/\log q\) of \(\Theta_q\),
\[
|f(z_\ell)|\asymp |\ell|^{-1},\qquad
|\Theta_p(z_\ell)|^2+|\Theta_{q^\beta}(z_\ell)|^2
\asymp\delta_{|\ell|}^2+\||\ell|\beta\|^2.
\]
The constants are uniform on \(\beta\in[1,2]\). The lattice sampler has squared operator norm at most \(\log q/(1-q^{-1})\), and its explicit right inverse has squared norm at most \(q/\log q\). Pointwise minimum-norm sample splitting and that right inverse give the \(p\) and \(q^\beta\) components when (5) is finite. The remaining numerator vanishes on the lattice, so division by the pure Blaschke factor \(\Theta_q\) supplies the \(q\) component in \(H^2\).

Consequently NB-360's comparison, which does not require finite Diophantine type, gives
\[
cS_\alpha(\beta)\le E_3(\beta)\le C(1+S_\alpha(\beta)),
\tag{8}
\]
where \(E_3\) is the infimum of the sum of the three squared physical component norms over exact decompositions of \(t\), and is \(+\infty\) if none exists. The upper inequality constructs all three components, including the anchor component. Constants depend on \(p,q,b\). No bounded inverse of \(B\), extra zero at \(s=1\), or unweighted Gram-only criterion is used.

## 2. A clipped first moment has exactly the ordinary Brjuno threshold

Put
\[
W(\alpha)=\sum_{n\ge1}\min\left(\frac1n,\frac1{n^2\delta_n}\right).
\tag{9}
\]
An elementary continued-fraction block estimate gives
\[
\boxed{W(\alpha)<\infty\quad\Longleftrightarrow\quad
\mathcal B_1(\alpha)<\infty.}
\tag{10}
\]
Here are both directions, including the near-return contribution.

Fix \(j\ge1\), write \(q_0=Q_j,Q_0=Q_{j+1}\), and partition \([q_0,Q_0)\cap\mathbb N\) into blocks
\[
kq_0\le n<\min((k+1)q_0,Q_0),\qquad
1\le k\le K:=\lfloor(Q_0-1)/q_0\rfloor.
\]
For \(q_0>1\), distinct points \(n\alpha\pmod1\) in each block are separated by more than \(1/(2q_0)\): their index difference is below \(Q_j\), so best approximation and the convergent error formula give
\[
\|d\alpha\|\ge\|Q_{j-1}\alpha\|
>\frac1{Q_j+Q_{j-1}}\ge\frac1{2q_0}
\quad(1\le d<Q_j).
\tag{11}
\]
An arc of radius \(y\) around zero therefore contains at most \(4q_0y+1\) such points. If their distances from zero are ordered as \(d_1\le d_2\le\cdots\), then \(d_h\ge(h-1)/(4q_0)\) for \(h\ge2\). Bound the closest point using the \(1/n\) branch of (9), and all the others using the reciprocal-distance branch. With \(H_m=\sum_{h=1}^m1/h\), the block contribution is at most
\[
\frac1{kq_0}+\frac{4H_{q_0}}{k^2q_0}.
\tag{12}
\]
For \(q_0=1\), every block has only one point, so (12) remains valid without (11). Summing in \(k\) bounds the contribution on \([Q_j,Q_{j+1})\) by
\[
\frac{H_K+4\zeta(2)H_{q_0}}{q_0}
\ll\frac{1+\log Q_{j+1}}{Q_j}.
\tag{13}
\]
The denominators grow at least at Fibonacci rate, so \(\sum_j1/Q_j<\infty\). This proves sufficiency in (10), with the finitely many \(n<Q_1\) harmless.

Conversely, let \(L_j=\lfloor\sqrt{Q_{j+1}/Q_j}\rfloor\). For every \(1\le m\le L_j\), the index \(n=mQ_j\) belongs to \([Q_j,Q_{j+1})\), and
\[
n\delta_n\le m^2Q_j\|Q_j\alpha\|
<\frac{m^2Q_j}{Q_{j+1}}\le1.
\tag{14}
\]
Its contribution to (9) is exactly \(1/(mQ_j)\). These sets of indices are disjoint for different \(j\), and
\[
W(\alpha)\ge\sum_{j\ge1}\frac{H_{L_j}}{Q_j}
\ge\frac12\sum_{j\ge1}\frac{\log(Q_{j+1}/Q_j)}{Q_j}.
\tag{15}
\]
Indeed \(H_L\ge\log(L+1)\), and \(L_j+1>\sqrt{Q_{j+1}/Q_j}\). Since \(\sum_j(\log Q_j)/Q_j<\infty\), (15) proves necessity in (10).

For \(n\ge2\) and \(0<a\le1/2\), the one-variable integral satisfies
\[
2\int_0^{1/2}\min\left(1,\frac1{n^2(a^2+y^2)}\right)dy
\asymp\min\left(\frac1n,\frac1{n^2a}\right)
\tag{16}
\]
with absolute constants. If \(a\ge1/n\), the integral equals \(2\arctan(1/(2a))/(n^2a)\). If \(a<1/n\), integration on \([0,1/n]\) bounds it below by \(1/n\); splitting there and using \(y^{-2}\) bounds it above by \(4/n\).

Multiplication by \(n\) preserves Haar measure modulo one, so Tonelli, (10), and (16) show
\[
\int_1^2\sum_{n\ge1}\min\left(1,
\frac1{n^2(\delta_n^2+\|n\beta\|^2)}\right)d\beta<\infty
\quad\Longleftrightarrow\quad\mathcal B_1(\alpha)<\infty.
\tag{17}
\]
When finite, the clipped series converges almost surely. Only finitely many original terms can then exceed one, and every term is finite because \(\alpha\) is irrational. Thus the original series (5) converges almost surely. This proves (2) through (6).

Equation (17) classifies this **clipped first-moment method**, not almost-sure convergence itself. An infinite expectation alone cannot establish almost-sure divergence. The negative example below uses a separate metric theorem, without assuming independence of the phase events.

## 3. A totient-weighted near-return set forces generic failure

Let
\[
\mathcal A_\alpha=\{n\ge2:n\|n\alpha\|\le1\}.
\]
The Duffin--Schaeffer theorem of Koukoulopoulos--Maynard implies
\[
\boxed{\sum_{n\in\mathcal A_\alpha}\frac{\varphi(n)}{n^2}=\infty
\quad\Longrightarrow\quad
S_\alpha(\beta)=\infty\text{ for almost every }\beta.}
\tag{18}
\]
Apply their [Theorem 1, p. 253](https://annals.math.princeton.edu/wp-content/uploads/annals-v192-n1-p05-s.pdf) to the nonnegative function \(\psi(n)=n^{-1}\mathbf1_{\mathcal A_\alpha}(n)\). The divergence hypothesis is precisely \(\sum_n\varphi(n)\psi(n)/n=\infty\). For almost every \(\beta\), infinitely many distinct denominators in \(\mathcal A_\alpha\) then satisfy \(\|n\beta\|\le1/n\). At each one,
\[
\frac1{n^2(\delta_n^2+\|n\beta\|^2)}\ge\frac12.
\tag{19}
\]
The series does not even have terms tending to zero. No monotonicity condition on the sparse function \(\psi\) is required. Integer shifts extend the full-measure conclusion from \([0,1]\) to every unit interval.

For (3), the denominator recursion gives
\[
\log Q_{j+1}=Q_j^{3/2}+\log Q_j+O(1).
\tag{20}
\]
Thus \(\mathcal B_2(\alpha_-)<\infty\), by Fibonacci growth. Also \(Q_{j+1}/Q_j^A\to\infty\) for every fixed \(A\), so the convergent error bound proves that \(\alpha_-\) is Liouville.

Use the disjoint sets \(\{mQ_j:1\le m\le L_j\}\) from (14), omitting finitely many initial indices if necessary. They lie in \(\mathcal A_{\alpha_-}\). Two elementary totient facts suffice:
\[
\varphi(q_0m)\ge\varphi(q_0)\varphi(m),\qquad
\sum_{m\le L}\frac{\varphi(m)}{m^2}\ge\frac{H_L}{\zeta(2)}.
\tag{21}
\]
The first follows prime by prime. For the second, the identity \(\sum_{d\mid n}\varphi(d)=n\) gives exactly
\[
H_L=\sum_{d\le L}\frac{\varphi(d)}{d^2}
\sum_{k\le L/d}\frac1{k^2}
\le\zeta(2)\sum_{d\le L}\frac{\varphi(d)}{d^2}.
\]
Consequently the Duffin--Schaeffer weight on the \(j\)-th set is at least
\[
\frac{\varphi(Q_j)}{\zeta(2)Q_j^2}H_{L_j}
\ge\frac{\varphi(Q_j)}{2\zeta(2)Q_j^2}
\log(Q_{j+1}/Q_j)
\ge\frac{\varphi(Q_j)}{2\zeta(2)\sqrt{Q_j}}.
\tag{22}
\]
The last inequality uses \(Q_{j+1}\ge Q_j\exp(Q_j^{3/2})\). For every integer \(Q\ge1\),
\[
\varphi(Q)\ge\sqrt{Q/2}.
\tag{23}
\]
Indeed the prime-power factors of \(\varphi(Q)^2/Q\) are \(p^{a-2}(p-1)^2\); they are at least one except for \(p=2,a=1\), which contributes \(1/2\). Thus each disjoint set contributes at least \(1/(2\sqrt2\zeta(2))\) to (18). Summing proves divergence and hence (4).

## 4. The positive extension really includes Liouville pairs

For comparison, define another continued fraction by
\[
\alpha_+=[1;2,a_2,a_3,\ldots],\qquad
a_{j+1}=\lceil\exp(\sqrt{Q_j})\rceil.
\tag{24}
\]
Its denominators, computed separately from those in (3), satisfy
\[
\log Q_{j+1}=\sqrt{Q_j}+\log Q_j+O(1).
\]
It is Liouville for the same convergent-error reason, but now \(\mathcal B_1(\alpha_+)<\infty\). Equation (2) therefore supplies generic completion beyond NB-360's finite-type regime. The two examples separate Liouville behavior itself from the summability needed by the positive argument; they do not classify all Liouville ratios.

## Prior art, mathematical delta, and boundaries

Lee, Marmi, Petrykiewicz and Schindler, *Regularity properties of k-Brjuno and Wilton functions*, [Section 1.2, equation (1.4)](https://link.springer.com/article/10.1007/s00010-023-00967-w), gives the classical conditions (1). No novelty is claimed for those conditions or continued-fraction constructions. Best-approximation spacing, Haar integration, and the totient identities are classical; (10) is proved directly rather than imported as a new named criterion.

Koukoulopoulos and Maynard, *On the Duffin--Schaeffer conjecture*, Ann. of Math. 192 (2020), 251--307, DOI `10.4007/annals.2020.192.1.5`, [Theorem 1](https://annals.math.princeton.edu/wp-content/uploads/annals-v192-n1-p05-s.pdf), is the load-bearing metric theorem for the negative direction. Their discussion also credits earlier results covering \(\psi(n)=O(1/n)\), which includes the function used here. Thus (18) is a direct classical metric application, not a new divergence theorem.

Beresnevich, Haynes and Velani's [fixed-coordinate multiplicative framework, Section 2.2 and Theorem 2.2](https://arxiv.org/pdf/1511.06862), is neighboring prior art. Its multiplicative inequality is different from (5); no present-day open-problem claim is inferred from that older text. Existing links between Brjuno/Wilton functions and Nyman fractional-part autocorrelation likewise do not make the vocabulary new. The result here is the explicit transfer to **algebraic three-orbit membership with physical component norms** through the already-persisted NB-356 criterion.

The mathematical delta is (2) beyond finite type, and the counterexample (3)--(4) to an almost-everywhere converse of NB-361. Together they prevent conflating three questions: existence of any completing seed, generic completion, and convergence of a sufficient expectation estimate. A complete fiber classification remains open in this finding.

- For every orbit sum \(w\), \(\|e-w\|^2=1-b^2+\|t-w\|^2\). The common Burnol floor is unchanged. There is no RH conclusion or new estimate for a zeta zero.
- Both explicit ratios are real Liouville numbers. No result about a specified third integer seed, such as \(5\) added to \(2,3\), follows. Countable arithmetic seed sets can lie in a metric exceptional set.
- Full closed real-dilation spaces are used. No finite generator count, dilation range, discrete-section rate, or absolute-coefficient estimate is provided.
- No positive fractional-moment bound or uniform budget is claimed under (2). The clipped expectation (17) does not bound the expectation of the full energy.
- In (4), approximation to \(t\) remains possible because the original irrational pair has dense sum in \(\mathcal N\). Its total component norm must diverge as error tends to zero: otherwise weak compactness in the direct sum of the three closed spaces would produce the excluded exact decomposition. This is qualitative, with no asserted rate.

Evidence is the analytic derivation using the stated primary theorem. An ephemeral exact-rational check tested (12)--(15) on 133 continued-fraction blocks covering 44,100 integer indices, the totient product inequality on 4,096 pairs, and the harmonic divisor identity for 256 cutoffs; all passed. Those finite checks establish no metric or infinite-limit claim. The decisive audits are separation only within blocks of length \(Q_j\), disjointness of the near-return sets, retention of the totient factor in (22), and the distinction between an infinite clipped expectation and genuine almost-sure divergence. No Lean verification or independent adversarial approval is asserted.
