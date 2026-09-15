# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Prove the completed-Weil boundary expansion strongly enough to trigger the source-trace Tauberian mechanism

**Linked intuitions:** `MI-016-weil-form-observability-is-stronger-than-moment-observability`, `MI-017-fixed-order-shift-differentiability-survives-without-uniform-half-sobolev-control`, `MI-018-stretched-volterra-amplitude-selection-is-an-endpoint-matching-problem`, `MI-019-moving-green-atoms-require-tail-anti-concentration-beyond-weighted-l1`, `MI-020-half-derivative-is-the-generic-moving-diagonal-sobolev-threshold`.

PL-297--PL-312 close the fixed-order state-side and limiting outer gates. PL-313 identifies the compressed-corner communication channel: for compact physical mismatch the finite-`s` Green transfer reaches the unique obstructed regular outer direction through the scalar endpoint moment `M_±`.

PL-314 isolates the moving-diagonal obstruction. The stretched Green measure has an atom at fixed `q=r`, corresponding to physical logarithmic distance `Q=r/s`, so weighted `L^1` tail control can miss sparse packets exactly where the observer samples. PL-315--PL-316 show that smoothness, all finite logarithmic moments, every subcritical Sobolev gain and even critical zero-extension `H^{1/2}` can coexist with order-one normalized transfer along selected scales. PL-317 shows that any fixed supercritical zero-extension gain suppresses the moving sample, while PL-318 shows that bounded logarithmic zero-order forcing, even arbitrarily small after scaling, does not.

PL-319 now identifies a source-coupled route that is strictly weaker in spirit than demanding generic supercritical regularity. For a right-endpoint residual `m(Q)`, the one-dimensional logarithmic Laplacian has the exact coordinate identity

`F(Q)=2Qm(Q)-int_(Q0)^Q m(P)dP+H_(Q0)m(Q)+c_(Q0)(Q)m(Q)`.

Whenever `m in L^1(dQ)` and the singular translation remainder satisfies `H_(Q0)m(Q)->0` — `W^{2,1}` is one sufficient condition, not the asserted endpoint class — this becomes

`F(Q)=2Qm(Q)-M+o(1)`.

Hence existence of the endpoint source trace `lim F(Q)` is equivalent to the exact moving-tail law `Qm(Q)->0`. The Tauberian reverse uses integrability: a nonzero limit of `Qm(Q)` would force a nonintegrable `1/Q` tail.

The actual completed-Weil eigen-equation already supplies the **convergent source trace** after the boundary state is placed in the logarithmic-Laplacian representation: fixed translations, the continuous archimedean term and the scalar state all have one-sided endpoint limits. The sparse PL-315--PL-318 counterexamples fail exactly here; bounded source size was insufficient, while trace convergence is structural.

The remaining theorem is now narrower. One must prove the leading logarithmic-Laplacian boundary matching

`u(x_Q)=C Q^(-1/2)+m(Q)`

for the actual completed-Weil branch and show that the residual lies in a class strong enough for `m in L^1` and `H_(Q0)m(Q)->0`, or prove those two consequences directly. The canonical `Q^(-1/2)` profile itself is compatible with a finite source trace because the `2Qm` and accumulated-mass terms cancel at leading order; the Tauberian identity applies only after that leading coefficient has been matched.

Once those residual gates are crossed, `Qm(Q)->0` and the PL-314 rank-one limit follow automatically from the eigen-equation. The moving-diagonal anti-concentration condition is therefore no longer an independent conjectural input. Only then should the scalar `M_±` balance be used as the arithmetic endpoint.

## Prove a rational-prime-specific sign or first-crossing law only after stable matching

The Green-kernel transfer, universal stretched profile, logarithmic source-trace identity and exact regular inverse are geometric. The scalar endpoint moment can have either sign. Rational-prime specificity must enter through the actual mismatch/source relation or selected singular amplitude after the finite-`s` matching theorem **and the PL-319 residual gate** are proved.

A useful sign theorem must come from the actual rational-prime eigen-equation: a boundary-weighted lower law, source-specific oscillation or maximum principle, an absolute-value defect identity, a source-sensitive matching condition, or another order structure unavailable to matched locally finite shift systems.

## Keep outer geometry, source-trace convergence, residual class and arithmetic sign separate

PL-313 closes the geometric rank-one channel. PL-314--PL-318 show that weak integrated control, generic critical regularity and bounded forcing do not pass through a singular moving observation. PL-319 changes the frontier by showing that **convergent source trace plus an integrable/Dini residual does**: the desired pointwise tail law is then a Tauberian consequence rather than a separate regularity assumption.

Future work should therefore not spend effort proving another generic norm bound on the forcing. The live analytic obligations are the leading `Q^(-1/2)` coefficient matching and a residual theorem sufficient to make the singular translation remainder vanish. Those obligations are distinct from the later arithmetic sign/first-crossing mechanism.