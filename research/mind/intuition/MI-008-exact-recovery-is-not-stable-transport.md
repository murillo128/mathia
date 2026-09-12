# MI-008 — Exact recovery, quotient geometry, target discriminants, and source-normalized response are different resources

**Evidence level:** supported by the finite inverse/timing/zero-count results through AF-290 and the scalar propagation/Green results through PF-304; no universal target modulus or full mixed-response theorem is claimed.

Arithmetic Fidelity separates acquisition from the final analytic target. AF-279--AF-287 classify aliasing, genuinely mixed recovery, sample complexity, frame conditioning, and rowwise timing perturbation for finite Dirichlet coefficients. AF-288--AF-289 then identify the common timing center as the exact gauge `F(s)->F(s+i sigma)`. For a common-clock-invariant target only the residual differential radius

\[
r(\tau)=\inf_\sigma\max_j|\tau_j-\sigma|
\]

enters the coefficient-orbit error.

AF-290 adds the missing target geometry. For a finite Dirichlet polynomial and compact Jordan boundary `Gamma`, the coefficient vectors where a zero reaches the boundary form a discriminant `Delta_Gamma`, and

\[
\operatorname{dist}_2(b,\Delta_\Gamma)
=
\min_{z\in\Gamma}
\frac{|P_b(z)|}{(\sum_{n\le N}n^{-2\operatorname{Re}z})^{1/2}}.
\]

This is the exact uniform perturbation radius protecting the zero count. It is covariant under the common-clock vertical-translation gauge, so the composition is clean: coefficient-orbit error is harmless to the zero-count target only while it remains below the normalized discriminant distance. Source conditioning and target conditioning are independent; AF-290 gives classes where the target margin collapses despite a finite well-defined coefficient model.

Prime Flute supplies a complementary source-normalized phenomenon. PF-297--PF-302 show scalar directional losses accumulating to round-trip extinction. PF-303 identifies the scalar killing vector `d` as the exact Green-potential currency, and PF-304 shows that `P_N=G_ND_N` is a reversible Markov kernel. Hence

\[
\|G_Nf\|_{\ell^p(d)}
\le
\|D_N^{-1}f\|_{\ell^p(d)},
\qquad1\le p\le\infty.
\]

The absence of a depth-uniform scalar spectral gap is therefore not itself a forced-response obstruction once the source is measured in the matching killing currency. The unresolved burden is the physical map from the true forcing and reassembly into those norms.

The cross-line lesson is concrete: **remove exact nuisance symmetries first, normalize by the actual source geometry second, and then price distance to the destination's ill-posed set**. An ambient perturbation bound can overcharge a gauge direction; a stable source representation can still lie next to a target discontinuity; a bad bare spectral gap can disappear in the correct source-weighted response norm.

**Boundary.** AF-290 is finite-support and fixed-contour zero count; it does not provide an RH-relevant uniform discriminant margin. PF-303--PF-304 are finite scalar statements and do not prove the complete boundary response factors through their Markov normalization. None of these currencies transfers automatically to another target.
