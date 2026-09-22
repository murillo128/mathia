# PL-424 — A biunimodular matched control makes all mod-5 residue/character variances agree while the dephasing image-cone verdict flips

**Evidence/status:** `EXACT-DERIVED + PRIOR-ART-AUDITED + DECISIVE-REPRESENTATION-OBSTRUCTION`.

**Parent findings:** `PL-415`, `PL-419`, `PL-421`, `PL-422`, `PL-423`.

## Claim

The live `PL-421` local-factor gate at `p=5`,

\[
S-\frac14\operatorname{Diag}(S)\succeq0,
\tag{1}
\]

cannot be certified from variance information alone, even if one knows **all four residue-class variances and all four Dirichlet-character variances exactly**. More strongly, there are two positive-semidefinite covariance models satisfying the reality/conjugation symmetry of real residue data for which

- every residue variance is identical,
- every character variance is identical,
- the complete multiplicative-residue group average (the `C_4` twirl) is identical,

but one covariance lies in the positive image of the local dephasing map `Psi_5` and the other does not.

The obstruction is therefore not lack of enough scalar variance asymptotics. It is missing **cross-channel phase/coherence information**. In particular, standard short-interval/AP results that only control total or per-character variances cannot by themselves prove the `PL-421` Loewner floor for the deterministically source-subtracted family left open by `PL-423`.

## 1. Residue and character covariance are Fourier-dual matrices

Order the reduced residues modulo `5` as the powers `1,2,4,3` of the generator `2`, and order the four characters by `j=0,1,2,3`. Let

\[
F_{rj}=\frac12 e^{-2\pi i rj/4},\qquad 0\le r,j\le3,
\tag{2}
\]

be the normalized `C_4` Fourier/character table. For any square-integrable four-channel residue signal `R(y)` and its character coordinates `A(y)=F^*R(y)`, define

\[
S=\langle R,R\rangle,
\qquad
K=\langle A,A\rangle.
\tag{3}
\]

Then

\[
\boxed{S=FKF^*.}
\tag{4}
\]

The diagonal of `S` is the list of residue-class variances, while the diagonal of `K` is the list of character-channel variances. The `PL-421` positive-image criterion is (1), equivalently the normalized residue correlation matrix must have smallest eigenvalue at least `1/4` on its active support.

For real residue data the character coordinates obey the usual reality constraint

\[
A_0,A_2\in\mathbb R,
\qquad
A_3=\overline{A_1}.
\tag{5}
\]

The matched controls below respect this constraint; the obstruction is not an artifact of allowing arbitrary complex covariance matrices.

## 2. Two covariances have the same eight marginal variances but opposite cone membership

First take

\[
K_{\mathrm{good}}=I_4.
\tag{6}
\]

Then `S_good=I_4`, so all eight residue/character marginal variances are `1`, and

\[
S_{\mathrm{good}}-\frac14\operatorname{Diag}(S_{\mathrm{good}})
=\frac34 I_4\succ0.
\tag{7}
\]

Thus `S_good` lies strictly inside the `PL-421` positive image cone.

Now use the explicit vector

\[
v=(1,i,1,-i)^T.
\tag{8}
\]

It satisfies the reality symmetry `v_0,v_2 in R` and `v_3=overline{v_1}`. Direct evaluation of (2) gives

\[
\boxed{Fv=w=(1,1,1,-1)^T.}
\tag{9}
\]

Hence `v` is biunimodular for this Fourier matrix: every coordinate of both `v` and `Fv` has modulus `1`. Put

\[
K_{\mathrm{bad}}=vv^*,
\qquad
S_{\mathrm{bad}}=FK_{\mathrm{bad}}F^*=ww^*.
\tag{10}
\]

Both matrices are positive semidefinite and

\[
\boxed{
\operatorname{Diag}(K_{\mathrm{bad}})
=\operatorname{Diag}(S_{\mathrm{bad}})
=I_4.
}
\tag{11}
\]

Therefore the good and bad controls have **exactly the same four character variances and exactly the same four residue variances**.

But `S_bad` has eigenvalues `(4,0,0,0)`. Since its residue diagonal is `I_4`,

\[
S_{\mathrm{bad}}-\frac14I_4
\tag{12}
\]

has eigenvalues

\[
\boxed{\left(\frac{15}{4},-\frac14,-\frac14,-\frac14\right).}
\tag{13}
\]

Thus `S_bad` violates the image-cone condition maximally in three independent directions. Equivalently its normalized correlation matrix has `lambda_min=0<1/4`.

The two covariance models can also be realized by actual `L^2` channel functions obeying (5). For the bad control take a real unit vector `f(y)` and `A(y)=f(y)v`. For the good control choose orthonormal real functions `f_0,f_2,g,h` and set

\[
A_0=f_0,\quad A_2=f_2,\quad
A_1=(g+ih)/\sqrt2,\quad A_3=(g-ih)/\sqrt2.
\tag{14}
\]

Then the corresponding character Gram matrices are exactly `vv^*` and `I_4`. Hence the matched control survives the basic pointwise reality structure inherited from the prime residue counts.

## 3. Even multiplicative-residue symmetrization erases the failure

Let `P` be the cyclic permutation matrix induced by multiplying reduced residues by `2 mod 5`, and define the complete local twirl

\[
\mathcal T(S)=\frac14\sum_{k=0}^3 P^kSP^{-k}.
\tag{15}
\]

The vector `w=(1,1,1,-1)` has zero periodic autocorrelation at every nonzero cyclic shift:

\[
\sum_{r=0}^3 w_r\overline{w_{r+k}}=0,
\qquad k=1,2,3.
\tag{16}
\]

Consequently

\[
\boxed{
\mathcal T(S_{\mathrm{bad}})=I_4
=\mathcal T(S_{\mathrm{good}}).
}
\tag{17}
\]

This is the same finite harmonic phenomenon usually called a CAZAC/biunimodular sequence. Equation (17) is important for the arithmetic interpretation: averaging over all reduced residue relabelings can turn a covariance that fails the local de-aliasing floor into exactly the same symmetrized covariance as one that passes it.

Therefore a theorem controlling only a residue-summed variance, a multiplicatively symmetrized covariance, or the diagonal character variances cannot establish (1) without an additional theorem recovering or bounding the unsymmetrized coherences.

## 4. Relation to the live deterministic subtraction after PL-423

`PL-423` leaves open the deterministic source subtraction

\[
r_a(y;h)=P_a(y;h)-\frac h4,
\tag{18}
\]

because its principal character channel is the genuine total short-interval fluctuation rather than an exact zero mode. The natural next attempt is to use existing short-interval variance and Dirichlet-`L` pair-correlation theory to estimate the four character sectors.

The present matched control shows exactly what such an attempt would still be missing. Even perfect asymptotics for all four diagonal quantities

\[
\int |A_\chi(y)|^2\,dy
\tag{19}
\]

plus perfect knowledge of all four residue variances do not imply the matrix inequality (1). One must control cross terms

\[
\int A_\chi(y)\overline{A_\psi(y)}\,dy,
\qquad \chi\ne\psi,
\tag{20}
\]

strongly enough to obtain a lower eigenvalue bound for the **full** covariance matrix after return to residue coordinates.

This is sharper than the earlier `PL-419` obstruction. `PL-419` shows that positive residue diagonal readouts cannot reconstruct the signed `PL-415` supertrace. Here the target is instead the positive-image cone itself, and the control gives the same marginal variances in **both dual bases** while flipping the cone verdict.

## 5. Prior-art and novelty audit

The Fourier ingredient is classical. Vectors whose entries and normalized discrete Fourier transforms are both unimodular are standard biunimodular/CAZAC sequences; see, for example, G. Björck and B. Saffari, “New classes of finite unimodular sequences with unimodular Fourier transforms. Circulant Hadamard matrices with complex entries,” *C. R. Acad. Sci. Paris Sér. I Math.* **320** (1995), 319–324, and H. Führ and Z. Rzeszotnik, “On biunimodular vectors for unitary matrices,” *Linear Algebra Appl.* **484** (2015), 86–129, DOI `10.1016/j.laa.2015.06.019`, arXiv `1506.06738`.

Variance of primes in short intervals/arithmetic progressions and its relation to Dirichlet-`L` zero statistics is also established prior art; sources 105–107 in `research/prime_lattice/SOURCES.md` already anchor that literature. D. A. Goldston and C. Y. Yildirim, “Primes in Short Segments of Arithmetic Progressions,” *Canad. J. Math.* **50** (1998), 563–580, DOI `10.4153/CJM-1998-031-9`, is a particularly direct example whose basic observable is total variance summed over reduced residue classes.

No novelty is claimed for CAZAC sequences, Fourier duality, Gram matrices, covariance twirling, or the variance literature. The targeted audit did not locate the line-specific statement that the `p=5` `PL-421` Schur/dephasing image cone admits reality-compatible matched covariance controls with identical marginals in both the residue and character bases but opposite cone membership. The durable contribution is only that exact representation-level obstruction.

## 6. Adversarial audit and scope

1. `K_bad` and `K_good` are matched formal covariance models, not claims about the actual von-Mangoldt residue process. Their role is information-theoretic: no argument using only the matched marginal data can certify the cone. Actual arithmetic may impose stronger cross-covariance identities; proving one strong enough to force (1) remains a valid route.

2. The controls respect the basic reality/conjugation constraint (5), but they do not claim to satisfy every higher-order identity of primes. Any surviving arithmetic theorem must identify the extra identity explicitly rather than infer it from positivity, character orthogonality, or variance asymptotics alone.

3. The result does not say that character-variance estimates are useless. They can supply diagonal scale and can combine with genuinely independent off-diagonal bounds, for example a direct operator-norm estimate on the correlation error. What is ruled out is **variance-only certification** of the `1/4` floor.

4. The `C_4` twirl in (15) is a local multiplicative-residue symmetry. Equality of twirls does not imply equality of the unsymmetrized arithmetic processes. That distinction is precisely the point: group averaging can erase the coherence that decides the `PL-421` gate.

5. No implication toward RH is claimed. Passing the local image cone would only reconstruct a positive preimage for the mod-5 local factor; all later source-replacement, continuation, and global localization gates of the line would still remain.

## Consequence for the research line

The next analytic target after `PL-423` should **not** be “prove sufficiently sharp variances for the four mod-5 character channels.” Even exact diagonal variances in both natural Fourier-dual bases leave the decisive Loewner floor undetermined.

A viable continuation must instead obtain a genuinely matrix-valued arithmetic estimate: control the cross-character/cross-residue covariance strongly enough to force

\[
S-\frac14\operatorname{Diag}(S)\succeq0,
\tag{21}
\]

or replace this local-image route by a source-faithful signed statistic that does not require the cone. The missing datum has now been isolated as unsymmetrized coherence rather than scalar variance size.
