# PL-113 — Relative log-prime pair kernels scalarize to vertical prime-zeta power spectra

## Claim

One explicit escape left open by `PL-112` can be closed for a broad and natural class of pair interactions. Fix a depth `l>=1` and let `K:R->C` be a bounded even Fourier--Stieltjes kernel,

```text
K(x)=integral_R exp(i t x) dnu(t),
```

where `nu` is a finite symmetric complex measure. Define the depth-`l` pair observable on the exponent lattice by

```text
C_(l,K)(n)
 = sum_(p<q,
        v_p(n)>=l,
        v_q(n)>=l)
     K(log p-log q).
```

Then, for `Re(s)>1`, its Dirichlet transform factors exactly as

```text
sum_(n>=1) C_(l,K)(n) n^(-s)
 = zeta(s) Q_(l,K)(s),
```

with

```text
Q_(l,K)(s)
 = 1/2 integral_R
     [ P(ls-it) P(ls+it) - P(2ls) ]
     dnu(t),
```

where

```text
P(z)=sum_p p^(-z)
```

is the prime zeta function in its half-plane of absolute convergence.

Thus a fixed-depth pair coupling whose prime-label dependence uses only the **relative logarithmic energy** `log p-log q` does not retain a new two-coordinate operator invariant. Fourier diagonalization turns it into an average of scalar vertical prime-zeta products. For real `s=sigma>1` and a positive symmetric measure `nu`, the first product is the ordinary scalar power spectrum

```text
P(l sigma-it)P(l sigma+it)=|P(l sigma+it)|^2.
```

The constant kernel `K=1` reduces to

```text
Q_(l,1)(s)
 = 1/2 [P(ls)^2-P(2ls)],
```

which is exactly the `k=2` elementary-symmetric case of `PL-112`. The present finding therefore closes the most direct **translation-invariant relative-energy pair-kernel** extension of that fixed-degree branch.

**Evidence/status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION`, decisive only for fixed depth and bounded even Fourier--Stieltjes kernels depending on `log p-log q`. No novelty is claimed for Fourier--Stieltjes/Bochner diagonalization or for prime-zeta continuation. The line-specific result is the exact collision between that classical harmonic mechanism and the surviving pair-kernel escape recorded in `PL-112`.

## Exact derivation in the absolutely convergent region

For distinct primes `p,q`, the condition

```text
v_p(n)>=l,
v_q(n)>=l
```

is equivalent to `p^l q^l | n`. Hence, for `sigma=Re(s)>1`, absolute convergence gives

```text
sum_(n>=1,
     p^l q^l|n)
  n^(-s)
 = (pq)^(-ls) zeta(s).
```

Because `K` is bounded and

```text
sum_(p<q) (pq)^(-l sigma)
 < infinity
```

when `l sigma>1`, Fubini is legitimate and

```text
sum_n C_(l,K)(n)n^(-s)
 = zeta(s)
   sum_(p<q)
     K(log p-log q)(pq)^(-ls).
```

Write `a=ls`. Evenness of `K` lets the unordered pair sum be replaced by one half of the ordered off-diagonal sum:

```text
sum_(p<q) K(log p-log q)(pq)^(-a)
 = 1/2 sum_(p!=q)
     K(log p-log q)p^(-a)q^(-a).
```

Insert the Fourier--Stieltjes representation. Since `nu` is finite and `Re(a)>1`, the prime sums converge uniformly in the Fourier variable in absolute value, so Fubini again applies:

```text
sum_(p,q)
  p^(-a)q^(-a)
  exp(it(log p-log q))
 = P(a-it)P(a+it).
```

The diagonal `p=q` contributes `P(2a)`. This proves

```text
Q_(l,K)(s)
 = 1/2 integral_R
     [P(ls-it)P(ls+it)-P(2ls)]
     dnu(t).
```

Nothing from analytic continuation has entered the derivation. The formula is initially an identity only in `Re(s)>1`.

## A genuine continuation window exists without continuing the prime-zeta integral

The pair factor also has the direct absolutely convergent representation

```text
Q_(l,K)(s)
 = sum_(p<q)
     K(log p-log q)(pq)^(-ls).
