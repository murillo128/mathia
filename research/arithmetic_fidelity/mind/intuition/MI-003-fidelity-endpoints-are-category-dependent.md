# MI-003 — Exact source-category membership, divisor complexity, and metric fidelity are different claims

**Evidence level:** supported by exact counterseparations

## Core intuition

Exact analytic-source membership can be rigid without being a robust metric certificate. The current zeta-source evidence now adds a second boundary: even exact Bohr recurrence and the correct rational-prime-power frequency support can coexist with an infinite off-critical zero transport. What matters after category membership is the **coefficient/divisor law carried inside that category**.

Thus fidelity has at least three distinct currencies: exact membership, finite-complexity identifiability, and quantitative stability. None can be substituted silently for another.

## Strongest justified claim

AF-007--AF-011 separate differential, jet, stochastic, and supportwise notions of fidelity. AF-266--AF-268 give the vertical zeta-source analogue: finite count-preserving zero surgeries can approach the genuine logarithmic derivative arbitrarily closely in sup norm, yet every nontrivial finite surgery exits `AP(R)` because its defect is a nonzero `C_0(R)` function.

AF-269 extends that categorical obstruction to every paired zero rearrangement with finite total displacement. Such a defect is still in `C_0(R)`, so exact Bohr almost-periodicity forces the signed divisor transport to be trivial.

AF-270 proves that this is not an all-infinite-surgery theorem. A periodic exponential polynomial can move an entire critical vertical lattice to symmetric off-critical lattices with infinite total transport while preserving exact ordinate counts, reflection, Bohr periodicity, and an absolutely convergent logarithmic-derivative expansion on one rational-prime-power ray. Frequency support and exact recurrence are therefore too coarse.

AF-271 isolates the next information scale. For a periodic quotient with `r` distinct divisor orbits, the first `r` prime-power coefficients detect nontriviality exactly by a Vandermonde argument. But no fixed prefix works for unbounded complexity, and exact detection has no positive stability modulus when divisor nodes collide. A separation/compactness hypothesis restores a quantitative lower bound.

## Synthesis of evidence

The current frontier is no longer “does an RH-violating control remain almost periodic?” The answer can be yes for infinite periodic controls. The useful question is what **zeta-specific coefficient law or cross-prime compatibility** excludes those controls without simply reinstating the Euler product as an assumption.

A source theorem should therefore state its information budget explicitly. Exact category membership can kill finite-total transports; bounded divisor complexity converts a finite coefficient prefix into exact fidelity; stable finite-prefix fidelity additionally needs geometric separation. A successful RH bridge must use whichever of these is genuinely consumed downstream.

## Counterevidence / boundary cases

AF-270 is an engineered one-prime periodic control, not a zeta model. It shows insufficiency of recurrence, reflection, counting, and frequency support, not that the full zeta coefficient law admits an off-critical realization. AF-271 treats bounded finite periodic divisor complexity and does not give a uniform complexity bound for arbitrary source-preserving controls.

Metric instability also remains real: nontrivial divisor configurations can approach each other so closely that exact finite detection has an arbitrarily small coefficient signature. Exact algebraic fidelity is therefore not automatically numerically usable.

## Epistemic status

**Supported category/complexity/stability boundary:** finite-total transport is excluded by exact recurrence, infinite periodic off-critical transport can preserve that category, bounded periodic complexity is finitely identifiable, and stable identification needs additional separation.

## Novelty/prior-art status

The almost-periodic, exponential-polynomial, Vandermonde/Prony, and Diophantine ingredients retain their finding-level prior-art classifications. This note synthesizes their role in the fidelity hierarchy.

## Falsification criterion

Construct a nontrivial finite-total zero transport whose right-half-plane defect is Bohr almost periodic, invalidate the AF-270 periodic off-critical control, or exhibit a bounded-`r` periodic divisor quotient whose first `r` source coefficients agree with the reference despite a nontrivial divisor. Strategically, a zeta-specific coefficient law that excludes the AF-270 family would cross the present gate.

## Lean-formalizable core

The finite-dimensional Vandermonde detection statement of AF-271 and its separated-node lower-bound skeleton are natural finite algebra targets.