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

AF-282--AF-285 price the finite-prefix two-prime repair. On the known prefix `1,...,N`, joint phase spacing is `Theta(1/N)`, uniform stable coefficient recovery has sharp coordinatewise mixed degree `Theta(N)`, and linear-size raw acquisition is possible. AF-287 now strengthens the sample-selection statement: classical frame sparsification yields an **unweighted `O(N)` subset of raw mixed samples with uniformly bounded condition number**.

That bounded-condition frame closes the independent-jitter gap left by AF-286. For arbitrary rowwise offsets `|tau_j|<=T`, the exact matrix expansion gives

\[
\|\widetilde A-A\|\le \|A\|\bigl(e^{T\log N}-1\bigr),
\]

so a nominal least-squares decoder on the selected frame has fixed relative `ell^2` distortion whenever `T=O(1/\log N)`. The common-offset subclass from AF-286 already forces the same order. Hence full known-prefix coefficient recovery has the sharp worst-case timing scale

\[
T_{\rm jitter}(N)=\Theta(1/\log N)
\]

for both arbitrary independent rowwise jitter and common-mode timing uncertainty, even though the latter is an exact coefficient gauge rather than generic perturbation.

The finite-prefix timing frontier has therefore moved. The live questions are now target-sensitive: which RH-relevant or arithmetic downstream functionals descend through the common-clock gauge and need no clock-origin lift; what changes with unknown support or infinite Dirichlet sources; and which source constraints reduce the coefficient-level timing bill.

## Treat the information bills separately

Finite local degree determines prime-power depth at one prime, not prime breadth. Separate marginal channels can destroy joint interaction; complete mixed channels can restore exact separation. On the `log2/log3` prefix, label spacing, mixed degree, raw sample count, condition number, common-clock provenance, and independent jitter are distinct resources. AF-287 shows that the earlier `sqrt(N)` independent-jitter loss was an artifact of a weak frame estimate, not a new information scale.

Future fidelity claims must state which resource is being bounded: difference-object complexity, local depth, prime breadth, observation dimension, coupling geometry, cadence/fiber geometry, label resolution, mixed degree, sample count, time horizon, common-mode provenance, independent jitter, coefficient-recovery norm, source weights, support knowledge, and downstream target metric. Exact injectivity, polynomial label spacing, linear sample count, bounded condition number, and inverse-log timing stability are distinct statements.