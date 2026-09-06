# ANF-072 — central-notch six-point collapse reversal reduces to real multiplicity

**Status:** `EXACT-DERIVED + CENTRAL-NOTCH + COMPLETE-ONE-PAIR-REVERSAL-SCREENING + STRUCTURAL-REDUCTION`. `ANF-070` screens the complete Montgomery--Taylor negative-curvature class, while `ANF-071` confines any reversal created from the base-nonreversing side to a thin `D=0`, `y=0` layer. That remaining layer cannot exhaust the affine margin. More strongly, for every objective-compatible central-notch width
\[
0<\eta<3-\sqrt6,
\]
and every
\[
\boxed{0<s\le \frac1{4000},}
\tag{1}
\]
every one-pair/four-real-anchor configuration for which the **notched** profile reverses real collapse has strictly positive candidate affine slack.

Consequently, at these parameters a one-pair six-point affine violation cannot be created by moving a doubled real point off the real axis. If
\[
W_{y,T}=\{iy,-iy,t_1,t_2,t_3,t_4\}
\]
violates the candidate central-notch affine inequality, then its collapsed real multiset
\[
R_T=\{0,0,t_1,t_2,t_3,t_4\}
\]
already violates it. Thus the first one-pair six-point obstruction, if one remains, is a **real-multiplicity** obstruction rather than a new vertical complex geometry.

Use the notation
\[
J_s=J_{\rm MT}-s\phi_\eta,
\qquad
\phi_\eta(\alpha)=b_\eta\left(1-\frac{|\alpha|}{\eta}\right)_+,
\qquad
m_\eta:=b_\eta\eta,
\]
with `0<b_eta<=1`, and let `F_s=\widehat J_s`. Put
\[
D(T)=2K_0+\sum_{j=1}^4K(t_j),
\qquad
D_s(T)=2K_s(0)+\sum_{j=1}^4K_s(t_j).
\]
The candidate intercept is `A_s=2-2s m_eta`, and write `S_s` for the corresponding six-point affine slack.

## 1. The `D>=0` boundary layer has a fixed zeroth-order collapsed margin

Let
\[
r(t)=\left(-\frac{K_0}{3}-K(t)\right)_+,
\qquad
e(t)=\left(K(t)+\frac{K_0}{3}\right)_+.
\]
The certified spatial floor of `ANF-070` is
\[
F_{\rm MT}(t)\ge\frac18r(t).
\tag{2}
\]
Since
\[
K(t)=-\frac{K_0}{3}-r(t)+e(t),
\]
one has the exact identity
\[
\sum_{j=1}^4r(t_j)
=\frac{2K_0}{3}+\sum_{j=1}^4e(t_j)-D(T)
\ge\frac{2K_0}{3}-D(T).
\tag{3}
\]
The collapsed Montgomery--Taylor slack from `ANF-068` is
\[
\mathcal S_{\rm MT}(R_T)
=4\sum_jF_{\rm MT}(t_j)
+2\sum_{j<k}F_{\rm MT}(t_j-t_k).
\tag{4}
\]
All terms are nonnegative. Equations (2)--(4) therefore give the bound, valid without assuming `D(T)<0`,
\[
\boxed{
\mathcal S_{\rm MT}(R_T)
\ge \frac{K_0}{3}-\frac{D(T)}2.
}
\tag{5}
\]
This is the key point missed by a first-order treatment of the `ANF-071` layer: on the boundary `D=0`, the base collapsed slack does not vanish. It has the fixed floor `K_0/3`.

For the triangular notch, the exact slack identity of `ANF-068` gives
\[
\mathcal S_s(R_T)
=\mathcal S_{\rm MT}(R_T)
+s\left(12m_\eta-E_{\Phi_\eta}(R_T)\right).
\tag{6}
\]
The spectral amplitude of `R_T` is
\[
2+\sum_{j=1}^4e^{-2\pi i\alpha t_j},
\]
whose modulus is at most `6`, and `\int\phi_\eta=m_\eta`. Hence
\[
E_{\Phi_\eta}(R_T)\le36m_\eta
\]
and therefore
\[
\boxed{
\mathcal S_s(R_T)
\ge\mathcal S_{\rm MT}(R_T)-24s m_\eta.
}
\tag{7}
\]

