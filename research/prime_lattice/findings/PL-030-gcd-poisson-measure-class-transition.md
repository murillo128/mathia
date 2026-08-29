# PL-030 — The weighted exponent metric is the classical GCD–Poisson kernel; its `1/2` phase change is measure-class geometry, not zero localization

## Claim

The most canonical translation-radial positive kernel built from the exact prime-exponent geometry is already classical GCD-sum/Poisson-kernel structure.

For positive integers `m,n`, define the weighted `l1` exponent distance

```text
d_log(m,n)
  = sum_p |v_p(m)-v_p(n)| log p.
```

Then

```text
d_log(m,n)
  = log([m,n]/(m,n)),
```

and for every `sigma>0`

```text
K_sigma(m,n)
  = exp(-sigma d_log(m,n))
  = product_p p^(-sigma |v_p(m)-v_p(n)|)
  = (gcd(m,n))^(2 sigma)/(mn)^sigma.
```

Thus the radial kernel of the exact weighted exponent lattice is precisely the normalized generalized GCD kernel studied in the classical GCD-matrix literature. It is also the `rho=0`, `tau=2 sigma` boundary of the LCM family in `PL-016`, outside that finding's compact-operator regime `rho>0`.

The kernel has an exact harmonic realization on the infinite prime torus. Let `nu_sigma` be the product of one-circle Poisson probability measures with radii

```text
r_p = p^(-sigma).
```

The Fourier coefficient of the one-prime Poisson measure at frequency `k` is `r_p^|k|`; hence, for every finitely supported integer vector `gamma`,

```text
nu_sigma_hat(gamma)
  = product_p p^(-sigma |gamma_p|).
```

Taking `gamma=v(m)-v(n)` gives

```text
nu_sigma_hat(v(m)-v(n)) = K_sigma(m,n).
```

So every finite GCD matrix is a Gram matrix of prime-torus characters in `L^2(nu_sigma)`. This is the infinite-product version of the Poisson-integral representation used by Aistleitner–Berkes–Seip for GCD sums.

The product measure itself has a genuine phase transition exactly at the critical exponent:

```text
nu_sigma equivalent to product Haar  <=>  sigma>1/2,
nu_sigma singular to product Haar    <=>  0<sigma<=1/2.
```

This follows from Kakutani's product-measure criterion because the Hellinger affinity `h(r)` between the one-circle Poisson measure of radius `r` and Haar satisfies

```text
h(r)=1-r^2/4+O(r^4),
```

while

```text
sum_p r_p^2 = sum_p p^(-2 sigma)
```

converges exactly for `sigma>1/2`.

Thus `Re(s)=1/2` really is singled out by a nontrivial harmonic property of the exact prime-weighted exponent lattice: it is the boundary where its canonical product-Poisson spectral measure leaves the Haar measure class.

However, this phase transition is **unconditional and zero-blind**. Along the vertical Kronecker flow, changing `t` only rotates the Poisson centers. On every finite integer set the corresponding Gram matrices are diagonal-unitarily conjugate,

```text
K_(sigma,t)(m,n)
  = exp(-it(log m-log n)) K_sigma(m,n),

K_(sigma,t) = D_t K_(sigma,0) D_t^*,
(D_t)_(n,n)=n^(-it).
```

Therefore their eigenvalues, singular values and determinants are independent of `t`. No Riemann-zero ordinate can be selected by this canonical Poisson/GCD Gram spectrum.

There is also no hidden determinant-zero mechanism at the critical radius. For the truncation `{1,...,N}`, incidence/Möbius factorization gives

```text
det [K_sigma(m,n)]_(m,n<=N)
  = product_(n<=N) J_(2 sigma)(n)/n^(2 sigma)
  = product_(n<=N) product_(p|n) (1-p^(-2 sigma))
  > 0,
```

where `J_a=id^a*mu` is the generalized Jordan totient. At `sigma=1/2`,

```text
det K_(1/2,N) = product_(n<=N) phi(n)/n > 0.
```

Hence the critical `1/2` phenomenon here is a change of infinite-product measure class, not a vanishing finite spectral determinant.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE` for the route

```text
weighted exponent-lattice l1 metric
    -> canonical positive radial / GCD kernel
    -> Poisson spectral measure or finite Gram spectrum
    -> critical-line or zero-ordinate localization.
