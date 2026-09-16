# RE-156 — terminal source relocation capacity has a fourth-root transition

**Status:** `EXACT-DERIVED + LITERATURE-INPUT + MATCHED-SYNTHETIC-SOURCE-CAPACITY + SHRINKING-TERMINAL-LAYER-THRESHOLD + PNT-STABLE + PRIOR-ART-BOUNDED`. `RE-155` shows that exact source and generalized-CA event matching through every fixed fraction of the finite Robin horizon does not determine the `RE-153` Pareto-weighted Chebyshev source. The fixed-fraction restriction can be removed quantitatively: for equal-cardinality source relocations confined to a shrinking terminal layer of relative width `epsilon_p`, the total leverage is

\[
\boxed{
\operatorname{Cap}_p(\epsilon_p)
\asymp
\epsilon_p^2\,
\frac{\sqrt p\log p}{\log U_A(p)}.
}
\tag{1}
\]

Hence the order-one transition for this matched-control architecture is

\[
\boxed{
\epsilon_*(p)
:=
\sqrt{\frac{\log U_A(p)}{\sqrt p\log p}}
=
\sqrt A\,p^{-1/4}(\log p)^{1/3}(\log\log p)^{1/6}.
}
\tag{2}
\]

Thus PNT-scale source surgery survives not only to `(1-epsilon)U_A(p)` for every fixed `epsilon>0`, but through shrinking terminal layers whenever `epsilon_p/epsilon_*(p) -> infinity`; at `epsilon_p asymp epsilon_*(p)` the same relocation class still has order-one capacity. Only below this fourth-root relative scale does this **particular equal-cardinality terminal relocation mechanism** lose order-one leverage. This is an information obstruction, not a theorem that ordinary primes realize the relocation and not a proof that propagation below `epsilon_*(p)` controls Robin height.

Retain `RE-153`--`RE-155` and write

\[
U:=U_A(p)
=
\exp\!\left(
A(\log p)^{5/3}(\log\log p)^{1/3}
\right),
\qquad A>A_0,
\tag{3}
\]

where `A_0` is the `RE-022` PNT-tail threshold. Let

\[
\mathcal A_p(Q)
:=
\int_{J_p}
\frac{t-\vartheta_Q(t)}{\sqrt t}\,d\nu_p(t)
\tag{4}
\]

be the canonical normalized source coordinate, and for `epsilon=epsilon_p -> 0` let

\[
T_p(\epsilon):=[(1-\epsilon)U,U].
\tag{5}
\]

Consider controls obtained from the ordinary primes `P` by deleting `m` ordinary primes in `T_p(epsilon)` and inserting exactly `m` distinct non-prime real labels in the same layer, with no changes below `(1-epsilon)U`. Define

\[
\operatorname{Cap}_p(\epsilon)
:=
\sup_Q
\left|
\mathcal A_p(Q)-\mathcal A_p(P)
\right|.
\tag{6}
\]

If

\[
\epsilon_p
\gg
\exp\!\left(-aV(U_A(p))\right),
\qquad
V(x)=\frac{(\log x)^{3/5}}{(\log\log x)^{1/5}},
\tag{7}
\]

with the same absolute PNT constant `a>0` used in `RE-022`, then (1) holds with constants independent of `p` and `epsilon_p`.

For every fixed `A>A_0`, condition (7) already holds throughout the fourth-root transition. `RE-022` gives

\[
V(U_A(p))
=
\kappa_A\log p\,(1+o(1)),
\qquad
\kappa_A=A^{3/5}(3/5)^{1/5},
\tag{8}
\]

and chooses `A_0` so that `a\kappa_A>1/2`. Therefore

\[
\exp(-aV(U_A(p)))
=
p^{-a\kappa_A+o(1)}
=o(\epsilon_*(p)).
\tag{9}
\]

The existing unconditional PNT remainder is already strong enough to populate the shrinking shells at the scale where relocation capacity changes from vanishing to order one.

## 1. Near the horizon the exact label influence is locally linear

`RE-154` gives the exact influence of one added label `q<U`:

\[
\Lambda_p(q)
=
\frac{\sqrt p\log p}{Z_p}
\log q\,\bigl(h(q)-h(U)\bigr),
\qquad
Z_p=2+o(1),
\tag{10}
\]

where

\[
h(t)=\frac{-\log(1-t^{-1})}{\log t}.
\]

Set

\[
F_U(q):=\log q\,(h(q)-h(U)).
\tag{11}
\]

