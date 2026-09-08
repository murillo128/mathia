# ANF-113 — relative endpoint localization makes capacity-saturated supercritical tails cascade

**Status:** `EXACT-DERIVED + RELATIVE-ENDPOINT-TRANSFER + SHARP-HEIGHT-CAPACITY-NORMALIZATION + SUPERCRITICAL-SPARSE-NARROWING + FIXED-NOTCH-COMPENSATOR-REFINEMENT`. `ANF-112` proves packet transfer under the absolute localization hypothesis `E_in(P_n)=o(L_n)`, and from that recovers every source-heavy sub-square-root packet with `4πH_n/log R_n -> 1`. The absolute normalization is stronger than the transfer actually needs. Once the packet source mass is written as

\[
M_n:=\frac{E_0(P_n)}{L_n},
\]

all polarization estimates naturally live at scale `M_nL_n`. Therefore it is enough that the packet be endpoint-localized **relative to its own source norm**,

\[
\frac{E_{\rm in,\delta_n}(P_n)}{E_0(P_n)}\to0,
\qquad \delta_n\downarrow0.
\]

This matters precisely beyond the leading-critical chamber. Let

\[
R_n:=\frac{L_n}{m_n^2}\to\infty,
\qquad
A_n:=4\pi H_n,
\qquad
m_n:=|P_n|,
\]

and assume the packet is source-heavy, `M_n>=lambda>0`. The exact linear zero of the Montgomery--Taylor spectrum gives a universal height-capacity envelope of order

\[
M_n\ \lesssim\ \frac{e^{A_n}}{R_nA_n^2}.
\]

If the packet lies within a **subexponential factor** of that envelope,

\[
\boxed{
\log_+\!\left(\frac{e^{A_n}}{R_nM_nA_n^2}\right)=o(A_n),
}
\tag{1}
\]

then it is automatically relatively localized in a shrinking endpoint band. The packet theorem can therefore be restarted and forces a fresh disjoint source-heavy layer at height tending to infinity.

Consequently, multiplicative supercriticality `A_n >= (1+c)log R_n` is not by itself an escape from the height cascade. A sparse supercritical packet can avoid this mechanism only by being **exponentially source-unsaturated** relative to the amount of source energy its height could support, or by leaving the sub-square-root regime. In the notch-invisible chamber of `ANF-107`, this means that a capacity-saturated sparse compensator cannot remain an isolated source-cancellation device: it must spawn new disjoint height mass.

## 1. Packet-relative localization is the correct transfer hypothesis

Retain the setup of `ANF-112`. Let `W_n=P_n\sqcup U_n` be a physical Montgomery--Taylor near-extremizer with

\[
L_n:=L(W_n)\to\infty,
\qquad
E_0(W_n)=L_n+o(L_n),
\qquad
|P_n|=o(L_n).
\tag{2}
\]

Assume the packet is source-heavy and write

\[
M_n:=\frac{E_0(P_n)}{L_n}\ge\lambda>0.
\tag{3}
\]

The affine floor argument of `ANF-112` gives, with no upper bound on `M_n`,

\[
\mathcal C_0(P_n,U_n)
\le
-\left(\frac12-o(1)\right)M_nL_n,
\tag{4}
\]

and the triangle inequality gives

\[
E_0(U_n)
\le
L_n\bigl(\sqrt{M_n}+1+o(1)\bigr)^2.
\tag{5}
\]

Now weaken the localization assumption. Suppose there are `delta_n downarrow 0` such that

\[
\varepsilon_n
:=
\frac{E_{\rm in,\delta_n}(P_n)}{E_0(P_n)}
\to0,
\tag{6}
\]

where

\[
E_{\rm in,\delta}(X)
:=
\int_{|\alpha|\le1-\delta}
J_0(\alpha)|S_X(\alpha)|^2\,d\alpha.
\]

By Cauchy--Schwarz and (5),

