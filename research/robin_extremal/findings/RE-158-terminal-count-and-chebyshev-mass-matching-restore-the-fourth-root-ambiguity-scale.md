# RE-158 — terminal count and Chebyshev-mass matching restore the fourth-root ambiguity scale

**Status:** `EXACT-DERIVED + MATCHED-GENERALIZED-SOURCE-OBSTRUCTION + ENDPOINT-COUNT-AND-CHEBYSHEV-MASS-MATCHED + SECOND-ORDER-TERMINAL-CURVATURE + SHRINKING-LAYER-THRESHOLD + PRIOR-ART-BOUNDED`. `RE-157` shows that two PNT-small insertion packets of equal cardinality can move the normalized Robin source by order one down to the terminal scale

\[
\epsilon_{\mathrm{PNT}}(p)
=\frac{\log U_A(p)}{\sqrt p\log p}
=\epsilon_*(p)^2,
\]

because their **first-order placement moment** may differ. That freedom survives even though the two controls have the same number of inserted labels. If one also matches their total logarithmic mass exactly, so that both the terminal counting increment and terminal Chebyshev increment agree after the layer is passed, the first-order placement term cancels. The remaining ambiguity is controlled by the curvature of the exact Robin influence and has capacity

\[
\boxed{
\operatorname{Cap}^{(\vartheta)}_p(\epsilon,\delta)
\asymp
\delta\,\epsilon^2
\frac{\sqrt p\log p}{\log U_A(p)}
=
\delta\left(\frac{\epsilon}{\epsilon_*(p)}\right)^2.
}
\tag{1}
\]

Consequently, under a vanishing coarse-PNT perturbation budget `delta_p -> 0`, order-one source ambiguity survives whenever

\[
\boxed{
\frac{\epsilon_p}{\epsilon_*(p)}\longrightarrow\infty,
}
\tag{2}
\]

whereas every such endpoint-matched insertion family is `o(1)`-stable when `epsilon_p=O(epsilon_*(p))`. Thus matching one additional terminal statistic—total Chebyshev mass—raises the insertion-placement ambiguity scale from the `RE-157` square-root/PNT scale `epsilon_PNT` back to the `RE-156` fourth-root scale `epsilon_*`. The identical exponent has a different cause: `RE-156` pays a second factor of `epsilon` because ordinary primes available for deletion are scarce; here it comes from cancellation of the linear placement moment and exposure of the quadratic curvature of the Robin kernel.

Retain the notation of `RE-153`--`RE-157` and write

\[
U:=U_A(p),
\qquad
\epsilon_*^2
=\epsilon_{\mathrm{PNT}}
=\frac{\log U}{\sqrt p\log p},
\qquad
T_p(\epsilon):=[(1-\epsilon)U,U].
\tag{3}
\]

For an increasing real-label source `Q`, let

\[
\mathcal A_p(Q)
:=
\int_{J_p}
\frac{t-\vartheta_Q(t)}{\sqrt t}\,d\nu_p(t)
\tag{4}
\]

be the canonical normalized source coordinate. The exact influence of one added label `q<U` is

\[
\Lambda_p(q)
=
\frac{\sqrt p\log p}{Z_p}
\log q\,\bigl(h(q)-h(U)\bigr),
\qquad
Z_p=2+o(1),
\tag{5}
\]

and adding `q` changes `A_p` by `-Lambda_p(q)`.

## 1. Logarithmic terminal position exposes the exact first two placement moments

Put

\[
a(t):=-\log(1-t^{-1}),
\qquad
z:=\log\frac Uq,
\qquad
q=Ue^{-z}.
\tag{6}
\]

For `q in T_p(epsilon)`,

\[
0\le z\le L_\epsilon:=-\log(1-\epsilon)
=\epsilon+O(\epsilon^2).
\tag{7}
\]

Since `log(t)h(t)=a(t)`, the bracket in (5) has the exact form

