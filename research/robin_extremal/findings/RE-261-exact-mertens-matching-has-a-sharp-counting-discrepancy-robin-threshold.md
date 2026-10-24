# RE-261 — Exact Mertens matching has a sharp counting-discrepancy Robin threshold

**Status:** EXACT-DERIVED + SHARP-SOURCE-STABILITY + DISCRETE-REAL-AND-INTEGER-LABEL-REALIZATION + CLASSICAL-DISCREPANCY-MECHANISM; independent adversarial review pending.

**Dependencies:** RE-169 (Mertens compensation), RE-154 (post-selector relocation scale), RE-258 (prime-cell counting bound), RE-260 (infinite exact matching with unit shifts). The prime-distribution inputs to sharpness are the classical PNT and, for finite integer-label splitting, its fixed-modulus arithmetic-progression version.

Prime-cell interlacing and unit displacement impose strong source fidelity. The relevant more general quantity is the **maximum counting discrepancy**, rather than the number of modified atoms or finite support. With exact Mertens matching, an integer counting budget \(1\le K=o(p/\log p)\) permits a worst-case normalized transient Robin discrepancy

\[
\boxed{\left(\frac12+o(1)\right)\frac{K\log p}{\sqrt p}.}
\tag{1}
\]

The upper bound covers infinite sources; finite, cardinality-preserving real-label transports already establish sharpness. The same sharp constant holds for distinct **integer** labels, even when every changed label lies below \(2p+o(p)\): finite exact Euler-factor splitting attains the bound with a net addition of \(K\) labels. A separate construction with infinitely many unit prime shifts has counting discrepancy returning to zero between tail shifts. Near equality forces a specific two-phase counting profile around \(2p\). Thus exact normalization does not improve the critical counting scale \(K\asymp\sqrt p/\log p\), although it constrains how the excursion and its compensation must be arranged. This is a synthetic-source theorem, not an estimate for the ordinary-prime Robin tail.

The finite-scale counting relaxation can also be solved exactly. Its
unique maximizing height is \(p+\sqrt{p(p-1)}\); the resulting explicit
bound improves (6) for every admissible discrete source. Exact attainment
at a fixed \(p\) is asserted only for the measurable counting relaxation,
not for the prime-deletion/integer-insertion source class.

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

### Exact finite-scale norm of the counting relaxation

Let \(\mathcal A_{p,K}\) be the measurable real functions on
\([p,\infty)\) with \(|A|\le K\) almost everywhere and
\(\int_p^\infty A\,d\mu=0\). Every counting discrepancy in (2)
belongs to this class. Define \(E_A(U)\) by the right side of (10).
For \(p\ge3\), set
\[
u_p=p+\sqrt{p(p-1)},\qquad
f(u_p)=\frac{f(p)}2,\qquad
\alpha=\exp(f(p)/2).
\tag{11a}
\]
The exact fixed-height relaxed norm is
\[
\frac1K\sup_{A\in\mathcal A_{p,K}}|E_A(U)|=N_p(U)
=\begin{cases}
f(p)-h(U)\log p,&p\le U\le u_p,\\[2mm]
f(U)+h(U)\log\!\dfrac{Up}{v(U)^2},&U>u_p,
\end{cases}
\quad
v(U)=\frac{\alpha U}{1+(\alpha-1)U}.
\tag{11b}
\]
In the second case, \(p<v(U)<U\) and
\(f(v(U))-f(U)=f(p)/2\). Thus
\[
\boxed{\sup_{U\ge p}|E_Q(U)|\le K C(p),\qquad
C(p)=f(p)\left(1-\frac{\log p}{2\log u_p}\right)
=\frac{f(p)}2\left(1+\frac{\log(u_p/p)}{\log u_p}\right).}
\tag{11c}
\]
This bound holds for every \(Q\in\mathcal C_{p,K}\), without an
asymptotic restriction on \(K\). It is the exact all-height norm over
\(\mathcal A_{p,K}\), and
\[
C(p)=\frac1{2p}+\frac{\log2}{2p\log p}
 +O\!\left(\frac1{p(\log p)^2}+\frac1{p^2}\right).
\tag{11d}
\]

To prove (11b), write
\[
-E_A(U)=\int_p^\infty A(t)r_U(t)\,d\mu(t),\qquad
r_U(t)=\mathbf1_{[p,U]}(t)\,[1+h(U)(t-1)].
\tag{11e}
\]
The kernel is strictly increasing on \([p,U]\) and zero afterwards.
If \(U\le u_p\), the prefix has at most half of the total
\(\mu\)-mass \(f(p)\). Taking \(A=K\) on the prefix and
\(A=-K[f(p)-f(U)]/f(U)\) on the tail is admissible and maximizes
the integral, since the kernel is nonnegative. Its value divided by
\(K\) is \(f(p)-f(U)+h(U)\log(U/p)
=f(p)-h(U)\log p\).

