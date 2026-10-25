# RE-267 — Net counting budget controls positive Robin excursions without a pair-count bound

**Status:** EXACT-DERIVED + ONE-SIDED-SOURCE-STABILITY; independent adversarial review pending.

**Dependencies:** RE-261 (counting representation of the Robin source integral), RE-263 (subdyadic two-prime classification), RE-266 (single-pair sign geometry).

RE-266 bounds the positive excursion by the number of independently matched pairs. That number can exceed the source's net counting discrepancy, because different repairs can cancel at a counting cutoff. Nevertheless, quadratic positive stability survives with the **net counting budget alone**, for an arbitrary finite number of such pairs. The new input is a nonnegative weighted counting primitive, combined with a uniform quadratic lower bound on the first possible positive height. No assertion of an optimal leading constant is made here.

## 1. The larger source class

Let \(p\ge3\) be an ordinary prime. Form
\[
Q=(\mathbb P\setminus D)\cup B
\]
from any finite number \(m\) of nontrivial, individually exact repairs
\[
\{r_j,s_j\}\longmapsto\{a_j,b_j\},\qquad
3\le r_j<s_j<2r_j,
\qquad
\frac{a_j}{a_j-1}\frac{b_j}{b_j-1}
=\frac{r_j}{r_j-1}\frac{s_j}{s_j-1}.
\tag{1}
\]
The deleted labels are distinct ordinary primes; the inserted labels are distinct composite integers; different repairs have disjoint labels; and every altered label exceeds \(p\). Order \(a_j<b_j\). Assume only
\[
A(t):=\Pi_Q(t)-\pi(t),\qquad \sup_{t\ge p}|A(t)|\le K,
\quad K\ge1.
\tag{2}
\]
There is **no bound on \(m\) in terms of \(K\)**. Finite matching in (1) gives equal insertion/deletion counts and exact Mertens normalization \(\Gamma(Q)=\gamma\), where
\[
f(t)=\log\frac{t}{t-1},\qquad h(t)=\frac{f(t)}{\log t},\qquad
\Gamma(Q)=\lim_{x\to\infty}
\left(\sum_{q\in Q,\ q\le x}f(q)-\log\log x\right).
\]
Put
\[
\Delta\vartheta(t)=\sum_{q\in Q,\ q\le t}\log q
-\sum_{r\in\mathbb P,\ r\le t}\log r,
\qquad E_Q(U)=\int_p^U\Delta\vartheta(t)h'(t)\,dt.
\tag{3}
\]
Then
\[
\boxed{E_Q(U)\le0\quad(p\le U\le2p^2),}
\tag{4}
\]
and, uniformly in the number, heights and interleaving of the repairs,
\[
\boxed{\sup_{U\ge p}E_Q(U)
\le K h(2p^2)\log(2p)
=\left(\frac14+O\!\left(\frac1{\log p}\right)\right)\frac K{p^2}.}
\tag{5}
\]
The supremum is nonnegative because \(E_Q(p)=0\). This is a one-sided statement; negative excursions can still have order \(K/p\), as in RE-265.

For a family of such sources, an order-one positive Robin-normalized excursion requires a much larger net counting budget than the unrestricted critical scale. Specifically, if
\[
\sqrt p\log p\,E_Q(U)\ge\delta>0,
\]
then
\[
\boxed{K\ge(4\delta+o(1))\frac{p^{3/2}}{\log p}.}
\tag{6}
\]
In particular \(K=o(p^{3/2}/\log p)\) forces the positive normalized supremum to tend to zero, regardless of how many pairs are used. The constant four in this necessary bound is not claimed sharp.

## 2. Pairwise exactness supplies a nonnegative primitive

