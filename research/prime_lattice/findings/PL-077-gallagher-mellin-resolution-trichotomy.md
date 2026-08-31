# PL-077 — Gallagher smoothing gives a Mellin-resolution trichotomy: diagonal, fixed shifts, then short-interval variance

## Claim

The positive finite-horizon branch of `PL-072`--`PL-076` admits an exact logarithmic-frequency localization which explains, in one formula, why the arithmetic content changes when the Dirichlet-polynomial length crosses the observation scale.

For a finite coefficient family `a_n` supported on a macroscopic band `X<n<=B X`, write

```text
D_X(t)=sum_(X<n<=B X) a_n n^(-it),

sinc(u)=sin(u)/u,

W_T(t)=(1/(2 pi T)) sinc^2(t/(2T)).
```

Then Fourier inversion gives the exact positive identity

```text
integral_R W_T(t) |D_X(t)|^2 dt

 = sum_(m,n) a_m conjugate(a_n)
     (1-T |log(m/n)|)_+

 = T integral_R
     | sum_(X<n<=B X,
             |log n-u|<=1/(2T)) a_n |^2 du.
```

Thus an observation scale `T` in the vertical/Kronecker variable resolves the positive integer cone in **logarithmic boxes of width `1/T`**. At height `n~X`, such a box has ordinary additive width

```text
H ~ X/T.
```

This yields a sharp information trichotomy for this canonical Gallagher-smoothed quadratic statistic:

```text
X/T -> 0
    -> eventually no off-diagonal integer pairs;

X/T -> H_0 in (0,infinity)
    -> only finitely many additive lags survive;

X/T -> infinity
    -> a growing collection of lags is exactly a
       multiplicative short-interval variance.
```

For zeta-sensitive coefficients this routes the three regimes to already known arithmetic theories. In particular, after centering the prime coefficient with `b(n)=Lambda(n)-1`, taking

```text
a_n=b(n)n^(-sigma)
```

turns the right-hand side into a weighted multiplicative short-interval variance. On a log box centered at `x=e^u`, the radial factor contributes locally `x^(-2 sigma)` while `du=dx/x`; hence the geometric measure is

```text
x^(-2 sigma-1) dx.
```

At the half weight `sigma=1/2`, this becomes

```text
x^(-2) dx,
```

which is exactly the classical weight appearing in the multiplicative Selberg mean square used by Selberg and by Goldston--Montgomery in the prime/zero pair-correlation theory. The occurrence of `1/2` in this positive finite-horizon statistic therefore has a precise Mellin-geometric explanation, but it is again **not a zero-localization mechanism**: it is the exponent for which log-Haar measure plus two radial half-weights produces the standard `x^(-2) dx` short-interval variance measure.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART/REDIRECT` for the route

```text
sharp positive-cone band
+ canonical positive time smoothing
+ Lambda(n)n^(-1/2) arithmetic weighting
    -> new prime-lattice global spectral invariant.
```

The exact identity is ordinary Fourier/Plancherel geometry on the frequency set `{log n}` and is a direct Mellin version of Gallagher's classical mean-square localization. The arithmetic regimes it exposes are classical: fixed finite lags lead back to Hardy--Littlewood-type shifted `Lambda` correlations (`PL-075`), while growing short intervals enter the Selberg-variance / Montgomery pair-correlation dictionary already surrounding `PL-076`.

The finding does **not** identify the unsmoothed rectangular time average of `PL-075` with the Selberg integral. The `sinc^2` time weight is a deliberate positive Gallagher smoothing whose Fourier transform has compact support in the log-frequency gap. Any mechanism that depends essentially on oscillatory tails of the rectangular `sinc` kernel remains outside this exact reduction.

## Exact logarithmic localization

Let

```text
lambda_n=log n
```

and regard the coefficient family as the finite discrete measure

```text
mu=sum_n a_n delta_(lambda_n).
```

The Fourier transform of `mu` is exactly

```text
mu_hat(t)=sum_n a_n exp(-it lambda_n)=D_X(t).
```

With the normalization above,

```text
integral_R W_T(t) exp(-iut) dt
 = (1-T|u|)_+.
