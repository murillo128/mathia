# WI-325 — endpoint carrier resonance survives snapping to actual zeta-zero ordinates

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE`.

WI-324 exhibited an explicit near-Riemann--Siegel endpoint family

\[
U_M=2\pi M\left(M+\frac12\right),
\qquad X_M=M,
\]

for which the bare logarithmic carrier `n^{iU_M}` has a coherent block of length `\asymp M^{1/3}`. Its main stated boundary was that `U_M` was an artificial height rather than an actual zeta-zero ordinate, leaving open the possibility that membership in the zero set itself might impose enough Diophantine nonresonance to kill the carrier.

That escape does not survive the explicit Riemann--von Mangoldt error term. Hasanalizade--Shen--Wong's zero-count bound implies that every sufficiently high interval of length `2` contains a nontrivial zeta zero. Hence each `U_M` can be moved forward by at most `2` to an actual zero ordinate `\gamma_M`, while the induced perturbation of the WI-324 carrier on its `M^{1/3}` coherent block is only `O(M^{-2/3})` in phase. The same sector argument therefore gives

\[
\boxed{
\left|\sum_{0\le j<L_M}
 e\!\left(\frac{\gamma_M}{2\pi}
 \log\frac{M+j}{M}\right)\right|
\ge \frac{L_M}{2},
\qquad
L_M=\left\lfloor\frac{M^{1/3}}4\right\rfloor,
}
\]

for all sufficiently large `M`, with `\gamma_M` the ordinate of an actual nontrivial zeta zero and

\[
2\pi M\left(M+\frac12\right)<\gamma_M
\le 2\pi M\left(M+\frac12\right)+2.
\]

Thus **actual-zero-ordinate membership by itself does not remove the endpoint cubic carrier resonance**. Any successful refinement of the distinguished-bow route that uses the fact that its height is a zeta zero must exploit additional information: off-critical status, joint bow geometry, a zeta-value/phase relation stronger than ordinate membership, local zero configuration, or signed arithmetic cancellation in the von-Mangoldt coefficients.

This does **not** produce an actual off-line bow and does not show that the full prime-weighted source sum is large. The snapped zero may lie on the critical line, and the arithmetic coefficients can still cancel a coherent bare carrier. The result closes only the weaker proposed route in which zero-ordinate membership itself was expected to furnish the missing nonresonance.

## 1. An explicit fixed vertical interval always contains a zero

Let

\[
F(T):=\frac{T}{2\pi}\log\frac{T}{2\pi e}.
\]

Hasanalizade, Shen and Wong prove

\[
\left|N(T)-F(T)\right|
\le
E(T):=
0.1038\log T+0.2573\log\log T+9.3675
\tag{1}
\]

for `T\ge e`, where `N(T)` counts nontrivial zeros with `0<\Im\rho\le T`, with multiplicity. Since

\[
F'(t)=\frac1{2\pi}\log\frac{t}{2\pi},
\]

we have

\[
F(T+2)-F(T)
\ge
\frac1\pi\log\frac{T}{2\pi}.
\tag{2}
\]

Consequently

\[
\begin{aligned}
N(T+2)-N(T)
&\ge F(T+2)-F(T)-E(T+2)-E(T)\\
&\ge
\left(\frac1\pi-0.2076\right)\log T
-0.5146\log\log T+O(1).
\end{aligned}
\tag{3}
\]

The leading coefficient is strictly positive. Indeed the classical inequality `\pi<22/7` gives

\[
\frac1\pi-0.2076
>
\frac7{22}-\frac{519}{2500}
=
\frac{3041}{27500}>0.
\tag{4}
\]

Hence the right-hand side of (3) tends to `+\infty`. Therefore there exists `T_0` such that

\[
\boxed{N(T+2)-N(T)\ge1\qquad(T\ge T_0).}
\tag{5}
\]

In particular, every sufficiently high interval `(T,T+2]` contains the ordinate of at least one nontrivial zeta zero. No RH input is used.

## 2. Snap the WI-324 resonant heights to the zero set

For an integer `M` put

\[
A_M=M\left(M+\frac12\right),
\qquad
U_M=2\pi A_M.
\tag{6}
\]

For all sufficiently large `M`, apply (5) at `T=U_M`. Choose a nontrivial zero `\rho_M` with ordinate `\gamma_M` satisfying

\[
U_M<\gamma_M\le U_M+2.
\tag{7}
\]

Write

\[
\frac{\gamma_M}{2\pi}=A_M+\delta_M,
\qquad
0<\delta_M\le\frac1\pi.
\tag{8}
\]

The endpoint normalization is unchanged at leading and first correction order:

\[
\frac{\gamma_M}{M^2}
=
2\pi\left(1+\frac1{2M}\right)+O(M^{-2})
\longrightarrow2\pi
\tag{9}
\]

from above. The direct logarithmic dual length is

\[
Y_M=\frac{\gamma_M}{2\pi M}
=M+\frac12+\frac{\delta_M}{M},
\tag{10}
\]

so the source/dual geometry remains asymptotically self-dual exactly as in WI-323--WI-324.

The count-saturating source parametrization can also be kept exact. If

\[
c_M:=\frac{2\pi\log\gamma_M}{\log M},
\qquad
\alpha_M:=\frac{2\pi}{c_M},
\tag{11}
\]

then

\[
\gamma_M^{\alpha_M}=M.
\tag{12}
\]

Moreover

\[
\frac{c_M}
{4\pi\log\gamma_M/\log(\gamma_M/(2\pi))}
=
\frac{
\log(\gamma_M/(2\pi))
}{2\log M}
>1,
\tag{13}
\]

because `\gamma_M/(2\pi)>M(M+1/2)>M^2`. Thus snapping to an actual zero ordinate does not leave the source-compatible reciprocal-scale regime isolated in WI-322.

## 3. The cubic coherent block is stable under the snap

Use `e(x)=\exp(2\pi i x)` and define the relative carrier at the snapped height by

\[
C'_M(j):=
 e\!\left(
 (A_M+\delta_M)\log\left(1+\frac jM\right)
 \right).
\tag{14}
\]

WI-324 proved the exact decomposition

\[
A_M\log\left(1+\frac jM\right)
=
Mj-\frac{j(j-1)}2+\theta_{M,j},
\tag{15}
\]

where the first two terms are integers for integral `j`, and for

\[
0\le j<L_M,
\qquad
L_M:=\left\lfloor\frac{M^{1/3}}4\right\rfloor,
\tag{16}
\]

one has

\[
|\theta_{M,j}|\le\frac3{128}.
\tag{17}
\]

The snap changes the residual phase by only

\[
\delta_M\log\left(1+\frac jM\right).
\]

Using `\log(1+x)\le x`, (8), and (16),

\[
0\le
\delta_M\log\left(1+\frac jM\right)
\le
\frac{j}{\pi M}
\le
\frac{1}{4\pi M^{2/3}}.
\tag{18}
\]

Since `\pi>3`, equations (17)--(18) give, already with a deliberately crude uniform bound,

\[
\left|
\theta_{M,j}
+\delta_M\log\left(1+\frac jM\right)
\right|
<
\frac3{128}+\frac1{12}
=
\frac{41}{384}
<\frac16.
\tag{19}
\]

Hence every `C'_M(j)` in the block lies in the sector `|\arg z|<\pi/3`, so

