# ANF-182 — Endpoint geometry makes `K/a_X` a sharp derivative-flattening threshold

**Status:** `EXACT-DERIVED + MATCHED-CONTROL + SHARP-COMPLEXITY-THRESHOLD + POSITIVE-DISCRIMINATION-BOUNDARY`. `ANF-181` proves that the prime-scale endpoint-loading construction can make the entire exact-log derivative jet asymptotically flat through every order `r_X` satisfying

\[
\frac{r_X a_X}{K}\to0,
\qquad
 a_X:=\sqrt{\delta X\log X},
\qquad
 K=X^{1-2\varepsilon+o(1)}.
\]

It also observes geometrically that a dangerous packet which must finish loading before `K` cannot have relative exact-log frequency width smaller than order `a_X/K`. What remained open there was whether this was merely a limitation of the construction or whether derivative information actually becomes nontrivial at the reciprocal scale.

For the sector-aligned prime-scale matched-control class used in `ANF-175`--`ANF-181`, the threshold is sharp up to constants. Any target-sized packet made of `log X` atoms on `log X`-separated sites and completed before `K` has enough physical spread that an exact-log derivative of order

\[
\boxed{
 r_X\asymp \frac{K}{a_X}
}
\]

must differ from the zeroth-order profile by `Omega(a_X)` after the same normalization used in `ANF-181`. Thus the flattening theorem cannot be extended from `r_X=o(K/a_X)` to all `r_X=O(K/a_X)`: at a sufficiently large constant multiple of `K/a_X`, every sector-aligned target-sized packet is detected.

This is a sharpness theorem for the matched-control derivative obstruction, not a theorem that such enormous derivative orders are analytically available for the arithmetic source, and not a reconstruction theorem for the prime-minus-Ramanujan placement law.

## 1. Target charge forces `Theta(a_X)` physical spread

Use the prime-scale matched-control alphabet from `ANF-175`--`ANF-181`. Put

\[
A_X:=\log X,
\qquad
q_X:=\lceil\log X\rceil,
\qquad
a_X:=\sqrt{\delta X\log X}.
\tag{1}
\]

Let

\[
0<J=j_1<j_2<\cdots<j_m\le K
\tag{2}
\]

be active offsets satisfying

\[
j_{s+1}-j_s\ge q_X.
\tag{3}
\]

At the distinguished twist `U`, write the demodulated carrier phases as

\[
\zeta_s
:=
\exp\!\left(-iU\log\left(1+\frac{j_s}{X}\right)\right).
\tag{4}
\]

Assume, exactly as in the six-sector selection used to build the dangerous controls, that all `zeta_s` lie in one angular sector of width `pi/3`. After a common rotation we may therefore suppose

\[
\operatorname{Re}\zeta_s\ge \cos(\pi/6)=\frac{\sqrt3}{2}.
\tag{5}
\]

Define the distinguished load

\[
F_X(0):=A_X\sum_{s=1}^{m}\zeta_s
\tag{6}
\]

and suppose it is endpoint-dangerous:

\[
|F_X(0)|\ge a_X.
\tag{7}
\]

The trivial upper bound `|F_X(0)|<=A_X m` gives

\[
m\ge \frac{a_X}{A_X}.
\tag{8}
\]

Let `s_0:=ceil(m/2)`. From the spacing (3), for all sufficiently large `X`,

\[
j_{s_0}-J
\ge (s_0-1)q_X
\ge \frac{m}{3}q_X
\ge \frac{a_X}{3}.
\tag{9}
\]

Hence at least half of the active atoms lie a physical distance `Omega(a_X)` to the right of the first active atom. This conclusion uses only target charge, prime-sized atoms and prime-scale spacing; no distribution theorem for the actual primes is being inserted.

## 2. Exact logarithmic recentering converts that spread into a relative width `Omega(a_X/K)`

Use the exact logarithmic coordinate of `ANF-181`. Fix any constant `xi_*>0` and set

\[
W_X:=\frac{\xi_*}{\log(1+J/X)},
\qquad
\xi_s:=W_X\log\left(1+\frac{j_s}{X}\right).
\tag{10}
\]

Then `xi_1=xi_*` exactly and

\[
\frac{\xi_s}{\xi_*}-1
=
\frac{
\log(1+j_s/X)-\log(1+J/X)
}{
\log(1+J/X)
}.
\tag{11}
\]

Because `K=o(X)`, uniformly for `J<=j_s<=K`,

\[
\log\left(1+\frac{j_s-J}{X+J}\right)
\ge \frac{j_s-J}{4X}
\tag{12}
\]

for all sufficiently large `X`, while

\[
\log(1+J/X)\le \frac{J}{X}.
\tag{13}
\]

Combining (11)--(13),

\[
\frac{\xi_s}{\xi_*}-1
\ge
\frac{j_s-J}{4J}.
\tag{14}
\]

For every `s>=s_0`, equations (9), (14), and `J<=K` give

\[
\boxed{
\frac{\xi_s}{\xi_*}
\ge
1+c_0\frac{a_X}{K}
}
\qquad(s\ge s_0),
\tag{15}
\]

with an absolute constant `c_0>0` (for instance `c_0=1/12` works for large `X`).

Thus the lower bound `a_X/K` from the endpoint geometry is not merely attained by one extreme atom: a fixed positive fraction of the packet mass lies at that relative logarithmic distance from the left edge.

## 3. An order `Theta(K/a_X)` derivative must detect the packet width

Define the exact-log local profile

\[
F_X(y)
=
A_X\sum_{s=1}^{m}\zeta_s e^{-iy\xi_s}
\tag{16}
\]

and the normalized derivative observable used in `ANF-181`,

