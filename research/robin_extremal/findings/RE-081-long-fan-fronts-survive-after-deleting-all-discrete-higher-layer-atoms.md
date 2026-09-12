# RE-081 — long fan fronts survive after deleting all discrete higher-layer atoms

**Status:** `EXACT-DERIVED + QUANTITATIVE-RH-FAILURE + SAME-BLOCK-LONG-STRETCH + TRANSPORT-DECOMPOSITION + HIGHER-LAYER-ATOMS-NEGLIGIBLE + SELECTOR-DILATION-DOMINANCE + NEGATIVE/ROUTE-NARROWING + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`.

`RE-079` represents the two corrected fan Lyapunov increments by one positive transport measure `mu`: its total mass is corrected Chebyshev growth, while its `g(s)=1/(s log s)`-weighted mass is the fringe-corrected reciprocal/Mertens decrement up to the explicit first-layer-birth term. `RE-080` then proves that on a long same-block false-RH fan these two moments develop power-separated fronts. A natural remaining interpretation is that the genuine discrete CA prime-power events might have to realize that front.

They do not, at leading order.

Assume RH is false, write

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>\frac12,
\]

fix

\[
J=[b_0,b_1]\Subset(1-\Theta,\tfrac12),
\]

and take a long-stretched same-block family exactly as in `RE-080`, with selected endpoints

\[
(C_0,b_0,Z_0,Y_0,h_0),
\qquad
(C_1,b_1,Z_1,Y_1,h_1),
\qquad
r:=Y_1/Y_0\to\infty.
\]

Let `mu=mu_(0,1)` be the positive transport measure of `RE-079`, and put

\[
M:=\mu([Z_0,Z_1])
=\widehat H_1-\widehat H_0,
\]

\[
W:=\int_{[Z_0,Z_1]}g(s)\,d\mu(s)
=\widehat E_0-\widehat E_1+B_1(0,1).
\]

Split the measure canonically as

\[
\boxed{\mu=\mu_{\rm dil}+\mu_{\ge2},}
\tag{1}
\]

where `mu_(>=2)` is the sum of all discrete higher-layer atoms

\[
\mu_{\ge2}
:=\sum_{\substack{(p,j)\text{ crossed by the segment}\\j\ge2}}
(\log p)\,\delta_{\eta_{p,j}},
\tag{2}
\]

and `mu_dil` is the remaining continuous selector-dilation transport: `dZ` inside fixed-state cells and the pushed-forward `dD_c` measure across tied switches.

Then both higher-layer contributions are asymptotically negligible relative to the corresponding full long-fan moments:

\[
\boxed{
M_{\ge2}:=\mu_{\ge2}([Z_0,Z_1])
\ll \sqrt{Z_1}(\log Z_1)^{3/2}
=o(M),}
\tag{3}
\]

and

\[
\boxed{
W_{\ge2}:=
\int_{[Z_0,Z_1]}g(s)\,d\mu_{\ge2}(s)
\ll Z_0^{-1/2}\log Z_0
=o(W).}
\tag{4}
\]

More quantitatively, using the uniform false-RH amplitude floor of `RE-040` and the endpoint decoupling of `RE-080`,

\[
\boxed{
\frac{M_{\ge2}}M
\ll_J
Y_1^{\,b_1-1/2}(\log Y_1)^{1/2}
\longrightarrow0,}
\tag{5}
\]

\[
\boxed{
\frac{W_{\ge2}}W
\ll_J
Y_0^{\,b_1-1/2}\log Y_0
\longrightarrow0.}
\tag{6}
\]

The strict inequality `b_1<1/2` is exactly what kills the square-root prime-power layer after normalization.

Consequently, if

\[
M_{\rm dil}:=\mu_{\rm dil}([Z_0,Z_1]),
\qquad
W_{\rm dil}:=\int g\,d\mu_{\rm dil},
\]

then

\[
\boxed{
M_{\rm dil}=M(1+o(1)),
\qquad
W_{\rm dil}=W(1+o(1)).}
\tag{7}
\]

The first-layer correction of `RE-079` is smaller still:

\[
B_1(0,1)\ll Z_0^{-1}=o(W).
\tag{8}
\]

Thus the actual corrected Lyapunov changes themselves are asymptotically carried by selector dilation:

\[
\boxed{
\widehat H_1-\widehat H_0
=M_{\rm dil}(1+o(1)),}
\tag{9}
\]

