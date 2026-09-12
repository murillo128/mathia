# PL-288 — The one-stroke Legendre tail certificate has an intrinsic square-root transport barrier

**Evidence:** `LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION + ROUTE-NARROWING`

**Status:** `CERTIFIED-TAIL-L2-LOCALIZATION + SQRT-MARGIN-BARRIER + NO-QUANTITATIVE-SOURCE-TRANSPORT`

## Claim

The certified finite reduction at aperture `a=0.8` gives much stronger information than mere positivity: its discarded Legendre block is coercive at order one and couples to the retained block only at size below `10^-100`. Nevertheless, **those block estimates alone cannot supply the quantitative prime-shift transport needed after `PL-287`**.

Let `Q` denote the exact localized Weil form at `a=0.8`, let `R<=Q` be Zhu's one-stroke lower form at `T^sharp=200`, and split the even Legendre space into the first `N=200` even modes and their orthogonal complement,

\[
H=H_N\oplus H_T.
\]

Write the normalized exact ground state as `g=x+y` with `x in H_N`, `y in H_T`. Source 58 gives

\[
R=
\begin{pmatrix}
A&B\\ B^*&D
\end{pmatrix},
\qquad
A\ge 0,
\qquad
D\ge dI,
\qquad
\|B\|\le\varepsilon,
\]

with

\[
d=0.5134667\ldots-10^{-100},
\qquad
\varepsilon\le10^{-100},
\]

while its independently certified variational upper bound gives

\[
\lambda_1(Q)\le 2.27\times10^{-17}.
\]

Since `R<=Q`,

\[
\lambda_1(Q)
=Q(g)
\ge R(g)
\ge d\|y\|^2-2\varepsilon\|y\|.
\]

Hence

\[
\boxed{
\|y\|
\le
\frac{\varepsilon+\sqrt{\varepsilon^2+d\lambda_1(Q)}}{d}
<6.65\times10^{-9}.
}
\]

This is an unusually strong certified localization of the exact ground state in ordinary `L^2`. But it is only a **square-root-in-the-spectral-margin** estimate. For every contraction `U` on `H`,

\[
\bigl|\langle Ug,g\rangle-\langle Ux,x\rangle\bigr|
\le 2\|y\|+\|y\|^2
<1.33\times10^{-8}.
\]

For the difference of two compressed translation channels the corresponding a priori uncertainty is below `2.66e-8`, but still about nine orders of magnitude larger than the certified positivity margin `8.9e-18`. Because fixed-domain translations are not norm-continuous on the ambient low-regularity space (`PL-285`--`PL-286`), the small `L^2` tail norm does not acquire a useful factor of `|delta|` without additional frequency regularity of that tail.

The square-root scaling is not an artifact of dropping the eigenvector equation. There are two-dimensional positive models with `R<=Q`, an isolated ground eigenvector of `Q`, and tail size `Theta(sqrt(lambda_1(Q)))`. Thus no argument using only the one-stroke block coercivity, the exact ground-state equation, and boundedness of the shift channels can improve the scale to `O(lambda_1)` or otherwise reach the current Weil margin. The live target after `PL-287` therefore remains genuinely **state-specific Fourier-tail regularity (or a source-specific cancellation identity)**, not stronger bookkeeping of the existing finite reduction.

## 1. Certified tail localization from Zhu's lower form

Source 58, Xuefeng Zhu's *Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau-Widom decay law*, proves at `L=0.8`, `T^sharp=200` that the lower form `R` has the block structure above in the even Legendre basis. The first `200` even orders are `0,2,...,398`. On the discarded block,

\[
D\ge (\beta^*-\varepsilon_D)I,
\qquad
\beta^*=0.5134667\ldots,
\qquad
\varepsilon_D\le10^{-100},
\]

and the leading-tail coupling satisfies

\[
\|B\|\le\varepsilon_B\le10^{-100}.
\]

The same paper gives the unconditional upper bound

\[
\lambda_1(Q)\le 2.27\times10^{-17}
\]

from an explicit geometric-side trial function. These are theorem/certificate inputs, not zero-side assumptions.

For a normalized exact ground vector `g=x+y`, positivity of the retained block permits us to discard its contribution:

\[
R(g)
=
\langle Ax,x\rangle
+2\operatorname{Re}\langle By,x\rangle
+\langle Dy,y\rangle
\ge
-2\varepsilon_B\|x\|\|y\|
+d\|y\|^2.
\]

Using `||x||<=1`, `R(g)<=Q(g)=lambda_1(Q)`, and solving the resulting quadratic inequality yields

\[
\|y\|
\le
\frac{\varepsilon_B+\sqrt{\varepsilon_B^2+d\lambda_1(Q)}}{d}.
\]

Substituting the certified constants gives `||y||<6.65e-9`, or equivalently

\[
\|y\|^2<4.43\times10^{-17}.
\]

This conclusion concerns the **exact** `Q`-ground state; it does not identify it with the numerical bottom eigenvector of the reduced matrix.

## 2. Why this does not control moving prime shifts at the required scale

Let `U` be any contraction, in particular a compressed translation associated with one prime-power lag. Expanding `g=x+y`,

