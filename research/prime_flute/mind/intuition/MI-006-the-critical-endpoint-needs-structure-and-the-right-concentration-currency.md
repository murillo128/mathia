# MI-006 — The critical endpoint needs quantitative cut-flux control in the correct `L log L` currency

**Evidence level:** supported by exact geometry, critical weak-ideal architecture, reciprocal-prime Schur reduction, and compactness/countermodel results through PF-223

## Core intuition

The Prime-Flute endpoint is no longer blocked by coefficient currency, fixed-scale localization, regular-body transport, decomposition-cuff smoothing, or even qualitative compactness of the remaining smooth coefficient transfer. The exact Lambert deformation is prime-summable in the critical `L log L` scale, the regular body reassembles without weak-endpoint loss, and PF-221 reduces the residual smooth word to `P[D,Omega]H`.

PF-222--PF-223 identify the remaining category sharply. The reciprocal-prime Schur commutator is genuinely compact in the physical block-Jacobi realization, but compactness plus arbitrarily strong **fixed-edge** smoothing does not imply weak trace class. The endpoint is a quantitative singular-value transport problem: local ideal strength must be controlled as the seam position and effective frequency multiplicity move to infinity.

## Strongest justified principle

PF-196--PF-204 establish the critical `L log L` currency, lossless localization/reassembly, and the native two-space factorization. PF-210--PF-221 then eliminate coefficient-adjacent low blocks and isolate the weighted Schur commutator. Same-module mixing cancels, so the reciprocal-prime coefficient enters only through differences between modules.

PF-222 writes the coefficient weight exactly as `Omega=sum_j delta_j E_j` and proves that each fixed cut flux `[D,E_j]` lies in every Schatten class by one-seam decoupling. The series converges in operator norm, giving `[D,Omega]` and `P[D,Omega]H` compact without a global bounded precision commutator or a uniform hopping estimate.

PF-223 proves the essential negative companion. There are positive block-Jacobi controls with the exact reciprocal-prime weight, finite-rank adjacent blocks and prefix fluxes, rank-one low sectors, and compact total commutator for which the low/high transport is not in `S_{1,infinity}`. The failure comes from growing effective multiplicity at vanishing operator scales. Qualitative locality, smoothing, finite rank, and compactness cannot be multiplied together informally to obtain the endpoint.

## Counterevidence / boundary

PF-223 is an abstract control, not a counterexample to the canonical thin-pant geometry. It deliberately omits PF-212's physical high-frequency singular-value decay and permits local constants/effective ranks to degenerate arbitrarily. A source-specific quantitative seam/frequency theorem may still close the smooth route.

The result also leaves PF-204's unsmoothed mixed transport and PF-183's true short-collar conservative splice independent. Compactness of the smooth commutator proves neither scattering completeness, determinant control, prime/clone separation, nor any RH consequence.

## Epistemic status

**Exact qualitative compactness with an exact abstract obstruction to upgrading it without position-dependent singular-value control; the canonical weak-`S_1` estimate remains open.**

## Falsification criterion

Derive weak trace class from only the qualitative hypotheses retained by PF-223, contradicting its explicit singular-value counting, or invalidate PF-222's cut decomposition/compactness in the canonical flute. A positive continuation should prove a canonical `j`- and frequency-dependent estimate whose weighted cut-flux accumulation has `O(1/t)` singular-value counting.
