# ANF-142 — positive residual slack excludes exponential late-tail zero pinching

**Status:** `EXACT-DERIVED + POSITIVE-TRANSLATION-CASCADE + POSITIVE-RESIDUAL-SLACK + FINITE-A-ACTIVATION + ACTIVE-TAIL-ZERO-SEPARATION + ONE-SIDED-FLOOR-STABILITY + ARBITRARY-TERMINAL-DEPTH + SUBEXPONENTIAL-LOCAL-LOSS`. `ANF-137` isolates historical-zero pinching through the spend ratio `T/s`, while `ANF-141` shows that finite-`A` activation quantizes every physically present late layer. Combining those two facts removes the remaining possibility that the **physically active late tail itself** creates a fixed positive exponential source loss on the branch

\[
\delta_d\downarrow\delta_\infty>0.
\]

Cut the formal `ANF-133` cascade after stage `k`, terminate it at any finite `D>k`, and write

\[
T:=T_k^\infty=\delta_k-\delta_\infty.
\tag{1}
\]

At physical scale `A`, let

\[
m_{d,A}=\lfloor\theta_dA\rfloor
\]

and call a tail layer `d>k` **active** when `m_{d,A}\ge1`. Then every active historical tail layer satisfies, at every terminal ideal critical point `\xi\in K_D`,

\[
\boxed{
J_{d-1}\left(1+\frac{T_{d,D}}{s_d}\right)
\le \frac{AT}{\log2}.
}
\tag{2}
\]

Consequently every primitive binomial belonging to a physically active tail layer stays at distance at least

\[
\boxed{
\operatorname{dist}\bigl(\xi,Z(B_{j,d-1})\bigr)
\ge
\frac{2\delta_\infty}{\pi}e^{-AT}
}
\tag{3}
\]

from the terminal ideal critical skeleton. The corresponding **physical** tail curvature obeys

\[
\boxed{
0\le
-\bigl(G^{\rm phys}_{k:D,A}\bigr)''_{\rm tail}(\xi)
\le
C_{\delta_\infty}\,T\,e^{2AT}.
}
\tag{4}
\]

There is also a floor-stability statement that includes the formally present but physically inactive late layers. If `\mathcal M^{\rm ideal}_{k:D,A}` uses exponents `\theta_dA` and `\mathcal M^{\rm phys}_{k:D,A}` uses `m_{d,A}`, then at every real point where the ideal factors are finite,

\[
\boxed{
\frac{|\mathcal M^{\rm phys}_{k:D,A}(\alpha)|^2}
{|\mathcal M^{\rm ideal}_{k:D,A}(\alpha)|^2}
\ge e^{-2AT}
}
\tag{5}
\]

whenever the ratio is interpreted by continuity at removable common zeros. Thus flooring can make the physical tail **larger** when it removes a small ideal factor, but it cannot make it exponentially smaller by more than the future-slack budget.

Because `T_k^\infty\to0`, every moving cut `k=k(A)\to\infty` has

\[
AT_k^\infty=o(A).
\tag{6}
\]

Equations (3)--(5) therefore become uniformly subexponential, independently of how large the finite terminal depth `D(A)\ge k(A)` is. In particular, the mesoscopic regime left open by `ANF-141`,

\[
1\ll AT_k^\infty\ll A,
\]

can contain arbitrarily many active finite-`A` phase layers, but **those layers cannot create a new fixed positive exponential pinching loss at the terminal ideal saddles**. Any remaining arbitrary-depth failure on the `\delta_\infty>0` branch must occur at a finer-than-exponential scale, or through a one-sided physical oversource caused by omitted small ideal factors, or through conditioning already accumulated in the earlier prefix.

This is stronger than merely observing that `M=o(A)`. The load-bearing point is that activation supplies a lower bound on the *own spend* `s_d` of every physically present layer, exactly cancelling the dangerous denominator in the `ANF-137` ratio `T_{d,D}/s_d`.

## 1. Physical activation cancels the dangerous spend denominator

Retain the slack notation

\[
s_d
=\delta_{d-1}-\delta_d
=2\theta_dJ_{d-1}\log2,
\qquad
T_{d,D}
=\delta_d-\delta_D.
\tag{7}
\]

If tail layer `d` is physically active, then

\[
m_{d,A}=\lfloor\theta_dA\rfloor\ge1,
\]

