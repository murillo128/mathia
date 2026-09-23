# FD-297 — A fixed low-height anchor decides the capacity-rigid hard-remainder regime

- **Date:** 2026-09-23
- **Status:** proved an RH/simple-zero anchored rigidity bound reducing every zero-safe low-polynomial hard-remainder cutoff to one fixed low-height baseline
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** complete hard remainder / fixed anchor / zero-safe cutoffs / aggregate complete clusters / path rigidity / remainder-good dichotomy / route sharpening
- **Depends on:** FD-261, FD-267, FD-278, FD-280, FD-290, FD-292, FD-296
- **Classification:** `EXACT-DERIVED + RH-CONDITIONAL + SIMPLE-ZERO + FIXED-ANCHOR-RIGIDITY + HARD-REMAINDER-DICHOTOMY + ROUTE-SHARPENING`

## Claim

FD-296 shows that below the aggregate complete-cluster floor, one buffered remainder-good zero-safe cutoff makes an entire **dyadic** polynomial-height window remainder-good. That leaves the problem phrased dynamically: one still appears to need a first good return in every window to start the rigidity argument.

In fact the same exact-complement identity and aggregate cluster ledger remove that dynamical requirement. Below the same exponent threshold, the whole zero-safe hard-remainder trajectory from one **fixed low-height anchor** up to polynomial height has subcritical diameter. Consequently the near-capacity good/bad status of every zero-safe cutoff in the regime is asymptotically decided by one fixed baseline remainder.

Assume RH and simple nontrivial zeros. Work at fixed polynomial divisor depth

\[
x=N^{\lambda+o(1)},\qquad \lambda>0,
\tag{1}
\]

and put

\[
\beta:=\log_2\frac32,
\qquad
c:=1-\beta,
\qquad
L:=\log(2Nx).
\tag{2}
\]

Fix once and for all a height `T_bullet>0`, independent of `N` and `x`, lying in an open gap between distinct positive nontrivial-zero ordinates and at which the hard Perron decomposition used in FD-280 is defined. Because that gap has fixed positive width while `L^{-1}->0`, `T_bullet` is eventually zero-safe and no FD-276 reciprocal-log component crosses it.

Let

\[
H=x^{\tau+o(1)},
\qquad
0<\tau<\frac12,
\tag{3}
\]

and define

\[
\mathcal S_L([T_\bullet,H])
:=
\left\{T\in[T_\bullet,H]:
\operatorname{dist}(T,\Gamma_*)\ge\frac1L
\right\},
\tag{4}
\]

where `Gamma_*` is the set of distinct positive ordinates of nontrivial zeros.

The background hypothesis must now be global up to `H`, not merely local to one dyadic window. For every maximal FD-276 reciprocal-log component `mathcal C` with

\[
\max_{\rho\in\mathcal C}\Im\rho\le H,
\]

let `mathfrak B_C(L^{-1})` be its desingularized background envelope, and assume

\[
\boxed{
\mathfrak B_{\le H}
:=
\max_{\mathcal C:\,\max\Im\mathcal C\le H}
\max\!\left(1,\mathfrak B_{\mathcal C}(L^{-1})\right)
=
x^{b+o(1)}
}
\tag{5}
\]

for some fixed `b>=0`.

Write the complete physical hard remainder as in FD-280/FD-291,

\[
\mathcal R_{T,N}(d)
:=
\sum_{q\mid d}
\bigl(E_T(Nq)-E_T(N(q-1))\bigr),
\tag{6}
\]

with physical band norm

\[
\|F\|_{1,x}:=
\sum_{x<d\le2x}|F(d)|.
\tag{7}
\]

Define, as in FD-278 and FD-296,

\[
\kappa(\tau,\lambda)
:=
\frac{\tau}
{2\left(1-\dfrac{\tau}{\pi(1+1/\lambda)}\right)}.
\tag{8}
\]

Then uniformly for every eventually zero-safe cutoff

\[
T\in\mathcal S_L([T_\bullet,H]),
\]

we have

\[
\boxed{
\|\mathcal R_{T,N}-\mathcal R_{T_\bullet,N}\|_{1,x}
\le
N^{1/2}
 x^{1+\tau+\kappa(\tau,\lambda)+b+o(1)}.
}
\tag{9}
\]

The FD-261 positive-capacity scale is

