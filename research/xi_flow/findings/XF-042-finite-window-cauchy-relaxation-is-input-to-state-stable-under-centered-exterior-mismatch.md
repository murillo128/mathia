# XF-042 — finite-window Cauchy relaxation is input-to-state stable under centered exterior mismatch

**Status:** `EXACT-DERIVED` + `NONLINEAR-FORCED-RELAXATION` + `STRUCTURAL/BOUNDARY`. XF-041 proves nonlinear Cauchy spectral-gap damping for periodic gap controls, where quotienting by the period removes all exterior flux. Periodicity is not needed for the internal damping mechanism. On an arbitrary finite block of the exact real-simple Xi gap dynamics, the block shape satisfies a forced contraction inequality at the same `1/(N s^2)` Cauchy relaxation scale. The forcing is not the full exterior field: after the moving block mean is removed, only the **centered variation of the exterior gap-mismatch field** can replenish shape variance. Exterior coupling to gaps equal to the block mean is purely dissipative.

This makes the remaining boundary obstruction quantitative. A short finite block can sustain a nonconstant gap pattern only if its exterior generates nonuniform mismatch forcing at a rate comparable to the block's nonlinear Cauchy spectral gap. Thus XF-041's alternatives “exterior replenishment or genuinely longer wavelength” can be stated as an exact input-to-state condition rather than only as a qualitative boundary warning.

## 1. Exact finite-window shape equation

Work on a real-simple slice on which XF-014 gives the absolutely convergent gap equation

\[
g_i'
=2\sum_{k\ne i}c_{ik}(g_k-g_i),
\qquad
c_{ik}=c_{ki}
=\frac1{(x_i-x_k)(x_{i+1}-x_{k+1})}>0.
\tag{1}
\]

Fix a finite interval of gap indices

\[
I=\{a,a+1,\ldots,a+N-1\},
\qquad N\ge2,
\tag{2}
\]

and let

\[
\bar g_I:=\frac1N\sum_{i\in I}g_i,
\qquad
u_i:=g_i-\bar g_I,
\qquad
r_I:=\left(\sum_{i\in I}\nu_i^2\right)^{1/2}.
\tag{3}
\]

Then `sum_{i in I} nu_i=0`. Split (1) into interactions inside and outside `I`. Define

\[
w_i^{\rm out}
:=\sum_{k\notin I}c_{ik},
\tag{4}
\]

and the exterior mismatch field relative to the instantaneous block mean

\[
\boxed{
B_i^{\rm out}
:=2\sum_{k\notin I}c_{ik}(g_k-\bar g_I).
}
\tag{5}
\]

For the Xi zero set these sums are absolutely convergent on every real-simple slice. Indeed XF-014 proves absolute convergence of `sum c_ik |g_k-g_i|`, while `sum c_ik<infinity` follows from the same zero-location growth and the inverse-square tail of the conductances.

Since `g_k-g_i=(g_k-\bar g_I)-\nu_i`, equation (1) becomes, for `i in I`,

\[
g_i'
=2\sum_{\substack{j\in I\\j\ne i}}c_{ij}(\nu_j-\nu_i)
+B_i^{\rm out}-2w_i^{\rm out}\nu_i.
\tag{6}
\]

The internal pair terms sum to zero over `I`; hence the motion of `\bar g_I` is entirely determined by the exterior terms. Subtracting that mean motion gives the exact forced shape equation. For the energy argument it is cleaner not to write the mean derivative explicitly: because `sum nu_i=0`, differentiation of

\[
Q_I:=\frac12r_I^2=\frac12\sum_{i\in I}(g_i-\bar g_I)^2
\tag{7}
\]

gives simply `Q_I'=sum_i nu_i g_i'`.

## 2. The exterior splits into a favorable sink plus a centered mismatch input

Insert (6) into the derivative of (7) and symmetrize the internal pairs. One obtains the exact identity

