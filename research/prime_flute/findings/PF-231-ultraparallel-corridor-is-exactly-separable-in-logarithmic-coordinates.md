# PF-231 — ultraparallel corridor is exactly separable in logarithmic coordinates

**Status:** `EXACT-DERIVED + CONFORMAL-REDUCTION + OPERATOR-CALIBRATION + POSITIVE/ROUTE-NARROWING`. PF-230 shows that neighboring cuff axes have a genuinely variable `cosh(t)` Fermi-width profile on fixed windows and therefore cannot be replaced by a constant-width strip by a naive small-`s` metric perturbation. That variable Fermi graph is nevertheless not an intrinsic obstruction to the shifted axis-to-axis boundary problem. After an exact hyperbolic isometry and the conformal coordinate `w=log z`, the complete corridor between two ultraparallel axes at distance `s` is the rectangle

\[
(0,s)\times(0,\pi)
\]

with metric

\[
\boxed{g=\frac{dx^2+d\theta^2}{\sin^2\theta}.}
\]

For the shifted form associated with `-\Delta_g+1`, two-dimensional conformal cancellation gives

\[
\boxed{
\mathfrak q_s[u]
=\int_0^s\!\int_0^\pi
\left(
|\partial_xu|^2+|\partial_\theta u|^2+\csc^2\theta\,|u|^2
\right)d\theta\,dx.
}
\]

Thus the untrimmed corridor is **exactly separable**:

\[
(-\partial_x^2+A)u=0,
\qquad
A=-\partial_\theta^2+\csc^2\theta.
\]

If `K=A^{1/2}` is the Friedrichs square root on `L^2((0,\pi),d\theta)`, its two-axis form Dirichlet-to-Neumann matrix is exactly

\[
\boxed{
\Lambda_s
=K
\begin{pmatrix}
\coth(sK)&-\operatorname{csch}(sK)\\
-\operatorname{csch}(sK)&\coth(sK)
\end{pmatrix}.
}
\]

Moreover `A` is the elementary trigonometric Pöschl--Teller operator. With

\[
\alpha:=\frac{1+\sqrt5}{2},
\qquad
\alpha(\alpha-1)=1,
\]

its exact eigenvalues are

\[
\boxed{\lambda_m(A)=(m+\alpha)^2,\qquad m=0,1,2,\ldots.}
\]

Consequently the axis-to-axis cross block has exact mode amplitudes

\[
\boxed{
\kappa_m\operatorname{csch}(s\kappa_m),
\qquad
\kappa_m=m+\alpha,
}
\]

and the natural `s\kappa_m=O(1)` population is `O(s^{-1})`, with exponential decay beyond that band. PF-230's `\pi/s` Fermi inverse-width asymptotic is therefore consistent with an exact conformal rectangle of aspect `\pi/s`; the coefficient `\pi` is the conformal tangential length, not evidence for an additional logarithmic channel supply.

The PF-205 natural-width artificial boundaries also have an exact global description in these coordinates. If they are at inward hyperbolic distances `\rho_1,\rho_2` from the two axes, put

\[
f_\rho(\theta)
:=\operatorname{arsinh}(\sinh\rho\,\sin\theta).
\]

Then the trimmed corridor is exactly

\[
\boxed{
\Omega_{s,\rho_1,\rho_2}
=\left\{(x,\theta):
 f_{\rho_1}(\theta)<x<s-f_{\rho_2}(\theta),
\ 0<\theta<\pi
\right\}.
}
\]

Its Euclidean-coordinate width is

\[
a_s(\theta)
=s-f_{\rho_1}(\theta)-f_{\rho_2}(\theta).
\]

If `\rho_1+\rho_2\le\eta s` for some fixed `\eta<1`, then globally

