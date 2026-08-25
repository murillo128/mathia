# PF-024 — cusp channels force universal high-energy essential spectrum

**Status:** NEGATIVE/OBSTRUCTION + EXACT LOCAL SPECTRAL DERIVATION + LITERATURE CHECKED.

This note closes another coarse Laplacian branch. The prime-flute has infinitely many genuine hyperbolic cusp ends. Those ends alone force the entire standard cusp continuum into the essential spectrum, independently of every prime gap, cuff length, shear, or multi-gap cross-ratio.

The project-specific conclusion is therefore negative: the **set of Laplacian spectral energies at and above `1/4` cannot be a prime-gap signature**. Any arithmetic information in the Laplacian must be finer than mere membership in the high-energy essential spectrum.

## 1. Exact local cusp model

After the standard cusp normalization, every cusp end contains a region isometric to

```text
C_T = [T, infinity)_t x (R/Z)_x
```

with metric

```text
ds^2 = dt^2 + exp(-2t) dx^2.
```

Equivalently, in upper-half-plane coordinates `y = exp(t)`, this is the usual quotient of a horoball by `z -> z+1`.

The positive Laplacian is

```text
Delta = -partial_t^2 + partial_t - exp(2t) partial_x^2.
```

On the zeroth Fourier mode in `x`,

```text
Delta_0 = -partial_t^2 + partial_t
```

acting in

```text
L^2([T,infinity), exp(-t) dt).
```

The unitary substitution

```text
f(t) = exp(t/2) g(t)
```

conjugates this exactly to

```text
U Delta_0 U^(-1) = -d^2/dt^2 + 1/4
```

on the half-line.

Thus the threshold `1/4` is already present in a single normalized cusp before any global Fuchsian or prime geometry is used.

## 2. Weyl packets for every `lambda >= 1/4`

Fix

```text
lambda = 1/4 + r^2,
r >= 0.
```

Let `chi` be a smooth compactly supported cutoff on an interval and set, schematically,

```text
g_R(t) = R^(-1/2) chi((t-T_R)/R) exp(i r t),
```

with `T_R -> infinity` and `R -> infinity`.

After normalization,

```text
||g_R||_2 = 1 + o(1)
```

and

```text
||(-d^2/dt^2 + 1/4 - lambda) g_R||_2 = O(1/R).
```

Pulling back by the exact unitary conjugacy and taking the zeroth cusp Fourier mode gives functions supported arbitrarily far out the cusp with

```text
||(Delta - lambda) f_R||_2 -> 0,
||f_R||_2 -> 1,
f_R weakly -> 0.
```

Hence Weyl's criterion gives

```text
[1/4, infinity) subset sigma_ess(Delta_X_prime).
```

No finite-generation, geometrical-finiteness, trace formula, Eisenstein continuation, or global scattering construction is required for this inclusion.

## 3. Infinitely many cusps make the obstruction stronger

The prime-flute contains infinitely many mutually disjoint cusp ends. For any fixed `lambda >= 1/4`, the above packets can be placed in arbitrarily many distinct cusps.

Therefore, for every integer `N`, one can construct an `N`-dimensional orthonormal family of cusp-localized approximate `lambda`-eigenfunctions with residual tending to zero.

This should be described conservatively as **arbitrarily large approximate channel multiplicity**. It proves essential-spectrum membership very robustly, but this note does not assert a full absolutely-continuous multiplicity theorem for the infinitely generated surface.

For finite-area surfaces with finitely many cusps, the classical stronger theorem states that the absolutely continuous spectrum is `[1/4,infinity)` with multiplicity equal to the number of cusps. The present Weyl construction is the part of that mechanism that survives without finite-type hypotheses.

## 4. Combination with PF-021

PF-021 established from the distinguished cuff growth that

```text
0 in sigma_ess(Delta_X_prime)
```

and in fact

```text
inf sigma_ess(Delta_X_prime) = 0.
```

PF-024 now gives

```text
[1/4, infinity) subset sigma_ess(Delta_X_prime).
```

Thus neither endpoint phenomenon is a fine prime-gap invariant:

```text
spectral bottom 0
    <- coarse amenable/Folner geometry from the cuff chain,

standard high-energy continuum [1/4,infinity)
    <- universal local cusp geometry.
```

The only part of the **spectral set itself** where a prime-specific distinction could still survive is therefore the interval

```text
(0, 1/4).
```

Even there, PF-015 already shows that mere abundance of small eigenvalues on large finite many-cusp pieces is strongly topological. What remains potentially meaningful is fine position/multiplicity/right-limit structure, not the existence of low energies by itself.

## 5. Consequences for scattering and resonances

This result also clarifies what a future scattering theory could and could not encode.

The real line

```text
s = 1/2 + i r
```

corresponds to

```text
lambda = s(1-s) = 1/4 + r^2.
```

The existence of these continuum energies is therefore not evidence for any prime-induced functional equation or critical-line mechanism. It is forced locally by each cusp's one-dimensional zero Fourier mode.

Prime information could still affect

```text
scattering phases,
off-diagonal cross-cusp coefficients,
poles after meromorphic continuation,
residues,
relative spectral shift,
```

provided those objects can be defined for the infinite-cusp surface. PF-016, PF-018, and PF-019 already eliminate several simpler interpretations of those quantities.

## 6. Interior/exterior duality

PF-017 showed that inversion in the unit circle exchanges the interior and exterior Poincare copies isometrically but is not an internal symmetry of one prime-flute.

Because the exterior copy is isometric to the interior copy, it has exactly the same local cusp Weyl construction. Thus the ambient interior/exterior duality duplicates this universal continuum; it does not split or select special energies.

## 7. Novelty check

The general cusp spectral mechanism is classical, not novel.

Literature anchors checked in this pass include:

- the standard finite-cusp theorem that a hyperbolic surface with `k` cusps has absolutely continuous spectrum `[1/4,infinity)` of multiplicity `k`;
- the decomposition principle for essential spectrum of Laplace-type operators on cusp manifolds;
- the reduction of the zero cusp Fourier mode to a one-dimensional half-line Schrödinger operator with threshold `1/4`.

Relevant sources include work of Werner Mueller on spectral theory of manifolds with cusps; Clara Aldana's account of relative determinants and cusp scattering; and Golenia--Moroianu on conformally cusp manifolds and the decomposition principle.

Targeted searches did not reveal a separate theorem needed for the infinitely many-cusp specialization: the explicit Weyl sequence above proves the inclusion directly. No novelty is claimed for the local theorem.

The substantive prime-flute result is a **negative classification**:

```text
Laplacian spectral-set information at lambda >= 1/4
```

is universal cusp background and must be subtracted conceptually before looking for arithmetic structure.

## 8. What remains alive

After PF-024 the Laplacian branch narrows to genuinely finer data:

```text
fine sigma_ess structure in (0,1/4),
right limits of isolated prime clusters,
positions and residues of relative/scattering poles,
non-leading transfer spectrum,
renormalized cross-cusp operators,
spectral shift relative to a justified noncompact background.
```

Any candidate that merely rediscovers `[1/4,infinity)` or the parameterization `s=1/2+ir` should now be rejected immediately as universal cusp geometry.