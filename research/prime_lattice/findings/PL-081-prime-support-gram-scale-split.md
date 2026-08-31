# PL-081 — Prime basis directions split sharp-Gram bulk and extreme scales

## Claim

The most direct **support-only arithmetic escape** left outside `PL-080` behaves very differently from the full integer band, but the difference is controlled by classical prime-gap density rather than by analytic continuation or an RH-sensitive spectral law.

Fix

```text
0<a<b<infinity,
P_X={p prime : aX<p<=bX},
M_X=|P_X|,
```

and form the sharp finite-time Gram matrix of the prime basis directions

```text
G_(X,T)(p,q)
 =(1/T) integral_0^T exp(i t(log p-log q)) dt,
p,q in P_X.
```

Write

```text
H_X=X/T.
```

If

```text
1<=H_X=o(log X),
```

equivalently

```text
X/log X << T <= X,
```

then the prime-supported Gram matrix is asymptotically the identity in **normalized Hilbert--Schmidt norm**:

```text
boxed:
(1/M_X)||G_(X,T)-I||_F^2
  <<_(a,b) H_X/log X
  ->0.
```

Consequently, if `lambda_1,...,lambda_(M_X)` are its eigenvalues,

```text
(1/M_X) sum_j |lambda_j-1|^2 ->0,
```

so the empirical spectral measure converges to `delta_1`. Thus the integer-band Nyquist/prolate bulk phase of `PL-078`--`PL-080` disappears after restricting to the exponent-lattice **basis directions**: primes are too sparse for an order-one bulk interaction at `T~X` or, more generally, at every horizon strictly above the mean-prime-gap scale `X/log X`.

However the lower edge behaves differently. Maynard's bounded-gap theorem implies that there are infinitely many consecutive prime pairs with gap bounded by an absolute constant. Therefore for **every** horizon with

```text
T(X)=o(X),
```

there exists a sequence `X_j->infinity` for which

```text
boxed:
lambda_min(G_(X_j,T(X_j))) ->0.
```

In the wide intermediate regime

```text
X/log X << T(X) << X,
```

both statements hold simultaneously:

```text
bulk empirical spectrum -> delta_1,

but

smallest eigenvalue ->0 along a bounded-gap subsequence.
```

Hence prime support creates a genuine **bulk/extreme scale split**. The first scale not excluded for nontrivial bulk behavior is

```text
T ~ X/log X,
```

where a logarithmic Fourier cell has ordinary width `X/T~log X`, exactly the mean prime-gap / short-interval scale. Gallagher's classical theorem shows that, conditional on the Hardy--Littlewood prime-tuple conjectures, prime counts in intervals of length `lambda log X` have Poisson limiting statistics. Thus the surviving support-only sharp-Gram problem is routed into classical short-interval and prime-gap theory, not into a new exponent-lattice mechanism that singles out `Re(s)=1/2`.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART/REDIRECT`, with a `DECISIVE-NEGATIVE` conclusion for the route

```text
prime basis-direction support
+ unweighted sharp finite-time Gram bulk
+ horizon T >> X/log X
    -> new RH-sensitive prime-lattice spectral phase.
```

The result is deliberately a bulk statement plus a lower-edge obstruction. It does **not** determine the empirical law at the exact `T~X/log X` scale, fine determinant asymptotics, weighted `Lambda(p)p^(-1/2)` observables, or target-relative/Nyman quantities.

## Exact sharp kernel on the prime sector

As in `PL-079`--`PL-080`, centering the time interval removes a diagonal phase. Up to unitary diagonal conjugacy,

```text
A_(X,T)(p,q)
 =sinc((T/2)log(p/q)),

sinc(u)=sin(u)/u.
```

For `p,q in P_X`, the mean-value theorem gives

```text
|log(p/q)| >= |p-q|/(bX+O(1)).
```

Therefore, uniformly on the fixed macroscopic band,

```text
|A_(X,T)(p,q)|
 <<_(a,b) min(1,H_X/|p-q|),

H_X=X/T.
```

The diagonal is exactly one. All off-diagonal Hilbert--Schmidt mass is therefore controlled by how often two primes in the band occur at each additive gap.

