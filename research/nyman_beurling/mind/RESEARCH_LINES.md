# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Price height adaptation by ordered motion, repertoire entropy and linear source complexity

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-039-low-linear-source-complexity-suppresses-arbitrary-adaptation`.

NB-165--NB-167 isolate the capped Poisson transport metric actually seen by a compact signed sampler near `Re s=1`. NB-168 separates stationary source-specific resonance from a persistent mechanism: one fixed template cannot produce logarithmic Euler rescue on positive density under the subcritical transport budget. NB-169 then prices finitely many height-dependent templates by a refresh term.

NB-170--NB-171 identify the **ordered** adaptation currency. Total capped-transport variation and, more generally, finite `p`-variation bound the number of consecutive source-distinguishable templates available at the logarithmic rescue resolution. Even a path with infinite ordinary variation is constrained whenever some finite `p`-variation remains below its power-law tariff.

NB-172 shows that arbitrary temporal roughness is still not enough. Let `N_T(epsilon)` be the internal covering number of the *range* of templates in capped Poisson transport. Without any continuity, measurability, variation or interval-partition hypothesis, the rescue density is bounded by

`N_T(epsilon_T) X_T^2/log^2 T * (1 + 1/(T a_T^2))`,

at the source resolution `epsilon_T~log T/H_T`. Thus a family can switch infinitely often and have infinite `p`-variation for every finite `p`, yet remain harmless if it only revisits a small repertoire of geometrically distinct source shapes.

NB-173 adds a third, independent compression. If every adaptive template lies in the span of `m_T` stationary capped-transport-normalized source directions with coefficient `ell^2` energy at most `Y_T^2`, arbitrary height-dependent selection satisfies

`rescue density << m_T Y_T^2/log^2 T * (1 + 1/(T a_T^2))`.

Optimizing over all normalized stationary dictionaries gives the intrinsic linear source complexity `mathfrak L_T`, with the same bound and the exact inequality `X_T^2 <= mathfrak L_T`. No continuity, measurability, variation, interval partition or range-cover assumption is needed. A wildly oscillating continuum of templates may therefore have enormous metric entropy and infinite ordered variation while remaining harmless if it is generated inside a low-rank source span with sublogarithmic normalized coefficient energy.

The three currencies are genuinely complementary. Ordered variation prices how fast the source-resolvable shape moves; range entropy prices how many distinguishable shapes exist regardless of traversal; linear source complexity prices how many stationary source directions and how much normalized coefficient energy are needed to generate the entire adaptive family. Large complexity in one currency does not imply large complexity in the others.

A viable positive-density adaptive rescue must therefore evade **all applicable compressions**: it must have enough source-resolvable ordered motion, enough range entropy, and enough linear source complexity/energy, or exploit the known ultra-thin limitation of the stationary mean-square estimate. A concise nonlinear arithmetic rule remains a possible escape only if its realized template family genuinely generates large source complexity rather than merely many syntactic choices.

The next structural question is to relate these currencies without conflating them. NB-173 leaves open whether `mathfrak L_T` has a useful dual characterization, whether source-natural nonlinear dictionaries force lower bounds on it, and whether a family can simultaneously have low metric entropy but high linear complexity (or conversely) at the precise capped-Poisson resolution consumed by the explicit formula.

## Keep target conditioning and arithmetic-source persistence separate

Earlier findings already show that target amplification, radial depth, finite multibase visibility and recurrence observability do not by themselves control conditioning. NB-168--NB-173 are source-side persistence theorems: they price how much the compact arithmetic sampler may vary before logarithmic Euler rescue can occur on positive density. They do not turn a density obstruction into pointwise exclusion at a deliberately selected sparse sequence, nor do they remove the need to connect any surviving source response back to the Nyman target geometry.