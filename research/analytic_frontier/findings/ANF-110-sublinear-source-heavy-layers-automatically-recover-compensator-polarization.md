# ANF-110 — sublinear source-heavy layers automatically recover compensator polarization

**Status:** `EXACT-DERIVED + AFFINE-SPLIT-CORRECTION + SOURCE-HEAVY-POLARIZATION + HEIGHT-CASCADE-RECURSION`. `ANF-109` upgrades the secondary log--log height forced by a matched-critical sparse compensator into a genuinely source-heavy high layer, but leaves one stated obstruction to iterating the cascade: the extracted height layer was not shown to inherit the macroscopic negative source polarization used in `ANF-108`. That obstruction is not real in the sublinear-cardinality regime. The Montgomery--Taylor affine term has an exact overlap correction for an arbitrary conjugation-invariant split, and that correction is at most linear in the smaller component. Hence every source-heavy subconfiguration with `o(L)` points inside a global near-extremizer automatically anti-aligns macroscopically with its complement. For positive-height cuts the correction vanishes exactly.

More precisely, write

\[
E_0(X):=\|S_X\|_0^2,
\qquad
L(X):=2|X|-\sigma(X),
\qquad
\Delta(X):=E_0(X)-L(X)\ge0,
\]

where `sigma(X)` is the number of simple real sites and the final inequality is Lamzouri's Montgomery--Taylor floor. Let a finite conjugation-invariant multiset split arbitrarily as

\[
W=A\sqcup B.
\]

Define the affine overlap defect

\[
\kappa(A,B):=\sigma(A)+\sigma(B)-\sigma(W).
\]

Then

\[
\boxed{
0\le\kappa(A,B)\le2\min\{|A|,|B|\},
}
\tag{1}
\]

and the source excess satisfies the exact identity

\[
\boxed{
\Delta(W)
=
\Delta(A)+\Delta(B)+2\mathcal C_0(A,B)-\kappa(A,B),
}
\tag{2}
\]

where

\[
\mathcal C_0(A,B)
:=
\operatorname{Re}\langle S_A,S_B\rangle_0.
\]

Consequently, if `W_n=A_n sqcup B_n` is Montgomery--Taylor near-extremal, `L_n=L(W_n)`,

\[
\frac{\Delta(W_n)}{L_n}\to0,
\qquad
|B_n|=o(L_n),
\]

and `B_n` is source-heavy,

\[
\liminf_n\frac{E_0(B_n)}{L_n}\ge\lambda>0,
\]

then necessarily

\[
\boxed{
\limsup_n
\frac{\mathcal C_0(A_n,B_n)}{L_n}
\le-rac\lambda2.
}
\tag{3}
\]

Thus the fiber-complete hypothesis used in `ANF-104` is asymptotically unnecessary for source polarization of every sublinear source-heavy component. In particular, the source-heavy high layers extracted by `ANF-109` automatically recover the missing compensator sign whenever their cardinality is `o(L_n)`. If such a layer is also sub-square-root and lies in its own matched source-critical height window, the `ANF-108` endpoint argument can be repeated and forces a tertiary source-heavy height layer. The recursive gate is therefore no longer polarization: it is whether successive source-heavy layers remain sub-square-root and matched-critical rather than becoming macroscopically populated or escaping to a much higher height scale.

## 1. The affine defect of an arbitrary split is explicit

The Hilbert part is always additive up to polarization:

\[
E_0(W)=E_0(A)+E_0(B)+2\mathcal C_0(A,B).
\tag{4}
\]

Only `L` can fail to add. Since `|W|=|A|+|B|`,

\[
\begin{aligned}
L(A)+L(B)
&=2|W|-\sigma(A)-\sigma(B)\\
&=L(W)-\kappa(A,B),
\end{aligned}
\]

or equivalently

\[
\boxed{
L(W)=L(A)+L(B)+\kappa(A,B).
}
\tag{5}
\]

It remains to understand `kappa`. Work one real support site at a time. If the total multiplicity at that site is one, the unique point belongs to exactly one component and the local contribution to `kappa` is zero. If the total multiplicity is at least two, the site contributes only when one or both pieces see multiplicity exactly one. The local contribution is therefore `0`, `1`, or `2`, and a positive contribution requires the site to occur in both pieces. Hence `kappa>=0`, and the number of contributing sites is at most the number of real points in either component; allowing the possible value `2` proves (1).

Combining (4)--(5) with the definition of `Delta` gives (2) exactly. No asymptotic argument, horizontal separation, height bound, or fiber decomposition enters this identity.

There are two useful zero-defect cases. A split that keeps every real support site intact has `kappa=0`, recovering the bookkeeping used in `ANF-104`. More importantly for the present frontier, if `B` contains **no real points**, then `sigma(B)=0` and removing `B` does not change any real multiplicity, so

\[
\sigma(A)=\sigma(W),
\qquad
\boxed{\kappa(A,B)=0.}
\tag{6}
\]

