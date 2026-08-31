# MI-004 — The `W`-local conditioning spectrum is `L^2`-compressible but `l^1`-expensive

**Evidence level:** supported by exact Fourier-conductor identities and quantitative no-go estimates

## Core intuition

The deterministic `W`-local pair main is neither an arbitrary full-period obstruction nor a sparse collection of cheap low-conductor twists. Its Fourier energy has a sharp norm-dependent structure: most squared mass lies on subpolynomial conductors, but capturing that mass losslessly requires more than any fixed polylogarithmic cutoff, and the retained spectrum has a super-polylogarithmic Wiener mass. The viable interface is therefore collective `L^2`/square-function control, not termwise estimates followed by absolute summation.

## Strongest justified principle

WI-058 computes the exact squared-Fourier conductor law of the normalized `W`-local pair main. Active local primes enter the reduced conductor independently, with inclusion probability `1/p` or `2/p` according to the shift. This gives subpolynomial effective conductor in `L^2` even though the physical period `W` is much larger. The full period is therefore a misleading measure of analytic complexity.

WI-059 identifies the first boundary of that reduction. Projecting to conductors bounded by `(log X)^B` for any fixed `B` leaves a positive fraction of the normalized squared energy; an exponent growing slowly with `X` is needed for the discarded absolute `L^2` energy to become `o(1)`. Thus “polylogarithmic conductor” is not a stable fixed-scale simplification.

WI-060 then shows why a mode-by-mode repair still fails after the correct truncation. At a sufficient subpolynomial cutoff the retained Fourier `l^1`/Wiener mass is already larger than every fixed power of `log X`, whereas its `l^2` mass remains only polylogarithmic. Consequently any black-box additive-twist estimate with an arbitrary fixed logarithmic saving, assembled by triangle inequality over the retained modes, is structurally too expensive.

The remaining interface is collective: a weighted square-function or large-sieve estimate, cross-mode orthogonality/cancellation, or a direct theorem for the conditioned covariance in the exact source normalization. This is a norm/topology statement about the conditioning problem, not merely a request for a stronger bound on one Fourier coefficient.

## What remains possible

The `L^2` concentration does not itself provide the required source-faithful conditioned shifted-prime theorem, and no currently accepted finding closes the cross-conductor, translated-interval, local-main, parity/collision, and locked two-leg assembly. A collective estimate may still fail for arithmetic reasons not visible in the deterministic local-main spectrum.

Conversely, the large Wiener norm only kills absolute mode summation with fixed logarithmic savings. It does not rule out orthogonality, cancellation among modes, a conductor-weighted square function, or a direct covariance theorem that never decomposes into separately estimated characters.

## Status / novelty

The Fourier factorization, conductor-tail estimates, and Wiener/Parseval norm calculations are persisted exact findings with classical harmonic-analysis ingredients. Their synthesis as the required collective interface for the Yang/Weil welding problem is supported. No unreviewed conditioned-pair theorem is used as evidence here.

## Falsification criterion

Show that a fixed polylogarithmic conductor projection captures `1-o(1)` of the normalized `L^2` energy, contradicting WI-059, or bound the sufficient retained spectrum by a fixed polylogarithmic Wiener mass, contradicting WI-060. A positive advance would prove a source-compatible collective estimate whose cost follows the small `l^2` mass rather than the large `l^1` mass.

## Lean-formalizable core

- Product law for squared Fourier conductor mass.
- Parseval relation between conductor projection and discarded `L^2` energy.
- Separation between retained `l^1` and `l^2` norms at the sufficient cutoff.