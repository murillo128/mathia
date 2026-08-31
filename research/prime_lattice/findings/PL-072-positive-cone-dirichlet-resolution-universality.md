# PL-072 — Positive-cone finite-horizon resolution has the classical Dirichlet-polynomial `N ~ T` threshold

## Claim

The one-sided positive exponent semigroup left outside `PL-071` does restore an exact finite-horizon rigidity that the signed prime-character group does not have, but that rigidity is completely governed by the classical mean-value geometry of Dirichlet polynomials and does not supply a zeta-specific RH mechanism.

For `T>0` put

```text
nu_n^(T)(t)=T^(-1/2) n^(-it),
0 <= t <= T,
1 <= n <= N.
```

These are precisely the positive exponent-lattice characters with energies

```text
lambda_n=log n=<v(n),(log p)_p>.
```

Let `G_(T,N)` be their Gram operator on `ell^2({1,...,N})`. The Montgomery--Vaughan mean-value theorem gives the uniform quadratic-form estimate

```text
||G_(T,N)-I|| <= C N/T
```

for an absolute constant `C`. Hence

```text
N=o(T)
    -> G_(T,N) -> I in operator norm.
```

So below the Fourier-resolution scale `N~T`, the entire positive integer cone up to energy `log N` is asymptotically orthonormal on `[0,T]`; there is no hidden collective prime-lattice resonance to exploit there.

At the opposite extreme, if `N/T -> infinity`, the adjacent top characters `N^(-it)` and `(N-1)^(-it)` become asymptotically collinear because

```text
T log(N/(N-1)) ~ T/N -> 0.
```

At the transition itself, take `n_T/T -> x>0` and fixed integer offsets `j,k`. Then

```text
<nu_(n_T+j)^(T),nu_(n_T+k)^(T)>
 -> exp(i (k-j)/(2x))
    sinc((k-j)/(2x)),
```

with `sinc(y)=sin(y)/y` (up to the harmless conjugate phase convention for the inner product). Thus the local critical Gram geometry is a universal sinc kernel coming only from

```text
log(n+k)-log(n+j) ~ (k-j)/n.
```

Prime factorization, the Boolean square-free sector, zeta zeros, and analytic continuation do not enter.

The same threshold appears from fixed-target correlations. For a fixed real frequency `mu`, the positive spectrum `{log n:n>=1}` is locally discrete. Unless `mu=log n_0` for an integer `n_0`,

```text
d_+(mu)=inf_(n>=1) |mu-log n| > 0,
```

and therefore

```text
sup_n |(1/T) integral_0^T exp(i(mu-log n)t) dt|
    <= 2/(T d_+(mu))
    -> 0.
```

So the signed `log Q_(>0)` shadowing theorem of `PL-071` genuinely fails for a fixed target when inverse prime directions are forbidden. But this one-sided rigidity is only discreteness. Once the target energy moves into the crowded regime `exp(mu_T) >> T`, nearest-integer approximation again gives

```text
inf_n |mu_T-log n| = O(exp(-mu_T))=o(1/T),
```

provided the corresponding integer lies inside the cutoff. The boundary between resolvable and automatically unresolved positive energies is again `exp(mu)~T`, i.e. `mu~log T`.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE` for the route

```text
positive exponent cone
+ finite observation horizon
+ Gram / character near-resonance geometry
    -> new rational-prime or RH rigidity.
```

The one-sided cone is materially different from the signed group, but its first finite-horizon phase transition is the standard Dirichlet-polynomial resolution transition and is reproduced by any logarithmically sampled frequency family with the same local spacing. A surviving construction must therefore use arithmetic information not determined by the frequency ordering and spacing alone.

## Montgomery--Vaughan gives operator-norm orthogonality below `N~T`

For a coefficient vector `a=(a_1,...,a_N)`, define

```text
D_a(t)=sum_(n<=N) a_n n^(-it).
```

The Montgomery--Vaughan weighted Hilbert inequality implies the classical mean-value estimate

```text
integral_0^T |D_a(t)|^2 dt
  = T sum_(n<=N) |a_n|^2
    + O(sum_(n<=N) n |a_n|^2).
