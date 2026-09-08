# Xi-flow research lines

This file holds the current mathematical questions suggested by the durable Xi-flow intuitions. It is not a roadmap, task queue, status page, or history.

## Control q-scale source negativity at Fejer resolution, not by coarse roughness or bad-set measure

**Linked intuitions:** `MI-004-endpoint-prime-free-fourier-sector-is-volterra-triangular`, `MI-006-periodic-vieta-coordinates-diagonalize-the-nonlinear-heat-flow`, `MI-007-ultra-infrared-vieta-modes-should-be-quotiented-by-destination-energy`, `MI-008-gaussian-reference-localization-is-relatively-exact-but-not-global`, `MI-009-guarded-energy-can-enforce-static-real-divisor-feasibility`, `MI-010-endpoint-renormalization-is-source-fixed-before-discretization`.

XF-087--XF-100 close source extraction, endpoint renormalization, mesh sampling, full-prefix realization, and fixed-time periodic shadowing at the guarded low bandwidth, while showing that this entire prefix is prime-free. XF-101--XF-109 then move the sign question to the mass-preserving q-scale Toeplitz source and show that every nonpositive witness must carry macroscopic coefficient-Fourier mass outside a PNT-flat central window.

XF-110--XF-112 add strong global restrictions: only an `O((log q)^2/q)` fraction of the q-scale spectrum can be nonpositive; every nonpositive Rayleigh witness must use `Omega(q/(log q)^2)` coefficient coordinates; and every such witness must place fixed Fourier energy on a source-determined low-symbol set of normalized measure `O((log q)^2/q)` disjoint from the PNT-flat arc.

XF-113 proves that these restrictions are still not sufficient for positivity. An explicit Fejer-well control can satisfy the fixed `ell^1` budget, the exact `ell^2` dilution scale, central flatness, vanishing low-symbol measure, broad coefficient support, macroscopic noncentral concentration, and extreme lag roughness while its `(K+1)`-dimensional Toeplitz section retains a uniformly negative Rayleigh direction. The reason is scale mismatch: a bad set of measure `epsilon_a~(log a)^2/a^2` is still huge relative to Toeplitz resolution because `K epsilon_a~a(log a)^3 -> infinity`.

The live q-scale theorem must therefore control **source symbol geometry and depth after averaging at angular scale `1/K`**—equivalently the Fejer-scale negative wells actually visible to degree-`K` polynomial witnesses. A proof based only on total bad-set measure, coefficient sparsity, global `ell^2` dilution, central PNT flatness, or roughness cannot close the Toeplitz gate. The needed input must be Xi-specific and must rule out, shallow, or quantitatively constrain those Fejer-scale wells.

A prime-band route remains separate: crossing the first prime atom still requires a new distributional atomic source-to-grid interface and stability theorem before prime data can be invoked downstream.

## Force Xi-specific symmetry breaking, not merely a collective collision or concentration signal

XF-098--XF-100 show that even extensive collision participation can be invisible below the relevant symmetry frequency and that the current guarded trajectory can be shadowed by prime-free periodic data. XF-109--XF-113 show that q-scale negativity can survive every current coarse concentration gate through a matched Fejer-well control. These restrictions and countercontrols do not themselves prove `Lambda<=0`; they identify the precise symbol scale at which source-specific structure must enter.

A positive-`Lambda` contradiction must therefore connect the actual Xi transition to a source-faithful observable that defeats both the collision-invisible periodic controls and Fejer-scale negative-well controls. Collision count, density, bounded displacement, generic real-rooted heat flow, generic Toeplitz indefiniteness, or vanishing bad-set measure remain insufficient by themselves.

## Decide the low/q-scale versus prime-band fork explicitly

Staying below the first prime atom requires an Xi-specific coercivity theorem from archimedean/endpoint data and the mass-preserving q-scale source constraints already present there, now at Fejer resolution. Moving to `xi=Theta(1)` beginning at `lambda_2` requires handling distributional prime-power atoms and replacing the current perturbative point-sampling/shadow estimate.

The decisive test for either route is a matched periodic/source control at the exact bandwidth consumed by the destination theorem. Hidden high modes cannot be credited to a low-band argument, and a q-scale sign obstruction cannot be transferred to a prime-band model without a new interface theorem.

## Keep transition coercivity separate from transport at each declared scale

A successful source-to-grid theorem does not imply `Lambda<=0`, and a failed destination observable does not invalidate a source bridge proved in a weaker bandwidth. Future results should state explicitly whether they change source admission, transport stability, observable bandwidth, Fejer-scale symbol geometry, or transition coercivity, and should not transfer conclusions across those gates without a theorem.
