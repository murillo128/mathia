# WI-174 — The fixed-`p=2500` four-point constant is below `2343/10^6`, leaving less than `8.65e-6` bridge gain

**Status:** `LITERATURE+DERIVED + COMPUTATIONAL-INTERVAL + EXACT-DERIVED + DECISIVE-NEGATIVE + ROUTE-SPECIFIC-BARRIER + NO-NOVELTY-CLAIM`

## Claim

Let

\[
c_*:=\inf_{x,y,z\ge0}F_{4,2500}(x,y,z),
\]

where `F_{4,2500}` is the genuine Montgomery--Taylor four-point functional already matched end to end to the zeta bridge in WI-172:

\[
\begin{aligned}
F_{4,2500}(x,y,z)
={}&\frac{x+y+z}{2500}
+\frac23\bigl(w(x)+w(y)+w(z)\bigr)\\
&+w(x+y)+w(y+z)+2w(x+y+z),
\end{aligned}
\tag{1}
\]

with

\[
w(u)=\left(\frac{K(u)}{K(0)}\right)^2,
\qquad
K(u)=\int_{-1/2}^{1/2}\cos(\sqrt2\,t)\cos(2\pi ut)\,dt.
\tag{2}
\]

WI-172 gives the formally checked lower bound

\[
\frac{2330}{10^6}\le c_*.
\tag{3}
\]

At the explicit rational point

\[
(x,y,z)=\left(\frac{1047}{1000},\frac{1981}{1000},\frac{1047}{1000}\right),
\tag{4}
\]

an independent interval evaluation gives

\[
\begin{aligned}
F_{4,2500}(x,y,z)\in[
&0.002342449310626072708013502450797077339639225722144226885278126956573558602490790612818,\\
&0.002342449310626072708013502450797077339639225722144226885278126956573558602490791485844
].
\end{aligned}
\tag{5}
\]

In particular,

\[
\boxed{
\frac{2330}{10^6}\le c_*<\frac{2343}{10^6}.
}
\tag{6}
\]

Thus the accepted `c=2330/10^6` certificate is already within less than

\[
\boxed{13\times10^{-6}}
\tag{7}
\]

of the true local constant for this exact fixed-pressure functional.

More importantly, after optimizing the block size subject to the same bridge admissibility condition, **raising only this one local constant at fixed `p=2500` can improve WI-172's certified proportion by less than**

\[
\boxed{
8.649429810990894\times10^{-6}.
}
\tag{8}
\]

Equivalently, the best theorem output obtainable by this restricted route is strictly below

\[
\boxed{
B_{\rm cap}
=
\frac{71500000H_{\rm MT}-85600}{71333647}
=
0.6728690082686776503941843186909482699\ldots .
}
\tag{9}
\]

This is a route-specific barrier, not a ceiling on the Weil/inertia program: varying the pressure, changing the local functional/window, using multiple independent profiles, exploiting global source placement, coupling to the exceptional block, or importing genuinely new arithmetic information remain outside the claim.

## 1. Reproducible source-specific upper witness

The integral in (2) has the elementary closed form

\[
K(u)
=
\frac{\sin((\sqrt2-2\pi u)/2)}{\sqrt2-2\pi u}
+
\frac{\sin((\sqrt2+2\pi u)/2)}{\sqrt2+2\pi u},
\tag{10}
\]

with

\[
K(0)=\frac{2\sin(1/\sqrt2)}{\sqrt2}.
\tag{11}
\]

Equation (5) was recomputed from (10)--(11) by outward interval arithmetic at 80 decimal digits, taking the rational decimals in (4) as singleton intervals and evaluating the six distances

\[
x,\ y,\ z,\ x+y,\ y+z,\ x+y+z.
\]

The resulting interval width is below `9e-82`; its upper endpoint is more than `5.50e-7` below `2343/10^6`. This is intentionally classified as `COMPUTATIONAL-INTERVAL`, not as a Lean/kernel-checked theorem. The barrier needs only the coarse strict inequality `F<0.002343`, for which the numerical separation is very large relative to the displayed enclosure.

The point (4) is not a new optimizer claim. The public `teal-sea/zeta-lab` four-point study already reports

\[
\inf F_{4,2500}\approx0.0023423879
\]

near `(1.047, 1.981, 1.047)`. The contribution here is to turn those published approximate coordinates into a simple explicit rational witness, independently enclose its value, and propagate the resulting strict cap through Mathia's corrected bridge bookkeeping.

## 2. Exact propagation through the corrected four-point bridge

