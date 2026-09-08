# ANF-119 — interior-saddle Gram mass forces excision, overpolarized companions, or profile mirroring

**Status:** `EXACT-DERIVED + GLOBAL-COMPLETION-TRICHOTOMY + MINIMAL-POLARIZATION-EXCISION + MESOSCOPIC-SADDLE-COMPANION + LARGE-MASS-PROFILE-MIRRORING + FIXED-NOTCH-SEPARATION`. `ANF-118` closes the internal same-saddle translation-cloud problem: throughout `log(e+V_A)=o(A^(1/3))`, one explicit Gaussian Gram form decides the complete mesoscopic Montgomery--Taylor source mass of the cloud. The remaining loophole was external cancellation: a source-heavy, fixed-notch-invisible cloud might still be indispensable because its source norm cancels against the rest of a global near-extremizer.

That external loophole has a rigid three-regime form. For any sublinear physical packet `P_n` inside a Montgomery--Taylor near-extremizer `W_n=P_n sqcup U_n`, let
\[
M_n:=\frac{E_0(P_n)}{L_n},\qquad L_n:=L(W_n),
\]
and suppose the packet is source-localized in a measurable spectral set `B_n` in the relative sense
\[
E_{B_n^c}(P_n)=o(E_0(P_n)).
\]
If `M_n->0`, the packet is source-excisable. If `M_n` stays bounded above and below, then deleting it is again harmless whenever the complement has only `o(L_n)` Montgomery--Taylor excess; otherwise the complement must carry an **overpolarized companion** in the same spectral set, with an exact quantitative energy floor. If `M_n->infinity`, the complement is forced to reproduce the packet with opposite phase in the localized spectral profile: the cancellation becomes asymptotically a full Hilbert-space mirror.

Applied to the `ANF-118` interior-saddle clouds, `B_n` may be taken to be a shrinking `A^(-1/2)`-scale neighborhood of `|alpha|=a_gamma`, entirely outside every fixed notch `|alpha|<=eta<a_gamma`. Thus the Gaussian Gram observable now classifies not only the cloud's internal source remainder, but also the kind of external cancellation any global near-extremal completion would have to realize. A bounded order-one Gram mass is harmless at minimal polarization and otherwise forces fresh same-saddle source energy in the external remainder; a diverging Gram mass forces asymptotic profile mirroring. The still-open obstruction is therefore no longer arbitrary external cancellation, but a coupled architecture in which off-notch saddle cancellation coexists with the separate central-notch exposure needed to reach the fatal envelope.

## 1. Exact affine bookkeeping identifies the overpolarization parameter

Retain the Montgomery--Taylor source notation
\[
E_0(X)=\|S_X\|_0^2,
\qquad
L(X)=2|X|-\sigma(X),
\qquad
\Delta(X)=E_0(X)-L(X)\ge0,
\]
with restricted energies and cross terms
\[
E_B(X):=\int_BJ_0(\alpha)|S_X(\alpha)|^2\,d\alpha,
\]
\[
\mathcal C_B(P,U):=
\operatorname{Re}\int_BJ_0(\alpha)
S_P(\alpha)\overline{S_U(\alpha)}\,d\alpha.
\tag{1}
\]
Let
\[
W_n=P_n\sqcup U_n
\tag{2}
\]
be conjugation-invariant physical multisets satisfying
\[
L_n:=L(W_n)\to\infty,
\qquad
\frac{\Delta(W_n)}{L_n}\to0,
\qquad
|P_n|=o(L_n).
\tag{3}
\]
As in `ANF-111`, define the affine split defect
\[
\kappa_n:=\sigma(P_n)+\sigma(U_n)-\sigma(W_n).
\]
Then
\[
0\le\kappa_n\le2|P_n|=o(L_n),
\qquad
L(U_n)=L_n-o(L_n),
\tag{4}
\]
and the exact polarization identity is
\[
\Delta(W_n)
=
\Delta(P_n)+\Delta(U_n)
+2\mathcal C_0(P_n,U_n)-\kappa_n.
\tag{5}
\]
Put
\[
M_n:=\frac{E_0(P_n)}{L_n},
\qquad
X_n:=\frac{\Delta(U_n)}{L_n}\ge0.
\tag{6}
\]
Since `L(P_n)=o(L_n)`, equation (5) immediately gives the sharper asymptotic identity
\[
\boxed{
\frac{2\mathcal C_0(P_n,U_n)}{L_n}
=-(M_n+X_n)+o(1).
}
\tag{7}
\]
Thus the floor-required polarization `-E_0(P_n)/2` is only the **minimal** cancellation. The amount by which the complement ceases to be near-extremal is exactly the additional negative polarization:
\[
\boxed{
\Delta(U_n)
=-2\mathcal C_0(P_n,U_n)-E_0(P_n)+o(L_n).
}
\tag{8}
\]
This identity is the missing global-completion bookkeeping. A source-heavy packet is not automatically essential merely because it cancels macroscopically; it is essential only if the cancellation is stronger than the minimum needed to absorb the packet's own source excess.

