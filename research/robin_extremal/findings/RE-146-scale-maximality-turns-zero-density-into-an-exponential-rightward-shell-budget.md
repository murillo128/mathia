# RE-146 — scale-maximality turns zero density into an exponential rightward shell budget

**Status:** `EXACT-DERIVED + FINITE-ZERO-EDGE + ACTUAL-ZETA-ZEROS + LEADING-ROBIN-LAYER + SCALE-MAXIMAL-ANCHOR + INGHAM-ZERO-DENSITY + RIGHTWARD-SHELL + EXPONENTIAL-RADIUS-BUDGET + PRIOR-ART-AUDITED`.

`RE-145` puts the local reciprocal-box problem on an explicit scale: a positive Robin packet of scaled radius `R` loses at most `exp(-O(R))` in normalized visibility, independently of cardinality. What it does not price is cancellation arriving from outside that box. The present finding gives the first source-specific exterior estimate in the **same scaled-radius variable**, for the rightward horizontal shell, after making one additional choice that is intrinsic to the Robin weights: anchor at an atom that is maximal at the observation scale.

The gain is not a new zero-density theorem. It comes from coupling two facts that were previously used separately. Scale-maximality forces every zero farther to the right to pay for its horizontal advantage through a smaller Robin coefficient, hence through larger ordinate. Looking slightly earlier than the maximizing scale converts that coefficient loss into a fractional moment, and Ingham zero density sums the resulting tail. The outcome is an `exp(-cR)` rightward-shell budget. The near-left layer and horizontally near but vertically remote zeros are not controlled here, so this is a genuine reduction of the frontier rather than a closure of Robin visibility.

Fix

\[
\frac12<\sigma_0<\Theta<1,
\qquad
U\to\infty,
\tag{1}
\]

and consider positive-ordinate strict-subedge zeros `rho=beta+i gamma` of `zeta` with `beta>=sigma_0`. For the leading Robin layer write

\[
d_\rho:=\frac1{\rho(1-\rho)},
\qquad
 a_{\rho,0}(u)
 :=e^{-(\Theta-\beta)u}d_\rho,
\qquad
 M_\rho(U):=|a_{\rho,0}(U)|.
\tag{2}
\]

Choose `rho_0=beta_0+i gamma_0` to maximize `M_rho(U)` over this strict-subedge set, and put

\[
M_0(U):=M_{\rho_0}(U).
\tag{3}
\]

The maximum exists whenever the set is nonempty: the zero set is discrete, while `|d_rho|=O((1+gamma^2)^{-1})` uniformly in the critical strip, so all sufficiently high zeros have smaller `M_rho(U)` than any fixed nonzero candidate.

Assume along the scales under consideration that the maximal atom is algebraically strong,

\[
M_0(U)\ge cU^{-A}
\tag{4}
\]

for fixed `c,A>0`. This is the same strength regime used throughout the attained finite-edge branch.

## 1. Scale-maximality forces a rightward zero to climb exponentially in ordinate

For any zero `rho=beta+i gamma` with `beta>=beta_0`, maximality gives

\[
e^{-(\Theta-\beta)U}|d_\rho|
\le
e^{-(\Theta-\beta_0)U}|d_{\rho_0}|,
\tag{5}
\]

hence, writing `Delta=beta-beta_0>=0` and

\[
q_\rho:=\frac{|d_\rho|}{|d_{\rho_0}|},
\tag{6}
\]

we have the exact inequality

\[
e^{U\Delta}q_\rho\le1.
\tag{7}
\]

In particular, for the rightward scaled shell

\[
\mathcal R_R^+(U)
:=
\left\{\rho:\beta\ge\beta_0+\frac RU\right\},
\tag{8}
\]

one has

\[
q_\rho\le e^{-R}.
\tag{9}
\]

On every fixed compact horizontal strip inside `(0,1)`, the leading Robin coefficient satisfies

\[
|d_\rho|\asymp \frac1{1+\gamma^2}.
\tag{10}
\]

Therefore (9) implies, with constants depending only on the fixed strip,

\[
1+\gamma^2
\gg
e^R(1+\gamma_0^2),
\tag{11}
\]

or equivalently

\[
1+|\gamma|
\gg
e^{R/2}(1+|\gamma_0|).
\tag{12}
\]

This is the first load-bearing coupling. A zero cannot beat the scale-maximal anchor horizontally without moving exponentially farther out in ordinate as the scaled horizontal displacement `R` grows.

The strength assumption (4) also gives two elementary calibrations that will be useful below. Since `|d_rho|=O(1)` in the fixed strip,

\[
(\Theta-\beta_0)U
\le
A\log U+O(1),
\tag{13}
\]

so `beta_0->Theta`. And because the exponential factor in (2) is at most one,

