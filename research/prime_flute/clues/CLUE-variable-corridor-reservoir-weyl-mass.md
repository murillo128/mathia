---
id: CLUE-prime-flute-variable-corridor-reservoir-weyl-mass
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-228-flat-corridor-dressing-makes-inverse-seam-multiplicity-weak-trace-compatible.md
  - research/prime_flute/findings/PF-229-frozen-serial-schur-completion-preserves-flat-corridor-cut-scale.md
  - research/prime_flute/findings/PF-279-variable-scalar-schur-reservoirs-can-erase-local-corridor-cut-gain.md
  - research/prime_flute/findings/PF-280-one-sided-frequency-decoupled-schur-transfer-is-reservoir-stable.md
  - research/prime_flute/findings/PF-281-energy-normalized-cross-form-removes-bounded-frequency-coupling-gate.md
  - research/prime_flute/findings/PF-282-energy-normalized-cross-form-is-a-saturated-extension-angle.md
  - research/prime_flute/findings/PF-283-heavy-angle-counting-criterion-for-weak-trace-endpoint.md
  - research/prime_flute/findings/PF-284-two-sided-heavy-angle-counting-sandwich.md
  - research/prime_flute/findings/PF-285-complementary-weak-schatten-extension-strengths-close-the-weak-trace-endpoint-without-angle-decay.md
  - research/prime_flute/findings/PF-286-physical-extension-strengths-are-not-compact.md
  - research/prime_flute/findings/PF-222-reciprocal-prime-schur-commutator-is-compact-by-one-seam-decoupling.md
  - research/prime_flute/clues/CLUE-weak-trace-reassembly-with-summable-local-mass.md
---

# Does the physical heavy-sector extension angle close the weak-trace endpoint?

## Observation

PF-279 shows that a variable scalar reservoir can erase a favorable isolated cut scale, while PF-280/PF-281 separate that raw obstruction from the physically mixed low/high block. PF-282 gives the exact factorization

\[
T=F_P\Gamma_{PF}F_H,
\qquad
F_P=f(K_P^{1/2}),\quad F_H=f(K_H^{1/2}),
\qquad
f(t)=\frac{t}{\sqrt{1+t^2}},
\]

where the outer factors record extension strength and `\Gamma_{PF}` records the relative angle of the low-fed and high-fed extension ranges.

PF-283 supplies a convenient sufficient endpoint criterion. With

\[
Q_P^\tau=\mathbf1_{[\tau,1]}(F_P),
\qquad
Q_H^\tau=\mathbf1_{[\tau,1]}(F_H),
\qquad
\Gamma_{PF,\tau}=Q_P^\tau\Gamma_{PF}Q_H^\tau,
\]

it is enough that

\[
\sup_{0<\tau<\tau_0}
\tau\,N_{\Gamma_{PF,\tau}}(2\tau)<\infty.
\]

PF-284 shows that this particular `O(\tau^{-1})` count is not necessary: weak trace class itself only forces the weaker symmetric envelope `N_{\Gamma_{PF,\tau}}(2\tau)=O(\tau^{-3})`. PF-285 then identifies a second sufficient mechanism: if `F_P,F_H` have complementary finite weak-Schatten population exponents, the two strength factors alone can pay the weak-trace budget.

PF-286 now performs that first strength census for the **canonical physical split** and closes the population-only route negatively. PF-216 forces the low diagonal energy to be unbounded on the tangentially constant physical-low module tail, so

\[
\operatorname{rank}Q_P^\tau=\infty
\qquad(0<\tau<1).
\]

PF-227 forces the physical high strength to be noncompact, so there is `\tau_H>0` with

\[
\operatorname{rank}Q_H^\tau=\infty
\qquad(0<\tau\le\tau_H).
\]

Thus no finite `p_P,p_H` exist for PF-285's population-only criterion. The surviving endpoint question is genuinely angular: can `\Gamma_{PF}` turn two infinite-dimensional heavy sectors into a compact/weak-trace cross operator with the required thresholded singular-value decay?

## Research question

For the actual simultaneous one-cusp-pant extension, what is the singular-value distribution of

\[
\Gamma_{PF,\alpha,\beta}
=Q_P^\alpha\Gamma_{PF}Q_H^\beta
\]

on the physical heavy-strength sectors?

The strongest simple target remains the PF-283 symmetric law

