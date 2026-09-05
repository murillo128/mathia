# XF-045 — centered far-tail shape forcing has quadratic buffer suppression

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `STRUCTURAL/THRESHOLD`. XF-043 bounded the remote contribution to a finite block's shape equation by estimating the far gap-velocity tail itself, giving a normalized memory-scale floor `O(core span / buffer width)`. That estimate is valid but not sharp for shape. The shape vector has zero mean, and the exact far-tail velocity contains an additional positive diagonal sink. Keeping both cancellations yields one more power of the core-to-buffer ratio.

Let

\[
I=\{a,\ldots,a+N-1\},\qquad
\bar g=\frac1N\sum_{i\in I}g_i,\qquad
\nu_i=g_i-\bar g,
\qquad
r_I^2=\sum_{i\in I}\nu_i^2,
\tag{1}
\]

on a real-simple Xi-flow slice, and assume the core upper envelope

\[
0<g_i\le b_*\ll \frac1{\log T}
\qquad(i\in I).
\tag{2}
\]

Let the remote tails start at fixed gap labels `K_-<a` and `K_+>=a+N`, with physical separation at least `D` from the two ends of the core as in XF-043. Write

\[
S_I:=x_{a+N}-x_a=\sum_{i\in I}g_i\le Nb_*.
\tag{3}
\]

For

\[
D=R(T)\log T,
\qquad R(T)\to\infty,
\qquad D=o(T),
\tag{4}
\]

the exact remote contribution `R_far` to the centered shape energy satisfies the **one-sided** estimate

\[
\boxed{
\mathcal R_{\rm far}
\le
C\,\frac{r_I\sqrt N\,S_I}{D^2},
}
\tag{5}
\]

with an absolute/source-uniform constant after fixing the envelope constant in (2). No pointwise upper or lower bound on remote gaps is used. Consequently the XF-042 finite-window inequality sharpens to

\[
\boxed{
D^+r_I
\le
-\lambda_I r_I
+F_I^{\rm near}
+O\!\left(\frac{\sqrt N\,S_I}{D^2}\right),
\qquad
\lambda_I=\frac{2N}{b_*^2(N-1)^2}.
}
\tag{6}
\]

After source normalization `s\asymp 1/log T`, `A_I=r_I/(s\sqrt N)`, and `b_*\le Cs`, the remote-tail stationary floor is therefore

\[
\boxed{
A_{I,{\rm far}\text{-}{\rm floor}}
\ll_C
\left(\frac{Ns}{D}\right)^2.
}
\tag{7}
\]

At the full heat-memory scale `N=O(log^2 T)` and the source-valid buffer `D=R(T)log T`, this is

\[
\boxed{
A_{I,{\rm far}\text{-}{\rm floor}}
=O(R(T)^{-2}),
}
\tag{8}
\]

rather than the coarse `O(R(T)^-1)` floor of XF-043.

The improvement is structurally important after XF-044. A memory-wavelength slow mode repeated across the `M=R(T)log^2 T` source buffer has borderline triple-flux amplitude `Theta(R^-2)` in tangent response. Thus **the genuinely remote tail no longer sits one factor `R` above the inverse-buffer flux threshold**. The remaining precision obstruction is pushed into the near buffer and into the distinction between `O(R^-2)` and the positive little-`o(R^-2)` gate; the XF-044 slow-mode clock remains relevant to any larger residual supplied there.

## 1. Exact endpoint-minus-sink decomposition of the far velocity

XF-014 gives the absolutely convergent gap equation

\[
g_i'=2\sum_{k\ne i}c_{ik}(g_k-g_i),
\qquad
c_{ik}=\frac1{(x_i-x_k)(x_{i+1}-x_{k+1})}>0,
\tag{9}
\]

and the exact differenced-force identity

\[
\boxed{
c_{ik}(g_k-g_i)
=\frac1{x_{i+1}-x_{k+1}}
-\frac1{x_i-x_k}.
}
\tag{10}
\]

For the right remote tail set

\[
A_i^+
:=\sum_{k\ge K_+}c_{ik}(g_k-g_i).
\tag{11}
\]

Shift the first sum in (10) by one index. Absolute convergence permits the rearrangement and gives

