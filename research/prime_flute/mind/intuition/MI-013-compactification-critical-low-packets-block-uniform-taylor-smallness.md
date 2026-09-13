# MI-013 — Compactification-critical low packets survive in arithmetic-dependent interior boundary geometries

**Evidence level:** exact for the unprojected compactified cuff-cell form through [PF-322](../../findings/PF-322-physical-low-packets-retain-critical-compactified-transverse-energy.md), with the seam-artifact loophole removed by [PF-323](../../findings/PF-323-interior-critical-low-packets-avoid-the-cuff-seam.md) and the outgoing-boundary geometry sharpened by [PF-324](../../findings/PF-324-critical-packet-seam-distance-remembers-consecutive-prime-gap-ratio.md). This is still not a lower bound for the completed shear-deleted intrinsic `L/H` angle; the pant quotient, seam-energy normalization, physical projections and common completion may cancel the exhibited component.

The seam scale `s_n` tends to zero, and PF-233 writes the compactified transverse form schematically as `T_(a_n)=s_n^2 T_tilde_n`. PF-322 shows that `s_n` is not a uniform small parameter on the full fixed physical-low sector: a zero-mean Dirichlet packet can follow the receding high-weight region and retain order-one scaled energy.

PF-323 shows this is not caused by centering the packet at the quotient seam. Fix `0<lambda<1` and choose the unique interior point

`s_n cosh tau_(n,lambda)=lambda`.

On `x=tau-tau_(n,lambda)`, every fixed window `|x|<=R<log(1/lambda)` eventually lies strictly inside the cuff and

`s_n cosh(tau_(n,lambda)+x) -> lambda e^x`

uniformly on bounded `x`. The fixed-band packet therefore retains strictly positive limiting scaled transverse energy on an interior window.

PF-324 identifies the actual outgoing boundary seen from this critical coordinate. If

`r_n=h_(n+1)/h_n` and `D_(n,lambda)=ell_n/2-tau_(n,lambda)`, then exactly

`e^D = coth(h_n/4) s_n/(lambda+sqrt(lambda^2-s_n^2))`,

and hence

`D_(n,lambda)=log((1+r_n)/lambda)+o(1)`,

while the terminal scaled compactification coefficient satisfies

`s_n cosh(ell_n/2)=1+r_n+o(1)`.

Because `r_n=(g_(n+1)/g_n)(1+o(1))`, Pintz's consecutive-prime-gap-ratio theorem supplies subsequences with `r_n->0` and `r_n->infinity`. The same interior critical packet therefore sits in two genuinely different arithmetic boundary geometries: the outgoing seam stays at the finite limiting distance `log(1/lambda)` on one subsequence and escapes every fixed critical window on another.

So moving away from the seam does more than preserve the critical obstruction: it exposes a **source-dependent terminal parameter before quotient/projection**. There is no single gap-independent finite-pant boundary model to insert after the local limit. A uniform proof of the final direct-angle estimate must work in both the finite-boundary and escaping-boundary regimes.

The escaping-seam subsequence is especially diagnostic. Any cancellation explained only by a bounded-distance interaction with the outgoing seam cannot be invoked uniformly there. If the completed physical angle still gains the required superlinear power, the suppressing mechanism must be genuinely nonlocal in the finite-pant completion, seam normalization or `L/H` projection. If the two regimes instead produce different completed asymptotics, that would be a concrete route by which ordered prime-gap information survives past the local geometry.

**Boundary.** PF-324 proves arithmetic dependence of the input boundary position/scale, not of the completed angle, spectrum or any RH-relevant invariant. The packet is not compactly supported in the fixed interior window, and the independent conditional channel `T_H` remains separate. No conjectural prime-gap distribution is used beyond the audited extreme-ratio subsequences.
