# PF-019 — exact cross-cusp scattering channel and a noncompactness obstruction

**Status:** `EXACT-DERIVED` + standard cusp-scattering theory + `NEGATIVE/OBSTRUCTION` for a naive countable scattering determinant.

## Claim

The four-endpoint cross-ratio from PF-004 survives independent cusp normalization and appears directly in the standard Dirichlet-series formula for an off-diagonal scattering coefficient.

For

```text
a < b < c < d
X = b-a
Y = c-b
Z = d-c
```

use the prime-flute generator convention

```text
G(x,y) = 1/(y-x) * [[x+y, -2xy], [-2, x+y]].
```

The adjacent parabolic stabilizers are

```text
P_b = G(a,b) G(b,c)^(-1)
P_c = G(b,c) G(c,d)^(-1).
```

Their fixed points are `-b` and `-c` in this matrix convention. Define

```text
W_b = 2(1/X + 1/Y)
W_c = 2(1/Y + 1/Z).
```

The determinant-one scaling matrices

```text
sigma_b = [[-b sqrt(W_b), -1/sqrt(W_b)],
           [   sqrt(W_b),             0]]

sigma_c = [[-c sqrt(W_c), -1/sqrt(W_c)],
           [   sqrt(W_c),             0]]
```

normalize both primitive cusp stabilizers:

```text
sigma_b^(-1) P_b sigma_b = [[-1, 1], [0,-1]]
sigma_c^(-1) P_c sigma_c = [[-1, 1], [0,-1]].
```

Projectively these generate the standard unit-translation parabolic subgroup, so the raw cusp-width gauge identified in PF-018 has been removed.

Now consider the identity group element as a double-coset representative from cusp `b` to cusp `c`. Direct multiplication gives

```text
M_bc = sigma_b^(-1) sigma_c
```

with lower-left entry

```text
c_0 = sqrt(W_b W_c) (c-b).
```

Therefore exactly

```text
c_0^2
  = 4 (X+Y)(Y+Z)/(XZ).
```

Using the PF-004 cross-ratio

```text
chi = Y(X+Y+Z)/(XZ),
```

we get

```text
(X+Y)(Y+Z)/(XZ) = 1 + chi,
```

hence

```text
c_0 = 2 sqrt(1+chi).
```

PF-004 gives

```text
sinh(L/4)^2 = chi,
```

where `L` is the corresponding separating closed-geodesic length. Thus

```text
boxed: c_0 = 2 cosh(L/4).
```

This is an exact relation after canonical cusp normalization. Unlike the raw `W_b` of PF-018, `|c_0|` is unchanged by the remaining left/right unit translations in the choices of scaling matrices.

## Scattering interpretation

For a finite-area cusped Fuchsian surface, the standard off-diagonal scattering coefficient has, in `Re(s)>1`, a Dirichlet-series expansion of the form

```text
Phi_bc(s)
  = A(s) sum_D m(D) |c(D)|^(-2s),

A(s) = sqrt(pi) Gamma(s-1/2)/Gamma(s),
```

where `D` runs over cusp double cosets represented in

```text
sigma_b^(-1) Gamma sigma_c
```

and `c(D)` is the lower-left matrix entry after the width-one cusp normalization. In the usual weight-zero zero-frequency coefficient, the multiplicities are non-negative counts.

The identity double coset is therefore a genuine term with

```text
|c(D_id)|^(-2s)
  = [2 cosh(L/4)]^(-2s)
  = 2^(-2s) (1+chi)^(-s).
```

For real `s>1` this gives the positive lower bound

```text
Phi_bc(s)
  >= A(s) [2 cosh(L/4)]^(-2s)
```

whenever the classical scattering expansion is available.

For the exact prime endpoints

```text
u_n = cot(pi/p_n),
```

all of `X,Y,Z,chi,L` above are the exact quantities from the prime-flute, not their linearized shadows.

## Prime-gap consequence

PF-005 imports a theorem on three consecutive prime gaps that supplies infinitely many indices for which

```text
chi_n -> 0
L_n   -> 0.
```

Along that subsequence the normalized direct cusp-to-cusp scattering denominator satisfies

