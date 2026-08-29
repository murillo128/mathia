# WP-015 — Prime-Flute DtN positivity does not survive continuation to the critical scattering line

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the direct route

```text
canonical Prime-Flute DtN / Feshbach response
    -> spectral-parameter continuation
    -> intrinsic boundary positivity on Re(s)=1/2
    -> global Weil positivity.
```

This finding does **not** rule out a genuinely new graded, relative, cohomological, or compressed boundary construction whose positivity is proved independently. It rules out carrying the ordinary positive Dirichlet-to-Neumann energy exposed by PF-066 through the hyperbolic spectral parameter and treating the resulting critical-line boundary/scattering object as the missing positive Weil form.

## 1. Canonical positive boundary object at zero energy

PF-066 gives, for a canonically isolated Prime-Flute block, a positive self-adjoint zero-energy DtN map and an exact collar-stripping identity. In its notation,

\[
M_\varepsilon(0)=B_T-C_T(A_\varepsilon(0)+B_T)^{-1}C_T,
\]

hence

\[
C_T^{-1}(B_T-M_\varepsilon(0))C_T^{-1}=(A_\varepsilon(0)+B_T)^{-1}.
\]

The full boundary response therefore retains the core information hidden by the universal long collar. This leaves a natural candidate: continue the same response in the spectral parameter and ask whether its sign theorem survives on

\[
s=\frac12+it,
\qquad
\lambda=s(1-s)=\frac14+t^2.
\]

It does not.

## 2. Positive spectral energy creates a negative DtN direction immediately

Let `Omega` be one finite-area Prime-Flute block with its canonical geodesic boundary and let `Delta>=0` be the positive Laplacian. For real `lambda` below the first Dirichlet eigenvalue, let `u` solve `(Delta-lambda)u=0` with boundary trace `u|∂Omega=f`, and let `Lambda(lambda)` be the corresponding DtN map.

With the outward-normal convention for which the zero-energy DtN map is positive, Green's identity gives

\[
\boxed{
\langle f,\Lambda(\lambda)f\rangle
=\int_\Omega |\nabla u|^2\,dA
-\lambda\int_\Omega |u|^2\,dA.
}
\tag{1}
\]

At `lambda=0`, this is ordinary nonnegative Dirichlet energy and `Lambda(0)1=0`. For `0<lambda<lambda_1^D`, the solution with boundary trace `1` minimizes

\[
Q_\lambda(v)=\int_\Omega |\nabla v|^2\,dA-\lambda\int_\Omega|v|^2\,dA
\]

among all functions with the same trace. Since the constant function is admissible,

\[
\boxed{
\langle1,\Lambda(\lambda)1\rangle
\le Q_\lambda(1)
=-\lambda\operatorname{Area}(\Omega)<0.
}
\tag{2}
\]

Thus PF-066's PSD DtN form loses positive-semidefiniteness for **arbitrarily small positive spectral energy**. The failure occurs before any high-energy or scattering subtlety: the constant mode, null at zero, becomes a negative direction as soon as the spectral mass term is present. The exact Schur complement does not preserve the zero-energy sign because the bulk form `Delta-lambda` is no longer positive.

## 3. The ordinary outgoing DtN map is non-Hermitian on the critical scattering line

On the critical line,

\[
\boxed{\lambda(1/2+it)=1/4+t^2\ge1/4.}
\tag{3}
\]

PF-024 proves directly from the normalized cusp zero mode that

\[
\boxed{[1/4,\infty)\subset\sigma_{\rm ess}(\Delta_{X_{\rm prime}}).}
\tag{4}
\]

More strongly, the same zero mode gives an exact critical-line obstruction to ordinary DtN positivity, independent of the low-energy estimate (2). In logarithmic cusp height `t`, the normalized zero Fourier mode conjugates to the half-line operator

\[
-\frac{d^2}{dt^2}+\frac14.
\]

At a critical scattering energy

\[
\lambda=\frac14+r^2,
\qquad r>0,
\]

the radiation solutions of the conjugated equation are

\[
g_\pm(t)=e^{\pm irt},
\]

or, before the standard cusp conjugation,

\[
f_\pm(t)=e^{t/2}e^{\pm irt}.
\]

At a truncation horocycle `t=T`, the normal derivative divided by the boundary value is, up to the single global sign determined by the outward-normal convention,

\[
\pm\left(\frac12\pm ir\right).
\]

After removing the harmless real `1/2` conjugation term, the outgoing cusp DtN/Weyl multiplier has anti-Hermitian part of magnitude `r`. Equivalently, Green's flux identity records a nonzero imaginary boundary flux carried into or out of the cusp by the radiation condition. Therefore for every `r>0` the ordinary outgoing critical-line DtN boundary value is **not Hermitian**.

A positive-semidefinite quadratic form on a complex Hilbert space must be Hermitian. Consequently

\[
\boxed{
\text{ordinary outgoing DtN at }\lambda=\frac14+r^2
\text{ cannot be PSD for }r>0.
}
\]

This directly closes the possible gap between the low-energy variational failure and the actual critical scattering line: no comparison between `1/4+r^2` and the finite-block Dirichlet eigenvalue `\lambda_1^D` is needed. The obstruction is already present in the universal cusp channel and is independent of prime arithmetic.

A single cusp therefore does two things simultaneously: it forces the essential half-line (4), and its outgoing zero mode prevents the ordinary critical-line DtN boundary value from being a positive self-adjoint continuation of the zero-energy map. Any absolute boundary response there also contains a universal cusp spectral-density component shared by matched non-prime cusp surfaces.

## 4. What survives is Herglotz positivity, not a positive Weil energy

