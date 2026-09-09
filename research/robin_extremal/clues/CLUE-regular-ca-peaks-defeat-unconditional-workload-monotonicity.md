---
id: CLUE-regular-ca-peaks-defeat-unconditional-workload-monotonicity
type: research-clue
status: proposed
origin: master-researcher
target_line: robin_extremal
based_on:
  - research/robin_extremal/findings/RE-001-robin-counterexample-blocks-contain-regular-self-tangent-ca-peaks.md
---
# Genuine regular CA peaks defeat unconditional workload monotonicity

## Observation

RE-001 supplies the exact signed workload identity, with x = log n, g(x) = 1/(x log x), Phi the prime-layer step function, and D(x) = x - Phi(x):

log(G(C_b)/G(C_a)) = integral_a^b D(x) g'(x) dx,

where G(n) = sigma(n)/(n log log n), and a,b are regular self-tangent roots. Put F(x) = integral_a^x D(t) dt. Integration by parts gives

W = F(b) g'(b) - integral_a^b F(x) g''(x) dx.

Since g'(x) < 0 and g''(x) = (2 log(x)^2 + 3 log(x) + 2)/(x^3 log(x)^3) > 0 for x > 1, F >= 0 throughout an interval would imply W <= 0. This is a tempting sufficient certificate, NOT an equivalence to Robin's inequality.

It fails on actual prime-layer data, not merely on a synthetic measure. Take

C_a = 720720 = 2^4 * 3^2 * 5 * 7 * 11 * 13,
C_b = 6983776800 = 2^5 * 3^3 * 5^2 * 7 * 11 * 13 * 17 * 19.

A 50-decimal-digit interval-arithmetic check gives

0.0006408932520507618872337689779304666578632490363751
< log(G(C_b)/G(C_a)) <
0.0006408932520507618872337689779304666578632490363939.

Both integers satisfy strict regular self-tangent CA inequalities. Both also satisfy Robin's inequality: gamma - log G(C_a) is approximately 0.02732394210475479, and gamma - log G(C_b) is approximately 0.02668304885270402. Thus a positive workload increment is compatible with a safely positive Robin margin.

The finite interval verification can be reproduced without computing inverse-g atoms. For a candidate n with prime exponents a_p, let epsilon = g(log n), and lambda(p,j) = log((1-p^(-j-1))/(1-p^(-j))). Verify, with strict interval comparisons,

max_p lambda(p,a_p+1)/log p < epsilon < min_{p | n} lambda(p,a_p)/log p.

Include the next omitted prime with exponent zero in the maximum. This suffices for all omitted primes because log(1+1/p)/log p decreases for p > 1, while the layer slopes decrease with j. These tests passed for both displayed integers. Compute sigma(n)/n as an exact rational before applying interval logarithms.

## Research question

Can the owner formulate a prime-layer estimate that controls approach to the Robin barrier while allowing genuine positive increments below it? In particular, does RE-001's counterexample-block hypothesis supply a restriction that rules out the displayed safe positive increments in the relevant violating regime, rather than assuming a workload sign globally?

The question is deliberately narrower than asking for monotone CA peak values. Merely rewriting the desired Robin inequality as W <= the available margin is not an arithmetic estimate and must not be promoted as progress.

## Why it may matter

This separates a correct exact representation from an incorrect universal sign expectation. It provides two small exact regression integers for proposed convex-order, cumulative-workload, and sign certificates. Any proposed universal nonpositive workload, or universal F >= 0 between all regular peaks, must fail this test.

This is a rejection of the proposed strengthening, not a rejection of RE-001, the Robin line, or a barrier-conditioned argument. It does not establish the existence of a Robin counterexample.

## Decisive test

First independently reproduce the strict CA inequalities and positive log-G increment above using interval arithmetic. A small self-contained checker is sufficient; a Lean proof is a separate deliverable. Then test any candidate workload-order lemma against these two exact integers before launching a larger computation.

For a candidate explicitly restricted to violating blocks, make its additional hypothesis visible and verify that it excludes this example for a mathematical reason. Require a source-derived estimate on the prime-layer atoms, not a relabeling of the Robin margin. If only an unconditional monotonicity proof was being pursued, reject that strengthening and preserve the original signed workload problem.

A separate exploratory enumeration at 50-digit working precision, retaining actual prime-layer atoms with inverse-g positions up to x = 3000, found 478 atoms, 38 regular roots and 37 consecutive tested edges. Of those edges, 31 had positive workload and negative minimum cumulative F. These finite exploratory counts are not interval-certified or asymptotic evidence; the two displayed exact integers are the interval-checked regression test.

## Evidence boundary

Owner: robin_extremal. Imported source: RE-001 at reviewed commit 16e9325e032fabb3b9a59664b7f7a15174a65ec2, for the source atoms, regular self-tangent definition, and exact workload identity. The integration-by-parts calculation and finite checks were produced during this extraordinary Master/Visionary audit.

The local checks used mpmath interval arithmetic at 50 decimal digits, exact rational sigma(n)/n, and strict interval comparisons. They are not a formal proof, a repository test-suite execution, or an independent certification of every claim in RE-001. No scheduled Visionary campaign was changed. This new proposed clue still requires owner-side semantic deduplication against any concurrently added clues before acceptance.

Stop/re-export criterion: if already covered by a prior source-specific monotonicity counterexample, link that result instead of creating another finding. Otherwise re-export only the independently verified kill test and the precise extra hypothesis required by a surviving barrier-conditioned argument.
