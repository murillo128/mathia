# RE-040 — compact threshold fans are uniformly regular and CA-capacity constrained

**Status:** `EXACT-DERIVED + QUANTITATIVE-RH-FAILURE + SAME-BLOCK-UNIFORM-REGULARITY + UNIFORM-NONLINEAR-PRIME-RACE + EXACT-CA-SUPPORT-CAPACITY + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`. `RE-038` puts every admissible threshold exponent in a compact interval on the same finite Robin-counterexample blocks, but conservatively left open whether the adaptive maximizers could be made regular on one common sequence of blocks. `RE-039` then showed that the convex-envelope fan alone is algebraically universal. The missing bridge is in fact available from the exact CA support geometry: **on every sufficiently late common block, every adaptive amplitude maximizer is regular for every threshold in the compact interval, simultaneously.**

This removes the fixed-parameter extraction gap in `RE-038`. It also gives an exact arithmetic capacity budget absent from the synthetic control of `RE-039`: the threshold cell carried by one exposed CA state must fit inside the image of that state's genuine adjacent CA supporting-slope interval.

Assume RH is false and put

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>\frac12.
\tag{1}
\]

Fix once and for all

\[
J=[b_0,b_1]\Subset(1-\Theta,1/2).
\tag{2}
\]

Take the infinite family of finite positive CA counterexample blocks supplied by `RE-038` from one quantitative left-endpoint threshold `b_0`. For a block `\mathcal B` and `b\in J`, let `C` be any maximizer of

\[
A_b(C):=Y^b\bigl(e^{h(C)}-1\bigr),
\qquad
Y:=\log C,
\qquad
h(C):=\log G(C)-\gamma>0.
\tag{3}
\]

Write

\[
a(C):=1-e^{-h(C)},
\qquad
g(x):=\frac1{x\log x},
\tag{4}
\]

and let `epsilon_-(C)` and `epsilon_+(C)` be the CA supporting slopes on the immediately preceding and following CA transitions. Then, on every sufficiently late block, simultaneously for every `b\in J` and every maximizer `C`,

\[
\boxed{
\varepsilon_+(C)
<g(Y)-\frac{b\,a(C)}Y
<\varepsilon_-(C).
}
\tag{5}
\]

Consequently there is a unique real `Z_b(C)>Y` satisfying

\[
\boxed{
g(Z_b(C))=g(Y)-\frac{b\,a(C)}Y,}
\tag{6}
\]

and the ordinary CA event selector at that parameter chooses exactly `C`:

\[
\boxed{Y=\Phi(Z_b(C)).}
\tag{7}
\]

Thus the whole same-block threshold fan of `RE-038`, including all breakpoint ties, already lives inside genuine regular CA chambers. No diagonal extraction in `b` is needed.

There are two consequences. First, the translated nonlinear prime-race law of `RE-037` becomes uniform on the entire compact threshold fan. With

\[
L_b:=\log Z_b,
\qquad
U(Z):=\frac{Z-\vartheta(Z)}{\sqrt Z},
\qquad
V(Z):=E(Z)\sqrt Z\log Z,
\tag{8}
\]

where

\[
E(Z)=\sum_{p\le Z}-\log(1-p^{-1})-\gamma-\log\log Z,
\tag{9}
\]

and `Psi` is the exact nonlinear function of `RE-036`, the common blocks satisfy

\[
\boxed{
\sup_{b\in J}
\left|
V(Z_b)
-\sqrt{Z_b}L_b\,
\Psi_{b,L_b}\!\left(
\frac{U(Z_b)}{\sqrt{Z_b}L_b}
\right)
-\sqrt2\,\frac{2b-1}{b}
\right|
\longrightarrow0.
}
\tag{10}
\]

Here `Z_b` means the parameter of the rightmost maximizer, with the same convention as `RE-038`; at a breakpoint (10) also holds for every tied maximizer separately.

Second, let

\[
I_C:=\{b\in J:C\text{ is the rightmost maximizer of }A_b
\text{ on }\mathcal B\}.
\tag{11}
\]

Then (5) gives the exact containment

\[
\boxed{
I_C\subset
\left(
\frac{Y\bigl(g(Y)-\varepsilon_-(C)\bigr)}{a(C)},
\frac{Y\bigl(g(Y)-\varepsilon_+(C)\bigr)}{a(C)}
\right).
}
\tag{12}
\]

Therefore

\[
\boxed{
|I_C|
\le
\frac{Y\bigl(\varepsilon_-(C)-\varepsilon_+(C)\bigr)}{a(C)}.
}
\tag{13}
\]

Since the exposed threshold cells partition `J` up to their finitely many endpoints,

