# VIS-387 — qubit source-subspace spectral shape collapses to defect energy

## Claim

Let

`V = Herm_0(2)`

be the real Hilbert space of traceless Hermitian `2 x 2` matrices with Hilbert-Schmidt inner product, so `dim V = 3`. Let `S subset V` be an `r`-dimensional source subspace, `1 <= r <= 3`, with orthogonal projector `P_S`, and define the positive commutator Laplacian

`Delta_S = sum_(a=1)^r ad_(E_a)^* ad_(E_a)`

for any Hilbert-Schmidt orthonormal basis `{E_a}` of `S`.

Then, under the standard Pauli/Bloch identification of `V` with `R^3`,

`Delta_S = 2 (r I - P_S)`.

Consequently the qubit source-subspace spectrum has no independent shape freedom once the scalar defect energy is fixed.

For `r=1`, the spectrum on `V` is `{0,2,2}`; after removing the source kernel, every nonzero source-visible spectral measure is a single atom. For `r=3`, `Delta_S=4I`, again giving a single normalized atom. For `r=2`, the spectrum is `{2,2,4}`. If `g in V`, `g != 0`, and

`p = ||P_S g||^2 / ||g||^2`,

then the source-visible spectral measure is exactly

`mu_(S,g) = p delta_2 + (1-p) delta_4`,

while its scalar defect rate is

`m_(S,g) = <g, Delta_S g> / ||g||^2 = 4 - 2p`.

Hence

`p = (4 - m_(S,g))/2`,

so the complete spectral measure, and therefore any normalization of its positive spectral shape, is already determined by the scalar defect rate. In dimension `d=2`, normalized commutator-Laplacian spectral shape cannot provide a source-specific channel beyond the calibrated scalar defect observable of `VIS-385`.

**Evidence/status:** `EXACT-DERIVED + DIMENSIONAL NO-GO + CLASSICAL PAULI/SU(2) INGREDIENTS + NO-NOVELTY-CLAIM FOR LIE-ALGEBRA BACKGROUND`.

## 1. Pauli/Bloch reduction

Use the orthonormal Pauli basis

`F_i = sigma_i / sqrt(2)`, `i=1,2,3`,

for `V`. The classical Pauli commutation relation gives

`[F_i,F_j] = i sqrt(2) epsilon_(ijk) F_k`.

Write

`E = e . F`, `X = x . F`

with `e,x in R^3`. Then

`[E,X] = i sqrt(2) (e x x) . F`,

where `e x x` denotes the ordinary vector cross product, and therefore

`||[E,X]||_HS^2 = 2 ||e x x||^2`.

Let `{E_a}` be an orthonormal basis of `S`, corresponding to an orthonormal family `{e_a}` in `R^3`. By definition of the positive commutator Laplacian,

`<X, Delta_S X> = sum_a ||[E_a,X]||_HS^2`

`= 2 sum_a (||x||^2 - (e_a . x)^2)`

`= 2 (r ||x||^2 - ||P_S x||^2)`.

Because this holds for every `x`, polarization gives the operator identity

`Delta_S = 2(r I - P_S)`.

This identity is basis-independent and uses only the three-dimensional adjoint/Bloch geometry specific to the qubit case.

## 2. Rank-by-rank spectral collapse

### Rank one

If `r=1`, then

`Delta_S = 2(I-P_S)`.

Thus `S` is the zero eigenspace and `S^perp` is the eigenvalue-`2` eigenspace. Once the zero mode is removed, there is no spectral-shape parameter left: every nonzero positive spectral measure is concentrated at `2`, and mean normalization sends it to `delta_1`.

### Rank three

If `r=3`, then `P_S=I`, so

`Delta_S = 4I`.

Again every normalized spectral measure is `delta_1`.

### Rank two

If `r=2`, then

`Delta_S = 4I - 2P_S`.

It acts by `2` on `S` and by `4` on the one-dimensional complement `S^perp`. For nonzero `g`, let

