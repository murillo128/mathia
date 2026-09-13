---
id: CLUE-weil-inertia-first-global-crossing-sliding-autocorrelation-symbol
type: research-clue
status: accepted
origin: research-watch
target_line: weil_inertia
based_on:
  - research/weil_inertia/findings/WI-253-first-global-crossing-has-a-sliding-autocorrelation-flux-constraint.md
  - research/weil_inertia/findings/WI-254-sliding-aperture-profile-is-invertible-but-small-scale-firstness-is-saturated.md
  - research/weil_inertia/findings/WI-255-first-small-aperture-correction-is-universal-and-cannot-bootstrap.md
  - research/weil_inertia/findings/WI-256-next-small-aperture-remainder-is-a-local-translation-defect-modulus.md
  - research/weil_inertia/findings/WI-257-bounded-perturbation-zero-modes-do-not-upgrade-translation-regularity.md
  - research/weil_inertia/findings/WI-258-phase-modulation-couples-firstness-slack-to-localized-cosine-defect.md
  - research/weil_inertia/findings/WI-263-full-span-autocorrelations-can-null-the-first-prime-and-screen-the-localized-phase-defect.md
  - research/weil_inertia/findings/WI-264-finite-aperture-endpoint-autocorrelations-screen-all-prime-layers.md
  - research/weil_inertia/findings/WI-265-endpoint-screening-survives-an-abstract-first-crossing-compression-model.md
  - research/weil_inertia/findings/WI-266-suzuki-null-equation-rules-out-endpoint-bump-screening.md
  - research/weil_inertia/findings/WI-267-suzuki-null-modes-admit-no-prime-translation-free-support-gap.md
  - research/weil_inertia/findings/WI-268-archimedean-sign-change-breaks-unrestricted-semigroup-positivity.md
  - research/weil_inertia/findings/WI-269-first-crossing-null-modes-induce-a-psd-signed-source-laplacian.md
---

# Can Suzuki-specific first-crossing rigidity force unscreenable arithmetic overlap?

## Observation

`WI-253` and `WI-258` give exact lower-envelope families that every hypothetical first unrestricted localized Weil zero mode must satisfy. With

\[
d\mu_v(h)=C_v(h)\left[
\sum_{\log n<2a_*}\frac{\Lambda(n)}{\sqrt n}\,\delta_{\log n}(dh)
+w(h)\,dh
\right],
\]

the first-crossing mode obeys

\[
\mathcal F_v(r)=\int_0^{2a_*}\min(h,2r)\,d\mu_v(h)
\ge r\lambda_r>0
\qquad(0<r<a_*),
\]

while phase modulation supplies the additional localized cosine-defect family from `WI-258`.

`WI-264` showed that source signs and finitely many prime-power layers can be screened at the level of autocorrelation by a two-endpoint construction, and `WI-265` showed that generic abstract first-crossing positivity does not defeat that geometry. `WI-266` then used Suzuki's actual null equation to exclude the explicit endpoint family.

`WI-267` extracts a geometry-independent source-specific theorem from the same operator. For any nonzero null vector `A_a v=0`, with closed essential support `S` and active lag set

\[
\mathcal P_a=\{\log n:\Lambda(n)>0,\ \log n\le2a\},
\]

one has

\[
\boxed{
(-a,a)\subset
S\cup\bigcup_{\ell\in\mathcal P_a}
\bigl((S-\ell)\cup(S+\ell)\bigr).
}
\]

Thus no open support gap can be simultaneously free of `v` and every active prime translation. The proof works for the full operator domain `D(A_a)`, not only the `H_0^1` core: Suzuki's form-core identity yields `(-g'')*v=0` distributionally, and on a prime-translation-free gap the regular kernel has the exact exponential expansion

\[
k(h)=e^{h/2}-\sum_{m\ge0}e^{-(5/2+2m)h}.
\]

Splitting the convolution across the gap produces a Laurent series with disjoint exponent families; local nullity forces all coefficients to vanish, and polynomial moment uniqueness then forces both sides of `v` to vanish. Hence the only translation-free-gap null vector is the zero vector.

This resolves the clue's previous **support-spreading/no-long-gap sub-gate**. The remaining issue is stronger: prime translations may be active at every gap point and still cancel the continuous convolution without forcing a nonzero global autocorrelation at any one lag.