\[
\langle Ug,g\rangle-\langle Ux,x\rangle
=
\langle Ux,y\rangle
+
\langle Uy,x\rangle
+
\langle Uy,y\rangle.
\]

Therefore

\[
\bigl|\langle Ug,g\rangle-\langle Ux,x\rangle\bigr|
\le
2\|x\|\|y\|+\|y\|^2
\le
2\|y\|+\|y\|^2.
\]

At the certified tail norm this is `<1.33e-8`. For a moving lag one can compare `U_{h+delta}-U_h` by applying the same estimate to both expectations, obtaining a tail uncertainty `<2.66e-8` before using any extra regularity.

This is exactly where `PL-285`--`PL-287` matter. The finite-dimensional head has an ordinary quantitative modulus because its Legendre coefficients are controlled. The unknown tail does not: compressed translations are strongly continuous but not operator-norm continuous on the relevant ambient space, and `L^2` smallness by itself supplies no rate as `delta->0`. `PL-287` proves that the actual compact ground branch does beat the ambient inverse-log modulus, but only qualitatively because the missing input is a quantitative weighted Fourier-tail bound. The one-stroke certificate does not provide that missing input merely from its spectacular `10^-100` head-tail matrix coupling.

The numerical mismatch is decisive for this route. The current certified floor is

\[
8.9\times10^{-18},
\]

whereas the tail uncertainty in a single bounded shift expectation is of order `10^-8`. Even multiplying by a small aperture displacement is not justified on the tail without precisely the frequency regularity still missing in `PL-287`.

## 3. The square-root scale is sharp even when `g` is an exact isolated eigenvector

The preceding `sqrt(lambda)` loss is not caused merely by treating the ground vector as an arbitrary low-energy vector. Consider `H=C^2`,

\[
R=\begin{pmatrix}0&0\\0&d\end{pmatrix},
\qquad d>0.
\]

Choose `M>d` and `0<lambda<d`, and set

\[
y^2=
\frac{\lambda(M-d)}{d(M-\lambda)},
\qquad
c^2=1-y^2,
\qquad
g=(c,y),
\qquad
h=(-y,c).
\]

Define

\[
Q=\lambda\,gg^*+M\,hh^*.
\]

Then `g` is the simple normalized ground eigenvector of `Q` with eigenvalue `lambda`. A direct determinant calculation gives

\[
\det(Q-R)
=
\lambda M-d(\lambda c^2+My^2)
=0,
\]

and the diagonal entries are nonnegative, so `Q-R` is positive semidefinite. Hence `R<=Q`, exactly as in the one-stroke setup, while

\[
|y|
=
\sqrt{\frac{M-d}{d(M-\lambda)}}\,\sqrt\lambda
=
\Theta(\sqrt\lambda).
\]

For the norm-one self-adjoint swap

\[
U=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]

one has

\[
\langle Ug,g\rangle-\langle U(c,0),(c,0)\rangle
=2cy
=
\Theta(\sqrt\lambda).
\]

Thus the information `R<=Q`, order-one tail coercivity of `R`, a simple exact `Q`-ground state, and bounded source operators **cannot generically force an expectation error smaller than square-root order in the spectral margin**. Any better estimate in the localized Weil problem must use additional structure of the actual state or of the actual prime-shift family.

## 4. Prior-art and novelty audit

The finite-reduction inputs are all from Source 58 and are already recorded in `research/prime_lattice/SOURCES.md`. Zhu explicitly warns that direct order-space truncations of the Weil problem leave `O(1)` prime-shift coupling across a cut; the present result is consistent with that warning.

The Hilbert-space inequalities and the two-dimensional saturation model above are elementary exact deductions. No novelty is claimed for the abstract fact that quadratic coercivity controls a vector component at square-root scale. The durable Mathia delta is its application to the **certified `a=0.8` Weil constants**: even a tail block coercive at `~0.513` with `10^-100` matrix coupling localizes the exact ground only to `~6.65e-9` in `L^2`, while the quantity that must be transported is positive only at `~10^-17` scale. This rules out the tempting inference that Zhu's super-exponential finite-reduction tail control already supplies the quantitative branch transport left open by `PL-287`.

## 5. Boundary of the obstruction and consequence for the line

This finding does **not** say that the true ground-state tail is actually as large as `6.65e-9`, nor that its moving-shift expectation really changes at `10^-8` scale. The true state may be vastly better localized or may enjoy cancellations invisible to the certificate. It also does not obstruct a direct interval certificate at apertures larger than `0.8`.

It says only that the currently certified block data cannot prove the needed transport by themselves, even after using exact ground-state simplicity. To cross the next source activation using the branch route, one still needs at least one genuinely stronger ingredient, for example:

- a quantitative bound on the weighted Fourier tail of the actual ground branch;
- stronger regularity of the exact eigenfunction with an explicit uniform constant;
- a source-specific orthogonality/cancellation that suppresses head-tail shift cross terms; or
- a direct finite certificate over a nontrivial aperture interval rather than transport from a single endpoint.

This sharpens the post-`PL-287` target: **super-exponential truncation error of a lower certificate is not the same thing as super-exponential control of the exact ground state's transport-sensitive tail.**