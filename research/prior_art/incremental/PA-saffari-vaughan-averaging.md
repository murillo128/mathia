---
id: PA-saffari-vaughan-averaging
type: prior-art
canonical_name: Saffari–Vaughan averaging inequality
aliases:
  - Saffari–Vaughan multiplicative-to-additive window conversion
kind: mean-square-comparison
topics:
  - short-intervals
  - mean-square
  - multiplicative-windows
---

# Saffari–Vaughan averaging inequality

## What it is

For square-integrable \(F:\mathbb R\to\mathbb C\) and \(0<H\le X\),
\[
\int_X^{2X}|F(x+H)-F(x)|^2\,dx
\ll \sup_{H/(3X)\le\delta\le3H/X}
\int_X^{3X}|F((1+\delta)x)-F(x)|^2\,dx.
\]
Lemma 10 of Gorodetsky–Matomäki–Radziwiłł–Rodgers states and proves this comparison, attributing the proof to Saffari–Vaughan, p. 25.

## Relation to RH / Mathia research

[[research/mobius_cancellation/findings/MC-520-rh-mellin-variance-closes-conditional-farey-window-target|MC-520]], equations (10)–(12), uses the comparison to transfer its conditional multiplicative-window Möbius variance bound to fixed additive windows. MC-520 explicitly justifies local square integrability by truncation; it does not assume the Mertens function is globally square integrable.

## Known scope and limits

The comparison itself requires no RH and supplies no arithmetic cancellation. Its right side needs uniform control over the indicated multiplicative-window range. The theorem used here is the reproduced comparison, not the paper's separate squarefree-variance result.

## Related prior art

[[research/prior_art/incremental/PA-rh-reciprocal-zeta-subpower-bound|The RH reciprocal-zeta bound]] supplies MC-520's separate analytic input.

## Evidence and provenance

- Ofir Gorodetsky, Kaisa Matomäki, Maksym Radziwiłł and Brad Rodgers, *On the variance of squarefree integers in short intervals and arithmetic progressions*, [arXiv:2006.04060v2, Lemma 10, p. 14](https://arxiv.org/pdf/2006.04060v2); *Geometric and Functional Analysis* 31 (2021), 111–149, DOI `10.1007/s00039-021-00557-5`.
- B. Saffari and R. C. Vaughan, *On the fractional parts of x/n and related sequences. II*, *Annales de l'Institut Fourier* 27(2) (1977), 1–30, p. 25, DOI `10.5802/aif.649`; attribution checked in the reproduced proof and bibliography above.
- Persisted lookup trigger: `research/mobius_cancellation/findings/MC-520-rh-mellin-variance-closes-conditional-farey-window-target.md`, fixed-additive-window section.
