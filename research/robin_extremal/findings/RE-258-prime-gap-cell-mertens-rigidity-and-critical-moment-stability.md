# RE-258 — Prime-gap-cell integer transports are exactly Mertens-rigid and Robin-critically stable

**Status:** EXACT-DERIVED + LITERATURE-BOUND + PRIME-CELL-RIGIDITY + CRITICAL-MOMENT-STABILITY + ORDINARY-PRIME-APPLICATION-OPEN; independent adversarial review pending.

**Dependencies:** RE-169 (finite-source Mertens rule), RE-172 (finite prime-supported Euler-factor rigidity), RE-253 (signed triangular prime-counting moment), RE-254 (critical generalized-label transports), RE-256 (exact two-shell real-label compensation), RE-257 (subdyadic integer-label injectivity without cell fidelity). Classical Bertrand–Chebyshev postulate; Runbo Li's unconditional 0.52 prime-gap bound and Guth–Maynard's pointwise short-interval prime-number theorem, already anchored in the line's SOURCES.md.

RE-257 makes exact Mertens matching rigid for integer-label changes confined to a single subdyadic support but permits Robin-critical instability under extremely close *approximate* matching: the rounded RE-256 transport can traverse many genuine prime gaps. The missing geometric distinction is whether each integer replacement must stay inside the cell bounded by its two neighboring **original** primes. This natural rank-labelled constraint gives (i) exact global finite Mertens injectivity without any subdyadic-support hypothesis and (ii) uniform stability of the critical signed Robin moment even when Mertens matching is not imposed. Both are source-class statements, not new theorems about ordinary-prime Robin heights.

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

## 2. Uniform critical signed-moment stability

Let \(p\to\infty\) through ordinary primes, \(L=\log p\), and use RE-252–RE-256's critical horizon
\[
 H=H_\star(p)=\frac{p^{3/4}}{\sqrt L}
    \exp\!\left(\frac12L^{1/4}\right)=p^{3/4+o(1)}.
\tag{7}
\]
Let \(Q_p\) be any source satisfying (1), with all original prime labels through \(p\) unchanged. This is a condition on the complete source prefix, not merely matching its counting function. Alterations above \(p\) can be arbitrary in number and location as long as the cells and the discrete increasing-source condition hold; for each fixed \(p\), take finite support so that the finite Mertens convention remains meaningful.

For \(S=P,Q_p\) define
\[
 D_{S,p}(H)=
 \sum_{\substack{r\in S\\p<r\le p+H}}
       \bigl(H-(r-p)\bigr)-\frac{H^2}{2L}.
\tag{8}
\]
Then uniformly over all such \(Q_p\),
\[
\boxed{\frac{L}{p^{3/2}}
       \bigl(D_{Q_p,p}(H)-D_{P,p}(H)\bigr)
       =O\!\left(p^{-23/100+o(1)}\right)=o(1).}
\tag{9}
\]
In particular, the order-one critical signed excursion possible for RE-254/RE-256/RE-257 transports cannot occur within the original-prime-cell integer class. Exact Mertens normalization is not required for (9).

**Proof.** Define \(g_p\) as the largest consecutive-prime gap meeting the interval \([p/2,2p]\), with its two neighboring boundary primes included. Runbo Li's prime-in-short-interval theorem supplies
\[
 g_p\ll p^{13/25}=p^{0.52}.
\tag{10}
\]
Since \(g_p=o(H)\) and \(H=o(p)\), the labels that can contribute differently to (8) have original indices with
\[
 p<p_j\le p+H+g_p.
\tag{11}
\]
Indeed for \(p_j\le p\) the sources agree; for later indices (1) gives \(q_j>p_{j-1}\ge p\), so no lower-bound crossing occurs; and a prime more than \(g_p\) beyond \(p+H\) cannot enter from above. Every relevant displacement is at most \(g_p\).