This is already a structural change from the full integer band. For all integers, every gap `h` occurs at density one and produces the prolate/Nyquist symbol of `PL-078`. On prime support, each fixed gap is suppressed by a second sieve factor of order `1/log X`.

## Selberg sieve makes the normalized off-diagonal energy vanish

For `h>=1`, let

```text
N_h(X)
 =#{p in P_X : p+h in P_X and p+h prime}.
```

For large `X`, odd `h` contributes nothing because both primes in the macroscopic band are odd. The standard dimension-two Selberg/Brun upper-bound sieve gives, uniformly for even

```text
1<=h<=(b-a)X,
```

a bound of the form

```text
N_h(X)
 <<_(a,b)
 X/(log X)^2 * S_+(h),
```

where the harmless local factor may be taken as

```text
S_+(h)
 = product_(r|h, r>2) (r-1)/(r-2).
```

Only an upper bound is used; no twin-prime or Hardy--Littlewood asymptotic is assumed.

The mean size of this local factor is bounded. Indeed,

```text
S_+(h)
 = sum_(d|h,
        d odd square-free)
     g(d),

g(d)=product_(r|d) 1/(r-2).
```

Since

```text
sum_d g(d)/d
 = product_(r>2)
     (1+1/(r(r-2)))
 < infinity,
```

one gets the elementary average estimate

```text
sum_(h<=Y) S_+(h) << Y.
```

Partial summation then gives, for `H>=1`,

```text
sum_(h>=1)
  min(1,C H^2/h^2) S_+(h)
 <<_C H.
```

Grouping the Gram entries by `h=|p-q|` therefore yields

```text
||G_(X,T)-I||_F^2
 <<_(a,b)
 X H_X/(log X)^2.
```

The prime number theorem gives

```text
M_X
 ~ (b-a)X/log X.
```

Dividing the preceding estimates proves

```text
(1/M_X)||G_(X,T)-I||_F^2
 <<_(a,b) H_X/log X.
```

Thus every regime with

```text
H_X=o(log X)
```

has vanishing normalized off-diagonal energy.

The proof uses only three classical inputs:

```text
sharp sinc kernel on log frequencies,
prime density X/log X,
dimension-two sieve control of prime pairs.
```

There is no Euler product, analytic continuation, functional equation, or zero divisor in the argument.

## The bulk spectral law collapses to a point mass

Because `G_(X,T)-I` is Hermitian,

```text
||G_(X,T)-I||_F^2
 =sum_j (lambda_j-1)^2.
```

Hence

```text
(1/M_X)sum_j(lambda_j-1)^2 ->0.
```

For every bounded Lipschitz test function `phi`, Cauchy--Schwarz gives

```text
| (1/M_X)sum_j phi(lambda_j)-phi(1) |
 <=Lip(phi)
   [(1/M_X)sum_j(lambda_j-1)^2]^(1/2)
 ->0.
```

So the empirical spectral measure tends weakly to

```text
delta_1.
```

This is substantially stronger than saying that most pairwise inner products are small. It shows that **all but a vanishing spectral proportion** of the prime-supported Gram matrix is asymptotically orthonormal throughout `X/log X << T <= X`.

It is also a direct falsification of interpreting the full-integer Nyquist constant `1/(2 pi)` from `PL-080` as a robust arithmetic phase: once only the actual prime coordinate directions are retained, the relevant density is lower by `log X`, and the macroscopic bulk transition disappears at that scale.

## Bounded prime gaps survive in the extreme spectrum

Normalized Hilbert--Schmidt convergence does not control a vanishing number of extreme eigenvalues. Prime support makes that distinction unavoidable.

Maynard proves unconditionally that

```text
liminf_n (p_(n+1)-p_n) < infinity.
```

Thus there are an absolute constant `B` and infinitely many consecutive prime pairs

```text
p_j<q_j,
q_j-p_j<=B.
```

Choose any fixed

```text
x_0 in (a,b)
```

and choose `X_j` so that

```text
p_j/X_j -> x_0.
```

Then also `q_j/X_j->x_0`, so both primes lie in `P_(X_j)` for all sufficiently large `j`.

