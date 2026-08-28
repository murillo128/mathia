# PF-092 — sub-quarter essential spectrum blocks a standard near-one meromorphic Fredholm resolvent

**Status:** `DECISIVE NEGATIVE FOR ABSOLUTE/GLOBAL FREDHOLM-RESONANCE BRANCH + RIGOROUS OPERATOR-THEORETIC CONSEQUENCE`.

PF-043 proved that the fixed infinite prime-flute `X_prime` has infinitely many distinct positive essential spectral values

\[
0<\lambda_j<\frac14,
\qquad
\lambda_j\to0.
\]

They arise from recurrent isolated finite prime tangents and hence are not the universal cusp continuum `[1/4,\infty)` of PF-024. PF-054 further shows that sufficiently hierarchical isolated prime tangents can implant fine gap-ratio-dependent small spectral scales into the same global essential spectrum.

This note records a consequence that had only been stated informally in earlier scattering findings: these sub-quarter essential points **rule out the standard geometrically-finite-style meromorphic Fredholm resolvent/scattering picture in every neighborhood of `s=1` on the physical side**. Consequently the finite-tangent poles approaching `s=1` cannot be promoted to a discrete global resonance divisor of the ordinary `L^2` Laplacian by analytic Fredholm theory.

The statement is elementary once PF-043 is available, but it closes an important branch cleanly.

## 1. Move the essential spectral ladder to the `s`-plane

For every PF-043 value choose the physical root

\[
s_j:=\frac{1+\sqrt{1-4\lambda_j}}2\in\left(\frac12,1\right).
\]

Then

\[
\lambda_j=s_j(1-s_j),
\qquad
s_j\to1,
\]

and in fact

\[
1-s_j=\lambda_j+O(\lambda_j^2).
\]

Consider the natural analytic operator pencil

\[
P(s):=\Delta_{X_{\rm prime}}-s(1-s),
\]

with the usual closed realization

\[
P(s):H^2(X_{\rm prime})\longrightarrow L^2(X_{\rm prime}).
\]

For a self-adjoint Laplacian, the Weyl/Fredholm essential spectrum is exactly the set of real `lambda` for which

\[
\Delta-\lambda:H^2\to L^2
\]

is not Fredholm. Therefore

\[
\boxed{P(s_j)\ \text{is not Fredholm for every }j.}
\]

Since `s_j -> 1`, every neighborhood of `s=1` contains infinitely many such non-Fredholm physical parameters.

Also `0 in sigma_ess(Delta)` by PF-021, so `P(1)=Delta` itself is non-Fredholm.

## 2. Why this kills the standard meromorphic-Fredholm resonance mechanism

The analytic Fredholm theorem gives the familiar scattering/resonance mechanism only on a domain where the underlying analytic operator family is Fredholm: if one value is invertible, the inverse is finitely meromorphic, with isolated poles and finite-rank principal parts. Conversely, a finitely-meromorphic inverse cannot pass through a point at which the operator pencil is non-Fredholm.

But here, in every interval

\[
1-\varepsilon<s<1,
\]

there are infinitely many `s_j` for which `P(s_j)` is non-Fredholm. Hence there is **no neighborhood of `s=1` on the physical `L^2` realization** in which

\[
(\Delta-s(1-s))^{-1}
\]

can be obtained as the inverse of a Fredholm analytic family with merely discrete finite-rank poles.

Equivalently,

\[
\boxed{
\text{the ordinary near-one prime-flute resolvent is not a standard meromorphic-Fredholm resonance problem.}
}
\]

This is stronger than saying that a convenient Selberg product diverges. It is an operator-level obstruction coming from the actual essential spectrum.

## 3. Finite-tangent scattering poles cannot simply become global poles

PF-043 showed that a genus-zero recurrent tangent `Y_H` can have a residual eigenvalue

\[
\lambda_H=s_H(1-s_H),
\qquad \frac12<s_H<1,
\]

which is a genuine pole of the **finite-dimensional scattering matrix of the finite tangent**. Repetition of the isolated prime pattern then transplants `lambda_H` into

