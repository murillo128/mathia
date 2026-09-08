# ANF-111 — sublinear source-heavy layers force polarization, but cascade extraction can recycle earlier tails

**Status:** `EXACT-DERIVED + CORRECTION + AFFINE-SPLIT-POLARIZATION + LAYER-RECYCLING-OBSTRUCTION + CONDITIONAL-NONRECYCLING-GATE`. The arbitrary-split polarization mechanism behind the recent Montgomery--Taylor height analysis is valid and stronger than the earlier fiber-complete formulation: every source-heavy sublinear positive-height component of a global near-extremizer must anti-align macroscopically with its complement. However, that fact does **not** by itself make the height cascade recursively produce new disjoint layers. After extracting a secondary layer `V`, its complement still contains the original source-heavy tail `B`. The endpoint energy forced into that complement can be carried entirely by `B`; a later height cut may therefore rediscover an already known component rather than exhibit a tertiary one.

The correct recursive gate is consequently an **excision/non-recycling estimate**. If the new layer `V` has negligible source interaction with the previously extracted tail `B`, then its forced negative polarization must fall on the genuinely unused remainder, and the endpoint argument does produce new disjoint source-heavy mass there. Without such a bound, the claimed iteration is not justified.

## 1. Arbitrary sublinear source-heavy components still force negative polarization

Retain the Montgomery--Taylor source notation

\[
E_0(X):=\|S_X\|_0^2,
\qquad
L(X):=2|X|-\sigma(X),
\qquad
\Delta(X):=E_0(X)-L(X)\ge0,
\]

where `sigma(X)` counts simple real sites. For an arbitrary conjugation-invariant split

\[
W=A\sqcup B,
\]

define

\[
\kappa(A,B):=\sigma(A)+\sigma(B)-\sigma(W).
\]

At one real support site the local contribution to `kappa` is `0`, `1`, or `2`, and a positive contribution requires points from both pieces. Hence

\[
0\le \kappa(A,B)\le 2\min\{|A|,|B|\}.
\tag{1}
\]

Since cardinality is additive while the simple-real correction need not be,

\[
L(W)=L(A)+L(B)+\kappa(A,B).
\tag{2}
\]

Hilbert polarization gives

\[
E_0(W)=E_0(A)+E_0(B)+2\mathcal C_0(A,B),
\qquad
\mathcal C_0(A,B):=\operatorname{Re}\langle S_A,S_B\rangle_0.
\]

Combining this with (2) yields the exact identity

\[
\boxed{
\Delta(W)
=
\Delta(A)+\Delta(B)+2\mathcal C_0(A,B)-\kappa(A,B).
}
\tag{3}
\]

The sign is important: the failure of affine additivity enters as `-kappa` in the excess identity.

Let now `W_n=A_n\sqcup B_n` be Montgomery--Taylor near-extremal, write `L_n=L(W_n)`, and suppose

\[
\frac{\Delta(W_n)}{L_n}\to0,
\qquad
|B_n|=o(L_n),
\qquad
\liminf_n\frac{E_0(B_n)}{L_n}\ge\lambda>0.
\tag{4}
\]

From `Delta(A_n)>=0`, (3), `L(B_n)<=2|B_n|`, and (1),

\[
\begin{aligned}
2\mathcal C_0(A_n,B_n)
&\le
\Delta(W_n)-\Delta(B_n)+\kappa(A_n,B_n)\\
&=
\Delta(W_n)-E_0(B_n)+L(B_n)+\kappa(A_n,B_n),
\end{aligned}
\]

so

\[
\boxed{
\limsup_n
\frac{\mathcal C_0(A_n,B_n)}{L_n}
\le -\frac\lambda2.
}
\tag{5}
\]

Thus fiber completeness is asymptotically unnecessary for the polarization conclusion at sublinear cardinality. If `B_n` contains no real points, then `sigma(B_n)=0` and removing it changes no real multiplicity, so `kappa(A_n,B_n)=0` exactly. Every strict positive-height cut has this property.

This part is a durable exact strengthening of the bookkeeping used in `ANF-104`: the sign comes from the independent Montgomery--Taylor floors for both physical pieces, not from horizontal separation or an additional geometric hypothesis.

## 2. The secondary layer from ANF-109 therefore has the missing sign

Under the hypotheses of `ANF-108`--`ANF-109`, the original matched-critical sparse compensator `B_n` forces, for every fixed `0<theta<1`, a high layer

