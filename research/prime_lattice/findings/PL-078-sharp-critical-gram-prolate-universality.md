# PL-078 — The sharp critical sinc Gram limit is a classical prolate bandlimiting operator

## Claim

The oscillatory sharp-time kernel left outside the exact Gallagher localization of `PL-077` does **not** create a new spectral object at the local `N~T` resolution transition. The local sharp-window Gram limit already derived in `PL-072` is, after a diagonal phase gauge, exactly the classical discrete time-bandlimiting / prolate Toeplitz operator.

Let

```text
n_T/T -> x>0
```

and keep integer offsets `j,k` fixed. `PL-072` gives

```text
G_x(j,k)
 = exp(i(k-j)/(2x))
   sinc((k-j)/(2x)).
```

Conjugating by the diagonal unitary

```text
(U_x c)_j=exp(i j/(2x)) c_j
```

removes the phase and leaves the translation-invariant kernel

```text
K_x(j,k)=sinc((j-k)/(2x)).
```

It has the exact Fourier representation

```text
K_x(j,k)
 = integral_(-1/2)^(1/2)
     exp(i(j-k)u/x) du

 = x integral_(-1/(2x))^(1/(2x))
     exp(i(j-k)theta) dtheta.
```

Hence on `ell^2(Z)` the limiting Toeplitz operator is unitarily equivalent to multiplication on the circle by the periodized interval symbol

```text
m_x(theta)
 = 2 pi x
   sum_(ell in Z)
   1_[ -1/(2x), 1/(2x) ](theta+2 pi ell).
```

If

```text
r_x=1/(2 pi x),
q_x=floor(r_x),
```

then the periodized interval has multiplicity `q_x` or `q_x+1` almost everywhere. Therefore

```text
spectrum(K_x)
 subset { 2 pi x q_x,
          2 pi x (q_x+1) },
```

with only the values that occur on sets of positive measure retained. In particular, in the no-alias regime

```text
x>1/(2 pi),
```

one has

```text
K_x = 2 pi x P_x,
```

where `P_x` is the orthogonal Fourier projection onto the arc

```text
[-1/(2x),1/(2x)] subset (-pi,pi),
```

and consequently

```text
spectrum(K_x)={0,2 pi x}.
```

For every finite local block in this no-alias regime,

```text
(1/(2 pi x)) K_x(j,k)
 = sin(2 pi W_x (j-k))/(pi(j-k)),

W_x=1/(4 pi x),
```

with diagonal value `2W_x`. This is exactly Slepian's discrete prolate spheroidal (DPSS) concentration matrix. Its eigenvalue concentration near `1` and `0`, with about `2 M W_x=M/(2 pi x)` eigenvalues in the high-concentration cluster for an `M`-site block, is therefore classical time-bandwidth geometry.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE` for the route

```text
sharp rectangular observation window
+ local critical positive-cone Gram spectrum at n~xT
    -> new prime-lattice / RH-sensitive spectral invariant.
```

The conclusion is deliberately local and unweighted. It does **not** classify coefficient-dependent pointed quadratic forms, the whole macroscopic sharp band, or collective arithmetic information encoded by lags growing with `T`. It does close the more specific escape in which the oscillatory sinc tails of the sharp window are expected to produce, by their local Gram spectrum alone, a new arithmetic spectral phase at `N~T`.

## Exact Fourier multiplier

After removing the harmless phase from the `PL-072` kernel, write

```text
k_x(h)=sinc(h/(2x)),
h in Z.
```

The centered integral identity

```text
k_x(h)
 = integral_(-1/2)^(1/2) exp(i h u/x) du
 = x integral_(-1/(2x))^(1/(2x)) exp(i h theta) dtheta
```

is exact, including `h=0` by continuity.

Let `F:ell^2(Z)->L^2(T)` be the standard Fourier-series unitary. Periodizing the interval in the last integral shows that `k_x(h)` is the `h`-th Fourier coefficient of

```text
m_x(theta)
 =2 pi x sum_(ell in Z)
   1_[ -1/(2x),1/(2x) ](theta+2 pi ell).
```

Therefore

```text
F K_x F^*=M_(m_x).
```

No number-theoretic input occurs: this is ordinary Fourier duality for an equally spaced local frequency lattice.

The interval has length

```text
1/x=2 pi r_x.
```

Its periodic covering multiplicity is `q_x=floor(r_x)` or `q_x+1` almost everywhere. Thus the multiplier takes only

```text
2 pi x q_x=q_x/r_x
```

and

```text
2 pi x(q_x+1)=(q_x+1)/r_x.
```

When `r_x` is an integer, the covering multiplicity is constant and the operator is exactly the identity. When `0<r_x<1`, equivalently `x>1/(2 pi)`, the multiplier is `2 pi x` on one arc and `0` on its complement, so the operator is a scalar multiple of a projection.

This aliased/non-aliased distinction is sampling geometry only. It depends on the ratio `n/T` through the local spacing

```text
T(log(n+1)-log n) ~ 1/x,
```

not on the factorization of `n`.

## Exact identification with the discrete prolate matrix

Assume now

```text
x>1/(2 pi)
```

and set

```text
W_x=1/(4 pi x),
```

so `0<W_x<1/2`. The classical discrete bandlimiting matrix on a finite set of consecutive integer samples has entries

```text
B_W(j,k)
 = sin(2 pi W(j-k))/(pi(j-k))
```

with diagonal value `2W`.

Substituting `W=W_x` gives

```text
2 pi x B_(W_x)(j,k)
 = sinc((j-k)/(2x))
 = K_x(j,k).
```

