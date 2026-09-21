# MI-070 — Quotienting out a centralizer that contains the order unit destroys inherited positivity

**Evidence level:** exact operator-algebraic/order-unit synthesis from [WP-398](../../findings/WP-398-critical-centralizer-quotient-positivity-is-order-trivial.md), sharpening the diffuse-support and multi-frequency boundaries of MI-067--MI-069.

WP-397 leaves a bounded critical-factor route in which one accepts the unavoidable diffuse centralizer shadow and tries to read the nonzero gauge-frequency correlations as the arithmetic datum. WP-398 shows that simply forgetting that shadow cannot make ambient positivity orient the surviving information.

Let `M` be the critical Bost--Connes factor, `N` its gauge-fixed centralizer, and `E:M->N` the faithful gauge expectation. On self-adjoint parts set `V=M_sa`, `W=N_sa` and let `q:V->V/W` be the real information quotient. Because the order unit `1` lies in `W`, every self-adjoint class has a positive representative:

`q(M_+) = V/W`.

Indeed, for any self-adjoint `h`, `||h||1+h>=0` and the scalar shift disappears under `q`. The projected positive cone is therefore the whole quotient rather than a proper cone. No nonzero linear sign functional on the quotient can be justified from ambient positivity alone.

Fixing the centralizer shadow does not restore a local orientation. The expectation gives the canonical splitting

`V = W direct_sum ker(E|_V)`.

For every self-adjoint centered direction `k` with `||k||<1`, both `1+k` and `1-k` are positive and satisfy `E(1+/-k)=1`. Thus the normalized positive slice contains both signs of every sufficiently small bounded noncentral direction. Finite collections of nonzero gauge-frequency coefficients can likewise be reversed by replacing a small centered Fourier polynomial `h` with `-h` while keeping the same unit shadow.

This does not contradict MI-069/WP-397. Support domination remains a genuine constraint: nonzero Fourier coefficients must live over the support of the positive centralizer floor. WP-398 says something different. **Once a faithful diffuse shadow is accepted and then quotiented away, positivity supplies no arithmetic orientation on the remaining bounded directions.** Support and sign are separate resources.

A surviving critical-factor construction must therefore keep a source-forced relation between the noncentral correlations and the shadow, or use a joint nonlinear/global invariant whose sign depends on that relation. Merely forming a positive multi-frequency element and discarding its fixed-point component cannot produce a Weil sign. Other categories remain possible only if their readout does not reduce to the same order-unit quotient.

**Boundary.** WP-398 concerns the bounded critical factor, its unital gauge expectation and the real self-adjoint information quotient; `N` is not asserted to be an ideal or a C-star quotient. The result does not show that nonzero-frequency correlations are useless, only that their sign is not inherited from ambient positivity after the centralizer is forgotten. Continuous cores, one-sided correspondences, controlled unbounded nonhomogeneous forms and finite--archimedean assemblies remain distinct categories.
