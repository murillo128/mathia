# PC-266 — connected shared-upper collision spectrum is oscillatory and simple

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the fine-spacing / projective frontier left open by PC-257--PC-265.

PC-257 reduced the nonzero squared singular spectrum of the shared-upper defect to the collision-coordinate matrix

\[
M_q=W G_r W G_p,
\tag{1}
\]

where `W=diag(w_1,...,w_k)` has strictly positive collision weights, while `G_p,G_r` are the tridiagonal collision Gram matrices

\[
(G_p)_{aa}=(G_r)_{aa}=2,
\qquad
(G_p)_{a,a+1}=(G_p)_{a+1,a}=-\varepsilon_a,
\qquad
(G_r)_{a,a+1}=(G_r)_{a+1,a}=-\eta_a,
\tag{2}
\]

with `epsilon_a,eta_a in {0,1}`.  PC-258--PC-265 then classified several bulk, edge, and off-spectrum limits but deliberately left fine spacing, projective/rotation data, and genuinely long transfer behavior open.

There is an exact structural simplification before taking any limit: after the common checkerboard gauge, every connected collision component is an **oscillatory matrix** in the classical Gantmacher--Krein sense.  Consequently its squared singular spectrum is positive and simple, and its eigenvectors carry the classical sign-variation ordering.  Exact multiplicities in the full collision problem can therefore occur only between disconnected collision components; the reversal symmetry of PC-260 explains a distinguished family of such multiplicities by pairing reflected components.

This does **not** produce an RH mechanism.  It instead removes within-component exact degeneracy and ordinary Sturm/Pruefer nodal counting from the surviving arithmetic frontier.

## 1. Common checkerboard gauge

Let

\[
S=\operatorname{diag}(1,-1,1,-1,\ldots).
\tag{3}
\]

Since `S` commutes with the positive diagonal matrix `W`, define

\[
A_p=S G_p S,
\qquad
A_r=S G_r S,
\qquad
B=S M_q S=W A_r W A_p.
\tag{4}
\]

The matrices `A_p,A_r` are tridiagonal with diagonal entries `2` and nonnegative first off-diagonal entries:

\[
(A_p)_{a,a+1}=\varepsilon_a,
\qquad
(A_r)_{a,a+1}=\eta_a.
\tag{5}
\]

Thus the arithmetic signs in the collision Gram factors disappear under one shell-independent diagonal similarity.  The remaining question is not entrywise positivity alone but **total nonnegativity**, which is strong enough to control the complete finite spectrum.

## 2. Exact total-nonnegative factorization

Split `A_p` at every position where `epsilon_a=0`.  Every nontrivial block is the Toeplitz tridiagonal matrix

\[
T_m=
\begin{pmatrix}
2&1&&&\\
1&2&1&&\\
&\ddots&\ddots&\ddots&\\
&&1&2&1\\
&&&1&2
\end{pmatrix}.
\tag{6}
\]

It has the exact bidiagonal factorization

\[
T_m=L_mU_m,
\tag{7}
\]

where

\[
(L_m)_{ii}=1,
\qquad
(L_m)_{i,i-1}=\frac{i-1}{i}\quad(i\ge2),
\tag{8}
\]

and

\[
(U_m)_{ii}=\frac{i+1}{i},
\qquad
(U_m)_{i,i+1}=1.
\tag{9}
\]

Indeed, the first diagonal entry is `2`, and for `i>=2`

\[
(L_mU_m)_{ii}
=
\frac{i-1}{i}+\frac{i+1}{i}
=2,
\tag{10}
\]

while both first off-diagonals are exactly `1`.

Nonnegative bidiagonal matrices are totally nonnegative, and total nonnegativity is preserved under products by Cauchy--Binet.  Hence every `T_m` is totally nonnegative.  Contiguous direct sums preserve total nonnegativity, so both `A_p` and `A_r` are totally nonnegative.  Positive diagonal matrices are totally nonnegative as well.  Equation (4) therefore gives the exact conclusion

\[
\boxed{B=W A_r W A_p\ \text{is totally nonnegative}.}
\tag{11}
\]

Moreover `G_p` and `G_r` are positive definite collision Gram matrices and all `w_a>0`, hence

\[
\det B
=
\left(\prod_{a=1}^k w_a^2\right)
\det(G_r)\det(G_p)>0.
\tag{12}
\]

Thus `B` is nonsingular.

