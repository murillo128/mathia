# WP-015 — Prime-Flute DtN positivity does not survive continuation to the critical scattering line

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the direct route

```text
canonical Prime-Flute DtN / Feshbach response
    -> spectral-parameter continuation
    -> intrinsic boundary positivity on Re(s)=1/2
    -> global Weil positivity.
```

This finding does **not** rule out a genuinely new graded, relative, cohomological, or compressed boundary construction whose positivity is proved independently. It rules out carrying the ordinary positive Dirichlet-to-Neumann energy exposed by PF-066 through the hyperbolic spectral parameter and treating the resulting critical-line boundary/scattering object as the missing positive Weil form.

## 1. Prime Flute supplies a canonical positive boundary object at zero energy

PF-066 gives, for a canonically isolated prime block with separating geodesic of length `epsilon`, a positive self-adjoint zero-energy DtN map and an exact collar-stripping identity. In its notation,

\[
M_\varepsilon(0)
=B_T-C_T(A_\varepsilon(0)+B_T)^{-1}C_T,
\]

and therefore

\[
C_T^{-1}(B_T-M_\varepsilon(0))C_T^{-1}
=(A_\varepsilon(0)+B_T)^{-1}.
\]

Thus the full boundary response loses no information through the long universal collar. This left a precise candidate for the Weil-positivity program: continue the same canonical response in the spectral parameter and ask whether its geometric sign theorem survives on

\[
s=\frac12+it,
\qquad
\lambda=s(1-s)=\frac14+t^2.
\]

It does not.

## 2. The real DtN quadratic form becomes negative immediately for positive spectral energy

Let `Omega` be one of the finite-area Prime-Flute blocks with its canonical geodesic boundary, and let `Delta>=0` be the positive Laplacian. For real `lambda` below the first Dirichlet eigenvalue, define `Lambda(lambda)` by

\[
(\Delta-\lambda)u=0,
\qquad
u|_{\partial\Omega}=f.
\]

With the outward-normal convention for the positive zero-energy DtN map, Green's identity gives

\[
\boxed{
\langle f,\Lambda(\lambda)f\rangle
=
\int_\Omega |\nabla u|^2\,dA
-\lambda\int_\Omega |u|^2\,dA.
}
\tag{1}
\]

At `lambda=0` this is ordinary nonnegative Dirichlet energy and `Lambda(0)1=0`. For `0<lambda<lambda_1^D`, the solution with boundary trace `1` minimizes the coercive affine form

\[
Q_\lambda(v)=\int_\Omega |\nabla v|^2\,dA-\lambda\int_\Omega|v|^2\,dA.
\]

The constant function `v=1` is an admissible trial function. Hence

\[
\boxed{
\langle1,\Lambda(\lambda)1\rangle
=\min_{v|_{\partial\Omega}=1}Q_\lambda(v)
\le Q_\lambda(1)
=-\lambda\operatorname{Area}(\Omega)<0.
}
\tag{2}
\]

Therefore the PSD DtN form of PF-066 loses positive-semidefiniteness **for arbitrarily small positive spectral energy**. The obstruction occurs before any difficult scattering limit, prime-gap asymptotics, or high-energy phenomenon. The constant mode, null at zero, becomes a negative direction as soon as the spectral mass term is present.

This also falsifies the hope that PF-066's exact Schur complement might preserve the zero-energy sign automatically under spectral continuation. The Schur complement is positive at zero because it is the response of a positive bulk Dirichlet energy; `Delta-lambda` no longer supplies that positive bulk form for `lambda>0`.

## 3. The critical line is the universal cusp continuum, not a positivity region

For the hyperbolic spectral parameter,

\[
\lambda=s(1-s),
\]

so on the critical line

\[
\boxed{
\lambda\left(\frac12+it\right)=\frac14+t^2\ge\frac14.
}
\tag{3}
\]

PF-024 proves directly from the normalized cusp zero mode that

\[
\boxed{[1/4,\infty)\subset\sigma_{\rm ess}(\Delta_{X_{\rm prime}}).}
\tag{4}
\]

Indeed a single cusp already contains the half-line model `-d^2/dt^2+1/4`. Thus the entire critical scattering line lies in essential spectrum for a reason independent of the prime construction. Any absolute boundary response there necessarily contains a universal cusp spectral-density component shared by matched non-prime cusp surfaces.

## 4. The positivity that survives continuation is Herglotz positivity, and subtraction loses it

Energy-dependent DtN maps are Weyl--Titchmarsh functions up to the normal-orientation sign convention. In boundary-triple normalization,

\[
\boxed{
\operatorname{Im}M(z)
=(\operatorname{Im}z)\,\gamma(z)^*\gamma(z)\ge0,
\qquad z\in\mathbb C_+.
}
\tag{5}
\]

