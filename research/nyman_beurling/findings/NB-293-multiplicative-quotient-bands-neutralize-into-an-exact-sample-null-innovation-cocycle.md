# NB-293 — multiplicative quotient bands neutralize into an exact sample-null innovation cocycle

- **Date:** 2026-09-22
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-282, NB-285, NB-287, NB-290, NB-292
- **Classification:** `EXACT-DERIVED + CANONICAL-NYMAN-SOURCE + FIRST-FREE-SAMPLING + DILATION-SEMIGROUP + MULTIPLICATIVE-QUOTIENT-BAND + BLOCK-NULL-INNOVATION + MINIMUM-NORM-INTERPOLATION + TARGET-AWARE-DECREMENT + POSITIVE-GRAM-WHITENING + CANONICAL-DEFECT-CERTIFICATE + RATE-NOT-CLAIMED + PRIOR-ART-AUDITED`

## Claim

`NB-292` identifies the multiplicative quotient band

\[
W_{m,n,Z}
=
V_{mn-1,Z}\ominus S_mV_{n-1,Z}
\]

and its positive first-free sampling Gram

\[
\Gamma_{m,n,Z}
=
K_{mn-1,Z}-D_Z(m)K_{n-1,Z}D_Z(m)^*.
\]

It also splits the normalized canonical dilation defect inside that band into a first-free-visible repair part and a sample-null part. The missing link is target-aware: which part of a whole multiplicative band actually lowers the minimum synthesis cost when the dilated old section is enlarged to the canonical section?

Once the lower section is first-free-surjective, the answer is exact. The whole quotient band neutralizes against the dilated old section into a canonical block of new interpolation-null directions, and the minimum-norm synthesis gain is precisely the squared projection of the old minimum source onto that block.

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

Assume `L|_(V_(n-1))` is onto, as it is beyond the finite surjective cutoff supplied by `NB-282`. Put

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

Since `D` is invertible and the lower section is onto, `A` is positive definite. Let

\[
R_U:=P_UL^*A^{-1}
=S_mR_{n-1}D^{-1}
\]

be the minimum-norm right inverse of `L|_U`. Define the **block neutralization map**

\[
\boxed{
J_{m,n,Z}:W\to V,
\qquad
Jw:=w-R_UBw.
}
\tag{1}
\]

Then `J` is a linear bijection from the full quotient band onto the new nullspace block

\[
\boxed{
Q_{m,n,Z}
:=
D_{mn-1}\ominus S_mD_{n-1}.
}
\tag{2}
\]

Equivalently,

\[
\boxed{
D_{mn-1}
=
S_mD_{n-1}
\oplus
Q_{m,n,Z}
}
\tag{3}
\]

orthogonally, and every band direction becomes an exact first-free-null direction after subtracting the unique minimum-norm old-section repair of its samples. Its induced null metric is

\[
\boxed{
J^*J
=
I_W+B^*A^{-1}B
\succeq I_W.
}
\tag{4}
\]

These multiplicative null blocks inherit their own exact semigroup cocycle. For `k,m,n>=2`, whenever the relevant lower sections are already first-free-surjective,

\[
\boxed{
Q_{km,n,Z}
=
Q_{k,mn,Z}
\oplus
S_kQ_{m,n,Z}
}
\tag{5}
\]

orthogonally.

The target consequence is also exact. For an arbitrary first-free datum `y in C^N`, let

\[
g_{m,n}(y)
:=R_Uy
=S_mR_{n-1}D^{-1}y
\]

be its minimum-norm realization in the dilated old section `U`, and let

\[
h_{mn-1}(y)
:=P_VL^*K_{mn-1}^{-1}y
\]

be its minimum-norm realization in the enlarged canonical section `V`. Then

\[
\boxed{
h_{mn-1}(y)
=
g_{m,n}(y)-P_{Q_{m,n,Z}}g_{m,n}(y).
}
\tag{6}
\]

Hence the complete multiplicative-section improvement is the block Parseval mass