\[
\boxed{
\begin{aligned}
Q_I'
={}&-2\sum_{\substack{i<j\\i,j\in I}}
c_{ij}(\nu_i-\nu_j)^2
-2\sum_{i\in I}w_i^{\rm out}\nu_i^2
+\sum_{i\in I}\nu_i B_i^{\rm out}.
\end{aligned}
}
\tag{8}
\]

Let

\[
\bar B_I^{\rm out}
:=\frac1N\sum_{i\in I}B_i^{\rm out},
\qquad
\widetilde B_i^{\rm out}
:=B_i^{\rm out}-\bar B_I^{\rm out}.
\tag{9}
\]

Because the shape vector has zero mean,

\[
\sum_{i\in I}\nu_i B_i^{\rm out}
=\sum_{i\in I}\nu_i\widetilde B_i^{\rm out}.
\tag{10}
\]

Thus a spatially constant component of the exterior mismatch field moves the block mean but does not feed its shape. More importantly, the diagonal term in (8) is always nonpositive. Coupling a block gap to exterior gaps equal to `\bar g_I` contributes only `-2w_i^{out}\nu_i^2`; it **strengthens** relaxation rather than acting as an adverse boundary flux.

The only potentially adverse input in (8) is therefore the centered field `\widetilde B^{out}`. This is a sharper organization than bounding the raw finite-block boundary term of XF-014 by absolute values.

## 3. Nonlinear Cauchy coercivity gives an input-to-state estimate

Assume that throughout a time interval `[t_0,t_1]` the block has an independently controlled upper gap envelope

\[
0<g_i(t)\le b_*
\qquad(i\in I).
\tag{11}
\]

No lower gap bound is assumed. For `i<j` in `I`, both position differences in the denominator of `c_{ij}` span `j-i` gaps contained in `I`, so XF-015 gives

\[
c_{ij}
\ge\frac1{b_*^2(j-i)^2}.
\tag{12}
\]

The elementary finite-block fractional Poincare estimate from XF-015 is

\[
\sum_{i<j}\frac{(\nu_i-\nu_j)^2}{(j-i)^2}
\ge
\frac{N}{(N-1)^2}
\sum_{i\in I}\nu_i^2.
\tag{13}
\]

Set

\[
\mu_I
:=\frac{N}{b_*^2(N-1)^2},
\qquad
\lambda_I:=2\mu_I
=\frac{2N}{b_*^2(N-1)^2}.
\tag{14}
\]

Dropping the favorable exterior sink in (8), applying (12)--(13), and using Cauchy--Schwarz gives

\[
Q_I'
\le
-2\mu_I r_I^2
+r_I\,\|\widetilde B^{\rm out}\|_{\ell^2(I)}.
\tag{15}
\]

Consequently, in the ordinary sense when `r_I>0` and in the upper-Dini sense at `r_I=0`,

\[
\boxed{
D^+r_I
\le
-\lambda_I r_I
+F_I,
\qquad
F_I:=\|\widetilde B^{\rm out}\|_{\ell^2(I)}.
}
\tag{16}
\]

Gronwall/Duhamel yields the finite-window input-to-state estimate

\[
\boxed{
r_I(t)
\le
e^{-\lambda_I(t-t_0)}r_I(t_0)
+\int_{t_0}^{t}e^{-\lambda_I(t-s)}F_I(s)\,ds.
}
\tag{17}
\]

This is fully nonlinear in the zero configuration. The conductances may vary arbitrarily in time, gaps may have finite contrast, and small gaps only strengthen the internal lower bound. The sole local geometric hypothesis used for the displayed constant is the upper envelope (11).

A time-dependent version is immediate: if `b(t)` is any upper bound for the gaps of `I`, replace `lambda_I` by

\[
\lambda_I(t)=\frac{2N}{b(t)^2(N-1)^2}
\tag{18}
\]

and use the corresponding integrating factor. The fixed `b_*` form is more useful for source-scale comparisons.

## 4. Persistence requires quantitative exterior replenishment

