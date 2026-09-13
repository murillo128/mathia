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

`WI-267` now extracts a geometry-independent source-specific theorem from the same operator. For any nonzero null vector `A_a v=0`, with closed essential support `S` and active lag set

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

## Research question

Can the exact Suzuki null equation plus the pointwise translation domination from `WI-267` force a **quantitative unscreenable arithmetic overlap** for a hypothetical first-crossing mode?

The live target is no longer merely to prove that prime translations reach every support gap. That is now exact. What is needed is a bridge from translated activity to an invariant that cannot cancel globally, for example one of the following kinds of conclusions:

\[
\sum_{\ell\in\mathcal P_{a_*}}c_\ell |C_v(\ell)|
\ge \eta(a_*)>0,
\]

or a source-weighted signed lower bound strong enough to enter `\mathcal F_v(r)`, or a quantitative overlap/flux inequality on the finite translation graph that survives phases and signs. Any such bound must be derived from the actual equation rather than from generic support counting.

## Decisive test

Start from a nonzero hypothetical first-crossing mode with `a_*>0.8`, its exact distributional equation

\[
(-g'')*v=0\quad\text{on }(-a_*,a_*),
\]

and the support cover from `WI-267`. Decompose the complement of `S=supp(v)` into connected components. On each component, at least one active translate is present everywhere. The decisive positive route is to show that the finite family of translated pieces cannot cancel the analytic archimedean convolution on all components unless some arithmetic overlap carries a definite amount of mass or phase coherence.

Useful formulations may include a finite translation graph on support components, a local linear system obtained by differentiating or analytically continuing the gap equation, or a conservation/flux identity that sums over components and removes pointwise phase cancellation. A successful theorem should produce a quantity that is visible to the sliding lower-envelope family or another established Weil-form invariant.

The decisive negative test is a **source-compatible multi-component mode or asymptotically exact family** that satisfies the actual local convolution equation while obeying the `WI-267` translation cover and still screens all prime-lag autocorrelations relevant to the current first-crossing inequalities. Another abstract self-adjoint operator, another translation-free gap, or another endpoint-bump construction no longer reaches the gate.

## Stress tests

Any proposed bootstrap must survive all existing boundary results. `WI-257` rules out obtaining the needed regularity from generic bounded-self-adjoint zero-mode arguments. `WI-263` defeats one-prime sign/Bochner reasoning. `WI-264` shows that finitely many source atoms can be hidden from autocorrelation observables. `WI-265` shows that generic first-crossing positivity does not recover the missing source geometry. `WI-266` excludes the simplest endpoint screen only after restoring Suzuki's operator, and `WI-267` proves that every surviving null mode must have prime translations active throughout every support gap.

The new support cover is therefore necessary but not sufficient. It must not be silently upgraded to `C_v(\log n)\ne0`: a gap point `x` can have `v(x)=0` but `v(x+\ell)\ne0`, so translated activity there contributes to the pointwise null equation while contributing nothing directly to the autocorrelation integrand `v(x+\ell)\overline{v(x)}`. Likewise, finite-union support measure bounds from the cover are too weak on their own.

Any argument using Suzuki's pointwise formula must also respect the full-domain warning. General ground states lie in `D(A_a)`, not necessarily `H_0^1`. `WI-267` resolves this for the null equation by a form-core/distributional passage; subsequent steps should remain distributional or explicitly prove whatever additional regularity they need.

## Evidence boundary

`WI-267` proves exact pointwise translation domination of the support complement. It does **not** prove that arbitrary macroscopic support gaps are impossible; a gap is allowed when active prime translates cover it. It does not prove a positive prime-lag autocorrelation, a lower bound on overlap measure, a sign rule for translated pieces, or incompatibility of a translation-dominating multi-component support with the actual null equation.

The first-crossing lower-envelope constraints from `WI-253`/`WI-258` and the pointwise support theorem from `WI-267` are presently independent necessary conditions on the same hypothetical mode. The open problem is to couple them without discarding the source geometry that made `WI-266` and `WI-267` possible.

## Research disposition

The clue remains `accepted`, but the support-propagation subproblem is resolved. Do not spend further passes trying to prove merely that a Suzuki null vector cannot have a prime-translation-free gap; `WI-267` already gives the exact full-domain statement.

Attack the **activity-to-overlap** step: classify translation-dominating support graphs compatible with the null equation, then determine whether phase/sign cancellation can keep every source-relevant autocorrelation screened. Persist a positive quantitative overlap/flux theorem, or a genuine source-compatible multi-component countermodel that survives the actual equation. Either outcome materially advances the defect-to-zero program.