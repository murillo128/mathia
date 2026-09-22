# VIS-380 — bounded orbit amplification requires joint-commutator gap collapse

## Claim

Let `H=(H_1,...,H_r)` be a finite tuple of Hermitian coefficient-space operators and let

`C=R(H)=C^*`

be a Hermitian output of a noncommutative rational function defined at `H`. The positive-metric case of interest is `mI<=C<=MI`.

On the coefficient matrix space with Frobenius inner product define

`delta_H(X)=([X,H_1],...,[X,H_r])`

and the positive **joint commutator Laplacian**

`Delta_H=delta_H^* delta_H=sum_j ad_(H_j)^2`,

where `ad_A(X)=[X,A]`. Since each `H_j` is Hermitian, `ad_(H_j)` is self-adjoint for the Frobenius inner product. Hence

`<X,Delta_H X>=sum_j ||[X,H_j]||_F^2`.

Its kernel is exactly the joint commutant

`K_H={X:[X,H_j]=0 for all j}`.

Because every element of `K_H` commutes with every rational expression in the `H_j`, it also commutes with `C`. Thus `K_H subset ker(ad_C)`.

Assume `delta_H` is not identically zero and define the **joint commutator gap**

`mu_H=lambda_min(Delta_H|_(K_H^perp))>0`.

Then the similarity-orbit structured condition number from `VIS-379` has the exact generalized-Rayleigh representation

`Lambda_orb(C;H)^2`
` = sup_(X notin K_H) ||[X,C]||_F^2 / sum_j ||[X,H_j]||_F^2`
` = lambda_max(Delta_H^(dagger/2) ad_C^2 Delta_H^(dagger/2))`,

where the last operator is restricted to `K_H^perp` and `dagger` denotes the Moore--Penrose inverse.

If

`omega(C)=lambda_max(C)-lambda_min(C)`

is the spectral diameter of the Hermitian output, then

`||ad_C||_(F->F)=omega(C)`

and therefore

`Lambda_orb(C;H) <= omega(C)/sqrt(mu_H)`.

In particular, for a bounded positive metric `mI<=C<=MI`,

`Lambda_orb(C;H) <= (M-m)/sqrt(mu_H)`.

For the actual Wang Gram `G`, with

`epsilon_G(H)^2=sum_j ||[G,H_j]||_F^2`

and `kappa_G` as in `VIS-379`, one has

`kappa_G(C;H)^2`
` = ||[G,C]||_F^2 / epsilon_G(H)^2`
` <= Lambda_orb(C;H)^2`
` <= omega(C)^2/mu_H`.

Consequently, for any family `H_T,C_T,G_T` with uniformly bounded metric spread `omega(C_T)<=Omega`, if

`epsilon_T=epsilon_(G_T)(H_T)->0`

but

`||[G_T,C_T]||_F >= c>0`,

then necessarily

`mu_(H_T) <= (Omega^2/c^2) epsilon_T^2 ->0`.

Thus a bounded positive rational metric cannot turn vanishing external-generator orientation into order-one Gram orientation while the external tuple retains a uniform joint-commutator gap. **Divergent structured amplification requires the external operator tuple itself to develop an approximate new commutant direction (or the output metric spread to become unbounded).**

This requirement is sharp already in dimension two. Let

`H_delta=diag(0,delta)`,

`C_delta=I+delta^(-1) H_delta=diag(1,2)`,

and

`G=[[0,1],[1,0]]`.

Then `mu_(H_delta)=delta^2`, `omega(C_delta)=1`,

`epsilon_G(H_delta)=sqrt(2) delta`,

`||[G,C_delta]||_F=sqrt(2)`,

and therefore

`kappa_G=Lambda_orb=1/delta=omega(C_delta)/sqrt(mu_(H_delta))`.

The bound is attained exactly. The metric stays uniformly positive and uniformly conditioned; the entire amplification is paid by collapse of the external tuple's commutator gap together with the `delta^(-1)` parameter scaling in the constructor.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL STRUCTURED-CONDITION/SPECTRAL-GAP GEOMETRY + STRUCTURAL NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

No stronger estimate for the Chebyshev-theta remainder, the prime-number-theorem remainder, zeta zeros, or RH is claimed.

## 1. The orbit condition number is a quotient Rayleigh problem

`VIS-379` defined the simultaneous-similarity tangent map

`T_H(X)=delta_H(X)`

and showed that rational similarity covariance induces the well-defined orbit derivative

`D_R^orb(delta_H(X))=[X,C]`.

The ambiguity `X -> X+Z` with `Z in K_H` is harmless because `Z` also commutes with `C`. Therefore the orbit derivative is naturally a map on the quotient by the joint commutant.

For Hermitian generators,

`delta_H^* delta_H=Delta_H`

