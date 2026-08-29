# WP-015 — Prime-Flute DtN positivity does not survive continuation to the critical scattering line

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the direct route

```text
canonical Prime-Flute DtN / Feshbach response
    -> spectral-parameter continuation
    -> intrinsic boundary positivity on Re(s)=1/2
    -> global Weil positivity.
```

This finding does **not** rule out a genuinely new graded, relative, cohomological, or compressed boundary construction whose positivity is proved independently. It rules out taking the ordinary positive Dirichlet-to-Neumann energy exposed by PF-066, carrying the same response through the hyperbolic spectral parameter, and treating the resulting critical-line boundary/scattering object as the missing positive Weil form.

## 1. The candidate supplied by Prime Flute is unusually canonical

PF-066 gives a strong Mathia-native boundary object. For a canonically isolated prime block `Omega_epsilon` with outer separating geodesic `beta_epsilon`, the physical zero-energy Dirichlet-to-Neumann map `Lambda_epsilon(0)` is positive and self-adjoint, and the universal half-collar can be stripped **exactly**:

\[
M_\varepsilon(0)
=B_T-C_T(A_\varepsilon(0)+B_T)^{-1}C_T,
\]

where `M_epsilon=epsilon Lambda_epsilon`, while `A_epsilon` is the DtN operator of the canonically truncated core. Equivalently,

\[
C_T^{-1}(B_T-M_\varepsilon(0))C_T^{-1}
=(A_\varepsilon(0)+B_T)^{-1}.
\]

Unlike raw Steklov eigenvalues, the full response loses no information through the long collar. PF-066 therefore left a precise possible escape for the Weil-positivity program: carry the exact layer stripping through the spectral parameter and ask whether a boundary-energy theorem survives on the line

\[
s=\frac12+it,
\qquad
\lambda=s(1-s)=\frac14+t^2.
\]

The obstruction below is that the ordinary DtN sign theorem lives at zero/subthreshold energy, whereas the Weil/critical scattering parameter lies on the positive spectral continuum.

## 2. Positive zero-energy DtN becomes negative already for arbitrarily small positive energy

Let `Omega` be one of the finite-area Prime-Flute blocks with its canonical geodesic boundary, and let `Delta>=0` denote the positive Laplacian. For real `lambda` below the first Dirichlet spectral point, define `Lambda(lambda)` by solving

\[
(\Delta-\lambda)u=0,
\qquad
u|_{\partial\Omega}=f.
\]

With the physical outward-normal convention used for the positive zero-energy DtN map, Green's identity gives

\[
\boxed{
\langle f,\Lambda(\lambda)f\rangle
=
\int_\Omega |\nabla u|^2\,dA
-\lambda\int_\Omega |u|^2\,dA.
}
\tag{1}
\]

At `lambda=0` this is the ordinary nonnegative Dirichlet energy. In particular the constant boundary value has harmonic extension `u=1` and lies in the zero mode:

\[
\Lambda(0)1=0.
\]

For every sufficiently small `lambda>0`, however, the solution is the minimizer of the coercive affine quadratic functional

\[
Q_\lambda(v)
=
\int_\Omega |\nabla v|^2\,dA
-\lambda\int_\Omega |v|^2\,dA
\]

among functions with trace `1`. The constant trial function is admissible, so

\[
\boxed{
\langle 1,\Lambda(\lambda)1\rangle
=
\min_{v|_{\partial\Omega}=1}Q_\lambda(v)
\le Q_\lambda(1)
=-\lambda\,\operatorname{Area}(\Omega)<0.
}
\tag{2}
\]

Thus the positive DtN form of PF-066 loses positive-semidefiniteness **immediately on the positive-energy side**. This is not a high-energy pathology and does not depend on prime gaps, collar asymptotics, or a difficult scattering limit. The constant mode that is null at zero becomes a negative direction as soon as the spectral mass term is switched on.

Equation (2) is also a direct falsification of the hope that the exact Schur-complement structure in PF-066 might preserve positivity automatically under spectral continuation. The Schur complement is positive at zero because it is the response of a positive Dirichlet energy. Once the bulk form is `Delta-lambda`, that positivity hypothesis is gone.

## 3. The critical line lies exactly in the universal cusp continuum

For the Prime Flute the relevant hyperbolic spectral parameter is

\[
\lambda=s(1-s).
\]

On the critical line,

\[
\boxed{
\lambda\left(\frac12+it\right)=\frac14+t^2\ge\frac14.
}
\tag{3}
\]

PF-024 proves directly from a single normalized cusp channel that