\[
\boxed{
\Delta_{m,n,Z}(y)
:=
(D^{-1}y)^*K_{n-1}^{-1}(D^{-1}y)
-y^*K_{mn-1}^{-1}y
=
\|P_Qg_{m,n}(y)\|^2.
}
\tag{7}
\]

In finite-dimensional sample coordinates this same quantity is

\[
\boxed{
\Delta_{m,n,Z}(y)
=
y^*A^{-1}B
\bigl(I_W+B^*A^{-1}B\bigr)^{-1}
B^*A^{-1}y.
}
\tag{8}
\]

Writing

\[
M:=A^{-1/2}\Gamma A^{-1/2},
\qquad
x:=A^{-1/2}y,
\]

one obtains the equivalent target-spectral formula

\[
\boxed{
\Delta_{m,n,Z}(y)
=
x^*M(I+M)^{-1}x.
}
\tag{9}
\]

Thus the positive matrix cocycle of `NB-292` becomes coercive only through the spectral mass of the **actual transformed datum** in the generalized band modes. Large trace, determinant, operator norm, or scalar dilation loss by themselves still do not force a synthesis gain.

There is also a direct certificate from the normalized canonical innovation defect of `NB-292`. Recall

\[
b_{m,n,Z}
=S_m\psi_{n,Z}-c_{m,n}\psi_{mn,Z}\in W,
\qquad
\|b_{m,n,Z}\|^2=1-c_{m,n}^2,
\]

with sample defect

\[
d_{m,n,Z}=Lb_{m,n,Z}.
\]

Its block-neutralized form

\[
\widehat q_{m,n,Z}
:=Jb_{m,n,Z}
=b_{m,n,Z}-R_Ud_{m,n,Z}
\in Q_{m,n,Z}
\tag{10}
\]

has exact norm

\[
\boxed{
\|\widehat q_{m,n,Z}\|^2
=
1-c_{m,n}^2
+d_{m,n,Z}^*A^{-1}d_{m,n,Z}.
}
\tag{11}
\]

Since `g_(m,n)(y)` lies in `U` while `b_(m,n,Z)` lies in `W`, their only overlap after neutralization comes from the old-section repair. Therefore

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
\tag{12}
\]

whenever the denominator is nonzero; when the defect vanishes the right side is interpreted as zero.

This is the first direct target-aware section-enrichment certificate built from the vector defect exposed in `NB-292`. It still supplies no arithmetic lower bound on the numerator. The remaining question is now sharply localized: whether the actual moving Ford datum has non-negligible pairing with the old-section repair forced by the canonical dilation defect.

---

## 1. The dilated old kernel is exactly the old nullspace transported by the semigroup

The covariance from `NB-292` gives

\[
LS_m=DL.
\tag{13}
\]

Because `D` is diagonal with nonzero entries,

\[
LS_mh=0
\quad\Longleftrightarrow\quad
Lh=0.
\]

Therefore

\[
\boxed{
\ker(L|_U)
=S_mD_{n-1}.
}
\tag{14}
\]

Surjectivity of `L|_(V_(n-1))` and invertibility of `D` imply surjectivity on `U`. Its sampling Gram is

\[
LP_UL^*
=
DK_{n-1}D^*
=A\succ0.
\tag{15}
\]

For `x in C^N`, the vector

\[
S_mR_{n-1}D^{-1}x
\]

lies in `U`, has samples `x`, and has minimum norm because `S_m` is an isometry and `R_(n-1)` is the minimum-norm realization of `D^(-1)x` in `V_(n-1)`. Hence

\[
\boxed{
R_U
=S_mR_{n-1}D^{-1}
=P_UL^*A^{-1}.
}
\tag{16}
\]

In particular,

\[
R_U^*R_U=A^{-1}.
\tag{17}
\]

---

## 2. Every multiplicative band direction produces one new exact null direction

Take `w in W`. By definition `(1)`,

\[
LJw
=Bw-LR_UBw
=0,
\]