```

In particular,

```text
| integral_0^T |D_a(t)|^2 dt
    - T ||a||_2^2 |
 <= C N ||a||_2^2.
```

After division by `T`, the left-hand side is exactly

```text
|< (G_(T,N)-I)a,a >|.
```

Since `G_(T,N)-I` is self-adjoint,

```text
||G_(T,N)-I||
 = sup_(||a||=1) |< (G_(T,N)-I)a,a >|
 <= C N/T.
```

Consequently every singular value of the finite-time analysis map

```text
J_(T,N): ell^2({1,...,N}) -> L^2(0,T),
J_(T,N)a=T^(-1/2)D_a
```

lies between `sqrt(1-CN/T)` and `sqrt(1+CN/T)` whenever the lower bound is positive. In the regime `N=o(T)`, `J_(T,N)` is therefore asymptotically isometric in the strongest uniform quadratic sense, not merely coefficientwise.

This is important for the `prime_lattice` interpretation. Each index `n` may have a highly structured exponent vector `v(n)`, but the mean-square Gram estimate uses only the separation of the scalar frequencies `log n`. Any proposed finite-horizon mechanism based only on the pairings of the characters indexed by the positive cone is already controlled before prime-coordinate geometry has an opportunity to act.

## The supercritical cone contains universal near-collisions

For two normalized characters the Gram coefficient is explicit. Writing

```text
delta=log(n/m),
```

one has

```text
<nu_m^(T),nu_n^(T)>
 = (1/T) integral_0^T exp(i delta t) dt
 = exp(i T delta/2) sinc(T delta/2).
```

Take `m=N-1`, `n=N`. Then

```text
T delta
 = T log(N/(N-1))
 = T/N + O(T/N^2).
```

If `N/T -> infinity`, this tends to zero, so

```text
|<nu_(N-1)^(T),nu_N^(T)>| -> 1.
```

The `2 x 2` Gram minor has eigenvalues

```text
1 +/- |<nu_(N-1)^(T),nu_N^(T)>|,
```

and its least eigenvalue tends to zero. Thus no uniform Riesz lower bound can survive once the cutoff extends far past the observation horizon.

Again there is no number-theoretic input: the effect is simply that consecutive logarithms have spacing `~1/N`, below the Fourier resolution `1/T`.

## The critical local kernel is a universal sinc kernel

The threshold is not only an upper/lower estimate; its local geometry can be computed exactly.

Let

```text
n_T/T -> x>0
```

and fix integers `j,k`. For all sufficiently large `T`, the shifted indices are positive. Put

```text
delta_T=log((n_T+k)/(n_T+j)).
```

Taylor expansion gives

```text
T delta_T
 = T log(1+(k-j)/(n_T+j))
 -> (k-j)/x.
```

Substituting in the exact Gram formula yields

```text
<nu_(n_T+j)^(T),nu_(n_T+k)^(T)>
 -> exp(i (k-j)/(2x))
    sinc((k-j)/(2x)).
```

Thus every fixed finite window of lattice points around `n~xT` converges to the same Toeplitz-type sinc Gram matrix determined by `x` and integer offsets.

This limit depends on the additive ordering of ordinary integers and the derivative of `log x`; it is blind to the factorizations of `n_T+j` and `n_T+k`. Replacing the energies by a non-arithmetic control sequence

```text
lambda_n=log(n+theta),
0<theta<1,
```

produces exactly the same local limit. Therefore the critical Gram kernel fails the line's rational-prime discrimination test even before a Beurling comparison is needed.

## Fixed targets: one-sidedness restores discreteness, not RH structure

The strongest difference from `PL-071` occurs for a target frequency that does not move with `T`.

The signed prime character group is

```text
Gamma_P=log Q_(>0),
```

which is dense in `R`; `PL-071` used this to approximate every fixed real target to `O(1/T)` with a `T`-dependent signed exponent vector.

The positive cone has frequency set

```text
Lambda_+=log N={log n:n>=1},
```

which has no finite accumulation points. Hence, for fixed `mu`, either

```text
mu=log n_0
```

for one integer `n_0`, or there is a strict gap

```text
d_+(mu)=min_(n>=1)|mu-log n|>0.
```

The exact integral formula then gives

```text
|(1/T) integral_0^T exp(i(mu-log n)t) dt|
 <= min(1,2/(T|mu-log n|)),
