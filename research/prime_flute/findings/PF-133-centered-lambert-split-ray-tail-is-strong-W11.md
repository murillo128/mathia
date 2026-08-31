# PF-133 — the centered Lambert split-ray tail is strong `W^{1,1}`

**Status:** `EXACT-DERIVED + NEGATIVE/BOUNDARY`. PF-132 proves that the full left/right PF-121 split-ray mismatch has summable `L^infty + \dot W^{1,1}` trace seminorm, but each tail approaches a generally nonzero constant `beta_n-beta_{n+1}` and therefore is not itself `L^1` in Busemann height. The exact tail formula shows that this constant is the **only** nonintegrable deep-cusp mode: after subtracting it, the residual decays exponentially and is summable in the full strong `W^{1,1}` norm over all pants. This removes a specific deep-tail integrability loophole in the accepted wave-operator clue, but does not construct the required two-dimensional boundary-coherent metric comparison or prove the Güneysu--Thalmaier weighted criterion.

## Claim

Use PF-132's exact tail coordinate. For `beta>=0` put

\[
\phi_\beta(\tau)=\operatorname{arcosh}(e^\beta\cosh\tau),
\qquad \tau\ge2,
\tag{1}
\]

and define the centered remainder

\[
R_\beta(\tau)
:=\phi_\beta(\tau)-\tau-\beta.
\tag{2}
\]

For the exact prime/shift-clone Lambert traces let

\[
\beta_n
=\log\frac{\sinh a_n^+}{\sinh a_n},
\qquad
c_n:=\beta_n-\beta_{n+1},
\tag{3}
\]

so PF-132 gives

\[
\sum_n |c_n|<\infty.
\tag{4}
\]

On the full tail, the adjacent split-ray mismatch is

\[
D_n(\tau)
:=\Phi_n(\tau)-\Phi_{n+1}(\tau)
=\phi_{\beta_n}(\tau)-\phi_{\beta_{n+1}}(\tau).
\tag{5}
\]

Then there is an absolute tail constant `C` such that

\[
\boxed{
|D_n(\tau)-c_n|+|D_n'(\tau)|
\le C |c_n|e^{-2\tau},
\qquad \tau\ge2.}
\tag{6}
\]

Consequently

\[
\boxed{
\sum_n
\left(
\int_2^\infty |D_n(\tau)-c_n|\,d\tau
+
\int_2^\infty |D_n'(\tau)|\,d\tau
\right)<\infty.}
\tag{7}
\]

Equivalently, the centered traces `D_n-c_n` form an `ell^1` family in the strong `W^{1,1}([2,\infty))` norm. The nonzero scalar mode `c_n` is the complete obstruction to ordinary Busemann-`L^1` integrability of the exact PF-132 tail.

## 1. Exact centering isolates the only persistent mode

Differentiate (1) with respect to `beta`:

\[
\partial_\beta\phi_\beta(\tau)
=
\frac{\cosh\tau}
{\sqrt{\cosh^2\tau-e^{-2\beta}}}.
\tag{8}
\]

Therefore

\[
\partial_\beta R_\beta(\tau)
=
\left(1-e^{-2\beta}\operatorname{sech}^2\tau\right)^{-1/2}-1.
\tag{9}
\]

For `beta>=0` and `tau>=2`,

\[
0\le e^{-2\beta}\operatorname{sech}^2\tau
\le \operatorname{sech}^2 2<1.
\]

The elementary bound

\[
(1-z)^{-1/2}-1\le C z
\qquad (0\le z\le \operatorname{sech}^2 2)
\tag{10}
\]

gives

\[
\boxed{
|\partial_\beta R_\beta(\tau)|
\le C e^{-2\tau}.}
\tag{11}
\]

Since

\[
D_n(\tau)-c_n
=R_{\beta_n}(\tau)-R_{\beta_{n+1}}(\tau),
\tag{12}
\]

the mean-value theorem in `beta` immediately yields

\[
|D_n(\tau)-c_n|
\le C|c_n|e^{-2\tau}.
\tag{13}
\]

This is stronger than merely knowing that `D_n(\tau)->c_n`: it identifies a uniform exponential approach rate whose coefficient is exactly the adjacent `beta` variation already known to be `ell^1`.

## 2. The derivative residual has the same decay

Direct differentiation in `tau` gives

\[
\partial_\tau\phi_\beta(\tau)
=
\frac{\sinh\tau}
{\sqrt{\cosh^2\tau-e^{-2\beta}}}.
\tag{14}
\]

Differentiating this expression with respect to `beta`,