Since `log q h(q)=-log(1-q^{-1})`, direct differentiation gives

\[
\boxed{
-F_U'(q)
=
\frac1{q(q-1)}+\frac{h(U)}q.
}
\tag{12}
\]

Uniformly for `q in T_p(epsilon_p)` with `epsilon_p -> 0`, one has `q/U -> 1` and `h(U)=O(1/(U log U))`; hence

\[
-F_U'(q)=\frac{1+o(1)}{U^2}
\tag{13}
\]

uniformly on the whole layer. Combining (10), (13), and `Z_p=2+o(1)`, for any `q<s` there,

\[
\boxed{
\Lambda_p(q)-\Lambda_p(s)
=
\frac{1+o(1)}2
\frac{\sqrt p\log p}{U^2}(s-q).
}
\tag{14}
\]

In particular the full influence range across a layer of width `epsilon U` is

\[
\boxed{
\Lambda_p((1-\epsilon)U)-\Lambda_p(U)
=
\left(\frac12+o(1)\right)
\epsilon\frac{\sqrt p\log p}{U}.
}
\tag{15}
\]

This is the shrinking-layer version of the fixed-fraction relocation law in `RE-155`; no fixed limiting values of `q/U` are required.

## 2. PNT supplies the deletion labels at the transition scale

The unconditional Korobov--Vinogradov PNT remainder already anchored in `SOURCES.md` and used in `RE-015`/`RE-022` gives, uniformly for `x asymp U`,

\[
\vartheta(x)=x+O\!\left(xe^{-aV(x)}\right).
\tag{16}
\]

Under (7), subtracting (16) at the endpoints of `T_p(epsilon)` yields

\[
\vartheta(U)-\vartheta((1-\epsilon)U)
=(1+o(1))\epsilon U.
\tag{17}
\]

Every prime in the layer has logarithm `log U+o(log U)`, so

\[
\boxed{
\pi(U)-\pi((1-\epsilon)U)
=(1+o(1))\frac{\epsilon U}{\log U}.
}
\tag{18}
\]

The same estimate holds for every fixed fractional subinterval of the shrinking layer. Thus the available number of ordinary deletion labels is `Theta(epsilon U/log U)`. Equation (9) is load-bearing here: the particular horizon `U_A(p)` makes the PNT error much smaller than the fourth-root capacity scale.

## 3. Upper and lower relocation capacities match

Every equal-cardinality terminal relocation deletes at most the number of ordinary primes in (18). Pair each deleted label with one inserted label. By (15), every pair changes `A_p` by at most

\[
\left(\frac12+o(1)\right)
\epsilon\frac{\sqrt p\log p}{U}.
\tag{19}
\]

Multiplying (18) and (19) gives

\[
\operatorname{Cap}_p(\epsilon)
\ll
\epsilon^2\frac{\sqrt p\log p}{\log U}.
\tag{20}
\]

For the reverse inequality, split the terminal layer into separated early and late shells, for example

\[
I_-=[(1-\epsilon)U,(1-3\epsilon/4)U],
\qquad
I_+=[(1-\epsilon/4)U,(1-\epsilon/8)U].
\tag{21}
\]

Both contain `Theta(epsilon U/log U)` ordinary primes by the same PNT subtraction. Delete a fixed positive fraction of the ordinary primes in `I_-` and insert the same number of distinct non-prime real labels in `I_+`. Every pair has separation at least `epsilon U/2`, so (14) gives

\[
\Lambda_p(q)-\Lambda_p(s)
\ge
\left(\frac14+o(1)\right)
\epsilon\frac{\sqrt p\log p}{U}.
\tag{22}
\]

Using `Theta(epsilon U/log U)` such pairs yields

\[
\mathcal A_p(Q^+)-\mathcal A_p(P)
\gg
\epsilon^2\frac{\sqrt p\log p}{\log U}.
\tag{23}
\]

Reversing the relocation—insert early and delete ordinary primes late—gives the same lower bound in the negative direction. Equations (20)--(23) prove (1).

The dimensionless capacity parameter is therefore

\[
K_p(\epsilon)
:=
\epsilon^2\frac{\sqrt p\log p}{\log U}
=
\left(\frac{\epsilon}{\epsilon_*(p)}\right)^2.
\tag{24}
\]

If `epsilon/epsilon_* -> infinity`, the available matched-source displacement diverges. More quantitatively, for any prescribed fixed `Delta>0`, only

