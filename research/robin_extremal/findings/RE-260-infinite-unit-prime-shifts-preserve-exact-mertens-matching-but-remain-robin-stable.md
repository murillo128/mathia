# RE-260 — Infinite unit prime shifts preserve exact Mertens matching but remain uniformly Robin-stable

**Status:** LITERATURE+DERIVED + EXACT-SOURCE-CLASSIFICATION + FINITE-SUPPORT-RIGIDITY-BOUNDARY + UNIFORM-ROBIN-STABILITY; independent adversarial review pending.

**Dependencies:** RE-258 (finite integer prime-cell rigidity), RE-169 (Mertens compensation identity), RE-173 (the distinct infinite prime-multiplicity control). Classical prime number theorem and Kakeya's subsum interval criterion, proved in the form needed below.

RE-258's finite-support assumption is essential even for changes of **at most one unit per prime**, with no deletion, duplication, or departure from the original prime cells. After any sufficiently large frozen prime prefix, infinite unit shifts can preserve the ordinary Mertens constant exactly. Nevertheless, every such transport changes every truncated future Robin integral by only \(O(p^{-1/2})\) after Robin normalization. Thus source injectivity fails while quantitative stability survives, including at horizons beyond the first annulus. This is a theorem about synthetic integer-labelled sources, not about alternative ordinary primes or the ordinary divisor-sum function.

## 1. Exact Mertens range of the unit-shift class

Enumerate the ordinary primes \(p_j\), fix a sufficiently large prime \(p=p_m\), and let \(\mathcal U_p\) consist of strictly increasing integer-labelled sequences \(Q=(q_j)\) such that
\[
q_j=p_j\quad(j\le m),\qquad q_j-p_j\in\{-1,0,1\}\quad(j>m).
\tag{1}
\]
Support may be infinite. Strict increase is part of the definition: arbitrary mixed choices at twin primes can collide. The one-sign choices and the particular mixed construction below do not collide. Since consecutive odd primes differ by at least two, every admitted source satisfies the original-cell condition
\[
p_{j-1}<q_j<p_{j+1}\qquad(j>m).
\tag{2}
\]

Put
\[
f(t)=\log\frac{t}{t-1},\qquad
\Gamma(Q)=\lim_{x\to\infty}\left(\sum_{q_j\le x}f(q_j)-\log\log x\right).
\]
For an odd prime \(r\), define the positive changes
\[
\begin{aligned}
a_r&=f(r-1)-f(r)=\log\frac{(r-1)^2}{r(r-2)},\\
b_r&=f(r)-f(r+1)=\log\frac{r^2}{r^2-1},\\
A(p)&=\sum_{r>p,\ r\ \mathrm{prime}}a_r,\qquad
B(p)=\sum_{r>p,\ r\ \mathrm{prime}}b_r.
\end{aligned}\tag{3}
\]
Then every limit \(\Gamma(Q)\) exists, and the exact attainable range is
\[
\boxed{\{\Gamma(Q)-\gamma:Q\in\mathcal U_p\}=[-B(p),A(p)],
\qquad A(p)\sim B(p)\sim\frac1{p\log p}.}\tag{4}
\]
In particular,
\[
\boxed{\exists Q\in\mathcal U_p:\quad Q\ne P,\quad
\Gamma(Q)=\gamma.}\tag{5}
\]
Every nonidentity source in (5) has infinitely many changed indices. This is a stricter positional class than the full prime cells of RE-258; its Mertens range has scale \(1/(p\log p)\), compared with the \(1/p\) scale of the full-cell envelopes there.

### Convergence and the classical subsum mechanism

The expansions \(a_r=r^{-2}+O(r^{-3})\) and \(b_r=r^{-2}+O(r^{-4})\) give
\[
\sum_{j>m}|f(q_j)-f(p_j)|<\infty.
\]
At a cutoff \(x\), the difference between the paired partial sum and the difference of the two cutoff sums is \(O(x^{-1})\): only primes within one unit of \(x\) can be unmatched. Classical Mertens therefore yields the exact identity
\[
\Gamma(Q)-\gamma=\sum_{j>m}[f(q_j)-f(p_j)].\tag{6}
\]
No conditional rearrangement or formal infinite rational product is used.