```

Expanding the square therefore gives

```text
integral_R W_T(t)|D_X(t)|^2 dt
 =sum_(m,n) a_m conjugate(a_n)
   (1-T|lambda_m-lambda_n|)_+.
```

Now define the log-frequency box

```text
I_(T,u)=[u-1/(2T),u+1/(2T)].
```

The overlap length of the boxes centered at `lambda_m` and `lambda_n` is

```text
|I_(T,lambda_m) intersect I_(T,lambda_n)|
 =(1/T-|lambda_m-lambda_n|)_+.
```

Hence

```text
T integral_R
  |sum_(lambda_n in I_(T,u)) a_n|^2 du

 =sum_(m,n) a_m conjugate(a_n)
   (1-T|lambda_m-lambda_n|)_+,
```

which proves the displayed identity exactly.

No Euler product, asymptotic equidistribution, analytic continuation, or hypothesis about zeta zeros is present. The statement is a finite Fourier identity.

## The resolution parameter is `H=X/T`

For `u=log x`, the logarithmic box corresponds exactly to the multiplicative interval

```text
x exp(-1/(2T)) < n <= x exp(1/(2T)).
```

Its ordinary length is

```text
H_(x,T)
 =x (exp(1/(2T))-exp(-1/(2T)))
 =x/T+O(x/T^3).
```

On a fixed macroscopic band `x~X`, the number of neighboring integer sites that can interact is therefore controlled by

```text
H=X/T.
```

This recovers the resolution threshold of `PL-072` from a different and stronger positive-kernel viewpoint. It also identifies what the threshold means arithmetically: `N~T` is exactly the point at which a logarithmic Fourier cell first contains `O(1)` ordinary integer spacings.

### Diagonal regime: `X/T -> 0`

For distinct integers `m,n~X`,

```text
|log(m/n)| >= c_B/X
```

for a band-dependent positive constant once `X` is large. If `X/T->0`, eventually

```text
T |log(m/n)|>1
```

for every distinct pair in the band. Therefore the compact triangular kernel kills every off-diagonal entry **exactly**, not merely asymptotically:

```text
integral W_T |D_X|^2
 =sum_n |a_n|^2.
```

This is the positive-smoothed analogue of the asymptotic orthogonality found in `PL-072` by Montgomery--Vaughan.

### Microscopic regime: `X/T -> H_0`

If `m=n+h` with `n~X`, then

```text
T log((n+h)/n)=T h/n+O(T h^2/n^2).
```

When `X/T` stays bounded, the support condition

```text
T |log((n+h)/n)|<1
```

allows only `|h|=O_B(X/T)=O(1)`. Thus the entire off-diagonal arithmetic content of the Gallagher-smoothed statistic is a **finite collection of fixed additive shifts**.

For `a_n=Lambda(n)n^(-1/2)` these terms contain

```text
Lambda(n)Lambda(n+h),
```

so their evaluation is precisely Hardy--Littlewood prime-pair data, in agreement with the fixed-lag calculation of `PL-075`. There is no hidden infinite-dimensional prime-torus invariant left inside this positive smoothing at `X~T`: the log-frequency microscope has converted the problem into finitely many ordinary additive correlations.

### Mesoscopic/long regime: `X/T -> infinity`

When `H=X/T` grows, the same exact formula packages all lags within a multiplicative interval of relative size `1/T` into

```text
T integral
 |sum_(x exp(-1/(2T))<n<=x exp(1/(2T))) a_n|^2
 dx/x.
