# AF-291 — Dirichlet eta truncations have a sharp vanishing relative zero-count margin

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `ZERO-COUNT`, `TARGET-RELATIVE`, `CONDITIONING`, `NO-NOVELTY-CLAIM`

## Claim

AF-290 identifies the normalized distance to a boundary-zero collision as the exact local gate from coefficient recovery to finite Dirichlet zero-count fidelity. A natural RH-relevant carrier shows that this target margin can collapse with coefficient breadth even when the limiting analytic function stays uniformly separated from zero on the boundary.

Let

\[
\eta_N(s)=\sum_{n=1}^N(-1)^{n-1}n^{-s},
\qquad
b^{(N)}=\bigl((-1)^{n-1}\bigr)_{n=1}^N,
\]

and let

\[
\eta(s)=\sum_{n\ge1}(-1)^{n-1}n^{-s}
=(1-2^{1-s})\zeta(s),
\qquad \operatorname{Re}s>0.
\]

Fix a compact rectifiable Jordan curve `Gamma` contained in the half-plane `Re(s)>0`, and assume `eta` has no zero on `Gamma`. Write

\[
\alpha:=\min_{z\in\Gamma}\operatorname{Re}z>0.
\]

For the AF-290 coefficient geometry, define

\[
d_{\Gamma,N}
:=\operatorname{dist}_2\!\left(b^{(N)},\Delta_{\Gamma,N}\right),
\]

where `Delta_{Gamma,N}` is the set of coefficient vectors whose degree-`N` Dirichlet polynomial has a zero on `Gamma`, and normalize by

\[
\delta_{\Gamma,N}
:=\frac{d_{\Gamma,N}}{\|b^{(N)}\|_2}.
\]

Then

\[
\boxed{
 d_{\Gamma,N}\asymp \frac{1}{H_N(\alpha)},
 \qquad
 \delta_{\Gamma,N}\asymp
 \frac{1}{\sqrt N\,H_N(\alpha)},
}
\]

where

\[
H_N(x)=\left(\sum_{n\le N}n^{-2x}\right)^{1/2}.
\]

Hence the normalized zero-count margin always tends to zero and has the sharp three-regime scale

\[
\boxed{
\delta_{\Gamma,N}
\asymp
\begin{cases}
N^{-1/2}, & \alpha>1/2,\\[2mm]
(N\log N)^{-1/2}, & \alpha=1/2,\\[2mm]
N^{\alpha-1}, & 0<\alpha<1/2.
\end{cases}
}
\]

The collapse is therefore present even on a fixed contour on which the limiting `eta` function has a positive boundary modulus. It is not caused by the contour drifting toward a zero. It comes from the growing coefficient-space breadth and the norm of the boundary evaluation functional.

Consequently, no breadth-independent relative `ell^2` coefficient-recovery error can, through AF-290 alone, give a breadth-uniform zero-count guarantee for the raw eta truncations. A decoder intended to preserve the zero count on `Gamma` must eventually achieve relative coefficient error on the scale `o(delta_{Gamma,N})`, or use a different source/target geometry whose conditioning theorem is stronger.

## Uniform convergence on compact subsets of `Re(s)>0`

The alternating eta series converges locally uniformly in the open half-plane `Re(s)>0`. For completeness, this can be seen without importing analytic continuation.

Let `K` be compact in `Re(s)>0`, with

\[
\sigma_0:=\min_{s\in K}\operatorname{Re}s>0,
\qquad
M:=\max_{s\in K}|s|.
\]

Pair adjacent terms. For every `k`,

\[
(2k-1)^{-s}-(2k)^{-s}
=
\int_{2k-1}^{2k}s\,x^{-s-1}\,dx,
\]

so uniformly for `s in K`,

\[
\left|(2k-1)^{-s}-(2k)^{-s}\right|
\le
M(2k-1)^{-\sigma_0-1}.
\]

The majorant is summable. The paired partial sums therefore converge uniformly on `K`, and the difference between an odd and the preceding even partial sum is at most `N^{-sigma_0}`, which also tends uniformly to zero. Thus `eta_N -> eta` locally uniformly on `Re(s)>0`.

Since `Gamma` is compact and `eta` is nonzero there,

\[
m:=\min_{z\in\Gamma}|\eta(z)|>0.
\]

Uniform convergence gives, for all sufficiently large `N`, constants independent of `N` such that

\[
0<c\le |\eta_N(z)|\le C<\infty
\qquad(z\in\Gamma).
\]

This is the key point: the raw analytic boundary values stay uniformly well separated from zero while the normalized coefficient-space margin still collapses.

## AF-290 turns boundary separation into an exact coefficient-space scale

AF-290 gives the exact distance formula

\[
d_{\Gamma,N}
=
\min_{z\in\Gamma}
\frac{|\eta_N(z)|}{H_N(\operatorname{Re}z)}.
\]

Because `H_N(x)` is decreasing in `x`,

\[
H_N(\operatorname{Re}z)\le H_N(\alpha)
\qquad(z\in\Gamma).
\]

The uniform lower boundary bound therefore yields

\[
d_{\Gamma,N}\ge \frac{c}{H_N(\alpha)}.
\]

Choose `z_* in Gamma` with `Re(z_*)=alpha`, which exists by compactness. The uniform upper bound gives

\[
d_{\Gamma,N}
\le
\frac{|\eta_N(z_*)|}{H_N(\alpha)}
\le
\frac{C}{H_N(\alpha)}.
\]

Hence

\[
d_{\Gamma,N}\asymp H_N(\alpha)^{-1}.
\]

For the eta coefficient vector,

\[
\|b^{(N)}\|_2=\sqrt N,
\]

