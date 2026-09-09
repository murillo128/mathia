# Farey-discrepancy source anchors

This file records durable literature dependencies for `research/farey_discrepancy/`. It is an anchor list, not a search history.

## Core criterion

- [`research/prior_art/franel-landau-farey-discrepancy-criterion.md`](../prior_art/franel-landau-farey-discrepancy-criterion.md). Role: Mathia prior-art anchor for RH-equivalent Farey discrepancy bounds and the warning that a geometric redrawing is not new progress.
- [`research/prior_art/dedekind-sum-reciprocity-in-farey-correlations.md`](../prior_art/dedekind-sum-reciprocity-in-farey-correlations.md). Role: neighboring reciprocity/correlation structure relevant when a candidate uses arithmetic information beyond scalar discrepancy.

## Denominator shells and harmonic arithmetic

- Rogelio Tomás García, *New Analytical Formulas for the Rank of Farey Fractions and Estimates of the Local Discrepancy*, Mathematics **13** (2025), 140, DOI `10.3390/math13010140`. Role: prior-art boundary for decomposing Farey local discrepancy into exact-denominator/totient-level contributions and for Mertens-based discrepancy formulas used in `FD-001`.
- Srinivasa Ramanujan, *On Certain Trigonometrical Sums and Their Applications in the Theory of Numbers*, Transactions of the Cambridge Philosophical Society **22** (1918), 259--276. Role: classical source for Ramanujan sums and their divisor arithmetic used to derive the exact shell Fourier and Gram identities in `FD-001`.
- Paolo Codecà and Alberto Perelli, *On the uniform distribution (mod 1) of the Farey fractions and l^p spaces*, Mathematische Annalen **279** (1988), 413--422, DOI `10.1007/BF01456278`. Role: neighboring harmonic-analysis prior-art boundary for Farey uniform distribution and RH-sensitive norm estimates; `FD-001` does not claim that harmonic analysis of Farey fractions is new.

## Absolute-discrepancy endpoint barrier

- François Dress, *Discrépance des suites de Farey*, Journal de théorie des nombres de Bordeaux **11**(2) (1999), 345--367, MR 1745884, Numdam `JTNB_1999__11_2_345_0`. Role: primary source for the exact theorem that the normalized absolute discrepancy of the Farey sequence of order `n` is `1/n`; `FD-010` uses it to classify complete `L^infty` discrepancy as an endpoint-dominated quantity rather than an RH-sensitive replacement for the cumulative Franel statistic.

## Empirical-distribution quadratic identity

- Harald Cramér, *On the Composition of Elementary Errors: Second Paper: Statistical Applications*, Scandinavian Actuarial Journal **1928** (1928), 141--180, DOI `10.1080/03461238.1928.10416872`. Role: classical source boundary for the Cramér--von Mises integrated empirical-distribution quadratic statistic whose ordered-sample formula is specialized to the Farey endpoint grid in `FD-002`.
- Richard von Mises, *Wahrscheinlichkeit, Statistik und Wahrheit*, Springer, Berlin, 1928, DOI `10.1007/978-3-662-36230-3`. Role: classical source boundary for the same integrated-distribution quadratic criterion; `FD-002` proves its required Farey specialization directly and does not import statistical asymptotics.

## GCD-matrix factorization and duality

- H. J. S. Smith, *On the Value of a Certain Arithmetical Determinant*, Proceedings of the London Mathematical Society **s1-7** (1875), 208--213, DOI `10.1112/plms/s1-7.1.208`. Role: classical origin of GCD-matrix determinant factorization; `FD-003` specializes the Smith/Jordan divisor-incidence mechanism to the normalized square-GCD kernel arising from the Franel--Mertens energy.
- Pentti Haukkanen, Wang Jun and Juha Sillanpää, *On Smith's determinant*, Linear Algebra and its Applications **258** (1997), 251--269. Role: modern generalized Smith-matrix factorization/inverse prior-art boundary. `FD-003` derives the required finite factorization directly and does not claim GCD-matrix inversion or meet-matrix algebra as new.

## Möbius floor-quotient recurrence

- Marc Deléglise and Joël Rivat, *Computing the Summation of the Möbius Function*, Experimental Mathematics **5**(4) (1996), 291--295, DOI `10.1080/10586458.1996.10504594`. Role: primary computational prior-art boundary for the classical floor-quotient Möbius recurrence used to compute isolated Mertens values. `FD-005` derives the exact identity `sum_(d<=N) M(floor(N/d))=1` directly and uses it only as an affine compatibility constraint on the Franel--Mertens staircase.

## Prime-density auxiliary input

- Donald J. Newman, *Simple Analytic Proof of the Prime Number Theorem*, The American Mathematical Monthly **87**(9) (1980), 693--696, DOI `10.1080/00029890.1980.11995126`. Role: primary theorem anchor for the prime number theorem used in `FD-006` only to obtain the weighted dyadic-prime monomial Gram lower bound for a fixed family of Jordan-moment constraints. No quantitative zero-free estimate, RH, or RH-equivalent input is imported.
- Ch.-J. de la Vallée Poussin, *Sur la fonction ζ(s) de Riemann et le nombre des nombres premiers inférieurs à une limite donnée*, Mémoires couronnés et autres mémoires publiés par l'Académie royale des sciences, des lettres et des beaux-arts de Belgique, Collection in-8°, **59** (1899), 1--74, DOI `10.3406/marb.1899.2449`. Role: primary source boundary for the classical quantitative prime-number-theorem error arising from the zero-free region. `FD-012` uses only an unconditional bound of the form `vartheta(x)=x+O(x exp(-c sqrt(log x)))` to make dyadic-prime polynomial sampling uniform while the Jordan-moment depth grows; no RH-strength prime-distribution input is imported.

## Ordered Farey index and nonconsecutive determinant algebra

- R. R. Hall and P. Shiu, *The index of a Farey sequence*, Michigan Mathematical Journal **51**(1) (2003), 209--223, DOI `10.1307/mmj/1049832901`. Role: primary source for the classical Farey index `nu=(q_(i-1)+q_(i+1))/q_i` and the exact first-moment identity `sum_i nu_i=3N(Q)-1`; `FD-011` uses these as the prior-art boundary for the raw nearest-neighbor increment Plücker field.
- Alan K. Haynes, *Numerators of differences of nonconsecutive Farey fractions*, International Journal of Number Theory **6**(3) (2010), 655--666, DOI `10.1142/S1793042110003113`, arXiv `0907.0162`. Role: primary source for generalized Farey `k`-indices, their convergent-polynomial representation in finite windows of the ordinary index, and fixed-separation average asymptotics; `FD-011` uses it to classify fixed-lag raw increment minors as already inside the classical Farey-index algebra.

## Expansion rule

Add primary sources only when a canonical finding depends on an exact Farey discrepancy theorem, Möbius bridge, reciprocity identity, or genuinely stronger geometric/multiscale structure.