\[
\boxed{
\widehat E_0-\widehat E_1
=W_{\rm dil}(1+o(1)).}
\tag{10}
\]

In particular, deleting **every discrete higher-layer CA-event atom** does not destroy the `RE-080` power-front law. The continuous measure `mu_dil` has the same effective-selector exponent window and the same two one-sided front estimates, up to vanishing relative error.

This is a route-narrowing result rather than a contradiction to false RH. `RE-004` already says higher-layer transition coordinates have square-root count ceiling, and `RE-079` already notes that the endpoint higher-layer mass is lower order in its pointwise shadow. The new conclusion is the two-moment long-fan statement: even the reciprocal-weighted higher-layer contribution has a square-root tail ceiling, so the full `RE-080` moving front survives after all discrete higher-layer atoms are removed. Therefore a source-specific attack on the long-stretch branch cannot succeed merely by proving that higher-layer events are sparse, deep, lacunary, or low-rank. The leading obstruction has moved to the **continuous adaptive selector-dilation geometry over the genuine CA state staircase**.

## 1. The transport split is exact

`RE-076` gives, at every selected point,

\[
\widehat H(C,b)
=Z-\log\operatorname{rad}(C)
=(Z-Y)+P_C,
\tag{11}
\]

where `P_C` is the total active depth-at-least-two event mass. Across a higher-layer event `(p,j)`, `j>=2`, the radical does not change and `P_C` increases by exactly `log p`. Across a first-layer birth, `Y` and `log rad(C)` increase together, so `P_C` does not change. Inside a fixed-state threshold cell, only `Z` changes.

`RE-079` upgrades this endpoint decomposition to a measure identity. Its cell contribution is `dZ`; the smooth part of a tied switch is the positive pushed-forward measure `dD_c`; and every higher-layer event contributes exactly

\[
(\log p)\delta_{\eta_{p,j}}.
\]

Hence (1)--(2) are not a choice of bookkeeping. They are the canonical Lebesgue/atomic split already present in the fan transport construction. In particular,

\[
M_{\ge2}=P_{C_1}-P_{C_0},
\qquad
M_{\rm dil}
=(Z_1-Y_1)-(Z_0-Y_0),
\tag{12}
\]

and

\[
M=M_{\rm dil}+M_{\ge2}.
\tag{13}
\]

For the reciprocal moment, the exact CA event equation gives something even more useful. If

\[
\lambda_{p,j}
:=\log\frac{1-p^{-(j+1)}}{1-p^{-j}},
\]

then

\[
g(\eta_{p,j})
=\frac{\lambda_{p,j}}{\log p},
\]

so one higher-layer atom contributes exactly

\[
g(\eta_{p,j})\log p
=\lambda_{p,j}
\tag{14}
\]

to `W_(>=2)`. Thus its unweighted cost is `log p`, whereas its reciprocal cost is the much smaller finite-exponent-tail increment `lambda_(p,j)`.

## 2. Every higher-layer event has a two-sided prime-power scale

The square-root ceilings needed below require no prime number theorem. Put

\[
x:=p^{-j},
\qquad
u:=\frac{x(1-p^{-1})}{1-x}.
\]

For `p>=2` and `j>=2`, one has `x<=1/4` and

\[
\frac{x}{2}\le\nu\le\frac{4x}{3}\le\frac13.
\]

Since

\[
\lambda_{p,j}=\log(1+\nu)
\]

and `3 nu/4 <= log(1+nu) <= nu` on this range,

\[
\boxed{
\frac{3}{8}p^{-j}
\le
\lambda_{p,j}
\le
\frac43p^{-j}.}
\tag{15}
\]

Combining (15) with the exact event equation yields the uniform two-sided comparison

\[
\boxed{
\frac34p^j\log p
\le
\eta_{p,j}\log\eta_{p,j}
\le
\frac83p^j\log p.}
\tag{16}
\]

`RE-004` used the lower side, in slightly weaker form, to obtain the square-root **count** ceiling for higher-layer transitions. Here both sides matter because the weighted tail must also be controlled from the beginning of the fan segment.

## 3. The unweighted discrete mass is below the false-RH fan scale

Every atom of `mu_(>=2)` lies in `[Z_0,Z_1]` by `RE-079`, hence its event coordinate satisfies `eta_(p,j)<=Z_1`. From the lower side of (16),

\[
p^j\log p
\ll Z_1\log Z_1.
\]

Since `log p>=log 2`, every contributing prime power satisfies

