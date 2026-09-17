# PL-340 — PNT endpoint modes cap global jump coercivity at three-halves of source mass

**Evidence:** `EXACT-DERIVED + DECISIVE-NEGATIVE-FOR-JUMP-ONLY-COMPENSATION + PNT-MATCHED-CONTROL`

**Status:** `MACROSCOPIC-NEGATIVE-PRIME-DIRECTION + JUMP-GAP-CEILING + COMPLETION-STILL-REQUIRED + NO-RH-CONSEQUENCE`

## Precise claim

Let the fixed-domain prime operators of `PL-337`--`PL-339` on `I=(-1,1)` be

\[
K_a:=\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}
\bigl(S_{\log n/a}+S_{\log n/a}^*\bigr),
\qquad
P_a:=-K_a,
\tag{PL340-1}
\]

and write

\[
W_a:=\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n},
\qquad
J_a:=\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}D_{\log n/a}
=2W_aI-K_a.
\tag{PL340-2}
\]

`PL-339` proves

\[
J_a\ge(1-o(1))W_aI,
\qquad
\|P_a\|\le(1+o(1))W_a,
\qquad
W_a\sim2e^a.
\tag{PL340-3}
\]

The natural next possibility would be that compatibility among the many positive jump forms improves the lower edge of `J_a` all the way toward `2W_a`, thereby asymptotically canceling the scalar compensation in `P_a=J_a-2W_aI`. That possibility is ruled out by the already-established PNT endpoint modes.

For every fixed boundary depth `R>0`, put

\[
N_R:=1-e^{-R}.
\tag{PL340-4}
\]

There exist normalized symmetric and antisymmetric endpoint-layer states `u_{a,R}^+` and `u_{a,R}^-` such that

\[
\boxed{
 e^{-a}\langle K_au_{a,R}^{\pm},u_{a,R}^{\pm}\rangle
 \longrightarrow \pm N_R
}
\qquad(a\to\infty).
\tag{PL340-5}
\]

Consequently

\[
\boxed{
\frac{\langle P_au_{a,R}^{\pm},u_{a,R}^{\pm}\rangle}{W_a}
\longrightarrow \mp\frac{N_R}{2}
}
\tag{PL340-6}
\]

and, for the symmetric state,

\[
\boxed{
\frac{\langle J_au_{a,R}^{+},u_{a,R}^{+}\rangle}{W_a}
\longrightarrow 2-\frac{N_R}{2}.
}
\tag{PL340-7}
\]

Letting `R` be arbitrarily large after the `a->infinity` limit gives the asymptotic spectral constraints

\[
\boxed{
\limsup_{a\to\infty}
\frac{\inf\sigma(P_a)}{W_a}
\le-\frac12,
\qquad
\liminf_{a\to\infty}
\frac{\sup\sigma(P_a)}{W_a}
\ge\frac12,
}
\tag{PL340-8}
\]

hence

\[
\boxed{
\frac12
\le
\liminf_{a\to\infty}\frac{\|P_a\|}{W_a}
\le
\limsup_{a\to\infty}\frac{\|P_a\|}{W_a}
\le1.
}
\tag{PL340-9}
\]

For the positive jump sector, combining (PL340-7) with the lower bound from `PL-339` yields

\[
\boxed{
1
\le
\liminf_{a\to\infty}\frac{\inf\sigma(J_a)}{W_a}
\le
\limsup_{a\to\infty}\frac{\inf\sigma(J_a)}{W_a}
\le\frac32.
}
\tag{PL340-10}
\]

Thus the accumulated jump forms are indeed coercive at total-source scale, but their joint lower edge cannot approach the `2W_a` needed to neutralize the scalar compensation. The isolated prime block has both positive and negative Rayleigh directions of order `W_a` unconditionally. This closes the route

\[
\text{stronger joint jump coercivity alone}
\quad\Longrightarrow\quad
P_a\ge-o(W_a)I.
\]

It does **not** imply that the completed Weil operator has a negative direction. `PL-059` proves that the zeta-pole term cancels precisely the universal first-order PNT endpoint mode used below. The conclusion is therefore a route boundary: completion or a genuinely centered/source-specific mechanism is mathematically indispensable.

## 1. Unitary identification with the boundary operator of `PL-051`

Work first on the moving interval

\[
H_a=L^2(-a,a).
\]

Let

\[
\widetilde K_a
=
\sum_{\log n<2a}
\frac{\Lambda(n)}{\sqrt n}
\bigl(T_{\log n}+T_{\log n}^*\bigr),
\tag{PL340-11}
\]

