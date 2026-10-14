# RE-258 — Prime-gap-cell integer transports are exactly Mertens-rigid and Robin-critically stable

**Status:** EXACT-DERIVED + SHARP-INTERLACING-COUNT + SHARP-MERTENS-ENVELOPE + PRIME-CELL-MERTENS-RIGIDITY + ROBIN-CRITICAL-STABILITY + ORDINARY-PRIME-APPLICATION-OPEN; independent adversarial review pending.

**Dependencies:** RE-169 (finite-source Mertens rule), RE-172 (finite prime-supported Euler-factor rigidity), RE-253 (signed triangular prime-counting moment), RE-254 (critical generalized-label transports), RE-256 (exact two-shell real-label compensation), RE-257 (subdyadic integer-label injectivity without cell fidelity). Classical Bertrand–Chebyshev postulate; Runbo Li's unconditional 0.52 prime-gap bound and Guth–Maynard's pointwise short-interval prime-number theorem, already anchored in the line's SOURCES.md.

RE-257 makes exact Mertens matching rigid for integer-label changes confined to one subdyadic support, but permits Robin-critical instability under extremely close approximate matching: its rounded transports cross many original prime gaps. Requiring each integer replacement to stay between its two **original neighboring primes** gives global finite Mertens injectivity with no subdyadic restriction. More strongly, the two ordered counting functions differ by **at most one at every height**. This elementary interlacing fact yields a sharp, unconditional first-annulus bound, improves the previous exponent from −0.23 to −0.75, and forces Mertens near-matching of order 1/p without assuming it. None of these source-class statements supplies an ordinary-prime Robin sign theorem.

## 1. Exact global theorem for prime-gap cells

Enumerate the ordinary primes as \(2=p_1<p_2<\cdots\). Let \(Q=(q_j)_{j\ge1}\) be an increasing positive-integer-labelled source, with \(q_1=2\), with \(q_j=p_j\) except at finitely many indices, and satisfying the **original-prime-cell condition**
\[
 p_{j-1}<q_j<p_{j+1}\qquad(j\ge2).
 \tag{1}
\]
There is no requirement that the \(q_j\) themselves be prime; they may be composite. The cells are indexed by the unmodified ordinary-prime sequence, not by the replacement source.

Write \(f(t)=\log(t/(t-1))\), and define the finite Euler-factor ratio
\[
\mathcal R(Q,P)=
 \prod_{j:q_j\ne p_j}
 \frac{q_j/(q_j-1)}{p_j/(p_j-1)}.
\tag{2}
\]
Then
\[
\boxed{\mathcal R(Q,P)=1\quad\Longleftrightarrow\quad q_j=p_j\ \text{for all }j.}
\tag{3}
\]
Consequently, under the RE-169 finite-source Mertens convention,
\[
\boxed{\Gamma(Q)=\gamma\quad\Longrightarrow\quad Q=P.}
\tag{4}
\]
Unlike RE-257, no single interval containing all modifications, no ratio bound between the largest and smallest changed primes, and no predetermined terminal shell is assumed.

**Proof.** Suppose \(Q\ne P\) and let \(m\ge2\) be the *largest* altered index; put \(r=p_m\). The product (2) is rational, so inspect its \(r\)-adic valuation. At every altered index \(j<m\), condition (1) gives
\[
 1<q_j<p_{j+1}\le r,
\]
and also \(p_j<r\). Therefore the numerator and denominator of both relevant Euler factors are strictly less than \(r\); all their \(r\)-adic valuations vanish. At indices \(j>m\), factors cancel exactly.

