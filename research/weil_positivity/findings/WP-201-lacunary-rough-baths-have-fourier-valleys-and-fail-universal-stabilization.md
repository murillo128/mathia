# WP-201 — Lacunary rough baths have Fourier valleys and fail universal stabilization

**Status:** `DERIVED + EXACT + HIGHER-ORDER-SPECTRAL-SHIFT + COMMUTING-INFINITE-DIMENSIONAL + LACUNARY-COUNTERCONTROL + SCHATTEN-ROUGHNESS-NOT-SUFFICIENT + FOURIER-VALLEYS + FULL-WEIL-AUTOCORRELATION-CONE + DECISIVE-NARROWING + MATCHED-NONARITHMETIC-CONTROL + PRIOR-ART-AUDITED + NOT-A-WEIL-BRIDGE`.

`WP-198` showed that leaving `S^{4k-1}` while staying in the natural `S^{4k}` class can defeat the finite positive-source zero-mode obstruction. `WP-200` then proved that every power-law centered bath in the strip

\[
\mathcal S^{4k}\setminus\mathcal S^{4k-1}
\]

universally stabilizes every fixed finite positive payload after enough bath copies. That power-law theorem deliberately did not claim that membership in the rough Schatten strip alone is sufficient.

It is not sufficient. For every order

\[
n=4k\ge4,
\tag{1}
\]

there is an explicit bounded centered diagonal bath

\[
H_0=0,
\qquad
V_0\ge0,
\qquad
V_0\in\mathcal S^n\setminus\mathcal S^{n-1},
\tag{2}
\]

whose order-`n` even spectral-shift multiplier is strictly positive at every frequency but has arbitrarily deep high-frequency valleys:

\[
\boxed{
F_0(\xi)>0\quad(\xi\in\mathbb R),
\qquad
\liminf_{\xi\to\infty}\xi F_0(\xi)=0.
}
\tag{3}
\]

Those valleys are enough to defeat universal stabilization. For the one-dimensional positive off-zero payload

\[
H_f=1,
\qquad
V_f=1,
\tag{4}
\]

and every finite bath multiplicity `M`, the direct sum

\[
\widetilde H=0^{\oplus M}\oplus H_f,
\qquad
\widetilde V=V_0^{\oplus M}\oplus V_f
\tag{5}
\]

fails positivity on the full real Weil autocorrelation cone. Thus the sharp power-law threshold of `WP-200` is a **regularity/scale-thickness phenomenon inside that model family**, not a classification by Schatten membership alone.

The actual analytic resource exposed by `WP-200` is a uniform lower envelope of the centered Fourier multiplier. Divergent `(n-1)`st source-jump mass is necessary to leave the `WP-198` bounded-variation no-go in this commuting category, but it does not by itself prevent lacunary singular values from leaving frequencies at which the positive reservoir is asymptotically too weak.

## 1. Two uniform upper bounds for one centered channel

For a centered scalar channel of size `a>0`, `WP-198` gives the exact multiplier

\[
F_a(\xi)
=
\frac1{(n-3)!\,\xi^2}
\int_0^a
(1-\cos(t\xi))(a-t)^{n-3}\,dt
\qquad(\xi\ne0),
\tag{6}
\]

with the continuous value

\[
F_a(0)=\frac{a^n}{n!}.
\tag{7}
\]

The elementary inequalities

\[
1-\cos u\le\frac{u^2}{2},
\qquad
1-\cos u\le2
\tag{8}
\]

give two complementary bounds. First,

\[
\begin{aligned}
F_a(\xi)
&\le
\frac1{2(n-3)!}
\int_0^a t^2(a-t)^{n-3}\,dt\\
&=
\frac{a^n}{n!}.
\end{aligned}
\tag{9}
\]

Second, for `xi!=0`,

\[
\begin{aligned}
F_a(\xi)
&\le
\frac{2}{(n-3)!\,\xi^2}
\int_0^a(a-t)^{n-3}\,dt\\
&=
\frac{2a^{n-2}}{(n-2)!\,\xi^2}.
\end{aligned}
\tag{10}
\]

Hence every centered diagonal bath with singular values `(a_j)` satisfies

\[
\boxed{
F(\xi)
\le
C_n\left[
\frac1{\xi^2}
\sum_{a_j\ge |\xi|^{-1}}a_j^{n-2}
+
\sum_{a_j<|\xi|^{-1}}a_j^n
\right]
}
\tag{11}
\]

for `|xi|>=1`. Compare this with the lower bound in `WP-200`,

\[
F(\xi)
\ge
\frac{c_n}{\xi^2}
\sum_{a_j\ge4/|\xi|}a_j^{n-2}.
\tag{12}
\]

Together, (11)--(12) show why power laws behave regularly: every frequency sees a controlled amount of singular-value mass near its reciprocal scale. A lacunary sequence can instead make both terms in (11) small simultaneously.

## 2. A block-lacunary bath in `S^n` but not `S^{n-1}`

Choose a decreasing sequence

\[
1>s_1>s_2>\cdots\downarrow0
\tag{13}
\]

