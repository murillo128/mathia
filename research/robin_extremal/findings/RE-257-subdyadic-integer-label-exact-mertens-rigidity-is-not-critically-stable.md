# RE-257 — Subdyadic integer labels make exact Mertens matching rigid but not critically stable

**Status:** EXACT-DERIVED + SUBDYADIC-INTEGER-RIGIDITY + SHARP-QUALITATIVE/QUANTITATIVE-FIDELITY-SEPARATION + ORDINARY-PRIME-APPLICATION-OPEN; independent adversarial review pending.

**Dependencies:** RE-169 (finite-source Mertens sum rule), RE-172 (prime-supported finite exact rigidity and the unrestricted integer-label caveat), RE-254 (rounding of smooth near-frontier transports), RE-255 (critical triangular endpoint fidelity), RE-256 (two adjacent critical shells with exact real-label Mertens balance); Guth–Maynard's pointwise short-interval theorem as already recorded in SOURCES.md.

RE-256 matches the ordinary Mertens normalization exactly using **real** generalized-prime labels inside two consecutive near-frontier shells. RE-172 proves exact finite Mertens rigidity when all altered labels themselves remain primes, but explicitly notes that unrestricted **integer** labels admit telescoping relations. There is a sharper *local* distinction: in any interval shorter than a factor of two, an ordinary-prime source is already exactly Mertens-rigid against **arbitrary positive-integer replacement labels**, even with no rank or counting constraint. Nevertheless, rounding RE-256 produces nontrivial integer-label sources with Mertens mismatch far *below* the Robin-critical scale and an order-one first-shell moment. Thus exact integer rigidity supplies no uniform critical-scale stability.

## 1. Exact subdyadic Euler-factor rigidity

**Theorem.** Let \(3<A<B<2A\). Let \(P\) be any finite set of ordinary primes in \((A,B)\), and \(Q\) any finite multiset of integers in \((A,B)\). Define
\[
\mathscr E(S)=\prod_{n\in S}\frac{n}{n-1},
\]
with multiplicities. Then
\[
\boxed{\mathscr E(Q)=\mathscr E(P)\quad\Longrightarrow\quad Q=P}
\tag{1}
\]
as multisets. No matching-count, rank, spacing, prime-distribution, or CA-selector hypothesis is required.

**Proof.** Fix \(q\in P\). Because all members of \(P\) are odd primes, the factor \(q/(q-1)\) contributes exactly one positive \(q\)-adic valuation. Other prime numerators contribute none. If \(r\in P\), then
\(0<r-1<B<2A<2q\); a denominator \(r-1\) divisible by \(q\) would therefore have to equal \(q\), making \(r=q+1\), an even integer greater than two and hence not a prime. Thus
\[
v_q(\mathscr E(P))=1.
\tag{2}
\]
For every \(n\in Q\), both \(n\) and \(n-1\) are strictly below \(2q\). The only possible positive \(q\)-valuation among the numerator factors is at \(n=q\), and the only possible negative valuation is at \(n=q+1\). Writing \(m_Q(n)\) for multiplicity (zero when \(n\notin Q\)),
\[
v_q(\mathscr E(Q))=m_Q(q)-m_Q(q+1).
\tag{3}
\]
Equal products imply \(m_Q(q)-m_Q(q+1)=1\), so \(m_Q(q)\ge1\). This holds for every \(q\in P\): \(P\) is a submultiset of \(Q\). But every additional integer factor \(n/(n-1)\) is strictly greater than one. Product equality therefore excludes any extra labels, including duplicate primes. Hence \(Q=P\). \(\square\)

The subdyadic restriction is substantive, not a cosmetic assumption: outside it, the exact telescoping identity
\[
\frac21=\frac32\cdot\frac43
\tag{4}
\]
shows that arbitrary integer labels can reproduce a prime Euler factor. This example does **not** imply that the factor-of-two bound is the best possible threshold in every special interval; it only invalidates unrestricted global integer-label injectivity.

## 2. Consequence for the two-shell RE-256 construction

