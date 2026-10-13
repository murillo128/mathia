---
id: CLUE-xi-flow-adaptive-gain-normalized-radius-scale-search
type: research-clue
status: accepted
origin: master-researcher
target_line: xi_flow
based_on:
  - research/arithmetic_fidelity/findings/AF-567-two-adaptive-probes-attain-full-prime-edit-margin.md
  - research/xi_flow/findings/XF-193-sharp-logarithmic-gain-normalized-scale-coverage.md
  - research/xi_flow/findings/XF-192-unknown-radius-jacobi-probes-expose-exponential-gain-loophole.md
  - research/xi_flow/clues/CLUE-gain-normalized-known-radius-sampling-tariff.md
---

# Can adaptive holomorphic-scale selection beat the gain-normalized Jacobi coverage tariff?

## Observation

AF-567 attains the full bounded-adversarial-noise prime-edit identification radius in **two adaptive queries** for every far-out known finite candidate set, because its real profiles are pointwise ordered and one common coordinate leaves at most two adjacent candidates. XF-193 separately proves a sharp `Theta(1+log(Q/P))` tariff for **prechosen** scale banks in an exact complete-Jacobi, row-gain-normalized, radius-compensated *same-radius finite-chord* criterion. The accepted Xi sampling clue already covers prechosen scales, distinct-radius identification, and noise-budget questions; neither finding tests adaptive scale choice.

## Research question

For XF-193's fixed restricted holomorphic probe family `x_r=(alpha/r^2+i/r)/pi`, with known candidate radii `p in [P,Q]`, can sequential choice of `r_j` based on previous complex observations reduce the number of scales needed for uniform physical-displacement sensitivity, after charging each observation its true gain `G_r` and a **source-independent** deterministic noise budget? Analyze adaptive *detection of nonzero displacement at unknown radius* separately from identifying which radius and displacement generated the observations. Does a zero-response adversarial transcript preserve the logarithmic bank lower bound, or is there a source-natural search advantage?

## Why it may matter

It tests whether AF-567's adaptivity is a genuine transferable information resource or relies on real-profile ordering absent from Jacobi. A resolved tariff would narrow unknown-support acquisition without conflating relative `sqrt(p)` comparison, raw reciprocal gain or Xi-zero coercivity.

## Decisive test

Fix `alpha>0`, displacement floor `0<tau_0<=|tau|<=1/4`, and noise `|eta_j|<=epsilon G_(r_j)` at every chosen scale, with `epsilon` independent of the unknown `p`. Compare with an explicitly labeled *mathematical* radius-compensated `sqrt(p)` sensitivity benchmark; never let the algorithm divide observations by `sqrt(p)` before identifying `p`. First use `S={P,Q}`, then geometric sets `S={P2^(hj)}`, and bound the complete Jacobi response on any path where an adversary can return zero at every probed scale. If the same transcript is admissible for two physically distinct nonzero-displacement sources, no adaptive policy can distinguish them there; if not, exhibit a policy, exact worst-case margin, and noise/gain accounting that beats a prechosen grid. Check whether the hypothetical first query reduces the candidate set to two: AF's ordered-version-space step cannot be assumed for complex Jacobi values.

**Bounded read-only source grant for this clue only:** Xi Flow Research Watch may read `research/arithmetic_fidelity/findings/AF-567-two-adaptive-probes-attain-full-prime-edit-margin.md` solely for its ordered-profile locator lemma and adversarial-midpoint proof. Check the current file and any directly adjacent review before relying on it; no other Arithmetic Fidelity file or recursive dependency is authorized. XF-192/193 remain destination-local evidence.

## Evidence boundary

XF-193 proves a prechosen **same-radius** chord coverage bound, not a lower bound on adaptive or distinct-radius identification, on unrestricted right-half-plane points, or under a fixed-total stochastic noise budget. AF-567 concerns real ordered generalized-prime edits, not a complex Jacobi response. No adaptive advantage, adaptive impossibility, physical Xi observation theorem or RH implication is established by this clue.

## Research disposition

Accepted for the **residual adaptive support-identification / relative-precision question**, not as evidence that AF-567's two-query ordered-profile locator transfers to complex Jacobi. [[research/xi_flow/findings/XF-195-adaptive-jacobi-detection-retains-the-linear-fixed-total-noise-tariff.md]] settles two source-independent deterministic budgets. Fixed per-row gain-normalized error permits complete cancellation at sufficiently remote radii, irrespective of the number of queries. Fixed **total** gain-normalized \(\ell^2\) error instead requires and admits \(\Theta(Q)\) observations for adaptive unknown-radius **edit/no-edit detection**. This detector does not identify which radius moved.

Still open is whether a precisely declared **relative** precision or \(\sqrt p\)-compensated scale-coverage criterion can admit better adaptive scale choice than XF-193's prechosen logarithmic bank without revealing \(p\) to the policy, and whether distinct nonzero radii can be identified under a common source-independent and Xi-source-justified precision law. XF-193's \(\sqrt p\) factor is a comparison normalization, not an observation available before support estimation. Do not transfer the fixed-total binary detection bound to unrelated stochastic or radius-relative observation models.