The corresponding centered `2 x 2` principal Gram block is

```text
[ 1      sinc(u_j) ]
[ sinc(u_j)   1    ],

u_j=(T(X_j)/2)log(q_j/p_j).
```

If `T(X)=o(X)`, then

```text
|u_j|
 << B T(X_j)/X_j
 ->0.
```

The smaller eigenvalue of this block is

```text
1-|sinc(u_j)| ->0.
```

Cauchy interlacing therefore gives

```text
lambda_min(G_(X_j,T(X_j)))
 <=1-|sinc(u_j)|
 ->0.
```

So the extreme lower edge can become singular long before the **bulk** notices the prime density. This phenomenon is not an RH signal either: it is directly supplied by the unconditional bounded-prime-gap theorem.

In particular, when

```text
X/log X << T(X) << X,
```

the matrix has a point-mass bulk at `1` but nevertheless develops arbitrarily small eigenvalues along a subsequence. Any determinant or condition-number experiment in this regime must therefore distinguish a bulk law from rare-gap extreme statistics; mixing the two can manufacture an apparent spectral transition that is simply prime-gap geometry.

## The first surviving bulk scale is the mean-prime-gap scale

A time horizon `T` resolves logarithmic frequency differences of size approximately

```text
1/T.
```

Near `p~X`, that corresponds to an ordinary additive window

```text
H~X/T.
```

The expected number of primes in such a window is approximately

```text
H/log X
 ~ X/(T log X).
```

The proven Hilbert--Schmidt estimate is the rigorous pair-sieve counterpart of this density calculation. As long as

```text
X/(T log X) ->0,
```

the normalized bulk is diagonal. The first scale at which this argument no longer forces collapse is

```text
T~X/log X,
```

where a Fourier cell has width

```text
H~log X
```

and contains order-one primes on average.

This is not a newly discovered arithmetic scale. Gallagher's 1976 theorem shows, conditional on the Hardy--Littlewood prime `k`-tuple conjectures, that the number of primes in randomly translated intervals of length

```text
lambda log X
```

converges to a Poisson law of mean `lambda`. Modern short-interval and prime-gap work develops exactly this regime.

Therefore a nontrivial prime-supported sharp-Gram limit at `T~X/log X`, if one is constructed, must confront the same local prime-point process: normalized gaps, singular-series correlations, and short-interval counting statistics. The finite-time Gram notation does not by itself create an additional route to the zeta zero divisor.

## Prime powers do not change the support-only bulk conclusion

The nonzero support of the von Mangoldt function in a macroscopic band consists of primes and prime powers. The number of powers `p^k~X` with `k>=2` is

```text
O(sqrt(X)).
```

Since

```text
M_X~X/log X,
```

this is `o(M_X)`. Adding all prime-power sites therefore changes an unweighted support Gram matrix by only `o(M_X)` rows and columns; by rank/interlacing, it does not change the limiting empirical spectral measure.

Thus the same `delta_1` bulk conclusion applies to the **unweighted prime-power support** throughout `X/log X << T <= X`.

This statement must not be confused with inserting the actual von Mangoldt amplitudes. The weighted vector

```text
Lambda(n)n^(-1/2)
```

is a different observable. `PL-075`--`PL-077` already show that its fixed-lag and long/smoothed channels lead to Hardy--Littlewood correlations, Selberg short-interval variance, and Montgomery zero pair correlation. The present finding closes only the support-only spectral escape.

## Prior art and novelty audit

The ingredients are classical and are not claimed as discoveries.

