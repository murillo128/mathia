# Prime-circle research lines

This file holds the current mathematical questions suggested by the durable prime-circle intuitions. It is not a roadmap, task queue, status page, or history.

## Move below the quantitative square-zero defect without collapsing to the Fejer power quotient

**Linked intuitions:** `MI-012-finite-scalar-cross-shell-fusion-is-closed-under-classical-packet-algebra` through `MI-018-quadratic-square-zero-defect-is-fejer-autocorrelation-and-forgets-source-phase`.

PC-295 closes the complete absolute singular spectrum under diffuse averaging, PC-296 closes raw eigenvalues, and PC-297 identifies their common fixed-scale explanation: the normalized boundary-log matrix approaches a universal square-zero class of norm `1/2`, so every fixed positive pseudospectral scale is classicalized.

PC-298 makes the approximation quantitative. Under the same diffuseness regime, there is a square-zero `S_q` with deterministic norm `1/2+O(q^-3)` and

`E ||T_q-S_q||_op <= C r_q`,

where

`r_q = delta_q^(1/3) + delta_q^(1/2) log q + (log q)/N`.

Consequently, for every shrinking pseudospectral scale `epsilon_q` with `r_q/epsilon_q -> 0`, the rescaled `epsilon_q`-pseudospectrum still converges to the universal square-zero disk. The surviving one-profile information must therefore live at or below the actual defect scale `r_q`.

PC-299 identifies the first intrinsic low-mode defect there. If `C=Z^*X` is the cross-Gram matrix, then `A^2=X D C D Z^*`; source-averaged quadratic loop closure is exactly a Fejer autocorrelation. The opposite-mode channel has universal floor `1/N` plus a positive weighted sum of `|muhat(mt)|^2`, and the symmetric Frobenius energy has the analogous universal baseline plus source power. For primes, the excess is a classical mean-square exponential-sum packet.

This narrows the subdefect route again. Resolving `O(r_q)` is not enough if the observable immediately squares and averages the cross-Gram coefficients: that quotient discards Fourier phase and lands in the classical additive prime-pair/exponential-sum interface. A surviving prime-specific construction must preserve phase or higher joint structure, use source-coupled left/right relations, noncommuting multiple profiles, cross-level structure, or otherwise prove information beyond the Fejer power spectrum.

## Keep singular strength, loop closure, source phase and perturbation resolution separate

Diffuse averaging preserves same-side singular channels but makes the left/right frames asymptotically orthogonal. PC-298 quantifies how fast the operator enters the square-zero class. PC-299 then shows that the first positive quadratic measure of the residual loop is not a new spectral variable: it is source autocorrelation with a universal baseline.

Any next nonnormal observable must state both **the scale at which it resolves the defect** and **which information of `C` it retains**. A shrinking parameter is not informative unless it reaches `O(r_q)`, and reaching that scale is still insufficient if the final statistic forgets the source phase or reduces to a known additive-power quantity.