so

\[
\theta_dA\ge1.
\tag{8}
\]

Multiplying (7) by `A` gives the exact activation inequality already implicit in `ANF-141`,

\[
As_d
=2(\theta_dA)J_{d-1}\log2
\ge2J_{d-1}\log2.
\tag{9}
\]

Hence

\[
J_{d-1}
\le\frac{As_d}{2\log2}.
\tag{10}
\]

For every `k<d\le D`, both

\[
s_d\le T_k^\infty=T
\]

and

\[
T_{d,D}\le T_k^\infty=T.
\]

Therefore

\[
\begin{aligned}
J_{d-1}\left(1+\frac{T_{d,D}}{s_d}\right)
&=J_{d-1}
+J_{d-1}\frac{T_{d,D}}{s_d}\\
&\le
\frac{As_d}{2\log2}
+\frac{AT_{d,D}}{2\log2}\\
&\le\frac{AT}{\log2},
\end{aligned}
\tag{11}
\]

which proves (2).

This is the finite-scale counterpart of the obstruction in `ANF-137`. There, a tiny `s_d` can make `T_{d,D}/s_d` arbitrarily large. Here a layer with such tiny spend is simply absent until `A` is large enough that `\theta_dA\ge1`; once it becomes physically present, (9) says that its denominator cannot be smaller than one `A^{-1}` quantum per critical chamber.

## 2. Every active late zero is uniformly separated from every terminal ideal saddle

`ANF-137` proves that for every terminal ideal critical point `\xi\in K_D` and every historical binomial

\[
B_{j,d-1}(\alpha)
:=1+e^{-2\pi i\tau_{j,d-1}\alpha},
\]

one has

\[
\operatorname{dist}\bigl(\xi,Z(B_{j,d-1})\bigr)
\ge
\frac{2\delta_{d-1}}{\pi}
2^{-J_{d-1}(1+T_{d,D}/s_d)}.
\tag{12}
\]

On the present branch

\[
\delta_{d-1}\ge\delta_\infty.
\tag{13}
\]

For a physically active tail layer, insert (2) into (12):

\[
2^{-J_{d-1}(1+T_{d,D}/s_d)}
\ge
2^{-AT/\log2}
=e^{-AT}.
\tag{14}
\]

Equations (12)--(14) prove (3).

The same substitution controls the individual modulus. `ANF-137` gives

\[
|B_{j,d-1}(\xi)|
\ge
2\,2^{-J_{d-1}(1+T_{d,D}/s_d)},
\]

hence

\[
\boxed{
|B_{j,d-1}(\xi)|\ge2e^{-AT}
}
\tag{15}
\]

for every primitive factor in every physically active tail layer. Thus no active late factor can be exponentially closer than rate `T` to a terminal ideal saddle.

Notice the quantifier: `D` is arbitrary and finite. The bound depends only on the future slack available immediately after the cut, not on the number of subsequent formal stages.

## 3. The physical late-tail curvature is paid by the same mesoscopic quantum

At a terminal ideal saddle, `ANF-137` bounds the weighted curvature of the **ideal** stage-`d` layer by

\[
0\le
-2\theta_d(\log|Q_{d-1}|)''(\xi)
\le
\frac{\pi^2s_d}
{4\log2\,\delta_{d-1}^2}
4^{J_{d-1}(1+T_{d,D}/s_d)}.
\tag{16}
\]

The physical coefficient is `m_{d,A}/A\le\theta_d`, so the physical contribution is no larger. Using (2), (13), and

\[
4^{AT/\log2}=e^{2AT},
\]

we obtain

\[
0\le
-2\frac{m_{d,A}}A(\log|Q_{d-1}|)''(\xi)
\le
C_{\delta_\infty}s_de^{2AT}.
\tag{17}
\]

Summing only over physically active layers after `k`,

\[
\sum_{d=k+1}^{D}s_d
\le T,
\]

which proves (4).

A first-derivative bound is equally explicit. From

\[
B(\alpha)=2e^{-\pi i\tau\alpha}\cos(\pi\tau\alpha)
\]

and (15),

\[
\left|(\log|B|)'(\xi)\right|
=\pi\tau|\tan(\pi\tau\xi)|
\le C_{\delta_\infty}e^{AT},
\tag{18}
\]

because `ANF-134` gives `\tau\le1/(2\delta_\infty)`. The exact active primitive-factor count from `ANF-141`,

