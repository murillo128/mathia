# NB-141 — Selberg density makes polynomial confluence cells rare but not forbidden

**Status:** `DERIVED + SOURCE-SPECIFIC + SELBERG-ZERO-DENSITY + TWO-DIMENSIONAL-CONFLUENCE-CELLS + HEIGHT-MEASURE-RARITY + SPARSE-MATCHED-CONTROL + TARGET-AWARE + NEGATIVE/WORST-CELL-BOUNDARY`.

`NB-140` isolates a sharp local obstruction: for fixed horizontal displacement `a>0`, a pairwise-distinct simple packet of rank `d_G ~ c log G` contained in a sufficiently small two-dimensional polynomial cell converges to the same target-poor confluent state space as the one-zero jet. The current source question is therefore not whether such a packet is numerically ill-conditioned, but whether the actual zeta divisor can place logarithmically many relevant right-half zeros in one forbidden cell.

The near-critical Selberg zero-density estimate already used in `NB-116` gives a genuine source-specific gain, but it is an **average-height gain rather than a worst-cell exclusion**. Fix

\[
0<a<\frac12,
\qquad c>0,
\qquad \Delta_G\le \frac a2,
\tag{1}
\]

and, for `t in [G,2G]`, let

\[
\mathcal C_G(t)
:=
\left\{
\rho=\beta+i\gamma:
\zeta(\rho)=0,
\left|\beta-\left(\frac12+a\right)\right|\le \Delta_G,
\ |\gamma-t|\le \Delta_G
\right\},
\tag{2}
\]

with zeros counted with multiplicity. Put

\[
m_G(t):=\#\mathcal C_G(t),
\qquad
d_G:=\lfloor c\log G\rfloor,
\tag{3}
\]

and define the set of logarithmically crowded centers

\[
\mathcal E_G
:=
\{t\in[G,2G]:m_G(t)\ge d_G\}.
\tag{4}
\]

Then Selberg density implies

\[
\boxed{
|\mathcal E_G|
\ll_{a,c}
\Delta_G\,G^{1-a/8}.
}
\tag{5}
\]

Consequently, for the polynomial cells relevant to `NB-140`,

\[
\Delta_G=G^{-B},
\tag{6}
\]

one has

\[
\boxed{
\frac{|\mathcal E_G|}{G}
\ll_{a,c}
G^{-B-a/8}
\longrightarrow0.
}
\tag{7}
\]

Thus a uniformly random height in `[G,2G]` is overwhelmingly unlikely, in Lebesgue measure, to center a cell containing `Theta(log G)` right-half zeros at fixed horizontal displacement. The same conclusion holds for a disjoint `Delta_G`-grid: the proportion of grid cells that can contain `d_G` such zeros is `O_{a,c}(G^{-B-a/8})`.

This is a real strengthening of the source picture after `NB-140`, but it does **not** provide the theorem the target argument needs. A sparse sequence of exceptional cells can survive every estimate above. More strongly, for any fixed

\[
0<c<0.05038
\tag{8}
\]

and any

\[
B>c\log\!\left(\frac4a-3\right),
\tag{9}
\]

there is a simple zeta-symmetric synthetic divisor satisfying the explicit Riemann--von Mangoldt error envelope used in `NB-112`--`NB-140`, the Selberg global zero-density envelope used in `NB-116`, and the fixed-height Vinogradov--Korobov zero-free envelope, while containing infinitely many right-half packets of `floor(c log G_k)` points inside cells of radius `G_k^{-B}`. By `NB-140`, each selected packet has vanishing normalized Nyman-target projection.

Hence

\[
\boxed{
\text{global zero density}
+\text{ explicit zero count}
+\text{ zero-free region}
\not\Rightarrow
\text{uniform }o(\log G)\text{ occupancy of polynomial cells}.
}
\tag{10}
\]

The live source discriminator remains genuinely local: a worst-cell upper bound, or a theorem coupling the actual local zero packet directly to target-bearing Nyman geometry.

## 1. Selberg density gives an average occupancy bound for the forbidden cells

Because `Delta_G<=a/2`, every zero in `(2)` satisfies

\[
\beta
\ge
\frac12+\frac a2.
\tag{11}
\]

Let

\[
N_>(\sigma,T)
:=
\#\{\rho=\beta+i\gamma:\zeta(\rho)=0,
\ 0<\gamma\le T,
\ \beta>\sigma\},
\tag{12}
\]

again with multiplicity. The Selberg estimate anchored in `SOURCES.md` and already used in `NB-116` is

\[
N_>(\sigma,T)
\ll
T^{1-\frac14(\sigma-1/2)}\log T
\tag{13}
\]

