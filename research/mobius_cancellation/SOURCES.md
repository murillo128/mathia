# Sources

## MC-S1 — Matomäki and Radziwiłł, multiplicative functions in short intervals

Kaisa Matomäki and Maksym Radziwiłł, *Multiplicative functions in short intervals*, Annals of Mathematics 183 (2016), 1015–1056. DOI: https://doi.org/10.4007/annals.2016.183.3.6. arXiv: https://arxiv.org/abs/1501.04585.

Role: landmark almost-all short-interval theorem. In particular, for the Möbius function it establishes cancellation in almost all intervals `[x,x+psi(x)]` for any `psi(x) -> infinity`, providing the qualitative local-cancellation baseline for this line.

## MC-S2 — Matomäki, Radziwiłł, Shao, Tao and Teräväinen, almost-all higher uniformity

Kaisa Matomäki, Maksym Radziwiłł, Xuancheng Shao, Terence Tao and Joni Teräväinen, *Higher uniformity of arithmetic functions in short intervals II. Almost all intervals*, Inventiones mathematicae 244 (2026), 967–1091. DOI: https://doi.org/10.1007/s00222-026-01408-6. arXiv v2: https://arxiv.org/abs/2411.05770v2.

Role: quantitative almost-all input used in `MC-001`. Theorem 1.1(i), specialized to the trivial nilsequence, gives for fixed `A>0` and `X^(1/3+epsilon) <= H <= X^(1-epsilon)` a bound `|sum_{x<n<=x+H} mu(n)| <= H/log^A X` outside an exceptional set of measure `O(X/log^A X)` (with fixed auxiliary complexity parameters). The paper also records the broader short-interval Möbius context and earlier qualitative/quantitative variants.

## MC-S3 — Leong, asymptotic unconditional Mertens bound

Nicol Leong, *On some effective results involving zeros of the Riemann zeta function*, Bulletin of the Australian Mathematical Society 111 (2025), 563–565. DOI: https://doi.org/10.1017/S0004972725000188.

Role: comparison baseline for `MC-001` and `MC-002`. The article records an effective Korobov–Vinogradov consequence

`M(x) << x exp(-c (log x)^(3/5) (log log x)^(-1/5))`

for some `c>0`, and identifies this shape as the asymptotically strongest known unconditional estimate for the Mertens function.

## MC-S4 — Granville and Soundararajan, decay of mean values

Andrew Granville and K. Soundararajan, *Decay of Mean Values of Multiplicative Functions*, Canadian Journal of Mathematics 55 (2003), no. 6, 1191–1230. DOI: https://doi.org/10.4153/CJM-2003-047-0. arXiv: https://arxiv.org/abs/math/9911246.

Role: primary pretentious/Halász mean-value anchor for `MC-002`. The paper studies quantitative bounds for `(1/x) sum_{n<=x} f(n)` for `1`-bounded multiplicative `f` in terms of the prime-harmonic quantity `M = min_y sum_{p<=x}(1-Re(f(p)p^{-iy}))/p`, and records the standard `(1+M)e^{-M}` scale.

## MC-S5 — Granville and Mangerel, explicit modern Halász formulation

Andrew Granville and Alexander P. Mangerel, *Three conjectures about character sums*, Mathematische Zeitschrift 305 (2023), article 49. DOI: https://doi.org/10.1007/s00209-023-03374-8.

Role: explicit theorem statements used in `MC-002`. Section 3 defines the pretentious distance and states Halász's estimate `sum_{n<=x} f(n) << x(1+M)e^{-M}+x/T` for `M=min_{|t|<=T} D(f,n^{it};x)^2` and `1<=T<=log x`. The introduction also records the Hall–Tenenbaum real-valued bound `sum_{n<=x} f(n) << x exp(-tau D(f,1;x)^2)` with `tau=0.3286...`, together with an essentially sharp example for that form of estimate.

## MC-S6 — Rosser and Schoenfeld, reciprocal-prime mass

J. Barkley Rosser and Lowell Schoenfeld, *Approximate formulas for some functions of prime numbers*, Illinois Journal of Mathematics 6 (1962), no. 1, 64–94. DOI: https://doi.org/10.1215/ijm/1255631807.

Role: classical explicit anchor for the prime reciprocal sum used in `MC-002`. In particular, Mertens' second theorem gives `sum_{p<=x} 1/p = log log x + B_1 + o(1)`, so every standard pretentious distance accumulated with weight `1/p` has only `O(log log x)` total prime mass at scale `x`.

## MC-S7 — Jung and Lemke Oliver, pretentious detection of power cancellation

Junehyuk Jung and Robert J. Lemke Oliver, *Pretentiously detecting power cancellation*, Mathematical Proceedings of the Cambridge Philosophical Society 154 (2013), no. 3, 481–498. DOI: https://doi.org/10.1017/S0305004112000655. arXiv: https://arxiv.org/abs/1111.1921.