\[
m_p
\asymp_\Delta
\frac{U}{\epsilon\sqrt p\log p}
\tag{25}
\]

coherent relocations are required to achieve `|A_p(Q)-A_p(P)|>=Delta`, and

\[
\frac{m_p}{\epsilon U/\log U}
\asymp_\Delta
\frac1{K_p(\epsilon)}
\longrightarrow0.
\tag{26}
\]

Thus an asymptotically vanishing fraction of the primes available in the shrinking terminal shell still suffices for any fixed source displacement in the supercritical regime.

At `epsilon asymp epsilon_*`, (24) gives order-one total capacity. If instead `epsilon/epsilon_* -> 0` while (7) still holds, (20) shows that this **specific equal-cardinality terminal relocation architecture** has `o(1)` source leverage. That last statement is a boundary of the control construction, not a positive Robin theorem.

## 4. The controls remain invisible to coarse PNT information

All changes occur after `(1-epsilon)U`, so every control agrees exactly with the ordinary prime source below that cutoff. By the one-sided generalized-CA event property already used in `RE-154` and `RE-155`, its generalized event history also agrees exactly below `(1-epsilon)U`.

Even capacity-saturating controls remain PNT-small at scale `U`. They modify at most `Theta(epsilon U/log U)` labels, hence

\[
\sup_x|\pi_Q(x)-\pi(x)|
=O\!\left(\frac{\epsilon U}{\log U}\right)
=o\!\left(\frac U{\log U}\right)
\tag{27}
\]

and

\[
\sup_x|\vartheta_Q(x)-\vartheta(x)|
=O(\epsilon U)=o(U).
\tag{28}
\]

After both equal-cardinality modifications have been passed, every paired logarithmic difference is `O(epsilon)`, so the residual Chebyshev discrepancy is only

\[
O\!\left(\frac{\epsilon^2U}{\log U}\right)=o(U).
\tag{29}
\]

For fixed-displacement controls in the supercritical regime, (25) makes these perturbations smaller still. Shrinking the unmatched layer therefore does not by itself make the Pareto source stable under the same coarse PNT information used in `RE-155`.

## 5. Fourth-root scale and the remaining arithmetic gate

Using (3), equation (2) becomes

\[
\epsilon_*(p)
=
\sqrt A\,p^{-1/4}(\log p)^{1/3}(\log\log p)^{1/6}.
\tag{30}
\]

So the qualitative terminal gate left by `RE-155` is now a quantitative scale. Exact ordinary-source and generalized-event knowledge through `(1-\epsilon_p)U_A(p)` still fails, at PNT information level, to determine the `RE-153` source coordinate whenever `epsilon_p/epsilon_*(p) -> infinity`; at the transition scale the relocation class has order-one capacity.

The converse must not be overstated. When `epsilon_p=o(epsilon_*(p))`, this finding proves only that equal-cardinality relocations confined to that terminal layer cannot create an order-one change. It does not prove that a selector propagated that far controls the ordinary primes, that Robin's inequality follows, or that more structured signed modifications cannot escape. Zero-driven explicit-formula constraints, sharp square-root constants, correlations, nonlocal compensations, or exact ordinary-prime/global-CA identities can all use information absent from this matched-control class.

The unconditional PNT input in (16) is already recorded in `SOURCES.md` through Bellotti and was load-bearing in `RE-015`/`RE-022`. Generalized-prime perturbations and finite source surgery are classical background already bounded as prior art in `RE-154`--`RE-155`. A targeted audit of Robin/colossally-abundant Chebyshev--Mertens formulations and Beurling-prime perturbation literature did not locate the capacity law (1), the transition scale (2), or their splice to the self-tangent Pareto source. No new external theorem is load-bearing, so no `SOURCES.md` update is required.

## Research consequence

`RE-155` left open whether propagation through `(1-o(1))U_A(p)` might remove the matched-source freedom because PNT alone need not populate an arbitrarily thin terminal shell. For the equal-cardinality relocation mechanism, that question is now quantified: the shell's source capacity is `Theta((epsilon/epsilon_*)^2)` throughout the PNT-resolved regime.

Above `epsilon_*(p)` the PNT-stable relocation obstruction survives with growing capacity; at `epsilon_*(p)` it retains order-one capacity; below `epsilon_*(p)` this particular mechanism becomes subcritical. Further progress must either exploit that subcritical regime with a genuine CA-to-prime propagation theorem or introduce stronger arithmetic coupling that distinguishes the matched controls before the fourth-root terminal scale.