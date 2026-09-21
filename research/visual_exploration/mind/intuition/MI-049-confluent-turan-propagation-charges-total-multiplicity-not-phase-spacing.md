# MI-049 — Confluent Turán propagation charges total multiplicity, not phase spacing

**Evidence level:** exact/classical synthesis from [VIS-350](../../findings/VIS-350-confluent-turan-total-multiplicity.md), applied to the confluent Wang-tail representation VIS-349. The measurable Turán--Nazarov theorem is classical; the line-specific content is the coalescing-frequency limit and the resulting budget for Wang's finite interacting tail.

For a nonzero confluent exponential polynomial

`F(x)=sum_b Q_b(x) exp(-i b x)`

with distinct phases and total multiplicity `N=sum_b(deg Q_b+1)`, measurable Turán--Nazarov propagation holds with exponent `N-1`:

`sup_I |F| <= (A |I|/|E|)^(N-1) sup_E |F|`.

No minimum phase spacing enters. The result follows by approximating each polynomially weighted exponential by a cluster of ordinary exponentials and passing the classical measurable inequality through the uniform confluent limit.

Applied to the VIS-349 tail `E_(q,X)`, one-extra-order attenuation on `J_X subset I_X` forces

`X H_X/D_(q,X) <= (A |I_X|/|J_X|)^(N_X-1)`,

where `H_X=sup_(I_X)|E_(q,X)|` and `N_X` is the total confluent multiplicity. Thus phase coalescence does not create a separate local-concentration loophole. Its only possible advantage is indirect: it may make the entire reference norm `H_X` small relative to the underlying moment data.

The durable split is therefore **propagation versus norming**. Propagation is already priced by total dimension and window ratio; the unresolved finite-bank resource is the coefficient-to-function conditioning that determines `H_X` before the local window is examined.

**Boundary.** VIS-350 gives no uniform lower bound for `H_X` in raw Wang coefficients. Phase collisions, coefficient cancellation and moving systems may still lower the reference norm through genuine conditioning. The result only says that such a gain is not an unpriced failure of measurable Turán propagation.