# ANF-026 — the zero-Hurst fBm limit recrystallizes and its scale mixtures overshoot the band

**Status:** `LITERATURE+DERIVED + EXACT-WEAK-LIMIT + NEGATIVE/OBSTRUCTION + DIFFRACTION-DUAL`. `ANF-025` excludes every fixed fractional-Brownian Palm-lattice regularization because its diffuse structure factor behaves like `|h|^(1-2H)` and therefore decays more slowly than the linear Montgomery--Taylor envelope. It deliberately leaves one singular boundary open: the fixed-`H` asymptotic is not uniform as `H->0`, so a parameter-dependent weak-* limit might in principle have a different infrared profile.

That boundary can now be evaluated exactly. For the unit Palm lattice perturbed by fractional Brownian motion with

\[
\operatorname{Var}(B_n^H-B_m^H)=|n-m|^{2H},
\]

the full normalized diffraction measure has, as `H downarrow 0`, the weak-* limit

\[
\boxed{
\mu_0
=
\sum_{k\in\mathbb Z}e^{-2\pi^2k^2}\,\delta_k
+\bigl(1-e^{-2\pi^2h^2}\bigr)\,dh.
}
\tag{1}
\]

Thus the nonzero Bragg peaks erased for every `H>0` **reappear in the zero-Hurst limit**. The limiting process is diffraction-equivalent to an iid Gaussian-shuffled lattice: if `U_n` are iid `N(0,1/2)`, then the relative displacements `U_n-U_0` have exactly the limiting finite-dimensional law of `B_n^H`.

More strongly, randomizing the spatial scale after taking this zero-Hurst boundary does not rescue the Montgomery--Taylor target. Let

\[
a:=C_{\rm MT}^{-1}=0.753296067856070\ldots,
\qquad
\nu_a=a\,\delta_0+a|h|\,dh,
\]

and dilate (1) to arbitrary intensity `rho>0`:

\[
\boxed{
\mu_{0,\rho}
=
\rho\sum_{k\in\mathbb Z}e^{-2\pi^2k^2}\delta_{k\rho}
+
\left(1-e^{-2\pi^2(h/\rho)^2}\right)dh.
}
\tag{2}
\]

For **every** probability mixture `pi` of these scale profiles whose barycenter is locally finite,

\[
\boxed{
\int\mu_{0,\rho}\,d\pi(\rho)
\not\le\nu_a
\quad\text{on }(-1,1).
}
\tag{3}
\]

The proof of (3) does not use the residual Bragg atoms at all. The forward atom gives `E_pi rho<=a`. Markov's inequality then puts at least half of the scale mass below `2a`. At the single moderate frequency `h=1/2`, every such component has diffuse density at least

\[
1-e^{-\pi^2/(8a^2)}
=0.886288893468587\ldots,
\]

so the mixture diffuse density is at least

\[
0.443144446734293\ldots
>
\frac a2
=0.376648033928035\ldots .
\]

Continuity turns this strict pointwise gap into a positive-measure interval violation. Hence the natural `H->0` escape from `ANF-025` fails even after arbitrary post-limit scale convexification.

## 1. The small-Hurst field has an exact white-noise relative-displacement limit

For two-sided fractional Brownian motion normalized by `B_0^H=0`,

\[
\operatorname{Cov}(B_m^H,B_n^H)
=
\frac12\left(|m|^{2H}+|n|^{2H}-|m-n|^{2H}\right).
\tag{4}
\]

Fix finitely many distinct nonzero integer indices. As `H downarrow0`, every variance tends to one and every off-diagonal covariance tends to `1/2`. Since the vectors are Gaussian, their finite-dimensional distributions converge to the centered Gaussian vector with

\[
\operatorname{Var}(B_n^0)=1,
\qquad
\operatorname{Cov}(B_m^0,B_n^0)=\frac12
\quad(m\ne n).
\tag{5}
\]

Take iid standard Gaussians `xi_n` and define

\[
B_n^0:=\frac{\xi_n-\xi_0}{\sqrt2}.
\tag{6}
\]

Then (6) has exactly covariance (5). Equivalently, with `U_n:=xi_n/sqrt(2)` iid `N(0,1/2)`,

\[
B_n^0=U_n-U_0.
\tag{7}
\]

A common translation by `-U_0` does not affect any pair difference or diffraction measure. Therefore the zero-Hurst finite-dimensional limit of the fBm-perturbed Palm lattice is precisely the relative-displacement law of an iid Gaussian-shuffled lattice.

This small-Hurst finite-dimensional limit is not itself new. Malyarenko--Mishura--Ralchenko--Shklyar, *Entropy and alternative entropy functionals of fractional Gaussian noise as the functions of Hurst index* (2023, DOI `10.1007/s13540-023-00155-2`), explicitly records the `H=0` finite-dimensional Gaussian limit and the white-noise representation (6). The load-bearing Mathia question is what that singular limit does to the **diffraction measure** relevant to `ANF-020`.

