# MI-045 — Poisson-width packing can fake maximal coordinatewise phase codes

**Evidence level:** exact matched-control synthesis from [NB-174](../../findings/NB-174-source-resolution-approximate-linear-complexity.md), [NB-178](../../findings/NB-178-coordinatewise-phase-codes-recover-linear-source-complexity-certificates.md), and [NB-179](../../findings/NB-179-poisson-separated-dipoles-realize-maximal-coordinatewise-phase-codes-without-arithmetic.md).

NB-178 shows that coordinatewise capped-transport probes can certify large approximate source complexity when their response matrix has many `sqrt N` singular values. That is a genuine escape from the compactness ceiling of the jointly Hilbert Euler witness in NB-177, but it is not yet an arithmetic discriminator.

NB-179 constructs the decisive control. Put `N` disjoint signed dipoles on `2N` points separated by one capped-Poisson width and choose explicit scalar Lipschitz probes. Their response is exactly

`A=X H_N`,

with `H_N` a Sylvester Hadamard matrix. Every singular value is `X sqrt N`, and the NB-174 approximate complexity of the resulting finite range is exactly

`N(X-epsilon)_+^2`.

The coordinatewise nuclear certificate is therefore sharp on a source-free packing model. The effect comes from the generic ability of the capped metric space to store one sign bit per resolved dipole and reuse those bits across independent scalar probes. No Euler product, prime phase or Nyman generator is required.

This changes what a useful phase-code theorem must establish. The response matrix cannot be interpreted in isolation; the probe family and the admissible template range are part of the source claim. A source-selective certificate must either restrict probes to a uniformly generated arithmetic class, show that the actual Nyman range cannot be reproduced by Poisson-separated generic dipoles, or survive a matched control that has the same capped-transport packing geometry.

The durable distinction is between **dual expressivity** and **source selectivity**. Enlarging the dual class can remove a witness-induced compactness ceiling, but an expressive enough dual may then certify complexity that is already present in the ambient metric geometry. The matched control must be upgraded at the same time as the witness.

**Boundary.** NB-179 does not show that natural Nyman templates contain the synthetic dipoles, does not disprove large `mathfrak L_T(epsilon)`, and does not give logarithmic Euler rescue. It only proves that unrestricted coordinatewise Hadamard response is nonselective. The arithmetic problem begins after that generic packing capacity has been matched or factored out.