# AF-006 — Marked Hermitian spectra are classified by per-eigenspace Gram data

**Status:** `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`

## Claim

Let `H` and `H'` be finite-dimensional complex Hilbert spaces, let

\[
A:H\to H,
\qquad
A':H'\to H'
\]

be self-adjoint operators, and let

\[
U=(u_1,\ldots,u_m),
\qquad
U'=(u'_1,\ldots,u'_m)
\]

be ordered tuples of distinguished vectors. For each eigenvalue `lambda` of `A`, let `P_lambda` be the orthogonal projection onto the eigenspace `E_lambda`, and define the marked spectral Gram matrix

\[
G_\lambda(A,U)
=
\bigl(\langle P_\lambda u_i, P_\lambda u_j\rangle\bigr)_{i,j=1}^m.
\]

Define `G_lambda(A',U')` analogously. Then:

1. the unmarked eigenvalue multiset of a finite-dimensional self-adjoint operator is a complete invariant for unitary equivalence of the operator itself;
2. the pointed pairs `(A,U)` and `(A',U')` are jointly unitarily equivalent — there is a unitary `W:H->H'` such that
   \[
   WA=A'W,
   \qquad
   Wu_i=u'_i\quad(1\le i\le m)
   \]
   — if and only if they have the same eigenvalues with the same multiplicities and
   \[
   G_\lambda(A,U)=G_\lambda(A',U')
   \]
   for every eigenvalue;
3. the marked tuple is cyclic for `A`, meaning
   \[
   \operatorname{span}\{p(A)u_i:p\in\mathbb C[t],\ 1\le i\le m\}=H,
   \]
   if and only if
   \[
   \operatorname{rank}G_\lambda(A,U)=\dim E_\lambda
   \]
   for every eigenvalue `lambda`;
4. consequently, on the finitely cyclic locus, the atomic matrix-valued spectral measure
   \[
   \mathsf M_{A,U}
   =
   \sum_{\lambda} G_\lambda(A,U)\,\delta_\lambda
   \]
   alone is a complete invariant of the pointed pair up to joint unitary equivalence: its support gives the eigenvalues and the rank of each atom gives the spectral multiplicity;
5. for `m>=2`, retaining only the diagonal scalar spectral measures
   \[
   \mu_i
   =
   \sum_\lambda \|P_\lambda u_i\|^2\,\delta_\lambda
   \]
   is not sufficient in general, even when the tuple is cyclic. The missing off-diagonal entries of `G_lambda` carry genuine relational information between the marks.

Thus spectralization gives a clean Arithmetic Fidelity hierarchy. The unmarked spectrum remembers the operator only up to unitary conjugacy; adding separately marked scalar spectral weights remembers how each mark meets each eigenspace but can still forget the geometry **between** marks; the full matrix-valued spectral measure restores exactly those per-eigenspace relations. In this model, the relevant lift is not an eigenbasis label but a gauge-invariant relational Gram object.

The mathematics is classical spectral theorem / Gram-matrix / matrix-spectral-measure theory. The line-specific contribution is to isolate it as an exact worked model of how marking can restore provenance after spectral compression without reintroducing arbitrary coordinates.

## Derivation

### Unmarked self-adjoint spectrum

The finite-dimensional spectral theorem gives

\[
A=\sum_\lambda \lambda P_\lambda,
\]

with mutually orthogonal eigenspaces. Two self-adjoint operators are unitarily equivalent exactly when their eigenspaces have the same dimensions at the same eigenvalues, equivalently when their eigenvalue multisets agree.

So for the operator **without external marks**, passing to the spectrum with multiplicity loses eigenbasis coordinates but no unitary-conjugacy information. This is an important contrast with AF-003's GIT example, where the categorical quotient can identify distinct nonclosed orbits beyond the intended group action.

### Classification with an ordered tuple of marks

Assume first that a joint unitary `W` exists. Since `WA=A'W`, functional calculus gives

\[
WP_\lambda=P'_\lambda W.
\]

Therefore

\[
\langle P'_\lambda u'_i,P'_\lambda u'_j\rangle
=
\langle WP_\lambda u_i,WP_\lambda u_j\rangle
=
\langle P_\lambda u_i,P_\lambda u_j\rangle,
\]

so every marked spectral Gram matrix agrees. The spectral multiplicities also agree because `W` maps each eigenspace unitarily onto its counterpart.

Conversely, suppose the multiplicities and all `G_lambda` agree. Fix one eigenvalue and put

\[
v_i=P_\lambda u_i\in E_\lambda,
\qquad
v'_i=P'_\lambda u'_i\in E'_\lambda.
\]

