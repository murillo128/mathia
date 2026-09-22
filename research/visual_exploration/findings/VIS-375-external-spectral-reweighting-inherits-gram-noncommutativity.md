# VIS-375 — scalar spectral reweighting of one external Hermitian operator cannot create new Gram orientation

## Claim

Let `A_W` be a finite-dimensional Wang coefficient map with source-free Gram

`G=A_W^*A_W>=0`.

Let `H=H^*` be an externally supplied Hermitian operator on the coefficient space, with spectral resolution

`H=sum_alpha h_alpha P_alpha`,

where the `h_alpha` are the distinct eigenvalues of `H`. Let a positive relative coefficient metric be obtained by scalar functional calculus,

`C=f(H)=sum_alpha f(h_alpha) P_alpha`,

with

`m I <= C <= M I`,

for fixed `0<m<=M<infinity`. Define the discrete spectral Lipschitz constant

`L_H(f)=max_(h_alpha!=h_beta) |f(h_alpha)-f(h_beta)|/|h_alpha-h_beta|`,

with `L_H(f)=0` when `H` has only one distinct eigenvalue.

Then the commutator of the induced metric with the Wang Gram is bounded exactly at the Hilbert--Schmidt/Frobenius level by the noncommutativity already present in `H`:

`||[G,C]||_F <= L_H(f) ||[G,H]||_F`.

More precisely, for every pair of spectral blocks,

`P_alpha [G,C] P_beta`
` = (f(h_beta)-f(h_alpha)) P_alpha G P_beta`,

while

`P_alpha [G,H] P_beta`
` = (h_beta-h_alpha) P_alpha G P_beta`.

Consequently, scalar spectral reweighting `f(H)` cannot manufacture Gram orientation that was absent from the external operator `H`; it can only rescale the off-diagonal Gram blocks already exposed by `H`.

Combining this with the resolved-gap/cluster control in `VIS-374`, suppose the spectrum of `G` is partitioned into clusters of within-cluster width `eta` and resolved inter-cluster separation `gamma>0`. Then there exists a positive metric `C_*` commuting with the exact `G`, with `mI<=C_*<=MI`, such that every ordered squared Wang singular value obeys

`|s_k(A_W C^(1/2))^2-s_k(A_W C_*^(1/2))^2|`
` <= ||G||_op sqrt(M/m) L_H(f) ||[G,H]||_F/gamma + 2M eta`.

Thus a bounded positive metric generated as a scalar function of one external Hermitian operator remains spectrally close to Gram-commuting preconditioning whenever the external operator is nearly Gram-commuting on resolved gaps, the scalar filter has moderate spectral slope, and the unresolved Gram clusters are narrow.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL FUNCTIONAL-CALCULUS COMMUTATOR IDENTITY + STRUCTURAL NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This proves no estimate for the normalized Chebyshev-theta remainder, the prime-number-theorem remainder, zeta zeros, or RH. It does not rule out a physically fixed external operator with genuinely large resolved noncommutativity, nor structures outside bounded positive scalar functional calculus.

## 1. Why this is the next Wang control

`VIS-372` showed that an external Hermitian structure commuting exactly with `G` remains joint-spectral filtering. `VIS-373` priced arbitrary near-commuting positive metrics by the Gram commutator divided by resolved spectral gaps. `VIS-374` then closed the apparent loophole in which large rotations hide inside nearly degenerate Gram clusters: bounded positive orientation inside a narrow cluster is spectrally cheap.

A natural remaining construction is to start from one independently motivated Hermitian operator `H` and turn it into a positive metric by nonlinear scalar spectral reweighting: heat-type filters, resolvent-like weights, monotone spectral transforms, soft projectors, or other choices of `f(H)`.

Such a metric can look substantially different from `H` spectrally, so it is worth asking whether the nonlinear functional calculus itself can create the resolved orientation that the preceding controls require. The answer in Frobenius geometry is no: all off-diagonal orientation relative to `G` is inherited block-by-block from `H`.

This finding remains on the source-blind coefficient layer. Neither `H` nor `f` is assumed to encode prime-dependent source values, and no arithmetic source is used in the derivation.

## 2. Exact block identity

Because the `P_alpha` are spectral projectors of `H`,

`C P_alpha=P_alpha C=f(h_alpha)P_alpha`.

Therefore

`P_alpha G C P_beta=f(h_beta)P_alpha G P_beta`,

and

`P_alpha C G P_beta=f(h_alpha)P_alpha G P_beta`.

Subtracting gives

`P_alpha [G,C] P_beta`
` = (f(h_beta)-f(h_alpha))P_alpha G P_beta`.

The identical calculation for `H` gives

`P_alpha [G,H] P_beta`
` = (h_beta-h_alpha)P_alpha G P_beta`.

For `alpha=beta`, both blocks vanish. For distinct spectral values,

`|f(h_beta)-f(h_alpha)|`
` <= L_H(f)|h_beta-h_alpha|`.

Since the matrix blocks `P_alpha X P_beta` are mutually orthogonal in Frobenius inner product,

`||[G,C]||_F^2`
` = sum_(alpha,beta) |f(h_beta)-f(h_alpha)|^2 ||P_alpha G P_beta||_F^2`
` <= L_H(f)^2 sum_(alpha,beta) |h_beta-h_alpha|^2 ||P_alpha G P_beta||_F^2`
` = L_H(f)^2 ||[G,H]||_F^2`.