The cutoff weight \(w_b(t)=(b-t)_+\), \(b=p+H\), is globally 1-Lipschitz. Consequently the cancellation of the identical centering terms and rankwise pairing give the **exact deterministic bound**
\[
 |D_{Q_p,p}(H)-D_{P,p}(H)|
 \le \sum_{\substack{j\\p<p_j\le p+H+g_p}}
      |q_j-p_j|
 \le g_p\,[\pi(p+H+g_p)-\pi(p)].
\tag{12}
\]
Guth–Maynard's pointwise short-interval prime-number theorem applies to \(H+g_p=p^{3/4+o(1)}\), yielding
\[
 \pi(p+H+g_p)-\pi(p)\ll H/L.
\tag{13}
\]
Combining (10)–(13) gives
\[
 \frac{L}{p^{3/2}}|\Delta D|
 \ll\frac{H g_p}{p^{3/2}}
 \ll p^{-23/100}L^{-1/2}\exp(\tfrac12L^{1/4})
 =p^{-23/100+o(1)}.
\tag{14}
\]
All constants in this bound are independent of the chosen cell transport. \(\square\)

If a CA-preserving construction demands the stronger frozen prefix through \(p+H/4\), that is a subclass of these controls, so the same conclusion holds. The original-prime CA integer itself and its divisor-sum height remain fixed; (9) compares only the *future source-dependent triangular moment*.

## 3. Falsification, prior art and exact information boundary

The cell restriction is genuine. For example moving \(p_j=7\) to the composite label \(q_j=8\) within the original cell \((5,11)\), leaving the other primes fixed, is admissible and yields a different (non-Mertens-matched) integer source. RE-172 already shows finite injectivity when all changed labels themselves must be primes; RE-257 shows integer-label injectivity when *all changes jointly* lie in one subdyadic interval. Neither requires or derives (1), and neither yields this **unrestricted finite-support, prime-cell-indexed** injectivity theorem. Conversely, RE-257's rounded two-shell transport uses displacements of size about \(Le^{-L^{1/4}}H=p^{3/4+o(1)}\), vastly larger than the available \(O(p^{0.52})\) prime cells: its instability is therefore not a counterexample to (9).

The valuation argument is elementary unique factorization plus Bertrand–Chebyshev, not new Diophantine approximation or a theorem about actual prime gaps. The quantitative estimate is a combination of a Lipschitz triangular cutoff, the existing Guth–Maynard theorem and Li's known 0.52 gap bound. Searches against the immediate classical and modern prime-gap/Euler-factor literature and local RE-172/RE-254–RE-257 dependencies found no reason to claim independent number-theory novelty for the elementary tools. Existing SOURCES.md entries cover both modern inputs; no literature-index mutation is required.

The hypotheses cannot be suppressed silently. Arbitrary integer labels outside the original prime cells admit telescoping identities such as
\[
 \frac21=\frac32\frac43,
\tag{15}
\]
so integer support alone does not imply global injectivity. If replacements are real rather than integer, prime-adic valuations cannot be used. If infinitely many indexed prime cells may change, there need not be a last altered index, so (3) is not asserted. If only a common prime-counting envelope or relative adjacent-gap ratio is preserved, a label can cross many original prime cells and (9) need not hold. The moment bound does not assert a sign for \(D_{P,p}(H)\) or estimate the remaining remote Robin annulus.

**Research consequence.** The synthetic ambiguity near a CA-selected Robin frontier is sensitive not simply to integer labels, exact Mertens mass, or relative gap fidelity, but to whether the replacement source crosses *original prime-gap cells*. This is an exact, prime-specific fidelity discriminator: preserving every cell kills finite exact-Mertens compensation globally and kills the critical signed-moment excursion quantitatively. What is **not** proved is that any weaker natural CA selection or divisor-sum hypothesis enforces this cell fidelity, or that the actual ordinary-prime signed moment is small. Neither Robin's inequality nor RH follows.
