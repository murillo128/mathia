# ANF-112 — endpoint-localized sparse packets are either excisable or force new disjoint height mass

**Status:** `EXACT-DERIVED + PACKET-EXCISION-DICHOTOMY + ENDPOINT-POLARIZATION + RECYCLING-OBSTRUCTION-REMOVAL + CONDITIONAL-CASCADE-RESTART`. `ANF-111` corrects the naive recursive sparse-layer cascade: after extracting a secondary source-heavy layer `V`, the complement still contains the original tail `B`, so the negative polarization of `V` against that complement may be absorbed entirely by `B`. The proposed repair there was a pairwise non-recycling estimate such as `C_0(V,B)=o(L)`. That estimate is stronger than necessary. The correct object is the **aggregate packet** of all already extracted endpoint-localized sparse pieces.

If such a packet has negligible Montgomery--Taylor source norm, it can be deleted as a whole without changing near-extremality or fixed-notch exposure. If it retains macroscopic source norm, the global Montgomery--Taylor floor forces the packet to polarize negatively against the unused remainder; because the packet is already localized in a shrinking endpoint band, that negative interaction forces macroscopic endpoint energy into the unused remainder and hence a genuinely new, disjoint source-heavy height layer. Thus internal recycling among old layers has only two outcomes: it either makes the old packet removable, or it cannot prevent pressure from reaching unused mass.

The result is a packet-level replacement for the pairwise gate in `ANF-111`. It does **not** prove an infinite cascade automatically: to append each newly extracted layer to the packet and repeat, one still needs that layer to enter a sparse matched-critical regime giving endpoint localization and controlled source mass, or else one has reached the square-root/bulk or supercritical-height alternatives already identified in `ANF-109`--`ANF-111`.

## 1. Packet setup and affine bookkeeping

Retain the fixed-notch notation

\[
J_0=J_{\rm MT},\qquad
E_0(X)=\int J_0(\alpha)|S_X(\alpha)|^2\,d\alpha,
\]

