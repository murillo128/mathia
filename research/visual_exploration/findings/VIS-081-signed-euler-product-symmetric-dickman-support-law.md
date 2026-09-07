# VIS-081 — signed Euler-product support has a classical symmetric Dickman scaling law

## Claim

Use the critical-line notation of `VIS-080`, so

`T_(X,L)=sum_(a,b) [1/(ab)] sinc^2((L/2) log(a/b))`,

where the sum is over ordered coprime positive `X`-smooth integers `a!=b`.

Define

`M_X = prod_(p<=X) (p+1)/(p-1)`.

For every prime `p<=X`, let `K_p` be independent with the symmetric two-sided geometric law

`P(K_p=k) = [(p-1)/(p+1)] p^(-|k|)`, `k in Z`,

and put

`S_X = sum_(p<=X) K_p log p`.

Then the exact signed energy is the kernel average

`T_(X,L) + 1 = M_X E[sinc^2((L/2) S_X)]`.

Moreover,

`P(S_X=0)=1/M_X`,

so the `-1` in this identity removes exactly the zero exponent vector. Mertens' product theorem gives

`M_X ~ [e^(2 gamma)/zeta(2)] (log X)^2`.

The global scaling law of the support is classical. If `D_+` and `D_-` are independent standard Dickman random variables, then

`S_X/log X  ->_d  D_+ - D_-`

as `X->infinity`.

Indeed each `K_p` is exactly a difference

`K_p =_d A_p-B_p`,

where `A_p,B_p` are independent `Geom(1-1/p)` variables. Bhattacharjee--Molchanov's prime-geometric Dickman theorem applies independently to the positive and negative exponent fields. Equivalently, the limit is the signed one-dimensional specialization of their scale-invariant Poisson/Dickman construction, with equal positive and negative directions.

The limiting law is therefore not Gaussian. Its characteristic function is

`E exp(i t (D_+-D_-))`
` = exp(2 integral_0^1 [cos(tu)-1] du/u)`.

In particular its odd cumulants vanish and its even cumulants satisfy

`kappa_(2m)=1/m`.

Thus the variance is `1` and the fourth cumulant is `1/2`.

