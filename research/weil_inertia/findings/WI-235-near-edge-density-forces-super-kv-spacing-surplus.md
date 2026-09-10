# WI-235 — near-edge density forces a super-KV spacing-surplus tariff

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + DECISIVE-BOUNDARY`.

WI-232 identifies a genuine escape from density-matched bow screening: if the selected symmetrized bow opens its spacing from the local Riemann--von Mangoldt value by a relative surplus `epsilon_T`, the same vertical interval acquires `O(epsilon_T m + log T)` additional zero labels. WI-234 leaves this as an explicit live escape after Bellotti's near-edge zero-density theorem closes the exactly density-matched amplitude budget.

The escape is much more rigid than that formulation suggests. Keep WI-233's selected first-harmonic amplitude

\[
A_T:=\frac1m\sum_{j=1}^m\cosh a_j^{\rm sel}\ge1,
\]

put

\[
S(T):=\frac{(\log T)^{1/3}}{(\log\log T)^{1/3}},
\qquad
A_0:=\frac1{48.0718},
\]

and suppose a same-interval complementary zero population cancels the selected first reciprocal harmonic to `o(m)` error. In the near-density-matched regime

\[
\Delta_{\varepsilon}
=\frac{4\pi}{\ell_0}(1+\varepsilon_T),
\qquad
\ell_0=\log\frac{T_0}{2\pi},
\qquad
\varepsilon_T=o(1),
\]

with `m=T^{vartheta+o(1)}` and fixed `0<vartheta<1/2`, Bellotti's theorem implies the following alternative. If

\[
\frac{mA_T}
{T^{1/4}\exp[-(A_0/2+o(1))S(T)]}
\longrightarrow\infty,
\tag{1}
\]

then

\[
\boxed{
\frac1{S(T)}
\log\!\left(
\frac{(\varepsilon_T+(\log T)/m)T^{1/4}}{A_T}
\right)
\longrightarrow+\infty.
}
\tag{2}
\]

Thus once the selected amplitude is too large to be carried by Bellotti's bounded near-edge population, the spacing/count escape cannot be an arbitrarily small perturbation. It must beat **every fixed Korobov--Vinogradov subexponential correction** to the natural power threshold.

A useful fixed-depth consequence is immediate. If fixed `q>0` and `delta_0>0` satisfy

\[
\#\left\{j:\beta_j-\frac12\ge\delta_0\right\}\ge qm,
\tag{3}
\]

and

\[
m=T^{\vartheta+o(1)},
\qquad
\vartheta>\frac14-\frac{\delta_0}{2},
\tag{4}
\]

then every such local screen forces, for **every fixed** `C>0`,

\[
\boxed{
\frac{\varepsilon_T}
{T^{-(1/4-\delta_0/2)}\exp(CS(T))}
\longrightarrow\infty.
}
\tag{5}
\]

For the `beta=3/4` depth appearing on the Maynard--Pratt schematic bow plateau, `delta_0=1/4`. Whenever a fixed positive fraction of a bow of exponent `vartheta>1/8` lies at that depth, same-interval screening therefore requires

\[
\boxed{
\varepsilon_T T^{1/8}\exp[-CS(T)]\longrightarrow\infty
\quad\text{for every fixed }C>0.
}
\tag{6}
\]

In particular a surplus of size at most `T^{-1/8} exp(C S(T))` for any one fixed `C` cannot rescue that local screen. This does not rule out a genuinely larger power-scale or fixed spacing surplus, remote vertical screening, or distinguished source-side cancellation.

## 1. Exact near-density local count budget

Use the same interval as WI-232 but retain the spacing surplus:

\[
I=(T_0,T_0+m\Delta_\varepsilon],
\qquad
\Delta_\varepsilon=\frac{4\pi}{\ell_0}(1+\varepsilon_T).
\tag{7}
\]

The selected population consists of `m` distinct right-half-plane off-line labels and their `m` compulsory same-ordinate functional-equation mirrors. WI-232's Taylor expansion of the Riemann--von Mangoldt main term gives

\[
N(I)-2m
=2\varepsilon_Tm
+O\!\left(
\log T+\frac{m^2(1+\varepsilon_T)^2}{T\ell_0^2}
\right).
\tag{8}
\]

For `epsilon_T=o(1)` and `m=T^{vartheta+o(1)}`, `vartheta<1/2`, the Taylor remainder is `o(1)`. Hence every complementary label in the same interval, counting critical zeros, off-line mirrors, and multiplicity, fits into

\[
\boxed{
R=O(\varepsilon_Tm+\log T).
}
\tag{9}
\]

This is a count upper bound, not a claim that all available labels have the phase or radial position needed to screen the bow.

## 2. Bellotti converts the count reservoir into an amplitude reservoir

Fix any constant `A>A_0`. Bellotti's published near-edge theorem states that

\[
N(\sigma,T)=O_A(1)
\]

uniformly for

\[
\sigma\ge
1-A(\log T)^{-2/3}(\log\log T)^{-1/3}.
\tag{10}
\]

The zero-free edge with constant `A_0` bounds the first-harmonic modulus of every off-line mirror pair by

\[
E_0(T):=
T^{1/4}\exp[-(A_0/2+o(1))S(T)].
\tag{11}
\]

Among the complementary labels, only `O_A(1)` can lie deeper than the threshold (10). All remaining labels have first-harmonic modulus at most

\[
E_A(T):=
T^{1/4}\exp[-(A/2+o(1))S(T)].
\tag{12}
\]

Critical-line labels contribute modulus one and are harmless in this estimate because `E_A(T)\to\infty`. Triangle inequality therefore gives the spacing-sensitive version of WI-234's density-matched capacity law:

\[
\boxed{
|S_1^{\rm comp}|
\ll_A E_0(T)+R E_A(T).
}
\tag{13}
\]

No distributional assumption on the `R` shallow labels has been used; (13) deliberately gives every one of them its maximal allowed radial modulus and perfect phase alignment.

## 3. Arbitrary fixed Bellotti depth forces the super-KV tariff

WI-233 gives the exact selected first-harmonic amplitude

\[
B_1=2mA_T.
\tag{14}
\]

Cancellation to error `eta m`, `eta=o(1)`, forces

\[
|S_1^{\rm comp}|
\ge m(2A_T-\eta)
\ge mA_T
\tag{15}
\]

for large `T`. Combining (9), (13), and (15), for every fixed `A>A_0`,

\[
mA_T
\ll_A
E_0(T)+(\varepsilon_Tm+\log T)E_A(T).
\tag{16}
\]

Assume (1). Then the first term on the right of (16) is `o(mA_T)`. Absorbing it gives

\[
\varepsilon_T+\frac{\log T}{m}
\gg_A
A_T T^{-1/4}
\exp[(A/2+o(1))S(T)].
\tag{17}
\]

Consequently

\[
\liminf_{T\to\infty}
\frac1{S(T)}
\log\!\left(
\frac{(\varepsilon_T+(\log T)/m)T^{1/4}}{A_T}
\right)
\ge\frac A2.
\tag{18}
\]

The important point is Bellotti's quantifier: (10) holds for **every fixed** `A>A_0`. Since `A` in (18) can be chosen arbitrarily large before sending `T` to infinity, the liminf is `+infinity`, which proves (2). Dependence of the implied constant on `A` is harmless because `A` is fixed for each application and `S(T)\to\infty`.

This is the mathematical delta beyond merely inserting `R=O(epsilon_T m+log T)` into WI-233's deepest-zero tariff. A single zero-free edge would give only one fixed exponential correction. Bellotti's bounded-count theorem can be applied at every fixed deeper threshold, and the surviving shallow population must therefore move outward in count by more than every fixed `exp(C S(T))` correction.

## 4. Positive-density selected depth isolates the spacing surplus

Under (3), WI-233 gives

\[
A_T
\ge\frac q2\exp\!\left(\frac{\delta_0\ell_0}{2}\right)
=T^{\delta_0/2+o(1)}.
\tag{19}
\]

If (4) holds, then

\[
\frac{mA_T}{E_0(T)}
\ge
T^{\vartheta+\delta_0/2-1/4+o(1)}
\exp[(A_0/2+o(1))S(T)]
\longrightarrow\infty,
\tag{20}
\]

so hypothesis (1) is automatic. Also

\[
\frac{\log T}{m}
=T^{-\vartheta+o(1)}
=o\!\left(
T^{-(1/4-\delta_0/2)}\exp(CS(T))
\right)
\tag{21}
\]

for every fixed `C`, because the inequality in (4) is strict. Equation (2), or directly (17) with an `A` chosen larger than `2C`, therefore leaves the spacing surplus itself as the only possible local count reservoir and proves (5).

At the power level, (5) has a sharp interpretation. Any surplus `epsilon_T=T^{-kappa+o(1)}` with `kappa>1/4-delta_0/2` is impossible. At the boundary `kappa=1/4-delta_0/2`, a polynomial or logarithmic correction is still insufficient: the surplus must contain a factor larger than `exp(CS(T))` for every fixed `C`. The theorem does not exclude boundary surpluses with still larger `T^{o(1)}` factors, nor any surplus with a strictly larger power-scale reservoir.

## 5. Prior art and novelty audit

The external analytic inputs are exactly those already anchored for WI-232--WI-234:

- Chiara Bellotti, **A new zero-density estimate for $\zeta(s)$ and the error term in the prime number theorem**, *Bulletin of the London Mathematical Society* 58 (2026), no. 7, Paper e70442; arXiv:2508.02041. Theorem 1.2 supplies `N(sigma,T)=O_A(1)` for every fixed `A>A_0` at (10).
- Chiara Bellotti, **Explicit bounds for the Riemann zeta function and a new zero-free region**, *Journal of Mathematical Analysis and Applications* 536:2 (2024), 128249; arXiv:2306.10680. This supplies the current asymptotic zero-free constant `A_0=1/48.0718` used in (11).
- Elchin Hasanalizade, Quanli Shen and Peng-Jie Wong, **Counting zeros of the Riemann zeta function**, *Journal of Number Theory* 235 (2022), 219--241. The local Riemann--von Mangoldt error underlying (8) is inherited from WI-232.
- James Maynard and Kyle Pratt, **Half-Isolated Zeros and Zero-Density Estimates**, *IMRN* 2024:19 (2024), 12978--13014. Their Section 8 bow is the adversarial geometry being stress-tested, not a source for (2) or (5).

Within `weil_inertia`, WI-232 already proves the surplus count ledger (8)--(9), WI-233 proves the selected amplitude `mA_T`, and WI-234 proves the Bellotti capacity barrier only after specializing to density matching, where `R=O(log T)`. The new claim is the three-way conjunction with `epsilon_T` retained: the shallow screen has size `O(epsilon_T m+log T)`, while Bellotti allows only boundedly many labels at each fixed near-edge depth. The arbitrary fixed-`A` quantifier then forces the super-KV law (2), and (5) quantifies exactly how large the spacing-surplus escape must be for a selected positive-depth population.

A bounded external search around Bellotti near-edge density, Maynard--Pratt bows, spacing surplus, reciprocal-harmonic screening, and local Riemann--von Mangoldt budgets located the sources above but no published statement of (2), (5), or an equivalent local spacing-surplus tariff. Absence of a search hit is not evidence of priority, and no priority claim is made.

## 6. Boundaries, falsification test, and research consequence

The same-interval hypothesis is load-bearing. Remote zero populations can contribute to the global explicit-formula amplitude without being charged to (9), and distinguished prime/source-side cancellation remains the separate open problem isolated by WI-195--WI-208. Equation (2) therefore does not rule out zeta bows globally and is not an RH proof.

The positive-depth corollary also needs the strict exponent condition (4). If `vartheta+delta_0/2<1/4`, Bellotti's bounded deepest population is already large enough in principle to carry the selected first-harmonic target, so the argument cannot force a spacing reservoir. At the exact equality, subpower factors decide whether (1) holds and no unconditional simplification is claimed.

The result can be falsified by checking four interfaces:

1. WI-232 equation (31) must give the near-density excess count (8), including multiplicity, with negligible Taylor remainder in the stated range.
2. Bellotti Theorem 1.2 must hold for every fixed `A>A_0`; this quantifier, not merely one chosen threshold, is essential for passing from (18) to (2).
3. The deep/shallow split must give (13), with only `O_A(1)` labels allowed to use the zero-free-edge amplitude `E_0` and all remaining labels bounded by `E_A`.
4. WI-233's selected amplitude must be exactly `2mA_T`, so `o(m)` cancellation implies (15).

If these interfaces hold, the spacing-surplus tariff is exact. Its research consequence is a stricter version of the main local escape left by WI-234: **a positive but microscopic spacing surplus is not enough. Once selected amplitude outruns the bounded near-edge screen, local screening requires a count surplus above the natural power threshold by more than every fixed Korobov--Vinogradov subexponential factor.** The remaining ways out are correspondingly narrower: a genuinely larger spacing reservoir, vertical nonlocality, source-side cancellation, or failure of a positive-density selected radial population to form.