For `n=4`, `p=2500`, local constant `c`, and integer block size `m`, the bridge used in WI-172 is

\[
B(c,m)
=
\frac{
H_{\rm MT}-\frac{3(m-1)}{2500m}
}{
1-\frac{c(m-3)}m
},
\qquad
c(m-3)\le1.
\tag{12}
\]

For fixed `m`, `B(c,m)` is increasing in `c` throughout the admissible range. Set

\[
c_0:=\frac{2343}{10^6}.
\]

Because `c_*<c_0`, every possible improvement obtained solely by replacing WI-172's certified constant by a sharper constant for the same `F_{4,2500}` lies below the supremum obtained by allowing `c` up to `c_0` while retaining (12).

For `m\le429`, `c_0(m-3)<1`, so

\[
B(c,m)<B(c_0,m).
\]

Writing `a=3/2500`, the continuous derivative of the right-hand side with respect to `m` has the sign of

\[
3c_0H_{\rm MT}-a-2ac_0.
\tag{13}
\]

Since `H_MT>2/3`, (13) is bounded below by

\[
2c_0-a-2ac_0>0.
\tag{14}
\]

Hence the largest value in this first regime occurs at `m=429`:

\[
B(c_0,429)
=
\frac{71500000H_{\rm MT}-85600}{71333647}.
\tag{15}
\]

For `m\ge430`, admissibility itself is stronger than `c<c_0` and gives

\[
c\le\frac1{m-3}.
\]

Substituting the largest admissible value into (12),

\[
B\left(\frac1{m-3},m\right)
=H_{\rm MT}\frac{m}{m-1}-\frac3{2500},
\tag{16}
\]

which decreases with `m`. Therefore this regime is maximized at `m=430`. The comparison with (15) is exact:

\[
B(c_0,429)-B\left(\frac1{427},430\right)
=
\frac{7225000H_{\rm MT}+36699}{6955030582500}>0.
\tag{17}
\]

Combining the two regimes proves the strict cap (9) for the entire fixed-`p=2500`, same-functional, constant-only refinement route.

## 3. Remaining gain relative to WI-172

WI-172's checked theorem is

\[
B_{2330}
=
\frac{14400000H_{\rm MT}-17240}{14366681}
=
0.6728603588388666595002053005539310517\ldots .
\tag{18}
\]

Subtracting (18) from the cap (15),

\[
B_{\rm cap}-B_{2330}
=
\frac{40(47052500H_{\rm MT}+14931)}{146403964430801}
=
0.0000086494298109908939790181370172182594\ldots .
\tag{19}
\]

Because the true `c_*` is strictly below `c_0`, the actual remaining gain is **strictly less** than (19). Numerically this is less than `0.000865` percentage points.

The point is not that further tightening of `c=2330/10^6` is useless. It can still produce a valid strict improvement. The point is that this exact bounded route has now been quantitatively exhausted: no amount of proving the same fixed-pressure local minimum more accurately can generate a material jump in the certified proportion.

## 4. Prior-art audit and novelty boundary

The public `teal-sea/zeta-lab` `FOUR-POINT.md` already measured the `p=2500` infimum at approximately `0.0023423879` near the coordinates used in (4), and its pressure sweep explicitly showed that changing `p` changes the attainable bridge frontier. No novelty or priority is claimed for the approximate minimizer, the functional, the kernel, the pressure family, or the bridge.

WI-172 already established the exact lower certificate `2330/10^6`, its kernel correspondence, the corrected admissible `m=432`, and the theorem-level value (18). WI-166/WI-171 close the generic positive-weight/Gram relaxations, while WI-026 closes a broader collapsed single-profile pressure-family direction. This finding does not strengthen those barriers.

The durable Mathia-local deduction is narrower: the explicit rational upper witness (4)--(6), together with the exact optimization (12)--(17), quantifies how little room remains in **constant squeezing at fixed `p=2500`**. A targeted audit around the upstream four-point pressure studies and current Mathia findings found the approximate source minimum but not this explicit rational-witness-to-bridge-cap calculation. That absence is not used as a priority claim.

## Consequence for the research line

The active source-constrained clue should not spend further effort merely trying to raise `2330/10^6` toward the exact minimum of the same `F_{4,2500}`. The maximum possible payoff is now below (19). A materially stronger source-specific result has to alter at least one load-bearing ingredient: pressure, window/profile, global placement/assembly, independent source observables, or the coupling to the exceptional indefinite block.

This barrier does not characterize the uncertified complement and does not imply anything like RH. It only kills a weak refinement route cleanly, in the sense required by the canonical research mandate.
