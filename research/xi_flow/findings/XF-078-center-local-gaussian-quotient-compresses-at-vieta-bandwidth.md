# XF-078 — center-local Gaussian quotient compresses at ordinary Vieta bandwidth

**Status:** `EXACT-DERIVED` + `MATCHED-ZERO-FREE-CONTROL` + `CENTER-LOCAL-FINITE-BAND` + `GLOBAL/LOCAL-SEPARATION`. XF-077 proves that the matched zero-free Gaussian-reference quotient needs `Omega(L^2/v)` Fourier modes to capture a fixed fraction of its **full-period** derivative Sobolev energy. At the Xi scale this is `Theta((log T)^(9/2))`, larger by `Theta(sqrt(log T))` than the natural `Theta((log T)^4)` Vieta carrier.

That bandwidth obstruction is genuinely global. For the **same matched quotient at the same frozen time**, restriction to the center half-period admits an explicit entire trigonometric approximation at the ordinary Vieta bandwidth, with super-polynomial error. Put

\[
d:=\frac{\pi v}{L},
\qquad
a:=\frac{2\pi^2v}{L^2},
\qquad
R(z):=\frac{W_L(z-id)}{W_L(z)},
\tag{1}
\]

where `W_L` is the periodized Gaussian reference. Fix any

\[
0<\eta_0<\operatorname{arcosh}2.
\tag{2}
\]

Then for every fixed derivative order `J` there are constants `C_J>0`, `c_J>0`, and `a_J>0`, depending only on `J` and `eta_0`, such that for every `0<a<a_J` and every integer `D>=1` there is an `L`-periodic entire trigonometric polynomial

\[
F_D(z)=\sum_{|k|\le D}A_k e^{2\pi i k z/L}
\tag{3}
\]

with

\[
\boxed{
\max_{0\le j\le J}
\sup_{\substack{|\Re z|\le L/4\\
|2\pi\Im z/L|\le\eta_0}}
\left|
\left(\frac{L}{2\pi}\partial_z\right)^j
\bigl(R(z)-F_D(z)\bigr)
\right|
\le
C_J\left(
a^{-J}e^{-\pi^2/(2a)}+e^{-c_JD}
\right).
}
\tag{4}
\]

At the XF-073/XF-077 scaling

\[
L=(\log T)^3,
\qquad
v=(\log T)^{3/2}+O(1),
\qquad
a=\Theta((\log T)^{-9/2}),
\tag{5}
\]

the moving Xi high line has scaled imaginary height `2 pi Im z/L=O((log T)^(-2))`, so it lies in the rectangle of (4). Taking

\[
D=\Theta((\log T)^4)
\tag{6}
\]

gives

\[
\boxed{
\max_{j\le J}\sup_{\rm center\ high\ line}
\left|
\left(\frac{L}{2\pi}\partial_z\right)^j(R-F_D)
\right|
\le
\exp\!\bigl(-c_J(\log T)^4\bigr).
}
\tag{7}
\]

In the XF-067 normalization `N=2M`, choosing `D=M=N/2` uses exactly the symmetric integer-frequency set `-M,...,M`, hence `N+1` modes: the same mode count and frequency lattice as the ordinary degree-`N` periodic Vieta carrier. Thus the matched control that is asymptotically incompressible at `O(N)` modes in the **global** XF-077 Sobolev norm is simultaneously super-polynomially compressible at `N+1` modes on the **center-local** Xi rectangle.

This materially narrows the live obstruction. Static finite-band truncation and the `Theta(sqrt(log T))` seam bandwidth gap do **not** by themselves kill the center-local Gaussian-to-Vieta route. The remaining obligations are dynamical and source-specific: the actual Xi quotient must be transferred into the XF-070--XF-071 weighted destination norm, and any finite surrogate must pay its transport residual, normalization, and auxiliary-root costs. XF-078 does not provide those steps and does not identify a positive-`Lambda` transition state.

## 1. On the center strip the matched quotient is a half-frequency wave plus a Gaussian-small error

