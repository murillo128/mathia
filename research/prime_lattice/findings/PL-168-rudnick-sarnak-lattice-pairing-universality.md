# PL-168 — Restricted n-level zero correlations collapse exponent-lattice conservation to universal GUE pairings

## Claim

The most direct higher-zero-correlation escape left open by `PL-166`--`PL-167` is already classical in the low-Fourier-support regime. Rudnick--Sarnak's n-level correlation theorem converts the explicit formula into multiplicative matching conditions whose exponent-lattice form is

`v(n_1)+...+v(n_r)=v(n_(r+1))+...+v(n_(r+s))`.

For the Riemann zeta function, when the Fourier transform of the n-level test function is supported in

`sum_j |xi_j| < 2`,

the leading contribution is exhausted by the multi-diagonal sector: the numbers contributing at leading order reduce to distinct primes, the two sides have the same cardinality, and the primes on one side are a permutation of those on the other. The resulting pairing combinatorics is exactly what assembles into the universal sine-kernel/GUE determinant.

Thus a fixed-n higher-correlation statistic does not automatically create a new cross-prime invariant merely because its explicit-formula expansion contains several prime variables. In the rigorously controlled Rudnick--Sarnak support range, the prime-exponent lattice enters at leading order only through additive conservation plus unique-factorization pairings; irreducible mixed-prime configurations do not survive at the same scale.

There is a second obstruction to using this channel as an RH-localization mechanism. Rudnick--Sarnak's smoothed complex-zero correlation theorem is formulated so that it makes sense without RH and proves the same GUE expression in this restricted support class. Their standard ordinate-only n-level correlation statement is then obtained under RH. Consequently the low-support smoothed statistic cannot distinguish hypothetical off-line zeros, while the usual real-ordinate GUE formulation assumes the localization one would want to prove.

**Evidence/status:** `LITERATURE+DERIVED + PRIOR-ART/REDIRECT + NEGATIVE/OBSTRUCTION`. The n-level correlation theorem, support restriction, product-matching reduction, diagonal-pairing asymptotics, and GUE determinant are classical Rudnick--Sarnak prior art. The line-specific content is the translation of their multiplicative matching into exact exponent-vector conservation and the resulting restriction on the surviving `prime_lattice` higher-correlation branch. No novelty is claimed for n-level correlations, the explicit formula, the GUE law, or the pairing argument.

## The explicit-formula matching condition is exactly exponent-vector conservation

Rudnick--Sarnak apply a smoothed explicit formula independently in the n zero variables. On the arithmetic side this produces Dirichlet variables supported on prime powers, with signs according to which side of the Fourier expansion they enter. In the central range selected by the compact Fourier support, their reduction forces

`n_1 ... n_r = n_(r+1) ... n_(r+s)`.

Unique factorization turns this multiplicative identity into the exact prime-lattice equation

`sum_(j<=r) v(n_j) = sum_(r<j<=r+s) v(n_j)`.

This is the natural higher-order conservation law of the free abelian exponent lattice. It is stronger than the one-character first-moment condition used in `PL-162`--`PL-167`, because several prime-power variables can in principle participate in one balanced relation. The important point is what Rudnick--Sarnak then prove happens at leading order under the support restriction.

Their diagonal analysis shows that the main term occurs only in the balanced case `r=s`. Higher prime powers and repeated-prime degeneracies are lower order; the leading contribution is from distinct primes. Once the two products of distinct primes are equal, unique factorization leaves no nontrivial polygon in the exponent lattice: the primes on the positive side must be exactly a permutation of the primes on the negative side. In coordinates, the surviving configurations are sums of paired basis vectors `e_p-e_p`, not genuinely mixed conserved circuits.

This is visible directly in their main-term formula: after restricting to distinct primes, the inner equality `q_1...q_r=p_1...p_r` makes `(q_1,...,q_r)` a permutation of `(p_1,...,p_r)`. Their introduction explicitly identifies these diagonal pairings, rooted in unique factorization, as the source of the combinatorics that produces the GUE determinant.

## Pairing universality erases detailed prime geometry at leading order

The limiting n-level density is

`W_n(x_1,...,x_n)=det(K(x_i-x_j))`,

with

`K(x)=sin(pi x)/(pi x)`.

For zeta, the natural theorem-level support region is `sum_j |xi_j|<2`. Within this region the detailed arithmetic distribution of the prime variables does not survive as a new mixed-prime tensor in the leading law. What survives is the second-moment normalization of the prime coefficients together with the pairing/partition combinatorics.

Rudnick--Sarnak make the universality point stronger than is needed here. Their theorem applies to broad primitive automorphic L-functions and yields the same n-level GUE law even though the local coefficient distributions at the primes are not universal. They explain that a universal Rankin--Selberg second moment, combined with the diagonal pairings, is what removes those local differences. For `prime_lattice`, this is an adverse matched control: even replacing the trivial zeta local data by substantially different primitive automorphic local data leaves the same restricted-support limiting correlation.

Accordingly, the appearance of a determinant or an n-body zero statistic after several copies of the explicit formula is not by itself evidence for a new rational-prime spectral geometry. In this classical regime the determinant is the universal combinatorial packaging of pairings.

## Why this does not provide an RH localization mechanism

Rudnick--Sarnak deliberately separate two statements. Their smoothed theorem uses entire/localized test functions so that the correlation sum remains meaningful when the zero parameters are not real; this is the theorem that they prove without assuming RH. In the zeta case it already has the GUE asymptotic in the restricted support range.