For one pair, write \(P=rs\). Reconstructing the classification input: the subdyadic odd-prime hypothesis excludes \(r\mid s-1\). Both deleted primes therefore survive in the reduced numerator of the deleted Euler product. If they divide different insertion numerators and neither insertion contains both, monotonicity of \(t/(t-1)\) forces the trivial replacement. A nontrivial repair consequently has
\[
b=kP,\quad k\ge1,\qquad
a=\frac{kP-1}{k(r+s-1)-1},\qquad
p<a<r<s<b.
\tag{7}
\]
In particular
\[
a\le\frac{P-1}{r+s-2},\qquad
P\ge a(r+s-2)+1\ge2a\sqrt P-2a+1.
\]
Factoring the final quadratic as
\((\sqrt P-1)(\sqrt P-(2a-1))\ge0\) gives
\[
\sqrt P\ge2a-1>2p,
\tag{8}
\]
where the last inequality uses the integer condition \(a\ge p+1\).

Define \(d\mu(t)=dt/[t(t-1)]=-f'(t)dt\) and
\[
M_j(U)=\int_p^U A_j(t)\,d\mu(t),
\]
where \(A_j\) is the counting discrepancy of this pair. Its only nonzero intervals are \(A_j=1\) on \([a,r)\) and \(A_j=-1\) on \([s,b)\). Thus
\[
M_j(U)=
\begin{cases}
0,&U<a,\\
f(a)-f(U),&a\le U<r,\\
f(a)-f(r),&r\le U<s,\\
f(U)-f(b),&s\le U<b,\\
0,&U\ge b.
\end{cases}
\tag{9}
\]
The late branch and the zero terminal value use the exact identity
\(f(a)+f(b)=f(r)+f(s)\). Every branch is nonnegative. Summing over the finite family, even when its positive and negative counting intervals interleave, proves
\[
\boxed{M(U):=\int_p^U A(t)\,d\mu(t)=\sum_{j=1}^m M_j(U)\ge0.}
\tag{10}
\]
This does not assert that \(A\) itself is nonnegative, nor that the truncated Euler-log difference is nonnegative: the latter is \(f(U)A(U)+M(U)\). The primitive in (10) is the particular invariant needed below.

## 3. No individual positive contribution before quadratic height

The single-pair logarithmic discrepancy is positive on \([a,r)\), negative on \([r,b)\), and positive after \(b\). Since \(h'<0\), its integral decreases from zero to \(r\), increases from \(r\) to \(b\), then decreases towards zero. For \(s\le U\le b\), direct integration gives
\[
E_j(U)=f(b)-h(U)\log(P/a).
\tag{11}
\]
The point \(P/2\) lies strictly between \(s\) and \(b\), since \(r\ge3\). Also \(a<\sqrt P\), so
\[
\log(P/a)>\tfrac12\log(P/2).
\]
The elementary strict inequality
\[
f(P/2)>2f(P)
\tag{12}
\]
follows from \((P-1)^2>P(P-2)\). Therefore
\[
h(P/2)\log(P/a)>f(P)\ge f(b),
\qquad E_j(P/2)<0.
\tag{13}
\]
The preceding monotonicity gives \(E_j(U)\le0\) for every \(U\le P/2\). By (8), \(P/2>2p^2\). Summing proves (4). No upper bound on \(k\) or on the insertion height is used.

## 4. The net count controls every later cutoff

The exact Abel-summation formula of RE-261 is
\[
E_Q(U)=-M(U)-h(U)\int_p^U\frac{A(t)}t\,dt.
\tag{14}
\]
For completeness, it follows by integrating (3) by parts and using
\[
\Delta\vartheta(U)=\log U\,A(U)-\int_p^U A(t)\frac{dt}{t},
\qquad
\sum_{q\le U}f(q)-\sum_{r\le U,\ r\in\mathbb P}f(r)
=f(U)A(U)+M(U).
\]
The endpoint counting terms cancel, so these formulas include cutoffs at altered labels.

By (2) and (10),
\[
E_Q(U)\le K h(U)\log(U/p).
\tag{15}
\]
This step uses the net discrepancy, not \(\sum_j|A_j|\). Put
\(g_p(U)=h(U)\log(U/p)\). Differentiating and using
\(f(U)\le1/(U-1)\) gives
\[
g_p'(U)
=-\frac{\log(U/p)}{U(U-1)\log U}
 +\frac{f(U)\log p}{U(\log U)^2}
\le\frac{\log p-\log(U/p)\log U}
 {U(U-1)(\log U)^2}<0
\tag{16}
\]
for \(U\ge2p^2\), because \(\log(U/p)>1\) and \(\log U>\log p\).
Combine the early sign (4) with (15)--(16) to obtain (5).
Finally
\[
h(2p^2)\log(2p)
=f(2p^2)\frac{\log(2p)}{\log(2p^2)}
=\frac{1+O(1/\log p)}{4p^2},
\]
which proves the normalization consequences.

## 5. Controls, prior art and the remaining boundary

The larger admissible class is concrete. The two exact repairs, displayed as \((a,r,s,b)\),
\[
(21,31,61,1891),\qquad
(1001,1901,2113,20084065)
\tag{17}
\]
have disjoint labels, prime deletions and composite insertions. The second has \(b=5\cdot1901\cdot2113\). At prefix \(p=19\), their combined counting path at the eight ordered events is
\[
1,\ 0,\ -1,\ 0,\ 1,\ 0,\ -1,\ 0.
\]
Thus \(m=2\) but the net counting budget is one. The early insertion of the second repair lies inside the negative counting interval of the first; this tests actual overlap rather than merely adjoining two separated supports. RE-266's pair-count bound cannot replace its pair number by this net budget without an additional argument.

Supplementary exact checks enumerated the RE-263 candidate for all subdyadic odd-prime pairs with both primes below 5000. There were 1096 valid repairs with composite early insertion; all passed exact rational Euler equality, label ordering and the bound \(P\ge(2a-1)^2\). The 92 such repairs below 500 were used individually, together with (17) and disjoint two/three-pair groupings, for 120 source diagnostics. At 40 and 80 decimal digits, direct signed-atom integration agreed with (14), and (10), the sign at every \(P_j/2\), (4) and (5) passed at event cutoffs, intervening midpoints and a cutoff beyond all insertions. Primality was checked by an integer sieve. These logarithmic checks are numerical diagnostics, not interval certificates or a proof of the universal bound; the proof is (7)--(16).

The algebraic mechanism remains the elementary valuation and shifted-product analysis of RE-263; a classical comparison is T. Chen and R. Koo, [*Two-term Egyptian fractions*, Notes on Number Theory and Discrete Mathematics **19** (2013), 15--25](https://www.nntdm.net/papers/nntdm-19/NNTDM-19-2-15-25.pdf), Section 2. The signed counting integration belongs to the classical discrepancy/variation framework; compare C. Aistleitner and J. Dick, [*Functions of bounded variation, signed measures, and a general Koksma--Hlawka inequality*, Acta Arithmetica **167** (2015), 143--171](https://arxiv.org/abs/1406.0230). Neither paper is asserted to contain this Robin repair theorem. Searches by Euler-product matching, Mertens counting discrepancy, cumulative-sign bounds and Abel/majorization mechanisms support only this source-specific derived claim, not a globally new general inequality. No external prime-supply theorem is needed for the upper bound.

The mathematical delta is removal of the pair-count restriction: adding arbitrarily many independently matched pairs and hiding their number through counting cancellations cannot recover a positive critical Robin excursion. The proof needs both the nonnegative primitive and delayed positivity. Dropping the former recovers only the general \(O(K/p)\) counting bound; using the primitive without the height restriction would leave only a much weaker bound from (15).

This does not determine the sharp constant for the larger class. RE-266 retains its sharper \(1/8\) asymptotic constant under its different hypothesis of at most \(K\) pairs. Larger inseparable Euler-matched packets, prime-chain deletions outside the subdyadic class, and infinite completions are not covered here. Finite count preservation and exact Mertens matching alone do not imply (9) or (4).

All composite labels carry synthetic factors \(q/(q-1)\), not their ordinary divisor-sum factors. No constraint on actual CA exponent vectors, signed ordinary-prime tail estimate, Robin inequality or RH conclusion is established.