\[
\Re C'_M(j)>\frac12.
\tag{20}
\]

Summing (20) proves

\[
\boxed{
\left|\sum_{j=0}^{L_M-1} C'_M(j)\right|
\ge
\Re\sum_{j=0}^{L_M-1} C'_M(j)
>
\frac{L_M}{2}.
}
\tag{21}
\]

Thus the `M^{1/3}` cubic resonance of WI-324 is not an artifact of having chosen an artificial real height. It persists after a bounded perturbation, and the explicit zero-count theorem supplies such a perturbation landing on the actual zeta zero set for every sufficiently large `M`.

## 4. What this rules out, and what it does not

The new obstruction is deliberately narrow but decisive. WI-324 left open the possibility that the distinguished twist might be saved by an arithmetic statement of the schematic form

\[
\text{``if }U\text{ is a zeta-zero ordinate, then the endpoint carrier cannot resonate.''}
\]

Equations (5)--(21) refute that possibility when the hypothesis means only **membership of the ordinate in the zero set**. There are actual zeta-zero ordinates arbitrarily high, in fact one in each of the snapped intervals constructed above, at which the same coherent endpoint carrier survives.

This does not instantiate the full bow model. In particular:

- the zero `\rho_M` supplied by the count may be critical or off-critical;
- no selected off-line population with Maynard--Pratt bow geometry is constructed;
- the result concerns the bare logarithmic phase, not the signed coefficient sequence `\Lambda-\Lambda^\sharp` from the Gallagher source problem;
- global Riemann--Siegel cancellation can coexist with a coherent short block;
- no lower bound for the distinguished twisted prime covariance follows.

Therefore the live branch after WI-322--WI-324 is sharpened rather than closed: **any use of the actual distinguished height must exploit more than zero-ordinate membership**. Viable additional information could be off-line status, a relation tying the selected bow zero to neighboring zeros, a source-side identity using `\zeta(\rho)=0`, or direct arithmetic cancellation for the von-Mangoldt-weighted carrier.

## 5. Prior art and novelty audit

The zero-count input is established literature, not new mathematics here:

- Elchin Hasanalizade, Quanli Shen and Peng-Jie Wong, *Counting zeros of the Riemann zeta function*, Journal of Number Theory 235 (2022), 219--241, arXiv:2107.06506, DOI `10.1016/j.jnt.2021.06.032`. Their explicit bound is equation (1); the source is already anchored in `research/weil_inertia/SOURCES.md` for WI-232.
- The logarithmic Taylor resonance and its `M^{1/3}` coherent block are the exact Mathia result WI-324; WI-323 supplies the source-compatible self-dual interpretation.

The fixed-length zero-existence consequence (5) is an elementary deduction from the published explicit Riemann--von Mangoldt error, and the stability estimate (18)--(21) is elementary once WI-324 is available. The substantive delta is their combination: it removes WI-324's artificial-height caveat at the level of **zero-ordinate membership** while preserving all stronger caveats needed by the actual bow problem.

A bounded internal and external audit did not locate a source asserting this exact line-specific snapping consequence. That absence is not used as a priority claim. The classical ingredients remain attributed as above; only the derived obstruction for the WI-324 endpoint-resonance escape is recorded as Mathia's contribution.

## Research consequence

Do not spend further effort trying to obtain bow de-exceptionalization from a generic Diophantine nonresonance principle that assumes only `U=\Im\rho`. The exact zero set is vertically dense enough, at bounded scale, to intersect the WI-324 resonant neighborhoods while the cubic coherent block is stable under those bounded perturbations. The next admissible step must use information that distinguishes the **particular off-line bow zero and its arithmetic source** from an arbitrary zero ordinate.