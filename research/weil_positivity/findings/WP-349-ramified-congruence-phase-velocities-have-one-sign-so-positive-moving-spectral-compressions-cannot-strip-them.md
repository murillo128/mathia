---
id: WP-349
title: Ramified congruence phase velocities have one sign, so positive moving spectral compressions cannot strip them
branch: weil_positivity
status: supported
kind: ramified-phase-positive-compression-no-go
claim_strength: exact critical-line operator inequality from squarefree congruence scattering plus classical inner-function phase monotonicity
created: 2026-09-17
related: [WP-237, WP-242, WP-243, WP-345, WP-346, WP-347, WP-348]
prior_art:
  - Carlo Angelantonj, Ioannis Florakis, and Boris Pioline, Rankin-Selberg methods for closed strings on orbifolds, JHEP 07 (2013) 181, arXiv:1304.4271
  - M. N. Huxley, Scattering matrices for congruence subgroups, in Modular Forms (Durham, 1983), Horwood, 1984, 141-156
  - Tao Qian, Boundary derivatives of the phases of inner and outer functions and applications, Math. Methods Appl. Sci. 32 (2009), 253-263
---

# WP-349 — Ramified congruence phase velocities have one sign, so positive moving spectral compressions cannot strip them

## Claim

`WP-348` left one immediate escape open: although no **fixed** linear channel readout can remove the ramified `Gamma_0(N)` factors while retaining the common completed-zeta logarithmic derivative, perhaps an `s`-dependent positive channel compression could do so on the unitary line.

For the natural operation in which the positive compression is applied **after taking the scattering logarithmic derivative**, that escape is impossible. For every squarefree level `N`, every bad prime `p | N`, and every real `t`, the `p`-local logarithmic-derivative operator is not merely indefinite with a removable channel component: it is **strictly negative definite** in the sign convention of `WP-348`, with a uniform spectral gap.

Consequently any nonzero pointwise positive state, density-matrix readout, or orthogonal compression of the logarithmic-derivative operator retains a strictly nonzero ramified contribution. The compression may vary arbitrarily with `t`; positivity alone prevents cancellation. Thus positive moving spectral weights cannot isolate the common unramified `g'/g` block.

This does **not** rule out differentiating a moving compression chosen before the logarithmic derivative. Such a construction generates derivative-of-projector/connection terms and is a genuinely different mechanism. Nor does the result rule out noncommuting global couplings, nonlinear Schur/determinant constructions, or a different adelic Hilbert category.

**Classification:** `EXACT-DERIVED + CLASSICAL-INNER-PHASE-SIGN + STRICT-LOCAL-OPERATOR-SIGN + MOVING-POSITIVE-COMPRESSION-NO-GO + DECISIVE-NARROWING + NOT-A-WEIL-BRIDGE`.

## 1. Exact local logarithmic derivatives

For squarefree `N`, `WP-242` and `WP-348` give a constant Walsh--Hadamard channel basis in which

\[
\lambda_\varepsilon(s)
=
 g(s)\prod_{p\mid N}\nu_{p,\varepsilon_p}(s),
\qquad
 g(s)=\frac{\zeta^\star(2s-1)}{\zeta^\star(2s)},
\tag{1}
\]

with

\[
\nu_{p,+}(s)=\frac{1+p^{1-s}}{1+p^s},
\qquad
\nu_{p,-}(s)=\frac{p^{1-s}-1}{p^s-1}.
\tag{2}
\]

Write

\[
f_{p,\pm}(s)
:=
\frac{d}{ds}\log \nu_{p,\pm}(s).
\tag{3}
\]

Direct differentiation gives

\[
f_{p,+}(s)
=-\log p\left(
\frac{p^{1-s}}{1+p^{1-s}}
+
\frac{p^s}{1+p^s}
\right),
\tag{4}
\]

and

\[
f_{p,-}(s)
=-\log p\left(
\frac{p^{1-s}}{p^{1-s}-1}
+
\frac{p^s}{p^s-1}
\right).
\tag{5}
\]

Now put

\[
s=\frac12+it,
\qquad
q=\sqrt p>1,
\qquad
\theta=t\log p.
\tag{6}
\]

Then `p^s=q e^{i\theta}` and `p^{1-s}=q e^{-i\theta}` are conjugates. Therefore (4)--(5) become the real quantities

\[
f_{p,+}\left(\frac12+it\right)
=
-2\log p\,
\frac{q^2+q\cos\theta}
{q^2+1+2q\cos\theta},
\tag{7}
\]

and

