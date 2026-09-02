# PC-123 — coherent Toeplitz pseudodeterminant incoherentizes to a banded scalar recurrence

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` + `PRIOR-ART-REDIRECTION`. The pseudodeterminant reduction, the two-shell resultant identity, and the finite-state recurrence consequence are derived below. Equality of nonzero singular spectra, complementary-minor/Plücker identities, Sylvester resultants, and finite banded Toeplitz determinant theory are classical. No theorem-level novelty is claimed for those frameworks.

PC-122 showed that the most direct coherent matrix lift of several cyclotomic shell amplitudes,

\[
p(z)=(\Phi_{n_1}(z),\ldots,\Phi_{n_r}(z))^T,
\qquad
W_S(z)=p(z)p(z)^*,
\]

has an extensive exact nullspace: its ordinary block Toeplitz determinant becomes zero once the section is large enough. It explicitly left open the most canonical regularization of that singularity — delete the forced zero modes and take the product of the nonzero eigenvalues.

That repair also collapses. For every fixed finite shell set, the pseudodeterminant is the determinant of a fixed-band **output frame operator** in which all off-diagonal shell coherences have disappeared. Its dependence on section size is therefore governed by a finite transfer matrix and satisfies a constant-coefficient linear recurrence. For two shells there is a sharper exact formula: the entire pseudodeterminant is the classical cyclotomic resultant squared times an ordinary scalar Toeplitz determinant with symbol `|Phi_m|^2+|Phi_n|^2`.

Thus the canonical Euclidean quotient of the one-channel coherent block symbol does not reveal a hidden spectral divisor behind PC-122's zero determinant. It converts coherence into finite-band scalar algebra.

## 1. Coherent block Toeplitz sections as one rectangular multiplication map

Fix distinct shell indices

\[
S=\{n_1,\ldots,n_r\},\qquad r\ge2,
\]

and write

\[
f_j(z)=\Phi_{n_j}(z),
\qquad d_j=\deg f_j,
\qquad D=\max_j d_j.
\]

Give coefficient spaces the standard Hermitian inner product and let

\[
C_{j,N}:\mathcal P_{<N}\longrightarrow\mathcal P_{<N+D},
\qquad q\longmapsto f_jq,
\]

where coefficients above the true degree of `f_j q` are padded by zero. Define the joint multiplication map

\[
A_{S,N}=\begin{bmatrix}C_{1,N}&\cdots&C_{r,N}\end{bmatrix}:
\mathcal P_{<N}^{\oplus r}\longrightarrow\mathcal P_{<N+D}.
\]

With the Gram convention of PC-122, the coherent block Toeplitz section is exactly

\[
\boxed{
\mathbb T_N(W_S)=A_{S,N}^*A_{S,N}.
}
\]

For distinct cyclotomic polynomials any two channels are coprime. PC-122 therefore gives, for `N>D`,

\[
\operatorname{rank}A_{S,N}=N+D.
\]

Hence `A_{S,N}` is surjective onto the coefficient output space.

## 2. The canonical pseudodeterminant removes all off-diagonal shell coherence

The nonzero eigenvalues of `A^*A` and `AA^*` agree with multiplicity. Since `A_{S,N}` is surjective for `N>D`,

\[
\boxed{
\operatorname{pdet}\mathbb T_N(W_S)
=\det\bigl(A_{S,N}A_{S,N}^*\bigr).
}
\]

But block multiplication gives

\[
A_{S,N}A_{S,N}^*
=\sum_{j=1}^r C_{j,N}C_{j,N}^*.
\]

Therefore

\[
\boxed{
\operatorname{pdet}\mathbb T_N(pp^*)
=\det\!\left(\sum_{j=1}^r C_{j,N}C_{j,N}^*\right).
}
\]

This is the first obstruction. The original matrix symbol contains the coherent cross-shell entries

\[
f_i(z)\overline{f_j(z)},\qquad i\ne j.
\]

After passing to the canonical pseudodeterminant, those off-diagonal amplitudes do not survive as separate channels at all. The nonzero singular spectrum sees only the sum of the individual output-frame operators.

This is not a cyclotomic accident. It is the generic singular-value identity for any one-amplitude matrix symbol `p p^*` and therefore holds for matched non-arithmetic polynomial controls as well.

## 3. The remaining output operator has fixed finite bandwidth

Write

\[
f_j(z)=\sum_{u=0}^{d_j}a_{j,u}z^u.
\]

Using zero-based output indices `0<=a,b<N+D`,

\[
\left(C_{j,N}C_{j,N}^*\right)_{ab}
=\sum_{\ell=0}^{N-1}
 a_{j,a-\ell}\,\overline{a_{j,b-\ell}},
\]

with coefficients outside `0,...,d_j` interpreted as zero. Consequently

\[
\left(A_{S,N}A_{S,N}^*\right)_{ab}=0
\qquad\text{when }|a-b|>D.
\]

Away from the first and last `D` rows, the entries are translation invariant and equal the Fourier coefficients of the scalar Laurent polynomial

\[
\boxed{
s_S(z)=\sum_{j=1}^r |f_j(z)|^2.
}
\]

Thus, as `N` varies with the shell set fixed, the pseudodeterminant is the determinant of a matrix with:

- bandwidth `D` independent of `N`;
- a translation-invariant Toeplitz bulk determined by `s_S`;
- two endpoint blocks of width at most `D`, whose local pattern is also independent of `N`.

This finite-width structure already prevents an infinite new size-spectrum from hiding in the quotient.

## 4. Fixed-band determinant sequences are finite-state and C-finite

The recurrence consequence can be seen directly from the Leibniz expansion, without importing asymptotics. For a matrix of bandwidth `D`, a nonzero permutation term must satisfy

\[
|\pi(i)-i|\le D
\]

for every row `i`. Scan rows from left to right. At each cut, only the occupation pattern of columns within distance `D` of the cut can affect future admissible assignments; the sign contribution can likewise be updated from this finite frontier. There are finitely many such frontier states depending only on `D`.

Because the interior weights are translation invariant and the endpoint rules are fixed, there is a finite matrix `R_S` and fixed boundary vectors `u_S,v_S`, independent of section size, such that after absorbing the finite endpoint convention,

\[
\boxed{
\operatorname{pdet}\mathbb T_N(W_S)
=u_S^*R_S^N v_S
}
\]

for all sufficiently large `N` (equivalently, one may shift `N` by a fixed amount depending only on `D`). Cayley--Hamilton then gives a constant-coefficient linear recurrence of finite order. Hence the ordinary section-size generating function is rational.

This is the finite-state form of classical banded Toeplitz determinant theory. Basor--Forrester's rational-symbol Toeplitz formulas, already anchored in `research/prime_circle/SOURCES.md` for PC-121, sit in the same classical exact-evaluation framework. A directed novelty search also reaches the classical Day/Widom banded/rational Toeplitz formulas and modern recurrence presentations. The project-specific point here is not a new recurrence theorem but the exact reduction of PC-122's canonical pseudodeterminant to that finite-band class.

A rational generating function in the section variable has only finitely many algebraic exponential modes (with polynomial factors if characteristic roots collide). It cannot itself carry an infinite Riemann-zero divisor, a gamma factor, a functional equation, or a distinguished critical line. Applying a Mellin or Dirichlet transform afterwards would introduce a different externally chosen analytic object rather than expose a divisor already present in the fixed-shell Toeplitz quotient.

## 5. Two shells admit a sharper exact resultant-times-Toeplitz identity

For two coprime monic polynomials `f,g`, reorder them so that

\[
D=\deg f\ge \deg g.
\]

Let

\[
M_N=\begin{bmatrix}C_{f,N}&C_{g,N}\end{bmatrix}:
\mathcal P_{<N}\oplus\mathcal P_{<N}
\to\mathcal P_{<N+D}.
\]

For `N>D`, PC-122's syzygy calculation gives

\[
\ker M_N
=\{(gh,-fh):h\in\mathcal P_{<N-D}\}.
\]

Set `L=N-D` and define the kernel-basis map

\[
K_N:\mathcal P_{<L}\to
\mathcal P_{<N}\oplus\mathcal P_{<N},
\qquad
h\mapsto(gh,-fh).
\]

Then

\[
M_NK_N=0,
\qquad
\dim\operatorname{row}(M_N)+\dim\operatorname{col}(K_N)=2N.
\]

Hence the maximal minors of `M_N` and the complementary maximal minors of `K_N` are proportional Pluecker coordinates. The proportionality constant can be evaluated on one convenient complementary pair. Choose in `K_N` the `L` rows corresponding to coefficient positions `D,...,N-1` in the `-fh` block. Because `f` is monic, that minor is triangular with determinant `+/-1`. The complementary `(N+D) x (N+D)` minor of `M_N` contains all `N` shifts of `f` and the first `D` shifts of `g`; eliminating the high monic shifts reduces it to the padded Sylvester map at the PC-122 threshold. Its determinant is `+/-Res(f,g)`.

Therefore, for every maximal column set `I` of `M_N`,

\[
|\det(M_N)_I|
=|\operatorname{Res}(f,g)|
\,|\det(K_N)_{I^c}|.
\]

Cauchy--Binet now gives

\[
\begin{aligned}
\det(M_NM_N^*)
&=\sum_I |\det(M_N)_I|^2\\
&=|\operatorname{Res}(f,g)|^2
  \sum_J |\det(K_N)_J|^2\\
&=|\operatorname{Res}(f,g)|^2\det(K_N^*K_N).
\end{aligned}
\]

Finally, `K_N` is itself the stacked multiplication map `h -> (gh,-fh)`, so

\[
K_N^*K_N
=T_L\bigl(|f|^2+|g|^2\bigr),
\qquad L=N-D,
\]

where the Toeplitz section is taken with respect to the coefficient/Haar inner product. With the convention `det T_0=1`, the threshold case `N=D` is included as well. Thus

\[
\boxed{
\operatorname{pdet}\mathbb T_N
\!\left(
\begin{bmatrix}f\\g\end{bmatrix}
\begin{bmatrix}f\\g\end{bmatrix}^{\!*}
\right)
=
|\operatorname{Res}(f,g)|^2
\det T_{N-D}\bigl(|f|^2+|g|^2\bigr),
\qquad N\ge D.
}
\]

This is stronger than the generic output-frame reduction: for two shells all boundary corrections can be moved into the exact syzygy quotient, leaving an ordinary scalar Toeplitz determinant.

## 6. Cyclotomic specialization

Take

\[
f=\Phi_m,
\qquad g=\Phi_n,
\qquad m\ne n.
\]

Then the prefactor

\[
|\operatorname{Res}(\Phi_m,\Phi_n)|^2
\]

is exactly PC-002/PC-122's classical Apostol prime-power-jump invariant. The remaining scalar symbol is

\[
\boxed{
s_{m,n}(z)=|\Phi_m(z)|^2+|\Phi_n(z)|^2.
}
\]

Distinct cyclotomic polynomials have no common root, so `s_{m,n}` is strictly positive on the unit circle. It is a fixed Laurent polynomial of bandwidth `D`. Therefore its Toeplitz determinant sequence is in the regular finite-band regime described above: finitely many algebraic transfer modes and a constant-coefficient recurrence in section size.

The canonical pseudodeterminant has therefore separated the two kinds of information very cleanly:

\[
\boxed{
\text{coherent two-shell pseudodeterminant}
=
\text{classical pairwise resultant}^2
\times
\text{incoherent scalar finite-band determinant}.
}
\]

No independent cross-shell phase survives this quotient.

## 7. Exact stress test: `Phi_3` and `Phi_6`

Let

\[
f=\Phi_3=z^2+z+1,
\qquad
g=\Phi_6=z^2-z+1.
\]

Here `D=2` and

\[
|\operatorname{Res}(f,g)|=4.
\]

The quotient symbol simplifies to

\[
|f(z)|^2+|g(z)|^2
=2z^2+6+2z^{-2}
\qquad(|z|=1).
\]

Writing

\[
E_L=\det T_L(2z^2+6+2z^{-2}),
\qquad E_0=1,
\]

direct exact determinants give

\[
E_L=1,6,36,192,1024,5376,28224,147840,\ldots
\]

and satisfy the fixed recurrence

\[
\boxed{
E_L=6E_{L-1}-24E_{L-3}+16E_{L-4}
\qquad(L\ge4).
}
\]

Consequently the coherent block pseudodeterminants at `N=2,3,4,5,...` begin

\[
16,96,576,3072,16384,\ldots,
\]

exactly `16 E_{N-2}`. The first value `16` is PC-122's last nonsingular ordinary determinant; after the ordinary determinant becomes identically zero, its canonical pseudodeterminant simply continues along this finite recurrence.

## 8. Matched non-arithmetic control

Nothing in the reduction through Sections 1--5 requires cyclotomic polynomials, roots of unity, prime birth, or arithmetic refinements. For arbitrary fixed coprime monic polynomials `f,g`, the same identity holds:

\[
\operatorname{pdet}\mathbb T_N(pp^*)
=|\operatorname{Res}(f,g)|^2
\det T_{N-D}(|f|^2+|g|^2).
\]

For any fixed finite list of arbitrary polynomial channels, the pseudodeterminant likewise becomes the determinant of the fixed-band output frame `sum_j C_j C_j^*` and is C-finite in section size.

Thus the mechanism responsible for the regularized sequence is generic polynomial linear algebra. Cyclotomy supplies special coefficients and a classical special resultant, but not a new determinant mechanism.

## 9. Prior-art and novelty audit

The components of the reduction are classical even though their combination gives a useful project-specific no-go.

1. **Nonzero Gram spectra are classical linear algebra.** The positive eigenvalues of `A^*A` and `AA^*` are the squared nonzero singular values of `A`. Using `AA^*` to evaluate the pseudodeterminant is therefore standard.
2. **The two-shell proportionality is determinant-line/resultant algebra.** Complementary Pluecker coordinates of a subspace and its orthogonal complement are classical; evaluating the common factor on the padded Sylvester minor produces the ordinary polynomial resultant. PC-122 already identified that resultant at the last nonsingular section, and PC-002 classifies its cyclotomic value.
3. **Fixed-band Toeplitz determinant recurrences are classical.** The finite-frontier argument above derives exactly what is needed here. The surrounding literature includes the rational-symbol exact determinant theory already represented in `SOURCES.md` by Basor--Forrester, as well as the classical Day/Widom formulas and later Schur-polynomial/recurrence presentations for banded Toeplitz minors.

Directed searches for cyclotomic block-Toeplitz pseudodeterminants, Sylvester/resultant Gram quotients, and banded Toeplitz recurrences did not locate this exact Prime-Circle formulation. That absence is **not** treated as a theorem-level novelty claim. The durable contribution is the exact classification of the canonical regularization explicitly left open by PC-122.

## 10. Why this is a decisive negative for the canonical pseudodeterminant repair

PC-122 left the chain

\[
\text{coherent shell vector}
\to pp^*
\to \text{singular block Toeplitz section}
\to \text{remove forced zero modes}
\to \text{pseudodeterminant}
\to \text{new RH spectral divisor}
\]

open because the ordinary determinant vanishes too early to test it.

The actual chain is

\[
\boxed{
pp^*
\to A^*A
\to \operatorname{pdet}(A^*A)=\det(AA^*)
\to \text{fixed-band finite-state determinant}.
}
\]

For two shells it sharpens to

\[
\boxed{
\operatorname{pdet}
=|\operatorname{Res}(\Phi_m,\Phi_n)|^2
\det T_{N-D}(|\Phi_m|^2+|\Phi_n|^2).
}
\]

Thus deleting the extensive syzygy nullspace does not uncover hidden coherent modes. It **incoherentizes** them. The section-size dependence is finite-state and rational rather than carrying an infinite nontrivial divisor. There is no intrinsic `s`, no `s <-> 1-s` symmetry, no gamma factor, and no mechanism singling out `Re(s)=1/2`.

## 11. Boundary of the obstruction

The finding is deliberately limited to the canonical pseudodeterminant of the fixed finite-shell **rank-one coherent symbol**

\[
W_S=p p^*.
\]

It rules out the Euclidean quotient obtained by removing exactly the forced zero eigenspace while retaining the ordinary nonzero eigenvalues.

It does **not** rule out:

- a full-rank matrix symbol with several independently geometry-forced amplitude channels rather than one vector `p`;
- a non-Euclidean quotient metric or torsion-like normalization if that metric is derived intrinsically rather than selected to manufacture a determinant;
- a regime in which the shell set, conductors, or bandwidth grow with section size, so no fixed transfer matrix remains;
- a genuinely cross-level operator in which the varying conductor is part of the state space rather than a parameter labeling a fixed symbol;
- a separate geometry-forced spectral parameter entering before compression;
- the extensive old/new cotangent coupling and its surviving non-fixed-network boundaries;
- the nonlinear uniformization/monodromy branch.

Conversely, keeping a fixed finite set of cyclotomic amplitudes in one coherent rank-one matrix symbol and then replacing its zero determinant by the ordinary pseudodeterminant is now classified and should not be pursued as a new RH mechanism.

## 12. Falsification surface

The result has six exact audit points.

1. **Gram factorization:** PC-122's block Toeplitz section must equal `A^*A` for the stated multiplication map.
2. **Rank:** for distinct cyclotomic channels and `N>D`, `A` must have rank `N+D`; failure would invalidate the pseudodeterminant-to-output-determinant step.
3. **Coherence loss:** direct multiplication must give `AA^*=sum_j C_j C_j^*` with no cross terms.
4. **Finite bandwidth:** the output frame must have bandwidth at most `D` and a translation-invariant bulk with only fixed-width endpoint defects.
5. **Two-shell complementary minors:** maximal minors of `M_N` must be `Res(f,g)` times complementary minors of the syzygy map `K_N`; the chosen monic minor must fix the proportionality constant exactly.
6. **Toeplitz quotient:** `K_N^*K_N` must equal the scalar Toeplitz section of `|f|^2+|g|^2`; direct coefficient matrices for sample cyclotomic pairs must reproduce the stated pseudodeterminants.

Failure of any item invalidates the corresponding conclusion. If all hold, the canonical fixed-shell coherent pseudodeterminant has only finite-state section-size complexity.

## Research consequence

The pseudodeterminant loophole left by PC-122 is closed for the same one-channel coherent construction:

\[
\boxed{
W_S=p p^*
\quad\Longrightarrow\quad
\operatorname{pdet}\mathbb T_N(W_S)
\text{ is a fixed-band C-finite sequence in }N.
}
\]

For two shells its exact quotient is only a classical resultant squared times a scalar positive-symbol Toeplitz determinant. Further Toeplitz work should therefore require genuinely independent geometry-forced channels, a varying cross-level/bandwidth construction, or a different intrinsic quotient structure rather than another regularization of the same rank-one coherent block symbol.