\[
V_n
:=
\left\{a\in A_n:
|\operatorname{Im}a|>
\frac{1-\theta}{4\pi}\log\log R_n
\right\},
\qquad
R_n=\frac{L_n}{|B_n|^2}\to\infty,
\tag{6}
\]

with

\[
\liminf_n\frac{E_0(V_n)}{L_n}\ge c_\theta>0.
\tag{7}
\]

Put `D_n=W_n\setminus V_n`. For large `n`, `V_n` is real-free, so its affine defect against `D_n` vanishes. Whenever

\[
|V_n|=o(L_n),
\tag{8}
\]

(5) and (7) imply

\[
\boxed{
\limsup_n
\frac{\mathcal C_0(V_n,D_n)}{L_n}
\le -\frac{c_\theta}{2}<0.
}
\tag{9}
\]

Hence the sign obstruction stated after `ANF-109` is genuinely closed: a sublinear source-heavy secondary layer is automatically a compensator.

If, in addition, `V_n` is sub-square-root and lies in its own matched source-critical window, put

\[
R_{V,n}:=\frac{L_n}{|V_n|^2}\to\infty,
\qquad
4\pi H_{V,n}
\le
\log R_{V,n}+2\log\log R_{V,n}+O(1).
\tag{10}
\]

Then the source-heaviness in (7) and the tail bound of `ANF-103` give the matching lower height bound and `E_0(V_n)=O(L_n)`. With

\[
\delta_{V,n}
:=4\frac{\log\log R_{V,n}}{\log R_{V,n}},
\tag{11}
\]

the same endpoint localization calculation as in `ANF-108` gives

\[
\frac1{L_n}
\int_{|\alpha|\le1-\delta_{V,n}}
J_0(\alpha)|S_{V_n}(\alpha)|^2\,d\alpha
=o(1).
\tag{12}
\]

Since `E_0(D_n)=O(L_n)`, the inner-band part of (9) is `o(L_n)` by Cauchy--Schwarz. Therefore the valid conclusion is

\[
\boxed{
E_{\mathrm{edge},\delta_{V,n}}(D_n)
\ge c'_\theta L_n
}
\tag{13}
\]

for some `c'_theta>0`. Equation (13) is a real recursive-looking pressure, but it is pressure on the **whole complement** of `V_n`; it has not yet isolated unused mass.

## 3. The complement still contains the original tail, so the next extraction can recycle it

The decisive bookkeeping point is

\[
D_n=W_n\setminus V_n
=
B_n\sqcup U_n,
\qquad
U_n:=W_n\setminus(B_n\cup V_n).
\tag{14}
\]

The original `B_n` has not been removed. It is already source-heavy, and in the matched-critical chamber `ANF-108` shows that its source energy is concentrated in a shrinking neighborhood of the Montgomery--Taylor endpoints. Thus (13) does not imply

\[
E_{\mathrm{edge},\delta_{V,n}}(U_n)\gg L_n,
\tag{15}
\]

nor does (9) imply a macroscopic negative interaction between `V_n` and `U_n`. Both statements are compatible with the old tail `B_n` carrying the relevant endpoint energy and absorbing the required negative cross term.

This invalidates the automatic step from (13) to a **new disjoint tertiary component**. A height extraction applied directly to `D_n`, for example

\[
T_n(h):=\{d\in D_n:|\operatorname{Im}d|>h_n\},
\tag{16}
\]

can include the already known `B_n`. Proving `E_0(T_n(h))/L_n\gg1` therefore establishes only that the complement contains source-heavy high mass, something already compatible with the original construction. It does not show that `U_n` contains such mass.

The issue is logical rather than a numerical constant. The original tail lives at a logarithmic source-critical scale, while the secondary pressure generated from `V_n` is only a log--log scale in its new sparsity ratio. In the natural matched regime there is ample height room for `B_n` to satisfy any later high-cut condition. More generally, even without a lower bound on every individual height in `B_n`, the established hypotheses provide no estimate excluding `B_n` from carrying the endpoint portion required in (13). The recursive inference therefore lacks a non-recycling premise.

A useful matched-control abstraction makes the failure transparent. In a Hilbert space, let a near-minimizing total vector contain two already identified components `b` and `v` with macroscopic norms and negative inner product. The statement that `v` anti-aligns with its complement and that `v` is spectrally localized only forces the complement to have mass in the same spectral region; that mass may be exactly `b`. No third orthogonal or disjoint profile follows. The Montgomery--Taylor affine floor supplies the sign in (9), but it does not add the missing profile orthogonality.

