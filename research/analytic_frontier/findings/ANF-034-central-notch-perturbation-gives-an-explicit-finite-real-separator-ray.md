# ANF-034 — a central-notch perturbation gives an explicit finite-real separator ray

**Status:** `EXACT-DERIVED + CONSTRUCTIVE-SEPARATION + FINITE-REAL-SCALAR + SHARP-FACE-PERTURBATION + STRUCTURAL-BOUNDARY`. `ANF-033` proves that the Montgomery--Taylor budget is disjoint from the weak-* finite-diffraction closure and therefore that some positive support-one spectrum beats the Montgomery--Taylor ratio on **all** finite real configurations. Its final separator, however, is obtained abstractly by convex separation. The proof of `ANF-033` contains enough quantitative slack to do better: a separator can be chosen on a concrete one-parameter ray obtained by cutting a small central notch out of the exact Montgomery--Taylor spectrum.

Let `J_MT` and `R_MT=widehat J_MT` be the exact extremizer of `ANF-030`, and let

\[
\nu_{\rm MT}
=a_{\rm MT}\delta_0+a_{\rm MT}|\alpha|\,d\alpha,
\qquad
\int J_{\rm MT}\,d\nu_{\rm MT}=1.
\]

Then there exist an even continuous tent `phi>=0`, compactly supported in an arbitrarily small interval around the origin and satisfying

\[
0\le \phi\le J_{\rm MT},
\]

and a number `s in (0,1)` such that

\[
\boxed{
J_s:=J_{\rm MT}-s\phi\ge0
}
\tag{1}
\]

is supported in `[-1,1]` and satisfies the **uniform** finite-real separation

\[
\boxed{
\inf_X\left(
\int J_s\,d\mu_X-
\int J_s\,d\nu_{\rm MT}
\right)>0,
}
\tag{2}
\]

where `X` ranges over all nonempty finite sets of distinct real points and `mu_X` is the normalized diffraction measure of `ANF-020`. Equivalently,

\[
\boxed{
q_{\rm real}(J_s)
>
\frac{C(J_s)}{C_{\rm MT}},
\qquad
\frac{C(J_s)}{q_{\rm real}(J_s)}<C_{\rm MT}.
}
\tag{3}
\]

Thus the existential separator of `ANF-033` need not be an arbitrary Hahn--Banach profile. It can be taken **arbitrarily close to the Montgomery--Taylor extremizer in the explicit direction `-phi`**, with the perturbation supported only near zero frequency.

## 1. A central tent stays inside the sharp spectrum

`ANF-030` proves that `J_MT` is continuous and strictly positive on `(-1,1)`. Fix any sufficiently small

\[
0<\eta<1
\]

and put

\[
b_\eta
:=
\min\left\{
1,
\min_{|\alpha|\le\eta}J_{\rm MT}(\alpha)
\right\}>0.
\tag{4}
\]

Define the even tent

\[
\boxed{
\phi_\eta(\alpha)
:=
b_\eta\left(1-\frac{|\alpha|}{\eta}\right)_+.
}
\tag{5}
\]

Then

\[
0\le\phi_\eta\le1,
\qquad
0\le\phi_\eta\le J_{\rm MT},
\qquad
\operatorname{supp}\phi_\eta\subset[-\eta,\eta].
\tag{6}
\]

Its exact Montgomery--Taylor budget is

\[
\begin{aligned}
p_\nu
&:=\int\phi_\eta\,d\nu_{\rm MT}\\
&=a_{\rm MT}b_\eta
+a_{\rm MT}\int_{-\eta}^{\eta}
|\alpha|b_\eta\left(1-\frac{|\alpha|}{\eta}\right)d\alpha\\
&=\boxed{
a_{\rm MT}b_\eta\left(1+\frac{\eta^2}{3}\right).
}
\end{aligned}
\tag{7}
\]

In particular

\[
p_\nu\ge a_{\rm MT}b_\eta>0.
\tag{8}
\]

For every `0<s<1`, (6) immediately gives `J_MT-s phi_eta>=0`, so positivity of the perturbed spectrum costs no further analytic argument.

## 2. Near the sharp face, finite configurations have too little central mass

For a finite real configuration `X`, retain the exact nonnegative sharp excess from `ANF-032`--`ANF-033`,

\[
\Delta(X)
:=
\int J_{\rm MT}\,d\mu_X-1
\ge0.
\tag{9}
\]

Fix a physical scale `L>0`. `ANF-032` supplies

\[
\kappa_L>0
\]

and a subset `Y subseteq X` obtained by deleting a fraction

\[
\varepsilon(X)
:=\frac{|X\setminus Y|}{|X|}
\le\frac{2\Delta(X)}{\kappa_L},
\tag{10}
\]

such that every interval of length `<L/2` contains at most two points of `Y`.

