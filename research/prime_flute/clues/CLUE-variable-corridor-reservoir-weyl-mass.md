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
  - research/prime_flute/findings/PF-222-reciprocal-prime-schur-commutator-is-compact-by-one-seam-decoupling.md
  - research/prime_flute/clues/CLUE-weak-trace-reassembly-with-summable-local-mass.md
---

# Does canonical tail mass prevent scalar reservoir amplification of a dressed cut?

## Observation

PF-279 proves that a variable scalar reservoir can erase PF-228's favorable isolated `w/s` cut scale. Its exact Weyl identity shows that boundary impedance alone is insufficient: the complete unprojected cut also sees the mass of the endpoint-normalized left/right extensions. PF-280 then separates that raw-cut obstruction from the physically mixed `P/H` block, and PF-281 replaces the potentially unbounded raw cross block by the canonical diagonal-energy-normalized cross form

\[
T_{PF}=A_{PF}^{-1/2}(PKH)_{\rm form}C_{PF}^{-1/2}.
\]

PF-282 now supplies the missing operator-valued reservoir interface. If `R_P,R_H` are the physical low/high restrictions of the normalized pant-extension energy map, then

\[
\boxed{
T_{PF}=Z_P^*Z_H
=f(|R_P|)\Gamma_{PF}f(|R_H|),
\qquad
f(t)=\frac{t}{\sqrt{1+t^2}},
\qquad
\Gamma_{PF}=V_P^*V_H.}
\]

The outer factors are bounded extension-strength filters; `\Gamma_{PF}` is the relative angle/correlation of the low-fed and high-fed extension ranges in the common energy space. Large reservoir mass therefore saturates the strength filters instead of amplifying the normalized mixed form without bound. On channels where both strengths exceed a fixed `\mu>0`, the singular values of `T_{PF}` and the corresponding compression of `\Gamma_{PF}` are equivalent up to fixed factors.

PF-282 also proves

\[
T_{PF}\text{ compact}
\iff
\Gamma_{PF,\mu}\text{ compact for every }\mu>0,
\]

where

\[
\Gamma_{PF,\mu}
=\mathbf1_{[\mu,\infty)}(|R_P|)\Gamma_{PF}
\mathbf1_{[\mu,\infty)}(|R_H|).
\]

Thus the scalar reservoir warning survives the physical normalization in a sharper form: a genuine obstruction must retain low/high **range overlap on reservoir-heavy channels**, not merely large extension norm.

## Research question

For the canonical simultaneous prime-flute precision, how large is the physical extension-angle operator

\[
\Gamma_{PF}=V_P^*V_H
\]

in the complete one-cusp-pant energy space? Does the reservoir-proof sufficient estimate

\[
\Gamma_{PF}\in\mathcal S_{1,\infty}
\]

hold, or can the fixed-strength compressions `\Gamma_{PF,\mu}` be controlled uniformly enough that their heavy-channel estimate combines with the weak-extension population as `\mu\downarrow0` to give

\[
T_{PF}\in\mathcal S_{1,\infty}?
\]

A negative answer should likewise be stated at this physical level: exhibit a fixed `\mu>0` and a canonical family of low/high inputs whose two extension strengths stay above `\mu` while their extension ranges retain enough common angle to violate compactness or the required endpoint singular-value count.

## Why it may matter

This is now the shortest exact interface between PF-279's reservoir warning and PF-281's surviving weak-trace theorem. A global weak-`S_1` estimate for `\Gamma_{PF}` immediately implies the same estimate for `T_{PF}` and hence closes PF-281's mixed Schur/commutator gate, regardless of how large same-sector diagonal extension energy becomes.

Conversely, a noncompact fixed-strength compression would kill this sufficient route cleanly: PF-282 shows that diagonal energy normalization cannot repair an ideal failure already present in the heavy extension angle. The remaining weak-strength channels are a different problem because their outer factors are genuinely small and may be paid for by physical-frequency or prime-index population.

The clue should therefore no longer seek an abstract operator analogue of the scalar `\beta'` as an independent missing invariant. PF-282 identifies the normalized diagonal extension Grams exactly,

\[
Z_P^*Z_P=I-A^{-1},
\qquad
Z_H^*Z_H=I-C^{-1},
\]

and isolates the genuinely new cross datum in `\Gamma_{PF}`.

## Decisive test

Construct the actual simultaneous pant-extension realization of

\[
K_{PF}=\Lambda_Q^{-1/2}\Lambda_E\Lambda_Q^{-1/2}
\]

with the physical `P/H` projectors fixed before any simplifying coordinate change. Verify the PF-281 form-domain hypotheses, form the restricted extension maps `R_P,R_H`, and estimate `\Gamma_{PF}=V_P^*V_H` without replacing the pant completion by a scalar same-mode model.

For a fixed `\mu>0`, PF-282 gives the exact heavy-channel comparison

\[
f(\mu)^2s_j(\Gamma_{PF,\mu})
\le s_j(T_{PF,\mu})
\le s_j(\Gamma_{PF,\mu}).
\]

First determine whether these compressions have uniform compact/weak-Schatten decay on the canonical tail. If they do, only then let `\mu\downarrow0` and charge the newly admitted channels to their small strength factors together with the physical-frequency or prime-index population. PF-282's compactness criterion alone is not a weak-trace theorem; the endpoint still needs quantitative counting.

Retain the physical split throughout. PF-279's scalar reservoir is unprojected and may lie entirely within one physical sector, while PF-227 shows that large raw high/high multiplicity remains real. Neither fact decides the mixed angle without the actual pant extension geometry.

## Evidence boundary

PF-279 remains the canonical scalar matched-control theorem. PF-280/PF-281 show why its unprojected amplification is not itself a mixed-frequency counterexample. PF-282 supplies the exact normalized strength-angle factorization and fixed-strength ideal equivalence.

No current result proves `\Gamma_{PF}\in\mathcal S_{1,\infty}`, uniform endpoint control of `\Gamma_{PF,\mu}` as `\mu\downarrow0`, or a canonical reservoir-heavy noncompact angle. No weak-Schatten failure, wave-operator conclusion, prime/clone separation, or RH consequence follows.

## Research disposition

The clue remains `accepted`. The missing interface is no longer algebraic: PF-282 identifies it exactly. The live question is now geometric and spectral—estimate the physical low/high extension angle, or construct a reservoir-heavy angle obstruction, in the complete pant geometry; then combine that result with the weak-strength population only if the weak-trace endpoint still requires it.