This is not a positive real quadratic form `M(lambda)>=0`; it is the universal Nevanlinna/Herglotz sign of the imaginary part. Boundary values on continuous spectrum encode positive spectral density, and scattering matrices can be written in terms of those boundary values and `Im M(lambda+i0)`.

The general mechanism is standard. See J. Behrndt, F. Gesztesy, S. Nakamura, *Spectral shift functions and Dirichlet-to-Neumann maps*, Math. Ann. 371 (2018), 1255--1300, DOI `10.1007/s00208-017-1593-4`, and J. Behrndt, M. M. Malamud, H. Neidhardt, *Scattering matrices and Dirichlet-to-Neumann maps*, J. Funct. Anal. 273 (2017), 1970--2025, DOI `10.1016/j.jfa.2017.06.001`.

For Weil positivity this surviving sign is too universal. To isolate prime-sensitive data one would naturally subtract a universal cusp/reference response. But if both `M_X` and `M_0` are Herglotz,

\[
\operatorname{Im}(M_X-M_0)
=
\operatorname{Im}M_X-
\operatorname{Im}M_0,
\tag{6}
\]

which has no sign in general. A difference of positive operator-valued spectral densities is not positive without an additional operator-ordering theorem. Relative DtN, spectral shift, and scattering phase can therefore carry information, but ordinary Weyl theory does not make them automatically nonnegative.

## 5. PF-078's Feshbach mechanism carries information, not a new sign theorem

PF-078 proves the singular marked-scattering limit

\[
\frac{\varepsilon}{\pi}
\Phi_\varepsilon^{\rm mark}
\left(1-\frac{\varepsilon z}{2\pi^2}\right)
\longrightarrow
(G_a-zI)^{-1},
\tag{7}
\]

where `G_a` is the positive weighted path Laplacian carrying the tangent gap data. This is a genuine Mathia-native Feshbach mechanism. But its limit is a resolvent: `(G_a-zI)^(-1)` is positive on the real axis only below the nonnegative graph spectrum (`z<0`) and develops poles/sign changes across the spectrum.

Hence Feshbach reduction packages the arithmetic-geometric information correctly but does not transport the zero-energy DtN positivity to positive spectral energies. In particular, the Schur/Feshbach escape explicitly left open by WP-009 is **not realized by the ordinary Prime-Flute Laplacian DtN/Feshbach machinery**.

## 6. Matched controls, novelty boundary, and surviving route

The no-go survives the relevant controls: the sign change (2) is a generic variational fact; the critical continuum (4) is forced by universal cusp geometry; the Herglotz identity (5) is universal for self-adjoint Weyl functions; and subtracting the universal background gives the unsigned difference (6). None of these facts distinguishes the rational primes.

No novelty is claimed for DtN variational theory, Weyl functions, Herglotz positivity, scattering formulas, or Feshbach reduction. The Mathia-specific durable conclusion is their composition with PF-066, PF-024, and PF-078:

\[
\boxed{
\begin{array}{c}
\text{Prime-Flute zero-energy DtN is positive}\\[2mm]
\Downarrow\ \lambda>0\\[2mm]
\text{real quadratic positivity fails immediately}\\[2mm]
\Downarrow\ \lambda=1/4+t^2\\[2mm]
\text{only universal Herglotz spectral-density positivity remains}\\[2mm]
\Downarrow\ \text{relative subtraction}\\[2mm]
\text{no sign survives without an additional theorem.}
\end{array}
}
\tag{8}
\]

A surviving boundary route therefore needs an additional global structure -- for example a grading/supertrace, a canonical compressed or relative space with an independent ordering theorem, an intersection/cohomological pairing, or a different Mathia-native operator -- whose sign is not inherited from ordinary elliptic Dirichlet energy. It must also couple canonically to the Prime-Lattice finite coefficients `Lambda(p^k)/sqrt(p^k)` and generate the archimedean/polar sector before positivity is invoked.

## 7. Audit / falsification core

The decisive checks are:

1. verify PF-066's zero-energy positivity and exact collar stripping;
2. apply Green's identity to obtain (1);
3. use boundary trace `1` and the constant trial function to obtain (2) for `0<lambda<lambda_1^D`;
4. verify `s=1/2+it -> lambda=1/4+t^2` and PF-024's universal cusp inclusion (4);
5. verify the standard Weyl identity (5), adjusting the harmless global sign for the opposite DtN normal convention if necessary;
6. verify that relative subtraction gives (6) and does not preserve the Herglotz cone;
7. verify PF-078's graph-resolvent limit and its real positivity only below the graph spectrum.

Failure of any of checks 2--7 would reopen the direct DtN/Feshbach route. Otherwise the next boundary-response candidate must contain an additional global sign mechanism rather than inherit positivity from the ordinary Laplacian.