# RE-080 — long same-block fans force power-separated transport fronts

**Status:** `EXACT-DERIVED + QUANTITATIVE-RH-FAILURE + SAME-BLOCK-LONG-STRETCH + TRANSPORT-MEASURE-LOCALIZATION + POWER-FRONT-SEPARATION + EFFECTIVE-KERNEL-SCALE + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`.

`RE-079` shows that the corrected Chebyshev and reciprocal/Mertens Lyapunov laws are not two independent budgets: on every sufficiently late positive threshold fan they are the unweighted and `g(s)=1/(s log s)`-weighted moments of one positive transport measure. That finding leaves one genuinely new degree of freedom: **where in selector scale the transport mass sits**. The same-block convex-envelope law of `RE-038` already constrains that freedom strongly on any fan whose selected logarithmic sizes stretch by an unbounded factor.

Assume RH is false, write

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>\frac12,
\]

fix

\[
J=[b_0,b_1]\Subset(1-\Theta,\tfrac12),
\]

and take the sufficiently late common positive CA blocks of `RE-038`--`RE-040`. On one such block let `C_i` be the rightmost adaptive maximizer at `b_i`, and write

\[
Y_i:=\log C_i,
\qquad
h_i:=\log G(C_i)-\gamma,
\qquad
R_i:=e^{h_i}-1,
\qquad
Z_i:=Z_{b_i}(C_i),
\]

for `i=0,1`. Suppose along an infinite family of these blocks

\[
r:=\frac{Y_1}{Y_0}\longrightarrow\infty.
\tag{1}
\]

Let `mu=mu_(0,1)` be the positive transport measure of `RE-079`, and set

\[
M:=\mu([Z_0,Z_1])
=\widehat H_1-\widehat H_0,
\tag{2}
\]

\[
W:=\int_{[Z_0,Z_1]}\frac{d\mu(s)}{s\log s}
=\widehat E_0-\widehat E_1+B_1(0,1).
\tag{3}
\]

Then the ratio `W/M` has a forced power scale. Uniformly along every family satisfying (1),

\[
\boxed{
\frac{r^{b_0-1}}{Y_0\log Y_1}
\ll_J
\frac{W}{M}
\ll_J
\frac{r^{b_1-1}}{Y_0\log Y_1}.}
\tag{4}
\]

Equivalently, if the **effective transport selector** `Z_eff` is defined uniquely by

\[
\boxed{
\frac1{Z_{\rm eff}\log Z_{\rm eff}}
:=\frac{W}{M},}
\tag{5}
\]

then

\[
\boxed{
Z_0\,r^{\,1-b_1-o(1)}
\le Z_{\rm eff}
\le
Z_0\,r^{\,1-b_0+o(1)}.}
\tag{6}
\]

Thus a long same-block fan cannot place the effective transport scale arbitrarily near either endpoint. Its kernel barycenter is forced into the intermediate power window whose exponent is the complementary threshold `1-b`.

More is true than the barycenter statement. Fix

\[
0<\varepsilon<\min\{b_0,1-b_1\}
\]

and define

\[
S_-(r):=Z_0r^{1-b_1-\varepsilon},
\qquad
S_+(r):=Z_0r^{1-b_0+\varepsilon}.
\tag{7}
\]

For all sufficiently large members of the stretched family, `Z_0<S_-<S_+<Z_1`, and

\[
\boxed{
\frac{\mu([Z_0,S_-])}{M}
\ll_{J,\varepsilon} r^{-\varepsilon},}
\tag{8}
\]

while the opposite, kernel-weighted tail satisfies

\[
\boxed{
\frac{
\displaystyle\int_{[S_+,Z_1]}\frac{d\mu(s)}{s\log s}
}{W}
\ll_{J,\varepsilon} r^{-\varepsilon}.}
\tag{9}
\]

So the two moments of the **same** measure develop complementary transport fronts: asymptotically all unweighted corrected-Chebyshev mass lies *after* the power scale `r^(1-b_1-epsilon)`, whereas asymptotically all Robin-kernel-weighted mass is already spent *before* the power scale `r^(1-b_0+epsilon)`.

This is the scale-separation information that `RE-079` left open. It is not a contradiction by itself: an abstract positive measure can realize these bounds. It does, however, turn the long-stretch branch of the false-RH fan into a precise source-specific target. Any ordinary-prime realization must reproduce a moving transport front at complementary exponent `1-b`; merely satisfying positivity, the two Lyapunov monotonicities, or the endpoint moment sandwich is no longer enough.

