# PL-074 — Critical pointed Möbius Gram splits into Mirsky support and Chowla orientation

## Claim

The simplest pointed escape left open by `PL-073` can be classified at the first nontrivial finite-horizon scale. Pointing the positive-cone Gram matrix at the fixed all-ones vector does break the Möbius torus gauge, but at the critical `N ~ T` resolution its first fixed-lag arithmetic terms are not a new multiplicative spectral invariant. They split into two classical additive-correlation problems:

```text
square-free support mu(n)^2
    -> Mirsky square-free-pair singular series (unconditional);

Möbius orientation mu(n)
    -> two-point shifted Möbius / Chowla correlation (open at fixed Cesàro shift).
```

More precisely, for a coefficient sequence `a(n)` and a fixed macroscopic band `0<a<b<infinity`, put

```text
I_T={n in N : a T < n <= b T},

D_(a,T)(t)=sum_(n in I_T) a(n) n^(-it),

Q_a(T)=(1/T) integral_0^T |D_(a,T)(t)|^2 dt.
```

With

```text
K_T(u)=(1/T) integral_0^T exp(+i t u) dt
      =exp(+i T u/2) sinc(T u/2),
```

one has the exact lag decomposition

```text
Q_a(T)
 = sum_(n in I_T) |a(n)|^2
   +2 T Re sum_(h>=1) C_(a,h)(T),

C_(a,h)(T)
 =(1/T) sum_(n,n+h in I_T)
   a(n) conjugate(a(n+h))
   K_T(log((n+h)/n)).
```

For every fixed `h>=1`, uniformly when `n/T` remains in `[a,b]`,

```text
T log((n+h)/n)=h/(n/T)+O_h(1/T),
```

so the critical kernel has the nonzero limit

```text
K_T(log((n+h)/n))
 -> kappa_h(n/T),

kappa_h(x)=exp(+i h/(2x)) sinc(h/(2x)).
```

Thus fixed additive shifts survive exactly at the same `N~T` scale at which `PL-072` found the universal sinc Gram transition.

For `a(n)=mu(n)^2`, Mirsky's square-free tuple theorem gives, for each fixed `h>=1`,

```text
(1/X) sum_(n<=X) mu(n)^2 mu(n+h)^2
 -> S_sf(h),

S_sf(h)=product_p (1-nu_p(h)/p^2),

nu_p(h)=1 if p^2 divides h,
          2 otherwise.
```

Partial summation therefore gives the weighted critical-band limit

```text
C_(mu^2,h)(T)
 -> S_sf(h) integral_a^b kappa_h(x) dx.
```

The square-free-support signal that survives the `PL-073` gauge obstruction is therefore already classical local sieve-density data at each fixed lag; no zeta zero, analytic continuation, or critical-line input enters this limit.

For `a(n)=mu(n)`, the corresponding term is

```text
C_(mu,h)(T)
 =(1/T) sum_(n,n+h in I_T)
   mu(n) mu(n+h)
   K_T(log((n+h)/n)).
```

A fixed-shift Chowla estimate

```text
sum_(n<=X) mu(n) mu(n+h)=o(X)
```

would force `C_(mu,h)(T)->0` by the same partial-summation argument. Conversely, evaluating these pointed critical-lag terms requires information about shifted Möbius correlations rather than only the multiplicative exponent geometry. The ordinary fixed-shift two-point Möbius Chowla problem remains open; known results instead include averaging over shifts and logarithmically averaged analogues.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART/REDIRECT` for the route

```text
PL-073 pointed all-ones Gram observable
+ critical positive-cone horizon N~T
+ square-free/Möbius coefficients
    -> new prime-lattice spectral RH mechanism.