To obtain the ordinary n-level correlation of real zero ordinates with a sharp height window, they then assume RH. This distinction matters for the research mandate. The unconditional smoothed theorem demonstrates that its limiting pairing law is compatible with the actual completed zero divisor without first proving that every zero lies on the critical line. Conversely, the standard real-ordinate GUE statement cannot be invoked as the missing half-line rigidity because RH is one of its hypotheses in this route.

Therefore this channel is analogous to several earlier `prime_lattice` controls: a mathematically genuine prime/zero correspondence exists, but the part that is rigorously universal is too insensitive to localize the divisor, while the sharper critical-line interpretation presupposes the localization.

## Relation to the recent finite-horizon phase branch

`PL-166` shows that growing-dimensional first moments with full positive Fourier support hit a primorial frequency ceiling before their additive prime bias becomes order one. `PL-167` shows that allowing mixed signs can avoid that ceiling only at the price of near-zero-frequency aliasing when the cancellation becomes too strong. Both findings therefore leave higher zero correlations as a formal escape because products involving several zero variables are not reducible to one torus character moment.

The present prior-art audit closes the cheapest version of that escape: **fixed-order, restricted-support n-level correlations obtained by multiplying the ordinary explicit formula**. Their multi-prime arithmetic side is not a new irreducible coupling. The support condition drives it to exponent-vector conservation, and the main asymptotic drives that conservation further down to pairings.

This also extends the redirect of `PL-076`. There the canonical smoothed quadratic long-von-Mangoldt aggregate lands in Montgomery pair correlation. Increasing the correlation order does not, by itself, leave classical territory: Rudnick--Sarnak already treat arbitrary fixed n in the low-support regime and obtain the universal GUE hierarchy.

## Prior-art and novelty audit

The primary source is Zeev Rudnick and Peter Sarnak, “Zeros of principal L-functions and random matrix theory,” *Duke Mathematical Journal* **81**(2) (1996), 269--322, DOI `10.1215/S0012-7094-96-08115-6`.

Theorem 1.1 proves the smoothed n-level asymptotic for primitive automorphic L-functions with Fourier support `sum |xi_j|<2/m`; for zeta (`m=1`) this is `sum |xi_j|<2`. Theorem 1.2 gives the standard n-level GUE correlation under RH. Section 3 derives the product-matching condition and proves dominance of diagonal pairings; Section 4 identifies the resulting combinatorial expression with the Fourier transform of the sine-kernel determinant. Their remarks explicitly say that, for zeta, the support `<2` is the natural range where all multi-diagonals dominate, while beyond that range saturation/polar and off-diagonal effects become significant.

A bounded modern audit found later work elaborating n-level correlations and random-matrix formulae, but no reason to reinterpret the Rudnick--Sarnak pairing mechanism as new prime-lattice structure. The exact lattice-conservation wording used here is only a coordinate translation of their multiplicative equality. The substantive research delta is a route classification relative to `PL-166`--`PL-167`, not a novelty claim.

## Adversarial boundaries

1. **The support restriction is load-bearing.** For zeta, `sum |xi_j|<2` is exactly the range in which Rudnick--Sarnak identify multi-diagonal dominance. Beyond it, off-diagonal prime correlations and the zeta pole can enter at leading scale. This finding does not rule out that regime.

2. **Fixed n is load-bearing.** No growing-correlation-order theorem is derived. A statistic whose order grows with height could have different combinatorics and conditioning.

3. **Frontier conditioning is outside the theorem.** The result averages the zero divisor through the standard n-level framework; it does not control a hypothetical sparse subsequence with `beta` near an extremal off-critical abscissa.

4. **Radial beta-sensitive observables remain possible.** The theorem does not rule out a deliberately nontranslation-invariant or target-relative statistic that retains individual `beta-1/2` weights instead of using the classical n-level scaling.

5. **Universality is not a Beurling theorem.** The matched control here is across primitive automorphic L-functions, not arbitrary generalized-prime systems. It is nevertheless sufficient to show that the low-support GUE law is not a fingerprint of the ordinary rational-prime exponent lattice alone.

6. **No claim is made that all higher zero correlations are pairwise.** The pairings dominate this theorem's restricted-support main term. Outside that regime genuine off-diagonal arithmetic correlations are expected and are classical objects in their own right.

7. **No Euler product is continued formally.** The arithmetic side enters through the explicit formula for the completed L-function, exactly as in Rudnick--Sarnak. The exponent-vector equation is applied only to finite integer products after that theorem-level bridge.

A falsification would require that the Rudnick--Sarnak product-matching condition fail to translate to exponent-vector conservation, that their low-support leading terms include a non-pairing mixed-prime contribution of the same order, or that their smoothed theorem require RH. None occurs in the cited theorem.

## Consequence for the research line

The generic suggestion “use higher zero correlations to obtain cross-prime information” is now too weak. In the first rigorous fixed-order regime where several explicit-formula prime variables can interact, the exponent lattice contributes only a conservation law whose leading solutions are universal pairings.

A viable higher-order escape from `PL-166`--`PL-167` must therefore leave at least one of the classicalizing assumptions: it must probe beyond the Rudnick--Sarnak Fourier-support range where genuine off-diagonal prime correlations survive, let the correlation order/support grow with height under quantitative control, retain horizontal `beta` information for a near-frontier subsequence, or introduce a target-relative arithmetic observable whose leading invariant is not the universal GUE hierarchy. Merely replacing a first moment by a fixed n-level determinant is not a new RH mechanism.