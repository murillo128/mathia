# RE-074 — bounded fan steps have only log-over-scale Mertens reset capacity

**Status:** `EXACT-DERIVED + QUANTITATIVE-RH-FAILURE + MATCHED-FIRST-LAYER-RUN + BOUNDED-INTERRUPTION-CAPACITY + MERTENS-RESET-COMPLEXITY + CHEBYSHEV-PRIME-MASS-BRIDGE + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`.

`RE-072`--`RE-073` show that a matched `0 -> 0` first-layer fan run carries a one-sided source ledger: the Chebyshev deficit

\[
H_\vartheta(x):=x-\vartheta(x)
\]

increases while the logarithmic Mertens-product error

\[
E_\ell(x):=\sum_{p\le x}-\log(1-p^{-1})-\gamma-\log\log x
\]

decreases, with a span-free joint cost. The remaining global escape is that later unmatched or higher-layer fan steps might reset the reciprocal source and thereby erase the matched-run descent. A bounded physical packet cannot do this efficiently.

The ordinary prime sources already give an exact reset budget. For every `2<=u<v`,

\[
\boxed{
\vartheta(v)-\vartheta(u)
\ge
(u-1)\log u\;\bigl(E_\ell(v)-E_\ell(u)\bigr)_+.
}
\tag{1}
\]

Thus positive Mertens recovery must be paid for by ordinary Chebyshev prime mass in the same selector interval. When the interval is one adjacent exposed-fan switch whose complete physical CA packet has cardinality at most a fixed `K`, `RE-061` makes the selector jump only logarithmic. Uniformly on the late compact fan,

\[
\boxed{
\bigl(E_\ell(Z_+)-E_\ell(Z_-)\bigr)_+
\ll_{J,K}\frac{\log Y}{Y},
}
\tag{2}
\]

where `Y=log C_-` is the lower physical state scale. An open fixed-state threshold cell has even smaller positive capacity: by `RE-059` it contains at most one fringe-prime source update, so its total upward variation satisfies

\[
\boxed{
\operatorname{Var}_+ E_\ell\ll_J \frac1Y.
}
\tag{3}
\]

Consequently a string of `N` subsequent fan transitions, each with physical packet cardinality at most `K`, beginning after a matched run whose terminal physical scale is `W`, has

\[
\boxed{
\operatorname{Var}_+ E_\ell
\ll_{J,K}
N\frac{\log W}{W}.
}
\tag{4}
\]

Now retain the setup of `RE-072`. Assume RH is false, put

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>\frac12,
\]

fix

\[
J=[b_0,b_1]\Subset(1-\Theta,\tfrac12),
\tag{5}
\]

and let a sufficiently late common positive block contain a consecutive matched first-layer run of threshold width

\[
w:=\beta_m-\beta_1>0.
\tag{6}
\]

Let `W` be the largest physical state scale in that run and write

\[
B:=E_\ell(Z_L)-E_\ell(Z_R)>0
\tag{7}
\]

for its total reciprocal-source descent. `RE-072` gives

\[
B\gg_J W^{-b_1}w.
\tag{8}
\]

If the next `N` bounded-packet fan transitions, together with their intervening cells, recover any fixed fraction `lambda in (0,1]` of that descent,

\[
E_\ell(Z_{\rm end})-E_\ell(Z_R)\ge\lambda B,
\tag{9}
\]

then (4) and (8) force

\[
\boxed{
N\gg_{J,K,\lambda}
\frac{W^{1-b_1}}{\log W}\,w.
}
\tag{10}
\]

Because `b_1<1/2`, a matched run with `w` bounded below by a positive constant cannot have a fixed fraction of its Mertens descent erased by only square-root-many bounded interruptions. It requires more than `W^(1/2+epsilon)` such transitions for some `epsilon>0` determined by `J`, up to the logarithm.

Equivalently, along any escaping family in which a fixed fraction of the matched Mertens descent is recovered within

\[
N=o\!\left(\frac{W^{1-b_1}}{\log W}w\right)
\tag{11}
\]

subsequent fan transitions, the physical packet cardinalities in that resetting segment cannot remain uniformly bounded. For every fixed `K`, some packet eventually has cardinality greater than `K`. The remaining fast-reset architecture is therefore forced into **unbounded packet complexity**, not merely a different mixture of bounded higher-layer, Egyptian, fringe, or deep-layer steps.

