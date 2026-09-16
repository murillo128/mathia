# RE-159 — fixed terminal moment matching has a sharp root-scale ambiguity hierarchy

**Status:** `EXACT-DERIVED + MATCHED-GENERALIZED-SOURCE-OBSTRUCTION + ALL-FIXED-ORDER-TERMINAL-MOMENT-HIERARCHY + PROUHET-SHARP-CONTROLS + SHRINKING-LAYER-THRESHOLD + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-153, RE-157, RE-158.

`RE-157` and `RE-158` expose the first two levels of the terminal source hierarchy. Equal inserted cardinality leaves a linear placement mode with ambiguity scale

\[
\epsilon_{\mathrm{PNT}}(p)
=
\frac{\log U_A(p)}{\sqrt p\log p},
\]

while additionally matching total inserted logarithmic/Chebyshev mass cancels that mode and leaves a quadratic spread mode with scale

\[
\epsilon_*(p)
=
\epsilon_{\mathrm{PNT}}(p)^{1/2}.
\]

These are the first two members of an exact fixed-order hierarchy. For every fixed integer \(r\ge1\), if two terminal insertion packets have equal cardinality and match their logarithmic-position power sums through order \(r-1\), then the first unconstrained Robin influence is the \(r\)-th placement moment. Its sharp vanishing-budget transition is

\[
\boxed{
\epsilon_r(p)
:=
\left(
\frac{\log U_A(p)}{\sqrt p\log p}
\right)^{1/r}.
}
\tag{1}
\]

More precisely, let

\[
U:=U_A(p)
=
\exp\!\left(
A(\log p)^{5/3}(\log\log p)^{1/3}
\right),
\qquad
L_\epsilon:=-\log(1-\epsilon),
\tag{2}
\]

and use logarithmic terminal position

\[
q=Ue^{-z},
\qquad
0\le z\le L_\epsilon.
\tag{3}
\]

Let two packets \(P_1,P_2\) each contain \(m\) distinct non-prime real labels in the terminal layer and write their positions as \(\{z_i\}_{i=1}^m\) and \(\{y_i\}_{i=1}^m\). Assume

\[
\sum_{i=1}^m z_i^k
=
\sum_{i=1}^m y_i^k
\qquad
(1\le k\le r-1).
\tag{4}
\]

Then, uniformly for \(\epsilon\to0\),

\[
\boxed{
\mathcal A_p(P\cup P_1)-\mathcal A_p(P\cup P_2)
=
-\frac{\sqrt p\log p}{Z_pU}
\left[
b_r(U)
\left(
\sum_i z_i^r-\sum_i y_i^r
\right)
+
O_r(m\epsilon^{r+1})
\right],
}
\tag{5}
\]

where \(P\) is the ordinary-prime source, \(Z_p=2+o(1)\), and

\[
b_r(U)=\frac1{r!}+O_r(U^{-1})
\qquad(r\ge2),
\tag{6}
\]

with the already known first-order coefficient \(b_1(U)=1+1/\log U+O(U^{-1})\).

Consequently

\[
\boxed{
\left|
\mathcal A_p(P\cup P_1)-\mathcal A_p(P\cup P_2)
\right|
\ll_r
m\epsilon^r\frac{\sqrt p\log p}{U}.
}
\tag{7}
\]

This upper bound has the correct order. Classical Prouhet--Thue--Morse equal-power partitions, affinely embedded into the terminal layer and repeated with distinct tiny translations, give equal-cardinality packets satisfying (4) but with

\[
\left|
\sum_i z_i^r-\sum_i y_i^r
\right|
\asymp_r m\epsilon^r.
\tag{8}
\]

Thus for a vanishing insertion intensity

\[
m_p
\sim
\delta_p\frac{U}{\log U},
\qquad
\delta_p\to0,
\tag{9}
\]

the attainable separation is

\[
\boxed{
\operatorname{Cap}^{(r)}_p(\epsilon,\delta)
\asymp_r
\delta\,\epsilon^r
\frac{\sqrt p\log p}{\log U}
=
\delta
\left(\frac{\epsilon}{\epsilon_r(p)}\right)^r.
}
\tag{10}
\]

Therefore order-one ambiguity survives with \(\delta_p\to0\) whenever \(\epsilon_p/\epsilon_r(p)\to\infty\), whereas every such fixed-\(r\) moment-matched insertion family using \(o(U/\log U)\) labels is \(o(1)\)-stable when \(\epsilon_p=O(\epsilon_r(p))\).

For the horizon (2),

\[
\boxed{
\epsilon_r(p)
=
A^{1/r}
p^{-1/(2r)}
(\log p)^{2/(3r)}
(\log\log p)^{1/(3r)}.
}
\tag{11}
\]

The cases \(r=1\) and \(r=2\) recover the scales of `RE-157` and `RE-158`. The new content is that **every additional fixed matched placement moment takes one more root of the same coarse-PNT scale**.

## 1. The exact Robin influence has a full terminal Taylor hierarchy

Retain the normalized source coordinate from `RE-153`,

\[
\mathcal A_p(Q)
=
\int_{J_p}
\frac{t-\vartheta_Q(t)}{\sqrt t}\,d\nu_p(t),
\tag{12}
\]

and the exact influence from `RE-154`--`RE-158` of inserting one label \(q<U\),

\[
\Lambda_p(q)
=
\frac{\sqrt p\log p}{Z_p}
\log q\,
\bigl(h(q)-h(U)\bigr),
\qquad
Z_p=2+o(1).
\tag{13}
\]

Adding \(q\) changes \(\mathcal A_p\) by \(-\Lambda_p(q)\).

Put

\[
a(t):=-\log(1-t^{-1}),
\qquad
q=Ue^{-z}.
\tag{14}
\]

`RE-158` used the exact identity

\[
\log q\,
\bigl(h(q)-h(U)\bigr)
=
a(Ue^{-z})-a(U)
+
\frac{a(U)}{\log U}z.
\tag{15}
\]

For \(z=o(1)\), the first term has the absolutely convergent expansion

\[
a(Ue^{-z})
=
\sum_{n\ge1}\frac{e^{nz}}{nU^n}.
\tag{16}
\]

Hence, for every fixed \(k\ge1\),

\[
\frac{d^k}{dz^k}
a(Ue^{-z})\Big|_{z=0}
=
\sum_{n\ge1}\frac{n^{k-1}}{U^n}.
\tag{17}
\]

For \(k\ge2\) define

\[
b_k(U)
:=
\frac{U}{k!}
\sum_{n\ge1}\frac{n^{k-1}}{U^n}.
\tag{18}
\]

The \(n=1\) term gives

\[
b_k(U)
=
\frac1{k!}+O_k(U^{-1}),
\tag{19}
\]

while for \(k=1\) the linear correction in (15) gives

\[
b_1(U)
=
\frac{U}{U-1}
+
\frac{Ua(U)}{\log U}
=
1+\frac1{\log U}+O(U^{-1}).
\tag{20}
\]

The \((r+1)\)-st derivative in (16) is \(O_r(U^{-1})\) uniformly for \(0\le z\le L_\epsilon=o(1)\). Taylor's theorem therefore yields

\[
\boxed{
\Lambda_p(Ue^{-z})
=
\frac{\sqrt p\log p}{Z_pU}
\left[
\sum_{k=1}^{r}b_k(U)z^k
+
O_r(z^{r+1})
\right].
}
\tag{21}
\]

This is an exact structural upgrade of the first- and second-order laws in `RE-157`--`RE-158`: there is no new analytic input at higher fixed order.

## 2. Matching lower placement moments cancels the hierarchy term by term

Let \(P_1,P_2\) be equal-cardinality terminal insertion packets and suppose (4) holds. Summing (21) over both packets cancels every term of order \(1,\ldots,r-1\), giving (5). Since all \(z_i,y_i\) lie in \([0,L_\epsilon]\) and \(L_\epsilon=\epsilon+O(\epsilon^2)\),

\[
\left|
\sum_i z_i^r-\sum_i y_i^r
\right|
\le 2mL_\epsilon^r
\ll m\epsilon^r.
\tag{22}
\]

Equations (5), (6), and (22) give (7).

The first matched moment has the familiar arithmetic interpretation. Equal cardinality gives equal terminal counting increment, and

\[
\sum_i z_i
=
m\log U-\sum_i\log q_i.
\tag{23}
\]

Thus matching the \(k=1\) placement moment is exactly matching total inserted Chebyshev/logarithmic mass, as in `RE-158`. The moments \(k\ge2\) are genuinely finer information about **where that equal logarithmic mass sits inside the terminal layer**. Endpoint values of \(\pi\) and \(\vartheta\) do not determine them.

If each packet uses \(m=o(U/\log U)\) labels, (7) becomes

\[
\left|
\Delta\mathcal A_p
\right|
=
o\!\left(
\epsilon^r\frac{\sqrt p\log p}{\log U}
\right)
=
o\!\left(
\left(\frac{\epsilon}{\epsilon_r(p)}\right)^r
\right).
\tag{24}
\]

Therefore

\[
\boxed{
\epsilon=O(\epsilon_r(p))
\quad\Longrightarrow\quad
\Delta\mathcal A_p=o(1)
}
\tag{25}
\]

for every vanishing-budget family satisfying the fixed moment constraints through order \(r-1\).

## 3. Prouhet packets make the \(r\)-th-order bound sharp

The upper bound would not identify a transition unless the first surviving moment could actually remain macroscopic after exact lower-moment matching. A classical Prouhet construction supplies precisely that control.

For fixed \(r\), put

\[
\sigma(j):=(-1)^{s_2(j)},
\qquad
0\le j<2^r,
\tag{26}
\]

where \(s_2(j)\) is the binary digit sum. The generating function factorizes as

\[
\boxed{
\sum_{j=0}^{2^r-1}\sigma(j)e^{jt}
=
\prod_{\ell=0}^{r-1}
\left(1-e^{2^\ell t}\right).
}
\tag{27}
\]

The right-hand side has a zero of exact order \(r\) at \(t=0\). Consequently

\[
\sum_j\sigma(j)j^k=0
\qquad
(0\le k<r),
\tag{28}
\]

while

\[
\boxed{
\sum_j\sigma(j)j^r
=
(-1)^r r!\,2^{r(r-1)/2}
\ne0.
}
\tag{29}
\]

Thus the even- and odd-binary-parity classes have equal cardinality and equal power sums through degree \(r-1\), but different \(r\)-th power sum.

Affine placement preserves this exact cancellation. Let \(L=L_\epsilon\), choose

\[
s:=\frac{L}{4\cdot2^r},
\tag{30}
\]

and, for one block, send \(j\) to

\[
z=\tau+sj,
\qquad
\frac L4<\tau<\frac L2.
\tag{31}
\]

All positions lie strictly inside \((0,L)\). By the binomial theorem, (28) implies exact equality of the two packet moments through degree \(r-1\), while the \(r\)-th difference is exactly

\[
s^r
(-1)^r r!\,2^{r(r-1)/2}.
\tag{32}
\]

Repeat the block \(N\) times with distinct generic translations \(\tau_b\) in the same interval. Translation changes no moment difference of degree at most \(r\) except through lower differences, which already vanish. The translations may be chosen so that all resulting real labels are distinct and non-prime. Each packet then has

\[
m=N\,2^{r-1}
\tag{33}
\]

labels and, for a constant \(c_r>0\) depending only on \(r\),

\[
\boxed{
\left|
\sum_i z_i^r-\sum_i y_i^r
\right|
=
c_r\,mL^r
=
(c_r+o(1))m\epsilon^r.
}
\tag{34}
\]

Substituting (34) into (5), using \(b_r(U)\to1/r!\) for \(r\ge2\) and \(Z_p\to2\), gives

\[
\boxed{
|\Delta\mathcal A_p|
\asymp_r
m\epsilon^r\frac{\sqrt p\log p}{U}.
}
\tag{35}
\]

For \(r=1\), the same conclusion is the two-point first-moment construction already classified in `RE-157`.

## 4. Vanishing PNT budget gives the sharp root-scale transition

Choose the packet cardinality to be a multiple of \(2^{r-1}\),

\[
m_p
=
2^{r-1}
\left\lfloor
\frac{\delta_pU}
{2^{r-1}\log U}
\right\rfloor,
\qquad
\delta_p\to0.
\tag{36}
\]

Then (35) becomes (10). If

\[
\frac{\epsilon_p}{\epsilon_r(p)}
\longrightarrow\infty,
\tag{37}
\]

choose

\[
\delta_p
\asymp_{r,\Delta}
\left(
\frac{\epsilon_r(p)}{\epsilon_p}
\right)^r
\tag{38}
\]

with the constant adjusted to produce any prescribed fixed separation \(\Delta>0\). Equation (37) makes \(\delta_p\to0\), while the super-polynomial size of \(U_A(p)\) ensures \(m_p\to\infty\), so the repeated distinct blocks exist.

Each control remains coarse-PNT-small. At every \(x\),

\[
|\pi_Q(x)-\pi(x)|
\le m_p
=
o(U/\log U),
\tag{39}
\]

and

\[
|\vartheta_Q(x)-\vartheta(x)|
\le(1+o(1))m_p\log U
=
o(U).
\tag{40}
\]

For every \(r\ge2\), the moment condition with \(k=1\) additionally gives exact equality of the two inserted total logarithmic masses. Hence after the terminal layer is passed,

\[
\pi_{P\cup P_1}(x)=\pi_{P\cup P_2}(x),
\qquad
\vartheta_{P\cup P_1}(x)=\vartheta_{P\cup P_2}(x)
\qquad(x\ge U).
\tag{41}
\]

Nevertheless, if (37) holds, the next unmatched placement moment can move the Robin source coordinate by order one.

Combining the lower construction with the universal upper bound (24) proves that \(\epsilon_r\) is the sharp vanishing-budget transition for this fixed-\(r\) architecture.

## 5. The hierarchy quantifies what a positive terminal theorem must remember

The first levels now line up exactly:

\[
\epsilon_1
=
\epsilon_{\mathrm{PNT}},
\qquad
\epsilon_2
=
\epsilon_*,
\qquad
\epsilon_r
=
\epsilon_{\mathrm{PNT}}^{1/r}.
\tag{42}
\]

Matching one more placement moment does not merely improve a constant. It changes the power of terminal width available to the adversarial source. Ignoring logarithmic factors, the \(r\)-th threshold is

\[
\epsilon_r(p)\asymp p^{-1/(2r)}.
\tag{43}
\]

Thus a theorem that controls only a fixed finite number of terminal moments has a calibratable resolution requirement. If moments through degree \(r-1\) are the only source information beyond coarse PNT, this matched-control class remains order-one ambiguous above \(p^{-1/(2r)}\) up to the displayed logarithmic factors. Reaching a thinner layer without using additional source-specific structure is not enough.

Conversely, this result does **not** say that ordinary primes supply arbitrary Prouhet packets, nor that controlling enough moments proves Robin. It only classifies an information-theoretic obstruction inside the generalized-source control class. A positive ordinary-prime/CA theorem may defeat it by coupling the moments, by short-interval rigidity, by exact prime-layer identities, or by a nonlocal signed relation that the synthetic controls do not preserve.

The quantifiers are also fixed-order. Nothing here is uniform in \(r=r(p)\). The constants in the Taylor remainder, the \(2^r\)-point Prouhet blocks, and the perturbation geometry all deteriorate with \(r\). Therefore (1) is an **all fixed orders** hierarchy, not a claim that a growing number of matched moments leaves the same asymptotic model.

## 6. Prior-art boundary

The equal-power-sum construction used in Section 3 is classical Prouhet--Tarry--Escott theory. A primary modern historical reference is E. M. Wright, *Prouhet's 1851 Solution of the Tarry-Escott Problem of 1910*, American Mathematical Monthly **66** (1959), 199--201, DOI `10.1080/00029890.1959.11989269`. The exact identity (27) is reproduced here, so no external theorem is needed for the derivation.

There is also nearby Robin/CA prior art on moments. Mantovanelli's August 2026 preprint, already anchored in `SOURCES.md`, gives a positive Hausdorff-moment hierarchy for the **CA workload itself**. That hierarchy is not the object classified here. Equations (21)--(42) concern moments of generalized-prime **terminal placement inside the exact RE-153 Robin influence**, used to test which local source summaries determine the Pareto-weighted height coordinate.

A targeted search across Robin/colossally-abundant moment formulations, Prouhet equal-power constructions, and Beurling/generalized-prime perturbations found the constituent classical mechanisms but not this terminal moment-cancellation/root-scale splice. The line-specific claim is therefore the exact hierarchy (1), (5), and (10), not novelty of Taylor expansion, Prouhet partitions, or moment methods themselves.

No external theorem is load-bearing: the full coefficient expansion follows from the exact influence already canonical in `RE-158`, and the sharp controls follow from the explicitly proved generating-function identity (27). No `SOURCES.md` update is required for correctness; Wright is recorded here as the classical novelty boundary.

## Research consequence

`RE-157` and `RE-158` were not isolated thresholds. They are the first two members of a general law:

\[
\boxed{
\text{match terminal placement moments }0,\ldots,r-1
\quad\Longrightarrow\quad
\text{first free mode }r
\quad\Longrightarrow\quad
\epsilon_r
=
\epsilon_{\mathrm{PNT}}^{1/r}.
}
\tag{44}
\]

The open selector-height clue is therefore more specific. A future positive source theorem should not merely say that the CA selector determines the terminal endpoint or even finitely many low-order summaries. It should state the **actual terminal distributional information** supplied by ordinary-prime and CA structure, and its resolution must be compared with the corresponding root-scale threshold. This turns the current source frontier from a sequence of ad hoc scales into an exact fixed-order moment hierarchy.
