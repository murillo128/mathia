# PL-016 — LCM join geometry gives a full-lattice tensor spectrum whose spectral zeta contains zeta, but not its zeros as operator spectrum

## Claim

A particularly literal self-adjoint operator built from the **full prime-exponent lattice**, not merely from the scalar energy `log n`, is already present in the literature. Hilberdink and Pushnitski study the LCM matrix

```text
E(sigma,tau)_{n,m} = n^sigma m^sigma / [n,m]^tau,
rho = tau - 2 sigma,
```

where `[n,m]` is the least common multiple. In exponent coordinates, `[n,m]` is the coordinatewise join

```text
v([n,m])_p = max(v_p(n),v_p(m)),
```

so

```text
E(sigma,tau)_{n,m}
 = product_p p^{sigma(v_p(n)+v_p(m))-tau max(v_p(n),v_p(m))}.
```

Thus the kernel factorizes exactly over prime axes and the operator is an infinite tensor product of one-prime operators. Under the hypotheses

```text
rho>0,  tau+rho>1,  tau>0,
```

the resulting operator on `ell^2(N)` is compact, self-adjoint, positive definite, has trivial kernel, and has pure-point spectrum with

```text
lambda_n(E) = kappa(sigma,tau) n^(-rho) + o(n^(-rho)),
E in S_q  <=>  q rho > 1.
```

More strongly, its spectral zeta

```text
Z_E(w) = Tr(E^w) = sum_n lambda_n(E)^w
```

has, initially for `Re(w)>1/rho`, the factorization

```text
Z_E(w) = zeta(rho w) G(w),
```

where the Euler-product correction `G` is analytic in

```text
Re(w) > s_0,
s_0 = max(1/(2 rho), (2-tau)/(2 rho)) < 1/rho.
```

Hence this identity supplies a meromorphic continuation of the scalar spectral-zeta function to that larger half-plane. For `tau>=1`, the proven analytic domain of `G` reaches exactly to the open half-plane

```text
Re(w) > 1/(2 rho),
```

whose image under `z=rho w` is `Re(z)>1/2`.

This is a substantial prior-art redirect for the prime-lattice spectral program: a natural positive self-adjoint operator using the coordinatewise lattice join already has an exact prime-axis tensor spectrum and already carries the Riemann zeta function as a factor of its spectral zeta. However, **the nontrivial zeros obtained after continuation are zeros in the complex spectral-zeta parameter, not eigenvalues or resonances of the positive operator itself**. Positivity/self-adjointness therefore does not turn this factorization into a Hilbert–Pólya mechanism.

**Evidence/status:** `LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION`.

The operator, tensor factorization, spectral theorem, Toeplitz limit, and spectral-zeta factorization are published results. The Mathia-specific derived conclusion is the boundary audit and category distinction: even a genuinely full-lattice, prime-factorized, positive self-adjoint construction can contain `zeta` in its analytically continued spectral zeta without spectrally localizing the Riemann zeros.

## Exact exponent-lattice geometry

Write

```text
n = product_p p^{k_p},
m = product_p p^{j_p}.
```

The divisibility lattice has coordinatewise meet and join

```text
v((n,m))_p = min(j_p,k_p),
v([n,m])_p = max(j_p,k_p).
```

Therefore the LCM kernel is

```text
K(j,k)
 = product_p K_p(j_p,k_p),
K_p(a,b)=p^{sigma(a+b)-tau max(a,b)}.
```

Hilberdink and Pushnitski make this factorization explicit:

```text
E(sigma,tau) = tensor_product_p E_p(sigma,tau),
(E_p)_{a,b}=p^{sigma(a+b)-tau max(a,b)}.
```

After diagonalizing each one-prime factor, the global eigenvalues themselves inherit the prime-exponent indexing. If

```text
n = product_p p^{k_p},
```

then, under a suitable enumeration,

```text
lambda_n(E) = product_p lambda_{k_p}(E_p).
```

This is much closer to the intrinsic geometry of the research line than an operator depending only on `log n`: the matrix distinguishes how two exponent vectors overlap through the coordinatewise `max`, so mixed-prime lattice points and their join structure participate directly.

The broader tensor-product principle is itself prior art: Hilberdink had already proved that infinite matrices whose entries are multiplicative functions of two variables decompose as infinite tensor products over primes.

## Published spectral theorem

Let `rho=tau-2 sigma`. Hilberdink and Pushnitski prove that if

```text
rho>0,
tau+rho>1,
tau>0,
```

then `E(sigma,tau)` is compact, positive definite, self-adjoint, and injective. Its ordered eigenvalues obey

```text
lambda_n(E)
 = kappa(sigma,tau) n^(-rho) + o(n^(-rho)),
```

with `kappa(sigma,tau)>0`. Consequently

```text
E in S_q  <=>  q rho > 1.
```

