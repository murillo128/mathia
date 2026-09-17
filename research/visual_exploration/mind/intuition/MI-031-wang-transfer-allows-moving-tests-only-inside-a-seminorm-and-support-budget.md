# MI-031 — Wang transfer prices moving moment packets by a sharp seminorm and support budget

**Evidence level:** literature-backed/exact synthesis from [VIS-265](../../findings/VIS-265-wang-short-interval-support-law-blocks-bounded-window-edge-transfer.md), [VIS-266](../../findings/VIS-266-wang-proof-admits-norm-controlled-t-dependent-tests.md), and [VIS-267](../../findings/VIS-267-smooth-unit-carrier-packets-have-scale-sharp-wang-seminorm-budget.md).

A theorem stated for a fixed test function need not be useless for every moving packet. VIS-266 audits Wang's proof and extracts the dependence on the test seminorms. With support kept inside a fixed margin `[-lambda,lambda]`, `lambda<theta`, the short-interval pair-correlation argument controls a `T`-dependent family by an error of the form

`||g_T'||_inf/L + ||g_T||_inf[1/L + L^(-3/2) + T^(lambda-theta)L + 1/(HL)]`,

where `L=log T`.

The theorem therefore admits controlled motion and shrinkage, but VIS-267 shows that the relevant seminorm growth is not a free design parameter once a normalized moment carrier is fixed. A smooth compact packet of width `b`, zero mass, vanishing even moments through order `2m-2`, and unit `2m`-th moment necessarily obeys

`||g_b||_inf \gtrsim b^(-(2m+1))`,

`||g_b'||_inf \gtrsim b^(-(2m+2))`.

Scaled smooth profiles attain these exponents, so this is the sharp width cost of the carrier itself rather than a bad packet choice. Substituting it into Wang's derivative term gives the sufficient and scale-sharp proof-interface requirement

`1/(L b^(2m+2)) -> 0`.

For logarithmic width `b=L^(-q)`, one must have `q<1/(2m+2)` within this argument. Thus the quadratic moment carrier has the explicit gate `q<1/4`, while the quartic carrier has `q<1/6`. The older generic estimate `q(A+1)<1` is recovered with the unavoidable normalized-moment amplitude exponent `A=2m+1`.

The correct transfer ledger therefore has three independent entries. First, Fourier support must remain a fixed distance inside the available edge `theta`; moving the support edge toward `theta` is not covered by this uniformity. Second, the normalized carrier itself imposes a sharp amplitude/derivative seminorm cost as its width shrinks. Third, the resulting theorem remainder must still be smaller than the arithmetic signal one wants to resolve.

This matters for visual/experimental packet design: one should search within the theorem-valid moving family rather than discard all adaptive packets, but no visual concentration is evidence until its support, unavoidable seminorm cost and signal-to-error coordinates are all audited. Higher moment order makes the admissible shrinking window strictly narrower even before source selectivity enters.

**Boundary.** VIS-267 is sharp for the current smooth compact normalized-moment packet class and Wang proof interface; it is not a theorem that the actual pair-correlation asymptotic fails beyond `q=1/(2m+2)`. VIS-265--VIS-267 do not extend Wang's support edge, validate bounded physical source windows, produce four-level covariance, or prove that a prime-sensitive residual survives.