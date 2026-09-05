# ANF-048 — bandwidth forces a sharp five-point relative-separation exclusion zone

**Status:** `EXACT-DERIVED + FREQUENCYWISE-POSITIVITY + SUPPORT-BANDWIDTH-EXCLUSION + SHARP-UNIVERSAL-THRESHOLD + HEIGHT-BALANCE-REFINEMENT + STRUCTURAL-REDUCTION`. `ANF-045`--`ANF-047` reduce the last irreducible cardinality-five geometry to two conjugate pairs plus one real point and identify cross-frequency phase coherence as the only remaining source of descent. The present finding shows that finite Fourier bandwidth itself removes a whole neighborhood of the relative horizontal diagonal **before any cross-frequency coherence analysis is needed**. If the positive spectral density is supported in `[-B,B]`, then every genuinely two-pair five-point configuration with pair-center separation

\[
|x_1-x_2|\le \frac{1}{3B}
\]

has strictly larger energy than its real-part collapse, at every pair of heights and every common horizontal translation. For support one this gives the absolute exclusion zone `|x_1-x_2|<=1/3`. The constant `1/3` is optimal among rules using only positivity and the bandwidth: immediately beyond it one can construct a continuous nonnegative spectrum and a genuine two-pair configuration with negative defect. Comparable pair heights enlarge the safe zone; for equal heights the sharp phase-blind radius becomes

\[
\frac{\arccos(-7/8)}{2\pi B}
=\frac{0.4195693767\ldots}{B}.
\]

Thus the compact obstruction box of `ANF-044` has an additional hole around `d=x_1-x_2=0`; any remaining central-notch falsifier must have a finite, non-small relative horizontal separation.

Let

\[
F(z)=\widehat J(z)
=\int_{-B}^{B}J(\alpha)e^{-2\pi i\alpha z}\,d\alpha,
\qquad
J\ge0,
\tag{1}
\]

where `B>0` and `J` is continuous, even and nonzero. Retain the two-pair geometry

\[
W=\{x_1\pm iy_1,x_2\pm iy_2,r\},
\qquad y_1,y_2>0,
\tag{2}
\]

and put

\[
t_j=x_j-r,
\qquad
d=t_1-t_2=x_1-x_2.
\tag{3}
\]

For a fixed frequency define

\[
a=\cosh(2\pi\alpha y_1)-1,
\qquad
b=\cosh(2\pi\alpha y_2)-1,
\tag{4}
\]

\[
\phi=2\pi\alpha d,
\qquad
c=\cos\phi,
\qquad
s=a+b,
\tag{5}
\]

and

\[
V_\alpha
=a e^{2\pi i\alpha t_1}
+b e^{2\pi i\alpha t_2}.
\tag{6}
\]

The exact Hilbert normal form of `ANF-045` is

\[
\boxed{
h_\alpha
=|V_\alpha|^2+\operatorname{Re}V_\alpha
+2s(1+c),
}
\tag{7}
\]

with

\[
H_J(y_1,y_2;t_1,t_2)=\int J(\alpha)h_\alpha\,d\alpha,
\qquad
E_F(W)-E_F(R(W))=4H_J.
\tag{8}
\]

The key point is that the magnitude of `V_alpha` is independent of the common translation. Writing

\[
R:=|V_\alpha|
=|a e^{i\phi}+b|,
\tag{9}
\]

one has

\[
R\le a+b=s
\tag{10}
\]

and, from `Re V_alpha>=-R`,

\[
\boxed{
h_\alpha
\ge R^2-R+2s(1+c).}
\tag{11}
\]

This elementary pointwise inequality is enough to create a bandwidth-scale geometric exclusion zone.

## 1. The universal one-third bandwidth zone is strictly safe

Suppose first that

\[
c=\cos(2\pi\alpha d)\ge-\frac12.
\tag{12}
\]

Then

\[
2s(1+c)\ge s\ge R,
\tag{13}
\]

so (11) immediately gives

\[
\boxed{h_\alpha\ge R^2\ge0.}
\tag{14}
\]

