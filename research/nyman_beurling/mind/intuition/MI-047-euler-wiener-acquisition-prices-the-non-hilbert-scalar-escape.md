# MI-047 — Euler--Wiener acquisition prices both source mass and aggregate phase complexity

**Evidence level:** exact/literature-backed synthesis from [NB-176](../../findings/NB-176-euler-weighted-fourier-fingerprints-certify-source-complexity.md) through [NB-188](../../findings/NB-188-hadamard-scale-euler-aggregation-forces-square-root-source-amplification-and-bounded-fanout.md). The Wiener/source-density inequalities are exact in the declared acquisition model; no global Nyman approximation theorem follows.

Retaining genuine Euler frequencies is not enough: the true amplitudes and their acquisition topology are load-bearing. The scalar Euler readout lives naturally in an absolute Wiener/Dirichlet geometry. At width `a`, its source budget is

`W(a)=sum Lambda(n)n^(-1-a) max{2,a log n} ~ (2+e^(-2))/a`.

NB-184 shows that, after quotienting the invisible constant mode, density-one heights can acquire this scalar family cheaply throughout the quadratic regime `T a^2 -> infinity`. NB-185--NB-186 then show that fixed and growing raw prime-phase codes survive that filter, with raw Hadamard-scale nuclear rank `N~1/a` already accessible at the cubic simultaneous-selection scale.

NB-187 exposes the amplitude mismatch. Under the normalized Euler--Wiener measure, the scaled frequency `u=a log n` has a nondegenerate limiting distribution, while the first `N~1/a` primes all satisfy `u->0` and carry only

`Theta_N(a) ~ [2/(2+e^(-2))] a log(1/a) -> 0`

of the total source budget. More generally, any `O(1/a)` individual prime channels carry vanishing Wiener mass. A positive fraction of the physical source therefore requires exponentially many microscopic Euler channels, not merely Poisson-many favorable phases.

NB-188 prices attempts to compress that enormous source population into a Hadamard-scale code. For same-frequency linear aggregates with source-relative coefficients, a dense `N x N` nuclear response forces a source-density gain at least of square-root size. If the response is assembled with bounded row acquisition gain, its effective source fanout must remain `O(1)`; broad overlapping reuse dilutes the nuclear certificate. On a source subset of normalized mass `Theta_S`, the required multiplier/gain grows at least like `sqrt(N/Theta_S)` in the relevant normalization.

Thus the non-Hilbert escape is not free in either direction. Selecting a small favorable prime block loses almost all physical source mass, while aggregating the missing mass into only `O(1/a)` observables forces strong reweighting and bounded effective fanout if one wants to preserve Hadamard-scale phase complexity. The surviving same-frequency route is therefore a **high-gain, bounded-fanout source compression**, not a diffuse average over many weak Euler channels.

The reusable lesson is that source-faithful rank requires three ledgers simultaneously: geometric phase rank, normalized source mass, and acquisition amplification/fanout. A large raw phase matrix can be mathematically irrelevant if it occupies vanishing source mass; a large source aggregate can be equally irrelevant if broad overlap collapses the phase nuclear norm.

**Boundary.** NB-188 applies to the declared linear same-frequency Wiener aggregation model and does not rule out nonlinear compression, architectures with strong cancellation outside that factorization, or a different source-faithful observable. It does not settle the quadratic finite-height endpoint or connect an surviving aggregate certificate to global Nyman approximation. The live target is an explicit arithmetic aggregation that pays the required gain while preserving a positive source fraction and destination relevance, or a theorem showing that such gain/fanout is unaffordable.