# WP-131 — Bounded radial–solenoid Gamma intertwiners vanish by spectral type

**Status:** `EXACT-DERIVED + CROSS-LINE-BRIDGE + DECISIVE-NEGATIVE + SPECTRAL-TYPE-OBSTRUCTION + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION`.

`WP-130` proves that the Prime-Circle solenoid Gamma generator

\[
G_\Sigma=F(\Delta_{\rm leaf})
\]

and the radial/log-scale Gamma generator

\[
G_{\mathbb R}=F(-\partial_x^2)
\]

have incompatible canonical spectral types: the first is pure point in the rational character basis, while the second is continuous in the Fourier/Mellin variable. It therefore rules out a unitary identification, but explicitly leaves open a nonunitary measure-changing transform or boundary map that might intertwine the two geometries.

For **bounded exact Hilbert-space intertwiners**, that escape is actually empty. Fix any heat time `tau>0` and put

\[
T_\Sigma(\tau)=e^{-\tau G_\Sigma},
\qquad
T_{\mathbb R}(\tau)=e^{-\tau G_{\mathbb R}}.
\]

Then

\[
\boxed{
X T_\Sigma(\tau)=T_{\mathbb R}(\tau)X,
\quad
X:L^2(\Sigma_{\mathbb Q})\to L^2(\mathbb R)
\text{ bounded}
\Longrightarrow X=0,
}
\]

and likewise

\[
\boxed{
Y T_{\mathbb R}(\tau)=T_\Sigma(\tau)Y,
\quad
Y:L^2(\mathbb R)\to L^2(\Sigma_{\mathbb Q})
\text{ bounded}
\Longrightarrow Y=0.
}
\]

The proof is elementary and exact. The solenoid semigroup has a complete orthonormal eigenbasis `chi_q`, `q in Q`. The radial semigroup is Fourier multiplication by

\[
m_\tau(\xi)=e^{-\tau H_\infty(\xi)},
\]

and `WP-129` proves that `H_infty` is even and strictly increasing in `|xi|`. Every level set of `m_tau` therefore has Lebesgue measure zero, so the radial semigroup has **no nonzero `L^2` eigenvectors**. An intertwiner must send each solenoid eigenvector to a radial eigenvector with the same eigenvalue, hence to zero. Completeness of the characters gives `X=0`; the reverse direction follows by taking adjoints.

Thus the spectral mismatch in `WP-130` is stronger than failure of unitary equivalence. No bounded change of Hilbert-space representation can exactly transport the canonical solenoid Gamma dynamics to the radial Gamma dynamics, or conversely, while respecting even one nontrivial heat-semigroup time.

This does **not** rule out an unbounded/distributional generalized-eigenfunction transform, a boundary operator that is not an exact intertwiner, a quotient/compression changing the generator, or a genuinely nonseparable radial–leaf/finite–archimedean construction. Those mechanisms would be additional geometry rather than a hidden bounded identification of the two existing Gamma operators. No global Weil positivity theorem follows here.

## 1. Exact bounded semigroup models avoid unbounded-domain ambiguity

`WP-129` defines

\[
H_\infty(t)
=\operatorname{Re}\psi\!\left(\frac14+\frac{it}{2}\right)-\psi\!\left(\frac14\right)
=F(t^2),
\]

with `F` a strictly increasing complete Bernstein function. `WP-130` then compares two nonnegative self-adjoint generators.

On the radial/log-scale side,

\[
G_{\mathbb R}=F(-\partial_x^2)
\]

on `L^2(R,dx)`. Under Fourier transform,

\[
\widehat{G_{\mathbb R}f}(\xi)
=H_\infty(\xi)\widehat f(\xi).
\]

On the solenoid side, `PC-065` supplies the canonical leafwise Laplacian

\[
\Delta_{\rm leaf}\chi_q=(2\pi q)^2\chi_q,
\qquad q\in\mathbb Q,
\]

and therefore

\[
G_\Sigma\chi_q=H_\infty(2\pi q)\chi_q.
\]

Rather than formulate an intertwining relation directly for these unbounded generators, fix any `tau>0`. Functional calculus gives bounded self-adjoint contractions

\[
T_{\mathbb R}(\tau)=e^{-\tau G_{\mathbb R}},
\qquad
T_\Sigma(\tau)=e^{-\tau G_\Sigma}.
\]

