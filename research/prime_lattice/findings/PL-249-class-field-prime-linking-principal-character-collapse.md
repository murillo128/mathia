# PL-249 — Class-field prime linking is canonical global row data, but the principal zeta character kills its monodromy

## Claim

The live frontier after `PL-240`–`PL-248` asks for a source-derived relation among distinct rational-prime rows, a canonical global selector, and survival of that relation in the same principal channel that carries the ordinary Riemann zeta divisor. Adelic/class-field geometry supplies a particularly strong matched control for the first two requirements, but its standard linear readout fails the third.

Connes and Consani construct an adelic space `X_Q` whose rational-prime places are periodic scaling orbits `C_p` of length `log p`. For every finite abelian extension `L/Q` they construct a canonical finite abelian cover of `X_Q`; at every unramified rational prime `p`, the monodromy of `C_p` in that cover is precisely the arithmetic Frobenius `Frob_p in Gal(L/Q)`. Thus the prime rows are not being coupled by an invented kernel or a chosen graph: a single global class-field object canonically assigns their monodromies.

For integers prime to the ramification conductor, Artin reciprocity extends these prime labels multiplicatively,

`Frob(n) = product_p Frob_p^(v_p(n))`.

This is an exact finite-quotient representation of the positive exponent lattice. Its additive energy remains

`log n = sum_p v_p(n) log p`,

while the same vector carries a global monodromy coordinate in `Gal(L/Q)`. Deninger's arithmetic dynamical systems independently realize the same logarithmic arithmetic scale: closed points have periodic-orbit length `log N(x)`, and the positive integer monoid acts by commuting Frobenius maps. For `Spec Z`, the primitive orbit lengths are `log p`; unique factorization therefore recovers the same prime-generator bookkeeping. Morishita's comparison of Deninger systems with Connes–Consani adelic spaces confirms that these are neighboring realizations of the same arithmetic-dynamical dictionary rather than an arbitrary juxtaposition.

However, the standard character decomposition that turns abelian monodromy into scalar `L`-data erases this information exactly in the principal Riemann channel. For a one-dimensional character `chi` of `Gal(L/Q)`, the unramified local Artin factor is

`L_p(s,chi) = (1 - chi(Frob_p) p^(-s))^(-1)`.

For the trivial character `chi=1`, every Frobenius label is sent to `1`, so

`L_p(s,1) = (1-p^(-s))^(-1)`

and globally

`L(s,1) = zeta_Q(s)`.