and assign to scale `s_k` the finite multiplicity

\[
N_k=\left\lceil s_k^{-(n-1)}\right\rceil.
\tag{14}
\]

The bath `V_0` is diagonal with `N_k` copies of `s_k` for each `k`. Every block carries at least unit `(n-1)`st mass:

\[
N_k s_k^{n-1}\ge1,
\tag{15}
\]

so automatically

\[
\sum_kN_k s_k^{n-1}=\infty.
\tag{16}
\]

On the other hand, while `s_k<=1`,

\[
N_k s_k^n
\le s_k+s_k^n
\le2s_k.
\tag{17}
\]

Thus any choice with `sum_k s_k<infinity` gives

\[
V_0\in\mathcal S^n\setminus\mathcal S^{n-1}.
\tag{18}
\]

The remaining freedom in the gaps between successive scales will be used to create Fourier valleys.

## 3. Recursive placement of valleys at a fixed negative payload phase

Set

\[
\varepsilon_k=2^{-k}.
\tag{19}
\]

Suppose `s_1,...,s_k` have been chosen and define the finite coarse-scale moment

\[
A_k
=
\sum_{i\le k}N_i s_i^{n-2}.
\tag{20}
\]

Choose a phase point

\[
X_k=\frac\pi2+2\pi m_k,
\qquad m_k\in\mathbb N,
\tag{21}
\]

so large that, with `r_k=X_k^{-1}`,

\[
r_k<s_k,
\qquad
r_kA_k\le\varepsilon_k.
\tag{22}
\]

This is always possible because the progression in (21) is unbounded and `A_k` is finite.

After choosing `X_k`, choose the next scale so small that

\[
s_{k+1}
\le
\min\left\{
\frac{s_k}{4},
\frac{r_k}{4},
\frac{3}{16}\varepsilon_k r_k
\right\}.
\tag{23}
\]

Continue recursively. The first condition makes `sum s_k<infinity`; hence (18) holds. It also implies that the entire future `n`th-moment tail obeys

\[
\begin{aligned}
B_k
&:=
\sum_{i>k}N_i s_i^n\\
&\le
2\sum_{i>k}s_i\\
&\le
\frac83s_{k+1}\\
&\le
\frac12\varepsilon_k r_k.
\end{aligned}
\tag{24}
\]

The second condition in (23) places every later scale below `r_k`, while (22) places every earlier scale above `r_k`.

## 4. The centered positive multiplier has `o(1/xi)` valleys

Evaluate the bath multiplier at `X_k`. For the blocks `i<=k`, use the large-frequency bound (10); for the blocks `i>k`, use the uniform bound (9). Because `s_i>r_k` for `i<=k` and `s_i<r_k` for `i>k`,

\[
\begin{aligned}
F_0(X_k)
&\le
\frac{2}{(n-2)!X_k^2}
\sum_{i\le k}N_i s_i^{n-2}
+
\frac1{n!}
\sum_{i>k}N_i s_i^n.
\end{aligned}
\tag{25}
\]

Multiplying by `X_k=r_k^{-1}` and applying (22), (24),

\[
\boxed{
X_kF_0(X_k)
\le
\left(\frac{2}{(n-2)!}
+
\frac1{2n!}
\right)\varepsilon_k
\longrightarrow0.
}
\tag{26}
\]

This proves the valley half of (3).

There is no loss of pointwise positivity. Every scalar summand in (6) is strictly positive for `xi!=0`, and every summand has positive value (7) at zero. Moreover (9) and `sum_j a_j^n<infinity` give uniform convergence of the multiplier series. Therefore

\[
F_0\in C(\mathbb R),
\qquad
F_0(\xi)>0
\quad\text{for every }\xi\in\mathbb R.
\tag{27}
\]

So the obstruction is not a sign defect of the bath itself. It is the lack of a **uniform high-frequency positive floor** strong enough to dominate arbitrary finite source oscillation.

## 5. One scalar off-zero source defeats every finite multiplicity

Use the fixed payload (4). Its scalar order-`n` spectral-shift density is

\[
q_f(x)
=
\frac{(2-x)^{n-1}}{(n-1)!}
\mathbf1_{[1,2]}(x).
\tag{28}
\]

As in the source-jump analysis of `WP-198`, its distributional derivative has the positive source jump

\[
J\delta_1,
\qquad
J=\frac1{(n-1)!},
\tag{29}
\]

plus an absolutely continuous `L^1` term. Hence its even Fourier multiplier satisfies

\[
G_f(\xi)
=
-\frac{J\sin\xi}{\xi}
+o(|\xi|^{-1}).
\tag{30}
\]

The valley frequencies were deliberately chosen so that

\[
\sin X_k=1.
\tag{31}
\]

Consequently

\[
X_kG_f(X_k)\longrightarrow-J<0.
\tag{32}
\]

For any fixed finite bath multiplicity `M`, direct-sum additivity gives total multiplier

\[
\widetilde F_M(\xi)
=M F_0(\xi)+G_f(\xi).
\tag{33}
\]

Equations (26) and (32) imply