\[
\log q\,\bigl(h(q)-h(U)\bigr)
=
a(Ue^{-z})-a(U)+\frac{a(U)}{\log U}z.
\tag{8}
\]

Taylor expansion at `z=0` is especially transparent. Direct differentiation gives

\[
\frac{d}{dz}a(Ue^{-z})\Big|_{z=0}
=\frac1{U-1},
\qquad
\frac{d^2}{dz^2}a(Ue^{-z})\Big|_{z=0}
=\frac{U}{(U-1)^2}.
\tag{9}
\]

Uniformly for `0<=z<=L_epsilon` with `epsilon->0`, the third derivative is `O(1/U)`. Hence

\[
\boxed{
\Lambda_p(Ue^{-z})
=
\frac{\sqrt p\log p}{Z_pU}
\left[
 b_1(U)z+b_2(U)z^2+O(z^3)
\right],
}
\tag{10}
\]

where

\[
b_1(U)
=\frac{U}{U-1}+\frac{Ua(U)}{\log U}
=1+\frac1{\log U}+O(U^{-1}),
\tag{11}
\]

and

\[
b_2(U)
=\frac{U^2}{2(U-1)^2}
=\frac12+O(U^{-1}).
\tag{12}
\]

Equation (10) refines the first-derivative law of `RE-156`--`RE-157`. The linear statistic is not an arbitrary coordinate: for an insertion packet `{q_i}` of cardinality `m`,

\[
\sum_{i=1}^m z_i
=m\log U-\sum_{i=1}^m\log q_i.
\tag{13}
\]

Therefore two equal-cardinality packets have the same first `z`-moment **if and only if they have exactly the same total Chebyshev weight** `sum log q_i`. Matching the terminal endpoint values of both `pi` and `theta` cancels the complete linear term in (10).

## 2. Exact endpoint matching leaves a quadratic placement degree of freedom

Let two insertion packets

\[
P_1=\{q_1,\ldots,q_m\},
\qquad
P_2=\{r_1,\ldots,r_m\}
\subset T_p(\epsilon)
\tag{14}
\]

consist of distinct non-prime real labels. Write

\[
z_i=\log(U/q_i),
\qquad
y_i=\log(U/r_i).
\tag{15}
\]

Assume the exact endpoint matching conditions

\[
|P_1|=|P_2|=m,
\qquad
\sum_{i=1}^m\log q_i
=\sum_{i=1}^m\log r_i.
\tag{16}
\]

By (13), `sum z_i=sum y_i`. Let `Q_1=P cup P_1` and `Q_2=P cup P_2`, where `P` is the ordinary-prime source. Applying (10) and cancelling the linear term gives

\[
\boxed{
\mathcal A_p(Q_1)-\mathcal A_p(Q_2)
=
-\frac{\sqrt p\log p}{Z_pU}
\left[
 b_2(U)
 \left(\sum_i z_i^2-\sum_i y_i^2\right)
 +O(m\epsilon^3)
\right].
}
\tag{17}
\]

In particular, for arbitrary endpoint-matched packets,

\[
\boxed{
|\mathcal A_p(Q_1)-\mathcal A_p(Q_2)|
\ll
m\epsilon^2\frac{\sqrt p\log p}{U}.
}
\tag{18}
\]

The source coordinate therefore remembers the **spread** of terminal logarithmic locations after endpoint count and total Chebyshev mass have been erased. It is not determined by those two endpoint statistics.

The quadratic freedom is genuinely realizable. Let `L=L_epsilon` and take `m` even. Choose distinct numbers `t_j,s_j=o(L)` for `1<=j<=m/2`, all positive and small enough that the following labels are distinct and non-prime. Define a spread packet by the `z`-coordinates

\[
\{t_j,L-t_j:1\le j\le m/2\},
\tag{19}
\]

and a centered packet by

\[
\{L/2-s_j,L/2+s_j:1\le j\le m/2\}.
\tag{20}
\]

Every pair in both packets has sum `L`, so (16) holds **exactly**. Their quadratic moments satisfy

