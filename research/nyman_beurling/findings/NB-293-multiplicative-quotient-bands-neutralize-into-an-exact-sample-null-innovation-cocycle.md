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

Once the lower quotient section is first-free-surjective, this band has an exact target-aware interpretation: **every band direction can be neutralized by its old-section sample repair to produce a new first-free-null direction, and the minimum synthesis gain is exactly the projection onto the resulting null block.**

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

Assume `L|_(V_(n-1))` is onto, as it is beyond the finite cutoff from `NB-282`. Set

\[
U:=S_mV_{n-1},
\qquad
V:=V_{mn-1},
\qquad
W:=V\ominus U,
\]

and

\[
D:=D_Z(m),
\qquad
A:=LP_UL^*=DK_{n-1}D^*,
\qquad
B:=L|_W,
\qquad
\Gamma:=BB^*.
\]

Then `A` is positive definite and the minimum-norm right inverse on `U` is

\[
R_U=P_UL^*A^{-1}=S_mR_{n-1}D^{-1}.
\tag{1}
\]

Define the block neutralization map

\[
\boxed{
J_{m,n,Z}:W\to V,
\qquad
Jw=w-R_UBw.
}
\tag{2}
\]

Then `J` is a linear bijection from `W` onto

\[
\boxed{
Q_{m,n,Z}
:=
D_{mn-1}\ominus S_mD_{n-1}.
}
\tag{3}
\]

Equivalently,

\[
\boxed{
D_{mn-1}=S_mD_{n-1}\oplus Q_{m,n,Z}
}
\tag{4}
\]

orthogonally. The induced metric is

\[
\boxed{
J^*J=I_W+B^*A^{-1}B\succeq I_W.
}
\tag{5}
\]

The new null blocks inherit the same multiplicative orthogonal geometry:

\[
\boxed{
Q_{km,n,Z}
=
Q_{k,mn,Z}\oplus S_kQ_{m,n,Z}.
}
\tag{6}
\]

For any first-free datum `y in C^N`, let

\[
g_{m,n}(y):=R_Uy=S_mR_{n-1}D^{-1}y
\]

be its minimum-norm realization in `U`, and let

\[
h_{mn-1}(y):=P_VL^*K_{mn-1}^{-1}y
\]

be its minimum-norm realization in `V`. Then

\[
\boxed{
h_{mn-1}(y)
=
g_{m,n}(y)-P_{Q_{m,n,Z}}g_{m,n}(y).
}
\tag{7}
\]

Hence the whole multiplicative-section improvement is

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

The same quantity has the finite-dimensional forms

\[
\boxed{
\Delta_{m,n,Z}(y)
=
y^*A^{-1}B
\bigl(I_W+B^*A^{-1}B\bigr)^{-1}
B^*A^{-1}y
}
\tag{9}
\]

and, with

\[
M:=A^{-1/2}\Gamma A^{-1/2},
\qquad
x:=A^{-1/2}y,
\]

\[
\boxed{
\Delta_{m,n,Z}(y)=x^*M(I+M)^{-1}x.
}
\tag{10}
\]

If `M e_j=lambda_j e_j` and `x=sum_j x_j e_j`, then

\[
\boxed{
\Delta_{m,n,Z}(y)
=
\sum_j\frac{\lambda_j}{1+\lambda_j}|x_j|^2.
}
\tag{11}
\]

Thus the positive matrix cocycle from `NB-292` becomes coercive only through spectral mass of the **actual transformed datum**. Large trace, determinant, operator norm, or scalar dilation loss by themselves do not force a target gain.

There is also a direct certificate from the normalized canonical innovation defect of `NB-292`. Let

\[
b_{m,n,Z}
=S_m\psi_{n,Z}-c_{m,n}\psi_{mn,Z}\in W,
\qquad
\|b_{m,n,Z}\|^2=1-c_{m,n}^2,
\]

and

\[
d_{m,n,Z}=Lb_{m,n,Z}.
\]

Its neutralized direction

\[
\widehat q_{m,n,Z}
:=Jb_{m,n,Z}
=b_{m,n,Z}-R_Ud_{m,n,Z}
\in Q_{m,n,Z}
\tag{12}
\]

has norm

\[
\boxed{
\|\widehat q_{m,n,Z}\|^2
=
1-c_{m,n}^2+d_{m,n,Z}^*A^{-1}d_{m,n,Z}.
}
\tag{13}
\]

Therefore

\[
\boxed{
\Delta_{m,n,Z}(y)
\ge
\frac{|d_{m,n,Z}^*A^{-1}y|^2}
{1-c_{m,n}^2+d_{m,n,Z}^*A^{-1}d_{m,n,Z}}
}
\tag{14}
\]

