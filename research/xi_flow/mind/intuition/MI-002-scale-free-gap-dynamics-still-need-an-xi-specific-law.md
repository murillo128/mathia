# MI-002 — Scale-free gap dynamics avoid high-zero degeneration but still need an Xi-specific coercive law

**Evidence level:** exact for XF-004--XF-005; RH/de Bruijn--Newman consequence remains open

## Core intuition

An absolute gap is the wrong currency for a height-uniform backward-heat argument because the natural zero spacing tends to zero. Normalizing the squared gap by its exterior inverse-square environment produces a scale-invariant coordinate, but scale invariance alone does not make it arithmetic.

The useful target is therefore a **source-specific law for the normalized interaction**, not merely the existence of a dimensionless variable.

## Strongest justified principle

XF-004 turns the scale problem into a hard obstruction: every sufficiently high zeta window contains absolute gaps of order `1/log T`, so an estimate whose continuation time is proportional to gap squared gives at best `O(1/log^2 T)`, never a fixed backward interval.

XF-005 defines `R=qS` and obtains the exact scale-free law `q'=4(2-R)`. The equilibrium is `R=2`; `R<2` opens the pair and `R>2` contracts it. Collision birth has `R -> 0`, and the integrated deficit `2-R` exactly controls the accumulated squared-gap change.

This is the right dimensional form, but it is universal for real-zero heat flows. A proof relevant to the de Bruijn--Newman constant must derive an Xi-specific upper bound, average, correlation, or monotonicity for `R` that matched non-Xi heat flows do not share.

## Evidence synthesis and boundaries

A local bound such as `R<2` on selected Lehmer pairs is not yet a global continuation theorem. The required estimate must survive height growth, cover the relevant pair population, and control how exterior fields interact when many gaps evolve simultaneously.

## Status / novelty

Scale normalization and the gap ODE are exact persisted derivations. The synthesis is the separation between removing dimensional degeneration and obtaining source-specific coercivity.

## Falsification criterion

Produce a matched non-Xi real-zero heat flow satisfying every proposed normalized `R` inequality while having a different collision threshold, or derive from the Xi representation an inequality for the time-integrated `2-R` deficit that yields a fixed backward interval uniformly in height.

## Lean-formalizable core

- Absolute-gap scaling obstruction.
- Scale invariance of `qS`.
- Exact normalized gap-flow identity.
- Integration of the equilibrium deficit.