Role: primary source for `MC-003` and for the adversarial clue that motivated it. The paper defines the convolution quantity `H_beta(f,g)`, strong/total `beta`-pretentiousness, prime-power-sensitive distances, and transfer theorems preserving power cancellation. Theorem 1.1 gives `S_g(x) << x^max(alpha,beta)` when `S_f(x) << x^alpha` and the functions are strongly `beta`-pretentious; Theorems 1.2–1.5 analyze related distances and show explicitly why prime-only pretentiousness can fail to detect the desired power-cancellation scale.

## MC-S8 — Humphries, Liouville summatory bounds and RH equivalence

Peter Humphries, *The distribution of weighted sums of the Liouville function and Pólya's conjecture*, Journal of Number Theory 133 (2013), no. 2, 545–582. DOI: https://doi.org/10.1016/j.jnt.2012.08.011. arXiv: https://arxiv.org/abs/1108.1524.

Role: Liouville comparison baseline for `MC-003`. The paper records the classical equivalence `RH iff L(x)=O_epsilon(x^(1/2+epsilon))` and, in Theorem 2.1 at weight zero, the unconditional Korobov–Vinogradov-shaped estimate `L(x) << x exp(-c (log x)^(3/5) (log log x)^(-1/5))`. Thus the natural Liouville comparator supplies no fixed unconditional exponent below `1` to feed into a power-cancellation transfer theorem.

## MC-S9 — DLMF divisor identity for Liouville

NIST Digital Library of Mathematical Functions, §27.6, *Divisor Sums*, equation 27.6.1; notes cite Apostol, *Introduction to Analytic Number Theory* (1976), Chapter 2. https://dlmf.nist.gov/27.6.

Role: authoritative classical anchor for the square-divisor identity used in `MC-003`. DLMF records `sum_{d|n} lambda(d)=1` when `n` is a square and `0` otherwise. Möbius/Dirichlet inversion yields `lambda(n)=sum_{d^2|n} mu(n/d^2)`, from which the exact summatory square-convolution relation follows.

## MC-S10 — Shi, Chowla sequences and independent random constructions

Ruxi Shi, *Construction of some Chowla sequences*, Monatshefte für Mathematik 194 (2021), 193–224. DOI: https://doi.org/10.1007/s00605-020-01448-x.

Role: exact sequence-theoretic anchor for `MC-004`. Definition 3.3 gives the finite-index Chowla property; for `{-1,0,1}` sequences it is equivalent to the usual Chowla condition. Proposition 5.7 states that an independent, not necessarily identically distributed, sequence in `S^1 union {0}` is almost surely Chowla when the nontrivial index moments vanish eventually. This applies to the support-matched random base `mu(n)^2 epsilon_n` used in `MC-004`.

## MC-S11 — Pincus and Singer, slow bias under qualitative normality

Steve Pincus and Burton H. Singer, *A zoo of computable binary normal sequences*, Proceedings of the National Academy of Sciences 109 (2012), no. 47, 19145–19150. DOI: https://doi.org/10.1073/pnas.1215998109.

Role: adjacent prior art for the perturbative obstruction in `MC-004`. The paper records that changing `o(N)` entries of a binary normal sequence preserves normality (Theorem Pr-4) and constructs normal sequences with arbitrarily slow prescribed decay of one-symbol bias. It therefore supplies a close symbolic-dynamics precedent for the principle that qualitative finite-pattern equidistribution does not control the rate of an anchored partial sum. `MC-004` uses a separate support-matched Chowla construction rather than claiming this normality result as arithmetic evidence.

## MC-S12 — Montgomery and Vaughan, square-free counting

Hugh L. Montgomery and Robert C. Vaughan, *Multiplicative Number Theory I: Classical Theory*, Cambridge Studies in Advanced Mathematics 97, Cambridge University Press (2007), Chapter 6, Exercise 19. ISBN 9780521849036; chapter DOI: https://doi.org/10.1017/CBO9780511618314.008.

Role: classical square-free counting anchor for `MC-004`. The exercise records `Q(x)=(6/pi^2)x+R(x)` for the number of square-free integers and derives an error stronger than `O(sqrt(x))`. The weaker elementary form `Q(x)=(6/pi^2)x+O(sqrt(x))` is sufficient to show that an interval of length `x/log x` contains asymptotically `(6/pi^2)x/log x` square-free integers.

## MC-S13 — Matomäki, Radziwiłł and Tao, averaged Chowla

Kaisa Matomäki, Maksym Radziwiłł and Terence Tao, *An averaged form of Chowla's conjecture*, Algebra & Number Theory 9 (2015), no. 9, 2167–2196. DOI: https://doi.org/10.2140/ant.2015.9.2167. arXiv: https://arxiv.org/abs/1503.05121.

