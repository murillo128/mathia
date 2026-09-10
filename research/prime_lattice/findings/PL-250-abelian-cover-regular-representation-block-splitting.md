# PL-250 — Keeping the full abelian class-field cover still splits off zeta as an invariant character block

## Claim

`PL-249` established a canonical source-derived relation among rational-prime rows: for a finite abelian extension `L/Q`, the Connes–Consani class-field cover labels every unramified prime orbit by `Frob_p in G = Gal(L/Q)`, and the exponent vector carries the exact quotient

`v(n) -> product_p Frob_p^(v_p(n))`.

The obvious escape from the principal-character collapse is to avoid projecting to the trivial character and instead retain the full cover, for example through the regular representation `C[G]`, an equivariant trace, or an Artin determinant. That escape does **not** work inside the standard linear `G`-equivariant/Artin formalism. For finite abelian `G`, finite Fourier transform decomposes the regular representation canonically as

`C[G] = direct_sum_(chi in G^) C_chi`.

The trivial character is therefore an invariant direct summand before any scalar projection is chosen. Any operator commuting with the regular `G`-action is block diagonal in this character decomposition; because every character occurs with multiplicity one, each block is scalar. Traces add and determinants multiply across those blocks. In particular, the Artin `L`-function of the regular representation factors as

`L(s, rho_reg) = product_(chi in G^) L(s,chi) = zeta_L(s)`,

while the trivial block is exactly

`L(s,1_G) = zeta_Q(s) = zeta(s)`.

