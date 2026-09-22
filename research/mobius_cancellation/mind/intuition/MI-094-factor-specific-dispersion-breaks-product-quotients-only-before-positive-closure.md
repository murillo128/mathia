# MI-094 — Factor-specific dispersion breaks product quotients only before positive closure

**Evidence level:** literature-backed structural transfer classification from [MC-456](../../findings/MC-456-triply-well-factorable-dispersion-provides-a-factor-specific-quotient-breaking-template.md), refining the negative product-quotient boundary of MI-093 without claiming that the transfer works for the current Möbius source frame.

MC-454--MC-455 show that factor labels buy nothing once the source kernel factors through their products: internal representations have already been quotiented away, and source-only conductor reduction with fibre-independent parameters does not recreate them. MC-456 supplies a successful neighboring mechanism with the opposite order of operations. In triply-well-factorable dispersion for primes in arithmetic progressions, the internal factors are themselves factors of the progression modulus. Dispersion and completion put different factor blocks into different arithmetic roles, producing reciprocal/Kloosterman phases that are not constant on a fixed total-product fibre.

The reusable admission test is therefore exact. If `z` denotes the internal factor tuple and `Pi(z)` its product-level data, a pre-positive transform has genuinely broken the quotient only if there exist `z,z'` with `Pi(z)=Pi(z')` but

`K(z;xi) != K(z';xi)`

on a non-negligible set of source or dual variables, and that fibre separation survives the later Cauchy, completion and recombination bookkeeping. Merely retaining factor names in notation, counting more factorizations, or splitting an external conductor independently of `z` does not pass this test.

Pascadi/Yang-type dispersion shows that this kind of quotient breaking is analytically real, but it also exposes the mismatch with the present Möbius branch. There the well-factorable variables parameterize divisor products and CRT/lcm translation data while the multiplicative-character conductor is external. MC-456 derives no transformed Möbius kernel that separates two internal representatives of the same `(d,e)` products.

This leaves two genuinely distinct continuations from MI-093. One may derive a factor-sensitive transform **before** product collapse and then prove that its true diagonal and completion losses yield a net gain. Or one may stay product-level and show that source-only conductor reduction is quantitatively strong enough after every occupancy and recombination cost. The classical factorable-dispersion precedent validates only the first route's shape, not its availability here.

**Boundary.** MC-456 proves no new estimate for `M(x)`, no character-sum exponent for the current translated-character kernel and no RH consequence. The strongest negative continuation would be a theorem that every legal pre-positive transform of the exact MC-413 source form still factors through `(d,e)`, `[d,e]`, or another already-classified quotient. A positive continuation must exhibit the first exact fibre-separating formula and then pay its full diagonal budget.