\[
f_{p,-}\left(\frac12+it\right)
=
-2\log p\,
\frac{q^2-q\cos\theta}
{q^2+1-2q\cos\theta}.
\tag{8}
\]

The denominators are strictly positive because `q>1`. The numerators are also strictly positive because

\[
q^2\pm q\cos\theta
=q(q\pm\cos\theta)>0.
\tag{9}
\]

Hence, pointwise on the complete unitary line,

\[
\boxed{
 f_{p,+}\left(\frac12+it\right)<0,
 \qquad
 f_{p,-}\left(\frac12+it\right)<0.
}
\tag{10}
\]

The sign is not marginal. For both channels the rational factor in (7)--(8) is at least `q/(q+1)`, so

\[
f_{p,\pm}\left(\frac12+it\right)
\le
-c_p,
\qquad
c_p
:=
2\log p\,\frac{\sqrt p}{\sqrt p+1}
>0.
\tag{11}
\]

Thus the bad-prime phase velocity stays uniformly away from zero for all spectral parameters.

## 2. The local operator is strictly negative definite

Let `H_N` be the constant Walsh--Hadamard matrix diagonalizing the squarefree cusp-scattering tensor. In its channel basis define the `p`-local logarithmic-derivative block

\[
D_p(t)
=
\operatorname{diag}
\left(
 f_{p,+}\left(\frac12+it\right),
 f_{p,-}\left(\frac12+it\right)
\right).
\tag{12}
\]

On the full `2^{\omega(N)}`-channel space this acts as

\[
F_p(t)
=
I\otimes\cdots\otimes D_p(t)\otimes\cdots\otimes I.
\tag{13}
\]

Equation (11) gives the operator inequality

\[
\boxed{
F_p(t)\preceq -c_p I
}
\qquad
\text{for every real }t.
\tag{14}
\]

Conjugating by the fixed unitary `H_N` preserves this inequality, so it is not an artefact of choosing the diagonal channel coordinates.

Because the diagonalization is independent of `s`, the full scattering logarithmic derivative decomposes exactly as

