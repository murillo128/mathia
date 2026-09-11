# WI-246 — Joint Robin incompatibility is strict at finite radius but neutral at leading order

## Status

- **Evidence:** `EXACT-DERIVED + CLASSICAL-SPECTRAL + STRUCTURAL-RIGIDITY + DECISIVE-NEGATIVE`.
- **Scope:** this sharpens the finite-radius mean-side reserve of `WI-245` by proving that its termwise Robin sum is never the exact combined variational constant at finite radius. It also proves a barrier: optimizing all of the same positive digamma resolvents jointly cannot improve the leading `a^{-2}` source tariff or its coefficient.
- **Novelty boundary:** the two-projection/principal-angle calculation used below is classical operator theory (Halmos' two-subspaces framework and later two-projection literature). The line-local contribution is its specialization to the incompatible Dirichlet--Robin ground states from `WI-245`, together with the matching common-test upper bound that fixes the exact leading asymptotic of the combined reserve. A targeted audit did not locate this zeta/Weil specialization. No priority claim is made.

## Claim

Retain the notation of `WI-245`. On `L^2(0,a)`, let

\[
K^-_{\alpha,a}f(x)
=\int_0^a \frac\alpha2
\left(e^{-\alpha|x-y|}-e^{-\alpha(x+y)}\right)f(y)\,dy,
\qquad
A_{\alpha,a}:=I-K^-_{\alpha,a}.
\]

For

\[
b_n=n+\frac14,
\qquad
\alpha_n=2b_n,
\qquad
c_n=\frac1{b_n},
\]

define the exact combined finite-radius mean reserve as the quadratic-form infimum

\[
\boxed{
\beta_*(a)
:=
\inf_{\substack{\|f\|_2=1\\ f\text{ in the form domain}}}
\sum_{n=1}^\infty c_n
\langle f,A_{\alpha_n,a}f\rangle.
}
\]

Thus `M(0)+beta_*(a)` is the optimal lower bound obtainable from the **entire positive digamma-resolvent mean form** on normalized odd functions supported in `[-a,a]`.

Let

\[
B_{\rm Robin}(a)
=\sum_{n=1}^\infty c_n d_{\alpha_n}(a)
\]

be the termwise lower bound from `WI-245`. Then for every finite `a>0`,

\[
\boxed{
\beta_*(a)>B_{\rm Robin}(a).
}
\]

More quantitatively, if `kappa_{alpha,j}(a)` is the `j`-th positive solution of

\[
\kappa a+\arctan(\kappa/\alpha)=j\pi,
\]

set

\[
d_{\alpha,j}(a)
:=\frac{\kappa_{\alpha,j}(a)^2}
{\alpha^2+\kappa_{\alpha,j}(a)^2},
\qquad
g_\alpha(a):=d_{\alpha,2}(a)-d_{\alpha,1}(a)>0.
\]

Let `phi_alpha` be the normalized first Dirichlet--Robin eigenfunction,

\[
\phi_\alpha(x)
=\frac{\sin(\kappa_{\alpha,1}(a)x)}
{\|\sin(\kappa_{\alpha,1}(a)\,\cdot)\|_2},
\]

and put

\[
\rho(a):=
|\langle\phi_{5/2},\phi_{9/2}\rangle|<1,
\]

\[
A(a):=\frac45g_{5/2}(a),
\qquad
B(a):=\frac49g_{9/2}(a).
\]

Then the explicit positive correction

\[
\boxed{
\varepsilon(a)
:=\frac{A(a)+B(a)
-\sqrt{(A(a)-B(a))^2+4A(a)B(a)\rho(a)^2}}{2}>0
}
\]

satisfies

\[
\boxed{
\beta_*(a)\ge B_{\rm Robin}(a)+\varepsilon(a).
}
\]

So the warning in `WI-245` that no single vector need extremize every Robin resolvent is not merely formal: simultaneous extremization is quantitatively impossible.

However, this incompatibility cannot improve the leading large-radius tariff. Define

\[
\boxed{
U_D(a)
:=\sum_{n=1}^\infty
\frac1{b_n}
\frac{\pi^2}{4b_n^2a^2+\pi^2}.
}
\]

Then

\[
\boxed{
B_{\rm Robin}(a)<\beta_*(a)\le U_D(a),
}
\]

and both outer quantities have the same leading asymptotic. Consequently

\[
\boxed{
\lim_{a\to\infty}a^2\beta_*(a)
=rac{\pi^2}{4}\zeta\!\left(3,\frac54\right).
}
\]

Equivalently, even the **optimal joint use** of the positive digamma-resolvent decomposition gives the same leading source surcharge as `WI-245`:

\[
\boxed{
\frac12\beta_*(a)
=\frac{\pi^2}{8}\zeta\!\left(3,\frac54\right)a^{-2}
+o(a^{-2}).
}
\]

Thus the finite-radius incompatibility is real but asymptotically subleading. Any stronger leading-order coercivity must use information not present in the termwise positive-resolvent floor alone: for example zeta-specific signed-source structure, first-crossing constraints, or another mean-side invariant.

## Exact derivation

### 1. Every single Robin ground state has a positive spectral gap

`WI-245` identifies the eigenfunctions of `A_{alpha,a}` as the Dirichlet--Robin modes

\[
\sin(\kappa_{\alpha,j}x),
\]

with increasing eigenvalues

\[
d_{\alpha,j}
=\frac{\kappa_{\alpha,j}^2}{\alpha^2+\kappa_{\alpha,j}^2}.
\]

Let `P_alpha` be the rank-one orthogonal projection onto the first normalized mode `phi_alpha`. By the spectral theorem,

\[
\boxed{
A_{\alpha,a}
\succeq d_{\alpha,1}I
+g_\alpha(I-P_\alpha),
\qquad
g_\alpha=d_{\alpha,2}-d_{\alpha,1}>0.
}
\]

After multiplying by `c_n` and summing, retain only the nontrivial spectral-gap remainders for `n=1,2`. All omitted remainders are positive semidefinite. Since

\[
\alpha_1=\frac52,
\quad c_1=\frac45,
\qquad
\alpha_2=\frac92,
\quad c_2=\frac49,
\]

we obtain, in quadratic-form sense,

\[
\sum_{n\ge1}c_n A_{\alpha_n,a}
\succeq
B_{\rm Robin}(a)I
+A(a)(I-P_{5/2})
+B(a)(I-P_{9/2}).
\]

### 2. Distinct Robin parameters cannot share the ground state

For fixed `a`, the first modes for `alpha=5/2` and `alpha=9/2` are not collinear. Indeed, collinearity of two nonzero sine modes on an interval forces their frequencies to agree, say `kappa`. The two Robin boundary conditions would then give

\[
\kappa\cos(\kappa a)+\frac52\sin(\kappa a)=0,
\]

\[
\kappa\cos(\kappa a)+\frac92\sin(\kappa a)=0.
\]

Subtracting yields `2 sin(kappa a)=0`. But then the first equation would force `kappa cos(kappa a)=0`, impossible for a positive Robin eigenfrequency. Hence

\[
\boxed{\rho(a)<1.}
\]

The overlap is completely explicit. If `k=kappa_{5/2,1}(a)` and `ell=kappa_{9/2,1}(a)`, then

\[
I(k,\ell)
=\frac{\sin((k-\ell)a)}{2(k-\ell)}
-\frac{\sin((k+\ell)a)}{2(k+\ell)},
\]

with the removable `k=ell` case interpreted by continuity, and

\[
N(k)^2=\frac a2-\frac{\sin(2ka)}{4k}.
\]

Thus

\[
\rho(a)=\frac{|I(k,\ell)|}{N(k)N(\ell)}.
\]

### 3. Classical two-projection algebra gives a uniform strict correction

For unit vectors with rank-one projections `P,Q` and overlap `rho=|<p,q>|`, the smallest eigenvalue of

\[
A(I-P)+B(I-Q),
\qquad A,B>0,
\]

is

\[
\boxed{
\frac{A+B-\sqrt{(A-B)^2+4AB\rho^2}}2.
}
\]

This follows immediately by restricting to `span{p,q}`; on its orthogonal complement the eigenvalue is `A+B`. It is also a standard special case of the classical two-projection/principal-angle calculus.

Because `rho(a)<1`, the displayed eigenvalue is strictly positive. Applying it to the two retained Robin gaps proves

\[
\beta_*(a)
\ge B_{\rm Robin}(a)+\varepsilon(a)
>B_{\rm Robin}(a).
\]

This is a **uniform** gap in the variational problem at every fixed finite radius; it does not rely on existence of a minimizer for the full infinite quadratic form.

### 4. A common Dirichlet sine gives the matching upper envelope

To determine whether the strict correction can alter the leading large-`a` scale, use one test vector for all resolvents:

\[
f_a(x)=\sqrt{\frac2a}\sin\frac{\pi x}{a},
\qquad
k:=\frac\pi a.
\]

Fix `alpha>0` and let

\[
u=K^-_{\alpha,a}f_a.
\]

By the Green-operator identity of `WI-245`,

\[
-u''+\alpha^2u=\alpha^2f_a,
\qquad
u(0)=0,
\qquad
u'(a)+\alpha u(a)=0.
\]

A particular solution is

\[
u_p=\mu f_a,
\qquad
\mu=\frac{\alpha^2}{\alpha^2+k^2}.
\]

Since `f_a(a)=0` and `f_a'(a)=-sqrt(2/a) k`, the Robin residual of `u_p` is negative. The exact solution is

\[
\boxed{
u(x)=\mu f_a(x)+C\sinh(\alpha x),
\qquad
C=\frac{\mu\sqrt{2/a}\,k}{\alpha e^{\alpha a}}>0.
}
\]

Both `f_a` and `sinh(alpha x)` are positive on `(0,a)`. Therefore

\[
\langle f_a,K^-_{\alpha,a}f_a\rangle
>\mu,
\]

and hence

\[
\boxed{
\langle f_a,A_{\alpha,a}f_a\rangle
<\frac{k^2}{\alpha^2+k^2}
=\frac{\pi^2}{\alpha^2a^2+\pi^2}.
}
\]

For `alpha_n=2b_n`, multiplying by `1/b_n` and summing gives a convergent majorant,

\[
\beta_*(a)
\le
\sum_{n=1}^\infty
\frac1{b_n}\frac{\pi^2}{4b_n^2a^2+\pi^2}
=U_D(a).
\]

The same estimate proves directly that `f_a` lies in the form domain.

### 5. The joint correction is necessarily subleading

For every fixed `n`,

\[
a^2\frac1{b_n}
\frac{\pi^2}{4b_n^2a^2+\pi^2}
\longrightarrow
\frac{\pi^2}{4b_n^3}.
\]

Moreover,

\[
0\le
a^2\frac1{b_n}
\frac{\pi^2}{4b_n^2a^2+\pi^2}
\le\frac{\pi^2}{4b_n^3},
\]

and the right-hand series converges. Dominated convergence therefore gives

\[
\lim_{a\to\infty}a^2U_D(a)
=\frac{\pi^2}{4}
\sum_{n=1}^\infty\frac1{(n+1/4)^3}
=\frac{\pi^2}{4}\zeta\!\left(3,\frac54\right).
\]

`WI-245` already proved

\[
\lim_{a\to\infty}a^2B_{\rm Robin}(a)
=\frac{\pi^2}{4}\zeta\!\left(3,\frac54\right).
\]

The sandwich

\[
B_{\rm Robin}(a)<\beta_*(a)\le U_D(a)
\]

therefore yields

\[
\boxed{
\lim_{a\to\infty}a^2\beta_*(a)
=\frac{\pi^2}{4}\zeta\!\left(3,\frac54\right).
}
\]

So the simultaneous Robin incompatibility is an exact finite-radius improvement, but it cannot change either the `a^{-2}` order or its leading coefficient.

## Structural consequence for the research line

`WI-245` left open a plausible local refinement: perhaps the termwise sum `B_Robin(a)` was substantially lossy because different exponential resolvents have different Robin extremizers. The first half of this finding confirms the incompatibility and turns it into an explicit positive correction `epsilon(a)`.

The second half closes the stronger version of that route. A single common Dirichlet sine already matches the termwise lower bound at leading `a^{-2}` order. Therefore no amount of exact simultaneous optimization of **the same positive resolvent decomposition** can produce a larger leading coefficient. This is a useful no-go result because it prevents spending effort on increasingly elaborate principal-angle combinations in the hope of changing the asymptotic tariff.

The unresolved program remains the one identified by the canonical mandate and `WI-245`: use finite-radius first-crossing structure or genuinely zeta-specific signed-source information to show that an off-line zero witness cannot pay even this sharp leading archimedean tariff. This finding supplies no source upper bound and does not assume global Weil positivity.

## Prior-art audit

A targeted audit was run after the exact claim was isolated.

1. P. R. Halmos, **Two subspaces**, *Transactions of the American Mathematical Society* **144** (1969), 381--389, is the classical source of the two-subspace/two-projection decomposition underlying the principal-angle calculation.
2. A. Böttcher and I. M. Spitkovsky, **A gentle guide to the basics of two projections theory**, *Linear Algebra and its Applications* **432** (2010), 1412--1459, surveys the same machinery and its spectral consequences.
3. Work on spectra of linear combinations of two projections, including J. Benítez and V. Rakočević, *Linear and Multilinear Algebra* **58** (2010), 673--679, confirms that the weighted two-projection spectral calculation is standard operator theory.
4. The zeta-side finite-interval context remains Suzuki's 2026 screw-function/Weil-form framework already anchored in `SOURCES.md` and the line-local findings. Targeted searches combining Weil/zeta, compact support, digamma resolvents, Robin spectrum, and two-projection optimization did not locate the finite-radius sandwich above.

The novelty claim is deliberately narrow: **not** the projection formula, not Robin Sturm--Liouville theory, and not the digamma expansion, but the exact specialization showing (i) strict finite-radius incompatibility of the Robin extremizers and simultaneously (ii) leading-order neutrality of that incompatibility for the `WI-245` tariff. Search failure is not evidence of priority, so none is claimed.

## Falsification and downstream use

This finding would fail if any of the following occurs:

- the `WI-245` Green-operator boundary condition or resolvent expansion is corrected materially;
- two distinct Robin parameters can share the first Dirichlet--Robin eigenfunction on the same finite interval;
- the common Dirichlet sine does not belong to the quadratic-form domain of the summed mean operator;
- the test-vector estimate fails to dominate the infinite sum by a summable `b_n^{-3}` envelope.

Each point is explicit in the derivation above. No numerical certification is used.

The most useful downstream rule is negative: do **not** expect a stronger leading finite-radius source tariff merely from coupling more of the positive Robin resolvents. To improve the leading coercivity, add information that distinguishes actual zeta source structure or first-crossing witnesses from arbitrary compactly supported odd vectors.

## Formalization handoff

No formalization issue is opened. The result is exact and elementary enough to formalize, but it is presently a route-closing structural refinement rather than a load-bearing theorem whose machine verification would unlock the next research step. The next bottleneck remains arithmetic/source-side, not this two-projection calculation.
