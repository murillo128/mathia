# MI-004 — Nyman source information localizes before the closure-level target gap is controlled

**Evidence level:** proved structural identities with an open source-to-target bridge

## Core intuition

A source-faithful quotient can expose the relevant directional mass while still hiding the target repair. The hidden quantity is now identified at two levels: finitely it is the gain from enriching the reciprocal-integer Nyman section by the parameters `M/n`; asymptotically it converges to a global projection gap between the natural and continuous Nyman closures.

Ambient norm control cannot reach the regime where this gap matters. The live problem is therefore a **source-to-target-orientation bridge**, not better conditioning or a vanishing-mesh argument.

## Strongest justified claim

NB-031--NB-048 construct the weighted tail-shell quotient, localize the directional Burnol-scale signal, and approximate the unique target repair recursively. The recursive error is explicit but still target-selected.

NB-049 proves the ambient-norm threshold is misaligned with the repair corridor: `||Omega_M||/d_N -> 0` forces `M d_N^2 -> infinity`, precisely where the weighted skeleton is already relatively lossless. Critical/subcritical repair requires directional information stronger than Cauchy through the full norm.

NB-050 gives the finite normal form. After Bagchi dilation the weighted tail is `C_(M,N)=span{rho_(M/n):M<n<=N}`, containing `V_K`, and

`widetilde d_(M,N)^2-d_N^2=(d_K^2-delta_(M,N)^2)/M`.

NB-051 shows the numerator is not generically a mesh error. If both scales grow with `N/M -> infinity`, then `delta_(M,N)->d_cont`, `d_K->d_nat`, and

`M(tilde d_(M,N)^2-d_N^2) -> Delta_*:=d_nat^2-d_cont^2`.

At fixed aspect ratio the finite enrichment can remain bounded away from zero. The recursive repair therefore misses a genuine target component in the extra continuous Nyman directions.

## Synthesis of evidence

The source and target sides are now exact but structurally different. One side is a localized directional flow; the other is a continuous-versus-natural projection gap. A new theorem must connect them, or prove that the relevant gap vanishes/has controlled sign under a source condition available before solving the Nyman target.

This also kills a tempting simplification: refining the finite grid does not automatically make the recursive repair exact at first order. The limiting obstruction can survive refinement as `Delta_*`.

## Counterevidence / boundary cases

NB-051 does not determine whether `Delta_*` is positive, zero, or how it interacts with RH in the regime needed by the research program. It identifies the limiting target quantity; it does not provide source access to it.

NB-049 remains a method obstruction only. Directional correlations can beat ambient norm bounds, and such a relation is precisely the surviving possibility.

## Epistemic status

**Exact source/target separation with closure-level normal form:** ambient norms activate too late, finite repair slack is an enrichment gap, and its two-scale first-order limit is the natural-versus-continuous target projection gap.

## Novelty/prior-art status

The Nyman family, Bagchi dilation, projection geometry, and closure arguments retain their finding-level prior-art boundaries. This intuition synthesizes the exact finite and limiting normal forms.

## Falsification criterion

Invalidate the NB-050 repair identity or the NB-051 convergence to `Delta_*`, or show that ambient norm control reaches the critical corridor despite NB-049. Strategically, a source-side formula or inequality controlling the continuous-versus-natural target gap would cross the current gate.