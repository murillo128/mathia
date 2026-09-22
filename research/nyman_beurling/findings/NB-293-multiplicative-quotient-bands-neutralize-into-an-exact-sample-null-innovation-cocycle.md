# NB-293 — multiplicative quotient bands neutralize into an exact sample-null innovation cocycle

- **Date:** 2026-09-22
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-282, NB-285, NB-287, NB-290, NB-292
- **Classification:** `EXACT-DERIVED + CANONICAL-NYMAN-SOURCE + FIRST-FREE-SAMPLING + DILATION-SEMIGROUP + MULTIPLICATIVE-QUOTIENT-BAND + BLOCK-NULL-INNOVATION + MINIMUM-NORM-INTERPOLATION + TARGET-AWARE-DECREMENT + POSITIVE-GRAM-WHITENING + CANONICAL-DEFECT-CERTIFICATE + RATE-NOT-CLAIMED + PRIOR-ART-AUDITED`

## Claim

`NB-292` gives the multiplicative quotient band

\[
W_{m,n,Z}=V_{mn-1,Z}\ominus S_mV_{n-1,Z}
\]

and its positive first-free sampling Gram

\[
\Gamma_{m,n,Z}
=
K_{mn-1,Z}-D_Z(m)K_{n-1,Z}D_Z(m)^*.
\]

The missing target-aware step is exact once the lower quotient section is first-free-surjective: **the entire band becomes a canonical block of new interpolation-null directions after subtracting the old-section repair of its samples, and the minimum synthesis gain is exactly the projection onto that block.**

Fix a finite zero packet `Z` and abbreviate

\[
V_r:=V_{r,Z},
\qquad
L:=L_Z,
\qquad
K_r:=LP_rL^*,
\qquad
D_r:=V_r\cap\ker L.
\]

Assume `L|_(V_(n-1))` is onto, as supplied eventually by `NB-282`. Put

\[
U:=S_mV_{n-1},
\qquad
V:=V_{mn-1},
\qquad
W:=V\ominus U,
\]

and write

\[
D:=D_Z(m),
\qquad
A:=LP_UL^*=DK_{n-1}D^*,
\qquad
B:=L|_W,
\qquad
\Gamma:=BB^*=\Gamma_{m,n,Z}.
\]

Then `A` is positive definite. The minimum-norm right inverse on `U` is

\[
R_U
:=P_UL^*A^{-1}
=S_mR_{n-1}D^{-1}.
\tag{1}
\]

Define

\[
\boxed{
J_{m,n,Z}:W\to V,
\qquad
Jw:=w-R_UBw.
}
\tag{2}
\]

Then `J` is a linear bijection onto

\[
\boxed{
Q_{m,n,Z}
:=
D_{mn-1}\ominus S_mD_{n-1},
}
\tag{3}
\]

so that

\[
\boxed{
D_{mn-1}
=
S_mD_{n-1}\oplus Q_{m,n,Z}
}
\tag{4}
\]

orthogonally. Moreover

\[
\boxed{
J^*J
=
I_W+B^*A^{-1}B
\succeq I_W.
}
\tag{5}
\]

Thus every multiplicative band direction can be made first-free-null by cancelling its samples with the unique minimum-norm vector from the dilated old section. The price of that cancellation is encoded exactly in `(5)`.

The null blocks themselves satisfy the multiplicative cocycle

\[
\boxed{
Q_{km,n,Z}
=
Q_{k,mn,Z}\oplus S_kQ_{m,n,Z}
}
\tag{6}
\]

orthogonally.

For any first-free datum `y in C^N`, let

\[
g_{m,n}(y):=R_Uy
=S_mR_{n-1}D^{-1}y
\]

be its minimum-norm realization in `U`, and let

\[
h_{mn-1}(y):=P_VL^*K_{mn-1}^{-1}y
\]

be the minimum-norm realization in `V`. Then

\[
\boxed{
h_{mn-1}(y)
=
g_{m,n}(y)-P_{Q_{m,n,Z}}g_{m,n}(y).
}
\tag{7}
\]

Consequently the whole multiplicative-section improvement is the block Parseval mass

\[
\boxed{
\Delta_{m,n,Z}(y)
:=
(D^{-1}y)^*K_{n-1}^{-1}(D^{-1}y)
-y^*K_{mn-1}^{-1}y
=
\|P_Qg_{m,n}(y)\|^2.
}
\tag{8}
\]

In sample coordinates,