## 2. The autocorrelation limit is summable against Schwartz tests

Let

\[
g_v(x):=\frac1{\sqrt{2\pi v}}e^{-x^2/(2v)}.
\]

For the unit-intensity Palm-lattice regularization used in `ANF-025`, the expected autocorrelation can be written

\[
\gamma_H
=
\delta_0+
\sum_{n\in\mathbb Z\setminus\{0\}}
 g_{|n|^{2H}}(x-n)\,dx.
\tag{8}
\]

Indeed the displacement difference between the Palm point at zero and the point with label `n` is Gaussian with variance `|n|^{2H}`. This is the spatial counterpart of the exact spectral formula in Thomassey--Lachièze-Rey--Shapira used by `ANF-025`.

For each fixed `n\ne0`,

\[
g_{|n|^{2H}}(x-n)\longrightarrow g_1(x-n)
\qquad(H\downarrow0).
\tag{9}
\]

The infinite sum may also be passed through the limit against every Schwartz test. Fix `H_0<1`. If `Z_{n,H}` is centered Gaussian with variance `|n|^{2H}`, then for `H<=H_0` the event `|Z_{n,H}|>|n|/2` has probability bounded by

\[
2\exp\bigl(-c|n|^{2-2H_0}\bigr),
\]

while on its complement a Schwartz test evaluated at `n+Z_{n,H}` has arbitrarily high polynomial decay in `|n|`. These two bounds give a summable majorant independent of small `H`. Hence

\[
\boxed{
\gamma_H\longrightarrow
\gamma_0
:=
\delta_0+
\sum_{n\ne0}g_1(x-n)\,dx
}
\tag{10}
\]

in the tempered-distribution sense, and therefore vaguely after Fourier transformation on compact frequency windows because the resulting diffraction measures are positive.

Rewrite the limit as

\[
\gamma_0
=
\delta_0-g_1(x)\,dx
+
\sum_{n\in\mathbb Z}g_1(x-n)\,dx.
\tag{11}
\]

## 3. Poisson summation shows that Bragg peaks return at `H=0`

In the Fourier convention `e^{-2pi i h x}`,

\[
\widehat{g_1}(h)=e^{-2\pi^2h^2}.
\tag{12}
\]

Poisson summation applied to the periodized Gaussian in (11) gives

\[
\widehat{
\sum_{n\in\mathbb Z}g_1(x-n)
}
=
\sum_{k\in\mathbb Z}e^{-2\pi^2k^2}\delta_k.
\tag{13}
\]

The first two terms of (11) transform to

\[
\left(1-e^{-2\pi^2h^2}\right)dh.
\tag{14}
\]

Equations (13)--(14) prove (1).

This makes the singular nature of `H->0` explicit. Thomassey--Lachièze-Rey--Shapira prove that every fixed `H>0` fBm regularization erases the nonzero lattice Bragg component and has an absolutely continuous Bartlett spectrum away from the forward peak. Yet the weak-* boundary `H=0` contains nonzero atoms of masses

\[
e^{-2\pi^2k^2},\qquad k\ne0.
\tag{15}
\]

The first one is tiny,

\[
e^{-2\pi^2}=2.675287991\ldots\times10^{-9},
\]

but strict measure domination is sensitive to any positive atom. Bragg erasure is therefore not closed under the zero-Hurst limit.

Formula (1) is also exactly the classical iid perturbed-lattice formula from `ANF-023` with Gaussian displacement characteristic function

\[
\varphi(h)=e^{-\pi^2h^2},
\qquad
|\varphi(h)|^2=e^{-2\pi^2h^2}.
\tag{16}
\]

So the zero-Hurst boundary does not create a new correlated diffraction phase; it returns to a specific iid-shuffled crystal after quotienting the irrelevant common translation.

## 4. Scaling to intensity `rho` gives the exact boundary family

Scale space by `x -> x/rho`, so the lattice intensity becomes `rho`. A finite normalized diffraction profile is then evaluated at frequency `h/rho`; passing this through (1) gives

\[
\mu_{0,\rho}
=
\rho\sum_{k\in\mathbb Z}e^{-2\pi^2k^2}\delta_{k\rho}
+D_\rho(h)\,dh,
\tag{17}
\]

where

\[
\boxed{
D_\rho(h)
:=1-e^{-2\pi^2(h/\rho)^2}.
}
\tag{18}
\]

The forward atom has mass `rho`. For one fixed scale, `ANF-023` already implies failure of every target `a delta_0+a|h|dh` with `a<1`: forward-atom domination forces `rho<=a`, placing the first residual Bragg atom at `h=rho` inside the open band. The point of the next step is to remove that pure-point argument, since a continuum of scales can smear reciprocal vectors just as in `ANF-022`.

