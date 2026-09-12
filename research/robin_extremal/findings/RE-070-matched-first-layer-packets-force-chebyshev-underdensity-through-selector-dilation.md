# RE-070 — matched first-layer packets force Chebyshev underdensity through selector dilation

**Status:** `EXACT-DERIVED + QUANTITATIVE-RH-FAILURE + FIRST-LAYER-ONLY-PACKET + MATCHED-FRINGE + SELECTOR-DILATION + CHEBYSHEV-UNDERDENSITY + UNBOUNDED-PACKET + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`.

`RE-068` shows that a complete matched `0 -> 0` first-layer packet is invisible to every additive endpoint prime weight: the ordinary primes crossed by the two adaptive selectors are exactly the physical first-layer event labels. `RE-069` then shows that directly transporting those labels from `p` to their delayed event coordinates `eta_p` contributes only an absolutely summable late tax to the exact Robin workload. The natural remaining first-layer datum is therefore not another weight on the same prime set, nor the direct linear delay transport, but the **geometric length of the selector interval that carries that fixed prime mass**.

That geometric channel does survive. In fact it has a rigid sign and a quantitative scale. Assume RH is false, put

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>\frac12,
\]

fix

\[
J=[b_0,b_1]\Subset(1-\Theta,\tfrac12),
\tag{1}
\]

and work on sufficiently late common positive CA counterexample blocks from `RE-040`. At a rightmost-fan breakpoint `b in J`, let

\[
C_-<C_+,
\qquad
Y_\pm:=\log C_\pm,
\tag{2}
\]

be consecutive exposed states tied at the same adaptive amplitude

\[
c:=A_b(C_-)=A_b(C_+)>0.
\tag{3}
\]

Let `Z_-`, `Z_+` be their adaptive tangent selectors. Suppose the complete physical packet from `C_-` to `C_+` is first-layer-only and has fringe pattern

\[
\chi_-=\chi_+=0.
\tag{4}
\]

No packet-cardinality bound is assumed.

Define on the formal common-amplitude curve

\[
a_c(Y)
:=\frac{cY^{-b}}{1+cY^{-b}},
\qquad
 g(x):=\frac1{x\log x},
\tag{5}
\]

and let `Z_c(Y)>Y` be determined by

\[
g(Z_c(Y))
=g(Y)-\frac{b\,a_c(Y)}Y.
\tag{6}
\]

The two exposed endpoints lie on this same curve:

\[
Z_c(Y_-)=Z_-,
\qquad
Z_c(Y_+)=Z_+.
\tag{7}
\]

Then uniformly on the interval between the tied late states,

\[
\boxed{
Z_c'(Y)-1
=b(1-b)a_c(Y)\log Y
\left(
1+O_J\!\left(\frac1{\log Y}+a_c(Y)\log Y\right)
\right).
}
\tag{8}
\]

Since `b<1/2` and the uniform small-height regime of `RE-040` gives `a_c(Y) log Y -> 0`, equation (8) is eventually positive. Thus the adaptive selector map does more than preserve state order as used in `RE-068`: **along every tied common-amplitude curve it expands logarithmic state length**,

\[
\boxed{Z_+-Z_->Y_+-Y_-.}
\tag{9}
\]

On the matched first-layer branch, `RE-068` gives the exact prime-set identity and hence

\[
\vartheta(Z_+)-\vartheta(Z_-)
=Y_+-Y_-.
\tag{10}
\]

Combining (9)--(10) yields the exact surviving source-geometric law

