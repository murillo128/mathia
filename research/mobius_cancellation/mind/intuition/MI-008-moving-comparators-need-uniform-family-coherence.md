# MI-008 — Moving comparators need uniform family coherence, and character imitation pays conductor and twisted-uniformity costs

**Evidence level:** supported by MC-053--MC-061; the fixed-class transfers and Burgess/conductor barriers are theorem-level in their stated hypotheses

## Core intuition

Allowing a comparator to depend on observation scale is a real escape from fixed-comparator transfer theorems, but finite-prefix agreement plus a good exponent for each frozen object is too weak. The missing resource is a **uniform, scale-coherent cancellation certificate whose arithmetic complexity is cheaper than the Möbius estimate being sought**.

Dirichlet characters make this boundary increasingly rigid. They can imitate Möbius on a long prefix, but exact fidelity forces conductor growth, two competing quadratic certificates repel in conductor, and even one weighted quadratic fit transfers a large bias into a twisted Möbius sum.

## Strongest justified principle

MC-053--MC-054 close broad fixed complex and completely multiplicative comparator classes by exponent transfer. MC-055--MC-056 show that moving quadratic characters can imitate a complete finite Möbius prefix while each frozen character has square-root cancellation, yet uniform constants and inter-scale replacement carry the hidden cost.

MC-057 makes exact quadratic interpolation quantitative: the conductor is eventually at least quadratic in the imitated prefix length. MC-058 shows that exact higher-order character imitation is much more expensive, with Burgess forcing conductor beyond `X^(4 sqrt(e)-o(1))` and in particular beyond `X^6` eventually in the stated regime. MC-059 proves that weighted approximate higher-order fidelity still retains a quartic conductor barrier.

MC-060 adds pair repulsion: two weighted quadratic fits cannot both remain subquadratic when their aggregate defect is bounded away from one; their product conductor is `X^(4-o(1))` or larger. MC-061 supplies a different obstruction for a single comparator: weighted quadratic proximity to Möbius forces a linear Liouville-character bias and hence a polynomially growing twisted-Möbius uniformity constant for every fixed sublinear exponent.

## What remains possible

A moving-comparator strategy must therefore be supported by a source-forced family theorem that simultaneously controls conductor growth, cancellation constants, and transitions between comparators. A family outside Dirichlet-character geometry may evade these exact barriers, but it must still expose an independently bounded complexity/uniformity resource rather than hide Mertens information in the moving certificate.

## Status / novelty

The transfer mechanisms, character interpolation, Burgess bounds, reciprocity, and square-divisor identities are classical or literature-backed. The synthesis is the uniformity gate: **prefix imitation consumes global family resources that per-object cancellation does not measure**.

## Falsification criterion

Construct a scale-dependent comparator family with strong Möbius fidelity and a uniform complexity/cancellation budget provably weaker than the target Mertens bound, or show that one of the conductor/twisted-uniformity barriers fails under its stated hypotheses.

## Lean-formalizable core

- Exact/weighted character-prefix conductor lower bounds.
- Product-conductor repulsion.
- Prefix-fidelity lower bound on family constants.
- Quadratic-fit implication for twisted Möbius bias.
