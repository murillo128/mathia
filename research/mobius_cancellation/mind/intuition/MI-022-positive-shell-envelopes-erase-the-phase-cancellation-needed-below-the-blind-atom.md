# MI-022 — Positive shell envelopes erase the phase cancellation needed below the blind atom

**Evidence level:** proved for the flat Christoffel shell polynomial and the positive-real / raw circle-norm extraction routes of MC-269--MC-272. No impossibility is claimed for signed or phase-sensitive coefficient extraction.

MC-269 reduces the live blind-support problem to one distinguished flat source vector. MC-270 shows why coefficient-uniform operator control is already too expensive: the row-norm floor reaches the scale of one blind atom. MC-271--MC-272 now show that preserving the flat vector is still not enough if the remaining shell information is immediately replaced by a positive scalar envelope.

For the shell-energy polynomial `G(z)=sum_j F_j z^j`, all coefficients are nonnegative and `F_0=Z^2`. The sparse source forces substantial high-degree mass and Parseval forces exponentially large total mass. Consequently every positive-real coefficient majorant `z^{-t}G(z)` stays at or above the blind scale. Moving to complex circles does not help if one takes an absolute `L^p`/Hardy norm before extracting the coefficient: the raw Cauchy certificate `r^{-t}||G(re^{i theta})||_p` also remains above `Z^2` for every radius.

The lost resource is therefore more specific than “flat-vector structure.” It is the **signed/angular cancellation in the exact target coefficient or off-diagonal quadratic form**. Any proof that first collapses the shell polynomial to a monotone positive majorant or absolute circle norm has already spent the only scale that could beat a single blind row.

The live route must keep phase until after the target coefficient is isolated: estimate the Fourier/Cauchy coefficient with cancellation, control the signed off-diagonal term of `<1_Z,A^*A1_Z>` directly, or find another source-specific structured coefficient class whose relaxation remains strictly below `Z^2`.

**Boundary.** MC-271--MC-272 do not prove that the desired cancellation exists or that every analytic generating-function method fails. They close only routes whose final estimate is an absolute positive envelope of the whole shell polynomial.