At \(j=m\), Bertrand's postulate gives \(p_{m+1}<2r\), hence
\[
 1<q_m<p_{m+1}<2r.
\tag{5}
\]
Because \(q_m\ne r\) and both \(q_m\) and \(q_m-1\) are below \(2r\), one has
\[
 v_r\!\left(\frac{q_m}{q_m-1}\right)
 =\begin{cases}-1,&q_m=r+1,\\0,&\text{otherwise}.\end{cases}
\tag{6}
\]
But \(v_r(r/(r-1))=1\). Thus \(v_r(\mathcal R(Q,P))=-1\) or \(-2\), contradicting \(\mathcal R(Q,P)=1\). Therefore no changed index exists. Conversely \(Q=P\) trivially gives equality. Equation (4) follows from the exact finite Mertens identity
\(\Gamma(Q)-\gamma=\sum_{j:q_j\ne p_j}[f(q_j)-f(p_j)]=\log\mathcal R(Q,P)\). \(\square\)

This descending-index argument is *global in the modification support* but *local in each index*. It does not use the number of altered cells, monotonicity of the final labels beyond their defining source interpretation, nor any analytic estimate for prime distribution beyond Bertrand's theorem. The condition \(q_j<p_{j+1}\) is the crucial private-prime certificate: all earlier replacement factors are built out of integers smaller than the final altered prime \(r\).

## 2. Sharp interlacing-count law and uniform Robin stability

Let \(p=p_m\ge3\) be an ordinary prime, put \(L=\log p\), and suppose \(Q\) satisfies (1) with the **complete original prefix frozen**: \(q_j=p_j\) for \(j\le m\). Write
\[
 A_Q(t)=\Pi_Q(t)-\pi(t),\qquad
 \Pi_Q(t)=\#\{j:q_j\le t\}.
\]
For any \(p_k\le t<p_{k+1}\), every \(j\le k-1\) has \(q_j<p_{j+1}\le p_k\le t\), while every \(j\ge k+2\) has \(q_j>p_{j-1}\ge p_{k+1}>t\). Thus only indices \(k,k+1\) can affect the count, and
\[
 \boxed{A_Q(t)=\mathbf1_{\{q_k\le t\}}+\mathbf1_{\{q_{k+1}\le t\}}-1
 \ \in\{-1,0,1\}.}
 \tag{9}
\]
This is a deterministic rank/interlacing statement: no gap bound, short-interval PNT, or integrality of the replacement labels is used in (9). Integrality is still essential for the exact product rigidity (3).

For the signed triangular statistic (8), the common centering term cancels and the frozen prefix gives
\[
 \Delta D_p(H):=D_{Q,p}(H)-D_{P,p}(H)
 =\int_p^{p+H}A_Q(t)\,dt.
 \tag{10}
\]
Therefore the **sharp finite-height uniform bound** is
\[
 \boxed{|\Delta D_p(H)|\le H\qquad(H\ge0).}
 \tag{11}
\]
More generally, for every absolutely continuous compactly supported test function \(\phi\) in \((p,\infty)\), Stieltjes integration by parts gives the bounded-variation stability rule
\[
 \sum_j\bigl(\phi(q_j)-\phi(p_j)\bigr)
 =-\int_p^\infty A_Q(t)\phi'(t)\,dt,\qquad
 \left|\sum_j(\phi(q_j)-\phi(p_j))\right|
 \le\int_p^\infty|\phi'(t)|\,dt.
 \tag{12}
\]
Only finitely many summands can be nonzero under the finite-support hypothesis.

### Automatic quantitative Mertens fidelity