\[
\boxed{
b_1-b_0
\le
\sum_{C\in\mathcal E(\mathcal B,J)}
\frac{Y_C\bigl(\varepsilon_-(C)-\varepsilon_+(C)\bigr)}
{1-e^{-h(C)}}.
}
\tag{14}
\]

The sum is over the distinct exposed CA states of the blockwise fan. Equation (14) is the promised **CA support-capacity budget**. Unlike the secant identities of `RE-038`, it cannot be manufactured from the Robin heights and intrinsic coordinates alone: it depends on the genuine prime-power event staircase through the adjacent CA support slopes.

## 1. The common counterexample blocks enter a uniform small-height regime

`RE-038` fixes `b_0` and uses Robin's quantitative false-RH theorem to obtain infinitely many distinct positive CA blocks containing states `N` with

\[
A_{b_0}(N)\ge c_0
\tag{15}
\]

for one constant `c_0>0`. These blocks escape to infinity. On any one of them, for every `b\in J`, a blockwise maximizer `C` satisfies

\[
A_b(C)\ge A_b(N)
=Y_N^{b-b_0}A_{b_0}(N)
\ge c_0.
\tag{16}
\]

The small-height estimate reconstructed in `RE-034` is global over sufficiently large positive CA states:

\[
\boxed{h(C)\log Y_C\to0.}
\tag{17}
\]

Because every state on the late blocks has `Y_C\to\infty`, (17) holds uniformly over all states selected by all `b\in J`. In particular, with

\[
R_C:=e^{h(C)}-1,
\tag{18}
\]

we have uniformly

\[
R_C\log Y_C\to0,
\qquad
a(C)=h(C)(1+o(1)).
\tag{19}
\]

The quantitative inheritance (16) also supplies a useful uniform lower scale. Since `A_b(C)=Y_C^bR_C>=c_0`,

\[
R_C\ge c_0Y_C^{-b}
\ge c_0Y_C^{-b_1}.
\tag{20}
\]

Hence, on late blocks,

\[
\boxed{h(C)\gg_J Y_C^{-b_1}}
\tag{21}
\]

uniformly over the fan.

## 2. Strict concavity makes every blockwise maximizer regular, including ties

Fix a late block, `b\in J`, and any maximizer `C` of (3). Put

\[
c:=A_b(C)=Y^b(e^h-1)
\tag{22}
\]

and use the exact adaptive barrier of `RE-034`,

\[
\tau_{b,c}(x):=\log(1+cx^{-b}),
\qquad
H_{b,c}(x):=\log\log x+\tau_{b,c}(x).
\tag{23}
\]

For every CA state `D` in the same positive block, maximality is exactly

\[
h(D)-\tau_{b,c}(\log D)\le0,
\tag{24}
\]

with equality at `C`. The immediate CA states outside the positive block have `h\le0<\tau_{b,c}`, so (24) also supplies the local comparison if `C` is at a block endpoint. No uniqueness of the amplitude maximum is required.

The derivative is

\[
H'_{b,c}(x)
=g(x)-\frac{bc}{x(x^b+c)}.
\tag{25}
\]

At `x=Y`, equation (22) gives

\[
\boxed{
H'_{b,c}(Y)=g(Y)-\frac{b(1-e^{-h})}{Y}
=g(Y)-\frac{b\,a(C)}Y.
}
\tag{26}
\]

The second derivative of the barrier is

\[
\tau''_{b,c}(x)
=
\frac{bc((b+1)x^b+c)}{x^2(x^b+c)^2}.
\tag{27}
\]

As in `RE-034`, consecutive CA neighbors lie at logarithmic distance `O(\log Y)` once the state is positive and large. On that whole neighboring interval, compactness of `J` and (19) give uniformly

\[
\frac{\tau''_{b,c}(x)}{|(\log\log x)''|}
=O_J(R_C\log Y)=o(1).
\tag{28}
\]

Thus `H_{b,c}` is strictly concave around every selected state, uniformly for `b\in J` on sufficiently late blocks.

Let `A<C<B` be the adjacent CA states and put `x=\log A`, `y=\log B`. The exact CA support identities are

\[
\log\rho(C)-\log\rho(A)
=\varepsilon_-(C)(Y-x),
\tag{29}
\]

\[
\log\rho(B)-\log\rho(C)
=\varepsilon_+(C)(y-Y).
\tag{30}
\]

The local maximality in (24) gives

\[
\varepsilon_-(C)
\ge
\frac{H_{b,c}(Y)-H_{b,c}(x)}{Y-x}
>H'_{b,c}(Y),
\tag{31}
\]

where the final inequality is strict concavity. Similarly,

\[
\varepsilon_+(C)
\le
\frac{H_{b,c}(y)-H_{b,c}(Y)}{y-Y}
<H'_{b,c}(Y).
\tag{32}
\]