```

The negative is deliberately narrow. Weighted/nonlocal kernels that add the completed Weil distribution, archimedean/adelic Fourier duality, a nontrivial boundary correction, or other information not determined by `|v_p(m)-v_p(n)| log p` are outside it.

## Exact exponent-lattice identity

Unique factorization gives

```text
m = product_p p^(a_p),
n = product_p p^(b_p).
```

Coordinatewise,

```text
v_p([m,n]) = max(a_p,b_p),
v_p((m,n)) = min(a_p,b_p),

max(a_p,b_p)-min(a_p,b_p)=|a_p-b_p|.
```

Therefore

```text
log([m,n]/(m,n))
  = sum_p |a_p-b_p| log p
  = d_log(m,n).
```

Using `[m,n](m,n)=mn`,

```text
exp(-sigma d_log(m,n))
 = ((m,n)/[m,n])^sigma
 = (m,n)^(2 sigma)/(mn)^sigma.
```

This makes the relation to `PL-016` exact. In the notation

```text
E(alpha,tau)_(m,n)=m^alpha n^alpha/[m,n]^tau,
rho=tau-2 alpha,
```

choose

```text
alpha=sigma,
tau=2 sigma,
rho=0.
```

Then `E(sigma,2 sigma)=K_sigma`. The compact spectral theorem of `PL-016` assumes `rho>0`, so the normalized GCD kernel is a genuine boundary case rather than a duplicate of its discrete compact spectrum.

## Poisson spectral representation

For `0<r<1`, write the normalized Poisson kernel on the unit circle as

```text
P_r(theta)
 = (1-r^2)/|1-r exp(i theta)|^2.
```

With normalized Haar measure `dm`, its Fourier coefficients are

```text
integral exp(-ik theta) P_r(theta) dm(theta) = r^|k|.
```

For `sigma>0`, let

```text
nu_sigma
 = tensor_product_p [P_(p^(-sigma))(theta_p) dm(theta_p)].
```

Every character of the infinite torus has finite support, so Fubini on that finite support gives exactly

```text
integral z^gamma dnu_sigma(z)
 = product_p p^(-sigma |gamma_p|).
```

For the characters `chi_n(z)=z^(v(n))`,

```text
<chi_m,chi_n>_(L2(nu_sigma))
 = K_sigma(m,n).
```

Consequently, for every finite Dirichlet polynomial

```text
F(z)=sum_n c_n z^(v(n)),
```

one has the exact quadratic identity

```text
integral |F(z)|^2 dnu_sigma(z)
 = sum_(m,n) c_m conjugate(c_n)
     gcd(m,n)^(2 sigma)/(mn)^sigma.
```

Aistleitner, Berkes and Seip use precisely this Poisson-polydisc representation to study GCD sums and the largest eigenvalues of their matrices. In their published analysis the behavior changes sharply on crossing `alpha=1/2`, because `sum_p p^(-2 alpha)` changes from convergent to divergent; they emphasize that `alpha=1/2` is the delicate endpoint.

## Kakutani makes the `1/2` boundary a measure-class theorem

Let `m_infty` be product Haar measure. Every local Poisson measure is mutually absolutely continuous with Haar. Kakutani's theorem says that the two infinite products are either equivalent or mutually singular, with the alternative controlled by the product of local Hellinger affinities.

For one factor define

```text
h(r)=integral sqrt(P_r(theta)) dm(theta).
```

A direct Taylor expansion at `r=0` gives

```text
sqrt(P_r(theta))
  = 1 + r cos(theta)
      + r^2((3/2)cos(theta)^2-1)
      + O(r^3),
```

and averaging gives

```text
h(r)=1-r^2/4+O(r^4).
```

(The function `h` is even, so the odd averaged terms vanish.) Hence for all sufficiently small `r`,

```text
c r^2 <= 1-h(r) <= C r^2
```

with absolute positive constants `c,C`.

Only finitely many primes have `p^(-sigma)` outside that small-radius range, so Kakutani reduces the global question to

```text
sum_p (1-h(p^(-sigma))) < infinity
  <=> sum_p p^(-2 sigma) < infinity
  <=> sigma>1/2.
