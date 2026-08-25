# PF-028 — bounded prime islands do not have the fixed finite-surface right limit claimed in PF-025

**Status:** `NEGATIVE/CORRECTION`. This invalidates the specific geometric-convergence step used in PF-025. It does not rule out every possible pointed/re-marked limit of isolated prime islands, but the claimed fixed finite-area surface `S_H` determined only by the translated offsets is not obtained by the stated normalization.

## Claim

PF-025 used the upper-half-plane isometry

```text
A_P(z) = pi z - P
```

and the asymptotic

```text
A_P(cot(pi/(P+eta))) -> eta
```

for each fixed offset `eta` to argue that a recurring bounded prime pattern

```text
P + H
```

has a fixed finite-area hyperbolic right limit `S_H`.

That inference is false for the zero-twist prime-flute. Convergence of the selected boundary points after `A_P` does **not** freeze the Fenchel--Nielsen data of the corresponding pants block. Every distinguished cuff internal to a fixed bounded prime constellation has length tending to infinity.

Consequently the marked finite block cannot converge in Teichmuller/Fenchel--Nielsen coordinates to a fixed finite-area punctured surface with those internal pants curves. The Weyl-sequence implantation argument of PF-025 therefore has no valid geometric substrate as currently written.

## 1. Exact cuff data contradict a fixed marked finite-surface limit

Let two primes in a bounded translated pattern be

```text
p = P + eta_i,
q = P + eta_{i+1},
d = eta_{i+1} - eta_i > 0,
```

with `d` fixed while `P -> infinity`. Put

```text
u_p = cot(pi/p),
nu_q = cot(pi/q).
```

PF-001 gives exactly

```text
exp(-ell(p,q)/2)
  = (sqrt(nu_q)-sqrt(nu_p))
    /(sqrt(nu_q)+sqrt(nu_p)).
```

Since

```text
nu_{P+eta} = (P+eta)/pi + O(P^-1),
```

we obtain

```text
exp(-ell(p,q)/2)
  = d/(4P) + O(P^-2),
```

and hence

```text
boxed:
ell(p,q) = 2 log(4P/d) + o(1) -> infinity.
```

Thus every fixed internal prime gap in the bounded island produces an internal distinguished cuff whose geodesic length diverges.

For a fixed finite pants block, these cuff lengths are genuine Fenchel--Nielsen length coordinates. Fenchel--Nielsen coordinates determine the marked hyperbolic structure, so a sequence in which an internal length coordinate tends to `+infinity` cannot converge to one fixed marked finite-area hyperbolic surface in which the same essential curve has a finite geodesic representative.

External short separating curves from PF-007 do not remove this problem. Pinching a boundary neck to a cusp sends that boundary length to zero; it does not turn unrelated internal cuffs with length tending to infinity into finite coordinates.

## 2. Why the endpoint-normalization argument fails

The error can also be seen directly at the matrix level.

PF-004 uses

```text
G(a,b)
  = 1/(b-a) * [[a+b,-2ab],[-2,a+b]].
```

Its trace is

```text
tr G(a,b) = 2(a+b)/(b-a).
```

Conjugation by any hyperbolic isometry preserves the trace. Therefore for the actual conjugated generator

```text
G_tilde_P
  = A_P G(nu_p,nu_q) A_P^(-1)
```

we have

```text
tr G_tilde_P
  = 2(nu_p+nu_q)/(nu_q-nu_p)
  = 4P/d + O(1)
  -> infinity.
```

By contrast, if one takes the limiting translated endpoints and **rebuilds** a new matrix from the same formula, one gets

```text
G(eta_i,eta_{i+1})
```

with finite trace

```text
2(eta_i+eta_{i+1})/d.
```

Hence

```text
boxed:
A_P G(nu_p,nu_q) A_P^(-1)
  does not converge to
G(eta_i,eta_{i+1}).
```

In particular, the operation

```text
transform the endpoints by A_P
then rebuild G from the transformed endpoints
```

is not the same as conjugating the original prime-flute group.