Taking square roots proves the claim.

No smooth extension of `f` away from the finite spectrum is required. Only its values on `spec(H)` matter, so `L_H(f)` is the exact finite spectral slope relevant to this statement.

## 3. What the scalar filter can and cannot amplify

The inequality separates two resources that can otherwise be conflated.

The first is **orientation already present in the external operator**, measured here by `||[G,H]||_F`. If `H` commutes with `G`, every scalar function `f(H)` commutes with `G` as well, recovering the exact-commuting case of `VIS-372`.

The second is the **spectral gain of the scalar transform**, measured by `L_H(f)`. A nonlinear filter may amplify an existing off-diagonal block when two `H` eigenvalues are mapped far apart relative to their original spacing, but that amplification is explicitly paid for by the spectral slope. It does not create an off-diagonal block where `H` had none.

This distinction matters especially when `H` has a nearly degenerate spectrum. Even with bounded metric eigenvalues `m<=f(h_alpha)<=M`, `L_H(f)` can become large if `f` sharply separates very close `H` eigenvalues. Such a construction is not forbidden, but the apparent orientation gain then comes from a steep spectral selector rather than from free positive geometry and must be charged as part of the mechanism.

## 4. Composition with the Gram-cluster bound

Apply `VIS-374` to `C=f(H)`. For a chosen Gram clustering with inter-cluster separation `gamma` and within-cluster width `eta`, that result gives a positive exactly `G`-commuting control `C_*` satisfying

`|s_k(A_W C^(1/2))^2-s_k(A_W C_*^(1/2))^2|`
` <= ||G||_op sqrt(M/m) ||[G,C]||_F/gamma + 2M eta`.

Substituting the present commutator estimate yields

`|s_k(A_W C^(1/2))^2-s_k(A_W C_*^(1/2))^2|`
` <= ||G||_op sqrt(M/m) L_H(f) ||[G,H]||_F/gamma + 2M eta`.

The resulting accounting is useful because each escape term now has an explicit origin. A scalar functional-calculus metric can matter on the destination squared-singular-value scale only if at least one of the following remains substantial:

- the external operator itself has resolved Gram noncommutativity;
- the scalar spectral transform has a large discrete slope `L_H(f)`;
- the relevant Gram clusters retain non-negligible width `eta`;
- the positive metric bounds `m,M` degenerate enough to repay an otherwise small effect.

If none of these occurs, the metric is approximated spectrally by an exactly Gram-commuting positive preconditioner.

## 5. Prior-art audit

The functional-calculus ingredients are classical. The block formulas above are the finite-dimensional spectral-theorem specialization of the standard divided-difference/double-operator-integral framework for functions of self-adjoint or normal operators. Birman and Solomyak, **Double Operator Integrals in a Hilbert Space**, *Integral Equations and Operator Theory* 47 (2003), 131--168, DOI `10.1007/s00020-003-1157-8`, survey that framework and its perturbation-theoretic use.

Aleksandrov and Peller, **Operator and commutator moduli of continuity for normal operators**, *Proceedings of the London Mathematical Society* 105 (2012), 821--851, DOI `10.1112/plms/pds012`, study substantially broader operator- and commutator-Lipschitz estimates for functions of normal operators and quasicommutators. Rajendra Bhatia, *Matrix Analysis*, Graduate Texts in Mathematics 169, Springer (1997), DOI `10.1007/978-1-4612-0653-8`, provides the standard finite-dimensional spectral and unitarily invariant norm background used throughout the surrounding Wang controls.

No novelty is claimed for the spectral theorem, divided differences, Frobenius block orthogonality, commutator-Lipschitz functional calculus, or the inequality `||[G,f(H)]||_F<=L_H(f)||[G,H]||_F` in this finite-dimensional setting. The Mathia-specific contribution is the control interpretation after `VIS-372`--`VIS-374`: a scalar positive spectral transform of one external Hermitian structure inherits rather than creates the resolved Gram orientation needed to leave the Wang preconditioning class.

## Dependencies

- `VIS-370`: exactly Gram-commuting positive metrics are sectorwise spectral filters/preconditioners.
- `VIS-371`: coordinate-free positive metric rules built only from one Gram are forced into the commuting class.
- `VIS-372`: a commuting external Hermitian operator still provides only joint spectral filtering.
- `VIS-373`: arbitrary bounded positive near-commuting metrics are controlled by gap-normalized commutator size.
- `VIS-374`: orientation hidden inside a narrow near-degenerate Gram cluster is spectrally cheap.
- `CLUE-wang-fixed-source-packet-localization`: accepted Wang clue further narrowed by the present source-blind control.

## Research consequence

A future Wang proposal of the form `C=f(H)` should not be credited with a new positive-Hilbert mechanism merely because the nonlinear filter produces a visually or numerically different metric spectrum. It should report, at the relevant finite scale, the external noncommutativity `||[G,H]||_F`, the discrete transform slope `L_H(f)`, the Gram resolution scales `gamma,eta`, and the metric bounds `m,M`.

If the composed bound above is negligible on the destination squared-singular-value scale, the construction remains spectrally close to Gram-commuting preconditioning. A genuinely new source-free positive-Hilbert mechanism must therefore bring resolved orientation already through `H`, pay for a sharp spectral selector, or leave the single-operator scalar-functional-calculus class.