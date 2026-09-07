# PC-207 — finite Fourier-leg Hardy lift factorizes into rational Toeplitz tensors

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the most canonical fixed-finite-valence repair left open by PC-206: retain every individual positive Fourier leg before quotienting the tuple to the single signed mismatch.

PC-206 proved that retaining only the total signed mismatch `Delta` in the bilateral regular representation of `Z` is still just scalar Laurent data. It explicitly left the individual packet indices `(k_1,...,k_r,ell_1,...,ell_q)` as a possible richer state. Those indices are materially different from `Delta`: every leg is intrinsically positive, so the source-native shift model is a positive orthant rather than another bilateral lattice.

For a fixed finite number of Cauchy--Poisson character legs at strictly positive packet depths, however, that positive-orthant lift is exactly separable. On `ell^2(N_0^d)`, the full coefficient array is a rank-one tensor product of one-leg periodic sequences. The resulting shift operator is therefore a tensor product of one-variable analytic Toeplitz multipliers, and periodicity makes each one-variable symbol rational. Cross-coordinate commutators vanish even after adjoining adjoints. The spectrum of the full source operator is the closure of the range of one separated rational polydisc symbol, hence a continuum rather than a discrete spectral divisor.

Thus preserving all individual Fourier indices is not sufficient when they are retained only through their canonical commuting Hardy shifts. A surviving individual-leg mechanism must couple those coordinates nonseparably, let the state dimension/valence grow, take a genuinely singular zero-depth limit before bounded multiplier reduction, or introduce another source-forced relation beyond the common-angle quotient.

## 1. The pre-mismatch coefficient array is exactly a tensor product

Use the source-native character packets from PC-197--PC-206. Let `chi_i` be primitive nonprincipal characters modulo `n_i`, `1<=i<=r`, and `psi_j` primitive nonprincipal characters modulo `m_j`, `1<=j<=q`. Fix strictly positive depths

\[
x_i>0,
\qquad
y_j>0,
\]

and put `d=r+q`. Before the common angular exponent is collected, the product packet has coefficients

\[
a_{\mathbf k,\boldsymbol\ell}
=
\prod_{i=1}^r
 \chi_i(k_i)e^{-x_i k_i}
\prod_{j=1}^q
 \overline{\psi_j(\ell_j)}e^{-y_j\ell_j},
\qquad
k_i,\ell_j\ge1.
\tag{1}
\]

The common-angle map later remembers only

\[
\Delta(\mathbf k,\boldsymbol\ell)
=
\sum_i k_i-
\sum_j\ell_j,
\tag{2}
\]

but (1) is the full state before that quotient. Crucially, (1) already factorizes over the individual coordinates. No mixed coefficient depending jointly on two distinct legs is present at this stage.

Because all depths are positive,

\[
\sum_{\mathbf k,\boldsymbol\ell}
|a_{\mathbf k,\boldsymbol\ell}|<\infty.
\tag{3}
\]

Hence the full leg array defines bounded shift operators without any Abel, zeta, or distributional regularization.

## 2. The canonical positive-orthant lift is a tensor Toeplitz multiplier

Let

\[
\mathcal H_d
=
\ell^2(\mathbb N_0^d)
\cong
\bigotimes_{a=1}^d\ell^2(\mathbb N_0),
\tag{4}
\]

and let `S_a` be the unilateral shift in coordinate `a`. Extend (1) by zero when any coordinate is zero and define the source lift

\[
\mathbb A
=
C
\sum_{\nu\in\mathbb N_0^d}
 a_\nu S_1^{\nu_1}\cdots S_d^{\nu_d},
\tag{5}
\]

where `C` is the fixed product of Gauss-sum prefactors from the character packets. Equation (3) gives absolute convergence in operator norm.

For one character/depth pair define

\[
B_{\chi,x}(z)
:=
\sum_{k\ge1}\chi(k)e^{-xk}z^k.
\tag{6}
\]

Dirichlet characters are periodic. Therefore, with

\[
P_\chi(w)=\sum_{a=1}^{n}\chi(a)w^a,
\]

we have the exact rational identity

