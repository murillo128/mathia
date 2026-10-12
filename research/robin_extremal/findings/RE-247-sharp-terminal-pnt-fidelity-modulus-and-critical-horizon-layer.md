# RE-247 — Sharp terminal PNT-fidelity modulus and critical horizon layer

**Status:** EXACT-DERIVED + QUANTITATIVE-PNT-FIDELITY + SHARP-MATCHED-SOURCE-MODULUS + MOVING-HORIZON-BOUNDARY + PRIOR-ART-BOUNDED.

**Parent findings:** RE-153, RE-155, RE-238, RE-246.

RE-238 gives an upper bound on the effect of a terminal source modification under a quantitative Chebyshev remainder. RE-246 constructs an order-one modification at the leading-order critical Korobov–Vinogradov exponent. The missing quantitative question is whether that upper bound has the *correct size* for each allowed terminal horizon, including horizons tuned through the critical second-order layer. It does: within the stated generalized-prime comparison class, the worst terminal ambiguity is comparable on both sides to one explicit scale. This gives an if-and-only-if source-information criterion, not merely a sufficient strict exponent test.

## 1. Sharp modulus theorem

Fix \(b>0\) and \(0<\alpha<3/4\). Let \(p\to\infty\), let \(U=U(p)\) satisfy \(U/p\to\infty\), and set
\[
T=e^{-2}U,\qquad
V(t)=\frac{(\log t)^{3/5}}{(\log\log t)^{1/5}},\qquad
E_b(t)=t e^{-bV(t)}.
\tag{1}
\]
These conditions ensure \(T>p+p^\alpha\) for all large \(p\).

