# MI-010 — Spectral fidelity requires an ideal budget and a declared multiscale description budget

**Evidence level:** proved for the operator-ideal, positive-mass, and finite-multiscale models covered by AF-108--AF-116

## Core intuition

A spectral object can be correct at every cutoff while its operator-ideal mass, determinant, or normalized shape escapes in the limit. Even after moving to relative scale, saying that a family “needs many scales” is incomplete: one scale, finitely many scales, tolerance-dependent covering complexity, worst-case scale labels, and average description cost are different resources.

The decisive question is therefore not just whether some normalization makes the spectrum tight. It is **how many moving scale centers are required, with what mass tolerance and what source-forced complexity budget**.

## Strongest justified principle

AF-108--AF-109 separate stagewise Schatten membership from a uniform ideal budget and ideal-norm fidelity. In positive trace class, trace tightness is the additional finite-window resource needed for trace and Fredholm determinant fidelity. AF-110--AF-112 show that infinitesimal eigenvalue clouds can make ordinary and regularized determinants collapse to zero-free exponentials or `1` even while finite spectral mass survives.

AF-113 shows that a nontrivial profile may survive after rescaling by a moving operator scale, but this requires relative-mass tightness rather than merely tracking the largest eigenvalue. AF-114 makes the one-scale condition exact for positive Schatten mass: some scalar centering makes the log-spectrum tight if and only if the pairwise log-ratio law is tight. The spike-plus-cloud example is therefore one-scale repairable after the right centering; max-scale failure alone is not intrinsic multiscale structure.

AF-115 gives the exact finite hierarchy. A family is repairable by `k` moving scale centers precisely when the probability that `k+1` independent mass samples are mutually separated beyond every fixed log-radius tends to zero. Persistent `m`-cloud examples calibrate the hierarchy and growing cloud count defeats every fixed `k`.

AF-116 then separates cardinality from description cost. A family can fail every fixed finite-scale model while, for each mass tolerance `epsilon`, needing only finitely many centers `K(epsilon)`; it can even have infinitely many exact scale labels but bounded mean bit cost under rapidly decaying mass weights. Thus “infinitely multiscale” is not a complete obstruction until the destination observable declares whether it charges worst-case cardinality, tolerance covering, entropy, or average code length.

## What remains possible

A concrete arithmetic application may force a canonical scale, a finite hierarchy, or a source-natural coding budget. The relevant theorem must prove exactly that resource and show that the target spectral invariant is continuous in it. Conversely, failure of any fixed `k` is not by itself evidence of unusable spectral complexity if the destination weights rare scales cheaply.

## Status / novelty

Schatten ideals, tightness, determinants, finite mixtures, packing, and coding/entropy are classical. The synthesis is the resource hierarchy: **relative spectral fidelity is a multiscale transport problem whose obstruction depends on the scale-description budget actually consumed downstream**.

## Falsification criterion

Produce a covered positive spectral family that violates the pairwise or `(k+1)`-separation characterizations, or an application whose final invariant is stable under a strictly weaker scale-complexity resource than the one claimed necessary. A positive application should derive its ideal, tightness, and scale-description budgets from the source rather than choose them after inspecting the target.

## Lean-formalizable core

- Uniform Schatten-budget assembly.
- Pairwise log-ratio criterion for one-scale tightness.
- `(k+1)`-separation criterion for `k`-scale repairability.
- Separation of fixed-cardinality, tolerance-covering, and weighted description complexity.