Together with (26), these are exactly (5).

This also handles a threshold breakpoint. If several states tie for the global maximum of `A_b`, each one separately satisfies (24), so every tied maximizer obeys the strict support inequality (5). The rightmost convention in `RE-038` is useful for defining a single fan but is not needed for regularity itself.

Since `g` is strictly decreasing, (5) defines a unique `Z_b(C)>Y` by (6). The CA supporting interval then says that `C` is the unique CA maximizer at parameter `g(Z_b(C))`. By the event representation of `RE-001`, this is equivalent to (7).

Thus the simultaneous-regularity caveat in `RE-038` was conservative: once the compact interval is fixed, the same strict-concavity argument used there pointwise is uniform enough to regularize the whole fan on each sufficiently late block.

## 3. The translated nonlinear race law is uniform over the fan

The compact parameter interval also removes the apparent need to apply `RE-037` one threshold at a time. From the exact tangent equation (6),

\[
\frac{g(Y)-g(Z_b)}{g(Y)}
=b\,a(C)\log Y=o_J(1)
\tag{33}
\]

uniformly, hence

\[
\frac{Z_b}{Y}\to1
\tag{34}
\]

uniformly over all selected states and thresholds. The mean-value theorem and (19) give

\[
\boxed{
Z_b-Y=(b+o_J(1))h(C)Y\log Y.
}
\tag{35}
\]

Using (21),

\[
Z_b-Y\gg_J Y^{1-b_1}\log Y,
\tag{36}
\]

which dominates `\sqrt Y` because `b_1<1/2`. Therefore all square-root CA corrections used in `RE-036`--`RE-037` are uniformly lower order relative to the selected displacement.

More directly, the proof of `RE-037` starts from the exact identity

\[
\mathcal R_b(Z)
:=
V(Z)-\sqrt ZL\,
\Psi_{b,L}\!\left(\frac{U(Z)}{\sqrt ZL}\right),
\tag{37}
\]

and decomposes it into the finite-exponent tail and the change from continuous CA displacement to the physical Chebyshev coordinate. Its two source-independent CA limits are

\[
\frac{\Phi_{\ge2}(Z)}{\sqrt Z}\to\sqrt2,
\qquad
\sqrt Z\log Z\,T(C)\to\sqrt2.
\tag{38}
\]

These limits depend on `Z`, not on `b`. The remaining derivative satisfies

\[
\Psi'_{b,L}(q)
\to\frac{1-b}{b}
\tag{39}
\]

uniformly when `b\in J` and `Lq\to0`; compactness keeps `1/b` bounded, while (33)--(36) give the required small-argument regime uniformly. Endpoint corrections are also uniform and vanish after the same normalization.

Consequently

\[
\sup_{b\in J}
\left|
\mathcal R_b(Z_b)
-
\left(
\sqrt2-rac{1-b}{b}\sqrt2
\right)
\right|
\to0,
\tag{40}
\]

which is exactly (10). In particular the source/selector coupling identified as the live target in `MI-001` now holds on one common sequence of actual counterexample blocks, not on unrelated fixed-`b` subsequences.

The coordinates remain quantitatively large uniformly. Equations (35)--(38) and the exact Euler-product identity give

\[
U(Z_b),\ V(Z_b)
\gg_J Z_b^{1/2-b_1}\log Z_b.
\tag{41}
\]

Thus (10) is not a statement near the origin: the entire compact fan must hit the translated nonlinear prime-race family to vanishing additive error while both coordinates diverge.

## 4. The same proof gives an exact threshold-capacity law for CA chambers

For a fixed selected state `C`, equations (5) and (26) can be solved directly for the admissible threshold exponent. Since `a(C)>0`,

\[
\varepsilon_+(C)
<g(Y)-\frac{ba(C)}Y
<\varepsilon_-(C)
\tag{42}
\]

is equivalent to

\[
\boxed{
\frac{Y(g(Y)-\varepsilon_-(C))}{a(C)}
<b<
\frac{Y(g(Y)-\varepsilon_+(C))}{a(C)}.
}
\tag{43}
\]

Every `b` in the rightmost selection cell `I_C` must satisfy (43), proving (12)--(13).

At a switch exponent `beta(C,D)` from `RE-038`, the two exposed states are both amplitude maximizers. Hence the same argument applies to both at the tie and yields the stronger coupling

\[
\boxed{
\beta(C,D)\in K_C\cap K_D,
}
\tag{44}
\]

where

\[
K_C:=
\left(
\frac{Y_C(g(Y_C)-\varepsilon_-(C))}{a(C)},
\frac{Y_C(g(Y_C)-\varepsilon_+(C))}{a(C)}
\right).
\tag{45}
\]