```

This is an exact infinite-dimensional geometric meaning of the critical exponent. It requires no analytic continuation of `zeta`, no functional equation and no information about its zeros.

There is now an independent machine-checked novelty control for this exact combination. The public Lean repository `idolum-ai/riemann-venue` proves `poissonProduct_dichotomy`: its product Poisson measures at radii `p^(-sigma)` are singular to product Haar iff `sigma<=1/2` and equivalent above. The same repository proves that the Fourier coefficient at `sigma=1/2` is the normalized GCD kernel `gcd(m,n)/sqrt(mn)`. Commit `5bd65e6c496cf9f81e4efe5e290a5531f7cc0bd5` (8 July 2026) introduced the dichotomy theorem. This repository is a formal research artifact rather than a peer-reviewed publication, so the mathematical authority for the present finding remains Kakutani plus the classical Poisson/GCD identities; its role here is to remove any plausible novelty claim for assembling these ingredients.

## Vertical flow is spectrally invisible to the finite GCD Gram family

The Bohr/Kronecker vertical flow is

```text
T_t(z)_p = exp(-it log p) z_p.
```

Moving the Poisson pole by this flow replaces the Fourier coefficient at `gamma` by

```text
exp(-it <gamma,log p>) nu_sigma_hat(gamma).
```

For `gamma=v(m)-v(n)`,

```text
<gamma,log p> = log m-log n,
```

so

```text
K_(sigma,t)(m,n)
 = m^(-it) n^(it) K_sigma(m,n).
```

On any finite set `A` of integers this is exactly

```text
K_(sigma,t)|_A
 = D_t [K_(sigma,0)|_A] D_t^*,
```

with `D_t` unitary diagonal. Thus all ordinary spectral invariants of the finite Gram family are constant along the full vertical orbit.

This gives a particularly clean falsification test for a tempting proposal:

```text
look for t at which the canonical prime-torus Poisson/GCD matrix
changes spectrum, becomes singular, or develops a determinant zero.
```

It cannot happen. The entire `t` dependence is a gauge conjugation.

This does **not** say that zeta values themselves are spectrally invisible to all GCD matrices. Bondarenko and Seip famously use the critical GCD kernel in the resonance method to obtain large values of `|zeta(1/2+it)|`. That is an important positive use of the kernel. But resonance combines the GCD quadratic form with a deliberately chosen Dirichlet polynomial and analytic mean-value arguments; the zero/value information is not encoded in a `t`-dependent eigenvalue of the bare kernel.

## Finite determinant factorization

There is also a purely finite incidence proof that no determinant zero emerges at the critical radius.

For `a>0`, define

```text
G_a(m,n)=gcd(m,n)^a.
```

Let

```text
J_a = id^a * mu.
```

Möbius inversion gives

```text
n^a = sum_(d|n) J_a(d),
```

hence

```text
gcd(m,n)^a
 = sum_(d|m, d|n) J_a(d).
```

On `{1,...,N}`, let `C_(d,n)=1_(d|n)`. Since `C` is triangular with ones on the diagonal,

```text
G_a = C^T diag(J_a(1),...,J_a(N)) C
```

and therefore

```text
det G_a = product_(n<=N) J_a(n).
```

Now set `a=2 sigma` and normalize by `D_(n,n)=n^(-sigma)`:

```text
K_sigma = D G_(2 sigma) D.
```

Since

```text
J_(2 sigma)(n)
 = n^(2 sigma) product_(p|n)(1-p^(-2 sigma)),
```

we obtain

```text
det K_sigma
 = product_(n<=N) product_(p|n)(1-p^(-2 sigma)) > 0.
```

At `sigma=1/2`, this becomes the classical Smith/Euler-totient factorization

```text
det K_(1/2)
 = product_(n<=N) phi(n)/n > 0.
