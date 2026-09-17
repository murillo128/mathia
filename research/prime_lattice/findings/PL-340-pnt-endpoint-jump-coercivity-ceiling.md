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

and

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

A natural remaining hope would be that compatibility among the many positive jump forms raises the lower edge of `J_a` all the way toward `2W_a`, asymptotically neutralizing the scalar compensation in `P_a=J_a-2W_aI`. The PNT endpoint modes already constructed in `PL-051` rule this out.

For every fixed endpoint depth `R>0`, put

\[
N_R:=1-e^{-R}.
\tag{PL340-4}
\]

There are normalized symmetric and antisymmetric endpoint-layer states `u_{a,R}^+` and `u_{a,R}^-` such that

\[
\boxed{
 e^{-a}\langle K_au_{a,R}^{\pm},u_{a,R}^{\pm}\rangle
 \longrightarrow \pm N_R
}
\qquad(a\to\infty).
\tag{PL340-5}
\]

Since `W_a\sim2e^a`, this gives

\[
\boxed{
\frac{\langle P_au_{a,R}^{\pm},u_{a,R}^{\pm}\rangle}{W_a}
\longrightarrow \mp\frac{N_R}{2}
}
\tag{PL340-6}
\]

and, on the symmetric state,

\[
\boxed{
\frac{\langle J_au_{a,R}^{+},u_{a,R}^{+}\rangle}{W_a}
\longrightarrow 2-\frac{N_R}{2}.
}
\tag{PL340-7}
\]

Letting `R` be arbitrarily large after the `a->infinity` limit yields

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

and therefore

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

Combining (PL340-7) with the lower bound of `PL-339` gives the jump-sector bracket

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

Thus the accumulated jump forms are coercive at total-source scale, but their joint lower edge cannot approach the `2W_a` needed to neutralize the scalar compensation. The isolated prime block has both positive and negative Rayleigh directions of order `W_a` unconditionally. This is a decisive negative for the route

\[
\text{stronger joint jump coercivity alone}
\Longrightarrow
P_a\ge-o(W_a)I.
\tag{PL340-11}
\]

It is **not** a negative-direction theorem for the completed Weil operator. `PL-059` proves that the zeta-pole term cancels precisely the universal first-order PNT endpoint mode used here. The conclusion is instead that completion, centering, or genuinely source-specific branch information is mathematically indispensable.

## 1. Transfer of the `PL-051` endpoint states to the fixed domain

On the moving interval `H_a=L^2(-a,a)`, let

\[
\widetilde K_a
=
\sum_{\log n<2a}
\frac{\Lambda(n)}{\sqrt n}
\bigl(T_{\log n}+T_{\log n}^*\bigr),
\tag{PL340-12}
\]

where `T_u` is translation by `u` compressed to `(-a,a)`. The dilation

\[
(U_af)(x)=a^{1/2}f(ax),
\qquad x\in(-1,1),
\tag{PL340-13}
\]

is unitary and satisfies

\[
U_aT_{\log n}U_a^{-1}=S_{\log n/a},
\qquad
K_a=U_a\widetilde K_aU_a^{-1}.
\tag{PL340-14}
\]

Hence the fixed-depth endpoint blow-up of `PL-051` is exactly an increasingly thin endpoint layer for the fixed-domain operator of `PL-339`.

For fixed `R`, define

\[
h_R(t)=e^{-t/2},
\qquad
\|h_R\|_2^2=N_R,
\tag{PL340-15}
\]

on `(0,R)`, and the unit vectors

\[
\eta_R^{\pm}
=
\frac1{\sqrt{2N_R}}(h_R,\pm h_R)
\in L^2(0,R)\oplus L^2(0,R).
\tag{PL340-16}
\]

`PL-051` proves

\[
e^{-a}J_{a,R}^*\widetilde K_aJ_{a,R}
\longrightarrow
B_R
=
\begin{pmatrix}
0&P_R\\
P_R&0
\end{pmatrix}
\quad\text{strongly},
\qquad
P_R=|h_R\rangle\langle h_R|,
\tag{PL340-17}
\]

with

\[
B_R\eta_R^{\pm}=\pm N_R\eta_R^{\pm}.
\tag{PL340-18}
\]

Set

\[
u_{a,R}^{\pm}:=U_aJ_{a,R}\eta_R^{\pm}.
\tag{PL340-19}
\]

These states are normalized and supported in fixed-domain endpoint strips of width `R/a`. Strong convergence on the fixed vectors `eta_R^pm` gives (PL340-5).

## 2. Fixed-fraction negative and positive prime directions

From `P_a=-K_a`, (PL340-5), and `W_a\sim2e^a`,

\[
\frac{\langle P_au_{a,R}^{+},u_{a,R}^{+}\rangle}{W_a}
\to-\frac{N_R}{2},
\qquad
\frac{\langle P_au_{a,R}^{-},u_{a,R}^{-}\rangle}{W_a}
\to+\frac{N_R}{2}.
\tag{PL340-20}
\]

Rayleigh's principle gives, for every fixed `R`,

\[
\limsup_{a\to\infty}\frac{\inf\sigma(P_a)}{W_a}
\le-\frac{N_R}{2},
\qquad
\liminf_{a\to\infty}\frac{\sup\sigma(P_a)}{W_a}
\ge\frac{N_R}{2}.
\tag{PL340-21}
\]

