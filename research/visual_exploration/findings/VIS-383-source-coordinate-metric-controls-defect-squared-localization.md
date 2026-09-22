# VIS-383 — defect-squared commutator localization is invariant only after fixing the source-coordinate metric

## Claim

Let

`H=(H_1,...,H_m)`

be a finite tuple of Hermitian source-coordinate operators on a finite-dimensional coefficient space, and define

`delta_H(X)=([X,H_1],...,[X,H_m])`,

`Delta_H=delta_H^* delta_H=sum_j ad_(H_j)^* ad_(H_j)`.

For a Hermitian Gram tangent `G`, write

`epsilon_H(G)^2=<G,Delta_H G>_F`

and, for fixed `alpha>0`, define the defect-normalized low-mode profile used by the accepted Wang localization clue,

`A_(G,H)(alpha)=||P_(0,alpha epsilon_H(G)^2]^(Delta_H) G||_F`.

Now change source coordinates by a real matrix `A=(a_(kj))`, setting

`H'_k=sum_j a_(kj) H_j`.

Then exactly

`delta_(H')=(A tensor I) delta_H`

and therefore

`Delta_(H')=delta_H^*(A^T A tensor I)delta_H`.

So the commutator Laplacian is not determined by the operator span alone: it also contains the Euclidean metric chosen on the source-coordinate index.

There is, however, an exact gauge class. If `A=sU` with `s>0` and `U` orthogonal, then

`Delta_(H')=s^2 Delta_H`,

`epsilon_(H')(G)^2=s^2 epsilon_H(G)^2`,

and hence for every `alpha>0`

`P_(0,alpha epsilon_(H')(G)^2]^(Delta_(H')) = P_(0,alpha epsilon_H(G)^2]^(Delta_H)`.

Consequently

`A_(G,H')(alpha)=A_(G,H)(alpha)`.

Thus common scaling, permutation, sign change, and orthogonal mixing of source coordinates are harmless for the defect-squared localization test.

By contrast, a general invertible anisotropic reweighting preserves the source-operator span and the exact joint commutant but can manufacture or remove order-one defect-normalized low-mode mass. If `sigma_min(A)=a>0` and `sigma_max(A)=b`, then the quadratic forms satisfy

`a^2 Delta_H <= Delta_(H') <= b^2 Delta_H`,

and

`a^2 epsilon_H(G)^2 <= epsilon_(H')(G)^2 <= b^2 epsilon_H(G)^2`,

but the spectral projectors in `A_(G,H)(alpha)` need not agree. The distortion is therefore a genuine conditioning resource, not a coordinate-free signal.

An explicit qubit control shows the effect. Let `sigma_x,sigma_y,sigma_z` be the Pauli matrices and put

`H_1=sigma_z/2`, `H_2=sigma_x/2`,

`E_x=sigma_x/sqrt(2)`, `E_y=sigma_y/sqrt(2)`, `E_z=sigma_z/sqrt(2)`.

For `0<eta<=1`, anisotropically reweight only the second source coordinate,

`H^(eta)=(H_1, eta H_2)`.

On the traceless Hermitian subspace,

`Delta_eta E_x=E_x`,

`Delta_eta E_z=eta^2 E_z`,

`Delta_eta E_y=(1+eta^2)E_y`.

Choose

`G=(E_x+E_z)/sqrt(2)`.

Then `||G||_F=1` and

`epsilon_eta^2=(1+eta^2)/2`.

At the pre-fixed threshold parameter `alpha=1/2`, the defect-normalized spectral cutoff is

`alpha epsilon_eta^2=(1+eta^2)/4`.

For `eta=1`, neither `E_x` nor `E_z` lies below the cutoff, so

`A_(G,H^(1))(1/2)=0`.

For every `eta<=1/sqrt(3)`, the `E_z` eigenvalue satisfies

`eta^2 <= (1+eta^2)/4`,

while the `E_x` eigenvalue remains above the cutoff. Hence

`A_(G,H^(eta))(1/2)=1/sqrt(2)`.

The same two-dimensional source span and the same exact joint commutant can therefore move from zero to order-one defect-squared low-mode mass solely by changing the relative metric on source coordinates.

**Evidence/status:** `EXACT-DERIVED + REPRESENTATION-INVARIANCE/NEGATIVE CONTROL + CLASSICAL QUADRATIC-FORM GEOMETRY + NO-NOVELTY-CLAIM`.