```

For the centered von Mangoldt coefficient

```text
a_n=(Lambda(n)-1)n^(-sigma),
```

this is a smooth-weight version of the variance of primes in multiplicative short intervals of length `H~x/T`.

At this point the surviving object is no longer a new lattice spectral statistic. Gallagher's classical lemma and its weighted variants are specifically designed to convert mean squares of exponential/Dirichlet polynomials into short-interval quadratic sums. Goldston--Montgomery proved, under RH, the equivalence between strong zero pair correlation and asymptotics for prime short-interval second moments; Chan sharpened this correspondence, and Bui--Keating--Smith extended the same variance/pair-correlation architecture to suitable arithmetic coefficients attached to the Selberg class.

The exact identity here is not claimed to reproduce every normalization or endpoint of those theorems verbatim. Its role is structural: once `X/T` grows, the positive Mellin-frequency localization lands in the same short-interval variance category on which that classical prime/zero dictionary operates.

## Why the half weight produces the classical `x^-2` measure

The half exponent in this branch can now be isolated without invoking a zeta zero.

On the local interval around `x=e^u`, for fixed `sigma` and large `T`,

```text
n^(-sigma)=x^(-sigma)(1+O_sigma(1/T)).
```

Thus the local quadratic mass has the geometric weight

```text
|x^(-sigma)|^2 du
 =x^(-2 sigma) dx/x
 =x^(-2 sigma-1) dx.
```

For `sigma=1/2`,

```text
x^(-2 sigma-1) dx=x^(-2) dx.
```

Selberg's RH-conditional multiplicative short-interval estimate and the Goldston--Montgomery pair-correlation equivalence use precisely quadratic forms of the shape

```text
integral
 |psi((1+delta)x)-psi(x)-delta x|^2
 dx/x^2.
