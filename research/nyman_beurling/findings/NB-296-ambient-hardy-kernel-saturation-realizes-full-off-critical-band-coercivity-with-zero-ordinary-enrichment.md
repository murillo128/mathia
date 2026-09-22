# NB-296 — Ambient Hardy kernel saturation realizes full off-critical band coercivity with zero ordinary enrichment

- **Date:** 2026-09-23
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-001, NB-002, NB-284, NB-292, NB-293, NB-294, NB-295
- **Classification:** `EXACT-CONTROL + HARDY-RKHS + FIRST-FREE-SAMPLING + DILATION-SEMIGROUP + MULTIPLICATIVE-QUOTIENT-BAND + AMBIENT-KERNEL-SATURATION + DE-BRANGES-ROVNYAK-DEFECT + TARGET-AWARE-BASELINE-SEPARATION + ZERO-ORDINARY-ENRICHMENT + PRIOR-ART-AUDITED`

## Claim

`NB-294` and `NB-295` show that an off-critical packet forces strong sampling gain when one compares the dilated old section

\[
S_mV_{n-1,Z}
\]

with the canonical enlarged section

\[
V_{mn-1,Z}.
\]

Both findings explicitly warn that this is not yet a decrement from the ordinary undilated section `V_(n-1,Z)`. The present control shows that this warning is sharp in the strongest possible sense: **the complete off-critical band coercivity, including the exact log-volume growth from `NB-295` and the target-uniform saturation from `NB-294`, can occur while the ordinary sampling problem does not improve at all.**

The control lives in the same Hardy space and uses the same inner dilation semigroup and the same point-evaluation sampling map as the actual first-free quotient problem. What it omits is precisely the arithmetic Nyman source restriction.

Let

\[
\Omega=\{s:\Re s>1/2\},
\qquad
\mathcal H=H^2(\Omega),
\]

and fix distinct points

\[
Z=\{\rho_1,\ldots,\rho_N\}\subset\Omega.
\]

Write

\[
(L_Zf)_j=f(\rho_j),
\qquad
k_{\rho_j}(s)=\frac1{s+\overline{\rho_j}-1},
\]

and let

\[
E_Z:=\operatorname{span}\{k_{\rho_1},\ldots,k_{\rho_N}\}.
\]

Its evaluation Gram is the positive-definite Cauchy matrix

\[
G_Z:=L_ZL_Z^*
=
\left(\frac1{\rho_j+\overline{\rho_k}-1}\right)_{j,k=1}^N.
\tag{1}
\]

Use exactly the Bagchi/Nyman Hardy dilation

\[
(S_mf)(s)=m^{1/2-s}f(s),
\qquad
D_Z(m)=\operatorname{diag}
\bigl(m^{1/2-\rho_1},\ldots,m^{1/2-\rho_N}\bigr),
\tag{2}
\]

so that

\[
L_ZS_m=D_Z(m)L_Z.
\tag{3}
\]

Define the ambient semigroup-orbit sections

\[
\boxed{
\widetilde V_r(Z)
:=
\operatorname{span}\{S_qE_Z:1\le q\le r\}
\qquad(r\ge1).
}
\tag{4}
\]

Then, for every `r>=1`,

\[
\boxed{
\widetilde K_{r,Z}
:=
L_ZP_{\widetilde V_r(Z)}L_Z^*
=
G_Z.
}
\tag{5}
\]

Hence the ordinary minimum interpolation cost is independent of the cutoff:

\[
\boxed{
\widetilde{\mathcal C}_r(y)
=
y^*G_Z^{-1}y
\qquad
\text{for every }r\ge1,\ y\in\mathbb C^N.
}
\tag{6}
\]

In particular,

\[
\boxed{
\widetilde{\mathcal C}_{n-1}(y)
-
\widetilde{\mathcal C}_{mn-1}(y)
=0
}
\tag{7}
\]

for every admissible `m,n,y`: there is **zero ordinary finite-section synthesis gain**.

Nevertheless the multiplicative-band comparison used in `NB-292`--`NB-295` is fully active. Since

\[
S_m\widetilde V_{n-1}(Z)
\subseteq
\widetilde V_{mn-1}(Z),
\tag{8}
\]

the old dilated sampling Gram is

\[
\widetilde A_{m,n,Z}
=
D_Z(m)G_ZD_Z(m)^*,
\tag{9}
\]

while the enlarged Gram remains `G_Z`. Therefore the quotient-band Gram is

