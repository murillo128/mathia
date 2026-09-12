# NB-064 — persistent target leakage forces near-kernel forward-memory modes

**Status:** `EXACT-DERIVED + TARGET-SINGULAR-CONCENTRATION + NECESSARY-PERSISTENCE-CONDITION + ONE-STEP-MEMORY-OBSTRUCTION + FLAT-CONTROL + METHOD-ADVANCE`.

`NB-063` reduces the collective late-quotient problem to a one-cell memory operator

\[
\Gamma_R:\mathcal G_R\to\mathcal X_R^\circ
\tag{1}
\]

and the exact defect-capture law

\[
\delta_R^2-\delta_{R+1}^2
=
\left\langle
z_R,(I+\Gamma_R\Gamma_R^*)^{-1}z_R
\right\rangle,
\qquad
z_R=x_R^\circ-\Gamma_Rp_R,
\tag{2}
\]

where

\[
p_R=P_{\mathcal G_R}J_Rh_*,
\qquad
x_R=(J_{R+1}-J_R)h_*,
\qquad
x_R^\circ=P_{\mathcal X_R^\circ}x_R,
\tag{3}
\]

and

\[
\delta_R^2=\|P_{\mathcal T_R}h_*\|^2
=\|(I-J_R)h_*\|^2+\|p_R\|^2.
\tag{4}
\]

The remaining obstruction was that the canonical target might repeatedly align with the finite-dimensional forward-memory channel. The present finding sharpens that statement substantially. Since the capture increments in (2) must tend to zero and the physical target-cell norm `||x_R||` tends to zero, one always has

\[
\boxed{
\left\|
\Gamma_R(I+\Gamma_R^*\Gamma_R)^{-1/2}p_R
\right\|
\longrightarrow0.
}
\tag{5}
\]

Equivalently, with

\[
T_R:=\Gamma_R^*\Gamma_R,
\tag{6}
\]

\[
\boxed{
\left\langle
p_R,T_R(I+T_R)^{-1}p_R
\right\rangle
\longrightarrow0.
}
\tag{7}
\]

Thus the visible target component cannot asymptotically occupy any forward-memory singular sector whose singular values stay bounded away from zero.

If the collective tail really persists,

\[
\delta_\infty:=\lim_{R\to\infty}\delta_R>0,
\tag{8}
\]

then `||p_R|| -> delta_infty`, and the normalized target direction

\[
u_R:=\frac{p_R}{\|p_R\|}
\tag{9}
\]

must concentrate entirely in singular values of `Gamma_R` tending to zero. More precisely, for every fixed `eta>0`, if `E_R^{\ge eta}` is the spectral projection of `T_R` onto `[eta^2,infinity)`, then

\[
\boxed{
\|E_R^{\ge\eta}u_R\|\longrightarrow0.
}
\tag{10}
\]

There is even a moving near-kernel formulation: one can choose `eta_R -> 0` and unit vectors `v_R in G_R` such that

\[
\boxed{
\|u_R-v_R\|\to0,
\qquad
\|\Gamma_Rv_R\|\le\eta_R\to0.
}
\tag{11}
\]

Therefore a nonzero limiting collective defect can survive only if the **target-bearing visible direction itself becomes an approximate right-kernel vector of the canonical one-cell forward-memory operator**. Bad conditioning somewhere in `G_R`, or even a growing operator norm `||Gamma_R||`, is not enough. The bad singular directions must asymptotically capture the distinguished target projection.

## 1. Vanishing capture forces filtered forward-memory silence

Put

\[
c_R:=\delta_R^2-\delta_{R+1}^2\ge0.
\tag{12}
\]

The spaces `K_R` increase, so `delta_R^2` decreases to a finite limit. Hence

\[
c_R\longrightarrow0.
\tag{13}
\]

Also the cells `X_R` are mutually orthogonal and `h_* in H^2`, so

\[
\sum_{R\ge2}\|x_R\|^2\le\|h_*\|^2,
\qquad
\|x_R\|\longrightarrow0.
\tag{14}
\]

Let