No arithmetic localization, Wang destination improvement, zeta-zero statement, or RH consequence is claimed.

## 1. Source-coordinate changes act through one positive index metric

For every matrix `X`,

`delta_(H')(X)_k`
` = [X,sum_j a_(kj)H_j]`
` = sum_j a_(kj)[X,H_j]`.

Writing the tuple space as the source-index Euclidean space tensored with coefficient matrices gives

`delta_(H')=(A tensor I)delta_H`.

Taking adjoints yields

`Delta_(H')`
` = delta_H^*(A^T A tensor I)delta_H`.

Only the positive matrix

`M=A^T A`

matters to the quadratic commutator energy. Left multiplication of `A` by an orthogonal matrix changes the displayed coordinates but not `M`; anisotropic singular values change the metric used to aggregate the individual commutators.

If `A` is invertible, then

`delta_(H')(X)=0 iff delta_H(X)=0`,

so the exact joint commutant is unchanged. The difference between `Delta_H` and `Delta_(H')` is therefore not a difference in which matrices commute exactly with the source span. It is a difference in how strongly the noncommuting directions are weighted.

This distinction is exactly what the defect-squared localization test must control: its positive spectral bands depend on that weighting even when the underlying source algebra does not.

## 2. Conformal source-coordinate changes cancel from the normalized profile

If `A=sU` with `U^T U=I`, then `A^T A=s^2 I` and hence

`Delta_(H')=s^2 Delta_H`.

The kernel is unchanged and every positive eigenvalue is multiplied by `s^2`, while every spectral eigenspace is identical. At the same time

`epsilon_(H')(G)^2`
` = <G,s^2 Delta_H G>_F`
` = s^2 epsilon_H(G)^2`.

Therefore the spectral inequality

`0 < s^2 lambda <= alpha s^2 epsilon_H(G)^2`

is equivalent to

`0 < lambda <= alpha epsilon_H(G)^2`.

The entire defect-normalized projector, not merely its dimension or smallest eigenvalue, is unchanged. This establishes the natural representation invariance of the accepted clue under orthogonal mixing and common scaling of the source coordinates.

The result also identifies what should count as a harmless coordinate perturbation in future visual or numerical diagnostics: rotations, reflections, permutations and one common scale do not alter `A_(G,H)(alpha)`.

## 3. General invertible changes preserve the commutant but not the localization geometry

Let the singular values of an invertible `A` lie in `[a,b]`. Then

`a^2 I <= A^T A <= b^2 I`.

Applying `delta_H^*(. )delta_H` preserves Loewner order, giving

`a^2 Delta_H <= Delta_(H') <= b^2 Delta_H`.

Evaluating the same forms on `G` gives the corresponding defect-energy comparison.

These inequalities control total commutator energy but do not identify spectral projectors. Unless `A^T A` is scalar, the new positive metric on source-index space can reweight different commutator directions unequally. In particular, even when the exact kernel is fixed, near-kernel directions and their ordering can move.

Thus a matched-control experiment cannot declare two source-coordinate presentations equivalent merely because they span the same operator family or have the same exact commutant. The source-index metric is part of the representation whenever the statistic uses `Delta_H`.

The condition number `b/a` is an explicit distortion budget. Bounded condition number prevents arbitrary quadratic-form distortion but does not restore exact projector invariance; a claimed arithmetic effect should therefore either fix a canonical source-coordinate metric before inspecting the signal or demonstrate robustness over an admitted bounded class of metrics.

## 4. A two-coordinate anisotropic control creates the target signal from geometry alone

The Pauli example isolates the representation artifact without any arithmetic input.

For `H_1=sigma_z/2`, the commutator-square operator acts with eigenvalue `1` on `E_x,E_y` and `0` on `E_z`. For `H_2=sigma_x/2`, it acts with eigenvalue `1` on `E_y,E_z` and `0` on `E_x`. Therefore

`Delta_eta=ad_(H_1)^2+eta^2 ad_(H_2)^2`

has positive eigenvalues

`1, eta^2, 1+eta^2`

on `E_x,E_z,E_y`, respectively.

The chosen Gram tangent has equal mass on `E_x` and `E_z`. At `eta=1`, its defect energy is `1`, so the `alpha=1/2` cutoff is `1/2`, below both occupied positive modes. The low-mode profile vanishes.