where `T_u` is translation by `u` compressed to `(-a,a)`. The dilation

\[
(U_af)(x)=a^{1/2}f(ax),
\qquad x\in(-1,1),
\tag{PL340-12}
\]

is unitary from `H_a` to `L^2(I)` and satisfies

\[
U_aT_{\log n}U_a^{-1}=S_{\log n/a}.
\tag{PL340-13}
\]

Hence

\[
K_a=U_a\widetilde K_aU_a^{-1}.
\tag{PL340-14}
\]

The fixed-depth endpoint compression in `PL-051` is therefore exactly a family of increasingly thin endpoint layers for the fixed-domain operators of `PL-339`; no new model is being inserted.

For fixed `R`, let

\[
h_R(t)=e^{-t/2},
\qquad
\|h_R\|_2^2=N_R,
\tag{PL340-15}
\]

on `(0,R)`, and define the unit vectors

\[
\eta_R^{\pm}
=
\frac1{\sqrt{2N_R}}(h_R,\pm h_R)
\in L^2(0,R)\oplus L^2(0,R).
\tag{PL340-16}
\]

`PL-051` proves strong convergence of the normalized endpoint compression,

\[
e^{-a}J_{a,R}^*\widetilde K_aJ_{a,R}
\longrightarrow
B_R
=
\begin{pmatrix}
0&P_R\\
P_R&0
\end{pmatrix},
\qquad
P_R=|h_R\rangle\langle h_R|,
\tag{PL340-17}
\]

and

\[
B_R\eta_R^{\pm}=\pm N_R\eta_R^{\pm}.
\tag{PL340-18}
\]

Set

\[
u_{a,R}^{\pm}:=U_aJ_{a,R}\eta_R^{\pm}.
\tag{PL340-19}
\]

These are normalized fixed-domain states supported in endpoint strips of width `R/a`. Equations (PL340-17)--(PL340-19) give (PL340-5) directly.

## 2. The scalar compensation leaves a fixed-fraction negative direction

The weighted prime-power mass satisfies, by the PNT and Stieltjes partial summation,

\[
W_a\sim2e^a.
\tag{PL340-20}
\]

Since `P_a=-K_a`, divide (PL340-5) by (PL340-20):

\[
\frac{\langle P_au_{a,R}^{+},u_{a,R}^{+}\rangle}{W_a}
\to-\frac{N_R}{2},
\qquad
\frac{\langle P_au_{a,R}^{-},u_{a,R}^{-}\rangle}{W_a}
\to+\frac{N_R}{2}.
\tag{PL340-21}
\]

For each fixed `R`, Rayleigh's principle therefore gives

\[
\limsup_{a\to\infty}\frac{\inf\sigma(P_a)}{W_a}
\le-\frac{N_R}{2},
\qquad
\liminf_{a\to\infty}\frac{\sup\sigma(P_a)}{W_a}
\ge\frac{N_R}{2}.
\tag{PL340-22}
\]

Because `N_R\uparrow1`, (PL340-8) follows. The norm lower bound in (PL340-9) is immediate, while its upper bound is exactly `PL-339`.

This proves more than the statement in `PL-339` that its lower estimate still *permits* a source-scale negative contribution. Such a contribution actually occurs on explicit endpoint-layer states, with asymptotic magnitude at least one half of total source mass after optimizing the fixed depth.

## 3. The positive jump gap has an asymptotic ceiling

Using the exact identity

\[
J_a=2W_aI-K_a,
\tag{PL340-23}
\]

on the symmetric endpoint state gives

\[
\frac{\langle J_au_{a,R}^{+},u_{a,R}^{+}\rangle}{W_a}
=
2-
\frac{\langle K_au_{a,R}^{+},u_{a,R}^{+}\rangle}{W_a}
\longrightarrow
2-\frac{N_R}{2}.
\tag{PL340-24}
\]

Hence

\[
\limsup_{a\to\infty}
\frac{\inf\sigma(J_a)}{W_a}
\le2-\frac{N_R}{2}
\tag{PL340-25}
\]

for every `R`. Sending `R->infinity` gives the upper `3/2` in (PL340-10). The lower `1` is the PNT-scale path-gap estimate of `PL-339`.

The constants have a clear interpretation. The source mass is asymptotically `2e^a`. The fixed-depth PNT boundary shell contributes a coherent prime-shift Rayleigh value approaching `e^a`. Thus on that state the jump decomposition reads, at leading order,