Thus the same projection that extracts the principal Riemann zeta factor annihilates all nontrivial abelian-cover monodromy. The finite cover still exists geometrically, but its Frobenius/linking labels are invisible to the scalar trivial-character channel. In the precise sense relevant to the current frontier, class-field geometry satisfies the source/global-selection gate but **does not make that structure survive ordinary character-linear extraction of `zeta(s)`**.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART-REDIRECT + NEGATIVE-BOUNDARY + NO-NOVELTY-CLAIM`. The adelic periodic-orbit cover, its Frobenius monodromy, Deninger's logarithmic orbit lengths and Frobenius actions, and Artin local factors are prior art. The exponent-lattice formula for `Frob(n)` is the direct multiplicative extension of the prime Artin map. The durable research delta is the matched-control consequence for the `prime_lattice` frontier: even a canonical number-field geometry that genuinely carries global Frobenius data can lose that data under the exact principal projection producing Riemann zeta.

## Source-derived global prime geometry

Connes–Consani's construction is unusually well matched to the geometric language of this line. Their `X_Q` has a periodic orbit `C_p` for each rational prime, with orbit length `log p`; the archimedean place is represented separately. Their Theorem 1 / Theorem 3.12 associates finite abelian extensions `L/Q` contravariantly with finite abelian covers and proves that, for an unramified prime `p`, the monodromy around `C_p` is the arithmetic Frobenius `Frob_p`. The connected components above `C_p` are labeled by the places of `L` above `p`.

This gives more than the bare Bohr frequencies. The prime coordinate `e_p` now carries both a geometric primitive period `log p` and a canonical monodromy element in one global cover. For an unramified positive integer

`n = product_p p^(v_p(n))`,

abelianity and the Artin map give the monodromy product

`Art_L(n) = product_p Frob_p^(v_p(n))`.

Accordingly the exponent lattice has a source-derived quotient

`N_0^(P_unram) -> Gal(L/Q),  v -> product_p Frob_p^(v_p)`.

This quotient is not a claim that the abstract monoid `N_0^(P)` itself contains class-field information. The extra structure is supplied by the number-field cover. That distinction matters: it passes the mandate's anti-reencoding gate because the labels are forced by arithmetic geometry, not assigned to prime axes after the fact.

Deninger's construction supplies a complementary control. For a normal arithmetic scheme of finite type, closed points correspond to compact packets of periodic orbits of length `log N(x)`, and the construction carries commuting Frobenius maps indexed by the multiplicative monoid of positive integers. The relation to exponent vectors is therefore exact at the semigroup level: `n=product p^(v_p(n))` composes the prime Frobenius generators with the same exponents, while logarithmic time adds to `log n`. This validates the arithmetic-dynamical interpretation of the prime-lattice energy independently of the Bohr transform.

## Why the principal character removes the monodromy

For a finite-dimensional Artin representation `rho`, the local Euler factor is defined from the action of Frobenius on the inertia invariants. In the one-dimensional unramified abelian case this reduces to

`det(1-rho(Frob_p)p^(-s))^(-1) = (1-chi(Frob_p)p^(-s))^(-1)`.

The trivial representation sends every group element to `1`. Hence at every prime, including the ramified primes because the trivial representation has full inertia invariants, the local factor is exactly `(1-p^(-s))^(-1)`. Therefore the Artin `L`-function of the trivial representation of `Gal(L/Q)` is the zeta function of the base field `Q`, namely Riemann zeta.

The collapse is consequently algebraic, before any difficult analysis:

`Frob_p -> chi(Frob_p) -> 1` when `chi=1`.

No relation among the nontrivial Frobenius classes can be recovered from this scalar readout, because all such classes have the same image. Passing from the collection of monodromies to the ordinary principal Euler factor forgets the cover data rather than turning it into a sign, positivity condition, spectral phase, or zero-localizing constraint.

This is the class-field analogue of the principal-channel collapses in `PL-240`–`PL-248`, but it is an independent geometric control. Those findings reached the obstruction through reciprocity matrices, multiple Dirichlet series, residues, and Kac–Moody local/global decomposition. Here the coupling/selector is supplied directly by a finite adelic cover and its monodromy, yet ordinary scalar character extraction still diagonalizes it away.

## Analytic-continuation control

The local Euler-product statement is initially an identity in the absolute-convergence half-plane. Nothing in this finding formally transports the product `product_p (1-p^(-s))^(-1)` through the critical strip.

The relevant global statement is instead the standard identity of Artin `L`-functions

`L(s,1_G) = zeta_Q(s)`.

It is first identified where the Euler products converge and then both sides have their usual meromorphic continuation. Continuing the resulting scalar function does not restore the discarded values `Frob_p`: the loss occurred when applying the trivial representation, not when taking an Euler product. Thus the negative survives analytic continuation in exactly the limited sense claimed here: the meromorphically continued principal scalar channel is still `zeta(s)`, while the nontrivial cover monodromy is absent from that channel.

This argument does not say that the full adelic space or full cover has no trace formula, resonance theory, or spectral realization involving zeta zeros. Connes's broader adelic program is explicit prior art for such structures. It says only that **abelian Frobenius monodromy read through the ordinary trivial character is not an additional zero-localizing invariant of Riemann zeta**.

## Adversarial controls

**A global cover is not automatically pairwise prime interaction.** The finite abelian cover gives one canonical arithmetic object whose monodromy labels all unramified prime rows and satisfies global reciprocity. The standard character readout remains multiplicative and Euler-factorized. The present finding therefore records a source-derived global relation/selector, not a theorem that every pair of distinct primes has a nonseparable local interaction term.

**Nontrivial characters retain monodromy but change the target.** If `chi` is nontrivial, the values `chi(Frob_p)` survive and produce a Dirichlet/Artin `L(s,chi)`. That is genuine arithmetic information, but it no longer gives the principal Riemann zeta factor. Enlarging to a family of twists reproduces the already-audited pattern that richer coupling can live in a surrounding `L`-family without constraining the principal member.

**Higher-dimensional or nonabelian representations do not refute the narrow obstruction.** Their local factors can retain nontrivial Frobenius conjugacy data. The statement here concerns the exact trivial representation whose Artin `L`-function is `zeta_Q`. A future mechanism may use nonlinear relations among several representations or the geometry of the cover itself, but then it must prove that the resulting invariant still constrains the principal zeta divisor rather than merely neighboring Artin `L`-functions.

**The cover geometry is not declared spectrally inert.** A nonlinear topological, cohomological, determinant, or target-relative invariant might remain nontrivial even after the scalar trivial-character projection. No theorem located in this audit rules that out. What is ruled out is treating the Frobenius character values themselves as the missing principal-channel coupling.

**Class-field theory is not being claimed as new prime-lattice geometry.** The periods, covers, Frobenius monodromy, and Artin factors are established prior art. Their role here is as a falsification control for a specific live design requirement.

## Prior-art and novelty audit

Primary and close sources:

- Alain Connes and Caterina Consani, “Knots, primes and class field theory,” arXiv:2501.06560 (2025), https://arxiv.org/abs/2501.06560. Theorem 1 / Theorem 3.12 constructs the finite abelian covers of `X_Q`; for unramified `p`, the periodic orbit `C_p` has length `log p` and monodromy `Frob_p`.
- Christopher Deninger, “Dynamical systems for arithmetic schemes,” arXiv:1807.06400, https://arxiv.org/abs/1807.06400. Constructs arithmetic dynamical systems in which closed points give packets of periodic orbits of length `log N(x)` and defines commuting Frobenius actions of the multiplicative monoid of positive integers.
- Masanori Morishita, “On a relation between Deninger's foliated dynamical systems and Connes-Consani's adelic spaces,” arXiv:2508.15971 (2025), https://arxiv.org/abs/2508.15971. Gives a direct comparison for abelian number fields and places the two constructions in the primes/knots/class-field-theory dictionary.
- J. S. Milne, *Class Field Theory*, version 4.03 (2020), https://www.jmilne.org/math/CourseNotes/cft.html, especially the chapters on global class field theory and `L`-series. Used only for the standard Artin-map/character `L`-function background; the principal-character collapse is immediate from the definition of the local Artin factor.

A repository audit before publication found no existing `PL-*` finding or `prime_lattice` literature-anchor entry centered on Deninger's arithmetic dynamical systems, Connes–Consani's 2025 class-field covers, or arXiv:2501.06560. `PL-240`–`PL-248` are the nearest internal controls: they establish the analogous survival problem for reciprocity/MDS/Kac–Moody structures but do not supply this source-derived adelic-cover matched control. No novelty is claimed for any class-field or dynamical theorem.

## Research implication

The current three-gate frontier should be sharpened one step further. It is not enough to find a canonical number-field object that assigns globally constrained data to every rational-prime row. **The proposed invariant must remain nontrivial under the exact projection that produces the principal Riemann zeta function.** Abelian-cover Frobenius characters fail this test maximally: the trivial character maps every prime monodromy to the same scalar `1`.

The surviving target is therefore narrower than “find cross-prime geometry.” A viable construction must either produce a genuinely nonlinear invariant of the global cover/linking data that is still visible in a principal-zeta trace/determinant/positivity statement, or find a different source-derived number-field object whose principal extraction is not equivalent to forgetting its mixed-prime structure. Twisting by a nontrivial character, adding ramification, or moving to a neighboring Artin `L`-function does not satisfy that requirement by itself.