\[
E_{\eta}(X)=\int \phi_\eta(\alpha)|S_X(\alpha)|^2\,d\alpha,
\qquad
0\le\phi_\eta\le J_0,
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

Think of `P_n` as the union of all sparse layers already extracted and `U_n` as the as-yet unused remainder. Assume

\[
|P_n|=o(L_n),
\qquad
E_0(P_n)=O(L_n).
\tag{3}
\]

No fiber-completeness assumption is needed. Let

\[
\kappa_n
:=\sigma(P_n)+\sigma(U_n)-\sigma(W_n).
\]

The affine defect identity of `ANF-111` gives

\[
0\le\kappa_n\le2|P_n|=o(L_n),
\tag{4}
\]

and therefore

\[
L(U_n)=L_n-L(P_n)-\kappa_n
=L_n-o(L_n).
\tag{5}
\]

Assume in addition that the packet is concentrated in a shrinking Montgomery--Taylor endpoint layer. Thus there are `delta_n downarrow 0` for which

\[
E_{\rm in,\delta_n}(P_n)
:=
\int_{|\alpha|\le1-\delta_n}
J_0(\alpha)|S_{P_n}(\alpha)|^2\,d\alpha
=o(L_n).
\tag{6}
\]

This is the only localization input. It concerns the aggregate packet norm on the interior band and makes no assertion about pairwise interactions among the pieces inside `P_n`.

## 2. If the packet cancels itself to source-negligibility, delete it

Suppose first that

\[
E_0(P_n)=o(L_n).
\tag{7}
\]

Because `S_{U_n}=S_{W_n}-S_{P_n}`, Hilbert geometry gives

\[
\bigl|E_0(U_n)-E_0(W_n)\bigr|
\le
2\sqrt{E_0(W_n)E_0(P_n)}+E_0(P_n)
=o(L_n).
\tag{8}
\]

Together with (1) and (5),

\[
\boxed{
\frac{E_0(U_n)}{L(U_n)}\to1.
}
\tag{9}
\]

So the unused remainder is itself a physical near-extremizer. The fixed-notch observable is equally stable. Since `phi_eta<=J_0`,

\[
E_\eta(P_n)\le E_0(P_n)=o(L_n),
\qquad
E_\eta(W_n)\le E_0(W_n)=O(L_n).
\]

Hence

\[
|E_\eta(U_n)-E_\eta(W_n)|
\le
2\sqrt{E_\eta(W_n)E_\eta(P_n)}+E_\eta(P_n)
=o(L_n),
\tag{10}
\]

and (5) yields

\[
\boxed{
h_\eta(U_n)-h_\eta(W_n)\to0.}
\tag{11}
\]

Thus arbitrarily strong cancellation among individually source-heavy old layers is not an obstruction. If their **sum** becomes source-negligible, the whole recycled packet can be excised and the decisive `ANF-099` exposure is unchanged. This is the packet analogue of `ANF-103`, but it allows arbitrary internal splitting of real multiplicities because the resulting affine error is only `o(L_n)` by (4).

## 3. A source-heavy endpoint packet must polarize against the unused remainder

Now pass to a subsequence on which the opposite alternative holds: for some fixed `lambda>0`,

\[
E_0(P_n)\ge\lambda L_n.
\tag{12}
\]

Write

\[
\mathcal C_0(P_n,U_n)
:=
\operatorname{Re}\int J_0
S_{P_n}\overline{S_{U_n}}.
\]

The exact arbitrary-split identity from `ANF-111` is

\[
\Delta(W_n)
=
\Delta(P_n)+\Delta(U_n)
+2\mathcal C_0(P_n,U_n)-\kappa_n,
\tag{13}
\]

where `Delta(X)=E_0(X)-L(X)>=0`. By (1), `Delta(W_n)=o(L_n)`. By (3)--(4), `L(P_n)=o(L_n)` and `kappa_n=o(L_n)`, while (12) gives

\[
\Delta(P_n)\ge\lambda L_n-o(L_n).
\]

Since `Delta(U_n)>=0`, (13) forces

\[
\boxed{
\mathcal C_0(P_n,U_n)
\le
-\frac\lambda2L_n+o(L_n).
}
\tag{14}
\]

This is the key point: once the **aggregate** old packet retains macroscopic source mass, it must cancel macroscopically against the unused remainder regardless of how much cancellation occurs inside the packet.

The remainder also has controlled source mass. From (1), (3), and the triangle inequality,

\[
\sqrt{E_0(U_n)}
\le
\sqrt{E_0(W_n)}+\sqrt{E_0(P_n)},
\]

so

\[
E_0(U_n)=O(L_n).
\tag{15}
\]

## 4. Endpoint localization transfers the forced polarization to unused mass

Decompose the source inner product into the interior band and the shrinking endpoint layer. By Cauchy--Schwarz, (6), and (15),

\[
\left|
\operatorname{Re}
\int_{|\alpha|\le1-\delta_n}
J_0S_{P_n}\overline{S_{U_n}}
\right|
\le
\sqrt{E_{\rm in,\delta_n}(P_n)E_0(U_n)}
=o(L_n).
\tag{16}
\]

Therefore (14) must be realized in the endpoint layer. If

\[
E_{\rm edge,\delta}(X)
:=
\int_{1-\delta\le|\alpha|\le1}
J_0(\alpha)|S_X(\alpha)|^2\,d\alpha,
\]

then

\[
\operatorname{Re}
\int_{1-\delta_n\le|\alpha|\le1}
J_0S_{P_n}\overline{S_{U_n}}
\le
-\frac\lambda2L_n+o(L_n).
\tag{17}
\]

Since `E_edge,delta_n(P_n)<=E_0(P_n)=O(L_n)`, endpoint Cauchy--Schwarz gives a constant `c_lambda>0` such that

\[
\boxed{
E_{\rm edge,\delta_n}(U_n)
\ge c_\lambda L_n
}
\tag{18}
\]

for all sufficiently large `n` on this subsequence. Thus a source-heavy old packet cannot absorb its own polarization forever: after aggregate packetization, the global floor forces a macroscopic endpoint signal into points that were not in the packet.

Notice what was *not* used. There is no estimate of `C_0(B,V)`, no sign assumption on any pair of old layers, no horizontal gap, and no claim that the old components are separately near-extremal. The entire internal interaction graph has disappeared into the single vector `S_{P_n}`.

## 5. Endpoint pressure forces a genuinely new disjoint high layer

The endpoint anti-concentration inequality of `ANF-108` says that any physical configuration `X` of height at most `H` obeys

\[
E_{\rm edge,\delta}(X)
\le
C_*(1+H)e^{4\pi H}\delta E_0(X).
\tag{19}
\]

Fix `0<theta<1` and set

\[
h_n
:=
\frac{1-\theta}{4\pi}
\log\frac1{\delta_n}.
\tag{20}
\]

Split the unused remainder by height,

\[
U_n=Q_n\sqcup V_n,
\qquad
Q_n:=\{u\in U_n:|\operatorname{Im}u|\le h_n\},
\]

\[
V_n:=\{u\in U_n:|\operatorname{Im}u|>h_n\}.
\tag{21}
\]

The layer `V_n` is automatically disjoint from every previously extracted component because `V_n subset U_n`.

The same two-case argument as in `ANF-109` now applies with no reference to a particular original tail. From (15), choose `C_U` with `E_0(U_n)<=C_UL_n` eventually and fix `M>4C_U`. If `E_0(Q_n)>ML_n`, reverse triangle inequality gives

\[
E_0(V_n)
\ge
\bigl(\sqrt M-\sqrt{C_U}\bigr)^2L_n.
\tag{22}
\]

Otherwise `E_0(Q_n)<=ML_n`, and (19)--(20) imply

\[
\frac{E_{\rm edge,\delta_n}(Q_n)}{L_n}
\ll
(1+h_n)e^{4\pi h_n}\delta_n
=
(1+h_n)\delta_n^\theta
\longrightarrow0.
\tag{23}
\]

Combining (18), (23), and the reverse triangle inequality in the endpoint seminorm gives

\[
E_0(V_n)
\ge E_{\rm edge,\delta_n}(V_n)
\ge c_{\lambda,\theta}L_n.
\tag{24}
\]

The two cases therefore prove

\[
\boxed{
\liminf_n\frac{E_0(V_n)}{L_n}>0,
\qquad
|\operatorname{Im}v|>
\frac{1-\theta}{4\pi}\log\frac1{\delta_n}
\quad(v\in V_n).
}
\tag{25}
\]

So any source-heavy endpoint-localized old packet forces a **new source-heavy layer in the unused remainder**, at the natural height scale `log(1/delta_n)`.

## 6. Application to the ANF-111 recycling obstruction

Return to the corrected two-generation picture of `ANF-111`. Let `B_n` be the original matched-critical sparse compensator and let `V_n` be the secondary source-heavy layer extracted by `ANF-109`. Suppose the recursive sparse branch is active: both have sub-square-root cardinality and each satisfies the matched source-critical upper bound needed by `ANF-108`. Write their sparsity ratios as

\[
R_{B,n}=\frac{L_n}{|B_n|^2}\to\infty,
\qquad
R_{V,n}=\frac{L_n}{|V_n|^2}\to\infty.
\]

Each component then has controlled source norm `O(L_n)` and interior source energy `o(L_n)` outside its own endpoint layer of width

\[
\delta_{B,n}
=4\frac{\log\log R_{B,n}}{\log R_{B,n}},
\qquad
\delta_{V,n}
=4\frac{\log\log R_{V,n}}{\log R_{V,n}}.
\tag{26}
\]

Let

\[
P_n:=B_n\sqcup V_n,
\qquad
\delta_n:=\max\{\delta_{B,n},\delta_{V,n}\}.
\tag{27}
\]

Because `delta_n->0`, the common interior band is contained in both individual interior bands. The triangle inequality in that restricted Hilbert norm gives

\[
E_{\rm in,\delta_n}(P_n)=o(L_n).
\tag{28}
\]

Also `|P_n|=o(L_n)` and `E_0(P_n)=O(L_n)`. Hence Sections 2--5 apply with no condition whatsoever on `C_0(B_n,V_n)`.

There are exactly two packet outcomes. If

\[
E_0(B_n\sqcup V_n)=o(L_n),
\]

then the two individually source-heavy layers have recycled almost completely **into each other**, but that very cancellation makes their union removable by (9)--(11). If instead their union retains macroscopic source mass, it forces endpoint energy into

\[
U_n=W_n\setminus(B_n\sqcup V_n)
\]

and (25) extracts a third source-heavy height layer entirely inside that unused remainder. The pairwise sufficient condition proposed in `ANF-111`, `C_0(V_n,B_n)=o(L_n)`, is therefore not a genuine gate in this matched-critical sparse branch.

This does not yet make the cascade unconditional. The newly extracted layer must still be classified. If it reaches square-root cardinality, the sparse recursion has terminated in the population alternative of `ANF-109`. If it is sparse but rises well above its source-critical height, it has entered the supercritical-height alternative. Only if it is again sparse and matched-critical does `ANF-108` endpoint-localize it, allowing it to be appended to the old packet and the packet argument restarted. The important correction is that **pairwise non-recycling estimates are not needed at any finite packet stage**; aggregate source norm is the sufficient state variable.

## 7. Adversarial checks and evidence boundary

The source upper bound `E_0(P_n)=O(L_n)` is load-bearing in the source-heavy branch. Without it, Cauchy--Schwarz in (17) would only force `E_edge(U_n)>=L_n^2/E_0(P_n)`, which could vanish relative to `L_n`. In the intended matched-critical application this upper bound is automatic from the individual `O(L_n)` bounds and the triangle inequality, but the abstract packet lemma states it explicitly.

The endpoint localization assumption (6) is also essential. Macroscopic negative packet--remainder interaction could otherwise be carried in the interior of `[-1,1]`, where bounded-height anti-concentration gives no reason for the unused remainder to grow a new high layer. The theorem is therefore not a generic statement about arbitrary source-heavy sublinear unions; it is specifically a statement about already endpoint-localized compensator packets.

A useful abstract stress test is maximal internal recycling. Two old vectors may each have norm `asymp sqrt(L_n)` while nearly cancelling, so their packet norm tends to zero. The theorem does not try to forbid this: it lands in Section 2 and deletes the packet. At the opposite extreme, if their sum retains norm `asymp sqrt(L_n)`, the Montgomery--Taylor affine floor applied to the physical packet/remainder split forces the negative external interaction (14). These two outcomes exhaust the Hilbert-space failure mode that invalidated the naive argument in `ANF-110`; no hidden assumption of pairwise orthogonality has been reintroduced.

The extraction step does not assert that the new layer is itself near-extremal, sparse, matched-critical, or notch-visible. Those are precisely the next branch tests. Nor does packet excision prove `beta_eta<B_eta`; it only shows that a completely self-cancelled recycled packet cannot be responsible for a larger fixed-notch envelope because its removal preserves (11).

The nearest conceptual language is again concentration--compactness/profile decomposition: one groups previously detected profiles and asks whether the aggregate packet vanishes or remains coupled to the remainder. No external compactness theorem is used here. Equations (8)--(18) are finite Hilbert-space geometry plus the exact Montgomery--Taylor affine floor, while (19)--(25) use the already-canonical endpoint anti-concentration estimate of `ANF-108`. No new literature dependency is load-bearing and `SOURCES.md` requires no update.

## 8. Frontier consequence

`ANF-111` correctly identifies recycling as the reason a pairwise recursive proof fails, but the obstruction can now be compressed. In the matched-critical sparse regime, maintain a single endpoint-localized packet `P` of all previously extracted layers. If its aggregate source norm collapses, excise the packet and continue with a near-extremizer having the same fixed-notch exposure. If its aggregate source norm stays macroscopic, its forced polarization pushes endpoint energy into the unused remainder and produces a new disjoint source-heavy height layer.

The remaining escape routes are therefore more concrete: a newly produced layer can reach square-root/bulk cardinality; it can move above the matched source-critical window so endpoint localization no longer follows from the current estimate; or, after packet excision, the residual near-extremizer can reorganize into a different geometric branch such as diffuse superlinear bulk. What no longer needs to be controlled is the complete pairwise interaction graph among finitely many already endpoint-localized sparse layers. **Aggregate packet source mass is enough to neutralize the recycling ambiguity.**