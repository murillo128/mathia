# MI-034 — Wang's diagonal source field is a Green potential of the Rodgers prime-power measure

**Evidence level:** exact representation synthesis from [VIS-271](../../findings/VIS-271-wang-fixed-alpha-prime-scale-mismatch.md) and [VIS-272](../../findings/VIS-272-wang-source-green-kernel-recovers-rodgers-prime-measure.md). The coefficient-level dictionary is exact; no shrinking-support pair-correlation asymptotic is inferred.

VIS-271 showed that a fixed positive Wang Fourier coordinate cannot be identified with a fixed Rodgers prime frequency: fixed Wang `alpha` tracks a prime scale growing like `T^alpha`, while a literal prime moves toward `alpha=0`. VIS-272 resolves the representation mismatch by changing to the source-native logarithmic coordinate before comparing formulas.

With

`q=log x/(2pi)`, `xi_n=log n/(2pi)`,

Wang's coefficient becomes

`a_n(e^(2pi q)) = Lambda(n)/sqrt(n) exp(-2pi|q-xi_n|)`.

Its diagonal source energy is therefore

`A(q)=int exp(-4pi|q-xi|) dmu(xi)`,

where

`mu = sum_(p,m) (log p)^2 p^(-m) delta_(m log p/(2pi))`

is exactly the weighted prime-power measure appearing in the Rodgers quadratic carrier. The exponential kernel is a one-dimensional Green kernel:

`(16pi^2-d_q^2) exp(-4pi|q-xi|)=8pi delta_xi`.

Hence, distributionally,

`mu=(16pi^2-d_q^2)A/(8pi)`.

For a sufficiently smooth decaying test `g`, the Rodgers prime-power quadratic term can equivalently be written

`C_2^pp(g)=-(1/(64pi^5)) int A(q)[16pi^2 g''(q)-g''''(q)] dq`.

The useful distinction is now exact. **The source-coordinate dictionary exists; the theorem-transfer uniformity does not yet.** A fixed Rodgers window around `q=xi_p` pulls back to a Wang window centered at `alpha_T=log p/log T` with width `O(1/log T)`. Recovering the fixed-source functional from Wang's short-interval theorem therefore requires asymptotic control in that shrinking regime, or an integrated adjoint formulation whose error survives the Green pairing. The Green identity itself does not authorize differentiating an asymptotic remainder.

**Boundary.** This is a representation theorem, not a pair-correlation theorem. It does not improve Wang's error term, establish the Rodgers lower-order term from Wang's statistic, or prove RH. The remaining question is whether Wang's explicit-formula/mean-square analysis can be made uniform for `alpha=O(1/log T)` families strongly enough to preserve the exact source dictionary after averaging.