\[
\begin{aligned}
A_i^+
&=
\frac1{x_{K_+}-x_i}
+\sum_{\ell\ge K_++1}
\left(
\frac1{x_{i+1}-x_\ell}
-\frac1{x_i-x_\ell}
\right)\\
&=
\boxed{
E_i^+-g_iW_i^+
},
\end{aligned}
\tag{12}
\]

where

\[
E_i^+:=\frac1{x_{K_+}-x_i},
\qquad
W_i^+
:=\sum_{\ell\ge K_++1}
\frac1{(x_\ell-x_i)(x_\ell-x_{i+1})}>0.
\tag{13}
\]

The left tail is identical after reversing indices:

\[
\boxed{
A_i^-=E_i^--g_iW_i^-
}
\tag{14}
\]

with

\[
E_i^-:=\frac1{x_{i+1}-x_{K_-+1}},
\qquad
W_i^-
:=\sum_{\ell\le K_-}
\frac1{(x_i-x_\ell)(x_{i+1}-x_\ell)}>0.
\tag{15}
\]

Define

\[
E_i:=E_i^++E_i^-,
\qquad
W_i:=W_i^++W_i^-,
\qquad
A_i^{\rm far}=E_i-g_iW_i.
\tag{16}
\]

This is stronger information than the absolute tail bound used in XF-043. The endpoint field `E_i` is paired with an explicitly positive conductance mass `W_i`; it is not a free additive forcing.

## 2. Centering converts the `g_i W_i` term into a favorable sink

Let

\[
Q_I:=\frac12r_I^2.
\tag{17}
\]

As in XF-043, the exact far-tail contribution to `Q_I'` is

\[
\mathcal R_{\rm far}
=2\sum_{i\in I}\nu_i A_i^{\rm far}.
\tag{18}
\]

Insert `g_i=\bar g+\nu_i` into (16):

\[
\begin{aligned}
\mathcal R_{\rm far}
={}&2\sum_{i\in I}
\nu_i(E_i-\bar gW_i)
-2\sum_{i\in I}W_i\nu_i^2.
\end{aligned}
\tag{19}
\]

The second term is nonpositive. Set

\[
C_i:=E_i-\bar gW_i.
\tag{20}
\]

Because `sum_i nu_i=0`, any constant component of `C` also disappears:

\[
\sum_i\nu_iC_i
=
\sum_i\nu_i(C_i-c)
\tag{21}
\]

for arbitrary `c`. Therefore

\[
\boxed{
\mathcal R_{\rm far}
\le
2r_I\sqrt N\,\operatorname{osc}_{i\in I}C_i.
}
\tag{22}
\]

The remote shape forcing is controlled by the **variation** of the endpoint-minus-sink field across the core, not by its `O(1/D)` absolute magnitude. This is the missing cancellation in the XF-043 estimate.

A useful stress test is the arithmetic lattice. There, for a tail aligned with the lattice, `E_i=sW_i` exactly, so `C_i=0` when `\bar g=s`; the remote tail produces no shape forcing at all. Equation (19), rather than a raw `|A_i^{far}|` bound, records that cancellation correctly.

## 3. The endpoint field varies only by `O(S_I/D^2)`

The cutoff hypotheses imply that every denominator in `E_i^+` and `E_i^-` is at least `D` throughout the core. Hence for any `i,j in I`, the mean-value theorem gives

\[
|E_i^+-E_j^+|
\le
\frac{|x_i-x_j|}{D^2}
\le
\frac{S_I}{D^2},
\tag{23}
\]

and similarly

\[
|E_i^--E_j^-|
\le
\frac{|x_{i+1}-x_{j+1}|}{D^2}
\le
\frac{S_I}{D^2}.
\tag{24}
\]

Thus

\[
\boxed{
\operatorname{osc}_I E
\le
\frac{2S_I}{D^2}.
}
\tag{25}
\]

This is the elementary multipole gain: after the constant mode is removed, a field created at distance `D` changes across a core of span `S_I` only at first derivative scale `S_I/D^2`.

## 4. The positive tail mass has the same Lipschitz scale after source counting

It remains to control the variation of `W_i`. Consider the right tail. For a fixed remote zero `x_\ell`, define

\[
f_\ell(u,v)
:=\frac1{(x_\ell-u)(x_\ell-v)}.
\tag{26}
\]

