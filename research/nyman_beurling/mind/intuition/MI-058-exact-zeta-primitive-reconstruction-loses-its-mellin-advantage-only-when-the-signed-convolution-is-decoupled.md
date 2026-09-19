# MI-058 — Exact zeta-primitive reconstruction localizes and transports back to one logarithmic-derivative carrier

**Evidence level:** exact synthesis from [NB-218](../../findings/NB-218-exact-zeta-primitive-convolution-isolates-mellin-tariff.md) through [NB-221](../../findings/NB-221-flat-soft-primitive-windows-factor-through-local-log-derivative-contour.md), refining the absolute reconstruction obstruction in [NB-217](../../findings/NB-217-reciprocal-log-support-mass-prices-two-sided-mellin-reconstruction.md).

Let `sigma>1`, let `h` be a smooth logarithmic source shell supported away from `u=0`, and define the `j`-fold vertical primitive and its matched reconstruction kernel. Fourier inversion gives an exact signed convolution for the Euler shell. The factors `(log n)^j` and `(log n)^(-j)` cancel coefficient by coefficient **inside the convolution**, and every finite polynomial jet of the primitive is annihilated because the shell kernel vanishes to all moments at the origin.

NB-218 therefore separates the exact algebra from the absolute reconstruction tariff. The lower bound `||K_j||_1/|M_psi(h)|>=2pi/J_j(E)` applies when kernel and primitive are decoupled by absolute values; it is not an algebraic multiplier in the signed identity. For a moving shell, the source is a carrier-frequency Fourier coefficient of the zeta primitive, so a pointwise primitive envelope is not the native quantity.

NB-219--NB-220 show that localization need not destroy this structure. A flat Gaussian-type soft vertical window has a Gaussian dual source profile; for any prescribed algebraic accuracy its order can be fixed so that the localized moving shell differs from the original by `O_B(X^-B)`, while the modified Euler source series is entire in `s`. Thus neither the infinite vertical line nor left-of-one source summability forces the Mellin tariff.

NB-221 then identifies what every **fixed** primitive depth becomes after faithful transport. Repeated integration by parts sends the primitive derivatives onto the flat window and yields

`I_j(s)=A_0(s)+sum_(k>=1) binom(j,k) i^k A_k(s)`,

where the leading term is always

`A_0(s)=(1/(2pi)) integral L_X(v) w_V(v) (-zeta'/zeta)(s+iv) dv`,

with coefficient exactly one, while every `k>=1` window-derivative correction is `O(log X V^(-2M-2))` for fixed `j` and sufficiently flat fixed order `M`.

The leading integral can be moved left locally without a global contour. Split at `|v|<=|t|/2`; leave the tails on the absolutely convergent `1+` line and move only the central segment through a finite rectangle. Throughout that rectangle the physical height remains comparable to `|t|`, so a Vinogradov--Korobov zero-free strip excludes nontrivial zeros and the zeta pole at height zero is never encountered. Remote zeta singularities therefore do not generate a residue budget.

This closes the representation/identification problem left by NB-220, but it also removes primitive depth as an independent source of analytic gain. After transport, the same local `-zeta'/zeta` convolution leads the expansion for every fixed `j`. Applying the existing pointwise Vinogradov--Korobov estimate to that carrier recovers the same log-squared corridor as NB-212, up to arbitrarily small algebraic localization errors.

The reusable lesson is that **representation repair can remove artificial proof costs without changing the final analytic carrier**. Exact coupling avoids the Mellin reconstruction tariff; analytic soft localization removes source-tail obstruction; finite-height contour transport removes remote-zero obstruction. Once all three are stripped away, the surviving bottleneck is cancellation inside one local logarithmic-derivative Fourier integral, not primitivization or continuation.

**Boundary.** NB-221 treats fixed primitive depth and does not prove cancellation in the transported `-zeta'/zeta` integral, improve the Nyman distance, or supply the final destination coupling from source control to near-optimal approximants. A genuine improvement must exploit signed/carrier-frequency cancellation beyond the pointwise Vinogradov--Korobov envelope rather than add another primitive or localization layer.