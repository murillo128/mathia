# PF-197 — matrix-valued critical Cwikel theory removes the local vector-endpoint gap

**Status:** `LITERATURE+DERIVED + ROUTE-SHARPENING + POSITIVE/BOUNDARY`. PF-196 identifies the correct critical coefficient currency for the exact Lambert body: the homogeneous `L log L` norm costs one Lambert-depth logarithm, but the exact prime/shift tail still sums that penalty. The remaining analytic endpoint discussion treated the available Cwikel--Solomyak theorem as essentially a scalar compact model and left open whether the **matrix-valued gradient form itself** has an appropriate weak-`S_1` theorem. That local obstacle is not real. Ponge's matrix-valued critical Cwikel theorem applies to arbitrary order `-n/2` pseudodifferential operators on a Hermitian vector bundle and gives `Q u P in S_{1,infinity}` with norm controlled linearly by the matrix-valued `L log L` norm. In dimension two, the localized PF-175 gradient-resolvent factors have exactly order `-1=-n/2`; after a finite block-bundle enlargement, the principal localized PF form is literally a corner of Ponge's `Q u P` operator. Ponge's underlying compact-support lemma is explicitly stated to continue to noncompact manifolds. Thus the endpoint program no longer needs a new scalar-to-vector Cwikel theorem. Its analytic burden is narrower and genuinely PF-specific: obtain a localized pseudodifferential decomposition of the actual two-metric resolvent form with **uniform or prime-summably controlled constants across the infinite normalized modules**, then control the off-diagonal/reassembly terms without losing the PF-196 effective-area budget. No global weak-`S_1` relative-resolvent theorem, endpoint conservative splice, wave equivalence, or RH consequence is established here.

## Claim

Let `g` and `h` be two smooth quasi-isometric metrics on a two-dimensional module on which the PF-175 relative first-resolvent form is localized. Write

\[
R_g=(\Delta_g+1)^{-1},\qquad R_h=(\Delta_h+1)^{-1},
\]

and let `C` be PF-175's cotangent coefficient defect, so that its critical gradient contribution is represented locally by

\[
\boxed{
T_C=(dR_h)^* M_C\, dR_g,
}
\tag{1}
\]

up to the bounded zero-order bundle/measure identifications already present in PF-175. On every fixed smooth relatively compact localization where the resolvents are replaced by their standard interior parametrices,

\[
dR_g,\ dR_h\in\Psi^{-1},
\tag{2}
\]

because `R_g,R_h` are elliptic operators of order `-2` and exterior differentiation has order `1`.

Raphaël Ponge proves the following critical Cwikel estimate. If `M^n` is a closed manifold, `E` is a Hermitian vector bundle, `P,Q in Psi^{-n/2}(M,E)`, and

\[
u\in L\log L(M,\operatorname{End}E),
\]

then

\[
\boxed{
Q M_u P\in\mathcal S_{1,\infty},\qquad
\|Q M_uP\|_{1,\infty}\le C_{P,Q}\|u\|_{L\log L}.
}
\tag{3}
\]

This is Proposition 3.13 of Ponge, *Weyl's Laws and Connes' Integration Formulas for Matrix-Valued `L log L`-Orlicz Potentials*, Mathematical Physics, Analysis and Geometry **25** (2022), article 10, DOI `10.1007/s11040-022-09422-9`, arXiv:2107.13605. The proof is by localization from a compact-support Cwikel lemma; Ponge's Remark 3.11 explicitly states that the compact-support lemma continues to hold when the ambient manifold is noncompact.

Equation (3) fits (1) at the local critical order without reducing the coefficient to a scalar. To make the bundle types literal, put

\[
E=\mathbb C\oplus T^*M
\]

and define block pseudodifferential operators

\[
\widetilde P=
\begin{pmatrix}
0&0\\
dR_g&0
\end{pmatrix},
\qquad
\widetilde Q=
\begin{pmatrix}
0&(dR_h)^*\\
0&0
\end{pmatrix},
\qquad
\widetilde u=
\begin{pmatrix}
0&0\\
0&C
\end{pmatrix}.
\tag{4}
\]

After inserting the compact cutoffs needed for an interior localization, `P_tilde,Q_tilde in Psi^{-1}(M,E)` and `u_tilde` is an `End(E)`-valued `L log L` coefficient whenever `C` is. The scalar-to-scalar corner of

\[
\widetilde Q M_{\widetilde u}\widetilde P
\]

is exactly (1). Compression of a weak-Schatten operator remains in the same ideal, so Ponge's theorem yields the **local** implication

\[
\boxed{
C\in L\log L
\quad\Longrightarrow\quad
T_C^{\rm local}\in\mathcal S_{1,\infty},
}
\tag{5}
\]

