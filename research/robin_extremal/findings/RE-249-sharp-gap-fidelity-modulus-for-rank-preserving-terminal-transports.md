# RE-249 — Sharp gap-fidelity modulus for rank-preserving terminal transports

**Status:** EXACT-DERIVED + QUANTITATIVE-PNT-FIDELITY + GAP-RIGIDITY-TRANSITION + SHARP-MATCHED-SOURCE-OBSTRUCTION + PRIOR-ART-BOUNDED; independent adversarial audit pending.

**Parent findings:** RE-238, RE-246, RE-247, RE-248.

RE-248 attains the sharp terminal generalized-prime source discrepancy while preserving label rank and keeping each neighboring gap comparable to its baseline. That does not quantify the stronger requirement that *every absolute gap change tends to zero*. The exact answer is a one-dimensional Lipschitz/obstacle extremal problem. It gives a continuous transition between source rigidity and the full RE-247 ambiguity, and identifies the critical absolute gap precision.

## 1. Statement

Fix \(b>0\), \(0<\alpha<3/4\), \(p\to\infty\), \(U=U(p)\) with \(U/p\to\infty\), and set
\[
a=e^{-2},\quad T=aU,\quad
V(t)=\frac{(\log t)^{3/5}}{(\log\log t)^{1/5}},\quad
E(t)=te^{-bV(t)},\quad E_U=E(U),\quad
B_{p,b,U}=\frac{\sqrt p\log p}{\log U}e^{-bV(U)}.
\tag{1}
\]
Let \(Q_*=(q_j)\) be the *fixed*, strictly increasing source from RE-247/248:
\[
q_1=2,\qquad q_{j+1}-\log q_{j+1}=q_j.
\tag{2}
\]
Its gaps equal \(\log q_{j+1}\), and
\(\vartheta_{Q_*}(t)=t+O(\log t)\), where
\(\vartheta_Q(t)=\sum_{q\in Q,q\le t}\log q\).

