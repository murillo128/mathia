# MI-044 — The quartic floor survives common prefilters; unrestricted joint filters erase the oscillation

**Evidence level:** exact/literature-backed synthesis from [MC-323](../../findings/MC-323-varying-modulus-prime-halasz-montgomery-obstruction.md) through [MC-332](../../findings/MC-332-unrestricted-mode-dependent-weights-erase-character-oscillation.md). The incidence and fixed-modulus arguments compress different source information; none proves a quartic lower bound for Möbius cancellation itself.

The exponent four is now a method boundary seen from several distinct places in the reciprocal endpoint package. MC-323--MC-327 obtain it by charging common source primes through conductor/incidence geometry and show that saturation forces essentially all logarithmic source mass into the half-loaded Hamming band. MC-328 then proves that low endpoint-polynomial Fourier degree cannot resolve that band. Independently, MC-329 reaches the same floor from the full fixed-common-modulus character family through a prime Halász--Montgomery `ell^2` bias-energy estimate.

The fixed-modulus route is itself rigid at the exponent. At Burgess/Halász--Montgomery order `k`, the neutral power threshold is `alpha<4k/(k+1)`; at `alpha=4` a positive residual exponent remains, and no fixed `alpha>4` is available for any `k`. Growing `k` can approach four from below but cannot cross it as a fixed-power theorem. Thus the coincidence with the incidence floor cannot be repaired by moving the order inside the same exponent geometry.

MC-330 localizes where signed information would have to enter. Once the character family has already been compressed to its total bias energy, arbitrary signed linear statistics and arbitrary quadratic kernels are controlled by the same Hilbert-space norm, and the exact reciprocal endpoint saturates that normalized bound. Signs, off-diagonal couplings, endpoint-matched projectors, and low rank introduced **after** `ell^2` compression are therefore not new resources.

MC-331 removes the most immediate upstream repair. Let one common complex coefficient vector `w=(w_r)` be applied to the shell primes before the character-family transform. At the exact one-defect endpoint,

`sum_a |T_w(a)|^2 = 2^R sum_s |W_s|^2 <= (2^R A/R) sum_r |w_r|^2`,

and deleting the principal character leaves the same top operator norm. The unweighted shell already attains this norm up to the asymptotically negligible principal-direction loss. Schlage-Puchta's prime Halász--Montgomery theorem is uniform in exactly these coefficients and charges them only through `sum |w_r|^2`, so the coefficient norm cancels between endpoint demand and analytic control. Optimizing a mode-independent prefilter cannot change the quartic power balance.

This includes every translation-invariant convolution on the character cube: Walsh diagonalization turns it into scalar weighting of the source sign cells, hence into the same common-coefficient class. Hamming adjacency, radial filters, cube Laplacians, noise operators, and arbitrary Walsh multipliers do not evade the boundary merely by being applied before the final energy sum.

MC-332 shows that the opposite extreme—arbitrary mode-dependent coefficients—is not a stronger escape but a degenerate one. For a general matrix `W=(w_(chi,r))`, rowwise Cauchy gives

`sum_chi |sum_r w_(chi,r) chi(r)|^2 <= A sum_(chi,r) |w_(chi,r)|^2`,

and the constant is exact because `w_(chi,r)=c_chi conjugate(chi(r))` removes the character phase pointwise. Once each mode can choose its own matched input, the oscillation is cancelled before any large-sieve theorem can exploit it.

The reciprocal endpoint makes the admission test stronger. Its character-evaluation matrix on the `R` one-defect source cells has rank exactly `R`, although there are `2^R-1` nonprincipal modes. Taking that rank-`R` matrix itself as the coefficient matrix dephases every endpoint mode simultaneously. Thus **low rank relative to the mode population does not exclude the bad matched filter**. What matters is whether the admissible coefficient geometry contains the evaluation representation it is supposed to test, not rank in isolation.

The surviving linear resource is therefore a genuinely **restricted joint prime--mode class**: richer than one common vector, but constrained in a source-natural way that excludes or quantitatively penalizes `conjugate(chi(r))`, the endpoint evaluation matrix, and asymptotically equivalent dephasing sequences. The analytic theorem must use that restriction essentially; if it reduces to a common-vector `ell^2` norm, MC-331 applies, while if it reduces to independent rowwise `ell^2`, MC-332 applies. Alternatives are a genuinely higher-order/nonlinear invariant, a prime-character theorem with different exponent geometry, or a different endpoint/source representation.

The reusable principle is about **admissible coupling geometry**, not simply whether a transform is placed before or after compression. Moving an operator upstream buys nothing when every mode still shares one vector; granting arbitrary joint freedom buys too much and destroys the oscillatory signal. A useful intermediate class must preserve cross-mode coupling while forbidding exact phase cancellation, with the price of that restriction visible in the analytic estimate.

**Boundary.** MC-331 assumes the same coefficient vector feeds every character. MC-332 assumes arbitrary rowwise mode dependence and shows that rank at most `R` is already too permissive at the exact endpoint. Neither rules out structured mode dependence defined by locality, factorization, shared latent parameters, algebraic restrictions, bilinear/tensor relations, or another source-derived class that excludes the matched filter. Equality of the quartic exponents remains a diagnosis of the present architectures, not a theorem that exponent four is optimal for the underlying Möbius problem.