Suppress the harmless positive prefactor in the Gaussian reference and write

\[
W(z):=e^{-z^2/(2v)},
\qquad
W_L(z)=\sum_{m\in\mathbb Z}W(z+mL).
\tag{8}
\]

For `|Re z|<=L/4`, division by the central image gives

\[
\frac{W_L(z)}{W(z)}
=1+\varepsilon_0(z),
\qquad
\varepsilon_0(z)
=\sum_{m\ne0}
\exp\!\left(
-\frac{m^2L^2+2mLz}{2v}
\right).
\tag{9}
\]

The same formula at `z-id` gives

\[
\frac{W_L(z-id)}{W(z-id)}
=1+\varepsilon_1(z),
\tag{10}
\]

where the additional factor in the `m`-th summand has modulus one because `d` is real. Hence both tails have the same absolute bound. If `p=|m|>=1`,

\[
m^2L^2+2mL\Re z
\ge
\left(p^2-\frac p2\right)L^2
\ge\frac p2L^2.
\tag{11}
\]

With

\[
\alpha:=e^{-L^2/(4v)}
=e^{-\pi^2/(2a)},
\tag{12}
\]

we therefore have

\[
|\varepsilon_0(z)|+|\varepsilon_1(z)|
\le\frac{4\alpha}{1-\alpha}.
\tag{13}
\]

The estimate is independent of `Im z`: the imaginary displacement contributes only phases to the image ratios. Applying the dimensionless derivative `(L/(2 pi)) partial_z` to the `m`-th image contributes a factor of size `pi |m|/a`. Consequently, for every fixed `J`,

\[
\max_{j\le J}
\sup_{|\Re z|\le L/4}
\left|
\left(\frac{L}{2\pi}\partial_z\right)^j
\varepsilon_r(z)
\right|
\le
C_Ja^{-J}\alpha,
\qquad r\in\{0,1\},
\tag{14}
\]

for all sufficiently small `a`. Since the denominator in (9) is then bounded away from zero, fixed-order quotient differentiation gives

\[
R(z)
=
\frac{W(z-id)}{W(z)}
\left(1+O_J(a^{-J}\alpha)\right)
\tag{15}
\]

in the corresponding fixed derivative sense on the center strip.

The unperiodized ratio is exact:

\[
\frac{W(z-id)}{W(z)}
=
\exp\!\left(
\frac{id z}{v}+\frac{d^2}{2v}
\right)
=
\boxed{
e^{a/4}e^{i\pi z/L}.
}
\tag{16}
\]

Thus the entire seam complexity of the matched control is absent locally up to the Gaussian image error `e^{-pi^2/(2a)}`. What remains on the center strip is simply a half-integer Fourier wave.

## 2. The half-frequency wave has an explicit integer-frequency approximation away from the seam

Set

\[
\theta:=\frac{2\pi z}{L},
\qquad
u:=\frac{1-\cos\theta}{2}.
\tag{17}
\]

On the rectangle

\[
|\Re\theta|\le\frac\pi2,
\qquad
|\Im\theta|\le\eta_0,
\tag{18}
\]

write `c=cos(Re theta)>=0`. A direct calculation gives

\[
|1-\cos\theta|^2
=1-2c\cosh(\Im\theta)+c^2+\sinh^2(\Im\theta).
\tag{19}
\]

For fixed imaginary part the right side decreases as `c` ranges from `0` to `1`, because `cosh(Im theta)>1` except at zero. Hence

\[
\boxed{
|\nu|
\le\frac{\cosh\eta_0}{2}
=:\rho<1.
}
\tag{20}
\]

The strict inequality is exactly (2). Since `1-nu=(1+cos theta)/2` stays in the disk centered at `1` of radius `rho<1`, the principal square root is analytic there. The elementary half-angle identities therefore give throughout (18)

\[
\boxed{
e^{i\theta/2}
=(1-\nu)^{1/2}
+\frac{i}{2}\sin\theta\,(1-\nu)^{-1/2}.
}
\tag{21}
\]

