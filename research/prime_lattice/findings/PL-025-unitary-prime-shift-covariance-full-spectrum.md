# PL-025 — Exact unitary prime-shift covariance forces full real spectrum

## Claim

The most direct reversible completion of the positive prime-exponent shifts is incompatible with a discrete Hilbert–Pólya spectrum.

Let `H` be self-adjoint on a nonzero Hilbert space and suppose that, for two multiplicatively independent primes (already `2` and `3` suffice), there are unitary operators `U_p` such that the self-adjoint covariance relation

```text
U_p^* H U_p = H + (log p) I
```

holds, equivalently on an invariant operator core,

```text
[H,U_p] = (log p) U_p.
```

Then

```text
sigma(H) = R.
```

Consequently `H` is neither semibounded nor compact-resolvent. In particular, no exact **unitary** realization of all prime-coordinate translations with their natural `log p` energy increments can have the Riemann-zero ordinates as its full discrete spectrum.

This is the reversible counterpart of the unilateral covariance in `PL-024`: the positive semigroup can retain the discrete positive spectrum `{log n}` precisely because its prime shifts are proper isometries rather than unitaries. Once the shifts are made reversible, their inverses generate the signed exponent lattice and the incommensurate prime energies force spectral translation invariance by a dense subgroup of `R`.

**Evidence/status:** `LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the route

```text
exact reversible prime-lattice shifts
    + exact log-prime covariance
    + self-adjoint compact-resolvent generator
    -> Hilbert–Pólya spectrum.
```

The semigroup-to-group dilation is classical operator-algebra prior art; the spectral no-go below is an elementary consequence of unitary equivalence, unique factorization, and the spectral theorem. No novelty is claimed for the general Weyl-covariance principle.

## Exact spectral obstruction

Assume

```text
U_p^* H U_p = H + a_p I,
a_p = log p.
```

Unitary conjugation preserves spectrum, while scalar translation shifts it. Therefore

```text
sigma(H)
  = sigma(U_p^* H U_p)
  = sigma(H + a_p I)
  = sigma(H) + a_p.
```

Hence `sigma(H)` is invariant under translation by every integer multiple of `log p`.

Using only `p=2` and `p=3`, it is invariant under

```text
G = {m log 2 + n log 3 : m,n in Z}.
```

The ratio `log 2 / log 3` is irrational: otherwise `log 2 / log 3 = a/b` with nonzero integers `a,b` would imply

```text
2^b = 3^a,
```

contradicting unique factorization. Therefore the additive subgroup `G` is dense in `R`.

Now choose any `lambda in sigma(H)`, which exists because `H` is self-adjoint on a nonzero space. For arbitrary `x in R`, choose `g_k in G` with

```text
g_k -> x-lambda.
```

Translation invariance gives `lambda+g_k in sigma(H)` for every `k`. Since the spectrum of a closed operator is closed,

```text
x = lim_k (lambda+g_k) in sigma(H).
```

Thus

```text
boxed: sigma(H)=R.
```

No commutation relation between `U_2` and `U_3` is needed for this spectral-set argument. If they really represent the signed prime-exponent lattice, they commute as well, but the obstruction is already stronger than that structure requires.

## The canonical signed-lattice model makes the failure explicit

The group completion of the positive exponent cone is

```text
direct_sum_p Z  ~=  Q_{>0}^x,
```

where a signed finite-support vector `alpha=(alpha_p)` corresponds to

```text
q(alpha)=product_p p^(alpha_p).
```

On `ell^2(Q_{>0})`, define

```text
U_r e_q = e_(rq),
H e_q   = (log q) e_q.
```

Then each `U_r` is unitary and

```text
U_r^* H U_r = H + (log r) I.
```

The point eigenvalues are

```text
{log q : q in Q_{>0}},
```

which are already dense in `R`; their closure is the full spectrum `R`.

The resolvent is visibly noncompact. For example, the distinct rationals

```text
q_n=(n+1)/n -> 1
```

give eigenvalues `log q_n -> 0`, so the resolvent eigenvalues

```text
1/(log q_n - i)
```

do not tend to zero. Equivalently, every bounded energy interval contains infinitely many signed-lattice states.

This is not a defect of the particular regular representation: the previous spectral-translation argument shows that **any** self-adjoint realization with exact unitary covariance for `2` and `3` already has `sigma(H)=R`.

## Why this matters after PL-023 and PL-024

`PL-023` showed that demanding exact **invariance** under every positive prime shift is too rigid: a bounded normal operator in that commutant collapses to a scalar, and an invariant self-adjoint resolvent collapses with it.

`PL-024` then checked the natural escape

```text
[H,S_p]=(log p)S_p
```

and found it already integrated in the Bost–Connes system. There the `S_p` are proper isometries on the positive lattice, and

```text
H e_n=(log n)e_n
```

has a discrete positive spectrum. The thermodynamic singularity is at `beta=1`, not at the Riemann critical line.

A tempting next modification is to restore reversibility by replacing the isometries by unitary prime translations. The present finding shows why that cannot produce a discrete zeta-zero Hamiltonian while retaining the exact same covariance:

```text
positive cone N_0^(P)
    + isometric prime shifts
    -> one-sided energies log n
    -> discrete positive spectrum