\[
\begin{aligned}
\frac{|\mathcal C_{\rm in,n}|}{M_nL_n}
&\le
\sqrt{
\frac{E_{\rm in,\delta_n}(P_n)}{M_nL_n}
\frac{E_0(U_n)}{M_nL_n}
}\\
&\le
\sqrt{\varepsilon_n}
\left(1+\frac1{\sqrt{M_n}}+o(1)\right)
=o(1),
\end{aligned}
\tag{7}
\]

uniformly because `M_n>=lambda`. Thus the negative polarization (4) again has to occur in the endpoint band:

\[
\mathcal C_{\rm edge,n}
\le
-\left(\frac12-o(1)\right)M_nL_n.
\tag{8}
\]

Since `E_edge(P_n)<=E_0(P_n)=M_nL_n`, endpoint Cauchy--Schwarz yields

\[
\boxed{
E_{\rm edge,\delta_n}(U_n)
\ge
\left(\frac14-o(1)\right)M_nL_n.
}
\tag{9}
\]

The rest of the extraction in `ANF-112` is unchanged. For any fixed `0<theta<1`, set

\[
h_n=
\frac{1-\theta}{4\pi}
\log\frac1{\delta_n}.
\tag{10}
\]

The endpoint anti-concentration estimate of `ANF-108`, applied to the part of `U_n` below height `h_n`, shows that the complementary layer

\[
V_n:=\{u\in U_n:|\operatorname{Im}u|>h_n\}
\]

satisfies

\[
\boxed{
E_0(V_n)
\ge
c_{\lambda,\theta}M_nL_n.
}
\tag{11}
\]

In particular `V_n` is disjoint from `P_n`, source-heavy at the packet's own scale, and `h_n->infinity` whenever `delta_n->0`. The absolute hypothesis `E_in=o(L)` of `ANF-112` is therefore sufficient but not necessary; **relative endpoint localization `E_in=o(E_0(P))` is the natural packet-transfer condition.**

## 2. The linear endpoint zero gives an exact interior-capacity estimate

Now specialize to a sparse packet `P` of cardinality `m` and maximal height `H`. Put

\[
A:=4\pi H,
\qquad
R:=\frac{L}{m^2}.
\tag{12}
\]

From `ANF-103`, the explicit Montgomery--Taylor spectrum satisfies

\[
0\le J_0(\alpha)\le G^2(1-|\alpha|),
\qquad |\alpha|\le1,
\tag{13}
\]

and the structure factor obeys

\[
|S_P(\alpha)|^2\le m^2e^{A|\alpha|}.
\tag{14}
\]

For `0<delta<1`, equations (13)--(14) give

\[
\begin{aligned}
E_{\rm in,\delta}(P)
&\le
2G^2m^2
\int_0^{1-\delta}
(1-\alpha)e^{A\alpha}\,d\alpha\\
&=
\frac{2G^2m^2}{A^2}
\left[
(1+A\delta)e^{A(1-\delta)}-(1+A)
\right]\\
&\le
\boxed{
\frac{2G^2m^2}{A^2}
(1+A\delta)e^{A(1-\delta)}.
}
\end{aligned}
\tag{15}
\]

The same integral with `delta=0` recovers the sharp universal source envelope

\[
E_0(P)
\le
2G^2m^2\frac{e^A-1-A}{A^2}
\le
2G^2m^2\frac{e^A}{A^2}.
\tag{16}
\]

If `M=E_0(P)/L`, then (16) becomes

\[
\boxed{
M\le
2G^2\frac{e^A}{RA^2}.
}
\tag{17}
\]

Thus `e^A/(RA^2)` is the correct universal source-capacity scale attached only to packet cardinality and maximal height. It is deliberately an upper envelope: no phase coherence, horizontal geometry, separation, or multiplicity assumption is used.

Dividing (15) by the **actual** packet energy `E_0(P)=ML=MRm^2` gives the more useful estimate

\[
\boxed{
\frac{E_{\rm in,\delta}(P)}{E_0(P)}
\le
2G^2
\frac{e^A}{RMA^2}
(1+A\delta)e^{-A\delta}.
}
\tag{18}
\]

