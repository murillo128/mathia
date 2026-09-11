# PF-290 — optimized local low/high correlation is an exact high-band shorting deficit

**Status:** `EXACT-DERIVED + CLASSICAL-SHORTED-FORM-IDENTITY + PF-289-OPERATIONALIZATION + POSITIVE/ROUTE-NARROWING`.

[[research/prime_flute/findings/PF-289-fixed-local-rayleigh-floors-suffice-for-a-heavy-angle-noncompactness-witness|PF-289]] reduces the cheapest fixed-threshold compactness falsifier to one local quantity: the energy-normalized mixed correlation between a PF-216 low-symmetric vector and a PF-227 physical-high witness with a fixed positive diagonal Rayleigh floor. The remaining vector choice can itself be removed exactly.

On each PF-227 adjacent-pant window, collect the finite-dimensional physical-high source/target witness directions into a local space `W_n`. PF-227 and positivity imply that the restriction of the diagonal precision form to `W_n` has spectral radius at least the fixed high/high crossing constant `b>0`. Therefore the local spectral subspace

\[
W_n^\sharp:=\mathbf 1_{[b/2,\infty)}(G_n)W_n,
\]

where `G_n` is the restricted form operator, is nonzero and every nonzero `h\in W_n^\sharp` automatically satisfies

\[
\frac{k[h]}{\|h\|^2}\ge b/2.
\]

For either PF-216 low vector `\ell_r` supported on an endpoint module of the same window, define the **high-band shorting deficit**

\[
\boxed{
\delta_{n,r}
:=
1-
\frac{\inf_{h\in W_n^\sharp} k[\ell_r+h]}
{k[\ell_r]}.
}
\]

Then, exactly,

\[
\boxed{
\delta_{n,r}
=
\sup_{0\ne h\in W_n^\sharp}
\frac{|k[\ell_r,h]|^2}{k[\ell_r]\,k[h]}
=
\frac{\|\Pi_{R W_n^\sharp}R\ell_r\|^2}{\|R\ell_r\|^2},
}
\]

where `R=K^{1/2}` is the canonical energy map and `\Pi_{R W_n^\sharp}` is orthogonal projection in the common energy space. Thus the optimized PF-289 correlation is the square root of a scalar variational energy drop. In a finite basis it is also an ordinary Schur-complement quantity,

\[
\boxed{
\delta_{n,r}
=
\frac{c_{n,r}^*G_{n,\sharp}^{-1}c_{n,r}}
{k[\ell_r]},
}
\]

with `G_{n,\sharp}` the positive Gram matrix `k[h_i,h_j]` on `W_n^\sharp` and `c_{n,r,i}=k[h_i,\ell_r]`.

Consequently the current local noncompactness test no longer requires selecting, phasing, or following individual PF-227 singular vectors. If, on a sparse separated tail,

\[
\limsup_n\max_{r\in\{n,n+1\}}\delta_{n,r}>0,
\]

then PF-289 applies with the automatically coercive optimizer in `W_n^\sharp`: one obtains a fixed positive heavy-angle compression that is noncompact, hence the PF-281/PF-282 mixed operator `T` is noncompact and the current weak-trace endpoint route fails.

The converse is deliberately not claimed. If these deficits tend to zero, only the **PF-227 local witness-band falsifier** has failed; other physical-high directions or global heavy-range geometry may still obstruct compactness.

## Claim

Let `k` be the closed nonnegative PF-281/PF-282 precision form on

\[
\mathcal H=\mathcal H_P\oplus\mathcal H_H,
\]

with associated nonnegative operator `K` and canonical energy map

\[
R:=K^{1/2}.
\]

Let `W\subset H\operatorname{Dom}k` be a nonzero finite-dimensional subspace, and let `G_W` be the unique nonnegative operator on `W`, with the inherited Hilbert inner product, satisfying

\[
\langle G_Wh,g\rangle=k[h,g],
\qquad h,g\in W.
\tag{1}
\]

Fix `M>0` and put

\[
W^\sharp:=\mathbf1_{[M,\infty)}(G_W)W.
\tag{2}
\]

Assume `W^\sharp\ne\{0\}`. Then every `h\in W^\sharp` satisfies

\[
\boxed{k[h]\ge M\|h\|^2.}
\tag{3}
\]

For any `0\ne\ell\in P\operatorname{Dom}k` with `k[\ell]>0`, define

\[
\eta_W(\ell)
:=
\sup_{0\ne h\in W^\sharp}
\frac{|k[\ell,h]|}
{\sqrt{k[\ell]k[h]}}
\tag{4}
\]

