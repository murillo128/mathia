# RE-092 — paired anchored-gap budgets are noncoercive at the host-moment frontier

**Status:** `EXACT-DERIVED + NEGATIVE/INFORMATION-CLASS-OBSTRUCTION + PAIRED-FIRST/HOST-LAYER-GAPS + SECOND-MOMENT-SHARPNESS + RE-091-FRONTIER-CALIBRATION + PRIOR-ART-AUDITED`.

`RE-091` turns sparse depth-`r` support-boundary hosts plus the complete second moment of ordinary prime gaps into the general physical-mass exponent

\[
\beta_r=
\frac12\left(\frac{123}{100}+\frac1r\right).
\tag{1}
\]

For `r=3` this is `469/600`; for `r=2` it is `173/200`. The live frontier after `RE-091` suggests an apparently stronger input from `RE-086`: once a selected cell has a first-layer boundary on one side and a depth-`r` boundary on the other, the **same cell** forces two anchored ordinary-prime gaps, one at scale `X` and one at the host base-prime scale `X^(1/r)`. Perhaps paying both gap costs simultaneously could improve (1).

At the level of gap magnitudes and separate prime-gap moment information, it cannot. There is a full-width matched control in which the first-layer gap burden saturates exactly the `RE-091` host/moment exponent while the depth-`r` anchored gap requirement tends to zero and is therefore automatically satisfied by every sufficiently large ordinary-prime gap. For the two depths relevant to the current frontier, `r=2,3`, this control is also compatible with the currently anchored large-gap theorems: throughout its admissible range the required first-layer gaps stay below the `x^0.45` threshold where Järviniemi's stronger aggregate estimate begins.

The result is an information-class sharpness statement, not an existence theorem for a genuine CA fan. It shows that adding the **second anchored-gap magnitude on the same cell** to the scalar package used by `RE-091` does not buy a better exponent. Any improvement must use information discarded by that package: the exact cross-scale incidence `eta_1(p)` versus `eta_r(q)`, which host primes actually occur as adjacent support boundaries, rightmost-maximizer compatibility, or another correlation between the two prime-gap locations.

Fix `r in {2,3}`, a threshold mass `L>0`, and a scale exponent `b in (0,1/2)`. Let `X` be a large physical scale. The number of possible depth-`r` prime hosts in a fixed bounded-ratio physical shell is

\[
N_r(X)\asymp_r \frac{X^{1/r}}{\log X},
\tag{2}
\]

by the prime number theorem and the fixed-layer event asymptotic

\[
\eta_r(q)=\frac{q^r}{r}\left(1+O_r((\log q)^{-1})\right).
\tag{3}
\]

Distribute total threshold width `L` evenly over `N_r(X)` abstract mixed `1/r` cells,

\[
w_X:=\frac{L}{N_r(X)}
\asymp_r L\,X^{-1/r}\log X,
\tag{4}
\]

and give every cell the false-RH-sized amplitude

\[
a_X:=X^{-b}.
\tag{5}
\]

This is compatible with the uniform small-height law because `a_X log X -> 0`, and it matches the polynomial amplitude floor used in the compact-fan elimination arguments.

For a first-layer boundary prime `p\asymp X`, `RE-086` forces the chamber-facing ordinary gap to satisfy

\[
d_1
\gg a_X w_X p\log p.
\tag{6}
\]

For the opposite depth-`r` boundary prime `q\asymp_r X^{1/r}`, the same cell simultaneously forces

\[
d_r
\gg a_X w_X q\log q.
\tag{7}
\]

For the matched control, choose the first-layer gap at the smallest admissible order in (6). Equations (2)--(5) then give

\[
\boxed{
d_1^{\rm ctrl}
\asymp_r
X^{1-b-1/r}(\log X)^2.
}
\tag{8}
\]

The lower bound required by the host-layer inequality (7) is only

\[
\boxed{
d_r^{\rm req}
\asymp_r
X^{-b}(\log X)^2
\longrightarrow0.
}
\tag{9}
\]

Thus, in the equal-width full-host regime, the anchored gap at the **host layer itself is asymptotically slack**. Every gap between sufficiently large consecutive primes has length at least `2`, so (7) eventually imposes no additional restriction on which depth-`r` host primes may be paired with the cells. The only nontrivial scalar gap burden is the first-layer one in (8).

## 1. The second-moment cost reproduces the `RE-091` exponent exactly

The control gaps in (8) contribute square mass

