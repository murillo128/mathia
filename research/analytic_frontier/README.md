# Analytic Frontier

## Scope

`analytic_frontier` is a classical analytic-number-theory research line for extracting mechanisms from the current quantitative frontier around the Riemann hypothesis and testing whether they can produce new RH-relevant leverage or transferable clues for other Mathia lines.

The line should concentrate on the active machinery that is currently producing unconditional progress: Dirichlet polynomials and their large values, zero-density estimates, zero-detecting arguments, mean values and moments of zeta and Dirichlet `L`-functions, mollifiers, exponential/sieve inputs, and zero statistics when they are used as quantitative analytic information rather than as a separate spectral program.

The purpose is not to repackage the whole classical literature or to optimize constants for their own sake. Prefer questions where a modern analytic estimate changes the available information budget, exposes a reusable structural mechanism, or gives a concrete bridge into an existing Mathia obstruction.

## Research objective

Seek explicit quantitative statements of the form

`new analytic control -> stronger zero-location / zero-density / moment information -> RH-relevant consequence or transferable mechanism`.

In particular, investigate whether recent large-value, zero-density, mollifier, correlation, or moment techniques can:

- strengthen unconditional control of zeros away from `Re s = 1/2`;
- supply missing arithmetic inputs required by `weil_inertia`, `mobius_cancellation`, or other active lines;
- identify finite-order statistics or estimates that are genuinely stronger than the information already encoded by classical support-one / first-two-moment arguments;
- expose a precise quantitative barrier showing why a tempting classical route cannot scale to RH.

A result is valuable even when it is negative, provided it sharply identifies the missing estimate, exponent, support range, correlation order, or uniformity regime.

## Boundaries

Do not treat a known equivalence to RH as progress. Do not count a restatement, a numerical verification at finite height, or a conditional theorem whose hypothesis already contains essentially the desired zero-location information as an RH advance.

Keep literature results, Mathia derivations, computational evidence, and speculative transfer clues epistemically separate. When using very recent preprints, independently audit the load-bearing estimate before treating it as evidence.

Do not duplicate `weil_inertia`: if the main mathematical object becomes the compressed Weil form, inertia, rank defects, or its specific prime-side matrix realization, hand the resulting question to that line. `analytic_frontier` owns the upstream analytic machinery and its quantitative consequences.

## Starting directions

The initial search surface is intentionally broad but classical:

1. Guth–Maynard-style large-value bounds for Dirichlet polynomials and their consequences for zero-density and primes in short intervals.
2. Modern zero-detecting and density estimates, especially where a new witness decomposition or mean-value estimate changes an exponent barrier.
3. Levinson–Conrey-type mollifier methods, including optimization of zeta/derivative combinations and twisted moments rather than mollifier length alone.
4. Pair/higher correlations and moments when they can be converted into unconditional quantitative zero-location information or a clearly isolated missing theorem.
5. Bridges from these tools into active Mathia lines, emitted as clues only after the exact transferred statement and decisive test are identified.

## Persistence

Use the standard Mathia Research Watch workflow and repository conventions. Durable results belong under `findings/`; speculative but falsifiable handoffs belong under `clues/`; granular research attempts belong wherever the Research Watch skill currently requires. Do not create artifacts merely to record activity.
