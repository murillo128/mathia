---
type: adversarial-review
target: research/arithmetic_fidelity/findings/AF-008-formal-jet-fidelity-quasianalyticity-boundary.md
---

# Adversarial review

## Adversary

The general quasianalytic extension in Claim 4 is missing a closure hypothesis needed by its own proof. The argument forms

\[
G(u,v)=D(u,v)-D(u,0)
\]

and then applies quasianalyticity to `G` as a germ on `R^(m+n)`. Closure under coordinate restriction gives only the `m`-variable germ `u -> D(u,0)`; it does not by itself imply that its cylindrical pullback `(u,v) -> D(u,0)` belongs to the original `(m+n)`-variable class. Without closure under precomposition with the coordinate projection (equivalently, cylindrical extension), `G` need not be an admissible germ and the quasianalyticity implication cannot be invoked.

The same missing closure is also needed for the stated converse characterization of single-point full-jet fidelity by quasianalyticity: embedding a one-variable flat germ as `(u,v) -> f(v_1)` is not guaranteed by restriction and subtraction alone. Standard real-analytic and Denjoy--Carleman classes do have the relevant composition/projection closure, so the core examples are not challenged; the issue is the stronger theorem as stated for *any* quasianalytic germ class with only the two listed closure properties.

The objection is resolved by either adding closure under pullback by coordinate projections/cylindrical extension to the hypotheses (and carrying it through the iff statement), or supplying a derivation showing that this closure follows from the class axioms already stated.