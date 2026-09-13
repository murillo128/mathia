# RE-107 — terminal amplitude floor eliminates whole-fan Chebyshev resets

**Status:** `EXACT-DERIVED + QUANTITATIVE-RH-FAILURE + GLOBAL-RAW-CHEBYSHEV-TRANSPORT + TERMINAL-SELF-HEIGHT-LOWER-BOUND + FRINGE-RESET-ELIMINATION + EXTREME-STRETCH-CLOSED + RE-106-BRANCH-COLLAPSE + PRIOR-ART-AUDITED`.

`RE-106` proves that the endpoint-corrected Chebyshev deficit gains a power-scale amount across every compact threshold fan, but its endpoint conversion deliberately leaves one apparent escape: a final fringe prime can subtract `log r_R`, and making that atom large enough seems to require a super-stretched terminal state on the deep base-two host ladder of `RE-063`. That branch is not actually self-consistent. The same quantitative false-RH amplitude floor that drives the corrected transport also forces the **terminal selected state itself** to sit a power-scale distance to the left of its adaptive selector. Once the terminal scale becomes large enough for `log r_R` to threaten the accumulated debt, this local selector displacement is enormously larger than the entire left-end raw Chebyshev deficit.

The consequence is stronger than the stretch dichotomy of `RE-106`: **the raw Chebyshev deficit gains the same power-scale amount across every sufficiently late compact fan, at every physical stretch.** The super-stretched base-two reset branch is therefore empty. This argument needs only the general compact-fan regime `J \Subset (1-\Theta,1/2)` and does not require the stronger `\Theta>\Theta_*` support-boundary reduction of `RE-102`--`RE-104`.

Assume RH is false and write

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>\frac12.
\tag{1}
\]

Fix

\[
J=[b_0,b_1]\Subset(1-\Theta,\tfrac12),
\qquad
\alpha:=1-b_1>\frac12.
\tag{2}
\]

Work on one sufficiently late common positive rightmost CA fan from `RE-040`. For a selected state `C` at threshold `b`, write

\[
Y_C:=\log C,
\qquad
Z_C:=Z_b(C),
\qquad
H_\vartheta(Z):=Z-\vartheta(Z),
\tag{3}
\]

and let `\delta_\vartheta(C,b)` be the binary first-layer fringe correction of `RE-059`. Let `L` and `R` be the selected points at the left and right endpoints `b_0,b_1` of the fan, with the usual rightmost tie convention, and set

\[
X:=Y_L,
\qquad
W:=Y_R.
\tag{4}
\]

Then there is a constant `c_J>0`, independent of the late block, such that

\[
\boxed{
H_\vartheta(Z_R)-H_\vartheta(Z_L)
\ge
c_J X^{\,1-b_1}\log X.
}
\tag{5}
\]

In particular,

\[
\boxed{
H_\vartheta(Z_R)>H_\vartheta(Z_L)
}
\tag{6}
\]

for every sufficiently late common positive fan. No assumption on the stretch `W/X`, the number of exposed states, packet cardinalities, higher-layer mass, or endpoint fringe pattern is needed.

Thus the reset alternative isolated in `RE-106`,

\[
H_\vartheta(Z_R)\le H_\vartheta(Z_L),
\tag{7}
\]

cannot occur eventually. In particular, the super-stretched terminal branch in which the right endpoint carries a fringe atom and has immediate physical successor quotient `2` is not a genuine asymptotic escape. `RE-063` remains valid as a classification of individual nonzero-fringe hosts; `RE-107` shows only that such a host cannot erase the total raw Chebyshev debt of an entire late compact fan.

## 1. The corrected whole-fan transport works on the full compact false-RH interval

`RE-076` gives the exact corrected coordinate

\[
\widehat H(C,b)
:=H_\vartheta(Z_C)+\delta_\vartheta(C,b)
=Z_C-\log\operatorname{rad}(C)
=(Z_C-Y_C)+P_C,
\tag{8}
\]

where `P_C\ge0` is the active depth-at-least-two event mass. It increases inside every exposed cell and strictly across every exposed switch.

Inside one cell the state is fixed. The tangent equation of `RE-040` is

\[
g(Z_C(b))=g(Y_C)-\frac{b\,a(C)}{Y_C},
\qquad
g(x)=\frac1{x\log x},
\tag{9}
\]

with

\[
a(C)=1-e^{-h(C)}.
\tag{10}
\]

Differentiating exactly,

