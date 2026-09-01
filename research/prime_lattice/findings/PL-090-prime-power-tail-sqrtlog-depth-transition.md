# PL-090 — Prime-power tails have a `sqrt(log X)` depth-population transition

## Claim

The fixed-minimum-depth rank obstruction of `PL-089` extends uniformly to growing exponent depth only below a precise first transition. Let

```text
0<a<b<infinity,
L=log X,
M_k(X)=#{p prime : aX<p^k<=bX},
Q_(X,>=K)={p^k : k>=K, aX<p^k<=bX}.
```

Assume `K=K(X)->infinity` and `K=O(sqrt(L))`. Uniformly for

```text
K<=k<=2K,
```

the prime number theorem with a standard zero-free-region error gives

```text
boxed:
M_k(X)
 =(log(b/a)+o(1)) exp(L/k)/L,
```

where the `o(1)` is uniform over that range.

This produces two distinct depth regimes.

1. If

```text
K=o(sqrt(L)),
```

then

```text
boxed:
sum_(k>K) M_k(X) / M_K(X) ->0.
```

Hence the minimum surviving depth still occupies asymptotically all indices of `Q_(X,>=K)`. The rank argument of `PL-089` therefore remains valid even when the minimum exponent tends to infinity, as long as it grows strictly slower than `sqrt(log X)`.

2. If

```text
K/sqrt(L)->alpha in (0,infinity),
q_alpha=exp(-1/alpha^2),
```

then for every fixed integer `r>=0`,

```text
boxed:
M_(K+r)(X)/M_K(X) -> q_alpha^r,
```

and in fact the whole tail has the asymptotic profile

```text
boxed:
|Q_(X,>=K)|/M_K(X) -> 1/(1-q_alpha),

M_(K+r)(X)/|Q_(X,>=K)|
 ->(1-q_alpha)q_alpha^r.
```

Thus at the first growing-depth transition `K~alpha sqrt(log X)`, the exponent offset `r=k-K` has a genuine geometric population law. In particular the deeper sector has asymptotic mass

```text
q_alpha>0,
```

so it is no longer a rank-`o(N)` perturbation of the minimum-depth block. The fixed-`K` ordinary-bulk no-go of `PL-089` cannot be extended through this scale by dimension counting alone.

More generally, for every fixed `R>=0`, the first `R+1` depth layers carry asymptotic mass

```text
1-q_alpha^(R+1),
```

so the entire critical-depth tail is rank-close, to arbitrary prescribed accuracy, to a **finite adjacent-depth stack**, but not to one depth alone.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-PNT + BOUNDARY/REDIRECT`.

This is not an RH-sensitive mechanism by itself. The transition is forced by ordinary prime density and the deterministic map `p -> p^k`, and therefore fails the line's rational-prime discrimination test whenever a generalized-prime control has the same sufficiently uniform PNT. Its value is that it closes the growing-`K` boundary left open by `PL-089` and isolates the first exponent-depth regime in which cross-depth couplings can contribute nonvanishing ordinary spectral mass.

## Uniform layer count at `k=O(sqrt(log X))`

Put

```text
y_k=exp(L/k)=X^(1/k),
u_k=(aX)^(1/k)=y_k a^(1/k),
v_k=(bX)^(1/k)=y_k b^(1/k),
Delta=log(b/a)>0.
```

For `k->infinity`, uniformly in `k>=K`,

```text
v_k-u_k
 =y_k [b^(1/k)-a^(1/k)]
 =y_k [Delta/k+O_(a,b)(1/k^2)].
```

On the interval `[u_k,v_k]`,

```text
log t=L/k+O_(a,b)(1/k),
```

so

```text
1/log t
 =(k/L)(1+O_(a,b)(1/L)).
```

Consequently

```text
li(v_k)-li(u_k)
 =(Delta+O(1/k)+O(1/L)) y_k/L.
