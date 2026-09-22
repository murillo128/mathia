# VIS-384 — Hilbert-Schmidt source-subspace Laplacian removes generator-coordinate gauge

## Claim

Fix the coefficient-space Hilbert geometry used by the Wang positive-Hilbert construction, and let `H=(H_1,...,H_m)` be any finite family of Hermitian source operators on `C^d`. Remove the commutator-invisible scalar parts by

`\bar H_j = H_j - tr(H_j) I/d`,

and let

`S = span_R{\bar H_1,...,\bar H_m} \subset Herm_0(d)`.

There is a canonical joint-commutator Laplacian attached to the **source subspace** `S`, independent of the chosen generator coordinates. If `E_1,...,E_r` is any Hilbert-Schmidt orthonormal basis of `S`, define

`Delta_S = sum_(a=1)^r ad_(E_a)^* ad_(E_a)`.

Then `Delta_S` is independent of the orthonormal basis. More strongly, if the original centered generators are used as an arbitrary possibly redundant frame and

`K_(jk)=<\bar H_j,\bar H_k>_F`,

then exactly

`Delta_S = sum_(j,k) (K^dagger)_(jk) ad_(\bar H_j)^* ad_(\bar H_k)`,

where `K^dagger` is the Moore-Penrose pseudoinverse.

Consequently `Delta_S` is unchanged by every replacement of the source-generator list that spans the same centered Hilbert-Schmidt subspace `S`: invertible anisotropic reweightings, nonorthogonal coordinate changes, permutations, common scalings, and redundant frame expansions all disappear. Scalar shifts `H_j -> H_j+c_j I` disappear as well.

For a Hermitian Gram tangent `G`, define

`epsilon_S(G)^2=<G,Delta_S G>_F`

and

`A_(G,S)(alpha)=||P_(0,alpha epsilon_S(G)^2]^(Delta_S) G||_F`.

This defect-squared low-mode profile depends on the source subspace and the fixed ambient Hilbert-Schmidt geometry, but **not** on how that same subspace was presented by generators. It therefore removes exactly the source-coordinate gauge exposed in `VIS-383`.

**Evidence/status:** `EXACT-DERIVED + REPRESENTATION-QUOTIENT + CLASSICAL FRAME/PSEUDOINVERSE ALGEBRA + NO-NOVELTY-CLAIM`.

No arithmetic localization, Wang destination gain, zeta-zero statement, or RH consequence is claimed.

## 1. The intrinsic object is the centered source subspace

Commutators cannot see scalar identity components:

`[X,H_j+c_j I]=[X,H_j]`.

So the source family relevant to the commutator geometry lives naturally in the quotient of Hermitian matrices by the scalar identity. Choosing the traceless representative gives the concrete Hilbert space `Herm_0(d)` with the Frobenius/Hilbert-Schmidt inner product already used by the current finite-dimensional Wang geometry.

Let `S` be the span of the centered source operators. If `E_1,...,E_r` and `F_1,...,F_r` are two Hilbert-Schmidt orthonormal bases of `S`, then `F_b=sum_a U_(ba)E_a` for an orthogonal matrix `U`. Linearity of the commutator gives

`ad_(F_b)=sum_a U_(ba) ad_(E_a)`.

Therefore

`sum_b ad_(F_b)^*ad_(F_b)`
` = sum_(a,c) (sum_b U_(ba)U_(bc)) ad_(E_a)^*ad_(E_c)`
` = sum_a ad_(E_a)^*ad_(E_a)`.

Thus `Delta_S` is a property of the subspace `S` inside the fixed coefficient-space Hilbert geometry, not of an orthonormal basis chosen to display it.

## 2. The pseudoinverse formula quotients arbitrary and redundant generator frames

Write the centered generators in an orthonormal basis of `S` as

`\bar H_j = sum_a C_(ja) E_a`,

where the `m x r` matrix `C` has full column rank. Their Gram matrix is

`K = C C^T`.

The Moore-Penrose identity for a full-column-rank synthesis gives

`C^T (C C^T)^dagger C = I_r`.

Now contract the commutator maps with the pseudoinverse Gram:

`sum_(j,k) (K^dagger)_(jk) ad_(\bar H_j)^*ad_(\bar H_k)`
` = sum_(a,b) [C^T K^dagger C]_(ab) ad_(E_a)^*ad_(E_b)`
` = sum_a ad_(E_a)^*ad_(E_a)`
` = Delta_S`.

This proves the frame formula and shows why redundancy is harmless: `K^dagger` does not assign physical significance to duplicate or linearly dependent coordinates; it contracts the frame back to the orthogonal projector onto the actual source subspace.

Equivalently, if `T:R^m -> Herm_0(d)` is the synthesis map `Tc=sum_j c_j \bar H_j`, then `T T^dagger` is the orthogonal projector onto `S`. The formula above is simply the commutator quadratic form contracted against that projector rather than against the arbitrary Euclidean metric of the generator list.

## 3. VIS-383's anisotropic Pauli control is exactly quotiented

`VIS-383` used

`H_1=sigma_z/2`, `H_2=sigma_x/2`

and the anisotropically reweighted presentation

`H^(eta)=(H_1,eta H_2)`.

