# MI-004 — Pointed positivity recovers the finite Weil coefficient, while canonical Hardy positivity leaves Mangoldt as a singular boundary trace

**Evidence level:** supported by exact positive constructions and obstructions from WP-067--WP-078, strengthened by the canonical cyclotomic Hardy-space control [WP-378](../../findings/WP-378-cyclotomic-hardy-positivity-factorizes-primewise-and-mangoldt-is-an-unbounded-boundary-trace.md).

The finite arithmetic package is stronger than merely having a formal Mangoldt label. In the pointed local Dirichlet geometry, intrinsic covers force the critical half-weight, a positive trace-class cocycle supplies `log n`, and Möbius extraction gives the exact scalar coefficient `Lambda(n)/sqrt(n)`. The obstruction moves to support selection and archimedean completion: the operation that kills mixed-prime shells leaves the positive cone, while canonical separated positive completions collapse to coboundary or invariant structures.

WP-067--WP-071 already identify the original topology warning: the exact shell anchor is unbounded in the natural rotation-invariant Hardy energy. WP-072--WP-074 show that this is not a no-go for positivity itself. Changing to a pointed local Dirichlet geometry makes boundary evaluation bounded, forces the `n^(-1/2)` normalization under covers, and produces positive trace-class defects of trace `log n`.

WP-075--WP-078 then isolate what that positive escape still does not solve. Shifted-resolvent digamma corrections form a scalar coboundary under multiplicative composition; invariant basepoint averaging supplies only the pointed and Haar extremes; and Möbius primitives have exact trace `Lambda(n)` and remain positive on prime powers but become nonzero trace-zero indefinite operators on mixed-prime integers. Exact finite selection is therefore present, but positivity is lost precisely where composite cancellation is imposed.

WP-378 returns to the most canonical analytic-disk alternative and sharpens the topology lesson. For `F_n(z)=log Phi_n(z)` in `H^2(D)`, the positive Gram kernel has genuine cross-prime terms but factorizes exactly into local Euler factors. Its diagonal depends only on `rad(n)`, assigns positive energy to mixed shells, and is independent of the prime-power exponent. The desired selector survives only at the boundary:

`F_n(1)=log Phi_n(1)=Lambda(n)`.

Boundary evaluation at `1` is unbounded in `H^2`; in particular `||F_(p^a)||_(H^2)` stays bounded as `p` grows while `F_(p^a)(1)=log p` diverges. Thus passing from radial data to the full analytic cyclotomic potential does create nontrivial positive incidence, but the canonical interior topology still separates that positivity from the exact Mangoldt readout.

The reusable principle is that **positivity, arithmetic incidence and selector regularity are independent gates**. A positive Hilbert geometry may contain real cross-prime information and still put the decisive arithmetic functional on a singular boundary. Conversely, a source-forced topology can regularize the selector while leaving mixed-prime support selection or archimedean coupling unresolved.

A surviving route must therefore derive a nonseparable finite--archimedean form, boundary/scattering geometry, higher cohomological mechanism or other source-forced topology in which the linear Mangoldt coefficient is obtained by a legitimate bounded/renormalized operation and the global sign is proved rather than inserted. Simply replacing the radial norm by canonical `H^2` positivity does not cross the boundary.

**Boundary.** WP-378 rules out the canonical unweighted Hardy Gram and fixed bounded `H^2` background readouts, not every weighted Hardy/Bergman/Dirichlet or singular boundary construction. The pointed Dirichlet results show one topology where the finite selector can be regularized, but they do not supply the completed Weil sign. No result here is a Weil-positivity proof or an RH criterion.