\[
|d_{\rho_0}|\ge cU^{-A},
\tag{14}
\]

which together with (10) gives

\[
1+|\gamma_0|\ll U^{A/2}.
\tag{15}
\]

## 2. Earlier observation turns maximality into a fractional coefficient moment

Fix `0<t<1` and put

\[
p:=1-t.
\tag{16}
\]

For every zero to the right of the anchor,

\[
\frac{|a_{\rho,0}(tU)|}{|a_{\rho_0,0}(tU)|}
=
e^{tU\Delta}q_\rho
=
\bigl(e^{U\Delta}q_\rho\bigr)^t q_\rho^{1-t}
\le
q_\rho^p,
\tag{17}
\]

where the last inequality is exactly (7). Thus the horizontal advantage of a rightward zero has disappeared. What remains is a fractional power of its coefficient ratio.

More generally, choose a fixed `eta` with `0<eta<1` and restrict to observation times

\[
0<t\le1-\eta.
\tag{18}
\]

Then `p>=eta`; because (7) also implies `q_rho<=1`, (17) yields uniformly on this earlier subwindow

\[
\frac{|a_{\rho,0}(tU)|}{|a_{\rho_0,0}(tU)|}
\le q_\rho^\eta.
\tag{19}
\]

Consequently

\[
\frac{
\sum_{\rho\in\mathcal R_R^+(U)}|a_{\rho,0}(tU)|
}{|a_{\rho_0,0}(tU)|}
\le
|d_{\rho_0}|^{-\eta}
\sum_{\rho\in\mathcal R_R^+(U)}|d_\rho|^\eta.
\tag{20}
\]

This is the second load-bearing step. The rightward shell has become a positive fractional moment of the Robin coefficient, so a one-level zero-density estimate can now control it without any phase information.

## 3. Ingham zero density makes the shell exponentially small in scaled radius

Fix `sigma_-<Theta`. By (13), for all sufficiently large `U` we have `beta_0>sigma_-`, hence every zero in `R_R^+(U)` is counted by `N(sigma_-,T)`.

Use the classical Ingham exponent already anchored in `SOURCES.md`,

\[
\nu_I(\sigma)
:=
\frac{3(1-\sigma)}{2-\sigma},
\tag{21}
\]

so that, with harmless logarithmic or `T^epsilon` loss,

\[
N(\sigma_-,T)
\ll_{\sigma_-,\varepsilon}
T^{\nu_I(\sigma_-)+\varepsilon}.
\tag{22}
\]

Write

\[
\nu:=\nu_I(\sigma_-).
\tag{23}
\]

If

\[
2\eta>\nu,
\tag{24}
\]

then dyadic summation of (22), using (10), gives for every sufficiently small `epsilon>0`

\[
\sum_{\substack{\beta\ge\sigma_-\\|\gamma|\ge H}}
|d_\rho|^\eta
\ll_{\sigma_-,\eta,\varepsilon}
H^{-2\eta+\nu+\varepsilon}.
\tag{25}
\]

Indeed the contribution from `H 2^j <= |gamma| < H 2^(j+1)` is

\[
\ll
(H2^j)^{-2\eta}
N(\sigma_-,H2^{j+1})
\ll
H^{-2\eta+\nu+\varepsilon}
2^{-j(2\eta-\nu-\varepsilon)},
\tag{26}
\]

and the geometric series converges once `epsilon<2 eta-nu`.

By (12), every member of `R_R^+(U)` has

\[
|\gamma|
\gg
H_R
:=
e^{R/2}(1+|\gamma_0|),
\tag{27}
\]

up to a fixed multiplicative constant. Substituting (25)--(27) into (20), and using

\[
|d_{\rho_0}|^{-\eta}
\asymp
(1+\gamma_0^2)^\eta,
\tag{28}
\]

gives the main estimate

\[
\boxed{
\sup_{0<t\le1-\eta}
\frac{
\sum_{\rho\in\mathcal R_R^+(U)}|a_{\rho,0}(tU)|
}{|a_{\rho_0,0}(tU)|}
\ll_{
\sigma_-,\eta,\varepsilon
}
(1+|\gamma_0|)^{\nu+\varepsilon}
\exp\!\left[-\left(\eta-\frac{\nu+\varepsilon}{2}\right)R\right].
}
\tag{29}
\]

The supremum notation in (29) means that the displayed upper bound is uniform for the indicated `t`; it is not an assertion that all earlier times belong to the original fixed-relative window. If the working observation window is `t in [1-kappa,1]`, choose

\[
\frac\nu2<\eta<\kappa.
\tag{30}
\]

Then the nonempty subwindow

\[
1-\kappa\le t\le1-\eta
\tag{31}
\]

inherits (29). Such a choice is possible whenever `nu_I(sigma_-)<2 kappa`. Since `sigma_-` may be chosen arbitrarily close to `Theta`, the relevant source-side condition is