Since `N_R\uparrow1`, (PL340-8) follows. The lower half of (PL340-9) follows from either spectral edge, while its upper half is exactly the improved norm bound of `PL-339`.

This strengthens the interpretation of `PL-339`: its source-scale negative allowance is not merely an artifact of a coarse lower estimate. Explicit endpoint states actually realize negative prime Rayleigh quotients of asymptotic size arbitrarily close to `W_a/2`.

## 3. Ceiling on the joint positive-jump gap

The identity `J_a=2W_aI-K_a` and the symmetric endpoint state give

\[
\frac{\langle J_au_{a,R}^{+},u_{a,R}^{+}\rangle}{W_a}
\to2-\frac{N_R}{2}.
\tag{PL340-22}
\]

Therefore

\[
\limsup_{a\to\infty}
\frac{\inf\sigma(J_a)}{W_a}
\le2-\frac{N_R}{2}
\tag{PL340-23}
\]

for every `R`, and `R->infinity` gives the upper `3/2` in (PL340-10). The lower `1` is `PL-339`.

At the level of leading scales, the endpoint witness has

\[
W_a\sim2e^a,
\qquad
\langle K_au_{a,R}^{+},u_{a,R}^{+}\rangle\sim N_Re^a,
\tag{PL340-24}
\]

so for large `R`

\[
\langle J_au_{a,R}^{+},u_{a,R}^{+}\rangle\sim3e^a,
\qquad
\langle P_au_{a,R}^{+},u_{a,R}^{+}\rangle\sim-e^a.
\tag{PL340-25}
\]

The many-channel positive jump sector is therefore genuinely large, but its joint coercivity cannot absorb the exact scalar compensation even asymptotically.

## 4. Completion and the correct surviving target

The endpoint family is the same universal PNT boundary mode isolated in `PL-051`. `PL-059` proves that the completed zeta-pole sector has the same normalized boundary limit with the opposite sign. Thus (PL340-8) cannot be used as a completed-Weil negativity certificate: completion canonically removes this first-order fixed-profile mode.

That cancellation makes the route consequence sharper rather than weaker. Further work should not try to improve a source-blind lower bound for `J_a` until it reaches `2W_a`; (PL340-10) proves that target false. A scalable RH-facing mechanism must instead act on the canonically centered pole-minus-prime residual, on the archimedean/form-domain interaction, or on the transported low branch and its source-specific boundary data.

## 5. Adversarial and novelty audit

No Euler product is used or analytically continued. For every finite `a`, the prime operator is the finite von-Mangoldt translation sum already present on the completed explicit-formula side. The large-`a` input is only the PNT boundary model of `PL-051` and the classical asymptotic `W_a\sim2e^a`.

The mechanism is not rational-prime-specific. `PL-051` depends at first order only on a positive weighted outer-shell law converging to `e^{-delta/2}d delta`; a matched Beurling/generalized-prime source with the same shell asymptotic has the same endpoint block and the same constants `1/2` and `3/2`. This is a no-go for universal jump-only positivity, not a new characterization of the rational primes.

A current literature audit around Suzuki's localized Weil operator, prime-power translations, endpoint/boundary scaling, and recent truncated-Weil operator work did not locate an independent theorem strengthening this exact bracket. No novelty is claimed from search absence: (PL340-8)--(PL340-10) are explicit consequences of the already-persisted `PL-051` boundary theorem combined with the later `PL-339` jump decomposition.

Boundary conditions and failure modes:

- The result gives one-sided asymptotic brackets, not exact limits of the spectral edges.
- The endpoint witnesses depend on `a`; they are variational test states, not the tracked low eigenbranch of `PL-338`.
- The zeta-pole cancellation of `PL-059` prevents promotion of the negative prime direction to a completed-Weil negative direction.
- Matched generalized-prime systems with the same shell law reproduce the leading constants.
- High-frequency prime-log recurrence may change operator or essential-norm edges, but cannot erase the explicit Rayleigh values above.

## Consequence for `prime_lattice`

`PL-339` established the lower half of the large-source picture: the positive atomic jump sector does not dilute as prime powers accumulate. The present result establishes the complementary ceiling: **joint jump coercivity cannot become strong enough to neutralize its own scalar compensation.** The prime block retains source-scale two-sided directions before completion, while completion already cancels the universal endpoint component responsible for the displayed witness.

The live target is therefore narrowed to centered, source-specific structure: the residual atomic/archimedean interaction, or branchwise information such as threshold transport and noncollapse of the canonical boundary coefficient. Improving source-blind jump gaps alone cannot close the RH-facing sign problem.

## Dependencies

- `PL-051`: fixed-depth boundary blow-up and universal rank-one PNT Hankel limit with eigenvalues `+/- (1-e^{-R})`.
- `PL-059`: canonical cancellation of that PNT boundary mode by the zeta-pole sector.
- `PL-337`: exact decomposition `P_a=J_a-2W_aI` into positive atomic jumps plus scalar compensation.
- `PL-339`: exact path-chain gaps, `J_a>=(1-o(1))W_aI`, `||P_a||<=(1+o(1))W_a`, and `W_a~2e^a`.
