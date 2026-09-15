# PL-320 — A convergent full-tail singular remainder forces the `Q^{-1/2}` coefficient and the moving-tail law

**Evidence:** `LITERATURE+EXACT-DERIVED + POSITIVE-BOUNDARY-MATCHING + GATE-REDUCTION`

**Status:** `LEADING-COEFFICIENT-NO-LONGER-INDEPENDENT + Qm-TAIL-AUTOMATIC + CONDITIONAL-MOMENT + ABSOLUTE-L1-STILL-OPEN`

## Precise claim

`PL-319` leaves two apparently separate endpoint tasks for the actual completed-Weil state: first prove a genuine leading boundary coefficient

\[
u(x_Q)=C Q^{-1/2}+m(Q),
\qquad x_Q=1-2e^{-Q},
\]

and then prove enough residual regularity/integrability to force the `PL-314` moving-tail condition `Qm(Q)->0`. The exact endpoint identity from `PL-319` shows that the first task and the pointwise part of the second task are in fact the same Tauberian problem.

Fix `Q_0>log 4`. Let `g(Q)` be any right-endpoint tail profile for which the exact `PL-319` identity holds,

\[
F(Q)=2Qg(Q)-U(Q)+H_{Q_0}g(Q)+c_{Q_0}(Q)g(Q),
\qquad
U(Q):=\int_{Q_0}^{Q}g(P)\,dP,
\tag{PL320-1}
\]

with

\[
\begin{aligned}
H_{Q_0}g(Q)
={}&\int_0^{Q-Q_0}
\frac{g(Q)-g(Q-h)}{e^h-1}\,dh\\
&+\int_0^\infty
\frac{g(Q)-g(Q+h)}{e^h-1}\,dh
\end{aligned}
\tag{PL320-2}
\]

and `c_{Q_0}(Q)` as in `PL-319`. Assume

\[
g(Q)\to0,
\qquad
F(Q)\to F_\infty,
\qquad
H_{Q_0}g(Q)\to H_\infty.
\tag{PL320-3}
\]

Then the boundary quotient exists automatically:

\[
\boxed{
C:=\lim_{Q\to\infty}\sqrt Q\,g(Q)
=\frac12\lim_{Q\to\infty}\frac{1}{\sqrt Q}
\int_{Q_0}^{Q}g(P)\,dP.
}
\tag{PL320-4}
\]

More strongly, with

\[
m(Q):=g(Q)-C Q^{-1/2},
\tag{PL320-5}
\]

one has

\[
\boxed{Qm(Q)\longrightarrow0}
\tag{PL320-6}
\]

and the residual has a convergent improper logarithmic moment,

\[
\boxed{
\lim_{Q\to\infty}\int_{Q_0}^{Q}m(P)\,dP
\quad\text{exists finitely}.}
\tag{PL320-7}
\]

Thus, for the actual completed-Weil eigenstate, **leading-coefficient matching and moving-diagonal anti-concentration are not independent gates**. `PL-319` already proves that the eigen-equation supplies the finite source trace after splitting off a compactly supported bulk component, while source 97 gives `g(Q)=O(Q^{-1/2})` and hence `g(Q)->0`. The remaining pointwise matching gate is therefore reduced to the single local statement

\[
\boxed{H_{Q_0}g(Q)\text{ has a finite endpoint limit}.}
\tag{PL320-8}
\]

This does **not** yet give the absolute `L^1(dQ)` residual required by the sufficient theorem in `PL-314`. That remaining distinction is real, not bookkeeping.

## 1. Exact Volterra reduction

Define

\[
R(Q):=F(Q)-H_{Q_0}g(Q)-c_{Q_0}(Q)g(Q).
\tag{PL320-9}
\]

Since `c_{Q_0}(Q)` has a finite limit and `g(Q)->0`, assumptions (PL320-3) imply

\[
R(Q)\to R_\infty:=F_\infty-H_\infty.
\tag{PL320-10}
\]

Equation (PL320-1) becomes the first-order Volterra identity

\[
\boxed{2Qg(Q)-U(Q)=R(Q).}
\tag{PL320-11}
\]

Put

\[
W(Q)=\frac{U(Q)}{\sqrt Q}.
\]

Because `U'=g`, (PL320-11) gives the exact derivative

\[
\boxed{
W'(Q)=\frac{R(Q)}{2Q^{3/2}}.
}
\tag{PL320-12}
\]

The right-hand side is integrable at infinity because `R` is bounded. Hence `W(Q)` has a finite limit; write that limit as `2C`. Solving (PL320-11) for `g` gives

