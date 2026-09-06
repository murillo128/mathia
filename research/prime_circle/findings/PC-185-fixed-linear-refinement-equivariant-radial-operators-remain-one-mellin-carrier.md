# PC-185 — fixed linear refinement-equivariant radial operators remain one Mellin carrier

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` for obtaining a second Prime-Circle radial arithmetic carrier by applying any fixed bounded shell-independent linear operator, or any finite family of such operators, that is equivariant under the intrinsic integer refinement dilations.

PC-184 shows that every fixed finite Euler-derivative jet of the cyclotomic log-potential has Mellin fiber rank one. The natural escape is to replace finite local derivatives by a genuinely nonlocal radial filter. For the source-native symmetry class, that escape also collapses: on the weighted radial Hilbert spaces where every cyclotomic potential lives, integer-refinement equivariance forces every bounded linear filter to be a Mellin multiplier. A finite family therefore multiplies the same shell-dependent Mellin amplitude by a universal vector of symbols; it cannot manufacture a second arithmetic carrier.

Moreover, because the cyclotomic potential Mellin amplitude is zero-free on every vertical line in its natural half-plane, any nonzero positive dilation-equivariant quadratic readout of such a family is strictly positive on every shell. Thus bounded linear scale-equivariant nonlocality cannot preserve the prime-power null selector either.

## 1. Weighted radial representation forced by refinement

For `n>1` put

\[
F_n(x)=\log\Phi_n(e^{-x}),\qquad x>0.
\]

For every `c>0`, let

\[
H_c=L^2\!\left((0,\infty),x^{2c-1}\,dx\right).
\]

Since `F_n` is bounded at `0+` and decays exponentially at infinity, `F_n\in H_c` for every `c>0`.

The normalized dilation representation

\[
(U_a^{(c)}f)(x)=a^c f(ax),\qquad a>0,
\]

is unitary on `H_c`. Its Mellin-Plancherel transform is

\[
(\mathcal M_c f)(t)
=\frac1{\sqrt{2\pi}}
\int_0^\infty f(x)x^{c+it-1}\,dx,
\]

under which

\[
\boxed{
\mathcal M_c U_a^{(c)}\mathcal M_c^{-1}
=M_{a^{-it}}.
}
\tag{1}
\]

Thus the intrinsic power refinements `x -> qx` act as the ordinary characters of the additive log-depth variable.

## 2. Integer refinement covariance already forces a Mellin multiplier

Let `T:H_c->H_c` be bounded and shell-independent, and assume only covariance under the actual integer refinement semigroup,

\[
TU_q^{(c)}=U_q^{(c)}T
\qquad(q=2,3,\ldots).
\tag{2}
\]

Because each `U_q^{(c)}` is unitary, (2) also gives commutation with `U_{1/q}^{(c)}` and hence with `U_r^{(c)}` for every positive rational `r`. Positive rationals are dense in `R_+`, the dilation representation is strongly continuous, and `T` is bounded. Therefore

\[
TU_a^{(c)}=U_a^{(c)}T
\qquad(a>0).
\tag{3}
\]

After Mellin-Plancherel, `T` commutes with every multiplier `e^{-it y}`, `y\in R`. This multiplication representation has spectral multiplicity one, so its commutant is the multiplication algebra. Hence there is an essentially bounded symbol `m_T(t)` such that

\[
\boxed{
\mathcal M_c(Tf)(t)=m_T(t)\mathcal M_c f(t).
}
\tag{4}
\]

This is the exact operator-theoretic form of the scale-invariant/Mellin-convolution principle. It includes arbitrary bounded nonlocal radial kernels in the covariance class; locality or finite differential order was never assumed.

## 3. Every finite family has shell Mellin rank one

PC-184 gives the exact Mellin transform

\[
\mathcal F_n(s)
:=\int_0^\infty F_n(x)x^{s-1}\,dx
=-\Gamma(s)\zeta(s+1)n^{-s}
\prod_{p\mid n}(1-p^s),
\qquad \Re s>0.
\tag{5}
\]

Let `T_1,...,T_r` be any fixed bounded operators satisfying (2), with multiplier symbols `m_1,...,m_r`. For

\[
J_n=(T_1F_n,\ldots,T_rF_n)^{\mathsf T},
\]

(4) gives

\[
\boxed{
\mathcal M_cJ_n(t)
=\mathcal F_n(c+it)
\begin{pmatrix}
m_1(t)\\
\vdots\\
m_r(t)
\end{pmatrix}.
}
\tag{6}
\]

At every Mellin frequency the entire internal fiber therefore has rank at most one in shell-dependent data. The vector of symbols is universal: it depends on the chosen filters, not on `n`. No number of fixed bounded scale-equivariant nonlocal filters can create an independent shell amplitude.

This is strictly broader than the finite Euler-jet obstruction in PC-184. Mellin convolution operators, bounded functions of the dilation generator, bounded scale filters, and other shell-independent nonlocal operators in the dilation commutant all obey (6).

## 4. Positive covariant readouts cannot preserve a prime-power null selector

Equation (5) is zero-free throughout its natural half-plane. Indeed, for `c>0`, `zeta(1+c+it)` is zero-free because its real part exceeds one; `Gamma` has no zeros; and

\[
|p^{c+it}|=p^c>1,
\]

so no factor `1-p^{c+it}` vanishes. Thus

\[
\boxed{
\mathcal F_n(c+it)\neq0
\quad\text{for every }n>1,\ t\in\mathbb R.
}
\tag{7}
\]

Now allow the most general bounded positive dilation-equivariant quadratic readout on the finite vector `J_n`. In Mellin space it is multiplication by a measurable positive-semidefinite matrix `W(t)`. Therefore

\[
Q(n)
=\int_{\mathbb R}
|\mathcal F_n(c+it)|^2
m(t)^*W(t)m(t)\,dt,
\tag{8}
\]

up to the common normalization of Mellin-Plancherel, where `m=(m_1,...,m_r)^T`.

The effective weight

\[
w(t)=m(t)^*W(t)m(t)\ge0
\]

is independent of the shell. If `Q(n_0)>0` for one shell, then `w` is nonzero on a set of positive measure. By (7), the same set contributes strictly positively for every other shell. Consequently, whenever the displayed energies are finite,

\[
\boxed{
Q(n_0)>0\text{ for one }n_0>1
\Longrightarrow
Q(n)>0\text{ for every }n>1.
}
\tag{9}
\]

In particular no such positive architecture can have a positive response on a prime power and zero response on a mixed-prime shell.

## 5. The raw flux does not contradict the one-carrier statement

The unweighted flux `rho_n=-F_n'` is not a bounded operator on a fixed `H_c`, so it is outside the bounded theorem above. But it illustrates the same graded mechanism rather than supplying a counterexample. Integration by parts gives