The total-nonnegative/oscillatory machinery used here is classical.  The original source is F. Gantmacher and M. Krein, *Sur les matrices completement non negatives et oscillatoires*, Compositio Mathematica **4** (1937), 445--476, available through NUMDAM: <https://www.numdam.org/item?id=CM_1937__4__445_0>.  A modern systematic reference, including bidiagonal factorization and spectral structure, is S. M. Fallat and C. R. Johnson, *Totally Nonnegative Matrices*, Princeton University Press (2011), DOI <https://doi.org/10.23943/princeton/9780691121574.001.0001>.

## 3. Double-gap seams are exactly the reducibility seams

Call the seam between collision coordinates `a` and `a+1` a **double gap** when

\[
\varepsilon_a=\eta_a=0.
\tag{13}
\]

At a double gap both Gram factors split, hence so do `B` and `M_q`.  Conversely, direct multiplication of (4) gives

\[
B_{a,a+1}
=
2w_a^2\varepsilon_a
+2w_aw_{a+1}\eta_a,
\tag{14}
\]

and

\[
B_{a+1,a}
=
2w_{a+1}^2\varepsilon_a
+2w_aw_{a+1}\eta_a.
\tag{15}
\]

Since all collision weights are positive, both entries are strictly positive exactly when

\[
\varepsilon_a+\eta_a>0.
\tag{16}
\]

Therefore the maximal contiguous blocks obtained by cutting at all double gaps are precisely the components on which `B` has positive first super- and subdiagonal entries.

Let `C` be any such maximal component.  Then `B_C` is totally nonnegative and nonsingular, and every entry immediately above and below its diagonal is positive.  The classical Gantmacher--Krein criterion therefore makes `B_C` **oscillatory**: some positive power of `B_C` is totally positive.

Because

\[
M_C=S_CB_CS_C,
\tag{17}
\]

`M_C` is similar to `B_C` and has exactly the same eigenvalues.

## 4. Spectral consequence: connected components have simple positive spectrum

An oscillatory matrix has real, strictly positive, pairwise distinct eigenvalues.  Hence every maximal collision component satisfies

\[
0<\lambda_{C,1}<\lambda_{C,2}<\cdots<\lambda_{C,|C|},
\tag{18}
\]

with no internal multiplicity.  By PC-257 these eigenvalues are precisely the nonzero squared singular values contributed by that collision component.

Thus:

\[
\boxed{
\text{within a connected collision component, every nonzero squared singular value is simple.}
}
\tag{19}
\]

The associated eigenvectors also obey the classical oscillation/sign-variation ordering after the checkerboard gauge.  Therefore a nodal count, Sturm index, or ordinary Pruefer sign-rotation index that uses only this finite oscillatory structure is already tied to eigenvalue ordering.  It is not an independent arithmetic observable.

For the full collision matrix the characteristic polynomial factors over the maximal double-gap components.  Equation (19) gives the stronger exact multiplicity classification

\[
\boxed{
\text{a repeated squared singular value can occur only by coincidence between distinct double-gap components.}
}
\tag{20}
\]

In particular, if the collision chain has no double-gap seam, the entire nonzero squared singular spectrum is simple.

This statement does **not** claim that every cross-component coincidence is symmetry-forced.  Distinct unrelated components can in principle share an eigenvalue accidentally.  What is excluded exactly is an eigenvalue collision internal to one connected component.

## 5. Reversal symmetry explains a forced source of multiplicity

PC-260 proved the exact reversal relation

\[
J_kM_qJ_k=M_q.
\tag{21}
\]

Reversal preserves the double-gap set, so it permutes the maximal collision components.  If a component is mapped to a distinct reflected component, the two component matrices are permutation-similar and therefore isospectral.  Every eigenvalue of that pair then occurs with global multiplicity at least two.

A reversal-fixed central component remains oscillatory and therefore has simple internal spectrum.  Consequently the reflection mechanism does not contradict (19): its degeneracy comes from **two disconnected copies**, not from a collision of eigenvalues inside a connected transfer problem.  Higher global multiplicities would require additional coincidences among distinct components.

This identifies a concrete geometric origin for some exact degeneracies already visible in finite shared-upper examples: double-gap disconnection followed by the exact palindrome of PC-260.

## 6. Exact finite control: `(p,r,q)=(7,13,17)`

For the shared-upper triple `(7,13,17)`, the ordered collision coordinates are

\[
(1,2),\ (3,6),\ (4,7),\ (6,11),
\tag{22}
\]

with collision weights

\[
(w_1,w_2,w_3,w_4)=(15,4,4,15)
\tag{23}
\]

and adjacency bits

\[
(\varepsilon_1,\varepsilon_2,\varepsilon_3)
=(\eta_1,\eta_2,\eta_3)
=(0,1,0).
\tag{24}
\]