\[
\boxed{
\widetilde\Gamma_{m,n,Z}
=
G_Z-D_Z(m)G_ZD_Z(m)^*
\succeq0.
}
\tag{10}
\]

This control obeys the exact positive cocycle from `NB-292`:

\[
\boxed{
\widetilde\Gamma_{km,n,Z}
=
\widetilde\Gamma_{k,mn,Z}
+
D_Z(k)\widetilde\Gamma_{m,n,Z}D_Z(k)^*.
}
\tag{11}
\]

Let

\[
\widetilde M
=
\widetilde A^{-1/2}
\widetilde\Gamma
\widetilde A^{-1/2}.
\]

If

\[
H_Z
=
\sum_{j=1}^N
\left(\Re\rho_j-\frac12\right),
\]

then the determinant lower bound of `NB-295` is not merely compatible with zero ordinary enrichment; it is **saturated exactly**:

\[
\boxed{
\det(I+\widetilde M)
=
m^{2H_Z}.
}
\tag{12}
\]

For a fixed off-critical packet, put

\[
\delta_Z
=
\min_j\left(\Re\rho_j-\frac12\right)>0.
\]

The `NB-294` argument applies with lower Gram `G_Z`, giving

\[
\boxed{
\widetilde M
\succeq
\left(
\frac{m^{2\delta_Z}}{\kappa(G_Z)}-1
\right)_+I.
}
\tag{13}
\]

Consequently the relative gain from the **dilated** old section to the enlarged section tends to one uniformly for every nonzero datum:

\[
\boxed{
\inf_{y\ne0}
\frac{
 y^*\widetilde A^{-1}y-y^*G_Z^{-1}y
}{
 y^*\widetilde A^{-1}y
}
\longrightarrow1
\qquad(m\to\infty),
}
\tag{14}
\]

while `(7)` remains identically zero.

Thus the raw off-critical coercivity isolated in `NB-294`--`NB-295` is not, by itself, a source-arithmetic enrichment signal. It can be exhausted entirely by **repairing the loss introduced by dilation relative to an already-saturated evaluation space**.

---

## 1. Why every ambient orbit section has the same sampling Gram

The adjoint of point evaluation satisfies

\[
L_Z^*e_j=k_{\rho_j}.
\]

Therefore

\[
\operatorname{ran}L_Z^*=E_Z.
\tag{15}
\]

Because `S_1=I`, every section in `(4)` contains `E_Z`. Hence

\[
P_{\widetilde V_r}L_Z^*=L_Z^*,
\]

which immediately gives

\[
L_ZP_{\widetilde V_r}L_Z^*
=L_ZL_Z^*
=G_Z.
\]

This proves `(5)`.

There is a useful geometric reformulation. Since

\[
E_Z=(\ker L_Z)^\perp,
\]

inside every finite orbit section one has the orthogonal split

\[
\boxed{
\widetilde V_r(Z)
=
E_Z
\oplus
\bigl(\widetilde V_r(Z)\cap\ker L_Z\bigr).
}
\tag{16}
\]

All source directions added after `E_Z` are therefore interpolation-null after their `E_Z` component is removed. They enlarge the source space but cannot lower the minimum norm needed to realize a fixed sample vector below the ambient Hardy minimum `y^*G_Z^(-1)y`.

This is exactly why the ordinary cutoff cost in `(6)` is frozen.

---

## 2. The same sections preserve the exact multiplicative geometry

The Hardy multiplier in `(2)` is inner on the boundary `Re s=1/2`, so each `S_m` is an isometry and

\[
S_kS_m=S_{km}.
\tag{17}
\]

For `q<=n-1`,

\[
mq\le m(n-1)\le mn-1.
\]

Thus every generator `S_(mq)E_Z` of `S_m\widetilde V_(n-1)` already belongs to `\widetilde V_(mn-1)`, proving `(8)`.

Let

\[
\widetilde U=S_m\widetilde V_{n-1}.
\]

Since `S_m` is an isometry,

\[
P_{\widetilde U}
=S_mP_{\widetilde V_{n-1}}S_m^*.
\]

Using `(3)` and its adjoint,

\[
\begin{aligned}
L_ZP_{\widetilde U}L_Z^*
&=
L_ZS_mP_{\widetilde V_{n-1}}S_m^*L_Z^*\\
&=
D_Z(m)
\widetilde K_{n-1,Z}
D_Z(m)^*\\
&=
D_Z(m)G_ZD_Z(m)^*,
\end{aligned}
\]

which proves `(9)`.

Because `\widetilde U subseteq \widetilde V_(mn-1)`, the orthogonal quotient band has sampling Gram equal to the difference of the two projection Grams. Together with `(5)` this gives `(10)` and its positivity.