Now use the absolutely convergent binomial series

\[
(1-\nu)^{1/2}
=\sum_{n\ge0}a_n\nu^n,
\qquad
(1-\nu)^{-1/2}
=\sum_{n\ge0}b_n\nu^n,
\tag{22}
\]

where

\[
a_n=(-1)^n\binom{1/2}{n},
\qquad
b_n=\frac1{4^n}\binom{2n}{n}.
\tag{23}
\]

Define

\[
P_D(\theta)
:=
\sum_{n=0}^{D}a_n\nu^n
+\frac{i}{2}\sin\theta
\sum_{n=0}^{D-1}b_n\nu^n.
\tag{24}
\]

Because `nu` is affine in `cos theta`, `nu^n` has Fourier frequencies only in `[-n,n]`; multiplication by `sin theta` increases the degree by at most one. Therefore

\[
\boxed{
P_D(\theta)
=\sum_{|k|\le D}p_{k,D}e^{ik\theta}.
}
\tag{25}
\]

This is an ordinary finite trigonometric polynomial, not a fractional-frequency or meromorphic object.

The tails in (22) are geometric on `|nu|<=rho`. For any fixed `J`, termwise differentiation adds only fixed powers of `n`; hence, after enlarging `rho` to any fixed `rho_*` with `rho<rho_*<1`,

\[
\boxed{
\max_{0\le j\le J}
\sup_{(18)}
|\partial_\theta^j(P_D(\theta)-e^{i\theta/2})|
\le
C_J\rho_*^D
\le C_Je^{-c_JD}.
}
\tag{26}
\]

No approximation theorem stronger than the binomial series is being used. The construction is explicit.

The place where it must fail globally is also explicit. At the opposite seam `theta=pi mod 2 pi`, `nu=1` and `1+cos theta=0`; the two half-angle branches in (21) meet their square-root singularity. Thus the same point that generates the theta seam and the XF-077 global spectral layer is precisely where the center-local geometric expansion loses its convergence margin.

## 3. Combining the two approximations proves the finite-band center theorem

Define

\[
F_D(z):=e^{a/4}P_D\!\left(\frac{2\pi z}{L}\right).
\tag{27}
\]

Equation (25) makes `F_D` an `L`-periodic entire trigonometric polynomial supported on `|k|<=D`. On the rectangle in (4), equations (15), (16), and (26) give

\[
R-F_D
=
\left(R-e^{a/4}e^{i\pi z/L}\right)
+e^{a/4}
\left(e^{i\theta/2}-P_D(\theta)\right).
\tag{28}
\]

The factor `e^{a/4}e^{i theta/2}` is uniformly bounded above and below when `a` is small and `|Im theta|<=eta_0`. Fixed dimensionless derivatives of the first term are bounded by (14)--(16), while those of the second term are bounded by (26). This proves (4).

There is no conflict with XF-076. `F_D` is not asserted to satisfy the exact Gaussian quotient drift globally, or even locally as a function of heat time; it is a frozen-time entire surrogate. XF-076 proves that exact global quotient transport plus finite frequency forces triviality. XF-078 proves that **static center-local approximation does not** force a large bandwidth or a large truncation error.

There is likewise no conflict with XF-077. On the full period the matched quotient has poles arbitrarily close to the real seam as `a->0`, and its derivative Sobolev energy spreads over `Theta(a^-1)` modes. Equation (4) excludes the seam by a fixed horizontal margin. The same function can therefore be globally incompressible and locally compressible in the two different norms/domains without contradiction.

## 4. The Xi zero-count mode budget is already enough locally

At the Xi localization scale,

\[
a^{-1}=\Theta((\log T)^{9/2}),
\qquad
\alpha
=\exp\!\left(-\Theta((\log T)^{9/2})\right).
\tag{29}
\]

XF-067--XF-071 use a periodic root model with

\[
N=\Theta((\log T)^4)
\tag{30}
\]