Now suppose the base profile is nonreversing, `D(T)>=0`, but the notch creates a reversal. `ANF-071` proves
\[
0\le D(T)<s b_\eta\eta^3,
\qquad
0<-D_s(T)\le s b_\eta\eta^3.
\tag{8}
\]
Combining (5), (7), and (8),
\[
\boxed{
\mathcal S_s(R_T)
>
\frac{K_0}{3}
-\frac{s b_\eta\eta^3}{2}
-24s b_\eta\eta.
}
\tag{9}
\]
Thus the collapsed configuration retains a positive **zeroth-order** margin as `s->0`; no first-order cancellation on `D=0` is possible.

## 2. The vertical loss in the new layer is quadratic in the curvature defect

The all-order theorem of `ANF-069` applies to `J_s`, because `J_s>=0` is nonzero, continuous, even, and compactly supported. Its quartic floor for four anchors gives, for every `y>0`,
\[
E_{F_s}(W_{y,T})-E_{F_s}(R_T)
\ge
-\frac{3D_s(T)^2}{2M_{2,s}(0)},
\tag{10}
\]
where `ANF-071` gives the exact moment
\[
M_{2,s}(0)
=M_2(0)-\frac{s b_\eta\eta^5}{15}.
\tag{11}
\]
On the notch-created branch (8), equations (9)--(11) yield
\[
\boxed{
\begin{aligned}
\mathcal S_s(W_{y,T})
>
&\frac{K_0}{3}
-\frac{s b_\eta\eta^3}{2}
-24s b_\eta\eta\\
&-\frac{3s^2b_\eta^2\eta^6}
{2\left(M_2(0)-s b_\eta\eta^5/15\right)}.
\end{aligned}
}
\tag{12}
\]
The potentially negative vertical contribution is therefore second order in the already thin curvature width. The `O(sqrt(s))` height compactification of `ANF-071` is consistent with this estimate but is not needed for the affine conclusion.

For the objective-compatible range, `eta<3-sqrt(6)<0.551`, `b_eta<=1`, and `s<=1/4000`. Using the canonical certified bounds
\[
K_0>0.1549985926411760,
\qquad
M_2(0)>0.05854458579969,
\]
one has
\[
M_{2,s}(0)>0.0585.
\]
The three losses on the right side of (12) are respectively less than `0.000021`, `0.003306`, and `0.00000005`. Therefore
\[
\boxed{
\mathcal S_s(W_{y,T})>0.0483
}
\tag{13}
\]
for every notch-created reversal with `D(T)>=0`.

## 3. The same small `s` screens notched reversals on the `D<0` side

It remains to remove a minor logical gap left by `ANF-070`: its base slack bound is global in height, but its explicit notch-loss estimate was stated only where the **base** profile itself reverses. A notched crossing could in principle extend slightly beyond the base crossing.

If `D(T)<0` and the notched profile reverses at height `y`, then `D_s(T)<0` by `ANF-069`. The global Montgomery--Taylor curvature minimum used in `ANF-069` gives
\[
-D(T)<d:=0.055099459323598.
\tag{14}
\]
Moreover the triangular curvature perturbation satisfies
\[
|D_s(T)-D(T)|\le s b_\eta\eta^3,
\tag{15}
\]
because the six curvature slots each have absolute value at most `K_phi(0)=b_eta eta^3/6`. Hence
\[
-D_s(T)<d+s b_\eta\eta^3.
\tag{16}
\]
Applying the quartic height bound of `ANF-069` to `J_s`, then using `s<=1/4000`, `eta<0.551`, `b_eta<=1`, `M_{2,s}(0)>0.0585`, and `pi>3.14`, gives
\[
\boxed{y<0.268.}
\tag{17}
\]

