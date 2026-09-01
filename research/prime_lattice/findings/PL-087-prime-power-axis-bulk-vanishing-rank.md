# PL-087 — Prime-power exponent depth is a vanishing-rank sector of the natural von-Mangoldt Gram bulk

## Claim

`PL-086` leaves one important boundary open: on the full von-Mangoldt support, the exponent depth `k` of an axis point `p^k` survives pointwise through

```text
Lambda(p^k)/log(p^k)=1/k.
```

That surviving depth does **not**, however, change the ordinary macroscopic empirical spectral law of the natural finite-time Gram matrix on a fixed multiplicative shell. The reason is not cancellation or a zeta identity; it is a deterministic density obstruction.

Fix

```text
0<a<b<infinity,
Q_X={p^k : p prime, k>=1, aX<p^k<=bX},
P_X={p prime : aX<p<=bX},
R_X=Q_X\P_X,
N_X=|Q_X|, M_X=|P_X|, r_X=|R_X|.
```

For any `T>0`, let

```text
G_(X,T)(m,n)
 =(1/T) integral_0^T exp(i t(log m-log n)) dt
```

and form the naturally prime-scaled von-Mangoldt half-weighted Gram matrix on the whole prime-power axis shell,

```text
A_(X,T)(m,n)
 = X/(log X)^2
   * Lambda(m)Lambda(n)/sqrt(mn)
   * G_(X,T)(m,n),
       m,n in Q_X.
```

Its principal block indexed by `P_X` is exactly the prime matrix `H_(X,T)` of `PL-086`.

Then

```text
r_X
 ~ 2(sqrt(b)-sqrt(a)) sqrt(X)/log X,

M_X
 ~ (b-a) X/log X,
```

so

```text
boxed:
r_X/N_X = O(X^(-1/2)) -> 0.
```

After ordering the prime indices first,

```text
A_(X,T) = [ H_(X,T)   C_X ]
          [ C_X^*      D_X ],
```

and comparison with

```text
A_(X,T)^0 = diag(H_(X,T),0_(r_X))
```

gives

```text
rank(A_(X,T)-A_(X,T)^0) <= 2 r_X.
```

Hence the empirical eigenvalue distribution functions satisfy, uniformly in `T`,

```text
boxed:
sup_y |F_A,X,T(y)-F_H,X,T(y)|
 <= 3 r_X/N_X
 =O(X^(-1/2)).
```

Consequently **every weak bulk spectral limit of the full prime-power-axis Gram is the same as the corresponding prime-only bulk limit**. In particular, under the full local Hardy--Littlewood hierarchy used in `PL-085`, at the prime mean-gap horizon

```text
T_X=cX/log X,
```

the full axis empirical spectral measure converges weakly to exactly the same generic Poisson-sinc macroscopic mixture as the prime block. The higher prime powers cannot restore an RH-sensitive ordinary bulk law merely because their pointwise von-Mangoldt amplitude retains the exponent depth `1/k`.

This conclusion is deliberately only about the **ordinary dimension-normalized weak empirical spectral law**. It does not control `W_2`, high moments, the hard edge, the smallest eigenvalues, raw determinants, depth-conditioned spectra, or any completed Weil quadratic form.

**Evidence/status:** `EXACT-DERIVED + LITERATURE-CONTEXT + DECISIVE-NEGATIVE` for the route

```text
full prime-power axis support
+ Lambda(n)n^(-1/2) amplitudes
+ ordinary dimension-normalized finite-time Gram bulk
    -> new arithmetic spectral law beyond the prime-only bulk.
```

No novelty is claimed for the scarcity of higher prime powers, the prime number theorem, eigenvalue interlacing/rank inequalities, or the von-Mangoldt support. The durable line-specific content is their exact combination with `PL-085`--`PL-086`, which shows that the exponent-depth variable survives at each axis point but is invisible to this particular macroscopic spectral statistic because it occupies vanishing matrix rank.

## Higher prime powers have vanishing density in a fixed shell

Every member of `R_X` has a unique representation `p^k` with prime base `p` and exponent `k>=2`. Thus

```text
r_X
 = sum_(k>=2)
   [pi((bX)^(1/k))-pi((aX)^(1/k))],
```

with only `k<=log_2(bX)` contributing.

The square layer is dominant. By the prime number theorem,

```text
pi(sqrt(bX))-pi(sqrt(aX))
 ~ 2(sqrt(b)-sqrt(a)) sqrt(X)/log X.
```

For `k>=3`, the elementary bound

```text
pi((bX)^(1/k)) <= (bX)^(1/k) <= (bX)^(1/3)
```

and the `O(log X)` number of possible exponents give

