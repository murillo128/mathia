# RE-261 — Exact Mertens matching has a sharp counting-discrepancy Robin threshold

**Status:** EXACT-DERIVED + SHARP-SOURCE-STABILITY + DISCRETE-REAL-AND-INTEGER-LABEL-REALIZATION + CLASSICAL-DISCREPANCY-MECHANISM; independent adversarial review pending.

**Dependencies:** RE-169 (Mertens compensation), RE-154 (post-selector relocation scale), RE-258 (prime-cell counting bound), RE-260 (infinite exact matching with unit shifts). The only prime-distribution input to sharpness is the classical PNT.

Prime-cell interlacing and unit displacement impose strong source fidelity. The relevant more general quantity is the **maximum counting discrepancy**, rather than the number of modified atoms or finite support. With exact Mertens matching, an integer counting budget \(1\le K=o(p/\log p)\) permits a worst-case normalized transient Robin discrepancy

\[
\boxed{\left(\frac12+o(1)\right)\frac{K\log p}{\sqrt p}.}
\tag{1}
\]

The upper bound covers infinite sources; finite, cardinality-preserving real-label transports already establish sharpness. The same sharp constant holds for distinct **integer** labels: a finite integer packet followed by infinitely many unit prime shifts realizes exact normalization without increasing the counting budget. Near equality forces a specific two-phase counting profile around \(2p\). Thus exact normalization does not improve the critical counting scale \(K\asymp\sqrt p/\log p\), although it constrains how the excursion and its compensation must be arranged. This is a synthetic-source theorem, not an estimate for the ordinary-prime Robin tail.

## 1. Source class and finite-height bound

Let \(p\ge3\) be an ordinary prime, \(L=\log p\), and \(K\ge1\) an integer. Let \(\mathcal C_{p,K}\) consist of locally finite, strictly increasing, unbounded real-label sources \(Q\subset(1,\infty)\) that agree with the ordinary primes \(P\) on \((1,p]\), and satisfy
\[
A(t):=\Pi_Q(t)-\pi(t),\qquad |A(t)|\le K\quad(t\ge p),\qquad
\Gamma(Q)=\gamma.
\tag{2}
\]
Here \(\Pi_Q\) counts labels, with no prime-power weights, and
\[
f(t)=\log\frac t{t-1},\quad h(t)=\frac{f(t)}{\log t},\quad
k(t)=\frac1{t\log t},\quad
\Gamma(Q)=\lim_{x\to\infty}\left(\sum_{q\le x}f(q)-\log\log x\right).
\tag{3}
\]
The limit in (3) exists for every source with the prefix and counting conditions, as proved below; exact equality in (2) is an additional constraint.

For \(S=P,Q\), put
\[
\vartheta_S(t)=\sum_{s\in S,\ s\le t}\log s,\qquad
I_S(t)=(\vartheta_S(t)-t)h'(t)-(h(t)-k(t)),\qquad
E_Q(U)=\int_p^U(I_Q-I_P)(t)\,dt.
\tag{4}
\]
For every finite \(U\ge p\),
\[
\boxed{|E_Q(U)|\le K\left[
\min\{f(p)-f(U),f(U)\}+h(U)\log(U/p)\right].}
\tag{5}
\]
In particular,
\[
\boxed{\sup_{Q\in\mathcal C_{p,K}}\sup_{p\le U\le\infty}|E_Q(U)|
\le K\left[\frac{f(p)}2+\frac1{e(p-1)\log p}\right]
=\left(\frac12+O(L^{-1})\right)\frac Kp.}
\tag{6}
\]
The \(O\)-constant is absolute, independent of \(K,Q,U\). The full tail satisfies \(E_Q(\infty)=0\); (6) controls intermediate excursions, not a residual terminal mismatch.

### Exact counting representation

