# ANF-112 — endpoint-localized sublinear packets are either excisable or force new disjoint height mass

**Status:** `EXACT-DERIVED + PACKET-EXCISION-DICHOTOMY + UNBOUNDED-SOURCE-TRANSFER + ENDPOINT-POLARIZATION + RECYCLING-OBSTRUCTION-REMOVAL + LEADING-CRITICAL-CASCADE-RESTART + SUPERCRITICAL-CHAMBER-NARROWING`. `ANF-111` shows why a naive layer-by-layer cascade can recycle its negative polarization through previously extracted tails. The packet repair of the first version of this finding was correct, but its audit claimed that the auxiliary bound `E_0(P_n)=O(L_n)` was load-bearing. It is not. Normalizing by the packet's own source mass shows that **every** source-heavy endpoint-localized sublinear packet, even one with `E_0(P_n)/L_n -> infinity`, forces endpoint energy of comparable scale into the unused remainder and hence a new disjoint source-heavy height layer.

This removes a second apparent escape mechanism from the packet argument: source-norm blowup does not defeat endpoint transfer. Combined with the universal sparse endpoint estimate of `ANF-103`, it also extends the recursive chamber beyond the bounded matched-critical window. A sub-square-root source-heavy packet with

\[
\frac{4\pi H_n}{\log R_n}\to1,
\qquad
R_n:=\frac{L_n}{|P_n|^2}\to\infty,
\]

is automatically localized in a shrinking endpoint band, even if its additive excess above `log R_n+2 log log R_n` diverges. Therefore such a packet still forces fresh height mass. A sparse supercritical branch can terminate this mechanism only after reaching **multiplicative** supercriticality, `4 pi H_n >= (1+c) log R_n` along a subsequence, or by leaving the sub-square-root regime.

## 1. Packet setup and affine bookkeeping

Retain the fixed-notch notation

\[
J_0=J_{\rm MT},\qquad
E_0(X)=\int_{-1}^{1}J_0(\alpha)|S_X(\alpha)|^2\,d\alpha,
\]

\[
E_\eta(X)=\int \phi_\eta(\alpha)|S_X(\alpha)|^2\,d\alpha,
\qquad 0\le\phi_\eta\le J_0,
\]

and

\[
L(X)=2|X|-\sigma(X),
\qquad
h_\eta(X)=\frac{E_\eta(X)}{L(X)}.
\]

Let `W_n` be a physical Montgomery--Taylor near-extremizing sequence,

\[
L_n:=L(W_n)\to\infty,
\qquad
E_0(W_n)=L_n+o(L_n),
\tag{1}
\]

and split it into conjugation-invariant pieces

\[
W_n=P_n\sqcup U_n.
\tag{2}
\]

Assume only

\[
|P_n|=o(L_n).
\tag{3}
\]

There is **no upper bound** on `E_0(P_n)`. With

\[
\kappa_n:=\sigma(P_n)+\sigma(U_n)-\sigma(W_n),
\]

`ANF-111` gives

\[
0\le\kappa_n\le2|P_n|=o(L_n),
\qquad
L(U_n)=L_n-L(P_n)-\kappa_n=L_n-o(L_n).
\tag{4}
\]

Assume that the aggregate packet is localized in a shrinking Montgomery--Taylor endpoint layer: there are `delta_n downarrow 0` such that

\[
E_{\rm in,\delta_n}(P_n)
:=\int_{|\alpha|\le1-\delta_n}
J_0(\alpha)|S_{P_n}(\alpha)|^2\,d\alpha
=o(L_n).
\tag{5}
\]

This is an **absolute** `o(L_n)` condition, not merely a small fraction of the packet norm. It is the only localization hypothesis in the abstract packet theorem.

## 2. Source-negligible packets are still removable

If

\[
E_0(P_n)=o(L_n),
\tag{6}
\]

then `S_{U_n}=S_{W_n}-S_{P_n}` and Hilbert geometry give

\[
|E_0(U_n)-E_0(W_n)|
\le
2\sqrt{E_0(W_n)E_0(P_n)}+E_0(P_n)
=o(L_n).
\]

Together with (1) and (4),

\[
\boxed{\frac{E_0(U_n)}{L(U_n)}\to1.}
\tag{7}
\]

Since multiplication by `sqrt(phi_eta/J_0)` is a contraction in the source Hilbert norm, the same estimate gives

\[
|E_\eta(U_n)-E_\eta(W_n)|=o(L_n),
\qquad
\boxed{h_\eta(U_n)-h_\eta(W_n)\to0.}
\tag{8}
\]