## 5. A one-frequency diffuse lower bound kills every post-limit scale mixture

Let `pi` be any probability measure on positive scales and let

\[
\overline\mu
:=
\int\mu_{0,\rho}\,d\pi(\rho).
\tag{19}
\]

Assume for contradiction that

\[
\overline\mu\le\nu_a
\qquad\text{on }(-1,1)
\tag{20}
\]

for `a=a_MT`. The atom at zero in (19) has mass

\[
\overline\rho:=\int\rho\,d\pi(\rho),
\]

so

\[
\boxed{\overline\rho\le a.}
\tag{21}
\]

Markov's inequality therefore gives

\[
\pi\{\rho>2a\}
\le\frac{\overline\rho}{2a}
\le\frac12,
\]

hence

\[
\boxed{\pi\{\rho\le2a\}\ge\frac12.}
\tag{22}
\]

The diffuse profile (18) decreases with `rho` at every fixed `h>0`. At

\[
h_0:=\frac12,
\]

every component in the event from (22) obeys

\[
D_\rho(h_0)
\ge
1-\exp\left(-\frac{\pi^2}{8a^2}\right).
\tag{23}
\]

Averaging and discarding all other nonnegative components yields

\[
\boxed{
\overline D(1/2)
\ge
\frac12\left(
1-e^{-\pi^2/(8a^2)}
\right).
}
\tag{24}
\]

For the exact Montgomery--Taylor value,

\[
1-e^{-\pi^2/(8a^2)}
=0.886288893468587\ldots>a
=0.753296067856070\ldots .
\tag{25}
\]

Therefore

\[
\overline D(1/2)
\ge0.443144446734293\ldots
>
0.376648033928035\ldots
=\frac a2.
\tag{26}
\]

The gap is `0.066496412806258...`, far larger than any numerical-enclosure issue. Moreover `D_rho(h)` is bounded by one and continuous in `h`; dominated convergence makes `overline D` continuous on the open positive band. Thus the strict failure in (26) persists on a neighborhood of `1/2`, contradicting the absolutely continuous part of the measure domination (20). This proves (3).

Notice what the argument does **not** use: the weights `e^{-2pi^2 k^2}` of the residual reciprocal-lattice atoms, arithmetic commensurability between scales, or a Möbius harmonic inversion. The Gaussian shuffle itself creates too much moderate-frequency diffuse scattering once the forward-atom budget forces the mean scale below `a`.

## 6. Prior-art and novelty boundary

The fBm regularization, disappearance of nonzero Bragg peaks for fixed `H>0`, and the small-frequency law used in `ANF-025` are prior art from Thomassey--Lachièze-Rey--Shapira, arXiv:2602.19773v1. The `H=0` finite-dimensional Gaussian/white-noise representation is also known, as recorded explicitly by Malyarenko--Mishura--Ralchenko--Shklyar (2023). The diffraction of iid perturbed lattices and its Gaussian specialization are classical and already anchored through Klatt--Kim--Torquato in `SOURCES.md` and `ANF-023`.

What is derived here is the exact passage from the fBm Palm-lattice family to the zero-Hurst diffraction measure (1), the resulting reappearance of Bragg peaks despite their absence for every positive `H`, and the scale-mixture obstruction (21)--(26) specialized to the Montgomery--Taylor order interval. A targeted search across small-Hurst fBm limits, stationary-increment lattice regularization, shuffled-lattice diffraction and Bragg cloaking did not locate this exact weak-limit/MT-budget combination. No publication-level novelty claim is made.

No new `SOURCES.md` entry is required for the proof. Equations (4)--(16) derive the needed limit directly, while the external H=0 reference only establishes that the finite-dimensional white-noise limit itself is known prior art.

## 7. Evidence boundary and next filter

This finding closes the explicit **post-limit** `H=0` boundary left by `ANF-025`: fixed positive intensity fails, and arbitrary convex mixtures of the resulting zero-Hurst scale profiles fail even after continuous scale mixing removes their individual Bragg atoms.

It does **not** yet classify every singular double scaling performed before the limit. In particular, a family with

\[
H\downarrow0,
\qquad
\rho_H\downarrow0
\]

may probe frequencies `h/rho_H` that diverge while the Hurst exponent simultaneously degenerates; the convergence in Sections 1--4 is not asserted to be uniform in that regime. Likewise, an `H`-dependent mixture whose scale distribution itself collapses toward zero before taking the weak-* limit is not automatically represented by first taking `H=0` and then mixing (17).

That is now the precise remaining fBm-related question. Any such double-scaling candidate must be tested at the **full band profile**, not by the fixed-`H` infrared exponent alone. The configuration-level escape of `ANF-006` remains outside this universal-affine scalar diffraction branch and is unaffected.