```

So the finite kernel remains strictly positive definite exactly where its infinite spectral measure becomes singular to Haar. The two phenomena must not be conflated.

## Novelty audit

Primary literature anchors:

- Christoph Aistleitner, Istvan Berkes, Kristian Seip, **“GCD sums from Poisson integrals and systems of dilated functions,”** *Journal of the European Mathematical Society* **17**(6) (2015), 1517–1546. DOI `10.4171/JEMS/537`. They study exactly the kernel `gcd(m,n)^(2 alpha)/(mn)^alpha`, identify its quadratic forms as Poisson integrals on a polydisc, obtain spectral-norm bounds, and isolate `alpha=1/2` as the delicate transition associated with divergence of `sum_p p^(-2 alpha)`.
- Shizuo Kakutani, **“On equivalence of infinite product measures,”** *Annals of Mathematics* (2) **49** (1948), 214–224. DOI `10.2307/1969123`. Classical product-measure equivalence/singularity criterion used for the measure-class dichotomy.
- Peter Lindqvist, Kristian Seip, **“Note on some greatest common divisor matrices,”** *Acta Arithmetica* **84**(2) (1998), 149–154. DOI `10.4064/aa-84-2-149-154`. Classical GCD-matrix/spectral context including the Smith determinant tradition.
- Andriy Bondarenko, Kristian Seip, **“Large greatest common divisor sums and extreme values of the Riemann zeta function,”** *Duke Mathematical Journal* **166**(9) (2017), 1685–1701. DOI `10.1215/00127094-0000005X`. Demonstrates that the critical normalized GCD kernel is genuinely useful for zeta **large-value** resonance, while not turning its bare spectrum into a zero-localization mechanism.
- `idolum-ai/riemann-venue`, `RiemannVenue/Kakutani/PoissonDichotomy.lean` and `RiemannVenue/Kakutani/SpectralMeasure.lean`, public Lean 4 formal research artifact, accessed 29 August 2026. It independently machine-checks the product-Poisson/Haar dichotomy and the critical GCD Fourier coefficient. It is used only as a modern novelty/formalization control, not as a substitute for peer-reviewed mathematical sources.

No novelty is claimed for GCD matrices, Poisson integral representations, Kakutani's theorem, Smith's determinant identity, or the `1/2` square-summability transition. The exact exponent-distance identification is elementary. The useful research-line result is the combined obstruction: **the most canonical positive radial geometry supplied by `|v(m)-v(n)|` really does produce a sharp harmonic phase boundary at `1/2`, but its ordinary finite spectrum is gauge-invariant along the vertical prime flow and therefore cannot locate zeta zeros.**

## Boundary of the obstruction

This finding does not rule out every weighted lattice construction.

It does not cover:

- a kernel that uses signs/orientation, Möbius data, or more than the absolute coordinate difference `|v_p(m)-v_p(n)|`;
- a nonlocal coupling between different prime axes rather than a product of one-prime radial kernels;
- an archimedean/adelic completion implementing the Fourier–Mellin duality of `PL-014`;
- a completed Weil quadratic form, where prime powers are coupled to the zero distribution through additive Fourier analysis and the gamma factor;
- scattering, relative determinants, or resonances against a noncompact reference operator;
- analytic observables built from a chosen resonator, where the GCD kernel is only one ingredient rather than the whole zero mechanism.

The public formalization mentioned above in fact goes beyond the static dichotomy into translated product-measure singularity and completed-Weil experiments. Those claims should be audited separately before being imported; their existence is nevertheless a warning that the bare GCD/Poisson critical-boundary route is already a developed research program rather than unexplored prime-lattice territory.

## Audit / falsification tests

The finding can be falsified or materially narrowed by any of the following:

1. `d_log(m,n)` fails to equal `log([m,n]/(m,n))`;
2. `exp(-sigma d_log)` fails to equal the normalized GCD kernel;
3. the Fourier coefficient of the one-circle Poisson measure fails to be `r^|k|`;
4. Kakutani's criterion applied to `r_p=p^(-sigma)` gives a threshold different from convergence of `sum_p p^(-2 sigma)`;
5. a finite vertical-flow Gram matrix is not diagonally unitarily conjugate to its `t=0` version;
6. the incidence/Möbius determinant calculation produces a zero or sign change for some `sigma>0`;
7. a proposed operator uses completed/global data outside the radial GCD kernel, in which case it lies outside this obstruction rather than contradicting it.

Items 1–6 are exact elementary/classical checks. Item 7 is the intended escape boundary.

## Consequence for the research line

After `PL-016` and `PL-029`, it was still natural to ask whether explicitly weighting the full exponent lattice by its exact log-prime metric might produce a distinguished positive kernel whose boundary spectrum reveals `Re(s)=1/2`.

The answer is now sharply split:

```text
YES:
weighted exponent distance
  -> normalized GCD kernel
  -> infinite prime-torus Poisson spectral measure
  -> exact measure-class transition at sigma=1/2.

NO:
that transition
  -> zero localization / zero ordinates.
```

The `1/2` boundary here is real mathematics, not numerology. But it is governed by the square-summability threshold

```text
sum_p p^(-2 sigma),
```

and the finite spectral data are invariant under the actual vertical flow. A viable RH mechanism therefore needs an additional structure that couples this critical prime geometry to **completed analytic information**. The promising boundary is no longer “find a natural critical kernel”; the canonical one already exists. It is “explain how a global completion turns a zero-blind `1/2` measure-class transition into Weil positivity, a resonance condition, or another invariant that can actually constrain the zero divisor.”
