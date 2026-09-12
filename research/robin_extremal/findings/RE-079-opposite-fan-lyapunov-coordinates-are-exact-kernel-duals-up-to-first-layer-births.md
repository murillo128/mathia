# RE-079 — opposite fan Lyapunov coordinates are exact kernel-duals up to first-layer births

**Status:** `EXACT-DERIVED + GLOBAL-FAN-STIELTJES-DUALITY + LYAPUNOV-DEPENDENCE + ARBITRARY-MIXED-PACKETS + HIGHER-LAYER-EXACT-PAIRING + FIRST-LAYER-BIRTH-CORRECTION + NEGATIVE/OBSTRUCTION + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`.

`RE-076` and `RE-078` produce two global one-sided coordinates on every sufficiently late false-RH threshold fan: the corrected Chebyshev deficit

\[
\widehat H(C,b)=Z_b(C)-\log\operatorname{rad}(C)
\]

increases strictly, while the fringe-corrected logarithmic Mertens error

\[
\widehat E(C,b)=E_\ell(Z_b(C))-\delta_\ell(Z_b(C))
\]

decreases strictly. It is tempting to treat these as two independent irreversible source budgets. That interpretation is false. The two monotone laws are exact transforms of the **same positive fan-transport measure**, with kernel

\[
g(s)=\frac1{s\log s},
\]

apart from one completely explicit correction carried by new first-layer support births.

Assume RH is false, put

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>\frac12,
\]

fix

\[
J=[b_0,b_1]\Subset(1-\Theta,\tfrac12),
\]

and work on a sufficiently late common positive rightmost CA fan from `RE-040`. Let two selected fan points `0<1` be ordered in the fan orientation, with selectors `Z_0<Z_1`, and abbreviate

\[
\widehat H_i:=\widehat H(C_i,b_i),
\qquad
\widehat E_i:=\widehat E(C_i,b_i).
\]

Let `B_1(0,1)` be the total finite-exponent-tail mass created by first-layer support births crossed by the segment,

\[
B_1(0,1)
:=\sum_{p\in\mathcal B_1(0,1)}\tau_p,
\qquad
\tau_p:=-\log(1-p^{-2})>0.
\]

Then there is a positive finite measure `mu_(0,1)` supported on `[Z_0,Z_1]` such that

\[
\boxed{
\mu_{0,1}([Z_0,Z_1])
=\widehat H_1-\widehat H_0
}
\tag{1}
\]

and

\[
\boxed{
\widehat E_0-\widehat E_1+B_1(0,1)
=\int_{[Z_0,Z_1]}g(s)\,d\mu_{0,1}(s).
}
\tag{2}
\]

The measure is canonical from the fan geometry. Inside a fixed selected-state cell it is simply selector displacement `dZ`. Across a tied switch it has a continuous selector-dilation part and one atom of mass `log p` at the physical CA event coordinate of every higher-layer exponent increment. First-layer births contribute no atom to `mu`; they are exactly the correction `B_1` in (2).

Consequently the two Lyapunov increments obey the exact scale sandwich

\[
\boxed{
g(Z_1)(\widehat H_1-\widehat H_0)
\le
\widehat E_0-\widehat E_1+B_1(0,1)
\le
g(Z_0)(\widehat H_1-\widehat H_0).}
\tag{3}
\]

Equivalently,

\[
\boxed{
Z_0\log Z_0\,
(\widehat E_0-\widehat E_1+B_1)
\le
\widehat H_1-\widehat H_0
\le
Z_1\log Z_1\,
(\widehat E_0-\widehat E_1+B_1).}
\tag{4}
\]

Thus on every bounded-dilation selector window `Z_1<=K Z_0`,

\[
\boxed{
\widehat H_1-\widehat H_0
\asymp_K
Z_0\log Z_0\,
(\widehat E_0-\widehat E_1+B_1).
}
\tag{5}
\]

There is no second same-scale coercive budget available merely by adding the monotonicity of `widehat H` to the monotonicity of `widehat E`. They are one transport ledger measured once in unweighted mass and once through the decreasing Robin kernel `g`.

The first-layer discrepancy is itself globally tiny at late scale. Since

\[
\tau_p=-\log(1-p^{-2})\ll p^{-2},
\]

all future support births after selector scale `Z_0` satisfy

\[
\boxed{
B_1(0,\infty)\ll \frac1{Z_0}.
}
\tag{6}
\]

