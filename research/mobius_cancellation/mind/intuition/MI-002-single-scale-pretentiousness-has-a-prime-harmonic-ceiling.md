# MI-002 — Comparator closeness is useful only with a power-sensitive transfer budget cheaper than the target

**Evidence level:** supported through MC-052 together with the persisted classical pretentious and Landau mechanisms

## Core intuition

Ordinary prime-harmonic closeness can miss a polynomial endpoint defect, while stronger power-aware carriers can detect it. But detection is not cancellation, and the newest comparator results show that enlarging the comparator class does not automatically make transfer cheaper.

For real square-free-supported comparators, global Möbius closeness plus an independently proved power saving already bootstraps to essentially the same power saving for Möbius and the matching zeta zero-free half-plane. Complex phases are the first genuinely different boundary: ordinary closeness then supplies a simple boundary zero and only a quadratic phase budget, not the absolute convolution control needed for exponent-preserving transfer.

## Strongest justified principle

MC-045--MC-048 separate visibility from transport. A terminal prime slab is invisible to the ordinary `1/p` metric but visible to the power-aware carrier at the target scale; the classical prime-only Cauchy transfer nevertheless loses too much exponent to exploit that detection at RH scale.

MC-049 closes the globally Liouville-close completely multiplicative real comparator route: a fixed comparator with the desired power cancellation already forces the corresponding zeta zero-free region.

MC-050 and MC-051 show that complete multiplicativity and exact `+-1` signs are not load-bearing. The same bootstrap survives for square-free-supported real comparators with `f(p) in [-1,1]`. Positivity of the quotient coefficients upgrades boundary continuation to power-aware absolute convolution control, and the comparator estimate transfers back to Möbius.

MC-052 identifies the first surviving category change. For complex square-free-supported `f`, finite ordinary Möbius distance still forces a simple zero of `F` at `s=1`, but only yields

`sum_p |1+f(p)|^2/p < infinity`

and corresponding quadratic convolution control. Exponent-preserving Cauchy transfer to a target `alpha` needs a much stronger weighted quadratic budget near `beta<2 alpha-1`; the automatic boundary information is therefore far too weak at the RH scale. Complex phase structure is a real escape only if arithmetic supplies that missing power-sensitive budget or a cheaper signed transfer.

## What remains possible

A live route may use complex phase cancellation, bilinear/signed convolution, scale-coupled comparators, or another source-specific structure not reducible to positive absolute inversion. The comparator's own cancellation theorem and the transfer cost must both be audited against the intended conclusion.

## Status / novelty

Pretentious distance, Landau positivity, Dirichlet convolution, and Cauchy transfer are classical. The synthesis is the sharpened hierarchy: **real square-free comparator enlargement does not help; complex phases change the available norm from absolute to quadratic, exposing a precise missing exponent budget rather than supplying it**.

## Falsification criterion

Produce a source-natural complex comparator whose independently proved cancellation plus ordinary Möbius closeness yields the required power-sensitive inverse-kernel control without already implying the target zero-free region, or a signed transfer that avoids the absolute/Cauchy cost on the persisted terminal controls.

## Lean-formalizable core

- Real square-free quotient positivity and inverse-convolution bootstrap.
- Complex boundary simple-zero implication.
- Ordinary pretentious distance to quadratic prime-defect control.
- Weighted `L2` transfer exponent budget.