```text
c_0,n -> 2,
```

and therefore, for each fixed real `s>1`, the direct scattering contribution tends to the nonzero universal value

```text
A(s) 2^(-2s).
```

Equivalently,

```text
[2 cosh(L_n/4)]^(-2s)
  = 2^(-2s) (1 - s chi_n + O(chi_n^2)).
```

So the extreme prime-gap event does not create a singular local scattering factor. It produces a finite, strongly coupled cross-cusp channel whose prime-specific correction is of order `chi_n`.

## Countably many cusps: obstruction to a naive determinant

The full prime-flute has countably many cusps. Suppose one tries to assemble the normalized cusp coefficients, in the absolutely convergent half-plane, into an operator

```text
Phi(s) : ell^2(cusps) -> ell^2(cusps)
```

using the canonical unit-width channel normalization.

On the PF-005 subsequence there are distinct adjacent cusp pairs `(i_k,j_k)` with

```text
|Phi(s)_{i_k,j_k}| >= c_s > 0
```

for fixed real `s>1`, because the identity-double-coset contribution alone has a positive lower bound.

Hence any operator realization with these matrix coefficients cannot be compact. Indeed the standard basis vectors `e_{j_k}` converge weakly to zero, whereas

```text
||Phi(s) e_{j_k}|| >= c_s.
```

The same statement applies to `Phi(s)-I`, since these are off-diagonal entries.

Therefore the most naive infinite-cusp analogue

```text
det_Fredholm Phi(s)
```

or a determinant obtained by treating `Phi(s)-I` as a trace-class perturbation of a direct sum of decoupled standard cusp channels is obstructed already in the initial half-plane. If the countable matrix does not define a bounded operator at all, the obstruction is stronger.

This does **not** rule out every relative scattering construction. A viable determinant would have to subtract or absorb a genuinely noncompact cross-cusp background rather than only the independent local cusp models.

## Why this matters

This is the first exact bridge found in this line where the PF-004 multi-gap cross-ratio enters a standard spectral/scattering formula **after** the local cusp gauges have been removed:

```text
four prime vertices
    -> Möbius cross-ratio chi
    -> separating geodesic L
    -> normalized cusp double-coset coefficient c_0
    -> an actual term of Phi_bc(s).
```

At the same time it gives a negative structural result: the infinitely many arithmetically forced almost-pinched configurations prevent the normalized all-cusp scattering matrix from being a compact perturbation of the decoupled cusp identity.

## Novelty / literature audit

The ingredients are standard separately:

1. cusp scaling matrices normalize primitive parabolics to unit translation;
2. for finite-area cusped surfaces, scattering entries are Dirichlet series over cusp double cosets with weights `c^(-2s)`;
3. Penner lambda-length/decorated-Teichmuller theory gives the general geometric role of normalized cusp-to-cusp quantities and cross-ratios;
4. degeneration of Eisenstein/scattering data under pinching is a classical subject.

A targeted search did **not** locate the prime-gap specialization

```text
c_0 = 2 cosh(L/4)
```

combined with PF-005 to force non-decaying off-diagonal channels in a countably cusped prime-flute. Treat the algebraic identity as a strong Lean candidate; treat the infinite-operator/scattering conclusion as analytically conditional on the precise operator realization, but the compactness obstruction itself is elementary once those matrix coefficients are admitted.

Useful literature anchors for later audit:

- standard finite-area scattering coefficient formula via cusp scaling matrices and Kloosterman/double-coset Dirichlet series;
- Penner decorated Teichmuller theory and lambda lengths;
- Obitsu, and Garbin--Jorgenson--Munn, on Eisenstein series under hyperbolic degeneration;
- general convergence results for Eisenstein-type series on Fuchsian groups in a right half-plane.

## Lean candidates

High-value finite core:

1. verify both cusp-normalization identities;
2. verify the lower-left entry of `sigma_b^(-1) sigma_c`;
3. prove `c_0^2 = 4(1+chi)`;
4. combine with PF-004 to prove `c_0 = 2 cosh(L/4)` under positivity hypotheses.

The scattering Dirichlet-series theorem and the functional-analytic compactness statement should remain separate theorem-import layers.