with a constant determined by the localized order-`-1` factors. The same argument allows matrix-valued cotangent coefficients; the vector-gradient nature of PF-175 is therefore not an independent endpoint obstruction.

For the exact PF-191 Lambert coefficient, PF-196 already proves

\[
\|C_n\|_{L\log L}
\lesssim
\frac{d_n(1+a_n)}{\cosh a_n}
\tag{6}
\]

up to the fixed quasi-isometry comparison between `C_n` and the metric-deviation scalar, and moreover

\[
\boxed{
\sum_n\frac{d_n(1+a_n)^k}{\cosh a_n}<\infty
\qquad\text{for every fixed }k\ge0.
}
\tag{7}
\]

Consequently, if the PF localization can be arranged so that the constants in (3) for the module family obey one fixed polynomial Lambert-depth envelope

\[
C_{P_n,Q_n}\le C(1+a_n)^m
\tag{8}
\]

for some fixed `m` -- in particular if they are uniform -- then (6)--(7) give the prime-summable local weak-trace budget

\[
\boxed{
\sum_n
\|T_{C_n}^{\rm local}\|_{1,\infty}^{\#}<\infty.
}
\tag{9}
\]

Equation (9) is **conditional on the quantitative family estimate (8)** and on a localization that represents the actual PF resolvent form by the critical pseudodifferential pieces plus controlled remainders. Ponge's theorem does not by itself provide (8), does not sum an infinite family of varying localizations, and does not identify the full noncompact relative resolvent with the direct sum of those pieces.

## 1. Why this is the right critical operator order

PF-175's strong-Schatten proof factors the coefficient perturbation into two gradient-resolvent half-factors. At the endpoint, treating the halves separately asks for a one-sided weak-`S_2` theorem. PF-195 shows that this cannot be obtained from bare critical coefficient `L^2` mass by generic Cwikel theory while retaining the Lambert effective-area gain.

The direct two-sided form is different. In two dimensions

\[
dR:\ L^2\longrightarrow L^2(T^*M)
\]

has pseudodifferential order `-1`, so the composition

\[
(dR_h)^*M_CdR_g
\]

is exactly the critical `Q u P` geometry for Ponge's theorem: both smoothing factors have order `-n/2`, while the rough coefficient stays unsplit in `L log L`. This is precisely the route suggested abstractly after PF-196, but the matrix-valued theorem shows that no scalarization of the principal coefficient is needed.

The scalar density term in PF-175 is not the critical difficulty. It has resolvent factors of order `-2` on both sides rather than gradient-resolvent factors of order `-1`. The endpoint frontier is therefore correctly concentrated on the cotangent coefficient term (1), localization/reassembly, and the geometric construction supplying its coefficient budget.

## 2. Local noncompactness is not the theorem-level blocker

Ponge's global Proposition 3.13 is stated on a closed manifold because its proof patches finitely many local Cwikel estimates. The local ingredient, Lemma 3.9, treats operators whose relevant kernels/symbols are compactly supported in a coordinate patch, and Remark 3.11 states explicitly that this lemma continues to hold if the ambient manifold is noncompact.

That distinction matters for the prime flute. It means that the infinite-type noncompact surface does not automatically invalidate the critical Cwikel mechanism on one compactly localized module. The real issue is **uniformity over infinitely many modules and the terms produced when the global resolvent is cut apart**.

Concretely, for a coefficient supported where `chi=1`, one would decompose a factor such as

\[
\chi dR_g
=
\chi dR_g\chi'
+
\chi dR_g(1-\chi'),
\qquad \chi'=1\text{ near }\operatorname{supp}\chi.
\tag{10}
\]

The first term is the local pseudodifferential piece to which (3)--(5) apply. The second is off-diagonal and smoothing by pseudolocality, but on the full prime flute its Schatten norm and its **uniform dependence on the module** still have to be proved. The same applies on the target side and to commutator/partition terms introduced by a finite-color or IMS reassembly.

Thus the correct endpoint question is no longer

\[
\text{``does a matrix/vector critical weak-}S_1\text{ theorem exist?''}
\]

but rather

\[
\boxed{
\text{``can the PF modules be localized with prime-summably controlled Cwikel and off-diagonal constants?''}
}
\tag{11}
\]

That is a materially narrower and more falsifiable analytic gate.

## 3. Interaction with the exact Lambert budget

PF-191 is unusually favorable for the uniformity problem. In its area coordinates the ambient local hyperbolic metric is

\[
g=\frac{dy^2}{1+y^2}+(1+y^2)d\tau^2,
\]

independent of the Lambert depth `a`; the parameter enters through the domain/cross-section and the exact transport. PF-196 then proves that the coefficient's critical Orlicz cost is not merely finite modulewise but prime-summable even after **any fixed polynomial loss in `a`**.

This does not prove (8). Cutoff derivatives, boundary/corner placement, target/source chart conversion, or global-resolvent off-diagonal tails may depend on `a` in ways not measured by the coefficient norm. But it changes the quantitative target: exact uniformity is sufficient rather than necessary. A localization proof may spend a fixed polynomial amount of Lambert-depth currency and still preserve summability by PF-196.

Conversely, a bound that forgets the shrinking effective cross-section and charges each module at scale `O(d_n)` remains insufficient. Ponge's theorem is linear in the `L log L` norm, so any loss of the `1/cosh a_n` factor would enter through the PF localization constants or through reassembly, not through the critical Cwikel theorem itself.

## 4. Prior art and novelty assessment

**Raphaël Ponge**, *Weyl's Laws and Connes' Integration Formulas for Matrix-Valued `L log L`-Orlicz Potentials*, Mathematical Physics, Analysis and Geometry **25** (2022), article 10. DOI `10.1007/s11040-022-09422-9`; arXiv:2107.13605.

- Proposition 3.13 proves (3) for matrix-valued `L log L` coefficients and arbitrary critical-order pseudodifferential factors `P,Q in Psi^{-n/2}` on a closed manifold.
- Lemma 3.9 is the compactly supported local form obtained by coordinate/trivialization transfer from the torus Cwikel estimate.
- Remark 3.11 explicitly states that Lemma 3.9 continues to hold on noncompact manifolds.
- Corollary 3.15 specializes the result to connection-Laplacian critical factors.

Ponge's theorem itself is prior art, as are the ordinary facts that an elliptic first resolvent has pseudodifferential order `-2`, that `dR` has order `-1`, and that finite bundle block enlargements preserve pseudodifferential order. No novelty is claimed for any of those facts.

The project-specific deduction is the route sharpening (4)--(11): **the principal PF-175 vector-gradient endpoint term already fits an existing matrix-valued critical weak-`S_1` theorem after localization, and PF-196 has exactly the coefficient currency that theorem requires.** Therefore the unresolved analytic endpoint is quantitative family uniformity plus global reassembly, not absence of a suitable vector-valued Cwikel theorem. A targeted search did not identify a theorem that simultaneously supplies those uniform constants for the degenerating/infinite PF module family and controls the full two-metric resolvent reassembly; search absence is not treated as a novelty theorem.

## 5. Falsification and boundary checks

A later adversary can test PF-197 through the following chain:

1. verify Ponge Proposition 3.13 with the exact hypotheses `P,Q in Psi^{-n/2}(M,E)` and `u in L log L(M,End(E))`, and its linear weak-`S_1` estimate;
2. verify Remark 3.11 applies only to the compact-support/local lemma, not automatically to the entire global proposition on an arbitrary noncompact manifold;
3. on a fixed smooth two-dimensional PF localization, verify `R_g,R_h in Psi^{-2}` and hence `dR_g,dR_h in Psi^{-1}` for the interior parametrix pieces;
4. check the block construction (4) and that its scalar corner is exactly the PF-175 principal coefficient form (1), modulo only bounded zero-order identifications;
5. use PF-175's pointwise `|C|<=C delta` and PF-196's actual Luxemburg estimate to verify the local coefficient input (6);
6. keep (8) explicitly conditional: Ponge's theorem does not state a uniform constant for an infinite varying family of PF modules;
7. derive an explicit cutoff/parametrix decomposition such as (10), and prove the off-diagonal, smoothing, commutator, interface, and finite-color reassembly pieces are trace class or weak `S_1` with prime-summable cost;
8. reject any argument that obtains local weak `S_1` only by replacing the PF-196 coefficient scale with `O(d_n)`, or that assumes bounded-overlap geometry automatically controls weak-Schatten counting without an operator-level decomposition.

PF-197 would be overclaimed if read as proving any of the following, none of which is asserted:

- the complete prime/shift first relative resolvent belongs to `S_{1,infinity}`;
- Ponge Proposition 3.13 applies globally without modification to the infinite prime flute;
- its constant is uniform over the PF module family;
- all off-diagonal/global resolvent terms are trace class;
- the endpoint exact-area conservative splice of PF-183 exists;
- PF-195's one-sided weak-`S_2` obstruction has disappeared;
- ordinary Kato--Rosenblum wave equivalence follows from weak `S_1`;
- the prime flute is spectrally distinguishable from the composite shift clone at an RH-relevant level.

The finding removes one **local analytic false gap** while leaving both of the accepted weak-endpoint clue's genuine gates intact: canonical endpoint geometry and no-loss global operator reassembly.