\[
\begin{aligned}
N_r(X)(d_1^{\rm ctrl})^2
&\asymp_r
\frac{X^{1/r}}{\log X}
X^{2-2b-2/r}(\log X)^4\\
&=
\boxed{
X^{2-2b-1/r}(\log X)^3.
}
\end{aligned}
\tag{10}
\]

Stadlmann's load-bearing theorem used in `RE-091` is

\[
\sum_{p_n\le x}(p_{n+1}-p_n)^2
\ll_\varepsilon x^{123/100+\varepsilon}.
\tag{11}
\]

Consequently the matched control is compatible, at exponent level with all fixed logarithmic powers absorbed into `X^epsilon`, precisely when

\[
2-2b-\frac1r
\le \frac{123}{100},
\tag{12}
\]

or equivalently

\[
\boxed{
b\ge b_r^*:=1-\beta_r,
\qquad
\beta_r=
\frac12\left(\frac{123}{100}+\frac1r\right).
}
\tag{13}
\]

This is exactly the complement of the sufficient elimination frontier in `RE-091`. Cauchy--Schwarz there was therefore not losing an exponent inside this scalar information class: equal allocation over the whole sparse host family produces the matching obstruction.

The control also respects the first-moment geometry. Its total exceptional first-layer gap length is

\[
N_r(X)d_1^{\rm ctrl}
\asymp_r
X^{1-b}\log X=o(X),
\tag{14}
\]

for every fixed `b>0`. Hence these exceptional gaps occupy only a vanishing fraction of a bounded-ratio shell and can be embedded in a PNT-scale abstract prime mesh while the remaining gaps carry the ordinary `log X` average spacing. Likewise the total physical width of the corresponding support chambers is `O(X^{1-b}\log X)=o(X)`, so disjoint placement is not itself an obstruction.

At the host scale `Q\asymp_r X^{1/r}`, equation (9) is eventually below the deterministic lower bound `2` for gaps between odd primes. Thus enforcing the paired host-layer inequality contributes no extra selected-gap condition beyond the ordinary prime sequence itself; the complete second-moment theorem at scale `Q` remains compatible automatically.

This is the promised strengthening of `RE-087`. That finding showed that **marginal** anchored-gap capacities diverge when each layer is summed separately. Here the two anchored inequalities are imposed **cell by cell on the same abstract mixed `1/r` family**, together with the same second-moment budget that powers `RE-091`. The paired magnitude constraints still admit fixed total threshold width.

## 2. Depth three: `469/600` is sharp for the current scalar package

For `r=3`,

\[
\boxed{
\beta_3=\frac{469}{600},
\qquad
b_3^*=\frac{131}{600}.
}
\tag{15}
\]

At the critical control scale, the required first-layer gaps have exponent

\[
1-b_3^*-\frac13
=\frac{269}{600}
=0.448333\ldots .
\tag{16}
\]

This provides a useful prior-art calibration. Järviniemi's stronger aggregate large-gap theorem begins at gap length `x^0.45`; the critical `RE-091` control lies just below it:

\[
\frac{269}{600}
=\frac{270}{600}-\frac1{600}
<0.45.
\tag{17}
\]

Therefore the current `x^0.45` aggregate theorem does not invalidate the matched control at or above `b=131/600`. The all-large short-interval exponent `0.52` is still farther away. A targeted current search found no primary theorem improving the complete `1.23+epsilon` square-sum exponent or supplying an aggregate-gap estimate below `x^0.45` strong enough to remove this control. This is a bounded search statement, not a priority claim.

Hence the `469/600` frontier of `RE-091` is not merely the output of one convenient Cauchy estimate. Within the presently available package

\[
\text{depth-3 host count}
+
\text{paired anchored gap magnitudes}
+
\text{PNT-scale density}
+
\text{current complete gap second moment},
\tag{18}
\]

it is the sharp exponent boundary. Improving it requires a relation between **which** depth-3 host `q` occurs and **which** first-layer gap at scale `X` contains its event image, not another separate estimate for the size of `d_3`.

## 3. Depth two: the surviving mixed `1/2` channel has a `173/200` scalar barrier

For the actual residual left by `RE-091`, take `r=2`. Then

\[
\boxed{
\beta_2=\frac{173}{200}=0.865,
\qquad
b_2^*=\frac{27}{200}=0.135.
}
\tag{19}
\]

At the critical scale the required first-layer gaps have size

\[
d_1^{\rm ctrl}
=X^{73/200+o(1)},
\tag{20}
\]