\[
Z_C'(b)
=
\frac{a(C)}{Y_C[-g'(Z_C(b))]}.
\tag{11}
\]

The quantitative inheritance in `RE-040` gives uniformly over the entire selected fan

\[
e^{h(C)}-1\ge c_0Y_C^{-b}
\ge c_0Y_C^{-b_1},
\tag{12}
\]

while the common small-height regime gives `h(C)\to0`. Hence, after changing the constant,

\[
a(C)\ge c_JY_C^{-b_1}.
\tag{13}
\]

Also `Z_C/Y_C\to1` uniformly. Since

\[
-g'(x)=\frac{\log x+1}{x^2(\log x)^2},
\tag{14}
\]

(11)--(14) yield

\[
\boxed{
Z_C'(b)
\ge
c_JY_C^{1-b_1}\log Y_C.
}
\tag{15}
\]

The rightmost fan is physically oriented, so `Y_C\ge X` throughout the threshold interval. The cell interiors partition `J` up to finitely many breakpoints, and every switch contribution to `\widehat H` is positive by `RE-076`. Integrating (15) over the fixed positive width of `J` therefore gives

\[
\boxed{
\widehat H_R-\widehat H_L
\ge
A_X,
\qquad
A_X:=c_1X^\alpha\log X,
}
\tag{16}
\]

for one `c_1=c_1(J)>0`. This is the transport estimate used in `RE-106`, but its derivation uses only `RE-040` and `RE-076`; the stronger support-boundary hypothesis `\Theta>\Theta_*` is unnecessary.

Returning to the raw deficit,

\[
H_{\vartheta,R}-H_{\vartheta,L}
=(\widehat H_R-\widehat H_L)
+\delta_{\vartheta,L}-\delta_{\vartheta,R},
\tag{17}
\]

so, because `\delta_{\vartheta,L}\ge0`,

\[
\boxed{
H_{\vartheta,R}-H_{\vartheta,L}
\ge
A_X-\delta_{\vartheta,R}.
}
\tag{18}
\]

The only remaining issue is whether the single terminal fringe atom can be as large as `A_X`.

## 2. Every selected endpoint carries its own power-scale raw Chebyshev floor

Fix any selected state `C` at threshold `b\in J`, and abbreviate `Y=Y_C`, `Z=Z_C`. The exact tangent equation (9) gives

\[
\frac{b\,a(C)}Y
=g(Y)-g(Z)
=\int_Y^Z[-g'(t)]\,dt.
\tag{19}
\]

For sufficiently large `t`, the function `-g'(t)` in (14) is decreasing. Therefore

\[
\frac{b\,a(C)}Y
\le
(Z-Y)[-g'(Y)],
\tag{20}
\]

and hence

\[
Z-Y
\ge
\frac{b\,a(C)Y(\log Y)^2}{\log Y+1}.
\tag{21}
\]

Using `b\ge b_0>0` and (13),

\[
\boxed{
Z-Y
\ge
c_JY^\alpha\log Y.
}
\tag{22}
\]

The radical-gap identity (8) now converts this selector displacement into a raw source lower bound. Since

\[
H_\vartheta(Z)
=(Z-Y)+P_C-\delta_\vartheta(C,b),
\qquad P_C\ge0,
\tag{23}
\]

and a nonzero fringe correction has the form `\delta_\vartheta=\log r` with `r\le Z`, always

\[
0\le\delta_\vartheta(C,b)\le\log Z.
\tag{24}
\]

Uniformly `Z/Y\to1`, so `\log Z=\log Y+o(1)`. Because `\alpha>0`, equations (22)--(24) imply the endpoint self-height estimate

\[
\boxed{
H_\vartheta(Z)
\ge
c_2Y^\alpha\log Y
}
\tag{25}
\]

for every sufficiently late selected state, after reducing `c_2>0`.

This is the missing feedback in `RE-106`. Making a fringe atom large requires moving the endpoint to a large physical scale, but the false-RH amplitude floor then forces the selected tangent itself to create a raw Chebyshev deficit of power size in that larger scale. The fringe atom grows only logarithmically in the same scale.

## 3. The terminal fringe cannot reset the fan at either moderate or extreme stretch

Apply (18) at the two fan endpoints. If

\[
\delta_{\vartheta,R}\le\frac12A_X,
\tag{26}
\]

then immediately

\[
H_{\vartheta,R}-H_{\vartheta,L}
\ge\frac12A_X.
\tag{27}
\]

It remains only to treat the case in which the terminal atom is large. By (24),

\[
\delta_{\vartheta,R}>\frac12A_X
\quad\Longrightarrow\quad
\log Z_R>\frac12A_X.
\tag{28}
\]

Since `Z_R/W\to1`, (28) implies, for all sufficiently late blocks,

\[
\log W>\frac13A_X.
\tag{29}
\]

Thus

\[
W>\exp(A_X/3).
\tag{30}
\]

At the right endpoint, (25) gives

\[
H_{\vartheta,R}\ge c_2W^\alpha\log W.
\tag{31}
\]

At the left endpoint no prime-number theorem input is needed: `\vartheta(Z_L)\ge0`, hence

\[
H_{\vartheta,L}=Z_L-\vartheta(Z_L)\le Z_L=(1+o(1))X.
\tag{32}
\]

Combining (29)--(32),

\[
H_{\vartheta,R}-H_{\vartheta,L}
\ge
c_2W^\alpha\log W-(1+o(1))X.
\tag{33}
\]

Because `A_X=c_1X^\alpha\log X` with `\alpha>0`, the lower bound `W>\exp(A_X/3)` makes the first term on the right of (33) exceed both `X` and `A_X` by an arbitrarily large factor. Hence eventually

\[
H_{\vartheta,R}-H_{\vartheta,L}
\ge\frac12A_X
\tag{34}
\]

in this second case as well. Absorbing constants proves (5).

The argument exposes why the apparent super-stretched escape of `RE-106` was self-defeating. `RE-106` priced a reset only by comparing the accumulated corrected debt with the terminal atom `\log r_R`. But the terminal state is itself one of the same quantitative false-RH amplitude maximizers. Enlarging `r_R` enough to pay the old debt simultaneously enlarges `Y_R`, and the local displacement `Z_R-Y_R\gg Y_R^\alpha\log Y_R` then creates a much larger new raw deficit before the fringe subtraction is applied.

## 4. Stress tests and evidence boundary

The argument does not assume any RH-strength estimate for `\vartheta`. The only upper bound used at the left endpoint is the trivial positivity `\vartheta(Z_L)\ge0`. The power-scale lower bound at the right endpoint comes from the false-RH amplitude floor and exact CA selector geometry, not from an external prime-error theorem. Thus (5) is not a disguised prime-number-theorem comparison.

A one-state fan is the first matched control. Then `W=X`, the integrated corrected rise is already `\asymp X^\alpha\log X`, while any fringe atom is only `O(\log X)`; (27) applies. At the opposite extreme, let the terminal state be arbitrarily large. The endpoint correction may then be arbitrarily large in absolute terms, but (25) grows as `W^\alpha\log W`, so the terminal raw deficit eventually dominates both its own fringe atom and the entire left endpoint. There is no intermediate scale left uncovered: (26) and its complement exhaust all possibilities.

The conclusion is about the **net endpoint transport across one compact adaptive fan**. The ordinary function `H_\vartheta(x)=x-\vartheta(x)` is not globally monotone, and fringe crossings may still create local downward jumps inside the fan. `RE-107` does not claim pointwise monotonicity in `x`, monotonicity across every exposed switch, or a contradiction to false RH by itself.

Nor does this remove the need for a global source argument. Different positive counterexample blocks can begin at unrelated source phases, and (5) does not compare the right endpoint of one block with the left endpoint of the next. What it removes is the internal whole-fan reset architecture: higher layers, unmatched packets, endpoint fringe atoms, and arbitrary physical stretch cannot make the raw Chebyshev source return to or below its left-end value during one late compact threshold sweep.

## 5. Prior-art boundary and research consequence

The proof is line-internal after the classical CA event structure: `RE-040` supplies the uniform quantitative false-RH amplitude floor and adaptive tangent equation, while `RE-076` supplies the exact radical-gap correction and positive switch transport. A targeted current search of Robin/CA work, including the recent prime-layer workload formulation and recent explicit-window approaches using Chebyshev estimates, found no theorem asserting this adaptive **raw endpoint Chebyshev transport** or the self-defeating fringe-reset mechanism. No new external result is load-bearing here, so `SOURCES.md` requires no update.

The mathematical consequence is that the frontier left by `RE-106` should be changed. There is no longer a need to rule out a super-stretched base-two reset endpoint: that endpoint cannot perform the reset. The surviving problem is more global and source-conditioned. A false-RH construction must now accommodate a power-scale **positive raw Chebyshev transport on every late compact threshold fan**, while still arranging the sequence of positive Robin-counterexample blocks supplied by the source oscillation. The natural next question is therefore how the raw Chebyshev rise (5) couples to the reciprocal-Mertens coordinate and to the inter-block source phase, not whether a sufficiently large local fringe atom can cancel it.

## Consequence

The endpoint fringe is not an asymptotic reset resource. Across every sufficiently late compact false-RH CA fan,

\[
H_\vartheta(Z_R)-H_\vartheta(Z_L)
\gg_J X^{1-b_1}\log X>0,
\]

uniformly in the fan's physical stretch. `RE-106` correctly identified that any hypothetical reset would have to pay for the whole corrected debt with one final fringe atom, but `RE-107` closes that branch by feeding the required terminal scale back into the same false-RH amplitude law. The larger the proposed reset atom, the larger the terminal selector displacement, and the latter eventually wins by a power of the terminal scale.