so `Jw in D_(mn-1)`. Moreover `w` is orthogonal to all of `U`, while `R_UBw` belongs to the orthogonal complement of `ker(L|_U)` inside `U`. Hence

\[
Jw\perp S_mD_{n-1}.
\]

Thus

\[
\operatorname{ran}J\subseteq Q_{m,n,Z}.
\tag{18}
\]

The map is injective: if `Jw=0`, then `w=R_UBw` lies simultaneously in `W` and `U`, so `w=0`.

For surjectivity, take `q in Q_(m,n,Z)` and split it uniquely as

\[
q=u+w,
\qquad
u\in U,
\quad
w\in W.
\tag{19}
\]

Since `Lq=0`,

\[
Lu=-Bw.
\tag{20}
\]

The condition `q perp S_mD_(n-1)` and `w perp U` imply

\[
u\perp\ker(L|_U).
\tag{21}
\]

Among vectors of `U` with samples `-Bw`, the unique one orthogonal to the kernel is the minimum-norm repair `-R_UBw`. Thus

\[
q=w-R_UBw=Jw.
\]

This proves that `J` maps `W` bijectively onto `Q`, and `(3)` follows.

Because the two terms in `Jw` belong to orthogonal spaces,

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
\langle Bw,A^{-1}Bt\rangle.
\end{aligned}
\tag{22}
\]

This is exactly `(4)`.

One consequence sharpens the visible/null split of `NB-292`. If `w in W cap ker L`, then `Bw=0` and

\[
\boxed{Jw=w.}
\tag{23}
\]

Thus the already-sample-null part of the quotient band embeds unchanged into the new kernel block. But it is also orthogonal to every old-section source in `U`. Such a direction, by itself, cannot lower the synthesis norm when passing from `U` to `V`. Target improvement appears only when a band direction has nonzero samples and its neutralization acquires the compensating old-section component `-R_UBw`.

This does **not** say that a sample-null band vector is globally irrelevant to every ordinary cutoff. It is a statement about the natural multiplicative enrichment `S_mV_(n-1) subset V_(mn-1)`. Relative to another, non-dilated starting section, the same vector can sit in a different part of the `NB-287` null-innovation filtration.

---

## 3. The null blocks satisfy the same multiplicative orthogonal geometry

The semigroup preserves first-free nullspaces by `(13)`. Therefore

\[
S_{km}D_{n-1}
\subseteq
S_kD_{mn-1}
\subseteq
D_{kmn-1}.
\tag{24}
\]

Split the orthogonal difference between the first and last spaces at the middle one:

\[
\begin{aligned}
D_{kmn-1}\ominus S_{km}D_{n-1}
&=
\bigl(D_{kmn-1}\ominus S_kD_{mn-1}\bigr)\\
&\quad\oplus
\bigl(S_kD_{mn-1}\ominus S_{km}D_{n-1}\bigr).
\end{aligned}
\tag{25}
\]

The first term is `Q_(k,mn,Z)`. Since `S_k` is an isometry and `S_(km)=S_kS_m`, the second is `S_kQ_(m,n,Z)`. This proves `(5)`.

Hence `NB-292` has two parallel multiplicative cocycles:

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

for the exact first-free-null freedom unlocked after those bands are neutralized against the old sample-surjective section.

The passage `W -> Q` is not isometric in general. Equation `(4)` records exactly the extra norm paid by the old-section sample repair. This metric distortion is target-relevant and is absent from a purely scalar pivot description.

---

## 4. Minimum-norm synthesis removes exactly the new null block

Let

\[
g:=g_{m,n}(y)=R_Uy.
\]

It is feasible in `U`, hence also feasible in `V`, and satisfies

\[
g\perp S_mD_{n-1}
\tag{26}
\]

by minimum-norm interpolation in `U`. Every feasible vector in `V` is in the affine space

\[
g+D_{mn-1}.
\]

Using `(3)` and `(26)`, minimizing its norm first kills the component in `S_mD_(n-1)` and then subtracts the orthogonal projection onto `Q`. Therefore