Thus every finite section of the phase-gauged local limit is **exactly** a scalar multiple of the DPSS/prolate concentration matrix. Slepian's discrete theory studies precisely the eigenvectors and eigenvalues of this matrix as the spectral-concentration problem for a finite discrete time series.

The trace already gives the correct Shannon count. For an `M x M` block,

```text
Tr K_x=M.
```

Since the high cluster lies near `2 pi x`, the number of high-concentration eigenvalues is asymptotically

```text
M/(2 pi x)=2 M W_x,
```

which is the classical time-bandwidth/Shannon number. The remaining bulk lies near zero, with only the familiar prolate transition region between the two clusters.

Consequently the striking sharp-window spectral separation is not evidence for a hidden Riemann spectrum. It is the standard spectrum of a finite time / finite bandwidth concentration operator.

## Relation to the exact `PL-072` Gram matrix

The statement above concerns the limit obtained after fixing local offsets and sending `T->infinity`. It does not silently replace the exact logarithmic Gram matrix by an arithmetic progression.

For

```text
n_T/T -> x
```

and fixed `j,k`, Taylor expansion gives

```text
T log((n_T+k)/(n_T+j))
 =(k-j)/x+o(1),
```

which is exactly the derivation already audited in `PL-072`. Therefore every fixed finite Gram block converges entrywise, hence in operator norm, to the corresponding finite prolate block after diagonal phase conjugacy.

One may also let the local block grow slowly with `T`, but the required uniform error bookkeeping then depends on the chosen growth rate and is not part of this finding. No simultaneous thermodynamic-limit theorem is being smuggled into the fixed-block statement.

This boundary matters: a macroscopic fraction of the full `n~T` band samples the curvature of `log n`, so it is not one stationary prolate Toeplitz matrix. The present result rules out **local sharp-kernel spectral novelty**, not every global sharp-band observable.

## Prior-art and novelty audit

No novelty is claimed for the sinc projection, the discrete prolate matrix, its time-bandwidth interpretation, or its eigenvalue concentration.

- **David Slepian**, “Prolate Spheroidal Wave Functions, Fourier Analysis, and Uncertainty—V: The Discrete Case,” *Bell System Technical Journal* **57**(5) (1978), 1371–1430, DOI `10.1002/j.1538-7305.1978.tb02104.x`, is the primary classical source for DPSS/DPSWF theory and the discrete time/frequency concentration problem.
- The preceding `PL-072` already derives the local sinc Gram kernel from the sharp finite-time Dirichlet-character family and proves that the same kernel occurs for the non-arithmetic control frequencies `log(n+theta)`.

The only line-specific contribution stored here is the collision audit between those two facts: the remaining sharp local kernel is not merely *similar* to a familiar Fourier kernel; after the elementary diagonal gauge it is exactly the prolate concentration matrix, and its bilateral limit is a periodized interval multiplier. Therefore its local spectral clustering is imported wholesale from classical sampling theory.

A targeted literature audit around the sinc Toeplitz matrix, discrete prolate spheroidal sequences, time-band limiting, and spectral concentration recovered Slepian's mature theory rather than a zeta-specific operator attached to prime exponents.

## Adversarial and rational-prime controls

Several boundaries prevent the negative conclusion from being overextended.

1. **Prime factorization is absent.** The derivation uses only `log(n+k)-log(n+j)~(k-j)/n`. The matched family `log(n+theta)` from `PL-072` produces the same local operator.
2. **The diagonal phase is pure gauge.** Conjugating by `U_x` changes no eigenvalue, singular value, determinant, condition number, or other unitary spectral invariant.
3. **Sharp oscillatory tails are retained.** Unlike the compact triangular gap kernel in `PL-077`, the sinc kernel has its full `1/h` oscillatory tail. The reduction to the prolate operator therefore does not discard the feature being tested.
4. **Coefficient-dependent observables remain outside the no-go.** Multiplying the characters by `Lambda`, square-free support, a fixed target vector, or another non-unimodular arithmetic coefficient turns the Gram spectrum into a pointed/weighted question not classified by the bare prolate operator.
5. **Macroscopic curvature remains outside the no-go.** The full band `aT<n<=bT` has a slowly varying local parameter `x=n/T`; a global statistic may couple many such local blocks. Calling the whole matrix one DPSS operator would be false.
6. **No analytic continuation occurs.** Everything here is a finite-time Fourier limit. It neither uses nor produces the zeta functional equation, explicit formula, or zero divisor.
7. **The alias regime is also universal.** For `x<=1/(2 pi)`, the bilateral multiplier is the elementary periodic covering count displayed above, not a hidden arithmetic spectrum.

These controls leave a clear falsification test. If a proposed RH mechanism at the `N~T` transition depends only on eigenvalue concentration of the local sharp rectangular-window Gram matrix, then replacing the prime-exponent indexing by the matched logarithmic control preserves the same prolate spectrum. Such a mechanism cannot distinguish the rational-prime norm map.

## Consequence for the current finite-horizon branch

The local quadratic geometry is now classified for both canonical observation windows:

```text
sharp rectangular time window
    -> oscillatory sinc kernel
    -> local DPSS / prolate concentration spectrum;

Gallagher sinc^2 time smoothing
    -> compact triangular log-gap kernel
    -> exact logarithmic boxes / short-interval variance (`PL-077`).
```

Both are classical Fourier-resolution structures before arithmetic coefficients are inserted. The sharp kernel's long oscillatory tail is therefore not, **at the local Gram-spectral level**, a surviving source of Riemann-specific rigidity.

A useful continuation of this branch must use information not contained in that unweighted local spectrum: a genuinely global sharp-band coupling, a distinguished arithmetic target/coefficient, completion or functional-equation data, or a higher-order invariant that survives the existing Dirichlet-polynomial/correlation reductions and the line's Helson/Beurling controls.
