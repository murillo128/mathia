# MI-006 — Mixed-prime coupling must precede positivity; shellwise radial scalarization and semigroup promotion do not preserve the selector

**Evidence level:** supported through WP-164 by exact completion/resultant calculations, toric torsion rigidity, cyclotomic radial identities, Mellin classification, and complete-monotonicity obstruction

## Core intuition

The critical one-prime Weil rays can live inside a positive all-prime carrier only if genuinely mixed-prime or finite--archimedean information is present **before** positive completion. Canonical filling, determinants, tensor products, normalization, and shellwise positive scalarization cannot manufacture an interaction missing from the source incidence.

The cyclotomic radial path sharpens this ordering principle. It carries the exact Mangoldt selector in signed form, but that selector is destroyed by every nearby positive Mellin homogeneity and cannot be reinterpreted, even on prime-power shells where the flux is pointwise positive, as a positive self-adjoint semigroup coefficient.

## Strongest justified principle

WP-096--WP-160 establish the algebraic/completion boundary: exact sparse positivity needs mixed mass; normalized all-prime/resultant data universalize; canonical cell filling preserves flatness; block/tensor determinant constructions factor; and any scalable fixed finite-arity algebraic torsion incidence returns to translated torus geometry and prime-primary splitting.

WP-161--WP-162 change category to a genuine real radial deformation. The centered potential has boundary value `Lambda(n)`, and its inward flux `rho_n(s)` has total mass `Lambda(n)` and is pointwise positive for all `s>0` exactly on prime powers. Mixed-prime Mangoldt zeros arise from cancellation of positive and negative radial flux, so shellwise positive norms/energies immediately lose the selector.

WP-163 classifies the canonical dilation-homogeneous scalarizations. For `alpha>0`, the Mellin readout is

`-Gamma(alpha) zeta(alpha) n^(1-alpha) prod_{p|n}(1-p^(alpha-1))`.

The sparse Mangoldt support occurs **only at `alpha=1`**, through the critical pole-zero cancellation. For `0<alpha<1` every shell becomes positive; for `alpha>1` every shell is nonzero with parity sign. Positivity and sparse support cannot coexist inside this shellwise Mellin family.

WP-164 closes the next operator-positive interpretation. Every `rho_n` fails complete monotonicity; already `rho_n'''(0+)=J_4(n)/120>0`. Hence no positive measure Laplace representation and no coefficient `<v,e^{-sA}v>` of a nonnegative self-adjoint semigroup can equal the flux. This remains true for finite positive mixtures of radial scales. The prime-power control `rho_2(s)=1/(e^s+1)>0` makes the distinction between pointwise and operator positivity explicit.

## What remains possible

A surviving positive route must keep the signed flux through a genuinely coupled finite--archimedean or mixed-prime operation and impose positivity only after that coupling. Alternatively it must change the operator/category before positivity so that the new source object is not a shellwise scalar Mellin/Laplace readout of `rho_n`.

Live categories include source-varying/growing-arity incidence, nonlocal or cohomological finite--archimedean coupling, and noncommuting signed assemblies. They must still survive the earlier critical roughness, spectator-prime, domain, and exhaustion controls.

## Status / novelty

Resultants, toric Manin--Mumford, cyclotomic values, Jordan totients, Mellin/Bose integrals, complete monotonicity, and Bernstein--Widder theory are classical. The persisted synthesis is the source-ordering principle: **the radial selector is genuinely source-native, but shellwise attempts to make it positive either fill in its zeros or fail the operator-positive category; mixed signed coupling must precede positivity**.

## Falsification criterion

Produce a positive Mellin homogeneity `alpha!=1` retaining exact Mangoldt support, a positive-measure Laplace representation of a prime-power `rho_n`, or a source-forced coupled construction whose positivity is established only after assembly and whose mixed-prime cancellation survives the matched controls.

## Lean-formalizable core

- Mellin divisor-product formula and uniqueness of `alpha=1` for Mangoldt support.
- Sign classification for `alpha<1` and `alpha>1`.
- Boundary-jet complete-monotonicity obstruction and finite positive scale-mixture stability.
