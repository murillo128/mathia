# PC-385 — submesh inverse-power chords have a universal aliasing phase diagram

**Status:** `ASYMPTOTIC-DERIVED` + `DECISIVE-BOUNDARY` for the genuinely submesh regularization regime left open by PC-384.

PC-384 classifies fixed positive inverse powers of the regularized common-anchor chord at exact mesh scale `m eta -> tau>0`. Its explicit remaining loophole is the genuinely submesh regime `eta=eta_m ->0` with `delta_m=m eta_m ->0`, where the singularity is narrower than one inverse-image cell and could in principle interact with the discrete root fiber in a new way.

It does not produce arithmetic information. The normalized root-fiber energy is exactly a pushforward of a one-point singular probability measure, and its nonconstant Fourier coefficients are only high-frequency samples of a positive classical kernel. Submesh behavior is governed by the singularity exponent and scalar combinations of `m` and `eta_m`; prime and composite degrees with the same parameters have the same laws. The only surviving effects are uniformization, a universal anchor spike, or concentration at the anchor.

## 1. Exact pushforward and positivity

For `alpha>0`, set

\[
g_{\alpha,\eta}(\theta)
=\bigl(2(\cosh\eta-\cos\theta)\bigr)^{-\alpha},
\qquad
c_{\alpha,\eta}=\int_{\mathbb T}g_{\alpha,\eta}\,dm,
\tag{1}
\]

and let

\[
(E_m g)(e^{ix})=\frac1m\sum_{j=0}^{m-1}
g\!\left(\frac{x+2\pi j}{m}\right),
\qquad
A_{m,\alpha,\eta}=\frac{E_m g_{\alpha,\eta}}{c_{\alpha,\eta}}.
\tag{2}
\]

Thus `A` is the positive multiplier in the normalized `T^*T` branch of PC-380--PC-384. If

\[
d\mu_{\alpha,\eta}=c_{\alpha,\eta}^{-1}g_{\alpha,\eta}\,dm,
\tag{3}
\]

then exactly

\[
A_{m,\alpha,\eta}\,dm=(z\mapsto z^m)_*\mu_{\alpha,\eta}.
\tag{4}
\]

Writing `rho=e^{-eta}` gives

\[
g_{\alpha,\eta}(\theta)
=\rho^\alpha |1-\rho e^{i\theta}|^{-2\alpha}.
\tag{5}
\]

The binomial expansion of the two factors in (5) shows that every Fourier coefficient of `g_(alpha,eta)` is nonnegative. Root averaging keeps exactly the modes divisible by `m`; hence, after normalization,

\[
A_{m,\alpha,\eta}(x)-1
=2\sum_{k\ge1}a_{mk}(\alpha,\eta)\cos(kx),
\qquad a_{mk}\ge0.
\tag{6}
\]

Consequently the anchor controls uniform flattening:

\[
\boxed{\ \sup_x |A_{m,\alpha,\eta}(x)-1|
=A_{m,\alpha,\eta}(1)-1\ }
\tag{7}
\]

whenever `A(1)>=1`, as it is here by positivity and mean one. There is therefore no hidden angular cancellation capable of rescuing this scalar modulus branch.

## 2. Subcritical singularities: `0<alpha<1/2`

Here the zero-cutoff density is integrable and

\[
c_{\alpha,0}
=\frac{4^{-\alpha}}{\pi}
B\!\left(\frac{1-2\alpha}{2},\frac12\right).
\tag{8}
\]

At the anchor, the `j=0` sample contributes

\[
\frac1m g_{\alpha,\eta_m}(0)
\sim \frac{1}{m\eta_m^{2\alpha}}.
\tag{9}
\]

The remaining samples form the singular trapezoidal sum for the integrable zero-cutoff kernel and converge to `c_(alpha,0)`. With

\[
\lambda_m=m\eta_m^{2\alpha},
\tag{10}
\]

one obtains

\[
A_{m,\alpha,\eta_m}(1)
=1+\frac{1}{c_{\alpha,0}\lambda_m}+o(1)+o(\lambda_m^{-1}).
\tag{11}
\]

Thus `lambda_m -> infinity` gives uniform convergence `A_m ->1`; `lambda_m -> lambda in (0,infinity)` leaves the universal bounded spike `1+1/(c_(alpha,0)lambda)` at the common anchor; and `lambda_m ->0` makes the sup norm diverge. None of these alternatives sees the factorization of `m`.

