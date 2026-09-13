# MI-013 — Autocorrelation shell energy is exactly a weighted two-sample crowding problem

**Evidence level:** exact for the autocorrelation-taper subclass through [VIS-203](../../findings/VIS-203-autocorrelation-tapers-make-exact-difference-shells-noncancelling.md), the fixed-scale exact-shell multiplicity theorem of VIS-204, and [VIS-205](../../findings/VIS-205-dangerous-shell-energy-pair-crowding.md). No theorem yet makes the resulting pair-crowding mass vanish for the prime-ratio weights or improves the VIS-202 method threshold.

For a shifted autocorrelation taper, the centered Fourier kernel has a common linear phase and nonnegative amplitude. Prime-ratio coefficients can therefore be written `c_lambda=e^(iH lambda/2)b_lambda` with `b_lambda>=0`. Grouping the finite-start energy by exact differences produces nonnegative shell amplitudes

`B_xi = sum_(lambda-mu=xi) b_lambda b_mu >= 0`.

Thus multiplicity inside one exact shell reinforces rather than cancels.

VIS-204 adds a fixed normalized-scale multiplicity cap: every dangerous nonzero shell has at most four ordered representations for sufficiently large `y`. VIS-205 then removes the remaining representation ambiguity. With `R=sum b_lambda^2`, `nu(lambda)=b_lambda^2/R`, and

`Q(A)=sum_(lambda!=mu, 0<|lambda-mu|<=A b_y) nu(lambda)nu(mu)`,

the dangerous exact-shell energy satisfies

`Q(A) <= S(A)/R^2 <= 4 Q(A)`.

So after nonnegative shell aggregation and bounded exact multiplicity, **the fixed-scale shell-energy problem is, up to a universal factor, exactly the probability that two independent energy-weighted frequency samples form a dangerous close pair.**

This is strictly weaker than the previous nearest-neighbor resource. If

`C(A)=sum_(delta_lambda<=A b_y) nu(lambda)`,

then `Q(A)<=C(A)`, so `D_v=o(y^2)` still suffices, but the converse need not hold. A heavy frequency can have only extremely light close partners: it is fully charged by `C` but contributes little to `Q`. The shell-energy route can therefore succeed even when the stronger one-sided crowding criterion is unavailable.

At the dangerous `|xi|=O(y^-2)` scale, subquadratic start windows do not attenuate these shells. The cheapest surviving positive-taper target is now a **weighted pair-incidence theorem** for bounded-determinant prime-product collisions, not a maximum spacing theorem and not a proof that close neighbors are absent.

**Research consequence.** Estimate `Q(A)` directly from the explicit taper weights, or construct a source-valid lower bound showing it remains macroscopic. Only if that fails should the line pay for a genuinely signed/complex taper or cross-shell interference mechanism.

**Boundary.** The comparison is for fixed normalized windows and the nonnegative autocorrelation class. Growing shell windows and sign-changing centered tapers remain separate.
