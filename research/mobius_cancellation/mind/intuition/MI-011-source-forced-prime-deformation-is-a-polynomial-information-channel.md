# MI-011 — Source-forced prime deformation is a polynomial information channel with a collision--reconstruction barrier

**Evidence level:** exact finite deformation and norm tradeoff through MC-096

## Core intuition

A source-forced deformation can expose genuine prime coordinates without producing cancellation. Full product-fiber Walsh coordinates retain orthogonality but make endpoint evaluation expensive; radial/count quotients make the endpoint cheap by collapsing many source coordinates together. MC-096 shows that this is an exact quantitative tradeoff, not merely a weakness of total-degree radialization.

## Strongest justified principle

MC-091--MC-095 build the exclusive-prime deformation, product fibers, and radialized polynomial channel. MC-096 proves that for every partition into prime-count blocks the collision map and endpoint reconstruction map have operator-norm product at least `N^{1-o(1)}`. The witness already occurs on a source-forced degree-two rectangle of large primes where all coefficients have one sign. Degree one is comparatively harmless at the critical power scale, so the first serious low-degree obstruction is the loss of within-shell arithmetic structure, not Möbius parity itself.

## What remains possible

A useful quotient must retain more than block counts, or a theorem must prove cancellation within the collision classes using the actual arithmetic weights. A coupled recurrence may also avoid factorizing the problem into collision followed by endpoint reconstruction. Merely adding finitely or subpolynomially many count labels cannot reconcile generic Walsh `L^2` control with cheap endpoint recovery.

## Status / novelty

The Hilbert-space norm calculation is elementary. The durable synthesis is source-specific: **the natural prime deformation is a real information channel, but count-based compression has an unavoidable polynomial collision/reconstruction cost before any Mertens gain appears**.

## Falsification criterion

Construct a prime-block count quotient for the MC-092 product fibers for which both collision and endpoint-reconstruction norms are `N^{o(1)}`, or invalidate the degree-two same-sign rectangle used in MC-096.