\[
A_R:=(I+\Gamma_R\Gamma_R^*)^{-1/2}.
\tag{15}
\]

Equation (2) says exactly

\[
\|A_Rz_R\|^2=c_R.
\tag{16}
\]

Since `A_R` is a contraction and `Gamma_R p_R=x_R^circ-z_R`,

\[
\begin{aligned}
\|A_R\Gamma_Rp_R\|
&\le
\|A_Rx_R^\circ\|+\|A_Rz_R\|\\
&\le
\|x_R\|+\sqrt{c_R}
\longrightarrow0.
\end{aligned}
\tag{17}
\]

Functional calculus, or the polar decomposition of `Gamma_R`, gives the standard intertwining identity

\[
(I+\Gamma_R\Gamma_R^*)^{-1/2}\Gamma_R
=
\Gamma_R(I+\Gamma_R^*\Gamma_R)^{-1/2}.
\tag{18}
\]

Thus (17) proves (5). Squaring it gives

\[
\|A_R\Gamma_Rp_R\|^2
=
\left\langle
p_R,
\Gamma_R^*(I+\Gamma_R\Gamma_R^*)^{-1}\Gamma_Rp_R
\right\rangle
=
\left\langle
p_R,T_R(I+T_R)^{-1}p_R
\right\rangle,
\tag{19}
\]

which proves (7).

The filter in (7) is important. On a singular value `sigma`, its weight is

\[
\frac{\sigma^2}{1+\sigma^2}.
\tag{20}
\]

It behaves like `sigma^2` near zero but tends to `1` for large singular values. Consequently an arbitrarily large `||Gamma_R||` cannot make a substantial target component disappear from (7); only concentration near the kernel can do so.

## 2. Persistent leakage forces spectral concentration at zero

From (4), with

\[
\tau_R:=\|(I-J_R)h_*\|^2,
\qquad
\ell_R:=\|p_R\|^2,
\tag{21}
\]

we have

\[
\delta_R^2=\tau_R+\ell_R.
\tag{22}
\]

Because `J_R -> I` strongly,

\[
\tau_R\to0.
\tag{23}
\]

Under the persistence hypothesis (8), therefore

\[
\|p_R\|^2=\ell_R\longrightarrow\delta_\infty^2>0.
\tag{24}
\]

Normalize as in (9), and define

\[
q_R:=\left\langle
u_R,T_R(I+T_R)^{-1}u_R
\right\rangle.
\tag{25}
\]

Equations (7) and (24) give

\[
q_R\to0.
\tag{26}
\]

For fixed `eta>0`, the spectral multiplier in (20) is at least

\[
\frac{\eta^2}{1+\eta^2}
\tag{27}
\]

on the spectral sector `T_R>=eta^2`. Hence

\[
q_R
\ge
\frac{\eta^2}{1+\eta^2}
\|E_R^{\ge\eta}u_R\|^2,
\tag{28}
\]

and (10) follows.

This is stronger than the statement that the target makes a small angle with some poorly transmitted direction. For every fixed positive transmission threshold, **all** normalized target mass eventually leaves that sector.

## 3. The target direction actually has an approximate-kernel representative

The fixed-threshold statement can be diagonalized. Choose

\[
\eta_R:=\max\{q_R^{1/4},R^{-1}\},
\tag{29}
\]

so `eta_R -> 0`. Let `E_R^{<eta_R}` denote the spectral projection of `T_R` onto `[0,eta_R^2)`. Equation (28), with the moving threshold, gives

\[
\|(I-E_R^{<\eta_R})u_R\|^2
\le
\frac{1+\eta_R^2}{\eta_R^2}q_R
\longrightarrow0.
\tag{30}
\]

Indeed, if `eta_R=q_R^(1/4)`, the right side is `O(q_R^(1/2))`; if `eta_R=R^-1`, then `q_R<R^-4` and it is `O(R^-2)`.

For all large `R`, `E_R^{<eta_R}u_R` is therefore nonzero. Define

\[
v_R:=
\frac{E_R^{<\eta_R}u_R}
{\|E_R^{<\eta_R}u_R\|}.
\tag{31}
\]

Then