Let \(p\to\infty\) through ordinary primes, \(L=\log p\), and set
\[
e_p=e^{-L^{1/4}},
\qquad
H=H_\star(p)=\frac{p^{3/4}}{\sqrt L}e^{L^{1/4}/2}.
\tag{5}
\]
For sufficiently large \(p\), \(2H<p\), so all of \((p,p+2H)\) lies inside one subdyadic interval \((p,2p)\).

Suppose a positive-integer-label generalized-prime source \(Q_p\) agrees with the ordinary primes outside \((p,p+2H)\), changes only finitely many labels, and has the same exact Mertens normalization \(\Gamma(Q_p)=\gamma\) in the sense of RE-169. Finite support gives
\[
\Gamma(Q_p)-\gamma
=
\log\mathscr E\bigl(Q_p\cap(p,p+2H)\bigr)
-\log\mathscr E\bigl(P\cap(p,p+2H)\bigr).
\tag{6}
\]
Theorem (1), applied with \(A=p\) and any \(B\) strictly between the largest potentially altered label and \(2p\), implies
\[
\boxed{\Gamma(Q_p)=\gamma\quad\Longrightarrow\quad Q_p=P.}
\tag{7}
\]
In particular the nonzero first-shell signed discrepancy of RE-256 cannot coexist with **both exact global Mertens matching and integer labels** when its entire alteration is confined to these \(o(p)\) adjacent shells. This implication even survives loss of rank or count fidelity. It does not assume that arbitrary integer labels are primes.

## 3. Critical-scale near-matching still permits an order-one first shell

