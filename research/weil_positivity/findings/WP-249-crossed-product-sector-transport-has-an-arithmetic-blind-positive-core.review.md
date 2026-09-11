---
type: adversarial-review
target: research/weil_positivity/findings/WP-249-crossed-product-sector-transport-has-an-arithmetic-blind-positive-core.md
---

# Adversarial review

## Adversary

Section 1 justifies the existence of the product automorphism `alpha` by saying that every quasi-local observable has finite support. That is false for the algebra defined in (1): `A` is the norm closure of the finite-support local algebras, so a general quasi-local element need not have finite prime support; Section 5 itself correctly acknowledges this for nonlocal coefficients.

The main crossed-product obstruction appears repairable, but the `EXACT-DERIVED` setup needs the actual extension argument. The local tensor automorphisms must be shown compatible under the inclusions `A_F -> A_{F'}` and hence define an isometric *-automorphism on the dense local union, which then extends uniquely (with its inverse) to the C*-completion. Please persist that argument, or an equivalent correct construction of `alpha`, while keeping the finite-support claims in (8)--(13) explicitly restricted to local coefficients. This would resolve the objection without changing the mathematical identity of the finding.

## Owner

The objection to the sentence "every quasi-local observable has finite support" is correct; that sentence is not needed for the claim. The product automorphism exists by the inductive-limit extension argument suggested in the review.

For each finite `F`, let `alpha_F = \bigotimes_{p\in F} alpha_p` on `A_F`. If `F \subset F'`, the canonical inclusion is `i_{F,F'}(a)=a\otimes 1`, and because every local automorphism is unital,

\[
alpha_{F'}(i_{F,F'}(a))=alpha_F(a)\otimes 1=i_{F,F'}(alpha_F(a)).
\]

Hence the `alpha_F` are compatible and define a well-defined *-automorphism `alpha_0` on the algebraic local union `A_loc=\bigcup_F A_F`. Each `alpha_F` is isometric, so `alpha_0` is isometric and extends uniquely by continuity to an isometric *-endomorphism `alpha` of the norm completion `A`. Applying the same construction to `alpha_F^{-1}` gives an isometric extension `beta`; on the dense local union `beta alpha=alpha beta=id`, and therefore by continuity the same identities hold on all of `A`. Thus `alpha` is a C*-automorphism independently of whether it is spatial in the spherical representation.

The finite-support statements used later should indeed be read only for local coefficients: if `a\in A_S`, then `alpha(A_S)=A_S`, giving (8)--(10); and if every Fourier coefficient `a_n\in A_S`, then (11)--(13) remain in `A_S`. General quasi-local elements may have no finite support, exactly as Section 5 already states. This repairs the setup without changing the mathematical claim; if accepted, the canonical finding should replace the erroneous sentence by this extension argument.

## Adversary

The objection is mathematically resolved. The compatibility identity for the local tensor automorphisms gives a well-defined isometric *-automorphism on the dense local union, and the inverse family supplies the inverse after extension to the C*-completion. This is the missing construction of `alpha`; it also correctly separates the later finite-support claims, which apply only to local coefficients, from general quasi-local elements.

Closure is pending durable persistence: the canonical finding still contains the false sentence that every quasi-local observable has finite support and does not yet contain the extension argument. Please replace that sentence by the compatible-local-automorphism extension proof (or an equivalent correct construction) while retaining the explicit local-coefficient scope of (8)--(13), then leave the sidecar for final verification.

## Owner

The accepted construction is now persisted in the canonical target: compatible local tensor automorphisms define the isometric automorphism on the dense local union and extend, together with the inverse family, to the C*-completion. The finite-support statements are restricted to local coefficients, while general quasi-local elements are explicitly left outside that support claim.