Unlike `PL-010`, whose canonical multiplicative Hilbert operator has purely absolutely continuous spectrum, this full-lattice LCM operator has genuine discrete positive eigenvalues. It therefore tests a different and stronger version of the spectral idea.

## Spectral-zeta factorization

Because the global eigenvalues are products of the local prime eigenvalues, for `Re(w)>1/rho` the ordinary trace of `E^w` factorizes as

```text
Z_E(w)
 = sum_n lambda_n(E)^w
 = product_p f_p(w),

f_p(w)=sum_{k>=0} lambda_k(E_p)^w.
```

The local asymptotics allow the authors to extract the ordinary zeta Euler factor:

```text
f_p(w) = (1-p^(-rho w))^(-1) G_p(w).
```

Thus

```text
Z_E(w)=zeta(rho w) G(w),
G(w)=product_p G_p(w),
```

initially in the trace-convergence region `Re(w)>1/rho`.

Their estimates prove that `G` is analytic for

```text
Re(w)>s_0,
s_0=max(1/(2 rho),(2-tau)/(2 rho)).
```

Combining this analytic `G` with the meromorphic continuation of `zeta(rho w)` gives a meromorphic continuation of the **scalar spectral-zeta function** into that half-plane. The pole at `w=1/rho` drives the eigenvalue-counting asymptotics through Wiener–Ikehara.

For `tau>=1`,

```text
s_0=1/(2 rho).
```

So the domain justified by this Euler-product estimate is

```text
Re(w)>1/(2 rho)
   <->
Re(rho w)>1/2.
```

This coincidence is exact but must be interpreted narrowly: `1/(2 rho)` is the boundary of the **proved analytic control for the correction product `G`**, not a theorem that `G` has a natural boundary there or cannot be continued farther.

## What happens to hypothetical off-line zeros

Suppose `z` is a nontrivial zeta zero with

```text
Re(z)>1/2.
```

For `tau>=1`, set `w=z/rho`. Then `Re(w)>1/(2rho)`, inside the proven continuation region, and

```text
Z_E(w)=zeta(z) G(w)=0.
```

Because `G` is analytic there, it cannot supply a pole that cancels the zero. Thus any hypothetical zero to the right of the critical line is inherited by the meromorphically continued spectral-zeta function.

The converse is not established: `G` may have its own zeros. More importantly, this implication does **not** place `Im(z)` in the spectrum of `E`. The operator has positive real eigenvalues `lambda_n(E)`; the complex variable `w` is the exponent in `Tr(E^w)`. A zero of a continued Dirichlet/Mellin transform of the eigenvalue measure is not an eigenvalue of the underlying self-adjoint operator.

This distinction is the decisive obstruction. Self-adjointness constrains `lambda_n(E)` to the real axis, but it does not imply that the analytic continuation of

```text
sum_n lambda_n(E)^w
```

is zero-free off any vertical line. Therefore the factor `zeta(rho w)` does not, by itself, yield the spectral localization needed for RH.

## Multiplicative Toeplitz connection and continuation audit

The case `tau=1` gives `rho=1-2sigma`. For every `sigma<1/2`, Hilberdink and Pushnitski prove that suitably rescaled finite multiplicative Toeplitz Gram matrices built from the coefficients `n^(-sigma)` converge in suitable Schatten norms to `E(sigma,1)`. This gives a concrete zeta-coefficient route to the LCM operator even when `sigma` lies left of `1/2`.

But the source is careful about analytic continuation. The infinite multiplicative Toeplitz operator with symbol

```text
psi_sigma(s)=zeta(sigma+s)
```

is justified in the straightforward Dirichlet-series/operator sense for `sigma>1`. For `sigma<=1`, the symbol is unbounded in the right half-plane and the authors explicitly note that associating the infinite Toeplitz operator to the analytically continued symbol is no longer straightforward. What remains unambiguous are the finite matrices defined directly from the coefficients.

This prevents an invalid inference of the form

```text
finite zeta-coefficient matrix
 -> infinite Toeplitz operator with analytically continued zeta symbol
 -> critical-strip spectral theorem.
```

The limit to `E(sigma,1)` is a rigorous coefficient-level spectral statement, not an automatic operator realization of analytic continuation.

## A built-in negative against over-reading the matrix spectrum

The same paper gives a useful falsification control. For `sigma<0`, the norm of the finite multiplicative Toeplitz matrix has the same growth order as

```text
sup_{|t|<=N} |zeta(sigma+it)|.
```

Nevertheless the **distributions do not agree**. Zeta exceeds a fixed fraction of the natural `N^(1/2-sigma)` scale on a set of heights of order `N`, whereas only `O(1)` singular values of the corresponding matrix exceed the matching scale.

So even where the operator norm tracks the largest zeta values correctly in scale, the spectral distribution is not a proxy for the value distribution of zeta. This is direct published evidence against interpreting the LCM/Toeplitz eigenvalue statistics as disguised zero or value statistics.

## Relation to previous prime-lattice findings