`ANF-070` already proves the global base-profile bound
\[
\mathcal S_{\rm MT}(W_{y,T})>\frac{93}{10000}
\qquad(D(T)<0,\ y>0).
\tag{18}
\]
Its exact notch identity gives
\[
\mathcal S_s(W_{y,T})
\ge
\mathcal S_{\rm MT}(W_{y,T})
-s m_\eta
\left[
\left(2\cosh(2\pi\eta y)+4\right)^2-12
\right].
\tag{19}
\]
From `eta<0.551`, (17), and `pi<22/7`,
\[
2\pi\eta y<0.929<1.
\]
For `0<=x<1`, the elementary series estimate `(2n)!>=2^n` gives
\[
\cosh x
=\sum_{n\ge0}\frac{x^{2n}}{(2n)!}
\le\sum_{n\ge0}\left(\frac{x^2}{2}\right)^n
=\frac1{1-x^2/2}.
\tag{20}
\]
At `x<0.929` this implies that the bracket in (19) is less than `45`. Therefore
\[
\boxed{
\mathcal S_s(W_{y,T})
>
\frac{93}{10000}-45s b_\eta\eta
>0.0031.
}
\tag{21}
\]
Thus every notched collapse reversal on the base negative-curvature side is safe as well, including a possible small extension beyond the base crossing.

## 4. Complete consequence for one-pair six-point vertical motion

For fixed `T`, `ANF-069` applied to the notched profile says exactly:
\[
D_s(T)\ge0
\Longrightarrow
E_{F_s}(W_{y,T})>E_{F_s}(R_T)
\quad(y>0),
\tag{22}
\]
while `D_s(T)<0` gives the unique collapse-reversing branch. Sections 2 and 3 prove that every point of that reversing branch has positive affine slack when (1) holds.

The real-count term and cardinality term are identical for `W_{y,T}` and `R_T`; only the energy changes. Hence, if a one-pair six-point configuration were to violate the candidate affine inequality, it cannot lie on the reversing branch. It must satisfy
\[
E_{F_s}(W_{y,T})\ge E_{F_s}(R_T),
\]
and then
\[
\mathcal S_s(R_T)\le\mathcal S_s(W_{y,T})<0.
\tag{23}
\]
Therefore
\[
\boxed{
\mathcal S_s(W_{y,T})<0
\quad\Longrightarrow\quad
\mathcal S_s(R_T)<0
\qquad
\left(0<\eta<3-\sqrt6,\ 0<s\le\frac1{4000}\right).
}
\tag{24}
\]
This does not prove the six-point affine inequality: the collapsed multiset has a double real point, and the finite-real separator of `ANF-034` concerns distinct real sets. What (24) proves is that **one conjugate pair introduces no additional six-point obstruction beyond that real-multiplicity boundary** for the explicit small central-notch regime.

## 5. Prior art, stress tests, and next boundary

A fresh structure-level literature check revisited the Montgomery--Taylor extremal/Hilbert-space framework of Carneiro--Chandee--Littmann--Milinovich and the September 2026 Hilbert-space formulation of Lamzouri. Those sources provide the ambient pair-correlation machinery already recorded in `SOURCES.md`; no searched source formulates the finite one-pair notch-collapse reduction (24), and no new external theorem is load-bearing here. `SOURCES.md` therefore remains unchanged.

The load-bearing audit points are all explicit. Equation (5) uses only the certified spatial floor of `ANF-070` and keeps the positive anchor--anchor terms discarded. Equation (7) pays the worst possible triangular spectral energy `36m_eta`, so it does not assume favorable notch phase. Equation (10) is the profile-generic quartic floor of `ANF-069`, applied legitimately because `J_s>=0`. The numerical cutoff `1/4000` is deliberately conservative; its purpose is to give a simple uniform regime, not to optimize the admissible notch amplitude.

The result does not control two or more nonreal pairs, does not settle total cardinality eleven where the one-pair coefficient protection first stops being automatic, and does not itself prove the mixed-multiplicity real inequality for `R_T`. The decisive six-point one-pair question has moved: instead of analyzing a singular vertical boundary layer near `D=0`, determine whether the candidate central-notch affine slack can be negative on the collapsed real multisets `\{0,0,t_1,t_2,t_3,t_4\}`. A negative example there is already a real-multiplicity obstruction; a uniform nonnegative proof would close the complete one-pair six-point category.