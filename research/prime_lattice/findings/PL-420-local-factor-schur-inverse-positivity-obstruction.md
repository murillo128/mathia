# PL-420 — Exact local-factor deletion is the nonpositive inverse of a completely positive Schur multiplier

**Evidence/status:** `EXACT-DERIVED + LITERATURE-CALIBRATED + DECISIVE-POSITIVITY-OBSTRUCTION` for positivity-preserving residue-matrix de-aliasing.

**Parent findings:** `PL-413`, `PL-415`, `PL-419`.

## Claim

`PL-419` shows that the positive residue-class pair-correlation readouts lose exactly the off-diagonal coherence required by the mod-5 source repair. A natural escape is to retain the **full** residue correlation matrix and apply the local Hardy--Littlewood factor deletion there, hoping that matrix positivity survives and can then feed a Hilbert-space or spectral argument.

It does not survive in general. On the reduced residue group

\[
U_p=(\mathbb Z/p\mathbb Z)^\times,
\]

let `B_p` be the matrix of the ordinary prime-pair local factor

\[
(B_p)_{ab}=\beta_p(b-a),
\qquad a,b\in U_p,
\tag{1}
\]

and let `G_p` be its **entrywise** reciprocal,

\[
(G_p)_{ab}=g_p(b-a)=\beta_p(b-a)^{-1}.
\tag{2}
\]

Because the local factor only distinguishes `a=b` from `a\ne b`, the same kernel may equivalently be written as `g_p(a/b)` on `U_p`. The exact deletion of the `p`-factor on a residue-pair matrix `R` is therefore the Schur/Hadamard multiplier

\[
\boxed{\Phi_{g_p}(R)=G_p\circ R.}
\tag{3}
\]

The ordinary local-factor multiplier `Phi_{beta_p}(R)=B_p\circ R` is completely positive, but its exact linear inverse `Phi_{g_p}` is **not even positive** for every odd prime `p`. Equivalently,

\[
\boxed{
\Phi_{g_p}=\Phi_{\beta_p}^{-1}
\quad\text{as entrywise multipliers, but}\quad
\Phi_{g_p}(R)\not\ge0\text{ for some }R\ge0.
}
\tag{4}
\]

For the live `p=5` repair, the obstruction is precisely the signature already exposed in `PL-415`--`PL-419`: `G_5` has one positive eigenvalue and three negative ones. Thus **keeping the full cross-residue matrix does not restore a positivity-preserving exact de-aliasing map**. Any successful positive operator route must either use additional arithmetic constraints restricting the allowed residue matrices, encode the local division by a different non-Schur construction, or abandon ordinary positivity/complete positivity at this step.

This is stronger than the scalar blindness of `PL-419`. There the problem was that four positive diagonal residue readouts did not determine the signed supertrace. Here even if the complete residue matrix is retained, applying the exact inverse local factor is not a positive map on the ambient covariance cone.

## 1. The ordinary local factor is a positive Schur symbol

For an odd prime `p`, the Hardy--Littlewood pair local factor is

\[
\beta_p(h)
=\frac{1-\nu_p(h)/p}{(1-1/p)^2},
\qquad
\nu_p(h)=
\begin{cases}
1,&p\mid h,\\
2,&p\nmid h.
\end{cases}
\tag{5}
\]

Hence on reduced residues

\[
(B_p)_{ab}
=
\begin{cases}
\displaystyle \frac{p}{p-1},&a=b,\\[6pt]
\displaystyle \frac{p(p-2)}{(p-1)^2},&a\ne b.
\end{cases}
\tag{6}
\]

Write `n=p-1`. Since a matrix with diagonal `d` and constant off-diagonal `c` has one eigenvalue `d+(n-1)c` on the constant vector and eigenvalue `d-c` on its orthogonal complement, (6) gives

\[
\lambda_{\mathbf 1}(B_p)
=
\frac{p\,(p^2-3p+3)}{(p-1)^2}>0,
\tag{7}
\]

and

\[
\lambda_{\perp}(B_p)
=
\frac{p}{(p-1)^2}>0
\tag{8}
\]

with multiplicity `p-2`. Therefore

\[
\boxed{B_p>0.}
\tag{9}
\]

The finite-dimensional Schur product theorem then makes

\[
R\mapsto B_p\circ R
\tag{10}
\]

a positive, in fact completely positive, map on `M_{p-1}(C)`. This can also be checked directly: if `B_p=sum_j v_jv_j^*`, then

\[
B_p\circ R
=
\sum_j \operatorname{diag}(v_j)\,R\,\operatorname{diag}(v_j)^*.
\tag{11}
\]