The two ordered vector families have the same Gram matrix. The standard Gram uniqueness theorem therefore gives an isometry

\[
W_\lambda:
\operatorname{span}\{v_i\}
\longrightarrow
\operatorname{span}\{v'_i\}
\]

with `W_lambda v_i=v'_i` for every `i`. Equal spectral multiplicities give

\[
\dim E_\lambda=\dim E'_\lambda,
\]

so this isometry extends to a unitary from the whole eigenspace `E_lambda` onto `E'_lambda`.

Taking the orthogonal direct sum over eigenvalues,

\[
W=\bigoplus_\lambda W_\lambda,
\]

produces a unitary `H->H'`. It intertwines `A` and `A'` because each summand maps the `lambda`-eigenspace to the `lambda`-eigenspace. Also

\[
Wu_i
=
\sum_\lambda W_\lambda P_\lambda u_i
=
\sum_\lambda P'_\lambda u'_i
=u'_i.
\]

This proves the pointed classification theorem.

## Why cyclicity lets the matrix measure replace the unmarked spectrum

For a finite-spectrum self-adjoint operator, polynomial interpolation lets one choose a polynomial taking arbitrary prescribed scalar values on the distinct eigenvalues. Hence

\[
\operatorname{span}\{p(A)u_i\}
=
\bigoplus_\lambda
\operatorname{span}\{P_\lambda u_1,\ldots,P_\lambda u_m\}.
\]

Therefore the tuple `U` is cyclic exactly when its projected marks span every eigenspace.

For any finite vector family, the rank of its Gram matrix equals the dimension of its linear span. Thus

\[
U\text{ cyclic}
\iff
\operatorname{rank}G_\lambda(A,U)=\dim E_\lambda
\quad\text{for every }\lambda.
\]

On this locus, every eigenspace appears in the support of `M_{A,U}` and the atom rank recovers its multiplicity. The matrix measure therefore contains both the unmarked spectral data and the complete relative geometry of the marked vectors inside each eigenspace.

This finite-dimensional statement is the atomic specialization of the classical matrix-measure representation of finitely cyclic self-adjoint operators.

## Exact counterexample: separate scalar marks lose relational geometry

Let

\[
H=\mathbb C^2,
\qquad
A=0,
\]

and let `e_1,e_2` be the standard orthonormal basis. Compare the two ordered marked tuples

\[
U=(e_1,e_2),
\qquad
V=\left(e_1,\frac{e_1+e_2}{\sqrt2}\right).
\]

Both tuples are cyclic for `A`: because `A=0`, their polynomial cyclic subspace is simply the span of the marked vectors, which is all of `C^2` in both cases.

There is only one eigenvalue, `lambda=0`, with multiplicity two. Every marked vector has norm one. Hence the two individual scalar spectral measures are identical in both pointed systems:

\[
\mu_1=\mu_2=\delta_0.
\]

The unmarked spectrum also agrees.

But the full Gram atoms are

\[
G_0(A,U)
=
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix},
\qquad
G_0(A,V)
=
\begin{pmatrix}
1&1/\sqrt2\\
1/\sqrt2&1
\end{pmatrix}.
\]

No unitary can carry the ordered tuple `U` to `V`, because a unitary preserves inner products whereas

\[
\langle e_1,e_2\rangle=0
\qquad\text{but}\qquad
\left\langle e_1,\frac{e_1+e_2}{\sqrt2}\right\rangle
=\frac1{\sqrt2}.
\]

So **diagonal spectral marking can be complete for each mark separately while still being incomplete for the jointly marked object**. The lost information is exactly cross-mark relational data.

## Arithmetic Fidelity interpretation

This example gives a precise version of the recurring marked-versus-unmarked intuition.

A spectral compression can be perfectly faithful to the operator's intrinsic unitary class and still be unfaithful to a discriminator that depends on the operator's relation to distinguished upstream structure. The correct question is therefore not simply

\[
\text{“does the spectrum determine the operator?”}
\]

but

\[
\text{“what is the object whose provenance must survive, and what quotient is intended?”}
\]

For a Hermitian operator with an ordered family of retained marks, the spectral theorem decomposes the fidelity problem eigenspace by eigenspace. Inside each eigenspace, the unitary gauge is intentionally invisible; the complete invariant of the marked vectors under that gauge is their Gram matrix. The global pointed invariant is therefore the collection of those local Gram objects indexed by eigenvalue.