For \(f(t)=\log(t/(t-1))\), the finite-source identity of RE-169 and (9) give the **exact** representation
\[
 \Gamma(Q)-\gamma
 =\sum_j[f(q_j)-f(p_j)]
 =\int_p^\infty\frac{A_Q(t)}{t(t-1)}\,dt,
\]
and hence
\[
 \boxed{|\Gamma(Q)-\gamma|
 \le\int_p^\infty\frac{dt}{t(t-1)}
 =\log\frac p{p-1}=O(p^{-1})
 =o((\sqrt p\,L)^{-1}).}
 \tag{13}
\]
Thus every finite-support, prefix-frozen prime-cell transport automatically satisfies **much better than Robin-critical approximate Mertens matching**, even if exact matching fails. Exact equality is still rigid by (3). **Exact Mertens-envelope sharpness.** For the fixed prefix \(p=p_m\), integrality and (1) give
\(p_{j-1}+1\le q_j\le p_{j+1}-1\) for \(j>m\). Since
\(f(t)=\log(t/(t-1))\) is strictly decreasing, every admissible finite-support source satisfies
\[
\boxed{-M_-(p)\le\Gamma(Q)-\gamma\le M_+(p),}
\tag{13a}
\]
where the sharp positive envelopes are the convergent sums
\[
\begin{aligned}
M_+(p)&=\sum_{j>m}\bigl[f(p_{j-1}+1)-f(p_j)\bigr],\\
M_-(p)&=\sum_{j>m}\bigl[f(p_j)-f(p_{j+1}-1)\bigr].
\end{aligned}
\tag{13b}
\]
They are **exact suprema** over finite-support integer transports: choose each changed label at its smallest or largest allowed integer, truncate at a terminal index, and let that index grow. Both choices remain strictly increasing at every index, including support boundaries. Termwise monotonicity proves that no other admissible source can exceed these envelopes.