and, in the convenient even normalization, `N=2M`. Taking `D=M` in (27) gives `2M+1=N+1` Fourier modes, exactly the ordinary finite Vieta count. The geometric term in (4) then satisfies

\[
e^{-c_JD}
=
\exp\!\left(-\Theta((\log T)^4)\right),
\tag{31}
\]

while the image term is even smaller. This proves (7).

The contrast with XF-077 is quantitative, not semantic. The exact same matched quotient obeys

\[
\frac{\|R-F\|_{\dot H^s_{\rm idx}(\mathbb T_L)}^2}
{\|R\|_{\dot H^s_{\rm idx}(\mathbb T_L)}^2}
\ge1-O((\log T)^{-1/2})
\tag{32}
\]

for every global `O(N)`-mode surrogate in the XF-077 setting, yet it has the center-local approximation (7) using `N+1` modes. Therefore the `Theta(sqrt(log T))` deficit is a **seam-crossing cost**, not an intrinsic local information count for the matched heat datum.

The high-line location used in XF-073 fits comfortably inside the complex rectangle. There `Im z=hA log T`, so

\[
\left|\frac{2\pi\Im z}{L}\right|
=O((\log T)^{-2})\to0.
\tag{33}
\]

Thus (7) applies not merely on the real center interval but on the actual center-local complex contour geometry that motivated Gaussian periodization.

## 5. What this changes in the current frontier

XF-074--XF-077 successively rule out a global holomorphic quotient, a reference-only exact repair, an exact nonconstant finite-band quotient, and an ordinary-bandwidth global Sobolev approximation. Those are genuine obstructions, but they do not stack into a center-local no-go. XF-078 gives an explicit matched control demonstrating that the static finite-band step itself becomes cheap once the seam is excluded.

Accordingly, a future negative theorem against the center-local route must use more than the global `L^2/v` seam bandwidth. It must show that the **actual destination operation** re-exposes the seam or otherwise forces a norm/transport cost that the local approximation (4) cannot avoid. Conversely, a positive theorem still has to do substantially more than truncate (27): it must transport an actual Xi-dependent surrogate through time and into the XF-070--XF-071 weighted log-Vieta resource, control any auxiliary zero divisor created by that surrogate, and prove that a hypothetical positive-`Lambda` transition is nontrivial in the same quotient.

The finding therefore closes only one architectural ambiguity: `XF-077` cannot be promoted from a global Sobolev obstruction to a local mode-count obstruction. The natural Xi zero-count bandwidth is already sufficient for the matched zero-free datum on the safe center contour.

## 6. Prior-art and falsification boundary

The ingredients in section 2 are classical elementary approximation theory: the half-angle identities, the binomial series for `(1-u)^(+/-1/2)`, and the fact that a polynomial in `cos theta` is a finite trigonometric polynomial. Gaussian periodization and the theta seam are likewise classical and already delimited in XF-073--XF-077. A targeted prior-art check against standard Fourier/trigonometric approximation, compact localization, and theta-function references found no source attaching this elementary center expansion to the Xi-scale comparison `N=Theta((log T)^4)` versus the global seam scale `a^-1=Theta((log T)^(9/2))`. No novelty is claimed for the approximation ingredients themselves, and no new load-bearing `SOURCES.md` entry is required because the proof is explicit.

The result is deliberately a matched-control and frozen-time theorem. It does **not** show that the actual Xi Gaussian quotient is `O(N)`-mode compressible in the XF-070 weighted resource, does not estimate the heat-time residual of `F_D`, does not preserve a prescribed zero divisor, and does not supply a Vieta state with the collision/normalization properties required downstream. Those are precisely the remaining falsifiers.

To invalidate XF-078 itself, one would have to break one of its explicit identities: exhibit a point in the stated center rectangle where `|nu|>=1`, invalidate the Gaussian image estimate (11)--(14), or show that the polynomial (24) contains frequencies outside `[-D,D]`. None of those tests uses RH, real-zero labeling, or numerical evidence.