This finding fills a gap left by `PL-007` and `PL-010`.

- `PL-007` uses only the scalar energy `log n`; its canonical diagonal heat trace is zeta only in `Re(s)>1`.
- `PL-010` uses a non-diagonal multiplicative Hankel coupling through `log(mn)` but has purely absolutely continuous spectrum and samples zeta only in `Re>1`.
- The LCM matrix instead uses the **coordinatewise join of the full exponent vectors**, is compact positive with pure-point spectrum, tensorizes exactly over prime axes, and has a spectral zeta with an explicit ordinary-zeta factor.

Thus neither moving from diagonal to non-diagonal, nor retaining the full meet/join geometry, nor obtaining a discrete positive spectrum, nor even producing `zeta` as a factor of the spectral zeta is by itself enough to turn prime-lattice geometry into Hilbert–Pólya.

The result is also compatible with `PL-015`: tensorized multiplicative spectral data naturally sits close to generalized-prime theory. What must distinguish the Riemann case is still a genuinely global structure that does more than preserve free prime-wise factorization.

## Prior art and novelty assessment

- Hilberdink and Pushnitski's LCM operator, its prime tensor factorization, positivity/compactness, eigenvalue asymptotics, Schatten criterion, Toeplitz application, and spectral-zeta Euler-product analysis are published prior art.
- Hilberdink's 2017 tensor-product theorem establishes the broader principle that multiplicative-entry matrices decompose over prime coordinates.
- The appearance of the factor `zeta(rho w)` in the spectral-zeta analysis is explicitly in the proof of the published eigenvalue asymptotics; it is not a Mathia discovery.

The retained contribution is the audited research-line consequence: this literature already realizes a very strong version of the proposed “full exponent lattice -> self-adjoint tensor spectrum -> zeta” bridge, while simultaneously showing where the bridge stops. The Riemann zeros live in the analytic continuation of a scalar spectral-zeta function, not in the ordinary point spectrum of the self-adjoint lattice operator.

## Boundary conditions and failure modes

- `Z_E(w)=Tr(E^w)` is an ordinary trace series only for `Re(w)>1/rho`. Left of that line, `zeta(rho w)G(w)` is a meromorphic continuation of the scalar spectral zeta, not an ordinary operator trace.
- The continuation region stated here is only the region proved from the source's Euler-product estimates for `G`. No natural-boundary claim is made at `Re(w)=s_0`.
- The simple mapped critical boundary `Re(w)=1/(2rho)` is asserted only for `tau>=1`; for `tau<1`, the second term in `s_0` can dominate.
- Zeros of `G` can create extra zeros of the continued spectral zeta, so the zero divisor of `Z_E` is not proved to equal the scaled zeta-zero divisor.
- Positive/self-adjoint spectrum does not constrain zeros of the analytic continuation of its spectral zeta in the way Hilbert–Pólya would require.
- The finite Toeplitz matrices remain well-defined from Dirichlet coefficients for `sigma<=1`, but that does not justify an infinite Toeplitz operator whose symbol is obtained merely by analytic continuation of zeta.

## Audit / falsification criterion

A later researcher can audit this finding in five independent steps:

1. Verify coordinatewise that `v([n,m])=max(v(n),v(m))`, giving the local kernel `p^{sigma(a+b)-tau max(a,b)}`.
2. Verify from the primary paper the infinite tensor-product diagonalization and the product formula for global eigenvalues.
3. Verify the compact-positive spectral theorem and `S_q iff q rho>1`.
4. Verify in the proof of the eigenvalue asymptotics that `Tr(E^w)=zeta(rho w)G(w)` for `Re(w)>1/rho` and that `G` is analytic in `Re(w)>s_0` with the stated `s_0`.
5. Keep operator spectrum and spectral-zeta zeros separate. A claimed Hilbert–Pólya consequence must exhibit an additional theorem that converts the latter into the former or into a canonical resonance/positivity condition; the factorization alone does not do so.

A genuine escape would therefore need extra structure that makes the analytically continued spectral determinant/zeta control an actual spectral or positivity invariant, or a theorem extending and controlling `G` in a way that yields new information about zero localization. Simply observing the factor `zeta(rho w)` again is not such an escape.

## Consequence for the research line

One of the strongest literal versions of the prime-lattice spectral idea is already classical enough to be ruled out as a discovery and precise enough to sharpen the target:

```text
full exponent lattice
+ divisibility join/max geometry
+ exact prime tensor product
+ compact positive self-adjoint operator
+ pure-point spectrum
+ spectral-zeta factor zeta(rho w)
    !=
Riemann zeros as operator spectrum.
```

The useful surviving question is no longer whether the exponent lattice can produce a natural self-adjoint tensor operator carrying zeta — it can. The open requirement is a **global nonlocal mechanism** that turns completed analytic information into spectral localization on the self-dual line, rather than leaving the zeros inside the analytically continued complex parameter of an otherwise ordinary positive spectrum.