This is a frequencywise statement: no cancellation between different `alpha` is being used.

If `|d|<=1/(3B)`, then for every `alpha` in the spectral support,

\[
|2\pi\alpha d|
\le \frac{2\pi}{3},
\tag{15}
\]

hence (12) holds everywhere because cosine is decreasing on `[0,pi]`. Therefore

\[
H_J
\ge
\int J(\alpha)R(\alpha)^2\,d\alpha.
\tag{16}
\]

The right side is exactly the positive shape functional `Q` of `ANF-045`. For a genuine two-pair split `y_1,y_2>0`,

\[
Q>0.
\tag{17}
\]

Indeed, if `Q=0`, then `a(alpha)e^{2pi i alpha d}+b(alpha)` vanishes on an open interval where `J>0`; analyticity would force it to vanish identically, contradicting its nonzero quadratic term

\[
2\pi^2(y_1^2+y_2^2)\alpha^2+O(\alpha^3)
\]

at the origin. Consequently

\[
\boxed{
|x_1-x_2|\le\frac1{3B}
\quad\Longrightarrow\quad
H_J>0
}
\tag{18}
\]

for every `y_1,y_2>0`, every real anchor `r`, and every common translation of the two pair centers. Equivalently,

\[
\boxed{
E_F(W)>E_F(R(W)).
}
\tag{19}
\]

No curvature assumption `m_5(J)>=0` is needed. The result holds globally in height and depends only on spectral positivity and bandwidth.

For the support-one profiles used throughout the Montgomery--Taylor and central-notch branch,

\[
\boxed{|x_1-x_2|\le\frac13}
\tag{20}
\]

is therefore an absolute forbidden region for a negative two-pair five-point defect.

## 2. Height balance widens the exclusion zone

The crude step `R<=s` is sharp when one pair amplitude is negligible, but it throws away useful information when the two heights are comparable. For `alpha!=0` define the balance coefficient

\[
\chi(\alpha)
:=\frac{4ab}{(a+b)^2}
\in(0,1].
\tag{21}
\]

A direct calculation gives

\[
\boxed{
\frac{R^2}{s^2}
=1-\frac{\chi}{2}(1-c).
}
\tag{22}
\]

Assume on the relevant spectral support that

\[
\chi(\alpha)\ge\chi_0,
\qquad 0\le\chi_0\le1.
\tag{23}
\]

Put `z=1+c`. Then

\[
\frac{R}{s}
\le
\sqrt{1-\chi_0+\frac{\chi_0}{2}z}.
\tag{24}
\]

Hence the positive residual in (11) already dominates the full linear descent whenever

\[
2z
\ge
\sqrt{1-\chi_0+\frac{\chi_0}{2}z}.
\tag{25}
\]

Squaring gives the exact threshold

\[
8z^2-\chi_0z-2(1-\chi_0)\ge0.
\tag{26}
\]

Define

\[
\boxed{
z_0(\chi_0)
:=
\frac{\chi_0+
\sqrt{\chi_0^2+64(1-\chi_0)}}{16},
}
\tag{27}
\]

and

\[
\boxed{c_0(\chi_0):=z_0(\chi_0)-1.}
\tag{28}
\]

Then

\[
\boxed{
\cos(2\pi\alpha d)\ge c_0(\chi_0)
\quad\Longrightarrow\quad
h_\alpha\ge R^2.}
\tag{29}
\]

The endpoints are

\[
c_0(0)=-\frac12,
\qquad
c_0(1)=-\frac78.
\tag{30}
\]

Thus every positive balance lower bound widens the one-third zone.

For equal heights `y_1=y_2`, one has `a=b` and hence `chi=1` at every nonzero frequency. Therefore

\[
\cos(2\pi\alpha d)\ge-\frac78
\]

is sufficient frequencywise, and compact support gives

\[
\boxed{
|d|
\le
\frac{\arccos(-7/8)}{2\pi B}
=
\frac{0.4195693767448\ldots}{B}
\quad\Longrightarrow\quad
H_J>0.}
\tag{31}
\]

