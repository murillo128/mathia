# PF-025 — recurring prime islands implant pattern-specific small spectrum

**Status:** LITERATURE+DERIVED / substantive candidate. The proof chain uses standard ingredients, but the arithmetic-to-essential-spectrum specialization appears not to be covered by the literature located so far. One local topological identification inherited from PF-004/PF-007 should still receive an independent formal audit before this is promoted to a project theorem.

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

The Fuchsian side-pairing matrices and the orthogonal-circle geometry depend continuously on their real endpoints. Therefore every compact part of the island away from the two exterior collars converges smoothly to the corresponding compact part of a fixed finite hyperbolic surface `S_H`.

The large prime-free intervals on both sides give, through the exact PF-004 cross-ratio formula,

```text
sinh(L_j^-/4)^2 -> 0,
sinh(L_j^+/4)^2 -> 0,
```

so the two separating neck lengths satisfy

```text
L_j^- -> 0,
L_j^+ -> 0.
```

Pinching those two necks replaces them by cusps. In the standard tight-flute pants topology, an internal chain of `r` cusp pants has genus zero, `r` original cusps, and two geodesic boundary components; pinching the two boundaries gives a connected finite-area genus-zero surface with

```text
n_H = r + 2
```

cusps.

This topology is consistent with the standard definition of a tight flute as an infinite chain of tight pairs of pants.

**Audit boundary.** The remaining local geometric task is to write explicitly, in the prime side-pairing convention, that the two PF-004 words used in PF-007 are the simple primitive separating classes bounding exactly this finite pants block. Their translation-length formula is already exact; this is a topological word-identification check, not an analytic gap in the argument below.

## 3. A direct Weyl-sequence argument implants every small `L2` eigenvalue

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

For each `m`, choose an occurrence of `H` so far out that:

1. its two necks are sufficiently short;
2. the compact set containing `supp(phi_m)` is represented inside the island;
3. the metric on that compact set is sufficiently close to the metric of `S_H`.

Transport `phi_m` through this local almost-isometry and extend it by zero to obtain `Phi_m` on `X_prime`. Choose the occurrences pairwise disjoint and escaping every compact subset of `X_prime`.

Smooth convergence on the support gives

```text
||Phi_m|| -> 1,
||(Delta_X_prime - lambda) Phi_m|| -> 0.
```

Escaping supports give

```text
Phi_m -> 0 weakly.
```

Weyl's criterion therefore yields

```text
lambda in sigma_ess(Delta_X_prime).
```

This argument only needs local smooth convergence on larger and larger compact subsets. It does not require a global scattering theory, a Selberg trace formula, or bounded geometry of the whole infinite flute.

Classical hyperbolic-degeneration theory supplies a stronger surrounding framework for precisely this kind of pinching convergence; see, for example, Ji's work on spectral degeneration of hyperbolic Riemann surfaces and Wolpert's spectral-limit papers. Hide–Thomas also use explicit bi-Lipschitz comparison and eigenfunction transplantation when short geodesics are pinched to cusps.

References:

- L. Ji, *Spectral degeneration of hyperbolic Riemann surfaces*, J. Differential Geom. 38 (1993), 263–313.
- S. A. Wolpert, *Spectral limits for hyperbolic surfaces, I*, Invent. Math. 108 (1992), 67–89.
- W. Hide and J. Thomas, *Small eigenvalues of hyperbolic surfaces with many cusps*, arXiv:2410.06093, especially Section 4 on collapsing short geodesics and comparing small eigenvalues.

## 4. Such a recurrent limit can be forced to have positive small spectrum

Hide–Thomas prove the following current form of their topological lower bound:

```text
For every a > 0 there exists b > 0 such that
if g < a n, a finite-area hyperbolic surface of signature (g,n)
has at least b(2g+n-2) eigenvalues in [0,1/4).
```

Apply this to `S_H`, where `g=0` and `n=n_H=r+2`. Since Pintz allows `k0`, hence `r`, to be chosen arbitrarily large, choose it large enough that

```text
b(n_H-2) > 1.
```

The zero eigenvalue is simple on the connected finite-area surface `S_H`; therefore at least one further eigenvalue satisfies

```text
0 < lambda_H < 1/4.
```

By the Weyl argument,

```text
lambda_H in sigma_ess(Delta_X_prime).
```

Thus the combination of a prime-cluster theorem and hyperbolic spectral geometry gives an unconditional route to **nonzero essential spectrum below `1/4`** for the prime-flute, subject only to the explicit separating-word audit stated above.

Reference:

- W. Hide and J. Thomas, *Small eigenvalues of hyperbolic surfaces with many cusps*, arXiv:2410.06093, Theorem 1.3 in the current version.

## 5. What is and is not prime-specific

PF-015 already showed that the **number** of small eigenvalues on a genus-zero surface with many cusps is largely topological. That is not the new signal here.

The finer datum is

```text
H
 -> exact limiting endpoint/cross-ratio geometry
 -> S_H
 -> {lambda_j(S_H) : 0 < lambda_j < 1/4}
 -> sigma_ess(Delta_X_prime).
```

The exact positions of the eigenvalues of `S_H` depend on its moduli, which in this construction are selected by the recurrent prime offsets and their exact Möbius/cross-ratio geometry. A generic punctured sphere with the same number of cusps has no reason to have the same small eigenvalues.

This is therefore not a restatement of “there are many cusps” or “there are unusual prime gaps.” It is a mechanism by which a **fixed recurring finite arithmetic configuration can implant its finite-surface spectral data into the essential spectrum of one infinite hyperbolic surface**.

Important limitations:

- no injectivity is claimed: different patterns can in principle be isospectral;
- no Riemann-zero relation is claimed;
- no density or completeness statement for `sigma_ess ∩ (0,1/4)` is claimed;
- the coarse existence/count of small eigenvalues is not prime-specific;
- the potentially prime-specific object is the set of exact spectral positions attached to each recurrent right-limit surface `S_H`.

## 6. Novelty check

The ingredients are individually standard or published:

1. Pintz: recurring isolated bounded prime clusters from a fixed finite offset set;
2. exact prime-circle endpoint normalization and PF-004 cross-ratio neck geometry;
3. classical pinching convergence of hyperbolic surfaces;
4. Weyl's criterion for essential spectrum;
5. Hide–Thomas: many small eigenvalues on finite-area surfaces with many cusps.

Searches for combinations of prime gaps/prime constellations with hyperbolic Laplacian essential spectrum, Fuchsian right limits, or pinching spectral implantation did not locate a published version of this arithmetic specialization. General right-limit/limit-operator principles exist for Jacobi operators, graphs, and bounded-geometry settings, but they do not directly cover this degenerating infinite-type surface and are not needed for the direct Weyl construction above.

Accordingly, the **general spectral mechanism is not novel**, while the candidate contribution is the concrete prime-flute theorem obtained by composing these ingredients.

## Research consequence

This is the first branch in the spectral investigation that survives the repeated universality tests in a nontrivial way.

The useful target is no longer a scalar invariant such as

```text
delta,
inf sigma,
number of small eigenvalues,
Selberg convergence threshold,
```

but the family of pattern-dependent finite spectra

```text
H -> Spec_L2(S_H) ∩ (0,1/4).
```

A next serious test should compare two recurrent patterns with the same cusp count and determine whether their exact `S_H` moduli produce provably or numerically distinct small eigenvalues. That would test whether this channel carries actual relational prime information rather than merely topology.