As `eta` decreases, the operator span and joint commutant do not change, but the `E_z` commutator cost falls like `eta^2`. Once `eta^2<=(1+eta^2)/4`, the normalized cutoff contains the entire `E_z` component and the profile jumps to `1/sqrt(2)`.

Nothing source-specific happened. The low mode was created by assigning a smaller weight to one source generator. This is exactly the kind of false positive that the Visual Exploration mandate's normalization and representation controls are meant to eliminate.

## 5. Consequence for the accepted Wang localization clue

`VIS-382` proves that persistent bounded-spread output orientation forces Gram mass into an `O(epsilon_G^2)` band of the joint commutator Laplacian. The accepted clue then proposes to test whether such mass is source-specific by studying

`A_G(alpha)=||P_(0,alpha epsilon_G^2]G||_F`.

The present result adds a necessary representation gate before that comparison is interpreted.

The metric on the source-coordinate index must be fixed independently of the observed localization. Equivalent presentations related by common scaling and orthogonal mixing can be pooled because the normalized profile is exactly invariant. Anisotropic reweightings cannot be treated as harmless reparameterizations merely because they leave the source span unchanged; they modify the object whose low spectrum is being measured.

Accordingly, matched controls for the defect-squared localization test should preserve the pre-declared source-coordinate metric, or else explicitly match/charge its anisotropy. If a positive effect disappears after this gauge is fixed, it was representation leverage rather than source-specific approximate-commutant geometry.

This does not resolve the clue. After fixing the coordinate metric, the central question remains whether the resulting low eigenspace and Gram overlap are forced by arithmetic/source structure and survive source-free controls.

## Prior-art and novelty audit

The identity

`Delta_(H')=delta_H^*(A^T A tensor I)delta_H`

is elementary finite-dimensional Hilbert-space algebra: it is the usual transformation law for a frame/analysis operator under a change of coordinates. No new general theorem is claimed.

A closely related representation freedom is classical in the Gorini--Kossakowski--Sudarshan--Lindblad theory of quantum Markov semigroups: orthogonal/unitary mixing of a family of noise operators leaves the associated quadratic dissipative form unchanged, while a nontrivial positive coefficient matrix records anisotropic weighting of those channels. This is standard background going back to V. Gorini, A. Kossakowski and E. C. G. Sudarshan, *Completely positive dynamical semigroups of N-level systems*, Journal of Mathematical Physics 17 (1976), 821--825, DOI `10.1063/1.522979`, and G. Lindblad, *On the generators of quantum dynamical semigroups*, Communications in Mathematical Physics 48 (1976), 119--130, DOI `10.1007/BF01608499`.

`VIS-380` already bounded the joint-commutator Laplacian against the classical approximate-commutant/spectral-gap literature. The Mathia-specific content here is only the control consequence for the current defect-normalized Wang localization statistic: **its exact harmless gauge is conformal-orthogonal source-coordinate change, not arbitrary invertible reparameterization**, and the Pauli control shows why anisotropic generator weighting must be fixed or priced before any observed low-mode mass is credited to arithmetic structure.

A repository audit found `VIS-375` for scalar spectral reweighting of one external coefficient-space operator and `VIS-379`--`VIS-382` for similarity-orbit and commutator-spectrum conditioning, but no current Visual Exploration finding that audits the metric on the source-generator index itself.

## Dependencies

- `VIS-380`: the joint commutator Laplacian is the source-tuple spectral-gap object controlling bounded orbit amplification.
- `VIS-381`: bounded output orientation requires Gram alignment with low positive commutator modes.
- `VIS-382`: persistent bounded-spread orientation forces such mass already at the defect-squared spectral scale.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue whose proposed low-mode statistic requires the representation gate derived here.

## Research consequence

Future evaluations of the Wang defect-squared localization channel should state the source-coordinate inner product as part of the construction before inspecting the low-mode profile. Test exact invariance under common scale and orthogonal mixing as a basic implementation check. Treat anisotropic source-coordinate weights as an explicit resource with their condition number and provenance, not as free normalization.

Only after that gauge is fixed does excess `A_(G,H)(alpha)` relative to source-free controls become a candidate source-specific signal. The next substantive question remains the one in the accepted clue: whether any admissible arithmetic/source construction produces robust low-mode mass after this coordinate-metric freedom and the previously identified matrix-conditioning freedoms are all quotiented or priced.