The PNT and partial summation give
\[
\sum_{r>x,\ r\ \mathrm{prime}}r^{-2}\sim\frac1{x\log x}.
\tag{7}
\]
Consequently both coefficient sequences in (3), when restricted to sufficiently large primes, satisfy the tail domination conditions
\[
a_r\le\sum_{s>r}a_s,\qquad b_r\le\sum_{s>r}b_s.
\tag{8}
\]
Here and below the sums over \(r,s\) are over ordinary primes.

For completeness, if \(c_n>0\), \(\sum c_n<\infty\), and \(c_n\le\sum_{k>n}c_k\) for every \(n\), then every \(z\in[0,\sum c_n]\) is a subsum. With a current residual \(z_n\in[0,c_n+R_n]\), \(R_n=\sum_{k>n}c_k\), omit \(c_n\) if \(z_n\le R_n\); otherwise include it. In the latter case \(0\le z_n-c_n\le R_n\), because \(R_n\ge c_n\). The residual after either decision lies in \([0,R_n]\), hence tends to zero. This is the classical Kakeya interval argument.

For \(z\in[0,A(p)]\), apply this argument to the \(a_r\) and shift precisely its chosen primes down by one. Such one-sign choices are strictly increasing, including at the frozen-prefix boundary. For \(z\in[-B(p),0]\), apply it to the \(b_r\) and shift the selected primes up by one. Writing \(q(r)\) for the replacement of original prime \(r\), termwise bounds \(-b_r\le f(q(r))-f(r)\le a_r\) give containment in the interval (4), even for mixed choices. This proves (4), including attained endpoints (all tail primes shifted in one direction).

### A nontrivial exactly normalized source

Let \(r\) be the first prime after \(p\). For sufficiently large \(p\),
\[
0<a_r<B(r),\tag{9}
\]
by (7). Choose a subset \(S\) of the primes larger than \(r\) such that
\[
\sum_{s\in S}b_s=a_r.\tag{10}
\]
Set \(q(r)=r-1\), \(q(s)=s+1\) for \(s\in S\), and leave every other prime unchanged (again \(q(r)\) denotes the replacement label). The initial downward move followed only by upward moves is strictly increasing. Equation (6) gives \(\Gamma(Q)=\gamma\), and \(Q\ne P\).

The set \(S\) must be infinite. If it were finite and nonempty, let \(s\) be its largest element. All earlier replacement labels are less than \(s\), whereas the last changed Euler-factor ratio is
\[
\frac{(s+1)/s}{s/(s-1)}=\frac{s^2-1}{s^2},
\]
whose \(s\)-adic valuation is \(-2\). No earlier ratio has a nonzero \(s\)-adic valuation, so the finite product cannot equal one. The empty set cannot pay the positive debt \(a_r\). This reconstructs the relevant RE-258 finite obstruction and explains precisely why it disappears in (10).

## 2. Uniform stability of every future Robin integral

For \(S=P,Q\), define
\[
\vartheta_S(t)=\sum_{s\in S,\ s\le t}\log s,\quad
h(t)=\frac{f(t)}{\log t},\quad k(t)=\frac1{t\log t},\quad
I_S(t)=(\vartheta_S(t)-t)h'(t)-(h(t)-k(t)).
\]
There is an absolute constant \(C\) such that, for all sufficiently large primes \(p\),
\[
\boxed{\sup_{Q\in\mathcal U_p}\sup_{p\le U\le\infty}
\left|\sqrt p\log p\int_p^U(I_Q-I_P)(t)\,dt\right|
\le C p^{-1/2}.}\tag{11}
\]
There is no exact-Mertens hypothesis in (11), and no upper restriction on \(U\).