Thus complete internal recycling has the benign outcome already identified in the first version: if the old packet cancels to source-negligibility, delete it as a whole. The residual configuration remains a physical near-extremizer with the same asymptotic fixed-notch exposure.

## 3. A source-heavy packet polarizes at its own source scale

Pass now to a subsequence on which the packet is source-heavy. Write

\[
M_n:=\frac{E_0(P_n)}{L_n},
\qquad
M_n\ge\lambda>0.
\tag{9}
\]

No boundedness of `M_n` is assumed. Let

\[
\mathcal C_0(P_n,U_n)
:=\operatorname{Re}\int J_0S_{P_n}\overline{S_{U_n}}.
\]

The arbitrary-split identity of `ANF-111` is

\[
\Delta(W_n)
=
\Delta(P_n)+\Delta(U_n)
+2\mathcal C_0(P_n,U_n)-\kappa_n,
\tag{10}
\]

where `Delta(X)=E_0(X)-L(X)>=0`. By (1), `Delta(W_n)=o(L_n)`; by (3)--(4), `L(P_n)=o(L_n)` and `kappa_n=o(L_n)`; and `Delta(U_n)>=0`. Hence

\[
2\mathcal C_0(P_n,U_n)
\le
-E_0(P_n)+o(L_n),
\]

so, uniformly for `M_n>=lambda`,

\[
\boxed{
\mathcal C_0(P_n,U_n)
\le
-\left(\frac12-o(1)\right)M_nL_n.
}
\tag{11}
\]

The global near-extremizer has only source norm `asymp sqrt(L_n)`, so the remainder cannot have an unrelated arbitrarily larger norm. The triangle inequality gives

\[
\sqrt{E_0(U_n)}
\le
\sqrt{E_0(W_n)}+\sqrt{E_0(P_n)},
\]

and therefore

\[
\boxed{
E_0(U_n)
\le
L_n\bigl(\sqrt{M_n}+1+o(1)\bigr)^2.
}
\tag{12}
\]

For bounded `M_n` this recovers the `O(L_n)` estimate used previously. For `M_n->infinity`, (11)--(12) express a stronger rigidity: packet and remainder must carry source norms of the same large order and cancel macroscopically.

## 4. Endpoint localization transfers that polarization without any source upper bound

Split the cross term into the interior and endpoint bands. Put

\[
\varepsilon_n:=\frac{E_{\rm in,\delta_n}(P_n)}{L_n}\to0.
\]

By Cauchy--Schwarz and (12), the interior interaction satisfies

\[
|\mathcal C_{\rm in,n}|
\le
\sqrt{E_{\rm in,\delta_n}(P_n)E_0(U_n)}
\le
L_n\sqrt{\varepsilon_n}
\bigl(\sqrt{M_n}+1+o(1)\bigr).
\tag{13}
\]

Because `M_n>=lambda`,

\[
\frac{|\mathcal C_{\rm in,n}|}{M_nL_n}
\le
\sqrt{\varepsilon_n}
\left(\frac1{\sqrt\lambda}+\frac{2}{\lambda}\right)
=o(1).
\tag{14}
\]

Thus the negative interaction in (11) cannot disappear into the interior even when `M_n` diverges. If

\[
E_{\rm edge,\delta}(X)
:=\int_{1-\delta\le|\alpha|\le1}
J_0(\alpha)|S_X(\alpha)|^2\,d\alpha,
\]

then

\[
\mathcal C_{\rm edge,n}
\le
-\left(\frac12-o(1)\right)M_nL_n.
\tag{15}
\]

Endpoint Cauchy--Schwarz and `E_edge(P_n)<=E_0(P_n)=M_nL_n` therefore give

\[
\boxed{
E_{\rm edge,\delta_n}(U_n)
\ge
\left(\frac14-o(1)\right)M_nL_n.
}
\tag{16}
\]

This corrects the earlier audit of this finding. The crude estimate `L_n^2/E_0(P_n)` loses the packet scale because it inserts only a fixed `Omega(L_n)` lower bound for the cross term. The affine floor actually supplies the stronger `Omega(E_0(P_n))` polarization in (11); after normalizing consistently by `M_n`, the apparent loss vanishes.

## 5. Fresh high mass is forced at the same packet scale

The endpoint anti-concentration estimate of `ANF-108` says that every physical configuration `X` of height at most `H` satisfies