\[
\boxed{
[1/4,\infty)\subset\sigma_{\rm ess}(\Delta_{X_{\rm prime}}).
}
\tag{4}
\]

The proof is local: the zeroth Fourier mode of every cusp is unitarily equivalent to the half-line operator

\[
-\frac{d^2}{dt^2}+\frac14.
\]

Consequently the whole critical scattering line (3) sits in essential spectrum for a reason that is **independent of the prime construction**. It is already forced by the universal geometry of a hyperbolic cusp.

This matters twice. First, one cannot reach the critical line by preserving the subthreshold positive DtN theorem: the path has crossed the positive spectrum long before `lambda=1/4+t^2`. Second, the absolute critical-line boundary response carries a large universal cusp spectral density that survives every matched non-prime control with the same cusp geometry.

## 4. What positivity survives is Herglotz spectral-density positivity, not a Weil energy

Energy-dependent DtN maps are standard Weyl--Titchmarsh functions, up to the normal-orientation sign convention. In boundary-triple normalization the Weyl function `M(z)` satisfies

\[
\boxed{
\operatorname{Im}M(z)
=(\operatorname{Im}z)\,\gamma(z)^*\gamma(z)\ge0,
\qquad z\in\mathbb C_+.
}
\tag{5}
\]

Thus the canonical positivity that survives spectral continuation has changed category. It is not

\[
M(\lambda)\ge0
\]

as a self-adjoint real quadratic form. It is the **Nevanlinna/Herglotz sign of the imaginary part in the upper half-plane**. Boundary values `M(lambda+i0)` on continuous spectrum encode the absolutely continuous spectral channels, and general scattering matrices can be represented directly in terms of those boundary values and `Im M(lambda+i0)`.

This is well-established operator theory, not a new Mathia mechanism. See J. Behrndt, F. Gesztesy, S. Nakamura, *Spectral shift functions and Dirichlet-to-Neumann maps*, Math. Ann. 371 (2018), 1255--1300, DOI `10.1007/s00208-017-1593-4`, especially the Weyl identity; and J. Behrndt, M. M. Malamud, H. Neidhardt, *Scattering matrices and Dirichlet-to-Neumann maps*, J. Funct. Anal. 273 (2017), 1970--2025, DOI `10.1016/j.jfa.2017.06.001`.

For the present research line, (5) fails the substantive target in the same way that several earlier candidates did: its positivity follows for **every self-adjoint boundary problem**. It does not select the rational-prime geometry or generate the Weil finite weights. In the Prime Flute, PF-024 identifies the critical-line carrier on which this positive spectral density lives as universal cusp background.

## 5. Canonical background subtraction destroys the Herglotz sign

A natural reply is to subtract the universal cusp response and keep only a prime-sensitive relative DtN/scattering object. But the positivity in (5) is not stable under this operation.

If `M_X` and `M_0` are two Weyl/DtN functions, each has

\[
\operatorname{Im}M_X(z)\ge0,
\qquad
\operatorname{Im}M_0(z)\ge0
\]

in the upper half-plane. The relative response has

\[
\operatorname{Im}(M_X-M_0)
=
\operatorname{Im}M_X-\operatorname{Im}M_0,
\tag{6}
\]

which has no sign in general. A difference of positive operator-valued spectral densities is not positive unless an additional operator ordering theorem is available.

That is exactly the kind of extra theorem the Weil-positivity program is searching for; ordinary DtN/Weyl theory does not provide it. In particular, one cannot argue

```text
absolute DtN is Herglotz-positive
    -> subtract universal cusp/collar background
    -> prime-sensitive relative response is still positive.
```

The second implication is false as a structural principle. Relative spectral shift and scattering phase are therefore legitimate **information carriers**, but not automatic sources of nonnegativity.

## 6. Feshbach reduction does not move the sign theorem to the Weil line

PF-078 proves an important positive analytic result near `s=1`: after splitting the Laplacian into its finite-dimensional small-mode sector and a uniformly gapped complement, the physical marked scattering block has the singular scaling limit

\[
\frac{\varepsilon}{\pi}
\Phi_\varepsilon^{\rm mark}
\left(1-\frac{\varepsilon z}{2\pi^2}\right)
\longrightarrow
(G_a-zI)^{-1}.
\tag{7}
\]

This is a genuine Mathia-native Feshbach mechanism and preserves ordered gap information. But it also gives a clean control for the present question. The limiting object is a resolvent. For a positive graph Laplacian `G_a`,

\[
(G_a-zI)^{-1}\ge0
\]

