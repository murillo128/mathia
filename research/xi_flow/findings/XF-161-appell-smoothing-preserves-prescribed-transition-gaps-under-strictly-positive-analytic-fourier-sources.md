---
type: negative
research_line: xi_flow
finding_id: XF-161
status: canonical
---

# XF-161 — Appell smoothing preserves prescribed transition gaps under strictly positive analytic Fourier sources

**Confidence:** high for the finite-horizon source class proved below. The Appell identity, Gaussian source convolution, and Möbius transition map are exact. Combined with XF-160, they produce smooth strictly positive even Fourier densities with asymptotically prescribed nonzero transition gaps on every arbitrarily prescribed finite heat window. This does **not** produce one deformation with a Gaussian-mixture source valid for all positive heat times, and it does not reproduce the superexponential tails or arithmetic structure of the Riemann Xi kernel.

## Statement

XF-160 showed that nonnegativity of the Fourier source does not exclude the maximal-contact transition mechanism, but its controls use finite discrete measures. That leaves an immediate source-side escape: perhaps the obstruction is an artifact of atoms, whereas the Xi source is a smooth strictly positive density.

That escape also fails at the level of finite heat windows. Let

\[
U_s=-aU_{zz},\qquad a>0,
\tag{1}
\]

be either centered positive-spectrum control from XF-160, written at time zero as

\[
U(0,z)=\int_{\mathbb R}e^{i\eta z}\,d\mu(\eta),
\tag{2}
\]

where `mu` is a finite, nonzero, even, nonnegative discrete measure. Fix `sigma>0`, put

\[
h(s):=1-\frac{2as}{\sigma^2},
\qquad
\phi_\sigma(s):=\frac{s}{h(s)},
\tag{3}
\]

and, for `s<sigma^2/(2a)`, define the backward-heat Appell transform

\[
\boxed{
V(s,z):=
 h(s)^{-1/2}
 \exp\!\left(-\frac{z^2}{2\sigma^2h(s)}\right)
 U\!\left(\phi_\sigma(s),\frac{z}{h(s)}\right).
}
\tag{4}
\]

Then:

1. `V_s=-aV_zz` exactly on `s<sigma^2/(2a)`.
2. Its time-zero Fourier source is absolutely continuous,

\[
V(0,z)=\int_{\mathbb R}e^{i\xi z}\nu_\sigma(\xi)\,d\xi,
\tag{5}
\]

with

\[
\boxed{
\nu_\sigma(\xi)
=
\frac{\sigma}{\sqrt{2\pi}}
\int_{\mathbb R}
\exp\!\left[-\frac{\sigma^2}{2}(\xi-\eta)^2\right]
\,d\mu(\eta).
}
\tag{6}
\]

For the XF-160 measures this is a finite Gaussian mixture. It is even, strictly positive on all of `R`, real-analytic (indeed entire as a function of `xi`), and has Gaussian tails.
3. For every `s<sigma^2/(2a)`, the same solution has the exact source representation

\[
\boxed{
V(s,z)
=
\int_{\mathbb R}e^{as\xi^2}\nu_\sigma(\xi)e^{i\xi z}\,d\xi.
}
\tag{7}
\]

4. Zeros are transported only by a real dilation. Since the prefactor in `(4)` never vanishes and `h(s)>0`, `V(s,.)` has only real zeros if and only if `U(phi_sigma(s),.)` has only real zeros.

The time map `phi_sigma` is strictly increasing and sends

\[
\left(-\infty,\frac{\sigma^2}{2a}\right)
\longrightarrow
\left(-\frac{\sigma^2}{2a},\infty\right).
\tag{8}
\]

Its inverse is

\[
\boxed{
\Psi_\sigma(t)
=
\frac{t}{1+2at/\sigma^2},
\qquad t> -\frac{\sigma^2}{2a}.
}
\tag{9}
\]

Hence, whenever an old all-real threshold `Lambda_U` lies in the interval on the right of `(8)`, the transformed threshold is exactly

\[
\boxed{
\Lambda_V=\Psi_\sigma(\Lambda_U).
}
\tag{10}
\]

Now fix an arbitrary desired limiting transition gap `rho>0` and an arbitrary finite positive observation horizon `T>0`. Choose any

\[
\sigma^2>2aT
\tag{11}
\]

and calibrate the XF-160 old gap by

\[
\boxed{
\rho_0
:=
\frac{\rho}{1+2a\rho/\sigma^2}.
}
\tag{12}
\]

Then `0<rho_0<sigma^2/(2a)` and

\[
\Psi_\sigma(-\rho_0)=-\rho.
\tag{13}
\]

Apply `(4)` separately to the XF-160 pair with parameters `lambda=1` and `lambda=lambda_(r,rho_0)`. If their transformed thresholds are denoted by `Lambda^A_M(1)` and `Lambda^A_M(lambda_(r,rho_0))`, then for all sufficiently large `M`, `(10)` applies and XF-160 gives

\[
\boxed{
\Lambda^A_M(1)\longrightarrow0,
\qquad
\Lambda^A_M(\lambda_{r,\rho_0})\longrightarrow-\rho.
}
\tag{14}
\]

