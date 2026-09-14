# ANF-185 — Triangular twist averaging turns the critical aperture into a universal one-height high-pass

**Status:** `EXACT-DERIVED + MATCHED-CONTROL + FIXED-BASE-APERTURE-AVERAGE + ONE-HEIGHT-HIGH-PASS + SHARP-PHYSICAL-THRESHOLD`. `ANF-183` proves that prime-scale endpoint memory is invisible throughout every physical twist aperture `T=o(X/a_X)` but must be detected somewhere once `T=Theta(X/a_X)`, using a symmetric three-point probe after rephasing at the packet's first active site. The same threshold admits a stronger fixed observable: a triangular average over the aperture, rephased only at the deterministic base point `X`, detects every sector-aligned dangerous packet at critical aperture and is itself invisible on a matched packet below that aperture.

More precisely, with

\[
A_X:=\log X,
\qquad
q_X:=\lceil\log X\rceil,
\qquad
a_X:=\sqrt{\delta X\log X},
\qquad K=o(X),
\]

consider active offsets

\[
0\le j_1<\cdots<j_m\le K,
\qquad
j_{s+1}-j_s\ge q_X,
\]

and carrier phases `zeta_s` contained in one angular sector of width `pi/3`. After one common rotation assume

\[
\operatorname{Re}\zeta_s\ge\cos(\pi/6)=\frac{\sqrt3}{2}.
\]

Put

\[
F_X(\tau)
:=A_X\sum_{s=1}^m
\zeta_s\exp\!\left(-i\tau\log\left(1+\frac{j_s}{X}\right)\right).
\]

For `T>0`, let

\[
\kappa_T(\tau)
:=\frac1T\left(1-\frac{|\tau|}{T}\right)_+
\]

be the normalized triangular aperture kernel and define

\[
\mathcal D_T(F_X)
:=F_X(0)-\int_{-T}^{T}\kappa_T(\tau)F_X(\tau)\,d\tau.
\]

Then:

1. there are dangerous prime-scale packets with `|F_X(0)|>=a_X` for which

\[
\mathcal D_{T_X}(F_X)=o(a_X)
\qquad\text{whenever}\qquad
T_X=o(X/a_X);
\]

2. every sector-aligned packet satisfying `|F_X(0)|>=a_X` obeys

\[
\boxed{
|\mathcal D_T(F_X)|\gg a_X
}
\qquad\text{for}\qquad
T=C\frac{X}{a_X}
\]

once the absolute constant `C` is sufficiently large.

Thus the sharp aperture `X/a_X` from `ANF-183` does not require an adaptive sample location or knowledge of the packet's first active site. A single deterministic aperture average at base `X` works for the whole matched-control class. Moreover the average collapses exactly to one weighted distinguished-height Dirichlet polynomial with a positive sinc-squared high-pass multiplier, so the source-side target can be formulated without simultaneously estimating shifted twists.

## 1. The triangular aperture has an exact positive high-pass multiplier

The kernel has unit mass and the elementary Fourier transform

\[
\int_{-T}^{T}
\kappa_T(\tau)e^{-i\tau\lambda}\,d\tau
=
\operatorname{sinc}^2\!\left(\frac{T\lambda}{2}\right),
\tag{1}
\]

where `sinc(y)=sin(y)/y` and `sinc(0)=1`. Therefore, writing

\[
\lambda_s:=\log\left(1+\frac{j_s}{X}\right),
\qquad
W(y):=1-\operatorname{sinc}^2\!\left(\frac y2\right),
\tag{2}
\]

we obtain the exact identity

\[
\boxed{
\mathcal D_T(F_X)
=A_X\sum_{s=1}^m\zeta_s W(T\lambda_s).
}
\tag{3}
\]

The multiplier satisfies

\[
0\le W(y)\le1,
\qquad
W(0)=0,
\qquad
W(y)=\frac{y^2}{12}+O(y^4)
\quad(y\to0).
\tag{4}
\]

This positivity is the reason the packet location no longer has to be removed by an adaptive first-site rephasing. The deterministic base `X` gives `lambda_s>=0` for every admissible offset, and every atom receives a nonnegative scalar weight.

## 2. Every subcritical aperture still admits a blind dangerous packet