The triangle inequality supplies the uniform scale control needed below:
\[
\sqrt{E_0(U_n)}
\le
\sqrt{E_0(W_n)}+\sqrt{E_0(P_n)},
\]
so
\[
\boxed{
\frac{E_0(U_n)}{L_n}
\le
\bigl(1+\sqrt{M_n}+o(1)\bigr)^2.
}
\tag{9}
\]
In particular, whenever `M_n` lies in a fixed compact subinterval of `(0,infinity)`, both `X_n` and the complement source norm are `O(1)` after normalization by `L_n`.

## 2. Minimal polarization makes a fixed-notch-invisible packet globally excisable

First consider the source-negligible regime
\[
M_n\to0.
\tag{10}
\]
Then Hilbert geometry alone gives
\[
|E_0(U_n)-E_0(W_n)|
\le
2\sqrt{E_0(W_n)E_0(P_n)}+E_0(P_n)
=o(L_n).
\]
Together with (4),
\[
\boxed{
\frac{E_0(U_n)}{L(U_n)}\to1.
}
\tag{11}
\]
Because every fixed-notch form satisfies `0<=phi_eta<=J_0`, the same argument gives
\[
E_\eta(P_n)=o(L_n),
\qquad
|E_\eta(W_n)-E_\eta(U_n)|=o(L_n),
\tag{12}
\]
and hence
\[
\boxed{
h_\eta(U_n)-h_\eta(W_n)\to0.}
\tag{13}
\]
So the `M_n->0` branch is completely removable.

Now suppose instead that for fixed `0<lambda<=Lambda<infinity`,
\[
lambda\le M_n\le\Lambda.
\tag{14}
\]
Assume the packet is fixed-notch invisible,
\[
E_\eta(P_n)=o(L_n).
\tag{15}
\]
If
\[
X_n=\frac{\Delta(U_n)}{L_n}\to0,
\tag{16}
\]
then (4) and the definition of `X_n` give
\[
\frac{E_0(U_n)}{L(U_n)}\to1.
\tag{17}
\]
Moreover `E_eta(U_n)<=E_0(U_n)=O(L_n)`, so Cauchy--Schwarz in the notch form yields
\[
\begin{aligned}
|E_\eta(W_n)-E_\eta(U_n)|
&\le E_\eta(P_n)
+2\sqrt{E_\eta(P_n)E_\eta(U_n)}\\
&=o(L_n).
\end{aligned}
\tag{18}
\]
Therefore
\[
\boxed{
X_n\to0
\quad\Longrightarrow\quad
\frac{E_0(U_n)}{L(U_n)}\to1,
\qquad
h_\eta(U_n)-h_\eta(W_n)\to0.
}
\tag{19}
\]
This is stronger than componentwise source polarization. A bounded source-heavy packet whose notch mass is negligible is **globally excisable at minimal polarization**: the complement is itself a physical Montgomery--Taylor near-extremizer carrying the same asymptotic fixed-notch exposure.

Consequently, if such a packet is genuinely indispensable to a fatal sequence, one must pass to a subsequence on which
\[
\boxed{X_n\ge\varepsilon>0.}
\tag{20}
\]
The external remainder then has a macroscopic source excess, and (7) says that the packet is overpolarized by exactly that excess.

## 3. Spectral localization transfers the full overpolarization into the same window

Assume now that there are measurable symmetric sets `B_n subset [-1,1]` such that
\[
\boxed{
E_{B_n^c}(P_n)=o(E_0(P_n)).
}
\tag{21}
\]
In the bounded source-heavy regime (14), this is `o(L_n)`. Equation (9) and Cauchy--Schwarz imply
\[
|\mathcal C_{B_n^c}(P_n,U_n)|
\le
\sqrt{E_{B_n^c}(P_n)E_0(U_n)}
=o(L_n).
\tag{22}
\]
Combining (7) and (22),
\[
\boxed{
\frac{2\mathcal C_{B_n}(P_n,U_n)}{L_n}
=-(M_n+X_n)+o(1).
}
\tag{23}
\]
Also
\[
E_{B_n}(P_n)=M_nL_n+o(L_n).
\tag{24}
\]
A second Cauchy--Schwarz inequality therefore gives the quantitative companion floor
\[
\boxed{
\frac{E_{B_n}(U_n)}{L_n}
\ge
\frac{(M_n+X_n)^2}{4M_n}+o(1).
}
\tag{25}
\]
Equivalently,
\[
\boxed{
\frac{E_{B_n}(U_n)}{L_n}
\ge
\frac{M_n}{4}
+\frac{X_n}{2}
+\frac{X_n^2}{4M_n}
+o(1).
}
\tag{26}
\]
The first term is the companion mass forced by the packet's own floor cancellation. Every unit of complement excess contributes at least another half unit of source energy in the **same** spectral window, plus the positive quadratic correction. Thus an essential bounded-mass packet cannot hide its extra cancellation in an unrelated part of the spectrum.