\[
\boxed{(1-\eta)s\le a_s(\theta)\le s,}
\qquad
\boxed{|f_\rho'(\theta)|\le\sinh\rho.}
\]

For `\rho_i=O(s)`, uniformly on the **whole** interval `0\le\theta\le\pi`,

\[
\boxed{
a_s(\theta)
=s-(\rho_1+\rho_2)\sin\theta+O(s^3).}
\]

In particular the PF-205 trim does not create a hidden logarithmic width budget:

\[
\boxed{
\frac{\pi}{s}
\le
\int_0^\pi\frac{d\theta}{a_s(\theta)}
\le
\frac{\pi}{(1-\eta)s}.
}
\]

This does **not** prove the actual dressed `w/s` estimate sought after PF-228. The artificial hypercycles are variable graph boundaries in logarithmic coordinates, and straightening them produces tangential/transverse coupling. The exact reduction instead isolates where the remaining geometry can enter: the PF-205 hypercycle trim and its boundary normalizers, physical `P/H` projections, neighboring-cell inhomogeneity, and global Schur inversion. The hyperbolic axis fanout itself is no longer a candidate mechanism for destroying the corridor transfer law.

## Claim

Let `\gamma_0,\gamma_s\subset\mathbb H^2` be disjoint geodesics whose common-perpendicular distance is `s>0`, and let `\mathcal C_s` be the component between them. Then:

1. There is an isometry of `\mathbb H^2` sending the axes in the upper-half-plane model to
   \[
   \gamma_0=\{|z|=1,\ \Im z>0\},
   \qquad
   \gamma_s=\{|z|=e^s,\ \Im z>0\}.
   \]
   The branch `w=\log z=x+i\theta`, `0<\theta<\pi`, maps `\mathcal C_s` onto `(0,s)\times(0,\pi)` and gives the metric above.
2. The shifted quadratic form and operator separate exactly as stated, and the form DtN matrix is the functional-calculus matrix `\Lambda_s` above.
3. The Friedrichs realization of `A=-\partial_\theta^2+\csc^2\theta` has eigenvalues `(m+\alpha)^2`, so the untrimmed cross-DtN channel count on every fixed scaled band `s\kappa_m\le Z` is
   \[
   \#\{m:s(m+\alpha)\le Z\}
   =\frac Zs+O(1).
   \]
4. The inward equidistant curves at distances `\rho_1,\rho_2` are the exact logarithmic graphs `x=f_{\rho_1}(\theta)` and `x=s-f_{\rho_2}(\theta)`. The global width bounds and uniform small-`s` expansion above follow.
5. After straightening the trimmed domain by
   \[
   x=f_{\rho_1}(\theta)+a_s(\theta)X,
   \qquad 0<X<1,
   \]
   and writing
   \[
   b_s(X,\theta)=f_{\rho_1}'(\theta)+a_s'(\theta)X,
   \]
   the shifted energy is exactly
   \[
   \boxed{
   \int_0^1\!\int_0^\pi
   \left[
   a_s^{-1}|v_X|^2
   +a_s\left|v_\theta-\frac{b_s}{a_s}v_X\right|^2
   +a_s\csc^2\theta\,|v|^2
   \right]d\theta\,dX.
   }
   \]
   Under the PF-205 scale `\rho_i=O(s)` with `\rho_1+\rho_2\le\eta s`, one has `a_s\asymp s` and `b_s=O(s)` uniformly. There is therefore no untracked geometric blow-up beyond the explicit thin-width scaling, although the order-one ratio `b_s/a_s` means mode mixing cannot simply be discarded.

For the canonical neighboring prime-flute cuffs, take `s=s_n=(h_n+h_{n+1})/2` as in PF-215/PF-230 and the PF-205 inward distances `\rho_n,\rho_{n+1}`. PF-230 gives ` (\rho_n+\rho_{n+1})/s_n\le\kappa+o(1)` with fixed `\kappa<1/4`, so the uniform trimmed-corridor bounds apply after a finite head.

## 1. Exact logarithmic rectangle

Any two ultraparallel geodesics are isometric to nested semicircles centered at the origin. Scaling fixes the inner radius to one. Along the imaginary common perpendicular, hyperbolic distance is

\[
\int_1^{e^s}\frac{dr}{r}=s,
\]

so the outer radius is `e^s`.

Write

\[
z=e^{x+i\theta},
\qquad
0<\theta<\pi.
\]

Then

\[
|dz|^2=e^{2x}(dx^2+d\theta^2),
\qquad
\Im z=e^x\sin\theta.
\]

The upper-half-plane metric `g=|dz|^2/(\Im z)^2` therefore becomes

\[
\boxed{g=\csc^2\theta\,(dx^2+d\theta^2),}
\tag{1}
\]

while `1<|z|<e^s` is exactly `0<x<s`. This is a global identity, not a thin-corridor approximation.

PF-230's Fermi graph `r_s(t)\sim s\cosh t` and the logarithmic rectangle describe the same region in different coordinates. The nonconstant Fermi width is real as a normal-distance statement, but it does not imply a nonseparable conformal principal energy for the full axis corridor.

## 2. The shifted energy is exactly separable

In two dimensions, for a conformal metric `g=e^{2\varphi}(dx^2+d\theta^2)`, the gradient part of the Dirichlet energy is conformally invariant. With `e^{2\varphi}=\csc^2\theta`,

\[
|\nabla_gu|_g^2\,d\mu_g
=(|u_x|^2+|u_\theta|^2)\,dx\,d\theta,
\]

and

\[
|u|^2d\mu_g
=\csc^2\theta\,|u|^2dx\,d\theta.
\]

Hence the `-\Delta_g+1` energy is exactly

\[
\mathfrak q_s[u]
=\int_0^s\!\int_0^\pi
\left(
|u_x|^2+|u_\theta|^2+\csc^2\theta|u|^2
\right)d\theta\,dx,
\tag{2}
\]

and the interior equation is

\[
(-\partial_x^2+A)u=0,
\qquad
A=-\partial_\theta^2+\csc^2\theta.
\tag{3}
\]

The ideal endpoints `\theta=0,\pi` are encoded by the Friedrichs form of `A`; the singular potential forces the finite-energy endpoint behavior and no extra arbitrary boundary condition is inserted there.

Let `K=A^{1/2}`. Solving (3) by functional calculus on `[0,s]` gives, for boundary data `(f_0,f_s)`, the boundary energy pairing with

\[
\Lambda_s
=K
\begin{pmatrix}
\coth(sK)&-\operatorname{csch}(sK)\\
-\operatorname{csch}(sK)&\coth(sK)
\end{pmatrix}.
\tag{4}
\]

This is the exact analogue of PF-228's straight-corridor matrix. The statement is made in the natural flat `d\theta` pairing supplied by (2). If one represents normal derivatives instead on the physical geodesic measure `ds_g=d\theta/\sin\theta`, multiplication/conjugation by the boundary density changes the operator representation; no physical-`L^2(ds_g)` singular-value claim is being smuggled into (4).

## 3. Exact transverse spectrum

Set

\[
\alpha=\frac{1+\sqrt5}{2},
\qquad
\alpha(\alpha-1)=1.
\tag{5}
\]

For `m\ge0`, define

\[
\phi_m(\theta)
=(\sin\theta)^\alpha C_m^\alpha(\cos\theta),
\tag{6}
\]

where `C_m^\alpha` is the Gegenbauer polynomial. The Gegenbauer differential equation gives directly

\[
A\phi_m=(m+\alpha)^2\phi_m.
\tag{7}
\]

The change `x=\cos\theta` turns their `L^2(d\theta)` orthogonality into the standard Gegenbauer weight `(1-x^2)^{\alpha-1/2}dx`, so these modes form the Friedrichs eigenbasis. Thus

\[
\operatorname{spec}A
=\{(m+\alpha)^2:m\ge0\}.
\tag{8}
\]

The cross block in (4) therefore has exact scalar amplitudes

\[
c_m(s)=\frac{m+\alpha}{\sinh(s(m+\alpha))}.
\tag{9}
\]

For `s(m+\alpha)=O(1)`, `c_m(s)` is of order `1/s`; once `s(m+\alpha)\gg1`, it decays exponentially in the scaled frequency. In particular the number of modes with `s(m+\alpha)\le Z` is `Z/s+O(1)` for fixed `Z`.

This does not yet contain PF-228's decisive **normalized dressed** factor `w/s`: equation (9) is the raw two-axis shifted DtN cross block. Its role is to show that exact hyperbolic axis geometry already has the same `z/\sinh z` transfer shape before the PF-205 boundary-energy normalization is imposed.

## 4. Exact PF-205 hypercycle graphs

For `z=e^{x+i\theta}`, the signed distance to the unit semicircle satisfies

\[
\sinh d_0(z)
=\frac{|z|^2-1}{2\Im z}
=\frac{\sinh x}{\sin\theta}.
\tag{10}
\]

Therefore the inward equidistant curve `d_0=\rho` is exactly

\[
x=f_\rho(\theta)
:=\operatorname{arsinh}(\sinh\rho\,\sin\theta).
\tag{11}
\]

After scaling by `e^{-s}`, the corresponding formula for the outer axis gives the inward graph

\[
x=s-f_\rho(\theta).
\tag{12}
\]

Hence the PF-205-style doubly trimmed corridor has exact width

\[
a_s(\theta)
=s-f_{\rho_1}(\theta)-f_{\rho_2}(\theta).
\tag{13}
\]

Since `0\le\sin\theta\le1`,

\[
0\le f_\rho(\theta)\le\rho,
\tag{14}
\]

and differentiation gives

\[
f_\rho'(\theta)
=\frac{\sinh\rho\cos\theta}
{\sqrt{1+\sinh^2\rho\sin^2\theta}},
\tag{15}
\]

so `|f_\rho'|\le\sinh\rho`. If `\rho_1+\rho_2\le\eta s< s`, equations (13)--(14) give

\[
(1-\eta)s\le a_s(\theta)\le s
\tag{16}
\]

globally, including the cusp-side ends `\theta\to0,\pi`.

For `\rho=O(s)`, Taylor expansion is uniform because `|\sin\theta|\le1`:

\[
f_\rho(\theta)
=\rho\sin\theta+O(s^3).
\tag{17}
\]

This proves the stated uniform width expansion. Equation (16) also yields immediately

\[
\frac\pi s
\le
\int_0^\pi\frac{d\theta}{a_s(\theta)}
\le
\frac{\pi}{(1-\eta)s}.
\tag{18}
\]

Unlike PF-230's Fermi-normal calculation, (11)--(18) cover the entire logarithmic tangential interval. They are still geometric identities and bounds, not a DtN singular-value theorem for the trimmed domain.

## 5. Exact fixed-domain form after trimming

Put

\[
x=f_{\rho_1}(\theta)+a_s(\theta)X,
\qquad 0<X<1,
\tag{19}
\]

and write `u(x,\theta)=v(X,\theta)`. At fixed physical `x`,

\[
\partial_xu=\frac1{a_s}v_X,
\qquad
\partial_\theta u
=v_\theta-\frac{b_s}{a_s}v_X,
\qquad
b_s=f_{\rho_1}'+a_s'X.
\tag{20}
\]

Since `dx\,d\theta=a_s\,dX\,d\theta`, substitution into (2) gives the exact fixed-domain form

\[
\mathfrak q_s[v]
=\int_0^1\!\int_0^\pi
\left[
 a_s^{-1}|v_X|^2
 +a_s\left|v_\theta-\frac{b_s}{a_s}v_X\right|^2
 +a_s\csc^2\theta|v|^2
\right]d\theta\,dX.
\tag{21}
\]

For the canonical PF-205 regime, (15)--(16) give

\[
a_s\asymp s,
\qquad
b_s=O(s),
\qquad
\frac{b_s}{a_s}=O(1)
\tag{22}
\]

uniformly. Thus there is no logarithmic coefficient blow-up hidden in the hyperbolic fanout. But `b_s/a_s` need not tend to zero, and modes with tangential scale `1/s` are exactly the critical population. Equation (21) therefore forbids the opposite overclaim as well: exact conformal straightening of the axes does **not** justify replacing the PF-205 trimmed problem by a diagonal Fourier model.

## 6. Prior-art and novelty audit

The logarithmic strip/band model of the hyperbolic plane and conformal invariance of two-dimensional Dirichlet energy are classical. The one-dimensional operator in (3) is a trigonometric Pöschl--Teller system; the classical solvable-potential literature goes back to G. Pöschl and E. Teller, *Bemerkungen zur Quantenmechanik des anharmonischen Oszillators*, Zeitschrift für Physik 83 (1933), 143--151, DOI `10.1007/BF01331132`. A structure-directed search did not identify a literature theorem whose content is the PF-specific weak-ideal conclusion sought here.

No novelty is claimed for the strip coordinate, the Pöschl--Teller spectrum, or the general functional-calculus DtN formula on a product cylinder. Equations (1)--(9) are recorded because they identify the exact operator model of the **specific PF-230 neighboring-axis corridor**. Equations (10)--(21) are the project-specific bridge to the PF-205 artificial seam geometry. The durable delta is the localization of the remaining obstruction: variable hyperbolic axis fanout is removable exactly; the actual difficulty begins with the hypercycle trim/boundary normalization and subsequent noncommutative/global reassembly.

## 7. Falsification and boundary checks

1. The exact separability and mode formula (4)--(9) apply to the **untrimmed axis-to-axis corridor**. They are not asserted for the PF-205 trimmed interfaces.
2. The form DtN matrix uses the `d\theta` pairing naturally produced by the conformal energy. Converting to a physical boundary `L^2(ds_g)` realization requires the appropriate boundary-density identification.
3. The Pöschl--Teller spectrum controls the axis corridor's separated modes. It does not identify the physical `P/H` decomposition used in PF-212/PF-221.
4. The global width estimate (16) assumes `\rho_1+\rho_2<s`; PF-230 verifies a stronger uniform tail inequality for the canonical PF-205 choice.
5. The coordinate inverse-width estimate (18) is not a Weyl law or singular-value count for the trimmed DtN map.
6. Straightening the hypercycle boundaries gives the order-one coupling `b_s/a_s`; no claim is made that mode mixing is perturbatively small at the critical `1/s` tangential scale.
7. Nothing here proves the PF-228 `w/s` factor for the actual normalized pant, nested weak `\mathcal S_{1,\infty}` reassembly, prime/clone separation, wave-operator completeness, determinant/resonance control, or any RH implication.

## Consequences for the research line

PF-230's variable Fermi fanout was a real warning against a naive constant-width metric perturbation, but it is not itself the missing operator obstruction. Before artificial trimming, the neighboring-axis `-\Delta+1` boundary problem is exactly a separable conformal rectangle with a Pöschl--Teller transverse operator and the same hyperbolic `z/\sinh z` transmission shape that underlies PF-228's favorable control. The natural `O(s^{-1})` axis channel scale is exact.

The first smooth-route gate can therefore be sharpened again. It is no longer necessary to compare an arbitrary variable hyperbolic pant directly with a flat cylinder. In the exact logarithmic coordinates, the metric part has already been removed. What must now be quantified is whether PF-228's normalized `w/s` Schur gain survives replacing the straight boundaries by the explicit PF-205 hypercycle graphs (11)--(13), together with the real neighboring boundary-energy operators and physical projections. Equation (21) is a concrete fixed-domain starting form for that comparison. Only after this one-cut problem is settled does the PF-222 nested weak-trace reassembly become the next independent gate.