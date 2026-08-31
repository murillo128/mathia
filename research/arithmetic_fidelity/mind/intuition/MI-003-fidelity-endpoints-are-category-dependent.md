# MI-003 — Infinitesimal, average, formal, and zero-error fidelity are different mathematical claims

**Evidence level:** supported by exact counterseparations

## Core intuition

There is no single numerical notion of “how much information survives” that can be moved freely among smooth, stochastic, formal, and supportwise settings. Several natural fidelity tests agree at one endpoint and diverge sharply at another. The category of the claim is therefore part of the claim itself.

## Strongest justified principle

AF-007 measures smooth local loss by the vertical differential rank. It gives a sharp first-order lower bound on the dimension of a smooth lift, but it cannot see disconnected fibers or other discrete ambiguities. AF-010 supplies a parallel warning for jets: all finite jets may be compatible with factorization while a smooth flat germ still carries hidden variation; full-jet fidelity needs a quasianalytic/analytic category plus the relevant closure theorem.

AF-009 and AF-011 separate probabilistic notions. Conditional variance is the exact `L²` prediction defect and can tend to zero under increasingly informative observations. Zero-error recovery is instead a support-confusability statement: a single discordant overlap is fatal, however small its probability mass. Garbling worsens both notions, but their vanishing criteria are genuinely different.

Thus a fidelity argument must state whether it is local-differential, average-risk, formal-jet, or supportwise. Passing one test cannot silently be promoted to another.

## What remains possible

Bridges between categories are valuable when extra hypotheses are explicit — connected fibers for differential factorization, quasianalyticity for full jets, quantitative support separation for converting average to zero-error, and so on. The point is not to isolate the categories permanently, but to prove the bridge rather than assume it.

## Status / novelty

The individual criteria and counterseparations are persisted findings. The category-gate formulation is a supported synthesis.

## Falsification criterion

Derive a theorem under stated natural hypotheses that makes two currently separated endpoints equivalent, or exhibit a claimed cross-category inference that survives the persisted flat-germ, disconnected-fiber, or rare-support-conflict controls.

## Lean-formalizable core

- Vertical-rank lower bound for smooth lifts.
- Conditional-variance Pythagorean identity and garbling monotonicity.
- Support-confusability graph criterion.
