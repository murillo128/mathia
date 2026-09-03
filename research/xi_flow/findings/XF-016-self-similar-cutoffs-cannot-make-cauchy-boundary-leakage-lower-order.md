# XF-016 — self-similar cutoffs cannot make Cauchy boundary leakage lower order

**Status:** `EXACT-DERIVED` + `NEGATIVE/OBSTRUCTION` + `LITERATURE-CALIBRATED`. XF-014 gave an exact positive-conductance diffusion for the real-simple Xi gap vector, and XF-015 showed that bounded gap envelopes make its quadratic bulk dissipation uniformly comparable to the inverse-square / `H^{1/2}` Cauchy form. The natural next attempt is to replace a hard finite block by a smooth taper and hope that the boundary term becomes lower order when the mesoscopic window grows.

That does not happen for a fixed-shape self-similar cutoff. The exact nonlinear gap equation has a weighted localization identity whose error is itself an inverse-square fractional form. In one dimension `H^{1/2}` is scale critical, so dilation does not create a small parameter. On the arithmetic-lattice linearization the localized dissipation and the cutoff leakage both have nonzero `N -> infinity` limits, and the leakage remains nonzero after weighted-mean centering.

## 1. Exact nonlinear localization identity

On a real-simple slice, XF-014 gives

\[
g_i'=2\sum_{k\ne i}c_{ik}(g_k-g_i),
\qquad c_{ik}=c_{ki}>0.
\tag{1}
\]

Let `psi_i` be a finitely supported real cutoff, fix a reference spacing `h`, and put

\[
v_i=g_i-h,
\qquad
E_\psi=\frac12\sum_i\psi_i^2v_i^2.
\tag{2}
\]

Since `g_k-g_i=v_k-v_i`, symmetrizing the pairs in (1) and using

\[
(a-b)(p^2a-q^2b)=(pa-qb)^2-(p-q)^2ab
\tag{3}
\]

gives the exact identity

\[
\boxed{
\begin{aligned}
E_\psi'
={}&-2\sum_{i<k}c_{ik}(\psi_iv_i-\psi_kv_k)^2\\
&+2\sum_{i<k}c_{ik}(\psi_i-\psi_k)^2v_iv_k.
\end{aligned}}
\tag{4}
\]

The first line is localized positive-conductance dissipation. The second is the localization leakage and has no fixed sign.

The same formula holds after removing the constant gap mode by taking

\[
\mu_\psi(t)=\frac{\sum_i\psi_i^2g_i(t)}{\sum_i\psi_i^2},
\qquad v_i=g_i-\mu_\psi.
\tag{5}
\]

Indeed `sum psi_i^2 v_i=0`, so the extra `mu_psi'` term produced by differentiating (2) vanishes. Thus weighted-mean centering does not remove the second line of (4).

## 2. Fixed-shape dilation is scale critical

Linearize at an arithmetic lattice of spacing `h`. Then

\[
h^2c_{ik}=\frac1{(i-k)^2}.
\tag{6}
\]

Writing `v_i=h u_i`, the powers of `h` cancel and the linearized weighted energy satisfies

\[
\frac{d}{dt}\frac{h^2}{2}\sum_i\psi_i^2u_i^2
=-2D_N(\psi,u)+2R_N(\psi,u),
\tag{7}
\]

with

\[
D_N=\sum_{i<k}\frac{(\psi_iu_i-\psi_ku_k)^2}{(i-k)^2},
\qquad
R_N=\sum_{i<k}\frac{(\psi_i-\psi_k)^2u_iu_k}{(i-k)^2}.
\tag{8}
\]

Take fixed compactly supported `C^1` profiles `psi,U` and sample them at scale `N` by

\[
\psi_i=\psi(i/N),
\qquad
u_i=U(i/N).
\tag{9}
\]

Riemann-sum convergence gives

\[
D_N\to
\int_{x<y}\frac{(\psi(x)U(x)-\psi(y)U(y))^2}{(x-y)^2}\,dx\,dy,
\tag{10}
\]

and

\[
R_N\to
\int_{x<y}\frac{(\psi(x)-\psi(y))^2U(x)U(y)}{(x-y)^2}\,dx\,dy.
\tag{11}
\]

There is no power of `N` in either limit. Equivalently, the cutoff cost

\[
J_N(\psi)=\sum_{i<k}
\frac{(\psi(i/N)-\psi(k/N))^2}{(i-k)^2}
\tag{12}
\]

converges to

\[
J(\psi)=\int_{x<y}\frac{(\psi(x)-\psi(y))^2}{(x-y)^2}\,dx\,dy>0
\tag{13}
\]

