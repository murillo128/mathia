# NB-297 — projected dilation escape gives a baseline-free ordinary-enrichment certificate

- **Date:** 2026-09-23
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-014, NB-282, NB-284, NB-287, NB-290, NB-292, NB-293, NB-296
- **Classification:** `EXACT-DERIVED + CANONICAL-NYMAN-SOURCE + FIRST-FREE-SAMPLING + ORDINARY-NESTED-SECTION + DILATION-ESCAPE + PRINCIPAL-ANGLE-DEFECT + SOURCE-SAMPLE-INTERTWINING-DEFECT + SCHUR-COMPLEMENT + TARGET-AWARE-LOWER-CERTIFICATE + AMBIENT-SATURATION-CONTROL-KILLED + RATE-NOT-CLAIMED + PRIOR-ART-AUDITED`

## Claim

`NB-296` shows that the strong off-critical multiplicative-band coercivity of `NB-294`--`NB-295` can be spent entirely on repairing the **dilated old baseline** while the ordinary undilated finite-section cost does not improve at all. The next useful observable therefore has to live inside the ordinary nested increment

\[
K_{mn-1,Z}-K_{n-1,Z},
\]

not only inside the quotient relative to `S_m V_(n-1,Z)`.

There is a canonical baseline-free block supplied by the actual Nyman dilation itself. Fix a finite zero packet `Z`, abbreviate

\[
U:=V_{n-1,Z},
\qquad
V^+:=V_{mn-1,Z},
\qquad
L:=L_Z,
\qquad
K:=K_{n-1,Z}=LP_UL^*,
\]

and suppose `L|_U` is onto. Let

\[
S:=S_m,
\qquad
(S h)(s)=m^{1/2-s}h(s),
\qquad
D:=D_Z(m),
\]

so that

\[
LS=DL,
\qquad
SU\subseteq V^+.
\tag{1}
\]

Project the dilated old section against the **undilated** old section and define

\[
\boxed{
R_{m,n,Z}:=(U+SU)\ominus U
=\overline{(I-P_U)SU}.
}
\tag{2}
\]

(All spaces here are finite-dimensional, so the closure is harmless.) Its first-free sampling Gram is

\[
\boxed{
\Xi_{m,n,Z}:=LP_{R_{m,n,Z}}L^*\succeq0.
}
\tag{3}
\]

Because

\[
U\oplus R_{m,n,Z}=U+SU\subseteq V^+,
\]

one has the ordinary-section Loewner bound

\[
\boxed{
0\preceq \Xi_{m,n,Z}
\preceq K_{mn-1,Z}-K_{n-1,Z}.
}
\tag{4}
\]

Thus `Xi` is not a gain against a transported baseline. It is an explicit positive block already contained in the genuine ordinary enrichment from `n-1` to `mn-1`.

More importantly, `Xi` has an exact source/sample factorization. Let

\[
E:\mathbb C^d\to U,
\qquad d=\dim U=n-2,
\]

be any isometric synthesis map onto `U`, and set

\[
X:=LE,
\qquad
T:=E^*SE,
\qquad
Q:=I_d-T^*T,
\qquad
Y:=DX-XT.
\tag{5}
\]

Then

\[
\boxed{
Q=E^*S^*(I-P_U)SE\succeq0,
}
\tag{6}
\]

\[
\boxed{
Y=L(I-P_U)SE,
}
\tag{7}
\]

and

\[
\boxed{
\Xi_{m,n,Z}
=
YQ^+Y^*.
}
\tag{8}
\]

Equation `(8)` is basis-independent despite the coordinate notation. It separates two necessary ingredients of ordinary multiplicative enrichment: `Q` measures how much of the dilated source actually escapes the old section, while `Y` measures which part of that escaping source remains visible to the first-free zero sampler. The combination `DX-XT` is an exact **source-sample intertwining defect**.

For the actual canonical Nyman family the source escape is macroscopically large in rank. Put

\[
q_{m,n}:=\max\left\{1,\left\lfloor\frac{n-1}{m}\right\rfloor\right\}.
\tag{9}
\]

Finite independence and the exact dilation law give

\[
\boxed{
SU\cap U=S_mV_{q_{m,n},Z},
}
\tag{10}
\]

hence

\[
\boxed{
\operatorname{rank}Q
=
\dim R_{m,n,Z}
=
n-1-q_{m,n}.
}
\tag{11}
\]