Thus retaining the entire finite abelian cover does preserve Frobenius data in the **other** character blocks, and the full determinant can depend on that data, but it does not feed those blocks into the principal Riemann channel. The ordinary zeta factor remains a canonical direct factor. A genuinely new mechanism would have to leave this linear equivariant block decomposition — for example through a source-forced nonlinear invariant or a canonical non-equivariant coupling — and then prove that the resulting coupling constrains the principal zeta divisor rather than merely the surrounding Artin family.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION + PRIOR-ART-REDIRECT + NO-NOVELTY-CLAIM`. Regular-representation decomposition, Artin formalism, and the factorization of Dedekind zeta into character `L`-functions are classical. The durable delta is the matched-control consequence for the current `prime_lattice` frontier: **keeping all character channels does not repair `PL-249` as long as the proposed operator/trace/determinant remains linear and `G`-equivariant.**

## Exact finite-group block decomposition

Let `G` be a finite abelian group and let `lambda(g)` denote its left regular representation on `V=C[G]`. Finite-group Fourier transform gives

`V ~= direct_sum_(chi in G^) C_chi`,

with

`lambda(g)|_(C_chi) = chi(g)`.

Equivalently, the trivial-character projector is the canonical central idempotent

`e_1 = |G|^(-1) sum_(g in G) lambda(g)`.

Hence `C_1 = e_1 V` is an invariant line determined by the group action itself, not by an arbitrary later choice of basis.

Now let `T` be any linear operator on `V` satisfying

`T lambda(g) = lambda(g) T` for every `g in G`.

Since the character spaces are pairwise inequivalent one-dimensional irreducibles, Schur/Fourier diagonalization gives

`T = direct_sum_(chi in G^) t_chi`.

Therefore

`Tr(T) = sum_chi t_chi`

and, for every scalar parameter for which the expression is defined,

`det(I-T) = product_chi (1-t_chi)`.

There is no off-diagonal transfer from a nontrivial character into the trivial line while `G`-equivariance is retained. This is a finite-dimensional algebraic statement and does not depend on Euler products, convergence, or analytic continuation.

For the exponent lattice, the source-derived class-field quotient from `PL-249` sends an unramified integer

`n = product_p p^(v_p(n))`

to

`Art_L(n) = product_p Frob_p^(v_p(n)) in G`.

Applying the regular representation and then finite Fourier transform yields simultaneously

`rho_reg(Art_L(n))  <->  ( chi(Art_L(n)) )_(chi in G^)`

with

`chi(Art_L(n)) = product_p chi(Frob_p)^(v_p(n))`.

Thus the full cover indeed retains a family of prime-exponent phase fingerprints, but it retains them as **separate character channels**. The principal channel is the component `chi=1`, for which every fingerprint equals `1`.

## Artin determinant and the Dedekind-zeta matched control

At an unramified prime `p`, the local factor attached to the regular representation is

`L_p(s,rho_reg) = det(I-rho_reg(Frob_p)p^(-s))^(-1)`.

Fourier diagonalization gives the exact local factorization

`L_p(s,rho_reg) = product_(chi in G^) (1-chi(Frob_p)p^(-s))^(-1)`.

The `chi=1` eigenline contributes exactly `(1-p^(-s))^(-1)`. All dependence on the nontrivial Frobenius class lies in the remaining factors.

Globally, Artin formalism is multiplicative on direct sums. Since the regular representation is `Ind_{1}^{G}(1)`, induction compatibility gives

`L(s,rho_reg) = zeta_L(s)`.

For abelian `G`, decomposing `rho_reg` into its one-dimensional characters therefore yields the classical factorization

`zeta_L(s) = zeta(s) product_(chi != 1) L(s,chi)`.

This is a particularly strong adversarial control because it tests exactly the proposal “do not throw away the cover; take the determinant of all of it.” The result is richer than zeta, but its richness is a product of neighboring character channels. The principal Riemann factor is still split off rather than altered by them.

The same conclusion applies to any construction whose only interaction with the finite cover is through linear `G`-equivariant functional calculus on `C[G]`: central/convolution operators, their traces, ordinary finite-dimensional determinants, and direct-sum Artin `L`-functions all respect the character blocks. Calling the aggregate object “global” does not by itself create cross-character dynamics.

## Analytic-continuation control

The local Euler factors and their infinite product are used only in their absolute-convergence region. For the one-dimensional characters of a finite abelian extension of `Q`, the associated Artin `L`-functions are Hecke/Dirichlet `L`-functions with their standard analytic continuation; the trivial character has the simple pole inherited from `zeta(s)`.

The identity

`zeta_L(s) = product_(chi in G^) L(s,chi)`

is first obtained in the common Euler-product half-plane and then extends by uniqueness of meromorphic continuation. Nothing here formally continues a primewise determinant through the critical strip. More importantly, the direct-sum decomposition of `C[G]` is algebraic and already separates the trivial block before continuation. Meromorphic continuation of the global product does not re-couple character blocks that were linearly independent at the representation-theoretic level.

## Adversarial controls

**The full determinant is not trivial.** For a nonidentity `Frob_p`, the product over all characters depends on its order, so the regular-representation determinant genuinely retains class-field information. The negative claim is narrower: that information occurs outside, or multiplicatively alongside, the trivial block and therefore supplies no automatic principal-zeta constraint.

**A factorization can still participate in a deeper global theorem.** It is logically possible that a source-derived positivity, duality, or trace relation for the *whole* cover forces correlated statements about all factors and thereby constrains `zeta(s)`. No such implication follows from regular-representation decomposition or Artin formalism alone, and none was located in this audit. Any future proposal must exhibit that additional theorem explicitly; merely replacing `zeta` by `zeta_L` or the regular determinant is not sufficient.

**Arbitrary cross-character mixing is not an escape.** One can of course write a matrix that mixes the Fourier blocks, but then it fails to commute with the canonical `G`-action. Under the line mandate such a choice is programmable unless an independent arithmetic/geometric source forces it. The surviving question is therefore not whether a coupling matrix can be invented, but whether the cover supplies a canonical non-equivariant or nonlinear coupling whose principal-channel consequence survives the generic/Helson/Beurling controls.

**The claim is abelian and linear.** Nonabelian covers replace characters by higher-dimensional irreducibles and the regular representation contains them with multiplicity, but the general Artin direct-sum philosophy still suggests a related decomposition. This finding does not use that extension and does not claim that every nonlinear invariant of a nonabelian cover is inert.

## Prior-art and novelty audit

Primary/classical anchors:

- Jürgen Neukirch, *Algebraic Number Theory*, Springer, 1999, Chapter VII, “Zeta Functions and L-series,” especially the Artin `L`-series discussion. The chapter defines the regular representation, its irreducible-character decomposition, the trivial representation, and Artin `L`-series formalism.
- J. S. Milne, *Class Field Theory*, version 4.03, 6 August 2020, Chapter VI, “L-series and the Density of Primes,” https://www.jmilne.org/math/CourseNotes/cft.html. Used for the abelian Artin/Weber `L`-series and class-field-theoretic analytic background.
- Alain Connes and Caterina Consani, “Knots, primes and class field theory,” arXiv:2501.06560 (2025), https://arxiv.org/abs/2501.06560. Source of the finite abelian adelic cover and Frobenius monodromy already audited in `PL-249`.

An internal audit before publication found no existing `PL-250` and no stored `prime_lattice` finding centered on the regular representation, Dedekind-zeta factorization, or the claim that full equivariant cover retention still canonically splits off the principal zeta block. `PL-249` is the immediate dependency but proves only the scalar trivial-character collapse; the present finding closes its most direct linear escape. No novelty is claimed for any representation-theoretic or Artin theorem.

## Research implication

The source/global-selector requirement isolated in `PL-249` must now be strengthened to a **non-block-diagonal survival test**. A proposed class-field/cover mechanism does not pass merely because the full object remembers all Frobenius classes. If its canonical linearization decomposes into Artin character blocks and `zeta(s)` occupies the trivial block, then the extra arithmetic information has not yet reached the target divisor.

The next viable construction must therefore provide a source-forced operation that does not reduce to characterwise scalar functional calculus: for example a genuinely nonlinear invariant of the cover, a canonical target-relative compression, or a positivity/duality theorem that couples the blocks and has a demonstrable implication for the trivial factor. It must also explain why that coupling is arithmetic rather than programmable and why it survives analytic continuation in the principal Riemann channel.