The Fejer-majorant estimate in `ANF-033`, applied to the tent (5), gives for the survivor, with the original `|X|` normalization,

\[
\boxed{
\int\phi_\eta\,d\widetilde\mu_Y
\le
b_\eta B_{\eta,L},
\qquad
B_{\eta,L}
:=
\frac4{c_0}\left(\eta+\frac4L\right),
}
\tag{11}
\]

where

\[
c_0
=\int_{-1}^{1}
\left(\frac{\sin\pi u}{\pi u}\right)^2du>0.
\]

Since `B_{eta,L}->0` by first taking `eta->0` and then `L->infinity`, choose `eta,L` so that

\[
\boxed{B_{\eta,L}<a_{\rm MT}.}
\tag{12}
\]

Define the fixed positive central-mass gap

\[
G
:=p_\nu-b_\eta B_{\eta,L}
>0.
\tag{13}
\]

`ANF-033` also controls the spectral cost of the deleted points. Because `phi_eta<=J_MT`, its equation (15) may be used with constant `C_phi=1`. Combining it with (10), if

\[
r_L:=\frac2{\kappa_L},
\]

then

\[
\left|
\int\phi_\eta\,d\mu_X
-
\int\phi_\eta\,d\widetilde\mu_Y
\right|
\le
E_L(\Delta(X)),
\tag{14}
\]

where one may take

\[
E_L(t)
:=
2\sqrt{(1+t)(1+r_L)t}
+(1+r_L)t.
\tag{15}
\]

The only property needed below is the exact one

\[
E_L(t)\longrightarrow0
\qquad(t\downarrow0).
\tag{16}
\]

Choose `delta>0` so small that

\[
E_L(\delta)\le\frac G2.
\tag{17}
\]

Then every configuration with `Delta(X)<=delta` satisfies, by (11)--(17),

\[
\boxed{
\int\phi_\eta\,d\mu_X
\le p_\nu-\frac G2.
}
\tag{18}
\]

Thus the sharp `J_MT` face has a definite one-sided defect in the central tent direction: configurations that are nearly optimal for `J_MT` necessarily carry **strictly less** `phi_eta` mass than the Montgomery--Taylor budget.

## 3. Configurations away from the sharp face are paid for by their existing excess

The preceding estimate handles small `Delta`. For arbitrary `X`, (6) and (9) give the crude but exact inequality

\[
\boxed{
\int\phi_\eta\,d\mu_X
\le
\int J_{\rm MT}\,d\mu_X
=1+\Delta(X).
}
\tag{19}
\]

Now set

\[
D_s(X)
:=
\int J_s\,d\mu_X
-
\int J_s\,d\nu_{\rm MT}.
\tag{20}
\]

Using the exact calibration of `J_MT`,

\[
D_s(X)
=
\Delta(X)
-s\left(
\int\phi_\eta\,d\mu_X-p_\nu
\right).
\tag{21}
\]

If `Delta(X)<=delta`, (18) gives

\[
\boxed{D_s(X)\ge \frac{sG}{2}.}
\tag{22}
\]

If `Delta(X)>=delta`, use only (19) and `p_nu>=0`:

\[
D_s(X)
\ge
\Delta(X)-s(1+\Delta(X))
\ge
\delta-s(1+\delta).
\tag{23}
\]

Choose finally

\[
\boxed{
0<s<
\min\left\{
1,
\frac{\delta}{2(1+\delta)}
\right\}.
}
\tag{24}
\]

Then (23) gives `D_s(X)>=delta/2` in the large-excess regime, while (22) gives `D_s(X)>=sG/2` in the small-excess regime. Therefore

\[
\boxed{
D_s(X)
\ge
\gamma
:=
\min\left\{
\frac{sG}{2},
\frac\delta2
\right\}
>0
\qquad\text{for every finite real }X.
}
\tag{25}
\]

This proves the uniform separation (2), not merely pointwise strictness.

Since `ANF-020` gives

\[
\int J_s\,d\nu_{\rm MT}
=\frac{C(J_s)}{C_{\rm MT}},
\tag{26}
\]

and

\[
q_{\rm real}(J_s)=\inf_X\int J_s\,d\mu_X,
\]

equation (25) proves (3).

## 4. The separator can be arbitrarily close to the Montgomery--Taylor extremizer

Once `eta` and `L` have been chosen as above, condition (24) permits arbitrarily small positive `s`. Hence for every norm controlled by the compact-band profile, in particular the uniform and `L^1` norms,

\[
J_s\longrightarrow J_{\rm MT}
\qquad(s\downarrow0).
\tag{27}
\]

Every sufficiently small positive point on this ray is already on the strict finite-real-survivor side of the Montgomery--Taylor ratio.