There is an important distinction between pointwise/sup behavior and mass. Since `g_(alpha,eta)/c_(alpha,eta)` converges in `L^1` to the integrable zero-cutoff density, for every fixed nonzero Fourier mode `k` the coefficient of the pushforward is the source coefficient at frequency `mk`, which tends to zero by Riemann--Lebesgue. Therefore, throughout this entire subcritical regime,

\[
A_{m,\alpha,\eta_m}\,dm \Longrightarrow dm.
\tag{12}
\]

The finite or divergent anchor spike has vanishing mass.

## 3. Critical singularity: `alpha=1/2`

Put

\[
L_m=\log(1/\eta_m),
\qquad M_m=\log m,
\qquad \delta_m=m\eta_m.
\tag{13}
\]

The normalization has the logarithmic asymptotic

\[
c_{1/2,\eta_m}=\frac{L_m}{\pi}+O(1).
\tag{14}
\]

At the anchor, the nonanchor root samples contribute `M_m/pi+O(1)` while the singular sample contributes `1/delta_m+o(1/delta_m)`. Hence

\[
\boxed{
A_{m,1/2,\eta_m}(1)
=\frac{M_m}{L_m}
+\frac{\pi}{\delta_m L_m}
+o\!\left(1+\frac1{\delta_mL_m}\right).
}
\tag{15}
\]

Let `Lambda_m=delta_m L_m`. If `Lambda_m -> infinity`, then necessarily `M_m/L_m ->1`, so (7) gives uniform convergence to `1`. If `Lambda_m -> Lambda in (0,infinity)`, again `M_m/L_m ->1` and the anchor tends to `1+pi/Lambda`. If `Lambda_m ->0`, the anchor diverges. The critical logarithm changes only the scalar threshold; it introduces no arithmetic discriminator.

## 4. Supercritical singularities: `alpha>1/2`

Now the normalization itself is concentrated at the anchor scale:

\[
c_{\alpha,\eta}
\sim C_\alpha\eta^{1-2\alpha},
\qquad
C_\alpha=
\frac{\Gamma(\alpha-1/2)}{2\sqrt\pi\,\Gamma(\alpha)}.
\tag{16}
\]

The single anchor sample therefore gives

\[
\boxed{
A_{m,\alpha,\eta_m}(1)
\sim \frac{1}{C_\alpha\delta_m}
\longrightarrow\infty.
}
\tag{17}
\]

Moreover `mu_(alpha,eta)` lives on angular scale `eta`; after the map `z -> z^m` that scale is `delta_m ->0`. Thus

\[
A_{m,\alpha,\eta_m}\,dm\Longrightarrow\delta_1.
\tag{18}
\]

This is precisely the concentration endpoint `tau ->0` of the wrapped Student-t family in PC-384, not a new arithmetic phase.

## 5. Matched controls and novelty boundary

Every formula above depends on the integer degree only through the sampling mesh and the scalars `m eta_m^(2 alpha)`, `m eta_m`, and logarithms thereof. Replacing a prime degree by a composite degree while keeping those geometric parameters fixed changes nothing. Primitive-shell, divisor, Ramanujan, or conductor data never enter (1)--(18).

The asymptotic mechanism is ordinary singular/near-singular trapezoidal aliasing. A literature audit against generalized Euler--Maclaurin and near-singular quadrature theory found no reason to treat that analytic mechanism as new; the durable mathematical content claimed here is instead the exact Prime-Circle pushforward reduction and the resulting falsification of arithmetic sensitivity. No independent spectral parameter, completed-zeta symmetry, zero-sensitive determinant, or critical-line selector is generated.

The submesh limit therefore closes the remaining scalar inverse-power regularization loophole left by PC-384.

## 6. Consequence for the research frontier

PC-383, PC-384, and the present result classify the shrinking regularized common-anchor inverse-chord modulus across exact-mesh and submesh scaling for every fixed positive inverse power relevant to this branch. Altering only the scalar singularity or its cutoff scale cannot recover prime-sensitive information after root-fiber averaging.

Any surviving use of this geometry must retain information before that scalarization: phase or nonnormal data, source/shell-sensitive profiles, genuinely nonlinear or tensor observables, or cross-level couplings whose arithmetic survives matched prime/composite controls. This finding does not rule out those mechanisms.