Write \(d\mu(t)=dt/[t(t-1)]=-f'(t)dt\). Abel summation gives
\[
\sum_{q\le x}f(q)-\sum_{r\le x,\ r\in P}f(r)
=f(x)A(x)+\int_p^x A(t)\,d\mu(t).
\tag{7}
\]
The boundary term tends to zero and \(\int_p^\infty |A|d\mu\le Kf(p)<\infty\). Consequently
\[
\Gamma(Q)-\gamma=\int_p^\infty A(t)\,d\mu(t)=0.
\tag{8}
\]
For the logarithmic source,
\[
\Delta\vartheta(t)=\log t\,A(t)-\int_p^t\frac{A(s)}s\,ds.
\tag{9}
\]
Integration by parts in (4), using \(h\log=f\), now yields the exact formula
\[
\boxed{E_Q(U)=-\int_p^U A(t)\,d\mu(t)
-h(U)\int_p^U\frac{A(t)}t\,dt.}
\tag{10}
\]
All endpoint counting jumps cancel in this identity; no atom-free cutoff is required. Since \(\Delta\vartheta(t)=O(K\log t)\), the improper integral in (4) converges absolutely. Equations (8) and (10) give its zero limit.

The first term of (10) is bounded both by the available prefix mass \(K[f(p)-f(U)]\) and, by (8), by the available tail mass \(Kf(U)\). The second term is at most \(Kh(U)\log(U/p)\). This proves (5). Finally \(f(U)\le1/(U-1)\), \(\log U\ge L\), and \(\sup_{r\ge1}(\log r)/r=1/e\), so
\[
h(U)\log(U/p)\le\frac1{e(p-1)L}.
\tag{11}
\]
The minimum of two nonnegative quantities summing to \(f(p)\) is at most \(f(p)/2\), proving (6). The factor \(1/2\) is the prefix/tail capacity balance imposed by exact Mertens matching, not an improved prime-distribution theorem.

## 2. Sharpness by finite discrete sources

Let \(p\to\infty\) through primes and let \(K=K(p)\ge1\) be any integer function satisfying
\[
K=o(p/\log p).
\tag{12}
\]
Then
\[
\boxed{\sup_{Q\in\mathcal C_{p,K}}\sup_{U\ge p}|E_Q(U)|
=\left(\frac12+o(1)\right)\frac Kp.}
\tag{13}
\]
The same asymptotic holds if the supremum is restricted to finite modifications with equal numbers of deletions and insertions. It still holds after requiring an arbitrarily prescribed longer frozen prefix \(T(p)\ge p\) with \(T(p)/p\to1\).

Fix a real \(M>1\), independent of \(p\), and put
\[
c_M=\frac{2M}{M+1},\qquad 1<c_M<M.
\tag{14}
\]
Insert \(K\) distinct real labels \(a_i\in(T,T+1)\). Delete \(2K\) distinct ordinary primes \(r_i=c_Mp+o(p)\). Such a cluster exists under (12): each fixed relative neighborhood of \(c_Mp\) contains \(\asymp p/L\) primes by the PNT, so the \(2K\) closest primes have relative distance tending to zero. This uses no shrinking-interval PNT.

The remaining positive Mertens debt is
\[
D_p:=\sum_{i=1}^{2K}f(r_i)-\sum_{i=1}^{K}f(a_i)
=\frac Kp\left(\frac2{c_M}-1+o(1)\right)
=\left(1+o(1)\right)\frac K{Mp}>0.
\tag{15}
\]
Choose distinct offsets \(0<\eta_i<1\). The continuous strictly decreasing function
\[
F_p(v)=\sum_{i=1}^K f(v+\eta_i)
\tag{16}
\]
takes the value \(D_p\) at a unique \(v_p=Mp(1+o(1))\): bracket the root between \((M-\epsilon)p\) and \((M+\epsilon)p\) for each fixed sufficiently small \(\epsilon>0\). Insert the \(K\) labels \(b_i=v_p+\eta_i\). Equations (15)–(16) make the finite Euler-log correction **exactly zero**.

All inserted labels may be chosen distinct from the surviving ordinary primes. To see this without assuming it, allow a common small translation of the early \(a_i\)'s within \((T,T+1)\). Its strictly monotone effect on \(D_p\) makes \(v_p\) strictly monotone too. The forbidden coincidences for either packet exclude only countably many translations. Any remaining translation preserves the root and every asymptotic estimate above.

The three packets are ordered for large \(p\): early insertions, middle deletions, late insertions. Thus \(A\) rises from \(0\) to \(K\), decreases to \(-K\), then rises to \(0\), never leaving \([-K,K]\). The source is strictly increasing after ordering, is unchanged below \(T\), has the same total number of removed and inserted labels, and belongs to \(\mathcal C_{p,K}\). In particular it can also be described as a finite order-preserving transport of indexed ordinary-prime labels; no original-prime-cell restriction is imposed.

Take \(U_p=\min_i r_i-1/2=c_Mp+o(p)\), before every deletion. Only the early packet has appeared, so
\[
\int_p^{U_p}A(t)\,d\mu(t)
=\sum_{i=1}^K[f(a_i)-f(U_p)]
=\frac Kp\left(1-\frac1{c_M}+o(1)\right).
\tag{17}
\]
The second term of (10) is \(O(K/(pL))\). Hence
\[
\boxed{E_Q(U_p)=-\frac Kp\left(\frac{M-1}{2M}+o(1)\right).}
\tag{18}
\]
For every fixed \(M\), this proves the corresponding lower bound for the supremum in (13). Taking the limit inferior in \(p\) first and then letting \(M\to\infty\) gives \(1/2\). Together with (6), this proves (13). No uniform prime theorem on a growing \(Mp\)-shell and no infinite discrete source limit is needed for this order of limits.

### Integer labels attain the same sharp norm through infinite completion

Let \(\mathcal C^{\mathbb Z}_{p,K}\) be the subclass of (2) with
\(Q\subset\{2,3,\ldots\}\), still with no repeated labels. Under (12),
\[
\boxed{\sup_{Q\in\mathcal C^{\mathbb Z}_{p,K}}\sup_{U\ge p}|E_Q(U)|
=\left(\frac12+o(1)\right)\frac Kp.}
\tag{18a}
\]
This remains true with any prescribed frozen prefix \(T=p+o(p)\),
\(T\ge p\). The witnesses below have infinitely many changed labels;
finite integer-label sharpness is not asserted.

Fix \(M>1\) and \(c_M\) as in (14). Replace the early real packet by the
first \(K\) even integers strictly larger than \(T\), denoted \(a_i\).
Then \(a_i=p+o(p)\) uniformly, since \(K=o(p/L)\). Delete \(2K\)
ordinary primes \(r_i=c_Mp+o(p)\), whose availability follows from the
same fixed-relative-neighborhood PNT argument used above. For large
\(p\) the packets are disjoint and ordered. Define
\[
D=\sum_{i=1}^{2K}f(r_i)-\sum_{i=1}^Kf(a_i)
  =(1+o(1))\frac K{Mp}>0,
\qquad
F(n)=\sum_{i=1}^K f(2(n+i)).
\tag{18b}
\]
Choose the integer \(n\) with \(F(n)\ge D>F(n+1)\), and insert the
\(K\) even integers \(b_i=2(n+i)\). Bracketing as in (16) gives
\(2n=Mp(1+o(1))\). The finite Euler-log correction is
\(\delta=F(n)-D\), and the step size telescopes:
\[
0\le\delta<F(n)-F(n+1)
=f(2(n+1))-f(2(n+K+1))
=O_M(K/p^2).
\tag{18c}
\]
The last bound follows by integrating \(-f'(t)=1/[t(t-1)]\) over an
interval of length \(2K\) at height \(Mp(1+o(1))\). In particular the
error is \(O(K/p^2)\), rather than a separate uncontrolled rounding
error for each continuous compensator.

In fact \(\delta>0\). The rational number
\[
C=\frac{\prod_i a_i/(a_i-1)\prod_i b_i/(b_i-1)}
        {\prod_i r_i/(r_i-1)}=e^\delta
\tag{18d}
\]
has strictly positive 2-adic valuation: all inserted labels are even,
their predecessors are odd, and all removed primes are odd. Thus
\(C\ne1\); together with the chosen bracket this proves strict
positivity. This is only a finite-product valuation argument.

Set \(H=2Mp\), beyond every altered finite label for large \(p\).
For ordinary primes \(s>H\), put
\[
\beta_s=f(s)-f(s+1)=\log\frac{s^2}{s^2-1},\qquad
B(H)=\sum_{s>H}\beta_s\sim\frac1{H\log H}.
\tag{18e}
\]
The asymptotic follows from \(\beta_s=s^{-2}+O(s^{-4})\) and the PNT
by partial summation. Also
\(\beta_s/\sum_{r>s}\beta_r\sim(\log s)/s\to0\), so every sufficiently
late term is at most its remaining tail. Therefore Kakeya's subsum
interval criterion gives every number in \([0,B(H)]\) as a sum of a
subset of the \(\beta_s\)'s. The elementary argument is to retain the
residual in the interval from zero to the remaining total: omit a
term if the later tail can still cover the residual, and include it
otherwise. Tail domination makes either chosen residual nonnegative;
the remaining total tends to zero.

The capacity comparison is decisive:
\[
\frac{\delta}{B(H)}=O_M(KL/p)=o(1).
\tag{18f}
\]
Choose a subset \(S\) of the primes above \(H\) with
\(\sum_{s\in S}\beta_s=\delta\), and replace each such \(s\) by
\(s+1\). All these labels are even, above the finite packets, and
distinct. Distinct odd primes differ by at least two, so any subset
of these upward unit shifts preserves strict order and has counting
discrepancy in \(\{-1,0\}\). No real-label adjustment or duplicated
atom remains.

The finite packets make \(A\) rise from zero to \(K\), fall to
\(-K\), then return to zero before \(H\). The tail adds only disjoint
negative unit pulses on \([s,s+1)\). Consequently \(|A(t)|\le K\)
on the entire ray, including \(K=1\). Absolute convergence of
\(\sum\beta_s\), or equivalently (7), now yields
\[
\Gamma(Q)-\gamma=\delta-\sum_{s\in S}\beta_s=0.
\tag{18g}
\]
For completeness, a cutoff can split at most one shifted pair, whose
unmatched Euler-log contribution is \(O(1/x)\). Thus passing from
paired sums to the cutoff definition of \(\Gamma\) does not change
the limit.

The compensating set \(S\) must be infinite. Each finite upward-shift
ratio \((s^2-1)/s^2\) has positive 2-adic valuation, as does \(C\).
No product of \(C\) with finitely many such ratios can equal one.
Their convergent infinite product can equal one in the real topology;
there is no claim of 2-adic convergence.

At \(U_p=\min_i r_i-1/2\), only the early packet is present. Since
every \(a_i=p+o(p)\), (17)--(18) apply unchanged:
\[
E_Q(U_p)=-\frac Kp\left(\frac{M-1}{2M}+o(1)\right).
\tag{18h}
\]
The infinite correction cannot alter this earlier measurement.
Take the limit inferior in \(p\) at fixed \(M\), then let
\(M\to\infty\), and combine with (6). This proves (18a) without a
uniform PNT on a growing shell or a numerical approximation to an
infinite exact product.

## 3. The sharp threshold and near-extremizer geometry

Multiplying (13) by \(\sqrt pL\) proves (1). Within (12), the worst-case normalized discrepancy tends to zero **if and only if**
\[
K\log p/\sqrt p\longrightarrow0.
\tag{19}
\]
At \(K\sim a\sqrt p/L\), its supremum tends to \(a/2\). By (18a), both conclusions hold also for the distinct-integer-label subclass. This sharpens the qualitative distinction between the stable prime-cell/unit-shift classes and the larger relocation classes: exact Mertens matching alone does not remove the counting threshold.

There is also a necessary shape for asymptotically maximal excursions. Suppose \(Q_p\in\mathcal C_{p,K}\) and finite \(U_p\ge p\) satisfy
\[
\frac pK|E_{Q_p}(U_p)|\longrightarrow\frac12.
\tag{20}
\]
Then
\[
\boxed{\frac{U_p}p\longrightarrow2,\qquad
\int_p^{U_p}|A-\tau_pK|\,d\mu
+\int_{U_p}^{\infty}|A+\tau_pK|\,d\mu=o(K/p),}
\tag{21}
\]
where \(\tau_p\in\{-1,1\}\) is the sign of \(\int_p^{U_p}A\,d\mu\), eventually nonzero.

Indeed (11) makes the second term of (10) negligible at the \(K/p\) scale. Both masses in the minimum in (5) must then be \((1/2+o(1))/p\), giving \(U_p/p\to2\). Because \(|A|\le K\) and its total \(\mu\)-integral vanishes, the sum of the two nonnegative defect integrals in (21) is exactly
\[
Kf(p)-2\left|\int_p^{U_p}A\,d\mu\right|=o(K/p).
\tag{22}
\]
This is weighted rigidity of the counting profile, not pointwise rigidity of label displacements. It identifies what a nearly optimal control must do before and after the excursion.

## 4. Prior art, validation, and limits

The general mechanism is classical one-dimensional discrepancy/variation duality and Abel summation. For an authoritative neighboring treatment, see C. Aistleitner and J. Dick, [*Functions of bounded variation, signed measures, and a general Koksma–Hlawka inequality*, Acta Arithmetica **167** (2015), 143–171](https://doi.org/10.4064/aa167-2-4), especially its introduction and signed-measure framework. No novelty is claimed for bounding a Stieltjes integral by counting discrepancy, or for balancing two complementary masses.

The line-local delta is the **sharp Mertens-conditioned Robin norm over admissible discrete sources**, including its finite real-label realization and necessary near-extremizer geometry. RE-154 establishes the relocation scale but not this optimal norm under exact normalization. RE-169 supplies the compensation identity but not a counting-budget extremum. RE-258 and RE-260 establish narrower positional stability and injectivity boundaries; their hypotheses do not classify growing counting budgets. RE-173 permits infinite prime multiplicities and RE-256 constructs local real-label compensation, without the optimal all-height counting-norm statement. The literature comparison does not establish a globally new discrepancy theorem.

The integer realization uses the classical subsum interval criterion
recorded by J. E. Nymann, [*Linear combinations of Cantor sets*,
Colloquium Mathematicum **68** (1995), 259--264](https://doi.org/10.4064/cm-68-2-259-264),
p. 259, attributed there to Kakeya. The criterion and its proof are
not new. RE-260 applies it to a globally unit-shifted, uniformly stable
source. Here the separate finite packet creates the large excursion;
the infinite unit-shift tail absorbs only its integer rounding debt.
Equation (18f) checks that this splice works throughout the same
\(K=o(p/L)\) regime without using an extra counting unit. RE-257's
integer rigidity assumes all alterations are confined to a finite
subdyadic interval, whereas this correction is necessarily unbounded.
The strengthened realization rules out integrality and distinctness
as repairs of the sharp counting-norm obstruction; it does not claim
a new general subsum or Mertens theorem.

The proof is analytic and exact. As a supplementary sign/endpoint check, a 65-digit decimal calculation constructed the three packets with \(M=8\), \(T=p+p^{3/5}\), \(K=\lfloor\sqrt p/\log p\rfloor\), and \(p=1009,10007,100003,1000003\). It checked the counting bound and equality between the atom-sum and (10), with residuals below \(10^{-60}\), and satisfied (5). Those finite floating-point checks are not interval certificates or evidence of the asymptotic theorem; the exact root argument, PNT availability, and inequalities above supply that proof.

For the integer realization, 27 finite packet checks used
\(p\in\{1009,10007,100003\}\), \(M\in\{2,4,8\}\),
\(T=p+\lfloor p^{3/5}\rfloor\), and
\(K\in\{1,\lfloor\sqrt p/L\rfloor,\lfloor p/L^2\rfloor\}\).
Exact rational arithmetic verified the strict Euler-product bracket,
positive 2-adic valuation, distinct labels and counting budget.
At 70 decimal digits the atom and counting formulas agreed within
\(10^{-65}\), and the finite unit-shift capacity from primes in
\((H,2H)\) exceeded the rounding debt in every case. These decimal
comparisons are supplementary, not interval certificates. No finite
calculation certifies the infinite exact match; (18e)--(18g) prove it.

Important boundaries:

- Finite sharpness witnesses use real labels; the distinct-integer witnesses require the infinite correction constructed above. Neither construction satisfies the original-prime-cell restriction. Finite integer prime-cell rigidity and finite ordinary-prime Euler-factor rigidity remain intact, and finite integer-label sharpness is not asserted.
- Infinite modifications are allowed in the upper bound because bounded \(A\) proves the needed convergence. No finite-support valuation argument is passed to an infinite product.
- Exact Mertens matching is essential for the smaller complementary-mass bound in (5); without it the zero integral in (8) is absent.
- The longer frozen prefix may be any \(T=p+o(p)\), including one beyond the known first-annulus localization scale. This is positional source agreement, not a new actual CA state or an altered ordinary divisor sum.
- At the critical budget \(K=O(\sqrt p/L)\), (9) gives a discrepancy from ordinary Chebyshev data of \(O(K\log t)\), smaller than every fixed KV relative envelope for \(t\ge p\) as \(p\to\infty\). This is fidelity of the *difference* and does not upgrade the KV constant available for ordinary primes.
- A zero full-tail difference does not force each truncated integral to vanish. Conversely the supremum over synthetic sources is not a lower bound for an actual ordinary-prime excursion.

**Research consequence:** an independent argument forcing counting fidelity \(o(\sqrt p/\log p)\) would suffice for uniform Robin stability even with infinitely many changes. At the critical scale, exact Mertens fidelity and a longer \(p+o(p)\) frozen prefix still allow a finite-height, source-realized excursion, even with distinct integer labels. The composite integer labels remain synthetic Euler atoms; their factors \(q/(q-1)\) are not the ordinary divisor-sum contributions of those composite integers. The arithmetic task remains to justify stronger fidelity or a signed restriction for actual CA-selected primes; no Robin inequality or RH conclusion follows here.