There is no assumption that `B_n` is an endpoint band, an interval, or a region on which `J_0` is monotone. The transfer is pure Hilbert geometry plus the affine Montgomery--Taylor floor. In particular it applies to the interior shrinking saddle windows produced by `ANF-118`, where the endpoint anti-concentration machinery of `ANF-108` is irrelevant.

The large-packet regime is even more rigid. Suppose
\[
M_n\to\infty
\tag{27}
\]
and retain the relative localization (21). Since
\[
S_{W_n}=S_{P_n}+S_{U_n},
\qquad
E_0(W_n)=L_n+o(L_n),
\]
we have
\[
\frac{\|S_{W_n}\|_0^2}{E_0(P_n)}
=\frac{1+o(1)}{M_n}\to0.
\tag{28}
\]
The reverse triangle inequality gives
\[
\left|
\sqrt{\frac{E_0(U_n)}{E_0(P_n)}}-1
\right|
\le
\sqrt{\frac{E_0(W_n)}{E_0(P_n)}}\to0,
\]
so
\[
\boxed{
\frac{E_0(U_n)}{E_0(P_n)}\to1,
\qquad
\frac{\Delta(U_n)}{E_0(P_n)}\to1,
\qquad
\frac{\mathcal C_0(P_n,U_n)}{E_0(P_n)}\to-1.
}
\tag{29}
\]
The localized profile itself mirrors. Restricting (28) to `B_n`,
\[
\boxed{
\frac{
\|\mathbf1_{B_n}(S_{P_n}+S_{U_n})\|_0^2
}{E_0(P_n)}
\to0.
}
\tag{30}
\]
Together with (21), this implies
\[
\boxed{
\frac{E_{B_n}(U_n)}{E_0(P_n)}\to1,
\qquad
\frac{
\|\mathbf1_{B_n}(S_{U_n}+S_{P_n})\|_0
}{\|\mathbf1_{B_n}S_{P_n}\|_0}
\to0.
}
\tag{31}
\]
Thus source blowup does not create an uncontrolled completion branch. It forces the external remainder to become an asymptotically exact **negative copy of the packet's complete localized source profile**. This is stronger than the order-one companion estimate (25).

## 4. ANF-118 clouds satisfy the hypotheses on an explicit shrinking off-notch saddle band

Fix `gamma>0` and use the exact `ANF-115` packet `P_A`, with
\[
a=a_\gamma
=\frac2\pi\arctan\frac1{\pi\gamma},
\qquad
E_A=E_0(P_A).
\]
Let
\[
T_A=\bigsqcup_jw_{j,A}(P_A+\tau_{j,A}),
\qquad
V_A=\sum_jw_{j,A},
\]
be an `ANF-118` translation cloud satisfying
\[
\log(e+V_A)=o(A^{1/3}).
\tag{32}
\]
Write `mathcal G_A` for its Gaussian Gram form and
\[
Z_A=\frac{E_0(T_A)}{E_A}.
\]
Then `ANF-118` gives
\[
Z_A=(1+o(1))\mathcal G_A+o(1).
\tag{33}
\]

Consider any physical global completion
\[
W_A=T_A\sqcup R_A
\tag{34}
\]
which is Montgomery--Taylor near-extremal, and suppose the natural packet and ambient scales are comparable:
\[
0<r_-\le\frac{E_A}{L(W_A)}\le r_+<\infty.
\tag{35}
\]
The cloud is automatically sublinear in the ambient affine scale. Indeed `ANF-115` gives
\[
\frac1A\log\frac{E_A}{|P_A|^2}\to f_\gamma>0,
\qquad
|P_A|=\exp(\gamma A\log2+o(A)),
\]
so (32) and (35) imply
\[
\frac{|T_A|}{L(W_A)}
=\frac{V_A|P_A|}{L(W_A)}\to0.
\tag{36}
\]
All points of `T_A` have nonzero imaginary part, so in this application the affine split defect is actually zero exactly.