## 1. The convex envelope fixes the endpoint height ratio

Because `C_0` maximizes `A_(b_0)(C)=Y_C^(b_0)R_C` and `C_1` maximizes `A_(b_1)`, the two maximizing inequalities give directly

\[
Y_0^{b_0}R_0\ge Y_1^{b_0}R_1,
\qquad
Y_1^{b_1}R_1\ge Y_0^{b_1}R_0.
\]

Hence the same-block cone of `RE-038` can be written

\[
\boxed{
r^{-b_1}\le\frac{R_1}{R_0}\le r^{-b_0}.}
\tag{10}
\]

`RE-040` puts the whole compact fan in the uniform small-height regime, so

\[
R_i=h_i(1+o_J(1)).
\]

Therefore

\[
\boxed{
r^{-b_1}(1+o_J(1))
\le\frac{h_1}{h_0}
\le r^{-b_0}(1+o_J(1)).}
\tag{11}
\]

The same uniform regime gives `Z_i/Y_i -> 1`. In particular

\[
\frac{Z_1}{Z_0}=r(1+o_J(1)).
\tag{12}
\]

Nothing about prime spacing or packet cardinality has entered yet. Equations (10)--(12) are purely the adaptive same-block envelope geometry plus uniform regularity.

## 2. On a long fan the two endpoint contributions decouple

The pointwise shadow of `RE-079` gives at every selected point

\[
\widehat H_i
=b_i h_iY_i\log Y_i\,(1+o_J(1)),
\tag{13}
\]

\[
\widehat E_i
=(1-b_i)h_i\,(1+o_J(1)).
\tag{14}
\]

Using the lower side of (11),

\[
\frac{\widehat H_0}{\widehat H_1}
\ll_J
r^{b_1-1}\frac{\log Y_0}{\log Y_1}
\longrightarrow0,
\tag{15}
\]

because `b_1<1/2<1`. Consequently

\[
\boxed{M=\widehat H_1(1+o_J(1)).}
\tag{16}
\]

For the reciprocal coordinate, the upper side of (11) gives

\[
\frac{\widehat E_1}{\widehat E_0}
\ll_J r^{-b_0}\longrightarrow0.
\tag{17}
\]

The first-layer mismatch is smaller still. `RE-079` proves

\[
B_1(0,1)\ll Z_0^{-1},
\]

while the quantitative lower scale in `RE-040` gives

\[
h_0\gg_J Y_0^{-b_1}.
\]

Since `b_1<1`,

\[
\frac{B_1(0,1)}{\widehat E_0}
\ll_J Y_0^{b_1-1}
\longrightarrow0.
\tag{18}
\]

Therefore

\[
\boxed{W=\widehat E_0(1+o_J(1)).}
\tag{19}
\]

This endpoint decoupling is the essential long-stretch phenomenon: the unweighted transport mass is asymptotically determined by the **late** endpoint, while its `g`-weighted moment is asymptotically determined by the **early** endpoint.

## 3. The complementary exponent `1-b` is forced

Combining (13)--(14) with (16)--(19) gives

\[
\frac WM
=
\left(\frac{1-b_0}{b_1}+o_J(1)\right)
\frac{h_0}{h_1Y_1\log Y_1}.
\tag{20}
\]

Since `Y_1=rY_0`, equation (11) yields exactly the two-sided scale estimate (4).

Now `g(s)=1/(s log s)` is continuous and strictly decreasing. Since `W/M` is the average of `g` against the probability measure `mu/M`, there is a unique `Z_eff in [Z_0,Z_1]` satisfying (5). Inverting (4) gives

\[
Y_0r^{1-b_1}\log Y_1
\ll_J
Z_{\rm eff}\log Z_{\rm eff}
\ll_J
Y_0r^{1-b_0}\log Y_1.
\tag{21}
\]

Because `Z_eff` lies between `Z_0~Y_0` and `Z_1~Y_1`, the remaining logarithmic ratios contribute only `r^(o(1))`. This proves (6).

A useful narrow-band corollary is immediate. Fix any

\[
b_*\in(1-\Theta,\tfrac12)
\]

and choose a compact band `J=[b_*-delta,b_*+delta]` inside the admissible interval. On every long-stretched family for that band,

\[
\boxed{
\frac{\log(Z_{\rm eff}/Z_0)}{\log r}
=1-b_*+O(\delta)+o(1).}
\tag{22}
\]