If \(U>u_p\), the interval \([v(U),U]\) has exactly half of
the total \(\mu\)-mass. Set \(\lambda=1+h(U)(v(U)-1)\).
The zero-moment condition gives the dual bound
\[
\int A r_U\,d\mu=\int A(r_U-\lambda)\,d\mu
\le K\int|r_U-\lambda|\,d\mu.
\tag{11f}
\]
Equality holds for \(A=K\) on \((v(U),U)\) and \(A=-K\)
on its complement. Integrating this profile gives the second branch
of (11b). Negating any profile handles the absolute value. This is
the classical weighted-median/one-moment duality; no general duality
theorem is needed beyond the displayed bound and its attaining profile.

The first branch is strictly increasing because \(h'<0\). To check
the second branch globally, put \(b=\alpha-1\) and
\(D(U)=\log(Up/v(U)^2)\). For \(U\ge u_p=\alpha/b\),
\[
D(U)\ge D(u_p)=\log(u_p/p)>0,\qquad
0<D'(U)=\frac{bU-1}{U(1+bU)}<\frac1U.
\]
Consequently
\[
N_p'(U)=f'(U)+h'(U)D(U)+h(U)D'(U)
< -\frac1{U(U-1)}+\frac{f(U)}{U\log U}<0,
\tag{11g}
\]
using \(f(U)\le1/(U-1)\) and \(U\ge u_p>e\).
The two branches agree at \(u_p\), proving its unique maximality
and (11c). At that height the relaxed maximizers are, up to overall
sign and null sets, \(A=K\) before \(u_p\) and \(A=-K\)
afterwards. The expansion (11d) follows from
\(u_p=2p-1/2+O(p^{-1})\) and \(f(p)=p^{-1}+O(p^{-2})\).

The relaxation discards prime locations, integer-valued counting jumps
and source realizability. Its exact maximizing profile is not an
admissible source agreeing through \(p\): local finiteness and prefix
agreement force the actual discrepancy to vanish on an interval
immediately to the right of \(p\). Thus (11c) is a sharp **relaxed**
norm and a universal source upper bound; it does not identify the
exact discrete-source supremum at a fixed \(p\). The constructions
below establish only the stated leading asymptotic source sharpness.

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
\(T\ge p\). The witnesses in this subsection have infinitely many
changed labels. The following subsection gives finite integer-label
witnesses with a different terminal counting profile.

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

### Finite integer splitting also attains the sharp norm

Let \(\mathcal C^{\mathbb Z,\mathrm{fin}}_{p,K}\) restrict
\(\mathcal C^{\mathbb Z}_{p,K}\) to sources whose symmetric difference
with the ordinary primes is finite. Under (12),
\[
\boxed{\sup_{Q\in\mathcal C^{\mathbb Z,\mathrm{fin}}_{p,K}}
\sup_{U\ge p}|E_Q(U)|
=\left(\frac12+o(1)\right)\frac Kp.}
\tag{18i}
\]
For any prescribed \(T\ge p\) with \(T/p\to1\), witnesses can agree
with the primes through \(T\), have every alteration in
\((T,2p+o(p)]\), and have exactly \(K\) deletions and \(2K\)
insertions. Thus (18i) does **not** assert sharpness with equal finite
insertion and deletion counts.

Choose the first \(K\) primes \(r_i>T\) satisfying
\(r_i\equiv2\pmod3\). The classical fixed-modulus PNT gives, for
each fixed \(\epsilon>0\),
\[
\pi((1+\epsilon)p;3,2)-\pi((1+\epsilon/2)p;3,2)
\sim\frac{\epsilon p}{4\log p}.
\]
Eventually \(T<(1+\epsilon/2)p\) and this count exceeds \(K\).
Consequently \(r_i=p+o(p)\) uniformly in \(i\). No PNT on a
shrinking interval or growing modulus is invoked.

Replace each \(r_i\) by the two labels \(2r_i-1,2r_i\). The identity
\[
\boxed{\frac{2r-1}{2r-2}\frac{2r}{2r-1}=\frac r{r-1}}
\tag{18j}
\]
is exact. For \(r\equiv2\pmod3\), \(r\ge5\), the first inserted
label is divisible by three and the second is even; both are
composite. They therefore cannot duplicate a surviving ordinary
prime. Different primes give disjoint pairs, so the resulting source
has distinct integer labels and no multiplicities. Equation (18j)
gives \(\Gamma(Q)=\gamma\) by a finite rational-product equality.

Each individual replacement contributes the counting function
\[
A_r(t)=
\begin{cases}
0,&t<r,\\
-1,&r\le t<2r-1,\\
0,&2r-1\le t<2r,\\
1,&t\ge2r.
\end{cases}
\tag{18k}
\]
Hence \(A=\sum_i A_{r_i}\) satisfies \(|A|\le K\) everywhere,
including inside both packets. After all modifications, \(A=K\),
not zero. Finite support of the *source difference* does not require
finite support of its cumulative counting function.

Put \(U_p=2\min_i r_i-3/2=2p+o(p)\). For all sufficiently large
\(p\), every deletion precedes \(U_p\) and every insertion follows
it. Direct integration of the deleted atoms gives
\[
\begin{aligned}
E_Q(U_p)
&=\sum_{i=1}^K\bigl[f(r_i)-h(U_p)\log r_i\bigr]\\
&=\left(\frac12+o(1)\right)\frac Kp>0.
\end{aligned}
\tag{18l}
\]
Indeed \(f(r_i)=(1+o(1))/p\) uniformly, whereas
\(h(U_p)\log r_i=(1+o(1))/(2p)\). The upper bound (6) proves
(18i). There is no compensation limit or second limiting parameter.

For \(U\ge2\max_i r_i\), the finite Euler-log difference is zero
and the logarithmic mass difference is \(\sum_i\log(4r_i-2)\).
The exact tail is therefore
\[
E_Q(U)=h(U)\sum_{i=1}^K\log(4r_i-2)\longrightarrow0.
\tag{18m}
\]
This checks that the nonzero terminal count is compatible with exact
Mertens normalization and zero full-tail discrepancy. At leading
order, the profile is \(-K\) between \(p\) and \(2p\), then \(+K\)
after \(2p\); it realizes the two-phase geometry in (21).

The same identity makes the universal subdyadic support restriction
in RE-257 sharp: already one prime \(r\equiv2\pmod3\) has a
nontrivial exact integer replacement supported on \([r,2r]\).
Such primes are arbitrarily large. Thus a universal rigidity theorem
on open intervals of multiplicative width strictly below two cannot
extend to any larger fixed width. This is not a classification of
each particular interval, nor a cardinality-preserving example.

## 3. The sharp threshold and near-extremizer geometry

Multiplying (13) by \(\sqrt pL\) proves (1). Within (12), the worst-case normalized discrepancy tends to zero **if and only if**
\[
K\log p/\sqrt p\longrightarrow0.
\tag{19}
\]
At \(K\sim a\sqrt p/L\), its supremum tends to \(a/2\). By (18a) and (18i), both conclusions hold also for the distinct-integer-label subclass and its finite-modification subclass. This sharpens the qualitative distinction between the stable prime-cell/unit-shift classes and the larger relocation classes: exact Mertens matching alone does not remove the counting threshold.

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

The line-local delta is the **sharp Mertens-conditioned Robin norm over admissible discrete sources**, including its finite real- and integer-label realizations and necessary near-extremizer geometry. RE-154 establishes the relocation scale but not this optimal norm under exact normalization. RE-169 supplies the compensation identity but not a counting-budget extremum. RE-258 and RE-260 establish narrower positional stability and injectivity boundaries; their hypotheses do not classify growing counting budgets. RE-173 permits infinite prime multiplicities and RE-256 constructs local real-label compensation, without the optimal all-height counting-norm statement. The literature comparison does not establish a globally new discrepancy theorem.

The finite-scale optimization (11b) is a specialization of classical
best constant approximation in \(L^1\), whose minimizers are weighted
medians. See L. G. Brown and B. J. Lucier,
[*Best approximations in L1 are near best in Lp, p < 1*,
Proceedings of the AMS **120** (1994), 97--100](https://www.math.purdue.edu/~lucier/pde-papers/nearbest.pdf),
opening page. The additional calculation here is the exact Robin
kernel norm and its maximizing height, including the finite-scale
correction in (11d); neither median duality nor a new arithmetic
exclusion theorem is claimed.

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

Finite splitting (18j) is elementary telescoping, already identified
as an integer-label injectivity obstruction in RE-172. The additional
prime-distribution input is the classical fixed-modulus PNT; see
Kiran S. Kedlaya, [*Notes on analytic number theory*, Section 4.4,
Theorem 4.12](https://kskedlaya.org/ant/chap-primes-in-ap.html).
Only the fixed progression \(2\pmod3\) is used. The contribution
of (18i)--(18m) is the simultaneous realization of the **sharp Robin
norm, distinct integer labels, finite support near the doubling
scale, and exact Mertens matching**. Neither telescoping nor the PNT
is a new theorem. The construction isolates the price as a nonzero
terminal counting offset, rather than unbounded modification support.
The earlier infinite construction remains relevant because its
counting discrepancy returns to zero between shifted pairs. No
claim of finite cardinality-preserving integer sharpness follows.

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

For finite splitting, 18 packet checks used
\(p\in\{1009,10007,100003\}\),
\(T\in\{p,p+\lfloor p^{3/5}\rfloor\}\), and
\(K\in\{1,\lfloor\sqrt p/L\rfloor,\lfloor p/L^2\rfloor\}\).
Exact rational arithmetic verified product equality, and integer
checks verified compositeness, distinctness, prefix agreement,
\(|A|\le K\), and final count \(A=K\). At 75 decimal digits,
192 cutoff checks, including jump locations, agreed between the
atom and counting formulas within \(3\cdot10^{-76}\), satisfied
(5), and checked (18m) beyond the last insertion. These decimal
checks are supplementary and are not interval certificates; the
finite rational identity and the asymptotic proof above are decisive.

For (11b), a supplementary floating-point optimization used
\(p\in\{3,11,101,1009\}\), ten cutoffs per \(p\) (including
\(u_p\), both sides of it, and \(100p\)), and meshes of 127, 511 and
2047 equal cells in \(x=f(t)/f(p)\), split additionally at
\(x=f(U)/f(p)\). Integrating the kernel on each cell and sorting
cell scores solves the resulting box-constrained, zero-mean linear
program. Across the 120 checks, its value never exceeded (11b) by
more than \(1.4\cdot10^{-15}f(p)\); the largest mesh deficit was
\(4.1\cdot10^{-6}f(p)\). At \(u_p\), agreement was within
\(1.4\cdot10^{-15}f(p)\). A further 8000 height comparisons agreed
with the proved monotonicity on the two branches. These are numerical
sign and optimization checks, not interval certificates; (11e)--(11g)
give the exact proof.

Important boundaries:

- The exact finite-scale constant (11c) is optimal over measurable zero-Mertens-moment profiles. Discrete-source asymptotic sharpness does not prove attainment of that finite-scale constant or its second-order term by ordinary-prime deletions and integer insertions.
- Finite cardinality-preserving sharpness witnesses use real labels. Finite distinct-integer witnesses in (18i) add \(K\) net labels; the alternative integer construction uses infinitely many unit shifts. None satisfies the original-prime-cell restriction throughout. Finite integer prime-cell rigidity and finite ordinary-prime Euler-factor rigidity remain intact. Finite cardinality-preserving integer sharpness is not asserted.
- Infinite modifications are allowed in the upper bound because bounded \(A\) proves the needed convergence. No finite-support valuation argument is passed to an infinite product.
- Exact Mertens matching is essential for the smaller complementary-mass bound in (5); without it the zero integral in (8) is absent.
- The longer frozen prefix may be any \(T=p+o(p)\), including one beyond the known first-annulus localization scale. This is positional source agreement, not a new actual CA state or an altered ordinary divisor sum.
- At the critical budget \(K=O(\sqrt p/L)\), (9) gives a discrepancy from ordinary Chebyshev data of \(O(K\log t)\), smaller than every fixed KV relative envelope for \(t\ge p\) as \(p\to\infty\). This is fidelity of the *difference* and does not upgrade the KV constant available for ordinary primes.
- A zero full-tail difference does not force each truncated integral to vanish. Conversely the supremum over synthetic sources is not a lower bound for an actual ordinary-prime excursion.

**Research consequence:** an independent argument forcing counting fidelity \(o(\sqrt p/\log p)\) would suffice for uniform Robin stability even with infinitely many changes. At the critical scale, exact Mertens fidelity and a longer \(p+o(p)\) frozen prefix still allow a finite-height, source-realized excursion, even with distinct integer labels and finitely many changes confined below \(2p+o(p)\). Finite support alone therefore does not restore stability; the finite construction has a nonzero terminal counting offset. The composite integer labels remain synthetic Euler atoms; their factors \(q/(q-1)\) are not the ordinary divisor-sum contributions of those composite integers. The arithmetic task remains to justify stronger fidelity or a signed restriction for actual CA-selected primes; no Robin inequality or RH conclusion follows here.