Along the core all distances to the right tail are at least the distance `d_\ell` from `x_\ell` to the right core edge, with `d_\ell\ge D`. The two partial derivatives of `f_\ell` have magnitude at most `d_\ell^{-3}`. Since both endpoint coordinates of a core gap move by at most `S_I` when `i` is replaced by `j`, the mean-value theorem gives

\[
|f_\ell(x_i,x_{i+1})-f_\ell(x_j,x_{j+1})|
\le
\frac{2S_I}{d_\ell^3}.
\tag{27}
\]

Therefore

\[
\operatorname{osc}_I W^+
\le
2S_I\sum_{\ell\ge K_++1}\frac1{d_\ell^3}
\le
\frac{2S_I}{D}
\sum_{\ell\ge K_++1}\frac1{d_\ell^2}.
\tag{28}
\]

XF-043 already derives from the Rodgers--Tao global count, uniformly in the real-simple regime,

\[
\sum_{d_\ell\ge D}\frac1{d_\ell^2}
\ll
\frac{\log T}{D}
+\frac{\log^2T}{D^2}
+\frac{\log T}{T}.
\tag{29}
\]

Hence

\[
\operatorname{osc}_I W^+
\ll
S_I\left(
\frac{\log T}{D^2}
+\frac{\log^2T}{D^3}
+\frac{\log T}{TD}
\right).
\tag{30}
\]

The left tail satisfies the same estimate. Since `\bar g\le b_*\ll1/log T`, equations (4) and (30) imply

\[
\boxed{
\bar g\,\operatorname{osc}_I W
\ll
\frac{S_I}{D^2}.
}
\tag{31}
\]

Indeed the second term in (30) gains the additional factor `log T/D=1/R(T)`, while the last is dominated because `D=o(T)`. Combining (25) and (31) yields

\[
\boxed{
\operatorname{osc}_I C
\ll
\frac{S_I}{D^2}.
}
\tag{32}
\]

Substituting (32) into (22) proves (5).

No remote-gap envelope entered this argument. The only source input beyond the exact zero-motion algebra is precisely the reciprocal-square far-tail count already established in XF-043 from the Rodgers--Tao global zero-counting theorem.

## 5. Quadratic normalized floor

Combine (5) with the internal Cauchy coercivity and near-zone organization of XF-042. Dropping only favorable terms gives

\[
Q_I'
\le
-2\mu_Ir_I^2
+r_IF_I^{\rm near}
+O\!\left(\frac{r_I\sqrt N S_I}{D^2}\right),
\qquad
\mu_I=\frac{N}{b_*^2(N-1)^2}.
\tag{33}
\]

Dividing by `r_I` in the ordinary sense when positive, and in the upper-Dini sense at zero, gives (6).

Normalize with a source spacing `s\asymp1/log T` and assume `b_*\le Cs`. Then

\[
D^+A_I
\le
-\lambda_IA_I
+\frac{F_I^{\rm near}}{s\sqrt N}
+O_C\!\left(\frac{S_I}{sD^2}\right).
\tag{34}
\]

If the near forcing is suppressed, Duhamel gives a remote equilibrium floor

\[
A_{I,{\rm far}\text{-}{\rm floor}}
\ll_C
\frac{S_I}{sD^2\lambda_I}.
\tag{35}
\]

Using `S_I\le Nb_*`, `b_*\le Cs`, and

\[
\lambda_I^{-1}
=\frac{b_*^2(N-1)^2}{2N},
\tag{36}
\]

we obtain

\[
\boxed{
A_{I,{\rm far}\text{-}{\rm floor}}
\ll_C
\frac{N^2s^2}{D^2}
=
\left(\frac{Ns}{D}\right)^2,
}
\tag{37}
\]

which is (7).

At `N=O(log^2 T)` the source-scale core span is `Ns=O(log T)`. With `D=R(T)log T`, (37) gives (8). In contrast, XF-043 bounded the raw far velocity by `O(1/D)` before centering and therefore obtained only one power of `Ns/D`. Both statements are correct; (37) uses more of the exact shape structure and is the relevant bound for the centered relaxation problem.

## 6. Interaction with the XF-044 precision clock

XF-044 identifies the slowest memory-scale Cauchy mode at

\[
q\asymp\log^2T
\tag{38}
\]

and shows that, when repeated across the source buffer

\[
M=R(T)\log^2T,
\tag{39}
\]