```

so in the nonexact case the supremum over all positive-cone characters is `O_mu(1/T)`.

This is a real one-sided rigidity, but it says only that a discrete spectrum can resolve a fixed nonmember at arbitrarily long observation time. If a zeta zero ordinate produced an exact identity such as

```text
2 gamma=log n,
```

that identity itself would be additional arithmetic information; the positive-cone Gram construction does not prove or forbid it.

## Moving targets recover automatic shadowing above energy `log T`

The fixed-target gap disappears when the target energy moves to where adjacent positive energies are closer than `1/T`.

Let

```text
x_T=exp(mu_T)
```

and choose `n_T` to be a nearest positive integer to `x_T`. If `x_T` is large, then

```text
|n_T/x_T-1| <= 1/(2x_T),
```

and therefore

```text
|log n_T-mu_T|=O(exp(-mu_T)).
```

If

```text
exp(mu_T)/T -> infinity,
```

then

```text
T |log n_T-mu_T| -> 0,
```

so the normalized finite-time correlation tends to `1`.

This observation does not preserve an arbitrary target module's integer relations and does not give a canonical zero-to-integer map. It is only a control against overinterpreting pairwise positive-cone resonances at growing energy: above `mu~log T`, near-unit correlation is again forced by generic resolution geometry.

Combining the fixed and moving regimes gives the phase diagram

```text
positive energies well below log T
    -> individually resolvable unless exactly equal;

cutoff N=o(T)
    -> the whole positive family is uniformly asymptotically orthogonal;

n~xT
    -> universal sinc local Gram kernel;

N/T -> infinity
    -> automatic adjacent near-collinearity.
```

None of these transitions uses zeta continuation or zero data.

## Prior-art and novelty audit

The central estimate is classical.

- H. L. Montgomery and R. C. Vaughan, “Hilbert's Inequality,” *Journal of the London Mathematical Society* (2) **8** (1974), 73--82, DOI `10.1112/jlms/s2-8.1.73`, prove the strengthened Hilbert inequality from which the weighted mean-value theorem for Dirichlet polynomials follows. Modern analytic-number-theory references routinely state the consequence in the form

```text
integral_0^T |sum_(n<=N) a_n n^(-it)|^2 dt
 = (T+O(N)) sum_(n<=N)|a_n|^2,