This also clarifies why storing one scalar weight per mark can fail. Scalar weights retain the norms of the projected marks but destroy their mutual angles and phases. The full matrix measure restores those relations without choosing an eigenbasis.

In the language of AF-004 and AF-005, this is another case where **relational cross-terms close an otherwise enlarged quotient fiber**. Here the cross-terms are sesquilinear rather than monomial phase relations, and completeness follows from Gram rigidity inside each spectral subspace rather than an annihilator lattice.

## Prior art and novelty assessment

The finite-dimensional self-adjoint spectral theorem and unitary classification by eigenvalues with multiplicity are classical. The fact that two finite vector families with the same Gram matrix are related by a unitary on their spans, extendable when ambient dimensions agree, is also standard linear algebra; Horn and Johnson's *Matrix Analysis* is an appropriate general reference for both unitary equivalence and Gram-matrix geometry.

Scalar spectral measures attached to cyclic vectors are a standard form of the spectral theorem. The multiple-vector analogue is the classical theory of matrix-valued spectral measures. Moszyński develops a representation theorem for finitely cyclic self-adjoint operators in matrix-measure `L^2` spaces, explicitly generalizing the scalar cyclic representation. Liaw and Treil likewise use matrix-valued measures as the natural spectral language for finite-rank/multiple-vector self-adjoint perturbation theory and construct the corresponding spectral representation.

Accordingly, no novelty is claimed for the classification mechanism itself. The Arithmetic Fidelity contribution is the **fidelity decomposition**:

\[
\text{unmarked spectrum}
\;<\;
\text{separate scalar marked measures}
\;<\;
\text{matrix-valued marked spectral measure},
\]

where the inequalities mean that the later object can distinguish pointed systems that the earlier one may identify. The counterexample above makes the middle failure exact and shows that “add markings” is still too vague: independent markings can remain lossy unless their mutual relations are retained.

## Boundaries and failure modes

- The exact proof above is finite-dimensional and self-adjoint. Infinite-dimensional operators may have continuous spectrum and require direct-integral/multiplicity theory and measurable matrix-valued measures.
- If the marked tuple is not cyclic, `M_{A,U}` alone does not see spectral subspaces orthogonal to the entire cyclic span. The unmarked spectrum/multiplicity data must then be retained separately, or another marking must expose the missing subspace.
- The theorem classifies an **ordered** marked tuple. If permutations or other transformations of the marks are intentionally gauge, the quotient must be modified accordingly.
- Full matrix spectral data are complete, but no universal claim of minimal encoding size is made. Another admissible observable family may encode the same quotient more economically.
- Diagonal scalar measures can be sufficient in special constrained classes, for example when cross-mark geometry is fixed independently. The counterexample rules out only universal sufficiency.
- The result says nothing about whether a concrete RH construction supplies canonical marked vectors, whether those vectors are cyclic, or whether an arithmetic discriminator depends on the resulting pointed spectral class.
- A spectrum, scalar spectral measure, or matrix spectral measure should not be imported into an arithmetic construction unless the operator and marks are independently natural there.

## Decisive audit test for marked spectral compressions

For a proposed spectral or determinant-based compression with distinguished upstream data:

1. identify the exact operator category and intended equivalence group;
2. identify which upstream structures become distinguished vectors/subspaces rather than silently discarding them before spectralization;
3. compute the spectral projections of those marks;
4. distinguish explicitly between unmarked eigenvalue data, diagonal scalar spectral weights, and full cross-mark matrix data;
5. test for two pointed systems with equal proposed compressed data but different per-eigenspace Gram matrices;
6. if relying on the matrix measure alone, verify cyclicity or otherwise account for invisible orthogonal spectral multiplicity.

A matched pair passing step 5 is a no-go certificate for any downstream function of the weaker compressed data. Conversely, equality of the full marked spectral Gram data plus multiplicities is an exact finite-dimensional certificate that no additional pointed information remains beyond unitary gauge.

## Consequence for the line

Add **pointed spectral quotients** to the Arithmetic Fidelity model library.

The important structural lesson is not merely that eigenvectors contain more information than eigenvalues. A basis-free, canonical lift exists: retain the spectral measure of the distinguished upstream marks, including their cross-correlations. For multiple marks, the off-diagonal matrix entries are not decorative; they are exactly what prevents separately preserved provenance channels from losing their relations to one another.

Future spectral applications should therefore ask whether the relevant arithmetic/geometric data survive as a cyclic marked family and whether the downstream object retains the corresponding matrix-valued spectral measure or collapses it prematurely to scalar traces, determinants, diagonal weights, or an unmarked spectrum.