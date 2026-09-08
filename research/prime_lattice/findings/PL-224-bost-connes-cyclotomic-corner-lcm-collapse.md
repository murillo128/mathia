# PL-224 — Bost–Connes cyclotomic corner products collapse exactly to the lcm join

## Claim

The most canonical finite cyclotomic coupling left open by `PL-223` has an exact semilattice collapse. In the rational Bost–Connes algebra let

\[
\rho_n(e(r)):=\mu_n e(r)\mu_n^*,
\qquad n\ge 1,
\qquad r\in\mathbb Q/\mathbb Z.
\]

For any finite family `n_1,...,n_k` and `r_1,...,r_k`, put

\[
L=\operatorname{lcm}(n_1,\ldots,n_k),
\qquad
R=\sum_{j=1}^k \frac{L}{n_j}r_j\in\mathbb Q/\mathbb Z.
\]

Then there is the exact operator identity

\[
\boxed{
\prod_{j=1}^k \rho_{n_j}(e(r_j))
=\rho_L(e(R)).
}
\]

Thus multiplication of these canonical gauge-neutral cyclotomic corners realizes the **join** of the exponent vectors:

\[
v_p(L)=\max_j v_p(n_j).
\]

For every Bost–Connes `KMS_beta` state `phi_beta`, at every real `beta>0`, the whole finite hierarchy consequently satisfies

\[
\boxed{
\phi_\beta\!\left(\prod_{j=1}^k\rho_{n_j}(e(r_j))\right)
=L^{-\beta}\phi_\beta(e(R)).
}
\]