for every nonconstant cutoff. This is exactly the one-dimensional `H^{1/2}` critical scaling: dilation leaves the seminorm at order one.

At the Xi fixed-time scale from XF-007--XF-008,

\[
N\asymp h^{-2}\asymp\log^2T,
\tag{14}
\]

so ordinary tapering leaves an `O(1)` localization term on the same scale as the useful nonlinear Cauchy coercivity of XF-015.

## 3. Centering does not recover an `o(1)` error

The critical leakage is not only a badly normalized constant mode. Choose a smooth compactly supported cutoff `psi` having two disjoint plateau intervals `A,B` with values `p,q>0`, `p != q`. Let `f_A,f_B` be nonnegative smooth functions supported strictly inside those plateaus and set

\[
U=f_A-\lambda f_B,
\qquad
\lambda=\frac{p^2\int f_A}{q^2\int f_B}.
\tag{15}
\]

Then

\[
\int\psi(x)^2U(x)\,dx=0,
\tag{16}
\]

so `U` is weighted-mean centered. Because `psi` is constant on each support, the only nonzero contribution to the continuum leakage (11) is the cross interaction:

\[
\boxed{
R(\psi,U)=-(p-q)^2\lambda
\int_A\int_B\frac{f_A(x)f_B(y)}{(x-y)^2}\,dx\,dy<0.}
\tag{17}
\]

Sampling this construction and changing `lambda` by `o(1)` gives exact discrete centering while preserving the nonzero limit. Therefore no estimate

\[
|R_N|\le \varepsilon_N C,
\qquad \varepsilon_N\to0,
\tag{18}
\]

can follow uniformly from fixed-shape localization and centering alone.

There is also a simple exact matched control. On a uniform gap lattice, choose a reference spacing different from the actual gap, so `v_i` is a nonzero constant in (4). The gap vector is an equilibrium, hence `E_psi'=0`; the localized dissipation and leakage in (4) cancel exactly. Equation (17) shows that the obstruction survives after this trivial constant mode is removed.

## 4. Gap envelopes do not supply the missing small parameter

Under the two-sided envelope of XF-015,

\[
mh\le g_r\le Mh,
\]

one has on the controlled interactions

\[
\frac1{M^2(i-k)^2}\le h^2c_{ik}\le\frac1{m^2(i-k)^2}.
\tag{19}
\]

If also `|v_i| <= C h`, the leakage in (4) obeys

\[
\left|2\sum_{i<k}c_{ik}(\psi_i-\psi_k)^2v_iv_k\right|
\le\frac{2C^2}{m^2}J_N(\psi).
\tag{20}
\]

By (13), this envelope-only bound is `O(1)`, not `o(1)`, for a self-similar taper. The centered lattice family proves that the lack of a vanishing factor is genuine: for every fixed perturbation amplitude, however small, a nonzero `N`-independent leakage survives the lattice limit. Thus a theorem based only on bounded gaps plus fixed-shape tapering cannot turn the boundary term into a lower-order error.

This is deliberately narrower than a no-go for all localization. A non-self-similar multiscale taper with a diverging inner/outer scale ratio may have different critical-capacity behavior. Arithmetic cancellation in the signed products `v_i v_k`, stronger exterior correlation information, or an overlapping/renormalized global entropy could also cancel leakage. Those possibilities remain open.

## 5. Prior art, falsification boundary, and next target

Fractional localization errors of this algebraic form are classical. Frank, Lieb and Seiringer, **Hardy-Lieb-Thirring inequalities for fractional Schrödinger operators**, *Journal of the American Mathematical Society* 21:4 (2008), 925--950, DOI `10.1090/S0894-0347-07-00582-6`, give an IMS-type nonlocal localization kernel of the form

\[
|x-y|^{-d-2s}\sum_j(\chi_j(x)-\chi_j(y))^2.
\]

Their stated Lemma 3.5 lies in the noncritical range `s<d/2`; the exponent formally becomes `2` at `d=1,s=1/2`. XF-016 does not invoke that theorem at its excluded endpoint: the discrete critical identity and scaling are derived directly in (4) and (10)--(13). The paper is used only to calibrate the prior-art class. No novelty is claimed for fractional IMS localization or `H^{1/2}` scale invariance.

The obstruction is also universal for matched one-dimensional logarithmic-repulsion controls, so it is not an Xi-specific selector and does not upper-bound `Lambda`. Its durable role is methodological: **XF-014's boundary problem cannot be closed merely by replacing the hard block with a conventional smooth cutoff.** The next useful target must add signed exterior information, a genuinely multiscale/capacitary cutoff, or an algebraic cancellation mechanism for overlapping/global entropies.