To retain the cancellation inside each shifted atom, for finite \(U\ge p\) define
\[
J_U(s)=\begin{cases}\log s\,[h(U)-h(s)],&p<s\le U,\\0,&s>U.\end{cases}
\]
Fubini for the finitely many atoms below \(U\) gives the exact identity
\[
\int_p^U(I_Q-I_P)(t)\,dt
=\sum_{j>m}[J_U(q_j)-J_U(p_j)].\tag{12}
\]
The function is continuous at \(s=U\). On \(p<s<U\),
\[
J_U'(s)=\frac{h(U)}s+\frac1{s(s-1)}.
\tag{13}
\]
Since \(h\) is positive and decreasing, \(0\le J_U'(s)\ll s^{-2}\); above \(U\) its derivative is zero. Thus each summand in (12) has absolute value at most \(C p_j^{-2}\), uniformly in \(U\), including when a shifted atom straddles the cutoff. Summing (7) gives \(O((p\log p)^{-1})\), proving (11) at finite \(U\). The same majorant permits \(U\to\infty\), with \(J_U(s)\to-f(s)\), and yields
\[
\boxed{\int_p^\infty(I_Q-I_P)(t)\,dt
=-(\Gamma(Q)-\gamma).}\tag{14}
\]
In particular the exactly normalized nonidentity source (5) has zero full-tail difference, while each intermediate discrepancy is bounded by (11). Any subannulus with both endpoints at least \(p\) has the same \(O(p^{-1/2})\) normalized bound by subtracting two prefixes.

These are also quantitatively faithful counting sources. Interlacing (2) gives \(|\Pi_Q(t)-\pi(t)|\le1\). With the frozen prefix, Abel summation gives
\[
\vartheta_Q(t)-\vartheta(t)
=\log t\,[\Pi_Q(t)-\pi(t)]
-\int_p^t\frac{\Pi_Q(u)-\pi(u)}u\,du
=O(\log t).\tag{15}
\]
Thus the *difference from ordinary primes* is below every fixed Korobov–Vinogradov envelope. This does not assert that ordinary primes satisfy arbitrary KV constants; \(Q\) inherits whichever ordinary-prime bound is actually available, with the harmless additional \(O(\log t)\) error.

## 3. Prior art and the exact research boundary

Kakeya's subsum criterion is classical. J. E. Nymann, [*Linear combinations of Cantor sets*, Colloquium Mathematicum **68** (1995), 259–264](https://doi.org/10.4064/cm-68-2-259-264), p. 259, states the interval criterion and attributes it to S. Kakeya, *On the partial sums of an infinite series*, Tôhoku Science Reports **3** (1914), 159–164. The argument needed here is fully reconstructed above. The PNT tail estimate (7) and the pairwise mean-value bound (13) are standard. No new theorem about subsum sets or prime distribution is claimed.

The closest local comparison is RE-173, whose infinite compensation deletes and duplicates ordinary-prime atoms and permits an order-one transient Robin displacement. It does not preserve one label per original prime, bounded positional displacement, or the unit interlacing bound. Here the new source-class conclusion is the **simultaneous** exact range (4), nontrivial exact normalization (5), and all-horizon stability (11) under unit integer displacement. RE-258 establishes finite product rigidity and finite-support cell stability; it does not establish this infinite exactly normalized class. These distinctions change which source-fidelity conclusion remains justified when finite support is removed.

Checks against overstatement:

- An infinite real-convergent product has no largest changed prime. Applying the finite valuation certificate to its limit would be invalid; every finite nontrivial truncation remains non-normalized.
- The inserted labels \(r-1\) and \(s+1\) are composite even integers for the primes used here. They are synthetic Euler atoms, not ordinary-prime factorizations of those integers.
- All labels below \(p\) are frozen. No claim about a new ordinary CA state or a new infinite family of actual Robin counterexamples is made.
- Exact equality of Mertens constants does not identify the source, even in this unit-shift class. It also does not create an order-one hidden Robin excursion: (11) rules that out uniformly over the entire future.
- The interval (4) is an infinite-source classification. Finite modifications cannot attain its nontrivial zero fiber; using numerical truncations would not prove exact equality.

**Research consequence:** finite prime-cell Mertens injectivity cannot be used as a uniqueness theorem for infinite sources. The positional stability mechanism is stronger and survives this loss of injectivity. Unit shifts therefore provide an exact-normalization control without reopening the order-one remote-tail ambiguity; the actual-prime, CA-selected signed tail in RE-259 remains unestimated.