Hence these source-forced multi-prime/cyclotomic correlations contain **no independent higher-order scalar data** beyond the one-point cyclotomic state and the elementary lcm/addition law. In the broken-symmetry Gibbs regime `beta>1`, any `1/zeta(beta)` dependence is exactly the already-known one-point dependence of `phi_beta(e(R))`; finite corner products do not generate a new determinant, trace, or cross-prime zero-localization constraint. In `0<beta<=1`, `PL-214` already identifies the one-point cyclotomic values as finite divisor/exponential data, so the same collapse is zeta-divisor free there.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION + PRIOR-ART-AUDITED + NO-NOVELTY-CLAIM`.

The negative is deliberately restricted to finite products of the canonical diagonal corners `rho_n(e(r))`. It does not classify arbitrary nonalgebraic elements of the cyclotomic diagonal, genuinely infinite-prime limits, unbounded affiliated observables, renormalized traces/determinants, noncommuting relative modular constructions, or adelic/Weil scattering.

## 1. The cyclotomic corner is a divisibility-filtered phase

The standard Bost–Connes representation on `ell^2(N)` has

\[
\mu_n\varepsilon_m=\varepsilon_{nm},
\qquad
 e(r)\varepsilon_m=e^{2\pi i rm}\varepsilon_m.
\]

Therefore

\[
\rho_n(e(r))\varepsilon_m
=
\begin{cases}
 e^{2\pi i r(m/n)}\varepsilon_m,&n\mid m,\\
 0,&n\nmid m.
\end{cases}
\]

This already shows that `rho_n(e(r))` is diagonal and that its support is the divisibility event `n|m`. The same object is the classical Bost–Connes endomorphism on the cyclotomic algebra; equivalently,

\[
\rho_n(e(r))
=\frac1n\sum_{ns=r}e(s).
\]

The latter formula is standard Bost–Connes/endomotive structure. The present finding uses it only as the intrinsic algebraic object and does not treat it as new.

## 2. Products are governed by coordinatewise maximum, not by a new interaction

Take first two factors. Let

\[
L=\operatorname{lcm}(n,m),
\qquad
R=\frac Ln r+\frac Lm s.
\]

On a basis vector `epsilon_a`, the product vanishes unless both `n|a` and `m|a`, which is equivalent to `L|a`. If `a=Lq`, then

\[
\begin{aligned}
\rho_n(e(r))\rho_m(e(s))\varepsilon_a
&=
 e^{2\pi i r(a/n)}e^{2\pi i s(a/m)}\varepsilon_a\\
&=
 e^{2\pi i q((L/n)r+(L/m)s)}\varepsilon_a\\
&=
\rho_L(e(R))\varepsilon_a.
\end{aligned}
\]

Hence

\[
\boxed{
\rho_n(e(r))\rho_m(e(s))
=\rho_{\operatorname{lcm}(n,m)}
\!\left(e\!\left(\frac Ln r+\frac Lm s\right)\right).
}
\]

Induction gives the finite-family formula in the claim. No limiting argument or analytic continuation is involved.

In exponent-lattice coordinates the support law is especially transparent. The event `n_j|a` imposes

\[
v_p(a)\ge v_p(n_j)
\]

for every prime `p`. Intersecting all such events imposes

\[
v_p(a)\ge \max_j v_p(n_j)=v_p(L).
\]

Thus the Bost–Connes cyclotomic corner product sees the lattice join exactly. The phase variable is transported compatibly by the integer coefficients `L/n_j`. This is genuine source-forced arithmetic structure, but it is a **semilattice composition law**, not an independent many-body interaction among prime directions.

## 3. KMS expectation collapses the entire finite hierarchy to one point

The Bost–Connes time evolution satisfies

\[
\sigma_t(\mu_L)=L^{it}\mu_L,
\qquad
\sigma_t(e(R))=e(R).
\]

For any `KMS_beta` state and real `beta>0`, the KMS identity applied to

\[
a=\mu_L,
\qquad
b=e(R)\mu_L^*
\]

gives

\[
\begin{aligned}
\phi_\beta(\rho_L(e(R)))
&=\phi_\beta(\mu_L e(R)\mu_L^*)\\
&=\phi_\beta\!\left(e(R)\mu_L^*\sigma_{i\beta}(\mu_L)\right)\\
&=L^{-\beta}\phi_\beta(e(R)),
\end{aligned}
\]

because `mu_L^*mu_L=1`. Combining with the operator identity yields

\[
\boxed{
\phi_\beta\!\left(\prod_j\rho_{n_j}(e(r_j))\right)
=L^{-\beta}\phi_\beta(e(R)).
}
\]

This statement is independent of which extremal state is chosen when `beta>1`: the state dependence survives only through the single cyclotomic coefficient `phi_beta(e(R))`.

For an extremal low-temperature Gibbs state indexed by arithmetic symmetry data `chi`, the classical one-point formula has the form

\[
\phi_{\beta,\chi}(e(R))
=\frac{1}{\zeta(\beta)}
\sum_{m\ge1}\frac{\chi(e(mR))}{m^\beta},
\qquad \beta>1.
\]

Therefore every finite corner correlation is merely

\[
L^{-\beta}
\frac{\text{one periodic/cyclotomic Dirichlet series}}{\zeta(\beta)}.
\]

The denominator is not multiplied with the correlation order, and no new joint prime factor appears. Meromorphically continuing this scalar quotient in a complex variable can of course expose Riemann zeros as poles, but that continuation is not a KMS state in the critical strip and supplies no positivity or self-adjoint localization principle. This is the same analytic-continuation boundary already isolated in `PL-212` and `PL-214`.

For `0<beta<=1`, the actual unique KMS state is instead the high-temperature state of `PL-214`; its value on every fixed `e(R)` is a finite divisor sum depending on the denominator of `R`. Consequently the finite corner hierarchy is finite/exponential data in this regime as well.

## 4. Why this closes a live branch after `PL-223`

`PL-223` identifies the finite-prime algebra generated only by the isometries `mu_p` with a tensor product of ordinary Toeplitz systems and explicitly leaves the cyclotomic diagonal outside that negative. The natural next test is therefore to mix the prime dilations with the canonical arithmetic phases while retaining a source-forced finite family.

The corners `rho_n(e(r))=mu_n e(r)mu_n^*` are the most intrinsic gauge-neutral such observables: they combine a divisibility condition, a cyclotomic phase, and the multiplicative semigroup action without adding an external coefficient system. Their products do produce nonfactorizing arithmetic expressions. However, the displayed identity proves that the apparent higher-order coupling is fully reducible to one corner at the lattice join.

For distinct primes `p,q`, for example,

\[
\boxed{
\rho_p(e(r))\rho_q(e(s))
=\rho_{pq}(e(qr+ps)),
}
\]

and therefore

\[
\boxed{
\phi_\beta(\rho_p(e(r))\rho_q(e(s)))
=(pq)^{-\beta}\phi_\beta(e(qr+ps)).
}
\]

This is a real cross-prime law, unlike the independent Toeplitz moments of `PL-223`, but it does not generate a new hierarchy of invariants: the two-prime readout is exactly a one-point readout at the join. The same statement holds at every finite order.

## 5. Prior-art and novelty audit

The algebra, the isometries `mu_n`, the cyclotomic generators `e(r)`, their semigroup relation, the time evolution, and the KMS phase structure are classical Bost–Connes theory; source 5 in `research/prime_lattice/SOURCES.md` is the primary anchor. The endomotive formulation writes the same canonical map explicitly as

\[
\rho_n(e(r))=\frac1n\sum_{ns=r}e(s),
\]

so regarding these maps as arithmetic semigroup endomorphisms is established prior art.

A targeted audit around Bost–Connes semigroup crossed products, endomotives, cyclotomic endomorphisms, and KMS correlations found no basis for a novelty claim. The lcm product identity is an elementary consequence of the classical action and should be regarded as a derived semilattice law, not a new theorem about the Bost–Connes system.

The durable Mathia delta is the **closure of a specific surviving research escape**. `PL-223` left finite source-forced cyclotomic couplings open; the canonical corner hierarchy is now classified exactly and shown not to create new scalar RH rigidity beyond the already-known one-point cyclotomic channel.

## 6. Boundaries and adversarial controls

**The collapse is finite.** An infinite product or norm/weak limit of corners can involve convergence, support, and renormalization phenomena that are absent from the finite identity. The result does not license passage to such a limit term by term.

**The diagonal algebra is much larger than the algebraic corner family.** Arbitrary bounded or measurable diagonal observables need not be a single `rho_n(e(r))` or finite product thereof. `PL-219` classifies scalar KMS readouts through the whole diagonal, but the present lcm identity does not claim a normal form for every diagonal element.

**Noncommuting relative objects are not covered.** Commutators, relative modular operators for genuinely noncommuting states, scattering data, and unbounded affiliated constructions are outside the claim.

**Nonfactorizing does not mean independent information.** The pair correlation generally differs from the product of its one-point expectations, so the result is not probabilistic independence. The exact statement is stronger and different: the product observable itself reduces to one canonical corner.

**The lcm geometry is arithmetic but not RH-selective.** Coordinatewise maximum is a genuine operation on the exponent lattice. Nothing in the identity distinguishes `beta=1/2`, the functional equation, or the Riemann zero divisor. The only zeta denominator available at low temperature is inherited from the already-classical one-point Gibbs normalization.

## Falsification / audit tests

The claim would require correction or narrowing if any of the following failed:

1. the standard representation did not satisfy `mu_n epsilon_m=epsilon_(nm)` and `e(r)epsilon_m=exp(2 pi i r m)epsilon_m`;
2. `rho_n(e(r))` did not act as the divisibility-filtered phase displayed above;
3. intersection of the supports `n_j|m` failed to equal `lcm(n_j)|m`;
4. the transported phase on that intersection were not `sum_j (L/n_j)r_j`;
5. the KMS identity failed to give `phi_beta(rho_L(e(R)))=L^(-beta)phi_beta(e(R))`; or
6. a finite product of these canonical corners contained scalar KMS information not determined by the resulting pair `(L,R)` and the one-point cyclotomic state.

All six tests are exact and independent of RH.

## Consequence for the research line

The bounded finite Bost–Connes frontier is now sharper. `PL-223` removes higher-order structure in the pure finite-prime isometry sector. `PL-224` shows that the most canonical finite **cyclotomic** enlargement also fails to create an irreducible hierarchy: its multiplication is just the exponent-lattice join together with transported cyclotomic addition, and every KMS moment reduces to one point.

A surviving source-forced Bost–Connes mechanism must therefore cross a genuinely global or noncommuting boundary: an infinite-prime limit whose convergence does not collapse to the diagonal one-point state, an unbounded/renormalized relative object, a noncommuting same-sector construction outside the centralizer controls of `PL-221`, or an adelic/Weil trace/positivity mechanism. Merely increasing the finite number of canonical cyclotomic prime corners is no longer a live escape.