```

The result does **not** prove that the full pointed quadratic form is equivalent to Chowla, nor that RH cannot imply estimates for it. It identifies the exact arithmetic content of every fixed-lag component at the first nontrivial resolution scale and shows that the two canonical pieces left by `PL-073` land in established square-free-pair and multiplicative-correlation theory.

## Exact pointed Gram identity

Let

```text
f_n(t)=T^(-1/2) n^(-it),
```

and let `G_(T,I)` be their Gram matrix over `n in I_T`. For a coefficient vector `a`,

```text
Q_a(T)=<a,G_(T,I)a>.
```

This is exactly the type of fixed-target statistic that escapes the diagonal-gauge invariance in `PL-073`: replacing `a` by `mu a` changes the pointed quadratic form even though the associated Gram matrices are unitarily conjugate.

Expanding the square gives

```text
Q_a(T)
 =(1/T) integral_0^T
   sum_(m,n in I_T)
     a(m) conjugate(a(n)) exp(-it log(m/n)) dt.
```

The diagonal `m=n` gives `sum |a(n)|^2`. Writing `n=m+h` in the off-diagonal part and pairing conjugate terms yields the displayed fixed-lag decomposition. No limiting argument, Euler product, or analytic continuation is used.

For `a=mu` and `a=mu^2`, the diagonal is the same:

```text
sum_(n in I_T) mu(n)^2.
```

Thus all orientation sensitivity lies in the off-diagonal shifted products.

## Why `N=o(T)` remains sign-blind

`PL-072` already records the Montgomery--Vaughan mean-value estimate

```text
| integral_0^T |sum_(n<=N) a_n n^(-it)|^2 dt
  -T sum_(n<=N)|a_n|^2 |
 <= C sum_(n<=N) n |a_n|^2.
```

For coefficients supported in `n<=N` this implies

```text
Q_a(T)=sum |a_n|^2 + O((N/T) sum |a_n|^2).
```

Hence if `N=o(T)`, both the square-free support vector `mu^2` and the oriented vector `mu` have the same leading quadratic statistic:

```text
Q_mu(T)=Q_(mu^2)(T)
        =sum_(n<=N) mu(n)^2 (1+o(1)).
```

The all-ones target breaks the exact gauge symmetry algebraically, but below the Fourier-resolution threshold the Gram operator is already too close to the identity for that breaking to survive at leading order.

Therefore the first natural place to inspect the pointed orientation is precisely `N~T`, not a longer observation regime.

## The critical kernel converts multiplicative characters into additive lags

Take a fixed lag `h` and `n/T=x` in a compact subset of `(0,infinity)`. Then

```text
log(1+h/n)=h/n+O_h(1/n^2),
```

and therefore

```text
T log(1+h/n)=h/x+O_h(1/T).
```

The finite-time character kernel consequently converges to

```text
kappa_h(x)=exp(+i h/(2x)) sinc(h/(2x)).
```

This is the same local sinc geometry as `PL-072`, now tested against arithmetic coefficients. The important change is informational: the kernel no longer asks about the prime-factor relation between two nearby exponent vectors. It weights the ordinary **additive shift pair**

```text
(a(n),a(n+h)).
```

For a fixed finite block around `n_T/T->x`, the limiting pointed quadratic form is therefore simply

```text
sum_(j,k) a(n_T+j) conjugate(a(n_T+k))
          kappa_(k-j)(x),
```

with the obvious convention `kappa_0=1`. The critical Gram geometry supplies the universal kernel; all nonuniversal information is the additive coefficient pattern placed into that kernel.

## Square-free support is Mirsky data at fixed lag

For square-free support, `a(n)=mu(n)^2`. The two-point density can be read directly prime by prime.

For a fixed prime `p`, requiring both `n` and `n+h` to be square-free forbids residue classes modulo `p^2`. If `p^2` does not divide `h`, the two forbidden residues

```text
n=0 mod p^2,

n=-h mod p^2
```

are distinct, giving local density `1-2/p^2`. If `p^2|h`, they coincide, giving local density `1-1/p^2`. Hence the natural singular series is

```text
S_sf(h)=product_p (1-nu_p(h)/p^2).
```

Mirsky's theorem supplies the asymptotic density. Since `kappa_h(n/T)` is a fixed smooth bounded weight on `[a,b]`, Abel/partial summation upgrades it to

```text
(1/T) sum_(aT<n<=bT)
  mu(n)^2 mu(n+h)^2 kappa_h(n/T)

 -> S_sf(h) integral_a^b kappa_h(x) dx.
