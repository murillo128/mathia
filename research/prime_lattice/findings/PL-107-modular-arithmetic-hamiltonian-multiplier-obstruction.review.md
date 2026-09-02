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