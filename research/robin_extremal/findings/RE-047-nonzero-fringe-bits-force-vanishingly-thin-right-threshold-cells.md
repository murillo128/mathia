# RE-047 — nonzero fringe bits force vanishingly thin right threshold cells

**Status:** `EXACT-DERIVED + QUANTITATIVE-RH-FAILURE + SAME-BLOCK-FAN-KINEMATICS + FIRST-LAYER-EVENT-QUANTIZATION + THRESHOLD-CELL-THINNING + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`. `RE-045` isolates a binary upper-fringe datum at one adjacent first-layer breakpoint of the false-RH threshold fan, and `RE-046` shows that a nonzero fringe bit cannot be followed through the same exposed state by the immediate clean first-layer successor switch. There is a stronger quantitative consequence: **if the bit is nonzero, the threshold cell entered at that switch has only a vanishingly small amount of parameter space left on its right.**

Assume RH is false, fix

\[
J=[b_0,b_1]\Subset(1-\Theta,1/2),
\tag{1}
\]

and work on one sufficiently late common positive CA counterexample block from `RE-040`. Let `beta` be an interior breakpoint at which the rightmost adaptive fan makes a unique adjacent first-layer switch

\[
C_-<C_+,
\qquad
C_+=pC_-,
\tag{2}
\]

through the ordinary prime `p`. Put

\[
C:=C_+,
\qquad
Y:=\log C,
\qquad
h:=\log G(C)-\gamma>0,
\qquad
a:=1-e^{-h}.
\tag{3}
\]

Let `I_C^+` be the maximal interval to the right of `beta`, truncated at `b_1` if necessary, on which `C` remains the rightmost fan maximizer; write its right endpoint as `beta_C`, so its right-hand width is

\[
\ell_C^+:=\beta_C-\beta.
\tag{4}
\]

For each `b` in this cell, `RE-040` gives the exact regular tangent selector `Z_C(b)` by

\[
\boxed{
g(Z_C(b))
=g(Y)-\frac{ba}{Y},
\qquad
g(x)=\frac1{x\log x}.}
\tag{5}
\]

Let `p^+` be the next ordinary prime after `p`, and let

\[
\chi_p=\mathbf 1_{\{p^+\le Z_C(\beta)\}}
\tag{6}
\]

be the fringe bit of `RE-045`. If

\[
\boxed{\chi_p=1,}
\tag{7}
\]

then

