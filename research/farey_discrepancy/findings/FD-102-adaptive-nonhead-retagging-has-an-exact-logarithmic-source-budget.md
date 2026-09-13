# FD-102 — adaptive nonhead retagging has an exact logarithmic source budget

**Status:** `EXACT-DERIVED + ADAPTIVE-RETAGGING + CARRIER-INDEPENDENT-POTENTIAL + EXACT-CEILING-CONTROL + SOURCE-DESCENT-CHARGE + LOGARITHMIC-DEPTH-THRESHOLD + FD100-FD101-LIFT + FD097-UNIFORMIZATION-FRONTIER + NO-RH-CONTRADICTION`.

`FD-100` proves that a fixed exact carrier spends a finite row inventory, and `FD-101` shows that a fixed tagged nonhead genealogy cannot use floor/ceiling drift to escape that inventory. Their explicit remaining loophole is adaptive retagging: after reaching the next physical predecessor, the energy argument may abandon the transported row and select a completely different nonsquarefree row, apparently resetting the carrier potential.

There is an exact carrier-independent charge for this reset. Every currently proved **nonhead** physical predecessor contracts the horizon by at least one dyadic step,

\[
\boxed{H'\le \left\lceil\frac H2\right\rceil.}
\tag{1}
\]

If a nonhead row at horizon `H` samples source quotient

\[
x=\left\lfloor\frac Hr\right\rfloor,
\]

then necessarily `r>=8`. This suggests the retagging potential

\[
\boxed{
\mathfrak A(H,x)
:=
\log_2\frac{H-1}{8x-1}.
}
\tag{2}
\]

It is nonnegative for every nonhead tagged coordinate. More importantly, after **arbitrary retagging** at the child horizon from source `x` to any new nonhead source `y`, one has the exact inequality

\[
\boxed{
\mathfrak A(H',y)
\le
\mathfrak A(H,x)-1
+
\log_2\frac{8x-1}{8y-1}.
}
\tag{3}
\]

Thus a carrier switch cannot replenish one unit of source-neutral inventory for free. If `y>=x`, so the retag does not move to a smaller source argument, then

\[
\boxed{
\mathfrak A(H',y)\le \mathfrak A(H,x)-1.
}
\tag{4}
\]

If the potential is reset upward, the reset is paid exactly by the logarithmic source-descent term in (3). The row identity never enters.

Iterating gives a particularly simple adaptive theorem. Along any sequence of `m` consecutive nonhead predecessor states, with completely arbitrary carrier reselection at every state,

\[
\boxed{
8x_m-1
\le
\frac{H_0-1}{2^m}.
}
\tag{5}
\]

Consequently a segment on which the sampled source never falls below its starting value `x_0` has length at most

\[
\boxed{
m\le \mathfrak A(H_0,x_0)
=
\log_2\frac{H_0-1}{8x_0-1}.}
\tag{6}
\]

On the frontier core of `FD-101`, where `x_0>=H_0^{\Theta-\delta+o(1)}`, this becomes

\[
\boxed{
m\le
(1-\Theta+\delta+o(1))\log_2 H_0.}
\tag{7}
\]

So the packet-level escape left after `FD-101` is narrower than stated there. **Adaptive carrier switching cannot hide source-neutral descent indefinitely and does not require its own genealogical conservation law.** Either a retag moves to a genuinely smaller source quotient, a head event is exposed, or after only logarithmically many nonhead physical predecessors the horizon/source geometry itself forces source descent. The remaining quantitative obstruction is now the one already latent in `FD-097`: make the projective predecessor transport uniform to the required `c log H` depth, or extract enough source progress from the head/source-descending events before that depth is reached.

## 1. Every current nonhead physical predecessor is at most a dyadic half-step

There are three nonhead physical repairs in `FD-091` and `FD-093`. Their row maps were used in `FD-100`; here we keep the physical horizons instead.

### Odd repeated-prime branch

Let `p>=3` be the repeated odd prime chosen for the tagged row. The physical repaired horizon is

\[
C
=
4\left\lfloor
\frac{\lceil H/p\rceil}{p}
\right\rfloor.
\tag{8}
\]

Because the tagged row is divisible by `p^2` and occurs at horizon `H`, we have `H>=p^2`. Write

\[
H=p^2q+a,
\qquad q\ge1,
\qquad 0\le a<p^2.
\tag{9}
\]

Then

\[
\left\lfloor
\frac{\lceil H/p\rceil}{p}
\right\rfloor
=
q+\varepsilon,
\qquad
\varepsilon\in\{0,1\},
\tag{10}
\]

and `epsilon=1` can occur only when `a>=p^2-p+1`. If `epsilon=0`, then

\[
C=4q
\le
\left\lceil\frac{p^2q+a}{2}\right\rceil
=
\left\lceil\frac H2\right\rceil,
\tag{11}
\]

since `p^2>=9`. If `epsilon=1`, then

\[
H\ge p^2q+p^2-p+1\ge 9q+7,
\]

so

\[
C=4q+4
\le
\left\lceil\frac{9q+7}{2}\right\rceil
\le
\left\lceil\frac H2\right\rceil.
\tag{12}
\]

Thus the odd repair satisfies (1) exactly, including the ceiling boundary cases.

### Eligible dyadic branch

Here the predecessor is simply

\[
H'=\left\lceil\frac H2\right\rceil,
\tag{13}
\]

so (1) is equality.

### Dyadic terminal nonhead branch

With the notation of `FD-093`, let

\[
A=\left\lceil\frac H2\right\rceil,
\qquad
B=\left\lfloor\frac A2\right\rfloor,
\]

and let `q>=3` be the deterministic odd prime used to repair the terminal nonhead row. Then

\[
C=4\left\lfloor\frac Bq\right\rfloor
\le \frac{4B}{3}
\le \frac{2A}{3}
\le A
=
\left\lceil\frac H2\right\rceil.
\tag{14}
\]

Therefore all current nonhead branches obey the common exact horizon contraction (1). The source-head construction of `FD-095` is deliberately excluded: its horizon retreat may be only additive, but it already moves the source argument backward and is therefore the other side of the dichotomy we want to expose.

## 2. A shifted horizon removes every ceiling error

The choice `H-1` in (2) is not cosmetic. For every integer `H>=2`,

\[
\boxed{
\left\lceil\frac H2\right\rceil-1
\le
\frac{H-1}{2}.
}
\tag{15}
\]

For odd `H` this is equality; for even `H` it is strict by `1/2`. Combining (1) and (15), every nonhead physical predecessor satisfies

\[
\boxed{H'-1\le\frac{H-1}{2}.}
\tag{16}
\]

Now let the next packet selection retag the child horizon onto any nonsquarefree row `r'` other than the four-adic head. Since `4` is the only nonsquarefree integer below `8`, every nonhead tag has

\[
r'\ge8.
\tag{17}
\]

Writing

\[
y=\left\lfloor\frac{H'}{r'}\right\rfloor,
\tag{18}
\]

gives `H'>=r'y>=8y`, hence

\[
H'-1\ge8y-1.
\tag{19}
\]

Thus `mathfrak A(H',y)>=0`. The same argument applies to the parent `(H,x)`.

Equation (16) now gives

\[
\frac{H'-1}{8y-1}
\le
\frac{H-1}{2(8y-1)}
=
\frac{H-1}{8x-1}\,
\frac12\,
\frac{8x-1}{8y-1},
\tag{20}
\]

which is exactly (3).

This potential is also the carrier inventory of `FD-100` with the carrier name removed. If `x=floor(H/r)` and `r>=8`, then

\[
rx\le H<r(x+1).
\tag{21}
\]

Using `r>=8` and `x>=1`,

\[
\frac r8
\le
\frac{H-1}{8x-1}
<
\frac{16}{7}\frac r8.
\tag{22}
\]

Hence

\[
\boxed{
\mathfrak A(H,x)
=
\log_2\frac r8+O(1)
}
\tag{23}
\]

with an absolute error bounded by `log_2(16/7)`. `FD-100` used `log_2(r/4)`; the two inventories therefore differ only by an absolute constant. The new point is that (2) survives arbitrary changes of `r` because it is expressed only through physical horizon and sampled source quotient.

## 3. Retagging resets are paid by source descent

Consider an adaptive sequence

\[
(H_0,r_0,x_0),
(H_1,r_1,x_1),
\ldots,
(H_m,r_m,x_m),
\tag{24}
\]

in which each transition `H_j -> H_(j+1)` is one of the current canonical nonhead physical predecessors, but after arrival the next row `r_(j+1)` may be chosen arbitrarily from the nonhead nonsquarefree sector. Put

\[
x_j=\left\lfloor\frac{H_j}{r_j}\right\rfloor,
\qquad
\mathfrak A_j=\mathfrak A(H_j,x_j).
\tag{25}
\]

Applying (3) at every step gives

\[
\mathfrak A_{j+1}
\le
\mathfrak A_j-1
+
\log_2\frac{8x_j-1}{8x_{j+1}-1}.
\tag{26}
\]

The source term telescopes, regardless of how often the carrier identity changes:

\[
\boxed{
\mathfrak A_m
\le
\mathfrak A_0-m
+
\log_2\frac{8x_0-1}{8x_m-1}.
}
\tag{27}
\]

Since `mathfrak A_m>=0`,

\[
2^m(8x_m-1)
\le
H_0-1,
\tag{28}
\]

which is (5).

There are two equivalent ways to read this identity.

First, if the retagged source never descends, `x_m>=x_0`, then the logarithmic term in (27) is nonpositive and every physical nonhead step consumes at least one full unit of adaptive potential. This proves (6).

Second, once the available initial potential has been spent, every additional nonhead step must be paid by a multiplicative reduction of the source scale. More quantitatively, for any fixed `0<rho<1` and `x_0 -> infinity`,

\[
m
\ge
\mathfrak A(H_0,x_0)+\log_2\frac1\rho+O(1)
\quad\Longrightarrow\quad
x_m\le \rho x_0+O(1).
\tag{29}
\]

Thus repeated packet switching can change which row carries the energy, but it cannot manufacture fresh source-neutral depth. The only way to reset the carrier-free budget is to spend actual source scale.

## 4. The frontier core turns the remaining problem into logarithmic-depth uniformization

`FD-101` records that the parent rows in the frontier block satisfy

\[
r_0\le R_{H_0}
=
\left\lfloor\frac{H_0}{L_{H_0}+1}\right\rfloor,
\qquad
L_{H_0}=H_0^{\Theta-\delta+o(1)},
\tag{30}
\]

so

\[
x_0=\left\lfloor\frac{H_0}{r_0}\right\rfloor
\ge L_{H_0}
=H_0^{\Theta-\delta+o(1)}.
\tag{31}
\]

Substituting (31) into (6) gives the explicit no-source-descent budget

\[
\boxed{
\mathfrak A(H_0,x_0)
\le
(1-\Theta+\delta+o(1))\log_2 H_0.
}
\tag{32}
\]

Therefore a chain of nonhead packet predecessors controlled uniformly for slightly more than

\[
(1-\Theta+\delta)\log_2 H_0
\tag{33}
\]

steps could not remain at the original source scale, **even if the dominant carrier is completely reselected at every step**. With `s` further nonhead steps, (29) forces roughly `s` additional binary units of source-scale loss.

This explains exactly why the diagonal consequence of `FD-097` is not yet enough. That finding proves that arbitrary fixed depths can be diagonalized with subpower projective degradation, but it deliberately gives no effective relation between available depth and starting horizon because the transport `o(1)` terms were not uniformized against the shrinking certificate. The geometry above shows what relation is actually needed: depth proportional to `log H`, with coefficient controlled by `1-Theta`, rather than merely an unspecified depth tending to infinity.

If one could extend the projective estimate

\[
\mathcal Q_\sigma(H_j)
\gtrsim
\mathcal Q_\sigma(H_0)b_\sigma^j
\tag{34}
\]

uniformly to the logarithmic depth (33), the deterministic retagging problem would already be closed. The cost would be polynomial rather than subpower,

\[
b_\sigma^m
=
H_0^{-(1-\Theta+\delta)\log_2(1/b_\sigma)+o(1)},
\tag{35}
\]

so a final argument would still have to show that this polynomially weakened packet remains strong enough, or improve the per-step coefficient. `FD-102` does not supply that analytic uniformity and therefore does not prove RH.

## 5. Matched controls and sharp boundaries

The record-seeded cascade of `FD-099` remains the right stress test. There

\[
H_0=9^mX,
\qquad
x_0=X,
\tag{36}
\]

and the completed source-neutral genealogy of `FD-100` has `3m-2` repairs before the four-adic head is exposed. The adaptive budget is

\[
\mathfrak A(H_0,x_0)
=
\log_2\frac{9^mX-1}{8X-1}
=m\log_2 9-3+o(1),
\tag{37}
\]

which is on the same logarithmic scale as that construction. Thus the theorem does not falsely rule out the known long source-neutral cascades; it explains their cost without tracking their prime-factor genealogy.

The constant `8` is also structural for a nonhead statement. Row `4` is the unique minimal nonsquarefree row and is precisely the source-head state. Once row `4` is allowed, `H>=8x` is false and the nonhead budget must terminate. This is desirable: reaching row `4` is exactly the alternative that `FD-095` and `FD-098` convert into backward source motion.

Finally, source descent is not being assumed monotone. Equation (27) permits arbitrary source ascents and descents between retags. Ascents only make the adaptive potential smaller. Descents can replenish it, but the logarithmic factor in (27) records their exact cumulative multiplicative price. There is therefore no hidden genealogical coherence assumption in the amortization.

## 6. Prior-art boundary and research consequence

A targeted literature audit rechecked the classical Farey--Mertens discrepancy setting together with Rogelio Tomás García's 2025 recursive formulas for Farey local discrepancy and the 2026 average-local-discrepancy work. Those papers derive rank/discrepancy identities from Möbius and Mertens sums or study gap-distribution lower bounds; no located source contains the Mathia-specific repeated-prime predecessor maps, the physical half-horizon lemma (1), or the adaptive potential (2). The present proof uses no external theorem beyond the already-canonical predecessor formulas of `FD-091` and `FD-093`, so `SOURCES.md` requires no update.

The live frontier changes in one important respect. After `FD-101`, `RESEARCH_LINES.md` still treats carrier switching as an independent resource that may need a new genealogical charge. `FD-102` provides that charge at the path level without preserving carrier identity: **a switch can reset source-neutral row inventory only by paying logarithmic source descent.** What remains is not to invent another carrier label, but to connect the projective energy transport to this exact deterministic budget at `Theta`-dependent logarithmic depth, while treating the source-head steps through their additive progress law.

A useful next theorem is therefore a logarithmic-depth uniformization statement: control the existing predecessor transport, including its asymptotic errors and shrinking occupation/defect certificate, for

\[
m\asymp(1-\Theta)\log H
\]

steps. Alternatively, one can bypass that target by proving that head events or source-descending retags occur earlier with enough quantitative mass to dominate the polynomial projective loss. Either route now addresses the actual remaining source-scale obstruction rather than carrier identity itself.