signed lattice Z^(P)
    + unitary prime shifts
    -> energies log q, q in Q_{>0}
    -> dense translation subgroup
    -> full spectrum R.
```

So the one-sidedness is not an incidental implementation detail. It is exactly what prevents the `log p` covariance from forcing a continuous/dense spectral support.

## Prior art and novelty audit

The relevant operator-algebraic completion is classical. Marcelo Laca proved that isometric representations/actions of suitable semigroups admit minimal unitary/automorphic dilations to the containing group, and treated the Bost–Connes system explicitly: the positive multiplicative semigroup is dilated to an action of `Q_{>0}^x` on the finite adeles, yielding the crossed product `C_0(A_f) ⋊ Q_{>0}^x`.

Primary source:

- Marcelo Laca, “From Endomorphisms to Automorphisms and Back: Dilations and Full Corners,” *Journal of the London Mathematical Society* **61** (2000), 893–904. DOI: https://doi.org/10.1112/S0024610799008492.

The general phenomenon that exact unitary translation covariance strongly constrains a self-adjoint spectrum is also classical Weyl-relation territory. Continuous weak Weyl relations impose still stronger spectral conclusions; for context see:

- Asao Arai, “Generalized Weak Weyl Relation and Decay of Quantum Dynamics,” *Reviews in Mathematical Physics* **17** (2005), 1071–1109. DOI: https://doi.org/10.1142/S0129055X05002479.

The arithmetic statement here uses less machinery. It needs only two discrete shifts, because `log 2` and `log 3` generate a dense additive subgroup. The durable value is therefore not a novelty claim but a prime-lattice-specific obstruction: **unitarizing the exact log-prime covariance destroys the discrete spectral geometry that a Hilbert–Pólya operator would need.**

## Boundary conditions and escape routes

### The negative is about exact unitary covariance

It does not rule out proper isometries, partial isometries, Toeplitz/compressed representations, scattering systems, or nonunitary transfer operators. Those can keep a one-sided energy geometry, as Bost–Connes itself does.

### Approximate or cocycle-corrected covariance is not covered

Relations such as

```text
U_p^* H U_p = H + (log p)I + K_p
```

with compact, trace-class, boundary, or genuinely arithmetic correction terms are outside the proof. Such corrections would have to carry the zero-sensitive information rather than being discarded as negligible.

### A full real spectrum does not forbid extra embedded structure

The result rules out identifying the **full operator spectrum** with the discrete Riemann zero ordinates and rules out compact resolvent. It does not prove that a system with continuous spectrum cannot encode zeta zeros as resonances, scattering poles, absorption lines, or distinguished embedded states. Connes' adelic trace-formula program is of that different type.

### One prime is not enough

With only one unitary covariance step `a=log p`, a closed spectrum may be invariant under `a Z` without filling `R`. The obstruction becomes decisive as soon as two multiplicatively independent directions are represented exactly; the ordinary prime lattice contains infinitely many such directions.

## Audit / falsification tests

This finding would be falsified or materially narrowed by any of the following:

1. a self-adjoint `H` and unitaries `U_2,U_3` satisfying the stated exact covariance while `sigma(H)` is not invariant under translation by `log 2` and `log 3`;
2. a rational relation between `log 2` and `log 3`;
3. a nonempty closed proper subset of `R` invariant under the dense group `Z log 2 + Z log 3`;
4. a compact-resolvent self-adjoint operator whose spectrum is all of `R`;
5. a proposed Hilbert–Pólya construction that genuinely uses unitary prime translations but avoids the hypothesis because the prime action is only compressed, projective with non-scalar cocycle, approximate, or acts on a different operator than the zero Hamiltonian.

The first four are ruled out by standard exact arguments. The fifth marks the actual design boundary for future work.

## Consequence for the research line

Together `PL-023`–`PL-025` produce a useful three-way constraint on operator designs based directly on exponent-lattice translations:

```text
exact prime-shift invariance + normality
    -> scalar/trivial                              [PL-023]

one-sided isometric shifts + exact log covariance
    -> Bost–Connes / discrete log n energies
    -> thermodynamic boundary beta=1             [PL-024]

reversible unitary shifts + exact log covariance
    -> spectrum invariant under Z log 2 + Z log 3
    -> sigma(H)=R, no compact resolvent           [PL-025]
```

A viable new spectral mechanism therefore cannot obtain the Riemann zeros merely by choosing a more symmetric representation of the same prime translations. It must either keep an essentially one-sided/compressed geometry and add a zero-sensitive global structure, or let the prime directions enter through a trace/scattering/adelic mechanism rather than as exact reversible spectral translations of the Hilbert–Pólya operator itself.
