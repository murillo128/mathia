# FD-169 — Unrestricted mixed measurements collapse partial Farey recovery to target rank

- **Date:** 2026-09-17
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** mixed linear observation / exact rank minimality / representation obstruction
- **Depends on:** FD-118, FD-168
- **Classification:** `EXACT-DERIVED + MIXED-LINEAR-OBSERVATION + RANK-MINIMALITY + NEGATIVE-OBSTRUCTION`

## Claim

The open `FD-168` branch of allowing arbitrary mixed linear measurements has a complete finite-dimensional answer in the same formal source model: **without structural restrictions on the measurement operator, exact recovery of an `R`-coordinate Möbius prefix needs exactly `R` real scalar measurements, and nonlinear decoding cannot improve this.**

Fix `H>=2` and

\[
1\le R\le \lfloor\sqrt H\rfloor.
\tag{1}
\]

Let

\[
V_H:=\mathbb R^{\mathcal Q_H}
\tag{2}
\]

be the formal normalized `FD-118` Fourier-skeleton space. As used in `FD-168`, the formal quotient-source vector and the normalized skeleton vector are related by a linear bijection, so every `Y\in V_H` is realized in that formal model.

Let

\[
T_{H,R}:V_H\longrightarrow\mathbb R^R
\tag{3}
\]

be the linear target map whose output is the first `R` cumulative source coordinates. In the physical case this is

\[
T_{H,R}Y=(M(1),\ldots,M(R)),
\tag{4}
\]

and its `r`-th row is the `FD-168` Möbius inverse row

\[
(T_{H,R}Y)_r
=
\frac1{k_r}
\sum_{d\mid k_r}
\mu(k_r/d)Y(d),
\qquad
k_r=\left\lfloor\frac Hr\right\rfloor.
\tag{5}
\]

The target map has

\[
\operatorname{rank}T_{H,R}=R.
\tag{6}
\]

Now permit an arbitrary real linear measurement operator

\[
L:V_H\longrightarrow\mathbb R^m
\tag{7}
\]

and even an arbitrary, possibly nonlinear, decoder

\[
\Phi:\mathbb R^m\longrightarrow\mathbb R^R.
\tag{8}
\]

Then exact recovery for every formal source,

\[
\Phi(LY)=T_{H,R}Y
\qquad(Y\in V_H),
\tag{9}
\]

is possible **if and only if**

\[
\boxed{
\ker L\subseteq\ker T_{H,R}.
}
\tag{10}
\]

Whenever (10) holds there is in fact a linear map `B:\mathbb R^m\to\mathbb R^R` such that

\[
\boxed{
T_{H,R}=BL.
}
\tag{11}
\]

Consequently

\[
R=\operatorname{rank}T_{H,R}
\le \operatorname{rank}L
\le m,
\tag{12}
\]

while equality is attained by taking `L=T_{H,R}` and `\Phi` to be the identity. Therefore

\[
\boxed{
 m_{\min}^{\mathrm{mixed}}(H,R)=R.
}
\tag{13}
\]

This is not a new compression mechanism. It is an obstruction to treating **unrestricted custom mixed measurements** as a meaningful Farey-information bottleneck: the measurement operator can simply perform the desired inverse transform before observation. Measurement count alone then collapses to the output rank.

As an exact corollary, `FD-168` is recovered by restricting `L` to raw-coordinate selectors. If `P_S` observes only skeleton coordinates in `S\subseteq\mathcal Q_H`, then

\[
T_{H,R}=BP_S
\quad\Longleftrightarrow\quad
\mathcal S_{H,R}\subseteq S,
\tag{14}
\]

where `\mathcal S_{H,R}` is the union of the nonzero Möbius-row supports from `FD-168`. Thus the larger count `|\mathcal S_{H,R}|` is precisely the price of the raw-coordinate observation restriction, not an intrinsic lower bound on unrestricted linear information.

## 1. The target map has exactly `R` independent coordinates

Write the formal quotient-source vector as

\[
m=(m_q)_{q\in\mathcal Q_H}\in\mathbb R^{\mathcal Q_H}.
\tag{15}
\]

