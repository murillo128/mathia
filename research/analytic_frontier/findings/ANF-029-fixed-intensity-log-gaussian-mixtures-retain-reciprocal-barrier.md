# ANF-029 — fixed-intensity log-Gaussian mixtures retain the reciprocal barrier

**Status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + DIFFRACTION-DUAL + MIXTURE-RIGIDITY`. `ANF-028` leaves open convex mixing over the logarithmic-variogram amplitude `c`, the intensity `rho`, or both. The amplitude part can be closed exactly. Mixing over `c` changes the strength and local shape of the softened reciprocal feature, but at fixed intensity every component keeps that feature at the **same reciprocal location**. Positivity of the Bartlett spectrum then prevents convex averaging from cancelling it.

Let

\[
v_c(t)=c\log(1+t^2),\qquad c>0,
\]

and let `S_c` be the unit-intensity diffuse structure factor derived in `ANF-028`,

\[
S_c(q)
=1+2\sum_{n\ge1}(1+n^2)^{-2\pi^2cq^2}\cos(2\pi qn).
\tag{1}
\]

For a probability measure `pi` on `(0,infinity)` and a fixed intensity `rho>0`, define the amplitude mixture

\[
\overline S_\pi(q):=\int S_c(q)\,d\pi(c),
\qquad
\overline\mu_{\pi,\rho}
:=\rho\,\delta_0+\overline S_\pi(h/\rho)\,dh,
\tag{2}
\]

whenever the mixture is locally finite. If it is not locally finite, domination by the finite Montgomery--Taylor budget already fails.

Then for every `0<a<1`,

\[
\boxed{
\overline\mu_{\pi,\rho}
\not\le
\nu_a:=a\,\delta_0+a|h|\,dh
\quad\text{on }(-1,1).
}
\tag{3}
\]

Thus **amplitude mixing alone cannot repair `ANF-028`**. Any surviving mixture in this logarithmic Gaussian Palm-lattice family must genuinely vary the intensity `rho`, because only varying `rho` moves the first reciprocal feature through the tested band.

## 1. Every amplitude has reciprocal liminf strictly above one

Set

\[
c_*:=\frac1{4\pi^2}.
\tag{4}
\]

`ANF-028` gives the complete local classification at the first reciprocal frequency `q=1`. If `0<c<c_*`, then

\[
S_c(1+\varepsilon)
\asymp
|\varepsilon|^{4\pi^2c-1}
\longrightarrow+\infty.
\tag{5}
\]

At the transition `c=c_*`,

\[
S_{c_*}(1+\varepsilon)
=-2\log|2\pi\varepsilon|+O(1)
\longrightarrow+\infty.
\tag{6}
\]

For `c>c_*`, the series is absolutely convergent at `q=1` and

\[
S_c(1)
=1+2\sum_{n\ge1}(1+n^2)^{-2\pi^2c}
>1.
\tag{7}
\]

Define the extended reciprocal liminf

\[
L(c):=\liminf_{q\to1,\ q\ne1}S_c(q).
\tag{8}
\]

Equations (5)--(7) imply the pointwise statement

\[
\boxed{L(c)>1\quad\text{for every }c>0,}
\tag{9}
\]

with `L(c)=+infinity` for `c<=c_*`.

The sign in (9) is not an artifact of the Fourier-series representation. Each `S_c(q)dq` is the diffuse part of a Bartlett spectrum and is therefore a positive measure; away from reciprocal frequencies, (1) gives its ordinary density. The reciprocal excess is consequently positive rather than an oscillatory singularity that could cancel under averaging.

## 2. Fatou makes the reciprocal excess survive every amplitude mixture

Take any sequence `q_n->1`, `q_n!=1`, along which

\[
\overline S_\pi(q_n)
\longrightarrow
\liminf_{q\to1,\ q\ne1}\overline S_\pi(q).
\]

The densities `S_c(q_n)` are nonnegative, so Fatou's lemma gives

\[
\begin{aligned}
\liminf_{q\to1,\ q\ne1}\overline S_\pi(q)
&\ge
\int \liminf_{n\to\infty}S_c(q_n)\,d\pi(c)\\
&\ge
\int L(c)\,d\pi(c).
\end{aligned}
\tag{10}
\]

Because `L(c)-1` is strictly positive for every `c>0` and `pi` is a probability measure,

\[
\int L(c)\,d\pi(c)>1,
\tag{11}
\]

possibly with value `+infinity`. Hence

\[
\boxed{
\liminf_{q\to1,\ q\ne1}\overline S_\pi(q)>1.
}
\tag{12}
\]

In particular there exist `eta>0` and `epsilon>0` such that

\[
\overline S_\pi(q)>1+\eta
\qquad
(0<|q-1|<\epsilon).
\tag{13}
\]

This is the load-bearing rigidity. Convex mixing may smooth the dependence on `c`, but it cannot lower the common reciprocal neighborhood below one because every component approaches that neighborhood from the same positive side.

## 3. Fixed intensity therefore contradicts every subunit Montgomery--Taylor budget

Assume for contradiction that (3) fails, so

\[
\overline\mu_{\pi,\rho}\le\nu_a
\quad\text{on }(-1,1)
\tag{14}
\]

for some `0<a<1`.

The atom at zero in (2) immediately forces

\[
\rho\le a<1.
\tag{15}
\]

Thus the first reciprocal location `h=rho` lies strictly inside the positive tested band. By (13), after shrinking `epsilon` if necessary,

\[
\overline S_\pi(h/\rho)>1+\eta
\tag{16}
\]

on a punctured interval around `h=rho` contained in `(0,1)`. But throughout `(0,1)` the target diffuse density satisfies

\[
a h<a<1.
\tag{17}
\]

Therefore (16) exceeds (17) on an interval of positive Lebesgue measure, contradicting (14). This proves (3).

The dichotomy is exact at the level relevant here. If `rho>a`, the candidate already fails through its forward atom. If `rho<=a`, amplitude averaging cannot remove the common finite-frequency obstruction at `h=rho`.

## 4. Intensity atoms in a joint mixture obey a strict mass cap

The same argument gives a useful necessary condition for the genuinely open joint mixture. Let `Pi` be a probability measure on pairs `(c,rho)`, and suppose its intensity marginal has an atom of mass `m>0` at some

\[
0<\rho_0<1.
\]

Let `pi_0` be the conditional amplitude law on that intensity atom and define

\[
R_0:=\int L(c)\,d\pi_0(c)>1.
\tag{18}
\]

The contribution of this one intensity atom to the diffuse density is

\[
m\int S_c(h/\rho_0)\,d\pi_0(c).
\tag{19}
\]

All other components of the joint mixture are nonnegative. Therefore, if the full mixture were dominated by `nu_a`, comparison as `h->rho_0` would require

\[
\boxed{
mR_0\le a\rho_0.}
\tag{20}
\]

Since `R_0>1`, every allowed intensity atom must satisfy the strict cap

\[
\boxed{m<a\rho_0.}
\tag{21}
\]

There is a stronger singular case. If the conditional amplitude law gives positive mass to

\[
0<c\le c_*=rac1{4\pi^2},
\]

then `R_0=+infinity` by (5)--(6), so **no positive atom at `rho_0` is possible at all**. Thus any joint survivor carrying critical-or-subcritical logarithmic amplitudes must spread those components over a non-atomic intensity distribution.

Equation (20) is only a necessary condition; it does not rule out sufficiently small atoms supported entirely on `c>c_*`. Its role is to isolate exactly how much discrete intensity mass can survive before the reciprocal feature alone breaks the order budget.

## 5. Consequence for the diffraction search

`ANF-028` showed that the logarithmic variogram is qualitatively different from ordinary fixed-Hurst fBm: it can match the required linear cusp and even pass the full local origin gate. The present result shows that the next convexification must also be qualitatively different from merely averaging the regularization strength. **The reciprocal location, not just the reciprocal height, is the relevant state variable.**

The remaining family is therefore

\[
\int\left[
\rho\delta_0+S_c(h/\rho)dh
\right]d\Pi(c,\rho),
\tag{22}
\]

with genuinely varying intensity. The origin conditions from `ANF-028`,

\[
\mathbb E_\Pi\rho\le a_{\rm MT},
\qquad
2\pi^2\mathbb E_\Pi\frac c\rho\le a_{\rm MT},
\tag{23}
\]

remain mutually compatible. The new finite-frequency restriction (20) is independent of those two moments and acts directly on atomic intensity mass.

This brings the open problem closer to the dilation-mixture obstruction of `ANF-022`. There the reciprocal lattice harmonics move with `rho` and a Möbius-weighted dual certificate proves that smearing them cannot fit inside the Montgomery--Taylor budget. Here the reciprocal features are softened rather than atomic, so the exact `ANF-022` dilation operator does not apply unchanged. A future no-go would need a positive dual test that charges the **integrated cost of moving the soft reciprocal profiles across intensity**, not merely their value at one common location.

## 6. Prior-art and novelty boundary

The point-process and structure-factor inputs are exactly those already used and anchored for `ANF-028`: stationary-increment Gaussian Palm-lattice regularization, positivity of the Bartlett spectrum, and the explicit logarithmic-variogram structure factor. The new step is elementary convex analysis: the reciprocal liminf classification from `ANF-028` is combined with positivity and Fatou's lemma.

A targeted prior-art search across perturbed-lattice diffraction, correlated Gaussian perturbations, paracrystal/shuffled-lattice spectra, and recent hyperuniform perturbed-lattice work did not locate this fixed-intensity amplitude-mixture obstruction or the atomic-intensity cap (20) in the Montgomery--Taylor order problem. The surrounding literature studies how correlations and displacement laws alter hyperuniformity or reciprocal structure, but no external theorem is needed for (3) or (20). No publication-level novelty claim is made, and no `SOURCES.md` edit is required.

## 7. Evidence boundary and decisive audit

This finding does **not** prove that arbitrary joint mixtures over `(c,rho)` fail. Its proof deliberately uses the fact that all components in an amplitude mixture share one reciprocal location. For a continuous intensity law, those locations move, and the Fatou argument at a single `h` no longer produces a uniform lower bound. That is the exact remaining escape.

The atomic corollary likewise does not prohibit every intensity atom: when the conditional amplitude law is supported in `c>c_*`, a sufficiently small atom can satisfy the necessary inequality (20). Nor does the argument extend to arbitrary stationary-increment Gaussian variograms whose reciprocal-frequency behavior may differ from the logarithmic family.

The decisive audit for the main theorem is simple: exhibit a probability law `pi` and fixed `rho` for which the nonnegative mixed density has reciprocal liminf at most one. Equations (5)--(12) show that this is impossible unless one of the `ANF-028` reciprocal asymptotics or Bartlett-spectrum positivity is wrong. The decisive next test for the open branch is instead a genuinely varying-intensity construction or a dual integral inequality that controls its total soft-reciprocal cost.