\[
h_{mn-1}(y)=g-P_Qg,
\]

proving `(6)`. Pythagoras gives

\[
\|g\|^2-
\|h_{mn-1}(y)\|^2
=
\|P_Qg\|^2.
\tag{27}
\]

The two norms are

\[
\|g\|^2
=y^*A^{-1}y
=(D^{-1}y)^*K_{n-1}^{-1}(D^{-1}y)
\tag{28}
\]

and

\[
\|h_{mn-1}(y)\|^2
=y^*K_{mn-1}^{-1}y.
\tag{29}
\]

This proves `(7)`.

Because `J` is injective with range `Q`, its orthogonal projector is

\[
P_Q
=
J(J^*J)^{-1}J^*.
\tag{30}
\]

For `g=R_Uy`, orthogonality of `U` and `W` gives

\[
J^*g
=-B^*R_U^*R_Uy
=-B^*A^{-1}y.
\tag{31}
\]

Substituting `(4)` and `(31)` into `(30)` proves `(8)`.

Since

\[
K_{mn-1}=A+\Gamma,
\qquad
\Gamma=BB^*,
\tag{32}
\]

Woodbury gives the equivalent identity

\[
\Delta_{m,n,Z}(y)
=y^*\bigl(A^{-1}-(A+\Gamma)^{-1}\bigr)y.
\tag{33}
\]

Whitening by `A^(1/2)` yields `(9)`. If `M` has eigenpairs `(lambda_j,e_j)` and

\[
x=\sum_jx_je_j,
\]

then

\[
\boxed{
\Delta_{m,n,Z}(y)
=
\sum_j
\frac{\lambda_j}{1+\lambda_j}|x_j|^2.
}
\tag{34}
\]

This is the exact target-alignment criterion for the band Gram. A large band can be irrelevant if its generalized eigenmodes miss the transformed datum.

There is also an exact target cocycle. Define `Delta_(m,n,Z)(y)` by `(7)`. Since `D_Z(km)=D_Z(k)D_Z(m)`, inserting the intermediate dilated section `S_kV_(mn-1)` gives

\[
\boxed{
\Delta_{km,n,Z}(y)
=
\Delta_{k,mn,Z}(y)
+
\Delta_{m,n,Z}\bigl(D_Z(k)^{-1}y\bigr).
}
\tag{35}
\]

The target transforms contravariantly along the inner factor. Therefore the matrix cocycle of `NB-292` cannot be turned into a fixed-datum scalar telescope without controlling this target transport.

---

## 5. The normalized canonical dilation defect gives one explicit target certificate

Apply the neutralization map to the canonical defect `b=b_(m,n,Z)` of `NB-292`. Its samples are `d=d_(m,n,Z)`, so

\[
\widehat q
=Jb
=b-R_Ud
\in Q.
\]

The two terms are orthogonal because `b in W` and `R_Ud in U`. Using `NB-292` and `(17)`,

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

which proves `(11)`.

For the old minimum source `g=R_Uy`,

\[
\langle g,b\rangle=0
\]

because `g in U` and `b in W`. Hence

\[
|\langle g,\widehat q\rangle|
=
|\langle R_Uy,R_Ud\rangle|
=
|d^*A^{-1}y|.
\tag{36}
\]

If `widehat q` is nonzero, normalize it and apply Bessel inside `Q`:

\[
\|P_Qg\|^2
\ge
\frac{|\langle g,\widehat q\rangle|^2}{\|\widehat q\|^2}.
\]

Together with `(7)`, `(11)`, and `(36)`, this is exactly `(12)`.

Now reconsider the `NB-292` orthogonal split

\[
b=s+z,
\qquad
z\in W\cap\ker L.
\]

The null component satisfies `Jz=z` by `(23)`, but

\[
\langle g,z\rangle=0.
\tag{37}
\]

