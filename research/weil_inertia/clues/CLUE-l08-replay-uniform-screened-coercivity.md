---
id: CLUE-weil-inertia-l08-replay-uniform-screened-coercivity
type: research-clue
status: proposed
origin: research-watch
target_line: weil_inertia
based_on:
  - research/weil_inertia/findings/WI-300-l08-compact-window-certificate-would-kill-complete-one-signed-screening.md
  - research/weil_inertia/findings/WI-298-rearrangement-collapses-complete-one-signed-screening-to-first-prime-aperture.md
  - research/weil_inertia/findings/WI-238-suzuki-localized-weil-operator-turns-rh-failure-into-a-finite-prime-zero-mode.md
---

# Does the L=0.8 replay give uniform coercivity for every one-signed completely screened function?

## Observation

Independent compute execution of [issue #152](https://github.com/murillo128/mathia/issues/152) reconstructed the geometric-side certificate in [Zhu, arXiv:2608.24827v2](https://arxiv.org/abs/2608.24827v2), obtaining

\[
Q_W(f)\ge c\|f\|_2^2,\qquad c=8.9\times10^{-18},
\qquad \operatorname{supp}f\subseteq[-0.8,0.8],
\]

for arbitrary complex functions in the localized form domain. The normalization audit against Suzuki gives scalar conversion exactly one. The certificate uses no zeta zeros or RH assumption.

The primary even matrix has exactly 200 Legendre modes at frequency cutoff 200; the odd replay has 200 odd modes at cutoff 150. All entries were reconstructed with outward Arb arithmetic, including Gauss nodes and weights, using 100 and 140 decimal digits respectively. A separate 150-digit checker constructs exact dyadic Gram factors and encloses their residuals. At shifts `9e-18` and `8.3e-15`, residual operator bounds are below `7.367e-32` and `1.328e-88`. Each sector also deducts `2e-38` for quadrature and `1e-100` for head-tail coupling; the discarded diagonal block stays above `0.22`. The resulting simple certified floors are `8.9e-18` even and `8.2065e-15` odd. Parity and real/imaginary decomposition give the full complex statement.

The exact source identities, analytic error estimates, source and matrix hashes, software versions, and complete reconstruction/checking code are preserved in the [issue evidence comment](https://github.com/murillo128/mathia/issues/152#issuecomment-5678076696). The author source archive supplied no executable certificate artifacts; the replay did not rely on a stored author matrix. This is a computer-assisted certificate, not a Lean formalization.

WI-298's packing and rearrangement mechanism may carry more of this new input than its first-crossing headline records: the support bound, norm preservation, and inequalities for the gamma and pole parts do not visibly require the original function to be a null mode or a first-crossing eigenfunction.

## Research question

Let `f` be any real, nonzero, compactly supported function in the Weil form domain, of one global sign, and suppose every active prime-power translation is screened:

\[
C_f(\log n):=\int_{\mathbb R}f(x+\log n)f(x)\,dx=0
\quad\text{for every prime power }n.
\]

Lags outside the support diameter vanish automatically. Does WI-298 plus the independently replayed window certificate imply the aperture-independent bound

\[
\boxed{Q_W(f)\ge c\|f\|_2^2\quad(c=8.9\times10^{-18})}
\]

throughout this restricted, nonlinear class, without a null-mode, first-crossing, or eigenfunction assumption?

## Why it may matter

This would remove the entire one-signed complete-screening alternative for any nonpositive compactly supported Weil test, and in particular supply the missing verified input of WI-300. Every real one-signed nonpositive test would then require a strictly positive prime-power autocorrelation. The proposed bound concerns a constrained class at arbitrary support, not unrestricted positivity beyond the computed window.

## Decisive test

Replace `f` by `-f` if necessary and audit WI-298's proof with `f>=0` but without its null-mode hypothesis. Screening at all powers of 2 makes the positivity set a measurable selector modulo `log 2`; hence its measure is at most `log 2`. Symmetric decreasing rearrangement `f*` therefore satisfies

\[
\operatorname{supp}f^*\subseteq[-(\log2)/2,(\log2)/2],
\qquad \|f^*\|_2=\|f\|_2.
\]

Verify the form-domain extension and both rearrangement inequalities `G(f*)<=G(f)` and `P(f*)<=P(f)`. The exact endpoint prime shifts on `f*` have zero overlap a.e. The proposed chain is then

\[
Q_W(f)=q_{\rm arch}(f)
\ge q_{\rm arch}(f^*)=Q_W(f^*)
\ge c\|f^*\|_2^2=c\|f\|_2^2.
\]

Kill the sharpening if packing or either energy comparison uses a hidden null/eigenfunction/first-crossing condition, if complete screening fails to remove a prime term, or if rearrangement loses the form domain. Confirm the certificate-to-Suzuki dictionary and inspect existing prior art before promoting this consequence. WI-238 continuity and monotonicity then recover WI-300's first-crossing exclusion as a corollary, but are unnecessary for the stronger displayed inequality.

## Evidence boundary

The independently checked numerical result is the fixed `L=0.8` full-complex certificate. The extension to arbitrary support is a source-derived proposed consequence for the explicitly screened one-signed class, awaiting Research Watch validation; it is not another numerical aperture computation or an unrestricted positivity theorem. No claim about sign-changing tests, unscreened one-signed tests, spectral simplicity, parity ordering of the ground state, RH, or mathematical novelty follows. This proposed clue neither changes canonical findings nor accepts its own research consequence.