\[
\mathcal C_{N,x}
:=
N^{1/2}x^{2-\beta}
=
N^{1/2}x^{1+c}.
\tag{10}
\]

Hence, whenever

\[
\boxed{
\Delta(\tau,\lambda,b)
:=
c-b-\tau-\kappa(\tau,\lambda)>0,
}
\tag{11}
\]

the whole zero-safe path from the fixed anchor to height `H` satisfies

\[
\boxed{
\sup_{T\in\mathcal S_L([T_\bullet,H])}
\|\mathcal R_{T,N}-\mathcal R_{T_\bullet,N}\|_{1,x}
\le
\mathcal C_{N,x}
 x^{-\Delta(\tau,\lambda,b)+o(1)}.
}
\tag{12}
\]

For a near-capacity budget

\[
B_{N,x}:=
\frac{\mathcal C_{N,x}}{\ell(x)},
\qquad
\ell(x)\to\infty,
\qquad
\ell(x)=x^{o(1)},
\tag{13}
\]

equation (12) is `o(B_{N,x})`. The reverse and forward triangle inequalities therefore give the uniform norm comparison

\[
\boxed{
\sup_{T\in\mathcal S_L([T_\bullet,H])}
\left|
\frac{\|\mathcal R_{T,N}\|_{1,x}}{B_{N,x}}
-
\frac{\|\mathcal R_{T_\bullet,N}\|_{1,x}}{B_{N,x}}
\right|
=o(1).
}
\tag{14}
\]

Thus, for every fixed `epsilon>0`:

- if
  \[
  \|\mathcal R_{T_\bullet,N}\|_{1,x}
  \le(1-\varepsilon)B_{N,x},
  \tag{15}
  \]
  then **every** zero-safe cutoff up to `H` is `B_{N,x}`-good for all sufficiently large `x`;

- if
  \[
  \|\mathcal R_{T_\bullet,N}\|_{1,x}
  \ge(1+\varepsilon)B_{N,x},
  \tag{16}
  \]
  then **no** zero-safe cutoff up to `H` is `B_{N,x}`-good for all sufficiently large `x`.

Only the `o(B_{N,x})` transition layer around the budget remains undecided by rigidity alone.

The exact numerical rigidity threshold is unchanged from FD-296. For tame backgrounds `b=0`, it is at least

\[
\tau<0.2683381468698344\ldots
\tag{17}
\]

uniformly in `lambda>0`, and for balanced depth `lambda=1`,

\[
\tau<0.2725714440906720\ldots .
\tag{18}
\]

The new conclusion is not a better exponent. It is that **below this exponent there is no independent low-height first-return problem at all**: moving the hard cutoff cannot change the near-capacity classification away from that of one fixed low-height remainder.

## 1. A fixed anchor is eventually a complete-cluster boundary

Let the fixed anchor lie in a zero gap

\[
\gamma_j<T_\bullet<\gamma_{j+1}
\]

of fixed width. Set

\[
\delta_\bullet
:=
\min(T_\bullet-\gamma_j,\gamma_{j+1}-T_\bullet)>0.
\tag{19}
\]

Since `L->infinity`, eventually `L^{-1}<delta_bullet`. Hence

\[
\operatorname{dist}(T_\bullet,\Gamma_*)\ge\frac1L.
\tag{20}
\]

Moreover the gap containing `T_bullet` then has width at least `2/L`. The FD-276 clustering rule joins consecutive simple critical zeros only across gaps `<2/L`, so no reciprocal-log component crosses the fixed anchor.

The same argument applies to every `T in mathcal S_L([T_bullet,H])`. Therefore the zeros with ordinates in `(T_bullet,T]` are a disjoint union of complete reciprocal-log components. This is the load-bearing reason that the incomplete-boundary singularity of FD-279 never appears.

No cutoff is displaced after selection. In particular the argument does not use the false hard-remainder continuity principle ruled out by FD-280.

## 2. The aggregate packet ledger is not intrinsically dyadic

FD-280 gives the exact identity

\[
\mathcal R_{T,N}-\mathcal R_{T_\bullet,N}
=
-\mathcal G_{(T_\bullet,T],N},
\tag{21}
\]

where the right side is the complete physical image of all zero residues inserted between the two hard cutoffs.