Choose a widening mesoscopic radius `s_A` with
\[
\log(e+V_A)=o(s_A^2),
\qquad
s_A^2=o(A^{1/3}),
\tag{37}
\]
and define the symmetric saddle band
\[
\boxed{
B_A:=
\left\{
\alpha\in[-1,1]:
\bigl||\alpha|-a\bigr|\le\frac{s_A}{\sqrt A}
\right\}.
}
\tag{38}
\]
The uniform tail estimate in `ANF-118`, together with `|p_A|<=V_A`, gives
\[
\frac{E_{B_A^c}(T_A)}{E_A}
\le
CV_A^2e^{-c_*s_A^2}=o(1).
\tag{39}
\]
By (35),
\[
E_{B_A^c}(T_A)=o(L(W_A)).
\tag{40}
\]
For every fixed `0<eta<a`, equation (22) of `ANF-118` also gives
\[
\boxed{E_\eta(T_A)=o(L(W_A)).}
\tag{41}
\]
Because `s_A/sqrt(A)->0`, the saddle band (38) is eventually disjoint from the fixed central notch:
\[
B_A\cap[-\eta,\eta]=\varnothing.
\tag{42}
\]

Equations (33), (35), and (39)--(42) put every admitted same-saddle cloud directly into the abstract completion trichotomy. After passing to a subsequence if necessary:

- if `(E_A/L(W_A)) mathcal G_A ->0`, then `M_A->0` and the cloud is globally excisable;
- if `M_A` stays in a compact subinterval of `(0,infinity)`, then either `Delta(R_A)/L(W_A)->0` and the cloud is again globally excisable with no change in fixed-notch exposure, or the remainder is overpolarized and (25) forces order-one source energy into the same shrinking off-notch saddle band;
- if `(E_A/L(W_A)) mathcal G_A ->infinity`, then (29)--(31) force `R_A` to mirror the complete saddle profile of `T_A` with opposite phase.

The second branch is the one left genuinely open by `ANF-118`. The crucial refinement is that **mere macroscopic cancellation is not enough** to make an order-one saddle cloud essential. If the external cancellation occurs at the minimal floor-required strength, deleting the entire cloud exposes another near-extremizer with the same notch observable. Essentiality requires strict overpolarization, and that overpolarization itself has to be carried in the same `A^(-1/2)`-scale off-notch spectral region.

## 5. Adversarial checks, prior-art boundary, and next gate

The theorem is deliberately quotient- and scale-aware. The sublinear hypothesis is used only to make `L(P_n)` and the affine split error negligible relative to the ambient scale. In the concrete `ANF-118` application it is automatic and the affine split error vanishes exactly. The finite-mass companion formula requires `M_n` bounded above and below; the separate profile-mirroring argument handles `M_n->infinity`, while `M_n->0` is directly excisable. Hence no source-mass subsequence is omitted.

The fixed-notch excision statement requires the packet notch mass to be `o(L_n)`. This is automatic for `ANF-118` only for fixed `eta<a_gamma`; it is not uniform as the notch edge approaches the saddle. Mixed packet shapes, different `gamma` values, moving saddles, and exponential cloud weights outside the `ANF-118` envelope remain outside scope. The theorem also does not say that the same-window companion is a translated copy of the original physical packet; only its source profile in the Montgomery--Taylor Hilbert space is constrained. In the diverging-mass branch that Hilbert profile is asymptotically mirrored, but physical realization of the mirror can still be highly nonunique.

A targeted prior-art check against Hilbert-space/profile-decomposition and concentration-compactness literature found the familiar opposite paradigm: bounded sequences are decomposed into asymptotically decoupled profiles with Pythagorean-type norm splitting. Those general results are useful context but do not supply (7), whose sign and exact overpolarization term come from the independent Montgomery--Taylor affine floors for physical subconfigurations. No external theorem is load-bearing here, so `SOURCES.md` does not need a new dependency. The claim is a Mathia-specific completion reduction, not a claim that Hilbert polarization or profile decomposition is new.

The next gate is now narrower than the one after `ANF-118`. In the order-one branch, a fatal completion must simultaneously realize: (i) strict complement excess `X_n>0`; (ii) the forced shrinking-band companion (25) at `|alpha|=a_gamma`; and (iii) enough **separate central-notch exposure** to reach the `ANF-099` envelope, because the entire compulsory cancellation band is asymptotically disjoint from the notch. A decisive next step would either prove that these two spectral roles cannot coexist in one physical near-extremal remainder, or construct a genuine global completion that does both while keeping the affine denominator unchanged. In the large-Gram branch the target is even more rigid: test whether an actual physical remainder can realize the required negative mesoscopic mirror without itself generating a removable packet pair.