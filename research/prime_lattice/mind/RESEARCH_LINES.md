# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Prove the singular endpoint remainder trace or weaken the absolute-transfer gate

**Linked intuitions:** `MI-016-weil-form-observability-is-stronger-than-moment-observability` through `MI-021-full-tail-volterra-trace-forces-leading-coefficient-and-pointwise-tail-law`.

PL-313 identifies the one-dimensional endpoint-moment channel by which a resolved physical corner reaches the obstructed regular outer direction. PL-314--PL-318 show why generic tail size, smoothness, critical Sobolev control and even bounded logarithmic forcing do not control the moving Green atom.

PL-319 gives the exact endpoint-coordinate identity. PL-320 applies it **before** assuming a leading coefficient. If the actual tail `g(Q)` satisfies `g(Q)->0`, the completed-Weil source trace `F(Q)` converges, and the local singular translation remainder `H_(Q0)g(Q)` also converges, then the Volterra relation forces

`g(Q)=C Q^(-1/2)+m(Q)`,

`Q m(Q)->0`,

and the improper integral `int m(Q)dQ` converges. Thus existence of the `Q^(-1/2)` coefficient and the moving-diagonal pointwise law are no longer independent analytic gates.

For the actual completed-Weil branch, the source equation already supplies the convergent source trace and existing boundary theory gives `g(Q)=O(Q^(-1/2))`. The remaining pointwise matching theorem is therefore the local statement

`H_(Q0)g(Q) -> H_infinity`.

This does **not** imply the absolute residual integrability used in the sufficient transfer theorem PL-314. The explicit control `m(Q)=sin Q/(Q log Q)` has `Qm->0`, a convergent improper moment and vanishing singular remainder, but is not in `L^1(dQ)`. The current analytic frontier is consequently two-pronged: prove absolute `L^1` for the actual completed-Weil residual from source-specific structure, or strengthen the PL-314 rank-one Green transfer so that the conditionally convergent moment plus `Qm->0` suffices.

## Keep endpoint matching and arithmetic sign separate

The Volterra mechanism is real-variable endpoint analysis and is not prime-specific. Even after the boundary transfer is closed, the scalar endpoint moment can have either sign. Rational-prime specificity must enter through the actual completed-Weil mismatch/source relation, a first-crossing/order principle, or another sign-producing structure unavailable to matched locally finite shift systems.

A future argument should not treat the newly forced coefficient `C` as an arithmetic sign theorem. PL-320 selects the asymptotic profile from source-trace consistency; it does not determine the RH-relevant orientation of the final scalar compatibility condition.