In particular, for every `m>=2` and every `n>=3`,

\[
\boxed{
\dim R_{m,n,Z}
\ge
\left\lceil\frac{n-1}{2}\right\rceil.
}
\tag{12}
\]

So every nontrivial integer dilation pushes at least roughly half of the old canonical source dimensions outside the old section before the final cutoff `mn-1` is reached. This is genuine source geometry. But rank alone still does not imply target gain: all of that escape can in principle be first-free-sample-null, which is exactly the failure mode detected by `Y=0`.

Finally, `(4)` gives a true baseline-free target certificate. For any datum `y in C^N`, let

\[
\Delta_{m,n,Z}^{\mathrm{ord}}(y)
:=
y^*K^{-1}y
-
y^*K_{mn-1,Z}^{-1}y.
\tag{13}
\]

Define

\[
M_{\mathrm{esc}}
:=K^{-1/2}\Xi_{m,n,Z}K^{-1/2},
\qquad
x:=K^{-1/2}y.
\tag{14}
\]

Then

\[
\boxed{
\Delta_{m,n,Z}^{\mathrm{ord}}(y)
\ge
x^*M_{\mathrm{esc}}(I+M_{\mathrm{esc}})^{-1}x.
}
\tag{15}
\]

Unlike the gain in `NB-293`--`NB-295`, the right side of `(15)` compares the **ordinary old section** `V_(n-1,Z)` with a subspace of the ordinary enlarged section. The ambient kernel-saturation control of `NB-296` kills this certificate exactly: there `U=ran L^*`, hence `U^perp subset ker L`, so `Y=0`, `Xi=0`, and the lower bound correctly reports zero ordinary enrichment even while the dilated-baseline band is fully coercive.

The new bottleneck is therefore sharper than after `NB-296`: source escape itself is abundant by `(11)`--`(12)`. What remains is to prove that the actual Nyman source-sample defect

\[
\boxed{Y=DX-XT}
\]

has enough target-aligned mass after being priced by the principal-angle metric `Q^+`.

## 1. The projected dilated copy is an ordinary innovation block

The canonical covariance from `NB-292` gives

\[
S_mV_{n-1,Z}\subseteq V_{mn-1,Z}.
\tag{16}
\]

Since also `U=V_(n-1,Z) subseteq V^+`, their sum lies in `V^+`. The orthogonal decomposition

\[
U+SU=U\oplus R_{m,n,Z}
\tag{17}
\]

therefore yields

\[
P_U+P_R=P_{U+SU}\preceq P_{V^+}.
\tag{18}
\]

Applying `L` on the left and `L^*` on the right gives

\[
K+\Xi_{m,n,Z}
\preceq K_{mn-1,Z},
\]

which is exactly `(4)`.

This is the key distinction from the band

\[
W_{m,n,Z}=V^+\ominus SU
\]

used in `NB-292`--`NB-295`. There the old comparison space is `SU`; here the old comparison space is the actual undilated `U`. The two orthogonal decompositions answer different questions. `NB-296` proves that the former can carry enormous off-critical gain while the latter carries none.

## 2. Principal-angle factorization of the ordinary escape Gram

Choose an isometry `E:C^d -> U`. Since `P_U=EE^*`, define the escape synthesis

\[
F:=(I-P_U)SE.
\tag{19}
\]

Its range is exactly `R_(m,n,Z)`. Because `S` and `E` are isometries,

\[
\begin{aligned}
F^*F
&=E^*S^*(I-P_U)SE\\
&=I_d-E^*S^*EE^*SE\\
&=I_d-T^*T
=Q,
\end{aligned}
\tag{20}
\]

proving `(6)`. The nonzero eigenvalues of `Q` are the squared sines of the nonzero principal angles between `U` and `SU`.

Under sampling,

\[
LF
=LSE-LEE^*SE
=DX-XT,
\tag{21}
\]

which proves `(7)`.

For any finite-rank synthesis `F`, the orthogonal projector onto its range is

\[
P_{\operatorname{ran}F}
=F(F^*F)^+F^*.
\tag{22}
\]

Therefore

\[
\begin{aligned}
\Xi_{m,n,Z}
&=LP_RL^*\\
&=(LF)(F^*F)^+(LF)^*\\
&=YQ^+Y^*,
\end{aligned}
\]