Every strict positive-height cut has exactly this property, even if it splits several nonreal conjugate pairs away from other points sharing the same horizontal center.

## 2. Any sublinear source-heavy component must anti-align

From (2) and the independent Montgomery--Taylor floors `Delta(A),Delta(B)>=0`,

\[
2\mathcal C_0(A,B)
\le
\Delta(W)-\Delta(B)+\kappa(A,B).
\tag{7}
\]

If `m=|B|`, then

\[
L(B)=2m-\sigma(B)\le2m,
\qquad
\kappa(A,B)\le2m.
\tag{8}
\]

Since `Delta(B)=E_0(B)-L(B)`, equations (7)--(8) yield the finite estimate

\[
\boxed{
\frac{\mathcal C_0(A,B)}{L(W)}
\le
\frac12\frac{\Delta(W)}{L(W)}
-
\frac12\frac{E_0(B)}{L(W)}
+2\frac{m}{L(W)}.
}
\tag{9}
\]

This already proves (3). If the whole configuration is near-extremal, the first term is `o(1)`; if `m=o(L)`, the last term is `o(1)`; and a source-heavy component contributes at most `-lambda/2+o(1)` through the middle term.

For a real-free component, (6) sharpens (9) to

\[
\boxed{
\frac{\mathcal C_0(A,B)}{L(W)}
\le
\frac12\frac{\Delta(W)}{L(W)}
-
\frac12\frac{E_0(B)}{L(W)}
+rac{|B|}{L(W)}.
}
\tag{10}
\]

Thus the sign is not a geometric extra hypothesis. It is forced by the coexistence of three facts: the union nearly saturates the Montgomery--Taylor floor, the component carries source energy much larger than its own affine size, and the complement separately obeys the same floor. A positive macroscopic self-energy excess has nowhere to go except a negative cross term.

The same correction also removes the fiber-complete restriction from the remote-decoupling estimate of `ANF-104` at sparse scale. From (2),

\[
\Delta(B)
\le
\Delta(W)+\kappa(A,B)+2|\mathcal C_0(A,B)|.
\tag{11}
\]

Inserting the kernel bound from `ANF-104` therefore reproduces its source-transfer inequality with only an additional `kappa/L=O(|B|/L)` term. For every sublinear tail this term vanishes. The finite exact statement (11), rather than a new decay theorem, is the relevant generalization here.

## 3. ANF-109's sparse secondary layer already has the missing sign

Retain the hypotheses of `ANF-109`. Thus an original matched-critical sparse compensator produces, for every fixed `0<theta<1`, a high layer

\[
V_n
:=
A_n^{>\theta}
=
\left\{a\in A_n:
|\operatorname{Im}a|>
\frac{1-\theta}{4\pi}\log\log R_n
\right\}
\]

such that

\[
\liminf_n\frac{E_0(V_n)}{L_n}
\ge c_\theta>0.
\tag{12}
\]

Let

\[
D_n:=W_n\setminus V_n,
\qquad
m_{\theta,n}:=|V_n|.
\]

For all sufficiently large `n` the height threshold is positive, hence `V_n` contains no real points and the split `W_n=D_n sqcup V_n` has `kappa(D_n,V_n)=0` exactly. Therefore, whenever

\[
m_{\theta,n}=o(L_n),
\tag{13}
\]

(10) and (12) give

\[
\boxed{
\limsup_n
\frac{\mathcal C_0(D_n,V_n)}{L_n}
\le-rac{c_\theta}{2}<0.
}
\tag{14}
\]

This closes the specific missing hypothesis stated at the end of `ANF-109`: in every sublinear-cardinality branch, the extracted source-heavy layer does not merely carry positive source energy. It is automatically a genuine compensator against the rest of the near-extremizer.

Notice that (13) is much weaker than the sub-square-root condition used by the universal height inversion. In particular, a layer of order `sqrt(L_n)` still has the forced sign (14). What fails at square-root scale is not polarization but the divergence of

\[
R_{\theta,n}:=
\frac{L_n}{m_{\theta,n}^2}.
\]

Thus the cardinality and sign gates are now cleanly separated.

## 4. Matched-critical sparse layers can be iterated one level further

Assume in addition to (12) that

\[
m_{\theta,n}=o(\sqrt{L_n}),
\qquad
R_{\theta,n}:=rac{L_n}{m_{\theta,n}^2}\to\infty,
\tag{15}
\]

and that the maximum height `H_{V,n}` of `V_n` lies in its own matched source-critical upper window,

\[
4\pi H_{V,n}
\le
\log R_{\theta,n}
+2\log\log R_{\theta,n}
+O(1).
\tag{16}
\]

Source-heaviness (12) and `ANF-103` provide the matching lower bound. Hence `E_0(V_n)=O(L_n)`. Since `E_0(W_n)=L_n+o(L_n)`, the triangle inequality also gives

\[
E_0(D_n)=O(L_n).
\tag{17}
\]

Choose

\[
\delta_{\theta,n}
:=4\frac{\log\log R_{\theta,n}}
          {\log R_{\theta,n}}.
\tag{18}
\]