No arithmetic hypothesis is involved in this positivity.

## 2. Entrywise deletion flips every nontrivial Fourier mode negative

The inverse local factor from `PL-415` is

\[
g_p(h)=\beta_p(h)^{-1}
=
\begin{cases}
\displaystyle \frac{p-1}{p},&p\mid h,\\[6pt]
\displaystyle \frac{(p-1)^2}{p(p-2)},&p\nmid h.
\end{cases}
\tag{12}
\]

Thus

\[
(G_p)_{ab}
=
\begin{cases}
\displaystyle \frac{p-1}{p},&a=b,\\[6pt]
\displaystyle \frac{(p-1)^2}{p(p-2)},&a\ne b.
\end{cases}
\tag{13}
\]

and the same two-eigenvalue calculation gives

\[
\boxed{
\lambda_{\mathbf 1}(G_p)=p-1,
\qquad
\lambda_{\perp}(G_p)
=-\frac{p-1}{p(p-2)}
}
\tag{14}
\]

with the second eigenvalue of multiplicity `p-2`. Hence

\[
\boxed{\operatorname{inertia}(G_p)=(1,p-2,0).}
\tag{15}
\]

This is exactly the multiplicative-character decomposition already found in `PL-415`: the trivial character has positive coefficient, while every nontrivial character has coefficient `-1/[p(p-2)]`. The matrix statement simply makes the positivity consequence explicit.

A Schur multiplier `R -> A circ R` can be positive only if its symbol `A` is positive semidefinite: apply the map to the rank-one positive matrix `11^*`. Therefore (15) gives the direct witness

\[
\boxed{
\Phi_{g_p}(\mathbf 1\mathbf 1^*)=G_p\not\ge0.
}
\tag{16}
\]

So `Phi_{g_p}` is not positive and therefore cannot be completely positive. The obstruction already occurs on a rank-one PSD input with strictly nonnegative entries; it is not caused by exotic complex phases.

For `p=5`,

\[
G_5=
\begin{pmatrix}
4/5&16/15&16/15&16/15\\
16/15&4/5&16/15&16/15\\
16/15&16/15&4/5&16/15\\
16/15&16/15&16/15&4/5
\end{pmatrix},
\tag{17}
\]

with spectrum

\[
\boxed{\{4,-4/15,-4/15,-4/15\}.}
\tag{18}
\]

Multiplying by `15/4` recovers exactly the residue-basis metric from `PL-419`,

\[
\frac{15}{4}G_5=4\mathbf1\mathbf1^*-I,
\tag{19}
\]

whose character-basis form is `D=diag(15,-1,-1,-1)`.

## 3. The exact repair is the inverse of a CP map, not a positive order inverse

Every entry of `B_p` is nonzero and `G_p` is its pointwise reciprocal. Consequently, for every matrix `R`,

\[
\Phi_{g_p}(\Phi_{\beta_p}(R))
=
(G_p\circ B_p)\circ R
=R,
\tag{20}
\]

and likewise in the opposite order. Thus the local deletion is genuinely the **linear inverse** of the ordinary local-factor Schur multiplier.

The distinction from an ordinary matrix inverse is essential:

\[
G_p\ne B_p^{-1}\quad\text{in general};
\tag{21}
\]

rather, `Phi_{g_p}=Phi_{beta_p}^{-1}` because the superoperators act entrywise. A completely positive invertible linear map need not have a positive inverse, and (14)--(16) show that this one does not.

This gives a precise operator-theoretic meaning to the sign change introduced by the endpoint repair. The original local Hardy--Littlewood factor can be inserted without leaving the positive covariance cone. **Dividing it back out is an order-destroying operation on the full ambient matrix cone.** The negative nonprincipal coefficients of `PL-415` are therefore not merely an inconvenient basis choice; they are the Fourier signature of a failure of positivity of the exact deconvolution map itself.

## 4. Relation to the live mod-5 source target

`PL-419` left one formal escape from the failure of the scalar positive residue aggregates `F_5(a)`: retain the full residue matrix `R`, including all off-diagonal coherences. Equation (3) shows what the exact `p=5` source repair then does to that matrix. Equation (18) shows that there is no general theorem of the form

\[
R\ge0
\Longrightarrow
G_5\circ R\ge0.
\tag{22}
\]

Indeed the implication fails for `R=11^*`.

