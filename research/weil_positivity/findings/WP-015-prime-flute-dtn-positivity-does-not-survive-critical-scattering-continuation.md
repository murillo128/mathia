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

Let `Omega` be one finite-area Prime-Flute block with its canonical geodesic boundary and let `Delta>=0` be the positive Laplacian. For real `lambda` below the first Dirichlet eigenvalue, define `Lambda(lambda)` by

\[
(\Delta-\lambda)u=0,
\qquad
u|_{\partial\Omega}=f.
\]

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

## 3. The critical line is universal cusp continuum

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

A single cusp already contains the half-line model `-d^2/dt^2+1/4`. Hence the whole critical scattering line lies in essential spectrum for a reason independent of the prime construction. Any absolute boundary response there contains a universal cusp spectral-density component shared by matched non-prime cusp surfaces.

## 4. What survives is Herglotz positivity, not a positive Weil energy

Energy-dependent DtN maps are Weyl--Titchmarsh functions up to normal-orientation convention. In boundary-triple normalization,

\[
\boxed{
\operatorname{Im}M(z)=(\operatorname{Im}z)\gamma(z)^*\gamma(z)\ge0,
\qquad z\in\mathbb C_+.
}
\tag{5}
\]

This is the universal Nevanlinna/Herglotz sign of an **imaginary part**, not a real quadratic inequality `M(lambda)>=0`. Boundary values on continuous spectrum encode positive spectral density and enter standard scattering formulas. The relevant prior-art anchors are J. Behrndt, F. Gesztesy, S. Nakamura, *Spectral shift functions and Dirichlet-to-Neumann maps*, Math. Ann. 371 (2018), 1255--1300, DOI `10.1007/s00208-017-1593-4`, and J. Behrndt, M. M. Malamud, H. Neidhardt, *Scattering matrices and Dirichlet-to-Neumann maps*, J. Funct. Anal. 273 (2017), 1970--2025, DOI `10.1016/j.jfa.2017.06.001`.

To isolate prime-sensitive data one would naturally subtract a universal cusp/reference response. But if `M_X` and `M_0` are Herglotz,

\[
\operatorname{Im}(M_X-M_0)=\operatorname{Im}M_X-\operatorname{Im}M_0,
\tag{6}
\]

which has no sign in general. A difference of positive operator-valued spectral densities is not positive without an additional operator-ordering theorem. Relative DtN, spectral shift, and scattering phase can carry information, but ordinary Weyl theory does not make them automatically nonnegative.

## 5. PF-078's Feshbach mechanism carries information, not a sign theorem

PF-078 proves the marked-scattering scaling limit

\[
\frac{\varepsilon}{\pi}
\Phi_\varepsilon^{\rm mark}
\left(1-\frac{\varepsilon z}{2\pi^2}\right)
\longrightarrow(G_a-zI)^{-1},
\tag{7}
\]

where `G_a` is the positive weighted path Laplacian carrying tangent gap data. This is a genuine Mathia-native Feshbach mechanism, but the limit is a resolvent. On the real axis `(G_a-zI)^{-1}` is positive only below the nonnegative graph spectrum (`z<0`) and develops poles/sign changes across it.

Therefore Feshbach reduction preserves useful arithmetic-geometric information but does not move the zero-energy DtN sign theorem to positive spectral energies. The Schur/Feshbach escape explicitly left open by WP-009 is **not realized by the ordinary Prime-Flute Laplacian DtN/Feshbach machinery**.

## 6. Matched controls and novelty boundary

The no-go survives the relevant controls: (2) is a generic variational fact; (4) is forced by universal cusp geometry; (5) is universal for self-adjoint Weyl functions; and subtracting the universal background gives the unsigned difference (6). None of these facts distinguishes rational primes.

No novelty is claimed for DtN variational theory, Weyl functions, Herglotz positivity, scattering formulas, or Feshbach reduction. The Mathia-specific durable conclusion is their composition with PF-066, PF-024, and PF-078:

\[
\boxed{
\begin{array}{c}
\text{Prime-Flute zero-energy DtN is positive}\\
\Downarrow\ \lambda>0\\
\text{real quadratic positivity fails immediately}\\
\Downarrow\ \lambda=1/4+t^2\\
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
3. `s=1/2+it -> lambda=1/4+t^2` together with PF-024's universal cusp inclusion (4);
4. the standard Weyl identity (5), up to the harmless global sign from the opposite normal convention;
5. the loss of sign under relative subtraction (6);
6. PF-078's graph-resolvent limit and its real positivity only below the graph spectrum.

Failure of any of checks 2--6 would reopen the direct DtN/Feshbach route. Otherwise the next boundary-response candidate must contain an additional global sign mechanism rather than inherit positivity from the ordinary Laplacian.