\[
\|u_R-v_R\|\to0,
\tag{32}
\]

while the spectral support of `v_R` gives

\[
\|\Gamma_Rv_R\|^2
=
\langle v_R,T_Rv_R\rangle
\le
\eta_R^2.
\tag{33}
\]

This proves (11). The near-kernel vectors are not arbitrary singular vectors selected after the fact: they asymptotically coincide with the normalized canonical target projection `p_R/||p_R||`.

## 4. A target-transversality criterion would now kill the persistent tail

The contrapositive is a concrete sufficient route. Suppose there exist constants `eta,kappa>0` and an unbounded sequence of `R` for which the normalized visible target has definite mass in the singular sector transmitted by at least `eta`,

\[
\|E_R^{\ge\eta}u_R\|\ge\kappa.
\tag{34}
\]

If `delta_infty` were positive, (10) would force the left side to tend to zero, a contradiction. Therefore

\[
\boxed{
(34)\quad\Longrightarrow\quad
\lim_{R\to\infty}\|P_{\mathcal T_R}h_*\|=0.
}
\tag{35}
\]

A uniform lower singular bound on `Gamma_R` would imply (34) whenever `p_R != 0`, but that is far stronger than necessary. It is enough to prove target-aware transversality: a fixed fraction of the distinguished direction `p_R` must repeatedly occupy a singular sector bounded away from zero.

This changes the next quantitative target. `NB-063` left two broad possibilities: control `||Gamma_R||`, or show that `z_R` cannot stay too small. The present result shows that **upper control of `||Gamma_R||` is not the intrinsic issue**. Under a persistent defect, target mass is forced toward the opposite end of the singular spectrum. A useful estimate should therefore lower-bound transmission specifically on `p_R`, or rule out concentration of `p_R` in the near-kernel spectral subspace.

## 5. Flat control and adversarial boundary

For the unit-outer control of `NB-056`, `NB-063` gives

\[
\Gamma_R^{(0)}=0.
\tag{36}
\]

Thus every visible direction is a kernel direction. The spectral concentration conclusion is then vacuous, while the actual collective target tail still tends to zero cubically. This is the correct negative control: **near-kernel concentration is necessary for persistent leakage, not sufficient for it**.

Likewise, (7) alone does not prove `p_R -> 0`. It only says that the part of `p_R` that can be transmitted through a singular value bounded away from zero vanishes. A source could in principle possess increasingly weak forward-memory modes and have the canonical target track them. Ruling out precisely that target tracking is now the remaining singular-geometric problem.

There is also no operator-norm claim. The proof never asserts `||Gamma_R|| -> 0`, a uniform lower singular value, norm convergence of the Hardy shift semigroup, or a frame bound for the whole causal family. It uses only the exact `NB-063` recursion, square summability of the fixed target cells, monotonicity of `delta_R`, and finite-dimensional spectral calculus on `G_R`.

## 6. Prior-art boundary

The spectral theorem, singular-value calculus, graph projections, and the implication from a vanishing quadratic form to concentration near the zero spectrum are standard finite-dimensional Hilbert-space facts; no novelty is claimed for them abstractly. Jongho Yang's 2026 work studies Friedrichs-angle geometry between Nyman--Beurling subspaces, and recent smoothed-Gram work studies spectral/block decay in Nyman families. Those literatures confirm that angle and spectral language themselves are established tools.

A targeted literature audit did not locate the present source-specific implication obtained from the `NB-063` one-cell recursion: persistent **collective late off-grid target gain** forces the normalized canonical visible projection into singular values tending to zero for the finite-window forward-memory map `Gamma_R`. No priority claim is made. No specialized external theorem is load-bearing beyond sources already anchored in `SOURCES.md`, so that file remains unchanged.

The durable line-local advance is the obstruction sharpening: after `NB-063`, persistent leakage no longer merely requires repeated alignment with a finite-rank memory channel. It requires a much more rigid sequence of **target-bearing approximate right-kernel modes** for the canonical one-cell continuation operator. Proving that the actual arithmetic target cannot track those modes would force the collective late-tail gain to vanish.