The exact rigidity of (7) is discontinuous at zero. Fix \(a>0\), take the real-label map \(F_{\lambda_p}\) constructed in RE-256, equations (6)–(12) there, with its exact Mertens root \(\lambda_p\), and round **each resulting label separately**:
\[
\widehat Q_p=
\left\{
\left\lfloor F_{\lambda_p}(q)+\tfrac12\right\rfloor
:q\text{ an ordinary prime}
\right\}.
\tag{8}
\]
For sufficiently large \(p\), the source is strictly increasing. Indeed RE-256 gives \(F_{\lambda_p}'=1+O_a(Le_p)\ge3/4\); the gap between successive odd primes is at least two, so after nearest-integer rounding successive labels are still separated by at least \(3(2)/4-1=1/2>0\). The pair \(2,3\) remains untouched.

All labels outside the two compact bump supports are identical to the original primes, and no displaced label crosses \(p+H\) or \(p+2H\). The entire genuine-prime/CA prefix through \(p+H/4\), the rank, and the number of labels in each of the two shells remain identical to RE-256. The source is nontrivial: the first bump is positive on a fixed subinterval containing \(\asymp H/L\) ordinary primes, while its displacement scale \(aLe_pH\) tends to infinity.

Write \(M_p\) for the number of labels meeting the two bump supports. The pointwise Guth–Maynard estimate, as applied in RE-256, yields \(M_p=O_a(H/L)\). The derivative of \(f(t)=\log(t/(t-1))\) has magnitude \(1/[t(t-1)]\ll p^{-2}\) on these supports. Since rounding changes each real label by at most \(1/2\), exact real-label balance gives
\[
\begin{aligned}
0<|\Gamma(\widehat Q_p)-\gamma|
&=\left|\sum_q\bigl[f(\lfloor F_{\lambda_p}(q)+1/2\rfloor)-f(F_{\lambda_p}(q))\bigr]\right|\\
&\ll\frac{M_p}{p^2}
\ll\frac{H}{Lp^2}
=o\!\left(\frac1{\sqrt pL}\right).
\end{aligned}
\tag{9}
\]
The **strict** inequality follows from (7) and the proven nontriviality of \(\widehat Q_p\), not from assuming that the individual rounding errors have one sign.

For either endpoint \(b=p+H\) or \(b=p+2H\), exactly the same atoms enter the real and rounded triangular sums. Their total change in the triangular statistic is at most \(M_p/2\). Using RE-256's exact real-label limits therefore proves
\[
\boxed{
\frac L{p^{3/2}}\bigl(D_{\widehat Q_p,p}(H)-D_{P,p}(H)\bigr)
=-a+o(1),\qquad
\frac L{p^{3/2}}\bigl(D_{\widehat Q_p,p}(2H)-D_{P,p}(2H)\bigr)=o(1).
}
\tag{10}
\]
The error contributed by rounding after scaling is at most
\(LM_p/p^{3/2}\ll H/p^{3/2}=o(1)\).

The exact finite-kernel identity RE-256(18) also applies to each of the endpoints. Rounding changes its finite Euler-factor sum by \(O(M_p/p^2)\) and its terminal Chebyshev-weight sum by \(O(M_p/p)\); since \(h(b)\ll(pL)^{-1}\), its normalized effect is \(O(H/p^{3/2})=o(1)\). Consequently
\[
\boxed{
\sqrt pL\int_p^{p+H}(I_{\widehat Q_p}-I_P)(t)\,dt=a+o(1),\qquad
\sqrt pL\int_p^{p+2H}(I_{\widehat Q_p}-I_P)(t)\,dt=o(1).
}
\tag{11}
\]

Finally, RE-256's real transported points are separated by at least \(3/2\), so replacing each by the nearest integer alters the counting function at any threshold by at most one. Every interval count changes by at most two. Since
\(x^{3/5}\exp(-(\log x)^{1/4})\to\infty\), this additive two is absorbed in the same common **all-start** Guth–Maynard-scale envelope for \(x^{3/5}\le y\le x^{0.99}\), after choosing a fixed sufficiently large \(x_0\). There is no claim that integer rounding preserves the real transport's \(1+o(1)\) *relative adjacent-gap ratios*: an additive unit is not negligible in a twin-prime gap.

Thus **exact matching plus integer labels is rigid locally, but even \(o((\sqrt p\log p)^{-1})\) Mertens matching plus integer labels, unchanged CA prefix and all-start short-interval PNT does not control the critical first-shell signed moment**.

## 4. Prior art, stress tests, and boundary

The proof of (1) is an elementary \(q\)-adic valuation/unique-factorization argument, not a new prime-distribution theorem. RE-172 already proves rational linear independence for the factors attached to *prime-supported* perturbations of arbitrary finite extent and explicitly exhibits (4) to show why unrestricted integer labels do not inherit its global theorem. The new contribution is the **subdyadic localization that restores exact integer-label rigidity** without assuming Q consists of primes, together with the quantitative rounding contrast for RE-256's two *near-frontier* shells. RE-254 already proves the one-shell integer rounding mechanism without exact Mertens balance; RE-256 proves two-shell exact Mertens balance for real labels. Neither contains the combination (7), (9), and (10). A structural prior-art search found the underlying unique-factorization and Mertens-product principles, but no need for any external theorem beyond the existing Guth–Maynard source and these elementary facts; no SOURCES.md change is justified.

Falsification boundaries: (i) positivity of every factor \(n/(n-1)\) is essential when passing from \(P\subseteq Q\) to \(P=Q\); signed or rational multiplicity perturbations are not covered by (1). (ii) Moving labels outside the subdyadic support or allowing real noninteger labels escapes (7). (iii) The rounded source has potentially **composite** integer labels and is not a second ordinary-prime sequence, so (10)–(11) do not imply an ordinary-prime Robin counterexample or a new bound for the actual prime moment. (iv) Exact injectivity alone supplies no lower bound at the Robin-critical scale for a nonzero rational Euler-product difference. The construction (9) witnesses precisely this lack of quantitative stability.

**Research consequence:** The apparent conflict between RE-172's prime-only rigidity and RE-256's real-label exact compensation is resolved more finely: *integer support within a single subdyadic critical neighborhood is already enough for exact rigidity*, but only **genuinely quantitative arithmetic fidelity**, not exact-product injectivity considered in isolation, could suppress the order-one near-frontier Robin source excursion. The ordinary-prime and remote-annulus questions remain open; RH is not proved.