This is exactly what the divergent cuff trace detects.

## 3. The missing geometric datum is the fan/base normalization

The prime-flute construction is not determined locally by the mutual differences of a bounded subset of endpoints alone. PF-001 already shows this: the canonical cuff depends on the ratio

```text
nu_q/nu_p,
```

not only on `nu_q-nu_p`.

Equivalently, the construction retains the distinguished fan/base normalization encoded by the ideal reference point used to build the zero-twist flute. Under

```text
A_P(z)=pi z-P,
```

that reference datum is moved to a location of order `-P`; it does not disappear merely because the selected cluster endpoints converge to the finite set `H`.

Cross-ratios involving only four selected endpoints remain Möbius invariant, which is why PF-004/PF-007 survive this correction. But the full marked pants geometry contains additional length data, and those data do not converge to the surface reconstructed from `H` alone.

## 4. Consequence for PF-025

The step

```text
recurring exact offset pattern H
  -> fixed finite-area surface S_H
```

is not established and, with the `A_P` argument used there, is false.

Therefore the subsequent claim

```text
Spec_L2(S_H) cap (0,1/4)
  subset sigma_ess(Delta_X_prime)
```

cannot currently be inferred from the recurring-prime-island construction. The abstract Weyl transplantation argument itself is standard and sound **if** one first has a genuine recurring geometric right limit, but PF-025 did not produce such a limit.

PF-025 should therefore be treated as superseded by this correction until a different geometric compactness/renormalization argument identifies an actual limit object.

## 5. What is still valid

This correction does **not** affect:

- PF-001: the exact distinguished-cuff formula;
- PF-004: the Möbius-invariant four-endpoint cross-ratio/geodesic identity;
- PF-005/PF-007: the existence of nonlocal simple classes with lengths tending to zero, subject to their stated topological audit;
- PF-019: finite four-endpoint cross-cusp identities after cusp normalization;
- PF-020/PF-027: the short-orbit and pinching obstructions.

The important distinction is now sharper:

```text
four-endpoint cross-ratio data
  -> can have finite/isometry-invariant limits;

full bounded prime island as a marked pants block
  -> contains distinguished cuffs ell_i -> infinity.
```

So a finite collection of convergent cross-ratios is not by itself enough to produce a finite-area surface right limit.

## 6. Spectral research consequence

The strongest previously surviving positive spectral candidate, PF-025, must be withdrawn in its current form.

A legitimate replacement would have to analyze the **singular large-cuff degeneration** of a bounded prime island rather than pretend that the island freezes after affine recentering. Possible limit objects could be re-marked/pointed surfaces, graph-like limits, or relative scattering objects, but each would need to be derived from the actual conjugated Fuchsian groups or from controlled Fenchel--Nielsen degeneration.

Until such a limit is identified, there is no justified pattern-specific family

```text
H -> Spec(S_H)
```

coming from the Pintz recurring-island argument.

## Literature / novelty check

No new external theorem is claimed here. The decisive input is internal consistency between two exact parts of the construction:

1. PF-001 forces the internal cuff lengths of a bounded translated prime cluster to diverge;
2. hyperbolic conjugation preserves traces/translation lengths.

The standard external fact used to interpret this is Fenchel--Nielsen theory: length and twist coordinates parameterize the marked hyperbolic structure of a fixed finite-type pants decomposition. Therefore divergent internal length coordinates are incompatible with convergence to the fixed marked finite-area surface postulated in PF-025.

This is a correction to our own candidate, not a novelty claim about hyperbolic degeneration.

## Lean candidates

The finite contradiction is a high-value formalization target:

1. prove the asymptotic `exp(-ell/2) ~ d/(4P)` for fixed `d`;
2. derive `ell -> infinity`;
3. prove trace invariance under conjugation;
4. show the trace of the conjugated `G(nu_p,nu_q)` diverges while the trace of `G(eta_i,eta_{i+1})` is fixed.

The Fenchel--Nielsen non-convergence conclusion can remain an imported geometric theorem layer.