\[
\boxed{
\Delta_{m,n,Z}(y)
=
y^*A^{-1}B
\bigl(I_W+B^*A^{-1}B\bigr)^{-1}
B^*A^{-1}y.
}
\tag{9}
\]

Equivalently, with

\[
M:=A^{-1/2}\Gamma A^{-1/2},
\qquad
x:=A^{-1/2}y,
\]

we have

\[
\boxed{
\Delta_{m,n,Z}(y)
=
x^*M(I+M)^{-1}x.
}
\tag{10}
\]

If `M e_j=lambda_j e_j` and `x=sum_j x_j e_j`, this is

\[
\boxed{
\Delta_{m,n,Z}(y)
=
\sum_j
\frac{\lambda_j}{1+\lambda_j}|x_j|^2.
}
\tag{11}
\]

Hence the positive matrix cocycle from `NB-292` becomes coercive only through the spectral mass of the **actual transformed datum** in its generalized band modes. Large trace, determinant, operator norm, or scalar dilation loss alone still do not force target improvement.

Finally, let

\[
b_{m,n,Z}
=S_m\psi_{n,Z}-c_{m,n}\psi_{mn,Z}\in W,
\qquad
\|b_{m,n,Z}\|^2=1-c_{m,n}^2,
\]

and

\[
d_{m,n,Z}=Lb_{m,n,Z}
\]

be the normalized canonical innovation defect from `NB-292`. Its neutralized null direction

\[
\widehat q_{m,n,Z}
:=Jb_{m,n,Z}
=b_{m,n,Z}-R_Ud_{m,n,Z}
\in Q_{m,n,Z}
\tag{12}
\]

has exact norm

\[
\boxed{
\|\widehat q_{m,n,Z}\|^2
=
1-c_{m,n}^2
+d_{m,n,Z}^*A^{-1}d_{m,n,Z}.
}
\tag{13}
\]

Therefore

\[
\boxed{
\Delta_{m,n,Z}(y)
\ge
\frac{
|d_{m,n,Z}^*A^{-1}y|^2
}{
1-c_{m,n}^2+d_{m,n,Z}^*A^{-1}d_{m,n,Z}
}
}
\tag{14}
\]

whenever the denominator is nonzero, with the right side interpreted as zero when the defect vanishes.

Equation `(14)` is a direct target-aware section-enrichment certificate built from the vector defect of `NB-292`. It still contains the missing arithmetic problem explicitly: prove a lower bound on the target pairing `d^*A^(-1)y` at moving Ford scales, with the repair cost in the denominator paid honestly.

---

## 1. Block neutralization is exactly the new nullspace

The covariance from `NB-292` is

\[
LS_m=DL.
\tag{15}
\]

Because `D` is invertible,

\[
\ker(L|_U)=S_mD_{n-1}.
\tag{16}
\]

Surjectivity of the lower section therefore passes to `U`, and `(1)` follows from the isometry of `S_m`: realizing samples `x` in `U` is equivalent to realizing `D^{-1}x` in `V_(n-1)`.

For `w in W`,

\[
LJw
=Bw-LR_UBw
=0.
\]

Also `w perp U`, while `R_UBw` belongs to the orthogonal complement of `ker(L|_U)` inside `U`. Hence

\[
Jw\perp S_mD_{n-1},
\]

so `ran J subseteq Q_(m,n,Z)`.

The map is injective because `Jw=0` would put the same nonzero vector in the orthogonal spaces `W` and `U`.

For surjectivity, take `q in Q_(m,n,Z)` and write uniquely

\[
q=u+w,
\qquad
u\in U,
\qquad
w\in W.
\tag{17}
\]

In words, `(17)` means `q=u+w` with the same variable `u` lying in `U` and `w` lying in `W`. Since `Lq=0`,

\[
Lu=-Bw.
\tag{18}
\]

The orthogonality `q perp S_mD_(n-1)` and `w perp U` imply that `u` is orthogonal to `ker(L|_U)`. Thus `u` is the unique minimum-norm vector in `U` with samples `-Bw`, namely

\[
u=-R_UBw.
\]

Hence `q=Jw`, proving the bijection and `(4)`.

For `w,t in W`, the `W` and `U` components are orthogonal, so

\[
\begin{aligned}
\langle Jw,Jt\rangle
&=
\langle w,t\rangle
+
\langle R_UBw,R_UBt\rangle\\
&=
\langle w,t\rangle
+
\langle Bw,A^{-1}Bt\rangle,
\end{aligned}
\]

because `R_U^*R_U=A^{-1}`. This proves `(5)`.

