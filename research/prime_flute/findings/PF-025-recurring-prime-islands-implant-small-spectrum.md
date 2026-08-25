# PF-025 — recurring prime islands implant pattern-specific small spectrum

**SUPERSEDED BY PF-028.** The affine endpoint recentering used below does not freeze the marked hyperbolic pants geometry: every distinguished cuff internal to a bounded translated prime pattern has length tending to infinity, and conjugating the actual generators preserves those divergent traces. Therefore the fixed finite-area right limit `S_H` asserted below is not produced by the stated argument, and the spectral implantation conclusion must not be used as an established candidate. The text is retained as research history; see `PF-028-bounded-prime-islands-do-not-have-the-claimed-fixed-surface-right-limit.md` for the correction.

**Status:** SUPERSEDED / INVALID AS STATED. The abstract Weyl-transplantation step would be valid given a genuine recurring geometric right limit, but this file does not establish such a limit.

## Statement

The isolated-cluster mechanism can be strengthened from “there are arbitrarily weak necks” to a genuine right-limit spectral statement.

Fix a sufficiently large integer `k0`. Pintz's Theorem 2 and its proof construct a finite set of bounded offsets

```text
H_m = {h_1 < ... < h_m}
```

depending only on `k0`, and infinitely many translates `P_j + H_m` containing at least `k0` consecutive primes, with prime-free intervals on both sides whose lengths tend to infinity on the Erdős–Rankin scale.

There are only finitely many subsets of `H_m`. Passing to an infinite subsequence therefore fixes one exact subset

```text
H = {eta_1 < ... < eta_r},   r >= k0,
```

such that at every selected occurrence the primes in the bounded island are exactly

```text
P_j + eta_1, ..., P_j + eta_r,
```

and the two exterior prime-free intervals tend to infinity.

Let `X_prime` be the zero-twist prime-flute. The claim is that the selected islands have a fixed finite-area hyperbolic right limit `S_H`, and

```text
Spec_L2(S_H) ∩ (0,1/4)  ⊆  sigma_ess(Delta_X_prime).
```

For `k0` sufficiently large, `S_H` has at least one positive eigenvalue below `1/4`. Consequently the prime-flute has at least one **pattern-selected** point of essential spectrum in `(0,1/4)` arising from a recurring bounded prime constellation.

This is materially stronger than the coarse statements `inf sigma_ess = 0` (PF-021) and `[1/4,infinity) subset sigma_ess` (PF-024): it places spectral points in the only interval where those universal arguments do not already determine membership.

## 1. The recurrence of one exact bounded constellation is unconditional

Pintz proves more than the existence of isolated bounded clusters. In the proof of Theorem 2 of arXiv:1406.2658, the candidate positions `h_1,...,h_m` are fixed once `k0` is fixed. The sieve forces every integer in a long interval outside those candidate positions to be composite, while Maynard–Tao supplies at least `k0` primes among the candidates.

Thus every occurrence determines a subset of one fixed finite set `H_m`. Since infinitely many occurrences exist and only finitely many subsets are possible, one subset `H` containing at least `k0` positions recurs infinitely often.

This removes an important ambiguity in PF-008: a **single finite prime pattern**, not merely clusters of bounded diameter, can be selected along an infinite subsequence.

Reference:

- J. Pintz, *On the ratio of consecutive gaps between primes*, arXiv:1406.2658v2, Theorem 2 and Section 4. The proof explicitly states that infinitely many blocks of at least `k0` consecutive primes occur in a bounded interval, preceded and followed by prime-free intervals of growing Erdős–Rankin size, and constructs them among a fixed finite set of offsets.

## 2. Exact prime-circle normalization gives a fixed hyperbolic local limit

**This section is the invalid step; see PF-028.**

For one occurrence with large base prime scale `P_j`, use the upper-half-plane isometry

```text
A_j(z) = pi z - P_j.
```

Since

```text
pi cot(pi/x) = x + O(1/x),
```

for every fixed integer offset `eta` we have

```text
A_j(cot(pi/(P_j+eta)))
  = pi cot(pi/(P_j+eta)) - P_j
  -> eta.
```

Hence the exact prime vertices of the recurrent island converge, after a genuine hyperbolic isometry, to the fixed endpoint configuration `H`.