By Section 1 this packet is a union of complete reciprocal-log clusters. Let `R` be the number of such clusters and `m_*` their largest cardinality. Since every included zero has ordinate at most `H=x^{tau+o(1)}`, Riemann--von Mangoldt gives

\[
R\le N_\zeta(H)=x^{\tau+o(1)}.
\tag{22}
\]

The FD-278 reciprocal-log packing estimate gives

\[
m_*
\le
\left(\kappa(\tau,\lambda)+o(1)\right)
\frac{\log x}{\log\log x}.
\tag{23}
\]

For each complete component, the FD-276 divided-difference estimate gives

\[
\sum_{x<d\le2x}
|Q_{\mathcal C}(N,d)|
\ll
x(2L)^{m_{\mathcal C}-1}
\mathfrak B_{\mathcal C}(L^{-1}).
\tag{24}
\]

Using the **global** envelope (5), triangle inequality across components gives

\[
\|\widetilde{\mathcal G}_{(T_\bullet,T],N}\|_{1,x}
\ll
xR(2L)^{m_*-1}\mathfrak B_{\le H}.
\tag{25}
\]

Since

\[
\log(2L)=\log\log x+O(1),
\tag{26}
\]

we obtain

\[
\|\widetilde{\mathcal G}_{(T_\bullet,T],N}\|_{1,x}
\le
x^{1+\tau+\kappa(\tau,\lambda)+b+o(1)}.
\tag{27}
\]

Restoring the common RH critical-line factor `N^(1/2)` proves (9) from (21).

Nothing in this population ledger requires the lower endpoint to be of order `H`. The dyadic formulation in FD-296 was useful for combining with occupation estimates, but the complete-packet estimate itself only pays for the **largest height reached**, the total number of components below it, their maximum reciprocal-log cardinality, and the background envelope. That is why a fixed lower endpoint is admissible once the envelope is strengthened from window-local to global below `H`.

## 3. Rigidity turns the low-height search into a static baseline test

Assume (11). Dividing (12) by (13) gives

\[
\sup_T
\frac{
\|\mathcal R_{T,N}-\mathcal R_{T_\bullet,N}\|_{1,x}
}{B_{N,x}}
\le
\ell(x)x^{-\Delta+o(1)}
=o(1).
\tag{28}
\]

For every norm,

\[
\bigl|\|A\|-\|B\|\bigr|\le\|A-B\|.
\tag{29}
\]

Taking `A=mathcal R_{T,N}` and `B=mathcal R_{T_bullet,N}` yields (14). Equations (15) and (16) then follow immediately from the fixed margin `epsilon`.

This strengthens the logical reduction in FD-296. There is no need to locate one buffered return separately in each dyadic window below the rigidity floor. Either the fixed low-height baseline is already inside the target by a fixed margin, in which case every zero-safe cutoff throughout the entire controlled range inherits goodness, or it is outside by a fixed margin, in which case no movement of the hard cutoff within that range can repair it.

In the good-anchor branch, the zero-safe and phase-good abundance established by FD-290/FD-292 is automatically remainder-good as well throughout the low-height regime. In the bad-anchor branch, those abundant admissible phase heights do not help: the hard remainder remains outside the same near-capacity target ball at all zero-safe cutoffs.

The next analytic target is therefore sharply localized: estimate **one fixed low-height complete hard remainder** `mathcal R_{T_bullet,N}` at the physical band scale. No height-selection or return-frequency theorem is needed before that baseline question is answered.

## 4. The choice of fixed anchor is asymptotically irrelevant at near-capacity scale

The reduction should not depend on a specially tuned constant height. Let `T_bullet` and `T_bullet'` be any two fixed low heights, each lying strictly inside a zero gap. Their difference packet contains only finitely many nontrivial zeros, independent of `x` and `N`.

FD-267 gives for a fixed finite Mellin zero packet the physical band scale

