# NB-068 — zero one-cell memory can coexist with a stable tail

**Status:** `EXACT-DERIVED + ABSTRACT-MATCHED-CONTROL + DECISIVE-NEGATIVE + BIDIAGONAL-BOUNDARY-CHAIN + EXACT-SCHUR-CALIBRATION + METHOD-BOUNDARY`.

`NB-063`--`NB-066` isolate the canonical one-cell forward-memory maps

\[
\Gamma_R:\mathcal G_R\to\mathcal X_R^\circ
\]

and show that a persistent stable-tail mode has square-summable one-cell transmission. `NB-067` then replaces this local description by the global continuation constant `Lambda_R` and its finite Schur certificates `Xi_(R,N)`. A natural remaining hope is that sufficiently weak local memory -- for example `Gamma_R=0`, finite-band causal coupling, or exact capture of every memory-free cell sector -- might already force the stable tail to vanish.

It does not. There is an explicit matched control in which **every canonical one-cell memory map is identically zero, every innovation has only one-cell forward bandwidth, the local visible/defect flags are exactly the same as in a flat control, yet a nonzero stable tail survives.** The obstruction is a scalar boundary chain at infinity, and `NB-067` detects it exactly through its finite future Schur complements.

More precisely, let

\[
\mathcal H
=\bigoplus_{j\ge1}\mathcal X_j,
\qquad
\mathcal X_j=\mathbb C e_j\oplus\mathcal Z_j,
\tag{1}
\]

where the `e_j` are orthonormal and every `Z_j` is an infinite-dimensional Hilbert space orthogonal to the scalar spine

\[
\mathcal S:=\overline{\operatorname{span}}\{e_j:j\ge1\}.
\tag{2}
\]

Let `J_R` project onto the first `R-1` cells, and choose a real sequence

\[
t_j>0,
\qquad
0<\sum_{j\ge1}t_j^2<\infty,
\qquad
t:=\sum_{j\ge1}t_je_j.
\tag{3}
\]

Consider two causal sources.

The flat source is

\[
D_j^{(0)}:=t_{j+1}e_j,
\qquad
\mathcal A_0=\mathcal S.
\tag{4}
\]

The boundary-chain source is

\[
D_j^{(t)}:=t_{j+1}e_j-t_je_{j+1},
\qquad
\mathcal A_t
:=\overline{\operatorname{span}}\{D_j^{(t)}:j\ge1\}
=\mathcal S\cap t^\perp.
\tag{5}
\]

For **both** sources and every `R>=2`,

\[
\boxed{
\mathcal G_R:=J_R\mathcal A
=\operatorname{span}\{e_1,\ldots,e_{R-1}\},
}
\tag{6}
\]

and therefore

\[
\boxed{
\mathcal K_R
=J_R\mathcal H\ominus\mathcal G_R
=\bigoplus_{j<R}\mathcal Z_j.
}
\tag{7}
\]

The newest innovation is the same in both models,

\[
C_R=(J_{R+1}-J_R)D_R=t_{R+1}e_R,
\tag{8}
\]

and

\[
\mathcal X_R^\circ
=\mathcal X_R\ominus\operatorname{span}\{C_R\}
=\mathcal Z_R.
\tag{9}
\]

Every old continuation in the boundary-chain source enters the new cell only through the scalar direction `e_R`, hence only through the removable innovation direction `C_R`. Consequently

\[
\boxed{
\Gamma_R^{(0)}=\Gamma_R^{(t)}=0
\qquad(R\ge2).
}
\tag{10}
\]

The pure one-cell defect sector is also identical:

\[
\mathcal N_R=\mathcal Z_R.
\tag{11}
\]

Nevertheless the stable tails are different:

\[
\boxed{
\mathcal T_\infty(\mathcal A_0)=\{0\},
\qquad
\mathcal T_\infty(\mathcal A_t)=\operatorname{span}\{t\}.
}
\tag{12}
\]

Thus the local flag `(G_R,K_R,C_R,Gamma_R,N_R)` can agree at every finite window while the global stable-tail space changes from zero to one dimension.

For the boundary-chain source the global continuation cost and every finite `NB-067` certificate are explicit. Write

\[
T_{<R}^2:=\sum_{j<R}t_j^2,
\qquad
T_{R:N+1}^2:=\sum_{j=R}^{N+1}t_j^2,
\qquad
T_{\ge R}^2:=\sum_{j\ge R}t_j^2.
\tag{13}
\]

Then

\[
\boxed{
\Lambda_R^2
=\frac{T_{<R}^2}{T_{\ge R}^2}
\longrightarrow\infty,
}
\tag{14}
\]

and for every finite `N>=R`,

\[
\boxed{
\Xi_{R,N}
=1+\frac{T_{<R}^2}{T_{R:N+1}^2}.
}
\tag{15}
\]

Hence for **every** horizon schedule `N(R)>=R`,

