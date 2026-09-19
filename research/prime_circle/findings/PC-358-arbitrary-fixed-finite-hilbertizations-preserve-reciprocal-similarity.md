# PC-358 — arbitrary fixed finite Hilbertizations preserve reciprocal similarity

- **Finding ID:** `PC-358`
- **Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` + `DECISIVE-BOUNDARY`
- **Research line:** `prime_circle`
- **Result type:** exact finite-dimensional Hilbert-metric / operator-theoretic obstruction
- **Scope:** closes the non-tensor, word-dependent, shell-dependent, and cross-degree finite-Hilbert-metric escape left outside PC-357; also identifies the exact bounded-parity condition under which an infinite completion remains spectrally control-blind
- **RH relevance:** high as a boundary result: no fixed positive metric on a finite Prime-Circle signature truncation can break the reciprocal matched-control similarity, regardless of how strongly that metric couples words, shells, or tensor degrees. Metric-sensitive quantities can separate, but only inside a static similarity-distortion budget. An infinite-depth metric-only repair must therefore make the algebraic reciprocal parity genuinely unbounded or alter the operator/domain/control law itself.

## Claim

PC-357 treats a fixed common one-particle metric `H` and its tensor powers. It deliberately leaves arbitrary nonfactorizing Hilbert structures outside its theorem: a metric could couple different words, different shells, and even different tensor degrees instead of arising from one tensor-product form.

That extra freedom does not help at any finite cutoff.

Let

\[
V_N:=\bigoplus_{m=0}^{N}K_S^{\otimes m}
\]

be the finite centered Prime-Circle word space from PC-355--PC-357, and let

\[
P_N:=\Gamma_N(J)=\bigoplus_{m=0}^{N}J^{\otimes m},
\qquad P_N^2=I.
\]

For the cyclotomic inversion defect and its matched reciprocal control, the algebraic left multipliers satisfy

\[
\boxed{
\widetilde L_N=P_NL_NP_N.
}
\tag{1}
\]

Now equip `V_N` with **any** positive-definite Hermitian form

\[
\langle x,y\rangle_{G_N}=x^*G_Ny,
\qquad G_N>0,
\]

with no grading, tensor-product, shell-diagonal, word-diagonal, or parity assumption. The same `G_N` is used for source and control because the question is whether one independently fixed ambient Hilbert geometry can distinguish them.

Let `R_N=G_N^{1/2}` and represent both operators in Euclidean coordinates:

\[
A_N=R_NL_NR_N^{-1},
\qquad
\widetilde A_N=R_N\widetilde L_NR_N^{-1}.
\]

Define

\[
S_N:=R_NP_NR_N^{-1}.
\]

Then `S_N^2=I` and, without any factorization assumption on the metric,

\[
\boxed{
\widetilde A_N=S_NA_NS_N^{-1}.
}
\tag{2}
\]

Thus every fixed positive finite-dimensional Hilbertization leaves source and matched control exactly similar. In particular they have the same characteristic polynomial, Jordan form, minimal polynomial, algebraic multiplicities, and rational functional-calculus spectrum. Since the finite left multiplier is still algebraically identity plus a nilpotent degree-raising map,

\[
\boxed{
\operatorname{Spec}A_N
=
\operatorname{Spec}\widetilde A_N
=
\{1\}.
}
\tag{3}
\]

The metric can still change singular values, resolvent norms, and pseudospectra because `S_N` need not be unitary. But all such separation is bounded by one global parity/metric mismatch,

\[
\boxed{
\Delta_N(G_N,J)
:=\kappa_2(S_N)
=\|P_N\|_{G_N}^{\,2}
\ge1.
}
\tag{4}
\]

For every singular value,

\[
\boxed{
\Delta_N^{-1}\sigma_k(A_N)
\le
\sigma_k(\widetilde A_N)
\le
\Delta_N\sigma_k(A_N),
}
\tag{5}
\]

and for every `z` outside the common spectrum,

\[
\boxed{
\Delta_N^{-1}
\|(zI-A_N)^{-1}\|_2
\le
\|(zI-\widetilde A_N)^{-1}\|_2
\le
\Delta_N
\|(zI-A_N)^{-1}\|_2.
}
\tag{6}
\]

Hence the corresponding epsilon-pseudospectra differ by at most the same rescaling of `epsilon`.

This strictly extends PC-357 at finite depth. The tensor-product metric there gives the special law `Delta_N=kappa_H(J)^N`; here `G_N` may be completely nonfactorizing, and the entire effect is still compressed into the single condition number (4).

At infinite depth there is also an exact boundary. Let `H_G` be any Hilbert completion of the algebraic word space on which the algebraic parity `P=Gamma(J)` extends to a bounded operator. Since `P^2=I` on the dense algebraic subspace, its bounded extension is automatically boundedly invertible with inverse `P`. If the source and control multipliers extend boundedly and (1) holds on the dense algebraic subspace, then

\[
\boxed{\widetilde L=PLP}
\tag{7}
\]

as bounded operators on `H_G`; therefore their Banach-space spectra are identical. Consequently a fixed-completion ordinary-spectrum repair is possible only beyond this bounded-parity regime: parity must fail to extend boundedly, or the domain/operator/control law must itself cease to be transported by parity. Unboundedness is only a necessary opening, not a positive RH mechanism.

## 1. The finite theorem is independent of how the metric is assembled

The PC-355 control law is algebraic. Before any Hilbert structure is chosen, the centered reciprocal twin acts letterwise by

\[
Jc=c,
\qquad
Jb_n=-b_n,
\]

and the induced tensor automorphism gives (1). This identity lives on the finite vector space `V_N`; it does not refer to adjoints, orthogonality, word lengths, or a tensor-product norm.

Every positive Hermitian form on a finite-dimensional complex vector space is obtained from the Euclidean form by one invertible whitening map `R_N=G_N^{1/2}`. Conjugating (1) by `R_N` gives

\[
\begin{aligned}
\widetilde A_N
&=R_NP_NL_NP_NR_N^{-1}\\
&=(R_NP_NR_N^{-1})
(R_NL_NR_N^{-1})
(R_NP_NR_N^{-1})\\
&=S_NA_NS_N.
\end{aligned}
\]

Because `P_N^2=I`, also `S_N^2=I`, so the final factor is `S_N^{-1}` as in (2).

Nothing in this argument requires `G_N` to preserve tensor degree. It may contain arbitrary positive cross terms between degrees, shells, and words. Such couplings can radically alter the Hilbert adjoint and nonnormal geometry of the multiplier, but they do not alter the underlying similarity class of the linear map.

The raw spectrum remains especially degenerate for an independent reason. Algebraically,

\[
L_N=I+Q_N,
\]

where `Q_N` strictly raises tensor degree before the degree-`N` quotient is taken. Therefore `Q_N^{N+1}=0`. A change of inner product cannot change that polynomial identity, so

\[
(A_N-I)^{N+1}=0
\]

and the same for the control. Equation (3) follows without any metric assumption beyond positive definiteness.

## 2. Arbitrary metric-sensitive separation has one global distortion budget

The induced operator norm of parity in the `G_N` metric is

\[
\|P_N\|_{G_N}
=
\|G_N^{1/2}P_NG_N^{-1/2}\|_2
=
\|S_N\|_2.
\]

Since `S_N^{-1}=S_N`,

\[
\kappa_2(S_N)
=\|S_N\|_2\|S_N^{-1}\|_2
=\|S_N\|_2^2
=\|P_N\|_{G_N}^2,
\]

which proves (4).

For any matrices `X,A,Y`, singular values satisfy

\[
\sigma_k(XAY)
\le
\|X\|_2\|Y\|_2\sigma_k(A).
\]

Applying this to `S_NA_NS_N^{-1}` gives the upper bound in (5), and applying the same inequality to the inverse similarity

\[
A_N=S_N^{-1}\widetilde A_NS_N
\]

gives the lower bound. The resolvent identity

\[
(zI-\widetilde A_N)^{-1}
=S_N(zI-A_N)^{-1}S_N^{-1}
\]

proves (6) in exactly the same way.

Thus an arbitrarily complicated finite Hilbert geometry cannot create an uncontrolled spectral effect. It can create large unitary-sensitive effects only by making the already-known reciprocal involution badly conditioned in that metric.

The usual resolvent definition of pseudospectrum then yields

\[
\Lambda_\epsilon(\widetilde A_N)
\subseteq
\Lambda_{\Delta_N\epsilon}(A_N),
\qquad
\Lambda_\epsilon(A_N)
\subseteq
\Lambda_{\Delta_N\epsilon}(\widetilde A_N).
\tag{8}
\]

This does not say that the bounds are attained, only that metric-sensitive source/control separation cannot outrun the common similarity distortion.

## 3. Large distortion can be manufactured without arithmetic

A two-dimensional even/odd toy already shows why the size of `Delta_N` is not itself arithmetic evidence. Let

\[
P=\begin{pmatrix}1&0\\0&-1\end{pmatrix}
\]

and choose the positive metric

\[
G_t=
\begin{pmatrix}
1&t\\
t&1
\end{pmatrix},
\qquad 0<t<1.
\]

This is the minimal possible model of a fixed Hilbert form coupling one parity-even and one parity-odd direction. Direct generalized-eigenvalue calculation gives

\[
\boxed{
\|P\|_{G_t}^2
=
\Delta(G_t,P)
=
\frac{1+t}{1-t}.
}
\tag{9}
\]

Hence the similarity-distortion budget diverges as `t -> 1^-`, despite this example containing no primes, roots of unity, cyclotomic polynomial, zeta function, or arithmetic input at all.

This is the appropriate matched-control warning for experiments with a complicated roots-of-unity metric. A large singular-value or pseudospectral gap may still be mathematically interesting, but its magnitude is not evidence of a zeta-selective mechanism until it is normalized against `Delta_N` and shown to use a source-specific relation between the metric and the actual cyclotomic defect that an admissible non-arithmetic reciprocal control does not share.

PC-357's exponential law is one structured instance of the same phenomenon. If

\[
G_N=
\bigoplus_{m=0}^{N}w_mH^{\otimes m},
\]

then

\[
S_N
=
\bigoplus_{m=0}^{N}
(H^{1/2}JH^{-1/2})^{\otimes m}
\]

and (4) reduces exactly to

\[
\Delta_N=\kappa_H(J)^N.
\]

The exponential growth there is therefore not a special property of the tensor metric; it is the explicit factorized value of the general distortion budget.

## 4. The infinite-depth boundary is bounded parity, not tensor factorization

Finite-dimensional equivalence of norms makes (2) unavoidable. Infinite depth is different only because the algebraic parity may cease to define a bounded operator in the chosen completion.

Let `V_alg` be the algebraic finite-word space and suppose a Hilbert norm completes it to `H_G`. Assume `P` is bounded on the dense subspace `V_alg` in that norm. It extends uniquely to a bounded operator on `H_G`; because `P^2=I` algebraically, continuity gives `P^2=I` on the completion. Thus `P` is automatically boundedly invertible.

If bounded operators `L` and `\widetilde L` extend the source and control left multipliers and satisfy

\[
\widetilde Lx=PLPx
\]

for every algebraic word vector `x`, density and boundedness extend the identity to all of `H_G`. Standard bounded similarity then gives

\[
\operatorname{Spec}\widetilde L
=
\operatorname{Spec}L
\]

and the same resolvent relation as above with the global condition number of `P`.

Therefore an infinite nonfactorizing Hilbert completion does not escape merely because it is nonfactorizing. It escapes this no-go only if at least one of the load-bearing bounded-similarity hypotheses fails. The most direct metric-only failure is

\[
\sup_{x\in V_{alg}\setminus\{0\}}
\frac{\|Px\|_G}{\|x\|_G}
=\infty.
\tag{10}
\]

PC-357 already supplies a concrete route to (10): for a fixed one-particle metric with `kappa_H(J)>1`, the norms of the tensor powers grow exponentially, so the canonical parity cannot remain bounded on the undamped full tensor tower. But (10) is not yet positive evidence. Once the intertwiner is unbounded, spectra may become domain-sensitive; one must still prove that the proposed completion and operator domains are forced by the Prime-Circle geometry, that both source and matched control define legitimate closed/bounded operators, and that any spectral difference survives a non-arithmetic control and carries an independently derived zeta-zero relation.

This isolates the genuine remaining topology/domain question much more sharply than the phrase “non-tensor Hilbert structure.”

## 5. What finite anchored or cross-word metrics can and cannot do

The common anchored vertex, angular chord geometry, or another intrinsic finite roots-of-unity construction could certainly induce a dense metric matrix on a finite word space. It might mix calibration and transverse directions, couple different shell labels, or correlate different Chen degrees. PC-358 does not deny the geometric content of such a matrix.

It says that **metric choice alone cannot change the algebraic reciprocal similarity class at finite depth**. If the operator remains the same truncated left multiplier and the matched control remains `theta_J(D)`, every common positive metric is absorbed into the whitening map `R_N`. Ordinary spectra and Jordan data are therefore unavailable as selectors. Singular or pseudospectral data can react to the metric, but the generic reaction must first be divided conceptually by the distortion already present in `Delta_N`.

Accordingly, a viable finite-dimensional repair must alter more than the Hilbert form. Examples genuinely outside the theorem include a source-forced operator or algebraic coupling that does not obey (1), a quotient/domain not transported by `P_N`, a boundary condition that changes the admissible state space rather than only its norm, or a joint invariant whose arithmetic content is proved to exceed the static similarity mismatch. The theorem does not prejudge whether such a construction exists.

## Prior-art and novelty audit

The abstract linear algebra is classical. Changing a positive-definite inner product to Euclidean coordinates by `G^{1/2}` is a similarity transform, and spectra are similarity invariants. Resolvent and pseudospectral sensitivity under nonunitary similarity is standard matrix analysis; Trefethen--Embree pseudospectral theory gives the conventional surrounding framework, and standard weighted-inner-product treatments express the same norm change through a similarity. No novelty is claimed for these facts.

The prior-art check therefore falsifies any attempt to advertise the metric theorem itself as a new operator-theoretic mechanism. The line-local contribution is narrower: PC-357 had established the exact Prime-Circle reciprocal similarity only for tensor-product Hilbertizations and explicitly left nonfactorizing word/shell/degree metrics outside its scope. Equations (1)--(10) remove that factorization hypothesis completely at finite cutoff and identify bounded extension of the same algebraic parity as the exact infinite-completion boundary.

No external theorem beyond standard finite-dimensional similarity/norm inequalities and the bounded-inverse consequence of `P^2=I` is load-bearing, so no new `SOURCES.md` dependency is required.

## Falsification / disproof audit

- **Metric generality:** `G_N` is an arbitrary positive-definite Hermitian matrix on the whole finite word space; it may mix tensor degrees, words, shell labels, calibration/transverse directions, and parity sectors.
- **Common-metric requirement:** source and control must use the same independently fixed `G_N`. If the metric is recomputed from each radial source, PC-356 applies instead. If source information is frozen into the control metric without independent geometric justification, the comparison is not a matched control.
- **Algebraic-control requirement:** the theorem assumes the exact PC-355 law `\widetilde L_N=P_NL_NP_N`. Changing the operator, quotient, domain, or coupling so this law fails is outside the theorem.
- **Positivity requirement:** `G_N>0` so whitening is invertible. A degenerate form whose nullspace is not parity-invariant can change the quotient state space and belongs to the domain/quotient boundary rather than this theorem.
- **Spectrum check:** similarity preserves characteristic polynomial, Jordan form, minimal polynomial, and ordinary spectrum. The additional `{1}` collapse follows independently from finite degree-raising nilpotence.
- **Singular-value check:** (5) follows from the standard product inequality applied in both directions; equality is not asserted.
- **Pseudospectrum check:** (6) is the exact resolvent similarity followed by norm submultiplicativity; (8) is only the resulting two-sided inclusion after epsilon rescaling.
- **Control check:** the two-dimensional metric example (9) produces arbitrarily large distortion without arithmetic, so distortion size by itself cannot certify Prime-Circle specificity.
- **Infinite-depth check:** bounded extension of parity is sufficient for exact bounded similarity. Failure of boundedness is only an opening; the theorem does not claim that unbounded parity automatically creates different spectra or any RH information.
- **Operator-domain check:** unbounded multipliers, non-parity-related closed domains, source-forced boundary conditions, and state-space changes require separate analysis.
- **RH check:** no complex zeta spectral parameter, completed-zeta functional equation, zero equation, positivity statement, or critical-line selector is produced.

## Boundary assessment

PC-356 showed that a Hilbert metric derived covariantly from the radial source is transported by the reciprocal control and restores exact isometry. PC-357 showed that freezing an independently justified **tensor-product** metric can break unitarity but only produces nonunitary similarity distortion. PC-358 removes the remaining finite factorization loophole: **every fixed positive Hilbert metric on the entire finite word space, however nonlocal or nonfactorizing, still leaves the source and reciprocal control exactly similar.**

The meaningful infinite-depth frontier is therefore no longer “try a more complicated Hilbert metric.” It is narrower: derive a Prime-Circle completion or operator domain for which the reciprocal parity is genuinely unbounded or inapplicable, or derive a source-forced operator/boundary coupling that changes the algebraic control law itself. Either route must then survive the line's non-arithmetic matched controls and acquire an independently forced connection to zeta zeros rather than merely a large norm or pseudospectral effect.