This is the quantitative bridge missing from the absolute normalization in `ANF-112`.

## 3. Subexponential capacity deficit forces shrinking-band localization

Return to a sequence with `R_n->infinity` and `M_n>=lambda>0`. By the source-heavy threshold of `ANF-103`, `A_n->infinity`. Define the logarithmic capacity deficit

\[
D_n
:=
\log_+\!\left(
\frac{e^{A_n}}{R_nM_nA_n^2}
\right).
\tag{19}
\]

Assume

\[
D_n=o(A_n),
\tag{20}
\]

which is exactly condition (1). Choose

\[
x_n:=2D_n+\sqrt{A_n},
\qquad
\delta_n:=\frac{x_n}{A_n}.
\tag{21}
\]

Then `x_n->infinity`, `x_n=o(A_n)`, and therefore `delta_n->0`. Substituting (21) into (18),

\[
\frac{E_{\rm in,\delta_n}(P_n)}{E_0(P_n)}
\le
2G^2
\exp(D_n-x_n)
(1+x_n).
\tag{22}
\]

Because

\[
D_n-x_n
=-D_n-\sqrt{A_n},
\]

the right side of (22) tends to zero. Hence

\[
\boxed{
\frac{E_{\rm in,\delta_n}(P_n)}{E_0(P_n)}\to0,
\qquad
\delta_n\to0.
}
\tag{23}
\]

Section 1 now applies. For every fixed `0<theta<1`, the unused remainder contains a disjoint layer `V_n` above

\[
\boxed{
|\operatorname{Im}z|
>
\frac{1-\theta}{4\pi}
\log\frac{A_n}{2D_n+\sqrt{A_n}},
}
\tag{24}
\]

with

\[
\boxed{
E_0(V_n)
\ge
c_{\lambda,\theta}M_nL_n.
}
\tag{25}
\]

Since `D_n=o(A_n)`, the logarithm in (24) tends to infinity. Thus **subexponential loss relative to the universal height-capacity envelope is insufficient to stop the disjoint height cascade.**

## 4. This strictly extends the leading-critical chamber of ANF-112

If

\[
\frac{A_n}{\log R_n}\to1
\]

and `M_n>=lambda`, then

\[
D_n
\le
(A_n-\log R_n)_+
+O(\log A_n)
=o(A_n),
\]

so (20) holds. Therefore `ANF-112` is recovered, including additive supercritical excesses that diverge but remain `o(log R_n)`.

The new content appears when the height is genuinely multiplicatively supercritical. Suppose, for example,

\[
A_n\sim\kappa\log R_n,
\qquad \kappa>1.
\tag{26}
\]

The universal envelope (17) allows source mass as large as

\[
M_n
\lesssim
\frac{R_n^{\kappa-1}}{(\log R_n)^2}
\]

up to constant and subpower factors. If the actual packet realizes that polynomial exponent, more generally if

\[
\log M_n
=
(\kappa-1)\log R_n-o(\log R_n),
\tag{27}
\]

then `D_n=o(A_n)` and the cascade still restarts. Thus the escape condition from `ANF-112`, `A_n >= (1+c)log R_n`, was only a **necessary first geometric screen**. It is not sufficient once the packet's actual source mass is tracked.

Conversely, if a source-heavy sub-square-root packet avoids the conclusion of Section 3, then after passing to a subsequence there is `epsilon>0` such that

\[
D_n\ge\epsilon A_n.
\]

Equivalently,

\[
\boxed{
M_n
\le
\frac{e^{(1-\epsilon)A_n}}{R_nA_n^2}
}
\tag{28}
\]

up to an inessential constant absorbed by reducing `epsilon`. A genuinely surviving sparse supercritical packet must therefore be **exponentially inefficient in height**: a fixed exponential fraction of the pointwise Fourier--Laplace capacity available at its maximal height is not realized in its actual Montgomery--Taylor source norm.

## 5. Consequence inside the fixed-notch intermediate chamber