\[
\Xi_{R,N(R)}
\ge
1+\frac{T_{<R}^2}{T_{\ge R}^2}
=1+\Lambda_R^2
\longrightarrow\infty.
\tag{16}
\]

The flat matched control has instead

\[
\boxed{
\Lambda_R^{(0)}=0,
\qquad
\Xi_{R,N}^{(0)}=1
}
\tag{17}
\]

for all `R,N`.

The conclusion is a strict method boundary: **small, square-summable, or even identically zero canonical one-cell memory does not control the stable tail. Nor does finite causal bandwidth.** A proof from the actual Nyman source must use a genuinely global continuation datum -- such as the finite Schur domination of `NB-067`, an equivalent boundary-chain estimate, or additional arithmetic structure that rules the boundary chain out. The one-cell `Gamma_R` geometry by itself cannot do so.

## 1. The boundary-chain span is exactly one hyperplane

Every vector `D_j^(t)` is orthogonal to `t` because

\[
\langle D_j^{(t)},t\rangle
=t_{j+1}t_j-t_jt_{j+1}=0.
\tag{18}
\]

Conversely, let `x=sum x_je_j in S` be orthogonal to every `D_j^(t)`. Then

\[
t_{j+1}x_j-t_jx_{j+1}=0,
\tag{19}
\]

so, because every `t_j` is nonzero,

\[
\frac{x_j}{t_j}=\frac{x_{j+1}}{t_{j+1}}
\qquad(j\ge1).
\tag{20}
\]

Thus `x` is a scalar multiple of `t`. Taking orthogonal complements inside `S` proves (5).

For any finite prefix `g in span{e_1,...,e_(R-1)}`, choose

\[
y_R=-\frac{\langle g,J_Rt\rangle}{t_R}
\tag{21}
\]

and put `a=g+y_Re_R`. Then `a` has finite support and is orthogonal to `t`, so `a in A_t`; hence `J_Ra=g`. This proves (6) for the boundary-chain source. It is immediate for the flat source. Equation (7) follows from the cell decomposition.

Since

\[
\mathcal A_0^\perp=\bigoplus_j\mathcal Z_j,
\qquad
\mathcal A_t^\perp=\left(\bigoplus_j\mathcal Z_j\right)\oplus\operatorname{span}\{t\},
\tag{22}
\]

while

\[
\overline{\bigcup_R\mathcal K_R}=\bigoplus_j\mathcal Z_j,
\tag{23}
\]

the `NB-066` identity `T_infinity=A^perp minus K_fin` gives (12).

This is the exact local/global pathology isolated abstractly in `NB-066`: every finite truncation of `t` looks natural because `J_Rt in G_R`, but the global vector `t` is orthogonal to the entire natural source.

## 2. The model has no canonical one-cell memory at all

For both sources, the new cell is

\[
\mathcal X_R=\mathbb Ce_R\oplus\mathcal Z_R
\tag{24}
\]

and the newest causal direction `C_R=t_(R+1)e_R` spans its scalar part. Thus `X_R^circ=Z_R`.

In the flat source every old generator has already ended before cell `R`, so `Gamma_R=0`. In the boundary-chain source each `D_j^(t)` is supported on exactly two adjacent scalar cells. At the step `R -> R+1`, the only old generator that can reach the new cell is `D_(R-1)^(t)`, and its new-cell component is a scalar multiple of `e_R`, hence of `C_R`. The quotient projection defining `Gamma_R` removes precisely that direction. Therefore (10) holds.

This control is stronger than merely setting a small operator norm. The global Gram matrix of the boundary-chain innovations is tridiagonal because

\[
\langle D_i^{(t)},D_j^{(t)}\rangle=0
\qquad(|i-j|>1),
\tag{25}
\]

so the source has only nearest-neighbor coefficient coupling. Yet the cumulative chain leaves the global boundary mode `t` unresolved.

The phenomenon is therefore not caused by long-range raw Gram entries or by a nonzero `Gamma_R` channel. It is the accumulation of removable scalar innovation components across infinitely many cells.

## 3. The `NB-066` extension lower bound is sharp in the control

Fix `g in G_R`. Any exact extension `a in A_t` with `J_Ra=g` can be written

\[
a=g+y,
\qquad
\operatorname{supp}y\subseteq\{R,R+1,\ldots\},
\tag{26}
\]

and the single hyperplane constraint is

\[
\langle y,(I-J_R)t\rangle
=-\langle g,J_Rt\rangle.
\tag{27}
\]

Cauchy--Schwarz is attained by taking `y` parallel to `(I-J_R)t`. Hence the least future energy is exactly

\[
\inf\|y\|^2
=
\frac{|\langle g,J_Rt\rangle|^2}{T_{\ge R}^2}.
\tag{28}
\]

Maximizing over `g` gives

\[
\Lambda_R^2
=
\frac{\|J_Rt\|^2}{\|(I-J_R)t\|^2}
=
\frac{T_{<R}^2}{T_{\ge R}^2},
\tag{29}
\]

