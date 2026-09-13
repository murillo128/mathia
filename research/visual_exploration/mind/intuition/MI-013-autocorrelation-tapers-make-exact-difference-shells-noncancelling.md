# MI-013 — Fixed-scale autocorrelation shell energy is dilute even when one-sided crowding is not controlled

**Evidence level:** exact for the autocorrelation-taper subclass through [VIS-203](../../findings/VIS-203-autocorrelation-tapers-make-exact-difference-shells-noncancelling.md), VIS-204, [VIS-205](../../findings/VIS-205-dangerous-shell-energy-pair-crowding.md), and [VIS-206](../../findings/VIS-206-fixed-scale-pair-crowding-bounded-degree.md). The conclusion is for fixed normalized collision width `A` in the strictly subcritical regime; growing `A(y)`, the full sinc-weighted intermediate shell range, and sign-changing tapers remain open.

For a shifted autocorrelation taper, the centered Fourier kernel has a common linear phase and nonnegative amplitude. Prime-ratio coefficients can be written `c_lambda=e^(iH lambda/2)b_lambda` with `b_lambda>=0`, so exact-difference shell amplitudes are nonnegative and multiplicity reinforces rather than cancels.

VIS-204 bounds every dangerous fixed-scale exact-shell multiplicity by four. VIS-205 then identifies the correct normalized resource: with `R=sum b_lambda^2`, `nu(lambda)=b_lambda^2/R`, and

`Q(A)=sum_(lambda!=mu, 0<|lambda-mu|<=A b_y) nu(lambda)nu(mu)`,

the dangerous exact-shell energy satisfies

`Q(A) <= S(A)/R^2 <= 4 Q(A)`.

This is strictly weaker than the one-sided nearest-neighbor mass `C(A)`. VIS-206 proves that the distinction is enough to cross the old fixed-scale obstruction. For fixed `A`, every dangerous prime-ratio frequency lies at top prime scale and has only `O_A(1)` dangerous neighbors: fixing one ratio turns each bounded-determinant relation into a one-dimensional Diophantine progression whose step is already comparable with the full prime box.

At the same time each dangerous vertex has

`nu(lambda) <<_(A,alpha,v) H (log y)^2/y^2`.

Under `H log y/y -> 0`, this tends to zero. Bounded local degree therefore gives

`Q_(y,H)(A) << H (log y)^2/y^2 -> 0`,

and hence `S_(y,H)(A)=o(R_v(y,H)^2)` for every fixed `A`.

So the square-root-log barrier in VIS-202 is not a barrier for the weaker two-sample shell resource. It belongs to the stronger one-sided crowding quantity and the proof architecture used to control it. **At fixed normalized scale, the actual positive shell energy is already dilute because no dangerous vertex can combine large normalized mass with large local degree.**

The remaining positive-taper problem begins when the collision window widens. If `A=A(y)` grows, the determinant difference range, lower bound on participating primes and local degree can all deteriorate. The next theorem should quantify that deterioration far enough to sum the sinc-weighted intermediate shells up to the dephasing scale, or identify where a genuinely signed/complex taper becomes necessary.

**Boundary.** VIS-206 proves neither `C(A)->0` nor `D_v=o(y^2)`, and does not contradict the VIS-202 method threshold. It gives no uniform bound for growing `A(y)` and no complete finite-start theorem below the coarse Hilbert horizon.