This is substantially wider than `1/(3B)`.

## 3. Every compact height box has a uniform wider safe zone

The balance improvement can be made uniform on the compact height boxes produced by `ANF-044`. Fix

\[
\varepsilon\le y_1,y_2\le Y,
\qquad 0<\varepsilon\le Y<\infty.
\tag{32}
\]

Using

\[
\cosh(2\pi\alpha y)-1
=2\sinh^2(\pi\alpha y),
\tag{33}
\]

one obtains for `0<|alpha|<=B`

\[
\frac1{R_{\varepsilon,Y,B}}
\le\frac{a}{b}
\le R_{\varepsilon,Y,B},
\tag{34}
\]

where

\[
\boxed{
R_{\varepsilon,Y,B}
:=
\left(
\frac{\sinh(\pi B Y)}
{\sinh(\pi B\varepsilon)}
\right)^2.
}
\tag{35}
\]

The bound follows because `sinh(kY)/sinh(k epsilon)` is increasing in `k>0`; differentiating its logarithm reduces this to the elementary monotonicity of `x coth x`.

Since `4r/(1+r)^2` is invariant under `r->1/r` and decreases for `r>=1`, (34) gives the uniform balance floor

\[
\boxed{
\chi(\alpha)
\ge
\chi_{\varepsilon,Y,B}
:=
\frac{4R_{\varepsilon,Y,B}}
{(1+R_{\varepsilon,Y,B})^2}
>0.
}
\tag{36}
\]

Consequently every shape in the height box is strictly safe whenever

\[
\boxed{
|d|
\le
D_{\varepsilon,Y,B}
:=
\frac{\arccos(c_0(\chi_{\varepsilon,Y,B}))}
{2\pi B}.}
\tag{37}
\]

Because `chi_{epsilon,Y,B}>0`,

\[
\boxed{
D_{\varepsilon,Y,B}>\frac1{3B}.}
\tag{38}
\]

So after `ANF-044` confines a possible negative defect to

\[
\varepsilon_J\le y_1,y_2\le Y_J,
\qquad
|d|\le2T_J,
\]

the present result removes a uniform open slab around the relative diagonal:

\[
\boxed{
D_{\varepsilon_J,Y_J,B}<|d|\le2T_J
}
\tag{39}
\]

is necessary for any remaining negative candidate. The unresolved shape domain is therefore not merely compact; it is separated by a positive distance from `d=0`.

## 4. The one-third constant is sharp from bandwidth information alone

The support-only radius `1/(3B)` cannot be enlarged uniformly over all continuous even nonnegative spectra and all genuine heights.

Fix any

\[
d_0>\frac1{3B}.
\tag{40}
\]

Because `2pi B d_0>2pi/3`, choose `alpha_0 in (0,B)` so that

\[
\frac{2\pi}{3}
<\phi_0:=2\pi\alpha_0d_0
<\pi.
\tag{41}
\]

Then

\[
1+2\cos\phi_0<0.
\tag{42}
\]

Choose asymmetric small heights

\[
y_1=\eta,
\qquad
y_2=\eta^2,
\tag{43}
\]

and choose `t_1` so that

\[
2\pi\alpha_0t_1=\pi,
\qquad
t_2=t_1-d_0.
\tag{44}
\]

At `alpha_0`, as `eta->0`, one has `b/a->0`, `a->0`, and the exact normal form (7) gives

\[
\frac{h_{\alpha_0}}{a}
\longrightarrow
-1+2(1+\cos\phi_0)
=1+2\cos\phi_0<0.
\tag{45}
\]

Thus `h_{alpha_0}<0` for sufficiently small positive `eta`. By continuity it remains negative on a small neighborhood of `alpha_0` and, by evenness, on the reflected neighborhood around `-alpha_0`. Choosing any nonzero continuous even `J>=0` supported inside those two neighborhoods gives

\[
H_J<0.
\tag{46}
\]

The spectrum may be normalized arbitrarily because scaling `J` does not change the sign. A sufficiently small positive central background can also be added while preserving (46), so the sharpness is not an artifact of forcing `J(0)=0`.

