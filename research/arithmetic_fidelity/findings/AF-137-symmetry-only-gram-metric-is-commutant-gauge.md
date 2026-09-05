# AF-137 — Symmetry-only Gram metrics are exactly commutant gauges

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-MECHANISM`, `NATURALITY-GATE`, `GAUGE-CLASSIFICATION`, `NO-NOVELTY-CLAIM`

## Claim

AF-136 shows that a source Gram spectrum is not intrinsic under arbitrary invertible generator reparameterization: target-relative information descends to projection geometry unless an independent coefficient metric restricts the gauge. A natural possible repair is to demand that the coefficient metric respect a declared symmetry. For compact-group symmetry this repair has an exact limitation.

Let `K` be a compact group, let `V` and `H` be finite-dimensional complex representations of `K`, and choose `K`-invariant Hermitian inner products on both spaces. Let

\[
A:V\to H
\]

be `K`-equivariant. Write the unitary representation on `V` in isotypic form

\[
V\cong\bigoplus_{\alpha\in I} M_\alpha\otimes W_\alpha,
\tag{1}
\]

where the `W_\alpha` are pairwise inequivalent irreducible `K`-representations and `M_\alpha\cong\mathbb C^{m_\alpha}` are multiplicity spaces. Fix one invariant reference inner product `\langle\cdot,\cdot\rangle_0` on `V`, let `A_0^*` be the corresponding adjoint, and put

\[
G_0=A_0^*A.
\tag{2}
\]

Then:

1. **All symmetry-compatible coefficient metrics are exactly the positive cone of the commutant.** Every `K`-invariant Hermitian inner product on `V` is uniquely
   \[
   \langle x,y\rangle_S
   =\langle Sx,y\rangle_0,
   \tag{3}
   \]
   for a positive-definite self-adjoint operator `S` commuting with `K`. Under (1),
   \[
   \boxed{
   S=\bigoplus_{\alpha\in I}(S_\alpha\otimes I_{W_\alpha}),
   \qquad S_\alpha>0.
   }
   \tag{4}
   \]
   Thus symmetry does not usually choose a coefficient metric; it reduces the metric gauge to one positive matrix on every multiplicity space.

2. **An equivariant Gram operator lies in the same commutant, and changing the invariant metric acts by positive congruence on its multiplicity blocks.** One has
   \[
   \boxed{
   G_0
   =\bigoplus_{\alpha\in I}(B_\alpha\otimes I_{W_\alpha}),
   \qquad B_\alpha\ge0.
   }
   \tag{5}
   \]
   If `A_S^*` denotes the adjoint for the metric (3), then
   \[
   A_S^*=S^{-1}A_0^*,
   \qquad
   G_S=A_S^*A=S^{-1}G_0.
   \tag{6}
   \]
   The isometry `S^{1/2}:(V,\langle\cdot,\cdot\rangle_S)\to(V,\langle\cdot,\cdot\rangle_0)` identifies this self-adjoint operator with
   \[
   \widehat G_S
   =S^{-1/2}G_0S^{-1/2}
   =\bigoplus_\alpha
   \left(S_\alpha^{-1/2}B_\alpha S_\alpha^{-1/2}\otimes I_{W_\alpha}\right).
   \tag{7}
   \]

3. **Among positive Gram eigenvalue magnitudes, symmetry alone preserves only isotypic support and rank.** Let
   \[
   r_\alpha=\operatorname{rank}B_\alpha.
   \]
   For any prescribed positive numbers
   \[
   \lambda_{\alpha,1},\ldots,\lambda_{\alpha,r_\alpha}>0,
   \tag{8}
   \]
   there is a `K`-invariant coefficient metric for which the positive eigenvalues of the `\alpha` block of `\widehat G_S` are exactly those values, each repeated `\dim W_\alpha` times. Consequently no ratio, ordering, spectral gap, threshold, or positive spectral scale inside or across active isotypic blocks is forced by `K`-invariance alone.

   More explicitly, if
   \[
   B_\alpha
   =U_\alpha\operatorname{diag}(b_1,\ldots,b_{r_\alpha},0,\ldots,0)U_\alpha^*,
   \qquad b_j>0,
   \tag{9}
   \]
   choose
   \[
   S_\alpha
   =U_\alpha\operatorname{diag}
   \left(
   \frac{b_1}{\lambda_{\alpha,1}},\ldots,
   \frac{b_{r_\alpha}}{\lambda_{\alpha,r_\alpha}},
   1,\ldots,1
   \right)U_\alpha^*.
   \tag{10}
   \]
   Equation (7) then gives the requested spectrum. In particular, every active block can be flattened to the identity on its positive range.

4. **Symmetry fixes the coefficient metric up to one global scale exactly in the irreducible case, but then the equivariant Gram spectrum is flat.** For nonzero `V`, the cone (4) consists only of scalar multiples of the identity iff `V` is irreducible. In that case Schur's lemma also forces
   \[
   G_0=\beta I_V,
   \qquad \beta\ge0.
   \tag{11}
   \]
   If `A\ne0`, irreducibility makes `A` injective and `\beta>0`. Every symmetry-compatible metric is `S=sI`, hence
   \[
   \widehat G_S=\frac{\beta}{s}I_V.
   \tag{12}
   \]
   Therefore the regime in which symmetry alone makes the metric canonical up to scale is exactly the regime in which an equivariant Gram operator has no nontrivial internal positive spectral hierarchy.

5. **Multiplicity-free reducible symmetry leaves an especially transparent scale gauge.** If every `m_\alpha=1`, then
   \[
   S_\alpha=s_\alpha>0,
   \qquad
   B_\alpha=b_\alpha\ge0,
   \tag{13}
   \]
   and the active Gram eigenvalue on the `\alpha`-isotypic component is simply
   \[
   \frac{b_\alpha}{s_\alpha}.
   \tag{14}
   \]
   The representation type of each component is canonical, but its positive spectral scale is not. If at least two components are active, their ordering can be reversed or otherwise prescribed by changing the invariant metric weights `s_\alpha`.

6. **Symmetry alone therefore cannot supply the missing metric demanded by AF-136 while simultaneously producing a nontrivial positive Gram spectral ranking.** There is a dichotomy:
   - if the coefficient representation is irreducible, the invariant metric is unique up to scale but the equivariant Gram spectrum is flat;
   - if it is reducible, the symmetry-compatible metric cone has nontrivial commutant freedom, and that freedom can arbitrarily rescale every active positive multiplicity eigenchannel.

   Hence a source-Gram cutoff justified by symmetry needs **additional mathematical data beyond invariance**: for example a source-canonical measure, energy, norm, trace normalization, local geometric metric, probabilistic law, or another independently defined structure that fixes the relative metric on the isotypic/multiplicity spaces. If a target mark is used to choose those weights, that is target-relative enrichment and must be audited as such rather than described as symmetry-only canonicity.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\begin{array}{c}
\text{compact symmetry reduces the full generator gauge to the commutant gauge;}\\
\text{the positive commutant cone is exactly the residual metric ambiguity;}\\
\text{irreducibility kills that ambiguity only by making every equivariant Gram scale flat;}\\
\text{therefore a nontrivial intrinsic Gram hierarchy requires extra structure beyond symmetry.}
\end{array}}
\tag{15}
\]

## Derivation

### Invariant metrics are positive commutant operators

Because `K` is compact, averaging any Hermitian inner product against normalized Haar measure gives a `K`-invariant reference metric. Fix such a metric `\langle\cdot,\cdot\rangle_0`, so the representation `\rho(g)` on `V` is unitary.

Every other Hermitian inner product can be written uniquely as (3) for a positive-definite `\langle\cdot,\cdot\rangle_0`-self-adjoint operator `S`. The new metric is `K`-invariant iff

\[
\langle S\rho(g)x,\rho(g)y\rangle_0
=\langle Sx,y\rangle_0
\qquad\forall g,x,y.
\tag{16}
\]

Using unitarity of `\rho(g)`, this is equivalent to

\[
\rho(g)^{-1}S\rho(g)=S,
\tag{17}
\]

so `S` lies in the commutant `\operatorname{End}_K(V)`.

Complete reducibility and Schur's lemma give the standard isotypic commutant decomposition

\[
\operatorname{End}_K(V)
\cong
\bigoplus_{\alpha\in I}
\operatorname{End}(M_\alpha)\otimes I_{W_\alpha}.
\tag{18}
\]

Intersecting (18) with the positive-definite self-adjoint cone proves (4).

This already gives the exact metric-canonicity criterion. If `V` is irreducible, Schur's lemma gives `\operatorname{End}_K(V)=\mathbb C I`, whose positive self-adjoint elements are `sI`, `s>0`. Conversely, if `V` is reducible, its invariant orthogonal decomposition contains a nontrivial invariant projection `P`; then

\[
S=aP+b(I-P),
\qquad a,b>0,
\quad a\ne b,
\tag{19}
\]

is a non-scalar invariant positive metric operator. Thus invariant metrics form one ray iff `V` is irreducible.

### Equivariance forces the Gram operator into the same commutant

Let `\sigma(g)` be the unitary representation on `H`. Equivariance says

\[
A\rho(g)=\sigma(g)A.
\tag{20}
\]

Taking adjoints in the reference metrics gives

\[
\rho(g)^{-1}A_0^*=A_0^*\sigma(g)^{-1}.
\tag{21}
\]

Therefore

\[
G_0\rho(g)
=A_0^*A\rho(g)
=A_0^*\sigma(g)A
=\rho(g)A_0^*A
=\rho(g)G_0,
\tag{22}
\]

so `G_0` belongs to the commutant and has block form (5), with each `B_\alpha` positive semidefinite.

For the metric (3), the adjoint is characterized by

\[
\langle Ax,y\rangle_H
=\langle x,A_S^*y\rangle_S
=\langle Sx,A_S^*y\rangle_0.
\tag{23}
\]

Comparison with the reference adjoint yields `SA_S^*=A_0^*`, proving (6). The map `S^{1/2}` is an isometry from the new coefficient Hilbert space to the reference one, and conjugating `G_S` by it gives (7).

Thus changing only the symmetry-compatible coefficient metric acts on each multiplicity-space Gram block by positive congruence.

### Positive congruence removes every active spectral magnitude

Fix one block and diagonalize it as in (9). For arbitrary desired positive values (8), the operator (10) is positive definite. Direct substitution gives

\[
S_\alpha^{-1/2}B_\alpha S_\alpha^{-1/2}
=
U_\alpha
\operatorname{diag}
(\lambda_{\alpha,1},\ldots,\lambda_{\alpha,r_\alpha},0,\ldots,0)
U_\alpha^*.
\tag{24}
\]

Hence the zero multiplicity, equivalently `r_\alpha`, survives every metric choice, but every positive eigenvalue magnitude is adjustable. Choosing all `\lambda_{\alpha,j}=1` flattens the active block. Choosing different values produces any desired positive scale profile.

This does not say that all source structure has disappeared. The `K`-representation itself, the isotypic labels, the physical kernel `\ker A`, and the ranks `r_\alpha` remain meaningful. The no-go is specifically about using **positive Gram spectral scale** as an intrinsic ranking when the only declared coefficient geometry is `K`-invariance.

### Canonical metric and rich equivariant spectrum are opposite symmetry regimes

Suppose first that `V` is irreducible. The preceding metric argument gives `S=sI`. Equation (22) and Schur's lemma give (11). If `A\ne0`, then `\ker A` is an invariant subspace and must be zero, so `G_0` is positive definite and `\beta>0`. Equation (12) follows. A symmetry-only spectral cutoff can therefore distinguish only the trivial alternatives `A=0` versus one flat positive block.

Suppose instead that `V` is reducible. Then non-scalar positive operators exist in the commutant. If `G_0` has at least two active multiplicity eigenchannels, item 3 lets their positive eigenvalue order be chosen arbitrarily. If it has at most one active eigenchannel, there is no nontrivial positive hierarchy to rank in the first place. In neither case does symmetry alone produce a canonical nontrivial ordering of positive Gram scales.

This is the exact residual-gauge answer left open by AF-136. Full `GL(V)` generator gauge was too large; imposing a compact symmetry replaces it by the smaller commutant gauge. But the commutant gauge is still precisely large enough to erase positive spectral scales whenever reducibility permits a potentially rich equivariant spectrum.

## Exact controls

### Two inequivalent symmetry types can swap their Gram order without changing the symmetry

Take `K=\mathbb Z/2\mathbb Z` and

\[
V=\mathbb C e_+\oplus\mathbb C e_-,
\]

with the trivial and sign characters on the two lines. Let `H` carry the same representation and define the equivariant map

\[
Ae_+=\sqrt{b_+}\,e_+,
\qquad
Ae_-=\sqrt{b_-}\,e_-,
\qquad b_+,b_->0.
\tag{25}
\]

Every invariant coefficient metric has

\[
S=\operatorname{diag}(s_+,s_-),
\qquad s_+,s_->0,
\tag{26}
\]

so the Gram eigenvalues are

\[
\frac{b_+}{s_+},
\qquad
\frac{b_-}{s_-}.
\tag{27}
\]

The symmetry type of each direction is unchanged, but either one can be made the larger eigenvalue by changing only `s_+/s_-`. Thus even a multiplicity-free symmetry decomposition does not canonically order its active sectors.

### Multiplicity creates matrix-valued gauge, not extra canonicity

Let `V=M\otimes W` with `\dim M=2` and `W` irreducible. Suppose

\[
B=\operatorname{diag}(1,\varepsilon),
\qquad 0<\varepsilon<1,
\tag{28}
\]

on the multiplicity space. The representation acts trivially on `M`, so every positive `2\times2` metric matrix is symmetry-compatible. Taking

\[
S=B
\tag{29}
\]

gives

\[
S^{-1/2}BS^{-1/2}=I_2.
\tag{30}
\]

Thus an apparently strong spectral separation `1:\varepsilon` can be completely flattened without violating equivariance. Repeated irreducible types are therefore exactly where symmetry leaves a matrix-valued metric ambiguity.

### Arithmetic specialization: character symmetry does not fix cross-character spectral weights

Let

\[
K=(\mathbb Z/q\mathbb Z)^\times
\]

and let `V` be the span of a finite set of distinct complex Dirichlet-character lines,

\[
V=\bigoplus_{\chi\in\Sigma}\mathbb C e_\chi,
\qquad
\rho(a)e_\chi=\chi(a)e_\chi.
\tag{31}
\]

This is a multiplicity-free representation of the finite abelian group `K`. For any equivariant map `A` into a unitary `K`-space, the reference Gram operator is diagonal by character,

\[
G_0e_\chi=b_\chi e_\chi,
\qquad b_\chi\ge0.
\tag{32}
\]

But every positive choice of character weights

\[
\langle e_\chi,e_\chi\rangle_S=s_\chi>0
\tag{33}
\]

is equally `K`-invariant, and the active Gram values become `b_\chi/s_\chi`. Therefore residue-class / character symmetry by itself cannot justify a spectral cutoff that ranks distinct nonzero character channels by Gram magnitude. A canonical arithmetic weighting would have to come from additional arithmetic or analytic structure, not from the symmetry action alone.

This is only an audit example; it does not assert that a particular Dirichlet-character construction is an RH mechanism.

## Prior art and novelty assessment

The representation-theoretic ingredients are classical. No novelty claim is made for Haar averaging, complete reducibility of compact-group representations, Schur's lemma, isotypic decomposition, the commutant formula (18), or positive congruence of Hermitian forms.

- Jean-Pierre Serre, ***Linear Representations of Finite Groups***, Graduate Texts in Mathematics 42, Springer (1977), DOI `10.1007/978-1-4684-9458-7`. Role: classical finite-group representation theory, complete reducibility, character decomposition, and Schur-lemma background; its compact-group chapter also places the unitary averaging argument in the standard setting.
- Roe Goodman and Nolan R. Wallach, ***Symmetry, Representations, and Invariants***, Graduate Texts in Mathematics 255, Springer (2009), DOI `10.1007/978-0-387-79852-3`. Role: authoritative compact/Lie-group representation and invariant-theory reference for invariant Hermitian structures, irreducible decomposition, intertwining operators, and commutants.
- William Fulton and Joe Harris, ***Representation Theory: A First Course***, Graduate Texts in Mathematics 129, Springer, DOI `10.1007/978-1-4612-0979-9`. Role: standard finite-dimensional representation-theory reference for Schur's lemma, irreducible decomposition, multiplicities, and the endomorphism algebra of a semisimple representation.
- Roger A. Horn and Charles R. Johnson, ***Matrix Analysis***, 2nd ed., Cambridge University Press (2012; digital edition 2013), DOI `10.1017/CBO9781139020411`. Role: standard Hermitian positive-definite matrix and congruence background underlying the block rescaling in (7)–(10).

The Arithmetic Fidelity result is the **exact naturality gate obtained by composing these classical mechanisms with AF-136's generator-gauge problem**. It identifies the residual gauge after imposing compact symmetry and proves a sharp dichotomy: symmetry makes the metric unique up to scale only when equivariance simultaneously makes the Gram spectrum flat; whenever a nontrivial positive equivariant Gram hierarchy is available, symmetry alone leaves enough metric freedom to change that hierarchy. This is a reusable no-go for claims that “the symmetry canonically chooses the spectral metric” without identifying the extra structure that fixes the commutant weights.

## Boundaries and falsification tests

The theorem has several deliberate boundaries.

- It concerns finite-dimensional **complex** coefficient representations of a compact group. Real irreducibles can have real, complex, or quaternionic commutants, and noncompact/nonunitary representations require a different metric-existence and commutant analysis.
- The map `A` is required to be equivariant and the destination metric invariant. If the construction breaks the symmetry, its Gram operator need not lie in the commutant and the theorem does not classify it.
- The no-go assumes that `K`-invariance is the only principle selecting the coefficient metric. A separately defined canonical norm or energy can legitimately reduce the cone (4), but that extra datum must be stated and audited.
- Rank, kernel, isotypic support, and representation type are not claimed to be lost. The adjustable quantities are positive spectral magnitudes and any ranking or cutoff based solely on them.
- A target-dependent metric can produce a meaningful target-relative compression. It is then a retained mark/lift, not a source-intrinsic metric obtained from symmetry alone.
- An overall scalar normalization never matters to spectral ordering, but independent isotypic or multiplicity-space weights do. Any claimed canonical cutoff should therefore identify exactly why those relative weights are fixed.

A decisive falsification of the present use would be a concrete arithmetic construction in which the coefficient representation is reducible but an **independently source-canonical** structure forces one particular positive commutant operator `S` up to global scale. Such an example would not contradict the theorem; it would exhibit precisely the additional data that escape its symmetry-only no-go and would become the next object for an Arithmetic Fidelity audit.

## Consequences for Arithmetic Fidelity

AF-136 reduced target-relative Gram information under unrestricted generator congruence to source-span projection geometry and required an independently justified coefficient metric before source spectral truncation could be treated as intrinsic. AF-137 closes the most obvious abstract escape: **compact symmetry alone does not provide that justification**.

The next useful question is therefore no longer whether symmetry can be invoked generically to canonize the Gram metric. For a concrete arithmetic or analytic carrier one must identify the actual source-native structure that fixes the relative commutant weights and then test whether it is stable, natural, and materially smaller than carrying the target information itself.

This also parallels the local equivariant quotient-repair result AF-079: symmetry restricts ambiguity to an intertwiner/commutant space, but declaring symmetry does not guarantee canonicity. Here the residual object is the positive cone of the coefficient commutant, and the irreducible case shows the price of eliminating it: the equivariant Gram hierarchy collapses to one flat scale.