\[
M_{k,D,A}
=\sum_{d=k+1}^{D}m_{d,A}J_{d-1}
\le\frac{AT}{2\log2},
\tag{19}
\]

therefore gives the normalized physical-tail slope estimate

\[
\boxed{
\left|
\bigl(G^{\rm phys}_{k:D,A}\bigr)'_{\rm tail}(\xi)
\right|
\le
C_{\delta_\infty}T e^{AT}.
}
\tag{20}
\]

Equations (3), (4), and (20) show that the complete physically active tail is locally conditioned at terminal ideal saddles on an `e^{-O(AT)}` spatial scale. If `k(A)\to\infty`, this is `e^{-o(A)}` automatically.

## 4. Flooring the whole late tail is one-sided stable, including inactive layers

The preceding section concerns the factors that are physically present. The potentially subtler issue is that the terminal ideal cascade also contains formal layers with

\[
0\le\theta_dA<1,
\qquad
m_{d,A}=0.
\]

Such a layer is omitted completely by the physical floor and may be arbitrarily close to a zero at the terminal ideal saddle. That can make the physical modulation much **larger** than the ideal one. It cannot create a comparable downward loss.

Let

\[
f_{d,A}:=\theta_dA-m_{d,A}\in[0,1)
\tag{21}
\]

be the fractional repetition removed by flooring. Pointwise,

\[
\log
\frac{|\mathcal M^{\rm phys}_{k:D,A}|^2}
{|\mathcal M^{\rm ideal}_{k:D,A}|^2}
=-2\sum_{d=k+1}^{D}
f_{d,A}\log|Q_{d-1}|.
\tag{22}
\]

Whenever `|Q_{d-1}|\le1`, the corresponding summand in (22) is nonnegative and may be discarded in a lower bound. If `|Q_{d-1}|>1`, positivity gives

\[
|Q_{d-1}|\le2^{J_{d-1}},
\]

so

\[
-2f_{d,A}\log|Q_{d-1}|
\ge
-2f_{d,A}J_{d-1}\log2.
\tag{23}
\]

Split the layers into active and inactive ones. For active layers, `f_{d,A}<1` and `m_{d,A}\ge1`, hence

\[
\sum_{\rm active}f_{d,A}J_{d-1}
\le
\sum_{\rm active}J_{d-1}
\le
M_{k,D,A}
\le\frac{AT}{2\log2}.
\tag{24}
\]

For inactive layers, `m_{d,A}=0`, so `f_{d,A}=\theta_dA` and

\[
\sum_{\rm inactive}f_{d,A}J_{d-1}
=A\sum_{\rm inactive}\theta_dJ_{d-1}
=\frac{A}{2\log2}
\sum_{\rm inactive}s_d
\le\frac{AT}{2\log2}.
\tag{25}
\]

Thus

\[
\sum_{d=k+1}^{D}f_{d,A}J_{d-1}
\le\frac{AT}{\log2}.
\tag{26}
\]

Combining (22)--(26) yields

\[
\log
\frac{|\mathcal M^{\rm phys}_{k:D,A}|^2}
{|\mathcal M^{\rm ideal}_{k:D,A}|^2}
\ge-2AT,
\]

which is exactly (5).

This estimate is deliberately one-sided. If an inactive ideal factor is extremely small, removing it can produce an arbitrarily large *increase* in physical modulation. Such a floor-induced oversource is a genuine remaining failure mode. What is now excluded is the opposite interpretation: inactive or barely active late layers cannot be blamed for a new fixed positive exponential **loss** at an ideal source-carrying saddle.

## 5. Uniform consequence for every unbounded moving cut

Assume throughout this section that

\[
\delta_\infty>0
\]

and take any integer-valued moving cut

\[
k(A)\longrightarrow\infty.
\]

Then

\[
T_{k(A)}^\infty\longrightarrow0,
\]

so

\[
AT_{k(A)}^\infty=o(A).
\tag{27}
\]

For every arbitrary finite terminal depth `D(A)\ge k(A)`, equations (3)--(5) become

\[
\operatorname{dist}(\xi,Z_{\rm active\ tail})
\ge e^{-o(A)},
\tag{28}
\]

