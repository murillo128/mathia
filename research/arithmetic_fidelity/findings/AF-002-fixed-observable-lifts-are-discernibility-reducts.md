# AF-002 — Fixed-observable lifts are decision-relative discernibility reducts

**Status:** `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`

## Claim

Let `X` be finite, let

\[
T:X\to Y
\]

be an already-retained compression or side-information map, let

\[
d:X\to D
\]

be the discriminator to be recovered, and let

\[
\mathcal F=\{f_1,\ldots,f_n\},\qquad f_i:X\to A_i,
\]

be a **fixed** library of candidate observable coordinates. For `J\subseteq\{1,\ldots,n\}`, write

\[
F_J(x)=(f_j(x))_{j\in J}.
\]

Define the unresolved conflict pairs

\[
\mathcal C(T,d)
=
\bigl\{\{x,x'\}:T(x)=T(x'),\ d(x)\ne d(x')\bigr\}.
\]

For each conflict `c={x,x'}`, define its discernibility set

\[
\Delta(c)
=
\{i:f_i(x)\ne f_i(x')\}.
\]

Then:

1. `d` is exactly recoverable from `(T,F_J)` if and only if
   \[
   J\cap\Delta(c)\ne\varnothing
   \qquad\text{for every }c\in\mathcal C(T,d).
   \]
2. If some `\Delta(c)` is empty, no lift assembled from the library can recover `d`.
3. Otherwise, the inclusion-minimal recovering subsets `J` are exactly the minimal transversals (minimal hitting sets) of the hypergraph
   \[
   \mathcal H(T,d,\mathcal F)
   =\{\Delta(c):c\in\mathcal C(T,d)\}.
   \]
   In particular, the minimum number of retained coordinates is the transversal number `\tau(\mathcal H)`.
4. If coordinate `i` has a nonnegative cost `w_i`, minimum-cost exact recovery is precisely the corresponding weighted hitting-set problem.

This is not a new combinatorial theory specific to Arithmetic Fidelity. It is the finite exact form of the **decision-relative discernibility / reduct** construction from rough-set theory, with `T` treated as side information already retained. The Arithmetic Fidelity consequence is therefore a prior-art redirect: once admissible lifts are specified as a fixed finite observable library, generic "minimal lift" selection should reuse reduct/discernibility theory rather than be redeveloped from scratch.

## Derivation

AF-001 gives the exact fiber criterion: `d` is recoverable from `(T,F_J)` if and only if

\[
T(x)=T(x'),\quad F_J(x)=F_J(x')
\Longrightarrow
 d(x)=d(x').
\]

Equivalently, for every pair with equal `T`-value and unequal discriminator value, at least one selected coordinate must differ. For a conflict `c={x,x'}`, the coordinates capable of doing that are exactly `\Delta(c)`. Hence

\[
d\text{ recoverable from }(T,F_J)
\iff
\forall c\in\mathcal C(T,d),\quad J\cap\Delta(c)\ne\varnothing.
\]

That is exactly the hitting-set condition in item (1).

If `\Delta(c)=\varnothing` for some conflict, every available coordinate agrees on the two states, so no subset of the library can separate them. This proves item (2).

When all discernibility sets are nonempty, a recovering subset is inclusion-minimal precisely when no selected coordinate can be removed while still hitting every `\Delta(c)`. That is the definition of a minimal hypergraph transversal. Minimizing `|J|` gives the transversal number, and replacing cardinality by `\sum_{j\in J}w_j` gives the weighted version.

## Exact bridge to rough-set reducts

In a Pawlak information system, a chosen set of condition attributes induces an indiscernibility relation: two objects are indistinguishable when all retained attributes agree. In a decision system, the target/decision attribute need only be preserved across pairs carrying different decisions. Skowron and Rauszer's decision-relative discernibility construction records, for each such pair, the set of condition attributes on which the pair differs; reducts are minimal attribute sets that preserve the required discernibility.

The present setup is the same mechanism with one extra piece of fixed side information. Pairs with

\[
T(x)\ne T(x')
\]

are already separated by the retained compression and impose no requirement on the lift library. Among pairs with equal `T`, only those with different `d`-values matter. Their discernibility entries are exactly the sets `\Delta(c)` above.

Thus the Arithmetic Fidelity hypergraph is a decision-relative discernibility hypergraph **conditioned on the already-kept data `T`**. The hitting-set statement is the Boolean form of the usual discernibility-function construction: each conflict contributes a clause saying that at least one attribute capable of separating that pair must be retained.

No historical novelty is claimed for this finite reduction.

## Why this matters for Arithmetic Fidelity

AF-001 showed that an unrestricted auxiliary mark is too powerful: one can simply take `M=d`, so unconstrained minimal-lift cardinality measures only fiberwise label count and not structural naturalness.

A fixed observable library is a genuine improvement because it makes admissibility explicit. If `d` is not already encoded among the allowed observables, recovery may fail or may require a nontrivial combination of independently supplied coordinates. The conflict hypergraph gives an exact audit object for that question.

It also makes **target leakage** visible rather than rhetorical. If the library is allowed to contain the target discriminator itself, then the single coordinate `f_i=d` belongs to every conflict discernibility set, so `{i}` is immediately a one-coordinate reduct. Therefore a library intended to test structural preservation must be fixed or justified independently of the answer it is meant to recover.

The important research frontier is consequently not generic finite feature minimization. It is the mathematical origin of the admissible observables: why phase, orientation, marking, boundary data, transverse data, operator-valued structure, or another coordinate is intrinsically available before the discriminator is known, and what additional naturality/equivariance/locality/operator constraints those observables satisfy.

## Prior art and novelty assessment

Pawlak's rough-set framework formalizes knowledge through indiscernibility relations induced by retained attributes. That already contains the basic idea that a target is exactly decidable only when the retained description does not merge objects that require different decisions.

Skowron and Rauszer's 1992 discernibility matrices/functions make the pair-separation structure explicit and use it to characterize reducts. In the decision-relative form, only pairs with different decision values generate discernibility requirements. This is the closest direct prior art to the hypergraph `\mathcal H(T,d,\mathcal F)`.

The same pair-separation combinatorics is also adjacent to zero-error function computation and characteristic-graph methods already recorded for AF-001. Those literatures reinforce the same lesson: once the admissible observations are fixed, exact recovery becomes a classical combinatorial separation problem.

The Mathia-specific contribution here is the **identification and boundary placement**: the obvious finite "choose the smallest set of intrinsic observables that preserves a discriminator after `T`" problem is classical reduct/discernibility mathematics. Arithmetic Fidelity should import it as infrastructure and reserve new claims for structural restrictions, infinite/analytic settings, or arithmetic consequences not already captured by that theory.

## Boundaries and failure modes

- The theorem is finite and deterministic. Infinite libraries, measurable structures, continuous observables, approximate recovery, noise, and probabilistic decision value require different machinery.
- The library coordinates are used only through equality/inequality. Geometry or metric structure inside an `A_i` is ignored.
- The cost statement assumes additive coordinate costs. Non-additive complexity or interaction costs need a different optimization object.
- The result selects from a predeclared coordinate library. It does not classify arbitrary nonlinear functions of the upstream object as admissible lifts.
- Treating `T` as fixed side information is essential. If `T` itself may be redesigned jointly with the lift, the optimization problem changes.
- A mathematically minimal reduct need not be canonical or natural; several incomparable minimal reducts may exist.
- The prior-art bridge does not show that rough-set algorithms are useful for infinite-dimensional RH constructions, and it makes no claim about rational-prime fidelity or RH.

## Consequence for the line

Do not spend future Arithmetic Fidelity work rediscovering generic finite minimal-feature selection. When a proposed lift is a subset of a fixed finite observable family, formulate the conflict discernibility sets and use reduct/hitting-set language immediately.

The research burden moves one level earlier: **derive the admissible observable family from intrinsic mathematics without target leakage**, then ask whether that structurally constrained family hits every discriminator conflict created by the compression. New theory is most likely to be needed when the admissible family is not a finite attribute table at all—for example when naturality, symmetry, locality, operator category, topology, or analytic continuation couples the observables globally.