Thus their transition gap tends to the arbitrarily prescribed value `rho`, while both time-zero Fourier sources are **strictly positive real-analytic densities** and their backward-heat Fourier integrals are valid throughout the arbitrarily prescribed window `(-infinity,T]`.

Consequently, positivity plus absolute continuity plus strict positivity plus real-analytic Gaussian-mixture regularity of the Fourier source, even together with exact backward-heat transport on every fixed finite heat window, is still insufficient to rule out the transition-time separation mechanism behind XF-160. Any successful Xi-specific source theorem must use structure stronger than those qualitative regularity properties.

## 1. Exact Appell covariance for coefficient `a`

The coefficient in `(4)` matters because the xi-flow normalization need not use the unit heat equation. Write

\[
t=\phi_\sigma(s)=\frac{s}{h(s)},
\qquad
x=\frac{z}{h(s)},
\qquad
P(s,z)=h(s)^{-1/2}e^{-z^2/(2\sigma^2h(s))}.
\tag{15}
\]

Since

\[
h'(s)=-\frac{2a}{\sigma^2},
\qquad
t'(s)=h(s)^{-2},
\qquad
x_s=\frac{2az}{\sigma^2h(s)^2},
\tag{16}
\]

a direct differentiation of `V=P U(t,x)` yields

\[
V_s+aV_{zz}
=
P h(s)^{-2}
\bigl(U_t+aU_{xx}\bigr)(t,x).
\tag{17}
\]

Equation `(1)` therefore implies `V_s=-aV_zz`. No asymptotic approximation is involved.

The same covariance also shows why the singular time `sigma^2/(2a)` is structural: at that time the real dilation `h(s)` collapses and the Gaussian Fourier source reaches the edge of its positive-time exponential-moment domain.

## 2. Gaussian multiplication smooths every XF-160 atom without changing sign

At `s=0`, `(4)` reduces to

\[
V(0,z)=e^{-z^2/(2\sigma^2)}U(0,z).
\tag{18}
\]

Using the Fourier identity

\[
e^{-z^2/(2\sigma^2)}
=
\frac{\sigma}{\sqrt{2\pi}}
\int_{\mathbb R}
 e^{-\sigma^2\xi^2/2}e^{i\xi z}\,d\xi,
\tag{19}
\]

multiplication in `z` turns `(2)` into the convolution `(6)`. Because `mu` is even and nonnegative, so is `nu_sigma`. Because `mu` is nonzero and every Gaussian in `(6)` is strictly positive, `nu_sigma(xi)>0` for every real `xi`.

For the finite XF-160 measure, `(6)` is explicitly a finite sum of shifted Gaussians with positive coefficients. It is therefore real-analytic on `R` and extends to an entire function of `xi`. Its tails are Gaussian up to a finite shift determined by the outermost frequency.

The exact positive-time representation `(7)` can also be verified without appealing to uniqueness of the PDE. Substituting `(6)` and integrating first in `xi`, the Gaussian exponent is

\[
-\frac{\sigma^2h(s)}2\xi^2
+(\sigma^2\eta+iz)\xi
-\frac{\sigma^2\eta^2}{2}.
\tag{20}
\]

For `h(s)>0` the integral is Gaussian and evaluates to

\[
h(s)^{-1/2}
 e^{-z^2/(2\sigma^2h(s))}
 e^{a\phi_\sigma(s)\eta^2}
 e^{i\eta z/h(s)}.
\tag{21}
\]

Integrating `(21)` against `mu` gives `(4)` exactly.

For these finite mixtures, the condition `s<sigma^2/(2a)` is also the sharp positive-time integrability boundary of `(7)`: the quadratic decay in `(6)` dominates `e^(as xi^2)` exactly before that time. Negative heat times only improve integrability.

## 3. The zero-transition threshold undergoes a Möbius time change

The prefactor `P(s,z)` in `(15)` is entire and zero-free in `z`; `h(s)` is positive on the Appell domain. Hence every zero `x_*` of `U(phi_sigma(s),.)` corresponds exactly to the zero

\[
z_*=h(s)x_*
\tag{22}
\]

of `V(s,.)`, with multiplicity preserved. In particular, reality or nonreality of the complete zero set is unchanged.

Moreover,

\[
\phi_\sigma'(s)=h(s)^{-2}>0.
\tag{23}
\]

If the old all-real set is `[Lambda_U,infinity)` and `Lambda_U>-sigma^2/(2a)`, its preimage inside the Appell domain is therefore

\[
[\Psi_\sigma(\Lambda_U),\sigma^2/(2a)).
\tag{24}
\]

This proves `(10)` as the first all-real time of the transformed deformation on its natural heat interval.

For the two XF-160 controls, the old thresholds converge to `0` and `-rho_0`. Equation `(12)` leaves a fixed margin

\[
\frac{\sigma^2}{2a}-\rho_0>0,
\tag{25}
\]

so both finite-degree thresholds lie in the image interval `(8)` for all sufficiently large `M`. Continuity of `Psi_sigma` then gives the first limit in `(14)` and

