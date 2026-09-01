# PL-088 — Fixed prime-power depth is a time-dilated prime layer, not a new spectral phase

## Claim

`PL-087` shows that all higher prime powers together form a vanishing-rank sector of the ordinary prime-power-axis Gram bulk, but it deliberately leaves **depth-conditioned spectra** open. For every fixed exponent depth `k>=2`, that escape has an exact reduction: after the change of variable `n=p^k`, the depth-`k` logarithmic Gram is just the ordinary prime-support Gram at the base-prime scale `Y=X^(1/k)` with time dilated by the factor `k`. The von-Mangoldt half-weight contributes only a deterministic depth factor and a deterministic macroscopic grading.

Fix

```text
0<a<b<infinity,
k>=2 fixed,
Y=X^(1/k),
a_k=a^(1/k),
b_k=b^(1/k),
P_(Y,k)={p prime : a_k Y<p<=b_k Y},
Q_(X,k)={p^k : p in P_(Y,k)}.
```

For `T>0`, let

```text
G_(X,T)^(k)(p^k,q^k)
 =(1/T) integral_0^T
   exp(i t(log(p^k)-log(q^k))) dt.
```

If `G_(Y,tau)^prime` denotes the ordinary prime-support Gram on `P_(Y,k)`, then there is the **exact identity**

```text
boxed:
G_(X,T)^(k)=G_(Y,kT)^prime.
```

Now restrict the naturally normalized von-Mangoldt half-weighted axis matrix of `PL-087` to the depth-`k` block:

```text
A_(X,T)^(k)(p^k,q^k)
 = X/(log X)^2
   * Lambda(p^k)Lambda(q^k)/(p q)^(k/2)
   * G_(X,T)^(k)(p^k,q^k).
```

Since `Lambda(p^k)=log p`, define

```text
B_(k,Y)(p)=(Y/p)^(k/2),
R_Y(p)=log p/log Y.
```

Then

```text
boxed:
A_(X,T)^(k)
 = (1/k^2)
   R_Y B_(k,Y)
   G_(Y,kT)^prime
   B_(k,Y) R_Y,
```

and, uniformly on the fixed base-prime band,

```text
||R_Y-I||_op=O_(a,b,k)(1/log Y).
```

Thus a fixed exponent depth contains no additional prime-lattice interaction beyond:

```text
prime support at scale Y=X^(1/k)
+ time change T -> kT
+ deterministic envelope (Y/p)^k
+ deterministic scalar 1/k^2.
```

Two consequences make the obstruction concrete.

First, at the **common prime-scale horizon** used in `PL-083`--`PL-087`,

```text
T_X=cX/log X,
```

every fixed depth `k>=2` is already far beyond its own mean-gap interaction scale. Unconditionally,

```text
(1/|P_(Y,k)|)
 ||G_(X,T_X)^(k)-I||_F^2
 =O_(a,b,c,k)(
   (log Y)^2/Y^(2k-2)
 )
 ->0.
```

Consequently the empirical spectral law of `A_(X,T_X)^(k)` converges in `W_2` to the deterministic pushforward of normalized Lebesgue measure on `[a_k,b_k]` under

```text
y -> 1/(k^2 y^k).
```

There is no nontrivial local-prime bulk interaction left on the fixed higher-depth layer at the common horizon.

Second, if time is retuned to the **depth-`k` mean-prime-gap horizon**

```text
T_(X,k)=cY/log X
       =cY/(k log Y),
```

then

```text
k T_(X,k)=cY/log Y,
```

which is exactly the critical prime-support horizon of `PL-083`--`PL-085` at the base scale `Y`. Under the same full local Hardy--Littlewood hierarchy used in `PL-085`, the depth-conditioned empirical law therefore becomes the same generic Poisson sinc Euclidean-random-matrix law, modified only by the deterministic local scalar

```text
(1/k^2) y^(-k).
```