The uncorrected coordinate Laplacian was

`Delta_eta=ad_(H_1)^2+eta^2 ad_(H_2)^2`,

so decreasing `eta` manufactured an order-one defect-normalized low-mode component while preserving the source span and exact joint commutant.

For every `eta>0`, however, the centered source subspace is the same two-plane

`S=span_R{sigma_z/2,sigma_x/2}`.

The Hilbert-Schmidt subspace Laplacian `Delta_S` is therefore exactly the same for all `eta`. In the frame formula the factor `eta^2` introduced into the second Gram coordinate is cancelled by the corresponding pseudoinverse weight. The false low-mode signal from `VIS-383` cannot be created by source-coordinate anisotropy once the statistic is expressed through `S`.

This is stronger than merely bounding the condition number of a coordinate change: the whole `GL(m)` presentation freedom is removed whenever it leaves the centered source subspace unchanged.

## 4. What remains physical after the quotient

The quotient is not free of geometric assumptions. It uses the fixed Hilbert-Schmidt metric on coefficient matrices. If that ambient metric is itself chosen after inspecting the target signal, or is allowed to vary source-dependently without accounting, the same kind of conditioning resource reappears one level higher. The current result therefore supplies a canonical metric only **relative to the coefficient-space Hilbert structure already admitted by the Wang construction**.

Nor does the quotient identify different source subspaces. If arithmetic data changes `S` itself, then `Delta_S` may change; that is precisely the sort of source-specific geometry the accepted localization clue is trying to detect. The quotient removes presentation leverage while retaining subspace geometry.

There is also a numerical boundary. The exact formula is well defined for a fixed subspace even when the displayed frame is redundant, but explicitly forming `K^dagger` can be ill-conditioned when the generator frame is nearly rank deficient. A numerical implementation should construct an orthonormal basis of the centered source span by a stable QR/SVD-type procedure and freeze the rank/tolerance rule before inspecting the localization statistic. Otherwise a data-dependent numerical rank threshold becomes a new representation resource even though the exact mathematics is coordinate-free.

## 5. Consequence for defect-squared localization

`VIS-382` proves that persistent bounded-spread output orientation requires Gram-tangent mass at the `O(epsilon^2)` scale of the joint commutator spectrum. `VIS-383` then shows that the naive coordinate Laplacian can move that mass merely by anisotropically reweighting source generators.

The present finding removes that obstruction. The accepted Wang localization clue can use

`Delta_S`, `epsilon_S(G)^2=<G,Delta_S G>_F`,

and

`A_(G,S)(alpha)=||P_(0,alpha epsilon_S(G)^2]^(Delta_S)G||_F`

as its default intrinsic statistic once the coefficient-space Hilbert metric and numerical rank rule are fixed independently of the observed signal.

Matched controls should therefore be compared after the same centering, source-span construction, ambient Hilbert metric, and rank rule. Excess low-mode mass that survives this quotient cannot be blamed on anisotropic reparameterization or redundant generator coordinates. It may still be explained by generic source-subspace geometry, approximate reducibility, block structure, or another source-free mechanism; those remain the decisive controls.

## Prior-art and novelty audit

The mathematical mechanism is classical finite-dimensional linear algebra. R. Penrose, **A generalized inverse for matrices**, *Proceedings of the Cambridge Philosophical Society* 51:3 (1955), 406--413, DOI `10.1017/S0305004100030401`, introduced the Moore-Penrose generalized inverse and its associated projector machinery. The identities used here are standard consequences of orthogonal projection/frame algebra; no new pseudoinverse, frame, Casimir, or operator-subspace theorem is claimed.

The Mathia-specific content is the control consequence for the current Wang defect-squared localization channel: `VIS-383` identified the generator-index metric as a false-positive resource, and the Hilbert-Schmidt source-subspace contraction shows exactly how to quotient that entire presentation freedom while preserving the source subspace that could still carry arithmetic information.

A local repository audit found no existing Visual Exploration finding that applies this source-subspace projector contraction to the `VIS-382` defect-squared statistic. `VIS-383` stops at fixing or pricing a generator-index metric; the present result supplies a canonical coordinate-free choice relative to the already fixed coefficient-space Hilbert geometry.

## Dependencies

- `VIS-382`: defect-squared low positive commutator modes are necessary for persistent bounded output orientation.
- `VIS-383`: arbitrary anisotropic source-coordinate metrics can manufacture the target normalized low-mode mass.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue whose source-specificity test needs a representation-stable commutator Laplacian.

## Research consequence

Future work on the accepted Wang localization clue should quotient generator coordinates before looking for source-specific low-mode excess. Use the centered source subspace `S` and its Hilbert-Schmidt orthonormal commutator Laplacian, or an exactly equivalent frame/pseudoinverse implementation, with coefficient-space metric and numerical rank rule frozen independently of the signal.

This closes the generator-coordinate gauge exposed by `VIS-383`; it does **not** establish the desired source-specific localization. The next substantive question is whether the resulting intrinsic `Delta_S` exhibits defect-squared Gram overlap that differs from matched non-arithmetic subspaces for reasons that can be identified mathematically and then propagated to the Wang destination after all remaining costs are charged.