\[
\boxed{
X_k\widetilde F_M(X_k)
\longrightarrow-J<0.
}
\tag{34}
\]

Thus `widetilde F_M(X_k)<0` for all sufficiently large `k`, independently of how large the fixed finite `M` is. By the exact order-`4k` criterion of `WP-193`, a negative value of the continuous even multiplier yields a real compactly supported smooth autocorrelation on which the Taylor remainder is negative. Therefore no finite number of copies of this bath stabilizes even the scalar payload (4).

This proves

\[
\boxed{
V_0\in\mathcal S^{4k}\setminus\mathcal S^{4k-1}
\quad\not\Longrightarrow\quad
\text{universal finite-payload stabilization.}
}
\tag{35}
\]

## 6. Aggressive falsification and exact scope

**Is the failure caused by leaving the natural higher-order spectral-shift class?** No. Equation (18) places the bath exactly in the natural `S^n` class used by `WP-193`--`WP-200`; only the stronger `S^{n-1}` source-variation condition fails.

**Is the bath itself nonpositive on the Weil cone?** No. Its multiplier is strictly positive at every real frequency by (27), so `WP-193` gives strict positivity on every nonzero real compactly supported smooth autocorrelation. Failure appears only after adding an off-zero source whose `1/xi` oscillation finds the bath's valleys.

**Does divergent `(n-1)`st source-jump mass still matter?** Yes, but only as a category boundary. Finite `(n-1)`st mass activates the almost-periodic zero-mode obstruction of `WP-198`. Infinite mass merely removes that proof; it does not guarantee a stabilizing Fourier floor.

**Does this contradict the power-law theorem of `WP-200`?** No. Power laws are anti-lacunary: their singular values populate every reciprocal scale with controlled truncated `(n-2)`nd mass. The lower bound of `WP-200` then decays no faster than `1/|xi|` throughout the rough power-law strip. The present construction deliberately destroys that scale thickness while preserving the same two Schatten memberships.

**Would allowing bath multiplicity to depend on frequency rescue the sign?** That is not a fixed geometric completion. Universal stabilization in `WP-199`--`WP-200` means one finite direct-sum multiplicity works for the whole cone. Equation (34) excludes every such fixed finite multiplicity.

**Could an infinite multiplicity or a nonseparable/coupled completion behave differently?** Yes. Infinite replication generally changes the Schatten class, and a genuinely coupled infinite source may have a different spectral-shift density. Neither category is ruled out here. Such a construction would need its own finiteness and sign theorem and, for this branch, source-forced arithmetic and archimedean incidence.

## 7. Prior-art and novelty boundary

The higher-order spectral-shift framework itself is classical. Potapov, Skripka, and Sukochev, *Spectral shift function of higher order*, Inventiones Mathematicae **193** (2013), 501--538, DOI `10.1007/s00222-012-0431-2`, proves existence and `L^1` control for `S^n` perturbations. Van Nuland and Skripka's later relative-Schatten and resolvent-comparable results enlarge the perturbation category. Those sources are operator-theoretic infrastructure, not arithmetic input.

A targeted literature audit for higher-order spectral-shift Fourier positivity, lacunary singular-value baths, source-boundary Schatten thresholds, and universal stabilization found the established trace-formula theory and unrelated uses of lacunary constructions in Koplienko-function boundary examples, but no directly matching theorem asserting or classifying the finite-payload stabilization property considered here. No broad external novelty claim is made from that absence.

The durable Mathia claim is the exact internal countercontrol (35): the `S^n\setminus S^{n-1}` condition that is sharp for power-law baths does not control the Fourier lower envelope in general. The proof uses only the explicit centered scalar multiplier already derived in `WP-198`, elementary moment bounds, and a lacunary block construction.

## 8. Consequence for `weil_positivity`

`WP-200` identified critical roughness as a powerful source-blind way to manufacture the sign demanded by the Weil autocorrelation cone. `WP-201` separates **roughness** from **scale thickness**. The first is measured by Schatten membership; the second controls whether the positive bath remains visible at every high frequency.

The relevant hierarchy is now:

\[
\boxed{
\begin{array}{c}
V\in\mathcal S^{4k-1}
\;\Rightarrow\;
\text{off-zero positive sources are obstructed in the commuting class},\\[3pt]
V\in\mathcal S^{4k}\setminus\mathcal S^{4k-1}
\;\Rightarrow\;
\text{the obstruction can fail, but stabilization is not automatic},\\[3pt]
\text{roughness + a uniform reciprocal-scale lower envelope}
\;\Rightarrow\;
\text{source-blind stabilization can occur.}
\end{array}
}
\tag{36}
\]

This is further bad news for interpreting a rough infinite sector as an explanatory Weil geometry. Even after its Schatten threshold is fixed, the desired sign depends on how singular-value mass is distributed across scales. A future Mathia-native candidate must therefore force not only the critical operator ideal but also the scale distribution or coupling that supplies the needed Fourier lower envelope, while simultaneously deriving the finite Mangoldt, Gamma, and polar/global structure. Otherwise the sign remains an adjustable analytic reservoir rather than an arithmetic-geometric theorem.