```

A classical de la Vallee Poussin-type PNT error is already much stronger than needed here:

```text
pi(t)=li(t)+O(t exp(-c sqrt(log t)))
```

for some `c>0`. The sharper Vinogradov--Korobov error recorded in `SOURCES.md` for `PL-062` is also more than sufficient. If `K=O(sqrt L)` and `K<=k<=2K`, then

```text
log y_k=L/k >> sqrt(L),
```

up to constants, and therefore the endpoint PNT error divided by the claimed main term is bounded by

```text
O(L exp(-c' L^(1/4)))=o(1)
```

uniformly in that range. This proves

```text
M_k(X)
 =pi(v_k)-pi(u_k)
 =(Delta+o(1)) exp(L/k)/L.
```

The need for a quantitative PNT rather than only `pi(x)~x/log x` is an audit point: the multiplicative shell in the base-prime variable has relative width only `Theta(1/k)`. At `k~sqrt(log X)` the classical zero-free-region error is nevertheless exponentially smaller than that width, so no unproved short-interval prime hypothesis is being inserted.

## Below `sqrt(log X)`, minimum-depth dominance survives

Assume now

```text
K->infinity,
K=o(sqrt L).
```

For `1<=r<=K`, the uniform layer asymptotic gives

```text
M_(K+r)/M_K
 =(1+o(1))
  exp[L/(K+r)-L/K]

 =(1+o(1))
  exp[-L r/(K(K+r))].
```

Since `K+r<=2K`,

```text
L r/(K(K+r))
 >= L r/(2K^2).
```

Thus the whole block `K<k<=2K` is bounded by a geometric series with ratio

```text
exp[-L/(2K^2)] ->0,
```

and its total mass relative to `M_K` tends to zero.

For `k>=2K`, no delicate prime estimate is needed. There are only `O(L)` possible prime-power exponents and

```text
M_k(X)
 <=pi((bX)^(1/k))
 <=(bX)^(1/k)
 <<exp(L/(2K)).
```

Meanwhile

```text
M_K(X) asymp exp(L/K)/L,
```

so

```text
sum_(k>=2K) M_k(X)/M_K(X)
 <<L^2 exp[-L/(2K)]
 ->0.
```

Combining the two ranges proves

```text
sum_(k>K)M_k/M_K->0.
```

Therefore the `PL-089` rank comparison is not merely a fixed-depth phenomenon. Every Hermitian matrix on the tail `Q_(X,>=K)` still has the same weak ordinary empirical spectral limits as its depth-`K` principal block throughout the growing range `K=o(sqrt(log X))`.

## At `K~alpha sqrt(log X)`, the depth profile becomes geometric

Let

```text
K/sqrt L->alpha>0.
```

For fixed `r`,

```text
L/(K+r)-L/K
 =-r L/[K(K+r)]
 ->-r/alpha^2.
```

The uniform layer asymptotic therefore gives

```text
M_(K+r)/M_K
 ->exp(-r/alpha^2)
 =q_alpha^r.
```

To justify summing over all depths, split the tail at `2K`. For `0<=r<=K`, the same exponent identity yields, for all sufficiently large `X`,

```text
M_(K+r)/M_K
 <=C_alpha exp(-c_alpha r),
```

because `L/[K(K+r)]` stays bounded below by a positive constant. This is a summable majorant independent of `X`. Dominated convergence then gives

```text
sum_(r=0)^K M_(K+r)/M_K
 ->sum_(r=0)^infinity q_alpha^r
 =1/(1-q_alpha).
```

The remaining exponents `k>=2K` again satisfy

```text
sum_(k>=2K)M_k/M_K
 <<L^2 exp[-L/(2K)]
 ->0,
```

now because `L/K~sqrt(L)/alpha->infinity`. Hence the geometric series is the entire asymptotic tail, not merely a fixed-offset local approximation.

It follows immediately that

```text
M_(K+r)/|Q_(X,>=K)|
 ->(1-q_alpha)q_alpha^r.
```

The minimum layer has mass `1-q_alpha` and all deeper layers together have mass `q_alpha`. The latter is strictly positive for every finite `alpha>0`.

## Spectral consequence: one-layer rank universality stops exactly here

Let `A_X` be any Hermitian matrix indexed by `Q_(X,>=K)`, and let `H_X^(R)` be its principal block on depths

```text
K,K+1,...,K+R.
```

The same block-rank argument as `PL-087`--`PL-089` gives

```text
sup_y |F_(A_X)(y)-F_(H_X^(R))(y)|
 <=3 *
   #{indices of depth >K+R}/|Q_(X,>=K)|.
```

At the critical depth scale this yields

```text
limsup_(X->infinity)
 sup_y |F_(A_X)(y)-F_(H_X^(R))(y)|
 <=3 q_alpha^(R+1).
```

For `R=0` the omitted fraction tends `q_alpha`, so dimension counting no longer forces the whole tail to share the depth-`K` empirical law. Conversely, by choosing `R` large but fixed, the omitted fraction can be made arbitrarily small. The first unresolved ordinary-bulk object is therefore not an uncontrolled infinite-depth matrix but a finite stack of adjacent exponent layers whose size is set by the desired spectral accuracy.

This statement is purely structural: it does not assert that the cross-depth blocks actually change the limiting spectrum. It says only that the exact no-go mechanism used in `PL-089` has reached its sharp population boundary and that any further collapse must use information about the cross-depth entries, not rank alone.

## Relation to the logarithmic Gram time scales

`PL-088` shows that the isolated depth-`k` block is a prime Gram at base scale

```text
Y_k=X^(1/k)
```

with observation time dilated by `k`. Its own mean-gap interaction horizon is, up to the fixed convention for the constant,

```text
T_crit,k asymp Y_k/log X.
```

At `K~alpha sqrt L`, the same calculation as above gives, for fixed `r`,

```text
Y_(K+r)/Y_K
 ->q_alpha^r,
```

and hence

```text
T_crit,K+r/T_crit,K
 ->q_alpha^r.
```

Thus the same geometric law controls both the population ratios and the relative local-resolution clocks of adjacent depth layers. A finite number of neighboring depths can carry nonvanishing mass while living at observation scales that differ only by fixed factors. This is the first regime in the prime-power filtration where a genuinely cross-depth finite-time Gram analysis is not eliminated in advance by either the single-ray time-dilation identity (`PL-088`) or the vanishing-rank tail argument (`PL-089`).

No RH consequence follows from that fact. Cross-depth correlations would have to be derived and compared against generalized-prime or other matched controls before they could count as arithmetic rigidity.

## Prior-art and novelty audit

The ingredients of the population transition are classical:

- counting one depth is exactly the prime-counting difference
  `pi((bX)^(1/k))-pi((aX)^(1/k))`;
- the quantitative prime number theorem controls this difference uniformly in the present shrinking base-prime shell;
- Riemann/Chebyshev prime-power counting classically decomposes prime-power sums into exponent layers;
- `PL-087`--`PL-089` already use fixed-depth PNT asymptotics and standard rank stability of empirical spectral distributions.

A targeted search around prime-power counting by growing exponent, prime-power exponent distributions, and `sqrt(log x)` depth scalings did not locate a source treating this exact shell-normalized geometric depth profile. That absence is not used as a novelty claim. The displayed transition is an elementary but previously unstored consequence of the quantitative PNT, and its durable role is to settle the explicit growing-`K` boundary in `PL-089`.

The mechanism also fails the strongest line-specific novelty control: any generalized-prime system with an equally uniform `pi_B(y)~y/log y` law on these multiplicative shells produces the same `exp(L/k)` layer hierarchy and the same `sqrt(log X)` transition. Therefore the geometric depth law is a **routing theorem**, not a rational-prime signature.

## Adversarial boundaries

1. **The theorem treats the first transition, not all growing depths.** The uniform PNT argument is stated for `K=O(sqrt(log X))`. For substantially larger `K`, the base-prime shell becomes thinner and the number of primes in one layer eventually ceases to be governed by this elementary uniform estimate.
2. **The critical geometric law is population geometry only.** It does not determine cross-depth Gram entries, a limiting ESD, hard-edge behavior, determinants, or zero-sensitive invariants.
3. **Rank non-negligibility is not evidence of spectral novelty.** At `K~alpha sqrt(log X)` deeper layers can affect a positive fraction of eigenvalues, but they may still reduce to a universal matched-control law after their actual correlations are analyzed.
4. **`K->infinity` is used in the new asymptotic formula.** Fixed `K` remains covered by the sharper constants in `PL-089`; the present `log(b/a)` simplification comes from expanding `a^(1/k),b^(1/k)` for growing `k`.
5. **The shell is fixed multiplicatively in the original variable.** Changing `(aX,bX]` to a shrinking or expanding shell changes the base-prime width and can move the transition.
6. **No analytic continuation is present.** The proof uses only prime counting and finite-dimensional rank geometry. It does not transport an Euler product into the critical strip or single out `Re(s)=1/2`.
7. **The `sqrt(log X)` threshold is not the zeta critical line.** It comes from balancing the adjacent-depth exponent loss `L/K^2` at order one. Interpreting the square root itself as RH-critical would be a category error.

## Consequence for the research line

The ordinary-bulk prime-power filtration now has a sharper phase diagram:

```text
K fixed
    -> minimum depth dominates (`PL-089`);

K->infinity, K=o(sqrt(log X))
    -> minimum depth still dominates (this finding);

K~alpha sqrt(log X)
    -> depth offsets have geometric mass
       (1-q)q^r, q=exp(-1/alpha^2);
    -> one-layer rank reduction fails;
    -> a finite adjacent-depth stack captures
       arbitrarily much ordinary spectral mass.
```

Accordingly, if the prime-power finite-time Gram branch is pursued further at ordinary-bulk level, the first structurally nontrivial target is a **finite cross-depth stack at `K~sqrt(log X)`**, not another fixed depth or fixed-depth tail. Any positive mechanism there must still survive the README's generalized-prime control and must add genuine analytic/global information before being related to RH.