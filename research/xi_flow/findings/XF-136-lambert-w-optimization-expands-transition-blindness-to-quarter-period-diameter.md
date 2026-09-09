# XF-136 — Lambert-W optimization expands transition blindness to quarter-period diameter

**Status:** `EXACT-DERIVED` + `SHARP-WITHIN-XF-133-PACKET-ENVELOPE` + `DECISIVE-NEGATIVE/TRANSITION-CONDITIONING` + `LOCAL-PATCH-OBSERVABILITY` + `LOG-JETS` + `UNIT-CIRCLE-MATCHED-CONTROL` + `CROSS-SCALE`. XF-133--XF-135 use the central divided-difference packet with the convenient choice `r=floor(M/3)` and the crude inequality `r!<=r^r`, obtaining transition blindness on physical disks of radius just below `log(2)L/(4 pi)≈0.05516L`. Keeping the exact factorial exponent and optimizing the packet depth shows that the same already-constructed transition-sharp family is invisible on a disk more than twice as large. The optimal exponential aperture of this packet envelope is explicit and is governed by `W_0(2)`, the principal Lambert-W value at `2`.

Let `N=2M` and retain the XF-133 packet amplitude

\[
A_{M,r}:=\frac{(r!)^2}{(M^2-r^2)^r},
\qquad 1\le r<M.
\tag{1}
\]

For `0<alpha<1`, set

\[
\Phi(\alpha)
:=
\alpha\left[
2+\log\!\left(\frac{1-\alpha^2}{\alpha^2}\right)
\right].
\tag{2}
\]

If `r/M->alpha`, Stirling's formula gives the exact exponential rate

\[
\boxed{
\log A_{M,r}
=
-M\Phi(\alpha)+O(\log M).
}
\tag{3}
\]

The function `Phi` has a unique global maximum at

\[
\boxed{
\alpha_*
=
\sqrt{\frac{W_0(2)}{2+W_0(2)}}
=0.5467052037\ldots,
}
\tag{4}
\]

and

\[
\boxed{
\Phi_*
:=\Phi(\alpha_*)
=
\sqrt{W_0(2)\bigl(2+W_0(2)\bigr)}
=1.5595342722\ldots .
}
\tag{5}
\]

Since `N=2M`, define

\[
\boxed{
b_*:=\frac{\Phi_*}{2}
=0.7797671361\ldots .}
\tag{6}
\]

Taking `r=floor(alpha_* M)` therefore yields

\[
\boxed{
A_{M,r}
=
\exp\bigl[-b_*N+O(\log N)\bigr].
}
\tag{7}
\]

Consequently the transition-sharp matched controls of XF-134 satisfy, for every fixed `eta>0`, every finite `rho>=0`, and every aperture

\[
B_N\le(b_*-\eta)N,
\tag{8}
\]

the uniform zero-delay estimate

\[
\boxed{
\sup_{s\ge0}\sup_{|\beta|\le B_N}
\left|
E_{\rm c}(\zeta_{\beta,N},s)
-
E_{{\rm c},\rho}(\zeta_{\beta,N},s)
\right|
\le
\exp[-\eta N+O(\log N)],
}
\tag{9}
\]

while

\[
\Lambda_{\rm per}(E_{\rm c})=0,
\qquad
\Lambda_{\rm per}(E_{{\rm c},\rho})=-\rho.
\tag{10}
\]

The same improvement propagates to XF-135. For every fixed `sigma>0`, if `J_N log(J_N+2)=o(N)`, then on the exterior patch

\[
\Omega_{B_N,\sigma}
=
\{\beta:|\beta|\le B_N,\ \operatorname{Re}\beta\ge\sigma\}
\tag{11}
\]

all logarithmic jets through order `J_N` remain exponentially transition-blind:

\[
\boxed{
\sup_{\substack{s\ge0,\ \rho\ge0\\
\beta\in\Omega_{B_N,\sigma}\\
1\le j\le J_N}}
\left|
\partial_\beta^j\log Q_s(\beta)
-
\partial_\beta^j\log Q_{s+\rho}(\beta)
\right|
\le
\exp[-\eta N+o(N)].
}
\tag{12}
\]

