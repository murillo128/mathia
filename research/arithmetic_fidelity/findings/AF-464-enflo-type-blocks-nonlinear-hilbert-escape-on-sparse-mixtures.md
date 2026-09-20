# AF-464 — Enflo type blocks nonlinear Hilbert escape on sparse mixtures

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `SOURCE-LAW`, `QUANTITATIVE-FIDELITY`, `NONLINEAR-TARGET`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-457 and AF-458 show that bounded affine/barycentric encodings of increasingly complex sparse mixtures lose total-variation conditioning in Hilbert space and, more generally, in Banach targets of nontrivial Rademacher type. Their explicit boundary is that an arbitrary nonlinear encoder of the whole probability law is not constrained by those linear arguments.

That escape disappears as soon as the nonlinear encoder is required to have a finite upper Lipschitz modulus. The obstruction is metric, not linear.

Let `A` contain at least `2k` atoms and let

\[
\Delta_k(A)
=
\{\mu:\mu\text{ is a probability law supported on at most }k\text{ atoms}\}
\]

with source metric

\[
d_{TV}(\mu,\nu)=\|\mu-\nu\|_1.
\]

Let `Y` be a metric/Banach target of Enflo type `p in [1,2]` with constant `T_p^E(Y)` in the normalization

\[
\mathbb E_\varepsilon
\left\|
\frac{f(\varepsilon)-f(-\varepsilon)}{2}
\right\|^p
\le
T_p^E(Y)^p
\sum_{j=1}^k
\mathbb E_\varepsilon
\left\|
D_jf(\varepsilon)
\right\|^p,
\]

where

\[
D_jf(\varepsilon)
=
\frac{f(\varepsilon)-f(\varepsilon^{(j)})}{2}
\]

and `epsilon^(j)` flips the `j`-th sign. For an arbitrary map

\[
F:\Delta_k(A)\to Y,
\]

define its upper and lower TV moduli

\[
L(F)
=
\sup_{\mu\ne\nu}
\frac{d_Y(F\mu,F\nu)}{\|\mu-\nu\|_1},
\qquad
\kappa(F)
=
\inf_{\mu\ne\nu}
\frac{d_Y(F\mu,F\nu)}{\|\mu-\nu\|_1}.
\]

If `L(F)<infinity`, then

\[
\boxed{
\kappa(F)
\le
T_p^E(Y)\,L(F)\,k^{1/p-1}.
}
\tag{1}
\]

Equivalently, every bi-Lipschitz encoding obeys

\[
\boxed{
\frac{L(F)}{\kappa(F)}
\ge
\frac{k^{1-1/p}}{T_p^E(Y)}.
}
\tag{2}
\]

For Hilbert space, `p=2` and the cube inequality has constant `T_2^E=1`, so every arbitrary Lipschitz nonlinear encoder satisfies

\[
\boxed{
\kappa(F)\le \frac{L(F)}{\sqrt{k}},
\qquad
\operatorname{dist}(F)\ge\sqrt{k}.
}
\tag{3}
\]

Thus **nonlinearity alone cannot restore complexity-independent pairwise TV fidelity in a Hilbert destination**. To evade the square-root obstruction, a proposed representation must change the source metric, restrict the admissible source family enough to remove large metric cubes, leave the nontrivial-type target category, or abandon any complexity-independent upper sensitivity bound.

The same conclusion transfers to a restricted source class `S` whenever `S` contains the paired-mixture cube constructed below. No affine structure of the encoder is required.

## Exact derivation

Choose `2k` distinct atoms

\[
a_1,b_1,\ldots,a_k,b_k.
\]

For each `epsilon in {-1,+1}^k`, define the `k`-sparse law

\[
\mu_\varepsilon
=
\frac1k\sum_{j=1}^k
\begin{cases}
\delta_{a_j},&\varepsilon_j=+1,\\
\delta_{b_j},&\varepsilon_j=-1.
\end{cases}
\tag{4}
\]

If two sign vectors differ in `r` coordinates, then exactly `r` atoms of mass `1/k` move from one member of each pair to the other. Hence

\[
\boxed{
\|\mu_\varepsilon-\mu_\eta\|_1
=
\frac{2}{k}d_H(\varepsilon,\eta).
}
\tag{5}
\]

So `Delta_k(A)` contains an isometric copy, up to the fixed scale `2/k`, of the `k`-dimensional Hamming cube.

Set

