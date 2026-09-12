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

## Separate source category, local depth, prime breadth, coupling, cadence, label resolution, mixed degree, sample count, and coefficient conditioning

**Linked intuitions:** `MI-003-fidelity-endpoints-are-category-dependent`, `MI-023-local-completeness-can-preserve-a-root-rate-discriminator-at-zero-density`, `MI-024-periodic-completeness-turns-li-cancellation-into-profinite-leakage`, `MI-025-regular-sampling-separates-aliasing-from-finite-window-stability`.

AF-244--AF-276 show that coarse symmetry, zero counting, endpoint jets, compact-open proximity, and periodic transport do not replace an exact source-category argument. Bounded Euler degree makes local prime-power depth finite and sharp, but global Euler fidelity still requires information at infinitely many prime locations. AF-275--AF-276 further show that finite collections of exact values or jets leave positive-dimensional tail fibers even inside degree-one Euler products.

AF-278--AF-281 separate continuous time breadth, one-lattice aliasing, marginal coupling loss, and exact mixed-channel recovery. If all mixed samples `F(c+i(k_1h_1+...+k_Jh_J))` are retained, ordinary Dirichlet coefficient fidelity is equivalent to `cap_j R_(h_j)={1}`; separate resonant marginals do not have the same information.

AF-282--AF-284 now price three different finite-prefix resources for the concrete `log2/log3` repair. On the known prefix `1,...,N`, joint phase spacing is `Theta(1/N)` and **uniform stable coefficient recovery has sharp coordinatewise mixed degree `Theta(N)`**. The dense `L=30N` square gives a stable frame, but AF-284 shows that its quadratic observation count is not intrinsic: classical matrix concentration extracts an **unweighted subset of distinct raw mixed moments of size `O(N log N)`** with a breadth-uniform inverse under adversarial per-sample absolute noise.

The remaining finite-prefix acquisition gap is therefore

\[
\Omega(N)\quad\text{versus}\quad O(N\log N),
\]

not `Omega(N)` versus `Theta(N^2)`. Determine whether the logarithmic factor is an artifact of generic row sampling or is forced by unweighted raw mixed-moment acquisition under a stated timing geometry. Weighted `O(N)` spectral sparsification is relevant prior art but changes the acquisition/noise semantics and must remain a separate model. Keep known support, maximal time horizon, timing precision, the weighted coefficients `b_n=a_n n^{-c}`, conversion back to an unweighted target, and the unrestricted infinite-source obstruction as separate costs.

## Treat the information bills separately

A finite local degree determines prime-power depth at one prime, not prime breadth. Separate marginal channels can destroy joint interaction; complete mixed channels can restore exact separation. On the `log2/log3` prefix, phase labels are only `Theta(1/N)` apart, stable mixed **degree** is `Theta(N)`, and an unweighted raw subset with `O(N log N)` scalar samples already suffices for breadth-uniform coefficient stability.

Future fidelity claims must therefore state which resource is being bounded: difference-object complexity, local depth, prime breadth, observation dimension, coupling geometry, cadence/fiber geometry, label resolution, mixed degree, sample count, time horizon, coefficient-recovery norm, source weights, support knowledge, and downstream target metric. Exact injectivity, polynomial label spacing, linear mixed degree, and near-linear sample count are distinct statements.