# PF-020 — short-orbit accumulation destroys the standard Selberg/wave trace geometry

**Status:** `NEGATIVE/OBSTRUCTION`, conditional only on the primitive/simple short-geodesic conclusion from PF-005/PF-007.

## Claim

The canonical cuff lengths themselves satisfy `ell_n -> infinity`; they are not the source of a short-length divergence. The obstruction comes from **nonlocal separating geodesics** produced by multi-gap prime configurations.

PF-004 gives the exact four-endpoint identity

```text
sinh(L/4)^2 = chi
```

for the separating curve around a block of cusps, and PF-005/PF-007 import prime-gap results that force infinitely many distinct simple primitive such curves with

```text
L_j -> 0.
```

Consequently the primitive length spectrum is not locally finite at zero. In fact, for every `epsilon > 0`,

```text
#{primitive gamma : ell(gamma) < epsilon} = infinity.
```

This already prevents the hyperbolic side of a standard Selberg trace formula from defining the usual locally finite orbital distribution near length zero.

## Direct trace-formula obstruction

For a finite-area hyperbolic surface, the hyperbolic contribution to Selberg's trace formula contains, for every primitive closed geodesic `gamma` of length `L` and every iterate `k >= 1`, a term of the form

```text
L / (2 sinh(k L / 2)) * g(k L),
```

where `g` is an even compactly supported test function (up to standard convention-dependent normalizing factors that do not affect the argument).

Take a nonnegative even `g in C_c^infty(R)` with

```text
g(t) = 1
```

on a neighborhood of `0`.

For the `k=1` contribution of the primitive prime-flute geodesics `gamma_j`,

```text
L_j / (2 sinh(L_j/2)) * g(L_j) -> 1.
```

Hence

```text
sum_j L_j / (2 sinh(L_j/2)) * g(L_j) = +infinity.
```

The obstruction is positive: there is no cancellation to exploit.

Equivalently, the formal hyperbolic orbital measure

```text
mu_hyp
  = sum_{gamma primitive} sum_{k>=1}
      [ell(gamma)/(2 sinh(k ell(gamma)/2))]
      delta_{k ell(gamma)}
```

has infinite mass in every neighborhood of `0`. It is therefore not a Radon measure, and its pairing with a positive test function supported near zero is not finite.

## Consequence for wave trace

In the usual compact/finite-geometry setting, the wave trace has its universal local singularity at `t=0`, while nontrivial closed geodesics contribute singularities at positive lengths. The classical Duistermaat--Guillemin/Chazarain picture relies on the positive-length periodic-orbit set being locally discrete in the regime where individual orbit singularities are analyzed.

For the prime-flute,

```text
L_j -> 0
```

with Selberg hyperbolic amplitudes tending to a nonzero constant. Thus nontrivial periodic-orbit singularities accumulate directly into `t=0`.

So a standard decomposition of the form

```text
local/Weyl singularity at t=0
+ locally finite sum of positive-length orbit singularities
```

cannot survive unchanged.

This is stronger than merely saying that existing finite-type trace-formula theorems do not apply: the usual geometric side already diverges on an explicit nonnegative test function.

## Consequence for prime-geodesic counting

The ordinary primitive-geodesic counting function

```text
Pi_X(L) = #{primitive gamma : ell(gamma) <= L}
```

is infinite for every `L>0`.

Therefore there is no standard prime geodesic theorem for the full prime-flute with a finite counting function on compact length intervals.

A regularization by **length cutoff alone** cannot solve the problem, because there is no first positive scale below which only finitely many primitive orbits occur. Any viable regularization would have to use additional structure, for example a spatial exhaustion/marking or an explicit subtraction of the arithmetically generated short-orbit background.

Such a regularization would no longer be the ordinary unmarked length-spectrum trace formula.

## Relation to the distinguished cuffs

This sharpens the earlier cuff results.

The distinguished cuff lengths obey

```text
ell_n ~ 2 log(4 p_n/g_n)
```

and, using the known prime-gap upper bounds,

```text
ell_n -> infinity.
```

So the canonical cuffs are individually harmless at the small-length end. Scalar observables of those cuffs tend to telescope or reduce to known prime Dirichlet data (PF-001, PF-002, PF-011).

The trace obstruction appears only after retaining **relations among several gaps**:

```text
prime-gap configuration
    -> cross-ratio chi
    -> nonlocal separating geodesic L
    -> L -> 0
    -> failure of local finiteness of the hyperbolic trace measure.
```

This reinforces the recurring conclusion that any prime-specific geometry lives in multi-gap/cross-ratio data, not in independent cuff factors.

## What this rules out

This rules out, in their standard forms,

```text
ordinary Selberg geometric trace sum
ordinary wave-trace orbit expansion near t=0
ordinary prime-geodesic counting theorem
any determinant obtained by integrating such an unrenormalized trace
```

for the full fixed prime-flute.

It does **not** prove that no renormalized trace or determinant can exist. It says that a successful construction must explicitly absorb an infinite, prime-dependent family of short primitive orbits; subtracting only universal area/cusp terms is insufficient.

## Novelty / literature audit

The general principles are classical:

- Selberg's hyperbolic trace term is weighted by `L/(2 sinh(kL/2))`;
- wave-trace singularities are tied to closed geodesic lengths in the finite-geometry setting;
- infinite-type hyperbolic surfaces may have non-discrete length spectra.

Recent work of Fanoni--Fisac (arXiv:2602.19670) explicitly isolates **infinite-type surfaces with discrete length spectrum** as the tractable regime for their isospectrality questions. The prime-flute lies on the opposite side: its primitive length spectrum accumulates at zero.

A targeted search did not locate a published Selberg/wave-trace construction for an infinite-type hyperbolic surface with an arithmetically forced infinite family of primitive geodesics accumulating at zero. The general obstruction is elementary once such a family exists; the potentially new content is the prime-gap specialization supplied by PF-004/PF-005/PF-007.

Useful literature anchors:

- the finite-area Selberg trace formula, especially the positive hyperbolic term;
- Chazarain and Duistermaat--Guillemin on wave-trace singularities and closed geodesics;
- Fanoni--Fisac, *Isospectrality for infinite-type hyperbolic surfaces with discrete length spectrum*, arXiv:2602.19670;
- Borthwick's spectral theory of finite-geometry hyperbolic surfaces for the standard trace/scattering framework.

## Lean / formalization boundary

The analytic trace formula itself is not an early Lean target. The finite core can be separated cleanly:

1. formalize PF-004;
2. formalize the elementary limit

```text
L / (2 sinh(L/2)) -> 1 as L -> 0+;
```

3. encode an abstract lemma: if a sequence of distinct primitive lengths tends to zero, then the positive `k=1` Selberg-weight sum against any test function equal to `1` near zero diverges.

The prime-gap theorem and the topological identification of the block curve remain external theorem interfaces.