\[
f(\varepsilon)=F(\mu_\varepsilon).
\]

A one-coordinate flip has source distance `2/k`; therefore

\[
\|f(\varepsilon)-f(\varepsilon^{(j)})\|
\le
\frac{2L(F)}{k},
\]

and in the Enflo normalization

\[
\|D_jf(\varepsilon)\|
\le
\frac{L(F)}{k}.
\tag{6}
\]

Apply Enflo type:

\[
\begin{aligned}
\mathbb E_\varepsilon
\left\|
\frac{f(\varepsilon)-f(-\varepsilon)}{2}
\right\|^p
&\le
T_p^E(Y)^p
\sum_{j=1}^k
\mathbb E_\varepsilon\|D_jf(\varepsilon)\|^p\\
&\le
T_p^E(Y)^p
k\left(\frac{L(F)}{k}\right)^p.
\end{aligned}
\tag{7}
\]

Hence at least one antipodal pair satisfies

\[
\frac{d_Y(f(\varepsilon),f(-\varepsilon))}{2}
\le
T_p^E(Y)L(F)k^{1/p-1}.
\tag{8}
\]

But antipodal sign vectors differ in all `k` coordinates, so by `(5)`

\[
\|\mu_\varepsilon-\mu_{-\varepsilon}\|_1=2.
\tag{9}
\]

Dividing `(8)` by `(9)` gives exactly `(1)`.

For Hilbert targets the constant-one case can also be derived directly by Walsh expansion. The diagonals-versus-edges identity gives

\[
\mathbb E\|f(\varepsilon)-f(-\varepsilon)\|^2
\le
\sum_{j=1}^k
\mathbb E\|f(\varepsilon)-f(\varepsilon^{(j)})\|^2,
\]

and `(3)` follows with no linearity assumption on `F`.

## Restricted-source form

The proof uses only the `2^k` laws in `(4)`. Therefore let `S` be any admissible source class equipped with TV distance. If there are paired atoms `a_j,b_j` for which every law `mu_epsilon` in `(4)` belongs to `S`, then every `L`-Lipschitz map `F:S->Y` obeys

\[
\boxed{
\kappa_S(F)
\le
T_p^E(Y)L(F)k^{1/p-1}.
}
\tag{10}
\]

This is a genuinely metric source certificate. AF-458 requires a full paired sign cube of normalized **secants** so that a linear target map can average signed differences. AF-464 instead requires a full cube of actual admissible **source points** and then applies metric type directly to an arbitrary nonlinear destination.

Consequently, a restricted arithmetic law can evade the nonlinear obstruction only by excluding such source-point cubes at growing dimension, or by distorting their source metric before the downstream representation is evaluated.

## What this adds to AF-457–AF-459

AF-457 gives the sharper Hilbert-specific affine ceiling `M/sqrt(2k)` under a per-atom norm budget. AF-458 extends the exponent to Banach targets of Rademacher type `p`, and AF-459 weakens exact affine cube completion to an average secant-completion profile. All three act through a linear signed-difference operator and explicitly leave arbitrary nonlinear encoders outside their scope.

AF-464 closes that particular escape at the metric level. Once both upper and lower sensitivity are measured in the same TV geometry, the source itself already contains Hamming cubes whose Euclidean/Hilbert distortion grows like `sqrt(k)`. The target does not need to be a barycenter, kernel mean, moment map, spectral mark, or any other linearized construction. State-dependent nonlinear features still face the same asymptotic incompatibility because Enflo type sees only distances.

The tradeoff is equally important: `(1)` is homogeneous in the upper modulus `L(F)`. An encoder can enlarge small distinctions by paying an equally growing upper sensitivity. Therefore the theorem rules out **uniform bi-Lipschitz conditioning**, not arbitrary injective nonlinear coding. That is the correct encoding-burden statement for this metric obstruction.

## Prior art and novelty audit

The mathematical obstruction is classical metric-embedding theory. **No novelty is claimed for Enflo type, Hamming-cube distortion, or the equivalence of Rademacher and Enflo type.**