`WI-268` closes a separate tempting shortcut. For the unrestricted localized Weil form, the off-diagonal continuous cross kernel is exactly `-w(h)` after the logarithmic singularity cancels Suzuki's regular remainder. Since `w(h)` changes sign at `h_0=\log\rho`, `\rho^3-\rho-1=0`, the full semigroup fails the first Beurling--Deny positivity criterion for every `a>h_0/2=0.1405997871...`, already before the first prime lag can activate. Thus a hypothetical first-crossing ground/null mode cannot be declared one-signed by ordinary Perron--Frobenius or positivity-preserving-semigroup theory. Any sign or overlap rigidity must come from the actual Suzuki equation, firstness, or a genuinely different cone/order structure.

`WI-269` now supplies such a source-conditioned structure. If `v` is the real first null mode, then every bounded real Lipschitz multiplier satisfies

\[
q_{a_*}(\chi v)
=
\sum_{\log n<2a_*}\frac{\Lambda(n)}{\sqrt n}D_\chi(v;\log n)
+
\int_0^{2a_*}w(h)D_\chi(v;h)\,dh
\ge0.
\]

Polarizing this identity shows that every finite multiplier partition of unity produces a positive-semidefinite signed Laplacian with zero row sums. For a sign-changing mode, the positive/negative nodal cut further gives the cancellation-free tariff

\[
\sum_{\log n<2a_*}\frac{\Lambda(n)}{\sqrt n}A_-(\log n)
+
\int_0^{h_0}w(h)A_-(h)\,dh
\le
\int_{h_0}^{2a_*}|w(h)|A_-(h)\,dh,
\]

where `A_-(h)` is the total opposite-sign overlap at lag `h`. This does not yet force a prime-lag overlap, but it replaces a single cancellation-prone scalar by a PSD family of localized source couplings and identifies exactly which long-range archimedean interaction can finance nodal prime overlap.

## Research question

Can the exact Suzuki null equation, the pointwise translation domination from `WI-267`, and the PSD signed-source Laplacian from `WI-269` force a **quantitative unscreenable arithmetic overlap** for a hypothetical first-crossing mode?

The live target is no longer merely to prove that prime translations reach every support gap. That is exact. Nor is it enough to add scalar autocorrelation constraints. What is needed is a bridge from translated activity to a localized source coupling that cannot be screened by phases/signs—for example a finite multiplier compression whose PSD/effective-resistance conditions force

\[
\sum_{\ell\in\mathcal P_{a_*}}c_\ell |C_v(\ell)|
\ge \eta(a_*)>0,
\]

or force a positive amount of prime-lag overlap before scalar cancellation, or yield a source-weighted signed lower bound strong enough to enter `\mathcal F_v(r)`. Any such bound must preserve the actual Suzuki source rather than return to generic support counting or generic ground-state positivity.

## Decisive test

Start from a nonzero hypothetical first-crossing mode with `a_*>0.8`, its exact distributional equation

\[
(-g'')*v=0\quad\text{on }(-a_*,a_*),
\]

the support cover from `WI-267`, and the multiplier form `\mathcal B_v` from `WI-269`. Choose a finite partition of unity adapted to support components, nodal components, or prime-translation neighborhoods. The decisive positive route is to prove that, if all source-relevant prime overlaps are below a proposed threshold, then the resulting signed Laplacian violates PSD—equivalently, a Schur-complement/effective-resistance or cut inequality becomes negative.

This test must retain the continuum archimedean edges and their sign change at `h_0`; replacing them by unsigned mass would erase the exact screening channel exposed by `WI-268` and `WI-269`. A useful finite theorem would therefore come with an error-controlled continuum-to-partition compression, not merely a heuristic graph picture.

The decisive negative test is a **source-compatible multi-component mode or asymptotically exact family** that satisfies the actual local convolution equation and the `WI-267` support cover while all finite source-adapted multiplier compressions remain PSD and all prime-lag autocorrelations relevant to the current first-crossing inequalities remain screened. Another abstract self-adjoint operator, another translation-free gap, another endpoint-bump construction, or another appeal to ordinary positive-semigroup ground-state theory no longer reaches the gate.

## Stress tests