The original version of this note then inferred that the Fuchsian side-pairing geometry converges to a fixed surface `S_H`. PF-028 shows that inference is false: the actual conjugated generators retain divergent traces and the internal Fenchel–Nielsen cuff lengths satisfy `ell_i -> infinity`.

The large prime-free intervals on both sides still give, through the exact PF-004 cross-ratio formula, short nonlocal separating classes under the hypotheses recorded in PF-007. That fact alone does not produce the fixed `S_H` claimed here.

## 3. Conditional Weyl-sequence argument

The following is a valid abstract mechanism **conditional on** first producing a genuine recurring smooth geometric right limit `S_H`; PF-028 shows that the construction in Section 2 does not do so.

Let

```text
lambda in Spec_L2(S_H) ∩ (0,1/4)
```

and let `phi` be a normalized `L2` eigenfunction.

Because `S_H` is complete, `C_c^infinity(S_H)` is a form/operator core for the Laplacian. We may choose compactly supported smooth functions `phi_m` with

```text
||phi_m|| -> 1,
||(Delta_S_H - lambda) phi_m|| -> 0.
```

If pairwise disjoint occurrences contained increasingly accurate copies of the supports of `phi_m`, transporting and extending by zero would give functions `Phi_m` on `X_prime` with

```text
||Phi_m|| -> 1,
||(Delta_X_prime - lambda) Phi_m|| -> 0,
Phi_m -> 0 weakly.
```

Weyl's criterion would then yield

```text
lambda in sigma_ess(Delta_X_prime).
```

Classical hyperbolic-degeneration theory supplies a surrounding framework for genuine pinching convergence; see Ji and Wolpert. What failed here is not Weyl's criterion but the identification of the actual prime islands with one fixed finite-area limit surface.

References:

- L. Ji, *Spectral degeneration of hyperbolic Riemann surfaces*, J. Differential Geom. 38 (1993), 263–313.
- S. A. Wolpert, *Spectral limits for hyperbolic surfaces, I*, Invent. Math. 108 (1992), 67–89.
- W. Hide and J. Thomas, *Small eigenvalues of hyperbolic surfaces with many cusps*, arXiv:2410.06093.

## 4. The former small-spectrum conclusion is withdrawn

The original note combined the asserted genus-zero finite-area limit with the Hide–Thomas lower bound to force a positive eigenvalue below `1/4` and then implant it into the essential spectrum.

Since the fixed finite-area surface `S_H` has not been obtained, that application is unavailable. In particular, this file no longer supports the conclusion

```text
0 < lambda_H < 1/4,
lambda_H in sigma_ess(Delta_X_prime).
```

Hide–Thomas remains a valid theorem about finite-area surfaces with many cusps; the missing object is the specific finite-area `S_H` that this note incorrectly claimed as the geometric limit of the recurring prime islands.

## 5. What remains true and potentially useful

The arithmetic recurrence statement remains valid: one exact bounded offset subset `H` can recur infinitely often inside isolated prime clusters.

The exact Möbius-invariant four-endpoint data also remain valid. In particular PF-004/PF-007 can produce finite or vanishing translation lengths for certain **composite/nonlocal** words even while the individual distinguished cuff lengths internal to the bounded cluster diverge.

This means the correct next problem is a singular-degeneration problem, not a frozen-surface problem:

```text
recurring bounded prime pattern
 + internal cuffs -> infinity
 + selected nonlocal necks -> 0
 -> determine the actual pointed/re-marked limit, if any.
```

Only after that limit is identified can a pattern-specific spectral implantation claim be reconsidered.

## 6. Novelty check

The ingredients in the original proposed theorem were individually standard or published. PF-028 found a direct incompatibility with the exact cuff formula already present in this repository, so no novelty claim from this file survives.

The research value of keeping this note is methodological: endpoint convergence under a convenient Möbius normalization is not enough to infer convergence of a marked Fuchsian quotient when other intrinsic length coordinates diverge.

## Research consequence

PF-025 is no longer the surviving positive spectral branch. The legitimate target is to understand the simultaneous degeneration

```text
internal distinguished cuffs -> infinity,
selected multi-gap separating curves -> 0,
```

using the actual conjugated group or controlled Fenchel–Nielsen geometry. Any future finite-surface right limit must pass this invariant-length check before spectral data are transplanted from it.