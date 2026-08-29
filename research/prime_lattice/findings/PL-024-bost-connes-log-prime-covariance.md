# PL-024 — Bost–Connes already realizes the log-prime covariant completion, but its thermodynamic boundary is `beta=1`

## Claim

The structured escape left open by `PL-023`,

```text
prime-coordinate shift S_p
    + logarithmic generator H
    + [H,S_p] = (log p) S_p,
```

is already realized in the classical Bost–Connes quantum statistical mechanical system.

In its standard positive-energy representation on `ell^2(N)`, the multiplicative isometries satisfy

```text
mu_n epsilon_m = epsilon_(nm),
H epsilon_m = (log m) epsilon_m,
```

so, exactly,

```text
[H,mu_n] = (log n) mu_n,
sigma_t(mu_n) = n^(i t) mu_n.
```

Because `mu_n=product_p mu_p^(v_p(n))`, the Bost–Connes semigroup is the positive prime-exponent lattice acting by coordinate translations, and the Hamiltonian is the same energy functional

```text
log n = sum_p v_p(n) log p
```

that appears in `PL-007` and `PL-023`.

However, this canonical covariant completion does **not** move the intrinsic thermodynamic boundary from the zeta pole to the Riemann critical line. Its ordinary Gibbs partition trace is

```text
Tr(exp(-beta H)) = sum_n n^(-beta) = zeta(beta)
```

only for `Re(beta)>1`, and the Bost–Connes phase transition occurs at `beta=1`. KMS states continue to exist for `0<beta<=1` even though `exp(-beta H)` is not trace class; that KMS extension is a `C*`-dynamical equilibrium construction, not analytic continuation of the scalar partition trace into the critical strip. In particular, the interval `0<beta<=1` is a single high-temperature KMS regime in the classical phase classification and contains no corresponding special transition at `beta=1/2`.

Thus the route

```text
log-prime covariance
    -> canonical arithmetic crossed product / KMS completion
    -> critical-line selector
```

is **not** a missing mechanism: its canonical realization is classical, and its intrinsic singular temperature is `1`, not `1/2`.

To make this noncommutative arithmetic dynamics genuinely zero-sensitive, the established Connes program adds substantially more structure — adele classes, scaling/trace formulas, Fourier duality, semilocal compression, Weil positivity, and spectral triples. That returns the problem to the completed adelic/Weil routes already isolated in `PL-013` and `PL-014`, rather than deriving the Riemann zero divisor from log-prime covariance alone.

**Evidence/status:** `LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION`.

The Bost–Connes system and its phase transition are classical literature. The identification of its multiplicative isometries with prime-exponent coordinate shifts and the exact commutator calculation are elementary specializations to this research line. No novelty is claimed for the operator relation itself.

## Exact lattice covariance

Write the standard basis of `ell^2(N)` as `{epsilon_m}` and define

```text
mu_n epsilon_m = epsilon_(nm).
```

Unique factorization gives

```text
mu_n = product_p mu_p^(v_p(n)).
```

Hence `mu_p` acts on exponent vectors exactly as

```text
v(m) -> v(m)+e_p.
```

Let the logarithmic Hamiltonian be

```text
H epsilon_m = (log m) epsilon_m.
```

Then on every basis vector,

```text
(H mu_n - mu_n H) epsilon_m
  = (log(nm)-log m) epsilon_(nm)
  = (log n) epsilon_(nm),
```

so

```text
boxed: [H,mu_n] = (log n) mu_n.
```

For a prime `p`, this is exactly the relation proposed as the canonical non-invariant alternative in `PL-023`:

```text
[H,mu_p] = (log p) mu_p.
```

Exponentiating the commutator gives the Bost–Connes time evolution

```text
sigma_t(mu_n)
  = exp(i t H) mu_n exp(-i t H)
  = n^(i t) mu_n.
```

Thus the frequencies `log p` are not merely analogous to Bost–Connes energies. They are the exact infinitesimal weights of the semigroup covariance.

## The crossed product adds arithmetic structure, but the thermal singularity stays at `1`

