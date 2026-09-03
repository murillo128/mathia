# WI-121 — Fujii number variance rules out positive-density long critical-screening islands

**Status:** `LITERATURE+DERIVED` + `EXACT-DERIVED` + `STRUCTURAL-RIGIDITY` + `PRIOR-ART-REDIRECT`. Fujii's unconditional short-interval moment theorem is classical literature. The line-specific deduction below applies it to the exact critical-lattice screening configurations from WI-005/WI-006. It does **not** prove a new numerical simple-critical proportion and does **not** rule out every possible screened exceptional configuration.

## 1. Claim

The exact long screening model that makes the support-one Weil/Gabor form blind to horizontal displacement in WI-005 cannot occur with positive zero-density for the actual zeta zero set.

Write

\[
L=\log T,\qquad h=\frac{2\pi}{L}.
\]

Let `K=K(T)` be an integer tending to infinity sufficiently slowly, with `K=o(L)`, and put

\[
\Delta=Kh=\frac{2\pi K}{L}.
\]

Call a **K-site critical-screening island** an interval containing the ordinates

\[
u,\ u+h,\ \ldots,\ u+(K-1)h
\]

with at least two zeta zeros, counted with multiplicity, at each listed ordinate. This includes either an off-critical functional-equation mirror pair at an ordinate or a critical-line multiple/double zero, exactly the ordinate-multiplicity pattern behind the critical-lattice screening alias in WI-005 and WI-006.

For every fixed integer `k>=1`, any pairwise interval-disjoint family of such islands contained away from the endpoints of `[T,2T]` has

