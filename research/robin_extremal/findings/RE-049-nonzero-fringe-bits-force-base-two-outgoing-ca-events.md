# RE-049 — nonzero fringe bits force base-two outgoing CA events

**Status:** `EXACT-DERIVED + QUANTITATIVE-RH-FAILURE + CURVATURE-CLEARANCE + BASE-2-EVENT-REDUCTION + LOGARITHMIC-HOST-SPARSITY + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`. `RE-048` pins every nonzero first-layer fringe switch to the final `O(1/log p)` fraction of the genuine CA support chamber of the entered state, but leaves the outgoing physical event completely unclassified. Strict concavity of the same adaptive barrier now supplies the missing lower clearance: a selected tangent cannot approach the outgoing support event more closely than one half of the logarithmic mass of that event. Combining that fact with the sub-half-unit fringe window collapses the outgoing CA transition to a single possibility.

Assume RH is false, fix

\[
J=[b_0,b_1]\Subset(1-\Theta,1/2),
\]

and work on one sufficiently late common positive CA counterexample block from `RE-040`. Let `beta` be an interior breakpoint at which the rightmost adaptive fan makes a unique adjacent first-layer switch

\[
C_-<C,
\qquad C=pC_-,
\tag{1}
\]

through the ordinary prime `p`. Put

\[
Y=\log C,
\qquad h=\log G(C)-\gamma>0,
\qquad a=1-e^{-h},
\tag{2}
\]

and let `Z=Z_C(beta)` be the upper adaptive tangent selector,

\[
g(Z)=g(Y)-\frac{\beta a}{Y},
\qquad g(x)=\frac1{x\log x}.
\tag{3}
\]

Let `D` be the immediate next CA state after `C`, write

\[
\Delta:=\log D-\log C=\log(D/C)>0,
\tag{4}
\]

and let `xi` be the outgoing CA event coordinate, so that

\[
\varepsilon_+(C)=g(\xi).
\tag{5}
\]

Then every sufficiently late selected state satisfies the asymptotic **curvature-clearance inequality**

\[
\boxed{
\xi-Z\ge\left(\frac12-o_J(1)\right)\Delta.
}
\tag{6}
\]

Now let `p^+` be the next ordinary prime and retain the fringe bit

\[
\chi_p:=\mathbf 1_{\{p^+\le Z\}}.
\tag{7}
\]

If

\[
\boxed{\chi_p=1,}
\tag{8}
\]

then `RE-048` gives

\[
0<\xi-Z<\frac12.
\tag{9}
\]

Equations (6) and (9) imply

\[
\Delta<1+o_J(1).
\tag{10}
\]

But `D/C` is an integer product of the prime-layer atoms firing at the next CA event. Hence, for every sufficiently late nonzero-fringe switch,

\[
\boxed{\frac DC=2.}
\tag{11}
\]

The outgoing event is therefore neither an ordinary next-prime event, nor a generic higher-layer event, nor a tied transition. It is a **single base-two layer event**:

\[
\boxed{\xi=\eta_{2,j}}
\tag{12}
\]

for some layer `j->infinity`.

This gives a second source-specific quantization. Since `RE-048` also gives

\[
p^+\le Z<\xi\le\eta_{p^+,1}<p^++\frac12
\tag{13}
\]

for all sufficiently large switches, while (6) and (11) give

\[
\xi-Z\ge\frac{\log2}{2}-o_J(1),
\tag{14}
\]

we obtain

\[
\boxed{
\left\lfloor\eta_{2,j}\right\rfloor=p^+,
\qquad
\frac{\log2}{2}-o_J(1)
\le
\{\eta_{2,j}\}
<\frac12.
}
\tag{15}
\]

Thus a nonzero fringe bit can occur only when a deep event of the fixed base-`2` CA ladder lands in a narrow right-half subinterval above an ordinary prime, and that prime must be exactly the successor of the prime generating the incoming fan switch.