the tangent triple-flux coefficient scales like `(M/q)^2\asymp R(T)^2`. Hence the borderline condition `M V_M=O(1)` corresponds to slow-mode amplitude

\[
|\varepsilon|=O(R(T)^{-2}),
\tag{40}
\]

while the positive `M V_M=o(1)` gate asks for `o(R^-2)` along that family.

Equation (8) now lands the **remote-tail forcing floor at exactly the same power**. Therefore the one-factor mismatch diagnosed in XF-044 is not intrinsic to the genuinely remote zeros; it came from the coarse absolute far-tail estimate available at the time. What remains is sharper and more local:

- the near buffer may still inject a memory-scale component larger than `R^-2`;
- an `O(R^-2)` remote contribution is only borderline, not enough by itself for the little-`o` positive gate;
- XF-044 still proves that any residual of size `1/R` at memory wavelength cannot be reduced to `1/R^2` by bounded-time universal Cauchy damping alone.

Thus the next constructive question is no longer whether the infinite remote tail is one power too large. It is whether the **near-buffer contribution admits an analogous centering/summation-by-parts gain**, or whether source information supplies the additional little-`o` needed at the critical `R^-2` scale.

## 7. Stress tests and hard boundary

The estimate is one-sided because the diagonal term in (19) is favorable. Taking an absolute value of the full remote contribution would throw away exactly the mechanism being proved. This is appropriate for the Lyapunov/relaxation inequality but should not be reinterpreted as an `L^infinity` bound on the far gap velocities themselves.

The core upper envelope (2) is still substantive. It is used twice: in the Cauchy coercivity `lambda_I` and to convert the oscillation of `W_i` into (31). No lower core gap bound is needed. As in XF-042/XF-043, no autonomous finite-window maximum principle supplies this envelope; a time-integrated application must justify it on the interval in question.

The result does not control `F_I^{near}`. In fact the improvement makes the near zone more clearly the dominant unresolved object. A neighboring gap just outside the core is not at distance `D`, so the multipole gain in (25)--(32) cannot be applied to it without a nested-buffer or taper argument.

The result also does not prove `Lambda=0`, exclude the XF-044 slow mode from the actual Xi zeros, or establish `M V_M=o(1)`. It only removes a previously quantified remote precision gap in the source-faithful real-simple regime.

Finally, the quadratic ratio in (37) is not asserted sharp. On an exact lattice the remote shape forcing vanishes identically, so additional source-specific cancellation could improve it further. Conversely, without using more than centering, the positive sink, the core envelope, and the reciprocal-square source count, the present argument gives no little-`o` gain over `(Ns/D)^2`.

## 8. Prior-art and novelty boundary

Removing the constant mode before estimating a distant nonlocal field is classical multipole/mean-zero analysis, and far-field localization estimates for nonlocal and fractional operators form a broad established literature. A targeted search around mean-zero fractional-Laplacian tails, nonlocal localization errors, and Cauchy-kernel commutators did not identify an external theorem that is load-bearing for (12)--(37), and no novelty is claimed for the general principle that centering gains a spatial derivative of a distant kernel.

The Mathia-local content is the exact way that principle interacts with the de Bruijn--Newman gap equation: the shifted-index identity (12)--(16) exposes a positive diagonal sink, the shape constraint `sum nu_i=0` removes the endpoint monopole, and the Rodgers--Tao reciprocal-square tail estimate turns the remaining variation into the quadratic buffer floor (37). Rodgers--Tao and the nonlocal Cauchy prior-art anchors needed for that interpretation are already recorded in `research/xi_flow/SOURCES.md`; no new external theorem is required, so `SOURCES.md` is unchanged.

## 9. Consequence for `xi_flow`

The far-tail branch has crossed the precision barrier that XF-044 left open by one power of `R`: after the exact centered decomposition, remote replenishment reaches the **borderline** memory-scale flux precision without waiting for an additional logarithmic Cauchy-relaxation clock. This does not yet enter the positive little-`o` regime.

The highest-value continuation is therefore local to the buffer. One should test whether the near-zone interaction can be organized by nested centering, overlap/discriminant summation by parts, or another source-sensitive cancellation so that its memory-scale component is `o(R^-2)`. A negative result would need a source-compatible near-buffer configuration that sustains an order-`R^-2` or larger slow component despite the favorable far-tail sink and the exact nonlinear gap dynamics.