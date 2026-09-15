# MI-021 — The source-coupled endpoint equation closes the moving Green transfer without an extra trace hypothesis

**Evidence level:** exact line-specific closure from [PL-321](../../findings/PL-321-conditional-moment-green-transfer.md)--[PL-323](../../findings/PL-323-coercive-tail-comparison-closes-pointwise-flux.md), using the endpoint identity of PL-319. The comparison principle is standard nonlocal analysis; the completed-Weil consequence is the durable delta.

The exact logarithmic endpoint equation has the form

`F(Q)=2Q g(Q)-U(Q)+H_(Q0)g(Q)+c_(Q0)(Q)g(Q)`,  `U(Q)=int_(Q0)^Q g(P)dP`.

PL-320 originally closed the transfer conditionally on a finite limit of the singular translation remainder `H_(Q0)g`. PL-322 shows that this extra trace hypothesis is not needed to select the critical profile or its residual moment. Because the kernel in `H` is symmetric, the primitive of `H g` is only a boundary flux and tends to zero under the sharp `g(Q)=O(Q^-1/2)` envelope. Together with the convergent completed-Weil source trace `F(Q)->F_infinity`, this forces a unique primitive coefficient `C` with

`U(X)=2C sqrt(X)-F_infinity+o(1)`

and makes the improper moment of `m(Q)=g(Q)-C Q^-1/2` converge automatically. The same identity then yields

`2Qm(Q)+H_(Q0)m(Q) -> 0`.

PL-323 closes the remaining pointwise gate. Positivity of the jump kernel and the growing potential `2Q` give a maximum-principle comparison with `1/Q` as an explicit supersolution; from the residual equation and continuity one obtains

`Qm(Q) -> 0`.

No sign of `m` is required. PL-321 then transports the conditionally convergent residual moment through the moving Green kernel. Thus the analytic moving-diagonal obstruction that survived PL-314--PL-321 is closed for the actual source-coupled completed-Weil branch **without** an independent `H g` convergence theorem or absolute `L^1` control.

The remaining endpoint problem is no longer ambient regularity. The transferred rank-one datum still needs a rational-prime-specific sign, first-crossing or scalar compatibility theorem strong enough to exclude the RH-obstructing branch. The mechanisms in PL-322--PL-323 are universal real-variable/nonlocal geometry and do not supply that arithmetic orientation.

**Boundary.** This closure depends on the exact source equation, its convergent source trace, the sharp half-order boundary envelope, continuity and pointwise realization of the singular operator. It is not a generic theorem that every critical tail has `o(1/Q)` residual, and it is not an RH proof.