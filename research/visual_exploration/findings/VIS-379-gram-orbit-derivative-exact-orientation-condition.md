# VIS-379 — the Gram-orbit derivative is the exact rational orientation condition number

## Claim

Let `G=G^*` be the source-free Wang Gram on a finite-dimensional coefficient space, let

`H=(H_1,...,H_r)`

be an `r`-tuple of external coefficient-space operators, and let `R` be a noncommutative rational function defined at `H`. As in `VIS-378`, regard `R` as the represented rational function rather than one chosen expression tree.

For any coefficient-space matrix `X`, define the simultaneous-similarity tangent

`T_H(X)=([X,H_1],...,[X,H_r])`

and the output tangent

`T_R(X)=[X,R(H)]`.

Similarity covariance gives the exact identity

`T_R(X)=D R_H(T_H(X))`.

If `T_H(X)=0`, then `X` commutes with every `H_j`, hence with every rational expression in the `H_j` and therefore with `R(H)`. Consequently `T_R(X)=0`, and the rule

`D_R^orb(T_H(X))=T_R(X)`

defines a linear map on the tangent space `range(T_H)` independently of the choice of `X`.

Equip tuples with

`||(K_1,...,K_r)||_(2,F)=(sum_j ||K_j||_F^2)^(1/2)`

and define the **similarity-orbit structured condition number**

`Lambda_orb(R;H)=||D_R^orb||_( (2,F) -> F )`.

Let `L_R(H)=||D R_H||_((2,F)->F)` be the full Fréchet-derivative norm from `VIS-378`. Then

`Lambda_orb(R;H) <= L_R(H)`.

For the actual Wang Gram, put

`epsilon_G(H)=||T_H(G)||_(2,F)`.

When `epsilon_G(H)>0`, define the **Gram-direction condition number**

`kappa_G(R;H)=||[G,R(H)]||_F / epsilon_G(H)`.

Then exactly

`||[G,R(H)]||_F = kappa_G(R;H) epsilon_G(H)`

and

`kappa_G(R;H) <= Lambda_orb(R;H) <= L_R(H)`.

When `epsilon_G(H)=0`, similarity covariance already forces `[G,R(H)]=0`; set `kappa_G=0` by convention.

Thus `VIS-378` can be sharpened twice. The full derivative norm is an unstructured sensitivity budget. Restricting it to the simultaneous-similarity orbit removes perturbation directions that cannot change coefficient orientation at all. Restricting further to the **actual Gram-generated tangent** removes orbit directions that exist mathematically but are not supplied by the Wang Gram under audit.

For a family indexed by `T`, if

`epsilon_T=epsilon_(G_T)(H_T) -> 0`

and `kappa_(G_T)(R_T;H_T)` stays bounded, then

`||[G_T,R_T(H_T)]||_F -> 0`

regardless of whether the full derivative norms `L_(R_T)(H_T)` diverge. Conversely, order-one output orientation with `epsilon_T->0` forces the **actual** directional condition numbers `kappa_(G_T)` to diverge. Divergence of the full derivative norm is necessary but is not, by itself, evidence that the available Gram orientation is being amplified.

If `C=R(H)` is a positive Hermitian metric with `mI<=C<=MI`, the clustered Wang control of `VIS-374` becomes

`|s_k(A_W C^(1/2))^2-s_k(A_W C_*^(1/2))^2|`
` <= ||G||_op sqrt(M/m) kappa_G(R;H) epsilon_G(H)/gamma + 2M eta`.

The rational-calculus accounting can therefore be stated in the direction actually supplied by the Wang Gram, without charging unrelated sensitivities of the rational map.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL STRUCTURED CONDITIONING/FREE DIFFERENTIAL CALCULUS + STRUCTURAL NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

No stronger estimate for the Chebyshev-theta remainder, the prime-number-theorem remainder, zeta zeros, or RH is claimed.

## 1. The similarity orbit is the relevant structured perturbation space

`VIS-378` used similarity covariance

`R(SH_1S^(-1),...,SH_rS^(-1))=S R(H) S^(-1)`

and differentiated `S(t)=exp(tG)` to obtain

`D R_H([G,H_1],...,[G,H_r])=[G,R(H)]`.

The same argument works with an arbitrary generator `X` in place of `G`:

`D R_H(T_H(X))=T_R(X)`.

The input directions relevant to orientation are therefore not the whole tuple space. They are the tangent directions produced by simultaneous similarity. A perturbation that changes eigenvalues, scalar offsets, or other data without lying in `range(T_H)` may make the rational function highly sensitive while contributing nothing to the orientation mechanism measured by commutators.