and

\[
\delta_W(\ell)
:=
1-
\frac{\inf_{h\in W^\sharp}k[\ell+h]}
{k[\ell]}.
\tag{5}
\]

Then

\[
\boxed{
0\le\delta_W(\ell)\le1,
\qquad
\delta_W(\ell)=\eta_W(\ell)^2.
}
\tag{6}
\]

More precisely, with

\[
\mathcal M_W:=R(W^\sharp),
\qquad
e_\ell:=\frac{R\ell}{\sqrt{k[\ell]}},
\tag{7}
\]

one has

\[
\boxed{
\eta_W(\ell)=\|\Pi_{\mathcal M_W}e_\ell\|,
\qquad
\inf_{h\in W^\sharp}k[\ell+h]
=k[\ell]\bigl(1-\eta_W(\ell)^2\bigr).
}
\tag{8}
\]

Because of (3), `R|_{W^\sharp}` is injective and `\mathcal M_W` is finite-dimensional. Hence both the supremum and infimum are attained.

If `(h_1,\ldots,h_d)` is any basis of `W^\sharp`, set

\[
(G_\sharp)_{ij}:=k[h_i,h_j],
\qquad
(c_\ell)_i:=k[h_i,\ell].
\tag{9}
\]

Then `G_\sharp` is positive definite and

\[
\boxed{
\eta_W(\ell)^2
=\delta_W(\ell)
=\frac{c_\ell^*G_\sharp^{-1}c_\ell}{k[\ell]}.
}
\tag{10}
\]

The formula is basis invariant.

### PF-227/PF-216 specialization

Let `b>0` be the fixed PF-227 high/high crossing constant. On one PF-227 local adjacent-pant window, let `W_n\subset H\operatorname{Dom}k` be the finite-dimensional span of the physical-high source and target witness images used by the crossing estimate. PF-227 supplies unit vectors `x_n,y_n\in W_n` with

\[
|k_H[y_n,x_n]|\ge b.
\tag{11}
\]

Form Cauchy--Schwarz gives

\[
k_H[x_n]k_H[y_n]\ge b^2,
\tag{12}
\]

so at least one of the two diagonal energies is at least `b`. Therefore

\[
\|G_{W_n}\|\ge b
\tag{13}
\]

and

\[
\boxed{
W_n^\sharp
:=\mathbf1_{[b/2,\infty)}(G_{W_n})W_n
\ne\{0\}.
}
\tag{14}
\]

Every nonzero vector in this space has the PF-289 high Rayleigh floor `b/2`.

For the PF-216 unit low-symmetric vectors `\ell_n,\ell_{n+1}` on the two endpoint modules of the same window, define

\[
\delta_n
:=
\max\{\delta_{W_n}(\ell_n),\delta_{W_n}(\ell_{n+1})\}.
\tag{15}
\]

If

\[
\boxed{\limsup_{n\to\infty}\delta_n>0,}
\tag{16}
\]

then choose a separated subsequence of windows and, on each window, an endpoint `r_n` and optimizer `h_n\in W_n^\sharp` realizing the corresponding correlation. Equations (3), (6), and PF-216 give fixed constants `M_H=b/2`, `c>0` and a tail low floor with

\[
\frac{k[\ell_{r_n}]}{\|\ell_{r_n}\|^2}\to\infty,
\qquad
\frac{k[h_n]}{\|h_n\|^2}\ge b/2,
\qquad
\frac{|k[\ell_{r_n},h_n]|}
{\sqrt{k[\ell_{r_n}]k[h_n]}}
\ge c.
\tag{17}
\]

PF-214 locality supplies the required cross-window energy orthogonality after sparsification. PF-289 therefore implies that some fixed positive heavy-angle compression is noncompact, and hence

\[
\boxed{T\text{ is noncompact}.}
\tag{18}
\]

## 1. The correlation optimization is just an energy-space projection

For `h\in W^\sharp`,

\[
k[\ell,h]=\langle R\ell,Rh\rangle,
\qquad
k[\ell]=\|R\ell\|^2,
\qquad
k[h]=\|Rh\|^2.
\tag{19}
\]

Because `R(W^\sharp)=\mathcal M_W`, equation (4) is exactly the norm of the linear functional induced by the unit vector `e_\ell` on the finite-dimensional subspace `\mathcal M_W`. Therefore

