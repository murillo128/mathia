# AF-138 — A source metric restores Gram spectral fidelity through a generalized pencil

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-MECHANISM`, `GAUGE-REPAIR`, `TARGET-RELATIVE`, `NO-NOVELTY-CLAIM`

## Claim

AF-136 shows that under the full invertible generator gauge the positive eigenvalue scale of a Gram matrix is not intrinsic, and AF-137 shows that compact symmetry by itself generally leaves a positive commutant cone of admissible coefficient metrics. The exact positive repair is classical: once the source independently supplies a positive-definite coefficient metric, the relevant spectral object is not the raw Gram matrix but the Hermitian-definite generalized eigenvalue pencil.

Let `H` be a complex Hilbert space, let

\[
A:\mathbb C^m\to H,
\]

and let `M>0` be a positive-definite Hermitian matrix representing an independently specified source inner product

\[
\langle x,y\rangle_M=x^*My.
\tag{1}
\]

With the ordinary coordinate adjoint define

\[
G=A^*A.
\tag{2}
\]

For a fixed target `k\in H`, also write

\[
b=A^*k,
\qquad
\kappa=\|k\|^2.
\tag{3}
\]

Then:

1. **The intrinsic source spectrum is the generalized spectrum of `(G,M)`.** The eigenvalues of
   \[
   Gx=\lambda Mx
   \tag{4}
   \]
   are exactly the eigenvalues of
   \[
   \widehat G=M^{-1/2}GM^{-1/2}
   =(AM^{-1/2})^*(AM^{-1/2}).
   \tag{5}
   \]
   Hence they are the squared singular values of `A` regarded as an operator from the Hilbert space `(\mathbb C^m,M)` to `H`.

2. **Simultaneous generator reparameterization and metric transport leave the whole generalized spectrum unchanged.** For any `R\in GL_m(\mathbb C)`, put
   \[
   A_R=AR,
   \qquad
   G_R=R^*GR,
   \qquad
   M_R=R^*MR.
   \tag{6}
   \]
   Then
   \[
   M_R^{-1}G_R
   =R^{-1}(M^{-1}G)R,
   \tag{7}
   \]
   so `(G_R,M_R)` has exactly the same generalized eigenvalues as `(G,M)`.

   More strongly, define
   \[
   U_R=M^{1/2}R M_R^{-1/2}.
   \tag{8}
   \]
   Then `U_R` is unitary and
   \[
   A_RM_R^{-1/2}=AM^{-1/2}U_R.
   \tag{9}
   \]
   Thus the metric-whitened source operators differ only by a unitary right action.

3. **The generalized Rayleigh quotient gives the coordinate-free meaning of the scale.** One has
   \[
   \frac{x^*Gx}{x^*Mx}
   =\frac{\|Ax\|^2}{\|x\|_M^2}.
   \tag{10}
   \]
   Consequently the min-max values of `(G,M)` measure source-output gain per unit of the independently declared source metric. A large generalized eigenvalue is therefore meaningful only to the extent that `M` itself is source-canonical.

4. **AF-135's target-relative fidelity defect has an exactly coordinate-invariant generalized form.** Put
   \[
   \widehat b=M^{-1/2}b
   \tag{11}
   \]
   and let `E_B` be the spectral projector of `\widehat G` for a Borel set `B\subset(0,\infty)`. Define
   \[
   \mu_{M;A,k}(B)
   :=\left\|E_B\widehat G^{\dagger/2}\widehat b\right\|^2.
   \tag{12}
   \]
   Its total mass is
   \[
   \mu_{M;A,k}((0,\infty))
   =\|P_{\operatorname{ran}A}k\|^2,
   \tag{13}
   \]
   and for a generalized spectral cutoff `\tau>0`,
   \[
   d_{M,\tau}^2
   :=\kappa-
   \left\|E_{[\tau,\infty)}\widehat G^{\dagger/2}\widehat b\right\|^2
   \tag{14}
   \]
   satisfies
   \[
   \boxed{
   d_{M,\tau}^2-
   \operatorname{dist}(k,\operatorname{ran}A)^2
   =\mu_{M;A,k}((0,\tau)).
   }
   \tag{15}
   \]
   Under `(6)`, the unitary `(8)` carries `\widehat G_R` and `\widehat b_R` to `\widehat G` and `\widehat b`, so the whole measure `(12)` is invariant.

5. **A metric known only up to global scale determines only relative spectral scale.** Replacing `M` by `cM`, `c>0`, sends every generalized eigenvalue to `\lambda/c`. Thus ordering, multiplicities, eigenvalue ratios, and dimension-based truncations survive a projectively canonical metric, whereas an absolute threshold `\lambda\ge\tau` requires a fixed normalization.

6. **Transporting the metric is essential.** If one changes generators by `R` but then silently resets the coefficient metric to the coordinate identity instead of transporting it to `R^*MR`, one has changed the mathematical source geometry rather than merely changed coordinates. The resulting raw Gram spectrum can be altered arbitrarily in the same way exposed by AF-136.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\begin{array}{c}
\text{full }GL\text{-gauge does not destroy spectral fidelity once a source metric is part of the object;}\\
\text{the invariant spectrum is the Hermitian-definite pencil }(G,M),\text{ not }G\text{ alone;}\\
\text{target-relative truncation is governed by the corresponding metric-whitened Picard tail;}\\
\text{the remaining nontrivial burden is to derive }M\text{ independently from the source.}
\end{array}}
\tag{16}
\]

This closes one side of the AF-136/AF-137 boundary. Those findings show why raw Gram spectra or symmetry-only metric choices are insufficient. AF-138 shows exactly what extra datum repairs the gauge and exactly which generalized spectral quantities become intrinsic once that datum is justified.

## Derivation

### The coefficient metric turns the synthesis map into a genuine Hilbert-space operator

The adjoint of `A:(\mathbb C^m,M)\to H` is

\[
A_M^*=M^{-1}A^*.
\tag{17}
\]

Indeed,

\[
\langle Ax,h\rangle_H
=x^*A^*h
=x^*M(M^{-1}A^*h)
=\langle x,A_M^*h\rangle_M.
\]

Therefore

\[
A_M^*A=M^{-1}G.
\tag{18}
\]

This operator is self-adjoint and positive in the `M`-inner product. The isometry

\[
J_M:(\mathbb C^m,M)\to\mathbb C^m,
\qquad
J_Mx=M^{1/2}x,
\tag{19}
\]

conjugates `(18)` to

\[
J_M(M^{-1}G)J_M^{-1}
=M^{-1/2}GM^{-1/2}
=\widehat G,
\tag{20}
\]

proving `(4)`--`(5)`. Thus the generalized eigenvalues are not an ad hoc replacement for the Gram spectrum; they are the ordinary squared singular values after expressing the declared source Hilbert geometry in orthonormal coordinates.

Equation `(10)` follows immediately from `x^*Gx=\|Ax\|^2`. Standard min-max theory for positive self-adjoint operators then gives the usual variational characterization of every generalized eigenvalue.

### Metric transport converts arbitrary generator changes into unitary gauge

For `(6)`, direct inversion gives

\[
M_R^{-1}G_R
=(R^*MR)^{-1}(R^*GR)
=R^{-1}M^{-1}GR,
\]

which proves `(7)`.

For the stronger whitening statement, compute

\[
U_R^*U_R
=M_R^{-1/2}R^*MRM_R^{-1/2}
=I,
\tag{21}
\]

so `U_R` is unitary. Also

\[
AM^{-1/2}U_R
=AM^{-1/2}M^{1/2}RM_R^{-1/2}
=ARM_R^{-1/2},
\]

which is `(9)`. Hence

\[
\widehat G_R
=U_R^*\widehat G U_R.
\tag{22}
\]

For target pairings,

\[
b_R=A_R^*k=R^*b,
\]

and

\[
\widehat b_R
=M_R^{-1/2}b_R
=M_R^{-1/2}R^*b
=U_R^*M^{-1/2}b
=U_R^*\widehat b.
\tag{23}
\]

Functional calculus applied to `(22)` now gives

\[
E_B(\widehat G_R)=U_R^*E_B(\widehat G)U_R,
\tag{24}
\]

and therefore the measure `(12)` is unchanged for every `B`.

This identifies the exact gauge repair. Declaring `M` reduces arbitrary `GL_m` coordinate freedom to ordinary unitary freedom after whitening. Every spectral statement invariant under unitary conjugacy becomes meaningful relative to that source metric.

### The target defect is the generalized Picard tail

The metric-whitened synthesis map is

\[
\widehat A=AM^{-1/2}.
\tag{25}
\]

Because `M^{-1/2}` is invertible,

\[
\operatorname{ran}\widehat A=\operatorname{ran}A.
\tag{26}
\]

Moreover

\[
\widehat A^*\widehat A=\widehat G,
\qquad
\widehat A^*k=\widehat b.
\tag{27}
\]

AF-135 therefore applies directly to `(\widehat G,\widehat b)`. It gives

\[
\|P_{\operatorname{ran}A}k\|^2
=\widehat b^*\widehat G^\dagger\widehat b
\tag{28}
\]

and splitting the spectral mass at `\tau` gives `(15)` exactly.

In a generalized eigenbasis `x_j` normalized by

\[
x_i^*Mx_j=\delta_{ij},
\qquad
Gx_j=\lambda_jMx_j,
\tag{29}
\]

the defect becomes

\[
d_{M,\tau}^2-d^2
=\sum_{0<\lambda_j<\tau}
\frac{|x_j^*b|^2}{\lambda_j}.
\tag{30}
\]

Equation `(30)` is the generalized-coordinate version of AF-135's whitened target tail. Both the denominator `\lambda_j` and the normalization of the eigenvectors are tied to the same source metric, so the expression survives arbitrary generator reparameterization when that metric is transported.

## Exact control: raw Gram order changes while the generalized spectrum does not

Take

\[
H=\mathbb C^2,
\qquad
A=\begin{pmatrix}1&0\\0&\sqrt\varepsilon\end{pmatrix},
\qquad
M=I,
\qquad 0<\varepsilon<1.
\tag{31}
\]

Then

\[
G=\operatorname{diag}(1,\varepsilon),
\]

so the generalized spectrum is `{1,\varepsilon}`.

For `L>0`, reparameterize with

\[
R_L=\operatorname{diag}(L,L^{-1}).
\tag{32}
\]

The transported data are

\[
G_L
=\operatorname{diag}(L^2,\varepsilon L^{-2}),
\qquad
M_L
=\operatorname{diag}(L^2,L^{-2}).
\tag{33}
\]

The raw Gram ordering reverses when `L^4` crosses `\varepsilon`, and its positive eigenvalue ratio can be made arbitrarily large or small. Yet

\[
G_Lx=\lambda M_Lx
\]

still has generalized eigenvalues exactly `1` and `\varepsilon` for every `L`.

Thus a basis rescaling destroys raw Gram scale but not metric-relative scale. Conversely, replacing `M_L` by `I` after `(32)` would no longer represent the same source Hilbert object; it would be a substantive metric change.

## Boundary: the theorem does not manufacture a canonical metric

AF-138 is a conditional repair, not a source of canonicity. Any positive-definite `M` makes the generalized spectrum coordinate invariant, but different independently chosen metrics generally produce different generalized spectra.

This matters especially after AF-137. A compact symmetry restricts admissible metrics to the positive cone of the commutant, but unless additional structure selects one point or ray in that cone, AF-138 yields a family of equally symmetry-compatible generalized spectra rather than one canonical hierarchy.

The following choices therefore require separate justification:

- a measure or probability law whose covariance induces `M`;
- a geometric energy or mass form;
- arithmetic weights attached intrinsically to the source generators;
- a trace normalization or local metric;
- any other source-defined positive form.

Choosing `M` from the downstream target, from the desired cutoff, or from a transformation designed specifically to flatten or sharpen `G` is a target-relative enrichment and must be audited as such. In particular, taking `M=G` on the active range trivially flattens every positive generalized eigenvalue to `1`; this is mathematically valid but carries no nontrivial source spectral ranking.

## Concrete arithmetic gate for finite Nyman-type Gram certificates

The local `CLUE-nyman-target-recovery-profile` was resolved abstractly by AF-135 but left one arithmetic question explicit: whether a finite Nyman family has a source-canonical coefficient geometry in which spectral truncation is meaningful.

AF-138 makes the required test precise. If a proposed arithmetic construction supplies positive metrics `M_n` for finite Gram matrices `G_n` and target pairing vectors `b_n`, the coordinate-invariant spectral data are

\[
\widehat G_n=M_n^{-1/2}G_nM_n^{-1/2},
\qquad
\widehat b_n=M_n^{-1/2}b_n.
\tag{34}
\]

A cutoff schedule can preserve the target distance only if its discarded generalized Picard tail

\[
\left\|E_{(0,\tau_n)}(\widehat G_n)
\widehat G_n^{\dagger/2}\widehat b_n\right\|^2
\to0.
\tag{35}
\]

The arithmetic burden is therefore twofold and cannot be bypassed by matrix algebra:

1. derive `M_n` from source-natural arithmetic or analytic structure independently of the target/RH conclusion;
2. prove a nontrivial tail estimate `(35)` in that metric.

Without the first step, the spectral hierarchy is a choice of coefficient geometry. Without the second, the hierarchy need not preserve the target observable even if it is canonical.

## Prior art and novelty assessment

No novelty claim is made for Hermitian-definite generalized eigenvalue problems, generalized singular values, metric whitening, Rayleigh quotients, or discrete Picard regularization.

- Cleve B. Moler and G. W. Stewart, **“An Algorithm for Generalized Matrix Eigenvalue Problems,”** *SIAM Journal on Numerical Analysis* 10(2), 241–256 (1973), DOI `10.1137/0710024`. Role: classical generalized matrix eigenvalue problem `Ax=lambda Bx` and its numerical treatment.
- Charles F. Van Loan, **“Generalizing the Singular Value Decomposition,”** *SIAM Journal on Numerical Analysis* 13(1), 76–83 (1976), DOI `10.1137/0713009`. Role: early generalized singular-value framework showing how a second quadratic form changes the intrinsic singular-value geometry.
- Christopher C. Paige and Michael A. Saunders, **“Towards a Generalized Singular Value Decomposition,”** *SIAM Journal on Numerical Analysis* 18(3), 398–405 (1981), DOI `10.1137/0718026`. Role: constructive GSVD and classical matrix-pair spectral structure.
- Per Christian Hansen, **“The Discrete Picard Condition for Discrete Ill-Posed Problems,”** *BIT* 30, 658–672 (1990). Role: classical target/right-hand-side weighting relative to small singular values; AF-138 transports the AF-135 Picard-tail audit to an independently declared source metric.
- Luis Báez-Duarte, **“New versions of the Nyman-Beurling criterion for the Riemann hypothesis,”** *International Journal of Mathematics and Mathematical Sciences* 31(7), 387–406 (2002), DOI `10.1155/S0161171202013248`. Role: authoritative Nyman-Beurling Hilbert-space approximation context for the concrete arithmetic gate; AF-138 proves no new Nyman theorem.

The new-to-this-line content is the exact synthesis of AF-135--AF-137 into a positive gauge-repair theorem: **a source metric converts full generator congruence into unitary gauge, the raw Gram spectrum into a generalized Hermitian-definite spectrum, and the target fidelity defect into an invariant generalized Picard tail.** The mechanism itself is classical linear algebra. Its value here is diagnostic: it states exactly what extra structure a spectral Mathia carrier must supply before spectral magnitudes can be treated as information rather than coordinates.

## Consequence for the current frontier

The abstract Gram-gauge question is now sharply separated into three cases:

1. no source metric: AF-136 reduces fixed-target fidelity to projection geometry;
2. symmetry only: AF-137 leaves the positive commutant metric gauge except in the flat irreducible regime;
3. independently justified source metric: AF-138 restores a genuine generalized spectral hierarchy and an invariant target-tail criterion.

Further generic matrix classification inside this triangle is unlikely to add much. The next useful step should be application-specific: exhibit a concrete arithmetic/analytic carrier with a source-canonical positive form and then prove or refute a target-tail estimate in the resulting generalized spectrum.