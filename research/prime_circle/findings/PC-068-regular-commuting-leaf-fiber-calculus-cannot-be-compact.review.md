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