uniformly on the fixed near-critical strip needed here. At

\[
\sigma_a:=\frac12+\frac a2
\tag{14}
\]

this becomes

\[
\boxed{
N_>(\sigma_a,T)
\ll_a
T^{1-a/8}\log T.
}
\tag{15}
\]

Now integrate the local occupancy over the possible cell centers. Every zero that can contribute to `m_G(t)` for some `t in [G,2G]` has ordinate in

\[
[G-\Delta_G,2G+\Delta_G]\subset(0,3G]
\tag{16}
\]

for all sufficiently large `G`. A fixed zero contributes only for centers

\[
t\in[\gamma-\Delta_G,\gamma+\Delta_G],
\tag{17}
\]

an interval of length at most `2 Delta_G`. Tonelli therefore gives the exact counting inequality

\[
\begin{aligned}
\int_G^{2G}m_G(t)\,dt
&\le
2\Delta_G\,
N_>(\sigma_a,3G)\\
&\ll_a
\Delta_G\,G^{1-a/8}\log G.
\end{aligned}
\tag{18}
\]

For large `G`,

\[
d_G\ge \frac c2\log G.
\tag{19}
\]

On `mathcal E_G`, the integrand is at least `d_G`, so Markov's inequality and `(18)` give

\[
\begin{aligned}
|\mathcal E_G|
&\le
\frac1{d_G}
\int_G^{2G}m_G(t)\,dt\\
&\ll_{a,c}
\Delta_G\,G^{1-a/8},
\end{aligned}
\tag{20}
\]

which proves `(5)`.

The cancellation of the logarithm in `(20)` is the useful feature. The global Selberg count supplies `G^(1-a/8) log G` possible right-half zeros, while an `NB-140` obstruction consumes `Theta(log G)` of them in one cell. The number or total center-measure of such cells therefore loses the `log G` factor.

A companion statement holds for disjoint cells. Let `t_1,...,t_J in [G,2G]` satisfy

\[
|t_j-t_k|>2\Delta_G
\qquad(j\ne k),
\tag{21}
\]

and suppose every cell `C_G(t_j)` contains at least `d_G` zeros. Their vertical windows are disjoint, so

\[
Jd_G
\le
N_>(\sigma_a,3G).
\tag{22}
\]

Hence

\[
\boxed{
J\ll_{a,c}G^{1-a/8}.
}
\tag{23}
\]

A maximal disjoint `Delta_G`-grid in `[G,2G]` has `asymp G/Delta_G` cells, so the fraction that can be logarithmically crowded is

\[
\ll_{a,c}
\Delta_G G^{-a/8}.
\tag{24}
\]

For `Delta_G=G^{-B}`, this is exactly the power saving in `(7)`.

## 2. Splicing the rarity estimate with `NB-140`

Retain the `NB-140` state parameters

\[
D_a=\frac4a-3,
\qquad
0<c<\frac18,
\qquad
d_G=\lfloor c\log G\rfloor.
\tag{25}
\]

Its target-aware confluence theorem says that if

\[
\Delta_G\,
G^{c\log D_a}
(\log G)^{25/2}
\longrightarrow0,
\tag{26}
\]

then every pairwise-distinct simple packet of `d_G` nodes inside the complex displacement disk of radius `Delta_G` has

\[
\frac{\|P_{\mathcal S_G^{\rm split}}e_G\|}
     {\|e_G\|}
\longrightarrow0.
\tag{27}
\]

For a polynomial radius `Delta_G=G^{-B}`, it is enough that

\[
B>c\log D_a.
\tag{28}
\]

Combining `(5)` and `(27)` produces a clean source/geometry separation:

* the **state theorem** says what happens if a logarithmic packet occupies one sufficiently small cell — the entire packet span is target-poor;
* the **Selberg theorem** says such heavily occupied cells occupy a vanishing fraction of height space;
* neither statement says that the exceptional set is empty.

The distinction matters because the present Nyman route is a worst-source argument. If the actual zeta divisor contains even one suitable cell along an unbounded sequence of heights, the fact that almost every nearby center is clean does not convert the packet into a target-bearing state. An average-height theorem and a uniform local occupancy theorem are not interchangeable.

There is also no contradiction when `B` is large enough that the absolute measure in `(5)` tends to zero. A single packet occupies only an `O(Delta_G)` interval of possible centers, whereas the upper bound `(5)` is larger by the factor `G^(1-a/8)`. Vanishing total measure therefore still leaves room for isolated exceptional cells.

## 3. A sparse logarithmic-rank matched control survives all current coarse source laws