Exactly as in `ANF-108`, the universal pointwise bound on `S_{V_n}` together with (16) gives

\[
\frac1{L_n}
\int_{|\alpha|\le1-\delta_{\theta,n}}
J_0(\alpha)|S_{V_n}(\alpha)|^2\,d\alpha
=o(1).
\tag{19}
\]

The macroscopic negative interaction (14) cannot occur on this inner band because (17), (19), and Cauchy--Schwarz make its inner contribution `o(L_n)`. Therefore it occurs in the shrinking endpoint layer, and another Cauchy--Schwarz inequality forces

\[
E_{\mathrm{edge},\delta_{\theta,n}}(D_n)
\ge c'_{\theta}L_n
\tag{20}
\]

for some `c'_theta>0`.

Applying the bounded-strip endpoint anti-concentration inequality of `ANF-108` to `D_n` now yields

\[
\boxed{
\liminf_n
\frac{H_{D,n}}
     {\log\log R_{\theta,n}}
\ge\frac1{4\pi}.
}
\tag{21}
\]

Moreover the layer-extraction argument of `ANF-109` uses only the source bound (17), the endpoint lower bound (20), and the same anti-concentration inequality. Hence for every fixed `0<theta'<1`, the tertiary layer

\[
T_n
:=
\left\{d\in D_n:
|\operatorname{Im}d|>
\frac{1-\theta'}{4\pi}
\log\log R_{\theta,n}
\right\}
\]

satisfies

\[
\boxed{
\liminf_n\frac{E_0(T_n)}{L_n}>0.
}
\tag{22}
\]

Thus a matched-critical sparse secondary layer really does generate a **source-heavy tertiary layer**. If `T_n` is again sublinear, its negative polarization is automatic by Section 2; if it is additionally sub-square-root and matched-critical relative to its own sparsity ratio, the same argument can repeat. No new sign lemma is needed at later positive-height stages.

## 5. Adversarial checks and prior-art boundary

The main bookkeeping risk is the definition of `sigma`: it counts **simple real sites**, not all real support sites. This is why `kappa` can equal `2` at a real site split as one point plus one point. The bound in (1) deliberately allows that factor two. The sign of (2) is also audit-sensitive: because `L(W)=L(A)+L(B)+kappa`, the excess identity contains `-kappa`, so solving for the cross term produces the harmless `+kappa` error in (7). Reversing this sign would incorrectly strengthen the theorem.

The source-heavy assumption refers to `E_0(B)/L(W)`, not to `Delta(B)/L(W)`. Passing from one to the other costs `L(B)/L(W)`, which is exactly why sublinear cardinality is required in (3). A macroscopic component can carry order-`L` source energy simply through its own affine floor and need not anti-align. Likewise, the recursive conclusion (21)--(22) requires the extra matched-critical upper bound (16). If the extracted layer rises much higher, its norm can be supermacroscopic and the endpoint width from `ANF-108` is no longer the correct one; that remains a distinct escape chamber.

The nearest general literature is concentration--compactness and norm splitting. Lions' concentration--compactness principle classifies loss of compactness and splitting of minimizing sequences through subadditivity, while the Brézis--Lieb lemma gives asymptotic splitting of `L^p` norms under pointwise convergence. Neither is used here and neither supplies (2)--(3): the present sign comes from the special affine Montgomery--Taylor floor obeyed separately by **both** physical subconfigurations, together with the explicit simple-real-site correction `kappa`. The identity itself is elementary Hilbert polarization plus affine bookkeeping, so no general novelty is claimed for norm decomposition and no new external theorem is load-bearing. `SOURCES.md` therefore remains unchanged.

A decisive finite audit of the new step is simple: choose any finite conjugation-invariant multiset, split multiplicities at several real sites in arbitrary ways, compute `sigma(A),sigma(B),sigma(W)`, and verify (2) directly from polarization. A counterexample would have to violate either the local multiplicity classification behind (1) or the already-canonical Montgomery--Taylor floor for one of the two pieces.

## 6. Consequence for the fixed-notch frontier

`ANF-108` and `ANF-109` had converted a minimally source-visible sparse tail into a log--log source-heavy secondary layer, but the program still listed recovery of the compensator sign as an independent recursion gate. Equations (3) and (14) remove that gate. **Every sublinear source-heavy positive-height layer in a near-extremizer is already forced to cancel macroscopically against its complement.**

The cascade frontier is therefore sharper. If a secondary layer is sub-square-root and remains in its matched-critical source window, a tertiary source-heavy layer follows by (21)--(22), and the same logic is recursively available. To escape this mechanism, a physical near-extremizer must eventually do at least one of three things: promote a layer to square-root-or-larger cardinality so its sparsity ratio stops diverging; send a sparse layer substantially above its matched-critical height window; or leave the sparse-tail chamber altogether through genuinely diffuse/macroscopic organization. The missing negative-polarization hypothesis from `ANF-109` is no longer an independent obstruction.