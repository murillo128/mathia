# MI-004 — The all-composite shift clone is compact-resolvent equivalent, so discrimination begins above essential spectrum

**Evidence level:** supported; compact relative resolvent is exact for the constructed identification, stronger relative classes remain open

## Core intuition

Large Fenchel--Nielsen coordinates and collapsing collars are poor proxies for operator distance in the prime flute. The exact all-composite shift control `q_n=p_n+1` can now be identified with the exact prime flute by a global marked bilipschitz map whose metric distortion tends to zero at infinity. This is strong enough to force **compact first relative resolvent** and equality of essential Laplace spectrum. Essential-spectrum data therefore cannot carry prime specificity for this construction.

## Strongest justified principle

PF-121--PF-124 remove the local geometric obstructions: long Lambert pieces with small cuff shifts admit asymptotically bilipschitz comparisons, cusp synchronization costs depend on summable adjacent differences, and the zero-twist cuff trace is coherent with the comparison.

PF-125 then completes the global compactness gate. Under the explicit marked identification between the exact prime flute and the exact shift clone, the transported metrics are uniformly equivalent and converge to one another at infinity in the required Fréchet-end sense. The Georgescu--Golénia comparison theorem therefore gives a compact difference of first resolvents and equality of essential spectra. Since every label `p_n+1` is composite, any invariant determined solely by this compact-resolvent class is not a rational-prime discriminator.

The stronger ideal story is different. PF-112 already shows that first-resolvent trace class is locally impossible for a nonisometric smooth metric comparison. PF-126--PF-130 show, however, that the actual clone defect is much better behaved than coarse coordinates suggest: the metric defect is `L^r` for every `r>1`; collapsing canonical collars are locally `S_r`-benign for `r>1`; the full collar wave weight is uniformly controlled; cusp synchronization has summable wave weight; and the Lambert body has strong `L¹` defect. None of these local statements by itself proves a global `S_r`, wave/scattering, resonance, or determinant comparison.

## What remains possible

Prime specificity could still appear in discrete spectrum, a stronger Schatten class with `r>1`, higher resolvent powers, heat/wave or scattering data, resonances, or a relative determinant — but only if the global construction is well defined and distinguishes the prime flute from the exact composite clone. `S_1` for the first resolvent is already the wrong target.

## Status / novelty

The global compact-resolvent equivalence and local ideal estimates are persisted findings. The conclusion is a no-go for essential-spectrum/compact-class discrimination, not an isospectrality theorem and not a proof of scattering equivalence.

## Falsification criterion

An essential-spectrum invariant of the prime flute that differs from the shift clone under the PF-125 identification would contradict the compact-resolvent theorem. A genuine advance would prove or refute a stronger global relative class — `S_r`, wave/scattering, discrete spectral shift, or determinant — and then test whether the resulting invariant survives the clone control.

## Lean-formalizable core

- Bilipschitz bounds for ideal Lambert quadrilaterals.
- Summability of cusp synchronization defects.
- Abstract implication from asymptotic metric equivalence to compact relative resolvent, assuming the analytic theorem as imported input.