The quotient is well defined. If two generators `X,Y` produce the same tangent tuple, then `Z=X-Y` commutes with every `H_j`. Since products, sums, and inverses of matrices commuting with `Z` still commute with `Z`, every rational representative of `R(H)` commutes with `Z` wherever it is defined. Hence

`[X,R(H)]=[Y,R(H)]`.

So `D_R^orb` is an intrinsic derivative on the similarity-orbit tangent space rather than a choice of generator coordinates.

Because this tangent space is a linear subspace of the full perturbation space and `D_R^orb` is the restriction of the Fréchet derivative to it,

`Lambda_orb(R;H)<=L_R(H)`

immediately.

## 2. The Wang Gram supplies only one tangent direction

The Wang audit does not have access to every simultaneous-similarity tangent. Its orientation source is the particular Hermitian matrix `G=A_W^*A_W`. Therefore the exact input tangent is

`K_G=T_H(G)=([G,H_1],...,[G,H_r])`.

If `K_G!=0`, linearity gives

`kappa_G(R;H)`
` = ||D_R^orb(K_G)||_F/||K_G||_(2,F)`
` = ||[G,R(H)]||_F/epsilon_G(H)`.

This is not merely an upper bound. It is the exact amplification factor for the orientation direction actually present in the current Wang construction.

The hierarchy

`kappa_G <= Lambda_orb <= L_R`

has a useful interpretation. `L_R` asks for the worst local sensitivity to arbitrary tuple perturbations. `Lambda_orb` asks for the worst local sensitivity among orientation-changing simultaneous similarities. `kappa_G` asks how much the one available Gram tangent is amplified. Only the last quantity directly certifies amplification of the resource supplied by the current construction.

A large value of either broader condition number remains useful as a warning or sufficient budget, but it can overcharge directions that the Wang mechanism never excites.

## 3. A genuine divergent derivative can be completely irrelevant to orientation

The distinction is not only about removable rational poles. Consider two Hermitian inputs

`H_1=delta I`,

`H_2=Y`,

where `delta>0` and `Y` is any fixed non-scalar Hermitian matrix. Let

`R(H_1,H_2)=H_1^(-1)+H_2`.

This is a genuine rational function whose sensitivity to the first input diverges as `delta->0`. Its derivative is

`D R_H(K_1,K_2)=-H_1^(-1) K_1 H_1^(-1)+K_2`,

so, for the tuple Frobenius norm,

`L_R(H) >= delta^(-2)`.

The divergence is real; it is not removed by rational simplification.

But `H_1` is scalar. For every similarity generator `X`,

`T_H(X)=(0,[X,Y])`.

On this entire orbit tangent space,

`D_R^orb(0,[X,Y])=[X,Y]`.

Therefore

`Lambda_orb(R;H)=1`

whenever the orbit is nontrivial. Moreover

`R(H)=delta^(-1) I+Y`,

so for every Gram `G`

`[G,R(H)]=[G,Y]`.

If `[G,Y]!=0`, then

`kappa_G(R;H)=1`

exactly, even while the full derivative norm tends to infinity like at least `delta^(-2)`.

This is the decisive negative control for interpreting `VIS-378`. A rational map can be arbitrarily ill-conditioned in a function-level direction that is completely invisible to simultaneous-similarity orientation. Full derivative blow-up is therefore not enough to identify the mechanism required by the Wang branch.

The scalar term `delta^(-1)I` may still make the positive metric norm large. That separate scale is already charged by the `m,M` factors in `VIS-374`. The present point is narrower: its huge derivative does not amplify Gram orientation at all.

## 4. The destination bound becomes directionally exact on the rational side

Suppose the rational output

`C=R(H)`

is positive with

`mI<=C<=MI`.

Choose the Gram clustering of `VIS-374`, with within-cluster width `eta` and resolved inter-cluster gap `gamma`. That finding gives an exactly Gram-commuting positive control `C_*` satisfying

`|s_k(A_W C^(1/2))^2-s_k(A_W C_*^(1/2))^2|`
` <= ||G||_op sqrt(M/m) ||[G,C]||_F/gamma + 2M eta`.

Now substitute the exact identity

`||[G,C]||_F=kappa_G(R;H) epsilon_G(H)`.

The result is

`|s_k(A_W C^(1/2))^2-s_k(A_W C_*^(1/2))^2|`
` <= ||G||_op sqrt(M/m) kappa_G(R;H) epsilon_G(H)/gamma + 2M eta`.

One may replace `kappa_G` by `Lambda_orb` or by `L_R` to obtain progressively coarser sufficient bounds, but only `kappa_G` measures the local rational amplification actually used by this Gram.

This separates four resources cleanly: inherited generator orientation `epsilon_G`, directional rational amplification `kappa_G`, Gram spectral resolution `gamma,eta`, and positive-metric scale/conditioning `m,M`. A large condition number in an orthogonal perturbation direction receives no orientation credit.

