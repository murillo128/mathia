# MI-058 — Exact zeta-primitive reconstruction can be localized before the Mellin advantage is lost

**Evidence level:** exact synthesis from [NB-218](../../findings/NB-218-exact-zeta-primitive-convolution-isolates-mellin-tariff.md) and [NB-219](../../findings/NB-219-smooth-vertical-windowing-localizes-zeta-primitive-convolution.md), refining the absolute reconstruction obstruction in [NB-217](../../findings/NB-217-reciprocal-log-support-mass-prices-two-sided-mellin-reconstruction.md).

Let `sigma>1`, let `h` be a smooth logarithmic source shell supported away from `u=0`, and define the `j`-fold vertical primitive and its matched reconstruction kernel. Fourier inversion gives an exact signed convolution for the Euler shell. The factors `(log n)^j` and `(log n)^(-j)` cancel coefficient by coefficient **inside the convolution**, and every finite polynomial jet of the primitive is annihilated because the shell kernel vanishes to all moments at the origin.

NB-218 therefore separates the exact algebra from the absolute reconstruction tariff. The lower bound `||K_j||_1/|M_psi(h)|>=2pi/J_j(E)` applies when kernel and primitive are decoupled by absolute values; it is not an algebraic multiplier in the signed identity. For a moving shell `h(u)=phi(u-X)`, the source is a carrier-frequency Fourier coefficient of the zeta primitive, so a pointwise primitive envelope is not the native quantity.

NB-219 now shows that the full vertical line can be localized without first destroying this structure. Multiply the Fourier kernel by a smooth cutoff `chi(v/V)` that equals one for `|v|<=V` and vanishes for `|v|>=2V`. On the natural `1+` line `sigma_X=1+r/X`, Fourier inversion transfers this cutoff back to the source as convolution with a Schwartz approximate identity. For every `A>0`, the resulting Euler-source perturbation is

`O_A(V^(-A))`

uniformly in the vertical ordinate. Any slowly growing `V_X` gives `o(1)` source error, and `V=X^epsilon` gives error smaller than every prescribed power of `X`. The finite-jet annihilation of the exact kernel survives to superalgebraic accuracy.

This changes the live bottleneck. The infinite vertical tail does not need to be estimated by `int |K P_j|`; it can be removed **at the source level** before estimating the primitive. Thus localization and signed cancellation are compatible on `Re(s)>1`.

The remaining obstruction is transport across `Re(s)=1`. Compact support in the vertical frequency creates Schwartz, but noncompact, tails in the logarithmic source variable. Those tails remain harmless with the positive Euler weight on `sigma>1` but need not be absolutely summable on a line left of one. A successful continuation must therefore carry the localized signed convolution through the pole/branch structure, horizontal contour pieces and zero-free rectangle without reverting to the absolute-norm tariff.

The reusable lesson is that **a proof-interface loss should be attacked before the destructive inequality is applied**. If a global acquisition domain can be localized by an operation that corresponds to a negligible source perturbation, there is no reason to pay for that domain with a global supremum. The next question is whether the same coupling survives the analytic transport required by the destination.

**Boundary.** NB-219 proves localization only on the absolutely convergent `1+` side; it does not provide a Vinogradov--Korobov saving, a contour-shift theorem, a Nyman-distance improvement or the destination coupling from near-optimal approximants to this source coefficient. The unresolved object is the localized signed carrier coefficient after crossing `Re(s)=1`.
