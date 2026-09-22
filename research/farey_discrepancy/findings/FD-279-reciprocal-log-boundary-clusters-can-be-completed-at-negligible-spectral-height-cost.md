# FD-279 — Reciprocal-log boundary clusters can be completed at negligible spectral-height cost

- **Date:** 2026-09-22
- **Status:** proved boundary-completion lemma conditional on RH and simple zeros
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** zeta-zero clusters / hard spectral truncation / boundary completion / Riemann--von Mangoldt / argument excursions / grouped spectral repair
- **Depends on:** FD-274, FD-276, FD-277, FD-278
- **Classification:** `EXACT-DERIVED + RH-CONDITIONAL + SIMPLE-ZERO + LOAD-BEARING-S(T)-BOUND + TRUNCATION-BOUNDARY-CLOSURE`

## Claim

FD-278 controls every **complete** reciprocal-log zero component below a finite spectral cutoff, but explicitly leaves open the one component cut by the upper truncation boundary. That proviso is necessary algebraically: if a hard cutoff keeps only part of a close-zero component, the internal reciprocal-gap cancellation of FD-274 can fail for the partial sum. However, in the whole low-polynomial spectral regime relevant to the FD-278 height tariff, the cut component can be completed by moving the cutoff only `O(1/log log x)` in ordinate. Hence it costs no spectral power.

Keep the polynomial-depth regime

\[
x=N^{\lambda+o(1)},\qquad \lambda>0,
\tag{1}
\]

and put

\[
L:=\log(2Nx)
=\left(a+o(1)\right)\log x,
\qquad
a:=1+\frac1\lambda.
\tag{2}
\]

Assume RH and simple nontrivial zeros. As in FD-276--FD-278, join two consecutive critical zeros whenever their ordinate gap is `<2/L`; the connected components are the reciprocal-log clusters.

Let a hard spectral cutoff satisfy

\[
T=x^{\tau+o(1)},
\qquad
0\le \tau<\pi a,
\tag{3}
\]

with `T -> infinity` when `tau=0`. If `T` lies in an exterior gap, all components below `T` are already complete. Otherwise let `C_T` be the unique reciprocal-log component cut by `T`. Then:

\[
\boxed{
|\mathcal C_T|
\le
\left(
\frac{\tau}
{2\left(1-\dfrac{\tau}{\pi a}\right)}
+o(1)
\right)
\frac{\log x}{\log\log x}
}
\tag{4}
\]

for fixed `tau>0`; for `tau=0`,

\[
\boxed{
|\mathcal C_T|
=o\!\left(\frac{\log x}{\log\log x}\right).
}
\tag{5}
\]

Moreover the whole cut component has ordinate diameter

\[
\boxed{
\operatorname{diam}(\mathcal C_T)
=O\!\left(\frac1{\log\log x}\right)
}
\tag{6}
\]

(with `o(1/log log x)` when `tau=0`). Consequently one can choose a new cutoff `T^+>=T`, lying immediately after the upper endpoint of `C_T` and before the next zero, such that

\[
\boxed{
T^+-T
=O\!\left(\frac1{\log\log x}\right),
\qquad
T^+=x^{\tau+o(1)},
}
\tag{7}
\]

and **every reciprocal-log component meeting `[0,T^+]` is complete**.

Thus the incomplete-component loophole in FD-278 is not a new power-scale spectral resource whenever the truncation height is analyst-controlled. At packet level, the hard cutoff may be replaced by a cluster-complete cutoff without changing its spectral-height exponent. What remains to be checked in any full explicit-formula implementation is only the effect of this tiny cutoff displacement on the separate truncation remainder.

## Evidence

### 1. A hard cut really can destroy the FD-274 cancellation

The completion step is not cosmetic. Let

\[
\mathcal C=\{\rho_1,\ldots,\rho_m\}
\]

be a finite cluster of distinct simple zeros and factor locally