## 5. Family-level closure and the sharper escape criterion

Let `G_T,H_T,R_T` be a parameter family and set

`epsilon_T=epsilon_(G_T)(H_T)`.

The exact identity gives

`||[G_T,R_T(H_T)]||_F=kappa_T epsilon_T`.

Hence if `epsilon_T->0` and `kappa_T=O(1)`, rational processing cannot create order-one Gram orientation. If the output commutator stays bounded below by a positive constant, then necessarily

`kappa_T -> infinity`

along a subsequence.

This implies `Lambda_orb,T->infinity` and `L_T->infinity`, but the converses fail. The example above already shows that `L_T` may diverge while both structured orientation condition numbers remain exactly one.

Accordingly, the surviving finite-dimensional rational escape after `VIS-378` is narrower than “find a rational family with a large derivative norm.” The candidate must show that the derivative is large **on the Gram-generated similarity tangent actually supplied by the external generators**. A near-pole, growing realization, changing dimension, or singular limit matters only when its sensitive directions overlap that tangent strongly enough to survive the destination costs.

## 6. Prior-art audit

The underlying conditioning language is classical and no novelty is claimed for it.

D. S. Kaliuzhnyi-Verbovetskyi and V. Vinnikov, **Noncommutative rational functions, their difference-differential calculus and realizations**, *Multidimensional Systems and Signal Processing* 23 (2012), 49--77, DOI `10.1007/s11045-010-0122-3`, develops the difference-differential/directional calculus for noncommutative rational functions used in `VIS-378` and here.

N. J. Higham, *Functions of Matrices: Theory and Computation*, SIAM (2008), DOI `10.1137/1.9780898717778`, treats matrix-function conditioning through Fréchet derivatives. N. J. Higham and S. D. Relton, **Estimating the Condition Number of the Fréchet Derivative of a Matrix Function**, *SIAM Journal on Scientific Computing* 36(6) (2014), C617--C634, DOI `10.1137/130950082`, further develops derivative-based condition-number estimation.

B. Arslan, V. Noferini, and F. Tisseur, **The Structured Condition Number of a Differentiable Map between Matrix Manifolds, with Applications**, *SIAM Journal on Matrix Analysis and Applications* 40(2) (2019), 774--799, DOI `10.1137/17M1148943`, explicitly studies structured condition numbers by restricting differentials/Fréchet derivatives to tangent spaces of matrix manifolds. This makes the general move from `L_R` to a tangent-space-restricted derivative standard conditioning methodology rather than a new theorem.

The Mathia-specific contribution is only the specialization of that classical structured-conditioning viewpoint to the **simultaneous-similarity orbit generated by Wang coefficient orientation**, followed by the further restriction to the actual Gram tangent and its composition with the `VIS-374` destination bound. The explicit hierarchy `kappa_G<=Lambda_orb<=L_R` is used here as an accounting boundary, not claimed as a new general result in numerical analysis or free function theory.

A repository audit found `VIS-375`--`VIS-378` for scalar, polynomial, rational-expression, and intrinsic full-derivative orientation budgets, but no current Visual Exploration finding that quotients the full derivative by the similarity-orbit tangent and then by the actual Gram direction.

## Dependencies

- `VIS-373`: resolved-gap orientation is controlled by gap-normalized Gram commutator size.
- `VIS-374`: bounded orientation inside narrow near-degenerate Gram clusters is spectrally cheap.
- `VIS-375`: scalar spectral reweighting inherits the Gram noncommutativity of its external generator.
- `VIS-376`: finite noncommutative polynomial assembly inherits generator-level Gram noncommutativity.
- `VIS-377`: a chosen finite rational expression has an expression-dependent inverse-conditioning commutator budget.
- `VIS-378`: similarity covariance replaces expression-level conditioning by the intrinsic full Fréchet derivative of the represented rational function.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue further narrowed by the structured-direction audit here.

## Research consequence

Future finite-dimensional Wang rational candidates should report conditioning in the same geometry as the claimed mechanism. The full derivative norm `L_R` is a safe but potentially severe overestimate. First restrict to the simultaneous-similarity tangent of the evaluated external tuple; then evaluate the derivative on the actual Gram-generated tangent.

A candidate receives orientation credit only for

`kappa_G(R;H) epsilon_G(H)=||[G,R(H)]||_F`.

If a claimed near-pole or singular limit makes `L_R` large but leaves `kappa_G` bounded, the instability is irrelevant to Gram orientation and cannot explain a new Wang destination scale. The next rational escape must therefore align its singular sensitivity with the Gram-accessible tangent while also paying the metric, Gram-gap, cluster-width, topology, and source-information costs already exposed by `VIS-369`--`VIS-378`.