Fix once and for all \(t_0=t_0(b)\) large enough that
\(|\vartheta_{Q_*}(t)-t|\le E(t)/4\) for \(t\ge t_0\).
For \(\eta=\eta_U\ge0\) with \(\eta_U=o(1)\), call a source \(Q=(r_j)\)
**admissible** when (i) it is a strictly increasing indexed transport of
\(Q_*\), (ii) \(r_j=q_j\) outside \(q_j\in(T,U)\), and the other \(r_j\)
remain in \((T,U)\), (iii)
\[
|\vartheta_Q(t)-t|\le E(t)\quad(t\ge t_0),
\tag{3}
\]
and (iv) for *every* pair of consecutive labels, including pairs
straddling shell endpoints,
\[
|(r_{j+1}-r_j)-(q_{j+1}-q_j)|\le\eta.
\tag{4}
\]
Use RE-247's exact kernel and normalization:
\[
h(t)=\frac{-\log(1-t^{-1})}{\log t},\quad
Z_{p,U}=\sqrt p\log p\int_{p+p^\alpha}^{U}
\sqrt t\,(-h'(t))dt=2+o(1),\quad
\mathcal A_{p,U}(Q)=\frac{\sqrt p\log p}{Z_{p,U}}
\int_{p+p^\alpha}^{U}(t-\vartheta_Q(t))(-h'(t))dt.
\tag{5}
\]
Let \(\Delta^{\rm gap}_{p,b,U}(\eta)\) be the supremum of
\(|\mathcal A_{p,U}(Q^1)-\mathcal A_{p,U}(Q^2)|\) over pairs of admissible
transports of this *same* \(Q_*\). Define
\[
\eta_{\rm crit}=(\log U)e^{-bV(U)},\qquad
M=\frac{\eta}{\eta_{\rm crit}},\qquad
f_M(u)=\min\{u,\ M(u-a),\ M(1-u)\}\quad(a\le u\le1),
\tag{6}
\]
and
\[
C(M)=\int_a^1\frac{f_M(u)}{u^2}\,du.
\tag{7}
\]

**Theorem (sharp gap-fidelity modulus).** Along every such
\(p,U,\eta_U>0\), allowing \(M=M_U\) to tend to zero, a finite positive
value, or infinity,
\[
\boxed{\displaystyle
\Delta^{\rm gap}_{p,b,U}(\eta)
 =B_{p,b,U}\bigl(C(M)+o(\min\{M,1\})\bigr).
}
\tag{8}
\]
For \(\eta=0\), the two transports coincide with \(Q_*\) and the
discrepancy is exactly zero. With \(K=(1+a)/(1-a)=\coth(1)\), the *explicit*
transition function is
\[
C(M)=
\begin{cases}
 2M\log\cosh(1),&0\le M\le K,\\[2mm]
 2+M\log\!\left(\dfrac{M^2}{M^2-1}\right)
   +\log\!\left(\dfrac{M-1}{M+1}\right),&M\ge K .
\end{cases}
\tag{9}
\]
It is continuous and strictly increasing; \(C(0)=0\),
\(0<C(M)<2\) for finite \(M>0\), and
\(C(M)=2-M^{-1}+O(M^{-3})\) as \(M\to\infty\).
Thus the ambiguity is \(o(B_{p,b,U})\) exactly when
\(\eta=o(\eta_{\rm crit})\), whereas the full \((2+o(1))B_{p,b,U}\)
of RE-247/248 survives exactly when
\(\eta/\eta_{\rm crit}\to\infty\), **even if \(\eta=o(1)\)**.
These equivalences refer to this matched, order-preserving generalized-source
comparison class, not to ordinary primes.

## 2. Upper bound: PNT envelope plus a discrete slope budget

For one admissible source write \(d_j=r_j-q_j\), with \(d_j=0\)
for all exterior indices, and let \(D=\max_j|d_j|\).
There are \(N=O(U/\log U)\) baseline labels in \((T,U)\).
For \(q_j\in(T,U)\) put
\[
W_j=\sum_{q_k\le q_j}\log(r_k/q_k).
\]
All terms outside the shell vanish. Since the interior labels \(q_k,r_k\)
both lie in \((T,U)\),
\[
|W_j|\le \sum_{q_k\in(T,U)}\frac{|d_k|}{T}
=O(D/\log U).
\tag{10}
\]
The exact baseline identity
\(\vartheta_{Q_*}(q_j)=q_j-(2-\log2)\) gives
\[
\vartheta_Q(r_j)-r_j=-(2-\log2)+W_j-d_j.
\tag{11}
\]
At \(r_j\), (3) and (10) yield
\(D\le E_U+O(D/\log U)+O(1)\), hence \(D=O(E_U)=o(U)\).
The gap condition (4), summed from either fixed exterior endpoint,
also gives
\[
D=O\!\left(\eta U/\log U\right)=O(ME_U).
\tag{12}
\]
Consequently
\[
|W_j|=O\!\left(E_U\min\{M,1\}/\log U\right).
\tag{13}
\]

Write \(u_j=q_j/U\). Uniformly in the fixed multiplicative shell,
\(E(r_j)/E_U=u_j+o(1)\); this uses
\(D/U=o(1)\) and \(V(Uu)-V(U)=o(1)\) for \(a\le u\le1\).
Thus (11), (3), and (13) give the obstacle bound
\[
|d_j|/E_U\le u_j+o(1).
\tag{14}
\]
On the other hand, the baseline gaps in the shell, including its two
straddling gaps, equal \(\log U+O(1)\). Since \(d_j\) is zero just outside
either endpoint and \(|d_{j+1}-d_j|\le\eta\),
\[
\frac{|d_j|}{E_U}
\le M(1+O(1/\log U))\min\{u_j-a,1-u_j\}
   +O(\eta/E_U).
\tag{15}
\]
When \(M\to0\), (15) alone bounds the displacement with relative
\(o(M)\) error; when \(M\) is bounded away from zero, (14) and (15)
combine with relative \(o(1)\) error. Splitting these two regimes proves
the uniform nodal majorant
\[
\frac{|d_j|}{E_U}
\le f_M(u_j)+o(\min\{M,1\}),
\tag{16}
\]
where the error is uniform in every shell index and every admissible
source. The endpoint \(O(\eta/E_U)=M O(\log U/U)\) is harmless.
The argument does **not** replace the changed logarithmic jump weights
by their original values: those weights are precisely what \(W_j\)
controls.

## 3. Exact source subtraction and positive discrete quadrature

All admissible sources have identical prefix and exterior index sets.
Integrate their Chebyshev steps against the exact positive kernel in (5).
For \(r\in(T,U)\) let
\[
F_U(r)=\log r\,[h(r)-h(U)]
=-\log(1-r^{-1})-h(U)\log r.
\]
Then
\[
-F_U'(r)=\frac1{r(r-1)}+\frac{h(U)}r>0.
\tag{17}
\]
The \(t\)-term in (5) cancels and the shared prefix cancels, giving the
**exact** identity
\[
\mathcal A(Q^1)-\mathcal A(Q^2)
=\frac{\sqrt p\log p}{Z_{p,U}}
\sum_{q_j\in(T,U)}
\int_{r_j^2}^{r_j^1}
\left(\frac1{r(r-1)}+\frac{h(U)}r\right)dr.
\tag{18}
\]
This avoids an \(O(\log U)\) staircase error that would swamp the
\(M\to0\) regime if one merely approximated both Chebyshev steps
separately.

Since \(r_j^i=q_j+O(E_U)\), \(T=aU\), and
\(h(U)=O(1/(U\log U))\), the positive integrand in (18) equals
\[
\frac{1+O(E_U/U+1/\log U)}{q_j^2}
\tag{19}
\]
uniformly on each integration segment. The absolute approximation
error is bounded by this relative \(o(1)\) times
\(\sum_j(|d_j^1|+|d_j^2|)/q_j^2\), not by an unjustified relative error
after potential signed cancellation.

The exact gap relation \(q_{j+1}-q_j=\log q_{j+1}\) provides the
positive quadrature law
\[
\sum_{q_j\in(T,U)}\frac{E_U f_M(q_j/U)}{q_j^2}
=\frac{e^{-bV(U)}}{\log U}
 \left(C(M)+o(\min\{M,1\})\right).
\tag{20}
\]
Indeed \(u\mapsto f_M(u)/u^2\) has uniformly bounded *relative*
total variation \(O(\min\{M,1\})\): \(f_M\) is nonnegative and unimodal,
its height is \(O(\min\{M,1\})\), and \(u^{-2}\) has bounded variation
on the fixed interval \([a,1]\). The baseline mesh is
\(O(\log U/U)\), while the gap-to-\(\log U\) relative error is
\(O(1/\log U)\); both quadrature errors are
\(o(\min\{M,1\})\) even when \(M\to0\) or \(M\to\infty\).

Apply (16), (19), (20), and \(Z_{p,U}=2+o(1)\) to (18).
Each of the two sources contributes at most the sum in (20), giving
\[
\Delta^{\rm gap}_{p,b,U}(\eta)
\le B_{p,b,U}\bigl(C(M)+o(\min\{M,1\})\bigr).
\tag{21}
\]

## 4. Matching constructive transports with tiny gap changes

Extend \(f_M\) by zero outside \([a,1]\); this extension is
\(M\)-Lipschitz and vanishes at both endpoints. Choose
\(\delta=(\log U)^{-1/2}\), \(\lambda=1-\delta\), and move the **same**
indexed labels by
\[
r_j^\pm=q_j\pm\lambda E_U f_M(q_j/U).
\tag{22}
\]
Labels outside the shell remain fixed. For shell and straddling gaps,
\[
|d_{j+1}^\pm-d_j^\pm|
\le \lambda E_U M\frac{q_{j+1}-q_j}{U}
=\lambda\eta\frac{q_{j+1}-q_j}{\log U}
\le\eta
\tag{23}
\]
for large \(U\), since those baseline gaps are
\(\log U+O(1)\) and \(\delta\gg1/\log U\).
As \(\eta=o(1)\), this also preserves strict increase.
Moreover, near \(T,U\), the absolute displacement is bounded by
\(\lambda\eta |q_j-T|/\log U\) or
\(\lambda\eta|U-q_j|/\log U\), respectively; hence no interior label
crosses either shell boundary. Thus rank, cardinality, exterior labels
and (4) all hold.

For the Chebyshev envelope, (10) and (12) give
\(W_j=O(E_U\min\{M,1\}/\log U)\).
Between consecutive transported labels,
\(\vartheta_{Q^\pm}(t)-t=-d_j^\pm+W_j-(2-\log2)+r_j^\pm-t\);
the final gap term is \(O(\log U)\).
Because \(f_M(u)\le u\), \(E(t)\ge(t/U)E_U\) on \([T,U]\)
for large \(U\), and \(\eta=o(1)\),
\[
|d_j^\pm|\le(1-\delta)E(t)+o(\delta E(t))
\]
whenever \(r_j^\pm\le t<r_{j+1}^\pm\) inside the shell.
The \(O(\log U)+O(E_U/\log U)\) staircase and changed-weight
errors are \(o(\delta E(t))\), since \(E(t)\asymp E_U\) there.
So both sources obey the **same unit envelope (3)** throughout
\([T,U]\). Below \(T\) they equal \(Q_*\). Above \(U\) the only
remaining discrepancy from \(Q_*\) is the total changed-log-weight
sum \(O(E_U/\log U)\); monotonic eventual growth of \(E(t)\) and the
baseline quarter-envelope secure (3) for every \(t\ge U\).
The same fixed \(t_0\) works for all sources and all large \(p\).

For the pair \(Q^+,Q^-\), all terms in (18) have the same positive
orientation. Equations (19), (20) and (22) therefore give
\[
\mathcal A(Q^+)-\mathcal A(Q^-)
=B_{p,b,U}\bigl(\lambda C(M)+o(\min\{M,1\})\bigr)
=B_{p,b,U}\bigl(C(M)+o(\min\{M,1\})\bigr),
\tag{24}
\]
because \(C(M)=O(\min\{M,1\})\) and \(\lambda\to1\).
This matches (21) without changing the number of labels or creating
dense jump packets.

## 5. Solving the one-dimensional extremal problem

A function \(f:[a,1]\to\mathbb R\) satisfying \(f(a)=f(1)=0\),
\(|f|\le u\), and Lipschitz constant at most \(M\) obeys pointwise
\(f(u)\le f_M(u)\). Since the weight \(u^{-2}\) is positive,
\(f_M\) is the exact maximizer of
\(\int_a^1 f(u)u^{-2}du\).
For \(0\le M\le K=(1+a)/(1-a)\), the obstacle \(u\) is inactive
and the tent \(M\min(u-a,1-u)\) integrates to
\(M\log((1+a)^2/(4a))=2M\log\cosh(1)\).
For \(M>K\), the left ramp meets the obstacle at
\(u_L=Ma/(M-1)\), the right ramp at \(u_R=M/(M+1)\);
integrating the left ramp, middle obstacle, and right ramp yields
(9). This also checks the threshold and the saturation limits.

The statement (8) is a *uniform asymptotic modulus*, not a claim that
the lattice of finite generalized-prime labels realizes an arbitrary
Lipschitz profile exactly at finite \(U\). The upper estimate uses
discrete gap and Chebyshev bounds; (22) constructs actual increasing
labels approaching the continuous extremizer.

## 6. Prior-art boundary, falsification controls, and Robin relevance

The variational fact that the maximum of a positive weighted linear
functional subject to endpoint, Lipschitz and obstacle constraints is
attained by the pointwise greatest feasible function is elementary.
Monotone label transports and Beurling generalized-prime flexibility
are established backgrounds; compare H. G. Diamond and W.-B. Zhang,
*Optimality of Chebyshev bounds for Beurling generalized numbers*,
Acta Arithmetica **160** (2013), 259–275,
DOI \`10.4064/aa160-3-3\`, whose theorem concerns generalized-integer
counting conditions, **not** the gap-constrained Robin terminal
modulus here. No novelty is claimed for Lipschitz tents or the
general existence of synthetic prime-like sources. The line-specific
delta beyond RE-248 is the *sharp critical gap scale and full constant
function* for a source-faithful discrete-weight Robin kernel under
fixed rank, exact exterior matching and a shared quantitative PNT
envelope. The literature checked did not supply this exact theorem;
independent novelty and proof audit remain appropriate.

Decisive failure checks are: use the **whole** all-height unit envelope
rather than a terminal-only estimate; retain the transported
\(\log r_j\) jump weights via (10)–(13); control the two boundary
straddling gaps in (23); preserve an \(o(\min\{M,1\})\) remainder when
\(M\) is tiny, using exact source subtraction rather than independent
staircase approximations; retain \(Z_{p,U}\to2\); and do not infer an
ordinary-prime theorem from an artificial rank-preserving source.
The \(\eta=o(1)\) hypothesis is part of the construction and
normalization, and the displayed \(C\) is **not** claimed for arbitrary
unbounded gap perturbations.

The result closes the precise gap-fidelity information question left
by RE-248 within this transport class: even uniformly vanishing
absolute gap errors need not erase terminal ambiguity unless they
are \(o((\log U)e^{-bV(U)})\). It does **not** rule out an
ordinary-prime-only selector, an actual colossally abundant state, or
a source-specific arithmetic estimate strong enough to imply
Robin's inequality. It proves neither a new inequality for ordinary
divisor sums nor RH.
