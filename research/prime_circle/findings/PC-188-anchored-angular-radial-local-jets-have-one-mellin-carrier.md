# PC-188 — anchored angular-radial local jets have one Mellin carrier

**Status:** `EXACT-DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-NEGATIVE` for obtaining a second Prime-Circle arithmetic carrier from any fixed finite collection of local angular/radial derivatives of the cyclotomic log-potential along the common anchored ray, after the scale normalization forced by power refinement.

PC-184 and PC-185 show that finite radial Euler jets and fixed bounded refinement-equivariant radial filters remain one shell-dependent Mellin carrier. They deliberately leave angular-radial coupled data outside those theorems. The most immediate genuinely two-dimensional repair is therefore to keep the full holomorphic cyclotomic field near the anchored radial ray and adjoin angular derivatives, or equivalently its harmonic conjugate, before any positive/self-adjoint scalarization.

That repair does not create a second local carrier. On the logarithmic cover of the punctured disk, holomorphy forces every mixed angular/radial derivative on the anchored ray to be a universal phase times an ordinary radial derivative of the same scalar profile. After scale normalization, every finite two-dimensional local jet is a finite Euler jet of PC-184. Its Mellin fiber therefore has rank one in shell-dependent data, and every nonzero positive shell-independent refinement-covariant quadratic readout is positive on every shell rather than retaining the prime-power/Mangoldt null selector.

This closes the **finite local angular-radial** escape only. Global angular information, nonlocal couplings between different angles or radii, shell-dependent operators derived from chord/old-new geometry, nonlinear products of local jets, and genuinely new second source fields remain outside the result.

## 1. The full cyclotomic field is holomorphic on the logarithmic half-plane

For `n>1`, `Phi_n` has all of its zeros on the unit circle and satisfies `Phi_n(0)=1`. Hence there is a unique holomorphic logarithm on the open unit disk normalized by

\[
L_n(z):=\Log\Phi_n(z),
\qquad
L_n(0)=0.
\]

Use logarithmic polar coordinates

\[
z=e^{-w},
\qquad
w=x-i\theta,
\qquad
x>0.
\]

Define

\[
G_n(w):=L_n(e^{-w}),
\]

which is holomorphic on the right half-plane `Re(w)>0`, and write

\[
u_n(x,\theta):=\Re G_n(x-i\theta),
\qquad
v_n(x,\theta):=\Im G_n(x-i\theta).
\]

Thus `u_n=log|Phi_n(e^{-x+i theta})|` is the two-dimensional logarithmic potential and `v_n` is its harmonic conjugate on the chosen disk branch.

On the anchored ray `theta=0`, `Phi_n(e^{-x})` is positive. Indeed it is real, nonzero on `0<e^{-x}<1`, and tends to `Phi_n(0)=1` as `x->infinity`, so its sign cannot change. Therefore

\[
\boxed{
G_n(x)=F_n(x):=\log\Phi_n(e^{-x})\in\mathbb R
}
\qquad(x>0).
\tag{1}
\]

All ordinary derivatives `G_n^{(k)}(x)` are real on this ray as well.

## 2. Every mixed local derivative is one radial derivative with a universal phase

Because `w=x-i theta`, differentiation gives

\[
\partial_x G_n=G_n'(w),
\qquad
\partial_\theta G_n=-iG_n'(w).
\]

The partial derivatives commute, so for all integers `a,b>=0`,

\[
\boxed{
\left.
\partial_x^a\partial_\theta^bG_n(x-i\theta)
\right|_{\theta=0}
=(-i)^b F_n^{(a+b)}(x).
}
\tag{2}
\]

Taking real and imaginary parts yields the complete anchored-ray Cauchy--Riemann reduction. If `b` is even,

\[
\boxed{
\partial_x^a\partial_\theta^b u_n(x,0)
=(-1)^{b/2}F_n^{(a+b)}(x),
\qquad
\partial_x^a\partial_\theta^b v_n(x,0)=0,
}
\tag{3}
\]

while if `b` is odd,

\[
\boxed{
\partial_x^a\partial_\theta^b u_n(x,0)=0,
\qquad
\partial_x^a\partial_\theta^b v_n(x,0)
=(-1)^{(b+1)/2}F_n^{(a+b)}(x).
}
\tag{4}
\]

Thus adjoining the harmonic conjugate does not supply an independent local field on the anchored ray. A particularly revealing first-order identity is

\[
\boxed{
\partial_\theta v_n(x,0)
=-F_n'(x)
=\rho_n(x),
}
\tag{5}
\]

