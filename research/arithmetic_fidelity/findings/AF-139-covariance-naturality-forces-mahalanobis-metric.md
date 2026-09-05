# AF-139 — Full affine naturality forces the inverse-covariance source metric

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-MECHANISM`, `GAUGE-REPAIR`, `SECOND-ORDER-BOUNDARY`, `NO-NOVELTY-CLAIM`

## Claim

AF-138 leaves one concrete source-metric question open: if a source probability law is independently part of the mathematical object, can its covariance supply a canonical positive coefficient metric rather than an arbitrary gauge choice?

For covariance-only constructions the answer is exact. Let

\[
\mathcal P_m=\{C\in M_m(\mathbb C):C=C^*>0\}
\]

be the positive-definite cone. Suppose a rule

\[
\Phi:\mathcal P_m\to\mathcal P_m
\]

assigns a coefficient metric to a source covariance and is natural under every invertible reparameterization in the following sense. If coordinates are changed by

\[
x_R=R^{-1}x,
\qquad R\in GL_m(\mathbb C),
\]

so that

\[
C_R=R^{-1}CR^{-*},
\tag{1}
\]

then the metric is required to transport as the same quadratic form:

\[
\Phi(C_R)=R^*\Phi(C)R.
\tag{2}
\]

Then there is one constant `c>0`, independent of `C`, such that

\[
\boxed{\Phi(C)=c\,C^{-1}.}
\tag{3}
\]

No continuity, differentiability, convexity, or spectral ansatz is needed. Full `GL_m` naturality alone makes the Mahalanobis/precision metric the unique positive metric obtainable from covariance alone, up to one global normalization.

Consequently, if a centered random coefficient vector `X` has positive-definite covariance

\[
C=\mathbb E[XX^*]
\]

and a synthesis map

\[
A:\mathbb C^m\to H
\]

is given, then choosing the normalized covariance-natural metric

\[
M=C^{-1}
\tag{4}
\]

turns AF-138's generalized Gram operator into

\[
\widehat G
=M^{-1/2}A^*AM^{-1/2}
=C^{1/2}A^*AC^{1/2}.
\tag{5}
\]

The corresponding output covariance is

\[
\Sigma=ACA^*.
\tag{6}
\]

Writing `\widehat A=AC^{1/2}`, one has

\[
\widehat G=\widehat A^*\widehat A,
\qquad
\Sigma=\widehat A\widehat A^*.
\tag{7}
\]

Hence `\widehat G` and `\Sigma` have the same nonzero eigenvalues with multiplicity. The generalized source spectrum forced by covariance naturality is therefore exactly the nonzero principal-variance spectrum of the output random object `AX`.

For a fixed target `k\in H`, let `F_B` be the spectral projector of `\Sigma` for a Borel set `B\subset(0,\infty)`. AF-138's target-relative generalized spectral measure becomes

\[
\boxed{
\mu_{C;A,k}(B)=\|F_Bk\|^2.
}
\tag{8}
\]

Thus a covariance-natural cutoff at variance level `\tau` loses exactly

\[
\boxed{
d_{C,\tau}^2-
\operatorname{dist}(k,\operatorname{ran}A)^2
=\|F_{(0,\tau)}k\|^2.
}
\tag{9}
\]

The low-generalized-eigenvalue Picard tail of AF-138 is not a separate object in this setting: it is precisely the target energy lying in low-variance principal components of the source-induced output covariance.

The second-order boundary is equally exact. Two source laws with the same covariance induce the same metric `(4)`, the same generalized spectrum `(5)`, the same output covariance `(6)`, and the same target spectral profile `(8)` for fixed `A,k`. Therefore no covariance-only natural metric can preserve a discriminator that lives purely in higher moments, phase relations not visible to covariance, or other distributional structure beyond second order.

## Derivation

### Full affine naturality uniquely determines the metric

First evaluate `\Phi` at the identity covariance. For every unitary `U`, equation `(1)` gives

\[
U^{-1}IU^{-*}=I.
\]

Equation `(2)` therefore implies

\[
\Phi(I)=U^*\Phi(I)U
\qquad
\text{for every unitary }U.
\tag{10}
\]

A Hermitian matrix commuting with the full unitary group is scalar, so

\[
\Phi(I)=cI
\tag{11}
\]

for some `c>0`.

Now fix arbitrary `C>0` and choose

\[
R=C^{1/2}.
\]

Then

\[
R^{-1}CR^{-*}
=C^{-1/2}CC^{-1/2}
=I.
\tag{12}
\]

Applying `(2)` and `(11)`,

\[
cI
=\Phi(I)
=C^{1/2}\Phi(C)C^{1/2}.
\]

Multiplying by `C^{-1/2}` on both sides gives `(3)`.

This proof is a transitive-group argument. The positive cone is one `GL_m` congruence orbit, while the stabilizer of `I` is the unitary group. The stabilizer forces the value at `I` to be scalar, and equivariance transports that single value to the whole cone.

### The probabilistic covariance transforms with the required opposite variance

Let `X` be centered with covariance `C`, and represent the same random source after a generator change `A_R=AR` by

\[
X_R=R^{-1}X.
\]

Then

\[
\operatorname{Cov}(X_R)
=R^{-1}CR^{-*}
=C_R.
\tag{13}
\]

Its inverse transforms as

\[
C_R^{-1}
=R^*C^{-1}R,
\tag{14}
\]

which is exactly the metric transport law required by AF-138. Therefore the inverse covariance is not merely a convenient whitening matrix; it has the correct tensorial transformation law for a coefficient inner product.

With `M=C^{-1}`, AF-138's metric-whitened synthesis map is

\[
AM^{-1/2}=AC^{1/2}=\widehat A,
\]

proving `(5)`--`(7)`.

### The target measure is the output-covariance spectral measure

Take a singular-value decomposition on the active finite-dimensional source range,

\[
\widehat A v_j=s_j u_j,
\qquad s_j>0.
\]

Then

\[
\widehat Gv_j=s_j^2v_j,
\qquad
\Sigma u_j=s_j^2u_j.
\tag{15}
\]

For the AF-138 whitened target pairing,

\[
\widehat b
=C^{1/2}A^*k
=\widehat A^*k,
\]

so

\[
\langle v_j,\widehat b\rangle
=s_j\langle u_j,k\rangle.
\tag{16}
\]

AF-138 weights the source-side component by `1/s_j^2`. Hence for every `B\subset(0,\infty)`,

\[
\left\|E_B(\widehat G)
\widehat G^{\dagger/2}\widehat b\right\|^2
=
\sum_{s_j^2\in B}|\langle u_j,k\rangle|^2
=\|F_Bk\|^2,
\]

which proves `(8)`. Equation `(9)` follows by taking `B=(0,\tau)` and using

\[
\overline{\operatorname{ran}\Sigma}
=\operatorname{ran}(AC^{1/2})
=\operatorname{ran}A
\]

in the present finite-source setting.

## Exact control: equal covariance preserves no higher-order discriminator

Already in one real dimension the covariance-natural metric has a large collision fiber. Consider centered random variables

\[
X_1=\begin{cases}
-1,&1/2,\\
+1,&1/2,
\end{cases}
\]

and

\[
X_2=\begin{cases}
-\sqrt3,&1/6,\\
0,&2/3,\\
+\sqrt3,&1/6.
\end{cases}
\]

Both satisfy

\[
\mathbb E[X_i]=0,
\qquad
\mathbb E[X_i^2]=1,
\]

but

\[
\mathbb E[X_1^4]=1,
\qquad
\mathbb E[X_2^4]=3.
\tag{17}
\]

For `A=1`, both source laws therefore induce the same covariance `C=1`, the same unique normalized natural metric `M=1`, the same generalized Gram spectrum `{1}`, and the same output-covariance spectral profile. Yet a fourth-moment discriminator separates them exactly.

This is not a defect in Mahalanobis geometry. It is the correct information boundary: a construction whose only input from the source law is covariance cannot recover information that covariance does not contain.

## Boundary conditions and falsification tests

The uniqueness statement depends on the exact declared category.

1. **Full invertible naturality is essential.** If only unitary/orthogonal coordinate changes are admitted, covariance-only rules such as `\Phi(C)=C`, `C^2`, or more general positive spectral functions are equivariant. The full `GL_m` congruence action is what collapses the metric freedom to `cC^{-1}`.

2. **The rule is covariance-only.** If `\Phi` may depend on the full source law, extra markings, higher moments, group structure, locality, arithmetic weights, or a second scatter functional, other affine-equivariant geometries can exist. AF-139 classifies only metrics whose declared source input is the positive-definite covariance matrix itself.

3. **Positive definiteness matters.** When `C` is singular, `C^{-1}` does not exist on the full coefficient space. The natural object is then the active covariance support/quotient, with any metric claim restricted to that support. Treating null-variance directions as ordinary finite-cost coordinates would add structure not supplied by the law.

4. **A probability law is not automatically canonical.** AF-139 shows that *given* an independently specified law and the decision to retain only covariance, its natural metric is forced. It does not justify choosing that law. A law selected from the downstream target, desired cutoff, or RH conclusion simply relocates the arbitrariness from `M` to the source distribution.

5. **Absolute spectral thresholds require source scale.** A normalized probability law fixes covariance scale, so `M=C^{-1}` fixes the generalized eigenvalue scale. If the source is specified only up to global dilation, the same projective ambiguity noted in AF-138 remains and only ratios/order are intrinsic.

The decisive matched-control test for any covariance-based arithmetic proposal is therefore stronger than checking coordinate invariance: construct a source control with the same declared covariance but different claimed arithmetic discriminator. If the downstream certificate depends only on `(A,C)` through `(5)`--`(8)`, that discriminator has already been erased.

## Prior art and novelty assessment

No novelty claim is made for covariance, Mahalanobis geometry, affine equivariance, whitening, principal components, or the equality of nonzero spectra of `B^*B` and `BB^*`.

- P. C. Mahalanobis, **“On the Generalized Distance in Statistics,”** *Proceedings of the National Institute of Sciences of India* 2 (1936), 49--55; reprinted in *Sankhya A* 80 (Suppl. 1), 1--7. Role: classical inverse-covariance geometry underlying `(3)`--`(4)`.
- Harold Hotelling, **“Analysis of a Complex of Statistical Variables into Principal Components,”** *Journal of Educational Psychology* 24 (1933), 417--441 and 498--520, DOI `10.1037/h0071325` and `10.1037/h0070888`. Role: classical principal-component interpretation of covariance eigenvectors/eigenvalues as variance directions.
- Agnan Kessy, Alex Lewin, and Korbinian Strimmer, **“Optimal Whitening and Decorrelation,”** *The American Statistician* 72(4), 309--314 (2018), DOI `10.1080/00031305.2016.1277159`. Role: modern systematic account of covariance whitening and its residual rotational freedom.
- Joni Virta, **“On characterizations of the covariance matrix,”** arXiv:`1810.01147` (2018). Role: neighboring prior art on affine/full-affine equivariance as a characterization principle for scatter functionals; AF-139 uses a simpler fixed-covariance-cone equivariance problem for the dual metric.

The exact uniqueness proof `(10)`--`(12)` is an elementary homogeneous-space argument and is not asserted to be a new theorem in invariant/statistical geometry. The new-to-this-line content is the diagnostic synthesis with AF-138: **if source covariance is the only retained probabilistic geometry and full generator reparameterization is treated as gauge, the metric repair is forced to be inverse covariance, its generalized Gram spectrum is exactly output PCA variance, and its entire fidelity ceiling is second order.**

## Consequence for the current frontier

AF-138's generic request to derive a source metric now has a complete answer for one important input class. A nondegenerate source probability law can provide the metric through covariance, and full affine naturality leaves no competing covariance-only choice beyond scale.

This also supplies a stopping rule. Once a proposed spectral carrier is reduced to a covariance-natural metric, further changes of whitening convention cannot recover arithmetic information absent from the covariance. Any stronger discriminator must enter through genuinely additional source structure: higher-order moments/cumulants, marked relations, arithmetic weights, locality, an independently defined energy, or another non-second-order object.

For an RH-facing application, the remaining burden is therefore not to optimize a covariance whitening. It is to prove that the rational-prime discriminator of interest is visible in the source law at second order, or else identify and justify the extra non-covariance structure that carries it through the compression.