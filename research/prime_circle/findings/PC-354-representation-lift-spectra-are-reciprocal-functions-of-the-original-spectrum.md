# PC-354 — finite representation-lift spectra are only reciprocal functions of the original spectrum

- **Finding ID:** `PC-354`
- **Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED`
- **Status detail:** `DECISIVE-NEGATIVE` for finite-dimensional algebraic representation lifts as a repair of the outer-parity spectral quotient in PC-353
- **Workflow:** `DERIVED + PRIOR-ART AUDIT + ADVERSARIAL CONTROL`
- **Research line:** `prime_circle`
- **Result type:** exact representation-theoretic no-go
- **Prime dependence:** none in the target-space theorem; the same statement holds for every matched reciprocal control satisfying the PC-353 outer-parity law
- **RH relevance:** high as a boundary result: exterior powers, tensor powers, symmetric powers, highest-weight representations, and finite collections of their spectra cannot turn the contragredient orientation of PC-353 into a source-specific or zero-selecting spectral mechanism

## Claim

PC-353 leaves one very natural representation-theoretic repair to test. Starting from an outer-parity development

\[
\widetilde D=D^{-\mathsf T}\in SL_d(\mathbb C),
\qquad d\ge3,
\]

one might pass to a nontrivial finite-dimensional representation

\[
\rho:SL_d(\mathbb C)\longrightarrow GL(V)
\]

before taking spectra, hoping that exterior powers, tensor powers, symmetric powers, or a higher highest-weight representation expose information invisible in the standard characteristic polynomial.

They cannot. For every finite-dimensional algebraic representation `rho`, the spectrum of `rho(D)` is already a fixed weight-monomial function of the ordinary eigenvalue multiset of `D`. Moreover

\[
\boxed{
\operatorname{Spec}\rho(\widetilde D)
=
\operatorname{Spec}\rho(D)^{-1}
}
\]

with algebraic multiplicity. Since `SL_d(C)` has no nontrivial determinant character,

\[
\det\rho(D)=1,
\]

and if `m=dim V` then

\[
\boxed{
\chi_{\rho(\widetilde D)}(z)
=(-1)^m z^m\chi_{\rho(D)}(z^{-1}).
}
\]

Thus a representation lift has only the same two possibilities already identified in PC-353:

- a self-dual representation has reciprocal-symmetric spectrum and is control-blind;
- a non-self-dual representation can retain an orientation between a representation and its contragredient, but that orientation is forced for every admissible non-arithmetic matched control as well.

In particular, **finite-dimensional representation spectralization cannot add a new arithmetic channel after the standard `SL_d` spectrum has been formed.** It only applies classical weight/contragredient functoriality to data that PC-353 already reduced to reciprocal duality.

## 1. Representation spectra are determined by the ordinary eigenvalues of the development

Let the eigenvalues of `D` be

\[
\lambda_1,\ldots,\lambda_d,
\qquad
\lambda_1\cdots\lambda_d=1,
\]

counted with algebraic multiplicity. Write the multiplicative Jordan decomposition

\[
D=D_sD_u=D_uD_s,
\]

with `D_s` semisimple and `D_u` unipotent. Algebraic representations preserve Jordan decomposition, so

\[
\rho(D)=\rho(D_s)\rho(D_u),
\]

where `rho(D_s)` is semisimple, `rho(D_u)` is unipotent, and the two commute. Consequently the eigenvalues of `rho(D)` are exactly those of `rho(D_s)`; the unipotent factor can alter Jordan blocks but cannot create a new spectral value.

After conjugating `D_s` into the diagonal torus, every weight `mu=(mu_1,...,mu_d)` of `rho` contributes the eigenvalue

\[
\lambda^\mu
:=
\lambda_1^{\mu_1}\cdots\lambda_d^{\mu_d}
\]

with the multiplicity of that weight. Therefore

\[
\boxed{
\operatorname{Spec}\rho(D)
=
\{\lambda^\mu:\mu\in\operatorname{Wt}(\rho)\}
}
\]

as a multiset.

This is already a strong no-go. Once the ordinary spectrum of `D` has been taken, no fixed finite-dimensional algebraic representation can recover any radial/Chen information that was lost by that quotient. Its spectrum is a deterministic algebraic transform of the same eigenvalue multiset. Exterior, symmetric, and tensor powers merely choose different fixed weight multisets.

## 2. Outer parity remains exact contragredient reciprocity in every representation

PC-353 gives

\[
\widetilde D=D^{-\mathsf T}.
\]

The matrices `D^{-1}` and `D^{-T}` are similar over `C`: every square matrix is similar to its transpose. If `P in GL_d(C)` conjugates one to the other, rescaling `P` by a scalar does not change the conjugation and can make `det P=1`. Hence they are conjugate already inside `SL_d(C)`. Applying `rho` gives

\[
\boxed{
\rho(\widetilde D)
\sim
\rho(D^{-1})
=
\rho(D)^{-1}.
}
\]

The spectral reciprocity follows immediately.

For completeness, `det o rho` is a one-dimensional character of `SL_d(C)`. Since `SL_d(C)` is perfect (equivalently, a connected semisimple algebraic group has no nontrivial algebraic characters), this character is trivial. Thus `det rho(D)=1`, and

\[
\begin{aligned}
\chi_{\rho(\widetilde D)}(z)
&=\det(zI-\rho(D)^{-1})\\
&=(-1)^m z^m\chi_{\rho(D)}(z^{-1}).
\end{aligned}
\]

Likewise, for every positive integer `k`,

\[
\boxed{
\operatorname{tr}\rho(\widetilde D)^k
=
\operatorname{tr}\rho(D)^{-k}.
}
\]

Newton identities therefore show that using traces of powers, characteristic coefficients, spectral determinants, or any finite algebraic combination of them does not open another channel.

## 3. Fundamental exterior powers reproduce exactly the coefficient reversal of PC-353

The result is particularly transparent for the fundamental type-`A` representations

\[
\rho_k=\Lambda^k\mathbb C^d,
\qquad 1\le k\le d-1.
\]

Their characters are the elementary symmetric functions

\[
\operatorname{tr}(\Lambda^kD)=e_k(\lambda_1,\ldots,\lambda_d).
\]

Because `prod_i lambda_i=1`, inversion gives

\[
e_k(\lambda_1^{-1},\ldots,\lambda_d^{-1})
=e_{d-k}(\lambda_1,\ldots,\lambda_d).
\]

Hence the outer-parity control acts exactly by

\[
\boxed{
\operatorname{tr}(\Lambda^k\widetilde D)
=
\operatorname{tr}(\Lambda^{d-k}D).
}
\]

These are precisely the complementary characteristic-polynomial coefficients already exchanged in PC-353. Passing to all fundamental representations therefore does not refine the standard spectral quotient at all; it simply repackages its coefficients.

More generally, an irreducible finite-dimensional representation with highest weight `lambda` has dual highest weight

\[
\lambda^*=-w_0\lambda.
\]

For type `A_{d-1}` this reverses the Dynkin labels. Equivalently,

\[
\chi_\lambda(\widetilde D)
=
\chi_{\lambda^*}(D).
\]

If `lambda=lambda^*`, the representation is self-dual and its entire spectral multiset is reciprocal-symmetric, so the matched control has the same spectrum. If `lambda != lambda^*`, the representation merely records which member of the classical contragredient pair is being viewed. No source-specific arithmetic enters this dichotomy.

Since irreducible type-`A` characters are Schur functions of the ordinary eigenvalues, and hence symmetric polynomials generated by the elementary symmetric functions, no higher highest-weight character can escape the same coefficient data.

## 4. The matched-control test is fatal to an arithmetic interpretation

The proof above never used cyclotomic coefficients, primitive shells, prime powers, Ramanujan sums, or zeta. Its only source-side input is the exact outer-parity relation from PC-353,

\[
\widetilde D=D^{-\mathsf T},
\]

which holds equally for every admissible reciprocal control profile in that construction.

Therefore any spectral asymmetry found after applying a fixed representation `rho` is reproduced by a non-arithmetic control with the same parity law. Self-dual representations erase that orientation; non-self-dual representations preserve it as ordinary contragredient orientation. Neither outcome can certify prime support, a Riemann zero, a gamma factor, a critical line, or an `s <-> 1-s` functional equation.

This rules out a broad but natural family of repairs:

\[
D
\longmapsto
\rho(D)
\longmapsto
\text{finite-dimensional spectrum/character}
\]

for every fixed algebraic representation `rho`, including finite direct sums, tensor products, exterior powers, symmetric powers, and irreducible highest-weight representations.

## Prior-art audit

No novelty is claimed for any representation-theoretic ingredient. The contragredient representation is classical: for a representation `rho`, the dual action is `rho^*(g)=rho(g^{-1})^T`, and the dual highest weight is `-w_0 lambda`. In type `A`, this is the nontrivial Dynkin-diagram reversal. Standard references include William Fulton and Joe Harris, *Representation Theory: A First Course*, Graduate Texts in Mathematics 129, Springer (1991), and the Encyclopedia of Mathematics entry **Contragredient representation**. A modern set of Harvard `18.755` notes states explicitly `L_lambda^*=L_{-w_0 lambda}` and the type-`A` diagram reversal.

Likewise, similarity of a matrix to its transpose is classical linear algebra, and the description of algebraic-representation spectra by torus weights is standard highest-weight theory. The line-local contribution is only the exact no-go obtained by composing those classical facts with the PC-353 outer-parity identity and then applying the Prime-Circle matched-control requirement.

A targeted novelty search found no reason to interpret this representation lift as a new zeta mechanism. On the contrary, the relevant literature places all of its algebra in standard contragredient/highest-weight duality. This finding therefore makes a **negative boundary claim**, not a historical novelty claim.

## Falsification / disproof audit

- **Jordan check:** an algebraic representation preserves semisimple/unipotent Jordan decomposition; the unipotent factor cannot alter eigenvalues.
- **Weight check:** restriction to the diagonal torus makes every representation eigenvalue a weight monomial in the ordinary eigenvalues of `D`.
- **Transpose check:** `D^{-T}` is conjugate to `D^{-1}` inside `SL_d(C)`, so every representation sends the two to similar matrices.
- **Determinant check:** `det o rho` is a character of `SL_d(C)` and is therefore trivial; the reciprocal characteristic-polynomial formula has no residual determinant factor.
- **Fundamental-representation check:** for `Lambda^k`, inversion exchanges `e_k` with `e_{d-k}`, reproducing exactly the coefficient reversal already present in the standard representation.
- **Control check:** every step survives replacement of the cyclotomic source by any matched reciprocal profile obeying the same outer-parity law.
- **Destination check:** the representation lift introduces no intrinsic spectral parameter, archimedean factor, zeta-zero equation, or critical-line selector.

## Boundary assessment

PC-353 showed that outer parity can make the standard conjugacy-class spectrum control-sensitive, but only through contragredient orientation. PC-354 closes the most direct representation-theoretic amplification of that channel: **no fixed finite-dimensional algebraic representation can turn that orientation into additional source information or an RH selector.** Representation spectra are functions of the original spectrum, and reciprocal control remains reciprocal in every representation.

This does **not** rule out constructions in which the state space, representation, or multiplication law itself changes with shell/refinement level in a source-forced way, nor does it rule out non-spectral covariants that retain a canonical frame supplied intrinsically by the roots geometry. It also does not rule out a source-forced infinite-dimensional operator with an independently justified analytic domain and destination theorem. Those escapes are materially different from applying another finite-dimensional representation after the PC-353 development has already been formed.

The surviving burden is therefore sharper: a viable continuation must introduce source-forced structure **before** the ordinary finite-dimensional spectral quotient, or supply an independently zero-sensitive infinite-dimensional destination whose coupling is derived from the roots/refinement geometry rather than chosen as a representation wrapper.