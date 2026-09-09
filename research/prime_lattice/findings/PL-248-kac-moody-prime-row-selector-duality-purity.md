# PL-248 — Kac–Moody multivariance lives inside each prime row; canonical global selection uses duality and purity

## Claim

`PL-247` established a genuine representation-theoretic escape from the affine one-variable obstruction: in indefinite Kac–Moody type the standard imaginary-root correction factor has support in several independent root-lattice directions. A closer arithmetic audit shows that this does **not** yet give the kind of mixed-rational-prime geometry required by the `prime_lattice` mandate.

For an `r`-variable multiple Dirichlet series

`Z(s_1,...,s_r) = sum_(m_1,...,m_r) c(m_1,...,m_r) product_i |m_i|^(-s_i)`,

the natural exponent data are a two-index array

`a_(p,i) = v_p(m_i)`.

The rational prime `p` indexes a **row**, while the Dirichlet/root variable `i` indexes a **column**. A local `p`-part and its Kac–Moody root variables act on the finite-dimensional row

`a_p = (v_p(m_1),...,v_p(m_r)) in N_0^r`.

Consequently, the multivariable imaginary-root correction from `PL-247` is multivariable **inside one fixed rational-prime row**. It is not, by itself, a coupling among distinct rational-prime coordinates `v_p(n)` and `v_q(n)` of a single integer. The genuinely cross-prime arithmetic interaction in the established multiple-Dirichlet-series constructions enters instead through twisted multiplicativity/residue-symbol factors relating coprime tuples. That is the reciprocity mechanism already audited in `PL-240`–`PL-242`, whose straightforward principal Riemann channel loses the nontrivial twist.

There is nevertheless a known way to select a canonical global object when Weyl symmetry leaves imaginary-root freedom: the axiomatic function-field construction of Sawin and its functional-equation analysis with Whitehead. But the selector is **extra geometric input**, not Kac–Moody symmetry alone. In the Sawin–Whitehead formulation the five axioms uniquely determine the coefficient system; the local-to-global axiom is realized by Verdier duality and the dominance axiom by cohomological purity of the perverse-sheaf construction. Popa–Walsh explicitly contrast this unique axiomatic MDS with the infinitely many invariant `p`-parts available in infinite Kac–Moody type and state that recovering the axiomatic MDS from a choice of `p`-parts is open beyond special cases.

