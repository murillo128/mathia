# PC-182 — monotone radial-depth positivity fills the Mangoldt nullspace

**Status:** `EXACT-DERIVED` + `CLASSICAL-PERIOD` + `DECISIVE-NEGATIVE` for the monotone scalar radial-depth/self-adjoint escape left open by PC-180 and PC-181, including the canonical first log-radial moment and its equivalent genuinely two-depth `min`-kernel flux form.

PC-180 proves that every radial-coordinate-independent symmetric first-order flux–potential coupling collapses to the rank-one von-Mangoldt boundary form, while PC-181 proves that positive functional calculus of the surviving skew carrier alone is selector-blind. The most immediate remaining repair is therefore to let the common log-radial depth itself weight the ordered coupling before symmetrization, or equivalently to use the induced nonlocal two-depth kernel on the signed fluxes.

That repair has an exact dichotomy. A constant radial weight gives only the classical `Lambda Lambda^T` boundary term. As soon as the scalar radial weight is monotone and genuinely depth-dependent, the new self-adjoint term is a positive Gram energy of the full cyclotomic potentials. Every non-prime-power shell then acquires strictly positive diagonal mass even though its total signed flux is zero. Thus this whole positive Stieltjes/Volterra kernel class cannot simultaneously retain exact Mangoldt support and gain radial coercivity.

For the canonical first moment `w(x)=x`, the self-adjoint term is

\[
\frac12 G_{mn},
\qquad
G_{mn}=\int_0^\infty F_m(x)F_n(x)\,dx,
\]

and the same matrix is the genuinely nonlocal signed-flux form

\[
\boxed{
G_{mn}
=\int_0^\infty\!\int_0^\infty
\min(u,v)\,\rho_m(u)\rho_n(v)\,du\,dv.
}
\]

The smallest mixed control is decisive: `Lambda(6)=0`, but `F_6` is nonzero and therefore `G_{66}>0`. The sign cancellation that makes the total flux of shell `6` vanish is destroyed by the positive nonlocal kernel rather than preserved by it.

## 1. Weighted ordered radial coupling

For every `n>1`, use the Prime-Circle radial potential and signed inward flux from PC-179,

\[
F_n(x)=\log\Phi_n(e^{-x}),
\qquad
\rho_n(x)=-F_n'(x),
\qquad x>0.
\]

Their endpoint values are

\[
F_n(0+)=\Lambda(n),
\qquad
F_n(\infty)=0.
\]

Let `S` be a finite shell set and let `w:[0,infty)->R` be locally absolutely continuous with finite `w(0)`, such that the boundary and integrals below converge. Define the ordered depth-weighted matrix

\[
\boxed{
B^{(w)}_{mn}
:=\int_0^\infty
w(x)\rho_m(x)F_n(x)\,dx.
}
\tag{1}
\]

For `w=1`, this is exactly the matrix `A` of PC-180. The first nonconstant source-coordinate choice is `w(x)=x`, where `x=-log r` is the canonical log-radial coordinate already singled out by the refinement/dilation analysis in PC-165.

## 2. Exact symmetric decomposition for every radial weight

The product rule gives

\[
\frac{d}{dx}\bigl(F_m(x)F_n(x)\bigr)
=-\rho_m(x)F_n(x)-F_m(x)\rho_n(x).
\]

Multiplying by `w(x)`, integrating by parts, and using the endpoint values yields

\[
\boxed{
B^{(w)}_{mn}+B^{(w)}_{nm}
=w(0)\Lambda(m)\Lambda(n)
+\int_0^\infty w'(x)F_m(x)F_n(x)\,dx.
}
\tag{2}
\]

Hence on the finite shell family

