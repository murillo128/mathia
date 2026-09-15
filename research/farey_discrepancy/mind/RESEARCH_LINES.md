# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Require quantitative anchor exposure, not connectivity alone, before treating ancestry energy as coercive

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-021-finite-lq-ancestry-coercivity-needs-quantitative-anchor-exposure`.

FD-117--FD-144 separate the reversible Farey skeleton, common-source escape, finite-information blindness and the opposite source-reconstruction boundary. FD-145 then exposes an exact structural obstruction: writing `a_n=mu(n)b(n)` on squarefree integers turns a zero ancestry defect into `b(pn)=b(n)`, so any visible component disconnected from the finite Möbius anchor has a free `Z_2` orientation.

FD-146 shows that repairing this connectivity defect is not enough. On the **full** squarefree ancestry graph every coefficient is connected to the anchor `1` and every local edge is observed, yet a fixed rank-wall source has normalized finite-`L^q` ancestry defect

`O(((log log T)^R0/log T)^(1/q)) -> 0`

while its normalized coefficient error tends to `2`. Equivalently, any uniformly normalized anchored Poincare constant must diverge at least like

`(log T/(log log T)^R0)^(1/q)`.

The wall is pointwise visible—its edge defect has magnitude `2` and `L^infinity` detects it—but its share of the full edge mass tends to zero. Connectivity is therefore qualitative; stable coefficient recovery requires **quantitative anchor exposure under the actual source-native normalization**. A useful ancestry/Farey observable must prove that every macroscopic orientation change crosses a boundary carrying nonvanishing observation mass, or use a nonlocal destination functional that couples the two orientations without reducing to diluted local edge energy.

## Determine the information threshold only after connectivity and exposure both survive

FD-144 remains the independent observation-budget obstruction, but its place in the audit is now later. Even after an observable has removed the exact disconnected-component gauge of FD-145 and defeated the vanishing-boundary construction of FD-146, `o(r_T)` arbitrary source-independent normalized ancestry tests can still be fooled by one common source along a subsequence.

The live coefficient-side theorem must therefore establish a source-native anchored inequality such as

`||b-1||_(L^q(V_T,nu_T)) <= C ||nabla b||_(L^q(E_T,eta_T))`

with `C` independent of `T` for the weights actually induced by the Farey/Franel skeleton, or identify a different quantitative exposure condition that defeats every fixed-rank wall. Only after such an inequality survives should the linear-rank information threshold of FD-144 be interpreted as the next bottleneck.

A destination-side Fourier-skeleton coercivity theorem remains a distinct route because it could bypass local coefficient recovery, the component gauge and the finite-`L^q` boundary dilution simultaneously.

## Keep connectivity, exposure, information, precision, provenance and target recovery separate

A coercive law must now state more than coordinate count. It should specify which coefficient component is anchored, how observation mass is distributed across cuts connecting macroscopic source regions to the anchor, how many independent source constraints are imposed at rank `r_T`, how they are normalized, whether they are source-independent, what precision is consumed, and how much source freedom remains.

The audit order for future ancestry claims is therefore: first test **anchor connectivity** against FD-145; then test **quantitative cut exposure in the claimed destination norm** against FD-146; then test the surviving information budget against FD-144. Direct source-identity encodings remain circular, while genuinely nonlocal Fourier/Farey observables must be judged separately by whether they force the target norm rather than merely identify coefficients.