- Per Enflo, **“On the nonexistence of uniform homeomorphisms between `L_p`-spaces,”** *Arkiv för Matematik* 8 (1969), 103–105, DOI `10.1007/BF02589549`. This is early foundational work introducing the cube/metric method behind unbounded distortion phenomena in Banach-space geometry.
- Paata Ivanisvili, Ramon van Handel, and Alexander Volberg, **“Rademacher type and Enflo type coincide,”** *Annals of Mathematics* 192(2), 665–678 (2020), DOI `10.4007/annals.2020.192.2.8`. They state Enflo type directly as a metric cube inequality and prove for every Banach space and `p in [1,2]` that
  \[
  T_p^R(Y)\le T_p^E(Y)\le\frac{\pi}{\sqrt2}T_p^R(Y).
  \]
  Thus the nonlinear cube obstruction is available exactly in the target categories whose linear Rademacher type drove AF-458.
- Assaf Naor, **“An introduction to the Ribe program,”** *Japanese Journal of Mathematics* 7(2), 167–233 (2012), DOI `10.1007/s11537-012-1222-7`. This is standard background for the program of translating linear Banach-space geometry into metric invariants and nonembeddability statements.

The line-specific derivation is the embedding `(4)`–`(5)` of the Hamming cube into the sparse probability simplex under TV and its use as a direct Arithmetic Fidelity source certificate. This is a specialization of classical metric type, not a new theorem in metric geometry.

## Boundary and falsification audit

- **Upper sensitivity is load-bearing.** Without a finite `L(F)`, no scale-normalized conclusion follows. Arbitrarily steep or discontinuous codes are outside the theorem; their encoding burden must be assessed separately.
- **This is stable fidelity, not injectivity.** Equation `(1)` does not force collisions. A nonlinear encoder may remain injective while its inverse conditioning deteriorates with `k`.
- **The source-point cube is stronger than secant richness.** A restricted source law may have many normalized completed secants yet exclude the actual `2^k` paired-mixture vertices needed by `(10)`. AF-459 remains the more flexible affine obstruction in that regime.
- **The source metric is TV / `ell^1`.** Replacing TV by Hellinger, Wasserstein, an arithmetic metric, or another intrinsic geometry changes the cube distances and requires a new audit.
- **The target type matters.** At `p=1`, `(1)` gives no decay. This is consistent with the `ell^1` boundary isolated by AF-456.
- **The Hilbert constant in `(3)` is sharp for the Hamming cube distortion but not claimed to be the sharp full-simplex lower-modulus constant.** AF-457's affine theorem has the stronger absolute factor `1/sqrt(2k)` because it exploits barycentric structure beyond the metric cube alone.
- **Finite alphabets impose a cutoff.** The dimension-`k` certificate requires `2k` distinct atoms.
- **No arithmetic conclusion follows merely from the unrestricted simplex.** A prime-facing application must prove that its actual admissible source family contains the paired-mixture cube or another metric cube of comparable dimension.

## Arithmetic specialization

Take the alphabet to be the rational primes. For unrestricted `k`-sparse probability laws on primes, every nonlinear representation

\[
F:\Delta_k(\mathbb P)\to H
\]

into Hilbert space with upper TV-Lipschitz modulus `L_k` has lower modulus

\[
\boxed{
\kappa_k\le\frac{L_k}{\sqrt{k}}.
}
\tag{11}
\]

Therefore no family of Hilbert-valued nonlinear encoders can have both a complexity-independent upper sensitivity and a complexity-independent inverse-TV margin as `k->infinity`. The obstruction is already present before any spectral, positive, quotient, determinant, trace, or asymptotic postprocessing.

For an actual arithmetic source law the decisive question is sharper: **does the admissible prime-derived family contain metric cubes of growing dimension under the source metric that the downstream theorem really consumes?** If yes, nonlinear Hilbert structure cannot rescue uniform pairwise fidelity. If not, the mechanism excluding those cubes is a concrete source rigidity worth isolating rather than treating “nonlinearity” itself as the escape.

## Consequence for the line

The current pairwise frontier after AF-463 is now split more cleanly. Convexity destroys pairwise linear protection by filling the affine paratingent direction space; AF-464 shows that simply making the destination nonlinear does not by itself evade the sparse-mixture obstruction when the source still contains large Hamming cubes and the destination has nontrivial metric type.

The remaining viable escape routes are therefore structurally narrower: a genuinely thin/nonconvex arithmetic source with bounded metric-cube dimension or increasing cube defect, a source metric in which those mixture cubes do not retain `ell^1` geometry, a target at the type-1 boundary, an encoding whose upper sensitivity necessarily grows and can be justified by the downstream theorem, or a source-anchored task that does not require arbitrary pairwise recovery.