If `w in W cap ker L`, then `Bw=0` and therefore

\[
\boxed{Jw=w.}
\tag{19}
\]

So the already-sample-null part of the band embeds unchanged into `Q`. But it remains orthogonal to every old-section source in `U`. Such a direction alone cannot lower the synthesis norm in the natural enrichment `U subset V`; target improvement appears only when a band direction has samples that must be cancelled by an old-section repair.

This last statement is deliberately local to the multiplicative block. It does not say that a sample-null band vector is irrelevant to every ordinary cutoff; relative to another starting section it can occupy a different part of the `NB-287` null-innovation filtration.

---

## 2. The null blocks inherit the semigroup cocycle

Equation `(15)` sends first-free-null vectors to first-free-null vectors. Hence

\[
S_{km}D_{n-1}
\subseteq
S_kD_{mn-1}
\subseteq
D_{kmn-1}.
\]

Splitting the orthogonal difference at the middle space gives

\[
\begin{aligned}
D_{kmn-1}\ominus S_{km}D_{n-1}
&=
\bigl(D_{kmn-1}\ominus S_kD_{mn-1}\bigr)\\
&\quad\oplus
\bigl(S_kD_{mn-1}\ominus S_{km}D_{n-1}\bigr).
\end{aligned}
\]

The first summand is `Q_(k,mn,Z)` and the second is `S_kQ_(m,n,Z)`, proving `(6)`.

Thus `NB-292` has parallel multiplicative structures:

\[
W_{km,n,Z}
=
W_{k,mn,Z}\oplus S_kW_{m,n,Z}
\]

for source quotient bands, and

\[
Q_{km,n,Z}
=
Q_{k,mn,Z}\oplus S_kQ_{m,n,Z}
\]

for the exact null freedom unlocked after those bands are neutralized against the sample-surjective old section. The map `J` is generally not isometric; `(5)` records exactly the repair-induced metric distortion.

---

## 3. Minimum-norm synthesis removes exactly the new null block

Let `g=R_Uy`. It is feasible in `U` and orthogonal to `S_mD_(n-1)`. Every feasible vector in `V` is in

\[
g+D_{mn-1}.
\]

Using `(4)`, the only new kernel component that can reduce its norm is `Q`. Orthogonal projection therefore gives `(7)`, and Pythagoras gives

\[
\|g\|^2-
\|h_{mn-1}(y)\|^2
=
\|P_Qg\|^2.
\]

The two norms are

\[
\|g\|^2
=y^*A^{-1}y
=(D^{-1}y)^*K_{n-1}^{-1}(D^{-1}y)
\]

and

\[
\|h_{mn-1}(y)\|^2
=y^*K_{mn-1}^{-1}y,
\]

which proves `(8)`.

Since `J` is injective with range `Q`,

\[
P_Q=J(J^*J)^{-1}J^*.
\]

For `g=R_Uy`, orthogonality of `U` and `W` gives

\[
J^*g
=-B^*A^{-1}y.
\]

Together with `(5)`, this proves `(9)`. Since

\[
K_{mn-1}=A+\Gamma,
\qquad
\Gamma=BB^*,
\]

Woodbury also gives

\[
\Delta_{m,n,Z}(y)
=y^*\bigl(A^{-1}-(A+\Gamma)^{-1}\bigr)y.
\tag{20}
\]

Whitening `(20)` gives `(10)` and `(11)`.

The target gain itself has an exact multiplicative chain rule. Define `Delta_(m,n,Z)(y)` by `(8)`. Since `D_Z(km)=D_Z(k)D_Z(m)`, inserting the intermediate space `S_kV_(mn-1)` yields

\[
\boxed{
\Delta_{km,n,Z}(y)
=
\Delta_{k,mn,Z}(y)
+
\Delta_{m,n,Z}\bigl(D_Z(k)^{-1}y\bigr).
}
\tag{21}
\]

Thus target gains do telescope across multiplicative factorization, but the datum transforms contravariantly. Any fixed-datum coercivity claim must control that transport rather than silently dropping it.

---

## 4. The canonical dilation defect supplies one explicit null direction

Apply `J` to the `NB-292` canonical defect `b=b_(m,n,Z)`. Its samples are `d=d_(m,n,Z)`, so `(12)` is immediate. Because `b in W` and `R_Ud in U`, the two terms are orthogonal. Hence

\[
\begin{aligned}
\|\widehat q\|^2
&=
\|b\|^2+
\|R_Ud\|^2\\
&=
1-c_{m,n}^2+d^*A^{-1}d,
\end{aligned}
\]