while the depth-2 anchored lower bound is only

\[
d_2^{\rm req}
=X^{-27/200+o(1)}.
\tag{21}
\]

The latter is completely vacuous. The former is far below both `x^0.45` and `x^0.52`, so neither the current Järviniemi aggregate theorem nor the all-large short-interval theorem sees the equal-width control.

Consequently, in the whole regime

\[
\boxed{
\frac{469}{600}<\Theta\le\frac{173}{200},
}
\tag{22}
\]

`RE-091` can force one-sided first-layer boundary contact on almost all threshold mass, but **the paired first/depth-2 gap magnitudes plus current separate moment bounds cannot force the opposite boundary to be first-layer as well**. Every admissible compact fan interval lies above `1-Theta>=27/200` at the lower end of this regime, exactly where the matched control remains compatible with the scalar inputs.

For `Theta>173/200`, the general `RE-091` host/moment calculation with `r=2` can already be run with `b<27/200`; depth-2 boundaries then become threshold-negligible. That positive extreme-frontier corollary is immediate from the existing exponent law. The new information here is why the same scalar route has no exponent room before that point, even after the two gap requirements are paired cell by cell.

## 4. What the control deliberately does not reproduce

The construction is a falsification control for a proof architecture, not a synthetic CA theorem. It keeps the cell count, total threshold width, amplitude scale, physical packing scale, both anchored-gap magnitudes, PNT-scale first-moment room, and the current complete gap second-moment exponent. It does **not** require the large-scale gap endpoint `p` and the host prime `q` to satisfy the exact mixed-boundary incidence

\[
\eta_1(p)\quad\text{adjacent to}\quad\eta_r(q)
\tag{23}
\]

inside one genuine CA event staircase, nor does it impose rightmost-maximizer selection on that pairing. Those are precisely the pieces of arithmetic information that remain capable of improving the frontier.

This boundary matters because merely saying that the two gaps are "simultaneous" is not enough. Their lower bounds have very different Jacobians. Once fixed threshold mass is spread across the natural `X^(1/r)` host population, inverse-layer expansion cancels the host sparsity exactly in (9), leaving a subunit base-gap request. Any successful paired-gap argument must therefore exploit **incidence/correlation**, not just multiply or separately sum the two gap-size inequalities.

A useful next target is consequently concrete: for `r=2`, bound the threshold mass of primes `q\asymp\sqrt X` for which the special physical point `eta_2(q)` can occur as an adjacent support boundary next to a first-layer event `eta_1(p)`, with the required rightmost-maximizer orientation. Equivalently, study the ordinary prime gap containing

\[
\eta_1^{-1}(\eta_2(q))
\tag{24}
\]

**conditioned on `q` itself being prime and selected by the CA fan**, rather than replacing those conditioned gaps by the unconditional gap moment. That source-specific incidence is not present in Stadlmann's or Järviniemi's theorems and is exactly what the matched control omits.

## Prior-art boundary

The load-bearing external estimate remains Julia Stadlmann's `sum d_n^2 << x^(1.23+epsilon)`, already anchored in `SOURCES.md` for `RE-091`. Olli Järviniemi's aggregate bounds at thresholds `x^0.45` and `x^0.5` were rechecked because they are the nearest stronger gap inputs; the critical depth-3 control lives at `x^(269/600)=x^0.44833...`, while the depth-2 control lives at `x^(73/200)=x^0.365`. No new external theorem is needed, so `SOURCES.md` is unchanged.

The nearest internal controls are `RE-055` and `RE-087`. `RE-055` shows that all-layer event-free chambers can be built in a PNT-dense generalized source, but it does not impose the current prime-gap second moment or calibrate the sparse-host exponent. `RE-087` proves divergence of separate marginal anchored-gap capacities, but does not pair the two gap inequalities on the same cells under the Stadlmann budget. The durable new delta is the matched exponent calculation (8)--(13): **the host-layer gap becomes asymptotically free exactly in the full-width allocation that makes the first-layer second moment sharp.**

## Consequence for the research line

`RE-091` correctly moved the live problem to first-layer-attached selection. The present stress test says what "joint" must mean. Pairing the two **sizes** of the ordinary gaps is not enough. Above `469/600` and up to `173/200`, the surviving `1/2` channel can only be attacked by preserving the exact cross-scale identity of the paired primes/events, their orientation in the consecutive CA staircase, or the rightmost-maximizer constraint. Replacing that incidence by separate moment budgets loses exactly the information needed to move the frontier.