\[
E_{\rm edge,\delta}(X)
\le
C_*(1+H)e^{4\pi H}\delta E_0(X).
\tag{17}
\]

Fix `0<theta<1` and define

\[
h_n:=\frac{1-\theta}{4\pi}\log\frac1{\delta_n}.
\tag{18}
\]

Split the unused remainder by height,

\[
U_n=Q_n\sqcup V_n,
\qquad
Q_n:=\{u\in U_n:|\operatorname{Im}u|\le h_n\},
\]

\[
V_n:=\{u\in U_n:|\operatorname{Im}u|>h_n\}.
\tag{19}
\]

Set

\[
a_n:=C_*(1+h_n)\delta_n^\theta\to0.
\tag{20}
\]

Equation (17) gives `E_edge(Q_n)<=a_nE_0(Q_n)`. Normalize all norms by `sqrt(M_nL_n)` and put

\[
x_n:=\sqrt{\frac{E_0(V_n)}{M_nL_n}},
\qquad
q_n:=\sqrt{\frac{E_0(Q_n)}{M_nL_n}}.
\]

From (12) and `M_n>=lambda`, there is a constant `Z_lambda` such that

\[
\sqrt{\frac{E_0(U_n)}{M_nL_n}}\le Z_\lambda,
\qquad
q_n\le Z_\lambda+x_n.
\tag{21}
\]

On the other hand, (16), endpoint triangle inequality, and (20) imply for all sufficiently large `n`

\[
\frac13
\le
\sqrt{a_n}\,q_n+x_n
\le
\sqrt{a_n}(Z_\lambda+x_n)+x_n,
\tag{22}
\]

after harmlessly weakening the asymptotic constant in (16). Since `a_n->0`, (22) forces `x_n` to stay bounded away from zero. Consequently there is `c_{lambda,theta}>0` such that

\[
\boxed{
E_0(V_n)
\ge
c_{\lambda,\theta}M_nL_n
\ge
c_{\lambda,\theta}\lambda L_n
}
\tag{23}
\]

for all sufficiently large `n` on the source-heavy subsequence, and every point of `V_n` satisfies

\[
\boxed{
|\operatorname{Im}v|
>
\frac{1-\theta}{4\pi}\log\frac1{\delta_n}.
}
\tag{24}
\]

Thus endpoint pressure not only survives unbounded packet source mass: **source blowup propagates to genuinely new unused height mass at comparable scale**. The new layer is disjoint from the packet by construction.

## 6. Finite packet recycling no longer needs controlled aggregate source norm

Suppose finitely many already extracted conjugation-invariant layers have been combined into `P_n`, with total cardinality `o(L_n)`, and suppose their aggregate satisfies (5). Pairwise interactions inside the packet are unrestricted. Then there are only two asymptotic outcomes.

If `E_0(P_n)=o(L_n)`, Sections 1--2 excise the entire packet while preserving near-extremality and fixed-notch exposure. Otherwise pass to a source-heavy subsequence. Sections 3--5 force a new disjoint layer in the unused remainder. This remains true whether `E_0(P_n)=O(L_n)` or `E_0(P_n)/L_n->infinity`.

Accordingly the `E_0(P_n)=O(L_n)` hypothesis in the previous version was not a genuine state variable of the cascade. The only packet-level analytic input needed by the source-heavy branch is **absolute endpoint localization** (5). At a finite stage, internal recycling can make the packet removable, but it cannot hide a non-negligible endpoint-localized packet from the unused remainder by making its source norm large.

## 7. Leading-critical sparse packets are automatically endpoint-localized

The remaining question is when (5) follows from geometry rather than being assumed. Let

\[
m_n:=|P_n|,
\qquad
R_n:=\frac{L_n}{m_n^2}\to\infty,
\qquad
H_n:=\max_{p\in P_n}|\operatorname{Im}p|,
\]

so `m_n=o(sqrt(L_n))`. Assume the packet is source-heavy as in (9), and write

\[
A_n:=4\pi H_n.
\]

`ANF-103` gives the universal lower threshold

\[
A_n
\ge
\log R_n+2\log\log R_n+O(1).
\tag{25}
\]

Now impose only the leading-scale upper condition

\[
\boxed{
\frac{A_n}{\log R_n}\to1.
}
\tag{26}
\]

This is much weaker than a bounded matched-critical window: the additive excess above `log R_n+2 log log R_n` may tend to `+infinity`, provided it is `o(log R_n)`.

Define