proving `(8)`.

Changing the orthonormal coordinates of `U` replaces `E` by `EU_0` with `U_0` unitary. Then `X`, `T`, `Q`, and `Y` transform covariantly and `YQ^+Y^*` is unchanged. Thus `Xi` is an intrinsic subspace quantity, not an artifact of Gram--Schmidt ordering.

Equation `(8)` also identifies the exact saturation condition

\[
\boxed{
\Xi_{m,n,Z}=0
\iff
Y=0
\iff
L(I-P_U)S_mU=\{0\}.
}
\tag{23}
\]

So absence of ordinary gain from the projected dilated copy means precisely that every source direction escaping `U` under dilation becomes sample-null after orthogonal projection. A large principal-angle defect `Q` cannot rule this out by itself.

## 3. Canonical arithmetic forces macroscopic source escape

Write the quotient atoms as in `NB-292`,

\[
H_{j,Z}=G_j/B_Z,
\]

so multiplication by `B_Z` is isometric and finite independence is inherited from the canonical Nyman atoms. The exact dilation law is

\[
S_mH_{j,Z}
=
\sqrt m\left(
H_{mj,Z}-\frac1jH_{m,Z}
\right).
\tag{24}
\]

Let

\[
q=q_{m,n}
=\max\left\{1,\left\lfloor\frac{n-1}{m}\right\rfloor\right\}.
\]

If `2<=j<=q`, then necessarily `m<n`, and both indices `m` and `mj` are at most `n-1`. Hence `(24)` lies in `U`, proving

\[
S_mV_{q,Z}\subseteq SU\cap U.
\tag{25}
\]

For the converse, let

\[
f=\sum_{j=2}^{n-1}a_jH_{j,Z}\in U
\]

and suppose `S_mf in U`. Expanding with `(24)` gives

\[
S_mf
=
\sqrt m\sum_{j=2}^{n-1}a_jH_{mj,Z}
-
\sqrt m\left(\sum_{j=2}^{n-1}\frac{a_j}{j}\right)H_{m,Z}.
\tag{26}
\]

When `m<n`, the correction `H_m` already lies in `U`; finite independence therefore forces `a_j=0` for every `mj>=n`, so `f in V_(q,Z)`. When `m>=n`, all `H_(mj)` lie outside `U` and are distinct from `H_m`; finite independence forces all `a_j=0`, while `q=1` and `V_(1,Z)={0}`. This proves `(10)` in both regimes.

Because `S_m` is injective,

\[
\dim(SU\cap U)=\dim V_{q,Z}=q-1.
\]

Since `dim U=n-2`,

\[
\dim R
=
\dim U-\dim(SU\cap U)
=(n-2)-(q-1)
=n-1-q,
\]

which proves `(11)`. As `m>=2`, one has `q<=max{1,floor((n-1)/2)}`, giving `(12)`.

This source-rank statement is deliberately weaker than a quantitative principal-angle bound. It says many directions escape exactly, but the corresponding nonzero eigenvalues of `Q` may still be arbitrarily small. Nor does it force `Y` to have comparable rank.

## 4. The escape Gram gives a genuine ordinary target decrement

Because `L|_U` is onto, `K` is positive definite. From `(4)`,

\[
K_{mn-1,Z}\succeq K+\Xi\succeq K\succ0.
\tag{27}
\]

Inverting reverses Loewner order:

\[
K_{mn-1,Z}^{-1}
\preceq
(K+\Xi)^{-1}
\preceq
K^{-1}.
\tag{28}
\]

Thus

\[
\Delta_{m,n,Z}^{\mathrm{ord}}(y)
\ge
y^*\bigl(K^{-1}-(K+\Xi)^{-1}\bigr)y.
\tag{29}
\]

Whitening by `K` and using

\[
I-(I+M)^{-1}=M(I+M)^{-1}
\]

proves `(15)`.

There is also a one-direction version useful for future arithmetic estimates. For `a in C^d`, set

\[
f_a:=Fa\in R,
\qquad
e_a:=Lf_a=Ya.
\tag{30}
\]

Let

\[
R_U:=P_UL^*K^{-1}
\]

be the minimum-norm right inverse on the old section. The neutralized vector

\[
q_a:=f_a-R_Ue_a
\tag{31}
\]

lies in `(U+R) cap ker L` and is orthogonal to the old kernel. Since `f_a perp U`,

