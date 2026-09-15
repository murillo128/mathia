# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Prove the singular endpoint remainder trace; conditional moments already close the Green transfer

**Linked intuitions:** `MI-016-weil-form-observability-is-stronger-than-moment-observability` through `MI-021-full-tail-volterra-trace-forces-leading-coefficient-and-pointwise-tail-law`.

PL-313 identifies the one-dimensional endpoint-moment channel by which a resolved physical corner reaches the obstructed regular outer direction. PL-314--PL-318 show why generic tail size, smoothness, critical Sobolev control and bounded logarithmic forcing do not control the moving Green atom.

PL-319 gives the exact endpoint-coordinate identity. PL-320 applies it before assuming a leading coefficient: if the actual tail `g(Q)->0`, the completed-Weil source trace `F(Q)` converges, and the local singular translation remainder `H_(Q0)g(Q)` converges, then the Volterra relation forces

`g(Q)=C Q^(-1/2)+m(Q)`,  `Qm(Q)->0`,

and the improper residual moment `int m(Q)dQ` converges.

PL-321 now removes the remaining absolute-`L^1` gap. For any locally integrable `m` with a convergent improper moment and `Qm(Q)->0`, the moving Green transfer converges to the rank-one endpoint value `e^-r M`. The pre-diagonal kernel supplies an explicit bounded-variation Abel weight, while `Qm->0` suppresses the moving/post-diagonal mass. Absolute residual integrability is not load-bearing.

Therefore the analytic endpoint-transfer frontier has collapsed to one local statement for the actual completed-Weil branch:

`H_(Q0)g(Q) -> H_infinity`.

If this holds, PL-320 generates the coefficient and residual laws and PL-321 completes the Green transfer. The previous alternative “prove absolute `L^1` or weaken the transfer theorem” is closed; only the singular remainder trace remains.

## Keep endpoint matching and arithmetic sign separate

The Volterra and Abel/Green mechanisms are real-variable endpoint analysis and are not prime-specific. Even after the boundary transfer is closed, the scalar endpoint moment can have either sign. Rational-prime specificity must enter through the actual completed-Weil mismatch/source relation, a first-crossing/order principle, or another sign-producing structure unavailable to matched locally finite shift systems.

A future argument should not treat the forced coefficient `C` or the now-closed conditional Green transfer as an arithmetic sign theorem. They establish that the endpoint information reaches the outer mode under one remaining trace hypothesis; they do not orient the RH-relevant scalar compatibility condition.