- **H. Halberstam, H.-E. Richert**, *Sieve Methods*, London Mathematical Society Monographs **4**, Academic Press, 1974, is a standard source for upper-bound sieve estimates for simultaneous primality of affine forms. It supplies the dimension-two prime-pair bound used above.
- **Ben Green, Terence Tao**, “Restriction theory of the Selberg sieve, with applications,” *Journal de Théorie des Nombres de Bordeaux* **18**(1) (2006), 147--182. DOI `10.5802/jtnb.538`, develops Selberg-sieve majorants for primes, twin primes, and prime `k`-tuples and is close harmonic-analysis prior art for prime-supported exponential systems.
- **James Maynard**, “Small gaps between primes,” *Annals of Mathematics* **181**(1) (2015), 383--413. DOI `10.4007/annals.2015.181.1.7`, proves in particular `liminf(p_(n+1)-p_n)<infinity`, supplying the unconditional extreme-eigenvalue subsequence.
- **P. X. Gallagher**, “On the distribution of primes in short intervals,” *Mathematika* **23**(1) (1976), 4--9. DOI `10.1112/S0025579300016442`, shows under the Hardy--Littlewood prime-tuple conjectures that prime counts on the `lambda log X` scale have Poisson limiting distribution.
- `PL-072`--`PL-080` already audit Montgomery--Vaughan, prolate/Slepian, Kac--Murdock--Szego, Ingham, and Landau sampling theory for the full integer support.

Searches around prime-supported Dirichlet-polynomial mean squares, Selberg-sieve restriction theory, nonharmonic Fourier sampling on prime frequencies, and bounded prime gaps did not locate a source stating the exact normalized-Hilbert--Schmidt/bounded-gap scale split above as a theorem. The durable line-specific content is therefore an **exact derived synthesis** of classical results, not a claim that the underlying sieve, gap, or sampling ingredients are new.

The novelty audit is negative for the RH mechanism: both sides of the split already have classical explanations. The bulk is controlled by sparse sampling density plus sieve pair bounds; the exceptional lower edge is controlled by bounded gaps; and the first unresolved bulk scale is exactly classical short-interval prime statistics.

## Adversarial boundaries

1. **No operator-norm convergence is claimed.** The bounded-gap argument proves that operator-norm closeness to the identity actually fails along suitable subsequences whenever `T=o(X)`, even though normalized Hilbert--Schmidt convergence holds in the stated intermediate range.
2. **No determinant limit follows from the bulk law.** A vanishing spectral fraction can dominate `log det`. `PL-080` already warns that determinant and smallest-eigenvalue scales can escape an empirical spectral law; prime support makes this concrete.
3. **The exact `T~X/log X` empirical law is open here.** Gallagher's Poisson theorem is conditional and concerns short-interval counts. It is prior-art evidence for what arithmetic scale has been reached, not a proof of a particular Gram spectral law.
4. **Actual von Mangoldt weights are excluded.** Weighting by `Lambda`, `Lambda/log`, Möbius data, or a distinguished target changes the observable and can import the classical correlation/explicit-formula channels of `PL-074`--`PL-077`.
5. **The result does not use the zeta continuation.** It therefore cannot itself localize zeros or distinguish `Re(s)=1/2` from another analytic boundary.
6. **The bulk no-go is not uniquely prime-specific.** Any sparse support with cardinality `asymp X/log X` and comparable averaged pair-count bounds has the same normalized Hilbert--Schmidt collapse. Rational-prime specificity enters only through finer gap/correlation data at or below the mean-spacing scale.
7. **Bounded gaps are an extreme, not bulk, discriminator.** They distinguish primes from a perfectly regular sparse control, but they are a theorem about local prime spacing and do not supply a spectral bridge to RH.

## Consequence for the prime-lattice search

The sharp finite-horizon branch now separates into three different information scales:

```text
full integer positive cone, T~X
    -> classical prolate/Nyquist bulk (PL-078--PL-080);

prime basis-direction support,
X/log X << T <= X
    -> bulk delta_1 by sieve sparsity;

prime basis-direction support,
T=o(X)
    -> rare bounded gaps can collapse the lower edge;

first bulk scale not ruled out:
T~X/log X
    -> mean prime gaps / short-interval prime statistics.
```

This is a material redirect. Simply replacing the full positive cone by the prime coordinate axes does introduce genuine arithmetic sparsity, but the first spectral effects are **prime-gap sampling phenomena**, not a mechanism connecting the exponent lattice to analytic continuation or to the Riemann critical line.

A surviving sharp-window route must therefore add something beyond support density and unpointed Gram spectrum: a distinguished arithmetic weight/target, an explicit-formula coupling, or another structure whose behavior at the mean-gap scale cannot be reproduced by generic sparse controls and whose relation to the zeta continuation is proved rather than inferred from sampling geometry.