\[
\boxed{
\begin{aligned}
&\bigl(Z_+-\vartheta(Z_+)\bigr)
-\bigl(Z_--\vartheta(Z_-)\bigr)\\
&\qquad=
(Z_+-Z_-)-(Y_+-Y_-)\\
&\qquad=
\int_{Y_-}^{Y_+}\bigl(Z_c'(t)-1\bigr)\,dt
>0.
\end{aligned}
}
\tag{11}
\]

More quantitatively,

\[
\boxed{
\bigl[Z-\vartheta(Z)\bigr]_{Z_-}^{Z_+}
=
 b(1-b)
\int_{Y_-}^{Y_+}
a_c(t)\log t\,dt
\,(1+o_J(1)).
}
\tag{12}
\]

The common positive blocks provide a uniform lower amplitude. In the notation of `RE-040`, there is `c_0>0`, independent of the late block and of `b in J`, such that every blockwise maximizer satisfies `A_b(C)>=c_0`. Hence `c>=c_0`, and (12) implies

\[
\boxed{
\bigl[Z-\vartheta(Z)\bigr]_{Z_-}^{Z_+}
\gg_J
\int_{Y_-}^{Y_+}t^{-b}\log t\,dt.
}
\tag{13}
\]

For a sublinear packet, `Delta Y:=Y_+-Y_-=o(Y_-)`, put `Y:=Y_-` and `a_-:=a_c(Y)`. Then (12) becomes the local density law

\[
\boxed{
Z_+-Z_-
=
\Delta Y
\left(
1+b(1-b)a_-\log Y+o_J(a_-\log Y)
\right),
}
\tag{14}
\]

while the prime mass remains exactly `Delta Y`. Therefore

\[
\boxed{
\frac{\vartheta(Z_+)-\vartheta(Z_-)}{Z_+-Z_-}
=
1-b(1-b)a_-\log Y
+o_J(a_-\log Y).
}
\tag{15}
\]

Since `c>=c_0` and `a_-~cY^{-b}` in the late small-height regime, the required relative Chebyshev deficit is at least of order

\[
Y^{-b}\log Y.
\tag{16}
\]

Thus the charge-silent matched packet is not source-free once pre-compression geometry is retained. It must sit on an adaptively selected interval whose weighted prime density is **strictly below one by the precise selector-dilation amount**. This does not yet contradict known prime distribution. It instead identifies the next source estimate that would actually attack the matched branch: on such selected intervals one would need control of

\[
\vartheta(Z_+)-\vartheta(Z_-)-(Z_+-Z_-)
\tag{17}
\]

at a scale finer than `(Z_+-Z_-)Y^{-b} log Y` in the sublinear regime. Ordinary `o(H)` short-interval asymptotics are not enough, because the forced relative deficit itself tends to zero.

## 1. The common-amplitude selector is asymptotically expanding

Write

\[
L:=\log Y,
\qquad
A(Y):=-g'(Y)
=\frac{L+1}{Y^2L^2}.
\tag{18}
\]

The tied amplitude relation is

\[
e^{h(Y)}-1=cY^{-b},
\tag{19}
\]

so (5) is exactly

\[
a_c(Y)=1-e^{-h(Y)},
\tag{20}
\]

and differentiation gives

\[
a_c'(Y)
=-\frac bY a_c(Y)(1-a_c(Y)).
\tag{21}
\]

Put

\[
d(Y):=Z_c(Y)-Y>0.
\tag{22}
\]

Taylor expansion of (6) at `Y`, using `a_c(Y)L=o(1)`, gives

\[
\boxed{
\frac{d(Y)}Y
=
\frac{b\,a_c(Y)L^2}{L+1}
\left(1+O_J(a_c(Y)L)\right)
=
b\,a_c(Y)L
\left(1+O_J\!\left(\frac1L+a_c(Y)L\right)\right).
}
\tag{23}
\]

In particular `d(Y)/Y=o(1)` uniformly along the late common-amplitude segment.

Differentiate (6). With `a=a_c(Y)`,

\[
g'(Z_c(Y))Z_c'(Y)
=g'(Y)
+\frac{ba}{Y^2}\bigl(1+b(1-a)\bigr).
\tag{24}
\]

The logarithmic derivative of `g'` gives

\[
\frac{g''(Y)}{-g'(Y)}
=\frac2Y+O\!\left(\frac1{Y\log Y}\right).
\tag{25}
\]

Using (23),

\[
\frac{g'(Z_c(Y))-g'(Y)}{A(Y)}
=
2b\,aL
\left(1+O_J\!\left(\frac1L+aL\right)\right),
\tag{26}
\]

whereas the positive correction in (24) satisfies

\[
\frac{baY^{-2}(1+b(1-a))}{A(Y)}
=
b\,aL(1+b)
\left(1+O_J\!\left(\frac1L+a\right)\right).
\tag{27}
\]

Both normalized corrections are `o(1)`. Dividing the two sides of (24) by `g'(Z_c(Y))` and subtracting one, (26)--(27) leave the coefficient

\[
2-(1+b)=1-b,
\tag{28}
\]

which proves (8). Because `J` is compactly contained in `(0,1/2)`, the main coefficient `b(1-b)` is uniformly positive.

The error control is uniform even if the packet contains an unbounded number of first-layer events. Along the formal segment, `c` and `b` are fixed and `a_c(t)` decreases with `t`; for late `Y_-`, the quantity `a_c(t) log t` is uniformly small for every `t>=Y_-`. No estimate of `Y_+-Y_-` or of packet cardinality was used.

## 2. Prime-set conservation turns selector expansion into a Chebyshev deficit

Under the first-layer-only and `0 -> 0` assumptions, `RE-068` proves

\[
\mathcal E
=
\{p\text{ prime}:Z_-<p\le Z_+\},
\tag{29}
\]

where `E` is the set of physical first-layer labels crossed by the complete packet. The exact state ratio therefore gives

\[
Y_+-Y_-
=
\sum_{p\in\mathcal E}\log p
=
\vartheta(Z_+)-\vartheta(Z_-),
\tag{30}
\]

which is (10). This equality contains no prime-number-theorem approximation.

Now define the standard Chebyshev deficit

\[
H_\vartheta(x):=x-\vartheta(x).
\tag{31}
\]

Using (30),

\[
\begin{aligned}
H_\vartheta(Z_+)-H_\vartheta(Z_-)
&=(Z_+-Z_-)-(Y_+-Y_-)\\
&=d(Y_+)-d(Y_-).
\end{aligned}
\tag{32}
\]

Equation (8) makes the last difference strictly positive and yields (11)--(12). This is the point at which the otherwise source-invisible matched packet becomes observable: **the prime labels are the same, but the tied tangent geometry asks that their exact logarithmic mass occupy a slightly longer selector interval than logarithmic state mass occupies.**

The conclusion is stronger than simply saying that there is a prime gap near one endpoint. The packet may contain arbitrarily many first-layer events. Equation (32) constrains the aggregate Chebyshev mass of the whole adaptively selected interval, so it remains meaningful in precisely the unbounded first-layer takeover left open by `RE-067`--`RE-069`.

## 3. False-RH amplitude supplies a quantitative deficit floor

The common blocks of `RE-040` were built from one quantitative false-RH threshold `b_0`. For every `b in J`, every blockwise maximizer has

\[
A_b(C)\ge c_0
\tag{33}
\]

for one fixed `c_0>0`. At a breakpoint the two tied states are both maximizers, so their common value `c` in (3) obeys the same lower bound.

Because

\[
a_c(t)
=\frac{ct^{-b}}{1+ct^{-b}}
\ge
\frac{c_0t^{-b}}{1+c_0t^{-b}},
\tag{34}
\]

and the right-hand side is asymptotic to `c_0 t^{-b}`, (12) gives (13). Explicitly,

\[
\int t^{-b}\log t\,dt
=
\frac{t^{1-b}}{1-b}
\left(
\log t-\frac1{1-b}
\right),
\tag{35}
\]

so a long matched first-layer packet must accumulate a correspondingly long positive excursion of `H_vartheta` between its two adaptive selectors.

If `Delta Y=o(Y)`, then `a_c(t)=a_-(1+o(1))` and `log t=log Y+o(1)` uniformly over the segment. Integrating (8) gives (14); combining with (30) gives (15). The lower amplitude bound and `a_- log Y -> 0` imply

\[
a_-\log Y
\gg_J Y^{-b}\log Y,
\tag{36}
\]

which is the floor (16).

For a bounded physical packet, `Delta Y=O(log Y)` and the absolute forced deficit can tend to zero; there is no discreteness contradiction. The value of (13)--(16) is instead that they continue to hold when the number of first-layer events grows. The formerly undifferentiated `unbounded packet` escape now carries a definite prime-density obligation whenever it remains pure first-layer and matched.

## 4. Boundary tests and what would actually close the branch

The matched fringe condition is essential. For `0 -> 1` or `1 -> 0`, `RE-068` inserts one endpoint prime into the exact multiset law, and (30) acquires the corresponding `+- log r` correction. Those packets are already isolated as the lacunary nonzero-charge classes of `RE-063`, `RE-066`, and `RE-067`.

The first-layer-only condition is also essential. A higher-layer event changes the frozen mass `P_C` of `RE-059`; after subtraction it leaves the higher-layer charge studied in `RE-060`--`RE-066`. Equation (30) is then false without that source term.

The common-amplitude condition is not optional bookkeeping. Equation (8) concerns the formal curve joining two states tied at one fan breakpoint. It should not be applied to arbitrary CA states with unrelated amplitudes. Consecutive exposed fan states at their breakpoint provide exactly the required common `b,c`.

The result does not contradict the prime number theorem. Equation (15) asks for a relative deficit tending to zero. To exclude a sublinear matched packet of selector length `H`, one would need, on these **adaptively selected intervals**, an estimate of the schematic strength

\[
\vartheta(x+H)-\vartheta(x)
=H+o(HY^{-b}\log Y),
\tag{37}
\]

not merely `H+o(H)`. Current global PNT errors and ordinary short-interval asymptotics do not supply such a power-scale relative saving uniformly on this selected family. In the false-RH regime this is also a necessary falsification check: because `b>1-Theta`, the scale `Y^{1-b}` remains below the natural `Y^Theta` size allowed by an off-critical prime-number-theorem error. The sign/dilation law is therefore a new structural obligation, not a hidden contradiction with the hypothesis under study.

A synthetic matched-prime control can also reproduce (30) together with an interval slightly longer than its assigned logarithmic mass by inserting the required local underdensity. Thus the result does not by itself break generalized-prime universality. What it does is identify **which extra datum must now be matched**: not another endpoint weight and not the direct first-layer delay tax, but the geometric mass-to-length relation of the actual ordinary-prime source on the fan-selected intervals.

## 5. Prior-art boundary and research consequence

Alaoglu--Erdos supplies the classical CA threshold structure, and the recent Mantovanelli prime-layer workload framework supplies the closest event/packet bookkeeping prior art already anchored in `SOURCES.md`. The literature audit for this pass found that framework and standard work on Chebyshev/PNT error control, but did not locate the line-specific adaptive statement (11)--(15): a matched false-RH fan breakpoint forces exact Chebyshev underdensity because the **common-amplitude tangent selector expands faster than logarithmic state size**. No priority claim is made, and no external theorem beyond the anchors already recorded in `SOURCES.md` is load-bearing here.

The live first-layer frontier after `RE-068`--`RE-070` is consequently narrower. Endpoint additive source statistics are exactly conserved; direct linear prime/event timing is summably suppressed by the Robin kernel; but selector geometry survives as the interval-length defect (11). A useful next step is therefore not another prime weight. It is either a source-specific estimate for `theta` on these adaptive underdensity intervals, or a cross-packet argument showing that the fan cannot repeatedly pay the positive `H_vartheta` increments required by matched first-layer takeovers while also accommodating the higher-layer/fringe transitions that interrupt them.