So conditioning on exponent depth avoids the vanishing-rank argument of `PL-087`, but it does **not** uncover a new zeta-sensitive spectral phase. At its natural interaction scale it is a deterministic regrading of the already-classicalized prime local process; at the common `X/log X` horizon it is asymptotically diagonal.

**Evidence/status:** `EXACT-DERIVED + LITERATURE-CONTEXT + CONJECTURAL-CONTROL + DECISIVE-NEGATIVE` for the route

```text
fixed prime-power depth k>=2
+ natural von-Mangoldt half-weight
+ depth-conditioned finite-time Gram spectrum
    -> a new exponent-depth spectral mechanism relevant to RH.
```

The negative conclusion is deliberately restricted to a **single fixed depth with the inherited shell normalization and finite-time logarithmic Gram**. It does not classify cross-depth Schur complements, growing depth `k=k(X)`, inverse-density amplifications, hard-edge/determinant observables coupling different depths, target-relative Nyman quantities, or the completed Weil form.

## Exact time-dilation identity

For `p,q in P_(Y,k)`,

```text
log(p^k)-log(q^k)
 =k(log p-log q).
```

Therefore

```text
G_(X,T)^(k)(p^k,q^k)

 =(1/T) integral_0^T
    exp(i k t(log p-log q)) dt.
```

With `u=kt`,

```text
G_(X,T)^(k)(p^k,q^k)

 =(1/(kT)) integral_0^(kT)
    exp(i u(log p-log q)) du

 =G_(Y,kT)^prime(p,q).
```

No asymptotics, prime distribution, Euler product, or analytic continuation enters this step. It is an exact consequence of the energy relation

```text
log(p^k)=k log p.
```

In exponent-lattice coordinates this says that the ray point `k e_p` does not supply a new frequency direction: it lies on the same prime coordinate ray as `e_p`, with generator frequency multiplied by `k`.

The same identity survives an arbitrary replacement of the rational prime frequencies `log p` by generalized frequencies `lambda_p`: the depth-`k` ray has frequency `k lambda_p`, so its Gram is still obtained by the time change `T->kT`. This is an immediate Beurling/generic-frequency falsification control against interpreting the identity itself as rational-prime rigidity.

## The inherited von-Mangoldt weight is only deterministic regrading

Because `X=Y^k` and `log X=k log Y`, the normalized amplitude attached to `p^k` is

```text
sqrt(X)/log X
 * Lambda(p^k)/p^(k/2)

 =Y^(k/2)/(k log Y)
  * log p/p^(k/2)

 =(1/k)
   (Y/p)^(k/2)
   (log p/log Y).
```

Writing this diagonal amplitude as

```text
D_(k,Y)=(1/k) B_(k,Y) R_Y
```

gives the exact matrix factorization

```text
A_(X,T)^(k)
 =D_(k,Y) G_(Y,kT)^prime D_(k,Y).
```

On `p=yY`, with `y in [a_k,b_k]`,

```text
R_Y(p)
 =1+log y/log Y,
```

so

```text
sup_(p in P_(Y,k)) |R_Y(p)-1|
 =O_(a,b,k)(1/log Y).
```

Hence the specifically von-Mangoldt part is again asymptotically scalar, just as in `PL-086`; the surviving fixed-depth information is the **deterministic** factor

```text
1/k^2 * (Y/p)^k.
```

The exponent depth is real information pointwise, but in this isolated block it only rescales a prime Gram already present at a smaller base scale.

## At the common `X/log X` horizon every fixed higher depth is over-resolved

Take

```text
T_X=cX/log X
   =cY^k/(k log Y).
```

Then the effective prime observation time is

```text
kT_X=cY^k/log Y,
```

which is much larger than the base-prime scale `Y` for every fixed `k>=2`.

For distinct `p,q in [a_kY,b_kY]`, the centered sharp kernel satisfies

```text
|G_(Y,kT_X)^prime(p,q)|
 <= min(
      1,
      2/(kT_X |log(p/q)|)
    ).
```