\[
\partial_\beta\partial_\tau\phi_\beta(\tau)
=
-
\frac{e^{-2\beta}\sinh\tau}
{(\cosh^2\tau-e^{-2\beta})^{3/2}}.
\tag{15}
\]

For `beta>=0`, `tau>=2`, the denominator is uniformly comparable to `cosh^3 tau`, hence

\[
\boxed{
|\partial_\beta\partial_\tau\phi_\beta(\tau)|
\le C e^{-2\tau}.}
\tag{16}
\]

Applying the mean-value theorem between `beta_n` and `beta_{n+1}` gives

\[
|D_n'(\tau)|
\le C|c_n|e^{-2\tau},
\tag{17}
\]

which together with (13) proves (6).

Integrating `e^{-2\tau}` on `[2,\infty)` and then using (4) proves (7).

## 3. Why this matters for the wave-operator gate

PF-132 deliberately stopped at the trace seminorm

\[
\|f\|_{\mathcal T}
=\|f\|_\infty+\int_0^\infty |f'(\tau)|\,d\tau,
\]

because a mismatch converging to a nonzero constant is not `L^1(d\tau)`. That distinction matters in a cusp. In the standard width-one metric

\[
ds^2=d\tau^2+e^{-2\tau}dx^2,
\]

the deep-cusp area density is `e^{-tau}` while the inverse unit-ball-volume factor appearing in the Güneysu--Thalmaier criterion grows at the reciprocal scale. Thus, for a perturbation occupying a fixed normalized horizontal fraction, those two factors cancel at the level of scaling and leave ordinary Busemann measure `d\tau` as the relevant deep-tail integrability test. PF-129 already exploited the complementary fact that a **constant** synchronization mismatch must be killed in a finite Busemann slab rather than propagated to infinite depth.

PF-133 shows that after removing precisely that scalar mode `c_n`, the exact Lambert tail has more than enough one-dimensional decay:

\[
\boxed{
\text{deep trace mismatch}
=
\text{summable scalar mode}
+
\text{summable strong-}W^{1,1}\text{ residual}.}
\tag{18}
\]

So there is no additional slow or oscillatory tail hidden inside the exact `arcosh(e^beta cosh tau)` law that could force divergence merely after the cusp volume cancellation.

This is a **trace-level** statement. It does not assert that an extension of `D_n-c_n` across a two-dimensional interface has pointwise metric deviation bounded by the right-hand side of (6). In particular, a naive vertical displacement varying across a fixed cusp width can acquire an `e^tau` transverse derivative in an orthonormal frame. The remaining wave-operator gate is therefore genuinely the two-dimensional extension/gluing problem, together with the control of globally thin noncanonical regions already isolated in the accepted clue.

## 4. Falsification and controls

The claim is finite and directly checkable:

1. verify the exact PF-132 tail identity (1) for the physical split-ray trace;
2. differentiate to obtain (8), (14), and (15);
3. on `beta>=0`, `tau>=2`, use `e^{-2 beta} sech^2 tau <= sech^2 2` to obtain uniform constants in (11) and (16);
4. apply the mean-value theorem in `beta` to the adjacent exact parameters;
5. use PF-132's proved `sum |beta_n-beta_{n+1}|<infinity`;
6. do **not** replace the centered trace estimate by an unproved two-dimensional extension theorem.

A counterexample would have to invalidate the exact PF-132 tail formula or its `ell^1` first-difference estimate. Extreme neighboring prime gaps do not enter the constants above.

## 5. Prior art and novelty audit

No novelty is claimed for the elementary asymptotics of `arcosh(e^beta cosh tau)` or for the general principle that integrable metric perturbations can preserve scattering data. Güneysu--Thalmaier, *Scattering theory without injectivity radius assumptions, and spectral stability for the Ricci flow* (Ann. Inst. Fourier 70 (2020), 437--456, DOI `10.5802/aif.3316`), prove an integral criterion for existence and completeness of wave operators for quasi-isometric complete metrics without an injectivity-radius lower bound. That theorem is the external target already audited in `SOURCES.md`; it does not turn boundary trace data into a global metric comparison.

Directed checks also recover the standard finite-geometry relative-scattering framework of Borthwick--Judge--Perry and neighboring metric-perturbation scattering theory, but no source found supplies the project-specific implication from this infinite family of Lambert split-ray traces to a boundary-coherent deformation on the zero-systole infinite flute.

The durable contribution here is therefore narrow and project-specific: PF-132 left open whether its nonzero tail limit concealed an additional nonintegrable deep-cusp remainder after centering. Equations (6)--(7) close that loophole exactly. They strengthen the evidence behind the accepted wave-operator clue but do not resolve it, and they carry no independent RH or primality-specific claim.