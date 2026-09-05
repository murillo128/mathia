# MI-011 — The first nonmultiplicative escape is additive correlation; naive affine traces still hit cancellation and analytic-continuation walls

**Evidence level:** supported through PL-171 by exact finite-horizon phase bounds, literature-backed low-support correlation formulae, and exact affine/congruence trace computations

## Core intuition

The multiplicative exponent lattice is an exact arithmetic coordinate system, but its natural finite-dimensional phase statistics increasingly classicalize. Positive finite-prime harmonic tests face dimension/frequency horizons; signed low-energy characters can alias on finite height windows; and low-support zero correlations reduce the lattice conservation law to universal GUE pairings.

The first persisted correction that is genuinely outside this quotient is **ordinary addition**. Ratios one-swap terms require shifted correlations `n` with `n+h`, information not encoded by multiplicative exponent differences alone. But simply adjoining affine maps `n -> an+b` does not yet solve the analytic problem: relative traces can collapse to finite-head boundaries, and congruence channels recover classical Dirichlet/Hurwitz data only in the half-plane where the relevant Schatten trace is already absolutely defined.

## Strongest justified principle

PL-164--PL-166 show that positive finite-prime phase detectors cannot be made order-one merely by increasing dimension inside the available finite-horizon comparison. Fixed prime support has a positive harmonic cap, growing dimension is limited by finite phase marginals, and the Ford--Maynard--Zaharescu comparison imposes a primorial frequency horizon `y << log T/loglog T`; before that horizon the first-order additive bias remains `o(1)`.

PL-167 shows that signed characters evade that high-frequency obstruction only through a different failure: finite-height aliasing. At logarithmic prime dimension, nontrivial signed prime-log characters can be almost constant over the observation interval and thereby lose horizontal/zero sensitivity.

PL-168 identifies the low-support zero-side analogue. In the Rudnick--Sarnak regime, exponent-lattice conservation collapses to the universal pairing structure underlying GUE statistics; no irreducible mixed-prime invariant survives in that channel.

PL-169 marks a genuine category change. The first ratios-conjecture one-swap correction imports additive shifted correlations between `n` and `n+h`; these are not functions of the multiplicative exponent-lattice difference alone. Thus additive structure is not an ornamental extension but a concrete source of arithmetic information missing from the pure multiplicative carrier.

PL-170--PL-171 test the canonical affine realization. Relative traces for affine shifts can cancel the infinite zeta tail down to a finite-head boundary and become zero-blind. Congruence projections recover Hurwitz/Dirichlet `L` channels for `Re(s)>1`, but their Schatten/trace-class boundary remains `q sigma>1`; periodic cancellation alone does not cross the analytic-continuation wall needed near the critical line.

## What remains possible

A live escape should couple multiplicative provenance to additive/affine information **before** it is reduced to an absolutely convergent trace or finite-head cancellation. Candidates include relative/renormalized objects whose continuation is source-forced, higher additive correlations with a nontrivial sign mechanism, or a mixed semigroup representation whose domain remembers both prime factorization and translation without treating either as a post-hoc coordinate.

The new evidence does not show that addition is sufficient for RH. It shows that addition is the first concrete information channel encountered here that is demonstrably absent from the exponent-lattice quotient and appears in nonuniversal arithmetic correlation formulae.

## Status / novelty

Prime-log tori, GUE low-support pairings, shifted divisor correlations, affine semigroups, Hurwitz zeta, Dirichlet `L`-functions, and Schatten thresholds are classical. The persisted synthesis is the boundary: **pure multiplicative phase carriers classicalize or alias; additive correlation is a genuine missing variable, but the naive affine trace representation still loses it at finite-head or absolute-convergence boundaries**.

## Falsification criterion

Derive the PL-169 one-swap arithmetic correction from the multiplicative exponent-difference quotient alone, contradicting its dependence on additive shifts; or construct, inside the PL-170/PL-171 canonical affine trace class without new renormalized/domain data, a critical-line zero-sensitive trace that evades the established cancellation/trace boundary.

## Lean-formalizable core

- Finite-prime phase/frequency horizon inequalities.
- Finite-height character aliasing construction.
- Separation of multiplicative exponent difference from additive shift `n -> n+h`.
- Affine relative-trace cancellation identity.
- Congruence projection to Dirichlet/Hurwitz channels and trace-class threshold.