```

Since `K` is bounded, this defines a holomorphic function whenever

```text
Re(s)>1/l.
```

Therefore the identity obtained in `Re(s)>1` supplies a genuine meromorphic continuation

```text
D_(l,K)(s)
 := zeta(s)Q_(l,K)(s)
```

through the larger half-plane `Re(s)>1/l`, using the classical meromorphic continuation of `zeta` and uniqueness of analytic continuation. This point is independent of any branch choice for the continued prime zeta function.

The location of the resulting boundary is controlled by the **depth** rather than by RH:

```text
l=1:  Q is guaranteed only for Re(s)>1;
l=2:  Q is guaranteed for Re(s)>1/2;
l>=3: Q is absolutely convergent on and across Re(s)=1/2.
```

For `l>=3`, every ordinary zeta zero in this half-plane is inherited through the naked factor `zeta(s)`. The pair factor may have additional zeros of its own, but it does not localize the Riemann zeros: their appearance in the continued Dirichlet transform has already been inserted by the scalar factor inherited from the unrestricted remainder of the integer lattice.

For `l=2`, the critical half-line coincides with the elementary convergence boundary `l Re(s)=1` of the prime sum. That coincidence is a depth-rescaled prime-harmonic threshold, not evidence for a Hilbert--Polya or self-duality mechanism. For `l=1`, even this coincidence disappears.

## Scalar prime-zeta continuation and its limitation

Fröberg's classical prime-zeta theory gives, on appropriate branch domains in `Re(z)>0`,

```text
P(z)
 = sum_(m>=1) mu(m)/m * log zeta(mz).
```

Consequently, for a **finite discrete** Fourier measure `nu`, the displayed formula for `Q_(l,K)` continues locally as a finite combination of shifted scalar prime-zeta functions wherever a common branch domain exists. Its singularities are inherited from the pole and zeros of scalar zeta through the standard prime-zeta logarithmic singularity pattern.

No stronger claim is made for an arbitrary continuous measure `nu`. One cannot simply move the prime-zeta continuation under the `t`-integral without uniform branch and integrability control. The direct double-prime representation above is the rigorous continuation statement used by this finding.

This distinction prevents the usual invalid step of transporting an Euler-product or prime-zeta identity from `Re(s)>1` into the critical strip by formal algebra.

## Generic free-monoid control

The same reduction is not special to rational primes. Let a free commutative monoid have generator energies

```text
lambda_1, lambda_2, ... >0,
```

and define

```text
P_lambda(z)=sum_j exp(-z lambda_j),

Xi_lambda(s)
 = product_j (1-exp(-s lambda_j))^(-1)
```

where these expressions converge. For the analogous depth-`l` pair observable with kernel `K(lambda_j-lambda_k)`, the identical calculation gives

```text
D_(lambda,l,K)(s)
 = Xi_lambda(s)/2
   integral_R
     [P_lambda(ls-it)P_lambda(ls+it)
      -P_lambda(2ls)]
     dnu(t).