so

\[
\delta_{\Gamma,N}
\asymp
\frac{1}{\sqrt N\,H_N(\alpha)}.
\]

Using the elementary asymptotics already isolated in AF-290,

\[
H_N(\alpha)
\asymp
\begin{cases}
1, & \alpha>1/2,\\
(\log N)^{1/2}, & \alpha=1/2,\\
N^{1/2-\alpha}, & 0<\alpha<1/2,
\end{cases}
\]

gives the three displayed decay laws.

The result is invariant under global rescaling of the coefficient vector: scaling all coefficients multiplies both `d_{Gamma,N}` and `||b^(N)||_2` by the same factor. Thus the decay is not an artifact of having chosen coefficients of magnitude one.

## Critical-strip consequence

The alternating representation is a particularly useful stress test because it reaches the critical strip directly. If the closure of the Jordan domain `Omega` bounded by `Gamma` lies in

\[
0<\operatorname{Re}s<1,
\]

then the factor `1-2^{1-s}` is nonzero throughout `Omega` and on its boundary. In that region, `eta` and `zeta` have exactly the same zeros with the same multiplicities.

Therefore `Gamma` may be chosen as a fixed zero-free boundary enclosing any prescribed finite collection of zeta zeros in the open critical strip. The eta truncations converge uniformly on that boundary and eventually have the same interior zero count by the ordinary Rouché/Hurwitz mechanism, yet their **relative coefficient-space protection radius still tends to zero at the scale above**.

For a contour whose left edge is

\[
\alpha=\frac12-\varepsilon,
\qquad 0<\varepsilon<\frac12,
\]

the relative protection radius is

\[
\delta_{\Gamma,N}\asymp N^{-1/2-\varepsilon}.
\]

Thus analytic convergence to the correct critical-strip zero count and stable recoverability from relative coefficient error are distinct statements. The first can hold on a fixed contour while the second becomes increasingly ill conditioned as the coefficient breadth grows.

## Information-theoretic interpretation

This gives a concrete answer to the current Arithmetic Fidelity question of whether a natural RH-relevant approximant can keep a nontrivial normalized distance from its target discriminant as breadth grows.

For raw eta truncation, it cannot. The target has two separate margins:

1. the function-space boundary margin `min_Gamma |eta_N|`, which remains bounded below on a fixed zero-free contour; and
2. the coefficient-space boundary-zero margin normalized by source size, which vanishes because the evaluation functional sees an expanding set of Dirichlet coordinates.

The distinction is structurally important. A source representation can converge perfectly in the analytic topology consumed by the final zero-count observable while becoming arbitrarily fragile in a stronger upstream coefficient metric. Calling the source representation "well conditioned" or "compressed" without naming the target metric therefore conflates two different resources.

This also sharpens the breadth bill identified in AF-275--AF-290. Recovering more coefficient coordinates can increase source completeness while simultaneously shrinking the relative perturbation radius within which a zero-count target is protected. More source information is not automatically more target robustness.

## Prior art and novelty assessment

The ingredients are classical and no general novelty is claimed.

- NIST DLMF §25.2(ii), Eq. 25.2.3, records the alternating representation
  `zeta(s)=(1-2^(1-s))^(-1) sum_{n>=1}(-1)^(n-1)n^(-s)` for `Re(s)>0`, citing Apostol. This supplies the standard eta/zeta bridge used here.
- The zeros of finite eta partial sums are already an active subject. Eric Dubon, **"A note on the density of zeros of partial sums of the Dirichlet lambda, beta and eta functions,"** *European Journal of Mathematics* 11, 29 (2025), DOI `10.1007/s40879-025-00821-0`, studies the critical intervals and density of real parts of zeros of `eta_N` and related Dirichlet polynomials. Thus neither the use of eta partial sums nor their zero geometry is new.
- AF-290 already supplies the exact coefficient-space distance-to-boundary-zero formula and its distance-to-ill-posedness interpretation. The present result is a specialization of that theorem to a natural RH-relevant sequence of source vectors plus a compact-uniform convergence argument.

The retained Arithmetic Fidelity contribution is the **quantitative composition**: on every fixed zero-free contour in `Re(s)>0`, the exact normalized AF-290 zero-count radius of the eta partial sums has an explicit vanishing breadth law, even though the analytic boundary modulus converges to a positive limit. The literature audit found established work on eta partial-sum zeros and their density, not a claim that this relative `ell^2` distance-to-discriminant remains bounded below. No novelty claim is made beyond recording this exact channel-specific consequence inside the Arithmetic Fidelity framework.

## Boundaries and failure modes

- The theorem concerns the raw coefficient geometry of the standard eta truncations. It does not prove that every RH-relevant approximation has a collapsing target margin.
- The result is target-relative. A different coefficient norm, preconditioner, nonlinear representation, or quotient changes the dual evaluation norm and therefore requires its own conditioning theorem.
- The vanishing normalized radius does not imply that `eta_N` has the wrong zeros on a fixed contour. Uniform convergence gives the opposite: once the boundary is zero-free, the zero count eventually stabilizes. The theorem says that this correct count is not protected against a breadth-independent relative `ell^2` coefficient perturbation.
- The statement is local to fixed compact contours. It does not control zero locations, multiplicities, matching over growing-height windows, or a global zero divisor.
- The eta factor introduces additional zeros on `Re(s)=1`. The clean zeta-zero interpretation above is restricted to domains compactly contained in `0<Re(s)<1`, where that factor is nonvanishing.
- Nothing here proves RH or supplies a route from eta truncations to RH. It is a conditioning obstruction for one natural source-to-zero-count channel.