The previous point can be made source-faithful rather than merely logical. Fix

\[
0<c<0.05038=\frac{0.10076}{2}
\tag{29}
\]

and choose `B` satisfying `(9)`. Select heights `G_k -> infinity` so rapidly that

\[
\sum_{j<k}\log G_j=o(\log G_k).
\tag{30}
\]

For example one may take

\[
G_k=\exp(\exp(k^2)).
\tag{31}
\]

At height `G_k`, place

\[
d_k:=\lfloor c\log G_k\rfloor
\tag{32}
\]

pairwise-distinct simple right-half points inside

\[
\left|\rho-\left(\frac12+a+iG_k\right)\right|
\le G_k^{-B},
\tag{33}
\]

and add their reflections across the critical line and their complex conjugates. The positive-ordinate contribution of the `k`th completed packet is `2d_k`: `d_k` right-half points and `d_k` left-half partners at the same approximate height.

To supply the bulk zero count, take a simple critical-line baseline with ordinates `tau_n` satisfying

\[
M(\tau_n)=n,
\qquad
M(T)=\frac{T}{2\pi}\log\frac{T}{2\pi e},
\tag{34}
\]

for all sufficiently large `n`, and include the negative conjugates. After finite initial adjustment its positive-ordinate counting function is

\[
N_0(T)=M(T)+O(1).
\tag{35}
\]

The sparse packets alter this by at most

\[
2\sum_{G_k\le T}d_k
\le
(2c+o(1))\log T
\tag{36}
\]

because of `(30)`. Since

\[
2c<0.10076,
\tag{37}
\]

the full synthetic counting function obeys, for all sufficiently large `T`, the explicit Bellotti--Wong envelope already used in this line,

\[
\left|N_{\rm syn}(T)-M(T)\right|
\le
0.10076\log T
+0.24460\log\log T
+O(1).
\tag{38}
\]

The construction also respects the Selberg global density envelope. For

\[
\sigma_a=\frac12+\frac a2,
\tag{39}
\]

the only synthetic zeros to the right of `sigma_a` are the sparse right-half packet points, so

\[
N_{>,\rm syn}(\sigma_a,T)
\ll
\sum_{G_k\le T}\log G_k
=O(\log T),
\tag{40}
\]

which is far below

\[
T^{1-a/8}\log T.
\tag{41}
\]

The fixed horizontal position `1/2+a` also lies eventually to the left of the Vinogradov--Korobov zero-free boundary near `1`, so that source law does not remove the packets. All inserted points are simple and pairwise distinct. In fact the baseline and packets may all be chosen simple, and the proportion of synthetic zeros on the critical line tends to one because the off-critical count is only `O(log T)` against a total `asymp T log T`.

Finally, `(9)` puts every selected packet inside the `NB-140` confluence regime. Therefore

\[
\boxed{
\frac{\|P_{\mathcal S_{G_k}^{\rm split}}e_{G_k}\|}
     {\|e_{G_k}\|}
\longrightarrow0
}
\tag{42}
\]

along the exceptional heights.

This is a matched-control construction, not a claim about the actual zeta divisor. The synthetic set is not asserted to come from an Euler product, the zeta explicit formula, or an entire function with the full analytic structure of `xi`. Its purpose is exactly to identify what the currently imported source laws do and do not encode. They encode strong global rarity, but no worst-cell exclusion.

The coefficient `0.05038` in `(29)` is not proposed as an intrinsic zeta threshold. It is only the convenient value that lets the simplest `N_0+packets` construction fit directly under the one-sided `0.10076 log T` explicit counting error. `NB-140` already shows local compatibility up to every `c<0.10076`. Any positive fixed `c` is enough for the present information test: the current laws do not imply `o(log G)` occupancy.

## 4. What stronger global zero-density theorems can and cannot change

The derivation is better stated abstractly. Suppose a source law gives, at the horizontal threshold relevant to a cell,

\[
N_>(\sigma_a,T)
\ll
T^{1-\delta_a}L(T),
\qquad \delta_a>0.
\tag{43}
\]

The same Tonelli/Markov argument gives

\[
\boxed{
\frac{|\mathcal E_G|}{G}
\ll
\Delta_G\,
G^{-\delta_a}
\frac{L(G)}{\log G}.
}
\tag{44}
\]

A better global density exponent therefore makes the bad-cell set rarer. It does not, by itself, make it empty. This remains true even if the global exceptional population is dramatically smaller than the known Selberg bound: one can concentrate a logarithmic number of points at very sparse heights while keeping the cumulative population negligible on the global scale.