\[
A_N(t)
:=
\left.
\Phi_N'(s)\Phi_N(s)^{-1}
\right|_{s=1/2+it}
=
\frac{g'}{g}\left(\frac12+it\right)I
+
\sum_{p\mid N}F_p(t).
\tag{15}
\]

In the present sign convention `A_N(t)` is the Hermitian phase-velocity operator on the unitary axis. Reversing the conventional sign of scattering phase reverses every sign in (10)--(15) simultaneously; the decisive fact is that the two ramified channels have the **same strict sign**.

## 3. Arbitrarily moving positive compressions still cannot strip the bad primes

Let

\[
V(t):\mathbb C^k\longrightarrow\mathbb C^{2^{\omega(N)}}
\tag{16}
\]

be any pointwise isometry. It may depend arbitrarily on `t`; no differentiability assumption is needed because the compression is applied to the already differentiated operator `A_N(t)`. From (14),

\[
V(t)^*F_p(t)V(t)
\preceq
-c_p I_k.
\tag{17}
\]

Therefore

\[
V(t)^*A_N(t)V(t)
=
\frac{g'}{g}\left(\frac12+it\right)I_k
+
\sum_{p\mid N}V(t)^*F_p(t)V(t),
\tag{18}
\]

with

\[
\sum_{p\mid N}V(t)^*F_p(t)V(t)
\preceq
-\left(\sum_{p\mid N}c_p\right)I_k
\prec0.
\tag{19}
\]

Hence no nonzero positive orthogonal compression can satisfy

\[
V(t)^*A_N(t)V(t)
=
\frac{g'}{g}\left(\frac12+it\right)I_k.
\tag{20}
\]

The same statement holds for arbitrary positive scalar states. If `omega_t` is any positive linear functional on the channel matrix algebra with `omega_t(I)>0`, then

\[
\omega_t(F_p(t))
\le
-c_p\,\omega_t(I)<0,
\tag{21}
\]

and therefore

\[
\omega_t(A_N(t))
=
\omega_t(I)\frac{g'}{g}\left(\frac12+it\right)
+
\sum_{p\mid N}\omega_t(F_p(t))
\tag{22}
\]

cannot equal the common zeta contribution alone. In the diagonal basis this is simply the statement that even `t`-dependent nonnegative channel weights cannot cancel terms that are all strictly of one sign.

This strengthens the fixed-channel pole-lattice argument of `WP-348` in exactly the positivity-relevant direction. `WP-348` allowed arbitrary fixed **signed** coefficients and obtained an identity-level no-go in the meromorphic variable `s`. The present result instead works pointwise on the unitary axis but permits arbitrary **moving positive** states and compressions, including non-diagonal density matrices and changing subspaces.

## 4. Adversarial controls and exact boundary of the no-go

**Could the two ramified channels cancel at isolated spectral parameters?** No under positivity. Equations (10)--(11) show that neither channel ever reaches zero and they always have the same sign. Signed coefficients can of course cancel a scalar combination at a selected `t`; that is precisely what positivity forbids.

**Could different bad primes cancel one another?** No. Every `F_p(t)` has the same strict operator sign, so the squarefree tensor sum in (19) becomes more negative as ramified primes are added.

**Could a non-diagonal positive state evade the channel-weight argument?** No. `F_p(t)` is negative definite as an operator. Positivity of a density matrix implies (21) without requiring simultaneous diagonalization of the state.

**Could a moving subspace evade the result?** Not when the operation is `compress A_N(t) at each t`: (17) is pointwise and does not care how `V(t)` moves. But a different operation,

\[
\frac{d}{ds}\log\bigl(V(s)^*\Phi_N(s)V(s)\bigr),
\tag{23}
\]

or differentiation of a moving projected scattering object, contains derivatives of `V(s)` and generally does **not** equal `V^*\Phi_N'\Phi_N^{-1}V`. Berry/connection-type terms may then appear. Equation (19) does not rule out that mechanism. It would need its own source-forced definition, covariance/domain analysis, and independent positivity theorem.

**Does the strict sign itself constitute a new theorem about inner functions?** No. Boundary phase monotonicity of a Blaschke/Mobius factor is classical: its phase derivative is a Poisson kernel of fixed sign. The ramified factors in (2), after the exponential change of spectral variable, are elementary reciprocal inner factors of exactly this type. The new content retained here is the consequence for the Mathia route: the classical one-sign phase property combines with the source-forced squarefree congruence tensor to close positive moving readouts of the post-differentiation operator.

**Does this prove Weil positivity or even give the desired sign?** No. The result is an obstruction. It says that ordinary positive channel geometry cannot use level variation to peel away the finite ramified dressing and expose the common completed-zeta block. The target `g'/g` still carries the desired arithmetic only after scalarization, where inherited unitarity gives a Hermitian phase generator but no Weil-positive quadratic form.

## 5. Prior-art and novelty boundary

The squarefree `Gamma_0(N)` scattering tensor and its local factors are classical; Angelantonj--Florakis--Pioline provide the explicit squarefree formula used in `WP-242`, while Huxley and later congruence-scattering treatments place these factors in the standard arithmetic scattering theory. No novelty is claimed for (1)--(5).

The one-sign boundary phase derivative is also classical inner-function structure. Qian records the standard fact that the derivative of the phase of an elementary Blaschke factor is the Poisson kernel and hence has a fixed sign, extending additively to finite Blaschke products. Equations (7)--(11) are the direct specialization to the ramified congruence factors, with orientation determined by the reciprocal convention.

The line-specific mathematical delta is the operator consequence (14)--(22): once the bad-prime factors are kept as source-defined scattering data, **every pointwise positive compression of the post-differentiation phase generator necessarily retains them**, even when the positive state or subspace moves with the spectral parameter. This is not presented as a new theorem in automorphic scattering; it is the exact no-go needed to audit the open moving-positive-channel escape in `WP-348`.

Targeted searches around congruence scattering, Maaß--Selberg logarithmic derivatives, scattering phase, and inner-function phase derivatives found the classical ingredients but no source asserting this Mathia-specific extraction consequence. The novelty claim is therefore deliberately limited to the synthesis/no-go, not to the local formulas or phase monotonicity.

## 6. Consequence for the research line

The simple level-channel escape is now split cleanly.

A **post-differentiation** source-defined positive compression cannot strip finite ramification: the unwanted local operator is uniformly definite with one sign, so positivity preserves rather than cancels it. To evade this obstruction, a surviving construction must alter the order of operations or the category. The immediate unresolved possibilities are a canonical moving projection/compression differentiated together with the scattering operator, producing genuine connection terms; a noncommuting global finite--archimedean form assembled before scalar logarithmic differentiation; or a different adelic/cohomological object in which unramified and ramified data are separated by intrinsic structure rather than by analytic subtraction.

None of those possibilities inherits a sign theorem from (14). In particular, choosing a moving projector specifically so that its connection term subtracts the known ramified derivative would merely reinsert the desired normalization unless that projector and its positivity are forced independently by the source geometry.
