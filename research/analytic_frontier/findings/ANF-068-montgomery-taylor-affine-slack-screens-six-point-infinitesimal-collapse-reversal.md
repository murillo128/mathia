# ANF-068 — Montgomery--Taylor affine slack screens six-point infinitesimal collapse reversal

**Status:** `EXACT-DERIVED + COMPUTER-ASSISTED-INPUT + SIX-POINT-AFFINE-SCREENING + CENTRAL-NOTCH-PERTURBATIVE-NO-GO + STRUCTURAL-REDUCTION`. `ANF-067` shows that Montgomery--Taylor real collapse first reverses direction infinitesimally at cardinality six: for one conjugate pair and four real anchors the vertical second variation can be negative. That sign reversal is real, but it is not close to saturating the affine counting inequality. The same curvature condition that makes the vertical motion descend forces at least three anchors into a compact interval on which the Montgomery--Taylor spatial kernel is uniformly positive. Their interaction with the doubled collapse point therefore creates a fixed affine margin before the vertical motion starts.

More precisely, let

\[
F:=R_{\rm MT}=\widehat J_{\rm MT}\ge0,
\qquad
K(t):=\int_{-1}^{1}\alpha^2J_{\rm MT}(\alpha)\cos(2\pi\alpha t)\,d\alpha,
\]

put `K_0=K(0)` and `k_*=\inf K`, and take four distinct nonzero real anchors

\[
T=\{t_1,t_2,t_3,t_4\}.
\]

Define

\[
R_T:=\{0,0,t_1,t_2,t_3,t_4\},
\qquad
W_{y,T}:=\{iy,-iy,t_1,t_2,t_3,t_4\},
\]

and the infinitesimal collapse coefficient from `ANF-037` and `ANF-067`,

\[
D(T):=2K_0+\sum_{j=1}^4K(t_j).
\tag{1}
\]

Let

\[
I:=\{t\in\mathbb R:0.545\le |t|\le1.01\},
\qquad
\rho_*:=\min_{t\in I}F(t).
\tag{2}
\]

Then

\[
\boxed{\rho_*>0,}
\tag{3}
\]

and every `T` with

\[
\boxed{D(T)<0}
\tag{4}
\]

satisfies the uniform Montgomery--Taylor affine-margin bound

\[
\boxed{
E_F(R_T)-8\ge12\rho_*.
}
\tag{5}
\]

Consequently the entire negative-second-variation class from `ANF-067` is uniformly harmless in a sufficiently small-height neighborhood, not only for the base Montgomery--Taylor certificate but also for every sufficiently small central-notch perturbation at the minimum deterministic slack of `ANF-046`. For each fixed notch width `0<\eta<1`, there exist `y_*>0` and `s_*>0`, depending only on the fixed Montgomery--Taylor profile and `eta`, such that

\[
D(T)<0,
\qquad 0<y\le y_*,
\qquad 0<s\le s_*
\]

implies that `W_{y,T}` satisfies the candidate central-notch affine inequality with a strictly positive margin uniform in `T`.

Thus the six-point phenomenon found in `ANF-067` does **not** expose an infinitesimal obstruction to the central-notch ray. Any six-point failure of that ray must use a genuinely finite-height mechanism, a different small-height regime not governed by negative Montgomery--Taylor second variation, or a larger configuration-level effect.

## 1. Negative second variation forces at least three anchors into the low-curvature annulus

`ANF-059` proves the certified exterior curvature bound

\[
|t|\le0.545\ \text{or}\ |t|\ge1.01
\quad\Longrightarrow\quad
K(t)>-\frac{K_0}{3}.
\tag{6}
\]

`ANF-066` identifies the global minimum `k_*` and, together with the strict five-point curvature margin already established in `ANF-038`, gives

\[
\boxed{2K_0+3k_*>0.}
\tag{7}
\]

Suppose at most two of the four anchors lie in the strict annulus

\[
0.545<|t|<1.01.
\]

Since `K>=k_*` everywhere and (6) holds outside the annulus, the worst possible sum occurs when exactly two anchors sit at the global minimum and the other two approach the exterior threshold. Hence

\[
\begin{aligned}
D(T)
&=2K_0+\sum_{j=1}^4K(t_j)\\
&>2K_0+2k_*-\frac{2K_0}{3}\\
&=\frac23\left(2K_0+3k_*\right)>0,
\end{aligned}
\tag{8}
\]

contradicting (4). Therefore

\[
\boxed{
D(T)<0
\quad\Longrightarrow\quad
\#\{j:0.545<|t_j|<1.01\}\ge3.
}
\tag{9}
\]

This is the key linkage missing from the sign calculation in `ANF-067`. The four anchor contributions to the curvature sum are not free to become negative while their affine interactions disappear: at least three must remain in one fixed bounded horizontal region.

## 2. The Montgomery--Taylor kernel has no zero on that annulus

`ANF-031` gives the exact positive zero set of the Montgomery--Taylor factor. If `F=S^2`, every genuine positive zero has the form