Thus the earlier `log(2)/2` aperture was not intrinsic. Within the existing central divided-difference construction, the sharp exponential aperture constant is `b_*`.

## 1. The missing exponential factor is already inside the factorial

Start from `(1)` and write `r=alpha M+O(1)`. The logarithmic Stirling expansion

\[
\log(r!)
=r\log r-r+O(\log r)
\tag{13}
\]

gives

\[
\begin{aligned}
\log A_{M,r}
&=2r\log r-2r-r\log(M^2-r^2)+O(\log M)\\
&=r\left[
2\log\!\left(\frac rM\right)
-2
-\log\!\left(1-\frac{r^2}{M^2}\right)
\right]
+O(\log M).
\end{aligned}
\tag{14}
\]

Dividing by `M` and sending `r/M->alpha` gives `(3)`.

This exposes the loss in the earlier convenient estimate. Replacing `r!` by `r^r` discards the factor `e^{-2r+o(r)}` from `(r!)^2`. Since the useful packet depth is itself proportional to `M`, that is an exponential loss in `N`, not a lower-order constant. Even the old choice `alpha=1/3` therefore supports a much larger aperture than the bound recorded in XF-133--XF-135; optimizing `alpha` gives the final constant `(6)`.

## 2. The optimal packet depth is a Lambert-W point

Differentiate `(2)`:

\[
\Phi'(\alpha)
=
\log\!\left(\frac{1-\alpha^2}{\alpha^2}\right)
-
\frac{2\alpha^2}{1-\alpha^2}.
\tag{15}
\]

Put

\[
x:=\frac{\alpha^2}{1-\alpha^2}>0.
\tag{16}
\]

Then the critical-point equation is

\[
-\log x=2x,
\tag{17}
\]

or equivalently

\[
(2x)e^{2x}=2.
\tag{18}
\]

Hence

\[
2x=W_0(2),
\tag{19}
\]

which gives `(4)`. The left side of `(17)` decreases strictly in `x` while the right side increases strictly, so this critical point is unique. Moreover `Phi(alpha)->0` as `alpha->0+`, while `Phi(alpha)->-infinity` as `alpha->1-`; the unique critical point is therefore the global maximum.

At the maximizer, `(17)` says

\[
\log\!\left(\frac{1-\alpha_*^2}{\alpha_*^2}\right)
=W_0(2).
\tag{20}
\]

Substituting `(4)` into `(2)` gives

\[
\Phi_*
=\alpha_*\bigl(2+W_0(2)\bigr)
=\sqrt{W_0(2)(2+W_0(2))},
\tag{21}
\]

proving `(5)`--`(7)`.

The same calculation gives a useful internal sharpness statement. For **any** depth sequence `1<=r_M<M`, Stirling's formula applied along subsequences gives

\[
\boxed{
\limsup_{M\to\infty}
\left(-\frac1N\log A_{M,r_M}\right)
\le b_*.
}
\tag{22}
\]

Thus no different proportional or non-proportional choice of `r` can improve the exponential decay rate of the XF-133 amplitude envelope `(1)`. This is sharpness only for this explicit packet family and its proved envelope; it is not a global observability threshold for all possible matched controls.

## 3. The transition-sharp controls inherit the optimized aperture without modification

XF-134 is valid for every `1<=r<M`, not merely `r=floor(M/3)`. Its collision amplitude is

\[
t_*=-\frac{2(-1)^{M+r}}{H_r},
\qquad |t_*|\le2,
\tag{23}
\]

and its alternating-sign argument uses only `r<M`. For the optimized depth `(4)`, the nondegeneracy margin

\[
M^2-r^2
=(1-\alpha_*^2)M^2+O(M)
\tag{24}
\]

remains a fixed positive fraction of `M^2`. The unit-circle admissibility and the exact transition identities `(10)` therefore survive unchanged.

XF-134 gives the exact observation estimate

\[
\sup_{s\ge0,\ |\beta|\le B}
|E_{\rm c}(\zeta_{\beta,N},s)
-E_{{\rm c},\rho}(\zeta_{\beta,N},s)|
\le4e^B A_{M,r}.
\tag{25}
\]

Insert `(7)` and `(8)`:

\[
\log(4e^{B_N}A_{M,r})
\le
-\eta N+O(\log N),
\tag{26}
\]

which proves `(9)` uniformly in the complete future heat history and uniformly in the finite shift `rho`.

For XF-135, its logarithmic-jet estimate contributes only the additional factor

\[
\frac{8j!e^{d_\sigma}}{m_\sigma d_\sigma^j}
\tag{27}
\]

on top of `e^B A_{M,r}`. Uniformly for `1<=j<=J_N`, the logarithm of `(27)` is `O(J_N log(J_N+2))=o(N)`. Equations `(7)`--`(8)` therefore give `(12)`, and the smallness condition needed to choose the logarithm branch is automatically satisfied for large `N`.

## 4. In physical coordinates the blind patch has nearly quarter-period diameter

The XF-067 physical coordinate is

\[
w=-e^{-2\pi iz/L},
\qquad
\zeta_{\beta,N}=-e^{\beta/N},
\tag{28}
\]

so on the principal local chart

\[
z=\frac{i\beta L}{2\pi N}.
\tag{29}
\]

Therefore `(8)` contains every fixed disk

\[
\boxed{
|z|
\le
\left(
\frac{b_*}{2\pi}-\varepsilon
\right)L
}
\tag{30}
\]

for arbitrary fixed `epsilon>0`. Numerically,

\[
\boxed{
\frac{b_*}{2\pi}
=0.1241037942\ldots .
}
\tag{31}
\]

The blind disk can therefore have diameter arbitrarily close to

\[
\boxed{
\frac{b_*}{\pi}L
=0.2482075883\ldots L,
}
\tag{32}
\]

almost one quarter of the whole period. The previously recorded radius `log(2)L/(4 pi)=0.0551589...L` was smaller by a factor `2.2499...`.

This matters qualitatively for the next gate. The obstruction is no longer confined to a visibly tiny neighborhood of the off-circle probe: a single transition-sharp central packet defeats complete future function values and subexponential logarithmic jets on a genuinely large macroscopic patch. Any target-side repair that still relies only on enlarging the same local patch must now cross at least the scale `(30)` before this particular counterexample ceases to certify exponential blindness.

## 5. Scope, prior-art audit, and next gate

Equation `(22)` is deliberately scoped. It says that `b_*` is the best exponential aperture obtainable from the **existing XF-133 central quadratic divided-difference packet and the amplitude envelope `A_(M,r)`**. It does not prove that observation beyond `(30)` is stable, nor that a different packet cannot hide on a larger fraction of the period. It also does not address the source-specific accessibility question: the matched controls are exact periodic unit-circle heat trajectories, not a proof that Xi itself contains this central packet direction.

A targeted prior-art search checked literature on divided differences of clustered exponential families, Riesz-basis/moment methods for spectral condensation, and standard Lambert-W optimization. Those areas contain the general ingredients separately, but the present calculation uses no external theorem beyond standard factorial asymptotics and does not rely on a literature result for the Xi-flow conclusion. No source anchor is therefore added to `SOURCES.md`, and no novelty claim is made beyond the explicit internal optimization of the already-derived XF-133--XF-135 control family.

The frontier is now cleaner. There are three genuinely different ways forward: prove a source-specific constraint that excludes the central packet, construct a target observable whose effective spatial reach is global enough to beat the optimized packet, or find a different matched control whose exponential aperture exceeds `b_*`. Merely increasing a fixed local patch modestly, taking complete future time history, taking logarithms or dividing by a common analytic reference, and adding any subexponential logarithmic jet order remain insufficient on the matched-control class.

## Conclusion

The `r=M/3` choice in XF-133--XF-135 hid a large exponential reserve. Optimizing the exact factorial amplitude gives the closed-form constant

\[
\boxed{
b_*=\frac12\sqrt{W_0(2)(2+W_0(2))}=0.7797671361\ldots,}
\]

with optimal depth `r≈0.546705M`. The same transition-sharp controls are therefore exponentially indistinguishable, throughout their complete future heat histories, on physical disks of radius almost `0.1241L`; their blind diameter is almost `0.2482L`. This is the sharp aperture of the current central-packet envelope and more than doubles the quantitative spatial frontier left by XF-135.