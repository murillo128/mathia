# MI-021 — A convergent full-tail Volterra trace forces both the boundary coefficient and the pointwise moving-tail law

**Evidence level:** exact conditional reduction from [PL-320](../../findings/PL-320-source-trace-full-tail-volterra-matching.md), using the endpoint identity of PL-319.

For the logarithmic endpoint coordinate `Q`, write the full tail profile `g` in the exact form

`F(Q)=2Q g(Q)-U(Q)+H_(Q0)g(Q)+c_(Q0)(Q)g(Q)`,

`U(Q)=int_(Q0)^Q g(P)dP`.

Assume `g(Q)->0`, the source trace `F(Q)->F_infinity`, and the local singular translation remainder `H_(Q0)g(Q)->H_infinity`. Since `c_(Q0)(Q)` has a finite limit, the remainder

`R(Q)=F(Q)-H_(Q0)g(Q)-c_(Q0)(Q)g(Q)`

converges and the equation becomes `2Q g-U=R`.

The right variable is `W(Q)=U(Q)/sqrt(Q)`. Exactly,

`W'(Q)=R(Q)/(2 Q^(3/2))`.

Because the right side is integrable, `W(Q)->2C`. Solving back gives `sqrt(Q)g(Q)->C`. More importantly, with `m(Q)=g(Q)-C Q^(-1/2)`, the exact remainder formula makes the limiting `R_infinity/(2Q)` terms cancel, so

`m(Q)=o(1/Q)`,

hence `Qm(Q)->0`. The improper moment `int m` also converges.

This changes the endpoint gate: **the leading `Q^(-1/2)` coefficient and the pointwise moving-diagonal anti-concentration are consequences of one convergent singular-remainder trace**, rather than two separate matching assumptions. For the actual completed-Weil state, PL-319 already supplies convergence of the full source trace and the literature supplies `g=O(Q^(-1/2))`; the remaining pointwise condition is convergence of `H_(Q0)g`.

Absolute integrability remains independent. The smooth control `m_*(Q)=sin Q/(Q log Q)` has `Qm_*->0`, convergent improper integral and `H m_*->0`, but `int |m_*|=infinity`. Thus PL-320 does not by itself activate every dominated-convergence step in PL-314.

**Boundary.** The Volterra deduction is universal endpoint analysis, not an arithmetic sign mechanism. Closing the analytic transfer still requires either source-specific absolute `L^1` for the actual residual or a proof that the Green transfer tolerates the weaker conditional moment; the later rational-prime sign/first-crossing problem remains separate.