The free Hamiltonian already appeared in Julia's primon gas and in `PL-007`. Bost–Connes adds a genuine arithmetic observable algebra: the multiplicative semigroup acts on the phase algebra associated to `Q/Z`, producing a noncommutative crossed-product system with cyclotomic/Galois symmetry and spontaneous symmetry breaking.

That enrichment is mathematically substantial, so this finding is **not** saying that the Bost–Connes system is just the bare exponent lattice. It says something narrower: the most canonical way to enrich the lattice while retaining the exact covariance suggested by `PL-023` is already known, and its equilibrium threshold does not select the Riemann critical line.

Indeed,

```text
exp(-beta H) epsilon_n = n^(-beta) epsilon_n,
```

hence

```text
Tr(exp(-beta H)) = zeta(beta)
```

precisely in the trace-class region `Re(beta)>1`. The divergence at `beta=1` is the same trace/pole boundary already identified for the diagonal semigroup in `PL-007`.

The Bost–Connes equilibrium-state theorem is richer than the Gibbs trace: there is a unique `KMS_beta` state for `0<beta<=1`, whereas for `beta>1` the low-temperature extremal KMS states exhibit symmetry breaking. Therefore the KMS formalism genuinely survives below the trace-class boundary, but it does so by the operator-algebraic KMS condition, not by declaring

```text
Tr(exp(-beta H)) = analytically continued zeta(beta).
```

Those are different mathematical statements. In particular, KMS existence for `beta=1/2` does not make `zeta(1/2)` a partition trace and does not supply the functional-equation symmetry `s <-> 1-s`.

## Why this sharpens PL-023 rather than duplicating PL-004 or PL-007

`PL-004` already recorded Bost–Connes as richer prior art beyond the free prime gas. `PL-007` identified the diagonal Hamiltonian `H=log N` and the trace/Schatten thresholds. Neither finding answered the specific design question produced later by `PL-023`: whether abandoning exact prime-shift invariance in favor of the structured covariance

```text
[H,S_p]=(log p)S_p
```

opens a new spectral class.

The present calculation answers that novelty question directly:

```text
PL-023 covariance candidate
       ||
       \/
Bost–Connes multiplicative isometries + log Hamiltonian
```

up to the extra classical arithmetic phase algebra of the Bost–Connes construction.

So `log p` as a commutator weight is useful structural language, but it is not by itself a new route to RH.

## The RH-sensitive noncommutative completion is already a different, completed route

Connes' later adele-class trace formula gives a spectral interpretation of critical zeros as an absorption spectrum and hypothetical noncritical zeros as resonances. Connes–Consani and subsequent work relate scaling actions, semilocal trace formulas, Fourier transform, quantized calculus, Sonin/prolate spaces, Weil positivity, and spectral triples to the zeta zero problem.

That progression matters for the prime-lattice line because it identifies what the elementary covariance is missing. The step from

```text
[H,mu_p]=(log p)mu_p
```

to an RH-level positivity or zero-localization statement does not come from the crossed-product time evolution alone. It requires completed global harmonic data of the same kind already encountered independently in:

```text
PL-014: adelic Fourier/Mellin duality and the self-dual axis Re(s)=1/2,
PL-013: completed Weil form, prime-power axis data, positivity, spectral triples.
```

This also preserves the analytic-continuation boundary correctly. The Bost–Connes heat trace reaches only `Re(beta)>1`; the completed trace-formula/Weil machinery is a different object with additional archimedean and Fourier structure. One must not identify the latter with an analytic continuation of the former operator trace.

## Prior art and novelty audit

The direct prior-art anchors already recorded in `research/prime_lattice/SOURCES.md` are:

- Jean-Benoît Bost and Alain Connes, *Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*, Selecta Mathematica 1 (1995), 411–457. This is the primary source for the arithmetic `C*`-dynamical system, zeta partition function, KMS phase transition, and symmetry breaking.
- Alain Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Selecta Mathematica 5 (1999), 29–106. This is the established move from quantum-statistical zeta structure to the adele-class trace-formula/zero-spectrum program.
- The Weil/spectral-triple literature already catalogued for `PL-013` supplies the later self-adjoint/positivity route, while Tate's thesis and its modern treatments in `PL-014` supply the additive-Fourier mechanism behind genuine continuation and the `1/2` self-dual axis.