There are therefore double-gap seams after coordinates `1` and `3`.  The collision problem splits into a singleton, one connected two-site component, and its reflected singleton.

Each singleton contributes

\[
4\cdot15^2=900.
\tag{25}
\]

For the middle component,

\[
W=4I,
\qquad
G_p=G_r=
\begin{pmatrix}
2&-1\\
-1&2
\end{pmatrix},
\tag{26}
\]

so

\[
M_{\mathrm{mid}}
=16G_p^2
=
\begin{pmatrix}
80&-64\\
-64&80
\end{pmatrix}
\tag{27}
\]

with eigenvalues `16` and `144`.  Hence the complete nonzero squared singular spectrum is

\[
\boxed{\{16,144,900,900\}.}
\tag{28}
\]

The repeated value `900` is not an internal spectral collision: it is produced by the two disconnected singleton components exchanged by reversal.  The middle connected component has the predicted simple spectrum.

## 7. What this closes for the RH search

This result addresses a specific part of the post-PC-265 frontier.  The finite collision transfer problem cannot acquire new arithmetic content merely through:

- an exact eigenvalue degeneracy inside a connected shared-upper component;
- an exceptional-point mechanism based on such an internal collision; or
- a classical nodal/sign-variation index of the checkerboard-gauged finite matrix.

All three are constrained by classical oscillatory-matrix theory.  The simplicity theorem is also **prime-blind at the structural level**: any matched control producing the same positive weights and binary Gram pattern obeys exactly the same argument.  Simplicity itself is therefore not a prime-specific signal.

The result does **not** classicalize the full long-transfer frontier.  It leaves open quantitative fine spacing between distinct simple eigenvalues, subleading edge fluctuations, near-spectrum/mesoscopic determinant statistics, genuinely asymptotic projective or Lyapunov data, and resonant exact itineraries that survive the prior-art filters.  Those observables can depend on how the source geometry drives a long sequence of weights and adjacency bits even though every finite connected component is oscillatory.

The useful boundary is consequently sharper than “the transfer matrix is tridiagonal”:

\[
\boxed{
\text{new information, if any, must live in the quantitative placement/evolution of the simple spectrum,}
}
\tag{29}
\]

not in internal multiplicity or ordinary oscillation count.

## 8. Prior-art and novelty audit

The mathematical implication

\[
\text{nonsingular TN + positive first off-diagonals}
\Longrightarrow
\text{oscillatory}
\Longrightarrow
\text{simple positive spectrum}
\tag{30}
\]

is classical Gantmacher--Krein theory, not a novel spectral theorem.  Bidiagonal factorization and the spectral/sign-variation structure of totally nonnegative matrices are likewise standard; Fallat--Johnson is a modern reference.

The line-local contribution is narrower and exact:

1. the source-forced matrices `G_p,G_r` from PC-257 admit the **same checkerboard gauge** into totally nonnegative tridiagonal blocks;
2. their weighted product `W A_r W A_p` remains totally nonnegative despite `M_q` itself being a nonsymmetric product;
3. the exact reducibility seams are precisely `epsilon_a=eta_a=0`;
4. every connected shared-upper collision component is therefore oscillatory; and
5. combining that with the reversal identity of PC-260 localizes symmetry-forced multiplicity to disconnected reflected components.

I did not find a prior-art source attaching this particular total-nonnegative gauge and double-gap decomposition to the prime-circle/shared-upper collision operator.  That absence is **not** evidence of independent novelty: the durable value here is the project-specific reduction to a classical matrix class and the resulting no-go boundary.

This does not recover `-zeta'/zeta`, impose an arbitrary spectral wrapper, or manufacture an external operator.  It is forced directly by the exact collision geometry already derived in PC-257.

## 9. Falsification and audit boundaries

The argument can fail only if one of its exact structural inputs fails.  In particular:

- a collision weight `w_a` would have to vanish or change sign;
- a Gram off-diagonal would have to leave the binary `0/-1` structure of PC-257;
- the nonzero squared singular spectrum would have to cease being represented by `M_q=W G_r W G_p`; or
- a claimed component would have to cross a seam where both adjacency bits vanish.

Within the PC-257 object none of these occurs.  The derivation uses no asymptotic approximation, no floating-point spectral evidence, and no unproved equidistribution input.

The conclusion should **not** be exported to a different cross-level operator merely because it also has a transfer representation.  The common checkerboard gauge, total nonnegativity, and exact double-gap criterion must be re-established for that object.  Likewise, the result says nothing by itself about hyperbolic prime-flute scattering or any other downstream geometry.