The cocycle `(11)` is then exact algebra. Since

\[
D_Z(km)=D_Z(k)D_Z(m),
\]

we have

\[
\begin{aligned}
&\widetilde\Gamma_{k,mn,Z}
+D_Z(k)\widetilde\Gamma_{m,n,Z}D_Z(k)^*\\
&=G_Z-D_Z(k)G_ZD_Z(k)^*\\
&\quad+D_Z(k)
\bigl(G_Z-D_Z(m)G_ZD_Z(m)^*\bigr)
D_Z(k)^*\\
&=G_Z-D_Z(km)G_ZD_Z(km)^*\\
&=\widetilde\Gamma_{km,n,Z}.
\end{aligned}
\]

So the control does not break the vector/matrix semigroup structure introduced specifically to escape the scalar lethargy controls of `NB-288`--`NB-291`.

---

## 3. The forced log volume is exactly the dilation Jacobian

For this control the enlarged sampling Gram is `G_Z`, so

\[
I+\widetilde M
=
\widetilde A^{-1/2}G_Z\widetilde A^{-1/2}.
\]

Therefore

\[
\det(I+\widetilde M)
=
\frac{\det G_Z}
{\det(D_Z(m)G_ZD_Z(m)^*)}.
\]

Now

\[
|\det D_Z(m)|^2
=
m^{-2H_Z},
\]

and `(12)` follows.

This identifies the sharp baseline hidden in the factorization of `NB-295`. There the exact identity is

\[
\det(I+M)
=
m^{2H_Z}
\frac{\det K_{mn-1,Z}}
{\det K_{n-1,Z}}.
\tag{18}
\]

The present control has

\[
\frac{\det\widetilde K_{mn-1,Z}}
{\det\widetilde K_{n-1,Z}}
=1,
\tag{19}
\]

while retaining the entire compulsory factor `m^(2H_Z)`. Hence **all conditioning-free log-volume pressure proved in `NB-295` can, in principle, be accounted for by the dilation baseline alone.** Any log-volume argument aimed at ordinary section enrichment has to control the residual ratio in `(18)`, not merely the forced `m^(2H_Z)` factor.

The target-wise version is equally explicit. Define the ordinary same-datum decrement

\[
\Delta_{\mathrm{ord}}(y)
:=
y^*K_{n-1,Z}^{-1}y
-
y^*K_{mn-1,Z}^{-1}y.
\tag{20}
\]

The multiplicative-band decrement from `NB-293` is

\[
\Delta_{\mathrm{dil}}(y)
:=
y^*A^{-1}y
-
y^*K_{mn-1,Z}^{-1}y.
\tag{21}
\]

They satisfy the exact bookkeeping identity

\[
\boxed{
\Delta_{\mathrm{ord}}(y)
=
\Delta_{\mathrm{dil}}(y)
-
\left(
 y^*A^{-1}y-y^*K_{n-1,Z}^{-1}y
\right).
}
\tag{22}
\]

The bracket is the cost change created before enrichment, solely by replacing the old section with its dilated copy. In the ambient control it is nonnegative, diverges relative to the fixed ambient cost for fixed off-critical `Z`, and exactly exhausts `\Delta_dil`; thus `\Delta_ord=0`.

Equation `(22)` is only an algebraic identity in the actual Nyman problem — its bracket need not have a fixed sign there. The control shows why a lower bound on `\Delta_dil` cannot be transferred to `\Delta_ord` unless that dilation term is separately controlled.

---

## 4. Scalar audit: complete coercivity with literally no enrichment

The one-point case removes every matrix-conditioning distraction. Normalize the single Hardy kernel so that

\[
G_Z=1,
\qquad
\rho=\frac12+\delta+i\gamma,
\qquad
\delta>0.
\]

Then

\[
A=m^{-2\delta},
\qquad
\Gamma=1-m^{-2\delta},
\qquad
M=m^{2\delta}-1.
\]

For any nonzero scalar datum `y`,

\[
\frac{\Delta_{\mathrm{dil}}(y)}{\mathcal C_U(y)}
=1-m^{-2\delta}
\longrightarrow1.
\tag{23}
\]

At the same time

\[
\Delta_{\mathrm{ord}}(y)=0
\tag{24}
\]

for every `m`. Thus neither bad conditioning, spectral concentration, nor target misalignment is needed to separate the two notions of gain. The baseline distinction alone is sufficient.