\[
\zeta(s)=P_{\mathcal C}(s)H_{\mathcal C}(s),
\qquad
P_{\mathcal C}(s)=\prod_{\rho\in\mathcal C}(s-\rho).
\tag{8}
\]

For a nonempty proper subset `S subsetneq C`, write

\[
P_{\mathcal C}=P_S R_S,
\qquad
R_S(s)=\prod_{\kappa\in\mathcal C\setminus S}(s-\kappa).
\tag{9}
\]

Then for every analytic amplitude `A`, the same barycentric identity used in FD-274 gives

\[
\boxed{
\sum_{\rho\in S}
\frac{A(\rho)}{\zeta'(\rho)}
=
[\rho:\rho\in S]
\left(
\frac{A}{R_S H_{\mathcal C}}
\right).
}
\tag{10}
\]

Indeed, for each included node `rho in S`,

\[
\zeta'(\rho)
=P_S'(\rho)R_S(\rho)H_{\mathcal C}(\rho),
\tag{11}
\]

and `1/P_S'(rho)` is exactly the barycentric coefficient in the divided difference on the included nodes.

For the full cluster `S=C`, `R_S=1` and (10) reduces to FD-274: all internal inverse-gap singularities have been compressed into a regular divided difference of `A/H_C`. For a proper subset, the omitted-factor denominator remains. The two-zero model is sharp. If

\[
\zeta(s)=(s-\rho_-)(s-\rho_+)H(s)
\tag{12}
\]

and the cutoff keeps only `rho_-`, then

\[
\frac{A(\rho_-)}{\zeta'(\rho_-)}
=
\frac{A(\rho_-)}
{(\rho_- -\rho_+)H(\rho_-)},
\tag{13}
\]

which can carry the full inverse-gap factor. Completing the pair instead gives

\[
\frac{A(\rho_-)}{\zeta'(\rho_-)}
+
\frac{A(\rho_+)}{\zeta'(\rho_+)}
=
[\rho_-,\rho_+]
\left(\frac A H\right),
\tag{14}
\]

which tends to a derivative as the two nodes coalesce. Therefore FD-278 was correct not to absorb its cut boundary component into the complete-component estimate.

For the actual divisor-replicated packet,

\[
A_{N,d}(s)
=N^{s-1/2}\frac{K_s(d)}s,
\qquad
K_s(d)=
\sum_{q\mid d}\left(q^s-(q-1)^s\right),
\tag{15}
\]

so (10) applies coordinate by coordinate. FD-275 already controls derivatives of `A_{N,d}` without a power of the spectral frequency; the only new singular object created by a partial cluster is precisely `R_S^{-1}`. This isolates the boundary problem before solving it geometrically below.

### 2. A reciprocal-log component crossing `T` cannot persist for unit spectral distance

Suppose first that the hard cutoff actually cuts a component. Let `gamma_0` be the last zero ordinate at or below `T`, and suppose for contradiction that the same component extends beyond `T+1`. Choose the first zero `gamma_m>T+1` in that component. Because every consecutive gap inside the component is `<2/L`,

\[
\gamma_0>T-\frac2L,
\qquad
\gamma_m<T+1+\frac2L,
\tag{16}
\]

and spanning unit distance with gaps `<2/L` forces

\[
m+1\ge \frac L2-O(1)
=\left(\frac a2+o(1)\right)\log x.
\tag{17}
\]

On the other hand, apply Riemann--von Mangoldt between points immediately outside `gamma_0` and `gamma_m`. The interval has length `1+O(1/L)` and upper height

\[
U=T+2=x^{\tau+o(1)}.
\tag{18}
\]

Its smooth zero-count contribution is

\[
\left(\frac{\tau}{2\pi}+o(1)\right)\log x.
\tag{19}
\]

Under RH, Carneiro--Chandee--Milinovich give

\[
|S(t)|
\le
\left(\frac14+o(1)\right)
\frac{\log t}{\log\log t},
\tag{20}
\]

so the endpoint error in this unit interval is only `O(log x/log log x)`. Hence

\[
m+1
\le
\left(\frac{\tau}{2\pi}+o(1)\right)
\log x.
\tag{21}
\]

Because `tau<pi a`, the leading coefficient in (21) is strictly smaller than the `a/2` forced by (17), a contradiction for large `x`.

The same argument downward shows that a component cut at `T` cannot extend below `T-1`. Thus the whole boundary component lies in

\[
[T-1-o(1),\,T+1+o(1)].
\tag{22}
\]

This bootstrap is useful because it justifies using `T+O(1)` as a uniform height for the sharper cardinality estimate; no assumption that the component was complete was needed.

### 3. The cut component obeys the same cardinality ceiling as complete components

Let

\[
\gamma_1<\cdots<\gamma_m
\]

be all ordinates of `C_T`. Since each internal gap is `<2/L`, its span `h` satisfies

\[
h=\gamma_m-\gamma_1
<\frac{2(m-1)}L.
\tag{23}
\]

Choose zero-free endpoints immediately outside `gamma_1` and `gamma_m`. Riemann--von Mangoldt gives

\[
m
\le
\frac{h}{2\pi}\log(2U)
+|S(t_+)|+|S(t_-)|+O(1),
\tag{24}
\]

with `U=T+2`. Using (23), (20),

\[
\log U=(\tau+o(1))\log x,
\qquad
L=(a+o(1))\log x,
\tag{25}
\]

we obtain

\[
m\left(
1-rac{\tau}{\pi a}+o(1)
\right)
\le
\left(\frac\tau2+o(1)\right)
\frac{\log x}{\log\log x}.
\tag{26}
\]

For fixed `0<tau<pi a`, division by the positive parenthesis proves (4). If `tau=0`, both the smooth density term and the RH `S(t)` budget are `o(log x/log log x)`, which gives (5).

This is numerically the same cardinality ceiling that appears in FD-278 for complete components, but its logical role is different: (26) needs only a run of reciprocal-log-connected zeros. Completeness and an exterior collar are not required.

### 4. Cardinality converts directly into negligible completion distance

Equation (23) together with (4) gives

\[
h
\ll
\frac1{\log\log x},
\tag{27}
\]

and (5) gives the corresponding little-`o` statement when `tau=0`. Since `T` lies inside this same component, the distance from `T` to its upper endpoint is at most `h+O(1/L)`.

Choose `T^+` just above `gamma_m` but strictly before the next zero; for instance use any positive displacement smaller than both the exterior gap and `L^{-2}`. Then

\[
0\le T^+-T
\le h+O(L^{-1}),
\tag{28}
\]

which proves (7). By construction the component formerly cut by `T` is now complete, and every earlier component was already complete. Because an additive `O(1/log log x)` shift is negligible relative to any `x^{tau+o(1)}` height, the spectral power exponent is unchanged.

No estimate for `1/zeta'(rho)` is used in this completion step. Close gaps may make the hard-cut partial packet individually large through (13), but the geometry plus zero-counting shows that all missing partners can be restored before the truncation height moves by a power-visible amount.

## Stress tests

The first stress test is the exact close pair. Let the cutoff pass between two zeros separated by `delta<<1/L`. Equation (13) can be of size `1/delta`; there is no uniform full-cluster background bound for that one-sided residue. Yet completing the component moves the cutoff by at most `delta+o(1/L)`, after which (14) restores the FD-274 cancellation. This verifies that the theorem removes a genuine hard-truncation artifact rather than assuming it away.

The second stress test is a long boundary component. The proof does not assume bounded cluster size. Equation (26) permits size as large as a constant times `log x/log log x`, exactly the growing regime retained by FD-276--FD-278. Even then its total spectral diameter is only `O(1/log log x)` because the connectivity scale itself is `1/log x`.

The third stress test is the height boundary `tau=pi a`. The argument intentionally stops there. When `tau` approaches `pi a`, the smooth expected zero density on an interval of reciprocal-log connected length can consume the whole cardinality budget and the denominator in (4) degenerates. This is consistent with FD-278, which also only needs the nondegenerate range `tau<pi a` for its low-height obstruction. No claim is made that reciprocal-log components remain short at arbitrarily high spectral height for fixed `x`.

The fourth stress test is a fixed or subpolynomial cutoff. If `tau=0` but `T->infinity`, the RH `S(t)` bound is `o(log x/log log x)` because `log T=o(log x)`, giving (5). If `T` remains bounded, only finitely many zeros are involved and the completion statement is trivially stronger than the asymptotic bound.

The fifth stress test is the explicit-formula remainder. The theorem is a statement about the finite zero packet and the geometry of its truncation. Moving from `T` to `T^+` changes which zero residues are included and can also change a separately derived explicit-formula remainder. No stability estimate for that remainder is smuggled into (7). A full Mertens explicit-formula implementation must re-audit that term at the cluster-complete cutoff.

## Prior-art check

The barycentric divided-difference identity, Riemann--von Mangoldt formula, and the interpretation of `S(t)` as the zero-counting error are classical. The RH-conditional sharp estimate

\[
|S(t)|\le(1/4+o(1))\log t/\log\log t
\]

is the Carneiro--Chandee--Milinovich theorem already anchored in `SOURCES.md` and already load-bearing for FD-277--FD-278.

A fresh search checked hard versus smoothed zero truncations, close-zero packets, partial residue sums, and divided-difference formulations. It found the standard explicit-formula/smoothing literature and the classical interpolation algebra, but no result coupling a reciprocal-log connected zero component to the FD-274 grouped consecutive-difference/divisor-replication packet and proving the power-neutral completion statement (7). No new external theorem is load-bearing here, so `SOURCES.md` does not need another anchor.

## Implications

FD-278 left the finite-packet spectral route with four qualitatively different escapes: higher spectral height, polynomially ill-conditioned desingularized backgrounds, the one incomplete component cut by the truncation boundary, and non-packet effects such as the explicit-formula remainder or multiple/off-critical zeros.

FD-279 removes the third escape **at packet power scale** throughout `tau<pi(1+1/lambda)`. The partial boundary packet can indeed be violently ill-conditioned, but that ill-conditioning is not intrinsic to the completed spectral object: all omitted members of the component lie only `O(1/log log x)` farther in ordinate. An analyst may therefore complete the component while retaining exactly the same spectral exponent `tau`.

In particular, the tame-background aggregate floor of FD-278 is not weakened by an adversarial hard cutoff placed inside a tiny gap. If one works with cluster-complete truncations, every included close-zero component is covered by the FD-276--FD-278 ledgers, with no leftover boundary component at the same power scale.

The natural next test is now the **remainder stability problem**: for the explicit Mertens packet actually used in FD-267--FD-273, prove that replacing `T` by the cluster-completed `T^+=T+O(1/log log x)` does not create a threshold-sized change in the nonzero remainder. If that succeeds, the hard-truncation branch is closed not only for the finite packet but for the full explicit-formula repair.

## Limitations

The zero-count completion estimate assumes RH and uses simple zeros, consistently with FD-276--FD-278. The geometric zero-count argument itself could be reformulated with multiplicities, but the grouped residue packet would then require the confluent analysis already left open in FD-274.

The theorem requires a fixed polynomial-height exponent `tau<pi(1+1/lambda)`. It makes no statement in the degenerate high-height regime at or beyond that boundary, where the reciprocal-log threshold can be comparable with or larger than typical zero spacing.

Finally, (7) is not by itself a theorem about the total explicit formula. It proves that the **finite zero-packet boundary** can be regularized at negligible spectral-height cost. The remainder, contour terms, and any source-specific dependence on the exact cutoff must still be transported across that displacement before one can claim a full source-side obstruction.