`p = ||P_S g||^2 / ||g||^2`.

The spectral theorem immediately gives

`mu_(S,g) = p delta_2 + (1-p) delta_4`.

Its first moment is

`m_(S,g) = 2p + 4(1-p) = 4-2p`.

Therefore the first moment recovers the only shape weight exactly. If the spectral coordinate is normalized by its mean, then

`mu_bar_(S,g) = p delta_(2/m) + (1-p) delta_(4/m)`

with `p=(4-m)/2`; normalization does not create an additional invariant. The same conclusion holds for any statistic of this two-atom measure: it is a deterministic function of the scalar defect rate.

For comparisons in which `g` is fixed, `||g||` is fixed as well, so the unnormalized defect energy `<g,Delta_S g>` carries exactly the same information as `m_(S,g)`.

## 3. Exact isotropic rank-two null

The rank-two case also admits an elementary exact isotropic calibration. A random two-plane `S in Gr(2,3)` can be represented by a uniformly random unit normal `n in S^2`. For `g_hat=g/||g||`, put

`q = (n . g_hat)^2`.

Then

`q ~ Beta(1/2,1)`,

`p = 1-q`,

and

`m_(S,g) = 2 + 2q`.

In particular,

`E m_(S,g) = 2 + 2/3 = 8/3`.

This agrees exactly with the `VIS-385` isotropic defect-energy mean

`E m = 2 d r / (d^2-1)`

at `d=2`, `r=2`. The agreement is a consistency check between the Grassmannian null model and the explicit qubit spectral decomposition, not an additional independence result.

## 4. Consequence for the Wang packet clue

The accepted clue

`research/visual_exploration/clues/CLUE-wang-fixed-source-packet-localization.md`

asks whether unitary-conjugacy-invariant spectral data of `Delta_S` can carry source-specific information after the exact scalar defect/scale calibrations of `VIS-385` and `VIS-386`.

The qubit case is now closed negatively: at `d=2`, the complete commutator-Laplacian spectral measure is fixed by source rank together with the scalar defect rate. There is no residual normalized spectral-shape degree of freedom for a Wang-packet discriminator to exploit.

Therefore any genuinely independent spectral-shape test in this branch must begin at `d>=3`, where `Herm_0(d)` no longer reduces to the three-dimensional cross-product geometry and `Delta_S` need not be an affine function of the source projector alone.

This does not establish that an independent shape channel exists for `d>=3`; it identifies the first dimension in which the qubit obstruction no longer proves that such a channel is impossible.

## Prior-art and novelty audit

The algebra used here is classical: the Pauli commutation relations, the Bloch-vector identification of traceless Hermitian `2 x 2` matrices with `R^3`, and the adjoint `SU(2)` / rotation-group geometry are standard. No novelty is claimed for those ingredients or for the general fact that qubit commutators reduce to cross products.

A targeted prior-art orientation around the `SU(2)` adjoint representation, Bloch-sphere commutator geometry, and Pauli cross-product formulas found the expected classical background. This finding therefore makes only the narrower Mathia claim proved above: for the particular source-subspace commutator Laplacian used by the current Wang-packet branch, that classical three-dimensional geometry forces an exact dimensional no-go for spectral shape beyond scalar defect energy. No broader literature-level novelty claim is made for that consequence.

## Boundaries

- The result is specific to `d=2`. It gives no positive spectral-shape result in `d>=3`.
- The scalar comparison is the defect rate `m=<g,Delta_S g>/||g||^2`; for fixed `g`, this is equivalent to the defect energy used in `VIS-385`.
- The global identity direction is outside `V=Herm_0(2)` and is not part of the stated spectrum.
- The zero vector `g=0` is excluded from normalized spectral measures.
- The result does not validate Wang localization, prove any Riemann-hypothesis implication, or show that higher-dimensional spectral shape is arithmetically informative.
- No retained visualization is needed: the obstruction is exact and representation-independent once the standard Pauli/Bloch identification is fixed.
