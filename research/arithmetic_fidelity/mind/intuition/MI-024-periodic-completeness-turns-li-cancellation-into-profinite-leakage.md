# MI-024 — Periodic completeness turns Li cancellation into a source-specific profinite phase problem

**Evidence level:** proved

## Core intuition

Sparse root-rate fidelity depends on the admissible output sampler, not only on how well a phase can be approximated globally. For one conjugate Li mode, arbitrary unbounded sampling is governed by the strongest half-integer approximation events. Requiring the sampler to revisit every residue class modulo every integer changes the quantifiers: catastrophic approximation matters only if exponential cancellation leaks into **every** profinite cylinder strongly enough to survive that coverage obligation.

The constrained currency is therefore a congruence-uniform cancellation exponent. However, periodic completeness itself supplies no universal safety margin: the residual theorem must use arithmetic information about the actual zero-derived phase.

## Strongest justified claim

AF-257 identifies the arbitrary-sampling exponent

`kappa_{1/2}(alpha)=2 limsup_{q_j even} log(q_{j+1})/q_j`.

AF-258 replaces it under periodic completeness by

`K_pc(alpha)=inf_M min_r K_{M,r}(alpha)`.

The worst periodically complete two-mode root rate is `q_rho exp(-K_pc(alpha))`; one safe cylinder with subexponential cancellation forces `K_pc=0`.

AF-259 classifies each cylinder through even principal convergents and odd transport multipliers. AF-260 eliminates the apparently unbounded multiplier optimization at fixed modulus: each cylinder is a weighted finite-state residue process, and exact `2`-adic shells satisfy explicit formulas. A single weak shell forces `K_pc=0`, whereas `K_pc>=c` requires every shell to carry jump rate at least `c`.

AF-261 shows that this finite-state pressure is not automatic. For every `c in [0,+infinity]` there is an irrational phase for which **every** congruence cylinder has exponent `c`, and the unrestricted exponent is also `c`. Periodic completeness can therefore be exactly as bad as arbitrary sparse sampling at any prescribed level.

AF-262 identifies a sharp safe source class. If the unit phase `nu=e^(2 pi i alpha)` is algebraic and non-torsion, Baker-type/Diophantine separation gives `kappa_{1/2}=0`; if it is torsion, `K_pc=0`; hence every algebraic unit phase has zero profinite obstruction. For a Keiper pair this applies conditionally if its doubled phase is algebraic. No algebraicity statement for actual nontrivial zeta zeros is assumed.

## Synthesis of evidence

Output coverage acts like an information-preserving topology on sparse observation, but topology alone does not regularize the phase. AF-260 makes the residual obstruction finite-state, AF-261 proves that the entire obstruction spectrum survives those finite-state constraints for arbitrary irrational phases, and AF-262 shows that genuine source arithmetic can collapse it.

The surviving theorem is therefore neither “prove generic irrational phases are well distributed” nor “use more congruence classes.” It is to prove that the actual Keiper phase belongs to a restricted arithmetic class, has a weak residue shell, or obeys another source-specific Diophantine law strong enough at the radial margin.

## Counterevidence / boundary cases

The classification is exact for one conjugate two-mode signal. Several comparable off-critical modes can cancel on higher-dimensional affine resonance fibers, where one safe one-dimensional cylinder need not control the full sum.

AF-261 is an engineered control, not a zeta model. AF-262 gives a sufficient algebraic class, not evidence that Riemann zeros or Keiper phases are algebraic. Periodic completeness also does not cover every zero-density sampler with a different combinatorial coverage law.

## Epistemic status

**Exact two-mode classification plus source boundary:** periodically complete fidelity is governed by profinite distribution of dangerous convergents; each fixed cylinder is finite-state, arbitrary irrational phases can realize every obstruction level, and algebraic unit phases have zero profinite obstruction.

## Novelty/prior-art status

The continued-fraction, algebraic-Diophantine, and congruence ingredients retain the prior-art boundaries recorded in AF-257--AF-262. This intuition makes no broader originality claim.

## Falsification criterion

Produce a periodically complete retained set violating the exact `K_pc` rate formula, invalidate the finite-state reduction of AF-260, construct an algebraic non-torsion unit phase with positive exponential half-integer cancellation, or show that AF-261's realization construction misses a required congruence cylinder. Any of these would materially change the classification.