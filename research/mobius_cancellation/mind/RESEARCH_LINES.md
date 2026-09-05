# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history. Lines should survive only while they separate genuinely different mechanisms.

## Find a source-forced coupled residual that retains signed information without reconstructing Mertens at the target resolution

**Linked intuitions:** `MI-008-moving-comparators-need-uniform-family-coherence`, `MI-009-dirichlet-factorization-gauge-does-not-distribute-cancellation`, and `MI-010-signed-retention-is-not-information-reduction`.

MC-066--MC-081 close positive quadratic feedback, standalone inverse control, complete Dirichlet recovery, and broad factorization-gauge escapes. MC-082 now adds a sharper information test: local divisor-density data can be identical on classes with opposite Liouville parity content, so signed parity is genuinely missing from those unsigned surrogates.

But MC-083--MC-085 show that merely restoring that sign or retaining a proper low-frequency source coupling is still insufficient. Constant-weight parity annuli, the exact source-coupled sawtooth annulus, and the low-frequency annular coupling at the resolution needed to control the omitted tail are all quantitatively Mertens-equivalent. A live residual must therefore preserve source-forced signed structure while discarding enough target information that its estimate is demonstrably weaker than reconstructing `M` itself.

## Derive an iterable strict contraction from a genuinely under-resolved signed annular residual

**Linked intuitions:** `MI-005-scale-doubling-is-exponent-neutral-without-new-signed-information`, `MI-009-dirichlet-factorization-gauge-does-not-distribute-cancellation`, and `MI-010-signed-retention-is-not-information-reduction`.

Repeated scale doubling can amplify a genuine subunit contraction, but algebraic degree, parity sensitivity, and proper Fourier truncation do not supply one. MC-085 identifies the exact trap: choosing enough low modes that the published generic Fourier remainder falls below the desired Mertens scale already makes the coupled estimate an approximate coordinate system for the target.

A positive continuation must exploit an arithmetic estimate on the omitted complement, the annular aggregate alone, or another source-derived partial coupling that remains below reconstruction resolution while still feeding a uniform strict contraction with summable iteration losses and global scale coverage.

## Keep comparator turnover and scale coverage in any alternative moving-family theorem

**Linked intuitions:** `MI-008-moving-comparators-need-uniform-family-coherence`.

The quadratic positive-feedback corridor is closed far beyond the earlier exceptional-character range, but alternative comparator families can still move with scale. Any such route must quantify how the chosen family persists or turns over, how transfer constants enter the exponent, and which signed coupling survives across the whole scale range. Per-scale existence remains insufficient.

## Treat asymptotically fixed Mellin drift as information-neutral unless the residual coupling changes

**Linked intuitions:** `MI-006-asymptotically-fixed-mellin-drift-is-information-neutral`, `MI-009-dirichlet-factorization-gauge-does-not-distribute-cancellation`, and `MI-010-signed-retention-is-not-information-reduction`.

Small deterministic Mellin shifts, fractional zeta gauges, or slowly varying normalizations do not create new signed information when they only reallocate the fixed Dirichlet singularity. A useful deformation must alter the source-forced coupled residual rather than reparameterize the same scalar carrier.