Equation (16) gives two equivalent ways to state the boundary burden. First, if for some `0<=theta<1`

\[
F_I(t)\le\theta\lambda_I r_I(t)
\qquad(t_0\le t\le t_1),
\tag{19}
\]

then

\[
\boxed{
r_I(t)
\le
r_I(t_0)
\exp\!\bigl(-(1-\theta)\lambda_I(t-t_0)\bigr).
}
\tag{20}
\]

So exterior influence that is small compared with the instantaneous Cauchy relaxation rate cannot preserve the shape.

Conversely, (17) gives a necessary integrated forcing condition. If

\[
r_I(t_1)\ge\rho\,r_I(t_0)
\qquad(0<\rho\le1),
\tag{21}
\]

then

\[
\boxed{
\int_{t_0}^{t_1}
e^{-\lambda_I(t_1-s)}F_I(s)\,ds
\ge
\bigl(\rho-e^{-\lambda_I(t_1-t_0)}\bigr)_+
r_I(t_0).
}
\tag{22}
\]

Thus once `lambda_I(t_1-t_0)` is large, persistence of a fixed fraction of the original gap-shape amplitude requires an order-one replenishment in the natural exponentially weighted input norm. This is not a heuristic statement that “the boundary might matter”; it is an exact necessary condition on the only exterior component capable of defeating the finite-window contraction estimate.

The estimate is conservative because (16) discarded the favorable sink `-2 sum w_i^{out} nu_i^2`. A configuration can therefore fail the forcing threshold (22) only more decisively; no adverse term was hidden in obtaining it.

## 5. Xi source scale: short finite blocks need strong nonuniform exterior forcing

Let the source spacing at height `T` be

\[
s=h_T\sim\frac{4\pi}{\log T},
\tag{23}
\]

and suppose an `N`-gap block remains in the finite-contrast regime

\[
b_*\le C s
\tag{24}
\]

for fixed `C`. Normalize the block shape and exterior input by

\[
A_I:=\frac{r_I}{s\sqrt N},
\qquad
\mathcal F_I:=
\frac{F_I}{s\sqrt N}.
\tag{25}
\]

Then (16) becomes

\[
D^+A_I
\le
-\lambda_I A_I+\mathcal F_I,
\tag{26}
\]

with

\[
\boxed{
\lambda_I
\ge
\frac{2N}{C^2s^2(N-1)^2}
=
\frac{N}{8\pi^2C^2(N-1)^2}
(\log T)^2\bigl(1+o(1)\bigr).
}
\tag{27}
\]

Hence the finite-window relaxation clock has the same characteristic scale

\[
\lambda_I^{-1}\asymp \frac{N}{(\log T)^2}
\tag{28}
\]

as the periodic Cauchy spectral gap in XF-041. The constant in (27) is deliberately elementary rather than sharp; the important point is the nonlocal `1/N` spectral scaling. A nearest-neighbor argument would instead lose a factor `N`.

Let `M=R(T)\log^2T` be the source buffer scale used in XF-035--XF-041, with `log M=O(log T)`. Under the relative forcing condition (19), an order-one normalized block shape reaches `A_I=O(M^{-2})` after

\[
\Delta t_*
\le
\frac{C^2s^2(N-1)^2}{2(1-\theta)N}
\bigl(2\log M+O_C(1)\bigr),
\tag{29}
\]

or, using (23),

\[
\boxed{
\Delta t_*
\le
\frac{16\pi^2C^2}{1-\theta}
\frac{(N-1)^2}{N}
\frac{\log M+O_C(1)}{(\log T)^2}
\bigl(1+o(1)\bigr).
}
\tag{30}
\]

Therefore

\[
\boxed{N=o(\log T)\quad\Longrightarrow\quad\Delta t_*=o(1)}
\tag{31}
\]

whenever the centered exterior mismatch remains a fixed fraction below the internal relaxation scale. This reproduces the source-scale separator of XF-041 **without periodic closure**.