\[
g(Q)=\frac{W(Q)}{2\sqrt Q}+rac{R(Q)}{2Q},
\tag{PL320-13}
\]

so `sqrt(Q) g(Q)->C`, proving (PL320-4).

The same calculation gives an exact remainder formula. Since

\[
W(Q)=2C-\int_Q^\infty\frac{R(P)}{2P^{3/2}}\,dP,
\]

we obtain

\[
\boxed{
m(Q)
=\frac{R(Q)}{2Q}
-\frac{1}{4\sqrt Q}
\int_Q^\infty\frac{R(P)}{P^{3/2}}\,dP.}
\tag{PL320-14}
\]

If `R(Q)->R_infty`, then

\[
\int_Q^\infty\frac{R(P)}{P^{3/2}}\,dP
=\frac{2R_\infty}{\sqrt Q}+o(Q^{-1/2}),
\]

and the two `R_infty/(2Q)` terms in (PL320-14) cancel. Therefore

\[
\boxed{m(Q)=o(Q^{-1}),}
\tag{PL320-15}
\]

which is exactly (PL320-6), strictly stronger than merely having the same `Q^{-1/2}` leading coefficient.

Finally,

\[
\begin{aligned}
\int_{Q_0}^{Q}m(P)\,dP
&=U(Q)-2C(\sqrt Q-\sqrt{Q_0})\\
&=-\frac{\sqrt Q}{2}
\int_Q^\infty\frac{R(P)}{P^{3/2}}\,dP
+2C\sqrt{Q_0},
\end{aligned}
\tag{PL320-16}
\]

so

\[
\boxed{
\int_{Q_0}^{Q}m(P)\,dP
\longrightarrow
2C\sqrt{Q_0}-R_\infty.}
\tag{PL320-17}
\]

A different harmless tail cutoff changes the finite constant in (PL320-17), not the existence of the limit or the coefficient `C`.

## 2. Application to the actual completed-Weil endpoint

`PL-319` already separates an actual state into a near-endpoint tail plus a compactly supported bulk component. The bulk contributes to `L_Delta u(x_Q)` by a term converging to a finite scalar as `Q->infinity`, so the tail source `F(Q)` has a finite limit whenever the full source does.

On a source-static aperture interval the completed-Weil eigen-equation is

\[
\left(\frac12L_\Delta+\gamma I\right)u
=(\lambda-K_a)u,
\tag{PL320-18}
\]

where `K_a` is a scalar term, finitely many compressed prime-power translations, and the continuous archimedean completion term. `PL-319` proves from this structure that `L_Delta u(x)` has a finite one-sided endpoint limit: outward fixed shifts eventually vanish, inward shifts converge to fixed interior values, the continuous kernel has a boundary limit, and `u(x)->0`.

Source 97 gives the sharp generic boundary upper law

\[
|u(x_Q)|=O(Q^{-1/2}),
\tag{PL320-19}
\]

but only two-sided comparability / Hopf-type lower information in the positive setting, not existence of a quotient `sqrt(Q)u(x_Q)`. Theorem 5.2 there, for example, proves the torsion bounds `c Q^{-1/2} <= u(x_Q) <= c^{-1}Q^{-1/2}` rather than a limiting coefficient. Thus the coefficient in (PL320-4) is not being imported from the existing boundary theorem.

For the actual state, the only new hypothesis needed to invoke the Volterra argument is therefore (PL320-8): convergence of the local singular translation remainder itself. If that holds at each endpoint, the `Q^{-1/2}` coefficient exists and the `PL-314` pointwise moving-diagonal obstruction is automatically suppressed.

## 3. Absolute `L^1` does not follow from this mechanism

The improvement above must not be overstated. The convergent improper moment (PL320-7) is weaker than

\[
\int_{Q_0}^\infty |m(Q)|\,dQ<\infty,
\]

which is the hypothesis used for the pre-diagonal dominated-convergence step in `PL-314`.

There is an explicit smooth control showing that this gap is genuine. After a smooth cutoff below some large `Q`, let

\[
m_*(Q)=\frac{\sin Q}{Q\log Q}.
\tag{PL320-20}
\]

Then

\[
Qm_*(Q)\to0,
\qquad
\int^{\infty}m_*(Q)\,dQ\text{ converges},
\qquad
\int^{\infty}|m_*(Q)|\,dQ=\infty.
\tag{PL320-21}
\]

Moreover `m_*'(Q)=O((Q\log Q)^{-1})`. The same near/far split used in `PL-319` therefore gives

\[
H_{Q_0}m_*(Q)\to0.
\tag{PL320-22}
\]

