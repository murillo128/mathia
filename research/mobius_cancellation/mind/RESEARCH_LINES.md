# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Prove signed signature discrepancy from actual source structure or leave the lcm-factorable quadratic frame

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-073-source-mode-averaging-collapses-to-a-signature-projector`.

MC-385--MC-396 identify genuine endpoint costs in source quotient rank/codimension, fourth-moment geometry, conductor and source incidence. MC-397--MC-399 then remove source-mode multiplicity, divisor-pair multiplicity and the standard lcm source phase as independent cancellation dimensions. MC-400 shows that the moving hyperbola endpoint is exactly invertible, MC-401 shows that the full endpoint collapses to a classical signed gcd/divisor incidence energy, and MC-402 shows that generic truncation merely introduces a Mertens-weighted incidence resolution.

MC-403 now closes the ambiguity around “collective source-family cancellation.” After grouping the lcm coefficient mass by source signature, the source modes are exactly its finite Fourier transform, and Parseval gives

`sum_(I!=0) |A_I(X)|^2 = H sum_omega |B_omega(X)-B_bar(X)|^2`.

Thus family-level `L^2` saving is **exactly signed equidistribution of the lcm coefficient mass across source-signature classes**, not an additional averaging dimension. Sparse signature occupancy can even force nontrivial source-mode energy when the principal signed mass is visible. Combining the same Fourier transform with MC-402 turns the truncated problem into a Mertens-weighted signed signature-discrepancy vector.

The live lcm branch is therefore sharply specified. A useful theorem must exploit arithmetic of the actual Selberg coefficients/source signatures to prove near-uniformity of those signed class masses, or directly control the Mertens-weighted discrepancy vector without first controlling `M` itself. If no such source-specific theorem exists, the remaining escape is a genuinely pre-quadratic variable whose phase or congruence does not factor through `[d,e]`.

## Keep formal dimension, retained arithmetic coupling and transferred difficulty distinct

A variable can survive notation while carrying no new information. The current audit consumes averaging indices by Fourier duality, pair labels by lcm regrouping, lcm phase at first correlation, scale-indexed endpoints by inversion, the complete endpoint by gcd factorization, the incomplete mask by Möbius incidence inversion, and now the entire source family by finite Fourier/Plancherel equivalence with one signed discrepancy vector.

This last step is stronger than saying that signatures and source modes are two labels. It identifies the exact norm that any collective theorem must make small. Merely having many modes, few occupied signatures, or an `L^2` average cannot be credited as gain without a theorem for the signed signature masses themselves.

A future theorem should therefore identify a source-specific statistic that survives all of these reductions without importing an unavailable Mertens estimate. The decisive test is whether the claimed saving comes from actual `g`/signature/joint structure, or whether exact algebra merely relocates the same cancellation burden into the discrepancy vector.