`FD-118` gives a linear bijection between `m` and the normalized skeleton `Y`. For `1<=r<=R<=sqrt(H)`, every integer `r` belongs to `\mathcal Q_H`, and `T_{H,R}` is simply the first `R` coordinate projection in `m`-space transported through that bijection.

Those `R` coordinate functionals are linearly independent. Hence their pullbacks through an invertible map remain linearly independent, proving (6). No arithmetic restriction on the physical Möbius trajectory is used here; this is exactly the same full formal real source space under which `FD-168` proves coordinate minimality.

This scope matters. A smaller source class could have lower intrinsic dimension or nonlinear structure. Equation (13) is therefore a theorem about the formal observation model, not a claim that every physically constrained source family needs `R` arbitrary measurements.

## 2. Exact nonlinear decoding forces linear factorization

Assume first that (9) holds. If `v\in\ker L`, then `Lv=L0`, so

\[
T_{H,R}v
=
\Phi(Lv)-\Phi(L0)
=0.
\tag{16}
\]

Thus `\ker L\subseteq\ker T_{H,R}`.

Conversely suppose (10) holds. Define on the image of `L`

\[
B_0(LY):=T_{H,R}Y.
\tag{17}
\]

This is well-defined: if `LY=LY'`, then `Y-Y'\in\ker L\subseteq\ker T_{H,R}`, so `T_{H,R}Y=T_{H,R}Y'`. Because both `L` and `T_{H,R}` are linear, `B_0` is linear on `\operatorname{im}L`. Extend it linearly from `\operatorname{im}L` to all of `\mathbb R^m`; call the extension `B`. Then (11) follows.

Therefore the existence of **any** exact decoder, no matter how nonlinear away from the realized measurement set, already forces a linear decoder on that set. Rank monotonicity applied to (11) gives the lower bound `m>=R`, and `L=T_{H,R}` proves sharpness.

Equivalently, exact mixed observation families are classified by either of the identical conditions

\[
\ker L\subseteq\ker T_{H,R}
\qquad\Longleftrightarrow\qquad
\operatorname{row}(T_{H,R})\subseteq\operatorname{row}(L).
\tag{18}
\]

The first is the indistinguishability formulation; the second says that the measurement row space must contain every target functional.

## 3. `FD-168` is the coordinate-selector specialization

Let `P_S:V_H\to\mathbb R^S` be the coordinate projection onto `S\subseteq\mathcal Q_H`. Its row space is exactly the subspace of linear functionals supported on `S`. By (18), exact prefix recovery from those raw coordinates is possible if and only if every row of `T_{H,R}` is supported inside `S`.

By (5), the support of row `r` is

\[
\left\{
 d\mid k_r:\mu(k_r/d)\ne0
\right\}.
\tag{19}
\]

Taking the union over `1<=r<=R` gives precisely `\mathcal S_{H,R}`. Therefore

\[
\ker P_S\subseteq\ker T_{H,R}
\quad\Longleftrightarrow\quad
\mathcal S_{H,R}\subseteq S,
\tag{20}
\]

which proves (14) and recovers the exact coordinate-minimality statement of `FD-168` as a special case of the general kernel criterion.

This also identifies what the gap

\[
R\le |\mathcal S_{H,R}|\le RH^{o(1)}
\tag{21}
\]

means. It is not evidence that the formal prefix contains more than `R` scalar degrees of freedom. It measures how many **pre-existing Fourier coordinates** are touched when the `R` target functionals are represented in the raw `FD-118` basis.

## 4. Representation audit: arbitrary mixing relocates the inverse rather than discovering structure

The factorization theorem is elementary finite-dimensional linear algebra; no novelty is claimed for the kernel criterion, quotient factorization, rank lower bound, or the fact that a target map itself is an optimal unrestricted measurement operator. The Farey-specific content is only the placement of `FD-168` inside that generic statement: the `FD-118` skeleton identifies the source and observation spaces, and the Möbius inverse rows identify the concrete target operator whose raw-coordinate support had looked like a sampling-complexity barrier.