and, for Hermitian `C`,

`ad_C^* ad_C=ad_C^2`.

Hence for every `X`,

`||delta_H(X)||_(2,F)^2=<X,Delta_H X>`,

`||[X,C]||_F^2=<X,ad_C^2 X>`.

Both quadratic forms vanish on `K_H`; subtracting the orthogonal projection of `X` onto `K_H` changes neither numerator nor denominator. The squared orbit condition number is therefore the largest generalized Rayleigh quotient of the pair

`(ad_C^2,Delta_H)`

on `K_H^perp`.

Since `Delta_H` is positive definite on that finite-dimensional subspace, the standard change of variables `Y=Delta_H^(1/2)X` gives

`Lambda_orb^2`
` = lambda_max(Delta_H^(-1/2) ad_C^2 Delta_H^(-1/2))`

there. Writing the same formula on the full matrix space with the Moore--Penrose inverse gives the stated intrinsic expression.

This is useful because `VIS-379` separated unstructured derivative sensitivity from similarity-orbit sensitivity, but it did not yet identify which geometry of the external tuple permits the orbit sensitivity itself to become large. The generalized denominator shows that the missing quantity is exactly the coercivity of the joint commutator form away from the true commutant.

## 2. The Hermitian output contributes only its spectral diameter

Diagonalize

`C=U diag(c_1,...,c_n) U^*`.

In the induced matrix-unit basis, `ad_C` has eigenvalues `c_b-c_a`. Therefore its Frobenius-operator norm is exactly

`||ad_C||_(F->F)=max_(a,b)|c_a-c_b|=omega(C)`.

On the other hand, by definition of `mu_H`, every `X in K_H^perp` satisfies the Poincare-type inequality

`sum_j ||[X,H_j]||_F^2`
` = <X,Delta_H X>`
` >= mu_H ||X||_F^2`.

Combining the two estimates gives

`||[X,C]||_F`
` <= omega(C)||X||_F`
` <= omega(C) mu_H^(-1/2) ||delta_H(X)||_(2,F)`.

Taking the supremum proves

`Lambda_orb(C;H)<=omega(C)/sqrt(mu_H)`.

For `mI<=C<=MI`, the spectral diameter is at most `M-m`, not merely `2M`. Thus a bounded, nearly scalar metric has even less available orientation leverage.

## 3. Gap collapse means an approximate new symmetry

The number `mu_H` is positive at every fixed finite-dimensional instance after quotienting the exact joint commutant. What matters for a family is whether it stays uniformly positive.

By the variational characterization,

`mu_H`
` = inf_{X perp K_H, ||X||_F=1} sum_j ||[X,H_j]||_F^2`.

Therefore `mu_(H_T)->0` exactly means that there are normalized matrix directions `X_T`, orthogonal to the exact joint commutant at each instance, that asymptotically commute with every external generator:

`sum_j ||[X_T,H_(T,j)]||_F^2 ->0`.

So the escape condition exposed here is not merely a large scalar condition number. The external operator family must approach an enlarged symmetry/commutant, or an equivalent near-degeneracy of its simultaneous-similarity orbit.

This is the coefficient-space analogue of a spectral-gap collapse: the commutator Dirichlet form loses coercivity transverse to its exact zero modes. Whether that near-symmetry is physically meaningful, source-dependent, or merely engineered must still be decided from the construction.

## 4. Quantitative consequence for the actual Gram tangent

`VIS-379` already gave the exact identity

`||[G,C]||_F=kappa_G epsilon_G(H)`

and the hierarchy

`kappa_G<=Lambda_orb<=L_R`.

The present gap estimate inserts a new middle-scale accounting:

`kappa_G`
` <= Lambda_orb`
` <= omega(C)/sqrt(mu_H)`.

Suppose the external tuple almost commutes with the actual Wang Gram, so `epsilon_G(H)` is small. If a candidate nevertheless claims a fixed nonzero output orientation `||[G,C]||_F`, then

`kappa_G >= ||[G,C]||_F/epsilon_G(H)`

must be large. With bounded `omega(C)`, the inequality above forces `mu_H` to be correspondingly small.

Thus a claimed rational-orientation gain has two nested obligations:

1. show that the **actual Gram direction** is amplified, as required by `VIS-379`, rather than merely exhibiting a large unstructured derivative; and
2. explain the **joint-commutator gap collapse** that makes such amplification possible under a bounded metric.

A near-pole or large rational coefficient is not enough by itself. It must be aligned with the approximate-commutant direction that the external tuple develops and with the actual Gram tangent that the Wang construction supplies.

## 5. The two-dimensional model saturates every scale

Take

`H_delta=diag(0,delta)`

with `delta>0`. The joint commutant is the diagonal matrix algebra. On an off-diagonal matrix unit, `ad_(H_delta)` has magnitude `delta`, so