This does **not** make `B_1` negligible relative to an arbitrarily short fan increment, whose decrease may be even smaller; it says only that the total discrepancy between the two transport ledgers has an absolutely summable late tail. The useful information left after (1)--(6) is therefore the **distribution in selector scale of the positive transport measure**. Any future contradiction must exploit where the mass of `mu` sits, a genuine prime-source upper bound, or a first-layer arithmetic restriction, rather than count the two monotone coordinates as independent costs.

## 1. Inside a fixed state cell the duality is exact

Fix one exposed regular CA state `C`. Put

\[
Y:=\log C,
\qquad Z:=Z_b(C),
\qquad h:=\log G(C)-\gamma.
\]

`RE-059` gives the exact corrected reciprocal-source identity

\[
\widehat E(C,b)
=h+T(C)+\log\log Y-\log\log Z,
\tag{7}
\]

where

\[
T(C):=-\sum_{p\mid C}\log(1-p^{-(a_p+1)}).
\]

`RE-076` gives

\[
\widehat H(C,b)=Z-\log\operatorname{rad}(C).
\tag{8}
\]

Within the selected-state cell, `C`, `Y`, `h`, `T(C)`, and `rad(C)` are fixed. Therefore

\[
d\widehat H=dZ,
\qquad
d\widehat E=-\frac{dZ}{Z\log Z}=-g(Z)dZ.
\tag{9}
\]

Hence on any oriented subinterval of that cell,

\[
\boxed{
\widehat E_0-\widehat E_1
=\int_{Z_0}^{Z_1}g(s)\,ds,
\qquad
\widehat H_1-\widehat H_0=Z_1-Z_0.}
\tag{10}
\]

This is not an asymptotic relation. The fringe correction removes the only ordinary-prime jump inside the chamber, leaving an exact differential identity. In measure language the cell contribution is simply

\[
d\mu=dZ.
\tag{11}
\]

Equation (10) is the simplest stress test of (2): the Mertens decrease is exactly the `g`-weighted Chebyshev-coordinate growth.

## 2. The smooth part of every tied switch has the same exact differential law

Consider a switch at fixed threshold `b in J` between tied exposed states `C_-<C_+`. Write

\[
Y_\pm:=\log C_\pm
\]

and let their common adaptive amplitude be `c>0`. Along the common-amplitude interpolation used in `RE-070`, `RE-076`, and `RE-078`, define

\[
h_c(t):=\log(1+ct^{-b}),
\qquad
a_c(t):=1-e^{-h_c(t)}
=\frac{ct^{-b}}{1+ct^{-b}},
\tag{12}
\]

and let `Z_c(t)` solve

\[
g(Z_c(t))=g(t)-\frac{b\,a_c(t)}t.
\tag{13}
\]

Put

\[
D_c(t):=Z_c(t)-t
\]

and retain the smooth reciprocal term of `RE-078`,

\[
F_c(t):=h_c(t)+\log\log t-\log\log Z_c(t).
\tag{14}
\]

The key observation is that the derivative relation used only asymptotically for the sign in `RE-078` has an exact primitive form. From (12),

\[
h_c'(t)=-\frac{b\,a_c(t)}t.
\]

Using the selector equation (13), this is exactly

\[
h_c'(t)=g(Z_c(t))-g(t).
\tag{15}
\]

Differentiating (14) now gives