\[
\boxed{
\mathcal M_{c+1}\rho_n(t)
=(c+it)\,\mathcal M_cF_n(t).
}
\tag{10}
\]

Thus differentiation is an intertwiner from the weight-`c` dilation representation to the weight-`c+1` representation, and after the natural weight shift the raw flux again carries the same shell amplitude. For `n=2`, direct quadrature at generic complex `s` agrees with

\[
\mathcal M F_2(s)=\Gamma(s)\zeta(s+1)(1-2^{-s}),
\qquad
\mathcal M\rho_2(s+1)=s\,\mathcal M F_2(s),
\]

providing a numerical sign/shift control on (10).

PC-179 and PC-183 already classify the distinct endpoint-sensitive positive route exposed when `rho_n` is integrated at its `s=1` boundary. Equation (10) only says that raw differentiation does not create a second *interior* Mellin carrier once its natural scaling degree is respected.

## 6. Prior art and novelty boundary

No novelty is claimed for the abstract harmonic-analysis ingredients. The Mellin transform is Fourier analysis on the multiplicative group `R_+`; after `x=e^y`, dilation becomes translation, and bounded operators commuting with the full translation representation are Fourier multipliers. Scale-invariant nonlocal and fractional operators formulated through Mellin convolution are an established analytic class. A directed prior-art check found this classical scale/Mellin framework, not a Prime-Circle-specific second carrier.

The durable contribution is the Prime-Circle **architecture obstruction** obtained by combining that standard commutant fact with the exact cyclotomic amplitude (5): the intrinsic integer refinement semigroup is already dense enough, after taking inverses, to force the full multiplier form, and the resulting universal fiber cannot evade the zero-free shell factor on `Re(s)>0`.

This is not a claim that every conceivable nonlocal operator is a Mellin multiplier. It applies only to fixed shell-independent bounded linear operators respecting the exact refinement covariance. Shell-dependent operators, nonlinear operators, operators with an additional geometry-forced scale, and cross-shell maps whose shell labels participate in the operator are outside the theorem.

## 7. Consequence for the live radial frontier

The `signed-radial-flux` clue remains alive, but its phrase “genuinely nonlocal radial operator” now needs an additional qualifier. **Nonlocality by itself is not enough.** A fixed linear radial filter that respects the source refinement action is only a Mellin multiplier and cannot create either a second arithmetic carrier or a positive prime-power selector.

A surviving radial mechanism must therefore do at least one of the following before positive/self-adjoint collapse: make the operator depend intrinsically on shell or cross-level geometry; introduce a second source field not obtained by a fixed refinement-equivariant linear transform of `F_n`; use a nonlinear or ordered cross-shell construction; or derive a sign-changing/indefinite coupling whose covariance is not the scalar dilation commutant classified here. Arbitrarily choosing a non-covariant kernel or a multiplier containing zeta data would be external spectral input, not progress from the Prime-Circle geometry.

## Audit / falsification test

The operator claim can be falsified by a bounded shell-independent `T:H_c->H_c` satisfying (2) for every integer `q>=2` but whose Mellin conjugate is not multiplication by an essentially bounded function. The density/strong-continuity argument rules this out.

The positivity claim can be falsified by an admissible positive covariant readout with `Q(n_0)>0` for one shell and `Q(m)=0` for another. Equation (8) and the pointwise zero-free property (7) rule this out.