\[
\nu_I(\Theta)<2\kappa
\tag{32}
\]

with strict slack. This window requirement is part of the theorem, not a technicality to suppress.

Finally (15) turns (29) into a pure scale/radius estimate:

\[
\frac{
\sum_{\rho\in\mathcal R_R^+(U)}|a_{\rho,0}(tU)|
}{|a_{\rho_0,0}(tU)|}
\ll
U^{A(\nu+\varepsilon)/2}
 e^{-cR},
\qquad
c:=\eta-\frac{\nu+\varepsilon}{2}>0.
\tag{33}
\]

Hence for

\[
R=\lambda\log U,
\qquad
\lambda>
\frac{A(\nu+\varepsilon)}{2c},
\tag{34}
\]

the entire sufficiently-rightward shell is `o(1)` relative to the scale-maximal anchor, uniformly on the subwindow (31).

## 4. What changed relative to RE-142 and RE-145

`RE-142` proves that upper zero-density envelopes cannot improve the generic `T^-2` cost incurred when an arbitrary designated strong atom is replaced by a farther-right atom. There is no contradiction. Here there is **no rightmost transfer**. The anchor itself is selected by the Robin amplitude at scale `U`, and maximality is used to derive the inequality (7). We then estimate an absolute exterior shell at an earlier time. The new source information is therefore the variational choice of anchor plus the actual coefficient law, not a stronger zero-density exponent.

`RE-145` gives local normalized visibility `exp(-O(R))` for a packet in a reciprocal box of scaled radius `R`, while (29) gives a rightward horizontal exterior budget `exp(-cR)` up to the explicit polynomial cost carried by the anchor ordinate. For the first time both sides of this part of the cancellation problem are priced in the same variable. This does **not** yet imply that the local floor beats the shell: the exponent in the `RE-145` interpolation floor is crude and may be larger than `c`, and the witness point furnished by local visibility still has to be coordinated with an early subwindow such as (31).

The result also does not touch two other exterior pieces. Zeros with

\[
|\beta-\beta_0|<\frac RU
\tag{35}
\]

but large vertical displacement are not in `R_R^+(U)`, and the near-left layer `beta<beta_0` remains the cancellation mechanism exhibited by `RE-144`. Those are now the honest remaining geometric pieces rather than being hidden inside a generic word such as “exterior.”

## 5. Adversarial audit

The estimate is deliberately leading-layer only. For `K>0` the coefficient is a `u`-dependent truncated expansion rather than the fixed `d_rho` used in the exact interpolation (17); no extension is claimed without a separate stability argument.

Multiplicity causes no problem: zeros are counted with multiplicity both in the Robin sum and in `N(sigma,T)`, so the dyadic estimate (25) keeps the same form. No simplicity, spacing, pair-correlation or phase-randomness hypothesis is used.

The scale-maximality assumption is stronger than merely designating some algebraically strong atom. It is essential: without (7), a farther-right zero may gain exponentially between `tU` and `U` without paying a coefficient penalty, and the fractional-moment reduction disappears. Conversely, scale-maximality is not an external conjecture; it is a choice among the actual Robin atoms at each scale.

The condition `2 eta>nu` is also essential to this proof. At the endpoint the fractional coefficient moment need not be summable under the stated one-level density law. Thus a too-short observation window is not covered.

Finally, (29) is an **absolute** shell estimate. It does not exploit cancellation among exterior modes, so any future sign/phase information can only improve this particular budget.

## 6. Prior-art and source audit

The only external theorem used load-bearingly is Ingham's classical zero-density estimate, already anchored in `research/robin_extremal/SOURCES.md`. A targeted prior-art check covered classical and modern zero-density literature, weighted zero sums, and Robin/RH explicit-formula work. Those sources contain the density estimate and related linear-statistic machinery, but I found no result in the checked literature that splices a **scale-maximal Robin atom**, the exact inequality `e^(U Delta) q<=1`, earlier-time fractionalization, and zero density to obtain an exponential budget in reciprocal-scale horizontal radius. The novelty claim is limited to that splice; neither Ingham's estimate nor the elementary coefficient asymptotic is claimed as new.

No new durable source dependency is introduced, so `SOURCES.md` does not need modification.

## 7. Next falsifiable target

The useful next target is no longer “control the exterior” as a single object. It is to synchronize the `RE-145` local witness with a subwindow where (29) holds, and to price the two pieces still outside this theorem: the near-left layer and the vertically remote strip with `|beta-beta_0|<R/U`. A successful splice would need the local `exp(-C R)` floor to dominate all three budgets for one common `R(U)` and one common observation point. If that comparison fails quantitatively, the failure itself should identify which source-specific relation among actual zeta zeros is still missing.