The host set is consequently logarithmically sparse. If `N_1(X)` denotes the number of sufficiently late nonzero-fringe switches from these common fans whose outgoing event satisfies `xi<=X`, then

\[
\boxed{N_1(X)=O(\log X).}
\tag{16}
\]

More precisely, distinct nonzero-fringe switches inject into distinct base-two layers, and

\[
N_1(X)
\le
\log_2 X+O(\log\log X).
\tag{17}
\]

The corresponding physical host coordinates are multiplicatively lacunary: if `xi_n` are the distinct hosts in increasing order, then

\[
\boxed{
\liminf_{n\to\infty}\frac{\xi_{n+1}}{\xi_n}\ge2.
}
\tag{18}
\]

Equivalently, the generating primes of successive nonzero-fringe switches have the same asymptotic lacunarity because `p~p^+~xi`.

## 1. Maximality gives a lower bound on the distance to the outgoing support event

At the breakpoint `beta`, put

\[
c:=A_\beta(C)=Y^\beta(e^h-1)>0
\tag{19}
\]

and use the adaptive barrier from `RE-034`, `RE-040`, and `RE-043`,

\[
\tau(x):=\log(1+cx^{-\beta}),
\qquad
H(x):=\log\log x+\tau(x).
\tag{20}
\]

Since `c=Y^\beta(e^h-1)`,

\[
H(Y)=\log\log Y+h.
\tag{21}
\]

Write

\[
F(E):=\log\rho(E)-\gamma
=\log\log(\log E)+h(E)
\tag{22}
\]

on CA states. The immediate successor `D` obeys

\[
h(D)\le\tau(\log D).
\tag{23}
\]

Indeed, if `D` remains in the same positive block, (23) is exactly the maximality of `C` for `A_\beta`; if `D` is the first state outside that block, then `h(D)<=0<\tau(\log D)` and the inequality is even stronger. Therefore

\[
F(D)\le H(Y+\Delta),
\qquad
F(C)=H(Y).
\tag{24}
\]

The physical CA support identity gives

\[
F(D)-F(C)=\varepsilon_+(C)\Delta=g(\xi)\Delta.
\tag{25}
\]

Combining (24)--(25),

\[
g(\xi)
\le
\frac{H(Y+\Delta)-H(Y)}{\Delta}.
\tag{26}
\]

At `Y`, the barrier tangent is exactly the selected slope,

\[
H'(Y)
=g(Y)-\frac{\beta a}{Y}
=g(Z).
\tag{27}
\]

The uniform small-height regime from `RE-040` gives on the whole neighboring CA interval

\[
-H''(x)
=(1+o_J(1))|g'(Y)|.
\tag{28}
\]

Here the already-established neighboring-CA spacing `Delta=O(log Y)` makes `g'` asymptotically constant across the interval, while the positive curvature `tau''` is only `o_J(|g'|)`.

The exact tangent-minus-secant identity is

\[
H'(Y)-
\frac{H(Y+\Delta)-H(Y)}{\Delta}
=
\frac1\Delta
\int_0^\Delta
(\Delta-u)(-H''(Y+u))\,du.
\tag{29}
\]

Using (28),

\[
H'(Y)-
\frac{H(Y+\Delta)-H(Y)}{\Delta}
=
\left(\frac12+o_J(1)\right)|g'(Y)|\Delta.
\tag{30}
\]

Equations (26)--(27) therefore imply

\[
g(Z)-g(\xi)
\ge
\left(\frac12+o_J(1)\right)|g'(Y)|\Delta.
\tag{31}
\]

For the nonzero-fringe configuration, `RE-048` gives `0<xi-Z<1/2` and `Z~Y~p`. The mean-value theorem then gives

\[
g(Z)-g(\xi)
=(1+o_J(1))|g'(Y)|(\xi-Z).
\tag{32}
\]

Cancelling the common derivative scale between (31) and (32) proves (6). Notice that the argument uses the **maximality of the entered amplitude state**, not merely the fact that `Z` lies inside its CA support chamber. An abstract chamber can place a selector arbitrarily close to its right edge; an exposed Robin-amplitude state must still leave enough curvature area to dominate its immediate physical successor.