\[
\eta_W(\ell)
=
\sup_{0\ne z\in\mathcal M_W}
\frac{|\langle e_\ell,z\rangle|}{\|z\|}
=
\|\Pi_{\mathcal M_W}e_\ell\|.
\tag{20}
\]

This removes the phase and basis dependence of an individual high witness. The optimizer is simply the pullback under `R|_{W^\sharp}` of the projection of `R\ell` onto the admissible high energy range.

## 2. The same number is a shorting deficit

The variational problem (5) is

\[
\inf_{h\in W^\sharp}\|R\ell+Rh\|^2
=
\operatorname{dist}(-R\ell,\mathcal M_W)^2.
\tag{21}
\]

Orthogonal projection gives

\[
\operatorname{dist}(-R\ell,\mathcal M_W)^2
=
\|R\ell\|^2-\|\Pi_{\mathcal M_W}R\ell\|^2.
\tag{22}
\]

Dividing by `k[\ell]=\|R\ell\|^2` proves (6)--(8).

In coordinates, minimizing

\[
k\!\left[\ell+\sum_i a_i h_i\right]
\tag{23}
\]

is the positive-definite normal equation with Gram matrix `G_\sharp`. Completing the square gives (10). Thus the decisive quantity can be obtained either as a principal-angle projection norm, a local constrained Dirichlet minimum, or a finite Gram/Schur-complement calculation; these are the same invariant.

## 3. PF-227 supplies a linear coercive test space, not just isolated witnesses

PF-289 uses one high vector per separated window and observes that PF-227 already supplies a fixed diagonal floor after choosing the stronger endpoint of a high/high crossing pair. For optimization it is better to make the floor linear and basis invariant.

Equations (11)--(13) say that the restricted form operator on the whole finite PF-227 endpoint-witness span has at least one eigenvalue `>=b`. Cutting that finite operator at `b/2` produces `W_n^\sharp`. The spectral cut cannot be empty, and every vector that remains satisfies the same scale-independent Rayleigh lower bound. One may therefore optimize correlation **inside a linear high space without ever leaving the PF-289 admissible class**.

This matters because an unconstrained optimizer over all of `W_n` could in principle concentrate on a very weak diagonal-energy direction. The spectral cut separates the two questions cleanly: PF-227 pays the strength floor; the shorting deficit measures only the angle with the PF-216 low extension.

## 4. The immediate geometric test is now a constrained variational problem

The local question in `CLUE-variable-corridor-reservoir-weyl-mass` can be asked without constructing a preferred PF-227 singular vector. On each actual one-cusp-pant window:

- build the physical-high PF-227 candidate span `W_n` with the real PF-205/PF-212 normalization;
- restrict the actual simultaneous precision form `k` to `W_n` and keep its `>=b/2` spectral subspace `W_n^\sharp`;
- for each adjacent PF-216 low vector compute the fractional energy reduction obtained by allowing only a correction from `W_n^\sharp`.

A fixed positive fractional reduction along infinitely many separated windows is exactly the persistent normalized mixed correlation required by PF-289. The calculation may be attacked variationally at the PDE level: it is enough to compare the raw low energy with the minimum energy after a **physical-high, PF-227-heavy** boundary correction. No individual high mode needs to be tracked through the optimization.

The separable untrimmed corridor of PF-231 is a useful zero calibration. If its relevant low and high energy ranges are exactly orthogonal, the constrained deficit is zero there. Any positive tail deficit for the actual prime-flute module must then be generated by the structures absent from that calibration: hypercycle trimming, physical seam normalization/projection mismatch, finite-pant/cusp completion, or neighboring-cell coupling.

## 5. PF-217 shorting does not answer the new test

[[research/prime_flute/findings/PF-217-tangential-boundary-screening-erases-the-raw-pant-mass-floor-after-shorting|PF-217]] also uses a variational shorting argument, but it shorts the **shifted** form

\[
\mathfrak a[f]=\|f\|^2+k[f]
\]

over the entire orthogonal complement of the one-dimensional tangentially constant module span. Its screening bump is deliberately allowed to use nonconstant low physical frequencies. That result proves that the PF-216 raw onsite mass floor does not survive unrestricted complementary-mode screening.

PF-290 uses a different object for a different gate: the unshifted precision form `k`, shorted only by the **physical-high coercive subspace** `W_n^\sharp` inherited from PF-227. A small PF-217 shorted energy therefore does not imply a positive `\delta_n`, and PF-217 cannot be used as a hidden proof of PF-289 noncompactness. The physical-high restriction is load-bearing.