A separate novelty search also finds later papers explicitly formulating RH-equivalent inequalities using Bost–Connes KMS observables. Those results confirm that the BC observable algebra can *host* arithmetic reformulations of RH; they do not make the bare covariance or the `beta=1` phase transition a derivation of critical-line zero localization. The negative claim here is therefore intentionally restricted to the canonical covariance/KMS mechanism itself.

No novelty is claimed for Bost–Connes, the log Hamiltonian, or the covariance relation. The durable research value is the identification that the precise escape proposed by `PL-023` is classical and that its canonical thermodynamic completion returns a `beta=1` boundary rather than a `1/2` zero mechanism.

## Boundary conditions and counterarguments

### This does not say Bost–Connes is irrelevant to RH

The Bost–Connes algebra contains far richer arithmetic information than the exponent lattice, including cyclotomic/Galois structure. Later noncommutative-geometric work uses related adele-class/scaling constructions in serious RH programs. The obstruction is only against treating the elementary log-prime covariance plus its standard KMS phase diagram as the missing critical-line mechanism.

### `beta=1/2` is not forbidden; it is simply not a distinguished BC phase boundary

A `KMS_(1/2)` state exists in the high-temperature regime. The point is that the classical KMS classification does not undergo a transition there, and the Gibbs operator is already non-trace-class. Any new significance assigned specifically to `1/2` therefore needs additional structure.

### KMS extension is not scalar analytic continuation

The existence of KMS states for `beta<=1` must not be used to write a regularized equality `Tr(exp(-beta H))=zeta(beta)` there. The left side is not an ordinary trace. A proposal that obtains the critical strip from KMS data must identify a new observable or theorem, not silently reuse the analytically continued scalar zeta function.

### The completed Connes/Weil route is outside the negative

Adele-class trace formulas, Fourier transform, semilocal compression, scattering/resonance constructions, or Weil positivity add exactly the sort of structure excluded from the elementary negative. They remain live RH-level mechanisms, but they are established prior art and are already tracked in `PL-013` and `PL-014`.

## Audit / falsification tests

The finding can be falsified or materially narrowed by any of the following:

1. the standard Bost–Connes representation does not contain multiplicative isometries acting as `epsilon_m -> epsilon_(nm)` with logarithmic Hamiltonian `H epsilon_m=(log m)epsilon_m`;
2. the resulting commutator fails to be `[H,mu_n]=(log n)mu_n`;
3. the ordinary Gibbs operator `exp(-beta H)` is trace class somewhere with `Re(beta)<=1`;
4. the original Bost–Connes KMS phase diagram has an intrinsic phase transition or symmetry change at `beta=1/2` comparable to its transition at `beta=1`;
5. a literature theorem derives localization of the Riemann zero divisor on `Re(s)=1/2` from the Bost–Connes covariance/KMS mechanism alone, without importing an RH-equivalent arithmetic criterion or additional completed trace-formula/Fourier structure.

The first four checks are classical and unconditional. The fifth is the novelty boundary for any future proposal along this route.

## Consequence for the research line

After `PL-023`, it is no longer enough to say that a useful operator should replace prime-shift invariance by controlled noncommutativity. The canonical relation

```text
[H,S_p]=(log p)S_p
```

has already been integrated into a deep arithmetic quantum statistical system.

The design space is therefore narrower:

```text
bare prime-shift invariance
    -> normal/self-adjoint triviality                  [PL-023]

canonical log-prime covariance
    -> Bost–Connes / zeta thermodynamics
    -> intrinsic phase boundary beta=1                [PL-024]

RH-sensitive completion
    -> additional adelic/Fourier/Weil structure
    -> established trace-formula/spectral programs    [PL-013, PL-014]
```

A genuinely new prime-lattice mechanism must add something that is neither merely the classical Bost–Connes covariance nor merely a repackaging of the known adelic/Weil completion. In particular, it must explain how the exact infinite rational-prime lattice couples to a completed global structure in a way that produces a falsifiable constraint on the zero divisor at `Re(s)=1/2`.