\[
\boxed{
\ell_C^+
\le
\frac{\eta_{p^+}-Z_C(\beta)}
{\inf_{b\in I_C^+}Z_C'(b)}
<
\frac{1}{2\inf_{b\in I_C^+}Z_C'(b)}.
}
\tag{8}
\]

Moreover, uniformly over such switches escaping to infinity,

\[
\boxed{
Z_C'(b)
=(1+o_J(1))aY\log Y
}
\tag{9}
\]

throughout the right cell. Consequently

\[
\boxed{
\ell_C^+
\le
\frac{1+o_J(1)}{2aY\log Y}
\ll_J
\frac{Y^{b_1-1}}{\log Y}.
}
\tag{10}
\]

Since `RE-043` gives `Y\asymp p` on this adjacent first-layer subfamily and `b_1<1/2`, equivalently

\[
\boxed{
\ell_C^+
\ll_J
\frac{p^{b_1-1}}{\log p}
=o_J(p^{-1/2}).
}
\tag{11}
\]

Thus a nonzero upper-fringe prime cannot occur in the interior of an ordinary-size exposed threshold cell. It is a **threshold-space boundary-layer phenomenon**: after the fan enters `C`, it must leave `C`—or hit the endpoint `b_1` of the monitored compact threshold interval—within `O_J(p^{b_1-1}/\log p)` of the switch exponent.

This strengthens `RE-046` without using any improvement to the translated prime-race remainder. `RE-046` says that `chi_p=1` forces some interruption before a clean `p^+` successor can be exposed. The present result says that the interruption is forced to occur in a quantitatively collapsing threshold interval.

## 1. A nonzero fringe bit leaves less than half a unit of physical selector travel

At the breakpoint `beta`, the upper tied selector is exactly

\[
Z_C(\beta)=Z_+(p;\beta).
\tag{12}
\]

`RE-044` proves the physical ordering

\[
p<\eta_p<Z_+(p;\beta)<\eta_{p^+}.
\tag{13}
\]

If `chi_p=1`, then by definition

\[
p^+\le Z_C(\beta)<\eta_{p^+}.
\tag{14}
\]

The first-layer event of `p^+` satisfies the exact CA threshold equation

\[
g(\eta_{p^+})
=
\frac{\log(1+(p^+)^{-1})}{\log p^+}.
\tag{15}
\]

The elementary inversion used in `RE-042`--`RE-044` gives, for all sufficiently large `p`,

\[
0<\eta_{p^+}-p^+<\frac12.
\tag{16}
\]

Therefore

\[
\boxed{
0<\eta_{p^+}-Z_C(\beta)<\frac12.
}
\tag{17}
\]

Now keep `C` fixed and increase the threshold exponent `b` inside `I_C^+`. By `RE-040`, whenever `C` is selected, `Z_C(b)` lies in the genuine open CA chamber selecting `C`. The next CA event after that chamber occurs no later than the future first-layer event `eta_(p^+)`: an intervening higher-layer or tied event can only end the chamber earlier. Hence for every `b` in the right cell,

\[
\boxed{Z_C(b)<\eta_{p^+}.}
\tag{18}
\]

Combining (17)--(18), the entire selector motion available to this cell after `beta` is less than one half in the physical `Z` coordinate. This statement already includes the exceptional-transition escape from `RE-046`: if a higher-layer or tied event intervenes, the available distance becomes even smaller.

## 2. The fixed-state adaptive selector moves rapidly in threshold space

Differentiate the exact selector equation (5). Since

\[
g'(x)
=-\frac{\log x+1}{x^2(\log x)^2},
\tag{19}
\]

we obtain the exact positive velocity

\[
\boxed{
Z_C'(b)
=
\frac{a}{Y|g'(Z_C(b))|}
=
\frac{aZ_C(b)^2(\log Z_C(b))^2}
{Y(\log Z_C(b)+1)}
>0.
}
\tag{20}
\]

`RE-040` proves uniformly over the entire compact fan that

\[
\frac{Z_C(b)}Y\to1.
\tag{21}
\]

Substituting (21) into (20) gives uniformly on `I_C^+`

\[
\frac{Z_C'(b)}{aY\log Y}
=
\left(\frac{Z_C(b)}Y\right)^2
\frac{(\log Z_C(b))^2}
{\log Y\,(\log Z_C(b)+1)}
=1+o_J(1),
\tag{22}
\]

which proves (9).

There is also a uniform lower scale for `a`. The quantitative inheritance in `RE-040` gives, for every selected state on sufficiently late common blocks,

\[
e^h-1\gg_J Y^{-b_1},
\tag{23}
\]

while the uniform small-height regime gives `h log Y -> 0` and hence

\[
a=1-e^{-h}=h(1+o_J(1))=(e^h-1)(1+o_J(1)).
\tag{24}
\]

Thus

\[
\boxed{a\gg_J Y^{-b_1}.}
\tag{25}
\]

Equations (20)--(25) show that one unit of threshold motion would move the selector by at least order

\[
Y^{1-b_1}\log Y,
\tag{26}
\]

which diverges faster than `sqrt(Y) log Y`. A nonzero fringe bit leaves less than `1/2` unit of physical room, so the corresponding threshold cell must collapse.

## 3. Integrating the selector velocity gives the cell-width bound

For any `b` with

\[
\beta<b<\beta_C,
\]

monotonicity and (18) give

\[
\int_\beta^b Z_C'(u)\,du
=Z_C(b)-Z_C(\beta)
<\eta_{p^+}-Z_C(\beta).
\tag{27}
\]

Therefore

\[
(b-\beta)
\inf_{u\in I_C^+}Z_C'(u)
<\eta_{p^+}-Z_C(\beta).
\tag{28}
\]

Letting `b` increase to the right endpoint proves the first inequality in (8); (17) proves the second. Combining with (9) yields

\[
\ell_C^+
\le
\frac{1+o_J(1)}{2aY\log Y},
\tag{29}
\]

and (25) gives the second estimate in (10).

If `C` loses the fan maximum before its CA selector reaches the next physical chamber boundary, the inequality is strict with additional slack. If `I_C^+` is truncated by `b_1`, the same proof bounds the distance from `beta` to that endpoint. If the right cell degenerates at a multiway fan tie, `ell_C^+=0` and the conclusion is immediate.

The theorem therefore does not require the next fan breakpoint itself to correspond to `p^+`, or even to an adjacent CA transition. It only uses the fact that `eta_(p^+)` is an unavoidable future physical event and hence an absolute ceiling for the selector while `C` remains selected.

## 4. Stress tests and what this does not prove

The estimate is not a hidden prime-gap theorem. Once `chi_p=1`, only the universal first-layer staggering

\[
0<\eta_{p^+}-p^+<1/2
\]

enters the numerator. The size of the ordinary gap `p^+-p` has already been absorbed into the fact that the upper selector crossed `p^+`. An earlier higher-layer CA event only strengthens the bound.

The conclusion also does not imply that nonzero fringe bits are rare in **fan count**. A compact threshold interval can contain many disjoint cells whose widths tend rapidly to zero, and `RE-004`'s zero transition-count density for higher-layer events does not by itself control their frequency inside the highly selected false-RH fan. No summability or lower bound for generic fan-cell widths is proved here.

Likewise, no occurrence theorem for `chi_p=1` is obtained. All currently exposed clean chains may have `chi_p=0`, consistently with `RE-046`. The result is conditional on a nonzero bit and says exactly what geometry that bit forces if it occurs.

Finally, the theorem uses no rate improvement in the uniform nonlinear prime-race law of `RE-040`. The residual quantum of `RE-045` may remain below the known race-error floor; the cell-thinning conclusion comes instead from exact selector kinematics plus the common-source location of the next prime event.

This is a useful matched-control boundary. An abstract affine fan can manufacture arbitrary breakpoint patterns as in `RE-039`, and an abstract support staircase can satisfy the chamber inequalities as in `RE-041`. The new estimate becomes source-specific only when the upper-fringe ordinary prime is identified with the same `p^+` whose physical CA first-layer event lies less than one half unit later.

## 5. Prior-art boundary

The CA supporting-slope and exponent-threshold structure used here is classical Alaoglu--Erdos material already anchored in `SOURCES.md`. Mantovanelli's recent prime-layer workload framework supplies the closest event-coordinate representation, and Zimov studies neighboring consecutive-CA transition constraints; those boundaries are already recorded in the line. A targeted current search also finds recent work on explicit windows for hypothetical CA counterexamples, but not an adaptive-threshold result of the form (8)--(11).

No new external theorem is load-bearing. The mathematical delta is the combination of the exact fixed-state selector velocity from `RE-040`, the fringe-prime localization of `RE-044`--`RE-045`, and the common-source fact that the next ordinary prime has a first-layer CA event within one half unit. `SOURCES.md` therefore requires no new dependency.

## Consequence

`RE-046` relocates every possible nonzero fringe quantum to a break of the clean adjacent-first-layer chain. `RE-047` sharpens that relocation: **the fan must encounter the break essentially immediately in threshold space**, on a scale at most

\[
O_J\!\left(\frac{p^{b_1-1}}{\log p}\right).
\tag{30}
\]

The next useful obstruction would have to show that the false-RH fan cannot support enough such collapsing interruption cells—for example by deriving a source-specific lower width, a summability restriction, or a capacity bound for the higher-layer/tied states that can terminate them. Ambient sparsity alone is not enough, but the exceptional-host problem has now acquired a quantitative threshold-space scale rather than merely a qualitative chain break.