\[
\sigma_{\rm ess}(\Delta_{X_{\rm prime}}).
\]

At that stage the spectral character changes:

\[
\boxed{
\text{finite-tangent residual pole}
\longrightarrow
\text{global essential spectral point},
}
\]

not, in general,

\[
\text{finite-tangent pole}
\longrightarrow
\text{finite-rank global resonance pole}.
\]

For the arbitrarily large prime clusters of PF-043 these global non-Fredholm points accumulate at `s=1`.

Thus a proposed global scattering determinant whose ordinary zero/pole divisor simply unions the finite-tangent poles is mathematically incompatible with the `L^2` operator structure.

## 4. Compact renormalizations do not repair the absolute branch

Essential spectrum is invariant under compact perturbations. Consequently replacing `P(s)` by

\[
P(s)+K(s)
\]

with `K(s)` compact cannot make the points `s_j` Fredholm.

Therefore a correction that is only compact/trace-class at operator level cannot turn the **absolute** prime-flute resolvent into the geometrically finite Fredholm situation near `s=1`.

This is relevant to PF-085/PF-087: trace-class endpoint or direct-scattering corrections can define useful **relative** determinants on their own domains, but they cannot erase the underlying sub-quarter essential spectrum of the absolute Laplacian.

## 5. Relation to the known geometrically finite theory

No novelty is claimed for the operator-theoretic implication

\[
\lambda\in\sigma_{\rm ess}(\Delta)
\Longleftrightarrow
\Delta-\lambda\ \text{is non-Fredholm}.
\]

Nor is novelty claimed for analytic Fredholm theory.

The contrast with the standard hyperbolic scattering literature is structural:

- Guillarmou--Mazzeo prove meromorphic continuation of the resolvent, Eisenstein series, and scattering operator for **geometrically finite** hyperbolic manifolds.
- Schulze's degeneration analysis also works at **fixed finite topological type** and uses meromorphic Fredholm theory away from the limit essential spectrum.
- The prime flute is infinitely generated/infinite type and, by PF-043, carries new essential spectrum **strictly below `1/4`**, with nonzero essential points accumulating at `0`.

Directed searches did not locate a theorem that restores a standard finite-rank meromorphic Fredholm resolvent for such a surface across an accumulation of physical sub-threshold essential points. The general Fredholm obstruction says precisely why one should not expect one on ordinary `L^2`.

The project-specific negative result is therefore the composition

\[
\boxed{
\text{recurrent isolated prime tangents}
\to
\lambda_j\in\sigma_{\rm ess}(\Delta),\ \lambda_j\downarrow0
\to
s_j\uparrow1\ \text{non-Fredholm}
\to
\text{no standard near-one absolute resonance divisor}.
}
\]

## 6. What remains alive

This does **not** rule out every generalized scattering construction. In particular it does not exclude:

1. a rigged/weighted-space continuation that deliberately suppresses the escaping Weyl sequences;
2. a **relative** resolvent or spectral-shift theory in which two operators share and cancel the same essential background;
3. local/marked scattering data attached to finite pointed tangents;
4. matrix-valued boundary/Weyl data whose natural singularities need not be finite-rank poles of the global `L^2` resolvent.

But any such construction must explicitly explain how it handles the prime-generated sub-quarter essential spectrum. It cannot simply import the geometrically finite statement that poles near `s=1` form a discrete finite-multiplicity resonance set.

This substantially narrows the global scattering branch: the viable target is now **relative or localized scattering**, not an absolute near-one Selberg/scattering determinant of the standard Fredholm type.

## 7. Interior/exterior duality

The ambient inversion taking the interior to the exterior prime-circle model preserves the intrinsic hyperbolic surface up to isometry, as in PF-017. Hence it preserves the full essential spectrum and the non-Fredholm sequence `s_j -> 1`.

The obstruction is therefore duality-invariant: switching the drawing from the interior to the exterior cannot produce a second Fredholm resonance theory or remove the essential points.