## 2. Sub-half-unit fringe clearance forces quotient two

Under `chi_p=1`, the next ordinary prime has already crossed the selector while its own first-layer CA event is still pending. `RE-048` gives

\[
p^+\le Z<\xi\le\eta_{p^+,1}<p^++\frac12,
\tag{33}
\]

and hence (9). Combining (6) with (9),

\[
\Delta
\le
(2+o_J(1))(\xi-Z)
<1+o_J(1).
\tag{34}
\]

The CA event representation of `RE-001` writes every transition mass as a sum of prime logarithms. Thus

\[
\Delta=\sum_{(q,k)\text{ firing at }\xi}\log q
=\log Q
\tag{35}
\]

for the integer quotient `Q=D/C>=2`.

Since

\[
1<\log3,
\tag{36}
\]

equation (34) eventually gives `Delta<log3`. The only possible integer quotient is therefore

\[
Q=2,
\]

proving (11). A tied event is impossible because any second atom would make the product quotient at least `2*3>2`; a prime base `q>=3` is impossible because its single mass is at least `log3`. Hence the sole outgoing atom is one exponent increment of the prime `2`, which proves (12).

This classification is substantially stronger than the alternatives left open by `RE-046`--`RE-048`. A nonzero fringe bit does not merely require "some exceptional interruption" before a clean `p^+` exit. The physical event immediately ending the entered CA chamber is forced onto one fixed high-layer ladder.

## 3. The same argument pins the base-two event above a prime

With `Delta=log2`, equation (6) becomes

\[
\xi-Z
\ge
\frac{\log2}{2}-o_J(1).
\tag{37}
\]

Put `q=p^+`. From `chi_p=1`, `q<=Z`, while (33) gives `xi<q+1/2`. Consequently

\[
q+rac{\log2}{2}-o_J(1)
\le
\xi
<q+\frac12.
\tag{38}
\]

For sufficiently large switches the interval in (38) lies strictly inside `(q,q+1)`. Therefore

\[
q=\lfloor\xi\rfloor.
\tag{39}
\]

Since `xi=eta_(2,j)`, this proves the floor-prime and fractional-part restrictions (15).

The width of the allowed fractional window tends to

\[
\frac12-\frac{\log2}{2}
=\frac{1-\log2}{2}
\approx0.1534.
\tag{40}
\]

No equidistribution claim for the fractional parts of `eta_(2,j)` is being made. Equation (15) is a necessary host condition, not an assertion that such layers occur infinitely often. It is nevertheless a much smaller arithmetic target than the unrestricted higher-layer/tied interruption class left by `RE-048`.

## 4. Base-two hosts are logarithmically sparse and geometrically lacunary

For the base-two layer `j`, retain the exact notation from `RE-020`,

\[
S_{2,j}=2+2^2+\cdots+2^j=2^{j+1}-2.
\tag{41}
\]

The exact event equation there gives

\[
\boxed{
S_{2,j}
\le
\frac{\eta_{2,j}\log\eta_{2,j}}{\log2}
\le
S_{2,j}+1.
}
\tag{42}
\]

If `eta_(2,j)<=X`, then

\[
2^{j+1}-2
\le
\frac{X\log X}{\log2},
\tag{43}
\]

so

\[
j
\le
\log_2X+O(\log\log X).
\tag{44}
\]

Each physical CA state has one immediate outgoing event and each state can be entered at most once by the rightmost fan. Distinct nonzero-fringe switches therefore map to distinct base-two layers. Equations (43)--(44) prove (16)--(17).

Moreover (42) yields

\[
\eta_{2,j}\log\eta_{2,j}
=(\log2)2^{j+1}(1+o(1)),
\tag{45}
\]

and hence

\[
\frac{\eta_{2,j+1}}{\eta_{2,j}}\longrightarrow2.
\tag{46}
\]