Equivalently, a persistent short-block obstruction must violate (19): at some times its centered normalized exterior gap-mismatch input must be comparable to

\[
\lambda_I A_I
\asymp
\frac{(\log T)^2}{N}A_I
\tag{32}
\]

(up to the fixed finite-contrast constant). Periodicity in XF-041 set this input identically to zero after quotienting. The finite-window problem is therefore precisely the problem of controlling or ruling out this nonuniform exterior replenishment.

## 6. Stress tests and boundary of the claim

The result does **not** assert that `F_I` is small for the actual Xi flow. Near-boundary gaps outside `I` may create a large and highly nonuniform mismatch field, and unconditional zero counting alone has not yet been shown to control (5) at the inverse-buffer scale. Equation (22) is a necessary burden on a persistent obstruction, not its exclusion.

The upper envelope (11) must hold through the time interval. Unlike the periodic maximum in XF-041, the maximum of a finite block can be driven upward by its exterior, so no autonomous maximum principle supplies `b_*`. This is an explicit additional input. No lower gap bound is needed for the internal coercivity, but the real-simple ODE still stops at an actual collision.

The block consists of fixed gap labels. A window fixed in physical space would gain entry/exit terms and is not covered by (8). Likewise, the source-scale use of a fixed reference `s` in (25) is only a normalization at a given high-zero scale; the exact energy itself is centered at the evolving block mean and does not assume that mean is constant.

The Poincare constant in (13) is not claimed sharp. Improving it changes only constants in (27)--(30), not the `1/(N s^2)` clock. The periodic quotient has a larger exact constant because it reintroduces all translates across the boundary.

Finally, the mechanism remains universal for ordered one-dimensional logarithmic repulsion. Synthetic real-rooted heat flows inherit the same forced contraction estimate. It is therefore a structural boundary theorem, not an Xi-specific selector and not an upper bound for `Lambda`.

## 7. Prior-art and novelty boundary

Robust consensus and graph-Laplacian systems with external disturbances have a large classical control-theory literature, and input-to-state or `H_infinity` estimates for forced consensus are not treated as new analytic principles here. A targeted prior-art check also found no reason to reinterpret the elementary Duhamel estimate (17) as a new general theorem. Rodgers--Tao remain the primary source for the Xi zero ODE and the need for spatial cutoff/error control, while Guillin--Le Bris--Monmarche already delimit the broader one-dimensional repulsive-contraction mechanism; both are anchored in `SOURCES.md`.

No new external theorem is load-bearing, so `SOURCES.md` does not need expansion. The Mathia-local content is the exact identification, in the nonlinear de Bruijn--Newman gap coordinates, of the exterior quantity that can oppose the Cauchy shape relaxation: equations (5), (8), and (16) show that only the **centered exterior gap mismatch** acts as an adverse input, while the remaining exterior coupling is dissipative. Equations (22) and (32) then translate XF-041's qualitative “exterior replenishment” escape into a quantitative source-scale requirement.

## 8. Consequence for `xi_flow`

XF-041 showed that finite-contrast sub-`log T` periodic microstructure dies in vanishing heat time. XF-042 removes periodicity from the damping side of that statement. **Every finite `N`-gap block with an `O(1)` upper gap envelope has nonlinear Cauchy shape relaxation at rate `asymp 1/(N s^2)`; what can prevent that relaxation is a centered exterior mismatch input of comparable size.**

This isolates the next positive interface more sharply. A useful Xi theorem no longer needs to prove finite-window Cauchy damping from scratch. It needs to control `\widetilde B^{out}`—possibly after inserting a broad buffer/capacitary cutoff, exploiting translated zero counting, or separating short-wave content from the exterior field—well enough to satisfy a condition of the form (19) for sub-`log T` modes. Conversely, a matched control that keeps a short block irregular while explicitly meeting the lower forcing burden (22) would demonstrate that exterior replenishment is a genuine dynamical escape rather than merely a bookkeeping artifact.