Thus, for the natural multiplicative enrichment from `S_mV_(n-1)` to `V_(mn-1)`, the sample-null piece of the canonical dilation loss is **target-silent at first order**: it is already orthogonal to the old feasible minimum source. The component capable of producing an immediate norm decrement is the sample-visible defect, because cancelling its samples tilts the null direction back into the old section.

This sharpens the post-`NB-292` fork. The visible/null split remains an exact source fact, but at a sample-surjective multiplicative block endpoint only the visible part can couple directly to the old minimum interpolant. A future argument based on the `z` term must therefore use a different cutoff geometry, not the direct block enrichment priced in `(7)`.

---

## 6. Stress tests, prior art, and research disposition

The identities above still do not force a Nyman approximation rate. Even very large positive band Grams can miss the actual target. For the finite-dimensional control

\[
A=I_2,
\qquad
\Gamma=\operatorname{diag}(\varepsilon,T^2),
\qquad
y=e_1,
\]

formula `(9)` gives

\[
\Delta
=
\frac{\varepsilon}{1+\varepsilon}.
\]

This can be arbitrarily small while the trace is arbitrarily large; taking `T` sufficiently large can also make the determinant arbitrarily large. Thus positivity of `Gamma`, large band volume, or strong Gram growth is not a substitute for target spectral mass.

The surjectivity hypothesis is essential to the clean statement. Before the lower section is onto, `A` is singular and a band can also enlarge the attainable sample range. Then the correct formulation requires Moore--Penrose inverses together with explicit range compatibility. This finding deliberately stays beyond the finite surjective cutoff already proved in `NB-282`, which is the regime relevant to the first-free finite-section excess of `NB-284`--`NB-287`.

The generic Hilbert-space ingredients in `(1)`--`(9)` are standard minimum-norm interpolation, orthogonal-kernel projection, and block pseudoinverse/Woodbury algebra; no novelty is claimed for those abstract facts. A fresh prior-art search found the expected classical Nyman dilation-semigroup background in Bagchi, general Nyman Gram analysis in Ehm, and Carvill's recent multiplicative-ladder Gram decay and block-compressibility. The surfaced literature does not provide the line-local multiplicative null block `(2)`, its cocycle `(5)`, or the target projection/canonical-defect formulas `(7)` and `(12)`. No external theorem is load-bearing for the derivation, so `SOURCES.md` requires no change.

The main research consequence is a sharper target than the raw positive cocycle from `NB-292`. In a moving packet `(Z_X,n_X,m_X)`, the exact multiplicative enrichment is controlled by either of the equivalent target-aware quantities

\[
\|P_{Q_{m_X,n_X,Z_X}}g_{m_X,n_X}(y_X)\|^2
\]

or

\[
x_X^*M_X(I+M_X)^{-1}x_X.
\]

A source-native lower bound may be attacked through the explicit canonical direction `(12)`, namely the pairing

\[
|d_{m,n,Z}^*A^{-1}y|.
\]

If that pairing is small throughout the Ford regime, the new vector/matrix dilation structure can still remain target-silent despite being inaccessible to the scalar graft of `NB-291`. If it is quantitatively nonzero after paying the denominator in `(12)`, it gives an immediate certified first-free synthesis decrement across the corresponding multiplicative block.

No local clue is resolved by this finding. In particular, `CLUE-visible-semigroup-defect-controls-section-enrichment` concerns the original residual and its actual Nyman-distance decrement; the present result prices the different first-free quotient interpolation problem. The structural analogy is useful, but identifying the two would conflate distinct target geometries.

## Research disposition

Keep. `NB-292` isolated the first source/sample vector coupling but left both its visible and sample-null charges without a target conversion. The present result supplies that conversion for the natural multiplicative quotient enrichment:

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

The decisive next estimate is no longer a lower bound on `Gamma`, `1-c^2`, or the sample-null charge separately. It is a moving-packet bound on the target spectral mass in `(9)`, or more concretely on the canonical pairing in `(12)`, with the transported datum `D_Z(m)^(-1)y` and its conditioning paid explicitly.