\[
J_a\sim4e^a-e^a=3e^a,
\qquad
P_a=J_a-2W_aI\sim-e^a.
\tag{PL340-26}
\]

The positive jump sector remains large, but the compensation is larger by an order-one fraction. No refinement based only on summing positive channel gaps can remove this endpoint witness.

## 4. Completion cancels this witness at first PNT order

The negative direction in (PL340-21) is deliberately **not** promoted to a completed-Weil sign conclusion. `PL-051` identifies the endpoint limit as the universal rank-one PNT Hankel block `B_R`; `PL-059` then proves that the zeta-pole sector has the same normalized boundary limit with the opposite sign in the completed Weil form. Thus the specific `O(e^a)` endpoint mode producing (PL340-8) is canonically centered by completion.

This is the important route distinction:

\[
\text{jump sector alone}
\quad\text{cannot neutralize }-2W_aI,
\]

while

\[
\text{completed pole-prime sector}
\quad\text{does neutralize the universal fixed-profile PNT mode}.
\]

What remains after that cancellation is the centered atomic discrepancy and its interaction with the archimedean/form-domain sector, not a missing improvement of the coarse jump Poincare constant. In particular, (PL340-10) should not motivate further attempts to push the universal lower bound for `J_a` toward `2W_a`; the endpoint family proves that target false.

## 5. Adversarial, matched-control, and novelty audit

The argument uses no Euler product and no analytic continuation step. Each finite-`a` prime operator is the finite von-Mangoldt translation sum already extracted from the completed Weil explicit formula. The only asymptotic input is the PNT-scale endpoint result already proved in `PL-051` and `W_a\sim2e^a`.

The mechanism is deliberately **not rational-prime-specific**. `PL-051` proves that the fixed-depth endpoint mode depends only on a positive weighted shell law converging to `e^{-\delta/2}d\delta`; a matched Beurling/generalized-prime source with the same shell asymptotic has the same `N_R` boundary block and therefore the same constants `1/2` and `3/2` above. The present result is consequently a no-go for a universal jump-only positivity strategy, not a new characterization of the rational primes.

A current literature audit around Suzuki's localized Weil operator, prime-power translation terms, endpoint/boundary scaling, and truncated Weil quadratic forms located the active 2026 Suzuki/Connes--Consani--Moscovici numerical and operator literature but no independent theorem that strengthens this line-local spectral bracket. No novelty is claimed on that basis: (PL340-8)--(PL340-10) are explicit consequences of the already-persisted `PL-051` boundary model combined with the later `PL-339` jump decomposition.

Adversarial boundaries:

- **No exact spectral-edge limit.** The result gives one-sided asymptotic brackets. It does not prove that `||P_a||/W_a`, `inf sigma(J_a)/W_a`, or either edge has a limit.
- **No completed-Weil negativity.** The pole cancellation in `PL-059` removes this universal fixed-profile PNT boundary mode at first order.
- **No branch statement.** The endpoint witnesses depend on `a`; they are variational test states, not the tracked low eigenbranch from `PL-338`.
- **No rational-prime rigidity.** The constants survive matched positive shell systems with the same PNT law.
- **No contradiction with stronger recurrence.** High-frequency prime-log recurrence may affect operator or essential-norm edges, but it cannot erase the explicit endpoint Rayleigh values used here.

## Consequence for `prime_lattice`

`PL-339` established that the positive atomic jump sector does not dilute as more prime powers activate. The present result supplies the complementary ceiling: **that coercivity cannot, even jointly, grow enough to absorb the exact scalar compensation.** The prime block has an unavoidable source-scale negative endpoint direction before completion, while completion already cancels that particular PNT-universal mode.

The live global target is therefore narrower. A scalable RH-facing argument must use the canonically centered completed operator and extract structure from the residual atomic/archimedean interaction, or from the actual transported eigenbranch and its source-specific boundary trace. Further improvement of source-blind positive jump gaps alone cannot close the sign problem.

## Dependencies

- `PL-051`: fixed-depth boundary blow-up and the universal rank-one PNT Hankel limit with eigenvalues `+/- (1-e^{-R})`.
- `PL-059`: canonical cancellation of that PNT boundary mode by the zeta-pole sector in the completed Weil form.
- `PL-337`: exact decomposition `P_a=J_a-2W_aI` into positive atomic jumps plus scalar compensation.
- `PL-339`: exact path-chain gaps, `J_a>=(1-o(1))W_aI`, `||P_a||<=(1+o(1))W_a`, and `W_a~2e^a`.