But `RE-038` already gives the same switch exactly from the Robin heights,

\[
\boxed{
\beta(C,D)
=
\frac{
\log(e^{h(C)}-1)-\log(e^{h(D)}-1)
}{
\log Y_D-\log Y_C
}.
}
\tag{46}
\]

Equations (44)--(46) are a direct algebraic/arithmetic splice: one scalar determined by the height secant must simultaneously lie in the genuine CA support chambers of both exposed states.

Finally the cells `I_C` cover `J` and have disjoint interiors. Summing (13) gives (14). This is precisely the extra datum missing from `RE-039`. Its synthetic construction can prescribe `Y_C`, `h(C)`, breakpoints, small heights and even the tangent displacement, but it has no free right to assign CA supporting intervals whose normalized capacities satisfy (43)--(46).

A useful extreme case is a fan consisting of one state throughout `J`. Then (13) forces

\[
\boxed{
\varepsilon_-(C)-\varepsilon_+(C)
\ge
(b_1-b_0)\frac{1-e^{-h(C)}}Y.
}
\tag{47}
\]

After inverting `g`, this means that a single-state fan requires a correspondingly large genuine event chamber at the adaptive displacement scale. More generally, if only a bounded number of states carry the fan, at least one of them must consume a fixed fraction of the total support capacity.

## 5. Stress tests and remaining escape routes

The capacity budget is a necessary condition, not yet an exclusion theorem. Nothing currently proves that the right side of (14) is eventually smaller than `b_1-b_0`. A block may evade a single wide chamber by exposing many CA states with smaller cells; `RE-039` already warned that the number of switches can diverge without violating the affine-envelope geometry.

Nor does (10) by itself contradict the finite spectral controls. `RE-033`--`RE-037` show that a finite dominant packet can hit every fixed translated nonlinear target in recurrent logarithmic windows. The new requirement is stronger because the whole fan is now tied simultaneously to actual CA chambers and exact switch secants. A matched control would have to realize the continuum relation (10) **and** the support-capacity constraints (43)--(46) on one block. No such control has been constructed here.

The quantitative scale also shows why current ordinary prime-gap technology does not immediately close the argument. From (21) and (35), a threshold cell of fixed positive width can demand a chamber on the `Y^{1-b}` displacement scale, which is super-square-root but may still lie above known unconditional short-interval resolution when `b` is very close to `1/2`. The existing `0.52` short-interval anchor in `SOURCES.md` therefore supplies useful comparisons in parts of the admissible range but not a uniform contradiction for every possible false-RH value of `Theta`.

No claim is made that the support-capacity sum is additive in physical event lengths; (14) is exactly a budget in **threshold-exponent space**. Converting it to a strong event-count or prime-gap lower bound requires controlling the nonlinear inverse `g` and the variation of `h(C)` across exposed states. Those are separate obligations.

## 6. Prior-art boundary and research consequence

The load-bearing external inputs are unchanged: Robin supplies the quantitative false-RH excursions and the CA counterexample-block behavior; Alaoglu--Erdos supplies the CA variational/supporting-slope framework. Musin is the nearest convex-envelope prior-art boundary, while the current standard/reciprocal prime-race literature bounds the source-side novelty claims already recorded for `RE-036`--`RE-039`.

A targeted search for colossally abundant supporting-parameter intervals, Robin local maxima, adaptive threshold envelopes and highest-abundant convex geometry found the classical CA definition, extremely/highest abundant variants, and Musin-style envelope organization, but no source imposing the compact family `A_b(C)=Y_C^b(e^{h(C)}-1)` on one Robin-counterexample block and deriving the normalized support-capacity constraint (12)--(14), nor the uniform translated race relation (10). No new theorem is load-bearing, so `SOURCES.md` does not require expansion.

The novelty boundary is deliberately narrow. Strict concavity turning a local maximum into an interior supporting slope is the same elementary mechanism already used in `RE-001` and `RE-034`; compactness arguments are not claimed as new mathematics. The line-specific gain is recognizing that these estimates are uniform over the entire `RE-038` threshold fan and therefore eliminate its last fixed-parameter extraction gap. The result also turns the genuine CA support interval into a quantitative resource consumed by each threshold cell.

The live problem is consequently sharper. `RE-039` proves that selector kinematics are freely programmable, while this finding proves that the actual false-RH fan must additionally satisfy **simultaneous vanishing-width prime-race calibration plus the exact CA support-capacity budget**. A closing theorem can now target that joint object directly: bound the total capacity available on a quantitative counterexample block, force too many or too-wide event chambers, or construct a matched arithmetic/spectral control showing that even this strengthened coupling remains realizable.