Role: arithmetic comparison boundary for `MC-004`. The paper proves Chowla-type correlations after averaging over shifts growing with `X`, with quantitative decay roughly `log log H / log H`, and extends the method to bounded multiplicative functions including Möbius. This is materially stronger information than merely knowing every fixed-shift qualitative correlation tends to zero, so `MC-004` does not treat the modern averaged theorem as covered by its no-go.

## MC-S14 — Granville and Koukoulopoulos, Landau–Selberg–Delange from prime averages

Andrew Granville and Dimitris Koukoulopoulos, *Beyond the LSD method for the partial sums of multiplicative functions*, Ramanujan Journal 49 (2019), no. 2, 287–319. DOI: https://doi.org/10.1007/s11139-018-0119-3. arXiv: https://arxiv.org/abs/1710.01389.

Role: primary asymptotic-transfer theorem for `MC-005`. Theorem 1 starts from a prime-value average `sum_{p<=x} f(p) log p = alpha x + O(x/log^A x)` for a divisor-bounded multiplicative function and gives the corresponding Landau–Selberg–Delange expansion. Its leading coefficient is the Euler product `prod_p (1+f(p)/p+f(p^2)/p^2+...)(1-1/p)^alpha`. Applied to the explicit square-free-supported residue-class sign family in `MC-005`, it gives a positive main term of order `x(log x)^(alpha-1)` without importing zero information near the critical line.

## MC-S15 — Montgomery and Vaughan, primes in arithmetic progressions

Hugh L. Montgomery and Robert C. Vaughan, *Multiplicative Number Theory I: Classical Theory*, Cambridge Studies in Advanced Mathematics 97, Cambridge University Press (2007), Chapters 4 and 11, *Primes in arithmetic progressions I/II*. Chapter 4 DOI: https://doi.org/10.1017/CBO9780511618314.006.

Role: classical prime-number-theorem-in-arithmetic-progressions anchor for `MC-005`. For each fixed modulus `q`, weighted primes are equidistributed among the reduced residue classes with an error stronger than any fixed inverse power of `log x`. This supplies the prime-average hypothesis for the explicit residue-class sign function used there.

## MC-S16 — Klurman, Mangerel, Pohoata and Teräväinen, square-free-supported multiplicative discrepancy

Oleksiy Klurman, Alexander P. Mangerel, Cosmin Pohoata and Joni Teräväinen, *Multiplicative functions that are close to their mean*, Transactions of the American Mathematical Society 374 (2021), no. 11, 7967–7990. DOI: https://doi.org/10.1090/tran/8427. arXiv: https://arxiv.org/abs/1911.06265.

Role: direct adjacent prior art for `MC-005`. Theorem 1.1 proves that for every multiplicative `g:N->{-1,+1}`, the square-free-supported sequence `mu^2 g` has unbounded partial sums. This confirms Aymone's square-free discrepancy conjecture and establishes that the exact-support multiplicative comparator class itself is already a studied object. `MC-005` uses a particular residue-biased member of this class for which standard Selberg–Delange theory yields the much larger explicit logarithmic-order asymptotic.

## MC-S17 — Venturini, auxiliary multiplicative Dirichlet series and zeta nonvanishing

Sergio Venturini, *Non vanishing of Dirichlet series of completely multiplicative functions*, Rivista di Matematica della Università di Parma 11 (2020), no. 1, 153–180. Journal page: https://www.rivmat.unipr.it/vols/2020-11-1/08-venturini.html. Repository record: https://hdl.handle.net/11585/729849.

Role: adjacent prior art for `MC-008`. Venturini proves that for a bounded completely multiplicative coefficient sequence, holomorphic continuation of its Dirichlet series to `Re(s)>1-delta` together with `L(1)=0` forces that half-plane to be zero-free for the Riemann zeta function. The hypotheses and mechanism are not the same as the explicit non-completely-multiplicative comparator in `MC-008`, but the paper establishes the broader prior-art principle that analyticity of an auxiliary multiplicative Dirichlet series can constrain the zeta zero divisor.

## MC-S18 — DLMF alternating-zeta prefactor

NIST Digital Library of Mathematical Functions, §25.2(ii), equation 25.2.3, *Riemann Zeta Function: Definition and Expansions*. https://dlmf.nist.gov/25.2.E3.

Role: authoritative classical anchor for `MC-008`. DLMF records `zeta(s)=eta(s)/(1-2^(1-s))` for `Re(s)>0`, equivalently `eta(s)=(1-2^(1-s))zeta(s)`. The factor `1-2^(1-s)` occurring in the explicit 2-adic transfer kernel of `MC-008` is therefore standard; its zeros lie on `Re(s)=1`, so no novelty is claimed for that factor or its zero set.