`ANF-107` shows that for fixed `0<eta<1`, a sub-square-root tail can be source-heavy while remaining notch-negligible throughout the chamber below

\[
4\pi\eta H
=
\log R+2\log\log R+O_\eta(1).
\tag{29}
\]

Such a tail acts only as a source compensator: its own notch energy and notch cross term are `o(L)`, while its negative source polarization lies in `J_0-phi_eta`.

The present finding adds a second restriction on that compensator. If its height is multiplicatively supercritical but still below the direct notch threshold, and its actual source mass is subexponentially close to the universal height-capacity scale in the sense of (1), then it cannot remain an isolated compensating tail. Equations (23)--(25) force new disjoint source-heavy height mass in the remainder.

For a finite ratio `A_n/log R_n -> kappa` with

\[
1<\kappa<\frac1\eta,
\]

a fatal notch-invisible sparse compensator must therefore do at least one of three things: leave the sub-square-root population regime, become exponentially source-unsaturated as in (28), or generate another disjoint high source-heavy layer. The former vague label “multiplicatively supercritical tail” is no longer a single escape chamber.

## 6. Adversarial checks and exact boundary

The normalization in Section 1 is essential. If only `E_in(P)=o(E_0(P))` is known while `M_n` is allowed to tend to zero, then (7) need not be small relative to the polarization scale; the fixed lower bound `M_n>=lambda` is therefore retained. This is not restrictive for the cascade branch, which by definition concerns source-heavy packets.

No lower bound on `E_edge(P)` is assumed. In deriving (9), using only `E_edge(P)<=E_0(P)` is conservative: if the packet has even less endpoint energy, Cauchy--Schwarz forces still more endpoint energy into the remainder. Likewise, (15)--(18) use the maximally coherent pointwise bound `|S_P|<=m e^{2pi|alpha|H}` and hence remain valid with arbitrary horizontal locations, multiplicities, collisions, and phase cancellation.

Condition (1) is sufficient, not necessary. Failure of (1) does **not** construct a counterexample and does not prove that a source-unsaturated packet can actually occur inside a physical near-extremizer. It only identifies the new quantitative escape that this method cannot eliminate. Nor does (25) show that the fresh layer is itself sub-square-root, capacity-saturated, or directly notch-visible; every new layer still has to be reclassified before recursion.

The `A^{-2}` factor is load-bearing only in defining the sharp height-capacity scale. It comes directly from the already-canonical linear endpoint zero of `J_0`; no external asymptotic theorem is used. If one dropped that factor and worked with the cruder `e^A/R` envelope, the qualitative subexponential conclusion would survive, but the matched `2 log log R` calibration from `ANF-103` would be obscured.

## 7. Prior-art boundary and research consequence

A targeted prior-art search used two independent formulations around endpoint concentration of exponential/Fourier--Laplace sums and a neighboring search around Turán--Nazarov, Paley--Wiener concentration, and concentration--compactness/profile decomposition. Classical Turán--Nazarov/Logvinenko--Sereda theory controls how exponential or bandlimited functions can concentrate on measurable sets, while Paley--Wiener concentration results optimize or bound mass placement under bandwidth constraints. No located result supplies the specific packet-relative transfer used here: the combination of the Montgomery--Taylor affine floor, a source-heavy component's forced negative polarization at scale `E_0(P)`, the linearly vanishing source spectrum, and a disjoint physical height extraction. No external theorem is load-bearing, so `SOURCES.md` is unchanged.

The sparse fixed-notch frontier is therefore narrowed again. `ANF-112` showed that additive supercriticality `A-log R=o(log R)` cannot terminate the cascade. The present result shows that even **multiplicative** supercriticality cannot do so when the packet uses its available height efficiently. A surviving sparse obstruction must now pay not merely height, but a quantitative **source-capacity deficit**: after some generation it must either approach square-root population, become exponentially inefficient relative to `e^A/(RA^2)`, or leave the sparse-tail geometry for diffuse bulk. Determining whether physical Montgomery--Taylor near-extremality itself forbids that exponential source-unsaturation is the next sharp gate.