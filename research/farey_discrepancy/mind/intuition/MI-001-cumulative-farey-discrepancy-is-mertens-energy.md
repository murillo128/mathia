# MI-001 — Cumulative Farey discrepancy exposes a sharp square-root free-source boundary

**Evidence level:** exact GCD-duality reductions and matched free-source constructions through FD-025

## Core intuition

The unrestricted multi-horizon relaxation is now quantitatively classified enough that generic horizon overlap is no longer the main mystery. Its decisive source currency is endpoint growth, with a sharp transition at the square-root scale.

Below that scale, saturation is impossible for any sublinear source; above it, sufficiently sparse horizons admit explicit saturating controls. The remaining leverage must therefore come from Möbius-specific structure, not from a better generic growth argument.

## Strongest justified principle

FD-018--FD-020 classify pointwise and Cesaro saturation through recurrence of bounded squarefree horizon ratios. FD-021--FD-023 show that a polynomially bounded saturating source forces the horizon ratios to escape every bounded/exponential regime on average. FD-024 constructs saturating unrestricted sources with envelope `n^alpha` for every `alpha>1/2` along sufficiently fast supermultiplicative horizons. FD-025 proves the converse lower boundary: a sublinear source exhibiting saturation must be super-square-root on the saturating endpoints.

Together these results locate the free interpolation threshold at exponent one half rather than at a particular horizon geometry.

## Program consequence

Test source laws that distinguish Möbius from arbitrary real sequences at the square-root-plus frontier. A useful theorem should forbid the FD-024 construction mechanism using exact divisor, sign, parity, or multiplicative consistency and then translate the resulting deficit back into the cumulative Farey/Mertens normalization.

## Counterevidence / boundary

The half-power threshold belongs to the unrestricted relaxation. It is not itself a Mertens bound and does not show that the Möbius source saturates or fails to saturate any chosen horizon family. Sparse horizons remain a genuine escape for arbitrary sources above the threshold.

## Epistemic status

**Exact free-model boundary at square-root endpoint scale, leaving a source-specific Möbius rigidity problem rather than an overlap-classification problem.**

## Falsification criterion

Produce an unrestricted saturating source with `A(H)=O(sqrt(H))`, or invalidate the FD-024 construction above the half-power threshold. A positive continuation should derive a Möbius-specific restriction that survives in the residual super-square-root corridor.