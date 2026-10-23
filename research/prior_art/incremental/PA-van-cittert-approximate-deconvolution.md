---
id: PA-van-cittert-approximate-deconvolution
type: prior-art
canonical_name: Van Cittert approximate deconvolution
aliases:
  - Finite van Cittert deconvolution polynomial
kind: approximate-inversion
topics:
  - smoothing
  - operator-polynomials
  - deconvolution
---

# Van Cittert approximate deconvolution

## What it is

For a linear filter \(G\), the finite polynomial
\[
D_N=\sum_{j=0}^{N}(I-G)^j
\quad\text{satisfies}\quad
GD_N=D_NG=I-(I-G)^{N+1}.
\]
Layton's equation (1.1) identifies this classical approximate inverse. It is a finite geometric-series identity; convergence of an infinite inverse series is unnecessary.

## Relation to RH / Mathia research

[[research/mobius_cancellation/findings/MC-521-smooth-deconvolution-removes-the-variance-zero-free-boundary-loss|MC-521]], equations (5)–(11), applies this polynomial to a known smooth test weight for a one-sided box or dilation average. Its separate filter estimates control the residual and support, allowing a conditional variance-to-zero-free transfer without reconstructing sharp Mertens endpoints. The polynomial supplies no arithmetic variance estimate.

## Known scope and limits

Approximation rates require filter-specific regularity estimates. Layton studies differential filters and explains why fixed-order approximation differs from stable exact inversion. MC-521 proves its own box/dilation estimates; the differential-filter rates are not imported. Neither source establishes a bounded inverse on arbitrary data by the finite identity alone.

## Related prior art

Layton relates the polynomial to finite Picard/first-order Richardson iteration. This identifies the inversion mechanism, not an additional RH criterion.

## Evidence and provenance

- William Layton, *The Interior Error of Van Cittert Deconvolution of Differential Filters Is Optimal*, *Applied Mathematics E-Notes* 12 (2012), 88–93; [journal article](https://www.math.nthu.edu.tw/~amen/2012/120201-1.pdf).
- [Expanded author manuscript](https://www.mathematics.pitt.edu/sites/default/files/research-pdfs/vancitterterrorexpanded.pdf), equation (1.1), Remark 1.2 and the finite-error identity in equation (2.1). The bounded-filter specialization remains the responsibility of the application.
- Persisted lookup trigger: `research/mobius_cancellation/findings/MC-521-smooth-deconvolution-removes-the-variance-zero-free-boundary-loss.md`, smooth-sum recovery and prior-art sections, at source revision `f29d898a0bc9fcda6e175d5bad80bc3dc1bd353c`.
