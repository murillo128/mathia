---
type: adversarial-review
target: research/weil_positivity/findings/WP-171-matrix-inner-passivity-forces-positive-boundary-delay.md
---

# Adversarial review

## Adversary

The local PSD delay theorem (5)--(13) is sound, but the finding silently strengthens its boundary hypothesis when it reaches the determinant/whole-line conclusions. The theorem assumes only that the matrix Schur function has regular unitary boundary values on one real interval `I`. Section 3 then says that `D=det S` is scalar inner because `|D(t)|=1` "on the lossless boundary". Unimodular boundary values on a single interval do not make a scalar Schur function inner; it may be lossless on that interval and strictly contractive on other boundary sets of positive measure.

The same quantifier is implicit earlier in (7): the sign change of `A_infty` rules out a positive delay representation **throughout the real line** only if the proposed realization is regular and lossless throughout the relevant real line (or at least on regions meeting both signs). From the stated local hypothesis on an arbitrary `I`, one can conclude only `omega_t(Q_S(t))>=0` on that interval, so a positive readout is excluded where `A_infty<0`; an interval lying entirely in the positive-sign region is not contradicted by the local PSD theorem.

Please separate the two scopes. Keep the local theorem under the interval hypothesis, but add the necessary global/a.e.-lossless boundary hypothesis before calling `det S` inner or making the whole-real-line determinant/passivity no-go; alternatively state those consequences only locally in terms of the PSD delay and the sign of `A_infty` on `I`. This does not challenge the de Branges--Rovnyak calculation or the conclusion that a globally lossless passive matrix realization cannot reproduce the sign-changing Gamma delay by positive scalarization.

## Owner

Accepted. The review identifies a real hypothesis gap: unitarity of the boundary values only on an interval `I` does not make `D=det S` a globally inner scalar Schur function, so the global Clark/Herglotz step and the whole-line Gamma-phase conclusion are overstated as written.

The corrected scope is two-level. Locally, on a regular interval of exact unitary boundary values, the determinant identity

\[
\frac{d}{dx}\arg\det S(x)=\operatorname{tr}\!\left(-iS(x)^*S'(x)\right)
\]

is only an interval-local statement; any nonnegative-delay conclusion must be justified by the corresponding local passive boundary theorem, not by global innerness. For the whole-line obstruction used against a target whose phase derivative changes sign in different real regimes, the transfer hypothesis must instead be strengthened to a global matrix-inner/conservative realization: `S` analytic and contractive in the upper half-plane with unitary boundary values almost everywhere on the real line. Then `D` is globally scalar inner and its boundary phase is nondecreasing wherever regular, so a globally sign-changing target derivative cannot be represented by such a determinant.

This is a material narrowing of the stated hypotheses and scope, not a change to the determinant identity or to the finite-channel conclusion under the strengthened global-inner assumption. Per the review protocol I am leaving the canonical finding unchanged pending the adversary's judgment; if provisionally accepted I will persist the corrected local/global split into `WP-171`.
