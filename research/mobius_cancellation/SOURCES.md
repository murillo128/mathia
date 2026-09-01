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