Transplanting the proof to any finite-dimensional invertible representation gives the same conclusion. If a desired `R`-dimensional linear statistic may itself be used as the acquisition map, then exact linear measurement complexity is just its rank. Hence an unrestricted mixed-measurement theorem here would be a representation relocation, not additional Farey arithmetic.

This is exactly why (13) should be read as a **negative observation-model result**. The formal phrase “custom mixed measurements” is too permissive to carry a source scarcity principle unless some independent physical or arithmetic restriction prevents choosing measurements that have already encoded the Möbius inverse.

A meaningful continuation must therefore constrain the observation class before asking for a lower or upper measurement count. Examples of potentially nontrivial restrictions include spatial point samples or local averages of the Farey field, geometrically local/coarsened operators, horizon-uniform acquisition rules, positivity or bounded-weight constraints, or source-oblivious operators fixed independently of the requested prefix. This finding does not select among those models.

## 5. Hostile audit and boundary

The theorem does **not** say that `R` physical Farey samples suffice. The optimal choice `L=T_{H,R}` is a legal operator only in the deliberately unrestricted skeleton model; implementing it from point values or another physically privileged observation family may require many observations and may be ill-conditioned.

It also does not improve the `FD-167`--`FD-168` stability constant. In a noisy mixed-measurement model, measurement count is meaningless without specifying normalization and the norm in which measurement noise is bounded: arbitrary rescaling or preconditioning of `L` can move conditioning between acquisition and decoding. No stable mixed-measurement claim is made here until that geometry is fixed.

The rank argument does not exclude **source-specific compression** either. It uses the same formal onto real source space as `FD-168`; a theorem exploiting multiplicativity, integrality, squarefree support, or another genuine property of the physical Möbius source would change the admissible set and is outside (13). Such a theorem would be arithmetically substantive in a way that the unrestricted factorization is not.

Finally, nothing here supplies destination coercivity. Directly measuring or exactly recovering `(M(1),...,M(R))` remains a source-identification statement. It yields no new RH-critical Franel--Landau norm estimate, and it does not resolve the separate problem of coupling recovered source information back to the ordered Farey geometry.

## Prior-art check

A fresh search across exact linear recovery, nullspace criteria, linear sufficient statistics, functional recovery, and rank-factorization formulations found the expected generic linear-algebra and compressed-sensing background but no Farey-specific theorem needed here. The only load-bearing step is the elementary equivalence (10)--(11), together with the already internal `FD-118`/`FD-168` transform. No new external source anchor is therefore required in `SOURCES.md`.

The novelty boundary is explicit: the factorization lemma itself is classical. The useful line-local conclusion is that the previously open **unrestricted mixed-measurement** branch cannot by itself produce a nontrivial information budget; it collapses exactly to target rank and subsumes the raw-coordinate minimality theorem as a constrained special case.

## Research consequence

The partial-observation frontier is now cleaner. Raw Fourier selection has a nontrivial exact sampler `\mathcal S_{H,R}` because the observation basis is fixed. Unrestricted linear mixing has no analogous scarcity theorem: it achieves the information-theoretic floor `R` by directly measuring the target functionals. Therefore any next measurement-complexity argument should first specify an observation family that is physically or arithmetically privileged and then analyze its kernel and conditioning.

The live branches are consequently **spatial/coarsened observation**, structurally restricted mixed operators, and source-specific compression on a genuinely arithmetic admissible class. The near-square-root size of `\mathcal S_{H,R}` remains relevant for the raw-coordinate model; (13) bypasses rather than improves that coordinate count. Destination coupling to the nonlocal Franel--Landau norm also remains a separate unresolved gate.

Clue transition check: no accepted clue changes status. This finding closes an observation-model branch exposed by `FD-168` but does not resolve the surviving clue-specific programs.

## Related findings

- `FD-118` — exact invertibility of the Farey-field Fourier skeleton.
- `FD-164`--`FD-166` — finite-horizon ambiguity and permanent-source rigidity.
- `FD-167` — complete-field stable source-prefix inversion.
- `FD-168` — coordinate-minimal stable partial Fourier sampling for a source prefix.
