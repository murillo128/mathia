# PL-139 — Pretentious function powers have an exact gcd torsion gauge

## Claim

For a unitary completely multiplicative function `f`, consider the set of positive exponents

`P(f) = {k >= 1 : f^k is pretentious}`.

A recent theorem-level observation of Charamaras--Mountakis--Tsinas shows that, whenever `P(f)` is nonempty, there is a unique least positive integer `ell_0` such that

`P(f) = ell_0 N`.

Equivalently, if `f^a` and `f^b` are both pretentious, then `f^gcd(a,b)` is pretentious. Hence any finite family of structured function powers has a sharp dichotomy in the prime-torus picture. If the observed exponents `K={k_1,...,k_r}` have gcd `d>1`, then every observation depending only on the powers `f^(k_j)` is exactly blind to an arbitrary prime-wise `d`-torsion phase field. If `gcd(K)=1` and every `f^(k_j)` is pretentious, then `f` itself is already pretentious.

Thus taking several powers of a multiplicative prime-phase state does not create an intermediate source of zeta-specific rigidity: with nontrivial gcd it factors through a huge torsion quotient of the prime torus, while with coprime exponents the qualitative pretentious information collapses back to ordinary pretentiousness of the original state.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART-REDIRECT + NEGATIVE/OBSTRUCTION`.

The divisibility classification of pretentious powers is literature, not a Mathia novelty claim. The exact coordinatewise torsion-kernel interpretation is an elementary derived translation into exponent-lattice/Pontryagin-dual coordinates. The durable consequence is a falsification boundary for proposals that try to obtain new cancellation rigidity merely by probing several function powers on the prime torus.

## Literature theorem: pretentious powers form a divisibility semigroup

For unitary multiplicative functions, the pretentious distance satisfies the multiplicative triangle inequality. If

`D(f^a, chi_1 n^(it_1)) < infinity`

and

`D(f^b, chi_2 n^(it_2)) < infinity`,

choose integers `u,v` with

`u a + v b = d = gcd(a,b)`.

Because `f` is unitary, negative powers are conjugates. Repeated use of the product triangle inequality therefore gives

`D(f^d, (chi_1 n^(it_1))^u (chi_2 n^(it_2))^v) < infinity`.

This is the unitary specialization of Lemma 2.8 in:

- Dimitrios Charamaras, Andreas Mountakis, Konstantinos Tsinas, “On multiplicative recurrence along linear patterns,” *Journal of the London Mathematical Society* **112**(3) (2025), e70292. DOI: https://doi.org/10.1112/jlms.70292. arXiv: https://arxiv.org/abs/2412.03504.

Their Corollary 2.9 records the resulting classification: if one positive power of `f` is pretentious, then there is a least `ell_0` such that `f^ell` is pretentious exactly when `ell_0 | ell`.

For a finite family `K`, the same Bezout argument gives the quantitative finite-distance implication

`D(f^d,G) <= sum_j |a_j| D(f^(k_j), g_j)`

whenever `sum_j a_j k_j=d`, each `g_j` is a twisted Dirichlet character comparator, and `G=product_j g_j^(a_j)`. In particular, if `d=1`, simultaneous finite pretentious distances for the chosen powers already put the original `f` in the ordinary pretentious class.

## Exact prime-torus kernel

Write the unitary prime phases as

`f(p)=omega_p in T`,

so that

`f(n)=product_p omega_p^(v_p(n))`.

For a finite exponent family `K={k_1,...,k_r}`, the pointwise power observation map on the full prime torus is

`Phi_K((omega_p)_p) = ((omega_p^(k_1))_p, ..., (omega_p^(k_r))_p)`.

Let `d=gcd(k_1,...,k_r)`. At one prime coordinate, the common kernel of the power maps is exactly `mu_d`, the group of `d`th roots of unity. Therefore

`ker Phi_K = product_p mu_d`.

This is an enormous exact gauge, not a conditioning issue. Choose arbitrary residues `a_p in Z/dZ` independently for every prime and define

`eta(p)=exp(2 pi i a_p/d)`,

extended completely multiplicatively. Then `eta^d=1`, and because `d | k_j`,

`(f eta)^(k_j) = f^(k_j)`

for every observed exponent `k_j`. In exponent coordinates,

`eta(n)=exp((2 pi i/d) sum_p a_p v_p(n))`.

Hence every power-only observable with common exponent divisor `d>1` factors through a quotient that erases an arbitrary prime-by-prime torsion character of the exponent lattice. This degeneracy survives replacement of the rational primes by any freely generated multiplicative frequency system; it is group-theoretic rather than zeta-specific.

If `d=1`, the algebraic kernel disappears. Bezout gives integers `a_j` with `sum_j a_j k_j=1`, so for unitary phases

`omega_p = product_j (omega_p^(k_j))^(a_j)`.

Thus coprime exact powers determine the original phase point coordinatewise. But at the qualitative pretentious level this same Bezout identity is precisely why simultaneous pretentiousness of those powers forces ordinary pretentiousness of `f`. There is no third regime in which several coprime powers are individually classical/structured while the base phase remains nonpretentious.

## Liouville is the canonical two-torsion control

The Liouville function is the prime-torus point

`lambda(p)=-1`,

hence

`lambda(n)=(-1)^(sum_p v_p(n))`.

Its powers satisfy the exact parity collapse

`lambda^(2m)=1`,

`lambda^(2m+1)=lambda`.

The Liouville function is nonpretentious by the classical prime-number-theorem/Dirichlet-character zero-free theory, while `lambda^2=1` is trivially pretentious. Thus its least structured exponent is `ell_0=2`, giving the simplest concrete instance of the Charamaras--Mountakis--Tsinas classification.

This is directly relevant to the RH target because

`sum_(n>=1) lambda(n)n^(-s) = zeta(2s)/zeta(s)`

in `Re(s)>1`. An off-critical zero of `zeta(s)` with `Re(s)>1/2` produces a genuine singularity of this quotient because `Re(2s)>1`, where `zeta(2s)` is nonzero. Yet every even function-power channel erases the Liouville sign field completely, while every odd channel merely reproduces the original field. Function-power tomography therefore supplies no progressively richer route to the zero-sensitive cancellation carried by `lambda`.

The Dirichlet-series identity above is used only in its honest absolute-convergence half-plane; the statement about a hypothetical zero in `Re(s)>1/2` uses the meromorphic continuation of the quotient and the zero-freeness of `zeta(2s)` for `Re(2s)>1`, not a continued Euler product.

## Relation to the prime-power metric in PL-138

This obstruction is different from the strong prime-power distance audited in `PL-138`. For a completely multiplicative function,

`f(p^j)=f(p)^j`,

so prime-power sampling certainly contains phase-power information. But the Jung--Lemke Oliver strong distance samples the full initial ray `j=1,...,d`; in particular it includes `j=1`, and therefore its exponent family has gcd one and no torsion kernel. `PL-139` does not weaken their transfer theorem.

Instead, it closes a natural attempted repair after `PL-138`: one cannot hope to manufacture a new source of cancellation by discarding the base phase and demanding that several higher function powers be individually structured. If their exponents share a divisor, an arbitrary prime-wise torsion gauge remains invisible. If their gcd is one, the hypothesis already implies ordinary pretentiousness of the base function by established theory.

Likewise, this finding does not say that quantitative distances between several powers are useless. They may sharpen estimates once a comparator or cancellation input is already present. The narrower negative statement is that the **qualitative structured-power pattern itself** has the exact gcd classification above and cannot provide an independent RH-selection mechanism.

## Prior-art and novelty audit

The load-bearing analytic statement is already explicit in Charamaras--Mountakis--Tsinas: Lemma 2.8 proves gcd closure of pretentious powers and Corollary 2.9 proves that the structured exponents are exactly the multiples of one least exponent. Their application is multiplicative recurrence, not Riemann-zero localization, but the theorem directly governs the proposed prime-torus power probe.

The coordinatewise kernel `product_p mu_d` is immediate compact-abelian-group algebra. It should not be claimed as a new theorem. Its value here is as the matched geometric explanation of why the divisibility classification is unavoidable: the power map on each prime circle has precisely the same torsion ambiguity, independently at every coordinate.

No source found in the targeted audit turns this power divisibility structure into an RH or critical-line mechanism. That absence is not a novelty claim. The positive content stored here is the 2025 theorem plus its exact prime-lattice specialization and Liouville control.

## Adversarial limits and consequence for the line

Several stronger claims would be false. The finding does not rule out joint correlations involving shifted values `f(n+h)`, nonlinear observables that retain the base phase, or prime-power metrics that include exponent one. It does not claim that pretentiousness itself is too weak for all power-saving questions; `PL-138` already records stronger relative metrics that genuinely transfer power cancellation. It also does not extend the torsion-kernel statement unchanged to nonunitary multiplicative functions, where zeros destroy the simple inverse/conjugate algebra used in the Bezout reconstruction.

The reusable boundary is narrower and exact. A proposal based only on a finite set of function powers must first compute the gcd of its exponents. For `d>1`, it is blind to `product_p mu_d`; for `d=1`, simultaneous qualitative pretentiousness already reduces to ordinary pretentiousness. A surviving RH mechanism must therefore add information that is not obtainable merely by taking more powers of the same prime-phase point: a target-relative correlation, global functional equation/completion, explicit-formula positivity, or another structure that actually couples the arithmetic phase to the zeta zero divisor.