# MI-010 — Retaining signed arithmetic is not enough when the retained resolution reconstructs the target

**Evidence level:** supported through MC-085 by exact parity controls, annular identities, source-coupled sawtooth recovery, and Fourier-resolution equivalences

## Core intuition

A useful Möbius carrier must pass two distinct gates. It must retain signed arithmetic that unsigned divisor-density surrogates erase, but it must also discard enough information that controlling the carrier is genuinely easier than controlling the Mertens target. Passing the first gate does not imply the second.

The new annular results make this distinction exact. Liouville parity separates classes that look identical to broad local divisor statistics, so sign is a real missing variable. Yet several natural ways of restoring that sign — constant-weight parity contrast, the exact source sawtooth coupling, or a low-frequency truncation resolved finely enough to control its generic remainder — are already Mertens-equivalent.

## Strongest justified principle

MC-082 constructs a decisive matched control for unsigned local information. Square-free integers with opposite Liouville parity can have the same fixed-depth local divisor-density main term even though one class contains no primes and the other contains all primes. Any argument based only on those density statistics is therefore blind to the sign channel needed for Möbius cancellation.

MC-083 restores parity in the most direct annular contrast and proves that a power bound for this constant-weight same-versus-opposite parity observable is equivalent, at the relevant exponent, to a Mertens bound. The sign is present, but no difficulty has been removed.

MC-084 gives the same verdict for the exact Huxley--Watt/source sawtooth annular decomposition after its coarse terms are kept: the full coupled source residual reconstructs the Mertens problem quantitatively. MC-085 then shows that merely making the coupling proper by truncating Fourier modes does not help when the cutoff is high enough that the generic omitted tail is already below the desired target scale; at that resolution the low-frequency observable remains Mertens-equivalent.

The correct discriminator is therefore **signed information plus under-resolution**. A candidate becomes potentially useful only when it retains a source-forced cancellation mechanism while its omitted information is controlled by an estimate not already equivalent to the target.

## What remains possible

A live annular route may use a much coarser signed statistic if the discarded high-frequency complement has independent arithmetic cancellation, or may exploit an aggregate coupling whose estimate is not invertible back to `M(X)`. Another possibility is an exact recurrence where the partial residual enters with a strict contraction while the omitted term is summable across scales.

The evidence does not say that every signed partial statistic is Mertens-equivalent. It says that parity sensitivity, exact source origin, or the formal fact of being a proper truncation are not sufficient evidence of information reduction.

## Status / novelty

Liouville parity, sawtooth expansions, annular decompositions, and Fourier truncation are classical ingredients. The persisted synthesis is the information gate: **a Möbius residual is useful only if it both retains signed source structure and remains quantitatively below the resolution needed to reconstruct the target**.

## Falsification criterion

Produce a bound in one of the MC-083--MC-085 covered observables at the stated resolution that yields a strictly weaker requirement than the corresponding Mertens bound, or construct a new source-forced signed residual whose omitted information is independently controlled while the residual itself drives a strict contraction.

## Lean-formalizable core

- Liouville-parity matched-control identities.
- Constant-weight annular Mertens equivalence.
- Exact sawtooth annular recovery equivalence.
- Low-frequency truncation plus remainder-resolution implication.
