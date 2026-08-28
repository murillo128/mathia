# MI-003 — Absolute Selberg/Fredholm theory fails for structural reasons, and relative thresholds need controls

**Evidence level:** proved

## Core intuition

The prime flute is not a geometrically finite surface with an inconveniently large error term.  Its global orbit and spectral structures violate the hypotheses behind the standard absolute Selberg/Ruelle/Fredholm picture in several independent ways.  Moreover, even when a selected relative operator is well defined, a sharp analytic threshold can come from the one-dimensional flute tail rather than from primes.  The viable global direction is therefore **relative/localized theory after universal-background subtraction**, not another absolute Euler product.

## Strongest justified impossibility principle

For the ordinary `L^2` Laplacian of the infinite prime flute:

1. infinitely many primitive geodesic lengths accumulate at zero and on positive compact intervals, so standard prime-geodesic counting, Selberg orbital measures and ordinary Selberg/Ruelle Euler products are not locally finite in the required sense;
2. zero systole prevents a faithful strictly uniformly expanding coding with standard periodic weights;
3. infinitely many recurrent prime tangents implant essential spectral values

\[
0<\lambda_j<1/4,\qquad \lambda_j\to0;
\]

4. hence, with `lambda_j=s_j(1-s_j)` and `s_j->1`, the analytic pencil

\[
P(s)=\Delta-s(1-s):H^2\to L^2
\]

is non-Fredholm at infinitely many `s_j` in every neighborhood of `1`.

Therefore there is no standard near-one **absolute** meromorphic-Fredholm resolvent on ordinary `L^2` whose singularities are merely isolated finite-rank resonance poles.  A finite-tangent residual/scattering pole can globalize into an essential spectral point rather than into a global pole.

## Synthesis of evidence

PF-033/PF-035/PF-036/PF-039/PF-040 rule out the ordinary heat/zeta determinant and several natural pseudo-/parity repairs.  PF-069/PF-075 show that deleting only the shortest cuffs is insufficient: positive-length primitive accumulation and bounded-symbolic-complexity orbit proliferation remain.  PF-070 gives the uniform-expansion obstruction.  PF-092 strengthens all of these with an operator-level near-one Fredholm obstruction coming from actual sub-quarter essential spectrum.

The relative story carries a second warning.  PF-083 shows that the canonical local exact/reference period-two factor is absolutely convergent and zero-free.  PF-085 shows that the canonical Grunsky--Schiffer completion of the endpoint deformation is trace class.  PF-084/PF-086/PF-087 do produce a sharp `Re s=1/4` boundary in selected long-block/direct-scattering sectors, but PF-088 reproduces exactly the same boundary after replacing primes by the integer sequence.  Thus

\[
\operatorname{Re}s=1/4
\]

is a one-dimensional propagation/Schatten threshold, not a prime-specific spectral exponent.

## Boundary cases

The negative is deliberately about the standard absolute `L^2` framework.  It does not rule out:

- relative resolvents or spectral-shift theory when a reference shares the essential background;
- weighted/rigged spaces that remove escaping Weyl sequences by design;
- localized or marked tangent scattering;
- operator-valued boundary/Weyl data;
- a genuinely new renormalized dynamical object whose subtraction is forced by geometry rather than chosen to rescue a divergent product.

Compact or trace-class corrections cannot repair the **absolute** Fredholm obstruction, because essential spectrum is invariant under compact perturbation.  They may nevertheless define meaningful relative objects.

## Status / novelty

The operator-theoretic implications of essential spectrum and the classical geometrically finite Selberg/Fredholm framework are standard.  The proved content here is their application to the established pathologies of the exact prime flute.  No novelty should be attached to the quarter exponent after PF-088's integer control.

## Falsification criterion

The absolute statement would be falsified by a standard ordinary-`L^2` analytic Fredholm family for `Delta-s(1-s)` on a full neighborhood of `s=1` despite the established sequence of essential spectral values there.  The arithmetic interpretation of a relative threshold is falsified whenever the same threshold survives a featureless regularly spaced control, as `1/4` does.

## Lean-formalizable core

- Infinite-product obstruction when infinitely many factors fail to tend to one.
- Local non-finiteness from infinitely many primitive lengths in a compact interval.
- Abstract implication `lambda in sigma_ess(Delta) -> Delta-lambda` non-Fredholm.
- Mapping `lambda_j->0` to physical roots `s_j->1`.
- `p`-series criterion producing the integer-control `1/4` row threshold.