```

or in the sharper weighted form used above.

No novelty is claimed for the Montgomery--Vaughan inequality, the mean-value theorem, Fourier resolution, or the sinc integral. The local critical-limit calculation and the fixed/moving target phase diagram are elementary consequences specialized to the exact positive exponent-lattice question left open by `PL-071`.

A targeted literature audit around Dirichlet-polynomial mean values, Hilbert inequalities, and large-value theory found the `N/T` transition as standard analytic-number-theory infrastructure, not a hidden prime-lattice spectral mechanism. Modern work on large values studies far subtler coefficient-dependent behavior beyond this quadratic baseline; that literature reinforces rather than weakens the conclusion that the bare Gram transition itself is classical.

The durable line-specific content is therefore a **negative information audit**: forbidding inverse prime directions does remove the universal fixed-target approximation from `PL-071`, but the first resulting finite-horizon geometry is fully explained by ordinary Dirichlet-polynomial frequency spacing.

## Matched-control and adversarial audit

The claim was stress-tested against the strongest obvious escape routes.

1. **Prime factorization is not used by the Gram theorem.** The quadratic estimate sees the ordered scalar frequencies `log n`, not the coordinate support of `v(n)`. A mechanism depending only on `G_(T,N)` cannot tell whether a near-collision came from two arithmetically related integers.
2. **The critical limit survives a fake logarithmic spectrum.** Replacing `log n` by `log(n+theta)` gives the same sinc kernel at `n~xT`, so the local transition is not a rational-prime invariant.
3. **The positive cone is genuinely different from the signed group.** The finding does not incorrectly extend `PL-071`: fixed nonmember targets cannot be shadowed to `1/T` forever by `{log n}`.
4. **Moving targets are only pairwise controlled.** The nearest-integer construction does not claim relation-compatible simultaneous approximation, injectivity, fixed prime support, or multiplicative compatibility. Those stronger constraints remain outside the no-go.
5. **No statement about exact zero/log-integer relations is made.** The argument neither proves nor assumes that `2 gamma` is never `log n`.
6. **The `N~T` scale is not the critical line.** It is a time-frequency resolution threshold in the vertical variable. Identifying its logarithm `log N~log T` with an RH symmetry parameter would be a category error without an independent canonical map.
7. **Coefficient-dependent arithmetic remains open.** Möbius/von-Mangoldt weights, target-relative coefficients, explicit-formula amplitudes, or a moving family whose dimension and arithmetic support are coupled nontrivially to `T` are not reduced to the unweighted Gram operator by this theorem.

These controls make the negative scope precise: ordinary positive-cone character geometry is exhausted at the first quadratic level, while genuinely arithmetic weighted/operator couplings remain possible research targets.

## Analytic-continuation audit

No analytic continuation is used.

Everything in the finding takes place in the exact finite Dirichlet polynomial

```text
sum_(n<=N) a_n n^(-it)
```

and the elementary frequency identity

```text
log n=<v(n),(log p)_p>.
```

The Montgomery--Vaughan estimate is a real-variable mean-square theorem for finite exponential sums. The fixed/moving target correlation formulas are exact finite integrals. Zeta zeros enter only as a possible external choice of target frequencies; no Euler product, Dirichlet series continuation, or explicit formula is invoked.

This is why the result is an especially clean control for `prime_lattice`: any RH interpretation attached to this bare finite-horizon phase transition would have to come from additional arithmetic structure, not from analytic continuation hidden in the proof.

## Relation to `PL-070` and `PL-071`

`PL-070` classified exact invariant coupling of the signed prime-log and RH zero Kronecker systems: only the exact intersection

```text
log Q_(>0) intersect <2 gamma>_Z
```

can produce a nonproduct joining.

`PL-071` then showed that replacing exact intersection by adaptive finite-time signed-character correlation destroys this rigidity: density of `log Q_(>0)` lets any fixed finite real frequency pattern be shadowed at `1/T` resolution with weighted signed-lattice radius only `O(log T)`.

The present result settles the most immediate one-sided escape explicitly left open there:

```text
signed lattice
    -> fixed-target shadowing is universal;

positive lattice
    -> fixed targets are discretely resolvable,
       but the whole family has the classical N~T
       Dirichlet-polynomial resolution transition.
```

Thus one-sidedness changes the theorem, but it does not by itself inject zeta arithmetic. Below `N~T` the positive characters are uniformly orthogonal; at and above `N~T`, the loss of resolution is explained by consecutive-integer logarithmic spacing.

## Consequence for the research line

The compact/finite-horizon branch is now narrowed again.

A useful rational-prime coupling cannot consist only of choosing positive exponent vectors and inspecting their unweighted finite-time character Gram matrix. The positive cone has a genuine semigroup asymmetry, but its first observable spectral effect is classical and universal:

```text
N/T -> 0       : identity Gram;
N/T ~ 1        : sinc local transition;
N/T -> infinity: unresolved adjacent characters.
```

The remaining live directions must add information that survives controls with the same scalar frequency spacing: for example multiplicative coefficient constraints, Möbius/von-Mangoldt weighting, a target-relative operator, a canonical support law tied independently to the completed zeta problem, or a non-Kronecker/non-Gram coupling. Merely banning inverse prime directions is no longer a sufficient escape from the finite-horizon no-go results.
