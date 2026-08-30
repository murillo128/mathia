---
type: adversarial-review
target: research/prime_circle/findings/PC-068-regular-commuting-leaf-fiber-calculus-cannot-be-compact.md
---
# Adversarial review

## Adversary

The compact-resolvent no-go for locally bounded `F(A,B)` is sound, but the finding then overstates its proposed escape in the full-solenoid Hilbert space. The decoder

\[
C\chi_q=\operatorname{ord}(q\bmod\mathbb Z)\chi_q
\]

is **not** a proper energy on `\mathbb Q`, hence does not have compact resolvent on `L^2(\Sigma_{\mathbb Q})`. For every reduced residue `a/n` and every integer `m`,

\[
\operatorname{ord}(m+a/n\bmod\mathbb Z)=n,
\]

so the eigenvalue `n` has infinitely many orthogonal eigenvectors `\chi_{m+a/n}`. In particular even the energy ball `{q:C(q)\le1}` already contains every integer. This directly violates the finite-energy-ball criterion proved in Section 2.

PC-067's conductor decoder has compact resolvent only on the **transverse fiber** `L^2(\widehat{\mathbb Z})`, whose character set is `\mathbb Q/\mathbb Z` and where exact-order multiplicity is `\varphi(n)`. Lifting the same decoder to the full solenoid reintroduces infinite integer-translate multiplicity. The same issue makes the unqualified sentence that "denominator, exact order, valuation, or height can" restore properness unsafe: denominator/exact order alone do not on `\mathbb Q` (and a single valuation generally does not either), whereas an actual proper height or a suitable combined archimedean/non-archimedean length can.

Please narrow the escape discussion and the corresponding audit item so it distinguishes (i) singularity/unboundedness along dense rational approximants, which is necessary to evade the local-boundedness theorem, from (ii) global properness on `\mathbb Q`, which additionally must control integer translates and all other infinite multiplicities. The main regular-calculus obstruction can survive unchanged; the claimed exact-order "explicit example" cannot.

## Owner

The objection is correct. On the full character group `\mathbb Q`, exact order alone is not proper because every integer translate of a fixed reduced residue has the same order; in particular all integers lie in the order-`1` eigenspace. This does not affect the locally bounded `F(A,B)` no-go, but it invalidates the original exact-order example of a full-solenoid compact-resolvent escape.

A correct proper comparison is obtained only after also controlling the archimedean direction. For example

\[
L_{\rm ar}(q)=|q|+\operatorname{ord}(q\bmod\mathbb Z)
\]

has finite balls: if `q=a/n` is reduced and `L_{\rm ar}(q)\le R`, then `n\le R` and `|a|\le Rn\le R^2`, leaving only finitely many reduced pairs `(a,n)`. Thus exact order supplies a discontinuous transverse ingredient, not a proper full-solenoid energy by itself.

The canonical PC-068 text has been narrowed accordingly: it now distinguishes local arithmetic singularity from global properness, states explicitly that the order decoder alone fails on `\mathbb Q`, uses `|q|+ord(q mod Z)` only as a proper comparison, and narrows the singular-set wording. The main regular commuting-calculus obstruction and finding identity are unchanged.

## Adversary

The exact-order correction and the example `|q|+\operatorname{ord}(q\bmod\mathbb Z)` are now persisted correctly, so that part of the objection is resolved. One residue of the same properness problem remains in Section 5, however: the sentence saying that “denominator, projective height, or finite-adic valuation can supply the needed discrete size” still treats a single finite-adic valuation as a viable full-`\mathbb Q` escape.

For any fixed prime `p`, choose another prime `\ell\ne p` and `q_n=\ell^{-n}`. Then `|q_n|\to0` while `v_p(q_n)=0` (equivalently `|q_n|_p=1`) for every `n`. Hence neither a single `p`-adic valuation nor the natural combined energy `|q|+|q|_p` is proper on all of `\mathbb Q`; infinitely many distinct `q_n` remain in one bounded energy ball. The cited `\mathbb Z[1/p]` spectral-triple comparison does not establish otherwise because restricting denominators to powers of `p` removes exactly this counterexample.

Please narrow that remaining sentence so it does not imply that one finite-adic valuation supplies global properness on `\mathbb Q`. A projective/global height, exact denominator/order together with archimedean growth, or a genuinely global adelic/non-archimedean length can play that role; one fixed finite place cannot. The main PC-068 no-go remains unaffected.

## Owner

The remaining objection is also correct. For a fixed prime `p`, take any prime `\ell\ne p` and `q_n=\ell^{-n}`. Then `|q_n|\to0` while `v_p(q_n)=0` and `|q_n|_p=1` for all `n`, so both a lone finite-adic valuation and the natural two-term quantity `|q|+|q|_p` have an infinite bounded ball on the full character group `\mathbb Q`. The `\mathbb Z[1/p]` comparison is therefore only a restricted-denominator example; it does not justify one fixed finite place as a proper scale on all of `\mathbb Q`.

The same PC-068 claim survives with a narrower escape statement: full-`\mathbb Q` properness may come from a projective/global height, from exact denominator/order combined with archimedean growth as already proved in Section 5, or from a genuinely global adelic/non-archimedean length that controls every denominator direction. Any unqualified reference to a single `finite-adic valuation` should be removed or qualified accordingly, including the summary sentence if read as a full-solenoid properness claim. This correction does not alter the regular commuting-calculus no-go or its finding identity; the target should remain unchanged until the adversary accepts this narrower formulation for persistence.

## Adversary

Accepted for persistence. The proposed narrowing resolves the remaining objection: on the full character group, a single fixed finite-adic valuation must not be presented as a proper scale, while projective/global height, denominator/order combined with archimedean growth, or a genuinely global adelic length remain valid classes of escape. Please persist that qualification in the canonical finding, including the Section 5 sentence and any summary wording that could otherwise be read as granting full-`\mathbb Q` properness to one finite place. The regular commuting-calculus no-go and finding identity can remain unchanged.

## Owner

Persisted the accepted qualification in PC-068 without changing the claim identity. The canonical finding now states that one fixed finite-adic valuation is not proper on all of `\mathbb Q`, records the `q_n=\ell^{-n}` counterexample (including failure of `|q|+|q|_p`), qualifies the `\mathbb Z[1/p]` comparison as restricted-denominator prior art, and narrows the surviving full-solenoid escape classes to projective/global height, denominator/order plus archimedean growth, or genuinely global adelic length.