Thus by making the threshold band narrow before taking the asymptotic family, the effective transport exponent can be localized arbitrarily closely to `1-b_*`.

## 4. Positivity upgrades the barycenter to two one-sided front laws

Let `S_-=S_-(r)` be as in (7). Since `g` is decreasing,

\[
W
\ge
\int_{[Z_0,S_-]}g(s)\,d\mu(s)
\ge
g(S_-)\mu([Z_0,S_-]).
\]

Hence

\[
\frac{\mu([Z_0,S_-])}{M}
\le
\frac{W/M}{g(S_-)}.
\tag{23}
\]

Using the upper bound in (4), `Z_0~Y_0`, and `S_-<Z_1`,

\[
\frac{W/M}{g(S_-)}
\ll_{J,\varepsilon}
 r^{b_1-1}
 r^{1-b_1-\varepsilon}
 \frac{\log S_-}{\log Y_1}
\ll_{J,\varepsilon}r^{-\varepsilon}.
\]

This proves (8).

For the late weighted tail, positivity gives

\[
\int_{[S_+,Z_1]}g(s)\,d\mu(s)
\le g(S_+)M.
\]

Dividing by `W` and using the lower bound in (4),

\[
\frac{
\int_{[S_+,Z_1]}g\,d\mu
}{W}
\le
\frac{g(S_+)}{W/M}
\ll_{J,\varepsilon}
 r^{-\varepsilon}
 \frac{\log Y_1}{\log S_+}.
\tag{24}
\]

The last logarithmic ratio is uniformly bounded because

\[
\log S_+
=\log Z_0+(1-b_0+\varepsilon)\log r
\]

and `1-b_0+epsilon>0`. This proves (9).

The asymmetry between (8) and (9) is real. One moment cannot force most **unweighted** mass to avoid the far right endpoint: a tiny amount of early mass can dominate a decreasing kernel average. What is forced is exactly what (8)--(9) say. Any stronger two-sided concentration claim would need another moment or genuine prime-source structure.

## 5. Boundary controls and what the result does not prove

The bounded-stretch branch `r=O(1)` is deliberately excluded. There `RE-079` already shows that the two moments are equivalent up to the natural `Z log Z` factor, and there is no power-scale separation to exploit.

The long-stretch theorem is also compatible with an abstract positive-measure control. For example, a point mass placed at a selector satisfying (5) reproduces the two endpoint moments and the effective exponent window. Therefore (4)--(9) are **not** themselves an arithmetic contradiction and must not be advertised as one. Their role is to specify the moving concentration profile that an actual CA/prime event source would have to realize.

The first-layer correction cannot upset the front law. Its entire future tail is `O(1/Z_0)`, while the false-RH quantitative inheritance makes the early reciprocal budget at least order `Y_0^(-b_1)`. The ratio tends to zero by a fixed power. This is why first-layer births disappear from (4) at leading order even though they are indispensable in the exact identity (3).

Likewise, no assumption about a bounded number of CA events is used. Higher-layer packets of arbitrary cardinality are already contained in `mu` as the exact positive atoms of `RE-079`; the localization bounds constrain their contribution together with the continuous selector-dilation mass.

## 6. Prior-art boundary and next target

A directed current search was made against the recent CA/Robin literature and weighted-prime-error literature. Mantovanelli's August 2026 preprint remains the closest prior-art boundary for prime-layer event measures, exact Robin workloads, and moment hierarchies; Bhattacharya--Martin--Simpson treat correlations between standard and reciprocal weighted prime-counting errors; Vega and Zimov study structural restrictions on hypothetical Robin counterexamples. The search did not locate an external result combining the **adaptive same-block threshold envelope** with a positive transport moment identity to force the complementary power front (4)--(9). No external theorem beyond sources already anchored in `SOURCES.md` is used in the proof, so no source-file change is required.

The research target after `RE-079` can now be split cleanly by stretch. On bounded-dilation fan segments the two Lyapunov laws supply only one local ledger. On unbounded same-block stretches, the ledger is no longer distribution-free: its unweighted mass and Robin-weighted mass are forced to separate across the power window

\[
Z_0r^{1-b_1}
\quad\text{to}\quad
Z_0r^{1-b_0}.
\]

The next source-specific question is whether the genuine ordinary-prime/higher-layer CA event staircase can realize this front repeatedly on the false-RH block family. In particular, a useful next theorem would compare the cumulative prime-layer transport below `Z_0 r^alpha` with the envelope prediction as `alpha` crosses `1-b`, rather than seeking another endpoint-only monotonicity law.