The mean-value theorem gives

```text
|log(p/q)|
 >= c_(a,b,k) |p-q|/Y,
```

hence

```text
|G_(Y,kT_X)^prime(p,q)|
 <<_(a,b,k)
 Y/(kT_X |p-q|).
```

For each fixed `p`, the other primes form a subset of the integers, so

```text
sum_(q!=p) 1/|p-q|^2
 <=2 sum_(h>=1) 1/h^2
 =O(1).
```

Therefore, writing `M_(Y,k)=|P_(Y,k)|`,

```text
(1/M_(Y,k))
 ||G_(Y,kT_X)^prime-I||_F^2

 << (Y/(kT_X))^2

 =O_(c,k)(
    (log Y)^2/Y^(2k-2)
   )
 ->0.
```

This estimate is stronger than needed and uses no sieve or Hardy--Littlewood input. The common horizon resolves distinct base primes so finely that the depth-conditioned exponentials are asymptotically orthogonal in normalized Hilbert--Schmidt norm.

Since `D_(k,Y)` is uniformly bounded above and below on the fixed band,

```text
A_(X,T_X)^(k)-D_(k,Y)^2
 =D_(k,Y)
  (G_(Y,kT_X)^prime-I)
  D_(k,Y)
```

has normalized Frobenius norm tending to zero. Hoffman--Wielandt then gives

```text
W_2(
  mu_(A^(k)),
  mu_(D_(k,Y)^2)
 )->0.
```

By the prime number theorem, the normalized base primes `p/Y` become uniformly distributed in the fixed macroscopic interval `[a_k,b_k]` for this coarse averaging, and

```text
D_(k,Y)(p)^2
 ->1/(k^2 y^k)
```

uniformly when `p/Y=y`. The diagonal empirical measure therefore converges to the deterministic pushforward stated in the claim.

This is a sharper statement than the vanishing-rank conclusion of `PL-087` for the fixed layer: even after conditioning so that the layer carries mass one, its common-horizon bulk is asymptotically diagonal rather than merely negligible in the full matrix.

## Retuning time recovers exactly the ordinary prime critical regime

The base-prime set `P_(Y,k)` has mean ordinary gap of order `log Y`. Since the depth-`k` frequency difference is multiplied by `k`, its first order-one local interaction occurs when

```text
Y/(kT) ~ log Y,
```

or equivalently

```text
T~Y/(k log Y)=Y/log X.
```

Set precisely

```text
T_(X,k)=cY/(k log Y).
```

Then

```text
G_(X,T_(X,k))^(k)
 =G_(Y,cY/log Y)^prime.
```

Thus every support-only statement in `PL-083`--`PL-085` transfers directly to the fixed-depth layer after replacing the macroscopic band `[a,b]` by `[a_k,b_k]`.

For the weighted matrix, the diagonal envelope `B_(k,Y)` is a bounded continuous function of `p/Y`. The compact-range moment argument and the `W_2` tail removal in `PL-085` are unchanged by such a deterministic bounded envelope. Under the same full local Hardy--Littlewood hierarchy, the local limiting kernel at macroscopic base point `y` is therefore

```text
k_(k,y,c)(u,v)
 =(1/k^2) y^(-k)
   sinc(c(u-v)/(2y)).
```

The resulting empirical spectral law is a macroscopic mixture of generic unit-intensity Poisson sinc Euclidean-random-matrix laws with that deterministic scalar grading. The exponent depth changes only the observation clock and the envelope; the local point-process input remains the ordinary prime process at scale `Y`.

In particular, the critical time depends strongly on depth:

```text
k=1:  T~X/log X;
k=2:  T~sqrt(X)/log X;
k=3:  T~X^(1/3)/log X;
...
```

(up to the fixed `k` convention absorbed by `log X=k log Y`). A single common observation horizon cannot place several fixed depths simultaneously in their mean-gap critical regimes.

## Prior-art and novelty audit