**Evidence/status:** `EXACT-DERIVED + LITERATURE-IDENTIFIED CLASSICAL DICKMAN LIMIT + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

No shrinking-window local limit, asymptotic for `T_(X,L)` under a joint law `X=X(L)`, sharp cutoff threshold, zeta approximation theorem, or RH consequence is claimed.

## 1. The primitive-ratio weights are a probability law

`VIS-080` reindexed the signed prime-exponent lattice by reduced `X`-smooth ratios. At `sigma=1/2`, an exponent vector `k=(k_p)` has weight

`prod_(p<=X) p^(-|k_p|)`.

The local normalization is

`sum_(k in Z) p^(-|k|)`
` = 1 + 2 sum_(k>=1) p^(-k)`
` = (p+1)/(p-1)`.

Hence the full normalization over finite prime support is exactly `M_X`, and the product probability measure is the stated law of the independent `K_p`.

With

`S_X=sum_(p<=X) K_p log p`,

unique factorization implies

`S_X=0  <=>  K_p=0 for every p<=X`.

Therefore

`P(S_X=0)`
` = prod_(p<=X) (p-1)/(p+1)`
` = 1/M_X`.

Multiplying the kernel expectation by `M_X` restores the unnormalized exponent weights. The zero vector contributes exactly `1`, leaving

`M_X E[sinc^2((L/2)S_X)]-1`
` = sum_(k!=0) prod_(p<=X) p^(-|k_p|) sinc^2((L/2) lambda_k)`
` = T_(X,L)`.

This is an exact probabilistic representation of the complete positive energy, not a sampling approximation.

## 2. The two-sided geometric exponent is a difference of classical prime-geometric exponents

Let `q=1/p`, and let `A_p,B_p` be independent with

`P(A_p=m)=P(B_p=m)=(1-q)q^m`, `m>=0`.

For `k>=0`,

`P(A_p-B_p=k)`
` = sum_(m>=0) (1-q)^2 q^(m+k) q^m`
` = [(1-q)/(1+q)] q^k`.

By symmetry the same formula with `|k|` holds for negative `k`, so

`P(A_p-B_p=k)`
` = [(p-1)/(p+1)] p^(-|k|)`.

Thus the entire signed support field has the exact decomposition

`S_X =_d U_X^+ - U_X^-`,

where

`U_X^+ = sum_(p<=X) A_p log p`,

`U_X^- = sum_(p<=X) B_p log p`,

and the two sums are independent.

This also identifies the finite law with the logarithm of the reduced ratio of two independent reciprocal-weighted `X`-smooth random integers. Any apparent large-scale shape in the signed support distribution must therefore first be compared with two copies of the classical reciprocal-smooth model rather than interpreted as new prime-resonance geometry.

## 3. The normalized support law is a symmetric Dickman difference

Bhattacharjee and Molchanov prove for independent

`A_p ~ Geom(1-1/p)`

that the prime-log sum normalized by the largest prime-log scale converges to the standard Dickman law. Their Theorem 3.6 states, along prime cutoffs `p_n`,

`[1/log p_n] sum_(p<=p_n) A_p log p  ->_d D`.

The same holds independently for the `B_p` field. Therefore the joint characteristic function factors and

`(U_X^+/log X, U_X^-/log X) ->_d (D_+,D_-)`,

with independent limits. Replacing an arbitrary real cutoff `X` by its largest included prime does not alter the logarithmic normalization asymptotically, so

`S_X/log X ->_d D_+-D_-`.

The same paper describes scale-invariant Poisson processes with random directions and the resulting multivariate Dickman family. Superposing the positive and negative unit-intensity prime-log limits gives the equivalent signed picture: total radial intensity `2 du/u` with independent Rademacher direction.

From the standard Poisson representation,

`log E exp(i t D_+) = integral_0^1 (exp(itu)-1) du/u`.

Adding the independent reflected copy gives

`log E exp(i t(D_+-D_-))`
` = 2 integral_0^1 [cos(tu)-1] du/u`.

Expanding at the origin yields `kappa_(2m)=1/m` and zero odd cumulants. In particular, a Gaussian approximation is not the correct global support control: the fourth cumulant survives in the limit.

## 4. The normalization is only logarithm-squared

The exact product can be factored as

`M_X`
` = prod_(p<=X) (1-p^(-2))`
`   prod_(p<=X) (1-p^(-1))^(-2)`.

The first product tends to `1/zeta(2)`, while Mertens' product theorem gives

`prod_(p<=X) (1-p^(-1)) ~ e^(-gamma)/log X`.

Hence

`M_X ~ [e^(2 gamma)/zeta(2)] (log X)^2`.

This scale explains why global weak convergence alone is insufficient for the joint window problem. `T_(X,L)` magnifies the probability mass seen by a sinc-square kernel around `S_X=0` by a factor of order `(log X)^2`, after exactly subtracting the zero atom.

The unresolved information is therefore local, not global: one needs control of the *off-zero* pure-point mass on a shrinking neighborhood of zero whose width depends on `L`.

## Prior-art and novelty assessment

Chinmoy Bhattacharjee and Ilya Molchanov, **Convergence to scale-invariant Poisson processes and applications in Dickman approximation**, *Electronic Journal of Probability* 25 (2020), paper 79, DOI `10.1214/20-EJP482`, is the decisive prior-art boundary. Their Theorem 3.6 treats exactly the one-sided prime model `Geom(1-1/p)` at frequencies `log p` and proves convergence of its normalized sum to the standard Dickman distribution. Their later sections develop the corresponding randomly directed scale-invariant Poisson processes and multivariate Dickman laws.

Régis de la Bretèche and Gérald Tenenbaum, **On strong and almost sure local limit theorems for a probabilistic model of the Dickman distribution**, *Lithuanian Mathematical Journal* 61 (2021), 301--311, DOI `10.1007/s10986-021-09529-6`, proves strong/local limit formulae for a related classical Bernoulli Dickman model. It shows that local Dickman approximation is an established subject, but its lattice model is not the present signed prime-log pure-point law and its theorem is not imported here.

Accordingly, **the Dickman limit itself is not a Mathia discovery**. The Mathia-specific contribution is the exact bridge from the `VIS-080` signed Euler-product energy measure to the difference of two classical prime-geometric Dickman models, together with the resulting falsification boundary: global support histograms, global cumulants, or an apparent non-Gaussian shape cannot be evidence for a new zeta channel.

## Boundary and falsification

Weak convergence of `S_X/log X` controls fixed-scale bounded continuous observables. It does **not** control the shrinking sinc window arising when `L=L(X)` grows, and it does not justify replacing the pure-point distribution near zero by the limiting continuous density.

The exact atom at zero also cannot be ignored. Its probability is `1/M_X`, and it contributes exactly the `1` removed in `T_(X,L)=M_X E[sinc^2((L/2)S_X)]-1`. Any local approximation that smears this atom into the continuous Dickman profile will give the wrong leading bookkeeping.

Falsify the exact probabilistic bridge by finding a prime-local signed exponent weight that differs from the law of `A_p-B_p`, or a nonzero exponent vector with zero log frequency. Falsify the global limit by identifying a hypothesis mismatch with the cited prime-geometric Dickman theorem after the two independent copies and normalization are made explicit.

No statement is made here about whether arithmetic recurrence at scales much finer than `log X` obstructs a local limit.

## Research consequence

`VIS-080` proved that `T_(X(L),L)->0` is impossible unless

`log X(L)/L -> 0`.

The present result closes another tempting shortcut: within or outside that corridor, the *global* shape of the signed support is already classical symmetric Dickman structure. The next decisive test is therefore an atom-separated local limit at the sinc scale for the off-zero law of `S_X` under a predeclared joint regime `X=X(L)`.

If such a local limit holds and the continuous symmetric-Dickman difference has density `g` at zero, the kernel scaling would predict, conditionally rather than as a claim,

`T_(X,L) ~ [2 pi e^(2 gamma) g(0)/zeta(2)] [log X/L]`.

This would match the order of the support-crowding floor from `VIS-080` and make `log X/L` the sharp baseline scale. Proving that local approximation, or showing that fine arithmetic recurrence invalidates it in some subexponential regime, is a separate next research question and is intentionally not executed in this invocation.