# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Match source sign complexity to a quantitative finite-order Euler modulus

**Linked intuition:** `MI-018-signed-complexity-only-transfers-through-sign-regular-observations`.

AF-215--AF-220 force ordered sign complexity but leave the quantitative transfer into the shrinking Euler-log observation window open. The next theorem must relate the source sign budget to a separation or curvature modulus at the resolution actually consumed by the target.

## Price the actual target metric before calling a representation compressed

**Linked intuitions:** `MI-019-faithful-translation-lifts-are-affine`, `MI-020-prime-tail-localization-has-an-information-conservation-law`.

AF-221--AF-233 show that localization has a real information bill and that contraction can lower it only in the metric actually used downstream. A useful compression claim still needs both a cheaper target geometry and a theorem that the final arithmetic argument consumes only that target.

## Build cancellation-coherent source access to the Li root-rate class

**Linked intuitions:** `MI-021-coarse-rh-endpoints-can-still-require-deep-source-access`, `MI-022-prefix-truncation-must-respect-cancellation-orbits`.

AF-234--AF-243 show that the RH root-rate endpoint tolerates large output error but is extremely sensitive to breaking the binomial cancellation orbit in the source representation. The live bridge must assemble the required cancellation orbit before the root-rate quotient is formed.

## Separate source category, breadth, coupling, resolution, sampling, and timing geometry

**Linked intuitions:** `MI-003-fidelity-endpoints-are-category-dependent`, `MI-023-local-completeness-can-preserve-a-root-rate-discriminator-at-zero-density`, `MI-024-periodic-completeness-turns-li-cancellation-into-profinite-leakage`, `MI-025-regular-sampling-separates-aliasing-from-finite-window-stability`.

AF-244--AF-276 show that coarse symmetry, zero counting, endpoint jets, compact-open proximity, and periodic transport do not replace an exact source-category argument. Bounded Euler degree makes local prime-power depth finite and sharp, but global Euler fidelity still requires information at infinitely many prime locations. AF-275--AF-276 further show that finite collections of exact values or jets leave positive-dimensional tail fibers even inside degree-one Euler products.

AF-278--AF-281 separate continuous time breadth, one-lattice aliasing, marginal coupling loss, and exact mixed-channel recovery. If all mixed samples `F(c+i(k_1h_1+...+k_Jh_J))` are retained, ordinary Dirichlet coefficient fidelity is equivalent to `cap_j R_(h_j)={1}`; separate resonant marginals do not have the same information.

AF-282--AF-285 price the finite-prefix two-prime repair. On the known prefix `1,...,N`, joint phase spacing is `Theta(1/N)`, uniform stable coefficient recovery has sharp coordinatewise mixed degree `Theta(N)`, and linear-size raw acquisition is possible. AF-287 strengthens the sample-selection statement: classical frame sparsification yields an **unweighted `O(N)` subset of raw mixed samples with uniformly bounded condition number**. For arbitrary rowwise offsets `|tau_j|<=T`, the exact matrix expansion gives fixed relative `ell^2` distortion exactly on the sharp scale `T=Theta(1/log N)`.

AF-288 now separates that coefficient-level timing bill from the target. A common offset acts by

\[
(a_n)\mapsto(a_n n^{-i\tau}),\qquad F(s)\mapsto F(s+i\tau).
\]

Hence the horizontal zero divisor, and in particular the RH predicate `Re rho=1/2` for every nontrivial zero, is exactly invariant under the complete common-clock orbit. Common clock origin is therefore **free for that target**, even though full coefficient recovery still pays `Theta(1/log N)`.

The same finding also separates exact source anchoring from robust calibration. If two known nonzero source coefficients occur at multiplicatively independent indices (for zeta, `2` and `3`), their phases determine `tau` uniquely on all of `R`. But irrational torus recurrence gives arbitrarily remote near-returns, so there is no source-independent global inverse modulus on an unbounded timing range. A bounded clock prior restores an ordinary local inverse-Lipschitz chart.

The timing frontier is now narrower: determine which intermediate RH mechanisms genuinely depend on absolute imaginary origin rather than horizontal divisor data; how independent non-common-mode jitter behaves after target-specific quotienting; and what changes for unknown support or infinite Dirichlet sources.

## Treat the information bills separately

Finite local degree determines prime-power depth at one prime, not prime breadth. Separate marginal channels can destroy joint interaction; complete mixed channels can restore exact separation. On the `log2/log3` prefix, label spacing, mixed degree, raw sample count, condition number, common-clock provenance, independent jitter, and the downstream target quotient are distinct resources.

AF-288 adds the sharp warning that **recovering a nuisance parameter is unnecessary when the requested target is constant on its gauge orbit**. Exact source anchors can remove a gauge without making the inverse globally stable, while a gauge-invariant target can avoid the lift entirely. Future fidelity claims must therefore state both the source category and the target metric before assigning an acquisition or calibration cost.