For the cutoff canonical profile `b(Q)=C Q^{-1/2}`, `PL-319` already gives `H_{Q_0}b(Q)->0` and a finite logarithmic source trace. Hence

\[
g(Q)=C Q^{-1/2}+m_*(Q)
\tag{PL320-23}
\]

has a finite source trace and a convergent full-tail singular remainder, satisfies the exact pointwise law `Q(g-CQ^{-1/2})->0`, and has a convergent improper residual moment, while its residual is not absolutely integrable.

Thus the full-tail source mechanism removes the **leading-coefficient** and **moving-diagonal pointwise** gates, but it cannot by itself justify the absolute `L^1` hypothesis used in `PL-314`.

## 4. Adversarial and novelty audit

**No generic boundary quotient theorem is being claimed.** The argument is conditional on convergence of the exact singular remainder (PL320-2). Existing logarithmic-Laplacian boundary theory supplies the sharp `Q^{-1/2}` scale but, in the literature audited through September 2026, the load-bearing results give upper bounds, two-sided comparison, or Hopf-type `liminf` information rather than a general quotient limit for bounded-source Dirichlet solutions. Search absence is not treated as evidence of broad novelty.

**The result is stronger than `PL-319` but uses its exact identity.** `PL-319` first assumes the coefficient `C` has been matched and then asks for an integrable/Dini residual. Here the same endpoint identity is applied to the full tail before subtracting a leading profile. Convergence of its singular remainder makes the coefficient emerge from the Volterra equation and forces the `o(1/Q)` residual pointwise.

**`PL-318` remains a sharp control.** Its sparse bounded-source example need not have a convergent endpoint source trace. The present theorem requires the actual source limit from the completed-Weil eigen-equation and, independently, convergence of the local singular remainder. Mere boundedness of either term is insufficient.

**Absolute integrability remains genuinely separate.** The oscillatory control (PL320-20) shows that even source-trace convergence plus `H->0` can leave a non-`L^1` residual. A future theorem must either prove absolute `L^1(dQ)` for the actual branch by source-specific structure, or strengthen `PL-314` so that a conditionally convergent residual moment plus `Qm(Q)->0` is enough for the rank-one Green transfer.

**The mechanism is universal, not arithmetic.** Nothing in (PL320-11)--(PL320-17) distinguishes rational primes. Prime specificity enters only through the completed-Weil source relation that supplies `F_infty` and through the later scalar compatibility/sign problem. This finding therefore advances the analytic matching gate but does not provide an RH sign mechanism.

**No analytic-continuation shortcut occurs.** The proof is entirely in the real-variable Dirichlet realization of the logarithmic Laplacian already justified in source 96 and in the persisted completed-Weil operator decomposition. No Euler product or half-plane identity is moved into the critical strip.

## Consequence for the research line

The endpoint program no longer needs to prove the leading `Q^{-1/2}` coefficient and `Qm(Q)->0` by separate matched-asymptotic estimates. The exact full-tail identity reduces both to the single local trace question

\[
H_{Q_0}g(Q)\to H_\infty.
\]

If this can be derived from the actual completed-Weil state-source coupling, then the only remaining analytic mismatch in the current `PL-313`--`PL-319` chain is **absolute pre-diagonal control**: either prove `m in L^1(dQ)` for the resulting residual, or replace the absolute-integrability step in `PL-314` by a justified conditional/oscillatory transfer theorem. The separate rational-prime first-crossing/sign gate remains downstream and untouched.

## Sources

- Source 96 in `research/prime_lattice/SOURCES.md`: Huyuan Chen and Tobias Weth, *The Dirichlet problem for the logarithmic Laplacian*, *Communications in Partial Differential Equations* **44**(11) (2019), 1100–1139. Supplies the singular-integral realization underlying (PL320-1).
- Source 97 in `research/prime_lattice/SOURCES.md`: Víctor Hernández-Santamaría, Luis Fernando López Ríos, Alberto Saldaña, *Optimal boundary regularity and a Hopf-type lemma for Dirichlet problems involving the logarithmic Laplacian*, *Discrete and Continuous Dynamical Systems* **45**(1) (2025), 1–36. Supplies the sharp `ell(delta)^{1/2} ~ Q^{-1/2}` boundary scale and the comparison/Hopf control used in the prior-art audit.
- `PL-314`: absolute `L^1(dQ)` plus `Qm(Q)->0` sufficient for the rank-one Green transfer; absolute `L^1` alone insufficient.
- `PL-318`: bounded logarithmic forcing still permits sparse moving-diagonal saturation.
- `PL-319`: exact endpoint-coordinate identity, convergent completed-Weil source trace, and residual source-trace Tauberian mechanism after leading matching.