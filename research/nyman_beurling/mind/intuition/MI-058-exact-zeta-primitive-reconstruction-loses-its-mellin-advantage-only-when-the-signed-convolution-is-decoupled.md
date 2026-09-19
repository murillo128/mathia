# MI-058 — Exact zeta-primitive reconstruction loses its Mellin advantage only when the signed convolution is decoupled

**Evidence level:** exact synthesis from [NB-218](../../findings/NB-218-exact-zeta-primitive-convolution-isolates-mellin-tariff.md), refining the absolute reconstruction obstruction in [NB-217](../../findings/NB-217-reciprocal-log-support-mass-prices-two-sided-mellin-reconstruction.md).

Let `sigma>1`, let `h` be a smooth logarithmic source shell supported away from `u=0`, and define the `j`-fold vertical primitive

`P_j(t)=sum_(n>=2) Lambda(n)/(log n)^j n^(-sigma-it)`

and reconstruction kernel

`K_(j,h)(v)=int u^j h(u)e^(ivu)du`.

Fourier inversion gives the exact signed identity

`sum Lambda(n)h(log n)n^(-sigma-it) = (1/(2pi)) int K_(j,h)(v) P_j(t+v) dv`.

The factors `(log n)^j` and `(log n)^(-j)` cancel coefficient by coefficient **inside the convolution**. For `j=1`, `P_1(t)=log zeta(sigma+it)` on the Euler-product half-plane, so this is the actual zeta primitive rather than a surrogate Fourier model.

Because `u^j h(u)` vanishes near `u=0`, every moment of `K_(j,h)` vanishes. The shell extraction is therefore unchanged if any finite polynomial in `v` is subtracted from `P_j(t+v)`. Large constant or finite Taylor-jet components of the primitive are invisible to the exact source observable; what matters is the primitive's vertical Fourier content at the shell's logarithmic carrier frequency.

This separates two currencies that NB-217 intentionally left entangled. The reciprocal-support lower bound

`||K_j||_1/|M_psi(h)| >= 2pi/J_j(E)`

is an exact obstruction for **absolute-value decoupling**, not an algebraic multiplier that appears in the exact signed reconstruction. The tariff re-enters when one bounds the convolution by `||K_j||_1 sup|P_j|` or otherwise prices kernel and primitive independently. A better pointwise bound for the primitive does not by itself exploit the available cancellation.

For a moving shell `h(u)=phi(u-X)`, the source is an explicit carrier-frequency coefficient

`(1/(2pi)) int B_X(v) P_j(t+v)e^(iXv) dv`.

The live analytic object is therefore this localized oscillatory coefficient, with kernel tails, contour transport, pole/branch terms and the zero-free window kept coupled. Any proof that takes absolute values before those interactions have occurred returns to the NB-217 tariff.

**Boundary.** The exact identity is established cleanly in `Re(s)>1`; it is not itself a saving on the Vinogradov--Korobov contour. Moving the coupled convolution left, truncating it to an effective vertical window and proving cancellation at carrier frequency `X` remain open analytic tasks. The Nyman destination coupling also remains separate: no result here shows that a near-optimal Nyman approximant forces the source coefficient being estimated.