proving `(13)`.

For the old minimum source `g=R_Uy`,

\[
\langle g,b\rangle=0,
\]

so

\[
|\langle g,\widehat q\rangle|
=
|\langle R_Uy,R_Ud\rangle|
=
|d^*A^{-1}y|.
\tag{22}
\]

Normalizing `widehat q` and applying Bessel inside `Q`, then using `(8)`, gives `(14)`.

This also clarifies the sample-null term from `NB-292`. There the canonical defect has the orthogonal split

\[
b=s+z,
\qquad
z\in W\cap\ker L.
\]

By `(19)`, `Jz=z`, but because `g in U` and `z in W`,

\[
\boxed{\langle g,z\rangle=0.}
\tag{23}
\]

Therefore the already-sample-null part of the canonical dilation loss is target-silent for the direct multiplicative block enrichment. Immediate norm reduction comes from the sample-visible defect because neutralizing it creates an old-section component that can overlap the target source.

This sharpens, but does not contradict, `NB-292`: its `z` component can still matter in a different cutoff geometry. What it cannot do is by itself certify the gain from `S_mV_(n-1)` to `V_(mn-1)`.

---

## 5. Stress tests, prior art, and research disposition

The theorem does **not** produce a Nyman approximation rate. A large positive band can still miss the target. For example,

\[
A=I_2,
\qquad
\Gamma=\operatorname{diag}(\varepsilon,T^2),
\qquad
y=e_1
\]

gives from `(10)`

\[
\Delta
=
\frac{\varepsilon}{1+\varepsilon}.
\]

This can be arbitrarily small while the trace is arbitrarily large; choosing `T` large enough can also make the determinant arbitrarily large. Positive matrix mass is therefore not a substitute for target spectral mass.

The lower-section surjectivity assumption is essential to the clean form. Before that cutoff, `A` is singular and adding a band can enlarge the attainable sample range. The correct statement then needs Moore--Penrose inverses and explicit range compatibility. This finding deliberately works in the post-`NB-282` regime used by the finite-section analysis of `NB-284`--`NB-287`.

The abstract ingredients are classical: minimum-norm interpolation, orthogonal projection onto a kernel, block pseudoinverse geometry, and Woodbury. No novelty is claimed for those generic identities. A fresh prior-art search found the expected dilation-semigroup background in Bagchi, Ehm's Nyman Gram analysis, and Carvill's recent multiplicative-ladder Gram decay and block-compressibility. The surfaced literature does not provide this line-local null block `Q_(m,n,Z)`, its cocycle `(6)`, or the target/canonical-defect conversions `(8)` and `(14)`. No external theorem is load-bearing, so `SOURCES.md` requires no change.

The decisive moving-packet quantities after `NB-292` can now be stated without ambiguity. The exact multiplicative enrichment is measured by either

\[
\|P_{Q_{m_X,n_X,Z_X}}g_{m_X,n_X}(y_X)\|^2
\]

or

\[
x_X^*M_X(I+M_X)^{-1}x_X.
\]

A more source-specific sufficient route is the canonical pairing from `(14)`,

\[
|d_{m,n,Z}^*A^{-1}y|.
\]

If that pairing stays small at Ford scales, the new vector/matrix dilation geometry can remain target-silent even though it is inaccessible to the scalar graft of `NB-291`. If it is quantitatively nonzero after paying the denominator in `(14)`, it gives an immediate certified first-free synthesis decrement.

No local clue is resolved here. In particular, `CLUE-visible-semigroup-defect-controls-section-enrichment` concerns the original residual and its actual Nyman-distance decrement, whereas this finding prices the first-free quotient interpolation problem. Their structures are analogous but their targets are not interchangeable.

## Research disposition

Keep. `NB-292` isolated the first vector/matrix source-sample coupling but stopped before target conversion. `NB-293` supplies the exact conversion for the natural multiplicative quotient enrichment:

\[
\boxed{
W_{m,n,Z}
\xrightarrow{\;w\mapsto w-R_ULw\;}
Q_{m,n,Z},
\qquad
\Delta_{m,n,Z}(y)
=
\|P_{Q_{m,n,Z}}g_{m,n}(y)\|^2.
}
\]

The next useful theorem must therefore control target spectral mass in `(10)`, or the canonical pairing in `(14)`, under the moving Ford packet. Another lower bound on `Gamma`, `1-c^2`, or the sample-null charge separately would still miss the target alignment that actually prices section enrichment.