The obstruction below is already exact for this single bounded time slice. Any stronger bridge that genuinely intertwines the full heat dynamics must in particular pass this test.

## 2. The radial Gamma heat operator has no point spectrum

Fourier transform identifies `T_R(tau)` with multiplication by

\[
\boxed{
m_\tau(\xi)=e^{-\tau H_\infty(\xi)}.
}
\]

`WP-129` proves that `H_infty(0)=0`, that `H_infty` is continuous, and that it is strictly increasing as a function of `|xi|` from `0` to `infinity`. Hence `m_tau` is continuous, equals `1` only at `xi=0`, tends to `0` as `|xi|->infinity`, and is strictly decreasing in `|xi|`.

For any scalar `lambda`, the level set

\[
\{\xi\in\mathbb R:m_\tau(\xi)=\lambda\}
\]

is empty, a singleton, or a pair `{+-xi_lambda}`. In every case it has Lebesgue measure zero. If a multiplication operator `M_m` on `L^2(R,d xi)` had a nonzero eigenvector `f` with eigenvalue `lambda`, then

\[
(m(\xi)-\lambda)f(\xi)=0
\]

almost everywhere, so `f` would have to be supported on a positive-measure level set of `m`. No such level set exists here. Therefore

\[
\boxed{
\sigma_p(T_{\mathbb R}(\tau))=\varnothing.
}
\]

This is the bounded-semigroup form of the continuous spectral statement already used in `WP-130`.

## 3. Every bounded solenoid-to-radial exact intertwiner is zero

The solenoid characters form a complete orthonormal basis and satisfy

\[
T_\Sigma(\tau)\chi_q
=e^{-\tau H_\infty(2\pi q)}\chi_q.
\]

Suppose a bounded operator

\[
X:L^2(\Sigma_{\mathbb Q})\to L^2(\mathbb R)
\]

obeys

\[
X T_\Sigma(\tau)=T_{\mathbb R}(\tau)X.
\]

For each `q in Q`,

\[
\begin{aligned}
T_{\mathbb R}(\tau)X\chi_q
&=X T_\Sigma(\tau)\chi_q\\
&=e^{-\tau H_\infty(2\pi q)}X\chi_q.
\end{aligned}
\]

Thus `X chi_q` would be an `L^2(R)` eigenvector of `T_R(tau)` with eigenvalue `exp[-tau H_infty(2 pi q)]`. Section 2 shows that no nonzero such vector exists. Hence

\[
X\chi_q=0
\qquad(q\in\mathbb Q).
\]

Completeness of the character basis and boundedness of `X` give

\[
\boxed{X=0.}
\]

No arithmetic estimate, limiting argument, or zero data enter the proof.

## 4. The reverse bounded intertwiner also vanishes

Suppose instead

\[
Y:L^2(\mathbb R)\to L^2(\Sigma_{\mathbb Q})
\]

is bounded and

\[
Y T_{\mathbb R}(\tau)=T_\Sigma(\tau)Y.
\]

Since both heat operators are bounded self-adjoint, taking adjoints gives

\[
T_{\mathbb R}(\tau)Y^*=Y^*T_\Sigma(\tau).
\]

This is exactly the solenoid-to-radial intertwining relation of Section 3 for `X=Y^*`. Therefore `Y^*=0` and hence

\[
\boxed{Y=0.}
\]

So the obstruction is symmetric despite the very different Hilbert-space realizations.

## 5. What this closes in WP-130

`WP-130` leaves open an “independently forced transform that changes measure or spectral type and rigorously intertwines radial Mellin and solenoid leaf geometry.” The present result sharpens that escape:

\[
\boxed{
\text{bounded exact Hilbert-space intertwiner}
\quad\Longrightarrow\quad
0.
}
\]

Changing the measure, using a nonunitary bounded map, allowing a non-isometric embedding, or dropping surjectivity does not help if the map still exactly intertwines the canonical Gamma heat operators. The obstruction is not norm preservation; it is the absence of any target eigenvector to receive the complete pure-point source basis.

A viable radial–leaf bridge must therefore leave at least one hypothesis of this theorem. Concrete surviving classes include:

- **distributional/generalized-eigenfunction transforms**, where solenoid characters may map to non-`L^2` plane-wave type objects;
- **unbounded maps with nontrivial domain issues** that are not bounded Hilbert-space morphisms;
- **boundary traces, Poisson maps, compressions, or Schur complements** that do not exactly intertwine the two existing semigroups;
- **new coupled generators or altered Hilbert structures** whose spectral type is changed before comparison;
- a genuinely **finite–archimedean or radial–leaf nonseparable geometry** whose sign theorem is established directly rather than inherited through an intertwiner.

These are materially stronger constructions than the nonunitary-change-of-representation escape left by `WP-130`.

## 6. Matched control and canonicality boundary

The argument is not special to the rational primes, zeta zeros, or the numerical values of the Gamma symbol. Let `h:[0,infinity)->R` be any continuous strictly monotone function of radial frequency, let `M_h` be multiplication by `h(|xi|)` on `L^2(R)`, and let `D` be any pure-point diagonal operator with a complete eigenbasis whose eigenvalues are sampled values of the same `h`. For any bounded injective scalar function `phi` on the relevant range, `phi(M_h)` has no point spectrum while `phi(D)` retains the complete eigenbasis. The same one-basis-line argument forces every bounded exact intertwiner to vanish.

Thus this is a **spectral-type theorem**, not arithmetic evidence. Its value for the Mathia program is negative and local: it prevents dense rational sampling of the right scalar dispersion from masquerading as a bounded geometric equivalence with the archimedean Mellin carrier.

The control also shows why replacing the Gamma symbol by another monotone CND warp cannot fix this route. Scalar functional calculus changes the eigenvalues but preserves the pure-point character decomposition on the solenoid and the multiplication representation on the radial side. As long as the radial multiplier has null level sets, bounded exact intertwiners remain zero.

## 7. Prior-art and novelty audit

No theorem-level historical novelty is claimed for the operator-theoretic mechanism. The spectral theorem for self-adjoint/normal operators and the classical Fuglede–Putnam intertwining theory imply much more general compatibility of bounded intertwiners with spectral structure. The exact proof needed here is simpler: a complete eigenbasis on one side plus absence of eigenvectors on the other already forces the intertwiner to vanish one basis vector at a time.

The directed audit included the classical Putnam paper, C. R. Putnam, *On Normal Operators in Hilbert Space*, American Journal of Mathematics **73** (1951), 357–362, DOI `10.2307/2372180`, and Mohammed Hichem Mortad, *The Fuglede-Putnam Theory*, Lecture Notes in Mathematics 2322, Springer (2022), DOI `10.1007/978-3-031-17782-8`, which surveys normal-operator intertwining relations and their extensions. These sources classicalize the ambient operator theory; the present contribution is only the Mathia-specific specialization that closes an explicit escape left by `WP-130`.

A bounded search for combinations of adelic/universal solenoids, leafwise Laplacians, digamma/Gamma subordination, pure-point versus absolutely-continuous spectral type, and bounded intertwiners found no source asserting this exact Mathia comparison. That absence is not evidence of historical novelty.

## 8. Falsification surface

The finding fails if any of the following is false under the canonical representations fixed in `WP-129`, `WP-130`, and `PC-065`:

1. `T_Sigma(tau)` has the complete character eigenbasis `chi_q`, `q in Q`;
2. `T_R(tau)` is Fourier multiplication by `exp[-tau H_infty(xi)]`;
3. `H_infty` is strictly increasing in `|xi|`, so every level set of that multiplier has Lebesgue measure zero;
4. a multiplication operator on `L^2(R)` can have a nonzero eigenvector supported only on a null level set;
5. an exact bounded intertwiner need not map an eigenvector of its source operator to an eigenvector with the same eigenvalue in the target;
6. the solenoid characters are not complete.

Items 1–3 are already established by the cited Mathia findings; items 4–6 are elementary Hilbert-space facts. No numerical experiment is load-bearing.

## Research consequence

The direct radial–solenoid bridge is now narrower than in `WP-130`. Matching the scalar Gamma dispersion on the dense rational spectrum is not merely insufficient for unitary equivalence: **there is no nonzero bounded exact semigroup intertwiner at all** between the canonical solenoid and radial Gamma carriers.

Accordingly, the next viable mechanism cannot be a bounded change of representation that preserves the existing dynamics. It must add genuinely new structure — distributional boundary theory, a non-intertwining compression/response, a changed Hilbert geometry, or a nonseparable finite–archimedean/radial–leaf generator — and must then prove its positivity independently while still recovering the finite Mangoldt and global counterterms required by the Weil criterion.