This distinction also prevents a false positive from enlarging the variational space. Shorting over a larger complement can only lower the minimum energy and increase the apparent deficit. For PF-289 the correction must remain inside a high subspace carrying the fixed diagonal floor used to enter a positive heavy threshold.

## 6. Prior art and novelty audit

The abstract identity behind (6)--(10) is classical. Orthogonal projection gives the Hilbert-space least-squares formula immediately, and its positive-operator formulation belongs to the theory of Schur complements and **shorted operators**. Anderson and Trapp, *Shorted Operators. II*, SIAM Journal on Applied Mathematics 28 (1975), 60--71, DOI `10.1137/0128007`, develops the positive-operator shorting framework. For nonnegative sesquilinear forms, Sebestyen, Tarcsay and Titkos, *A short-type decomposition of forms*, Operators and Matrices 9 (2015), 815--830, DOI `10.7153/oam-09-47`, arXiv `1406.6635`, gives a form-level shorting framework. No novelty is claimed for projection, completion of the square, generalized Schur complements, or shorted forms.

The project-specific delta is the combination of three already established PF facts: PF-227 guarantees a nonempty finite physical-high coercive spectral subspace, PF-216 supplies the repeated heavy low vector, and PF-289 turns any persistent normalized local low/high correlation into noncompactness of a fixed heavy-angle compression. Equations (14)--(16) replace the remaining witness-selection problem by one scalar, basis-invariant local variational deficit that can be estimated directly from the actual pant PDE.

No external theorem is imported into the proof of (3)--(18); the cited literature is prior-art context for the abstract shorting language.

## 7. Boundary conditions and falsification checks

1. **Use `k`, not the shifted form, for the PF-289 correlation.** Replacing `k` by `I+k` changes the angle being tested. PF-217's shifted shorting is therefore not interchangeable with (5).
2. **Keep the physical-high restriction.** Shorting over all complementary boundary data may produce a large deficit entirely through low-frequency screening and does not satisfy PF-289's high-side hypothesis.
3. **Keep the coercive spectral cut.** Optimizing over the whole PF-227 candidate span can select directions with arbitrarily weak diagonal Rayleigh quotient. `W_n^\sharp` is what makes the optimizer automatically admissible for a fixed heavy threshold.
4. **The threshold constant is not sacred.** `b/2` is convenient. Any fixed `0<M<b` gives a nonempty spectral subspace after choosing the local band as above and yields the same implication with constants changed.
5. **A positive limsup is only a sufficient negative test.** It proves noncompactness through PF-289. A vanishing deficit on these PF-227 bands does not prove compactness or weak trace class; other physical-high directions can still overlap the low-heavy range.
6. **Window separation remains necessary.** To invoke PF-289 globally, pass to windows separated beyond PF-214's block-Jacobi interaction range. Local positivity alone does not manufacture orthogonality across adjacent windows.
7. **Do not infer a deficit from raw high/high multiplicity.** PF-227 supplies the coercive high test space, not its angle with `\ell_r`. The mixed Gram vector `c_{n,r}` is still the new geometric data.
8. **A larger shorting space can overstate the relevant correlation.** Variational upper bounds are useful only when the trial correction lies in `W_n^\sharp` (or another physical-high subspace with a verified uniform Rayleigh floor).
9. **The finite Gram formula is exact but does not remove the PDE.** The entries of `G_{n,\sharp}` and `c_{n,r}` must still be controlled for the actual PF-205 normalized simultaneous precision, including finite-pant completion and the physical `P/H` split.

## Consequences for the research line

The immediate PF-289 task can now be stated as one local scalar asymptotic:

\[
\boxed{
\delta_n
=
\max_{r\in\{n,n+1\}}
\left(
1-
\frac{\inf_{h\in W_n^\sharp}k[\ell_r+h]}
{k[\ell_r]}
\right).
}
\tag{24}
\]

A positive tail limsup kills compactness of the current mixed physical-frequency endpoint. Decay `\delta_n\to0` kills only this local PF-227/PF-289 falsifier and sends the line back to PF-287's full fixed-threshold essential-orthogonality problem.

This is a sharper operational target than choosing individual PF-227 witnesses: it is phase-free, basis-free, automatically enforces the high Rayleigh floor, and admits both PDE variational estimates and finite-dimensional Gram calculations. The unresolved mathematics is now exactly whether the actual one-cusp-pant completion permits a fixed fraction of the PF-216 low extension energy to be screened by the **PF-227-heavy physical-high band**.