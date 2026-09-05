# PC-180 — symmetric cross-shell flux–potential couplings are pure von-Mangoldt boundary forms

**Status:** `EXACT-DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-NEGATIVE` for any finite, radial-coordinate-independent, self-adjoint shell coupling built linearly from one cyclotomic potential and one signed radial flux.

PC-179 leaves open a genuinely cross-shell use of the signed cyclotomic radial flux before scalar Mellinization or endpoint integration. The most direct source-native first-order coupling is to pair the flux of one shell with the potential of another and only then assemble across shell labels. This does retain nontrivial ordered interior information, but its entire symmetric/self-adjoint part collapses exactly to the common-vertex endpoint data.

For a finite shell family, the symmetrized flux–potential matrix is rank one:

\[
\boxed{\frac{A+A^{\mathsf T}}2=\frac12\Lambda\Lambda^{\mathsf T}.}
\]

Consequently every constant real symmetric shell mixer `C` gives

\[
\boxed{\int_0^\infty \rho(x)^{\mathsf T}C F(x)\,dx
=\frac12\Lambda^{\mathsf T}C\Lambda.}
\]

Thus any positivity or coercivity obtained in this first-order symmetric architecture is already positivity of a finite quadratic form in the classical von Mangoldt endpoint vector. The radial interior, including the sign-changing profile of non-prime-power shells, survives only in the antisymmetric ordered part, which cannot itself define a real quadratic positivity form.

## 1. Exact flux–potential matrix

For every `n>1`, use the radial cyclotomic potential and signed inward flux from PC-179:

\[
F_n(x):=\log\Phi_n(e^{-x}),
\qquad
\rho_n(x):=-F_n'(x),
\qquad x>0.
\]

The endpoint values are

\[
F_n(0+)=\log\Phi_n(1)=\Lambda(n),
\qquad
F_n(\infty)=\log\Phi_n(0)=0.
\]

PC-179 also gives `rho_n(x)=O(1)` as `x->0+` and exponential decay as `x->infinity`, so the following integrals are finite. Define the ordered cross-shell matrix

\[
A_{mn}:=\int_0^\infty \rho_m(x)F_n(x)\,dx.
\tag{1}
\]

This object is genuinely ordered: in general `A_{mn}` and `A_{nm}` need not agree. No Mellin transform, external spectral parameter, or shellwise absolute value has yet been applied.

## 2. The symmetric part is exactly a boundary term

On a finite interval `[epsilon,R]`, the product rule gives

\[
\frac{d}{dx}\bigl(F_m(x)F_n(x)\bigr)
=-\rho_m(x)F_n(x)-F_m(x)\rho_n(x).
\]

Integrating and taking `epsilon->0+`, `R->infinity` yields

\[
\boxed{A_{mn}+A_{nm}=\Lambda(m)\Lambda(n).}
\tag{2}
\]

Equivalently, for a finite shell set `S`, let

\[
\Lambda_S=(\Lambda(n))_{n\in S}.
\]

Then

\[
\boxed{
\operatorname{Sym}A_S
:=\frac{A_S+A_S^{\mathsf T}}2
=\frac12\Lambda_S\Lambda_S^{\mathsf T}.
}
\tag{3}
\]

Unless `S` contains no prime powers, this matrix has rank exactly one. In particular,

\[
\boxed{A_{nn}=\frac12\Lambda(n)^2.}
\tag{4}
\]

The apparent radial coupling has therefore lost all symmetric interior information before any further spectralization.

## 3. Every constant self-adjoint shell assembly collapses

Let `C` be any real symmetric matrix indexed by the finite shell set `S`, independent of the radial variable. Form the coupled scalar

\[
Q_C
:=
\int_0^\infty \rho(x)^{\mathsf T}C F(x)\,dx
=
\sum_{m,n\in S}C_{mn}A_{mn}.
\tag{5}
\]

Because a symmetric matrix contracts trivially with the antisymmetric part of `A`, equation (3) gives

\[
\boxed{
Q_C
=\frac12\Lambda_S^{\mathsf T}C\Lambda_S.
}
\tag{6}
\]

This includes arbitrary off-diagonal cross-shell mixing. If `C>=0`, then `Q_C>=0`, but that positivity is not a new geometric positivity theorem: it is precisely positivity of the finite quadratic form `Lambda_S^T C Lambda_S`.

The prime-power selector is retained only because the common-vertex endpoint has already collapsed each shell to

\[
\Lambda(n)=
\begin{cases}
\log p,&n=p^a,\\
0,&\text{otherwise}.
\end{cases}
\]

For example, if `m` is a prime power and `n` is not, then equation (2) gives

\[
A_{mn}+A_{nm}=0.
\]

Both ordered terms may be nonzero, but every symmetric readout cancels them exactly. Thus a sign-changing non-prime-power flux can influence this first-order matrix only through orientation, not through its self-adjoint part.

## 4. The exact surviving carrier is antisymmetric, not coercive

Define

\[
\Omega_S:=\frac{A_S-A_S^{\mathsf T}}2.
\tag{7}
\]

Then the full ordered matrix decomposes as