```text
sum_(k>=3) pi((bX)^(1/k))
 =O(X^(1/3) log X)
 =o(sqrt(X)/log X).
```

Therefore

```text
r_X
 ~ 2(sqrt(b)-sqrt(a)) sqrt(X)/log X.
```

Meanwhile

```text
M_X
 =pi(bX)-pi(aX)
 ~ (b-a)X/log X.
```

Hence

```text
r_X/M_X
 ~ [2(sqrt(b)-sqrt(a))/(b-a)] X^(-1/2),
```

and `N_X=M_X+r_X` has the same leading order as `M_X`.

This is the matrix analogue of the classical Chebyshev distinction between prime-only and prime-power counting: higher prime powers are indispensable to the exact von-Mangoldt/explicit-formula object but are lower-order in ordinary macroscopic counting.

## Exponent depth survives pointwise but not in population mass

For an axis point

```text
n=p^k=xX,
```

the normalized Gram amplitude is

```text
w_X(p^k)
 =sqrt(X/p^k) * Lambda(p^k)/log X

 =sqrt(X/n) * (1/k) * log n/log X.
```

Uniformly for `n in (aX,bX]`,

```text
log n/log X=1+O_(a,b)(1/log X),
```

so at fixed depth `k`,

```text
w_X(p^k)
 =(1+o(1)) /(k sqrt(x)).
```

Thus the `1/k` exponent-depth information identified in `PL-086` is genuine and order one **per higher-power point**. The negative result does not arise because the weights themselves become scalar, as they did on the prime layer. It arises because all `k>=2` layers together contain only `o(N_X)` points.

The diagonal makes the distinction especially transparent:

```text
A_(X,T)(p^k,p^k)
 = X/p^k * (log p/log X)^2
 = X/n * (1/k^2)(log n/log X)^2.
```

Hence, for a constant depending only on the fixed shell,

```text
0 <= A_(X,T)(p^k,p^k) <= C_(a,b)/k^2,
```

and therefore

```text
Tr(A_(X,T))-Tr(H_(X,T))
 =O_(a,b)(r_X).
```

After normalization by `N_X~X/log X`, the extra diagonal spectral mass is `O(X^(-1/2))`. The first empirical moment therefore also agrees asymptotically with the prime block.

## The rank obstruction is independent of time scale

Order `Q_X` so that the primes come first. The full matrix has block form

```text
A=[H C]
  [C* D],
```

where the lower block has size `r_X`. Set

```text
A^0=[H 0]
    [0 0].
```

Then

```text
A-A^0=[0 C]
        [C* D].
```

The top component of the image lies in the column space of `C`, of dimension at most `r_X`, while the bottom component lies in an `r_X`-dimensional coordinate space. Thus

```text
rank(A-A^0)<=2r_X.
```

For Hermitian matrices of common size `N`, the standard rank/interlacing inequality gives

```text
sup_y |F_B(y)-F_C(y)|
 <= rank(B-C)/N.
```

Applying it to `A` and `A^0`,

```text
sup_y |F_A(y)-F_(A^0)(y)|
 <=2r_X/N_X.
```

But

```text
mu_(A^0)
 =(M_X/N_X) mu_H +(r_X/N_X) delta_0,
```

so

```text
sup_y |F_(A^0)(y)-F_H(y)|
 <=r_X/N_X.
```

The triangle inequality yields the displayed `3r_X/N_X` bound.

Nothing in this proof uses the size of an off-diagonal entry, a prime-pair theorem, a zero-free region, or the observation horizon. It therefore holds **uniformly for every `T>0`**. Even exceptionally coherent cross-couplings between primes and prime powers can move only a vanishing fraction of the eigenvalues in the dimension-normalized distribution.

## Consequence at the critical prime horizon

At

```text
T_X=cX/log X,
```

`PL-085` shows, under the full local Hardy--Littlewood hierarchy, that the unweighted prime-support Gram has a deterministic Poisson-sinc bulk law, and `PL-086` shows that the prime-only von-Mangoldt half-weight has the same bulk law up to the deterministic macroscopic envelope `X/p`.

The rank estimate now transfers that **weak** limit immediately to the full prime-power axis matrix:

```text
mu_(A_(X,T_X))
   => same Poisson-sinc envelope mixture as mu_(H_(X,T_X)).
```

This transfer itself is unconditional; only the identification of the prime-block limit with the Poisson law inherits the Hardy--Littlewood hierarchy.

The distinction between weak convergence and `W_2` is essential. A vanishing-rank sector may contain a small number of very large or very small eigenvalues. Rank control alone therefore cannot transport second moments, high moments, extreme-eigenvalue asymptotics, or logarithmic statistics.