\[
z_n=n+\frac{\varepsilon_n}{\pi},
\qquad n\ge1,
\tag{10}
\]

where `epsilon_n>0` is the unique solution of

\[
(n\pi+\varepsilon_n)\tan\varepsilon_n
=\theta\tan\theta,
\qquad
\theta=2^{-1/2}.
\tag{11}
\]

For the first branch, the elementary estimates `tan(theta)>theta`, `sin x<x`, `cos x>1-x^2/2`, and `pi<22/7` give

\[
\theta\tan\theta>\frac12
\]

while, at `x=\pi/100`,

\[
(\pi+x)\tan x
<\frac{1111}{350}\frac{11/350}{1-121/245000}
<\frac18.
\tag{12}
\]

Since the left side of (11) is strictly increasing on the first positive tangent branch,

\[
\varepsilon_1>\frac\pi{100},
\qquad
z_1>1.01.
\tag{13}
\]

`ANF-031` also proves that there is no genuine positive zero below `z_1`; the apparent root at `theta/pi` is removable. Hence `F` is strictly positive on the compact set `I` in (2), proving (3). No numerical evaluation of `rho_*` is needed.

## 3. The collapsed six-point affine slack has a fixed positive floor

For the zero-slack Montgomery--Taylor affine inequality the intercept is `A=2`. The collapsed multiset `R_T` has cardinality six and exactly four simple real points, so its affine slack is

\[
\mathcal S_{\rm MT}(R_T)
:=4-\left(12-E_F(R_T)\right)
=E_F(R_T)-8.
\tag{14}
\]

Because the origin occurs twice, direct expansion of the ordered pair energy gives the exact identity

\[
\boxed{
\mathcal S_{\rm MT}(R_T)
=4\sum_{j=1}^4F(t_j)
+2\sum_{1\le j<k\le4}F(t_j-t_k).
}
\tag{15}
\]

All terms are nonnegative because `F=R_MT>=0`. If (4) holds, (9) puts at least three anchors in `I`, where `F>=rho_*`. Dropping every other positive term in (15) therefore gives

\[
\mathcal S_{\rm MT}(R_T)
\ge4(3\rho_*)
=12\rho_*,
\]

which is (5).

For the explicit rational witness of `ANF-067`, `T={0.74,0.75,0.76,0.77}`, one can see the screening even without `rho_*`. Since `J_MT=g*g` with `g>=0`, `int g=1`, and `supp g subset [-1/2,1/2]`,

\[
\widehat g(u)\ge\cos(\pi h)
\qquad(|u|\le h<1/2).
\tag{16}
\]

All six pairwise anchor separations are at most `0.03`, so the anchor--anchor terms alone in (15) give

\[
\mathcal S_{\rm MT}(R_T)
\ge12\cos^2(0.03\pi).
\tag{17}
\]

Thus the explicit witness used to reveal the sign reversal is very far from affine equality. The reversal was detecting the sign of a vertical derivative, not the exhaustion of the available counting margin.

## 4. The fixed margin survives a uniform small vertical displacement

Retain the exact one-pair/four-anchor decomposition from `ANF-037`:

\[
E_F(W_{y,T})-E_F(R_T)
=4\left(A_y+\sum_{j=1}^4L_y(t_j)\right),
\tag{18}
\]

where `A_y>=0` and each `L_y(t)` contains one factor `cosh(2pi alpha y)-1` against `J_MT(alpha) cos(2pi alpha t)`. Since `J_MT>=0`, is supported in `[-1,1]`, and has integral `F(0)=1`,

\[
L_y(t)
\ge-\left(\cosh(2\pi y)-1\right)
\qquad(t\in\mathbb R).
\tag{19}
\]

Consequently

\[
\boxed{
E_F(W_{y,T})-E_F(R_T)
\ge-16\left(\cosh(2\pi y)-1\right).
}
\tag{20}
\]

Choose `y_*>0` so that

\[
16\left(\cosh(2\pi y_*)-1\right)
\le6\rho_*.
\tag{21}
\]

Then (5) and (20) imply the uniform base-profile margin

\[
\boxed{
\mathcal S_{\rm MT}(W_{y,T})\ge6\rho_*
}
\tag{22}
\]

for every `T` satisfying (4) and every `0<y<=y_*`. Notice that no compactness in the fourth anchor is required; it may escape to infinity. The three anchors forced by curvature already pay the entire fixed margin.

## 5. A sufficiently small central notch cannot consume the margin

Fix the central tent from `ANF-034`--`ANF-046`,

\[
\phi_\eta(\alpha)
=b_\eta\left(1-\frac{|\alpha|}{\eta}\right)_+,
\qquad
\Phi_\eta=\widehat\phi_\eta,
\qquad
\int\phi_\eta=b_\eta\eta,
\tag{23}
\]

and put

\[
J_s=J_{\rm MT}-s\phi_\eta,
\qquad
F_s=F-s\Phi_\eta.
\tag{24}
\]

