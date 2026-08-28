# PC-027 — radial Dirichlet birth fields are a unimodular Möbius basis of the full-root fields

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` for the canonical radially regularized quadratic/infinite-mode Dirichlet-energy route and for basis-invariant finite-subspace spectralizations built from it. The underlying cyclotomic, Möbius, Ramanujan, resultant, and discriminant ingredients are classical; no novelty is claimed for them.

PC-021 left singularly renormalized and same-index nonlinear observables outside its regular-linear no-go theorem, and PC-024 only closed fixed finite polynomials in finitely many Fourier modes. The analytic Dirichlet energy of the **entire** cyclotomic field is therefore a natural remaining test: it couples all angular modes before taking any scale transform.

At every finite radial cutoff this route also collapses. Primitive-shell fields are related to the complete-polygon fields by an exact determinant-one Möbius change of basis, and every pairwise Dirichlet energy is a finite divisor-lattice combination of elementary logarithms. The infinite Fourier sum does not create a new spectral object before the boundary limit.

## 1. Normalized cyclotomic fields and exact Möbius basis change

For `|z|<1`, set

\[
\widehat\Phi_1(z):=1-z,
\qquad
\widehat\Phi_n(z):=\Phi_n(z)\quad(n>1),
\]

and choose the analytic logarithms normalized to vanish at `z=0`:

\[
F_n(z):=\Log \widehat\Phi_n(z),
\qquad
V_d(z):=\Log(1-z^d).
\]

The usual cyclotomic factorization and Möbius inversion give, for every `n>=1`,

\[
\boxed{
F_n(z)=\sum_{d\mid n}\mu(n/d)V_d(z).
}
\]

For a radial cutoff `0<r<1`, define

\[
F_{n,r}(z):=F_n(rz),
\qquad
V_{d,r}(z):=V_d(rz).
\]

The same identity holds exactly after regularization:

\[
\boxed{
F_{n,r}=\sum_{d\mid n}\mu(n/d)V_{d,r}.
}
\]

Now let `S` be any finite divisor-closed set of positive integers and order it increasingly. Let

\[
M_S(n,d)=
\begin{cases}
\mu(n/d),&d\mid n,\\
0,&d\nmid n.
\end{cases}
\]

Then `M_S` is lower triangular with every diagonal entry equal to `1`. Hence

\[
\boxed{\det M_S=1}
\]

and, for every fixed `0<r<1`,

\[
\boxed{
\operatorname{span}\{F_{n,r}:n\in S\}
=
\operatorname{span}\{V_{n,r}:n\in S\}.
}
\]

Thus birth extraction changes the canonical coordinate system inside this finite Dirichlet subspace, but it does not create a new subspace.

## 2. Exact Gram congruence and determinant equality

Use the analytic Dirichlet inner product

\[
\langle f,g\rangle_{\mathcal D}
=\frac1\pi\int_{\mathbb D}f'(z)\overline{g'(z)}\,dA(z).
\]

Let `G_S^{birth}(r)` be the Gram matrix of the `F_{n,r}`, and `G_S^{full}(r)` the Gram matrix of the `V_{n,r}`, both indexed by `S`. The exact basis relation gives

\[
\boxed{
G_S^{birth}(r)
=M_S G_S^{full}(r) M_S^{\mathsf T}.
}
\]

Consequently

\[
\boxed{
\det G_S^{birth}(r)=\det G_S^{full}(r)
}
\]

and both families have the same rank and the same orthogonal span.

This is a congruence, **not** a similarity. The ordinary eigenvalues of the two coordinate Gram matrices need not agree. Therefore this finding does not claim that every spectrum attached to the distinguished birth basis is identical to the full-root one. What it rules out is the stronger-looking but actually basis-invariant route in which the arithmetic is supposed to arise from the finite Hilbert subspace itself, its orthogonal projector, rank, or determinant-volume: those objects are already present before primitive-shell extraction.

## 3. The complete infinite-mode Gram entry has a finite divisor formula

PC-006 derived the Fourier representation

\[
\langle F_{m,r},F_{n,r}\rangle_{\mathcal D}
=
\sum_{k\ge1}\frac{c_m(k)c_n(k)}{k}r^{2k}.
\]

Write `x=r^2`. The classical divisor formula for Ramanujan sums is

\[
c_m(k)=\sum_{\substack{d\mid m\\d\mid k}}d\,\mu(m/d).
\]

Expanding both sums and then summing over multiples of `lcm(d,e)` gives the exact finite identity

\[
\boxed{
G_{m,n}(x)
:={\sum_{k\ge1}\frac{c_m(k)c_n(k)}{k}x^k}
=
-\sum_{d\mid m}\sum_{e\mid n}
\gcd(d,e)\,\mu(m/d)\mu(n/e)
\log\!\left(1-x^{\operatorname{lcm}(d,e)}\right).
}
\]

Indeed,

\[
\sum_{\operatorname{lcm}(d,e)\mid k}\frac{x^k}{k}
=-\frac1{\operatorname{lcm}(d,e)}
\log\!\left(1-x^{\operatorname{lcm}(d,e)}\right),
\]

and

\[
\frac{de}{\operatorname{lcm}(d,e)}=\gcd(d,e).
\]

This is the key obstruction. Although the left side couples **all** angular Fourier modes, at every `0<x<1` it is exactly a finite divisor-lattice expression. There is no residual infinite-mode degree of freedom hidden inside the radial quadratic energy.

## 4. Closed self-energy formula

The diagonal can be simplified further. Write

\[
\operatorname{rad}(n)=\prod_{p\mid n}p,
\qquad
q_n:=\frac{n}{\operatorname{rad}(n)}.
\]

Grouping the divisor pairs by their least common multiple gives

\[
\boxed{
G_{n,n}(x)
=
-q_n\sum_{t\mid\operatorname{rad}(n)}
\left(
\prod_{p\mid\operatorname{rad}(n)/t}(p-2)
\right)
\log\!\left(1-x^{n/t}\right).
}
\]

Only the top two valuations of each prime can occur because the Möbius factors vanish otherwise. Locally, if `p^a || n`, the two possible contributions are `p^{a-1}` when the least-common-multiple exponent drops to `a-1`, and `p^{a-1}(p-2)` when it stays at `a`. Multiplying these local contributions yields the displayed formula.

For a prime `p`, this reduces to

\[
\boxed{
G_{p,p}(x)
=-\log(1-x)-(p-2)\log(1-x^p).
}
\]

For odd `n`, the factor `p-2` at the newly introduced prime `2` is zero, and the formula gives

\[
\boxed{G_{2n,2n}(x)=G_{n,n}(x),}
\]

consistent with the exact shell relation `Phi_{2n}(z)=Phi_n(-z)` used in PC-019. Thus even the full radial energy retains that known unanchored `n <-> 2n` degeneracy.

## 5. Boundary limit recovers the PC-006 classical energies

As `x -> 1^-`,

\[
-\log(1-x^L)
=-\log(1-x)-\log L+o(1).
\]

On the diagonal, the sum of the coefficients in the preceding formula is `phi(n)`, so

\[
G_{n,n}(x)
=-\varphi(n)\log(1-x)
-\log|\operatorname{Disc}\Phi_n|+o(1),
\]

exactly the renormalized discriminant energy of PC-006.

For `m != n`, the finite limit is likewise

\[
G_{m,n}(x)\longrightarrow
-\log|\operatorname{Res}(\Phi_m,\Phi_n)|,
\]

again matching PC-006. Hence the finite-radius formula is not a new continuation beyond resultant/discriminant potential theory; it is an exact interpolation whose endpoint is the already-classified classical energy.

## 6. Prior art and novelty audit

No novelty is claimed for the ingredients used in the derivation.

- Cyclotomic factorization plus Möbius inversion is classical and already underlies PC-015 and PC-021.
- The Ramanujan-sum expansion of `log Phi_n` and product/correlation identities for Ramanujan sums are classical; Tóth's work recorded in `SOURCES.md` is a direct prior-art anchor for that arithmetic layer.
- The interpretation of mutual logarithmic energy as a resultant and renormalized self-energy as a discriminant is classical potential theory; Gustafsson--Tkachev is the existing anchor used in PC-006.
- Congruence of Gram matrices under a change of basis is elementary linear algebra.

The useful prime-circle result is therefore a **scope classification**, not a historical-priority claim: one of the most canonical infinite-mode quadratic escape routes left open by PC-021/PC-024 is already a determinant-one Möbius re-basing of the complete-polygon fields at every finite radial cutoff.

## 7. What this rules out, and what remains outside the theorem

This finding rules out treating any of the following, by themselves, as an independent prime-circle RH mechanism:

- the finite-radius Dirichlet subspace spanned by the complete cyclotomic fields;
- its orthogonal projector or rank after replacing full-root fields by primitive/birth fields;
- the finite Gram determinant/volume on a divisor-closed family;
- the apparent infinite-mode complexity of the regularized quadratic energy `G_{m,n}(x)` before the boundary limit.

It does **not** rule out:

1. coordinate spectra that deliberately use the distinguished birth basis, because congruence does not preserve ordinary Gram eigenvalues;
2. nonlinear functionals of the fields or of their Gram data;
3. a genuinely infinite-dimensional renormalized determinant if the Möbius basis transform ceases to be bounded or determinant-class in the chosen completion;
4. nonseparable cross-level dynamics;
5. shell-dependent metrics/operators, especially the nonlinear global Fuchsian uniformization and accessory-parameter defect of PC-017.

The third item is a sharp caveat rather than a proposed mechanism: any anomaly there would have to be traced to the infinite-dimensional Möbius operator/regularization itself, not inferred from the finite prime-circle Hilbert geometry.

## 8. Audit / falsification test

The result is exact at finite radius. A direct audit can falsify it by finding any `m,n` and `0<x<1` for which

\[
\sum_{k\ge1}\frac{c_m(k)c_n(k)}{k}x^k
\]

differs from the finite divisor-log expression in Section 3, or any finite divisor-closed `S` for which the Möbius incidence matrix fails to have determinant `1` or the Gram congruence fails.

A future candidate claiming to escape this obstruction should identify explicitly which hypothesis it breaks: finite divisor-closed truncation, quadratic Dirichlet energy, finite radial cutoff, linear Möbius re-basing, or basis-invariance. Merely summing more Fourier modes does not break any of them.

## Research consequence

PC-024 showed that fixed finite Fourier nonlinearities are too small; PC-027 shows that the canonical **all-mode quadratic Dirichlet energy** is still too rigid. This narrows the surviving prime-circle region toward genuinely nonlinear shell-dependent geometry, nonseparable cross-level dynamics, or a rigorously defined infinite-dimensional anomaly. In particular, the endpoint Fuchsian uniformization/accessory defect of PC-017 remains outside this no-go theorem.