This is also a useful adversarial check on the critical boundary. Formally setting `delta=0` removes the modulus contraction, gives `A=G` in the one-point case, and eliminates the forced gain, exactly as in `NB-294`.

---

## 5. What this control does and does not refute

The control is **not** a model of the arithmetic Nyman quotient sections. Its section generators are ambient reproducing-kernel orbits, not the Blaschke-deflated Dirichlet atoms `H_(j,Z)`. Therefore it does not show that the actual ordinary increment

\[
K_{mn-1,Z}-K_{n-1,Z}
\]

is small, nor that the genuine finite-section excess from `NB-284`--`NB-287` has slow decay.

What it does show is sharper and properly scoped: the following ingredients, even taken together, do not force ordinary finite-section improvement:

- the actual Hardy inner dilation `S_m`;
- exact sample covariance `L_ZS_m=D_Z(m)L_Z`;
- nested multiplicative orbit sections;
- the positive quotient-band identity `Gamma=K^+-DKD^*`;
- the exact matrix cocycle of `NB-292`;
- the fixed-packet all-target coercivity mechanism of `NB-294`;
- the full conditioning-free determinant pressure of `NB-295`.

All of them hold in the control while `(7)` says that ordinary sampling improvement is identically zero.

Therefore the next bridge cannot be another estimate that depends only on the raw whitened band `M`, its determinant, its eigenvalues, or its target occupation relative to the **dilated** baseline. It must use a source-specific fact that distinguishes the actual Nyman sections from ambient kernel saturation and survives the subtraction in `(22)`.

Two equivalent targets are now cleanly separated:

\[
\boxed{
K_{mn-1,Z}-K_{n-1,Z}
}
\tag{25}
\]

at the matrix level, or

\[
\boxed{
\Delta_{\mathrm{ord}}(y_Z)
=
y_Z^*\left(
K_{n-1,Z}^{-1}-K_{mn-1,Z}^{-1}
\right)y_Z
}
\tag{26}
\]

for the actual first-free Ford datum. Any successful continuation of the multiplicative-band route must prove a quantitative lower bound for `(25)` in a target-relevant direction, or for `(26)` directly, using arithmetic source geometry not present in the ambient control.

This sharpens the accepted `CLUE-visible-semigroup-defect-controls-section-enrichment.md`: visibility relative to a shifted/dilated trial family is not enough unless the resulting decrement is compared with the undilated old section. It also preserves the `CLUE-target-aware-finite-section-certificate.md` requirement that the target pairing and the actual finite-section geometry remain coupled.

---

## 6. Prior-art audit and evidence boundary

The Hardy semigroup input is classical and is already anchored in `SOURCES.md` through Bagchi (2006): multiplication by `m^(1/2-s)` is an inner isometry and supplies the Nyman dilation covariance. The identity

\[
G_Z-D_Z(m)G_ZD_Z(m)^*\succeq0
\]

is also the finite Pick matrix of the standard de Branges--Rovnyak kernel associated with the contractive/inner multiplier `m^(1/2-s)`. A fresh literature search found the expected general de Branges--Rovnyak kernel theory and no need for a new load-bearing source: in this finding positivity follows directly from the explicit subspace inclusion and projection-Gram calculation above.

No novelty is claimed for reproducing kernels, de Branges--Rovnyak positivity, or the Hardy semigroup itself. The line-local contribution is the matched control against the specific `NB-292`--`NB-295` multiplicative-band mechanism: **the recent off-critical coercivity theorems can be saturated inside ambient Hardy sampling while the ordinary same-datum section decrement is exactly zero.**

A direct numerical audit on a three-point off-critical packet independently verified positivity of `G_Z-DG_ZD^*` and the determinant identity `(12)` to floating-point precision. That computation is not needed for the proof.

No new external theorem is load-bearing, so `SOURCES.md` is unchanged. The result does not prove or disprove RH, does not estimate the actual Nyman Gram increment `(25)`, and does not consume either accepted clue named above.

## Research disposition

This is a negative structural result, but it changes the immediate frontier. `NB-294` removed target occupation above a fixed-packet coercivity gate, and `NB-295` removed conditioning from the existence of strong band modes. `NB-296` shows that **even perfect occupation of those modes can still be entirely a dilation-repair effect**.

The remaining quantitative question is therefore no longer whether the multiplicative band is strong relative to `S_mV_(n-1,Z)`. It is whether the actual arithmetic Nyman enlargement is strong relative to `V_(n-1,Z)` after the universal Hardy dilation baseline has been subtracted. The source-native observable is `(25)`, and the target-aware observable is `(26)`.