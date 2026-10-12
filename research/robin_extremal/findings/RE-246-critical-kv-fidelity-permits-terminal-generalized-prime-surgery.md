# RE-246 — Critical quantitative-PNT fidelity permits terminal generalized-prime surgery

**Status:** \`EXACT-DERIVED + CRITICAL-PNT-FIDELITY + MATCHED-GENERALIZED-PRIME-SOURCE + TERMINAL-SURGERY + SHARP-THRESHOLD-OBSTRUCTION + PRIOR-ART-BOUNDED\`.

**Parent findings:** RE-153, RE-155, RE-238.

RE-238 proves terminal-source rigidity under the quantitative Chebyshev bound
\[
|\vartheta_Q(t)-t|\le C t e^{-bV(t)},\qquad
V(t)=\frac{(\log t)^{3/5}}{(\log\log t)^{1/5}},
\]
when \(b\kappa_A>1/2\), where \(\kappa_A=A^{3/5}(3/5)^{1/5}\) is associated with the canonical Robin horizon \(U_A(p)\). It explicitly leaves equality open. The equality is **non-rigid** in the matched generalized-prime source class: even a *uniform-in-source* quantitative PNT bound with precisely \(b\kappa_A=1/2\) permits equal-cardinality terminal relocations that move the normalized Robin source observable by an arbitrary fixed amount.

This is a source-information obstruction, not a Robin counterexample. In particular it does not assert that ordinary primes themselves undergo a relocation.

## 1. Precise critical countermodel

Fix \(0<\alpha<3/4\), \(A>0\), \(b>0\) satisfying
\[
b\kappa_A=\frac12,\qquad
U=U_A(p):=\exp\!\left(A(\log p)^{5/3}(\log\log p)^{1/3}\right),
\qquad T=Ue^{-2}.
\tag{1}
\]
Let \(p\to\infty\) (in particular, one may use any unbounded sequence of eligible self-tangent CA frontier primes). Retain the deterministic kernel and normalization from RE-153:
\[
h(t)=\frac{-\log(1-t^{-1})}{\log t},\qquad Z_p=2+o(1),
\]
\[
\mathcal A_p(Q)=
\frac{\sqrt p\log p}{Z_p}
\int_{p+p^\alpha}^{U}(t-\vartheta_Q(t))(-h'(t))\,dt,
\qquad
\vartheta_Q(t)=\sum_{\substack{q\in Q\\q\le t}}\log q.
\tag{2}
\]
All \(Q\) below are strictly increasing, discrete real-label generalized-prime systems with \(q>1\), tending to infinity. The sum counts labels, not ordinary primality.

**Theorem (non-rigidity at equality).** Fix \(a>0\), \(c=e^{-3/2}\), and \(d=e^{-1/2}\). There is one fixed source \(Q_*\), independent of \(p\), and for every sufficiently large \(p\) two sources \(Q_p^+\), \(Q_p^-\), each obtained from \(Q_*\) by exactly
\[
m_p=\left\lfloor\frac{aU}{\sqrt p\log p}\right\rfloor
\tag{3}
\]
deletions and the same number of insertions, such that:

1. Each changed label lies in \((T,U)\), hence \(Q_p^\pm\cap[2,T]=Q_*\cap[2,T]\).
2. There are constants \(C,t_0\), independent of \(p\) and of the choice of source, for which **all three systems** obey
\[
|\vartheta_Q(t)-t|\le C\,t e^{-bV(t)}
\quad(t\ge t_0),\qquad Q\in\{Q_*,Q_p^+,Q_p^-\}.
\tag{4}
\]
3. The exact normalized Robin source coordinate has the nonzero limits
\[
\boxed{\lim_{p\to\infty}
\bigl(\mathcal A_p(Q_p^\pm)-\mathcal A_p(Q_*)\bigr)
=\pm\frac a2\left(\frac1c-\frac1d\right).}
\tag{5}
\]

Since \(a\) is arbitrary, the same quantitative PNT hypothesis plus exact agreement through the fixed terminal cutoff \(T\) does not determine \(\mathcal A_p\) even up to an \(o(1)\) error. The conclusion requires the exact **equality** \(b\kappa_A=1/2\); it does not contradict RE-238's strict rigidity.

## 2. A fixed baseline with a stronger-than-required PNT remainder

It is useful to avoid any unproved prime-distribution input by constructing \(Q_*\) explicitly. Set \(q_1=2\) and, for \(j\ge1\), take \(q_{j+1}>q_j\) to be the unique solution of
\[
q_{j+1}-\log q_{j+1}=q_j.
\tag{6}
\]
Existence and uniqueness follow because \(t-\log t\) is strictly increasing for \(t>1\). Thus \(q_{j+1}-q_j=\log q_{j+1}>0\), the sequence tends to infinity, and every sufficiently large fixed-proportion interval at height \(U\) contains \(\asymp U/\log U\) labels.

For \(C_0=2-\log2\), induction using (6) gives the exact identity
\[
\vartheta_{Q_*}(q_j)=\sum_{i=1}^j\log q_i=q_j-C_0.
\tag{7}
\]
Between two consecutive labels the Chebyshev step is constant, and their gap is \(\log q_{j+1}=O(\log t)\) at \(t\in[q_j,q_{j+1})\). Therefore
\[
\boxed{\vartheta_{Q_*}(t)=t+O(\log t).}
\tag{8}
\]
In particular \(Q_*\) satisfies (4) for every fixed \(b>0\), since \(t e^{-bV(t)}=t^{1-o(1)}\). This construction concerns the generalized-prime counting measure; it makes no claim about the integer-counting function of the associated Beurling semigroup.

## 3. Equal-cardinality terminal relocations and their exact influence

Take \(m=m_p\) from (3). Because
\[
\frac{m\log U}{U}
=O_a\!\left(\frac{\log U}{\sqrt p\log p}\right)=o(1),
\tag{9}
\]
the source (6) supplies at least \(m\) distinct labels inside either interval
\((cU,cU+4m\log U]\) or \((dU,dU+4m\log U]\): the gaps there are at most \(2\log U\) for all sufficiently large \(p\), and the interval widths are \(o(U)\).

For \(Q_p^+\), delete \(m\) baseline labels \(r_i=cU+o(U)\) from the first interval and insert \(m\) distinct real labels \(s_i=dU+O(1)\), avoiding all preexisting labels. For \(Q_p^-\), delete \(m\) labels \(s_i=dU+o(U)\) from the second interval and insert \(m\) new distinct labels \(r_i=cU+O(1)\). These are finite modifications of the same fixed system. As \(e^{-2}<c<d<1\), all changes lie in \((T,U)\) for large \(p\).

For a label \(q\) in the interior of the integration interval, deleting it increases (2) by
\[
\Lambda_p(q):=
\frac{\sqrt p\log p}{Z_p}
\log q\,[h(q)-h(U)],
\tag{10}
\]
while inserting it decreases (2) by the same quantity. This follows exactly from the step \(\log q\,\mathbf1_{[q,\infty)}\) in \(\vartheta_Q\) and \(\int_q^U(-h')=h(q)-h(U)\).

For \(r=cU+o(U)\), \(s=dU+o(U)\), uniformly in these relative neighborhoods,
\[
\begin{aligned}
\log r\,[h(r)-h(U)]-\log s\,[h(s)-h(U)]
&=-\log(1-r^{-1})+\log(1-s^{-1})\\
&\quad+(\log s-\log r)h(U)\\
&=\frac1U\left(\frac1c-\frac1d+o(1)\right).
\end{aligned}
\tag{11}
\]
The last term on the first line is \(O(1/(U\log U))\); importantly, the upper-endpoint subtraction has been retained rather than silently discarded. Summing (11) over exactly \(m\) relocations, using \(Z_p\to2\) and (3), proves (5), with opposite signs for the two directions.

## 4. Why the *same* quantitative PNT envelope survives at equality

The perturbation of the Chebyshev step function satisfies, for each choice of sign,
\[
\vartheta_{Q_p^\pm}(t)-\vartheta_{Q_*}(t)=0\quad(t\le T),
\qquad
\sup_{t\ge T}|\vartheta_{Q_p^\pm}(t)-\vartheta_{Q_*}(t)|
\le 2m\log U.
\tag{12}
\]
After \(U\), the residual is in fact \(O(m)\), since each relocated pair has logarithmic weight difference \(O(1)\), but the stronger cancellation is not needed for the envelope.

Put \(x=\log p\), \(y=\log\log p\). RE-238's second-order expansion, valid also at \(T=Ue^{-2}\), yields
\[
V(T)=\kappa_A x
\left[
1-\frac{\log y+3\log A}{25y}
+O_A\!\left(\frac{(\log y)^2}{y^2}\right)
\right].
\tag{13}
\]
Since \(b\kappa_A=1/2\), (3) and (13) imply
\[
\begin{aligned}
\log\frac{m\log U}{T e^{-bV(T)}}
&=-\frac{x(\log y+3\log A)}{50y}\\
&\quad+O_{A,a}\!\left(
\frac{x(\log y)^2}{y^2}+\log x+\log y
\right)
\longrightarrow-\infty.
\end{aligned}
\tag{14}
\]
Indeed \(x\log y/y\) dominates both \(x(\log y)^2/y^2\) and every fixed power of \(\log x\). Thus
\[
\boxed{m\log U=o\!\left(T e^{-bV(T)}\right).}
\tag{15}
\]
The function \(t\mapsto t e^{-bV(t)}\) is eventually increasing, because \(tV'(t)=o(1)\). Equations (8), (12), and (15) therefore establish (4) **simultaneously for all \(t\ge t_0\)** with a constant independent of \(p\), not just on the modified shell. This uniformity is the load-bearing improvement over the coarse \(o(U)\) control in RE-155.

The apparent first-order equality in \(b\kappa_A=1/2\) is misleading: the positive subpower correction in \(p^{1/2}e^{-bV(T)}\) creates enough room for the source excursion required by RE-238's necessary bound (11).

## 5. Ordinary-prime-anchored version when its PNT exponent is available

The synthetic baseline is not essential for some unconditional parameter choices. Let \(b_0>0\) be any constant for which the ordinary-prime quantitative PNT
\[
|\vartheta(t)-t|\ll t e^{-b_0V(t)}
\tag{16}
\]
is known, as in the source discipline of RE-015 and RE-238. Choose \(A\) large enough that \(b=1/(2\kappa_A)<b_0\). Use the **ordinary primes** as \(Q_*\) and select the \(m\) deletion primes in shrinking windows \((cU,cU+U/x]\), respectively \((dU,dU+U/x]\), where \(x=\log p\).

The quantitative PNT gives \(\asymp U/(x\log U)\) ordinary primes in each such window: its Chebyshev remainder there is \(o(U/x)\), and partial summation or the corresponding prime-count PNT transfers the estimate. There are enough primes because
\[
\frac{m}{U/(x\log U)}
\asymp_a\frac{\log U}{\sqrt p}\longrightarrow0.
\tag{17}
\]
All deleted labels still satisfy \(r_i/U\to c\) or \(s_i/U\to d\), and the new labels can again be distinct real numbers within \(O(1)\) of the opposite center. The same exact influence calculation proves (5). Since (15) also holds, both perturbed sources retain the *same critical exponent \(b\)* in their uniform Chebyshev remainder, with source-independent constants.

Here the sources agree with the **actual ordinary primes**, and hence with their source-generated CA event history, all the way to \(T=Ue^{-2}\). This is still a synthetic control beyond \(T\): inserting real labels does not produce a second ordinary-prime sequence or an ordinary counterexample to Robin's inequality.

## 6. Prior art, falsification checks, and research consequence

RE-155 already constructs equal-cardinality relocations in a fixed terminal fraction, computes their endpoint-subtracted influence, and shows only coarse PNT stability. RE-238 supplies the strict quantitative-PNT rigidity bound and correctly refuses to decide equality from a \(p^{o(1)}\) estimate. The new statement is the **critical compatibility proof** (13)--(15), together with an explicit all-height, common-constant Chebyshev source pair and the nonzero limit (5). Thus it closes precisely the equality question left open in RE-238; it is not a new estimate for ordinary-prime errors.

Finite modifications of Beurling generalized primes and agreement with ordinary primes below an arbitrarily prescribed cutoff have classical precedents (for example, Wen-Bin Zhang, *Normalization of Beurling generalized primes with Riemann Hypothesis*, Annales Univ. Sci. Budapest., Sect. Comput. **39** (2013), DOI 10.71352/ac.39.459). That literature is context, not an imported lemma or a claim that the specific critical Robin-source displacement is a new general Beurling theorem. No new external input beyond the quantitative PNT already anchored in SOURCES.md is load-bearing.

The decisive audit points are: the fixed baseline (6)--(8), enough labels for \(m=o(U/\log U)\), the *complete* endpoint term in (11), the sign and second-order size in (13)--(14), and a **uniform** common-constant bound on the whole ray in (4). A construction preserving only \(o(t)\), or merely bounding the changed shell, would not establish this result.

Consequently the strict side of RE-238 is an actual information threshold for matched generalized-prime sources: at \(b\kappa_A>1/2\) terminal source ambiguity vanishes, but at equality the stated quantitative PNT information alone still permits arbitrary fixed positive or negative shifts. This does **not** decide the ordinary-prime mixed-race sign, the selector/height correlation, the behavior of true Robin extrema, or RH. It identifies the missing source information at the critical terminal boundary rather than supplying it.