whenever the denominator is nonzero, with the right side interpreted as zero when the defect vanishes.

Equation `(14)` isolates the remaining arithmetic task: control the target pairing `d^*A^(-1)y` in the moving Ford regime while paying the repair cost in the denominator.

---

## 1. Why the quotient band is exactly a new null block

The covariance from `NB-292` is

\[
LS_m=DL.
\tag{15}
\]

Since `D` is invertible,

\[
\ker(L|_U)=S_mD_{n-1}.
\tag{16}
\]

Surjectivity of the lower section passes to `U`, and `(1)` follows from the isometry of `S_m`: realizing samples `x` in `U` is equivalent to realizing `D^{-1}x` in `V_(n-1)`.

For `w in W`, equation `(2)` gives

\[
LJw=Bw-LR_UBw=0.
\]

Also `w` is orthogonal to `U`, while `R_UBw` is orthogonal to `ker(L|_U)` inside `U`. Hence `Jw` belongs to `Q_(m,n,Z)`.

The map is injective because `Jw=0` would force the same vector to lie in the orthogonal spaces `W` and `U`.

For surjectivity, take `q in Q_(m,n,Z)` and write its unique orthogonal decomposition as `q=u+w`, with `u` in `U` and `w` in `W`. Since `Lq=0`,

\[
Lu=-Bw.
\tag{17}
\]

Because `q` is orthogonal to `S_mD_(n-1)` and `w` is orthogonal to `U`, the vector `u` is orthogonal to `ker(L|_U)`. It is therefore the unique minimum-norm realization in `U` of the samples `-Bw`, namely

\[
u=-R_UBw.
\tag{18}
\]

Thus `q=Jw`, proving the bijection and `(4)`.

For `w,t in W`, the `W` and `U` components of `Jw` and `Jt` are orthogonal. Since `R_U^*R_U=A^{-1}`,

\[
\langle Jw,Jt\rangle
=
\langle w,t\rangle
+
\langle Bw,A^{-1}Bt\rangle,
\]

which proves `(5)`.

If `w in W cap ker L`, then `Bw=0`, so

\[
\boxed{Jw=w.}
\tag{19}
\]

Therefore an already-sample-null band direction embeds unchanged into the new kernel block. But it remains orthogonal to every source in `U`, so it cannot by itself lower the minimum synthesis norm in the direct enrichment `U subset V`. Immediate target gain requires a band direction whose nonzero samples force a compensating old-section repair.

This is a statement about this multiplicative block only. Relative to a different, non-dilated cutoff, the same sample-null vector can occupy a different part of the `NB-287` null-innovation filtration.

---

## 2. The null blocks form a multiplicative cocycle

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
D_{kmn-1}\ominus S_{km}D_{n-1}
=
\bigl(D_{kmn-1}\ominus S_kD_{mn-1}\bigr)
\oplus
\bigl(S_kD_{mn-1}\ominus S_{km}D_{n-1}\bigr).
\]

The first summand is `Q_(k,mn,Z)` and the second is `S_kQ_(m,n,Z)`, proving `(6)`.

So `NB-292` now has parallel multiplicative structures: its source bands `W_(m,n,Z)` and the exact null blocks `Q_(m,n,Z)` obtained after sample neutralization. The map `J` is generally not isometric; `(5)` is the exact repair-induced metric distortion.

---

## 3. Minimum-norm synthesis removes exactly the new null block

The old minimum source `g=R_Uy` is feasible in `V` and orthogonal to `S_mD_(n-1)`. Every feasible vector in `V` lies in the affine space

\[
g+D_{mn-1}.
\]

Using `(4)`, the only new kernel component that can lower its norm is `Q`. Orthogonal projection gives `(7)`, and Pythagoras gives

\[
\|g\|^2-
\|h_{mn-1}(y)\|^2
=
\|P_Qg\|^2.
\]

Since

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

this proves `(8)`.

Because `J` is injective with range `Q`,

\[
P_Q=J(J^*J)^{-1}J^*.
\]

For `g=R_Uy`, orthogonality of `U` and `W` gives

\[
J^*g=-B^*A^{-1}y.
\]

Together with `(5)`, this proves `(9)`. Since

\[
K_{mn-1}=A+\Gamma,
\qquad
\Gamma=BB^*,
\]

Woodbury gives the equivalent identity

\[
\Delta_{m,n,Z}(y)
=y^*\bigl(A^{-1}-(A+\Gamma)^{-1}\bigr)y,
\tag{20}
\]

and whitening proves `(10)`--`(11)`.