\[
-\bigl(G^{\rm phys}_{\rm tail}\bigr)''(\xi)
\le e^{o(A)},
\qquad
\left|\bigl(G^{\rm phys}_{\rm tail}\bigr)'(\xi)\right|
\le e^{o(A)},
\tag{29}
\]

and

\[
\frac{|\mathcal M^{\rm phys}_{\rm tail}(\xi)|^2}
{|\mathcal M^{\rm ideal}_{\rm tail}(\xi)|^2}
\ge e^{-o(A)}
\tag{30}
\]

at every terminal ideal critical point `\xi\in K_{D(A)}`.

The prefix `1,\ldots,k(A)` is a different object. For each fixed `k`, `ANF-137` gives finite future-uniform zero-separation and derivative/curvature constants for those finitely many historical factors by replacing `T_{d,D}` with the finite limit `T_{d,\infty}`. A standard `ANF-138` slow selection can therefore make those **prefix** constants subexponential before allowing `k(A)` to increase. Once that is done, (28)--(30) show that no choice of the later finite terminal depth can reintroduce a fixed positive exponential local loss through the physically active tail.

Equivalently: on the positive-residual-slack branch, exponential local conditioning is a **prefix-diagonalizable** issue. The arbitrarily deep physical tail is automatically harmless in the downward direction at exponential scale. This is the quantifier improvement over `ANF-137`: its raw `Omega_D=o(A)` hypothesis is not needed for layers that are both late and physically active, because activation itself bounds their dangerous spend ratios.

## 6. What remains after the mesoscopic tail is de-pinned

The result does **not** prove a depth-uniform constant comparison

\[
E_0(X_A^{(D(A))})\asymp E_A.
\]

Subexponential conditioning still permits polynomial or stretched-exponential prefactor loss, and `ANF-141` explicitly leaves a mesoscopic number of active stages available. A single fixed-order zero already changes a Gaussian saddle integral by a power of `A`, so an unbounded mesoscopic sequence can matter even when no individual stage produces a fixed exponential-rate penalty.

Nor does (5) give a two-sided floor comparison. Omitting a formal factor with very small modulus can raise the physical modulation drastically. If that creates a new oversource, the physical cascade may fail source criticality for the opposite reason. Controlling or exploiting that one-sided oversource now becomes more relevant than searching for another late-tail pinching mechanism.

The theorem also remains specific to the positive binomial translation architecture of `ANF-133`. Signed or complex coefficients remove the coefficient-mass bound `|Q|\le2^J`, and a different physical discretization need not obey the activation inequality (9).

Within the present architecture, however, the live `\delta_\infty>0` gate is narrower than after `ANF-141`: **the mesoscopic finite-`A` tail can still perform unboundedly many exact phase cancellations, but it cannot hide an exponential source deficit inside historical-zero pinching.** Any fatal continuation must survive at the prefactor scale, or turn floor-induced oversource into a controlled new critical carrier, rather than relying on another exponential local-conditioning collapse.

## 7. Prior-art boundary

A directed audit against classical finite Riesz products, Remez-type inequalities for trigonometric polynomials, and saddle/Laplace asymptotics found the expected general theories of cosine-product concentration, small-value sets, and degenerate saddles. None supplies the Mathia-specific identity (2): it comes from combining the exact `ANF-137` future-to-own slack ratio with the exact finite-`A` activation quantum of `ANF-141`. The floor estimate (5) likewise uses only positivity, the exact coefficient mass `2^{J_{d-1}}`, and the internal slack bookkeeping.

No external theorem is load-bearing for (2)--(5), so `SOURCES.md` is unchanged. No novelty claim is made for the classical trigonometric inequalities themselves.

## 8. Research disposition

This finding advances the accepted positive-cascade obstruction without resolving `CLUE-near-extremizer-notch-exposure-envelope.md`. The clue asks for the true all-cardinality physical notch-exposure envelope. Here the conclusion is narrower: on the same-profile positive cascade and under `\delta_\infty>0`, finite-`A` activation eliminates exponential **downward** late-tail zero pinching as an independent escape mechanism.

The next decisive test is therefore prefactor-scale. Either prove that the accumulated polynomial/stretched-exponential losses of the mesoscopic active tail remain source-coercive, or show that the one-sided floor oversource in (5) can be repeatedly retuned without consuming the positive residual slack. A result at that scale would genuinely decide whether the positive-residual-slack branch can still support a fatal arbitrary-depth physical cascade.