# VIS-385 — isotropic source-subspace null fixes defect-energy moments

## Claim

Fix `d>=2` and let

`V=Herm_0(d)`

be the real Hilbert space of traceless Hermitian `d x d` matrices with Hilbert-Schmidt inner product, of dimension

`N=d^2-1`.

For an `r`-dimensional source subspace `S subset V` with Hilbert-Schmidt orthonormal basis `E_1,...,E_r`, keep the intrinsic commutator Laplacian from `VIS-384`,

`Delta_S=sum_(a=1)^r ad_(E_a)^* ad_(E_a)`.

Then three exact source-free calibration facts hold.

First,

`Tr_Herm Delta_S = 2 d r`,

independently of the position of `S`, and

`ker Delta_S = {X in Herm(d): [X,E]=0 for every E in S}`.

Thus if `kappa=dim_R ker Delta_S`, the positive eigenvalues of `Delta_S` always have total mass `2dr` and mean

`2dr/(d^2-kappa)`.

Second, if `S` is Haar-uniform on the real Grassmannian `Gr(r,V)`, then

`E_S[Delta_S]=(2 d r/N) P_0`,

where `P_0` is the orthogonal projector from `Herm(d)` onto `Herm_0(d)`. Hence for any fixed Hermitian Gram tangent `G`, with traceless part

`G_0=G-tr(G)I/d`,

one has the exact isotropic defect-energy baseline

`E_S[epsilon_S(G)^2]=(2 d r/N)||G_0||_F^2`,

where `epsilon_S(G)^2=<G,Delta_S G>_F`.

Third, this null has an exact finite-dimensional variance. Define on `V`

`Q_G=ad_(G_0)^* ad_(G_0)`.

Then

`epsilon_S(G)^2 = Tr(P_S Q_G)`,

with `P_S` the orthogonal projector onto `S`, and

`Var_S[epsilon_S(G)^2]`
` = [2 r (N-r)/(N(N-1)(N+2))]`
`   * [Tr(Q_G^2) - Tr(Q_G)^2/N]`.

For traceless Hermitian `G_0`,

`Tr(Q_G)=2d ||G_0||_F^2`

and

`Tr(Q_G^2)=2d tr(G_0^4)+6||G_0||_F^4`.

Therefore the first two moments of the source-subspace defect energy under the isotropic rank-`r` null are determined exactly by `d`, `r`, and the second/fourth spectral moments of the fixed Gram tangent.

**Evidence/status:** `EXACT-DERIVED + SOURCE-FREE-NULL + CLASSICAL HAAR/COMMUTATOR ALGEBRA + NO-NOVELTY-CLAIM`.

No source-specific low-mode localization, Wang destination gain, zeta-zero statement, or RH consequence is claimed.

## 1. Every rank-`r` source subspace has the same total commutator spectral mass

For one traceless Hermitian `E` with `||E||_F=1`, diagonalize it with eigenvalues `e_1,...,e_d`. On Hermitian matrices, `ad_E^*ad_E` has eigenvalue `(e_i-e_j)^2` on each of the two real off-diagonal directions associated with an unordered pair `i<j`, and eigenvalue zero on the diagonal subspace. Hence

`Tr_Herm(ad_E^*ad_E)`
` = sum_(i != j) (e_i-e_j)^2`
` = 2d sum_i e_i^2 - 2(sum_i e_i)^2`
` = 2d`.

Summing over an orthonormal basis of `S` gives

`Tr_Herm Delta_S=2dr`.

Also

`<X,Delta_S X>_F=sum_a ||[E_a,X]||_F^2`,

so the quadratic form vanishes exactly when `X` commutes with every element of `S`. This proves the kernel statement.

The consequence for controls is immediate: once `d` and `r` are fixed, total commutator spectral mass is not an arithmetic resource. A candidate source-specific signal must live in the redistribution of that fixed mass, the commutant dimension, or the alignment of the Gram tangent with particular spectral sectors.

## 2. The full traceless source space is a scalar Casimir

Let `F_1,...,F_N` be any Hilbert-Schmidt orthonormal basis of `V=Herm_0(d)`. Completing it with `I/sqrt(d)` to an orthonormal Hermitian basis gives the standard completeness identities

`sum_a F_a X F_a = tr(X) I - X/d`

and

`sum_a F_a^2 = (d^2-1)I/d`.

Therefore

`sum_a [F_a,[F_a,X]]`
` = 2d X - 2 tr(X) I`
` = 2d P_0 X`.

Thus the source-subspace map is linear in the orthogonal projector onto `S`, and the full-space average is exactly scalar on the traceless sector.

If `S` is Haar-uniform in `Gr(r,V)`, rotational invariance gives

`E[P_S]=(r/N) I_V`.

Applying the linear commutator contraction yields

`E[Delta_S]=(r/N) Delta_V=(2dr/N)P_0`.

For fixed `G`, scalar parts commute with everything, so

`E[epsilon_S(G)^2]=(2dr/N)||G_0||_F^2`.