\[
\boxed{
B_{\chi,x}(z)
=
\frac{P_\chi(e^{-x}z)}
{1-e^{-nx}z^n}.
}
\tag{7}
\]

The poles of (7) have modulus `e^x>1`, so `B_{chi,x}` is analytic on a neighborhood of the closed unit disk. Applying (6) coordinate by coordinate to (5) gives

\[
\boxed{
\mathbb A
=
C
\prod_{i=1}^r B_{\chi_i,x_i}(S_i)
\prod_{j=1}^q B_{\overline{\psi_j},y_j}(S_{r+j})
=
C\bigotimes_{a=1}^d B_a(S).
}
\tag{8}
\]

Thus the faithful fixed-valence individual-leg lift is not merely commuting: it is exactly a separated tensor product of one-variable rational shift multipliers.

## 3. Hardy-space representation gives one separated rational symbol

Under the standard unitary identification

\[
\ell^2(\mathbb N_0^d)
\cong
H^2(\mathbb D^d),
\tag{9}
\]

`S_a` becomes multiplication by the coordinate function `z_a`. Hence (8) becomes

\[
\boxed{
\mathbb A\cong M_f,
\qquad
f(z_1,\ldots,z_d)
=
C\prod_{a=1}^d B_a(z_a).
}
\tag{10}
\]

The symbol is rational, analytic past the distinguished boundary, and completely separated by coordinate. This is the finite-polydisc analytic Toeplitz/Hardy multiplier model, not a new operator species.

Its spectrum can be identified directly. If

\[
\lambda\notin\overline{f(\mathbb D^d)},
\]

then `1/(lambda-f)` is a bounded analytic multiplier and supplies the inverse of `lambda I-M_f`. Conversely, for every `w in D^d`, the Hardy reproducing kernel satisfies

\[
M_f^*k_w
=
\overline{f(w)}k_w,
\tag{11}
\]

so `f(w)` belongs to the spectrum of `M_f`; closedness supplies the boundary. Therefore

\[
\boxed{
\operatorname{Spec}(\mathbb A)
=
\overline{f(\mathbb D^d)}.
}
\tag{12}
\]

For a nonzero packet this is a nontrivial connected continuum. It is not a discrete sequence on which a Hilbert--Polya interpretation could arise merely by retaining the leg coordinates. Since `A` is bounded on an infinite-dimensional space, no resolvent of `A` can be compact: if a resolvent were compact, multiplying it by the bounded operator `lambda I-A` would make the identity compact.

## 4. Adjoining adjoints does not create mixed-leg noncommutativity

The unilateral boundary means that a one-coordinate analytic Toeplitz multiplier need not commute with its own adjoint. That is a genuine difference from the bilateral `Z` channel of PC-206 and is the main falsification point that must be checked rather than silently replaced by a bilateral lattice.

It nevertheless does not create a mixed-shell carrier here. Let

\[
A_a=B_a(S_a).
\]

Distinct tensor coordinates satisfy exactly

\[
\boxed{
[A_a,A_b]=0,
\qquad
[A_a,A_b^*]=0
\quad(a\ne b).
}
\tag{13}
\]

Every finite word in the coordinate multipliers and their adjoints can therefore be regrouped coordinatewise into a finite sum of separated tensors. In particular, all nonnormal Toeplitz boundary effects live inside independent one-variable factors; no commutator couples two different character legs unless an additional nonseparable operator is inserted.

This is the decisive distinction. The positive boundary at index zero is source-forced for each leg, but **its Toeplitz defect is coordinate-local**. Positivity of the individual indices by itself does not manufacture the mixed-prime off-diagonal interaction sought by the Prime-Circle mandate.

## 5. The common-angle quotient recovers the already classified scalar/conical side

The relation to PC-202--PC-206 is exact. On the distinguished torus, the original common angular variable is recovered by the diagonal/anti-diagonal substitution

\[
z_i=e^{i\theta}
\quad(1\le i\le r),
\qquad
z_{r+j}=e^{-i\theta}
\quad(1\le j\le q).
\tag{14}
\]

Then the separated polydisc symbol becomes precisely the original scalar packet product

