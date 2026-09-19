# MI-043 — Broad bounded exact-multiplicative operator classes reduce to scalar prime channels

**Evidence level:** exact synthesis from [PL-377](../../findings/PL-377-bounded-normal-infinite-representations-scalarize-to-measures-on-semicharacters.md) and [PL-378](../../findings/PL-378-uniformly-bounded-group-completion-unitarizes.md), extending the finite-dimensional classification PL-374--PL-376.

For a bounded normal completely multiplicative representation `rho:N->B(H)`, the commuting normal prime operators generate an abelian C*-algebra. Gelfand theory identifies them with scalar coordinate functions on a compact spectrum `X`, and every integer acts pointwise through a scalar semicharacter

`chi_x(n)=prod_p lambda_p(x)^(v_p(n))`.

Consequently every bounded linear observable is a measure mixture of scalar channels,

`L(rho(n)) = integral_X chi_x(n) dmu_L(x)`.

PL-377 therefore closes the idea that infinite Hilbert dimension plus normality creates irreducible cross-prime source geometry under exact complete multiplicativity.

PL-378 removes a complementary part of the nonnormal escape. Suppose every `rho(n)` is invertible, the semigroup representation extends to the group completion `G=Q_(>0)^x`, and the full group representation satisfies `sup_(q in G)||pi(q)||=M<infinity`. Because `G` is amenable, Day--Dixmier unitarization gives a bounded invertible `S` with condition number at most `M^2` such that `S pi(q) S^(-1)` is unitary for every `q`. The commuting unitary family has a spectral measure on the infinite prime torus, so its matrix coefficients are again Fourier--Stieltjes mixtures of scalar prime-torus characters.

Thus **nonnormality is not by itself a new arithmetic resource** when it can be removed by one uniformly controlled global change of Hilbert metric. Exact complete multiplicativity plus uniform group-like boundedness returns the representation to the same scalar character space, even though the original operators may look highly nonnormal.

The surviving boundary is now structural. One-sided noninvertible shifts do not extend to the rational group on the same space. Invertible semigroup representations may have inverse norms that grow and therefore fail the full-group bound. Unbounded/domain-sensitive models and controlled failures of exact multiplicativity lie outside Day--Dixmier. Metric-sensitive quantities such as pseudospectra, singular values or numerical ranges can survive similarity only if the original metric has an independent arithmetic meaning; otherwise they may reflect an arbitrary choice of equivalent Hilbert norm rather than source information.

The reusable audit is therefore not simply “operator-valued versus scalar.” Ask first whether the source algebra is abelian-normal; if not, ask whether group completion and uniform boundedness still make it unitarizable; if a proposed observable is not similarity-invariant, identify what makes the chosen metric source-canonical. Only a mechanism that survives those reductions has escaped the scalar prime-channel classification.

**Boundary.** PL-377 and PL-378 do not classify intrinsically one-sided noninvertible semigroups, inverse-norm growth, unbounded/domain-sensitive representations, nonlinear observables or controlled nonmultiplicativity. Similarity does not preserve every metric-sensitive nonnormal observable. Neither theorem supplies analytic continuation, zero localization or an RH criterion.