Any increasing subsequence of distinct base-two layers is at least as lacunary asymptotically, proving (18). Because the first-layer switch geometry gives `p~Z~xi`, the same multiplicative separation transfers to the generating primes of the nonzero-fringe switches.

This is much sharper than the generic zero-density statement for higher layers. A union over all higher-layer prime bases still has roughly square-root-scale complexity at event height `X`; the surviving nonzero fringe hosts have collapsed to one fixed-base ladder with only logarithmically many candidates below `X`.

## 5. Stress tests and boundary of the result

The result does **not** prove that any nonzero fringe bit exists. It only classifies and counts the locations that could host one. If all sufficiently late adjacent first-layer switches have `chi_p=0`, the theorem is vacuous, exactly as `RE-048` is.

Nor does logarithmic host sparsity by itself contradict false RH. The current fan theory supplies no lower bound requiring a positive density, a divergent weighted mass, or even infinitely many nonzero fringe bits. A false-RH fan could in principle place every surviving binary mismatch on a lacunary subsequence of base-two events. The next useful aggregate theorem must therefore force enough fringe mass, or show that the floor-prime/fractional condition (15) is itself too sparse to carry the required common-source race correction.

The curvature-clearance step is load-bearing. Dropping amplitude maximality and retaining only the abstract support interval invalidates (26): a synthetic support staircase may place a selector arbitrarily close to an outgoing event without paying the tangent-secant curvature cost. Thus `RE-041` does not reproduce (6) unless the synthetic heights also satisfy the same next-state amplitude domination at the edge.

The argument does not assume the Alaoglu--Erdos conjecture that every consecutive CA quotient is prime. Equation (35) allows arbitrary tied or multi-atom transitions; the small-mass conclusion then forces the integer quotient to be `2`, which retrospectively makes the outgoing transition unique. This avoids importing the open consecutive-prime-quotient conjecture.

Finally, (18) is a host-count statement in physical event scale, not a density theorem in threshold `b`. The threshold fan may assign highly nonuniform cell widths to the surviving hosts. Any capacity argument still has to use the amplitude/support coupling rather than infer threshold measure directly from `O(log X)` event count.

## 6. Prior-art boundary

Alaoglu--Erdos supplies the classical CA prime-exponent threshold structure and the fact that CA transitions are products of prime-layer atoms; that material is already anchored in `SOURCES.md`. Mantovanelli's 2026 prime-layer workload formulation is the closest current event-coordinate representation, and Zimov studies restrictions coming from consecutive CA quotients. The fixed-base event equation and its exact geometric-sum bracket are already recorded and used in `RE-020`.

A targeted current search found the classical prime/semiprime consecutive-quotient discussion, the recent exact prime-layer workload, and recent Robin-counterexample transition work, but no result coupling an adaptive Robin-amplitude fringe switch to a tangent-secant curvature clearance that **forces the outgoing quotient to equal `2`**, nor the resulting floor-prime condition for deep base-two event coordinates.

No new external theorem is load-bearing. The new content is obtained by combining `RE-040`'s strict adaptive-barrier concavity and local maximality with `RE-048`'s sub-half-unit support-edge window and the exact event quantization of `RE-001`. `SOURCES.md` therefore requires no new dependency.

## Consequence

The exceptional currency isolated by `RE-046`--`RE-048` is no longer an amorphous mixture of skipped states, higher layers, and tied events. **Every nonzero fringe bit forces the entered CA state to exit through the deep base-two ladder, within less than half a physical unit of the next ordinary prime.** Such hosts are only logarithmically numerous and asymptotically doubling in event scale.

This sharpens the live obstruction substantially. A closing argument no longer needs to control all exceptional CA transitions. It can target the one-dimensional sequence `eta_(2,j)`: either show that the prime/fractional window in (15) cannot support the fringe information demanded by a false-RH fan, or prove that any aggregate race correction carried by an `O(log X)` geometrically lacunary host set is too small to reconcile the uniform translated prime-race law.