\[
\boxed{A_S=\frac12\Lambda_S\Lambda_S^{\mathsf T}+\Omega_S,}
\qquad
\Omega_S^{\mathsf T}=-\Omega_S.
\tag{8}
\]

The matrix `Omega_S` is the only place where this construction can retain radial ordering/interior information. However, for every real shell-amplitude vector `a`,

\[
\boxed{a^{\mathsf T}\Omega_S a=0.}
\tag{9}
\]

Hence `Omega_S` cannot by itself supply the real positive quadratic form or coercivity margin sought by the signed-flux clue. Turning it into a positive object would require an additional operation — for example a source-forced second skew structure, a noncommuting product, a nonlinear expression such as a square, or a genuinely nonlocal radial operator. Such an operation is new mathematical input and must be audited independently; it is not supplied merely by pairing the existing potential and flux.

## 5. Why radial dependence is a genuine escape from this theorem

The collapse uses the fact that the shell mixer is independent of `x`. If instead `C=C(x)` is symmetric, the same calculation gives

\[
\int_0^\infty \rho(x)^{\mathsf T}C(x)F(x)\,dx
=
\frac12\Lambda_S^{\mathsf T}C(0)\Lambda_S
+\frac12\int_0^\infty F(x)^{\mathsf T}C'(x)F(x)\,dx,
\tag{10}
\]

assuming the boundary term at infinity vanishes and the displayed integral exists. The second term can retain interior information.

This is an exact boundary of the no-go result rather than evidence for a new mechanism. An arbitrary choice of `C(x)` would violate the Prime-Circle mandate's control against externally chosen operators/normalizations. A surviving candidate must derive the radial dependence, nonlocal kernel, or noncommuting operation intrinsically from the roots-of-unity/refinement geometry and then show that its useful sign or spectrum is not another Möbius/Lambert/cyclotomic reformulation.

## 6. Relation to PC-179 and the signed-flux clue

PC-179 proves that scalar Mellinization of each `rho_n`, or a linear shell combination followed by the same Mellin transform, already carries a universal `zeta(s)` factor and therefore does not provide an independent zero mechanism.

The present result attacks a different ordering of operations: first couple distinct shells in physical radial depth using `rho_m F_n`, and only afterward take a scalar. The outcome is still classical whenever the final shell coupling is symmetric and radial-coordinate-independent. In fact it collapses even earlier than Mellinization: the self-adjoint sector is already the rank-one endpoint kernel `Lambda Lambda^T/2`.

Therefore the accepted signed-radial-flux clue remains open only beyond this entire first-order symmetric class. A useful continuation must exploit the ordered antisymmetric sector together with additional source-forced structure, an `x`-dependent/nonlocal radial coupling, or a nonlinear/noncommuting assembly before endpoint reduction.

## 7. Prior-art and novelty audit

No novelty is claimed for the analytic identity behind (2)–(6). It is the ordinary product rule/integration-by-parts applied to logarithmic cyclotomic potentials. Likewise `Phi_n(1)=exp(Lambda(n))` is the classical common-vertex identity already persisted in PC-001, and the Ramanujan/Lambert descriptions of the same radial fields are classical and anchored in `research/prime_circle/SOURCES.md` and PC-179.

A directed check of the adjacent cyclotomic-logarithmic-derivative and Ramanujan/Lambert literature therefore places every ingredient on the classical side. The research contribution here is a **scope classification** specific to the Prime-Circle candidate architecture: allowing arbitrary finite cross-shell mixing does not rescue a self-adjoint first-order flux–potential positivity mechanism as long as the shell mixer is fixed along radial depth.

This finding does not claim a historically new theorem about cyclotomic polynomials or integration by parts.

## 8. Audit and falsification boundary

The core statement is exact. It can be falsified by any pair `m,n>1` for which direct evaluation of (1) violates

\[
A_{mn}+A_{nm}=\Lambda(m)\Lambda(n),
\]

or by any finite symmetric `C` for which (6) fails.

The negative classification does **not** cover:

- radial-coordinate-dependent shell mixers `C(x)`;
- genuinely nonlocal kernels coupling different radial depths `x` and `y`;
- nonlinear functions of the ordered matrix `A` or its skew part `Omega`;
- a second intrinsic noncommuting/skew structure that can pair with `Omega`;
- growing/infinite shell limits in which the relevant operator-domain issue is itself part of the construction.

Any continuation through one of those regimes must identify the source-forced extra structure and test it against the classical Möbius/divisor/Lambert controls rather than treating escape from (6) as evidence of RH relevance.

## Research consequence

The simplest genuinely cross-shell signed-flux assembly does **not** create a new positive carrier. Its entire self-adjoint first-order sector is already the common-vertex von Mangoldt vector in rank-one form. The only interior datum that survives before adding further structure is antisymmetric and hence non-coercive on its own.

This sharpens the live frontier from “couple shells before scalarization” to “derive a source-forced operation that converts ordered interior information into a nonclassical self-adjoint/sign structure without collapsing to endpoint, Möbius/Lambert, or an externally imposed kernel.”