## 1. Positive Mertens motion is paid for by ordinary prime mass

Put

\[
m_p:=-\log(1-p^{-1}).
\tag{12}
\]

For arbitrary real `2<=u<v`, exactly

\[
E_\ell(v)-E_\ell(u)
=
\sum_{u<p\le v}m_p
-
\log\frac{\log v}{\log u}.
\tag{13}
\]

The second term is nonpositive. Hence

\[
\bigl(E_\ell(v)-E_\ell(u)\bigr)_+
\le
\sum_{u<p\le v}m_p.
\tag{14}
\]

For every prime `p>u`,

\[
m_p
\le\frac1{p-1}
\le\frac1{u-1}
\le
\frac{\log p}{(u-1)\log u}.
\tag{15}
\]

Summing (15) over the primes in `(u,v]` proves (1).

There is also an exact measure identity behind this comparison. Define

\[
g(x):=\frac1{x\log x},
\qquad
\kappa_p:=m_p-\frac1p>0,
\qquad
K(x):=\sum_{p\le x}\kappa_p.
\tag{16}
\]

Since `g(p) log p=1/p`, the Stieltjes source measures satisfy

\[
\boxed{
dE_\ell=-g\,dH_\vartheta+dK.
}
\tag{17}
\]

The correction is summable. Indeed

\[
0<\kappa_p
=\sum_{r\ge2}\frac1{r p^r}
\le\frac1{p(p-1)},
\tag{18}
\]

so for every `A>=2`,

\[
\boxed{
0\le K(\infty)-K(A)
\le\sum_{n>A}\frac1{n(n-1)}
\le\frac1{\lfloor A\rfloor}.
}
\tag{19}
\]

Thus the standard and logarithmic-Mertens source ledgers are not independent currencies even outside a matched run: positive reciprocal motion must come from discrete prime atoms, and after the `1/p` component is identified the remaining discrepancy is a summable prime-square tail. Equation (17) is an elementary source identity; the line-specific content below is what the CA fan geometry forces when it is combined with bounded event packets.

## 2. One bounded fan switch can recover only `O(log Y / Y)`

Consider two consecutive exposed fan states `C_-<C_+` tied at a breakpoint `b in J`, and put

\[
Y_\pm:=\log C_\pm,
\qquad
Z_\pm:=Z_b(C_\pm),
\qquad
Y:=Y_-.
\tag{20}
\]

Assume the complete physical CA packet from `C_-` to `C_+` has at most `K` event occurrences. `RE-061` proves uniformly on the late compact fan that

\[
Y_+-Y_-=O_K(\log Y)
\tag{21}
\]

and, because the two tied states lie on one common-amplitude tangent curve,

\[
\boxed{
Z_+-Z_-=O_{J,K}(\log Y),
\qquad
Z_\pm/Y\longrightarrow1.
}
\tag{22}
\]

Moreover `dZ/dY=1+o_J(1)` on this short tied segment, so `Z_+>Z_-` for all sufficiently late blocks.

Apply (14) with `u=Z_-` and `v=Z_+`. The interval contains at most `O_{J,K}(log Y)` integers, and every prime in it satisfies `p\asymp_J Y`. Therefore

\[
\sum_{Z_-<p\le Z_+}m_p
\ll_{J,K}
\frac{\log Y}{Y},
\tag{23}
\]

which proves (2).

No classification of the packet is used. In particular the same reset cap applies to bounded first-layer packets, higher-layer packets, Egyptian-core packets from `RE-061`--`RE-064`, deep-layer packets, and packets touching a fringe host. Their residual charges may differ, but their ability to move the **ordinary** Mertens source upward across one adjacent exposed-fan switch is uniformly limited by the logarithmic selector span.

A useful equivalent interpretation follows from (1): a reset of size `delta>0` over one such switch would require

\[
\vartheta(Z_+)-\vartheta(Z_-)
\gg_J Y\log Y\,\delta.
\tag{24}
\]

But the selector interval itself has length only `O_{J,K}(log Y)` and contains only `O_{J,K}(log Y)` possible prime atoms. The bounded-packet geometry therefore imposes a finite prime-mass capacity on any attempted reciprocal-source reset.

## 3. Fixed cells contribute only one possible positive atom

Between adjacent fan breakpoints, keep one exposed state `C` fixed and write `Y=log C`. `RE-059` gives the exact raw-source form