## Why this does not classicalize away the prime-power axis

`PL-013` establishes that the completed Weil explicit formula uses exactly the prime-power axis skeleton and that recent self-adjoint Weil constructions genuinely depend on that completed object. The present finding does not say higher powers are irrelevant to zeta. It says something much narrower:

```text
prime-power axis depth
    + ordinary counting measure on a macroscopic shell
    + empirical Gram bulk
```

forgets the higher-depth sector because the spectral statistic weights each matrix index equally and the `k>=2` indices have vanishing density.

The completed explicit formula does **not** use that statistic. It sums the von-Mangoldt weights in a distributional/completed identity and can retain lower-density prime-power contributions at the scale relevant to its test function. There is therefore no contradiction between the present bulk no-go and the importance of prime powers in Weil's formula.

## Prior-art and novelty audit

The ingredients are classical:

- `Lambda(n)` is supported exactly on prime powers;
- higher prime powers form a lower-order subset of the prime-power counting function, with prime squares giving the leading correction to prime counting;
- Hermitian empirical spectral distributions are stable under perturbations of rank `o(N)`;
- `PL-013` already identifies the prime-power axis as the non-archimedean support of the completed Weil route;
- `PL-085`--`PL-086` already classify the support-only and prime-weighted critical bulk, subject to their stated Hardy--Littlewood input.

A targeted literature search around prime-power/von-Mangoldt Gram matrices, empirical spectral distributions, and low-rank prime-power corrections did not locate an external source asserting this exact finite-time axis-shell reduction. That absence is not used as a novelty claim. The result is stored as a line-specific **obstruction** obtained by combining classical sparsity with a standard rank argument.

The matched-control lesson is also negative: vanishing-rank insensitivity is generic matrix geometry, not a rational-prime-specific phenomenon. A spectral statistic that is expected to distinguish the ordinary zeta problem must deliberately retain the rare higher-depth sector rather than average it away.

## Adversarial boundaries

1. **Only ordinary empirical bulk is closed.** A rank-`o(N)` perturbation can alter outliers, the hard edge, or a determinant substantially. No statement about those observables follows from the rank bound.
2. **`W_2` is not transferred.** The rank estimate controls distribution functions/weak limits, not the second moment of the rare sector. The `W_2` theorem of `PL-085` for the prime block therefore becomes only a weak-limit statement for the full axis without further estimates.
3. **Equal weighting of indices is essential.** A depth-conditioned empirical law, a measure assigning nonvanishing mass separately to every `k`-layer, or an explicit rescaling of the rare sector is a different observable and requires its own audit.
4. **The shell is fixed multiplicatively.** The density comparison uses `aX<n<=bX` with fixed positive `a,b`. Shrinking windows or depth-dependent windows can alter the population ratios.
5. **The normalization is the prime-scale half-weight normalization.** A construction that amplifies higher powers by a factor growing like their inverse density can evade this particular no-go, but such amplification must be canonically justified and stress-tested against generic controls.
6. **Completed Weil forms remain outside the conclusion.** Their arithmetic term is not an ordinary dimension-normalized Gram ESD and already belongs to the classical RH-equivalent explicit-formula route of `PL-013`.
7. **Rare-sector spectral statistics remain open.** Schur complements, smallest singular values/eigenvalues, normalized `log det`, outlier processes, or target-relative observables could in principle retain the higher-power layers. The present result says only that a new mechanism must live in such a non-bulk statistic if it wants to exploit exponent depth.
8. **No analytic continuation is used.** Every matrix identity here is finite-dimensional; the only asymptotic arithmetic input for the density ratio is the prime number theorem. Nothing here transports the Euler product into the critical strip.

## Consequence for the prime-lattice search

`PL-086` showed that on prime support the von-Mangoldt coefficient itself becomes asymptotically deterministic, while pointing out that the axis depth `k` survives on `p^k`. The present result closes the most immediate attempt to recover that missing depth by simply restoring all prime powers to the same bulk Gram:

```text
prime layer k=1
   -> macroscopic population X/log X;

higher axis layers k>=2
   -> genuine 1/k amplitudes
   -> only sqrt(X)/log X total population;

ordinary empirical Gram spectrum
   -> higher-depth sector has vanishing rank fraction
   -> same weak bulk as k=1.
```

Accordingly, the productive residual target is no longer the ordinary full-axis ESD. A viable use of exponent depth must **upweight or condition on the rare axis layers, or use a non-bulk observable** such as a Schur complement, hard-edge statistic, relative determinant, target-relative pairing, or the already-completed Weil form. Any such choice must then explain why its normalization is forced by the arithmetic rather than chosen merely to magnify a vanishing sector.