```

The symmetric interval produced by the exact log box and the slowly varying `n^(-1/2)` coefficient require the usual harmless local-weight bookkeeping if one wants a theorem with exact constants. The structural coincidence of the measure, however, is forced directly by Mellin geometry:

```text
log-Haar measure dx/x
+ two copies of x^(-1/2)
= dx/x^2.
```

This gives a natural interpretation of the ubiquitous half weight in these finite-horizon mean squares, but also supplies a falsification control: **the same exponent is already built into the classical short-interval variance formalism before any statement about the location of zeros is made.**

## Prior-art and novelty audit

No novelty is claimed for the Fourier identity, Gallagher localization, Selberg's short-interval mean square, or the prime/zero pair-correlation equivalence.

- **P. X. Gallagher**, “A large sieve density estimate near `sigma=1`,” *Inventiones Mathematicae* **11** (1970), 329--339, DOI `10.1007/BF01403187`, is the classical source of the mean-square localization lemma for exponential sums.
- **Daniel A. Goldston, Hugh L. Montgomery**, “Pair correlation of zeros and primes in short intervals,” in *Analytic Number Theory and Diophantine Problems*, Progress in Mathematics **70** (1987), 183--203, is the classical RH-conditional equivalence between strong pair correlation and prime short-interval second moments. In its multiplicative form the prime variance carries the `x^(-2) dx` weight highlighted above.
- **Tsz Ho Chan**, “More Precise Pair Correlation of Zeros and Primes in Short Intervals,” *Journal of the London Mathematical Society* **68**(3) (2003), 579--598, DOI `10.1112/S0024610703004769`, refines the correspondence and records the Goldston--Montgomery equivalence explicitly.
- **Giovanni Coppola, Maurizio Laporta**, “A generalization of Gallagher's lemma for exponential sums,” *Siauliai Mathematical Seminar* **10**(18) (2015), 29--47; arXiv:1411.1739, explicitly develops weighted Gallagher inequalities for Dirichlet polynomials and Selberg integrals.
- **H. M. Bui, J. P. Keating, D. J. Smith**, “On the variance of sums of arithmetic functions over primes in short intervals and pair correlation for L-functions in the Selberg class,” *Journal of the London Mathematical Society* **94**(1) (2016), 161--185, DOI `10.1112/jlms/jdw030`, shows that the variance/pair-correlation architecture extends beyond the Riemann zeta function.
- `PL-076` already records Winston Heap's 2026 long-Dirichlet-polynomial theorem in which a different smoothing of the half-weight `Lambda` polynomial produces Montgomery's zero pair-correlation statistic directly under RH.

A targeted literature audit around Gallagher localization, Dirichlet-polynomial mean squares, Selberg integrals, prime short intervals, and pair correlation recovered this mature framework rather than a distinct zeta-specific spectral invariant attached to the exponent lattice. The durable line-specific content is the **resolution map** obtained by applying the exact logarithmic localization to the current `PL-072`--`PL-076` branch.

## Adversarial and analytic-continuation audit

Several boundaries are essential.

1. **The rectangular time average remains distinct.** `PL-074`--`PL-075` use the sharp interval `0<=t<=T`, whose kernel is an oscillatory `sinc` with long log-frequency tails. The present `W_T` has an infinite time tail but a compact triangular Fourier kernel. Fine cancellation carried only by the sharp kernel is not ruled out.
2. **Pair correlation is not RH.** Goldston--Montgomery/Chan equivalences are formulated under RH and concern zero-spacing statistics. They cannot be used circularly to locate all zeros on the critical line.
3. **Hardy--Littlewood input is conjectural at a prescribed shift.** In the microscopic `X/T=O(1)` regime, the routing to `Lambda(n)Lambda(n+h)` identifies the required arithmetic information but does not prove the prime-pair asymptotic.
4. **The half-weight statement is geometric, not spectral.** Producing `dx/x^2` does not generate a self-adjoint operator with zero ordinates as eigenvalues, nor does it use the functional equation.
5. **Centering matters.** The uncentered `Lambda` polynomial contains the deterministic prime-density/PNT component. The short-interval fluctuation relevant to pair correlation is exposed after the standard centering `Lambda-1` (or the corresponding `psi` main term).
6. **Exact constants require weight bookkeeping.** The local replacement `n^(-sigma)~x^(-sigma)` and symmetric-versus-forward multiplicative intervals are sufficient for the structural routing claim, not a claimed new asymptotic theorem with the exact Goldston--Montgomery constants.
7. **The architecture is not rational-prime unique.** Gallagher localization is coefficient-agnostic, and Bui--Keating--Smith exhibit analogous pair-correlation/variance relations for a wider Selberg-class setting. A candidate mechanism must add information beyond this universal Fourier resolution plus the chosen arithmetic coefficient.
8. **No analytic continuation occurs in the exact identity.** Zero-sensitive information appears only when one invokes the external explicit-formula/pair-correlation theory. The finite prime-lattice polynomial itself does not continue `-zeta'/zeta` from `Re(s)>1` to the critical strip.

## Consequence for the research line

The finite-horizon coefficient branch now has a unified scale diagram:

```text
log-frequency resolution 1/T
        |
        v
ordinary local width H=X/T

H -> 0
    -> exact diagonalization under Gallagher smoothing;

H = O(1)
    -> finitely many additive shifts
       -> Hardy--Littlewood / Chowla / Mirsky-type data;

H -> infinity
    -> short-interval variance
       -> classical Selberg / prime-zero pair-correlation theory.
```

Together with `PL-073`--`PL-076`, this removes another broad class of interpretations in which merely changing the observation horizon, inserting the canonical half weight, and taking a positive quadratic smoothing is expected to reveal a new RH-sensitive spectrum of the exponent lattice.

A surviving finite-horizon route must exploit information that this logarithmic localization does not preserve: for example a genuinely essential feature of the **oscillatory sharp-time kernel**, a distinguished target/completion, a higher-order invariant not reducible to the established correlation hierarchy, or a structure that independently couples analytic continuation/functional-equation data to the finite prime lattice. Merely observing the transition at `X/T~1` or the `sigma=1/2` Selberg measure is not sufficient evidence of critical-line rigidity.