Any proposed bootstrap must survive all existing boundary results. `WI-257` rules out obtaining the needed regularity from generic bounded-self-adjoint zero-mode arguments. `WI-263` defeats one-prime sign/Bochner reasoning. `WI-264` shows that finitely many source atoms can be hidden from autocorrelation observables. `WI-265` shows that generic first-crossing positivity does not recover the missing source geometry. `WI-266` excludes the simplest endpoint screen only after restoring Suzuki's operator, `WI-267` proves that every surviving null mode must have prime translations active throughout every support gap, and `WI-268` shows that ordinary Beurling--Deny/Perron--Frobenius order structure is unavailable for the unrestricted form throughout the relevant first-crossing regime. `WI-269` adds PSD only after conditioning on the actual null mode; it must not be misread as restoring a Markov sign pattern for the original operator.

The support cover is necessary but not sufficient. It must not be silently upgraded to `C_v(\log n)\ne0`: a gap point `x` can have `v(x)=0` but `v(x+\ell)\ne0`, so translated activity there contributes to the pointwise null equation while contributing nothing directly to the autocorrelation integrand `v(x+\ell)\overline{v(x)}`. Likewise, finite-union support measure bounds from the cover are too weak on their own.

Nor may one silently add a one-sign hypothesis for the ground/null mode. `WI-268` proves failure of positivity preservation of the full localized Weil semigroup once `a>h_0/2`, but that failure is not itself a nodal theorem: a particular ground state could still be one-signed for a more specialized reason. `WI-269` remains nontrivial in that case through its multiplier PSD family, but its nodal tariff becomes vacuous.

Conversely, for a sign-changing mode the nodal inequality in `WI-269` is not yet an arithmetic lower bound. Long-range archimedean opposite-sign overlap may finance all short-range and prime opposite-sign overlap. Any effective-resistance or cut argument must therefore prove that this financing channel is quantitatively insufficient in the actual source geometry, rather than simply discarding it.

Any argument using Suzuki's pointwise formula must also respect the full-domain warning. General ground states lie in `D(A_a)`, not necessarily `H_0^1`. `WI-267` resolves this for the null equation by a form-core/distributional passage; `WI-269` uses only the closed-form domain and normal contraction for nodal parts. Subsequent pointwise steps must explicitly justify any stronger regularity they need.

## Evidence boundary

`WI-267` proves exact pointwise translation domination of the support complement. It does **not** prove that arbitrary macroscopic support gaps are impossible; a gap is allowed when active prime translates cover it. It does not prove a positive prime-lag autocorrelation, a lower bound on overlap measure, a sign rule for translated pieces, or incompatibility of a translation-dominating multi-component support with the actual null equation.

`WI-268` proves that the unrestricted localized semigroup is not positivity preserving for `a>h_0/2`. It does **not** prove that the first-crossing null mode changes sign. Its role here is narrower and decisive: the standard positive-semigroup route cannot supply the missing sign/phase coherence.

`WI-269` proves that the actual first null mode induces a PSD signed-source multiplier form and, when sign-changing, satisfies an exact cancellation-free nodal compensation law. It does **not** prove that any prime-lag overlap is positive, that the long-range archimedean budget is too small, or that a finite effective-resistance obstruction exists. Those are now the live quantitative gates.

The first-crossing lower-envelope constraints from `WI-253`/`WI-258`, the pointwise support theorem from `WI-267`, and the multiplier PSD family from `WI-269` are independent necessary views of the same hypothetical mode. The open problem is to couple them without discarding the source geometry that made `WI-266`, `WI-267`, and `WI-269` possible.

## Research disposition

The clue remains `accepted`, with the activity-to-overlap gate narrowed to a concrete source-conditioned matrix problem. Do not spend further passes trying to prove merely that a Suzuki null vector cannot have a prime-translation-free gap; `WI-267` already gives the exact full-domain statement. Do not infer constant sign from ordinary Perron--Frobenius/Krein--Rutman or positivity-preserving-semigroup theory; `WI-268` gives an exact archimedean obstruction long before the relevant first crossing.

Attack the **finite signed-source compression** next: choose partitions adapted to the actual support/nodal geometry, preserve the continuous `w(h)` edges, and test PSD by cut, Schur-complement, or effective-resistance inequalities under the hypothesis that prime overlap is screened. Persist a quantitative obstruction that forces arithmetic overlap, or a genuine source-compatible multi-component countermodel whose exact multiplier Laplacians remain PSD while the prime observables stay screened. Either outcome materially advances the defect-to-zero program.