This does **not** mean that the repaired scalar prime-pair observable is negative. The entries of `G_5` are positive numbers, and the original lag-side quantity `g_5(h)C_X(h)` remains a positive reweighting of nonnegative raw pair counts. Matrix positivity and entrywise positivity are different notions. The no-go is specifically against transporting a PSD/Gram interpretation through the exact residue-matrix de-aliasing step.

Nor does (22) rule out positivity on a smaller arithmetic cone. If actual prime residue-correlation matrices satisfy additional inequalities strong enough to force

\[
G_5\circ R_{\rm arith}\ge0,
\tag{23}
\]

that would be genuine arithmetic input absent from the finite-group algebra. Such a theorem would be precisely the kind of extra rigidity that `PL-419` identified as missing. What is ruled out is obtaining it for free from Schur positivity, character orthogonality, or the fact that the unrepaired covariance matrix is PSD.

## 5. Prior-art / novelty audit

The operator-theory ingredient is classical. The Schur product theorem says that the entrywise product of positive semidefinite matrices is positive semidefinite; in finite dimensions a Schur map `X -> A circ X` is completely positive exactly when its symbol `A` is positive semidefinite. A modern positivity reference is N. M. Steen, I. G. Todorov and L. Turowska, “Local operator multipliers and positivity,” *Journal of Functional Analysis* **267** (2014), 80--111, DOI `10.1016/j.jfa.2014.04.007`. The finite-dimensional implication needed here is also proved directly in (11) and (16), so no deep operator-algebra theorem is being imported.

The arithmetic input is likewise not new: the two values of `beta_p`, the inverse values `g_p`, and the character decomposition are the standard Hardy--Littlewood local-density algebra already audited in `PL-414`--`PL-415`. Targeted searches around inverse singular-series factors, Schur multipliers, and positivity did not locate an established claim identifying this exact local prime-pair deletion as a nonpositive inverse Schur map.

The safe novelty claim is therefore only the **line-specific synthesis/no-go**: when the exact `PL-413` local-factor deletion is lifted from scalar lags to the full residue covariance matrix suggested by `PL-419`, the unique entrywise de-aliasing map is the inverse of a CP Schur multiplier but is itself nonpositive, with signature `(1,p-2)` for every odd prime. No novelty is claimed for the Schur theorem or the local-factor formulas separately.

## 6. Adversarial audit

1. **This is an ambient-cone obstruction, not an arithmetic impossibility theorem.** The witness `11^*` proves failure on the full PSD cone. Actual prime correlation matrices may occupy a special subcone. Any claim that they do must be proved arithmetically rather than inferred from generic positivity.

2. **Scalar positivity survives.** Since every entry of `G_p` is positive, multiplying nonnegative raw pair counts by `g_p` preserves their scalar sign. The result concerns positive-semidefinite matrix structure, not positivity of the original Hardy--Littlewood weighted count.

3. **Hadamard inverse is not matrix inverse.** The exact source deletion is entrywise division by the local factor. Confusing `G_p` with `B_p^{-1}` would invalidate the conclusion. Equation (20) is an identity of Schur-multiplier superoperators.

4. **Complete positivity is stronger than required by RH.** A valid zero-localization mechanism may be indefinite, Krein-space-valued, or target-relative. This finding only closes the shortcut in which exact local de-aliasing is supposed to preserve an ordinary PSD/Gram structure automatically.

5. **The reduced-residue restriction is deliberate.** Terms involving multiples of `p` are the prime-power exceptional set already isolated in `PL-414`; they do not alter the finite unit-group signature calculation that controls the local repair.

6. **No continuation claim is involved.** Everything here is finite-dimensional algebra on the local residue space. The result neither proves nor assumes RH/GRH and does not transport an Euler-product identity into the critical strip.

## Consequence for the line

After `PL-419`, “keep the full cross-residue matrix” remains necessary for fidelity, but it is **not sufficient for positivity**. The exact inverse local factor acts by a Schur multiplier whose nontrivial character eigenvalues are negative. Therefore the route

\[
\text{PSD residue covariance}
\longrightarrow
\text{exact }p=5\text{ de-aliasing}
\longrightarrow
\text{PSD repaired covariance}
\longrightarrow
\text{positive spectral localization}
\]

fails at the middle arrow before any zeta-zero input is used.

The surviving target is narrower. A positive operator mechanism would need to prove a genuinely arithmetic restricted-cone statement such as (23), implement the local deletion in a larger structure where the signed character modes are controlled by additional data, or work with an explicitly indefinite formalism and supply a separate divisor-sensitive theorem. Merely restoring the off-diagonal coherences that `PL-419` found missing cannot, by itself, recover a positivity-based RH mechanism.