This explains geometrically why `ANF-033` can separate the finite-diffraction closure even though `J_MT` itself is a sharp supporting functional. At the exposed `J_MT` face, near-minimizers have evacuated bounded three-point structure and therefore have too little spectral mass in a narrow neighborhood of zero. Subtracting a small central test rewards exactly that forced deficit. Configurations not close to the face cannot exploit the notch because their original positive `J_MT` excess pays for it.

The construction is therefore a standard exposed-face perturbation in spirit but with a Mathia-specific load-bearing fact: `ANF-032`--`ANF-033` provide a **uniform finite-configuration estimate** converting near-equality of the sharp Montgomery--Taylor energy into a strict central-mass deficit.

## 5. The spatial kernel must change sign, while the imaginary-axis two-point gate remains automatic

Let

\[
F_s:=\widehat J_s.
\tag{28}
\]

The separator cannot remain nonnegative on the real axis. Indeed, suppose `F_s(x)>=0` for every real `x`. The Carneiro--Chandee--Littmann--Milinovich one-delta extremal theorem used in `ANF-005` applies to the nonnegative admissible function `F_s/F_s(0)` and gives

\[
\frac{C(J_s)}{F_s(0)}\ge C_{\rm MT}.
\tag{29}
\]

But the singleton configuration gives

\[
q_{\rm real}(J_s)\le F_s(0),
\]

so (29) would imply

\[
\frac{C(J_s)}{q_{\rm real}(J_s)}
\ge C_{\rm MT},
\]

contradicting (3). Therefore

\[
\boxed{
\min_{x\in\mathbb R}F_s(x)<0.
}
\tag{30}
\]

The imaginary axis behaves in the opposite direction. Since `J_s>=0` is even,

\[
F_s(iy)
=\int_{-1}^{1}J_s(\alpha)\cosh(2\pi\alpha y)\,d\alpha
\ge
\int_{-1}^{1}J_s(\alpha)\,d\alpha
=F_s(0).
\tag{31}
\]

Thus after diagonal normalization, the elementary conjugate-pair lower barrier from `ANF-005` is automatically satisfied. The first unavoidable obstruction is instead the **real-axis negative excursion**, which forces positive normalization slack in any universal affine certificate and then exposes the full arbitrary conjugation-invariant configuration problem.

This sharpens the next scalar gate left by `ANF-033`: the finite-real separator is no longer merely existential, and the two-point imaginary-axis test does not kill it. What remains is to quantify the compulsory real-axis slack and test whether the resulting signed kernel can satisfy a universal affine counting inequality over complex conjugation-invariant multisets strongly enough to beat Montgomery--Taylor.

## 6. Prior-art and evidence boundary

No new external theorem is load-bearing. The exact Montgomery--Taylor extremizer and the full nonnegative one-delta theorem are already anchored in `SOURCES.md`; every other ingredient is internal to `ANF-030`--`ANF-033`. The present result is the two-regime perturbation argument (18)--(25), which turns the central-mass contradiction in `ANF-033` into a concrete positive-spectrum separator ray.

A targeted current search of the recent finite-compression/local-gap literature and public research artifacts found active improvements that retain additional Gram or multi-profile local information, including claimed numerical bounds beyond the Montgomery--Taylor endpoint. Those mechanisms are configuration-level refinements and do not supply this finite-real scalar notch construction. They therefore do not identify the present separator, and no publication-level novelty claim is made.

The theorem is exact but not yet numerically optimized. It proves existence of admissible `eta,L,delta,s` through explicit inequalities, while no interval-certified numerical choice is recorded here. Such numerics are unnecessary for (3), but they would be useful if one wants an explicit formula with a concrete rational `s` for the next complex-configuration search.

The finding does **not** prove a better unconditional zeta-zero proportion. It clears only the full finite-real scalar gate. `ANF-005`, `ANF-011`--`ANF-012`, and `ANF-017` already show why that is not the universal affine endpoint: arbitrary conjugation-invariant complex configurations can impose additional constraints, and the real-axis sign change (30) necessarily carries deterministic slack.

## 7. Decisive audit and next test

The proof can be falsified at only three structural interfaces. First, the central survivor bound (11) must use the original `|X|` normalization exactly as in `ANF-033`. Second, the deletion-error estimate (14) must be controlled by `Delta(X)` uniformly for fixed `L`; this is precisely the positive-sharp-energy estimate established there. Third, the large-excess branch requires `phi_eta<=J_MT`, which is built into (4)--(6). With those interfaces intact, the split at `Delta=delta` gives the uniform gap (25) directly.

The cheapest next scalar test is now concrete. Choose a certified numerical `eta,L,delta,s`, compute the real minimum of `F_s`, and feed the resulting compulsory slack into the necessary universal-affine constraints of `ANF-005`. If the optimized slack already erases the ratio gain, this entire central-notch ray dies before any higher complex configuration is needed. If it survives, the same explicit `F_s` becomes a genuine target for three- and higher-point conjugation-invariant falsifiers rather than an abstract Hahn--Banach separator.