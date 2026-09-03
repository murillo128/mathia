# ANF-001 — fixed-σ zero-energy bounds lose asymptotic force at the screening scale

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + DECISIVE-NEGATIVE` for attempts to use the currently tabulated zero-additive-energy exponents directly as the missing anti-screening input at horizontal depth `O(1/log T)`.

## 1. Current zero-energy input

For a multiset `W` of ordinates, let

\[
E_1(W)
:=\#\{(t_1,t_2,t_3,t_4)\in W^4:
|t_1+t_2-t_3-t_4|\le1\}.
\]

Tao--Trudgian--Yang's current ANTEDB formulation writes `N^*(σ,T)` for the additive energy of ordinates of zeta zeros with real part at least `σ` and `|Im ρ|<=T`, and defines `A^*(σ)` for **fixed** `σ` by

\[
N^*(\sigma-\delta,T)
\ll T^{A^*(\sigma)(1-\sigma)+o(1)}.
\tag{1}
\]

In the range closest to the critical line, `1/2 <= σ <= 2/3`, the current best tabulated unconditional bound remains Heath-Brown's 1979 estimate

\[
A^*(\sigma)
\le
\frac{10-11\sigma}{(2-\sigma)(1-\sigma)}.
\tag{2}
\]

The 2026 Tao--Trudgian--Yang improvements to zero additive energy begin at `σ=7/10`; they materially sharpen deeper fixed-`σ` regimes but do not replace (2) near `1/2`.

Primary sources:

- D. R. Heath-Brown, **Zero Density Estimates for the Riemann Zeta-Function and Dirichlet L-Functions**, *J. London Math. Soc.* (2) 19 (1979), 221--232.
- T. Tao, T. Trudgian and A. Yang, **New exponent pairs, zero density estimates, and zero additive energy estimates: a systematic approach**, arXiv:2501.16779, current manuscript dated 24 August 2026, together with the living ANTEDB zero-density-energy table.

No novelty is claimed for (1), (2), or the newer fixed-`σ` energy estimates.

## 2. Exact degeneration of the near-line exponent

Write

\[
\sigma=\frac12+x,
\qquad 0\le x\le\frac16.
\]

Multiplying (2) by `1-σ`, the exponent of `T` in (1) is bounded by

\[
B(x)
:=\frac{10-11\sigma}{2-\sigma}
=\frac{\frac92-11x}{\frac32-x}.
\tag{3}
\]

The trivial cubic-energy scale is `T^{3+o(1)}` because the Riemann--von Mangoldt formula gives `O(T log T)=T^{1+o(1)}` zeros and `E_1(W)<=|W|^3`. Relative to that trivial exponent, (3) has the exact gap

\[
\boxed{
3-B(x)=\frac{8x}{\frac32-x}.
}
\tag{4}
\]

Thus the available power saving vanishes linearly as `σ` approaches `1/2`. At `σ=1/2`, (2) gives exactly the trivial cubic exponent `3`.

This algebraic identity is the first boundary relevant to Mathia: the current energy theorem becomes asymptotically non-discriminating precisely as one approaches the critical line.

## 3. The `1/log T` diagnostic gives only a constant-factor saving

The natural horizontal coordinate in the compressed-Weil work is

\[
Y_\rho
:=|\beta-\tfrac12|L_T,
\qquad
L_T:=\log(T/2\pi).
\tag{5}
\]

To test what (2) could possibly say at fixed normalized depth, formally put

\[
x=\frac{a}{L_T}
\tag{6}
\]

for fixed `a>0`. This substitution is **not itself licensed by (1)**, whose quantifiers hold `σ` fixed; it is only a scale diagnostic. Equations (3)--(4) then give

\[
B(a/L_T)
=3-
\frac{8a/L_T}{\frac32-a/L_T}
=3-\frac{16a}{3L_T}+O_a(L_T^{-2}).
\tag{7}
\]

Consequently, even under a hypothetical uniform version allowing the moving `σ` in (6), the corresponding bound would have only

\[
T^{B(a/L_T)}
=
T^3\exp\!\left(-\frac{16a}{3}+o_a(1)\right).
\tag{8}
\]

For fixed bounded `a`, this is a constant-factor reduction of the cubic scale, not an `o(T^3)` saving. Letting `a` grow can suppress the deep horizontal tail, but that is not the unresolved regime described below.

The actual fixed-`σ` theorem is weaker for this purpose than the diagnostic (8), because it supplies no stated uniformity as `σ-1/2` shrinks like `1/log T`.

## 4. Why this misses the live horizontal obstruction

`WI-029` combines Jutila's published near-line zero-density theorem with the `weil_inertia` screening construction. It shows that if a positive-density off-line population exists, then after discarding an arbitrarily small deep tail it has a positive-density core at bounded normalized depth

\[
0<Y_\rho\le A
\tag{9}
\]

for some fixed `A`. The same finding records that this bounded-`Y` regime is exactly where the current single-scale compressed Weil operator admits the long-block double-zero/off-line screening model.

Zero additive energy is qualitatively richer than scalar zero counts because it constrains four-term relations among ordinates. It is therefore a natural candidate for the missing vertical information. But the current fixed-`σ` energy exponents do not yet supply that candidate at the required scale:

1. `A^*(σ)` is formulated for fixed `σ`, whereas every threshold resolving bounded `Y` has `σ=1/2+O(1/log T)`;
2. the best near-line exponent reaches the trivial cubic scale continuously at `σ=1/2` by (4);
3. even the optimistic moving-`σ` diagnostic (8) yields only a fixed multiplicative saving for fixed normalized depth;
4. the 2026 improvements in the current ANTEDB table begin at `σ=7/10`, far outside the bounded-`Y` region for large `T`.

Therefore the new additive-energy technology is not, **as currently stated**, a direct anti-screening theorem for the bounded-depth exceptional population.

## 5. The missing theorem has a sharper target than “improve `A^*(σ)`”

This identifies a more precise analytic frontier. A useful input for the bounded-depth problem must retain nontrivial force when the horizontal threshold moves with `T`. For example, one would need a theorem uniform for

\[
\sigma_T=\frac12+\frac{a}{\log T}
\tag{10}
\]

that gives a genuinely asymptotic restriction on the additive structure of the associated ordinates, rather than merely a fixed factor below the maximal cubic energy scale.

Even `N^*(\sigma_T,T)=o(T^3)` would be only a first coarse separator; the screening adversary is a statement about highly organized vertical configurations, so the more useful target is a normalized energy/correlation estimate relative to the actual number of relevant zeros that excludes long near-lattice blocks or another explicit screening control. A bandwise estimate for `a_0<Y<=a_1` would also be more directly aligned with the obstruction than a cumulative fixed-`σ` exponent.

This target is materially different from optimizing the existing fixed-`σ` table. It asks for **near-critical uniformity on the microscopic horizontal scale**.

## 6. Prior-art and novelty audit

The additive-energy definition, Heath-Brown bound, Tao--Trudgian--Yang improvements, and their ANTEDB optimization framework are literature results. The exact identity (4) is elementary algebra applied to Heath-Brown's bound.

The Mathia-specific contribution is the scale comparison with `WI-029`: the currently available zero-energy exponent gains collapse when transported to the `Y=O(1)` horizontal scale singled out independently by zero density plus Weil screening. A bounded search found no source making this exact cross-scale comparison; no priority claim is made from absence of a search hit.

This finding does **not** say additive energy is irrelevant to RH, that no stronger uniform theorem exists in unpublished work, or that a different correlation statistic cannot break screening. It says only that the current fixed-`σ` `A^*` technology, including the 2026 improvements, cannot be cited as though it already controls the bounded-depth population.

## 7. Decisive falsification / upgrade test

This obstruction should be withdrawn or materially revised if an authoritative source supplies either of the following:

- a zero-additive-energy estimate uniform for `σ=1/2+a/log T` over fixed bounded `a` with a saving that is asymptotically stronger than the cubic baseline in the relevant normalized formulation; or
- a bandwise/local correlation theorem at bounded `Y` that directly forbids the long near-lattice organization used by the screening model.

Absent such an input, future `analytic_frontier` work should not spend effort optimizing fixed-`σ` `A^*` constants as a route to the `weil_inertia` shallow-core problem. The research target is the missing **uniform near-line energy/correlation theorem**, not a better deep-strip exponent.