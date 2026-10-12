# RE-247 — Sharp terminal PNT-fidelity modulus and critical horizon layer

**Status:** EXACT-DERIVED + QUANTITATIVE-PNT-FIDELITY + SHARP-MATCHED-SOURCE-MODULUS + MOVING-HORIZON-BOUNDARY + PRIOR-ART-BOUNDED.

**Parent findings:** RE-153, RE-155, RE-238, RE-246.

RE-238 gives an upper bound on the effect of a terminal source modification under a quantitative Chebyshev remainder. RE-246 constructs an order-one modification at the leading-order critical Korobov–Vinogradov exponent. The missing quantitative question is whether that upper bound has the *correct size* for each allowed terminal horizon, including horizons tuned through the critical second-order layer. It does: within the stated generalized-prime comparison class, the worst terminal ambiguity has an exact asymptotic leading constant, and the upper bound is attained by explicit discrete sources obeying the same unit PNT envelope. This gives an if-and-only-if source-information criterion, not merely a sufficient strict exponent test.

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

**Theorem.** For every fixed \(b>0\) and every admissible \(U(p)\),
\[
\boxed{\Delta_{p,b,U}=(2+o(1))B_{p,b,U}.}
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
If the expression on the right fails to tend to \(+\infty\), admissible matched sources retain a nonvanishing terminal discrepancy along a subsequence. If it tends to \(-\infty\), the maximal discrepancy diverges. The constant (2) in (6) is optimal even though every source is a strictly increasing discrete system of labels and the PNT envelope constant is fixed at (1).

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

## 3. Saturating the upper bound with genuine discrete labels

The two-sided estimate of the earlier version of this finding can be made exact. The key is that a discrete positive source can shadow *either* permitted Chebyshev envelope throughout nearly the whole terminal shell: its nonnegative jumps are not a restriction at this very slowly varying error scale. This construction does not impose an unmentioned bound on the number of labels per short interval.

Use the fixed baseline \(Q_*=\{q_j\}\), defined by \(q_1=2\) and
\[
q_{j+1}-\log q_{j+1}=q_j.
\tag{13}
\]
As in RE-246, its gap is \(\log q_{j+1}\), and the exact identity
\(\vartheta_{Q_*}(q_j)=q_j-(2-\log2)\) yields
\[
|\vartheta_{Q_*}(t)-t|=O(\log t).
\tag{14}
\]
Choose once and for all \(t_0=t_0(b)\) so this error is at most \(E_b(t)/10\) for \(t\ge t_0\).

For each \(p,U\), let \(S=\vartheta_{Q_*}(T)\), and set
\[
\delta=(\log U)^{-1/2},\qquad
w=4E_b(T),\qquad
\rho(t)=\min\{(t-T)/w,1\}\quad(t\ge T),
\tag{15}
\]
\[
H_\pm(t)=S+(t-T)\pm(1-\delta)\rho(t)E_b(t).
\tag{16}
\]
Here \(w/T=4e^{-bV(T)}=o(1)\), so \(T+w<U\) for large \(p\). The envelope derivative satisfies
\[
E_b'(t)=e^{-bV(t)}(1-btV'(t))=o(1)
\quad(t\ge T),
\tag{17}
\]
uniformly, while \(\rho'(t)E_b(t)\le1/4+o(1)\) in the short ramp \(T<t<T+w\). Therefore \(H_\pm'(t)\ge1/2\) wherever differentiable, eventually, including slightly beyond \(U\). Both targets are strictly increasing. Moreover \(S-T=O(\log U)\) and \(\delta E_b(T)/\log U\to\infty\), so they stay a quantization margin inside the unit envelope:
\[
|H_\pm(t)-t|
\le(1-\delta)E_b(t)+O(\log U)
<E_b(t)-2\log U
\quad(T\le t\le U)
\tag{18}
\]
for all sufficiently large \(p\). The displayed \(2\log U\) may be replaced by any fixed multiple of \(\log U\).