This is a first-stage source-free null: it deliberately destroys coupling between the observed source subspace and a fixed Gram tangent while preserving ambient dimension, source rank, and the Hilbert geometry fixed in `VIS-384`.

## 3. Exact Grassmann variance of the defect energy

On `V`, define `Q_G` by

`<H,Q_G H>_F=||[H,G_0]||_F^2`.

For an orthonormal basis `E_a` of `S`,

`epsilon_S(G)^2=sum_a <E_a,Q_G E_a>=Tr(P_S Q_G)`.

For a Haar-uniform rank-`r` projector `P` in real dimension `N`, orthogonal invariance forces the second moment to have the form

`E[P_ij P_kl]=A delta_ij delta_kl + B(delta_ik delta_jl + delta_il delta_jk)`.

The deterministic identities `Tr P=r` and `Tr P^2=r` determine

`B = r(N-r)/(N(N-1)(N+2))`

and

`A = r(r(N+1)-2)/(N(N-1)(N+2))`.

Contracting against a real symmetric operator `Q` gives

`Var[Tr(PQ)]`
` = [2r(N-r)/(N(N-1)(N+2))]`
`   * [Tr(Q^2)-Tr(Q)^2/N]`.

Taking `Q=Q_G` proves the stated variance formula.

To make the dependence on `G` explicit, diagonalize `G_0` with eigenvalues `g_i`. On Hermitian off-diagonal directions, `Q_G` has eigenvalues `(g_i-g_j)^2`, each twice for `i<j`. Therefore

`Tr(Q_G)=sum_(i != j)(g_i-g_j)^2=2d sum_i g_i^2`

because `sum_i g_i=0`, while

`Tr(Q_G^2)=sum_(i != j)(g_i-g_j)^4`
` = 2d sum_i g_i^4 + 6(sum_i g_i^2)^2`.

No asymptotic approximation is used.

## 4. What this null does and does not test

The isotropic Grassmann null calibrates the most basic question: is the actual source subspace unusually aligned with the fixed Gram tangent already at the quadratic commutator-defect level?

If the observed `epsilon_S(G)^2` is ordinary relative to the exact mean/variance above but the defect-normalized low-mode projector mass from `VIS-384` is unusual, then the surviving signal is genuinely about **spectral organization beyond the first defect-energy moment**. If the defect energy itself is already exceptional, then source coupling enters earlier and should be explained before crediting a more elaborate low-mode statistic.

This is not yet the full matched control required by `CLUE-wang-fixed-source-packet-localization`. A Haar-random subspace does not preserve every resource of an admissible Wang packet: operator-norm profile, approximate block structure, Gram clustering, destination metric constraints, or any other source-side structure may differ. The exact null is therefore a calibration layer and falsification control, not a substitute for the clue's stronger matched ensemble.

The moment formulas also require `G` to be held fixed independently while `S` is randomized. If a control resamples `G` jointly with `S`, the conditional formulas above cannot be used without accounting for that coupling.

## Prior-art and novelty audit

The ingredients are classical. The identity for the full traceless commutator sum is the finite-dimensional adjoint/Casimir completeness relation for Hermitian matrices. The random-projector first and second moments are standard consequences of Haar orthogonal integration; see Benoit Collins and Piotr Sniady, **Integration with respect to the Haar measure on unitary, orthogonal and symplectic group**, *Communications in Mathematical Physics* 264:3 (2006), 773--795, DOI `10.1007/s00220-006-1554-3`, arXiv `math-ph/0402073`.

The formulas used here are derived directly from orthogonal invariance plus `Tr P=r` and `Tr P^2=r`; no new Haar-integration, random-projection, Casimir, or matrix-moment theorem is claimed.

The Mathia-specific content is the control consequence for the `VIS-384` source-subspace localization channel: fixed source rank already fixes total commutator spectral mass, and a Haar-random source subspace gives an exact finite-dimensional mean/variance baseline for the Gram defect energy before any nonlinear low-mode localization statistic is credited.

A local repository audit found no existing Visual Exploration finding that supplies this isotropic source-subspace null or the exact defect-energy variance for the current Wang localization clue.

## Dependencies

- `VIS-382`: defect-squared low positive commutator modes are necessary for persistent bounded output orientation.
- `VIS-383`: raw generator-coordinate metrics can manufacture defect-normalized localization.
- `VIS-384`: the centered Hilbert-Schmidt source subspace `S` and `Delta_S` remove generator-coordinate gauge.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue requiring matched source-free controls for source-specific low-mode overlap.

## Research consequence

Before interpreting defect-squared low-mode excess as source-specific, calibrate the actual pair `(G,S)` against the isotropic fixed-`G`, rank-`r` source-subspace null. The null supplies exact total spectral mass, exact mean defect energy, and exact finite-dimensional variance with no simulation error.

This creates a clean fork for the accepted clue. An anomalous defect energy means the arithmetic/source coupling is already visible at the quadratic commutator level and should be identified there. A normal defect energy together with anomalous low-mode projector mass isolates a genuinely higher-order spectral-localization question. Either outcome is more informative than comparing raw low modes without first pricing the universal Grassmann baseline.