Thus the live obstruction after `PL-247` is sharper than “find a multivariable correction.” Known Kac–Moody multivariance has the wrong index geometry for direct prime-axis coupling, while the known canonical global selector imports local-to-global duality and purity. A Riemann-zeta mechanism would need a number-field/prime-lattice analogue of that selector that is independently justified and whose mixed-prime information survives projection to the ordinary zeta channel.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART-REDIRECT + NEGATIVE-BOUNDARY + NO-NOVELTY-CLAIM`. The multiple-Dirichlet-series coefficient axioms, uniqueness, perverse-sheaf realization, Verdier-duality/local-to-global correspondence, purity/dominance correspondence, Kac–Moody decomposition, imaginary-root freedom, and analytic-continuation statements are prior art. The two-index `prime row × root-variable column` interpretation is an exact unpacking of the local prime-power coefficients and is not claimed as a new theorem. The durable delta is the routing consequence for `prime_lattice`: indefinite root-lattice dimensionality cannot be counted as mixed-rational-prime coupling, and the known source-forced global selector uses geometric input external to Weyl invariance.

## The two exponent lattices must not be conflated

The exponent-vector geometry of this research line starts with one positive integer

`n = product_p p^(v_p(n))`,

so its coordinates are indexed by rational primes. For an `r`-variable MDS, each summation variable has its own copy of this lattice:

`m_i = product_p p^(a_(p,i))`.

Equivalently the full exponent datum is an array `A=(a_(p,i))` with finitely many nonzero entries. Holding a rational prime `p` fixed gives the row `a_p in N_0^r`; holding a Dirichlet variable `i` fixed gives the ordinary prime-exponent vector of `m_i` across all rational primes.

This indexing is visible directly in the prime-power axiom of Sawin–Whitehead. At a fixed irreducible/global prime `pi`, the local coefficient has the form

`a(pi^(d_1),...,pi^(d_r); ...)`,

where `(d_1,...,d_r)` is the local valuation tuple. The Cartan/root-system data govern interactions among the `r` entries of this tuple. Likewise the Chinta–Gunnells `p`-part is a function of the root variables attached to one place.

Therefore the indefinite correction factor from `PL-247`, whose monomials are `e^lambda` for imaginary roots `lambda` in the Kac–Moody root lattice, enriches the **column geometry at fixed `p`**. It does not canonically identify an imaginary-root direction with one rational prime. Transposing these two index sets by hand would be an arbitrary re-encoding and would violate the line mandate unless an arithmetic construction itself supplied such a bridge.

This is a stronger control than the generic warning that a Kac–Moody root lattice is not the prime lattice. It specifies exactly where the two structures coexist in established arithmetic constructions and shows that they occupy different tensor factors/index levels.

## Where genuine cross-prime coupling actually enters

Sawin–Whitehead Axiom 1 is twisted multiplicativity. For coprime tuples of polynomials/integers, the coefficient of the product is the product of the separate coefficients times residue-symbol factors with exponents determined by the matrix/Cartan data. Those symbols compare factors belonging to different global primes after prime factorization.

Hence there are two logically distinct sources of nonseparability:

- the local Kac–Moody `p`-part couples root/Dirichlet-variable coordinates within one prime row;
- twisted multiplicativity couples different global prime rows through arithmetic residue symbols.

Only the second is directly of the mixed-rational-prime kind sought by this line. But `PL-240`–`PL-242` already audited the quadratic-reciprocity version of that mechanism: it is genuine arithmetic cross-prime structure, yet extracting the ordinary principal Riemann factor by the natural trivial/principal specialization separates or discards the twist rather than converting it into a sign or spectral constraint on the zeta zeros.

Thus indefinite imaginary-root support does not evade the principal-channel obstruction by itself. It adds local multivariable complexity before the global prime assembly; it does not prove that the cross-prime reciprocity data remain attached to the ordinary zeta divisor.

## Weyl symmetry leaves a global selection problem

Popa–Walsh prove a decomposition theorem for functions invariant under the twisted Chinta–Gunnells action for symmetrizable Kac–Moody root systems. In infinite type, and already visibly in affine type, imaginary roots produce free invariant coefficients. In the untwisted case they state that there are infinitely many choices of invariant `pi`-parts when the root system is infinite.

Their Corollary 4.5 identifies the remaining freedom with coefficients indexed by weights satisfying nonpositive simple-coroot pairings; the connected-support representatives are representatives of Weyl orbits of positive imaginary roots. In affine type these are exactly multiples of the minimal imaginary root, recovering the one-variable freedom of `PL-245`. Beyond affine type the imaginary-root structure is correspondingly more complicated.

Popa–Walsh also prove analytic continuation of the relevant Chinta–Gunnells averages to the interior of the complexified Tits cone. This is important control: the obstruction here is **not** that infinite Kac–Moody theory has no analytic continuation at all. Lee–Zhang had already constructed symmetrizable Kac–Moody multiple Dirichlet series over number fields with functional equations and meromorphic continuation to a convex subcone of the shifted Tits cone. Popa–Walsh improve the analytic picture for the individual averages, while emphasizing that controlling the coefficients in the global decomposition remains a separate problem.

So functional-equation/Weyl symmetry plus local analytic continuation does not uniquely select the global arithmetic series in infinite type.

## The known canonical selector is local-to-global geometry

Sawin's axiomatic multiple Dirichlet series over `F_q[T]`, later analyzed for functional equations by Sawin–Whitehead, supplies a canonical coefficient system by adding geometric axioms rather than choosing one Chinta–Gunnells invariant `p`-part arbitrarily.

The Sawin–Whitehead formulation uses five axioms. For the present boundary, three are decisive:

1. twisted multiplicativity supplies the arithmetic residue-symbol coupling;
2. the local-to-global principle relates the fixed-prime coefficients to global coefficient sums;
3. the dominance principle imposes weight bounds on the Weil-number constituents.

Their uniqueness theorem states that these axioms determine a unique coefficient system. Their discussion of the perverse-sheaf construction is equally important for source audit: the local-to-global axiom is a **Verdier-duality statement**, while the dominance axiom is a **cohomological-purity statement**. The selector therefore contains geometric information that is not a formal consequence of Weyl invariance or of the Kac–Moody correction factor.

Popa–Walsh make the comparison explicit. They note that the axiomatic method produces a unique untwisted MDS for arbitrary root data covered by the construction, whereas infinite Kac–Moody Chinta–Gunnells invariance leaves infinitely many possible `pi`-parts. They further state that choosing `pi`-parts so as to recover the axiomatic MDS is open in general; even for star-shaped systems beyond the established special cases, relating the two constructions remains an open problem.

This supplies exactly the kind of “source-forced selector” requested by `PL-247`, but also shows why it is not yet an RH mechanism for the rational-prime lattice: the forcing comes from a function-field geometric package whose duality and purity have no demonstrated number-field replacement here.

## Analytic-continuation control

This finding must not be read as saying that Kac–Moody multiple Dirichlet series lack continuation. Lee–Zhang prove meromorphic continuation on a convex subcone `X_0` of the shifted Tits cone for their symmetrizable Kac–Moody MDS. Popa–Walsh prove that the Chinta–Gunnells averages in their decomposition continue analytically to the interior of the complexified Tits cone. In explicit affine cases, additional functional equations/local-to-global normalization can yield still sharper formulas.

The remaining issue is instead **selection and survival**: which invariant local object is the arithmetic one, what extra global law selects it, and does that law remain nontrivial after restricting to the exact ordinary-zeta channel? None of the continuation statements alone answers those questions.

Likewise, no Euler product valid only in `Re(s)>1` is being transported formally to the Riemann critical strip. The literature cited here proves continuation for its own multivariable objects by its own functional-equation/geometric methods. Any future specialization to `zeta(s)` must separately prove that the relevant identity survives analytic continuation.

## Adversarial controls

**Multivariable root support is not mixed-prime support.** The full-rank imaginary cone of an indefinite Kac–Moody system is a theorem about the root-variable factor at a fixed place. It does not couple `v_p(n)` and `v_q(n)` for distinct rational primes unless a separate global construction does so.

**Twisted multiplicativity is genuine mixed-prime structure, but it is not new here.** Residue-symbol/reciprocity coupling is exactly the kind of rational-prime-specific datum demanded by the mandate. It was already the subject of `PL-240`–`PL-242`; the open requirement is to make it survive the principal Riemann extraction rather than merely reconstruct a larger family of Dirichlet `L`-functions.

**Purity is an input to the known selector, not a proof that every selector must use purity.** Sawin–Whitehead identify their dominance axiom with cohomological purity. This finding therefore rules out claiming that Weyl symmetry alone canonically chooses their object. It does not prove that no different number-field selector could exist.

**The function-field construction must not be promoted to a number-field RH proof.** Perverse-sheaf/Frobenius weight control is powerful source-derived structure in the function-field setting. A rational-prime analogue would require an independently constructed object and independently proved sign/self-adjointness/purity statement; importing the conclusion by analogy would be circular.

**Partial continuation is not uniqueness.** Lee–Zhang and Popa–Walsh provide substantial meromorphic/analytic continuation, so lack of continuation is not the obstruction being claimed. Conversely, continuation of each basis average does not by itself control the infinite global combination or identify the canonical arithmetic coefficients.

## Prior-art and novelty audit

Primary sources:

- Alexandru A. Popa and Jack Walsh, “A decomposition of Weyl group multiple Dirichlet series for symmetrizable Kac–Moody root systems,” arXiv:2607.11834 (2026), https://arxiv.org/abs/2607.11834. Relevant points: decomposition into shifted Chinta–Gunnells averages; imaginary-root coefficient freedom; infinitely many invariant `pi`-parts in infinite type; analytic continuation of the averages to the interior of the complexified Tits cone; comparison with the canonical axiomatic MDS and the open problem of recovering it from `pi`-parts.
- Will Sawin and Ian Whitehead, “Functional equations of axiomatic multiple Dirichlet series, Weyl groupoids, and quantum algebra,” arXiv:2507.08662 (2025; later revisions), https://arxiv.org/abs/2507.08662. Relevant points: five geometric axioms; twisted multiplicativity; prime-power coefficient axiom; local-to-global and dominance principles; uniqueness; functional equations; identification of Axiom 4 with Verdier duality and Axiom 5 with cohomological purity.
- Will Sawin, “General multiple Dirichlet series from perverse sheaves,” *Journal of Number Theory* **262** (2024), 408–453, arXiv:2209.13072, https://arxiv.org/abs/2209.13072. Relevant point: existence of the axiomatic coefficient system via trace functions of explicit perverse sheaves.
- Kyu-Hwan Lee and Yichao Zhang, “Weyl group multiple Dirichlet series for symmetrizable Kac–Moody root systems,” *Transactions of the American Mathematical Society* **367** (2015), 597–625, DOI `10.1090/S0002-9947-2014-06159-X`. Relevant control: functional equations and meromorphic continuation to a convex subcone of the shifted Tits cone for symmetrizable Kac–Moody MDS over number fields.

No novelty claim is made for the axioms, the decomposition, the continuation theorems, or the geometric interpretation of the axioms. The `prime row × root-variable column` distinction is an exact bookkeeping consequence of the local coefficient `a(pi^(d_1),...,pi^(d_r))`; it is recorded because it prevents a specific category error in transferring `PL-247` to the rational prime-exponent lattice.

A novelty search found no source claiming that the indefinite Kac–Moody imaginary correction, merely by being multivariable, supplies cross-rational-prime rigidity for the Riemann zeta function. The nearest literature instead separates local `p`-parts from global twisted multiplicativity and, in the axiomatic construction, supplies extra local-to-global/purity data. This supports the negative routing statement rather than a discovery claim.

## Research implication

The Kac–Moody branch should no longer treat “indefinite multivariable imaginary correction” as satisfying the mixed-prime gate of the `prime_lattice` contract. It satisfies a **local root-variable nonseparability** gate, which is weaker and lives at fixed global prime.

A surviving construction must now cross three explicit gates. First, it must produce a source-derived relation among distinct rational-prime rows, not merely among root variables at one place. Second, it must provide a canonical selector comparable in force to local-to-global duality/purity without assuming the desired Riemann-zero localization. Third, after specializing/extracting the ordinary Riemann factor, that relation must remain nontrivial and feed an independently controlled sign, positivity, self-adjointness, trace, determinant, or resonance mechanism.

The existing literature gives separate exemplars for the first two ingredients—reciprocity for cross-prime coupling, and function-field duality/purity for canonical selection—but the current audit finds no theorem that makes them survive together in the principal Riemann channel. That conjunction, rather than additional Kac–Moody rank or additional local imaginary-root dimension, is the next falsifiable target.