where `rho_n` is exactly the signed radial flux of PC-179. The apparently transverse first angular derivative of the conjugate field is the already-classified inward radial flux.

Equations (2)--(5) are stronger than a boundary-jet statement. PC-020 classifies the finite differential jet at the common vertex `x=0` as Jordan-totient data. Here the collapse holds at **every interior depth `x>0`** along the anchored ray before endpoint evaluation.

## 3. Refinement-normalized two-dimensional jets are exactly Euler jets

The intrinsic power refinement `z -> z^q` acts on logarithmic polar coordinates by

\[
\boxed{(x,\theta)\longmapsto(qx,q\theta).}
\tag{6}
\]

A local derivative of total order

\[
k=a+b
\]

therefore has scale degree `k`. The source-natural dimensionless normalization along the anchored ray is

\[
J_{a,b}^{(n)}(x)
:=x^{a+b}
\left.
\partial_x^a\partial_\theta^bG_n(x-i\theta)
\right|_{\theta=0}.
\tag{7}
\]

Let

\[
D:=x\frac{d}{dx}.
\]

The elementary identity

\[
x^k\frac{d^k}{dx^k}
=D(D-1)\cdots(D-k+1)
\tag{8}
\]

gives from (2)

\[
\boxed{
J_{a,b}^{(n)}
=(-i)^b P_k(D)F_n,
\qquad
P_k(D):=D(D-1)\cdots(D-k+1).
}
\tag{9}
\]

Consequently **any fixed finite linear collection of scale-normalized local angular/radial derivatives of `u_n` and `v_n` along the anchored ray is a fixed finite Euler jet of `F_n`**. Angular directions change only the universal coefficient/phase vector; they do not add shell-dependent data.

This is exactly the hypothesis class classified by PC-184. It also covers any fixed finite linear recombination of the normalized jet components. Nonlinear products of components are not being reduced to a linear Euler jet and remain outside this finding.

## 4. Mellin fiber rank remains one

PC-184 derives, for `Re(s)>0`,

\[
\mathcal F_n(s)
:=\int_0^\infty F_n(x)x^{s-1}\,dx
=-\Gamma(s)\zeta(s+1)n^{-s}
\prod_{p\mid n}(1-p^s),
\tag{10}
\]

and proves

\[
\boxed{
\mathcal F_n(s)\neq0
\qquad(n>1,\ \Re(s)>0).
}
\tag{11}
\]

The Mellin Euler rule is

\[
\mathcal M[D f](s)=-s\,\mathcal M[f](s).
\tag{12}
\]

Applying it to (9) gives

\[
\boxed{
\mathcal M[J_{a,b}^{(n)}](s)
=(-i)^bP_k(-s)\,\mathcal F_n(s).
}
\tag{13}
\]

For an arbitrary fixed finite two-dimensional local jet `J_n`, there is therefore a universal vector `p(s)`, independent of `n`, such that

\[
\boxed{
\widehat J_n(s)=\mathcal F_n(s)p(s).
}
\tag{14}
\]

The shell-dependent Mellin fiber has rank at most one. The same scalar amplitude appears whether the chosen coordinates are radial derivatives, angular derivatives, the harmonic pair `(u_n,v_n)`, or any fixed finite linear mixture of them.

One can equivalently keep the derivatives unnormalized and place order-`k` derivatives in their natural weight-shifted dilation spaces. Repeated integration by parts gives

\[
\int_0^\infty F_n^{(k)}(x)x^{s+k-1}\,dx
=(-1)^k(s)_k\mathcal F_n(s),
\tag{15}
\]

where `(s)_k=s(s+1)...(s+k-1)`. Thus the one-carrier statement is not an artifact of multiplying by `x^k`; the normalization simply puts all derivative orders in one common refinement representation.

## 5. Positive self-adjoint readouts still lose the Mangoldt selector

Take any finite jet of the form above and any fixed shell-independent positive matrix-valued kernel in the scalar-homogeneous refinement class of PC-184. After Mellin diagonalization its shell energy has the form

\[
Q(n)
=\int_{\mathbb R}
|\mathcal F_n(c+it)|^2\,d\nu(t),
\qquad c>0,
\tag{16}
\]

for one positive effective measure `nu` independent of `n`.

By (11), if `nu` is nonzero then the integrand is strictly positive for every shell at every frequency in its support. Therefore, whenever the energies are finite,

\[
\boxed{
Q(n_0)>0\text{ for one shell }n_0>1
\Longrightarrow
Q(n)>0\text{ for every shell }n>1.
}
\tag{17}
\]