\[
d_n:=1+(A_n-\log R_n)_+,
\qquad
\delta_n:=8\frac{d_n}{\log R_n}.
\tag{27}
\]

By (25), `d_n->infinity`; by (26), `d_n=o(log R_n)`. Hence `delta_n->0`. For large `n`, (25) also gives `A_n>=(1/2)log R_n`, so

\[
\delta_nA_n\ge4d_n.
\tag{28}
\]

Using the endpoint bound from `ANF-103`, `J_0(alpha)<=G^2(1-|alpha|)`, and the trivial pointwise estimate `|S_{P_n}(alpha)|<=m_ne^{2 pi |alpha|H_n}`, one obtains

\[
\frac{E_{\rm in,\delta_n}(P_n)}{L_n}
\ll
\frac1{R_n}
\exp\bigl(A_n(1-\delta_n)\bigr).
\tag{29}
\]

Since `A_n-log R_n<=d_n`, equations (28)--(29) yield

\[
\frac{E_{\rm in,\delta_n}(P_n)}{L_n}
\ll
\exp(d_n-4d_n)
=
\exp(-3d_n)
\longrightarrow0.
\tag{30}
\]

Thus (5) is automatic. Applying Sections 3--5 gives a fresh disjoint source-heavy layer above

\[
\boxed{
h_n
=
\frac{1-\theta}{4\pi}
\log\frac{\log R_n}{8d_n}
\longrightarrow\infty.}
\tag{31}
\]

When `A_n=log R_n+2 log log R_n+O(1)`, this recovers the previous log--log cascade scale up to the harmless `log log log R_n` correction caused by choosing a robust common endpoint width. More importantly, (31) continues to diverge throughout the entire additive `o(log R_n)` supercritical chamber.

## 8. Frontier consequence and adversarial boundary

The packet frontier is therefore stricter than in the previous version. At any finite endpoint-localized sublinear stage, **unbounded aggregate source norm is not an escape**. For a sub-square-root source-heavy packet, even an unbounded additive height excess is not an escape while `4 pi H_n/log R_n -> 1`: the packet still endpoint-localizes and forces fresh unused height mass. If a sparse branch is to stop this mechanism because of height rather than population, then after passage to a subsequence it must enter a genuinely multiplicative chamber,

\[
\boxed{
4\pi H_n\ge(1+c)\log R_n
}
\tag{32}
\]

for some fixed `c>0`. The other major escape remains the population transition `m_n not=o(sqrt(L_n))`, where `R_n` no longer diverges and the endpoint argument of `ANF-103` does not force a shrinking band.

Several limitations remain explicit. The theorem does not say that the newly extracted `V_n` is itself near-extremal, sub-square-root, leading-critical, or notch-visible. Those are the next classification tests before another recursive step. Condition (5) is genuinely necessary for the abstract packet transfer: without absolute endpoint localization, the negative interaction may live in the interior and no height conclusion follows. The leading-critical corollary uses only `m_n=o(sqrt(L_n))`, source-heaviness, and the max-height condition (26); it does not address a multiplicatively supercritical sparse packet, nor a diffuse superlinear bulk.

The `M_n->infinity` stress test is now built into the proof rather than excluded. Equation (12) controls the remainder on the packet scale, (14) makes the interior cross term `o(M_nL_n)`, and (16) transfers `Omega(M_nL_n)` endpoint energy. Conversely, for bounded `M_n`, the argument reduces to the earlier `O(L_n)` packet proof. No sign assumption on pairwise old-layer interactions, no horizontal gap, no fiber-completeness, and no hidden positivity of the spatial transform is used.

A targeted prior-art check against concentration--compactness/profile-decomposition language and sparse Fourier concentration/extrapolation did not locate a theorem supplying this Montgomery--Taylor affine-floor transfer or the leading-critical packet criterion (26)--(31). No external theorem is load-bearing: the proof uses the canonical Montgomery--Taylor floor, the explicit endpoint zero already established in `ANF-103`, and the endpoint anti-concentration inequality of `ANF-108`. `SOURCES.md` therefore requires no update.

The fixed-notch objective remains open. What has changed is the shape of the escape set: pairwise recycling, aggregate source blowup, and additive sublogarithmic supercriticality are no longer independent obstructions. A surviving sparse obstruction must eventually pay either square-root population or a multiplicative vertical excess, while diffuse superlinear bulk remains a separate chamber. This is the narrower packet-level compactness/height-cascade dichotomy needed to continue attacking the envelope `beta_eta` of `ANF-099`.