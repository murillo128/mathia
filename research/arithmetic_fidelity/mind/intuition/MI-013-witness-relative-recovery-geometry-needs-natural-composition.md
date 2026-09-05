# MI-013 — Witness-relative recovery composes after minimal backward saturation, but the saturated witness class must still be source-natural

**Evidence level:** supported through AF-134 by exact quotient-seminorm recovery, counterexamples to naive defect composition, and the minimal backward witness-saturation theorem

## Core intuition

Approximate fidelity is always relative to what downstream tests can observe. Stagewise recovery errors therefore compose only after each upstream stage is tested against every witness that later stages can pull back to it. AF-134 makes this constructive: for a fixed chain, there is a unique minimal backward saturation of the witness families, obtained by repeatedly adjoining the pullbacks of downstream witnesses and taking the convex symmetric hull.

This solves the abstract compatibility problem but not the scientific one. A saturated family can become much larger than the local tests originally proposed. A useful Mathia application must therefore derive the destination witnesses and their pullbacks from the mathematical task itself and show that the resulting saturation has controlled complexity, regularity, or geometry.

## Strongest justified principle

AF-126--AF-130 distinguish full bounded-decision recovery, restricted convex witness recovery, and metric-local/Wasserstein recovery. The same representation can be faithful for one witness class and lossy for another.

AF-131--AF-133 prove that scalar recovery defects do not compose by themselves. An intermediate reconstruction can move a residual that is invisible to the downstream quotient into a direction visible upstream; composition needs a transport/naturality condition on the witness geometry.

AF-134 gives the exact fixed-chain completion. If stage `i` has native witness body `A_i` and linear transition `L_i`, define recursively

`B_0=A_0` and `B_i=conv(A_i union L_i^* B_{i-1})`.

The induced seminorms satisfy the exact recursion `q_i=max(p_i,q_{i-1} o L_i)`, and `B_i` is minimal by inclusion among convex symmetric witness bodies making the chain compatible. Equivalently, the final blind subspace is the intersection of the native blind directions transported through all downstream stages. Thus there is no remaining ambiguity about the generic witness enlargement required for composition.

## What remains possible

The live question is application-specific naturality. A representation can pass the formal saturation theorem while the required `B_i` becomes so large or irregular that the claimed compression no longer buys anything. Positive results should derive a source-natural destination witness class, compute or bound its backward saturation, and prove that the resulting complexity or stability budget remains compatible with the intended approximation.

For nonlinear or stochastic transitions the same idea may require a different pullback/transport notion; AF-134 should not be silently extrapolated beyond its fixed linear witness setting.

## Status / novelty

Dual seminorms, convex symmetric witness bodies, pullbacks, and exact linear composition are classical functional-analytic ingredients. The persisted synthesis is the operational boundary: **the generic composition repair is the minimal backward saturation of downstream observables; remaining difficulty lies in proving that this saturated observation geometry is mathematically natural and affordable for the source representation**.

## Falsification criterion

Produce a fixed linear chain for which AF-134's recursive witness body is not minimal or does not yield the stated seminorm recursion, or exhibit a claimed Mathia compositional-fidelity theorem whose destination witnesses require a saturation outside the admitted source geometry.

## Lean-formalizable core

- Recursive witness-body saturation.
- Exact `max` seminorm recursion.
- Minimality by inclusion.
- Blind-subspace intersection under transported witnesses.