This is the precise sense in which the live theorem after `NB-140` is **local rather than merely density-theoretic**. To force

\[
\sup_{t\in[G,2G]}m_G(t)=o(\log G)
\tag{45}
\]

one needs information that controls the supremum, or another structural theorem that makes a crowded cell target-bearing. An estimate for the integral or average of `m_G(t)` cannot supply `(45)` without an additional anti-concentration input.

The conclusion is also stronger than a statement about multiplicity. The packets in the matched control are simple. Bounds on the order of one zero, including `NB-112`, do not constrain how many distinct simple zeros may occupy one tiny two-dimensional cell.

## 5. Representation and information audit

The observable in this finding is the **local source occupancy required to activate the target-poor state theorem**, not a raw condition number. The relevant coordinates are:

- horizontal displacement `a`, because zero density strengthens as the cell moves away from the critical line;
- cell radius `Delta_G`, because it controls both the confluence theorem and the amount of height-center measure charged by one zero;
- logarithmic occupancy `d_G`, because `NB-140` needs a growing packet while the global density budget is itself much larger;
- worst-cell versus averaged occupancy, because this distinction is exactly where the source information is lost.

The kill test is to replace the zeta source by a formal population obeying every coarse law used in the argument. Section 3 passes that test while retaining the target-poor packet. Therefore `(5)` must not be promoted into a uniform local theorem.

Conversely, the rarity estimate is not vacuous bookkeeping. The raw Riemann--von Mangoldt count would give only

\[
N(3G)=O(G\log G),
\tag{46}
\]

which inserted into `(18)` would yield at best

\[
\frac{|\mathcal E_G|}{G}
\ll
\Delta_G,
\tag{47}
\]

with no horizontal saving. Selberg supplies the additional factor

\[
G^{-a/8}.
\tag{48}
\]

Thus actual zeta zero-density information does quantitatively thin the set of dangerous centers; it simply does not thin it to zero cardinality.

## 6. Prior-art boundary

The load-bearing external theorem is Selberg's near-critical zero-density estimate in the explicit uniform form of Aleksander Simonič, already anchored in `SOURCES.md` for `NB-116`. No new source anchor is required. The Tonelli/Markov conversion `(18)`--`(20)` and its splice with the `NB-140` target-poor confluence theorem are derived here.

Recent work does not change the logical boundary. Guth and Maynard's improved global zero-density estimates sharpen exponents in parts of the critical strip, but they remain global counts of zeros to the right of a line; in the abstract formula `(44)` they improve `delta_a` without controlling the supremum in `(45)`. Biao Wang's September 2026 paper *Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals* gives lower bounds for simple/distinct critical zeros in short intervals, not a deterministic upper bound on the number of off-critical zeros in a polynomially shrinking two-dimensional cell. The matched packets above are already simple and distinct.

`NB-099` is the closest line-local negative precedent: it showed that fixed three-state collective-shear pathologies can be translated to sparse heights while respecting global zero-count information. The present result is not another fixed-rank sparsification. The packet rank now grows as `Theta(log G)`, the cells shrink polynomially in both strip coordinates, the endpoint is the representation-invariant target angle from `NB-140`, and Selberg density gives the explicit rarity exponent `B+a/8`. The new boundary is therefore specific to the current logarithmic-rank target-poor confluence mechanism.

No novelty is claimed for Selberg density, Markov's inequality, or the general principle that global density need not control a supremum. The line-local contribution is the quantitative bridge showing exactly how much the best imported near-critical density law suppresses the newly isolated `NB-140` cells, together with a source-faithful sparse control proving that the suppression is still insufficient for worst-cell coercivity.

## 7. Consequence for the research line

The source frontier can now be stated more sharply. `NB-140` showed that arbitrary two-dimensional logarithmic packets in sufficiently small polynomial cells are target-poor. `NB-141` shows that Selberg density makes such cells **power-law rare in height measure**:

\[
\Pr_{t\sim\mathrm{Unif}[G,2G]}
\bigl[m_G(t)\ge c\log G\bigr]
\ll
G^{-B-a/8}.
\tag{49}
\]

But the same current source laws remain compatible with infinitely many sparse exceptional cells, even with simple zeros and an asymptotically density-one critical-line background. Therefore an average-density improvement, by itself, is not the missing theorem.

The next useful source input must do one of two genuinely stronger things: prove a **uniform local upper bound** `m_G(t)=o(log G)` in every forbidden polynomial cell, or prove that an actual crowded packet necessarily occupies a target-bearing Nyman direction despite the generic confluence barrier. Anything that only improves the measure or global frequency of bad cells leaves the worst-cell escape open.