\[
p^j\le X_1,
\qquad
X_1\asymp Z_1\log Z_1.
\tag{17}
\]

Therefore

\[
M_{\ge2}
\le
\sum_{\substack{j\ge2\\p^j\le X_1}}\log p.
\tag{18}
\]

Bounding primes by all integers, the `j=2` term is at most

\[
O(\sqrt{X_1}\log X_1),
\]

while all `j>=3` together contribute

\[
O\!\left(X_1^{1/3}(\log X_1)^2\right)
=o(\sqrt{X_1}\log X_1).
\]

Thus

\[
M_{\ge2}
\ll
\sqrt{Z_1}(\log Z_1)^{3/2},
\]

which is the first half of (3).

Now use the long-fan normalization. `RE-040` gives uniformly over the compact fan

\[
h(C)\gg_JY^{-b_1},
\tag{19}
\]

while `RE-080` gives

\[
M=\widehat H_1(1+o_J(1)),
\qquad
\widehat H_1
=b_1h_1Y_1\log Y_1(1+o_J(1)),
\qquad
Z_1\sim Y_1.
\tag{20}
\]

Hence

\[
M\gg_JY_1^{1-b_1}\log Y_1.
\tag{21}
\]

Dividing the square-root ceiling by (21) gives (5). Because `b_1<1/2`, every fixed power loss beats the remaining logarithm.

This makes precise a point only used locally in `RE-079`: the higher-layer term `P_C` is not merely lower order at one selected endpoint. Its **entire atomic mass on a long stretched fan segment** is negligible compared with the transport mass forced by false-RH amplitude inheritance.

## 4. The reciprocal-weighted discrete tail is also negligible

The weighted estimate is different because an old small prime at great layer depth might occur late. Counting events is therefore not enough; use the exact weight (14).

For any atom in `[Z_0,Z_1]`, `eta_(p,j)>=Z_0`. The upper side of (16) implies

\[
Z_0\log Z_0
\le
\eta_{p,j}\log\eta_{p,j}
\ll
p^j\log(p^j).
\tag{22}
\]

For all sufficiently large `Z_0`, monotonicity of `x log x` then forces an absolute lower bound

\[
\boxed{p^j\ge cZ_0}
\tag{23}
\]

for one fixed `c>0`. For example, any sufficiently small absolute `c` works: if `p^j<cZ_0`, then `p^j log(p^j)` is too small to satisfy (22).

Using the upper side of (15) and then enlarging primes to all integers,

\[
W_{\ge2}
=\sum_{\substack{(p,j)\text{ in segment}\\j\ge2}}
\lambda_{p,j}
\ll
\sum_{\substack{j\ge2\\p^j\ge cZ_0}}p^{-j}.
\tag{24}
\]

Let `L=floor(log_2(cZ_0))`. For `2<=j<=L`, integral comparison gives

\[
\sum_{m\ge(cZ_0)^{1/j}}m^{-j}
\ll
(cZ_0)^{-(j-1)/j},
\]

and this is at most order `Z_0^(-1/2)`. Summing over the `O(log Z_0)` possible depths gives

\[
O(Z_0^{-1/2}\log Z_0).
\]

For `j>L`, the threshold is automatic and

\[
\sum_{j>L}\sum_{m\ge2}m^{-j}
\ll2^{-L}
\ll Z_0^{-1}.
\]

This proves the absolute bound in (4).

`RE-080` gives the opposite endpoint decoupling

\[
W=\widehat E_0(1+o_J(1)),
\qquad
\widehat E_0
=(1-b_0)h_0(1+o_J(1)).
\tag{25}
\]

Together with (19),

\[
W\gg_JY_0^{-b_1}.
\tag{26}
\]

Since `Z_0~Y_0`, division of (4) by (26) gives (6). Again the decisive margin is exactly `1/2-b_1>0`.

The first-layer discrepancy cannot replace the deleted higher-layer mass. `RE-079` gives its entire future bound

\[
B_1(0,\infty)\ll Z_0^{-1},
\]

so by (26)

\[
\frac{B_1(0,1)}W
\ll_JY_0^{b_1-1}
\to0.
\tag{27}
\]

Thus both discrete mechanisms in the exact duality -- higher-layer atoms and first-layer tail births -- disappear at leading order on the long-stretch false-RH normalization.

## 5. The power-separated front is already present in the continuous dilation measure

Equations (5)--(7) imply