The target gain also obeys an exact multiplicative chain rule. Define `Delta_(m,n,Z)(y)` by `(8)`. Since `D_Z(km)=D_Z(k)D_Z(m)`, inserting the intermediate section `S_kV_(mn-1)` gives

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

Thus multiplicative gains telescope only after the datum is transported contravariantly. A fixed-datum argument cannot omit that transformation.

---

## 4. The canonical defect gives one explicit target direction

Apply `J` to `b=b_(m,n,Z)`. Its samples are `d=d_(m,n,Z)`, so `(12)` is immediate. Since `b` lies in `W` and `R_Ud` lies in `U`,

\[
\|\widehat q\|^2
=
\|b\|^2+
\|R_Ud\|^2
=
1-c_{m,n}^2+d^*A^{-1}d,
\]

proving `(13)`.

For `g=R_Uy`, we have `g perp b`. Hence

\[
|\langle g,\widehat q\rangle|
=
|\langle R_Uy,R_Ud\rangle|
=
|d^*A^{-1}y|.
\tag{22}
\]

Normalize `widehat q`, apply Bessel inside `Q`, and use `(8)`. This gives `(14)`.

Now reconsider the `NB-292` split

\[
b=s+z,
\qquad
z\in W\cap\ker L.
\]

By `(19)`, `Jz=z`, but `g` lies in `U` while `z` lies in `W`, so

\[
\boxed{\langle g,z\rangle=0.}
\tag{23}
\]

Thus the already-sample-null part of the canonical dilation loss is target-silent for this direct multiplicative enrichment. The sample-visible defect is the component that can generate an immediate decrement because its neutralization creates an old-section component that overlaps the target source.

This sharpens rather than contradicts `NB-292`: the `z` term can still matter under another cutoff geometry, but it does not by itself certify the gain from `S_mV_(n-1)` to `V_(mn-1)`.

---

## 5. Stress tests, prior art, and research disposition

The theorem does **not** imply a Nyman approximation rate. A large positive band can miss the target. For example,

\[
A=I_2,
\qquad
\Gamma=\operatorname{diag}(\varepsilon,T^2),
\qquad
y=e_1
\]

gives

\[
\Delta=\frac{\varepsilon}{1+\varepsilon}.
\]

This can be arbitrarily small while the trace is arbitrarily large; choosing `T` large enough also makes the determinant arbitrarily large. Positive band mass is therefore not a substitute for target spectral mass.

The lower-section surjectivity hypothesis is essential to the clean form. Before that cutoff, `A` is singular and adding a band can enlarge the attainable sample range. The correct formulation then needs Moore--Penrose inverses plus explicit range compatibility. This finding deliberately stays in the post-`NB-282` regime used by `NB-284`--`NB-287`.

The abstract ingredients are classical minimum-norm interpolation, orthogonal projection onto a kernel, block pseudoinverse geometry, and Woodbury. No novelty is claimed for those generic identities. A fresh prior-art search found the expected dilation-semigroup background in Bagchi, Ehm's Nyman Gram analysis, and Carvill's recent multiplicative-ladder Gram decay and block-compressibility. The surfaced literature does not provide this line-local null block `Q_(m,n,Z)`, its cocycle `(6)`, or the target/canonical-defect conversions `(8)` and `(14)`. No external theorem is load-bearing, so `SOURCES.md` requires no change.

The next moving-packet target is now explicit. The exact multiplicative enrichment is measured by either

\[
\|P_{Q_{m_X,n_X,Z_X}}g_{m_X,n_X}(y_X)\|^2
\]

or

\[
x_X^*M_X(I+M_X)^{-1}x_X.
\]

A more source-specific sufficient route is the canonical pairing

\[
|d_{m,n,Z}^*A^{-1}y|.
\]

If this remains small at Ford scales, the vector/matrix dilation geometry can still be target-silent despite being inaccessible to the scalar graft of `NB-291`. If it stays quantitatively nonzero after the denominator in `(14)` is paid, it gives an immediate certified first-free synthesis decrement.

No local clue is resolved here. In particular, `CLUE-visible-semigroup-defect-controls-section-enrichment` concerns the original residual and its actual Nyman-distance decrement, while the present finding prices the first-free quotient interpolation problem. The analogy is structural, not an identification of targets.

## Research disposition

Keep. `NB-292` isolated the first vector/matrix source-sample coupling but stopped before target conversion. `NB-293` supplies that conversion for the natural multiplicative quotient enrichment:

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

The next useful theorem must control target spectral mass in `(10)`, or the canonical pairing in `(14)`, under the moving Ford packet. Another lower bound on `Gamma`, `1-c^2`, or the sample-null charge separately would still miss the target alignment that actually prices section enrichment.