which proves (14). Since `t` has infinitely many nonzero square-summable coordinates, the numerator tends to `||t||^2>0` and the denominator tends to zero.

For the distinguished stable mode itself, `g=J_Rt`, equation (28) gives

\[
\mathfrak E_R(t)
=
\frac{\|J_Rt\|^2}{\|(I-J_R)t\|},
\tag{30}
\]

so the lower bound in `NB-066`,

\[
\mathfrak E_R(t)\,\|(I-J_R)t\|
\ge\|J_Rt\|^2,
\tag{31}
\]

is an equality in this control. Its blow-up mechanism is therefore sharp, not an artefact of the Cauchy--Schwarz estimate used there.

## 4. Finite Schur complements see the hidden boundary mode exactly

Restrict now to future innovations `D_R^(t),...,D_N^(t)`. Their span is exactly the space of scalar vectors supported in coordinates `R,...,N+1` that can be used, together with the unique causal prefix for `g`, while preserving orthogonality to `t`.

Equivalently, after the early trace `g` is fixed, the admissible finite-horizon tail vectors are precisely the vectors `y` supported on `R,...,N+1` satisfying

\[
\langle y,P_{[R,N+1]}t\rangle
=-\langle g,J_Rt\rangle.
\tag{32}
\]

The minimum is again attained by the truncated `t` direction and equals

\[
\inf\|y\|^2
=
\frac{|\langle g,J_Rt\rangle|^2}{T_{R:N+1}^2}.
\tag{33}
\]

Therefore the finite total continuation norm is

\[
\|g\|^2
+
\frac{|\langle g,J_Rt\rangle|^2}{T_{R:N+1}^2}.
\tag{34}
\]

The largest generalized Rayleigh quotient is obtained for `g` parallel to `J_Rt`, giving exactly (15). Letting `N->infinity` recovers

\[
\Xi_{R,N}\downarrow1+\Lambda_R^2
\tag{35}
\]

as required by `NB-067`.

For the flat source the causal prefix representing `g` is already supported before cell `R`; future innovations are orthogonal to it and cannot reduce its norm. Hence every finite and infinite continuation cost is exactly the visible norm, proving (17).

Thus `NB-067` distinguishes two sources that `NB-063`'s canonical one-cell quotient geometry cannot distinguish. The finite Schur complement is not merely a computational repackaging of `Gamma_R`; it contains genuinely longer-range compatibility information.

## 5. Prior-art and falsification boundary

The weighted first-difference construction in (5) is elementary Hilbert-space/operator theory. Its global interpretation as an `l^2` boundary mode is closely analogous to the classical appearance of boundary conditions at infinity in limit-circle Jacobi theory. A bounded literature audit found, for example, the standard limit-circle treatment of selfadjoint Jacobi operators and boundary conditions at infinity (D. R. Yafaev, *Selfadjoint Jacobi operators in the limit circle case*, J. Operator Theory 89 (2023), 87--103). No novelty is claimed for weighted-difference hyperplanes, tridiagonal Gram matrices, or boundary-at-infinity phenomena.

No external theorem is load-bearing here: equations (18)--(35) are direct calculations. `SOURCES.md` therefore requires no new anchor.

The control is intentionally abstract. It does **not** assert that the actual Nyman innovations have a hidden one-dimensional boundary mode, nor that their finite Schur certificates diverge. The Nyman cells have additional source structure that may rule this pathology out. The result only falsifies deductions based on the local causal geometry shared by the two controls.

In particular, the following implications are invalid without extra hypotheses:

\[
\Gamma_R=0\ \forall R
\quad\Longrightarrow\quad
\mathcal T_\infty=\{0\},
\tag{36}
\]

and even

\[
\text{nearest-neighbor causal Gram coupling}
+\Gamma_R=0\ \forall R
\quad\Longrightarrow\quad
\sup_R\Lambda_R<\infty.
\tag{37}
\]

The matched flat source proves that the opposite stable-tail outcomes are compatible with the same finite-window subspace flag and canonical one-cell memory maps.

## 6. Consequence for the live Nyman--Beurling frontier

`NB-065` and the final part of `NB-066` show that persistent target mass follows an approximate-kernel trajectory for the one-cell maps. This finding shows that such local attenuation can be **perfect** and still coexist with a persistent global mode. Further attempts to rule out persistence solely through decay or summability of `||Gamma_R||`, through the dimension of the cell-memory channel, or through finite raw Gram bandwidth cannot succeed in this level of generality.

The live sufficient target from `NB-067` is therefore genuinely stronger and correctly placed. One must control a finite-horizon/global quantity such as

\[
S_{R,N(R)}\preceq C^2A_R
\tag{38}
\]

on an unbounded sequence, or prove an actual-source property that prevents the scalar boundary-chain mechanism. A particularly useful arithmetic next question is whether the Nyman causal innovations admit a source-forced coercivity or transfer estimate that rules out an `l^2` boundary mode analogous to `t` while remaining visible in finite Schur complements. Any such estimate would use information that the canonical one-cell quotient map deliberately discards.