\[
\frac{W_{\rm dil}}{M_{\rm dil}}
=
\frac WM(1+o(1)).
\tag{28}
\]

Therefore the two-sided moment estimate of `RE-080` remains unchanged at power scale:

\[
\boxed{
\frac{r^{b_0-1}}{Y_0\log Y_1}
\ll_J
\frac{W_{\rm dil}}{M_{\rm dil}}
\ll_J
\frac{r^{b_1-1}}{Y_0\log Y_1}.}
\tag{29}
\]

If `Z_(eff,dil)` is defined by

\[
g(Z_{\rm eff,dil})
:=\frac{W_{\rm dil}}{M_{\rm dil}},
\]

then the same inversion used in `RE-080` gives

\[
\boxed{
Z_0r^{1-b_1-o(1)}
\le
Z_{\rm eff,dil}
\le
Z_0r^{1-b_0+o(1)}.}
\tag{30}
\]

The one-sided fronts also survive. For fixed admissible `epsilon>0`, put

\[
S_-=Z_0r^{1-b_1-\varepsilon},
\qquad
S_+=Z_0r^{1-b_0+\varepsilon}.
\]

Because `mu_dil<=mu` as positive measures and `M_dil~M`, the early unweighted estimate of `RE-080` gives

\[
\boxed{
\frac{\mu_{\rm dil}([Z_0,S_-])}{M_{\rm dil}}
\ll_{J,\varepsilon}r^{-\varepsilon}+o(1).}
\tag{31}
\]

Likewise `W_dil~W` and positivity give

\[
\boxed{
\frac{
\displaystyle\int_{[S_+,Z_1]}g(s)\,d\mu_{\rm dil}(s)
}{W_{\rm dil}}
\ll_{J,\varepsilon}r^{-\varepsilon}+o(1).}
\tag{32}
\]

Thus the scale separation found in `RE-080` is not a hidden concentration of prime-power atoms. The leading measure that must move from the early to the late power region is the continuous selector-dilation component itself.

## 6. Boundary controls, prior-art boundary, and the remaining target

The long-stretch hypothesis is load-bearing for the **relative** conclusions. The absolute estimates (3)--(4) are general event-scale ceilings, but `M~widehat H_1` and `W~widehat E_0` are the endpoint-decoupling mechanism of `RE-080`. On a bounded-stretch or arbitrarily short fan segment, its total transport increment may be small enough that a single discrete event is not negligible.

The fixed compact restriction `b_1<1/2` is equally load-bearing. At the formal boundary `b_1=1/2`, the square-root event ceiling and the false-RH amplitude floor meet at the same power, so (5)--(6) no longer follow from these estimates. The theorem must not be extrapolated to the critical threshold by dropping logarithms.

No bounded-packet hypothesis is used. Tied transitions are harmless because (18) counts event occurrences rather than distinct coordinates; multiple higher-layer events at one coordinate simply contribute several positive atoms. Very deep events are harmless in the weighted estimate because their exact reciprocal cost is `lambda_(p,j)=O(p^-j)`.

The closest prior-art boundary remains Mantovanelli's August 2026 prime-layer workload and prime-frontier decomposition, already anchored in `SOURCES.md`. `RE-004` also already established the square-root higher-layer count ceiling, and `RE-079` explicitly used the fact that endpoint higher-layer mass is lower order. No novelty is claimed for prime-power sparsity, the event equation, or the decomposition of a CA state into first and higher layers. A directed current audit did not locate the specific adaptive long-fan consequence (5)--(7), nor the fact that the `g`-weighted higher-layer tail is negligible relative to the false-RH reciprocal budget so that the `RE-080` front survives after **all** discrete atoms are deleted. No new external theorem is load-bearing, so `SOURCES.md` requires no change.

The strategic implication is negative but sharp. The next long-stretch theorem should not try to contradict `RE-080` merely by bounding the number, depth, spacing, or total mass of higher-layer CA events: those atoms are already asymptotically absent from both normalized moments. What remains prime-specific is subtler. The continuous measure is generated only along the genuine sequence of exposed CA states and their physical spans, so a successful source theorem must constrain that **selector-dilation transport over the ordinary-prime-supported state staircase** -- for example its cumulative mass below `Z_0r^alpha`, the distribution of switch spans that generate it, or the ability of genuine CA endpoints to sustain the moving complementary exponent `1-b`. An abstract positive measure can still realize the front, and the present theorem does not convert selector dilation into an arithmetic contradiction.