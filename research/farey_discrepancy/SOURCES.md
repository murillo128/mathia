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

## Möbius cancellation auxiliary input

- H. Davenport, *On Some Infinite Series Involving Arithmetical Functions (II)*, The Quarterly Journal of Mathematics **os-8** (1937), 313--320, DOI `10.1093/qmath/os-8.1.313`. Role: primary source for the classical log-power saving in linear exponential sums weighted by `mu`; the zero-frequency specialization gives `M(x) <<_A x/log^A x` for every fixed `A`. `FD-030` uses only this unconditional cancellation, plus partial summation, to make the physical Mertens staircase negligible at scale `H/log^4 H` and to prove decay of a positive weighted lower-horizon Mertens combination in the square-GCD norm.

## Mertens growth and zeta-zero frontier

- E. C. Titchmarsh, revised by D. R. Heath-Brown, *The Theory of the Riemann Zeta-Function*, 2nd ed., Clarendon Press/Oxford University Press, 1986, Section 14.25, especially Theorem 14.25(C). Role: standard literature anchor for the Littlewood criterion `RH iff M(x)=O_epsilon(x^(1/2+epsilon))` and the corresponding zero-free-half-plane/power-growth argument. `FD-046` combines that classical frontier with an exact invertible floor-harmonic transform to transfer the zeta-zero power exponent to the quotient-shell source and to every fixed Jordan row; no novelty is claimed for the Mertens criterion itself.

## Prime-density auxiliary input

- Donald J. Newman, *Simple Analytic Proof of the Prime Number Theorem*, The American Mathematical Monthly **87**(9) (1980), 693--696, DOI `10.1080/00029890.1980.11995126`. Role: primary theorem anchor for the prime number theorem used in `FD-006` only to obtain the weighted dyadic-prime monomial Gram lower bound for a fixed family of Jordan-moment constraints. No quantitative zero-free estimate, RH, or RH-equivalent input is imported.
- Ch.-J. de la Vallée Poussin, *Sur la fonction ζ(s) de Riemann et le nombre des nombres premiers inférieurs à une limite donnée*, Mémoires couronnés et autres mémoires publiés par l'Académie royale des sciences, des lettres et des beaux-arts de Belgique, Collection in-8°, **59** (1899), 1--74, DOI `10.3406/marb.1899.2449`. Role: primary source boundary for the classical quantitative prime-number-theorem error arising from the zero-free region. `FD-012` uses only an unconditional bound of the form `vartheta(x)=x+O(x exp(-c sqrt(log x)))` to make dyadic-prime polynomial sampling uniform while the Jordan-moment depth grows; no RH-strength prime-distribution input is imported.

## Critical-line zero auxiliary input

- G. H. Hardy, *Sur les zéros de la fonction ζ(s) de Riemann*, Comptes rendus hebdomadaires des séances de l'Académie des sciences **158** (1914), 1012--1014. Role: primary source for Hardy's theorem that infinitely many nontrivial zeros of `zeta(s)` lie on `Re(s)=1/2`. `FD-033` uses only the existence of one such zero to force divergence of the critical Mellin square norm attached to the coefficient summatory function with Dirichlet series `zeta(s+1)/zeta(s)`; no RH assumption or zero-density input is used.

## Squarefree-density zero-free auxiliary input

- Arnold Walfisz, *Weylsche Exponentialsummen in der neueren Zahlentheorie*, Mathematische Forschungsberichte **15**, VEB Deutscher Verlag der Wissenschaften, Berlin, 1963, Satz §5.6.1. Role: primary source for the classical unconditional squarefree-counting estimate `Q(x)=x/zeta(2)+O(sqrt(x) exp(-c (log x)^(3/5)(log log x)^(-1/5)))`. `FD-045` transfers this estimate through an absolutely convergent weighted Jordan Euler factor, sharpening the centered nonsquarefree summatory law and extending the finite-row Mellin settling window past the square-root frequency scale without assuming RH.

## Zeta one-line frequency auxiliary input

- Kevin Ford, *Vinogradov's Integral and Bounds for the Riemann Zeta Function*, Proceedings of the London Mathematical Society **85**(3) (2002), 565--633, DOI `10.1112/S0024611502013655`. Role: primary source for the Vinogradov--Korobov bound `|zeta(sigma+it)| << |t|^(B(1-sigma)^(3/2)) log^(2/3)|t|`; `FD-044` uses only its `sigma=1` specialization after exact cancellation of the centered Jordan-density pole, obtaining a `log^(2/3)` frequency cost for sub-square-root finite-row windows. No RH, zero-density, or zero-spacing input is imported.

## Ordered Farey index and nonconsecutive determinant algebra

- R. R. Hall and P. Shiu, *The index of a Farey sequence*, Michigan Mathematical Journal **51**(1) (2003), 209--223, DOI `10.1307/mmj/1049832901`. Role: primary source for the classical Farey index `nu=(q_(i-1)+q_(i+1))/q_i` and the exact first-moment identity `sum_i nu_i=3N(Q)-1`; `FD-011` uses these as the prior-art boundary for the raw nearest-neighbor increment Plücker field.
- Alan K. Haynes, *Numerators of differences of nonconsecutive Farey fractions*, International Journal of Number Theory **6**(3) (2010), 655--666, DOI `10.1142/S1793042110003113`, arXiv `0907.0162`. Role: primary source for generalized Farey `k`-indices, their convergent-polynomial representation in finite windows of the ordinary index, and fixed-separation average asymptotics; `FD-011` uses it to classify fixed-lag raw increment minors as already inside the classical Farey-index algebra.

## Local gap-order and Markov-type controls

- Volker Augustin, Florin P. Boca, Cristian Cobeli and Alexandru Zaharescu, *The h-spacing distribution between Farey points*, Mathematical Proceedings of the Cambridge Philosophical Society **131**(1) (2001), 23--38, DOI `10.1017/S0305004101005187`. Role: primary prior-art boundary for fixed-`h` local Farey spacing distributions. `FD-013` does not claim local Farey gap statistics are new; it isolates what a complete first-order local gap inventory cannot coerce about cumulative rank-grid discrepancy.
- Philippe Jacquet, Charles Knessl and Wojciech Szpankowski, *Counting Markov Types*, DMTCS Proceedings vol. AM, AofA'10 (2010), DOI `10.46298/dmtcs.2768`. Role: prior-art boundary for first-order Markov-type terminology as exact adjacent-pair frequency data. `FD-013` derives its binary matched-control pair directly and does not import Markov-type enumeration estimates.
- Rogelio Tomás García, *A General Lower Bound for Average Local Discrepancy and an Application to the Farey Sequence*, Mathematics **14** (2026), 2543, DOI `10.3390/math14142543`. Role: current prior-art boundary for the effect of gap ordering and same-gap permutation families on average local Farey discrepancy. `FD-013` studies a different exact quadratic control in which reflection and all adjacent ordered gap-pair counts are additionally fixed.

## Extremal set-theory auxiliary input

- Emanuel Sperner, *Ein Satz über Untermengen einer endlichen Menge*, Mathematische Zeitschrift **27** (1928), 544--548, EuDML `167993`. Role: primary source for Sperner's theorem that an antichain in the Boolean lattice has size at most the central binomial coefficient. `FD-015` applies this classical bound only after deriving a Farey--Mertens GCD-duality non-saturation relation on comparable squarefree divisor-lattice horizons.

## Expansion rule

Add primary sources only when a canonical finding depends on an exact Farey discrepancy theorem, Möbius bridge, reciprocity identity, or genuinely stronger geometric/multiscale structure.