\[
\begin{aligned}
F_c'(t)
&=h_c'(t)+g(t)-g(Z_c(t))Z_c'(t)\\
&=g(Z_c(t))(1-Z_c'(t))\\
&=-g(Z_c(t))D_c'(t).
\end{aligned}
\tag{16}
\]

Thus

\[
\boxed{
F_c(Y_-)-F_c(Y_+)
=\int_{Y_-}^{Y_+}g(Z_c(t))\,dD_c(t).}
\tag{17}
\]

On sufficiently late compact false-RH fans, `RE-076` proves `D_c'(t)>0` uniformly. Hence `dD_c` is a positive measure, and after pushing it forward by the increasing selector map `s=Z_c(t)`, equation (17) is exactly a positive `g`-weighted transport contribution.

The asymptotic derivatives in `RE-076` and `RE-078`,

\[
D_c'(t)
=b(1-b)a_c(t)\log t\,(1+o_J(1))
\]

and

\[
F_c'(t)
=-\frac{b(1-b)a_c(t)}t\,(1+o_J(1)),
\]

are therefore not two unrelated drift calculations. Their ratio is forced by the exact identity (16): to first order it is simply `g(Z_c(t))~1/(t log t)`.

## 3. Every higher-layer event is an exact `g`-weighted atom

The remaining switch contribution comes from the finite-exponent tail `T(C)` and the higher-layer mass in `widehat H`. Consider one CA event that raises the exponent of prime `p` from `j-1` to `j`, with `j>=2`. Let its physical event coordinate be `eta_(p,j)`. The exact CA threshold equation is

\[
g(\eta_{p,j})
=\frac1{\log p}
\log\frac{1-p^{-(j+1)}}{1-p^{-j}}.
\tag{18}
\]

The contribution of `p` to `T` before and after the event is respectively

\[
-\log(1-p^{-j}),
\qquad
-\log(1-p^{-(j+1)}).
\]

Therefore the tail jump is exactly

\[
\begin{aligned}
\Delta T_{p,j}
&=-\log(1-p^{-(j+1)})+\log(1-p^{-j})\\
&=-\log\frac{1-p^{-(j+1)}}{1-p^{-j}}\\
&=-g(\eta_{p,j})\log p.
\end{aligned}
\tag{19}
\]

At the same time `RE-076` shows that this higher-layer event contributes the positive atom `log p` to the corrected Chebyshev increment through `P_(>=2)`. Thus its two-coordinate contribution is exactly

\[
d\widehat H=\log p,
\qquad
d(-\widehat E)=g(\eta_{p,j})\log p.
\tag{20}
\]

This is precisely (2) with an atom

\[
(\log p)\,\delta_{\eta_{p,j}}.
\tag{21}
\]

No asymptotic approximation, bounded-packet hypothesis, or fixed layer depth is involved. An arbitrarily large mixed higher-layer packet is simply a finite positive atomic measure added to the continuous selector-dilation measure from Section 2.

First-layer births are the unique exception. When a new prime `p` enters the support, there was no previous finite-exponent tail term; the birth creates

\[
\tau_p=-\log(1-p^{-2})>0.
\tag{22}
\]

It contributes no atom to `P_(>=2)` and therefore no atomic mass to `widehat H`. In `widehat E` it offsets part of the smooth decrease by exactly `tau_p`. This explains both the sign and the exact location of the correction `B_1` in (2). It is not a proof error or an untracked endpoint term: it is the sole structural mismatch between the two ledgers.

## 4. Concatenation gives one global positive transport measure

For each fixed-state cell piece, take the measure `dZ` from (11). For each switch, push the positive measure `dD_c(t)` through `Z_c(t)` and add the higher-layer atoms (21). All these pieces are positive on sufficiently late fans. The active-event representation `Y=Phi(Z)` and the monotone common-amplitude selector geometry place every switch event coordinate between its endpoint selectors, so concatenating the pieces along an oriented segment produces a positive measure `mu_(0,1)` supported on `[Z_0,Z_1]`.

Its total mass is exactly the corrected Chebyshev growth. Cell pieces contribute their selector displacement. A switch contributes

\[
D_c(Y_+)-D_c(Y_-)
+P_{\ge2}(-,+),
\]

which is exactly the switch increment of `widehat H` from `RE-076`. Summing therefore proves (1).

For the reciprocal coordinate, equation (10) gives the cell contribution, equation (17) gives the smooth switch contribution, and equation (19) gives every higher-layer atomic contribution. The only missing terms are the positive first-layer tail births (22). Hence

\[
\widehat E_0-\widehat E_1
=\int g\,d\mu_{0,1}-B_1(0,1),
\]

which is (2).

Because `g` is positive and strictly decreasing and the support lies in `[Z_0,Z_1]`,

\[
g(Z_1)\mu_{0,1}([Z_0,Z_1])
\le\int g\,d\mu_{0,1}
\le g(Z_0)\mu_{0,1}([Z_0,Z_1]).
\]

Substituting (1)--(2) proves (3)--(4), and bounded selector dilation gives (5).

The birth correction has an absolutely summable tail. Every support birth after the beginning of a sufficiently late segment has `p>=Z_0-O(1)` by the first-layer event/fringe geometry already used in `RE-075` and `RE-078`, and

\[
0<\tau_p
=-\log(1-p^{-2})
\ll p^{-2}.
\]

Therefore, even after replacing primes by all integers,

\[
B_1(0,\infty)
\ll\sum_{n\ge Z_0-O(1)}n^{-2}
\ll Z_0^{-1},
\]

which proves (6). No prime number theorem is required.

There is also a pointwise shadow of the same dependence. `RE-040` gives uniformly

\[
Z-Y=(b+o_J(1))hY\log Y,
\]

while the higher-layer mass in `widehat H=(Z-Y)+P_C` is only square-root scale and therefore lower order because `b_1<1/2`. `RE-078` gives

\[
\widehat E=(1-b)h(1+o_J(1)).
\]

Hence every selected point satisfies

\[
\boxed{
\widehat H
=b\,hY\log Y\,(1+o_J(1)),
\qquad
Y\log Y\,\widehat E
=(1-b)hY\log Y\,(1+o_J(1)).}
\tag{23}
\]

In particular the threshold itself is asymptotically reconstructed from the two corrected values:

\[
\boxed{
b
=\frac{\widehat H}
{\widehat H+Y\log Y\,\widehat E}
+o_J(1).}
\tag{24}
\]

The two coordinates are therefore coupled both infinitesimally by (2) and pointwise by (23)--(24).

## 5. Boundary tests and what this rules out

A fixed-state cell is the cleanest control. There are no event atoms and no first-layer births, so (2) reduces to the elementary exact identity

\[
\widehat E_0-\widehat E_1
=\log\frac{\log Z_1}{\log Z_0}
=\int_{Z_0}^{Z_1}\frac{ds}{s\log s}.
\]

For a pure higher-layer atomic transition, (19)--(20) give the identity one event at a time. For a first-layer birth, the positive `tau_p` correction is necessary: omitting it would falsely assert an atomic Chebyshev contribution that does not exist. These three controls fix the sign and show why the correction in (2) cannot be dropped.

Positivity of the smooth switch measure is a late-fan statement. It uses the same common-positive small-height regime and compact threshold interval as `RE-076`; the finding does not assert that `D_c'(t)>0` for arbitrary early CA states. Likewise, the support statement is about the selected CA fan, not arbitrary pairs of CA numbers.

The bound (6) must not be overread. On an arbitrarily short cell or switch, `widehat E_0-widehat E_1` can be smaller than `1/Z_0`, so the first-layer correction need not be relatively negligible for that particular increment. What is summable is its **entire future total**. This distinction is required to avoid turning an absolute tail estimate into a false local asymptotic.

Most importantly, (1)--(5) do not contradict false RH. They instead remove a tempting source of artificial coercivity. A proof cannot take a same-scale segment, charge its increase in `widehat H`, charge its decrease in `widehat E` again as an independent phenomenon, and multiply or add the two lower bounds as though they came from different arithmetic resources. Up to first-layer births, they are moments of one positive measure.

This also reframes `RE-071`--`RE-073`. Their opposite Chebyshev/Mertens drift on matched first-layer runs was a restricted asymptotic manifestation of the exact kernel duality now visible globally. `RE-076` and `RE-078` correctly establish opposite monotonicity through arbitrary packets, but the present identity shows that monotonicity alone supplies only one transport degree of freedom.

## 6. Prior-art boundary and the remaining research target

The prime-layer event equations and exact CA workload are close to the August 2026 framework of Marco Mantovanelli already anchored in `SOURCES.md`; in particular, that work is the appropriate prior-art boundary for interpreting CA transitions as an event measure integrated against the Robin kernel. No novelty is claimed for event-measure or workload bookkeeping itself. A directed current audit did not locate an external statement identifying Mathia's two **adaptive fringe-corrected fan Lyapunov coordinates** as the unweighted and `g`-weighted moments of one positive transport measure, nor the first-layer support-birth term as their sole exact mismatch. No external theorem beyond already anchored sources is load-bearing here, so `SOURCES.md` requires no change.

The strategic consequence is negative but useful. After `RE-078`, the live problem should not be phrased as obtaining independent upper capacities for two monotone source coordinates on the same physical window. The information that can still separate the genuine prime source from an abstract monotone control is finer:

- how the mass of `mu_(0,1)` is distributed between the beginning and end of a long selector interval, since `g` changes across scale;
- whether actual prime-layer arithmetic forbids the concentration profile needed by a false-RH fan;
- whether first-layer births, despite their summable tail, force a separate combinatorial or spacing cost;
- or whether an external prime-source estimate bounds one moment of `mu` more sharply than follows from the other.

In particular, bounded-dilation windows are now conceptually exhausted by the two monotonicity laws alone: equation (5) makes their costs equivalent after the natural factor `Z log Z`. New leverage must come from **scale separation or source-specific structure**, not from counting `widehat H` and `widehat E` twice.