# PC-355 — canonical free-Fock signature tower is unitarily control-blind

- **Finding ID:** `PC-355`
- **Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED`
- **Status detail:** `DECISIVE-NEGATIVE` for the canonical full-Fock / left-regular spectralization of the all-depth inversion defect as an escape from PC-354
- **Workflow:** `DERIVED + PRIOR-ART AUDIT + ADVERSARIAL CONTROL`
- **Research line:** `prime_circle`
- **Result type:** exact operator-theoretic no-go
- **Prime dependence:** none in the obstruction after the centered Prime-Circle signature and its matched reciprocal control are formed
- **RH relevance:** high as a boundary result: infinite tensor depth, increasing tensor cutoffs, degree weights, left-creation/Toeplitz realization, and their parity-compatible Hilbert limits do not make the faithful Chen data spectrally source-selective

## Claim

PC-354 rules out fixed finite-dimensional representation lifts after the outer-parity development, but deliberately leaves open a source-forced infinite-dimensional destination. The most canonical candidate is already present in the Chen object itself: represent the completed tensor algebra on its word Hilbert space by left multiplication, equivalently by the full-Fock left creation operators, and then take operator spectra or selfadjoint spectral data.

For the Prime-Circle centered inversion defect this candidate has an exact matched-control obstruction. Let `S` be any finite shell set containing shell `2`, and write the centered alphabet as

\[
K_S=\operatorname{span}\{c\}\oplus
\operatorname{span}\{b_n:n\in S\setminus\{2\}\},
\]

where `c` is the canonical shell-`2` calibration direction and the `b_n` are the transverse centered directions from PC-350--PC-352. Define the source-forced parity

\[
Jc=c,
\qquad
Jb_n=-b_n.
\]

If `\mathcal D_S` is the regularized inversion defect and `\widetilde{\mathcal D}_S` is the matched reciprocal control obtained by `W_n -> -W_n`, then degree by degree

\[
\boxed{
\widetilde{\mathcal D}_S=\theta_J(\mathcal D_S),
}
\]

where `theta_J` is the tensor-algebra automorphism applying `J` to every letter.

Now let

\[
\mathcal F_S^{\le N}
=\bigoplus_{m=0}^{N}K_S^{\otimes m}
\]

with the word basis orthonormal, and let `L_N(a)` denote left multiplication by a tensor series `a`, compressed to degrees at most `N`. The second-quantized parity

\[
\Gamma_N(J)
=\bigoplus_{m=0}^{N}J^{\otimes m}
\]

is unitary and satisfies the exact covariance identity

\[
\boxed{
L_N(\widetilde{\mathcal D}_S)
=
\Gamma_N(J)
L_N(\mathcal D_S)
\Gamma_N(J)^*.
}
\]

Hence every unitary-conjugacy invariant of the canonical truncated Fock operator is identical for the cyclotomic source and the matched non-arithmetic reciprocal control. This includes spectra, singular values, pseudospectra, numerical ranges, and the spectra or determinants of every `*`-polynomial formed functorially from the multiplier together with degree projections, the vacuum projection, or the number operator.

Moreover, because every signature defect has scalar term `1`,

\[
L_N(\mathcal D_S)=I+Q_N
\]

with `Q_N` strictly degree-raising and therefore nilpotent. Thus

\[
\boxed{
\operatorname{Spec}L_N(\mathcal D_S)=\{1\}
}
\]

for every finite tensor cutoff `N`. Passing from ordinary eigenvalues to singular/selfadjoint spectral data removes this unipotent collapse, but not the stronger matched-control unitary equivalence above.

The obstruction is compatible with increasing shell sets and with any degree-weighted Hilbert completion for which the left multiplier has a well-defined operator limit and the weights depend only on tensor degree. Consequently the canonical infinite-dimensional Fock/Toeplitz completion does not escape PC-354. An escape would need extra source-forced structure that breaks this parity functoriality; infinite dimension by itself is insufficient.

## 1. The centered connection makes the control an exact letter involution

PC-350 writes the radial connection using the canonical calibration shell `2` as

\[
\Omega
=c\,dX_2
+\sum_{n\ne2}b_n\,dW_n,
\qquad
W_n=X_n-\varphi(n)X_2.
\]

The matched reciprocal twin used in PC-351--PC-354 keeps the calibration coordinate and the reciprocity residue fixed while sending every transverse profile to its negative:

\[
\widetilde W_n=-W_n.
\]

Therefore

\[
\widetilde\Omega
=c\,dX_2
-\sum_{n\ne2}b_n\,dW_n
=\theta_J(\Omega).
\]

Chen iterated integrals are natural under linear maps of the alphabet: at homogeneous degree `m`, applying `J` to the driving one-form applies `J^{\otimes m}` to the signature coefficient. The reciprocity closing ray uses only the calibration direction `c`, which `J` fixes. Hence the finite-cutoff regularized defects already obey

\[
\widetilde{\mathcal D}_{S,R}
=\theta_J(\mathcal D_{S,R}),
\]

and the degreewise regularized limit gives the claimed identity for `\mathcal D_S`.

This step uses no spectral representation. The `Z/2` parity is already an exact automorphism of the universal source-native tensor object.

## 2. Full-Fock left multiplication implements that parity unitarily

Put the standard Hilbert structure on `K_S` in which the canonical centered letters are orthonormal. Since `J` only changes signs, it is a unitary involution. On the truncated full Fock space define

\[
\Gamma_N(J)
=I\oplus J\oplus J^{\otimes2}\oplus\cdots\oplus J^{\otimes N}.
\]

For a letter `v in K_S`, let `\ell_N(v)` be compressed left creation,

\[
\ell_N(v)\xi=P_{\le N}(v\otimes\xi).
\]

Directly on words,

\[
\Gamma_N(J)\,\ell_N(v)\,\Gamma_N(J)^*
=\ell_N(Jv).
\]

Multiplying this identity along a word and extending linearly gives, for every tensor polynomial `a`,

\[
\boxed{
L_N(\theta_J(a))
=\Gamma_N(J)L_N(a)\Gamma_N(J)^*.
}
\]

Only degrees through `N` contribute to the compressed multiplier, so the same formula applies to the formal regularized defect without making any convergence assumption about the complete infinite series. Substituting `a=\mathcal D_S` proves the source/control unitary equivalence exactly at every finite tensor depth.

The statement is stronger than the triangular-eigenvalue collapse of PC-351. Even if one replaces raw eigenvalues by a selfadjoint construction such as

\[
L_N(\mathcal D_S)^*L_N(\mathcal D_S),
\qquad
L_N(\mathcal D_S)+L_N(\mathcal D_S)^*,
\]

or by any fixed noncommutative `*`-polynomial, the matched control is obtained by conjugation with the same `Gamma_N(J)`. Singular values and all other unitary invariants therefore remain identical.

## 3. The raw left multiplier is spectrally trivial at every cutoff

Write the homogeneous expansion

\[
\mathcal D_S=1+d_1+d_2+\cdots,
\qquad d_m\in K_S^{\otimes m}.
\]

For the inversion defect `d_1=0` by PC-349, but that stronger fact is not needed here. On `\mathcal F_S^{\le N}`, left multiplication by every positive-degree term strictly raises tensor degree. Hence

\[
Q_N:=L_N(\mathcal D_S)-I
\]

satisfies

\[
Q_N^{N+1}=0.
\]

Thus the characteristic polynomial is

\[
\chi_{L_N(\mathcal D_S)}(z)
=(z-1)^{\dim\mathcal F_S^{\le N}}.
\]

Increasing tensor depth can retain arbitrarily much information in matrix entries and in nonnormal geometry, but the ordinary spectrum itself never sees it. This is the free-word analogue of the unipotent/triangular warning in PC-351, now intrinsic to the canonical left-regular representation rather than to a chosen finite matrix substitution.

## 4. Degree weights and growing shell sets do not break the obstruction

The finite-cutoff theorem is enough for an exact no-go and avoids assuming that the all-depth regularized defect is a bounded multiplier on an unweighted full Fock space. Nevertheless the natural limiting repairs are also controlled.

First, let the homogeneous sectors carry positive scalar weights `w_m`. Because `Gamma(J)` preserves each degree, it remains unitary for every such parity-compatible weighted Hilbert norm. Radial damping, signature-kernel-style degree weights, or any other regularizer depending only on word length therefore cannot distinguish the source from the matched control by a unitary spectral invariant.

Second, if `S subset T` are finite shell sets, the canonical inclusion `K_S -> K_T` preserves the decomposition into the even calibration line and odd transverse letters. The parity unitaries are compatible with these inclusions. Hence a growing-shell tower does not remove the conjugacy: every finite stage carries the same intertwiner, and any strong, norm, or resolvent operator limit built functorially from that tower inherits unitary equivalence whenever the limit exists.

This is deliberately conditional at infinite depth. No claim is needed that the formal defect belongs to a particular unweighted Fock multiplier algebra. The exact theorem holds at every finite shell set and every finite tensor degree; any claimed canonical Hilbert/Fock completion must then explain which non-parity-compatible, source-forced structure enters if it is to evade the obstruction.

## 5. Matched-control audit

The control is fatal to an arithmetic interpretation. The proof depends only on

\[
X_2\mapsto X_2,
\qquad
W_n\mapsto-W_n,
\]

not on cyclotomic factorization, primitive roots, prime powers, Ramanujan sums, or von Mangoldt support. Exactly the same tensor parity and Fock-space unitary exist for the non-arithmetic reciprocal controls already admitted in PC-350--PC-354.

Therefore a spectral feature invariant under unitary conjugacy in this canonical Fock realization cannot certify prime support, a Riemann zero, a gamma factor, a critical line, or an `s <-> 1-s` functional equation. The source remains faithfully encoded before quotienting, but the proposed spectral destination is blind to the arithmetic distinction demanded by the Prime-Circle research contract.

## Prior-art audit

No novelty is claimed for the operator-theoretic ingredients. Full Fock space, left creation operators, and noncommutative analytic Toeplitz/free-semigroup algebras are standard; the classical Popescu and Davidson--Pitts framework treats left creation as the canonical free-word shifts. A modern summary is Gelu Popescu, **Noncommutative domains, universal operator models, and operator algebras. II**, *Journal of Operator Theory* 93:2 (2025), 315--354, whose universal models are weighted left creation operators on full Fock space. The elementary covariance under a unitary change of one-particle basis is the standard second-quantization functoriality and is also proved directly above.

Hilbert tensorizations of path signatures and signature kernels are likewise established. Franz J. Kiraly and Harald Oberhauser, **Kernels for Sequentially Ordered Data**, *Journal of Machine Learning Research* 20:31 (2019), 1--45, develops signature-based tensor feature maps and their Hilbert-kernel realization. These references delimit the framework rather than supply a new arithmetic mechanism.

The line-local contribution is the exact composition of that classical Fock functoriality with the source-native Prime-Circle calibration/transverse involution from PC-350--PC-354. A targeted novelty search found no basis for treating the resulting unitary equivalence as a new zeta or RH spectral construction. The finding is a negative boundary statement: the most canonical infinite-dimensional realization of the all-depth Chen object preserves the same matched-control parity instead of breaking it.

## Falsification / disproof audit

- **Parity check:** the centered Prime-Circle connection has one even calibration letter and all transverse centered letters odd under the matched reciprocal twin.
- **Closure check:** the regularizing reciprocity ray lies in the even calibration direction, so `theta_J` commutes with the closure and survives the degreewise limit.
- **Word check:** on every word, `Gamma_N(J)` contributes exactly the product of the letter parities, proving the left-multiplier intertwining identity without representation-theoretic assumptions.
- **Truncation check:** only finitely many homogeneous coefficients act on `F_S^{<=N}`, so no convergence of the complete formal signature is required.
- **Spectrum check:** positive-degree left multiplication strictly raises degree, hence the raw truncated multiplier is identity plus nilpotent and has only eigenvalue `1`.
- **Selfadjoint check:** `Gamma_N(J)` is unitary, so passing to adjoints, singular values, pseudospectra, numerical ranges, or fixed `*`-polynomials cannot break the control equivalence.
- **Weight check:** any scalar degree weighting commutes with parity and leaves the intertwiner unitary.
- **Growing-shell check:** canonical shell inclusions intertwine the parity maps, so increasing the number of shell generators does not by itself create a parity-breaking limit.
- **Control check:** none of the preceding identities uses arithmetic once the reciprocal centered profiles are given; the same obstruction occurs for matched non-arithmetic controls.
- **Destination check:** the construction introduces no independently derived spectral parameter, archimedean factor, zero equation, or critical-line selector.

## Boundary assessment

PC-354 left a genuine opening: perhaps an infinite-dimensional state space forced by the all-depth signature, rather than another finite matrix representation, could provide the missing spectral destination. PC-355 closes the most canonical version of that opening. **The free-Fock/left-regular tower is exactly equivariant under the source/control parity, and that parity is implemented by a unitary at every tensor cutoff and throughout every parity-compatible degree-weighted limit.**

This does not rule out all infinite-dimensional operators. In particular, it does not exclude a construction whose domain, metric, boundary condition, coupling between shell and word degree, or other operator datum is itself forced by roots-of-unity geometry and is not functorial under the matched-control involution. It also does not exclude a non-spectral oriented covariant that retains a genuinely canonical frame.

What it does rule out is a much cheaper escape: merely Hilbertizing the full Chen series, moving to the canonical free-word shifts, adding degree weights, or letting shell/tensor dimension grow. A viable continuation must identify a **source-forced parity-breaking structure before the spectral quotient** and must still fail on the matched non-arithmetic reciprocal controls.