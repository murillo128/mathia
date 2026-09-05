# PC-181 — skew flux functional calculus is prime-blind on the mixed `{2,6}` control

**Status:** `EXACT-DERIVED` + `CLASSICAL-LINEAR-ALGEBRA` + `DECISIVE-NEGATIVE` for positive or self-adjoint repairs that first compress the signed radial flux–potential interaction to the skew carrier from PC-180 and then apply functional calculus to that carrier alone.

PC-180 leaves one precise piece of radial interior information after the constant self-adjoint first-order sector collapses to the von-Mangoldt boundary vector: the real skew matrix

\[
\Omega:=\frac{A-A^{\mathsf T}}2,
\qquad
A_{mn}=\int_0^\infty \rho_m(x)F_n(x)\,dx.
\]

A natural next attempt is therefore to turn `Omega` into a positive/self-adjoint object by squaring it, taking its modulus, or applying a spectral function to `i Omega`. The simplest source-native mixed control already rules out that whole repair as a way to preserve the prime-power selector. On the two-shell family `{2,6}`, the skew carrier is nonzero but every positive functional-calculus readout gives exactly the same diagonal response to the prime-power shell `2` and the non-prime-power shell `6`.

This does not show that the pairwise magnitude stored in `Omega` is trivial. It shows something narrower and decisive for the accepted signed-flux clue: **once the first-order ordered interior has been compressed to `Omega`, positivity obtained from `Omega` alone cannot retain shellwise Mangoldt support.** A surviving route needs additional source-forced structure before or alongside this compression.

## 1. The `{2,6}` mixed shell gives an exact nonzero skew block

Use the Prime-Circle radial fields from PC-179,

\[
F_n(x)=\log\Phi_n(e^{-x}),
\qquad
\rho_n(x)=-F_n'(x),
\]

and the ordered matrix `A` from PC-180. Since

\[
\Lambda(2)=\log 2,
\qquad
\Lambda(6)=0,
\]

PC-180 gives

\[
A_{2,6}+A_{6,2}=0.
\tag{1}
\]

The off-diagonal term is not zero. Indeed

\[
\rho_2(x)=\frac1{e^x+1}>0,
\]

while

\[
\Phi_6(r)=1-r+r^2=1-r(1-r)
\]

satisfies

\[
0<\Phi_6(r)<1
\qquad(0<r<1).
\]

Hence

\[
F_6(x)=\log\Phi_6(e^{-x})<0
\qquad(x>0),
\]

and therefore

\[
\boxed{
\omega:=A_{2,6}
=\int_0^\infty \rho_2(x)F_6(x)\,dx
=\int_0^1\frac{\log(1-r+r^2)}{1+r}\,dr
<0.
}
\tag{2}
\]

Numerically `omega ~= -0.12693500084879647`, only as an audit check; the strict sign in (2) is exact.

By (1), `A_{6,2}=-omega`, so on the ordered basis `(2,6)` the surviving skew carrier is exactly

\[
\boxed{
\Omega_{\{2,6\}}
=
\begin{pmatrix}
0&\omega\\
-\omega&0
\end{pmatrix},
\qquad \omega\ne0.
}
\tag{3}
\]

Thus the control is not killing the interior information by making the coupling vanish. It isolates a genuinely nonzero piece of the ordered radial interior.

## 2. Squaring or taking the modulus loses the selector maximally

Equation (3) immediately gives

\[
\boxed{
-\Omega_{\{2,6\}}^2
=\omega^2 I_2>0.
}
\tag{4}
\]

Since `Omega^T Omega=-Omega^2`, its positive modulus is likewise

\[
\boxed{
|\Omega_{\{2,6\}}|
=\sqrt{\Omega^{\mathsf T}\Omega}
=|\omega|I_2.
}
\tag{5}
\]

Let `e_2,e_6` denote the two shell-coordinate vectors. Then

\[
\boxed{
\langle e_2,-\Omega^2 e_2\rangle
=
\langle e_6,-\Omega^2 e_6\rangle
=\omega^2,
}
\tag{6}
\]

and the same equality holds for `|Omega|`.

This is the opposite of the matched-control behavior required by the signed-flux clue. The raw signed fields distinguish the two shells sharply: shell `2` has positive total flux `log 2`, whereas shell `6` has total flux zero and must change sign. The canonical nonlinear positivity repair `-Omega^2`, however, assigns them **identical strictly positive response**.

## 3. The obstruction covers the full one-carrier Hermitian functional calculus

The same collapse is not special to the square. Put

\[
H:=i\Omega_{\{2,6\}},
\qquad
\sigma:=|\omega|>0.
\]

Then `H` is Hermitian and

\[
H^2=\sigma^2 I_2,
\qquad
\operatorname{Spec}(H)=\{-\sigma,+\sigma\}.
\tag{7}
\]

For any real-valued scalar function `g` defined on these two spectral points, the finite spectral calculus reduces exactly to

\[
\boxed{
g(H)=\alpha I_2+\beta H,
}
\tag{8}
\]