\[
D_{r,X}(y)
:=
(-i\xi_*)^{-r}F_X^{(r)}(y).
\tag{17}
\]

At `y=0`,

\[
D_{r,X}(0)-F_X(0)
=
A_X\sum_{s=1}^{m}
\left[
\left(\frac{\xi_s}{\xi_*}\right)^r-1
\right]\zeta_s.
\tag{18}
\]

Every bracket in (18) is nonnegative. Rotate by the sector center and use (5); there can be no destructive cancellation in the real projection:

\[
|D_{r,X}(0)-F_X(0)|
\ge
\frac{\sqrt3}{2}A_X
\sum_{s=1}^{m}
\left[
\left(\frac{\xi_s}{\xi_*}\right)^r-1
\right].
\tag{19}
\]

Choose

\[
r_X:=\left\lceil C\frac{K}{a_X}\right\rceil
\tag{20}
\]

with a sufficiently large absolute constant `C`; `C=24` is more than enough with the rough constant in (15). Since `a_X/K->0`, equations (15) and (20) imply, for every `s>=s_0` and all large `X`,

\[
\left(\frac{\xi_s}{\xi_*}\right)^{r_X}-1
\ge c_1
\tag{21}
\]

for some absolute `c_1>0`. At least `m/2` indices satisfy this. Therefore, using (8),

\[
\begin{aligned}
|D_{r_X,X}(0)-F_X(0)|
&\ge
c_2 A_Xm\\
&\ge c_2 a_X.
\end{aligned}
\tag{22}
\]

Hence

\[
\boxed{
|D_{r_X,X}(0)-F_X(0)|\gg a_X
\qquad
\text{for some }r_X\ll K/a_X.
}
\tag{23}
\]

The entire normalized derivative jet therefore cannot remain `o(a_X)`-close to the zeroth-order profile through all orders comparable with `K/a_X`.

## 4. Together with `ANF-181`, this makes the derivative barrier sharp

`ANF-181` constructs endpoint-dangerous prime-scale controls for every integer sequence `r_X` satisfying

\[
r_X\frac{a_X}{K}\to0
\tag{24}
\]

such that

\[
D_{k,X}(y)=F_X(y)+o(a_X)
\qquad(0\le k\le r_X)
\tag{25}
\]

uniformly on every fixed normalized `y` window.

The present argument proves the complementary statement for the same sector-aligned matched-control architecture: if a target-sized packet is made of prime-sized, prime-spaced atoms and finishes before `K`, then by order

\[
r_X=O(K/a_X)
\tag{26}
\]

the flat-jet relation already fails at `y=0` by a macroscopic amount `Omega(a_X)`.

Consequently

\[
\boxed{
\frac{K}{a_X}
=
\frac{X^{1/2-2\varepsilon+o(1)}}{\sqrt{\log X}}
}
\tag{27}
\]

is the sharp complexity scale, up to constants and the boundary between `o(K/a_X)` and `Theta(K/a_X)`, for **derivative flattening of the sector-selected endpoint-memory controls**.

This removes one ambiguity left by `ANF-181`. The scale `K/a_X` was not just where the construction stopped being able to prove collapse. It is where exact-log derivative weights necessarily acquire order-one relative variation across a positive fraction of every such dangerous packet.

## 5. Stress tests and evidence boundary

The result is deliberately narrower than a source theorem.

First, it does not prove that the actual residual `Lambda-Lambda^sharp` produces a sector-aligned packet, nor that derivatives of order `K/a_X` can be estimated with the absolute precision needed at the distinguished height. The synthetic packet uses placement selected after inspecting the carrier; source-specific arithmetic placement remains the central missing input.

Second, equation (23) detects nonzero packet bandwidth but does not reconstruct the active sites. A full inversion problem at `m~a_X/log X` may have much worse conditioning. The claim is only that the specific asymptotic rank-one/flat-jet obstruction of `ANF-181` is exhausted at `Theta(K/a_X)` complexity.

Third, the proof uses equal prime-scale atom sizes and the `log X` spacing of the matched controls. The same quantile argument extends to unequal positive masses under a comparable local mass cap, but that generalization is not needed for the present decision boundary and is not claimed here.

Finally, the exact logarithmic coordinate is essential to the clean statement: no Taylor remainder is used to create the lower bound. If `J` is extremely small, the relative frequency spread is only larger, so late placement near the endpoint is the hardest case and is already covered by `J<=K`.

## 6. Prior-art audit and next gate

The neighboring inverse-problem literature confirms that clustered Fourier/Vandermonde systems become resolvable only when measurement bandwidth is large enough compared with node separation; sharp conditioning results for clustered nodes include Batenkov--Demanet--Goldman--Yomdin, *Conditioning of partial nonuniform Fourier matrices with clustered nodes* (2018), and related super-resolution work. That literature is conceptually adjacent but is not load-bearing here: (9)--(23) are an elementary endpoint-specific quantile and exact-log moment argument, and no external theorem is invoked. No `SOURCES.md` update is therefore required.

The research consequence is mainly negative about a possible generic escape. It is now precise how much local derivative complexity is needed merely to defeat the matched-control flattening: roughly `K/a_X`, polynomial in `X`. Replacing a fixed or slowly growing local jet by a moderately larger one does not help; reaching the threshold is qualitatively different, but doing so still supplies only packet-bandwidth information.

The next useful gate remains source-specific: either derive arithmetic placement information that prevents the carrier-selected packet in the first place, prove a directly signed estimate for the `ANF-169`/`ANF-172` Fejer slope observable, or exhibit a nonlocal/source-faithful observable whose effective resolving complexity reaches the `K/a_X` scale without requiring an intractable derivative hierarchy.