The core ingredients are classical or elementary:

- `log(p^k)=k log p` and `Lambda(p^k)=log p` are standard;
- finite-time exponential Grams are ordinary Dirichlet-polynomial mean-square objects;
- rescaling a frequency family by `k` is exactly equivalent to rescaling observation time by `k`;
- the prime number theorem gives the coarse base-prime density used for the deterministic diagonal limit;
- `PL-081`--`PL-085` already classify the relevant prime-support finite-time regimes, with their stated unconditional or Hardy--Littlewood assumptions.

A targeted literature search around prime-power Dirichlet-polynomial mean values, logarithmic prime-power frequency Grams, and fixed-depth prime-power spectral statistics did not locate a source stating this exact depth-conditioned matrix reduction. That absence is **not** used as a novelty claim. The durable content is the line-specific obstruction obtained by combining the exact time-dilation identity with the already-audited prime-support phase diagram.

Classical mean-value theory for Dirichlet polynomials is fully consistent with this reduction and supplies no missing zeta-zero input. More importantly for the mandate, the reduction is universal under generalized-prime/frequency replacement, so it fails the line's rational-prime discrimination control before any RH claim can arise.

## Adversarial boundaries

1. **`k` is fixed.** If `k=k(X)` grows, the base scale `Y=X^(1/k)` may grow too slowly or cease to tend to infinity, and the fixed-band prime asymptotics used here require a separate analysis.
2. **Cross-depth couplings are not classified.** The full matrix contains blocks between `p^k` and `q^ell` with `k!=ell`. The present exact reduction applies only to a single diagonal depth block and does not evaluate a Schur complement or a determinant that deliberately couples different depths.
3. **The critical Poisson law is conditional.** Its identification inherits the full local Hardy--Littlewood hierarchy of `PL-085`. The exact time-dilation/factorization and the common-horizon diagonalization are unconditional.
4. **Hard-edge and determinant observables can escape the bulk statement.** `W_2` convergence at the common horizon controls ordinary quadratic spectral transport, but a normalized `log det`, smallest eigenvalue, or rare resonance at the depth-critical horizon may require finer information.
5. **Inverse-density amplification is outside the inherited normalization.** One can multiply a rare depth block by a growing factor, but such a normalization is not supplied by the standard von-Mangoldt half-weight and must be justified independently rather than chosen to rescue the block.
6. **The completed Weil form is not a depth-by-depth Gram.** `PL-013` and the later localized-Weil findings use a completed prime-power sum plus the archimedean term. Their zero-sensitive structure is not contradicted by the present reduction.
7. **No analytic continuation occurs.** Every exact identity here is finite-dimensional and follows from logarithmic frequencies and the von-Mangoldt value on prime powers. The conditional local law uses Hardy--Littlewood prime statistics, not continuation of the Euler product.
8. **Generic-frequency control is fatal to novelty of the mechanism.** Replacing `log p` by arbitrary positive base frequencies preserves the exact `k`-ray/time-dilation identity. Any future use of exponent depth must therefore add a structure that couples different rays/depths in a rational-prime-specific way.

## Consequence for the prime-lattice search

The two most direct ways to make exponent depth visible in the prime-power Gram have now both been separated:

```text
all depths with ordinary empirical weighting
    -> k>=2 occupies vanishing rank (`PL-087`);

condition on one fixed depth k>=2
    -> exact prime-layer time dilation (this finding)
    -> at common T~X/log X: deterministic diagonal bulk
    -> at its own T~X^(1/k)/log X: generic prime/Poisson bulk.
```

So merely conditioning on `k` does not rescue the exponent-depth spectral program. A surviving use of the axis geometry must exploit **relations between different depths**, a non-bulk statistic, a canonically justified depth reweighting, or an external target/completion that is not invariant under the exact time-rescaling reduction. In particular, cross-depth Schur complements or completed explicit-formula couplings remain mathematically different questions; an isolated `k e_p` layer does not.