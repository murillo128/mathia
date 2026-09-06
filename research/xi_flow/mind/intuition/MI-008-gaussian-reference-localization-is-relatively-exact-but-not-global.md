# MI-008 — Gaussian-reference localization is accurate and bandwidth-sufficient locally, but Vieta conditioning is the live interface gate

**Evidence level:** exact Xi/Appell, seam, center-local approximation, selector localization, and Vieta-conditioning analysis through XF-080

## Core intuition

The Gaussian/Appell quotient is intrinsically local, but locality itself is no longer the main obstacle. XF-073--XF-074 establish super-polynomial Xi recovery on a safe center rectangle and a genuine global seam divisor. XF-078 then shows that the same matched quotient is **locally compressible at the ordinary Vieta mode count**, and XF-079 shows that the destination-matched weighted selector can be read at one center. The global seam bandwidth and full-center scan therefore do not block the center-local route.

The live obstruction is conditioning of the dictionary from an accurate local function to the normalized divisor/log-Vieta resource. XF-080 gives an exact matched control where exponentially accurate finite-band approximation produces a macroscopic first Vieta mode after outer normalization.

## Strongest justified principle

XF-073 uses the exact Gaussian/Appell symmetry of backward heat, periodizes both Xi and a known Gaussian reference, and divides. On `|Re z|<=L/4` the noncentral images pay a quadratic Gaussian penalty, giving super-polynomial relative recovery with derivative control on the actual high-line geometry.

XF-074 shows that the periodized reference has theta seam zeros and generic quotient poles, so the construction is not a global holomorphic zero carrier. XF-075--XF-077 rule out free exact global repairs and quantify the resulting full-period bandwidth cost.

XF-078 provides the crucial matched counterweight. Away from the seam the Gaussian quotient is a half-frequency wave plus Gaussian-small error, and an explicit integer-frequency trigonometric polynomial with `N+1` modes approximates it super-polynomially on the center rectangle. The global `Theta(L^2/v)` bandwidth is therefore a seam-crossing cost, not an intrinsic local information count.

XF-079 then uses the already chosen compact Fourier support to show exact sideband disjointness. At each physical frequency only one center harmonic is active, so the modulus and the weighted `X(B)` resource are independent of center. A single safe-center comparison is enough for the source norm.

XF-080 shows why those two repairs still do not complete the bridge. The explicit XF-078 Laurent polynomial has exponentially small outer coefficients; normalizing either edge to Vieta form yields `|P_1|=Theta(N)` and a non-unit terminal coefficient. Local function error does not control the normalized root/divisor coordinates because the inverse normalization is exponentially ill-conditioned.

Thus **mode sufficiency and center sufficiency do not imply Vieta-state sufficiency**. The interface must control the conditioning of the normalization that turns a finite trigonometric surrogate into the destination resource.

## What remains possible

Construct a different center-local surrogate with a lower-bounded outer coefficient and bounded low log-Vieta modes while preserving the XF-073 source accuracy; or bypass root-polynomial normalization and derive the XF-079 selector/logarithmic resource directly from the Gaussian quotient. Either route must be measured in the exact weighted destination norm.

The positive-`Lambda` half remains independent: even a perfect conditioned source bridge must still show nontrivial guarded destination mass for a hypothetical transition state.

## Status / novelty

Appell transforms, Gaussian/theta periodization, local trigonometric approximation, no-aliasing sidebands, and Fourier-extension conditioning are classical mechanisms. The durable Xi synthesis is the sharpened bridge boundary: **the center-local route has enough bandwidth and does not require a center scan, but normalized Vieta/divisor conditioning can still destroy the usable source state.**

## Falsification criterion

Show that the XF-078 explicit surrogate can be normalized into a bounded-displacement real periodic Vieta carrier despite XF-080's exact coefficient ratios; invalidate the XF-079 one-center norm identity; or prove a uniform implication from the center-local approximation norm to bounded normalized Vieta coordinates. Any such result would remove the current interface gate.