The positive envelope has an exact prime-square Euler-product form. The intervals \([p_{j-1}+1,p_j]\) cover every prime gap after \(p\) except its first unit. Integrating \(-f'(t)=1/(t(t-1))\) across these intervals gives
\[
\boxed{
M_+(p)=f(p)-\sum_{\substack{r\ge p\\r\ {\rm prime}}}
           \log\frac{r^2}{r^2-1}
       =f(p)+\sum_{\substack{r\ge p\\r\ {\rm prime}}}\log(1-r^{-2}).
}
\tag{13c}
\]
Omitting instead the last unit of each gap gives
\[
M_-(p)=f(p_{m+1})-
   \sum_{j\ge m+2}\log\frac{(p_j-1)^2}{p_j(p_j-2)}.
\tag{13d}
\]
The prime-number theorem and partial summation imply
\(\sum_{r\ge p,\ r\ {\rm prime}}r^{-2}=O((p\log p)^{-1})\) and
\(p_{m+1}=p(1+o(1))\). Therefore
\[
\boxed{M_+(p)=(1+o(1))p^{-1},\qquad
       M_-(p)=(1+o(1))p^{-1}.}
\tag{13e}
\]
The coefficient \(1\) in (13) is thus asymptotically optimal **in both signs** within the finite-support integer-cell class. These are suprema approached by longer finite transports, not claims of exact attainment. The prime-square Euler-product tail is classical; the exact source-constrained envelope is the line-local deduction.

### Uniform local Robin-kernel comparison

For \(S=P,Q\), retain the RE-253/RE-254 source-model kernel
\[
 \vartheta_S(t)=\sum_{r\in S,\ r\le t}\log r,\quad
 h(t)=\frac{-\log(1-t^{-1})}{\log t},\quad
 k(t)=\frac1{t\log t},\quad
 I_S(t)=(\vartheta_S(t)-t)h'(t)-(h(t)-k(t)).
\]
The \(h-k\) terms cancel between sources. Abel summation, with \(A_Q(p)=0\), yields the exact identity
\[
 \vartheta_Q(t)-\vartheta_P(t)
 =\log(t)\,A_Q(t)-\int_p^t\frac{A_Q(u)}u\,du
 =L A_Q(t)+O(H/p),\qquad p\le t\le p+H.
 \tag{14}
\]
Uniformly for \(0\le H\le p/2\), use \(h'(t)\ll(p^2L)^{-1}\), \(h''(t)\ll(p^3L)^{-1}\) to freeze \(h'\) at \(p\). With the exact positive \(a_p=-\sqrt p\,L^2h'(p)=Lp^{-3/2}(1+O(L^{-1}))\) from RE-253,
\[
 \boxed{\sqrt p\,L\int_p^{p+H}(I_Q-I_P)(t)\,dt
 =-a_p\,\Delta D_p(H)
 +O\left(\frac{L H^2}{p^{5/2}}\right).}
 \tag{15}
\]
The constant is absolute and independent of how many cells change. In particular, at the critical Guth--Maynard horizon
\[
 H_\star=\frac{p^{3/4}}{\sqrt L}\exp(\tfrac12L^{1/4})=p^{3/4+o(1)},
\]
equations (11) and (15) give
\[
 \boxed{\frac L{p^{3/2}}|\Delta D_p(H_\star)|
 \le \frac{LH_\star}{p^{3/2}}=p^{-3/4+o(1)},\qquad
 \left|\sqrt pL\int_p^{p+H_\star}(I_Q-I_P)\right|
 \le(1+o(1))a_pH_\star=o(1).}
 \tag{16}
\]
Neither bound invokes any prime-gap theorem or short-interval PNT. The earlier \(O(p^{-23/100+o(1)})\) bound of RE-258 was valid but substantially non-sharp: bounding each displacement by the *largest gap* before summing lost the rankwise cancellation encoded in (9).

### Exact finite-horizon integer-cell moment envelopes

The uniform rank bound (11) has an **exact attained integer-endpoint refinement**. Fix an integer \(b\ge p=p_m\), write \(H=b-p\), and let \(p^+=p_{m+1}\). Over all finitely supported integer-labelled sources satisfying (1) and the frozen prefix through \(p\),
\[
\boxed{
\begin{aligned}
\max_Q\Delta D_p(b-p)
 &=\#\{n\in\mathbb Z:p<n<b,\ n\text{ composite}\},\\
\min_Q\Delta D_p(b-p)
 &=-\#\{n\in\mathbb Z:p^+<n\le b,\ n\text{ composite}\}.
\end{aligned}}
\tag{17}
\]
Both extrema are **attained**, not just suprema. They depend only on the composite integers on the two indicated finite intervals; no prime-gap estimate is needed for (17).

To prove this, put \(g_b(x)=(b-x)_+\). The prefix is frozen, so (10) becomes the finite sum
\[
\Delta D_p(b-p)=\sum_{j>m}\left[g_b(q_j)-g_b(p_j)\right].
\]
For each \(j>m\), the integer-cell restriction is
\(p_{j-1}+1\le q_j\le p_{j+1}-1\). Since \(g_b\) is nonincreasing, choose \(q_j=p_{j-1}+1\) to maximize and \(q_j=p_{j+1}-1\) to minimize. The choices at different indices are simultaneously admissible and strictly increasing, including at both ends of a finite changed block; beyond a sufficiently large index their contributions vanish and the ordinary labels can be restored. Reindexing and telescoping yields the equivalent endpoint formulas
\[
\boxed{
\begin{aligned}
U_p(b)&=(b-p-1)_+
          -\#\{r\text{ prime}:p<r<b\},\\
V_p(b)&=-(b-p^+)_+
          +\#\{r\text{ prime}:p^+<r\le b\}.
\end{aligned}}
\tag{18}
\]
For integer \(b\), the first positive-part term counts \(p<n<b\), and the second counts \(p^+<n\le b\). Subtracting the displayed prime counts proves (17), including \(b=p\) and the initial prime-gap boundary. For real \(b\ge p\), the two extremal envelopes are exactly the piecewise-linear interpolations of their values at integer endpoints: the same endpoint label choices optimize every summand and \(g_b(n)\) has only integer breakpoints.

At the Guth--Maynard horizon \(H_\star=p^{3/4}L^{-1/2}\exp(\tfrac12L^{1/4})\), first let \(b=p+\lfloor H_\star\rfloor\), \(H=b-p\). The already cited pointwise short-interval theorem gives
\(\pi(p+H)-\pi(p)=H/L+O(H\exp(-L^{1/4}))\).
Equations (17)--(18), together with \(p^+-p\ll p^{13/25}\), therefore sharpen the signed extremal asymptotics to
\[
\boxed{
\begin{aligned}
\max_Q\Delta D_p(H)
 &=H\left(1-\frac1L\right)
    +O\left(H e^{-L^{1/4}}+1\right),\\
\min_Q\Delta D_p(H)
 &=-H\left(1-\frac1L\right)
    +O\left(H e^{-L^{1/4}}+(p^+-p)+1\right).
\end{aligned}}
\tag{19}
\]
Since \(e^{-L^{1/4}}=o(L^{-1})\) and
\((p^+-p)/H=o(L^{-1})\), both signed envelopes are
\(\pm H(1-L^{-1}+o(L^{-1}))\) in the corresponding order. Piecewise-linear interpolation gives the same formula at real \(H_\star\), with \(H_\star\) replacing \(H\).

These extrema are witnessed explicitly by the finite transports \(q_j=p_{j-1}+1\) (positive discrepancy) and \(q_j=p_{j+1}-1\) (negative discrepancy), restricted to the indices affecting the chosen endpoint. They freeze every ordinary-prime label through \(p\) and remain strictly increasing at the support boundaries. Combined with (15), the refinement also transfers to the leading signed first-annulus Robin-kernel **difference** between each source and the ordinary primes, with its sign reversed and an error smaller than the displayed \(H/L\) correction. This does not estimate the ordinary-prime moment itself.

## 3. Prior art, falsification, and exact information boundary

The one-unit counting discrepancy in (9) is the elementary consequence of interlacing two indexed ordered sequences; it is analogous to classical eigenvalue interlacing/spectral-shift counting bounds and is **not claimed as a new general theorem**. The substantive line-local correction is that this stronger representation of the very same RE-258 prime-cell condition gives a **sharp first-Robin-annulus stability law**, an automatic \(O(p^{-1})\) Mertens mismatch bound, and optimal signed controls. No new external analytic theorem is used. The pre-existing line SOURCES.md already anchors the Guth--Maynard and Li inputs needed for (17)--(19), and RE-169 anchors the finite Euler-product normalization.

The original global integer-factor rigidity (3) still requires **finite** support and ordinary-prime-cell integer labels: the largest changed index and its prime-adic valuation supply its unique-factorization certificate. Equation (9), by contrast, uses only original-cell positional interlacing and remains valid with real replacement labels. The finite-source Mertens identity (13) is asserted for finite differences, not arbitrary infinite perturbations without convergence control. The prefix-frozen hypothesis is essential for the integral identities from \(p\); without it an initial offset remains. An unrestricted integer transport may cross many original cells and fails the one-unit counting estimate; RE-254--RE-257 remain valid matched controls.

The extremizers (17)--(19) use integer labels that are generally **composite**, not additional ordinary-prime realizations. This sharp stability is a fidelity theorem for a synthetic class relative to the *fixed* ordinary primes, not a bound for \(D_{P,p}(H_\star)\) itself. It neither forces cancellation of the actual CA-selected signed prime moment nor estimates the remote Robin annulus. Exact finite Mertens matching implies identity by (3), but even a near-exact match as strong as (13) need not make \(\Delta D_p(H)\) vanish identically; the correct finite-height obstruction is the sharp \(H\)-bound (11). No Robin inequality or RH conclusion follows.

**Research consequence.** RE-258's geometric hypothesis does considerably more than the previous largest-gap argument detected: all rankwise cell transports have at most unit **global counting error**, automatically tiny Mertens error, and sharp \(p^{-3/4+o(1)}\) normalized first-annulus stability. The remaining source-specific question is why any naturally induced synthetic alternative should preserve these original-prime cells; the ordinary-prime signed-moment and remote-tail sign problems remain open.