Use the minimal prime-scale construction of `ANF-175` and `ANF-183`: take `Theta(a_X/A_X)` candidates on the progression with spacing `q_X` inside an initial interval of physical width

\[
B_X=\Theta(a_X),
\tag{5}
\]

partition their distinguished carrier phases into six sectors, and retain a most-populated sector. With a sufficiently large fixed candidate constant, the retained packet satisfies

\[
|F_X(0)|\ge a_X,
\qquad
A_Xm=O(a_X).
\tag{6}
\]

Every retained offset obeys `j_s<=B_X`, hence

\[
0\le\lambda_s
\le\frac{B_X}{X}
\ll\frac{a_X}{X}.
\tag{7}
\]

If `T_X=o(X/a_X)`, then `T_X lambda_s=o(1)` uniformly. By (3)--(4),

\[
\begin{aligned}
|\mathcal D_{T_X}(F_X)|
&\le
A_X\sum_s W(T_X\lambda_s)\\
&\ll
A_Xm\left(T_X\frac{a_X}{X}\right)^2\\
&=o(a_X).
\end{aligned}
\tag{8}
\]

Thus even this fixed aperture-average observable cannot beat the `X/a_X` threshold. The lower construction does not exploit an unknown packet location: it can be placed at the deterministic left base itself.

## 3. Critical aperture detects every dangerous sector packet with no adaptive choices

Now let the packet be arbitrary subject to the prime-scale spacing, sector condition, and

\[
|F_X(0)|\ge a_X.
\tag{9}
\]

The trivial estimate `|F_X(0)|<=A_Xm` forces

\[
m\ge\frac{a_X}{A_X}.
\tag{10}
\]

For `s_0=ceil(m/2)`, spacing and `j_1>=0` give, for all sufficiently large `X`,

\[
j_s\ge(s_0-1)q_X\ge\frac{a_X}{3}
\qquad(s\ge s_0).
\tag{11}
\]

Since `K=o(X)`, the inequality `log(1+u)>=u/2` applies uniformly to `u=j_s/X`, so the outer half of the packet satisfies

\[
\lambda_s
\ge c_0\frac{a_X}{X}
\qquad(s\ge s_0)
\tag{12}
\]

for an absolute `c_0>0`. Choose

\[
T=C\frac{X}{a_X}
\tag{13}
\]

with `C` so large that `T lambda_s>=4` throughout that outer half. Since

\[
\left|\operatorname{sinc}\left(\frac y2\right)\right|
\le\frac2y
\qquad(y>0),
\tag{14}
\]

we then have

\[
W(T\lambda_s)\ge\frac34
\qquad(s\ge s_0).
\tag{15}
\]

After the common sector rotation, all terms in (3) have nonnegative real projection. Hence

\[
\begin{aligned}
\operatorname{Re}\mathcal D_T(F_X)
&\ge
A_X\frac{\sqrt3}{2}
\sum_{s\ge s_0}W(T\lambda_s)\\
&\ge c_1A_Xm\\
&\ge c_1a_X.
\end{aligned}
\tag{16}
\]

Therefore

\[
\boxed{
|\mathcal D_T(F_X)|\gg a_X
\quad\text{for one fixed }T=CX/a_X,
}
\tag{17}
\]

uniformly over the complete sector-aligned matched-control class. Unlike the existence statement in `ANF-183`, there is no packet-dependent `tau_X`, no search over the aperture, and no first-active-site parameter in the detector.

## 4. The aperture average is exactly a one-height weighted source sum

The fixed-base formulation has a source-side advantage. For arbitrary coefficients `c_j` and distinguished twist `U`, define

\[
F_{c,U}(\tau)
:=
\sum_{j=0}^{K}
 c_j\left(1+\frac jX\right)^{-i(U+\tau)}.
\tag{18}
\]

This differs from the usual Dirichlet polynomial

\[
\sum_{j=0}^{K}c_j(X+j)^{-i(U+\tau)}
\]

only by the known unit phase `X^{i(U+tau)}`. Applying (1) term by term gives

\[
\boxed{
\mathcal D_T(c;U)
:=F_{c,U}(0)
-
\int_{-T}^{T}\kappa_T(\tau)F_{c,U}(\tau)\,d\tau
=
\sum_{j=0}^{K}
 c_j\left(1+\frac jX\right)^{-iU}
 W\!\left(T\log\left(1+\frac jX\right)\right).
}
\tag{19}
\]