\[
\|\mathcal R_{T_\bullet,N}-\mathcal R_{T_\bullet',N}\|_{1,x}
\le
N^{1/2}x^{1+o(1)}.
\tag{30}
\]

By comparison with the near-capacity budget,

\[
B_{N,x}
=
N^{1/2}x^{1+c-o(1)},
\qquad
c=0.4150374992\ldots,
\tag{31}
\]

so

\[
\frac{
\|\mathcal R_{T_\bullet,N}-\mathcal R_{T_\bullet',N}\|_{1,x}
}{B_{N,x}}
=
x^{-c+o(1)}
\longrightarrow0.
\tag{32}
\]

Hence replacing the fixed anchor by another fixed admissible anchor changes the normalized baseline by only `o(1)`. The good/bad dichotomy with any fixed margin is an asymptotic property of the low-height hard-complement baseline, not an artifact of the chosen fixed gap.

This finite-packet comparison is also why any fixed number of low-lying boundary residues can be absorbed without changing the power-scale conclusion.

## 5. Adversarial checks and limits

The reduction survives the following failure tests.

**Global versus local background control.** FD-296 only needed an envelope for components meeting one dyadic window. A fixed anchor compares across all lower windows, so (5) is deliberately stronger: it controls every complete reciprocal-log component reached below `H`. Without that global hypothesis, (9) is not justified.

**Incomplete boundary clusters.** Equation (9) is asserted only for zero-safe upper cutoffs, and the anchor is eventually zero-safe by (19)--(20). If either endpoint cuts a reciprocal-log cluster, FD-279 shows that inverse-gap singularities can reappear and the complete-component ledger cannot be invoked.

**Bad anchors cannot secretly return.** The second branch of the dichotomy uses the reverse triangle inequality, not a heuristic continuity argument. A capacity-separated bad anchor cannot cross into the target while the total path motion is `o(B_{N,x})`.

**The strict exponent margin is load-bearing.** At `Delta=0` the aggregate packet ledger is only capacity-scale up to subpowers; it no longer implies `o(B_{N,x})`. Nothing here is asserted at or above the rigidity boundary.

**The baseline is not estimated.** The finding removes a dynamical height-selection problem but does not prove that the fixed hard remainder is small or large. That static estimate is the remaining analytic gate.

**No independence is assumed.** The proof uses exact complement identities, deterministic cluster packing, and triangle inequalities. It does not assume random zero phases, independence between phase-good and remainder-good events, or genericity of the fixed anchor.

**Anchor independence is only at the target scale.** Different fixed anchors need not give identical remainders. Equation (32) says only that their difference is negligible relative to a near-capacity budget.

**The statement is conditional.** RH and zero simplicity enter through the FD-278/FD-276 complete-cluster machinery. The background exponent `b` is a genuine hypothesis, and the global version (5) is stronger than the dyadic assumption of FD-296.

**No high-height conclusion is claimed.** Above the aggregate rigidity floor the upper bound no longer prevents capacity-scale hard-remainder motion. This does not prove that such motion occurs; it only restores the genuine return/occupation problem.

## 6. Source and novelty audit

No new external theorem is load-bearing. The argument is a recombination of already persisted ingredients: the exact hard-complement identity of FD-280, the complete reciprocal-log aggregate ledger of FD-278/FD-276, Riemann--von Mangoldt as already used there, the finite-packet physical scaling of FD-267, and the capacity normalization of FD-261. `SOURCES.md` therefore needs no new entry.

No literature novelty claim is made. The contribution is an internal route sharpening: the previously dyadic hard-path rigidity estimate can be anchored at one fixed admissible height once the background envelope is made global below the upper cutoff.

The result is analytic and remains conditional on RH, zero simplicity, and the cluster-background hypothesis. It is not a formalization candidate in its present form.

## Conclusion

Below the FD-278/FD-296 aggregate cluster floor, the complete zero-safe hard remainder has too little total capacity to move by a near-capacity amount **even from one fixed low height all the way to polynomial height**. Consequently low-height cutoff selection is not a search for repeated returns: the entire controlled trajectory inherits its good/bad status from one static baseline up to `o(B_{N,x})`.

For tame backgrounds this applies uniformly at least through `tau<0.268338...`, and through `tau<0.272571...` at balanced depth `lambda=1`. The next decisive problem is therefore not occupation of many hard cutoffs. It is the single-baseline question

\[
\|\mathcal R_{T_\bullet,N}\|_{1,x}
\stackrel{?}{\ll}
\frac{N^{1/2}x^{2-\beta}}{\ell(x)}
\tag{33}
\]

for one fixed admissible `T_bullet`. A positive answer with margin propagates automatically to every zero-safe low-polynomial cutoff in the rigid regime; a negative answer with margin excludes all of them.