\[
M(Z)
=M_C+\chi_C(Z)m_{r_C},
\tag{25}
\]

where `M_C` is constant, `chi_C in {0,1}` is monotone as the tangent selector increases, and there is at most one fringe prime `r_C` in the whole support chamber. Hence

\[
E_\ell(Z)
=M_C+\chi_C(Z)m_{r_C}-\gamma-\log\log Z.
\tag{26}
\]

The continuous term strictly decreases with `Z`; the only possible upward motion is the single jump `m_(r_C)`. Uniform late-fan regularity has `r_C\asymp_J Z\asymp_J Y`, so

\[
\boxed{
\operatorname{Var}_+ E_\ell
\le m_{r_C}
\ll_J\frac1Y.
}
\tag{27}
\]

An empty cell or a cell with no fringe prime contributes zero positive variation. Thus allowing the continuum of threshold values between switches does not provide a hidden reset reservoir.

## 4. Bounded interruptions make the matched Mertens descent sticky

Start immediately after the matched run of (6)--(8), whose terminal scale is `W`, and follow `N` subsequent fan switches. Suppose every complete physical packet has cardinality at most `K`. The exposed physical scales are nondecreasing and at least `W`. On sufficiently large scales the function `log x/x` decreases. Therefore each switch contributes at most

\[
O_{J,K}\!\left(\frac{\log W}{W}\right)
\tag{28}
\]

to the positive variation of `E_ell`, by (2), and every intervening cell contributes the smaller `O_J(1/W)` amount from (3). Summing proves (4).

Combining (4) with the matched-run lower bound (8) gives (10). This is stronger than merely saying that interruptions must occur: **bounded interruptions have a quantitative reset throughput.** For a macroscopic threshold run `w>=w_0>0`,

\[
N\gg_{J,K,\lambda,w_0}
\frac{W^{1-b_1}}{\log W}.
\tag{29}
\]

Since `1-b_1>1/2`, the required bounded-step complexity is super-square-root in the terminal physical scale.

The statement is deliberately conditional on a later reset. False RH does not itself imply that `E_ell` must promptly return to its pre-run value; the selected opposite-sign prime-race cone of `RE-029` and the nonlinear tube of `RE-036` are compatible with positive Mertens error persisting while slowly decreasing. What (10) says is that **if** the fan uses reciprocal-source recovery as its escape from the matched ledger, bounded packets cannot accomplish that recovery cheaply.

## 5. Falsification, prior-art boundary, and research consequence

The fixed packet bound `K` is essential. An unbounded physical packet can have a selector span much larger than `O(log Y)` and can cross many ordinary prime atoms; this finding does not bound that regime. Equation (11) records exactly that escape rather than hiding it. The result also makes no claim that every matched Mertens descent must be reset, that `E_ell` has a global monotonic sign, or that the lower bound (10) itself contradicts false RH.

The cell estimate depends on the genuine ordinary-prime/CA support geometry of `RE-059`: one fixed support chamber contains at most one ordinary fringe prime. The switch estimate depends on the bounded-event tied-selector geometry of `RE-061`. If either hypothesis is removed, the `log Y/Y` throughput bound need not survive.

The source comparison (13)--(19) is elementary partial-summation/Stieltjes structure and is **not** claimed as new number theory. The closest current literature anchor for joint ordinary and reciprocal prime errors is Bhattacharya--Martin--Simpson, *Correlations of error terms for weighted prime counting functions* (Acta Arithmetica, online first 10 September 2026), already recorded in `SOURCES.md`; it studies global correlations and RH-equivalent sign phenomena, not adaptive CA fan reset complexity. Mantovanelli's 2026 CA packet/workload framework is the closest event-packet prior art, but does not supply the bounded-selector Mertens reset law above. A directed prior-art search found no source deriving the fan-specific implication (10). No new external theorem is load-bearing here, so `SOURCES.md` requires no change.

The remaining global frontier after `RE-073` is therefore sharper. A false-RH fan that alternates long matched runs with source-resetting interruptions has only three evident options: leave the matched Mertens descent largely unrecovered, spend at least the super-square-root bounded-transition budget (10), or use packets whose physical event cardinality becomes unbounded. The next useful target is correspondingly combinatorial/arithmetic: bound the number of available bounded fan interruptions on the relevant scale, or show that the unbounded-packet escape itself has insufficient CA capacity. Either would splice the matched-run source budget into a genuinely global fan obstruction.