\[
\sum_{P_{\rm spread}}z^2
-
\sum_{P_{\rm center}}z^2
=
\left(\frac14+o(1)\right)mL^2.
\tag{21}
\]

Using `L=epsilon+O(epsilon^2)`, `b_2(U)=1/2+o(1)` and `Z_p=2+o(1)`, equations (17) and (21) yield

\[
\boxed{
|\mathcal A_p(Q_{\rm spread})
-\mathcal A_p(Q_{\rm center})|
=
\left(\frac1{16}+o(1)\right)
 m\epsilon^2
 \frac{\sqrt p\log p}{U}.
}
\tag{22}
\]

Thus the upper bound (18) is sharp up to an absolute constant within this endpoint-matched insertion class.

## 3. The sharp vanishing-budget transition is the fourth-root scale

Put

\[
m_p
=2\left\lfloor
\frac{\delta_pU}{2\log U}
\right\rfloor,
\qquad
\delta_p\to0.
\tag{23}
\]

For the packets in (19)--(20), equation (22) becomes

\[
\boxed{
|\mathcal A_p(Q_{\rm spread})
-\mathcal A_p(Q_{\rm center})|
=
\left(\frac1{16}+o(1)\right)
\delta_p\epsilon_p^2
\frac{\sqrt p\log p}{\log U}
=
\left(\frac1{16}+o(1)\right)
\delta_p
\left(\frac{\epsilon_p}{\epsilon_*(p)}\right)^2.
}
\tag{24}
\]

If `epsilon_p/epsilon_*(p) -> infinity`, then for any prescribed `Delta>0` one may choose

\[
\delta_p
=(16\Delta+o(1))
\left(\frac{\epsilon_*(p)}{\epsilon_p}\right)^2.
\tag{25}
\]

This tends to zero, while (24) tends to `Delta`. Because `U_A(p)` is super-polynomial in `p` whereas the displayed terminal scales are only polynomially small up to logarithms, `m_p->infinity`, so the distinct packets can be realized.

Conversely, let two endpoint-matched packets each use

\[
m_p=o(U/\log U)
\tag{26}
\]

labels. Equation (18) gives

\[
|\mathcal A_p(Q_1)-\mathcal A_p(Q_2)|
=
o\!\left(
\epsilon_p^2\frac{\sqrt p\log p}{\log U}
\right)
=
o\!\left(
\left(\frac{\epsilon_p}{\epsilon_*(p)}\right)^2
\right).
\tag{27}
\]

Therefore

\[
\boxed{
\epsilon_p=O(\epsilon_*(p))
\quad\Longrightarrow\quad
|\mathcal A_p(Q_1)-\mathcal A_p(Q_2)|=o(1)
}
\tag{28}
\]

for every vanishing-budget endpoint-matched insertion family. Equations (24)--(28) establish the sharp lower envelope (2) for this architecture.

## 4. The controls match more than coarse PNT density

Both controls agree exactly with the ordinary prime source below `(1-epsilon)U`. Their terminal counting increments are both exactly `m_p`, and (16) makes their total inserted Chebyshev mass exactly equal. Hence after `U` is passed,

\[
\boxed{
\pi_{Q_1}(x)-\pi_{Q_2}(x)=0,
\qquad
\vartheta_{Q_1}(x)-\vartheta_{Q_2}(x)=0
\qquad(x\ge U).
}
\tag{29}
\]

Inside the terminal layer, each control differs from the ordinary source by at most

\[
|\pi_Q(x)-\pi(x)|\le m_p
=o(U/\log U)
\tag{30}
\]

and

\[
|\vartheta_Q(x)-\vartheta(x)|
\le(1+o(1))m_p\log U
=(1+o(1))\delta_pU
=o(U).
\tag{31}
\]

Thus the matched pair has the same source below the layer, the same endpoint values of both first-layer counting summaries after the layer, and only a PNT-small disturbance while traversing it. Nevertheless, above the fourth-root scale, the **path by which the equal terminal mass is placed** can change the Robin source coordinate by a fixed amount.

