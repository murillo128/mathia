# VIS-377 — bounded finite rational operator calculus inherits Gram noncommutativity

## Claim

Let `A_W` be a finite-dimensional Wang coefficient map with source-free Gram

`G=A_W^*A_W>=0`.

Let `H_1,...,H_r` be externally supplied bounded operators on the coefficient space. Consider any fixed finite noncommutative `*`-rational expression `E(H_1,...,H_r)` built from scalar multiples of the identity, the generators, addition, multiplication, adjoint, and inversion of intermediate operators at points where those inverses exist.

For every evaluated subexpression `X`, define its operator-size `N(X)=||X||_op`. Define recursively an orientation budget `Q_G(X)` by

`Q_G(cI)=0`,

`Q_G(H_j)=||[G,H_j]||_F`,

`Q_G(aX+bY)=|a|Q_G(X)+|b|Q_G(Y)`,

`Q_G(XY)=Q_G(X)N(Y)+N(X)Q_G(Y)`,

`Q_G(X^*)=Q_G(X)`,

and, whenever `X` is invertible,

`Q_G(X^(-1))=N(X^(-1))^2 Q_G(X)`.

Then every defined subexpression satisfies

`||[G,X]||_F <= Q_G(X)`.

In particular,

`||[G,E(H)]||_F <= Q_G(E(H))`.

If every generator commutes with `G`, then every defined finite `*`-rational expression in those generators also commutes with `G` exactly. More generally, for a family indexed by a parameter `T`, if the expression tree is fixed, all evaluated intermediate operator norms and inverse norms remain uniformly bounded, and

`epsilon_T=max_j ||[G_T,H_(j,T)]||_F -> 0`,

then

`||[G_T,E(H_T)]||_F = O_E(epsilon_T)`.

Thus a fixed bounded finite rational constructor cannot manufacture order-one Wang-Gram orientation from vanishing generator-level orientation. Any such amplification must be paid by at least one explicit resource: growing expression complexity, growing intermediate operator norms, or a near-singular inversion with diverging inverse norm.

The inversion tax is exact at the derivation level:

`[G,X^(-1)] = -X^(-1)[G,X]X^(-1)`.

Hence a single inverse can amplify a commutator by at most `||X^(-1)||_op^2`. A pole or nearly singular denominator is therefore not free geometry; its conditioning is the orientation-amplification budget.

If the final value

`C=E(H_1,...,H_r)`

is a positive Hermitian metric with

`mI<=C<=MI`,

then the cluster control of `VIS-374` applies. For any Wang-Gram clustering with within-cluster radius `eta` and resolved inter-cluster separation `gamma>0`, there exists a positive metric `C_*` commuting with `G`, with `mI<=C_*<=MI`, such that

`|s_k(A_W C^(1/2))^2-s_k(A_W C_*^(1/2))^2|`
` <= ||G||_op sqrt(M/m) Q_G(C)/gamma + 2M eta`.

Therefore bounded finite rational operator calculus remains inside the same resolved-orientation accounting as `VIS-373`--`VIS-376`. The genuinely new escape is not “use inverses” or “use a rational formula”; it is to drive a denominator toward singularity, let rational complexity grow, introduce generator-level orientation already at the source, or leave the bounded finite-dimensional positive-Hilbert setting.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL DERIVATION/INVERSE IDENTITY + STRUCTURAL NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

No estimate for the normalized Chebyshev-theta remainder, prime-number-theorem remainder, zeta zeros, or RH is proved here.

## 1. Why rational assembly is the next finite-calculus loophole

`VIS-375` shows that scalar spectral reweighting of one external Hermitian operator inherits its Gram noncommutativity. `VIS-376` extends this to finite noncommutative polynomials in several external generators. The immediate remaining finite-algebraic loophole is inversion: resolvents, Schur-complement-like expressions, transfer functions, or rational filters can become large even when polynomial combinations remain tame.

That difference is real, but it is a conditioning effect rather than free orientation. The inverse rule below isolates the exact price. Once every denominator stays uniformly separated from singularity, finite rational calculus preserves the smallness class of generator commutators just as finite polynomial calculus does.

