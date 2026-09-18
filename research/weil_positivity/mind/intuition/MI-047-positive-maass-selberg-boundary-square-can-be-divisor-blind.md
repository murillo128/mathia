# MI-047 — A positive Maaß--Selberg boundary square can remain divisor-blind even after constant-mode Hecke coupling

**Evidence level:** exact/literature-backed synthesis from [WP-237](../../findings/WP-237-arthur-height-operations-cannot-isolate-the-zeta-zero-block.md), [WP-287](../../findings/WP-287-nonlinear-height-postprocessing-does-not-escape-linear-weil-distribution.md), [WP-345](../../findings/WP-345-maass-selberg-height-derivative-is-a-positive-boundary-square-but-does-not-constrain-the-scattering-divisor.md), [WP-346](../../findings/WP-346-self-adjoint-robin-scattering-realizes-cdd-control-with-positive-full-truncated-norm.md), [WP-347](../../findings/WP-347-self-adjoint-point-scatterers-show-one-cusp-hyperbolic-realizability-does-not-fix-the-scattering-divisor.md), and [WP-356](../../findings/WP-356-hecke-truncation-commutator-is-positive-cusp-annulus-energy-but-does-not-isolate-weil-prime-weight.md).

The rank-one Maaß--Selberg relation supplies a genuine source-defined positive object. If `N_T(r)` is the truncated Eisenstein norm and `tau=log T`, then on the unitary axis `partial_tau N_(e^tau)(r)=|1+S(r)e^(-ir tau)|^2>=0`. But the same operation deletes the `T`-independent logarithmic-derivative term whose explicit-formula decomposition carries the zero divisor. The sign-visible boundary response and divisor-sensitive carrier live in different pieces of the formula.

WP-345--WP-347 show that this is not repaired by demanding abstract or geometric self-adjoint realizability. Inner/CDD factors preserve reciprocal symmetry and unitary-axis modulus while moving the meromorphic divisor; Robin channels realize elementary controls with positive full truncated norms; and real point interactions on a fixed finite-volume one-cusp hyperbolic surface produce genuine self-adjoint relative scattering factors with movable continued resonances. The missing selectivity must therefore use arithmetic structure absent from those controls.

WP-356 inserts exactly such arithmetic structure at the most literal place: a finite-prime Hecke correspondence is coupled to the cusp boundary **before** the positive norm is taken. On the constant Fourier mode, after the natural unitary change from height `y` to log height `x`, the self-adjointly normalized prime Hecke operator becomes

`T_p = S_L+S_(-L)`,  `L=log p`.

For the sharp cusp projection `P_tau`, the commutator has the exact square

`[P_tau,T_p]^*[P_tau,T_p] = 1_(tau-L,tau+L]`.

This is a real source-to-geometry dictionary: Hecke theory selects `L=log p`, and positivity is taken only after that arithmetic insertion. Yet the positive closure remembers only an unsigned annulus. On the critical Eisenstein constant term `e^(itx)+phi(t)e^(-itx)`, the energy is

`4L + 2 Re(phi(t)e^(-2it tau) sin(2tL)/t)`.

The divisor-sensitive scattering phase occurs only in the sign-indefinite interference term. Averaging in `tau` erases it and leaves `4 log p`; subtracting that background isolates the phase only by giving up inherited positivity. Continuous nonarithmetic translations satisfy the same annulus identity, and replacing `phi(t)` by an arbitrary unit-modulus phase preserves nonnegativity.

The critical prime amplitude creates a second obstruction. The standard Hecke normalization contains a `p^(-1/2)` factor, but the cusp Hilbert Jacobian cancels it when the operator is conjugated to log-height translations. The positive square therefore produces `log p` without the desired one-power `p^(-1/2)` attenuation. Any scalar repair enters quadratically: to obtain `p^(-1/2)` in the energy one would have to insert `p^(-1/4)` at vector level, and the tested geometry supplies no reason for that quarter-power.

The reusable principle is stronger than the earlier self-adjoint matched-control warning: **arithmetic insertion before positivity is necessary but still does not imply arithmetic selectivity after positivity**. One must compute the exact positive closure and check which source coordinates survive it. In the constant-mode Hecke/cusp model, the prime label survives as annulus width, while oriented scattering information and the critical half-density do not survive with the required sign and normalization.

This narrows the surviving automorphic route. A viable Maaß--Selberg/Hecke mechanism must use structure absent from the scalar constant-mode annulus: nonconstant Fourier modes, several finite-prime operators before scalarization, nonlocal operator order, higher-rank/adelic truncation, or a source theorem that installs the critical half-density and orientation at vector level before the positive square. Merely adding Hecke equivariance to the same constant-mode boundary norm is now classified.

**Boundary.** WP-356 does not rule out those richer automorphic couplings. The continuous-translation control shows that the positivity theorem itself is geometric, not that the Hecke identification `L=log p` is fake. The result says that this particular positive square fails to convert the arithmetic label into a divisor-selective signed Weil weight; it does not say every Hecke-equivariant positive construction must do so.