only in the usual subthreshold region `z<0`; as `z` crosses the nonnegative graph spectrum it develops poles and alternating-sign real resolvent sectors. Feshbach reduction packages the spectral information correctly, but it does not create a new positive quadratic form on positive spectral energies.

The same logic applies to the full surface: Schur complements of `H-z` inherit a positive-energy theorem only where the relevant bulk block remains positive/invertible with the required ordering. On the critical scattering line, `z=lambda>=1/4` belongs to the universal continuous spectrum (4), so that hypothesis is unavailable.

Therefore the escape left open in WP-009 -- that a larger Schur/Feshbach or boundary-response system might force the missing counterterm while remaining positive -- is **not realized by the ordinary Prime-Flute Laplacian DtN/Feshbach machinery**. A successful larger system would need an additional grading, quotient, relative intersection form, nonstandard inner product, or other structure whose sign theorem is not inherited from the raw elliptic energy.

## 7. Matched-control and novelty audit

The obstruction survives the relevant controls.

- The zero-energy DtN positivity and the sign change in (2) are generic variational facts; they do not depend on primality.
- The critical-line continuum (4) is forced by local cusp geometry and therefore persists for the all-composite Prime-Flute controls and any matched cusp surface.
- The Herglotz identity (5) is universal for self-adjoint Weyl functions.
- Removing that universal background by a relative difference loses the positive cone by the elementary identity (6).

The literature already contains the general boundary-triple/Weyl, DtN, scattering, Krein-resolvent, and spectral-shift machinery. No novelty is claimed for those facts. The Mathia-specific durable conclusion is the **three-stage no-go obtained by composing them with PF-066 and PF-024**:

\[
\boxed{
\begin{array}{c}
\text{canonical Prime-Flute zero-energy DtN is positive}\\[2mm]
\Downarrow\ \lambda>0\\[2mm]
\text{ordinary real quadratic positivity already fails}\\[2mm]
\Downarrow\ \lambda=1/4+t^2\\[2mm]
\text{only universal Herglotz/scattering spectral-density positivity remains}\\[2mm]
\Downarrow\ \text{relative subtraction}\\[2mm]
\text{no sign survives without an additional theorem.}
\end{array}
}
\tag{8}
\]

This is materially stronger than observing that the Prime-Flute spectrum itself is not RH-specific: it rules out using the **most canonical positive boundary-response structure currently available in Mathia** as the missing Weil positivity merely by spectral continuation or Feshbach/layer stripping.

## 8. Boundary of the no-go

WP-015 does not rule out every possible boundary construction. A counterexample to the stated obstruction would need to supply at least one of the following genuinely new ingredients:

1. a canonical relative/compressed boundary space on which the universal cusp spectral density is quotiented out **and** positivity follows from an independent theorem;
2. a graded or supertrace boundary form whose indefinite local pieces combine into a positive global pairing for structural reasons;
3. a different Mathia-native operator, not the ordinary Laplacian DtN/Weyl map, whose positive cone is naturally parameterized by the Weil test-function variable rather than by subthreshold spectral energy;
4. a canonical coupling to Prime Lattice that produces the exact `Lambda(p^k)/sqrt(p^k)` finite coefficients and the archimedean/polar terms before positivity is invoked.

Merely evaluating the same DtN family at another hand-picked parameter, taking `|M|`, `M^*M`, or staying in `lambda<0` would not answer the primary question: those operations either abandon the critical scattering geometry or manufacture positivity without reproducing the Weil local-to-global decomposition.

## 9. Audit core

The decisive checks are finite and explicit:

1. verify the zero-energy positivity and exact collar stripping in PF-066;
2. apply Green's identity to obtain (1);
3. with boundary trace `1`, insert the constant trial function to obtain the strict negative estimate (2) for `0<lambda<lambda_1^D`;
4. verify the critical-line mapping `s=1/2+it -> lambda=1/4+t^2`;
5. verify from PF-024 that `[1/4,infinity)` is already forced into essential spectrum by a single cusp channel;
6. verify the standard Weyl identity (5), with the harmless overall sign adjusted if one uses the opposite physical-normal convention;
7. verify that relative subtraction gives (6) and hence does not preserve the Herglotz cone;
8. verify that the PF-078 Feshbach limit is a graph resolvent and that its real positivity is confined to the subthreshold side.

Failure of any of items 2--8 would reopen the direct DtN/Feshbach route. Otherwise the next boundary-response candidate must contain an additional global sign mechanism rather than inherit positivity from ordinary elliptic Dirichlet energy.