This sharpens the information boundary from `RE-157`. There, equal cardinality removed only the zeroth-order counting discrepancy, leaving a linear placement degree of freedom and the scale `epsilon_PNT`. Here exact equality of total logarithmic mass removes that linear degree of freedom. The next Taylor coefficient is quadratic, and the threshold becomes

\[
\epsilon_*=\sqrt{\epsilon_{\mathrm{PNT}}}.
\tag{32}
\]

The coincidence with `RE-156` should not be conflated. In `RE-156`, the second `epsilon` factor comes from the number `Theta(epsilon U/log U)` of ordinary primes available for deletion. In (24), the insertion budget remains `delta U/log U` independently of the shell width; the second `epsilon` appears because endpoint Chebyshev matching cancels the linear influence and leaves only kernel curvature.

## 5. Scope, prior art, and the remaining arithmetic gate

This is again a matched generalized-source obstruction, not a modification of the ordinary primes and not a Robin counterexample. It proves neither that actual CA structure permits such terminal rearrangements nor that propagation to `epsilon_*` is sufficient for a positive Robin theorem. It says something narrower and useful: **endpoint knowledge of both `pi` and `theta` does not identify the terminal Robin source above the fourth-root scale** under a vanishing PNT perturbation budget. A positive argument must control the distribution of Chebyshev mass *inside* the layer, not merely its total amount at the far endpoint.

The accepted selector-height clue remains open. `RE-153` identifies the target as a Pareto-weighted Chebyshev-deficit average; `RE-154`--`RE-157` show successively that fixed-cutoff knowledge, near-complete source knowledge, and coarse terminal PNT control do not determine it. The present result isolates the next statistic: once terminal count and total logarithmic mass are matched, the first surviving source freedom is quadratic placement spread. A genuine CA-to-prime propagation theorem would have to constrain that internal placement, or exploit ordinary-prime identities unavailable to generalized controls.

The prior-art audit was deliberately separated from the algebra. Beurling generalized-prime perturbations are classical, and recent work on small perturbations of generalized-prime systems confirms that considerable geometric freedom can coexist with analytic constraints. Mantovanelli's 2026 preprint, already anchored in `SOURCES.md`, develops a **different** positive Hausdorff-moment hierarchy for the CA workload itself; no novelty is claimed for moment methods in Robin/CA analysis. The statistic in (16)--(24) is instead the local Taylor moment of terminal generalized-prime **placement** inside the exact `RE-153` Robin influence. A targeted search did not locate this endpoint-matched terminal curvature law or the transition (24). No external theorem is load-bearing: the result follows from the exact influence (5), elementary Taylor expansion, and the matched-control framework already canonical in `RE-154`--`RE-157`. No `SOURCES.md` update is required.

## Research consequence

The source-side terminal ladder now has two quantitatively distinct information levels. Equal inserted cardinality alone leaves first-order placement freedom and therefore ambiguity down to

\[
\epsilon_{\mathrm{PNT}}
=\epsilon_*^2.
\]

If total terminal Chebyshev mass is also matched exactly, that first-order freedom disappears and the sharp vanishing-budget ambiguity boundary rises to

\[
\boxed{
\epsilon_*(p)
=\sqrt{\frac{\log U_A(p)}{\sqrt p\log p}}
=\sqrt A\,p^{-1/4}(\log p)^{1/3}(\log\log p)^{1/6}.
}
\tag{33}
\]

Therefore a prospective positive theorem cannot be calibrated only by how close its propagation reaches to `U_A(p)`. It must also specify **which terminal source moments it controls**. Reaching the fourth-root layer while knowing only endpoint count and Chebyshev mass still leaves order-one ambiguity just above that scale; below it, this particular endpoint-matched insertion mechanism becomes subcritical and a stronger ordinary-prime/CA rigidity argument can meaningfully begin.