For the physical residual

\[
c_j=r_X(X+j),
\qquad
r_X=\vartheta-Q_R,
\tag{20}
\]

(19) is a **single weighted residual sum at the original distinguished height `U`**. The shifted twists in the left side are only an exact representation of the fixed spatial multiplier on the right; a source theorem may target the right side directly.

At the critical aperture `T~X/a_X`, the weight transitions on physical offset scale

\[
\frac XT\asymp a_X.
\tag{21}
\]

Thus the same scale that `ANF-175` identified as the minimum dangerous loading width and `ANF-183` identified by reciprocal twist resolution appears here as an explicit one-height high-pass cutoff. The new source-side alternative is consequently precise: prove an absolute `o(a_X)` estimate for (19) at `T=CX/a_X`, rather than uniform control of a packet-dependent three-height probe.

## 5. The high-pass has uniformly bounded variation, so no hidden stronger norm was introduced

The multiplier in (2) is not only bounded and nonnegative; it has finite total variation on the whole half-line. Put

\[
f(z):=\operatorname{sinc}^2 z.
\]

Near the origin, `f'(z)=O(z)`. For `z>=1`, direct differentiation gives

\[
|f'(z)|
\le \frac{C}{z^2}.
\tag{22}
\]

Hence

\[
\int_0^\infty |W'(y)|\,dy<\infty
\tag{23}
\]

with an absolute bound. Since `j -> T log(1+j/X)` is monotone, the discrete weight

\[
w_j:=W\!\left(T\log\left(1+\frac jX\right)\right)
\tag{24}
\]

has total variation `O(1)` uniformly in `X,T,K`. Abel summation therefore yields

\[
\boxed{
|\mathcal D_T(c;U)|
\ll
\sup_{0\le M\le K}
\left|
\sum_{j=0}^{M}
 c_j\left(1+\frac jX\right)^{-iU}
\right|.
}
\tag{25}
\]

This is an important stress test. Triangular twist averaging does not smuggle in a norm stronger than endpoint-prefix control: a theorem that already anchored every distinguished-twist prefix at `o(a_X)` would automatically control (19). Conversely, the matched packet in (17) shows that the explicit high-pass is strong enough to expose the target-sized endpoint-memory geometry once its transition scale reaches `a_X`.

The value of (19) is therefore representation, not a free estimate. It removes two adaptive ingredients from `ANF-183` and supplies one deterministic smooth weight that future source machinery can attack while retaining the exact prime-minus-Ramanujan cancellation.

## 6. Prior-art boundary and consequence for the frontier

The harmonic-analysis ingredients are classical. A triangular/Bartlett aperture has a sinc-squared Fourier transform, and positive triangular/Fejer averaging is standard; Abel summation is likewise a standard way to pass between weighted sums and partial sums. A directed prior-art search found these classical mechanisms but no theorem that supplies the Mathia-specific absolute estimate (19) for the distinguished prime-minus-Ramanujan residual at the critical scale `T~X/a_X`. No external theorem is load-bearing in the derivation, so `SOURCES.md` need not change.

The Mathia-specific content is the exact combination of the logarithmic carrier, the prime-scale atom/spacing model, sector positivity, and the critical endpoint-memory load `a_X`: together they turn the existential three-height discriminator of `ANF-183` into a **universal fixed-base aperture operator** and then into the one-height high-pass (19). This is distinct from the positive Fejer scale family of `ANF-172`: there the Fejer parameter is a physical window length and its dyadic scale slope recovers a signed lag shell; here the positive average is in the twist variable and its Fourier image is a spatial cutoff at the packet-loading scale.

This does not prove the bow variance theorem. The actual residual is not required to be sector-aligned, and no current result gives

\[
\mathcal D_{CX/a_X}(r_X;U)=o(a_X)
\tag{26}
\]

with the needed endpoint uniformity. What changes is the source target. To defeat the entire `ANF-175`--`ANF-183` sector-aligned matched-control obstruction, one no longer needs an adaptive shifted-height witness. It is enough to control the single deterministic weighted residual (19) at one distinguished height, with transition scale `a_X`. If that still cannot be reached, the direct signed Fejer-slope route of `ANF-169`--`ANF-172` remains the other phase-faithful interface.