---
id: CLUE-published-prime-existence-extends-minimax-sharpness
type: research-clue
status: resolved
origin: adversarial
target_line: arithmetic_fidelity
based_on:
  - research/arithmetic_fidelity/findings/AF-566-almost-all-short-interval-primes-sharpen-multi-probe-minimax.md
  - research/arithmetic_fidelity/findings/AF-565-sharp-two-probe-prime-edit-minimax-via-short-interval-primes.md
  - research/arithmetic_fidelity/findings/AF-564-finite-logarithmic-probe-designs-recover-multiway-prime-edit-margin.md
---

# Can published almost-all prime existence extend minimax sharpness through 24 probes?

## Observation

AF-566's transfer requires only prime **existence** outside an exceptional set of integer starts of size \(o(X)\). Its published-input consequence uses Guth--Maynard's stronger counting asymptotic with exponent \(2/15\), reaching \(k=8\). Its separate extension through \(k=25\) is conditional on Runbo Li's preprint exponent \(1/21.5\).

Chaohua Jia, [*Almost all short intervals containing prime numbers*, Acta Arithmetica 76 (1996), 21--84](https://matwbn.icm.edu.pl/ksiazki/aa/aa76/aa7613.pdf), states on p. 21 that, for sufficiently small fixed \(\epsilon>0\), all but \(O(X\log^{-B}X)\) integers \(n\in(X,2X)\) have at least \(0.005n^{1/20+\epsilon}/\log n\) primes in \((n,n+n^{1/20+\epsilon})\). The original theorem statement supplies an apparently sufficient, already published existence input. No counting asymptotic is needed for the two-endpoint selection argument.

## Research question

Does substituting Jia's theorem into AF-566 establish its same sharp minimax limit for every fixed \(9\le k\le24\) using published inputs, while leaving \(k=25\) outside this particular source substitution?

The relevant strict thresholds are
\[
\beta_k=3-3(3/2)^{-1/k},\qquad
\beta_{24}=0.05025740927\ldots>1/20,
\quad\beta_{25}=0.04826337276\ldots<1/20.
\]

## Why it may matter

This could separate the source dependency needed for budgets 9--24 from the stronger preprint dependency at budget 25. The useful distinction is between almost-all existence and almost-all asymptotic counting; importing the latter may unnecessarily restrict a construction that only selects two primes.

## Decisive test

Reconstruct AF-566 with fixed \(1/20+\epsilon<\beta<\beta_k\). Check the conversion from Jia's variable length to the common dyadic length: for \(n\le2X\), \(n^{1/20+\epsilon}\le X^\beta\) eventually. Retain integer-start exceptions, endpoint conventions, and the \(o(X)\) exceptional count. Then verify that \(n\mapsto\lfloor n+\Delta_j(n)\rfloor\) remains injective inside the same dyadic interval, the chosen prime endpoints approximate \(\Delta_j\) relatively, and all bottleneck heights, cross-pair exclusions and globally uniform response limits survive for fixed \(k\le24\). Reject the transfer if a required simultaneous-selection or uniformity condition exceeds the original theorem. Keep the \(k=25\) source boundary separate.

## Evidence boundary

Jia's theorem is an external published input; its sieve proof has not been reproduced here. The independently checked source substitution is persisted in AF-566 as linked below, without claiming a new prime theorem. The absolute identification margin still vanishes, the edited sources remain generalized-prime matched controls, and no RH-sensitive transfer or positive fixed-noise margin is supplied.

## Research disposition

Outcome: supported

Resolved by:

- [[research/arithmetic_fidelity/findings/AF-566-almost-all-short-interval-primes-sharpen-multi-probe-minimax.md]]

The source substitution is now proved in AF-566: Jia's integer exceptional
set remains \(o(X)\) after endpoint padding, and
\((2X)^{1/20+\epsilon}\le X^\beta\) eventually for the fixed chosen
\(1/20+\epsilon<\beta<\beta_k\). The injective shifted-start selection,
gap-relative error, equal bottleneck heights, cross-pair exclusion and global
response limit therefore apply unchanged for every fixed \(k\le24\).
Exact integer comparisons certify \(\beta_{24}>1/20>\beta_{25}\).
Jia's sieve theorem remains an external published input, and \(k=25\) remains
outside this particular substitution. No growing-budget sharpness, usable
finite prime-height bound, positive absolute-noise margin or RH implication
is established.
