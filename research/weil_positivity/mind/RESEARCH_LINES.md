# Weil-positivity research lines

This file holds the current mathematical lines of investigation suggested by the durable Weil-positivity intuitions. It is not a roadmap, task queue, status page, or history.

## Derive the nonlocal sampling object independently before asking it to reproduce Weil positivity

**Linked intuitions:** `MI-001-positivity-needs-a-sign-producing-global-operation`, `MI-010-source-forced-critical-gram-can-have-the-wrong-weil-orientation`, `MI-011-prime-ray-marginals-do-not-determine-mixed-prime-coupling`, `MI-012-automorphic-multiplicity-does-not-prevent-global-scalarization`, `MI-013-critical-sector-transport-needs-new-global-arithmetic-structure`.

WP-267--WP-272 separate critical source coherence, hostability, category descent, and scalar sign. WP-273 then proves that any positive compression of the canonical pole-completed carrier must be genuinely nonlocal: for function-generated ranges, the continuum `cosh(x/2) dx` norm must be contractively reconstructible from prime-power samples, and every localizable continuous test space fails.

WP-274 shows that **nonlocal analytic sampling is still not enough**. Multiplication by `cosh(x/2)^(1/2)` normalizes the critical Mangoldt half-density exactly to the positive discrete measure

`sigma_Lambda = sum_(n>=2) Lambda(n)/(n+1) (delta_(log n)+delta_(-log n))`.

This measure satisfies the Herglotz growth condition unconditionally. Classical Herglotz--Clark theory can therefore reconstruct a meromorphic inner function whose model space has `sigma_Lambda` as a Clark measure, making the pole-completed quadratic form identically zero on the pulled-back model-space range.

That existence theorem is not a Weil mechanism: the same construction works for essentially any Poisson-finite positive-minus-positive Jordan carrier because the desired sampling measure is fed into Herglotz inversion and the resulting model space returns that same measure by construction. It is a matched-control-stable representation tautology.

The surviving route must reverse the causal order. Derive an inner function, canonical system, de Branges Hamiltonian, boundary correspondence, matrix/noncommutative object, or equivalent nonlocal space from **independent source/Mathia geometry first**. Only then ask whether its pre-existing sampling or positivity law reproduces the Mangoldt term together with the Gamma and polar sectors in the correct Weil orientation. Building the analytic object from the target carrier itself is no longer evidence.

## Treat hostability, category descent, scalar sign, localizability, nonlocal realizability and independent model selection separately

WP-273 makes nonlocality necessary for the canonical compression route; WP-274 shows it is not sufficient. A model space manufactured by inverse Clark theory from the target measure passes the sampling identity for universal representation-theoretic reasons. The new discriminator is **independent selection of the analytic object before the target sign law is imposed**.