# MI-011 — Cross-scale collision observability can compress to one off-circle heat trace

**Evidence level:** exact upper-half reconstruction and one-point off-circle reconstruction for the periodic unit-circle model through XF-130

## Core intuition

The periodic collision-identifiability barrier is not fundamentally a need for many scalar channels. What matters is mixing reflected Vieta shells in a way that breaks the `k <-> N-k` degeneracy. Once that relation is present, a very small observable can contain the whole divisor.

The full upper half of proper harmonic heat histories is universally identifying, and one complex spatial heat trace off the unit circle compresses the same cross-scale information into a single channel. The remaining difficulty is therefore not periodic target observability but whether the actual Xi source can access such a relation with controlled interface error and conditioning.

## Strongest justified principle

XF-124--XF-128 show that sublinear proper-harmonic histories and even large terminal windows can be collision-blind. XF-129 proves the complementary positive boundary. Every proper harmonic history recovers the phase of its matching Vieta coefficient from its slowest heat tail; unit-circle self-inversivity reflects the upper half into the lower half. Thus all histories with `m>N/2` determine the divisor, modulo one even-degree central sign ambiguity that is only a rigid rotation and leaves collision geometry unchanged.

XF-130 then groups a one-point trace `Q_zeta(s)=E(zeta,s)` by the known heat rates `delta_k=delta_{N-k}`. Each rate exposes the reflected pair through one complex amplitude. Self-inversivity supplies the second real relation, and `|zeta|!=1` makes the resulting `2x2` real-linear system invertible. Taking `|zeta_N|=exp(sigma/N)` gives only `O_sigma(N)` worst spatial amplification, so one root-spacing-scale displacement off the real circle is already sufficient for exact recovery.

This separates **channel count** from **information category**. A single scalar history can be globally identifying when its spatial evaluation couples all Vieta shells before the heat-rate degeneracy is quotiented.

## Counterevidence / boundary

The theorem is an exact periodic target-side statement. It does not prove that the real Xi source supplies `Q_zeta`, that the periodic surrogate remains accurate at a complex displacement of order one root spacing, or that recovering the divisor in this way yields a useful quantitative upper bound for the Newman transition.

The inversion is polynomially conditioned in the spatial reflected-shell step, but extracting close heat exponents from finite/noisy time data is a separate conditioning problem. The exact full-history theorem should not be silently promoted to a finite-sample stability claim.

## Epistemic status

**Exact periodic collision observability with a sharp half-spectrum boundary and an exact one-channel compression; source accessibility and quantitative Xi transport remain open.**

## Falsification criterion

Produce two non-rotationally-equivalent unit-circle divisors with identical upper-half histories, or two distinct unit-circle divisors with identical `Q_zeta(s)` for a declared `|zeta|!=1`. A source-positive continuation should instead derive or approximate the off-circle/cross-scale trace from the actual Xi source and bound every interface and conditioning loss needed by the transition theorem.
