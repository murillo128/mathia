# MI-007 — Growing-depth coherent Gram spectra classicalize through a Nyquist/Schatten sampling boundary

**Evidence level:** supported by exact time-dilation/rank/trace identities, quantitative PNT transport, all-horizon Hilbert--Schmidt control, and classical prolate sampling theory

## Core intuition

Prime-power support and depth retain arithmetic data, but the ordinary coherent Gram construction loses far more of it than the first bulk arguments suggested. Through the first growing-depth range, the one-point shell becomes log-uniform, the normalized coherent operator is Hilbert--Schmidt universal at **every** observation horizon, and the remaining trace-class discrepancy develops a classical finite-rank/Nyquist phase. Neither convergence nor failure of convergence in these ordinary Schatten topologies is arithmetic evidence by itself.

## Strongest justified principle

PL-081--PL-093 establish the first layer: fixed depth is exact time dilation of the prime-support Gram; deeper fixed tails are rank-negligible; the first population transition occurs at `K ~ alpha sqrt(log X)`; natural von-Mangoldt weighting collapses normalized trace/determinant; and the first `K^2` repair becomes normalized-trace-norm equivalent to the unweighted shell envelope through that transition.

PL-094 removes the remaining one-point shell freedom. For `K -> infinity`, `K=O(sqrt(log X))`, the logarithmic shell coordinate converges to the elementary log-uniform law, and the diagonal envelope contributions to trace and log determinant are universal.

PL-095--PL-096 then control the off-diagonal coherent spectrum. Quantitative PNT first gives trace-norm transport below the inverse-PNT-error horizon. More strongly, PL-096 proves uniform `S_2` convergence of the normalized empirical covariance to the deterministic continuum time-band operator for **all** `T>0`. Ordered eigenvalues are uniformly `ell^2` close, fixed positive Fredholm determinants agree asymptotically, and along every `T_X -> infinity` the normalized operator norm tends to zero. Thus pushing the observation time beyond the PNT-error scale does not expose arithmetic in the `S_2` topology.

The `S_1` endpoint has a different but still classical obstruction. PL-097 shows that when `T_X/N_X -> infinity`, finite empirical rank forces the trace distance from the diffuse comparator to its maximal value. PL-098 identifies the exact finite-ratio rank floor through the prolate time-bandwidth dimension: a positive universal defect appears once `T_X/N_X` exceeds `2 pi/Delta`. PL-099 supplies the opposite control below that threshold: a deterministic midpoint frequency grid converges to the same continuum comparator in trace norm. Hence the basic sub-/super-Nyquist trace-class phase is sampling geometry, not prime arithmetic.

The exact critical ratio and the actual prime cloud's **excess** over the optimal rank floor may contain finer spacing information, but the existence, disappearance, or universal minimum size of the raw `S_1` defect does not.

## What remains possible

The surviving sector is genuinely finer than ordinary normalized Gram spectra: target-relative Schur complements, hard-edge/inverse statistics, condition numbers, singular or growing test functions, microscopic spacing observables, or the excess finite-window error after subtracting the sharp prolate rank floor. Any such candidate must also survive generalized-prime/Poisson controls rather than merely distinguish a discrete cloud from a continuum.

A later depth regime remains open only if it introduces a source-specific mechanism beyond the deterministic population/sampling geometry already isolated here.

## Status / novelty

PNT estimates, prolate time-band limiting, finite-rank approximation, Schatten inequalities, and sampling theory are classical ingredients. The persisted Prime-Lattice content is the exact organization of the growing prime-power Gram into log-uniform envelope, all-horizon `S_2` universality, and a classical Nyquist-controlled `S_1` boundary.

## Falsification criterion

Produce, in the audited growing-depth regime, a normalized `S_2` spectral statistic separated from the continuum comparator despite PL-096, or show that the `S_1` rank floor depends on arithmetic locations rather than only rank and prolate spectrum. A positive advance should isolate an excess or target-relative statistic after those universal components are removed.

## Lean-formalizable core

- Fixed-depth time-dilation and rank reductions.
- `K^2` normalized trace-norm envelope equivalence.
- Finite-rank trace-distance lower bound.
- Exact best rank-`N` trace approximation formula for a positive comparator.