\[
\boxed{
\frac{\#\{\text{specified screening zeros in the islands}\}}
{N(2T)-N(T)}
\ll_k
\frac{(\log K)^k}{K^{2k}}
}
\]

along any sufficiently slow choice of `K(T)` for which Fujii's asymptotic applies. In particular the right-hand side tends to zero. Thus a positive proportion of zeta zeros cannot be carried by longer and longer exact double-density critical-lattice screening islands.

The `k=1` case already gives the qualitative conclusion:

\[
\frac{\#\{\text{screening zeros in such islands}\}}{N(2T)-N(T)}
\ll \frac{\log K}{K^2}=o(1).
\]

## 2. Classical input: Fujii's unconditional mesoscopic moments

Let

\[
S(t)=\frac1\pi\arg\zeta\!\left(\frac12+it\right)
\]

with the standard Riemann--von Mangoldt convention. Fujii proved unconditionally, for every fixed integer `k>=1`, that for `0<Delta\ll1`,

\[
\int_0^T
\bigl[S(t+\Delta)-S(t)\bigr]^{2k}\,dt
=
\frac{(2k)!}{(2\pi)^{2k}k!}\,T
\bigl(2\log(2+\Delta\log T)\bigr)^k
+
O_k\!\left(
T\bigl(\log(2+\Delta\log T)\bigr)^{k-1/2}
\right).
\]

A modern restatement is equation (1.8) of Lugar--Milinovich--Quesada-Herrera, who explicitly note that this is unconditional and gives an asymptotic when `Delta log T -> infinity` sufficiently slowly.

For

\[
\Delta=\frac{2\pi K}{L},
\qquad K\to\infty
\]

sufficiently slowly, this yields the upper bound

\[
\int_T^{2T}
|S(t+\Delta)-S(t)|^{2k}\,dt
\ll_k T(\log K)^k.
\]

No Riemann hypothesis, pair-correlation conjecture, or support extension is used here.

## 3. Mesoscopic overcrowding is rare

The Riemann--von Mangoldt formula gives, uniformly for `t in [T,2T]`,

\[
N(t+\Delta)-N(t)
=
\frac{\Delta}{2\pi}\log\frac{t}{2\pi}
+
S(t+\Delta)-S(t)
+o(K).
\]

Since `Delta L/(2pi)=K` and `log(t/(2pi))=L+O(1)`, the smooth term is

\[
K+o(K).
\]

Fix `eta>0` and define

\[
E_{K,\eta}
=
\left\{
t\in[T,2T]:
N(t+\Delta)-N(t)\ge(1+\eta)K
\right\}.
\]

For large `T`, every `t in E_{K,eta}` satisfies

\[
S(t+\Delta)-S(t)\ge \frac{\eta K}{2}.
\]

Markov's inequality and Fujii's `2k`-th moment therefore give

\[
\boxed{
|E_{K,\eta}|
\ll_{k,\eta}
T\frac{(\log K)^k}{K^{2k}}.
}
\]

This is the arithmetic input missing from the coarse-count stress test in WI-005: long order-one excess density at the mean-spacing scale can occur only on a vanishing set of starting heights once the window contains `K -> infinity` mean spacings.

## 4. Exact screening islands force overcrowding on a whole interval of starts

Consider one K-site screening island beginning at `u`. For every

\[
t\in J_u:=\left[u-\frac{\Delta}{4},u+\frac{\Delta}{4}\right],
\]

the interval `[t,t+Delta]` contains at least

\[
\frac{3K}{4}-O(1)
\]

of the island's lattice sites. Because each such site carries at least two zeros counted with multiplicity,

\[
N(t+\Delta)-N(t)
\ge
\frac{3K}{2}-O(1).
\]

Hence, for example, for all sufficiently large `K`,

\[
J_u\subset E_{K,1/3}.
\]

The interval `J_u` has length `Delta/2`. If the original K-site islands are interval-disjoint, then their starting ordinates are separated by at least `(K-1)h`; for large `K` this exceeds `Delta/2`, so the corresponding `J_u` are also disjoint.

If `B` is the number of islands, the overcrowding estimate gives

\[
B\frac{\Delta}{2}
\le |E_{K,1/3}|
\ll_k T\frac{(\log K)^k}{K^{2k}}.
\]

Using `Delta=2pi K/L`,

\[
B
\ll_k
TL\frac{(\log K)^k}{K^{2k+1}}.
\]

There are `2K` specified screening zeros per exact double-density island, so

\[
2KB
\ll_k
TL\frac{(\log K)^k}{K^{2k}}.
\]

Finally `N(2T)-N(T)\asymp TL`, which proves the claimed density bound.

Endpoint conventions for `N(t)` affect only a measure-zero set of starts and do not change the argument.

## 5. Consequence for the WI-005 sharpness model

WI-005 correctly shows an **abstract matrix obstruction**: on an exact critical lattice, an off-line mirror pair and a critical-line double have the same aggregated support-one Gabor/Weil response, and long finite screening blocks lose only boundary-sized mass. That algebraic counterexample remains valid.

What changes is its status as a candidate positive-density extremizer for the actual zeta zeros. A long exact critical-screening block contains many disjoint K-site sub-islands for every sufficiently slow `K=o(L)`. If such long double-density blocks carried a positive proportion of all zeros, then the preceding estimate would produce a positive proportion of zeros in disjoint K-site screening islands, contradicting the `o(1)` density bound.

Thus coarse Riemann--von Mangoldt counting was genuinely too weak for this question, but the classical short-interval variance/moment theory is already strong enough to exclude the canonical long screening background.

This is a **rigidity statement about the exceptional complement**, not a claim that the complement is off-critical. The same ordinate overcrowding applies whether the multiplicity two comes from off-line mirror pairs, critical-line doubles, or a mixture.

## 6. Consequence for WI-120 and the remaining gate

WI-120 showed that moving edge profiles can reactivate a finite-block horizontal signal, while warning that a much longer surrounding exact screening lattice might cancel that local leakage. The present finding materially narrows that obstruction: such a long exact double-density screening background cannot recur with positive zero-density in the zeta zero set.

This does **not** yet turn WI-120 into a defect-to-zero bootstrap. The missing coercive statement is now sharper:

> prove that cancellation of a positive density of moving-edge local horizontal signals forces either mesoscopic ordinate overcrowding of the Fujii-controlled type or another quantitatively controlled zeta statistic.

If that dichotomy can be proved, the first branch is already negligible by the present argument. Without such a bridge, irregular sparse screening patterns, bounded-size clusters, near-line depth effects, ordinary-zero-assisted cancellation, or other cross-height geometries remain possible.

## 7. Stress tests and boundaries

The argument deliberately uses only the ordinate count and therefore cannot distinguish doubles on the critical line from off-line mirror pairs. That is a feature here: both are members of the uncertified complement and both generate the same double-density overcrowding.

The result also does not forbid isolated long islands. It proves a density statement. Nor does it say that every matrix configuration exhibiting support-one screening must resemble the exact critical lattice. WI-005/WI-006 remain valid no-go results for inference from the collapsed support-one form alone.

The choice `K -> infinity` is essential. Fujii's 1975 estimate does not give an asymptotic at bounded `Delta log T`, so this finding does not remove fixed-size microscopic screening clusters. Conversely, no support beyond one is being smuggled into the Weil-form argument: Fujii's theorem is an independent arithmetic theorem about the actual zero-count process, used only to falsify a proposed extremal zero configuration.

## 8. Prior-art audit and provenance

Primary source:

- Akio Fujii, **On the distribution of the zeros of the Riemann zeta function in short intervals**, *Bulletin of the American Mathematical Society* 81 (1975), 139--142, DOI `10.1090/S0002-9904-1975-13674-3`. Role: unconditional `2k`-th moments of `S(t+Delta)-S(t)` in short intervals.

Modern theorem-level restatement and range discussion:

- Meghann Moriah Lugar, Micah B. Milinovich and Emily Quesada-Herrera, **On the number variance of zeta zeros and a conjecture of Berry**, *Mathematika* 69 (2023), 303--348, DOI `10.1112/mtk.12184`, arXiv:2211.14918. Equation (1.8) restates Fujii's unconditional moment formula and explicitly records the sufficiently-slow `Delta log T -> infinity` asymptotic regime.

The audit also checked literature around zeta zeros in short intervals, gap/multiplicity estimates, and number variance. Those subjects are classical; this finding does not claim priority for the general overcrowding consequence of a moment bound. The durable Mathia contribution is the explicit application to the critical-lattice screening extremizers already isolated in WI-005/WI-006, and the resulting removal of one concrete positive-density cancellation model from the WI-120 frontier.

## 9. Research implication

The support-one screening alias is still exact algebraically, but **its canonical long-lattice extremizer is arithmetically inadmissible at positive density** for zeta. This is the first unconditional mechanism in this line that rules out a substantial family of the long screening configurations previously left alive by coarse zero counting.

The next useful target is not another refinement of the same variance estimate. It is the extraction lemma described above: turn sustained cancellation of the WI-120 moving-edge signal into a forced mesoscopic count excess or another already-controlled statistic. A successful coercive bridge would convert this structural rigidity into a genuine bootstrap on exceptional mass.