Therefore

\[
\boxed{
\frac1{3B}
}
\]

is the **largest universal safe radius derivable from bandwidth and spectral nonnegativity alone**. Any improvement for the Montgomery--Taylor or central-notch spectra must use their actual spectral mass distribution or the height balance, not only the location of their support.

## 5. The equal-height radius is likewise sharp for phase-blind support control

The balanced endpoint has a matching local sharpness statement. Put

\[
\theta_{\rm eq}:=\arccos(-7/8).
\tag{47}
\]

For any

\[
d_0>\frac{\theta_{\rm eq}}{2\pi B},
\tag{48}
\]

choose `alpha_0 in (0,B)` with

\[
\theta_{\rm eq}<\phi_0:=2\pi\alpha_0d_0<\pi.
\tag{49}
\]

Take equal small heights `y_1=y_2=eta`. Then `a=b`, and choose the common translation so that `V_{alpha_0}` is negative real. Writing `z_0=1+cos(phi_0)`, division of (7) by `s=2a` gives as `eta->0`

\[
\frac{h_{\alpha_0}}{s}
\longrightarrow
2z_0-\sqrt{\frac{z_0}{2}}.
\tag{50}
\]

Because `cos(phi_0)<-7/8`, one has `0<z_0<1/8`, and therefore

\[
2z_0-\sqrt{z_0/2}<0.
\tag{51}
\]

Again a narrow even spectral bump around `+-alpha_0` produces `H_J<0`. Hence the equal-height radius in (31) is optimal for a universal positive-spectrum argument that uses only the bandwidth and the equal-height constraint.

This sharpness does **not** claim that the fixed Montgomery--Taylor or central-notch spectra fail immediately beyond these radii. Their distributed spectral mass can prevent the near-monochromatic construction used above.

## 6. Prior art, falsification, and evidence boundary

The proof is a finite trigonometric/triangle-inequality consequence of the exact five-point Fourier--Laplace normal form already derived in `ANF-045`. A targeted search of the neighboring bandlimited positive-definite/extremal-function and zeta pair-correlation/semidefinite literature found the expected general Fourier-support and positivity machinery but no external result that supplies the exclusion radii (18), (31), or their sharpness constructions. No publication-level novelty claim is made, and no new `SOURCES.md` entry is required because no external theorem is load-bearing here.

The main adversarial checks are explicit. The strict conclusion uses `Q>0`, so both pair heights must be genuinely positive; if one pair is collapsed completely, the geometry belongs to the already-closed one-pair boundary. The cosine argument uses the entire spectral support, not merely most of its mass. The constant `1/(3B)` is therefore a worst-case support statement; a spectrum concentrated well inside `[-B,B]` should be evaluated with its actual effective support. The sharpness examples vary `J`; they show that no stronger theorem can follow from positivity plus bandwidth alone, not that a particular fixed `J` has a counterexample beyond the threshold.

The result says nothing about multisets of cardinality greater than five, nor does it prove the full universal affine counting inequality of `ANF-005`. It only removes a geometrically explicit subset of the final two-pair cardinality-five obstruction.

## 7. Consequence for the central-notch frontier

For every support-one central-notch survivor `J_s` from `ANF-034`--`ANF-047`, a negative two-pair five-point defect must now satisfy at least

\[
\boxed{|x_1-x_2|>\frac13.}
\tag{52}
\]

After inserting the height compactification of `ANF-044`, the stronger uniform radius (37) applies and pushes the candidate set farther away from the relative diagonal. Equal-height candidates cannot enter until

\[
|x_1-x_2|>0.4195693767\ldots.
\tag{53}
\]

Thus the remaining phase-aware certification problem is concentrated on **finite-height, finitely separated, genuinely nonlocal pair centers**. Small relative separation is not a possible hiding place for the last cardinality-five obstruction. The next useful analytic or interval certificate should exploit the fixed central-notch spectral mass on the residual annular shape region rather than spending effort near `d=0`, which is now closed exactly.