where

\[
\alpha=\frac{g(\sigma)+g(-\sigma)}2,
\qquad
\beta=\frac{g(\sigma)-g(-\sigma)}{2\sigma}.
\tag{9}
\]

Because `H` has zero diagonal in the shell basis,

\[
\boxed{
\langle e_2,g(H)e_2\rangle
=
\alpha
=
\langle e_6,g(H)e_6\rangle.
}
\tag{10}
\]

If `g(+/- sigma)>=0`, then `g(H)` is positive semidefinite, but equation (10) still forces equal prime-power and non-prime-power diagonal response. Even the two spectral projectors

\[
P_\pm=\frac12\left(I_2\pm\frac{H}{\sigma}\right)
\]

have diagonal `(1/2,1/2)`.

There is an equivalent purely real statement. Since `Omega^2=-sigma^2 I`, every real polynomial in `Omega` has the form `a I+b Omega`; if the result is required to be real symmetric, its odd part vanishes and only the scalar `a I` remains. Therefore no choice of polynomial degree repairs the selector after this compression.

## 4. Why this is a decisive Prime-Circle control rather than a generic toy example

The pair `{2,6}` is intrinsic to the original roots-of-unity tower. It uses the common anchored circle construction at the smallest prime-power shell and the smallest shell with two distinct prime factors. No matched non-arithmetic configuration, external normalization, radial kernel, or spectral parameter is inserted.

Moreover the coupling is exactly nonzero by (2). The failure therefore cannot be blamed on an accidental decoupling. It comes from the geometry of a single surviving skew degree of freedom: a two-dimensional real skew carrier has only one singular value, and every positive function of that carrier necessarily treats its two coordinate directions symmetrically.

The scalar `sigma=|omega|` can still carry information about the pair `(2,6)`. This finding does **not** claim that every all-shell invariant built from the collection of such off-diagonal magnitudes is classical or useless. It rules out the more specific route needed by the signed-flux positivity clue: obtaining a shellwise sign/coercivity margin with vanishing or suppressed non-prime-power response by applying a positive/self-adjoint function to `Omega` alone.

## 5. Prior-art and novelty audit

The matrix theory in Sections 2 and 3 is standard finite-dimensional linear algebra: real skew-symmetric matrices reduce to two-dimensional rotation blocks, and a scalar matrix function on a two-point spectrum is affine in the corresponding matrix. A directed check of standard matrix-analysis and matrix-function literature places those ingredients entirely on the classical side. No novelty is claimed for them, and no external theorem is needed for the proof because the complete two-by-two calculation appears above.

The research contribution is the **source-specific falsification control**: the first nonzero mixed Prime-Circle skew block is enough to show that the nonlinear `Omega`-only positivity escape explicitly left open by PC-180 does not preserve the exact prime-power selector. This is a restriction of the Prime-Circle candidate architecture, not a new theorem about skew matrices.

## 6. Boundary of the negative result

This finding does not rule out:

- a second independent, intrinsically derived noncommuting or skew structure paired with `Omega`;
- a radial-depth-dependent mixer or genuinely nonlocal kernel acting on `F_n(x),rho_n(x)` **before** compression to `A` and `Omega`;
- higher-order radial tensors that retain more than the first-order ordered matrix;
- all-shell constructions whose essential invariant is an off-diagonal magnitude, cycle, or commutator rather than a positive functional calculus of one skew carrier;
- growing/infinite shell limits where the operator domain or topology contributes new source-forced data.

In particular, multiplying `Omega` by an independently derived operator could break the two-shell symmetry. That would be genuinely new input and must be audited on its own; it is not supplied by taking a more elaborate function of `Omega`.

## 7. Audit and falsification test

The result can be falsified at its source by either of two elementary checks:

1. direct evaluation of `A_{2,6}` contradicts the strict sign in (2); or
2. a scalar function `g` on `{+/-sigma}` produces a matrix `g(i Omega)` whose two diagonal shell responses differ.

The first is impossible because its integrand is strictly negative for every `x>0`. The second is impossible by the exact two-point interpolation formula (8)-(10).

A later result would escape rather than falsify this finding if it uses additional source-forced structure not measurable from `Omega` alone.

## Research consequence

PC-179 closed shellwise Mellinization, and PC-180 closed constant self-adjoint first-order mixing while leaving `Omega` as the only ordered radial interior carrier. PC-181 now closes the **one-carrier nonlinear positivity repair**: squaring `Omega`, taking its modulus, taking positive spectral functions of `i Omega`, or any equivalent real-symmetric polynomial construction cannot retain the Mangoldt selector even on the exact mixed `{2,6}` control.

The signed-radial-flux clue therefore remains live only if Prime-Circle supplies an additional operation before or alongside `Omega`: a source-forced radial nonlocality/depth dependence, a second noncommuting structure, a higher-order object, or an all-shell interaction whose useful invariant is not positive functional calculus of the first-order skew matrix alone.