This result remains entirely on the source-blind coefficient layer. The generators may be physically meaningful external operators, but no arithmetic source value is used in the derivation.

## 2. Inner derivations propagate through inversion

For the Wang Gram define

`delta_G(X)=[G,X]`.

As used in `VIS-376`, `delta_G` obeys the Leibniz rule

`delta_G(XY)=delta_G(X)Y+X delta_G(Y)`.

If `X` is invertible, apply the derivation to

`XX^(-1)=I`.

Since `delta_G(I)=0`,

`delta_G(X)X^(-1)+X delta_G(X^(-1))=0`.

Multiplying on the left by `X^(-1)` gives the exact inverse identity

`delta_G(X^(-1))=-X^(-1)delta_G(X)X^(-1)`.

Therefore

`||delta_G(X^(-1))||_F`
` <= ||X^(-1)||_op^2 ||delta_G(X)||_F`.

Adjoint introduces no new cost because `G=G^*` and

`[G,X^*]=-[G,X]^*`,

so the Frobenius norms are equal.

Together with the triangle inequality and

`||AXB||_F<=||A||_op||X||_F||B||_op`,

these identities prove the recursive budget in the claim by structural induction over the rational expression tree.

## 3. Uniformly regular rational calculus cannot create an orientation scale

Fix one rational expression tree `E`. Suppose along a family indexed by `T` that every intermediate node `X_T` satisfies a uniform bound

`||X_T||_op<=R_X`,

and every inverted node satisfies

`||X_T^(-1)||_op<=K_X`,

with constants depending on the fixed node but not on `T`.

The recursive rules then turn `Q_G(E(H_T))` into a finite linear combination of the generator commutators with coefficients depending only on the fixed expression and the uniform `R_X,K_X` bounds. Consequently

`Q_G(E(H_T)) <= C_E max_j ||[G_T,H_(j,T)]||_F`

for one finite constant `C_E`.

Hence vanishing generator orientation implies vanishing output orientation. A finite rational expression can look substantially more complicated than its generators and may mix them noncommutatively, but under uniform regularity it does not create a new asymptotic commutator scale.

The contrapositive identifies the only finite-rational amplification mechanisms. If generator commutators are `o(1)` while the rational output has order-one Gram commutator, then at least one assumption used to obtain a uniform `C_E` must fail: expression complexity grows, an intermediate operator norm grows, or an inverted intermediate approaches singularity so that its inverse norm diverges.

## 4. The near-pole regime is an explicit conditioning resource

For one inverse node, the amplification factor is at most

`||X^(-1)||_op^2 = sigma_min(X)^(-2)`.

Thus a denominator with smallest singular value `rho` can amplify an inherited commutator by at most `rho^(-2)` before later product factors are charged. If `rho` tends to zero, this can indeed be large. The present finding does not rule that mechanism out; it classifies it as near-singular conditioning.

This matters for resolvent-type proposals. For a Hermitian generator `H` and spectral parameter `z` outside `spec(H)`, take

`X=zI-H`.

Then

`||(zI-H)^(-1)||_op = dist(z,spec(H))^(-1)`,

so

`||[G,(zI-H)^(-1)]||_F`
` <= dist(z,spec(H))^(-2) ||[G,H]||_F`.

A resolvent can therefore magnify pre-existing orientation when `z` approaches the spectrum, but the gain is exactly accompanied by the familiar squared resolvent-conditioning factor. Staying a fixed spectral distance away gives no new asymptotic orientation class.

## 5. Composition with Wang spectral control

Assume the rationally constructed output `C` is positive with `mI<=C<=MI`. `VIS-374` provides an exactly Gram-commuting positive control `C_*` satisfying

`|s_k(A_W C^(1/2))^2-s_k(A_W C_*^(1/2))^2|`
` <= ||G||_op sqrt(M/m) ||[G,C]||_F/gamma + 2M eta`.

Substituting the rational orientation budget yields