\[
\|q_a\|^2
=a^*Qa+e_a^*K^{-1}e_a,
\tag{32}
\]

while for the old minimum source `h_U(y)=R_Uy`,

\[
|\langle h_U(y),q_a\rangle|
=|e_a^*K^{-1}y|.
\tag{33}
\]

Bessel therefore gives the explicit baseline-free certificate

\[
\boxed{
\Delta_{m,n,Z}^{\mathrm{ord}}(y)
\ge
\frac{|e_a^*K^{-1}y|^2}
{a^*Qa+e_a^*K^{-1}e_a}
}
\tag{34}
\]

whenever `f_a!=0`; the right side is interpreted as zero for a zero escape direction.

Equation `(34)` is the direct ordinary-section analogue of the canonical-defect certificate in `NB-293`, but its numerator cannot be generated merely by the contraction of the dilated baseline. It measures the first-free sample of an actual source direction **after removing its projection onto the undilated old section**.

## 5. Ambient saturation is annihilated exactly

The control in `NB-296` takes the old section to be the ambient kernel span

\[
U=E_Z=\operatorname{ran}L^*=(\ker L)^\perp.
\]

For every vector `h`,

\[
(I-P_U)h\in U^\perp=\ker L.
\]

Therefore

\[
Y=L(I-P_U)S_mE=0,
\qquad
\Xi=0.
\tag{35}
\]

So `(15)` gives no ordinary target gain in exactly the model where `NB-296` shows the ordinary cost is already saturated, even though the multiplicative band relative to `S_mU` can attain the full determinant growth and uniform off-critical coercivity of `NB-294`--`NB-295`.

This is the main discrimination supplied by the present observable. `Gamma_(m,n,Z)` from `NB-292` detects how much the full section improves over the **dilated** copy. `Xi_(m,n,Z)` detects how much of the dilation itself escapes the **undilated** old section and remains visible after that escape. Only the latter is automatically a lower block of the ordinary increment.

The control also prevents overreading `(11)`--`(12)`. A source can have a large-dimensional geometric escape while its sampler annihilates every escaped direction. Hence rank, principal-angle mass, or source novelty alone still cannot replace the target-aware factor `Y`.

## 6. Prior-art audit and research disposition

The underlying ingredients are classical: orthogonal projection onto the range of a synthesis operator, principal angles between finite-dimensional subspaces, Moore--Penrose inversion, and minimum-norm interpolation. No novelty is claimed for those Hilbert-space identities. The Nyman dilation law and semigroup viewpoint are already classical in the Báez-Duarte/Bagchi formulation and are established locally before this finding.

A fresh literature search again found Hugh Carvill's 2025 preprint *Beurling Nyman Geometry and Gram Matrix Structure, Ladder Density and Polynomial Decay via Mellin Smoothing*, which studies Gram decay and block compressibility on multiplicative Nyman ladders, and the 2026 Hardy-space approximation work of Manzur--Noor--Quintero, which studies zero-free half-planes via finite Nyman approximation. The searched material did not expose the baseline-free projected-dilation escape Gram `(8)`, the exact canonical intersection/rank formula `(10)`--`(12)`, or the ambient-saturation discrimination `(35)`. These papers are adjacent prior-art boundaries, not load-bearing inputs.

No external theorem beyond standard finite-dimensional Hilbert-space algebra is needed for the proof, so `SOURCES.md` is unchanged. No `mind/**` file is updated: the result sharpens the current bridge but does not yet supply the moving-Ford estimate required for a durable rate statement.

Keep this finding as the first direct response to the baseline failure isolated by `NB-296`. The ordinary increment satisfies

\[
K_{mn-1,Z}-K_{n-1,Z}
\succeq
\boxed{YQ^+Y^*},
\qquad
Y=DX-XT,
\qquad
Q=I-T^*T.
\]

For the canonical Nyman source, `Q` has rank at least about half the old section dimension for every `m>=2`; the remaining obstruction is therefore not lack of source escape. It is the **visibility and target alignment of that escape**. A useful next pass should estimate `YQ^+Y^*` or the scalar certificate `(34)` in the moving Ford regime. If those quantities can still collapse while respecting the exact Nyman source metric, that collapse should be exhibited explicitly rather than inferred from the ambient kernel-saturation control, which this certificate already excludes.