In particular the exact mixed control cannot be preserved:

\[
\Lambda(2)=\log2,
\qquad
\Lambda(6)=0,
\]

but any nonzero positive readout (16) assigns positive energy to both shell `2` and shell `6`.

The angular component does not repair this failure. Equation (5) shows that its first transverse datum is the PC-179 signed flux, while higher local angular derivatives only move farther along the same derivative ladder. The prime-power endpoint anomaly can still be recovered through the singular boundary-sensitive flux integration already classified in PC-179/PC-183, but it is not an independent two-dimensional interior Mellin channel.

## 6. Adversarial controls and exact boundary

Several potential loopholes are load-bearing and therefore explicit.

First, the result uses the **anchored ray** `theta=0`. It does not say that the full angular field at different angles is determined by one radial sample after a nonlocal operation. Holomorphy determines local Taylor data, but a global angular coupling may retain spatial relations that are destroyed by restricting to one ray.

Second, the theorem concerns a **fixed finite local linear jet**. Products, determinants, nonlinear functions of several local derivatives, or growing derivative order can create Mellin convolutions or require new topologies. Such constructions must be audited separately rather than being declared covered by (14).

Third, the positive readout conclusion imports the same shell-independent scalar-homogeneous refinement hypotheses as PC-184. A shell-dependent matrix law, non-scalar refinement cocycle, indefinite kernel, singular boundary distribution, or operator derived jointly from radial and chord/old-new geometry is outside (16).

Fourth, marking the common ray is essential. At an arbitrary angle `theta_0`, the same holomorphic derivative identity still holds with the local complex value `G_n^{(k)}(x-i theta_0)`, but that value is no longer determined by the real radial profile `F_n(x)`. The present no-go is specifically about using the **common-anchor direction** as the proposed second local carrier.

The exact identity (2) can be falsified immediately by any `n>1`, `x>0`, and derivative orders `a,b` for which direct differentiation of `log Phi_n(e^{-x+i theta})` at `theta=0` disagrees with `(-i)^bF_n^{(a+b)}(x)`. Symbolic checks on composite controls such as `n=6` reproduce (2) through several mixed derivative orders; the proof itself is simply the chain rule for a holomorphic function. The Mellin conclusion can be falsified only if a scale-normalized mixed derivative escapes the polynomial-in-`D` form (9), or if the zero-free statement (11) fails in `Re(s)>0`; equations (8)--(10) exclude both possibilities.

## 7. Prior-art and novelty audit

No historical novelty is claimed for the analytic ingredients. Cauchy--Riemann theory makes angular and radial derivatives of a holomorphic function locally dependent, and logarithmic/polar formulations of holomorphic functions together with Mellin differentiation are classical. Modern polar-analytic literature also treats Cauchy formulas and differentiation in Mellin settings; this is neighboring analytic language, not a Prime-Circle novelty claim. Mellin diagonalization of the Euler/dilation generator and positive matrix-valued homogeneous kernels were already audited against standard harmonic analysis and operator-valued Bochner theory in PC-184/PC-185.

The cyclotomic input is likewise already canonical: `G_n` is only the holomorphic logarithm whose real part is the persisted Prime-Circle potential. The durable contribution is therefore a **line-specific architecture obstruction** obtained by combining these standard facts with the exact Prime-Circle refinement representation: the most obvious local two-dimensional candidate left outside PC-184 does not supply the missing second arithmetic carrier.

This finding is not a claim that two-dimensional Prime-Circle geometry is classicalized in full. PC-062 already closes fixed rotationally invariant linear spectralization on the round sphere; the present result closes a different, more local route in logarithmic coordinates. Neither theorem covers a source-forced nonlocal angular-radial interaction that mixes distinct spatial points before reduction to one ray or one Fourier multiplier.

## Research consequence

The phrase “add angular information” is now too weak as a continuation of the signed-radial program. Along the common anchored ray, the harmonic conjugate and every finite transverse derivative are only Cauchy--Riemann copies of the same radial derivative tower, and after refinement normalization that tower has Mellin fiber rank one.

A genuinely new second carrier must therefore enter **nonlocally or relationally before anchored-ray jet compression**: for example through a source-forced coupling of distinct angles/radii, a shell-dependent chord/old-new operator acting jointly with the radial field, a nonlinear/growing-order construction with a controlled limit, or another field not holomorphically generated by the same cyclotomic logarithm. Any such candidate must still pass the mixed-prime control and the existing cyclotomic/Mellin/classicalization gates rather than treating its two-dimensional appearance as evidence of new RH structure.