`|s_k(A_W C^(1/2))^2-s_k(A_W C_*^(1/2))^2|`
` <= ||G||_op sqrt(M/m) Q_G(C)/gamma + 2M eta`.

The accounting is now explicit. Generator commutators supply inherited orientation; products and sums propagate it; inverses multiply it by conditioning factors; Gram gaps and cluster widths determine how much of that orientation can alter the destination squared singular spectrum; and `m,M` charge positive-metric degeneration.

No finite rational notation hides these resources.

## 6. Prior-art audit

The algebraic ingredients are classical. For fixed `G`, the commutator map `delta_G(X)=[G,X]` is an inner derivation; derivations satisfy the Leibniz rule, and applying that rule to `XX^(-1)=I` gives the standard inverse identity `delta(X^(-1))=-X^(-1)delta(X)X^(-1)`. Kadison and Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I: Elementary Theory*, Academic Press (1983; AMS reprint 1997), is a standard operator-algebra reference for inner derivations and their algebraic framework.

Noncommutative rational functions and matrix evaluations of rational expressions are themselves established objects. Igor Klep, James Eldred Pascoe, and Jurij Volčič, **Regular and positive noncommutative rational functions**, *Journal of the London Mathematical Society* 95 (2017), 613--632, DOI `10.1112/jlms.12030`, studies regular and positive noncommutative rational functions through linear-system realizations. Jurij Volčič, **Matrix coefficient realization theory of noncommutative rational functions**, *Journal of Algebra* 499 (2018), 397--437, DOI `10.1016/j.jalgebra.2017.12.009`, develops realization theory for matrix evaluations of noncommutative rational functions.

No novelty is claimed for rational expressions, resolvents, the inverse derivation rule, noncommutative rational-function theory, or the elementary norm estimates above. The Mathia-specific contribution is the Wang control boundary after `VIS-373`--`VIS-376`: finite rational assembly does not evade generator-level Gram-orientation accounting unless its conditioning or complexity itself becomes a diverging resource.

A repository-level duplication check found earlier resolvent findings, including the unrelated source-smoothing Green-resolvent identity `VIS-292`, but no existing Visual Exploration finding that classifies finite noncommutative rational assembly of external Wang operators by generator commutators and inverse-conditioning cost.

## Dependencies

- `VIS-369`: freely aligned degenerating positive metrics can prescribe active singular spectra and are non-identifying unless their metric cost is justified.
- `VIS-370`: exactly Gram-commuting positive metrics are sectorwise spectral filters/preconditioners.
- `VIS-371`: coordinate-free positive metric rules built only from one Gram are forced into the commuting class.
- `VIS-373`: resolved-gap orientation is controlled by gap-normalized Gram commutator size.
- `VIS-374`: orientation confined to narrow near-degenerate Gram clusters is spectrally cheap.
- `VIS-375`: scalar functional calculus of one external Hermitian generator inherits its Gram noncommutativity.
- `VIS-376`: finite noncommutative polynomial assembly inherits generator-level Gram noncommutativity with an explicit algebraic complexity budget.
- `CLUE-wang-fixed-source-packet-localization`: accepted Wang clue further narrowed by the present rational-calculus control.

## Research consequence

The remaining finite-calculus loophole is no longer “try a rational filter” in the abstract. A rational Wang metric or transfer operator must expose its full regularity ledger: which external generators are justified independently, their Gram commutators, every denominator that is inverted, the smallest singular value or inverse norm of those denominators, expression complexity, and the final positive-metric bounds if the construction returns to Hilbert geometry.

If all of those resources remain uniformly bounded while the generator commutators vanish, the rational output remains asymptotically Gram-commuting and `VIS-374` reduces it to commuting preconditioning up to the explicit cluster error.

A genuinely different route must therefore use a near-pole/singular limit and pay its conditioning cost, let rational complexity grow, introduce substantial orientation already in a source-native generator, use a genuinely infinite-dimensional/unbounded limit whose domain and convergence are controlled, or leave positive-Hilbert metric geometry altogether.