\[
\Psi_\sigma(-\rho_0)
=
\frac{-\rho_0}{1-2a\rho_0/\sigma^2}
=-\rho,
\tag{26}
\]

which gives the second.

The calibration is important. Simply applying a fixed Appell transform to an XF-160 pair with old limiting gap `rho` would generally change the gap. Formula `(12)` chooses the old control so that the **new** limiting separation is exactly the prescribed `rho`.

## 4. What this removes from the source-side frontier

XF-160 left open the possibility that atomicity itself was responsible for the negative control. XF-161 removes that explanation on every finite heat window. The same transition geometry can be embedded in source densities that are simultaneously even, nonnegative, everywhere strictly positive, absolutely continuous, real-analytic, and finite Gaussian mixtures.

This is a meaningful strengthening because the Appell transform does not perturb zero locations approximately: it transports the full zero set by the exact map `(22)` and the heat parameter by the exact Möbius map `(9)`. The nonzero transition gap therefore survives as a theorem, not merely as a continuity heuristic.

What remains different from Xi is correspondingly sharper. The actual Riemann kernel has a very specific theta-series formula and superexponential decay, whereas `(6)` has only Gaussian tails. Its logarithmic derivatives, total-positivity properties, moment sequence, and large-frequency shape need not resemble those of `Phi`. A source-side proof must therefore exploit such quantitative shape information, or another exact Xi identity, rather than only positivity and qualitative smoothness.

A useful next gate is to ask for a **scale-stable tail or logarithmic-derivative inequality actually proved for the Xi kernel** and test it against the Appell-smoothed maximal-contact family. If Gaussian tails already violate that inequality, the inequality identifies genuine source information absent from the controls. If an appropriate rescaled version survives, the source obstruction must be refined again.

## Prior-art and novelty audit

The Appell transformation for the heat equation is classical. A modern reference already recorded in `SOURCES.md` is Amalia Torre, *Appell Transformation and Canonical Transforms*, SIGMA 7 (2011), 072, DOI `10.3842/SIGMA.2011.072`; it reviews the caloric Appell transform and its transform-theoretic interpretation. The broader de Bruijn--Newman framework for Fourier transforms of even nonnegative measures is also classical; XF-160 cites C. M. Newman, *Fourier transforms with only real zeros*, Proc. Amer. Math. Soc. 61 (1976), 245--251.

A directed search for Appell transformations specifically combined with de Bruijn--Newman transition constants or with this maximal-contact control did not locate a matching result. The classical ingredients are not claimed as new. The Mathia-specific contribution is their exact composition with XF-160: Gaussian convolution upgrades the source from a positive discrete measure to an everywhere-positive analytic density, while the Möbius calibration `(12)` preserves an arbitrary prescribed limiting transition gap on every fixed finite heat window.

No external theorem is load-bearing beyond the standard Appell identity, which is independently derived in `(15)`--`(17)` and `(20)`--`(21)`. `SOURCES.md` therefore requires no update.

## Falsification boundary

The finite-window qualifier is essential. A fixed Gaussian-mixture source in `(6)` does **not** define `(7)` for arbitrarily large positive `s`: the Fourier integral ceases to converge at `s=sigma^2/(2a)`. Given any finite `T`, `(11)` moves this singularity beyond `T`, but one does not obtain one source valid on all `s>=0`. Any claim of global positive-time equivalence to the Xi deformation would therefore be false.

The source tails are also only Gaussian. Xi's kernel decays superexponentially, so this construction does not show that the maximal-contact family survives a source theorem strong enough to encode Xi's true tails. Nor does analyticity of `nu_sigma` imply the special total-positivity, log-concavity, moment, or arithmetic conditions one might hope to derive for `Phi`.

Finally, XF-161 is a **source-class and zero-transition negative control**, not a transfer theorem for the normalized observation bounds of XF-159. Appell multiplication and space-time dilation change raw field amplitudes and observation geometry. No claim is made here that the full-field exponential blindness estimates survive unchanged after smoothing; the theorem proved is the persistence of the prescribed transition separation under substantially stronger source regularity.

The two matched controls still have different source densities. A diagnostic given the entire exact Xi source can distinguish them trivially. The result only eliminates the listed qualitative source properties as sufficient hypotheses for excluding the control.

No claim about the actual de Bruijn--Newman constant of the Riemann Xi function follows.

## Consequence for `xi_flow`

The source-side frontier has narrowed twice. XF-160 showed that **positivity is too weak**; XF-161 now shows that adding **absolute continuity, strict positivity and real-analytic Gaussian-mixture regularity is still too weak on every fixed heat window**. Atomicity is therefore not the essential defect of the maximal-contact countermodel.

The next source discriminator should be quantitative rather than qualitative: Xi's superexponential tail profile, a proven differential inequality for `Phi`, an explicit-formula constraint stable under the destination scaling, or another property that cannot be manufactured by Gaussian smoothing of the folded-binomial-plus-edge source. That is the point at which a source theorem would begin to distinguish Xi from the present negative controls rather than merely distinguish smooth functions from discrete measures.