\[
N_{\Gamma_{PF,\tau}}(2\tau)=O(\tau^{-1}),
\]

which is sufficient for `T\in\mathcal S_{1,\infty}`. Failure of that law is not endpoint failure. PF-284 leaves an intermediate regime, so the more flexible target is an asymmetric threshold budget: find physically adapted `\alpha_k,\beta_k,a_k` for which

\[
\alpha_k\beta_k a_k\,
N_{\Gamma_{PF,\alpha_k,\beta_k}}(a_k)
\]

stays uniformly bounded, or prove that the corresponding necessary budget diverges along a canonical sequence.

Because PF-286 shows that both physical sides contain infinite heavy populations, mere rank truncation can no longer help. The relevant theorem must establish actual transversality/compactness of the low-fed and high-fed pant extension ranges.

## Why it may matter

PF-281 proves that `T\in\mathcal S_{1,\infty}` closes the mixed Schur/reciprocal-prime commutator gate. PF-286 removes a potentially cheaper but misleading direction: there is no finite global strength exponent to estimate on either side, so further work on polynomial population counts cannot close the canonical endpoint.

This focuses the geometry sharply. A positive heavy-angle theorem would show that the actual pant extension separates physical low and high directions strongly enough to overcome infinite saturated strength on both sides. A negative theorem would need more than a failed convenient sufficient estimate: by PF-282, a fixed heavy compression that is noncompact is already a genuine obstruction to compactness of `T`, while PF-284 quantifies how much thresholded angle mass can remain compatible with weak trace class.

## Decisive test

Construct the actual simultaneous pant-extension realization of

\[
K_{PF}=\Lambda_Q^{-1/2}\Lambda_E\Lambda_Q^{-1/2}
\]

with the physical PF-212 `P/H` projectors fixed before any simplifying coordinate change. Form the polar range maps `V_P,V_H` and

\[
\Gamma_{PF}=V_P^*V_H.
\]

Use PF-286's heavy sectors as the stress-test domain rather than attempting another strength census. On the low side, the PF-216 constant-mode tail is heavy at every fixed threshold. On the high side, PF-227 supplies infinitely many fixed-strength high channels. Determine whether the corresponding extension images become asymptotically transverse after finite-pant completion and neighboring-cell coupling.

A decisive positive result should prove compactness plus a quantitative singular-value count for the relevant heavy compression, preferably the PF-283 `O(\tau^{-1})` sufficient law or an asymmetric PF-284-compatible replacement. A decisive negative result should exhibit an infinite orthonormal heavy sequence on which `\Gamma_{PF}` retains a fixed singular lower bound, giving a noncompact heavy compression and therefore, by PF-282, noncompact `T`.

Do not replace the physical angle by scalar same-mode reservoirs, raw high/high multiplicity alone, or a coordinate-mode angle that changes the fixed `P/H` split. PF-286 already uses those raw low/high estimates only to establish that the outer factors are heavy; the remaining question concerns their **common energy-range geometry**.

## Evidence boundary

PF-282 establishes the exact strength-angle factorization and the fixed-heavy-sector ideal equivalence. PF-283 establishes one sufficient symmetric heavy-angle count. PF-284 establishes the reverse comparison and the corresponding necessary weighted budget. PF-285 establishes an abstract population-only sufficient route, while PF-286 proves that this route does not apply to the canonical physical strength factors because both are noncompact with infinite heavy populations.

PF-286 does **not** show that `\Gamma_{PF}` is noncompact, that `T` fails to be compact, or that the weak-trace endpoint fails. Two noncompact strength factors can still have a compact or weak-trace sandwich when their ranges are sufficiently transverse. No physical principal-angle counting law has yet been proved, and no wave-operator, trace-formula, prime/clone separation, zeta-zero, or RH consequence follows.

## Research disposition

The clue remains `accepted`. The strength-population census requested by PF-285 is now resolved negatively by PF-286: finite weak-Schatten population exponents do not exist for the canonical low/high strength factors. The first live target is therefore the **physical heavy-sector extension angle**. Test compactness and thresholded singular-value decay of `Q_P^\alpha\Gamma_{PF}Q_H^\beta`; use PF-283 for a clean sufficient endpoint and PF-284 to distinguish failure of that sufficient estimate from a genuine endpoint obstruction.