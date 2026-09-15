# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Establish anchor connectivity before treating ancestry test count as coercive

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-020-relative-ancestry-constraints-need-an-anchored-component-before-their-count-can-be-coercive`.

FD-117--FD-144 separate the reversible Farey skeleton, common-source escape, finite-information blindness and the opposite source-reconstruction boundary. FD-144 shows that arbitrary source-independent normalized ancestry tests remain noncoercive throughout every sublinear-rank budget `L_T=o(r_T)`.

FD-145 exposes a prior structural obstruction. Writing `a_n=mu(n)b(n)` on squarefree integers turns a zero ancestry defect into the relative equation `b(pn)=b(n)`. If the visible ancestry graph is disconnected from the finite Möbius anchor, its whole component has an undetermined `Z_2` orientation. A fixed rank-wall source can therefore satisfy **every** visible high-rank ancestry equation exactly while having `a_n=-mu(n)` at every observed parent, independently of how many tests are taken.

The next coefficient-side theorem must therefore make its anchoring explicit. The requested coefficient vertices should lie in a visible ancestry component connected to at least one Möbius-fixed coefficient, or the observable must import equivalent absolute-orientation information through direct coefficients or a genuinely nonlocal Farey/Fourier coupling. Merely increasing the number or resolution of tests inside an unanchored high-rank component cannot be coercive.

## Determine the information threshold after the ancestry component is anchored

Once anchor connectivity is guaranteed, FD-144 becomes the relevant quantitative lower bound again: `o(r_T)` arbitrary source-independent normalized local tests can still be defeated by one common source along a subsequence. It remains open whether the linear-rank scale is sharp in an anchored model, whether source-native signed structure beats it, or whether a stronger common-source construction pushes the impossibility beyond `Theta(r_T)`.

In the central regime `r_T~log log T`, this asks for the first genuinely coercive source-native law between the sublinear-rank no-go and the high-information identity observations of FD-142. A successful proposal must not merely encode the squarefree parent under another name; its provenance from the Farey/Franel/ancestry skeleton and its effective information budget both matter.

A destination-side Fourier-skeleton coercivity theorem remains a distinct route because it could bypass coefficient recovery and the local ancestry gauge entirely.

## Keep connectivity, information, precision, provenance and target recovery separate

A coercive law must now specify more than coordinate count. It should state which coefficient component is anchored, which ancestry edges are visible, how many independent source constraints are imposed at rank `r_T`, how the tests are normalized, whether they are source-independent, what precision is consumed, and how much source freedom remains.

The audit order for future ancestry claims is therefore: first test **anchor connectivity** against the exact rank-wall control of FD-145; then test the information budget against the min-wise common-source control of FD-144; only after both survive should the observable be treated as evidence for coefficient recovery. Direct source-identity encodings remain circular, while nonlocal Fourier/Farey observables must be judged separately by whether they actually force the target norm rather than merely identify coefficients.