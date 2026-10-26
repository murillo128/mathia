---
id: PA-paley-wiener-l2-exponential-type
type: prior-art
canonical_name: L2 Paley–Wiener exponential-type theorem
aliases:
  - Paley–Wiener compact-support theorem
  - Paley–Wiener II
kind: Fourier support theorem
topics:
  - Fourier analysis
  - entire functions
  - compact support
---

# L2 Paley–Wiener exponential-type theorem

## What it is

For the convention \(F(z)=\int f(t)e^{itz}\,dt\), an entire function satisfying \(|F(z)|\le C e^{A|z|}\) and \(F|_{\mathbb R}\in L^2\) is the transform of a unique \(L^2\) function supported in \([-A,A]\). Conversely, such compact support gives these properties.

## Relation to RH / Mathia research

[[research/prime_lattice/findings/PL-487-sparse-mellin-division-preserves-gevrey-decay-and-support|PL-487]], §3, applies the theorem after centering and rotating its Laplace variable. Arbitrarily small support enlargements intersect to the original interval.

## Known scope and limits

The theorem supplies support containment, not Gevrey regularity, division estimates, or a fixed-box interpolant. PL-487 proves those conditional estimates separately; equality of disconnected supports is not asserted.

## Related prior art

[[research/prior_art/incremental/PA-paley-wiener-ingham-logarithmic-integral|The logarithmic-integral criterion]] instead constrains Fourier decay; it is a different theorem.

## Evidence and provenance

- Armin Rainer, *Real Analysis*, §8.3, Theorem 8.18, pp. 88–89, [author's notes](https://www.tuwien.at/mg/arainer/wp-content/uploads/2025/03/real-analysis.pdf). Its \(2\pi\) convention is rescaled above.
- Trigger: `research/prime_lattice/findings/PL-487-sparse-mellin-division-preserves-gevrey-decay-and-support.md`, §3 and its source 158.