For every strictly increasing discrete real-label generalized-prime source \(Q\), put
\[
\vartheta_Q(t)=\sum_{\substack{q\in Q\\q\le t}}\log q,\qquad
h(t)=\frac{-\log(1-t^{-1})}{\log t},
\tag{2}
\]
and define the *truncated Robin-kernel source functional*
\[
Z_{p,U}=\sqrt p\log p\int_{p+p^\alpha}^{U}
\sqrt t\,(-h'(t))\,dt=2+o(1),
\quad
\mathcal A_{p,U}(Q)=
\frac{\sqrt p\log p}{Z_{p,U}}
\int_{p+p^\alpha}^{U}(t-\vartheta_Q(t))(-h'(t))\,dt.
\tag{3}
\]
The normalization is the same as in RE-153. Its limit follows from that finding's integrable Pareto kernel and only requires \(U/p\to\infty\). At \(U=U_A(p)\), (3) is precisely the previous canonical terminal observable; at other \(U\), it is a deliberately varied truncation, **not** a new Robin counterexample criterion.

Fix a sufficiently large \(t_0=t_0(b)\) once and for all. Let \(\mathscr P_{p,b,U}\) be the class of source pairs \(Q_1,Q_2\) such that both systems have strictly increasing labels \(>1\), tend to infinity, agree on \((1,T]\), and satisfy the *common, unit-constant* bound
\[
|\vartheta_{Q_i}(t)-t|\le E_b(t)
\quad(t\ge t_0,\ i=1,2).
\tag{4}
\]
The same \(t_0\) and the same envelope constant apply to every pair and every \(p\). Define
\[
\Delta_{p,b,U}
=\sup_{(Q_1,Q_2)\in\mathscr P_{p,b,U}}
|\mathcal A_{p,U}(Q_1)-\mathcal A_{p,U}(Q_2)|,
\quad
B_{p,b,U}:=\frac{\sqrt p\log p}{\log U}\,e^{-bV(U)}.
\tag{5}
\]

**Theorem.** There is a universal fixed \(c_0>0\) such that, for every fixed \(b>0\) and every admissible \(U(p)\),
\[
\boxed{(c_0+o(1))B_{p,b,U}
\ \le\ \Delta_{p,b,U}\
\le (2+o(1))B_{p,b,U}.}
\tag{6}
\]
In particular,
\[
\boxed{\Delta_{p,b,U}\to0
\quad\Longleftrightarrow\quad
bV(U)-\tfrac12\log p+
\log\frac{\log U}{\log p}\longrightarrow+\infty.}
\tag{7}
\]
If the expression on the right fails to tend to \(+\infty\), admissible matched sources retain a nonvanishing terminal discrepancy along a subsequence. If it tends to \(-\infty\), the maximal discrepancy diverges. The claim is a sharp *order of magnitude*, not an assertion that the constants in (6) are best possible.

## 2. Upper bound: the exact terminal kernel norm

For sources agreeing below \(T\), RE-238's subtraction identity gives
\[
\mathcal A_{p,U}(Q_1)-\mathcal A_{p,U}(Q_2)
=\frac{\sqrt p\log p}{Z_{p,U}}
\int_T^U
(\vartheta_{Q_2}(t)-\vartheta_{Q_1}(t))(-h'(t))\,dt.
\tag{8}
\]
The assumption (4) bounds the absolute integrand by \(2E_b(t)(-h'(t))\).

The derivative identity
\[
-h'(t)=\frac{1}{t(t-1)\log t}
+\frac{-\log(1-t^{-1})}{t(\log t)^2}
=\frac{1+o(1)}{t^2\log t}
\tag{9}
\]
holds uniformly on \([T,U]\). With \(v=\log U\), the derivative of
\(v^{3/5}/(\log v)^{1/5}\) is
\[
\frac{v^{3/5}}{(\log v)^{1/5}}
\frac1v\left(\frac35-\frac1{5\log v}\right)=o(1).
\tag{10}
\]
Thus \(V(Ue^{-w})=V(U)+o(1)\), uniformly for \(0\le w\le2\), and
\[
\int_T^U E_b(t)(-h'(t))\,dt
=(1+o(1))e^{-bV(U)}
\int_T^U\frac{dt}{t\log t}
=\frac{2+o(1)}{\log U}e^{-bV(U)}.
\tag{11}
\]
Combining (8)--(11) with \(Z_{p,U}\to2\) gives
\[
|\mathcal A_{p,U}(Q_1)-\mathcal A_{p,U}(Q_2)|
\le(2+o(1))B_{p,b,U}.
\tag{12}
\]
The asymptotic is uniform over all source pairs in (4); no unstated smoothness of their step functions is used.

## 3. Lower bound: one baseline and uniformly admissible opposite surgeries

The matching construction does not assume any unproved result about ordinary primes. Take one fixed source \(Q_*=\{q_j\}\), defined by \(q_1=2\) and
\[
q_{j+1}-\log q_{j+1}=q_j.
\tag{13}
\]
As in RE-246, its gaps satisfy \(q_{j+1}-q_j=\log q_{j+1}\), and
\(\vartheta_{Q_*}(t)=t+O(\log t)\). Hence for one fixed sufficiently large \(t_0(b)\),
\[
|\vartheta_{Q_*}(t)-t|\le \tfrac1{10}E_b(t)
\qquad(t\ge t_0).
\tag{14}
\]
Set \(c=e^{-3/2}\), \(d=e^{-1/2}\) and choose one small absolute \(\epsilon>0\), say \(\epsilon=10^{-4}\). For each \(p\) put
\[
m=\left\lfloor
\epsilon\frac{Ue^{-bV(U)}}{\log U}
\right\rfloor.
\tag{15}
\]
Because \(V(U)=o(\log U)\), we have \(m\to\infty\) and
\(m\log U=(\epsilon+o(1))E_b(U)=o(U)\).

The baseline gaps near \(cU,dU\) are at most \(2\log U\). Thus there are at least \(m\) baseline labels in each of the intervals
\[
(cU,cU+4m\log U],\qquad(dU,dU+4m\log U],
\tag{16}
\]
and the intervals have width \(o(U)\). Construct \(Q_p^+\) by deleting \(m\) labels \(r_i=cU+o(U)\) from the first interval and inserting \(m\) distinct real labels \(s_i=dU+O(1)\) that avoid the baseline. Construct \(Q_p^-\) by the opposite relocation: delete \(m\) labels near \(dU\) and insert \(m\) fresh labels near \(cU\). Each modification has equal deletion and insertion counts, and every changed label lies strictly between \(T\) and \(U\).

For either modified source,
\[
\vartheta_{Q_p^\pm}(t)=\vartheta_{Q_*}(t)\quad(t\le T),
\qquad
|\vartheta_{Q_p^\pm}(t)-\vartheta_{Q_*}(t)|
\le2m\log U\quad(t\ge T).
\tag{17}
\]
Since \(E_b(t)\) is eventually increasing and
\(E_b(T)/E_b(U)=e^{-2}+o(1)\), the right side of (17) is less than
\(\tfrac1{10}E_b(t)\) for every \(t\ge T\) if \(\epsilon=10^{-4}\) and \(p\) is large. Together with (14), all three sources \(Q_*,Q_p^+,Q_p^-\) obey the very same unit-constant bound (4), with \(t_0\) independent of \(p\).

Deleting one label \(r\in(T,U)\) increases (3) by
\[
\frac{\sqrt p\log p}{Z_{p,U}}
\log r\,[h(r)-h(U)],
\tag{18}
\]
and inserting a label decreases it by the analogous expression. The *complete* endpoint-subtracted influence obeys, for \(r=cU+o(U)\) and \(s=dU+o(U)\),
\[
\log r\,[h(r)-h(U)]-\log s\,[h(s)-h(U)]
=\frac{c^{-1}-d^{-1}+o(1)}{U}.
\tag{19}
\]
This follows from
\(\log q\,h(q)=-\log(1-q^{-1})=q^{-1}+O(q^{-2})\)
and \((\log s-\log r)h(U)=O(1/(U\log U))\). It retains the upper-endpoint term.

Summing (19), using (15) and \(Z_{p,U}=2+o(1)\), gives
\[
\mathcal A_{p,U}(Q_p^\pm)-\mathcal A_{p,U}(Q_*)
=\pm\left(\frac{\epsilon}{2}
(c^{-1}-d^{-1})+o(1)\right)B_{p,b,U}.
\tag{20}
\]
Consequently the admissible pair \((Q_p^+,Q_p^-)\) satisfies
\[
|\mathcal A_{p,U}(Q_p^+)-\mathcal A_{p,U}(Q_p^-)|
=\left(\epsilon(c^{-1}-d^{-1})+o(1)\right)B_{p,b,U},
\tag{21}
\]
proving (6) with any \(c_0<\epsilon(c^{-1}-d^{-1})\).

The unit-constant restriction is important: the lower bound is not obtained by allowing a hidden \(p\)-dependent PNT constant. The construction also uses a single baseline for all \(p\), and the two changes are confined to a fixed terminal multiplicative shell.

## 4. The exact second-order inversion boundary

Write \(x=\log p\), \(v=\log U\). Formula (5) is exactly
\[
\log B_{p,b,U}
=\frac x2+\log x-\log v
-b\frac{v^{3/5}}{(\log v)^{1/5}}.
\tag{22}
\]
For sufficiently large \(x\), there is a unique \(v_*(x)>x\) solving
\[
\boxed{
b\frac{v_*^{3/5}}{(\log v_*)^{1/5}}
+\log\frac{v_*}{x}=\frac x2.
}
\tag{23}
\]
The left side is strictly increasing for large \(v\), and its value lies below \(x/2\) at \(v=x\) and above \(x/2\) at \(v=x^2\). Moreover,
\[
v_*(x)\sim A_b x^{5/3}(\log x)^{1/3},
\qquad
A_b=\left(\frac1{2b}\right)^{5/3}
\left(\frac53\right)^{1/3}.
\tag{24}
\]
At \(v=v_*\), the ambiguity is of constant order. The critical layer has a definite *log-horizon width*. For every fixed real \(s\), if
\[
v=v_*(x)+s\frac{v_*(x)}x
+o\!\left(\frac{v_*(x)}x\right),
\tag{25}
\]
then differentiation of (22)--(23) gives
\[
\frac{d}{dv}\left[
b\frac{v^{3/5}}{(\log v)^{1/5}}+
\log\frac vx
\right]_{v=v_*}
=\left(\frac3{10}+o(1)\right)\frac{x}{v_*}.
\tag{26}
\]
The second derivative contributes \(o(1)\) over (25), and hence
\[
\boxed{B_{p,b,U}\longrightarrow e^{-3s/10}.}
\tag{27}
\]
Thus the **maximal source ambiguity remains of positive constant order throughout every fixed-width rescaled transition layer**, whereas shifts much farther to the right drive it to zero. This is not an assertion of an exact limit for \(\Delta_{p,b,U}\); only its two-sided comparability to (27) is proved.

Two useful contrasts fix the interpretation.

* At the *exact* PNT inversion horizon \(bV(U)=x/2\), one has \(B=x/v\to0\). Terminal rigidity already holds there, despite leading-order equality of the powers of \(p\).
* At the usual canonical horizon \(U_A(p)=\exp(Ax^{5/3}(\log x)^{1/3})\) with \(b\kappa_A=1/2\), RE-238's second-order expansion gives
\[
\log B=
\frac{x(\log\log x+3\log A)}{50\log x}
+O\!\left(\frac{x(\log\log x)^2}{(\log x)^2}\right)
-\log\frac{\log U_A(p)}x
\longrightarrow+\infty.
\tag{28}
\]
It lies well on the non-rigid side of the *true* critical layer. RE-246's equality-case surgeries are therefore instances of the general sharp modulus, not paradoxes at an exactly balanced horizon.

## 5. Prior-art boundary, stress tests, and consequence

The positive-kernel upper estimate and matched-source subtraction identity originate in RE-238; the discrete baseline, equal-cardinality relocation and exact endpoint influence originate in RE-246 (and its RE-155 ancestor). What is newly established here is their **uniform two-sided modulus at arbitrary terminal horizons**, including an envelope constant fixed across the entire source family, the necessity-and-sufficiency criterion (7), and the resolved log-horizon transition layer (23)--(27). This is a quantitative completion of a local information-boundary question, not a new prime distribution theorem.

The quantitative PNT context is the Korobov–Vinogradov remainder already anchored through Bellotti in SOURCES.md. Finite perturbations of Beurling generalized-prime systems have prior-art precedents already acknowledged in RE-246; no novel generalized-prime existence theorem is claimed. All essential statements here follow by direct calculus and the explicit baseline/relocation construction. No additional external theorem is needed, and SOURCES.md is unchanged.

The falsification checks are: (i) use the true derivative (9), not a kernel lacking its logarithm; (ii) keep the full endpoint subtraction in (19); (iii) use the same \(t_0\) and envelope coefficient for all sources; (iv) distinguish the source-pair supremum from what occurs for the *single ordinary-prime sequence*; (v) keep \(U/p\to\infty\) so the normalization in (3) remains \(2+o(1)\); and (vi) do not read the moving truncation (25) as an alternative established Robin reduction.

The mathematical implication is exact but limited: **quantitative PNT fidelity alone fixes the terminal Robin-kernel observable precisely when \(B_{p,b,U}\to0\)** in this generalized-prime source class. It does not bound the source-specific middle annulus, correlate ordinary-prime CA selectors with the Robin height, prove an inequality for actual extremal integers, or resolve RH.