## 4. A precise non-recycling condition restores one genuine recursive step

The obstruction can be converted into an exact sufficient gate. Decompose as in (14). From linearity,

\[
\mathcal C_0(V_n,D_n)
=
\mathcal C_0(V_n,B_n)
+
\mathcal C_0(V_n,U_n).
\tag{17}
\]

Assume, in addition to (7)--(12), that the interaction with the previously extracted tail is negligible:

\[
\boxed{
\mathcal C_0(V_n,B_n)=o(L_n).
}
\tag{18}
\]

Then (9) and (17) force

\[
\mathcal C_0(V_n,U_n)\le-cL_n
\tag{19}
\]

for some fixed `c>0` along all sufficiently large indices. In the matched-critical regime, `E_0(B_n)=O(L_n)` and `E_0(V_n)=O(L_n)`; together with `E_0(W_n)=L_n+o(L_n)`, the triangle inequality gives

\[
E_0(U_n)=O(L_n).
\tag{20}
\]

Equation (12), (20), and Cauchy--Schwarz make the inner-band part of (19) `o(L_n)`. Hence the interaction in (19) must occur in the endpoint layer, and another Cauchy--Schwarz inequality gives

\[
\boxed{
E_{\mathrm{edge},\delta_{V,n}}(U_n)\ge c''L_n.
}
\tag{21}
\]

Now the bounded-strip anti-concentration argument of `ANF-108` and the layer-extraction dichotomy of `ANF-109` apply to the genuinely unused remainder `U_n`. Any source-heavy high layer obtained from (21) is disjoint from both `B_n` and `V_n`, so this is a legitimate next stage of the cascade.

Condition (18) is sufficient, not asserted automatically. A weaker one-sided bound preventing `B_n` from absorbing all of the negative polarization would also suffice. The live recursive question is therefore no longer “does a source-heavy layer have the right sign?” but rather “can interactions with **previously extracted** layers account for that sign?” This distinction must be tracked explicitly at every attempted iteration.

## 5. Prior-art boundary and adversarial checks

The nearest general language is concentration--compactness and profile decomposition: recursive profile extraction is normally accompanied by asymptotic orthogonality or a remainder estimate precisely so that a later extraction cannot simply rediscover an earlier profile. No external profile-decomposition theorem is used here, because the Montgomery--Taylor source space has its own affine floor, physical realizability constraints, and endpoint-weighted Fourier--Laplace geometry. The correction above follows solely from the canonical source identities and elementary Hilbert-space estimates, so no new `SOURCES.md` dependency is load-bearing and no general novelty claim about profile decomposition is made.

Three checks are essential. First, `sigma` counts simple real sites, which is why the arbitrary-split correction `kappa` can be positive; (3) has the sign `-kappa`. Second, source-heaviness means `E_0(B)/L(W)\gg1`, not `Delta(B)/L(W)\gg1`; sublinear cardinality is what makes the affine cost negligible. Third, endpoint energy in a complement is not monotone under deleting an already known component, because cross terms can be negative. One cannot pass from (13) to (15) by set inclusion.

The correction does not produce a physical counterexample to the fixed-notch program, and it does not weaken `ANF-108` or `ANF-109`: their first secondary-layer conclusions remain intact. It narrows only the attempted **iteration**. A counterexample to the valid part would have to violate the exact affine identity (3), the Montgomery--Taylor floor for one of the physical pieces, or the endpoint-localization estimates already established under the matched-critical hypotheses.

## 6. Consequence for the fixed-notch frontier

The current sparse-compensator picture is therefore sharper but less automatic than a naive cascade. A matched-critical original tail forces a source-heavy secondary high layer by `ANF-108`--`ANF-109`; if that layer is sublinear, its negative polarization is automatic by (5). If it is also sub-square-root and matched-critical, its complement must carry macroscopic endpoint energy by (13). **What does not follow is that this endpoint energy belongs to a new layer.**

To continue recursively, one must control the interaction graph among already extracted source-heavy components. The concrete next gate is an estimate such as (18), or a stronger decomposition theorem that gives asymptotic orthogonality/excision of previous layers in the Montgomery--Taylor source norm. Failing that, the same original high tail can absorb later compensator pressure indefinitely at the level of the present argument, and repeated log/log-log height cuts do not by themselves prove an infinite hierarchy of distinct physical components.