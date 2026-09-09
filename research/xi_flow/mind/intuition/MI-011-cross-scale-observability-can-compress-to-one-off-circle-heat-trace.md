# MI-011 — Exact state identification is easy; transition transport still requires antipodal or sufficiently deep complex reach

**Evidence level:** exact state-identification and transition-conditioning boundaries for raw traces, finite/infinite normalized jets, distributional sensors, and complex collars through XF-151

## Core intuition

The periodic polynomial state is algebraically easy to identify compared with the de Bruijn--Newman transition parameter. Local real traces, short scans, and off-circle samples can determine the state exactly while the target functional `Lambda_per` remains catastrophically ill-conditioned.

The current maximal-contact matched family makes this gap geometric and now survives much richer observation classes. Full derivative information is not a hidden substitute for spatial reach: even the complete root-scale analytic jet remains transition-blind away from the antipodal layer, and shallow complex continuation only trades against that deficit at an explicit exponential-type cost.

## Strongest justified principle

XF-143--XF-148 separate exact state recovery from transition conditioning and show that polynomially normalized real sensors remain exponentially blind unless their support enters an `O(L sqrt(log N/N))` antipodal layer for the maximal-contact pair.

XF-149 extends the obstruction to finite-order distributional sensing. With root-spacing normalization, derivative order `j` can remove at most `j` powers of the packet's spatial suppression, giving a quantitative derivative-depth/antipodal-reach tradeoff.

XF-150 closes the full-degree loophole using the exact reflected-binomial frequency profile. High normalized derivative orders are themselves exponentially small, so combining the spatial and frequency envelopes shows that the **entire real jet through degree `N-2`** remains exponentially blind on every fixed proper aperture and superpolynomially blind until the same shrinking antipodal layer is reached.

XF-151 removes the finite-degree restriction. The binomial moment controls every normalized derivative order, so the infinite analytic jet is still blind on the real axis. Entire continuation to a complex collar of depth `h_N` costs `exp(2 pi N h_N/L)` against the real-axis blindness exponent. Near the antipode this produces a parabolic tradeoff: complex reach of order `d_N^2/L` is the scale needed to compensate a real support deficit `d_N` in the present certificate.

## Program consequence

Do not optimize generic tomography, add derivative channels away from the visibility layer, or invoke shallow analytic continuation as if it supplied transition information for free. The next target-side theorem must derive source-faithful access to the required antipodal/deep-complex region with controlled sensor normalization, or the source side must exclude the maximal-contact matched packet or an equivalent transition-sharp family from Xi.

A proposed decoder should state separately its state-identification property and its inverse modulus for `Lambda_per`; the former is no substitute for the latter.

## Counterevidence / boundary

The matched family does not prove that near-antipodal or sufficiently deep complex access is sufficient for stable transition recovery. XF-151's collar estimate closes only the quantified shallow-reach regime. Data-adaptive nonlinear observables or source restrictions can evade the present sensor class if they are derived independently rather than selected from the target.

## Epistemic status

**Exact algebraic identifiability together with robust all-future transition-conditioning barriers extending through infinite normalized jets and shallow complex collars; a stable source-to-transition observable remains open.**

## Falsification criterion

Construct a polynomially conditioned `Lambda_per` decoder for the XF-151 matched pair using polynomially normalized observations that stay outside the quantified antipodal/complex reach boundary, or invalidate the exact derivative/binomial envelopes. A positive continuation should instead cross the derived reach boundary or prove a source restriction excluding the matched packet.