Construct \(Q_p^\pm\) by retaining all labels of \(Q_*\) at or below \(T\), and then placing labels successively at the unique roots \(r>T\) of
\[
H_\pm(r)=M+\log r,
\tag{19}
\]
where \(M\) is the total logarithmic weight of the labels already placed; continue until the next root exceeds \(U\). Such a root is unique and lies above the previous label since \(H_\pm'(r)-1/r>0\). The spacing is \(O(\log U)\) across the shell. At a newly placed label \(r\), the new Chebyshev step equals \(H_\pm(r)\); between labels it lags the increasing target by at most the next label's weight. Thus
\[
0\le H_\pm(t)-\vartheta_{Q_p^\pm}(t)
=O(\log U)\qquad(T\le t\le U).
\tag{20}
\]
To complete the sources, include *exactly* the original baseline labels \(Q_*\cap(U,\infty)\) above \(U\). Hence the systems consist of distinct real labels \(>1\), tend to infinity, and coincide with \(Q_*\) below \(T\) and above \(U\); their finite changes inside the shell need not preserve the number of labels.

Equations (18)--(20) imply the unit-constant PNT envelope (4) throughout \([T,U]\). Below \(T\) it follows from (14). Above \(U\), using the identical baseline tails,
\[
\vartheta_{Q_p^\pm}(t)-t
=\bigl(\vartheta_{Q_p^\pm}(U)-\vartheta_{Q_*}(U)\bigr)
 +\bigl(\vartheta_{Q_*}(t)-t\bigr),
\quad
|\vartheta_{Q_p^\pm}(U)-\vartheta_{Q_*}(U)|
\le(1-\delta)E_b(U)+O(\log U).
\tag{21}
\]
Since \(E_b(t)\) and \(E_b(t)/\log t\) are eventually increasing and \(\delta E_b(U)\gg\log U\), the unit bound also holds for *every* \(t\ge U\), with the same fixed \(t_0(b)\) and no source-dependent constant. This is an explicit realization by discrete generalized-prime labels, not by signed or continuously weighted measures.

On the main portion \([T+w,U]\), (16) and (20) show
\[
\vartheta_{Q_p^+}(t)-\vartheta_{Q_p^-}(t)
=2(1-\delta)E_b(t)+O(\log U).
\]
The same formula on the initial ramp has its main term multiplied by \(\rho(t)\). Set
\[
W_{p,U}:=\int_T^U E_b(t)(-h'(t))\,dt
=(2+o(1))\frac{e^{-bV(U)}}{\log U}.
\]
The lost ramp contributes only
\[
\int_T^{T+w}E_b(t)(-h'(t))\,dt
=O\!\left(\frac{e^{-2bV(T)}}{\log T}\right)=o(W_{p,U}),
\]
and integrating the discretization error \(O(\log U)\) against \(-h'\) contributes \(O(1/U)=o(W_{p,U})\). Therefore the exact matched-source identity (8) and \(Z_{p,U}=2+o(1)\) give
\[
\left|\mathcal A_{p,U}(Q_p^+)-\mathcal A_{p,U}(Q_p^-)\right|
=\frac{\sqrt p\log p}{Z_{p,U}}(2+o(1))W_{p,U}
=(2+o(1))B_{p,b,U}.
\]
Together with (12), this proves the asymptotically **exact** modulus (6) for every admissible moving horizon. The one-sided envelope constraints can be saturated simultaneously throughout a fixed multiplicative shell, apart from an asymptotically negligible initial adjustment and the negligible discrete jump resolution.

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
At \(v=v_*\), the maximal ambiguity tends to \(2\). The critical layer has a definite *log-horizon width*. For every fixed real \(s\), if
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
\boxed{B_{p,b,U}\longrightarrow e^{-3s/10},
\qquad \Delta_{p,b,U}\longrightarrow 2e^{-3s/10}.}
\tag{27}
\]
Thus the **maximal source ambiguity has the exact limit \(2e^{-3s/10}\)** throughout every fixed-width rescaled transition layer, whereas shifts much farther to the right drive it to zero. This is a sharp statement about the specified matched generalized-prime class, not ordinary primes.

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

The positive-kernel upper estimate and matched-source subtraction identity originate in RE-238; the discrete baseline, equal-cardinality relocation and exact endpoint influence originate in RE-246 (and its RE-155 ancestor). The earlier version of this finding established two-sided comparability for arbitrary terminal horizons. The additional mathematical content is a **discrete positive-label saturation lemma** that attains the upper constant (2), thereby promoting that modulus and the rescaled critical-layer law to exact asymptotic equivalents. The construction uses the freedom to choose distinct generalized-prime labels within a fixed terminal shell; the two shadow sources are not asserted to preserve the shell's original cardinality. This is a sharp source-information bound, not a new prime distribution theorem.

The quantitative PNT context is the Korobov–Vinogradov remainder already anchored through Bellotti in SOURCES.md. Classical generalized-prime construction and Chebyshev-bound literature (for example, Diamond–Zhang, *Acta Arith.* 160 (2013), 259–275) concerns broader existence and generalized-integer count conditions, not this fixed-envelope Robin-kernel optimum. No novelty is claimed for constructing generalized-prime systems as such. The constant is established directly by the explicit monotone-target discretization above, not by invoking an external existence theorem; SOURCES.md requires no new load-bearing source.

The falsification checks are: (i) use the true derivative (9), not a kernel lacking its logarithm; (ii) keep the full upper-endpoint subtraction in (8); (iii) check that the monotone targets discretize to positive log-weight jumps with \(O(\log U)\) error and satisfy the unit envelope even *after* the shell; (iv) use the same \(t_0\) for all sources; (v) distinguish the source-pair supremum from the *single ordinary-prime sequence*; (vi) keep \(U/p\to\infty\) for \(Z_{p,U}\to2\); and (vii) do not read the moving truncation (25) as an alternative established Robin reduction.

The mathematical implication is exact but limited: **quantitative PNT fidelity alone fixes the terminal Robin-kernel observable precisely when \(B_{p,b,U}\to0\)** in this generalized-prime source class. It does not bound the source-specific middle annulus, correlate ordinary-prime CA selectors with the Robin height, prove an inequality for actual extremal integers, or resolve RH.
