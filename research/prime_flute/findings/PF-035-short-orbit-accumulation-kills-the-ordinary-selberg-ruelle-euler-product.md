# PF-035 — short-orbit accumulation kills the ordinary Selberg/Ruelle Euler product on every right half-plane

**Status:** `DECISIVE-NEGATIVE` for ordinary Selberg/Ruelle zeta and any standard nuclear transfer-operator realization of that Euler product.

## Statement

Earlier prime-flute findings produce infinitely many distinct primitive closed geodesics

\[
\gamma_j,\qquad L_j:=\ell(\gamma_j)\to0.
\]

This has a consequence stronger than failure of the prime geodesic theorem, wave trace local finiteness, or the standard heat determinant: the ordinary Selberg and Ruelle Euler products do not possess **any** half-plane of ordinary convergence.

For the Selberg product

\[
Z_X(s)
=\prod_{\gamma\ \mathrm{primitive}}
\prod_{k=0}^{\infty}
\left(1-e^{-(s+k)\ell(\gamma)}\right),
\]

fix any complex \(s\) with \(\Re s>0\). Looking only at the \(k=0\) factors from the short primitive sequence gives

\[
a_j(s):=1-e^{-sL_j}.
\]

Since \(L_j\to0\),

\[
a_j(s)=sL_j+O(L_j^2)\to0.
\]

A necessary condition for an infinite product \(\prod_j a_j\) to converge to a nonzero value is \(a_j\to1\). Here the factors instead tend to zero. In fact, for every fixed \(s\ne0\) with \(\Re s>0\), sufficiently large \(j\) satisfy \(|a_j(s)|<1/2\), so partial products over this subsequence tend to zero exponentially in the number of included factors.

Therefore the formal Selberg Euler product cannot define a nonzero holomorphic function by ordinary convergence on **any** right half-plane:

\[
\boxed{\text{there is no }\sigma_0\text{ such that the ordinary Selberg product converges nontrivially for }\Re s>\sigma_0.}
\]

The same argument applies even more directly to the Ruelle product

\[
\zeta_R(s)^{-1}
=\prod_{\gamma\ \mathrm{primitive}}
\left(1-e^{-s\ell(\gamma)}\right).
\]

Thus

\[
\boxed{\text{the ordinary Ruelle Euler product also has no nontrivial right-half-plane convergence region.}}
\]

## Why this is stronger than previous trace/determinant obstructions

PF-020 showed that the primitive length spectrum is not locally finite at zero and that the usual geometric side of Selberg/wave trace diverges on positive test functions near zero.

PF-033 showed that the heat operator is not trace class and that subtracting the usual volume/cusp backgrounds does not produce the standard Laplacian determinant.

PF-035 moves the obstruction one step earlier: **before** meromorphic continuation, trace formulas, or determinants are considered, the basic Euler product from which Selberg/Ruelle theory normally starts already has no nontrivial domain of ordinary convergence.

For geometrically finite hyperbolic surfaces, the standard theory starts from a right-half-plane Euler product and then obtains meromorphic continuation, often via transfer operators. The prime flute lies outside that regime for a structural reason independent of finite generation: primitive periodic orbits accumulate at zero length.

## Consequence for transfer operators

Modern strict transfer-operator approaches for geometrically finite surfaces construct nuclear operators \(\mathcal L_s\) on suitable Banach spaces such that

\[
\det(1-\mathcal L_s)=Z_X(s)
\]

on an initial right half-plane where the periodic-orbit expansion is meaningful, and then use the determinant to continue the zeta function meromorphically.

The prime flute cannot admit such a **standard** realization for its ordinary Selberg Euler product:

1. there is no initial half-plane on which the orbit Euler product defines a nonzero holomorphic function;
2. the arbitrarily short primitive periodic orbits force the corresponding primitive factors to approach zero rather than one;
3. any candidate transfer operator whose Fredholm determinant is declared to be a zeta must therefore include a nonstandard renormalization/subtraction of the entire short-orbit sector before a determinant can exist.

This does not prove that no renormalized dynamical determinant can ever be defined. It proves that such an object would no longer be the ordinary Selberg/Ruelle zeta of the surface and would need a canonical geometric prescription for removing the infinite zero-length accumulation. Choosing an arbitrary cutoff or regrouping would not be acceptable as an RH mechanism.

## Novelty / literature check

The general Selberg/Ruelle and transfer-operator theory for geometrically finite surfaces is classical, and recent strict transfer-operator constructions still work in geometrically finite finite-topological-type settings. The 2022 Pohl–Wabnitz construction produces nuclear transfer operators whose Fredholm determinants equal Selberg zeta functions for geometrically finite noncompact orbisurfaces.

Recent work on infinite-type hyperbolic surfaces explicitly isolates the case of **discrete length spectrum** as a special regime. The prime flute is outside that regime because it has infinitely many primitive lengths tending to zero.

No claim is made that the elementary infinite-product obstruction is itself a new theorem in analysis. The prime-flute-specific contribution is that the exact prime-gap geometry supplies the required short primitive sequence, so the standard Selberg/Ruelle transfer-operator branch is ruled out for this surface for an explicit geometric reason.

## Research consequence

Do not spend further effort trying to obtain an ordinary Selberg zeta, Ruelle zeta, or strict nuclear transfer operator whose determinant is the unrenormalized primitive-geodesic product of the prime flute.

A viable dynamical zeta would have to be **relative/renormalized from the outset**, with a background forced by the exact multi-gap short-orbit geometry. The renormalization itself would have to carry mathematical content; otherwise it is only an arbitrary generating function.
