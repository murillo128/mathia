# MI-013 — Bost--Connes regularity needs an intermediate transverse category

**Evidence level:** supported by exact canonical-representation classifications through MC-149

## Core intuition

The Bost--Connes weak-completion problem is not repaired by adding the system's most obvious regularities. After strong/weak completion, canonical energy regularity is too weak because it is blind to every diagonal target, while raw semigroup regularity has no useful middle point: bounded commutators admit every bounded diagonal and compact/Schatten commutators reject Möbius itself.

The surviving category must therefore be **transverse to energy and quantitatively intermediate**. It has to restrict multiplicative variation in a source-forced way without becoming either a trivial `l^infty` bound or a decay condition incompatible with the actual Möbius sequence.

## Strongest justified principle

MC-147 identifies the target-completeness problem: the represented coefficient weak closure is all bounded diagonals and the represented full weak closure is all bounded operators. A useful topology cannot simply weaken norm continuity without another source restriction.

MC-148 proves that the canonical Hamiltonian supplies no such restriction. The time-flow fixed algebra and the canonical normal Gibbs centralizer are exactly the same diagonal algebra, and every bounded diagonal is infinitely smooth and entire under the canonical flow. Energy degree and energy smoothness therefore do not discriminate arithmetic targets after completion.

MC-149 tests the first genuinely transverse family. For `S_m e_k=e_mk`, the commutator weights are `a_mk-a_k`. Their operator norm is automatically at most `2||a||_infinity`, so raw boundedness again admits all bounded targets. Compactness is equivalent to those multiplicative differences tending to zero; Möbius violates this for every `m>=2`, with essential norm equal to its full norm and no finite Schatten membership. The obvious decay endpoint therefore selects the wrong class.

## Counterevidence / boundary

The classification is representation-specific and concerns the canonical Hamiltonian plus raw canonical semigroup commutators. Weighted or twisted commutators, averages over dilations, alternative correspondences/Dirac operators, different representations, or nonlinear relational constraints are not reduced to MC-149.

Such an escape is not evidence by itself. Its weights or twists must be source-forced rather than chosen to encode `mu`, and it must connect multiplicative information to the additive prefix order in `M(x)` at a cost below the RH-complete endpoint.

## Epistemic status

**Exact no-go synthesis for the canonical energy and raw-semigroup regularity classes; the intermediate transverse category is open.**

## Falsification criterion

Exhibit a bounded diagonal excluded by the claimed universal raw boundedness, a Möbius semigroup commutator that is compact for some `m>=2`, or invalidate the fixed-point/centralizer identification in the stated canonical representation. A positive escape should instead define an intrinsic intermediate transverse seminorm or relation, prove that Möbius satisfies it non-tautologically, and derive quantitative additive excursion control unavailable for arbitrary bounded diagonals.