`ANF-046` proves that the minimum deterministic slack allowed by the elementary affine tests is

\[
\delta_s=sb_\eta\eta,
\]

so the corresponding candidate intercept is

\[
A_s=1+F_s(0)-\delta_s
=2-2sb_\eta\eta.
\tag{25}
\]

For a six-point multiset with four simple real elements, its affine slack at this intercept is exactly

\[
\boxed{
\mathcal S_s(W_{y,T})
=\mathcal S_{\rm MT}(W_{y,T})
+s\left(12b_\eta\eta-E_{\Phi_\eta}(W_{y,T})\right).
}
\tag{26}
\]

Because `phi_eta>=0` and the multiset is conjugation invariant, its energy has the positive spectral representation

\[
E_{\Phi_\eta}(W_{y,T})
=\int\phi_\eta(\alpha)
\left|
2\cosh(2\pi\alpha y)
+\sum_{j=1}^4e^{-2\pi i\alpha t_j}
\right|^2d\alpha.
\tag{27}
\]

On `supp phi_eta`, the absolute value in (27) is at most

\[
2\cosh(2\pi\eta y)+4.
\]

Hence, uniformly in all horizontal anchors,

\[
\boxed{
E_{\Phi_\eta}(W_{y,T})
\le b_\eta\eta
\left(2\cosh(2\pi\eta y)+4\right)^2.
}
\tag{28}
\]

Set

\[
B_{\eta,*}
:=\left(2\cosh(2\pi\eta y_*)+4\right)^2-12>0
\tag{29}
\]

and choose

\[
0<s_*
\le
\min\left\{
1,
\frac{3\rho_*}{b_\eta\eta B_{\eta,*}}
\right\}.
\tag{30}
\]

Combining (22), (26), and (28) gives, for every `D(T)<0`, `0<y<=y_*`, and `0<s<=s_*`,

\[
\boxed{
\mathcal S_s(W_{y,T})\ge3\rho_*>0.
}
\tag{31}
\]

The admissible `s` in the finite-real separator construction of `ANF-034` may be taken arbitrarily small, so (30) can be imposed simultaneously with that construction and with the narrow-notch objective condition of `ANF-046`.

## 6. What this changes in the six-point frontier

`ANF-067` correctly identifies a sharp structural transition: the energy of the base Montgomery--Taylor kernel can decrease under real collapse reversal for the first time at cardinality six. Equation (31) shows that this transition is **not** the perturbative affine obstruction one might have expected. The curvature descent and affine saturation point in incompatible directions. To make the second variation negative, at least three anchors must stay in the low-curvature annulus; but on that same annulus the nonnegative Montgomery--Taylor kernel is bounded away from zero, so those anchors pay a fixed interaction cost with the doubled real point.

This rules out an entire next-step strategy: refining the `ANF-067` small-height witness, while keeping its negative Montgomery--Taylor second variation as the driving mechanism, cannot kill sufficiently small central notches. The loss is not a matter of optimizing the four rational anchor locations. It is uniform over the whole negative-second-variation class.

What remains genuinely open begins away from this infinitesimal regime. A six-point obstruction could still occur at finite positive height, where the full Fourier--Laplace geometry is not controlled by (1), or through a notch-dependent small-height family whose mechanism is not a negative Montgomery--Taylor second variation. Larger conjugation-invariant configurations also remain untouched. The result proves no universal affine theorem for `J_s` and no improvement in the unconditional zeta-zero proportion by itself.

## 7. Prior art and evidence boundary

A fresh search checked Lamzouri's 2 September 2026 Hilbert-space proof, the Carneiro--Chandee--Littmann--Milinovich extremal framework, and neighboring descriptions of the Montgomery--Taylor optimizer. Those sources establish the pair-correlation inequality and the extremal kernel, but no external result located in the search formulates the six-point curvature-versus-affine-margin screening (9)--(31). No publication-level novelty claim is made. The relevant primary sources are already anchored in `SOURCES.md`, so no source-file change is required.

The only computer-assisted input inherited here is the certified curvature annulus (6) and the already canonical strict curvature margin/minimum data from `ANF-059` and `ANF-066`. Once those inputs are granted, the screening argument itself is exact: (9) is a four-term pigeonhole estimate, (15) is an ordered-energy identity using `F>=0`, (20) is a support-one Fourier--Laplace bound, and (28) is the positive spectral representation of the notch energy.

The decisive falsification points are correspondingly narrow. The result fails if the `ANF-059` exterior threshold is wrong, if `F` has a genuine zero below `1.01`, if the collapsed energy decomposition (15) misses a multiplicity factor, or if the conjugation-invariant spectral identity (27) is invalid. `ANF-031` plus (12)--(13) closes the zero-set issue, and direct ordered-pair counting gives the factors `4` and `2` in (15).

The next decisive test should therefore compactify the **finite-height six-point** one-pair/four-anchor problem for a fixed narrow notch, rather than continue optimizing infinitesimal collapse directions already screened by (31).