```

The `O(1)` endpoint discrepancy from also requiring `n+h in I_T` is negligible after division by `T`.

This is a genuine arithmetic correction to the universal sinc kernel: it knows whether each `p^2` divides `h`. But it is **classical square-free tuple geometry**, not zero-sensitive information. In exponent language it comes only from the exclusion of coordinates `v_p>=2` and the Chinese-remainder interaction of that support condition under ordinary additive shifts.

## Möbius orientation becomes a Chowla/Elliott correlation

For the oriented coefficient vector, the same kernel is multiplied by

```text
mu(n) mu(n+h).
```

If the fixed-shift partial sum

```text
A_h(X)=sum_(n<=X) mu(n)mu(n+h)
```

satisfies `A_h(X)=o(X)`, then partial summation against the smooth slowly varying kernel gives

```text
C_(mu,h)(T)->0.
```

This is exactly the type of cancellation predicted by the two-point Chowla conjecture for Möbius. The literature audit gives a useful contrast:

- Mirsky's corresponding `mu^2` pair density is classical and explicit;
- Matomäki--Radziwill--Tao prove Chowla after averaging over shifts;
- modern work obtains strong logarithmically averaged two-point results and further quantitative refinements;
- the ordinary fixed-shift Cesàro correlation remains open.

Thus pointing does recover the sign field that `PL-073` gauged away, but the recovered information is not generated by the prime-torus Gram geometry. It is supplied by an additive correlation problem for the chosen multiplicative coefficients.

The same structural statement holds for a general bounded multiplicative coefficient `f`: the fixed-lag critical term contains

```text
f(n) conjugate(f(n+h)),
```

placing the problem in Elliott/Chowla-type multiplicative-correlation theory. This is an important falsification control: breaking torus gauge with a target is not enough by itself to select the Riemann/Möbius point from other multiplicative coefficient systems.

## Relation to Mertens cancellation and RH

At the distinguished time `t=0`, the Möbius Dirichlet polynomial is

```text
D_mu(0)=sum_(n in I_T) mu(n),
```

so a fixed basepoint can indeed retain ordinary Mertens cancellation, whose global power bounds are classically equivalent to RH.

The present calculation explains why the **quadratic vertical average** is a very different pointed observable. Once one averages `|D_mu(t)|^2` over a horizon at the first nontrivial resolution scale, the off-diagonal information is reorganized into additive shifted products `mu(n)mu(n+h)`.

Therefore one must not infer that a target-relative construction is useless merely because this particular pointed Gram statistic classicalizes. Nyman/Bagchi, for example, uses a target together with Mellin/Hardy analytic continuation and is not reduced to this finite Dirichlet-polynomial mean square.

## Prior-art and novelty audit

No novelty is claimed for any general ingredient.

- H. L. Montgomery and R. C. Vaughan, “Hilbert's Inequality,” *Journal of the London Mathematical Society* (2) **8** (1974), 73--82, DOI `10.1112/jlms/s2-8.1.73`, is already `research/prime_lattice/SOURCES.md` source 62 and supplies the subcritical mean-square control used in `PL-072`.
- L. Mirsky, “Note on an asymptotic formula connected with r-free integers,” *Quarterly Journal of Mathematics* **os-18**(1) (1947), 178--182, DOI `10.1093/qmath/os-18.1.178`, is the classical square-free tuple/pair-density anchor.
- K. Matomäki, M. Radziwill, T. Tao, “An averaged form of Chowla's conjecture,” *Algebra & Number Theory* **9**(9) (2015), 2167--2196, DOI `10.2140/ant.2015.9.2167`, proves an averaged-shift form and extends the method to general bounded multiplicative functions.
- Jared Duker Lichtman, “Averages of the Möbius Function on Shifted Primes,” *Quarterly Journal of Mathematics* **73**(2) (2022), 729--757, DOI `10.1093/qmath/haab054`, explicitly records the fixed-tuple Möbius Chowla conjecture and its open status while proving averaged variants.
- Terence Tao, “The logarithmically averaged Chowla and Elliott conjectures for two-point correlations,” *Forum of Mathematics, Pi* **4** (2016), e8, DOI `10.1017/fmp.2016.6`, is the standard logarithmically averaged two-point anchor. Current 2026 quantitative work continues to strengthen logarithmic/growing-shift forms without proving the ordinary fixed-shift Cesàro conjecture.

The lag decomposition and critical kernel are elementary consequences of the exact finite-time Gram formula already used in `PL-072`. The durable line-specific contribution is the **routing result** created by combining them with the `PL-073` information audit: the two most immediate pieces that survived its gauge obstruction separate at critical resolution into an unconditional Mirsky support channel and a Chowla/Elliott orientation channel.

A targeted literature search around Möbius Dirichlet-polynomial mean squares, shifted correlations, square-free tuples, and Chowla recovered these classical theories rather than a known zeta-specific theorem in which this pointed Gram transition forces critical-line localization. No claim of mathematical novelty is made for the underlying correlation theorems.

## Analytic-continuation and adversarial audit

No analytic continuation is used. Every displayed Gram identity is a finite integral of a finite Dirichlet polynomial. Mirsky's support limit is an ordinary density theorem, and the Chowla statement is used only as a named comparison/conditional implication, never as evidence.

The negative scope is deliberately limited.

1. **The full critical quadratic form is not classified.** The exact sum contains lags `h` growing with `T`; fixed-lag limits do not determine all possible collective cancellation among those terms.
2. **No equivalence with Chowla is claimed.** Chowla implies the vanishing of each fixed-lag Möbius contribution, but a particular weighted aggregate may conceivably be controlled by weaker information.
3. **No logical separation from RH is claimed.** The finding does not prove that RH cannot imply some shifted-correlation estimate. It says the critical pointed Gram calculation introduces an additive-correlation problem not supplied by the bare exponent-lattice geometry.
4. **Other targets remain open.** The all-ones coefficient target is the most immediate escape from `PL-073`, not the distinguished Nyman target or every possible target-relative operator.
5. **Higher moments remain open.** Cubic or higher pointed statistics would introduce higher additive coefficient correlations and need a separate audit.
6. **Non-unimodular weights remain open.** Von Mangoldt or completion-sensitive weights can carry information not present in the Möbius sign gauge; their finite-horizon behavior is not classified here.
7. **The Mirsky channel is arithmetic but not RH-sensitive at this level.** Its local factors distinguish square-free support of ordinary integers, yet the theorem uses no zero divisor or critical-line symmetry.
8. **Helson/Beurling controls still apply.** A general multiplicative coefficient produces the same shifted-correlation architecture. Any proposed RH mechanism must identify what extra zeta-specific structure constrains those correlations or couples them to analytic continuation.

## Consequence for the research line

The finite-horizon branch now has a sharper information map:

```text
bare positive characters
    -> universal Dirichlet-polynomial N~T resolution (`PL-072`);

Möbius +/- orientation, unpointed
    -> exact prime-torus/diagonal gauge (`PL-073`);

pointed quadratic statistic, N=o(T)
    -> asymptotically diagonal and sign-blind (`PL-072`);

pointed quadratic statistic, N~T, fixed additive lag
    -> square-free support: Mirsky singular series;
    -> Möbius orientation: Chowla/Elliott correlation.
```

So the phrase “keep a fixed target so the Möbius gauge becomes visible” is still too weak to define a new RH mechanism. At the first natural finite-time transition, the target either exposes classical square-free local-density data or hands the difficulty to classical additive correlations of multiplicative functions.

A genuinely surviving construction must therefore add structure not exhausted by this split: a target forced by analytic continuation (as in the Nyman line of findings), a nonquadratic/global coupling whose invariant is not merely a package of shifted multiplicative correlations, a completion-sensitive prime/zero observable, or another mechanism that passes the Helson/Beurling controls while producing a falsifiable localization or positivity statement.