\[
f(e^{i\theta},\ldots,e^{i\theta},
  e^{-i\theta},\ldots,e^{-i\theta})
=F(\theta).
\tag{15}
\]

Collecting Fourier exponents along (14) pushes the full tuple to the single mismatch (2), giving the `ell^2(Z)` Laurent channel classified by PC-206. Haar contraction instead imposes the corresponding linear matching relation and, after Mellinization, gives the rational-cone Dirichlet data classified by PC-201/PC-202 and its anchor-filter extensions.

Thus the canonical finite-valence picture has both ends classified:

\[
\boxed{
\text{independent leg coordinates}
\;\longrightarrow\;
\text{separated rational Hardy tensor},
\qquad
\text{common-angle quotient}
\;\longrightarrow\;
\text{Laurent/conical scalar data}.
}
\tag{16}
\]

There is no hidden coupled operator layer between those two descriptions unless the geometry supplies a new relation that acts before the quotient and is not coordinate-separable.

## 6. Prior-art and novelty audit

The analytic framework is classical. Periodicity of a Dirichlet character gives the rational generating function (7) by a geometric-series decomposition. The Hardy model of unilateral shifts and multivariable Toeplitz operators on polydiscs is standard operator theory. The local `SOURCES.md` already contains Guo--Yan, *Toeplitz operators on the Hardy space over the infinite-dimensional polydisc* (2022), as a modern symbolic-calculus anchor; its finite-variable sector contains the ordinary polydisc Toeplitz setting used here. A fresh directed check also found the finite-polydisc Brown--Halmos framework of Maji--Sarkar--Sarkar, *Bulletin des Sciences Mathématiques* 146 (2018), 33--49, DOI `10.1016/j.bulsci.2018.03.005`.

No novelty is claimed for rational periodic generating functions, unilateral shifts, Hardy multipliers, tensor products, or equations (9)--(13) as abstract operator theory. PC-198 already used the same periodic rationality to classify finite same-variable holomorphic shell products, while PC-202 and PC-206 classify the scalar quotients of the present state.

The durable line-specific contribution is the closure statement: **the most canonical fixed-finite-valence state that really does retain every individual positive Fourier index still factorizes into independent rational Toeplitz coordinates and therefore does not create a new mixed arithmetic operator geometry.**

## 7. Falsification controls and surviving boundary

The conclusion depends on assumptions that should remain explicit.

First, the packet valence `d` is fixed and finite. A state whose number of leg coordinates grows with refinement, or an infinite-depth limit formed before finite contraction, is not classified here. Second, every packet depth is strictly positive. The singular limit `x_a -> 0+` moves the rational poles in (7) onto the unit circle; a limit taken at the operator level before bounded Hardy reduction needs a separate domain/renormalization analysis and is not covered by (10)--(12).

Third, the coefficient tensor is the source product (1). Any shell/refinement-dependent kernel that couples two coordinates before multiplication, any noncommuting transfer relation forced by old/new incidence, or any nonseparable constraint beyond the common-angle map (14) lies outside the theorem. Likewise, global uniformization/monodromy is untouched.

The matched nonarithmetic control is sharp: replace every character in (1) by any bounded periodic sequence. Equations (3), (7), (8), (10), and the cross-coordinate commutation (13) remain true. Hence the operator architecture itself carries no prime-specific discriminator; arithmetic remains solely in the rational one-leg symbols.

## Research consequence

PC-206's surviving phrase "retain the individual Fourier legs" must now be narrowed. For fixed finite valence at positive depth, the canonical faithful lift is already exhausted:

\[
\boxed{
\text{full positive leg tuple}
\;\longrightarrow\;
\text{tensor product of rational analytic Toeplitz multipliers}
\;\longrightarrow\;
\text{continuous separated spectrum}.
}
\tag{17}
\]

A viable continuation must therefore retain **nonseparable** leg information, make the state genuinely grow/infinite before contraction, exploit a singular zero-depth boundary with controlled domains, or derive another source-forced nonabelian/refinement relation. Merely replacing the total mismatch basis by the full finite tuple basis is not enough.