`mu_(H_delta)=delta^2`.

Now set

`C_delta=I+H_delta/delta=diag(1,2)`.

The metric bounds are fixed:

`I<=C_delta<=2I`,

while `omega(C_delta)=1`.

Choose the Hermitian Gram direction

`G=[[0,1],[1,0]]`.

Direct calculation gives

`[G,H_delta]=[[0,delta],[-delta,0]]`,

hence

`epsilon_G=sqrt(2) delta`,

whereas

`[G,C_delta]=[[0,1],[-1,0]]`

has Frobenius norm `sqrt(2)`. Therefore

`kappa_G=1/delta`.

Because the quotient matrix space has only the off-diagonal commutator sector in this example,

`Lambda_orb=1/delta` as well.

Finally,

`omega(C_delta)/sqrt(mu_(H_delta))=1/delta`,

so the upper bound is exact.

This control is important for interpretation. Bounded positive output and bounded metric condition number do **not** by themselves prevent arbitrarily large orbit amplification. What pays for the amplification here is the collapsing separation of the external generator together with the parameter-dependent rescaling that maps that collapsing direction to an order-one metric difference. The new diagnostic therefore cannot be replaced by the metric bounds `m,M` already used in `VIS-374`.

## 6. Prior-art audit

The general structured-conditioning framework is classical. Bahar Arslan, Vanni Noferini, and Francoise Tisseur, **The Structured Condition Number of a Differentiable Map between Matrix Manifolds, with Applications**, *SIAM Journal on Matrix Analysis and Applications* 40:2 (2019), 774--799, DOI `10.1137/17M1148943`, treats condition numbers obtained by restricting differentials to tangent spaces of matrix manifolds and gives computational formulations. `VIS-379` already used this literature as the prior-art boundary for replacing an unstructured Frechet derivative norm by a similarity-orbit restricted one.

The rational functional-calculus input remains classical as well. D. S. Kaliuzhnyi-Verbovetskyi and V. Vinnikov, **Noncommutative rational functions, their difference-differential calculus and realizations**, *Multidimensional Systems and Signal Processing* 23 (2012), 49--77, DOI `10.1007/s11045-010-0122-3`, develops the noncommutative rational-function and difference-differential framework used in `VIS-378`--`VIS-379`.

Spectral gaps controlling approximate commutants are also standard operator-algebra/quantum-expander language. M. B. Hastings, **Random unitaries give quantum expanders**, *Physical Review A* 76 (2007), 032315, DOI `10.1103/PhysRevA.76.032315`, is a representative finite-matrix spectral-gap reference. The exact Hermitian commutator Laplacian `sum_j ad_(H_j)^2` used here is an elementary finite-dimensional Dirichlet form; no new general spectral-gap or quantum-expander theorem is claimed.

The Mathia-specific contribution is the accounting consequence obtained by composing these classical facts with the Wang orientation hierarchy: after `VIS-379` restricts sensitivity to the Gram-accessible similarity tangent, **uniformly bounded positive rational output plus a uniform joint-commutator gap forbids divergent orientation amplification**. A surviving bounded positive rational escape must therefore expose and price an approximate-commutant degeneration of the external tuple, not merely a large rational derivative somewhere in tuple space.

## Dependencies

- `VIS-374`: bounded positive metric orientation is already priced by resolved Gram gaps, near-degenerate Gram-cluster width, and metric bounds.
- `VIS-378`: the represented rational function has an intrinsic full Frechet derivative and similarity covariance.
- `VIS-379`: rational orientation sensitivity restricts first to the simultaneous-similarity orbit and then to the actual Gram-generated tangent.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue further narrowed by the joint-commutator-gap requirement here.

## Research consequence

For a finite-dimensional bounded positive rational Wang candidate `C=R(H)`, report the external tuple's joint commutator gap

`mu_H=lambda_min^+(sum_j ad_(H_j)^2)`

alongside the actual Gram tangent `epsilon_G(H)`, the directional amplification `kappa_G`, the output metric spread `omega(C)`, and the destination-side Gram-cluster quantities already required by `VIS-374`.

If `mu_H` stays bounded below and `omega(C)` stays bounded, the rational-orbit condition number is uniformly bounded and vanishing generator orientation cannot become order-one output orientation. If `mu_H` collapses, identify the approximate commutant direction that causes the collapse and show that it is an independently justified external/arithmetic resource rather than a freely engineered near-symmetry.

The next bounded-positive rational escape is therefore not just “find a sensitive rational function.” It must couple three structures at once: a collapsing external-tuple commutator gap, sensitivity aligned with that collapsing orbit direction, and the actual Wang Gram tangent, while still paying the metric and destination costs from `VIS-374` and the source-information costs of the accepted clue.