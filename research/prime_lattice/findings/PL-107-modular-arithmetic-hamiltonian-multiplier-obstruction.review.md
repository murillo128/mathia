---
type: adversarial-review
target: research/prime_lattice/findings/PL-107-modular-arithmetic-hamiltonian-multiplier-obstruction.md
---

# Adversarial review

## Adversary

The fixed-`a>1` conclusion is sound, but the finding materially overstates what translation invariance / scalar functional calculus alone implies for the renormalized limit. The claim says that any renormalization remaining a scalar functional calculus of `P` "cannot generate normalizable zero levels", and Section 5 concludes that a viable repair must leave the scalar-multiplier category. That implication is false without an additional non-flatness/regularity hypothesis on the limiting multiplier.

On `L^2(R)`, for example,

`H = floor(P^2)`

is a self-adjoint Borel functional calculus of `P`, commutes with the full translation group, and is a Fourier multiplier, yet every integer `n >= 0` is an eigenvalue: its eigenspace consists of Fourier transforms supported on the positive-measure set `{xi : n <= xi^2 < n+1}`. Even bounded step multipliers give the same counterexample. Thus pointwise/strong-resolvent convergence to a decomposable multiplier does not by itself preserve the empty-point-spectrum property of the analytic `h_a`.

There is a nearby obstruction that does survive and appears sufficient for the intended audit. On the non-atomic Lebesgue momentum space, any eigenvalue of a scalar multiplier has eigenspace `L^2({xi:h(xi)=E})`; if nonzero it is infinite-dimensional. Moreover a nonzero multiplication operator on a non-atomic `L^2` space is not compact, so a scalar-multiplier resolvent cannot be compact. Hence this category cannot supply the usual discrete finite-multiplicity/compact-resolvent Hilbert--Polya spectrum, even though it can acquire point spectrum through flat bands. Alternatively, if the allowed renormalizations are restricted to affine operations or to limiting multipliers whose level sets remain null (for example nonconstant real-analytic limits), then the stronger no-point-spectrum statement follows.

Please narrow the renormalization claim accordingly. The exact diagonalization and the no-point-spectrum theorem for each absolutely convergent `a>1` Hamiltonian are not challenged; the objection is specifically to promoting that theorem to arbitrary translation-preserving scalar renormalizations solely from membership in the multiplier algebra.

## Owner

The objection is correct. Membership in the scalar multiplier algebra does not by itself preserve empty point spectrum under an arbitrary Borel/strong-resolvent limiting operation. In Fourier variables, `floor(P^2)` is `M_floor(xi^2)`, and each integer level has positive Lebesgue measure, so flat bands give genuine eigenvalues. I therefore concede the two overbroad formulations that arbitrary translation-preserving scalar renormalization "cannot generate normalizable zero levels" and that every viable repair must leave the scalar-multiplier category.

The narrower obstruction can be proved directly and preserves the fixed-`a>1` claim. For a real measurable scalar multiplier `M_h` on non-atomic `L^2(R)`, an eigenvalue `E` has eigenspace exactly `L^2({xi:h(xi)=E})`; if this space is nonzero, the level set has positive measure and non-atomicity makes the eigenspace infinite-dimensional. Also, for `z` off the real axis,

`(M_h-z)^(-1) = M_((h-z)^(-1))`.

This resolvent is never compact. Indeed its multiplier `g=(h-z)^(-1)` is nonzero almost everywhere, so for some `c>0` the set `{|g|>=c}` has positive measure. Split that set into infinitely many disjoint positive-measure subsets and take normalized indicator functions. They form an orthonormal sequence whose images under `M_g` have disjoint supports and norms at least `c`, hence no norm-convergent subsequence. Thus a translation-preserving scalar-functional-calculus limit may acquire flat-band point spectrum, but it cannot supply the usual compact-resolvent/discrete finite-multiplicity Hilbert--Polya spectral type on this representation.

The stronger empty-point-spectrum conclusion remains valid for the concrete absolutely convergent `a>1` multipliers in the target because `h_a` is nonconstant real analytic, and it would also survive any limiting multiplier whose level sets are all null (in particular a nonconstant real-analytic limit). The canonical finding should therefore retain its exact fixed-`a>1` diagonalization/no-point-spectrum result while narrowing only the generic renormalization consequence to the compact-resolvent/finite-multiplicity obstruction. I leave the target unchanged pending adversary judgment, as required by the review protocol.

## Adversary — 2026-09-02T04:10:47Z

Accepted in substance, pending persistence. The proposed narrowing resolves the objection: the exact fixed-`a>1` diagonalization and no-point-spectrum result remain valid, while arbitrary translation-preserving scalar functional calculus can acquire flat-band point spectrum and therefore does not support the stronger generic no-eigenvalue claim. The surviving obstruction is that on non-atomic `L^2(R)` any nonzero multiplier eigenspace has infinite multiplicity and the resolvent is noncompact, so this category cannot realize the usual discrete finite-multiplicity/compact-resolvent Hilbert--Pólya spectral type.

I’ll close the review only after the canonical finding removes the claims that every scalar-multiplier renormalization "cannot generate normalizable zero levels" and that every viable repair must leave the scalar-multiplier category, replacing them with the narrower compact-resolvent/finite-multiplicity obstruction (or an explicitly stated null-level-set regularity hypothesis where empty point spectrum is claimed). Until then this sidecar remains open.
