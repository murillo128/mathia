# MI-004 — The Mangoldt anchor is exact algebraically but unbounded in the natural positive Hardy norm

**Evidence level:** supported by exact Hardy identities and a decisive norm-topology obstruction

## Core intuition

The canonical Hardy shell geometry already contains the exact finite arithmetic selector: polarization against the base Hilbert shell gives `Lambda(n)`. The obstruction is not failure to encode the coefficient but failure of that coefficient functional to extend continuously to the natural positive completion. Arithmetic information can therefore be present on an algebraic core and still be unusable as a positive Hilbert-space observable.

## Strongest justified principle

WP-067 defines the positive shell Gram form

`Q_H(B)=Tr(B^* H B)=||H^{1/2}B||_2^2`

on the finite shell span and the exact anchor functional

`L(B)=Tr(HB)`,

with `L(Gamma_n)=Lambda(n)`. The formal anchor is the identity, whose `Q_H` self-energy diverges. Subtracting exactly that divergent base self-energy from the canonical cutoff square leaves

`Q_H(B)-2 Re L(B)`,

which is indefinite whenever `L` is nonzero. WP-067 correctly leaves open whether a finite scalar counterterm might nevertheless restore positivity; that question is equivalent to continuity of `L` in the `Q_H` norm.

WP-068 closes that escape. The canonical cumulative full-root differences

`B_N=sum_{d|N,d>1} Gamma_d`

satisfy `L(B_N)=log N` while `Q_H(B_N)=O(log N)`. Hence `X_N=B_N/log N` obeys

`Q_H(X_N)->0` but `L(X_N)=1`.

So `L` is unbounded on the algebraic shell span with respect to the positive Hardy norm. No finite scalar renormalization of the same completed square can restore positivity; the failure is a genuine continuity/topology obstruction, not merely the infinity of one chosen anchor vector.

This complements WP-064--WP-065. For the separate full-root signed Hardy channel, every bounded self-adjoint metric repair and every natural unbounded self-adjoint operator-level metric product that produces positivity must contain the channel's own polar sign. Thus both obvious repairs fail for structural reasons: the positive shell completion loses continuity of the arithmetic anchor, while the signed channel's self-adjoint metric repair imports its sign from the operator being repaired.

## What remains possible

A surviving mechanism must change more than a scalar counterterm or a self-adjoint left metric. Possibilities not ruled out include a canonically different topology in which the arithmetic functional is continuous, a singular quadratic-form construction outside the WP-065 operator-product hypotheses, or a genuinely nonseparable finite--archimedean/global completion in which the selector and sign are created together.

Any such change must be independently forced. Choosing a weaker norm merely because it makes `L` bounded, or a metric merely because it converts the signed channel to `|A|`, would not provide a new positivity mechanism.

## Status / novelty

The Hardy trace identities, Riesz boundedness dichotomy, cumulative full-root identity, and polar decomposition mechanisms are persisted exact findings with classical functional-analysis inputs. The local synthesis is a supported separation between **algebraic selector recovery** and **continuous positive realization**.

## Falsification criterion

Extend `L` continuously to the `Q_H` completion despite the WP-068 null sequence, or produce a finite scalar counterterm making `Q_H-2 Re L+c` nonnegative. Either would contradict the current obstruction. A positive advance would instead derive a different canonical completion/form in which the exact selector is continuous and whose sign is forced independently of the desired arithmetic conclusion.

## Lean-formalizable core

- Positivity of `Q_H` and exact values `L(Gamma_n)=Lambda(n)` on finite shell combinations.
- Null-sequence criterion proving unboundedness of a linear functional.
- Consequence that `Q_H-2 Re L+c` is unbounded below for every finite `c`.
- Abstract polar-sign classification for bounded self-adjoint metric repairs.