Energy-dependent DtN maps are Weyl--Titchmarsh functions up to normal-orientation convention. In boundary-triple normalization,

\[
\boxed{
\operatorname{Im}M(z)=(\operatorname{Im}z)\gamma(z)^*\gamma(z)\ge0,
\qquad z\in\mathbb C_+.
}
\tag{5}
\]

This is the universal Nevanlinna/Herglotz sign of an **imaginary part**, not a real quadratic inequality `M(lambda)>=0`. The nonzero critical-line radiation flux above is the boundary-value manifestation of this distinction: scattering data naturally acquire an imaginary part rather than preserve the zero-energy real PSD form. Boundary values on continuous spectrum encode positive spectral density and enter standard scattering formulas. The relevant prior-art anchors are J. Behrndt, F. Gesztesy, S. Nakamura, *Spectral shift functions and Dirichlet-to-Neumann maps*, Math. Ann. 371 (2018), 1255--1300, DOI `10.1007/s00208-017-1593-4`, and J. Behrndt, M. M. Malamud, H. Neidhardt, *Scattering matrices and Dirichlet-to-Neumann maps*, J. Funct. Anal. 273 (2017), 1970--2025, DOI `10.1016/j.jfa.2017.06.001`.

To isolate prime-sensitive data one would naturally subtract a universal cusp/reference response. But if `M_X` and `M_0` are Herglotz,

\[
\operatorname{Im}(M_X-M_0)=\operatorname{Im}M_X-\operatorname{Im}M_0,
\tag{6}
\]

which has no sign in general. A difference of positive operator-valued spectral densities is not positive without an additional operator-ordering theorem. Relative DtN, spectral shift, and scattering phase can carry information, but ordinary Weyl theory does not make them automatically nonnegative.

This does **not** rule out positivity of every derived critical-line observable. A Herglotz imaginary part, a Cayley/scattering transform, a relative response with an independent ordering theorem, or a further Prime-Flute-specific compression may have a useful sign. Such a sign would be a new theorem about that derived object; it is not inherited from the zero-energy DtN energy.

## 5. PF-078's Feshbach mechanism carries information, not a sign theorem

PF-078 proves the marked-scattering scaling limit

\[
\frac{\varepsilon}{\pi}
\Phi_\varepsilon^{\rm mark}
\left(1-\frac{\varepsilon z}{2\pi^2}\right)
\longrightarrow(G_a-zI)^{-1},
\tag{7}
\]

where `G_a` is the positive weighted path Laplacian carrying tangent gap data. This is a genuine Mathia-native Feshbach mechanism, but the limit is a resolvent. On the real axis `(G_a-zI)^(-1)` is positive only below the nonnegative graph spectrum (`z<0`) and develops poles/sign changes across it.

Therefore Feshbach reduction preserves useful arithmetic-geometric information but does not move the zero-energy DtN sign theorem to positive spectral energies. The Schur/Feshbach escape explicitly left open by WP-009 is **not realized by the ordinary Prime-Flute Laplacian DtN/Feshbach machinery**.

## 6. Matched controls and novelty boundary

The no-go survives the relevant controls: (2) is a generic variational fact; (4) and the exact outgoing zero-mode flux are forced by universal cusp geometry; (5) is universal for self-adjoint Weyl functions; and subtracting the universal background gives the unsigned difference (6). None of these facts distinguishes rational primes.

No novelty is claimed for DtN variational theory, Weyl functions, Herglotz positivity, scattering formulas, or Feshbach reduction. The Mathia-specific durable conclusion is their composition with PF-066, PF-024, and PF-078:

\[
\boxed{
\begin{array}{c}
\text{Prime-Flute zero-energy DtN is positive}\\
\Downarrow\ \lambda>0\\
\text{real quadratic positivity fails immediately}\\
\Downarrow\ \lambda=1/4+t^2\\
\text{outgoing cusp DtN is non-Hermitian and carries radiation flux}\\
\Downarrow\\
\text{only universal Herglotz spectral-density positivity remains}\\
\Downarrow\ \text{relative subtraction}\\
\text{no sign survives without an additional theorem.}
\end{array}}
\tag{8}
\]

A surviving boundary route therefore needs an additional global structure -- grading/supertrace, a canonical compressed or relative space with an independent ordering theorem, an intersection/cohomological pairing, or a different Mathia-native operator -- whose sign is not inherited from ordinary elliptic Dirichlet energy. It must also couple canonically to the Prime-Lattice coefficients `Lambda(p^k)/sqrt(p^k)` and generate the archimedean/polar sector before positivity is invoked.

## 7. Audit / falsification core

The decisive checks are:

1. PF-066's zero-energy positivity and exact collar stripping;
2. Green's identity (1) and the constant-trial estimate (2) for `0<lambda<lambda_1^D`;
3. `s=1/2+it -> lambda=1/4+t^2` together with PF-024's normalized cusp zero-mode reduction to `-d^2/dt^2+1/4` and essential-spectrum inclusion (4);
4. at `lambda=1/4+r^2`, the radiation solutions `e^{±irt}` give an outgoing DtN/Weyl multiplier with nonzero anti-Hermitian part `±ir`, so the ordinary critical-line boundary value cannot be PSD;
5. the standard Weyl identity (5), up to the harmless global sign from the opposite normal convention;
6. the loss of sign under relative subtraction (6);
7. PF-078's graph-resolvent limit and its real positivity only below the graph spectrum.

Failure of any of checks 2--7 would reopen the direct DtN/Feshbach route. Otherwise the next boundary-response candidate must contain an additional global sign mechanism rather than inherit positivity from the ordinary Laplacian.