# MI-009 — Quotient repair separates algebraic defect, finite visibility, uniform conditioning, bidual coherence, and coefficient-category survival

**Evidence level:** supported by AF-078--AF-098; exact in the stated Banach/Lipschitz-free categories

## Core intuition

The question “can information be repaired after a quotient?” has several distinct levels even after the repair category is fixed. A defect may be algebraically nonrecoverable, positively separated from all recoverable data, invisible to every finite pointwise observation, recoverable on every finite subsystem only with diverging conditioning, or disappear after passing to a stronger coefficient category.

The newer results identify the missing local-to-global resource precisely: **finite exact solvability is cheap; uniform finite conditioning is what can force coherent global recovery**. Compactness may first produce that recovery only in the canonical bidual, leaving original-range fidelity as a separate gate.

## Strongest justified principle

AF-093 identifies the Lipschitz-versus-linear defect as the operator quotient `L(Z_F,K)/ran R_{F,K}`. AF-094 shows that robust defect is distance to the norm closure of `ran R`; AF-095 identifies that margin with bounded annihilator witnesses. AF-096 then closes the tempting dual-coefficient escape: if `K=Y^*`, ultrasummand linearization makes the restriction map surjective and the complete defect vanishes.

AF-097 adds a different topology. For every bounded `T:Z->K` and every finite-dimensional `E subset Z`, there is a global operator agreeing exactly with `T` on `E`. Hence extendable operators are pointwise/SOT/WOT dense even when they are not norm dense. A robust global defect can therefore be **exactly invisible at every fixed finite set of source points**.

AF-098 restores a quantitative finite certificate. Let `e_E(T)` be the least ambient operator norm of an exact interpolant on `E`, let `lambda_fin=sup_E e_E(T)`, and let `lambda_**` and `lambda_K` be the optimal bidual- and target-valued global extension costs. Then

`lambda_** <= lambda_fin <= lambda_K`.

Uniformly bounded finite repairs compactify into one `K**`-valued global repair. If `K` is `1`-complemented in `K**` — in particular if it is dual or reflexive — all three costs coincide. In that category, failure of a global extension is finitely detectable only after a norm budget is declared: the finite interpolation profile must diverge.

## Evidence synthesis and boundaries

Finite values alone do not see the defect; finite values plus a uniform conditioning budget can. Bidual coherence still need not imply original-range recovery for a general coefficient space, and none of these abstract extension theorems supplies arithmetic provenance, equivariance, positivity, locality, or a source-natural coefficient category.

A positive arithmetic application must therefore specify the repair category, observation topology, coefficient category, allowed norm budget, and whether landing in a completion is acceptable. A family of unrelated finite witnesses is not evidence of a global repair unless its conditioning remains uniformly controlled.

## Status / novelty

Lipschitz-free spaces, Banach `Ext`, closed-range theory, Hahn--Banach, Banach--Alaoglu/Tychonoff compactness, biduals, and ultrasummands are classical. The persisted synthesis is the fidelity hierarchy: **algebraic defect, norm-robust defect, finite pointwise visibility, uniform finite conditioning, bidual coherence, and original-range recovery are genuinely different gates**.

## Falsification criterion

Produce a target/category covered by AF-098 with uniformly bounded finite exact interpolation costs but no corresponding bidual extension, or a `1`-complemented target for which `lambda_fin` differs from the optimal global extension norm. An arithmetic application can evade the hierarchy only by justifying a different observation/repair category.

## Lean-formalizable core

- Operator-extension quotient and distance-to-range stability.
- Pointwise finite interpolation of arbitrary bounded fiber operators.
- SOT/WOT density versus norm closure.
- `lambda_** <= lambda_fin <= lambda_K`.
- Compactness globalization of uniformly bounded finite repairs.
- Equality of finite and global costs for `1`-complemented bidual targets.