\[
\boxed{
\operatorname{Sym}B^{(w)}
=\frac{w(0)}2\Lambda\Lambda^{\mathsf T}
+\frac12 G_{w'},
}
\tag{3}
\]

where

\[
(G_{w'})_{mn}
:=\int_0^\infty w'(x)F_m(x)F_n(x)\,dx.
\tag{4}
\]

For any real amplitude vector `a`,

\[
\boxed{
a^{\mathsf T}\operatorname{Sym}B^{(w)}a
=\frac{w(0)}2(a\cdot\Lambda)^2
+\frac12\int_0^\infty
w'(x)\left(\sum_{n\in S}a_nF_n(x)\right)^2dx.
}
\tag{5}
\]

Equation (5) makes the tradeoff exact. If `w'=0`, the whole symmetric sector is the classical boundary form from PC-180. If `w' >= 0`, the new interior contribution is positive semidefinite. If `w'` is positive on a set of positive measure, every individual nonzero shell field receives strictly positive interior energy.

## 3. Monotone depth destroys the exact prime-power nullspace

Let `n>1` be not a prime power. Then

\[
\Lambda(n)=0,
\]

but `F_n` is not identically zero. Since `F_n` is real analytic on `(0,infty)`, its zero set has measure zero unless the function vanishes identically. Therefore, whenever `w' >= 0` and `w'>0` on a set of positive measure,

\[
\boxed{
(\operatorname{Sym}B^{(w)})_{nn}
=\frac12\int_0^\infty w'(x)F_n(x)^2\,dx
>0.
}
\tag{6}
\]

Thus every non-prime-power basis direction that was exactly null under the total signed flux becomes positive under a genuinely monotone radial-depth self-adjoint repair.

More generally, if `a dot Lambda=0` but the combined field `sum a_n F_n` is nonzero, then (5) is strictly positive under the same hypothesis on `w'`. The monotone interior term therefore fills the Mangoldt-null subspace rather than coercing only the prime-power sector.

This is not merely a failure of one normalization. It is a structural incompatibility inside this class:

\[
\boxed{
\text{constant depth weight}
\Rightarrow
\text{exact Mangoldt boundary but no interior coercivity},
}
\]

whereas

\[
\boxed{
\text{strictly monotone depth weight}
\Rightarrow
\text{positive interior energy but loss of Mangoldt nullity}.
}
\]

## 4. The first log-radial moment is the canonical `min`-kernel nonlocal form

Set

\[
w(x)=x.
\]

Then `w(0)=0` and `w'=1`, so (3) becomes

\[
\boxed{
\operatorname{Sym}B^{(x)}=\frac12G,
\qquad
G_{mn}=\int_0^\infty F_m(x)F_n(x)\,dx.
}
\tag{7}
\]

Because

\[
F_n(x)=\int_x^\infty \rho_n(u)\,du,
\]

Fubini gives the exact genuinely two-depth representation

\[
\boxed{
G_{mn}
=\int_0^\infty\!\int_0^\infty
\min(u,v)\rho_m(u)\rho_n(v)\,du\,dv.
}
\tag{8}
\]

The kernel `min(u,v)` is the classical Brownian/Volterra covariance kernel and is positive semidefinite. More generally, combining the endpoint term in (2) with the tail representation gives

\[
\boxed{
B^{(w)}_{mn}+B^{(w)}_{nm}
=\int_0^\infty\!\int_0^\infty
w(\min(u,v))\rho_m(u)\rho_n(v)\,du\,dv
}
\tag{9}
\]

for the same class of weights. When `w` is nonnegative and nondecreasing, `w(min(u,v))` is itself a positive Stieltjes covariance kernel, since

\[
w(\min(u,v))
=w(0)+\int_0^{\min(u,v)}w'(x)\,dx.
\]

Therefore the no-go is genuinely nonlocal: replacing the scalar endpoint by the most canonical positive two-depth cumulative kernel does not preserve the signed prime-power selector.

## 5. Exact `{2,6}` matched control

The smallest prime-power/non-prime-power pair makes the leakage explicit without numerical approximation. For shell `2`,

\[
F_2(x)=\log(1+e^{-x})>0.
\]

For shell `6`, writing `r=e^{-x}` gives

\[
\Phi_6(r)=1-r+r^2=1-r(1-r),
\]

so for `0<r<1`,

\[
0<\Phi_6(r)<1,
\qquad
\boxed{F_6(x)<0.}
\tag{10}
\]

Hence

\[
\boxed{
G_{66}=\int_0^\infty F_6(x)^2dx>0,
\qquad
G_{26}=\int_0^\infty F_2(x)F_6(x)dx<0.
}
\tag{11}
\]

But PC-179 gives

\[
\boxed{\int_0^\infty\rho_6(x)dx=\Lambda(6)=0.}
\tag{12}
\]

Thus the `min`-kernel has not retained the cancellation on the control shell; it has converted the sign-changing flux into a strictly positive self-energy. The failure occurs before any Mellin transform, spectral determinant, or positive functional calculus is appended.

## 6. The first-moment Gram entries are already classical cyclotomic weight-three periods

The new positive matrix also does not open an unexplored finite period class. Cyclotomic factorization gives

\[
F_n(x)
=\sum_{d\mid n}\mu(n/d)\log(1-e^{-dx}).
\tag{13}
\]

Therefore

\[
\boxed{
G_{mn}
=\sum_{d\mid m}\sum_{e\mid n}
\mu(m/d)\mu(n/e)\,T(d,e),
}
\tag{14}
\]

with the universal two-scale kernel

\[
\boxed{
T(d,e)
:=\int_0^\infty
\log(1-e^{-dx})\log(1-e^{-ex})\,dx
=\sum_{r,s\ge1}\frac1{rs(dr+es)}.
}
\tag{15}
\]

Put `M=dr` and `N=es`. Root-of-unity filters for the divisibility conditions give exactly

\[
\boxed{
T(d,e)
=\sum_{\alpha^d=1}\sum_{\beta^e=1}
S(\alpha,\beta),
}
\tag{16}
\]

where

\[
S(X,Y)
:=\sum_{M,N\ge1}\frac{X^M Y^N}{MN(M+N)}.
\tag{17}
\]

This is precisely the weight-three colored Tornheim building block already encountered and classified in PC-102. As a simple diagonal check,

\[
\boxed{T(d,d)=\frac{2\zeta(3)}d.}
\tag{18}
\]

Jianqiang Zhao's classical colored-Tornheim reduction, already anchored in `research/prime_circle/SOURCES.md`, expresses these depth-two colored Tornheim values in terms of double polylogarithms at roots of unity. Thus the canonical first radial moment introduces a new **positive assembly of existing cyclotomic periods**, not a new finite period class or an intrinsic Riemann-zero divisor.

## 7. Prior-art and novelty audit

No novelty is claimed for the analytic ingredients. Equation (2) is weighted integration by parts. The kernel `min(u,v)` in (8) is the standard cumulative/Volterra covariance kernel. Equations (15)--(17) place the finite matrix entries in the classical colored Mordell–Tornheim / cyclotomic multiple-polylogarithm class; PC-102 and the Zhao source anchor already delimit that period theory inside this research line.

The substantive research contribution is the **Prime-Circle scope theorem**: one of the principal escapes explicitly left by PC-180 and PC-181 — adding source-native radial depth and positive nonlocality before self-adjoint readout — has an exact selector/coercivity tradeoff. In the entire monotone scalar-depth/Stieltjes-kernel class, any genuine positive interior term necessarily assigns positive mass to non-prime-power shells that the signed flux had annihilated.

A directed literature check found the relevant kernel and period mechanisms on the classical side before any RH interpretation. No prior-art claim is made for the project-specific statement that this class fails the Prime-Circle matched-control selector test.

## 8. Boundary of the negative result

This finding does **not** reject the broader accepted signed-radial-flux clue. It does not cover:

- sign-changing or nonmonotone radial weights, where `w'` is not positive and cancellation can survive;
- genuinely two-depth kernels not representable as `w(min(u,v))` with monotone `w`;
- a shell matrix `C(x)` whose eigenspaces themselves vary with radial depth and therefore introduce source-forced noncommutation;
- a second independent skew/ordered carrier combined with the PC-180 `Omega` before positive scalarization;
- higher-order radial tensors, nonlinear ordered assemblies, or growing/all-shell operator domains.

Those are real escapes rather than loopholes in the proof. Any positive continuation must show that the additional structure is forced by the roots-of-unity/refinement geometry and, on a mixed control containing a non-prime-power shell, preserves a nontrivial signed cancellation or yields a target-relevant sign/coercivity statement not present in the classical Tornheim/Volterra controls.

## Audit / falsification test

The central identity can be falsified by any admissible `w` and shell pair `(m,n)` for which direct integration of (1) violates (2). The nonlocal form can be falsified by a pair for which (7) and (8) disagree. The matched-control conclusion can be falsified only if `F_6` vanished almost everywhere despite (10), or if a strictly positive `w'` produced zero integral in (6); neither is possible.

The program-level negative classification would fail only by exhibiting a source-forced radial/nonlocal self-adjoint construction outside the monotone Stieltjes class that retains the signed non-prime-power cancellation and produces an RH-relevant invariant unavailable from the classical controls.