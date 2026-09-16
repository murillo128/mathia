# MI-023 — First-prime orientation requires supercritical residual control, not the canonical half-log boundary law

**Evidence level:** exact/source-specific synthesis from [PL-324](../../findings/PL-324-odd-sector-order-positivity-breaks-exactly-at-first-prime.md) through [PL-327](../../findings/PL-327-critical-log-holder-first-prime-reflection-threshold.md). The single-shift flip decomposition and canonical logarithmic-Laplacian boundary exponent are prior art as audited in the findings; no RH conclusion is claimed.

Once `2a` crosses `log 2`, the first active prime-power channel is the truncated translation by `b=log 2`. In the first-prime window this operator is exactly a flip between the two overlap edge strips, with spectrum `{-1,0,1}` and infinite-dimensional signed sectors. Odd parity removes the generic archimedean order obstruction until this event, but the active arithmetic channel is already indefinite. The question is which signed state the full Weil operator selects, not whether both signs exist.

PL-326 shows why the closed fixed-aperture endpoint law does not answer that question. With `a_delta=(log 2)/2+delta`, the reflection acts on a layer of width `2 delta`. Comparison families can share the same critical endpoint germ and satisfy the strongest pointwise fixed-aperture residual law while an antisymmetric bump inside the shrinking layer reverses the reflection sign. Absolute `L^2` or endpoint-potential smallness is insufficient because the positive critical reflection itself is only of order `delta/log(1/delta)`.

PL-327 identifies the sharp generic regularity threshold. The canonical critical profile has size

`B_delta(t)=C_delta (log(2a_delta/t))^(-1/2)`

and reflection reserve of order `|C_delta|^2 delta/L_delta`, where `L_delta~log(1/delta)`. If the residual `r_delta` has a logarithmic Hölder modulus of exponent `alpha>1/2` with

`(M_delta/|C_delta|) L_delta^(1/2-alpha) -> 0`,

then the residual is small enough in the moving layer to preserve the positive reflection. Equivalently it forces the `PL-326` scale `||r_delta||_2=o(|C_delta| sqrt(delta/L_delta))`.

The exponent `1/2` is exact. At `alpha=1/2`, one can insert a reflection-antisymmetric residual with uniformly bounded critical seminorm, unchanged leading boundary coefficient, `||r_delta||_2^2` of order `delta/L_delta`, and vanishing endpoint-potential energy, yet make the first-prime reflection negative. For every `alpha<1/2` the same mechanism dominates even more strongly. Thus the canonical `ell^(1/2)` logarithmic boundary regularity of the Dirichlet logarithmic Laplacian lies precisely at the non-orienting threshold.

This changes the live regularity target. A stronger Hölder exponent for the **whole state** is not plausible once the state genuinely carries the nonzero critical `ell^(1/2)` profile. The useful theorem must gain beyond `1/2` only after subtracting that leading profile, or directly suppress the reflection-antisymmetric component `P_- r_delta` by the actual completed-Weil eigen-equation/source coupling. Generic endpoint regularity at its canonical exponent cannot supply the missing arithmetic sign.

The reusable lesson is that boundary asymptotics and moving-layer orientation consume different currencies. A sharp leading germ can be fully determined while the destination sign remains controlled by a residual component living at the same squared-mass scale as the sign reserve. The decisive estimate must therefore be relative to the selected state's shrinking arithmetic channel, not merely optimal in the ambient boundary regularity class.

**Boundary.** The PL-326/PL-327 counterfamilies are not eigenstates and do not determine the sign of the actual ground branch. Supercritical residual control would orient only the first newly active prime channel; a separate theorem is still needed to connect that local orientation to the global lowest-eigenvalue/Weil-positivity mechanism. The exact surviving question is whether the actual completed-Weil equation forces such residual control or an equivalent signed suppression.