```

Thus the mechanism depends only on three generic pieces:

```text
free commutative factorization,
additive generator energies,
Fourier diagonalization of energy differences.
```

It does not by itself distinguish `lambda_p=log p` from a broader multiplicative-frequency system. The rational primes enter only through the chosen scalar generator sum `P_lambda=P` and the monoid partition function `Xi_lambda=zeta`.

This is the line-specific falsification control required by the research mandate. A proposed RH mechanism that uses only this pair-kernel architecture must identify additional rational-prime structure not present in the generic formula above.

## Relation to earlier findings

`PL-112` showed that fixed-degree **symmetric count** couplings of the depth occupancies scalarize through Newton identities to `P(ls),...,P(kls)`. It explicitly left prime-label-dependent pair kernels as a possible escape. The present result closes the natural subfamily in which label dependence is translation invariant in the logarithmic energy coordinate.

`PL-081` already studies a different occurrence of a relative-log kernel,

```text
sinc((T/2)log(p/q)),
```

in a finite-time Gram matrix on the prime basis and routes its critical scale to prime-gap/short-interval statistics. `PL-113` does not claim that log-ratio kernels are new. Its object is instead a divisibility/depth observable on full exponent vectors and its conclusion is an exact Dirichlet-transform scalarization. The two findings therefore provide complementary controls: finite-time prime-support Gram geometry can expose additive prime-gap statistics, whereas a fixed-depth global Dirichlet transform of a Fourier-diagonalizable relative-energy pair interaction collapses to scalar prime-zeta vertical products.

`PL-003` remains a separate stronger warning against interpreting generic prime-phase harmonic structure as Riemann-zero rigidity: Helson-type phase twists preserve the ambient multiplicative frequency geometry while allowing radically different divisors.

## Prior-art and novelty audit

The number-theoretic scalar object is classical. Carl-Erik Fröberg, “On the prime zeta function,” *BIT Numerical Mathematics* **8**(3) (1968), 187--202, DOI `10.1007/BF01933420`, is already recorded in `research/prime_lattice/SOURCES.md` as the main prime-zeta continuation anchor. Fourier--Stieltjes representation and the Bochner theorem for positive-definite kernels are standard harmonic analysis.

A targeted literature search for prime-zeta mean squares, vertical products, Fourier kernels on prime logarithms, and pair-correlation formulations did not locate a theorem whose mathematical content is the present depth-divisibility observable. Nearby literature instead falls into established but different channels: multiple/almost-prime zeta functions, multiplicative Toeplitz/Helson matrices, and prime/zero pair-correlation theory. Accordingly, no literature novelty is claimed for the algebraic identity itself. Its durable value is a **negative route classification**: an explicit open branch from `PL-112` reduces to known scalar harmonic data and passes the generic-free-monoid falsification control in the wrong direction.

## Adversarial controls and limitations

1. **Fixed depth is essential.** If `l` grows with a cutoff, observation scale, or spectral parameter, the threshold `Re(s)>1/l` moves and the reduction need not control the resulting asymptotic regime uniformly.
2. **Translation invariance in log energy is essential.** A kernel depending genuinely on the identities of `p` and `q`, on congruence data, on local fields, or on a non-translation-invariant two-prime invariant is not covered.
3. **Fourier--Stieltjes regularity is essential.** Singular kernels outside this bounded class may require a different transform theory or renormalization. The finding does not rule them out.
4. **Pair degree is fixed.** Higher interaction degree with degree growing in the problem size is not reduced here. Fixed higher degree with suitable translation-invariant kernels may admit analogous Fourier reductions, but that requires a separate statement.
5. **Scalarization is not triviality.** `P(ls-it)P(ls+it)` contains genuine rational-prime information and, after continuation where justified, inherits zeta singularities. The negative claim is that this information is carried by scalar prime-zeta data and generic free-monoid harmonic structure, not that the function is elementary.
6. **Positivity is generic.** If `K` is continuous positive definite, Bochner represents it by a positive measure, so any positivity of the underlying kernel matrix comes from a general harmonic theorem. Such positivity alone cannot single out RH.
7. **No zero-free statement follows.** Even for `l>=3`, `Q_(l,K)` can have its own zeros. The factorization does not prove that zeros of the complete transform coincide with zeta zeros, and it gives no mechanism forcing the latter to `Re(s)=1/2`.
8. **No formal continuation under an integral.** For continuous `nu`, the Fourier--prime-zeta integral is used only in its absolute-convergence domain unless separate uniform continuation estimates are supplied.

## Consequence for the research line

The surviving pair-interaction target after `PL-112` can now be sharpened. Merely replacing the symmetric count `binom(omega_l,2)` by a fixed kernel of the relative energy

```text
log p-log q
```

does not escape scalarization when that kernel is Fourier--Stieltjes. The next credible pair route must use at least one ingredient that the generic free-monoid identity destroys: absolute prime labels, genuinely arithmetic two-prime relations, non-translation-invariant local/global data, interaction degree or depth that grows with scale, or a distinguished target/operator whose positivity is not a generic Bochner consequence.

In particular, **relative log-energy geometry alone is not enough**. Its natural harmonic diagonalization is already the scalar vertical prime-zeta power spectrum.