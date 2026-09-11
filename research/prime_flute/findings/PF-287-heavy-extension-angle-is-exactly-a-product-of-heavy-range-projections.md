# PF-287 — heavy extension angle is exactly a product of heavy range projections

**Status:** `EXACT-DERIVED + CLASSICAL-TWO-SUBSPACE-GEOMETRY + FORM-NATIVE-ENDPOINT-REDUCTION + POSITIVE/ROUTE-SHARPENING`.

[[research/prime_flute/findings/PF-282-energy-normalized-cross-form-is-a-saturated-extension-angle|PF-282]] identifies the physical mixed operator as

\[
T=F_P\Gamma F_H,
\qquad
F_P=f(|R_P|),\quad F_H=f(|R_H|),
\qquad
f(t)=\frac{t}{\sqrt{1+t^2}},
\qquad
\Gamma=V_P^*V_H,
\]

and PF-283/PF-284 reduce the endpoint to thresholded singular-value counts of

\[
\Gamma_{\alpha,\beta}=Q_P^\alpha\Gamma Q_H^\beta,
\qquad
Q_P^\alpha=\mathbf1_{[\alpha,1]}(F_P),
\qquad
Q_H^\beta=\mathbf1_{[\beta,1]}(F_H).
\]

The remaining practical difficulty is that `\Gamma` is introduced through the polar range maps `V_P,V_H`, whereas the actual prime-flute geometry is given by the nonnegative precision form `k` and its low/high restrictions. There is an exact form-native reduction that removes that mismatch.

For every fixed pair of positive strength thresholds, the heavy angle is the cross-Gram operator of two **isometric unit-energy extension maps**. Equivalently, it has exactly the same nonzero singular-value distribution as the product of the orthogonal projections onto the corresponding heavy extension ranges in the common energy space. Thus the compactness part of the live endpoint question is literally an **essential-orthogonality problem for two infinite-dimensional physical extension ranges**, and the weak-trace endpoint is its quantitative thresholded version.

More precisely, put

\[
W_P^\alpha:=V_PQ_P^\alpha,
\qquad
W_H^\beta:=V_HQ_H^\beta.
\]

Because every positive threshold lies inside the initial support of the relevant polar isometry, `W_P^\alpha` and `W_H^\beta` are isometries from the heavy input subspaces onto closed subspaces of the common energy space. If

\[
\Pi_P^\alpha:=W_P^\alpha(W_P^\alpha)^*,
\qquad
\Pi_H^\beta:=W_H^\beta(W_H^\beta)^*
\]

are the orthogonal projections onto those heavy extension ranges, then

\[
\boxed{
\Gamma_{\alpha,\beta}
=(W_P^\alpha)^*W_H^\beta,
}
\tag{1}
\]

and

\[
\boxed{
\Pi_P^\alpha\Pi_H^\beta
=W_P^\alpha\Gamma_{\alpha,\beta}(W_H^\beta)^*.
}
\tag{2}
\]

Consequently, for every `a>0`, with `N_A(a)=\operatorname{rank}\mathbf1_{(a,\infty)}(|A|)`, including the value `+\infty`,

\[
\boxed{
N_{\Gamma_{\alpha,\beta}}(a)
=N_{\Pi_P^\alpha\Pi_H^\beta}(a).
}
\tag{3}
\]

Compactness and membership in every compact two-sided symmetric ideal are therefore exactly equivalent for the thresholded angle and the corresponding projection product.

The same operator can be read directly from the physical form, without constructing `V_P,V_H`. Define

\[
\rho(\alpha):=\frac{\alpha}{\sqrt{1-\alpha^2}}.
\]

Since `f` is increasing,

\[
Q_P^\alpha=\mathbf1_{[\rho(\alpha),\infty)}(|R_P|),
\qquad
Q_H^\beta=\mathbf1_{[\rho(\beta),\infty)}(|R_H|).
\tag{4}
\]

Hence `|R_P|^{-1}` and `|R_H|^{-1}` are bounded on the respective heavy subspaces. For

\[
x\in\operatorname{Ran}Q_P^\alpha,
\qquad
y\in\operatorname{Ran}Q_H^\beta,
\]

one has the exact identity

\[
\boxed{
\langle x,\Gamma_{\alpha,\beta}y\rangle
=
k\!\left[|R_P|^{-1}x,\ |R_H|^{-1}y\right].
}
\tag{5}
\]

Thus the live angle can be attacked as an **unshifted diagonal-energy-normalized low/high cross form**. No polar-decomposition estimate is required. In any compatible operator-block realization where the off-diagonal form is represented by `B`, equation (5) is the thresholded form version of

\[
Q_P^\alpha |R_P|^{-1} B |R_H|^{-1} Q_H^\beta,
\]

but (5), not existence of a globally bounded `B`, is the invariant statement.

Combining (3) with PF-284 gives the endpoint sandwich directly in heavy-range geometry:

\[
\boxed{
N_T(a+\alpha+\beta)
\le
N_{\Pi_P^\alpha\Pi_H^\beta}(a)
\le
N_T(\alpha\beta a).
}
\tag{6}
\]

Therefore `T` is compact if and only if every fixed positive-threshold pair of heavy extension ranges is essentially orthogonal, and weak trace class forces the quantitative necessary condition

\[
\boxed{
\sup_{\alpha,\beta,a>0}
\alpha\beta a\,
N_{\Pi_P^\alpha\Pi_H^\beta}(a)<\infty.
}
\tag{7}
\]

Conversely, the PF-283 matched sufficient criterion becomes

\[
\boxed{
N_{\Pi_P^\tau\Pi_H^\tau}(2\tau)=O(\tau^{-1})
\Longrightarrow
T\in\mathcal S_{1,\infty}.
}
\tag{8}
\]

PF-286 shows that neither heavy range can be discarded by finite-rank strength truncation. Equations (3)--(8) therefore sharpen the surviving physical question: determine whether the **unit-energy low-fed and high-fed extension ranges themselves become quantitatively orthogonal**, despite both carrying infinitely many heavy channels.

## Claim

Under the hypotheses and notation of PF-282--PF-284, for every `0<\alpha,\beta<1`:

1. `W_P^\alpha=V_PQ_P^\alpha` and `W_H^\beta=V_HQ_H^\beta` are isometries from the heavy input subspaces onto closed heavy extension ranges;
2. `\Gamma_{\alpha,\beta}` is their cross-Gram operator, and its counting function agrees exactly with that of the product of the two heavy-range projections as in (3);
3. for every compact two-sided symmetric ideal `\mathcal J`,
   \[
   \Gamma_{\alpha,\beta}\in\mathcal J
   \iff
   \Pi_P^\alpha\Pi_H^\beta\in\mathcal J;
   \]
4. the thresholded angle is represented directly by the normalized cross form (5);
5. `T` is compact if and only if `\Pi_P^\alpha\Pi_H^\beta` is compact for every positive `\alpha,\beta`;
6. the PF-283/PF-284 endpoint criteria are exactly the projection-product counts (6)--(8);
7. a fixed-threshold noncompactness obstruction can be certified by finite energy-normalized cross-Gram matrices of arbitrarily large dimension.

The last point gives a concrete falsifier. Fix `\alpha,\beta` and suppose there is `c>0` such that for every `m` one can find orthonormal heavy vectors

\[
x_1,\ldots,x_m\in\operatorname{Ran}Q_P^\alpha,
\qquad
y_1,\ldots,y_m\in\operatorname{Ran}Q_H^\beta
\]

for which the `m\times m` matrix

\[
G_m(i,j)
:=
k\!\left[|R_P|^{-1}x_i,\ |R_H|^{-1}y_j\right]
\tag{9}
\]

satisfies `s_m(G_m)\ge c`. Then

\[
N_{\Pi_P^\alpha\Pi_H^\beta}(c/2)=\infty,
\]

so the heavy projection product, `\Gamma_{\alpha,\beta}`, and `T` are noncompact. In particular the weak-trace endpoint fails before any finer counting asymptotic is needed.

## 1. Heavy polar maps are isometries

For the polar decomposition

\[
R_P=V_P|R_P|,
\]

one has

\[
V_P^*V_P=\operatorname{supp}|R_P|.
\]

Because `\alpha>0`, equation (4) gives

\[
Q_P^\alpha\le\operatorname{supp}|R_P|.
\]

Therefore

\[
(W_P^\alpha)^*W_P^\alpha
=Q_P^\alpha V_P^*V_PQ_P^\alpha
=Q_P^\alpha.
\tag{10}
\]

So `W_P^\alpha` is an isometry when its domain is restricted to `\operatorname{Ran}Q_P^\alpha`. Its range is closed, and `\Pi_P^\alpha=W_P^\alpha(W_P^\alpha)^*` is the orthogonal projection onto it. The same argument applies on the `H` side.

Using `\Gamma=V_P^*V_H`,

\[
(W_P^\alpha)^*W_H^\beta
=Q_P^\alpha V_P^*V_HQ_H^\beta
=\Gamma_{\alpha,\beta},
\tag{11}
\]

which proves (1). Multiplying by the isometries gives

\[
\Pi_P^\alpha\Pi_H^\beta
=W_P^\alpha\Gamma_{\alpha,\beta}(W_H^\beta)^*,
\tag{12}
\]

and conversely

\[
\Gamma_{\alpha,\beta}
=(W_P^\alpha)^*(\Pi_P^\alpha\Pi_H^\beta)W_H^\beta.
\tag{13}
\]

Thus any two-sided ideal contains one operator exactly when it contains the other.

For the counting identity, note that

\[
(\Pi_P^\alpha\Pi_H^\beta)^*
(\Pi_P^\alpha\Pi_H^\beta)
=
W_H^\beta\Gamma_{\alpha,\beta}^*\Gamma_{\alpha,\beta}(W_H^\beta)^*.
\tag{14}
\]

On the orthogonal complement of `\operatorname{Ran}W_H^\beta` the left side is zero. Its positive spectral part is therefore isometrically equivalent to `\Gamma_{\alpha,\beta}^*\Gamma_{\alpha,\beta}`, proving (3) without assuming compactness.

## 2. The same angle is the unshifted normalized physical cross form

The threshold relation (4) implies

\[
\bigl\||R_P|^{-1}Q_P^\alpha\bigr\|
\le\rho(\alpha)^{-1},
\qquad
\bigl\||R_H|^{-1}Q_H^\beta\bigr\|
\le\rho(\beta)^{-1}.
\tag{15}
\]

For heavy vectors `x,y`, put

\[
u=|R_P|^{-1}x,
\qquad
v=|R_H|^{-1}y.
\]

These vectors lie in the diagonal form domains and have canonical energy extensions

\[
R_Pu=V_Px,
\qquad
R_Hv=V_Hy.
\tag{16}
\]

The defining form identity from PF-282 then gives

\[
\begin{aligned}
k[u,v]
&=\langle R_Pu,R_Hv\rangle\\
&=\langle V_Px,V_Hy\rangle\\
&=\langle x,Q_P^\alpha V_P^*V_HQ_H^\beta y\rangle,
\end{aligned}
\tag{17}
\]

which is (5).

This is the useful computational form of the theorem. The vectors `u,v` are normalized by their **unshifted diagonal extension energies**, not by the shifted factors `I+K_P` and `I+K_H`. The lower strength threshold makes this normalization bounded. Hence a geometric estimate of cross energy on heavy channels is exactly an estimate of the angle operator; there is no additional polar-map loss to pay.

In a block-operator model one may write this symbolically as a diagonally normalized off-diagonal form. If the full precision operator happens to admit the relevant block action, it is also the normalized failure of the physical `P/H` splitting to reduce that precision operator. The form statement (17) is deliberately stronger as a workflow interface because it remains valid even when the raw off-diagonal block is not bounded.

## 3. Compactness is essential orthogonality of the physical heavy ranges

For two closed subspaces with orthogonal projections `\Pi_1,\Pi_2`, the condition `\Pi_1\Pi_2` compact is commonly called **essential orthogonality**. Equations (1)--(3) show that this classical two-subspace notion is exactly the fixed-threshold compactness gate in Prime Flute.

There is also a direct sequence criterion. For fixed `\alpha,\beta`, `\Gamma_{\alpha,\beta}` is compact if and only if every orthonormal sequence `y_n` in `\operatorname{Ran}Q_H^\beta` satisfies

\[
\boxed{
\sup_{\substack{x\in\operatorname{Ran}Q_P^\alpha\\\|x\|=1}}
\left|
k\!\left[|R_P|^{-1}x,\ |R_H|^{-1}y_n\right]
\right|
\longrightarrow0.
}
\tag{18}
\]

Indeed the supremum is exactly `\|\Gamma_{\alpha,\beta}y_n\|` by (5), and a bounded Hilbert-space operator is compact exactly when it sends every orthonormal sequence to a norm-null sequence.

This criterion is stronger operationally than merely naming a principal angle. It says what must actually be proved on the one-cusp pant: every orthonormal family of **unit-energy physical-high heavy extensions** must lose uniform correlation with the entire physical-low heavy extension range.

The full compactness statement follows from PF-284. If `T` is compact then every fixed heavy compression `\Gamma_{\alpha,\beta}` and hence every projection product is compact. Conversely, if all fixed-threshold products are compact, then the matched heavy block

\[
T_{\tau,\tau}=Q_P^\tau TQ_H^\tau
\]

is compact for every `\tau>0`, while PF-284 gives

\[
\|T-T_{\tau,\tau}\|\le2\tau.
\]

Thus `T` is a norm limit of compact operators.

## 4. Finite cross-Gram witnesses give a decisive negative test

Let `X_m,Y_m:\mathbb C^m\to\mathcal H` be the isometries with columns `x_i,y_j` from (9). By (5),

\[
X_m^*\Gamma_{\alpha,\beta}Y_m=G_m.
\tag{19}
\]

Compression cannot increase approximation numbers, so

\[
s_m(G_m)\le s_m(\Gamma_{\alpha,\beta})
\]

whenever the latter is interpreted through approximation numbers; equivalently, the spectral counting rank of `|\Gamma_{\alpha,\beta}|` above any threshold below `c` is at least `m`. If such witnesses exist for arbitrarily large `m`, then (3) gives

\[
N_{\Pi_P^\alpha\Pi_H^\beta}(c/2)=\infty.
\tag{20}
\]

PF-284 then gives

\[
N_T(\alpha\beta c/2)=\infty,
\tag{21}
\]

so `T` is not compact and cannot belong to `\mathcal S_{1,\infty}`.

This is a materially cheaper falsifier than attempting the full small-threshold asymptotic first. A single fixed pair `\alpha,\beta` with arbitrarily large uniformly correlated unit-energy families kills the endpoint. Only if all such fixed-threshold obstructions are absent is it necessary to measure the finer `\tau\downarrow0` counting law.

## 5. Consequence for the current Prime-Flute frontier

PF-286 proves that the canonical physical low and high strength factors each have infinite-dimensional heavy sectors. That result by itself says nothing about their relative position in the common energy space. The present reduction identifies the missing object without an additional abstract layer:

\[
\boxed{
\text{heavy endpoint geometry}
=
\text{cross energy of unit-energy low/high extensions}
=
\text{product of heavy extension-range projections}.
}
\]

The next physical calculation should therefore not perform another census of the eigenvalues of `F_P` or `F_H`. It should estimate (18), or construct/refute the finite witnesses (9), for the actual simultaneous one-cusp-pant extension after the physical `P/H` split has been fixed.

PF-231 remains useful as a calibration because the untrimmed ultraparallel corridor has an exact separable energy representation. But PF-231 itself explicitly leaves the PF-205 hypercycle trim, physical projectors, neighboring-cell inhomogeneity, and global Schur inversion as the places where mode mixing enters. The present finding does **not** infer essential orthogonality from that separability. It says that those remaining geometric effects should now be measured by their contribution to the unit-energy cross form / projection product rather than by raw reservoir mass or channel count.

## 6. Prior art and novelty audit

The general geometry is classical. Galántai, *Subspaces, angles and pairs of orthogonal projections*, Linear and Multilinear Algebra 56 (2008), 227--260, DOI `10.1080/03081080600743338`, treats principal angles and pairs of orthogonal projections in the standard two-subspace framework. Andruchow--Corach, *Essentially orthogonal subspaces*, Journal of Operator Theory 79 (2018), 79--100, DOI `10.7900/jot.2016dec13.2138`, explicitly studies pairs of projections `P,Q` for which `PQ` is compact. Andruchow--Corach, *Schmidt decomposable products of projections*, Integral Equations and Operator Theory 89 (2017), DOI `10.1007/s00020-017-2402-x`, further treats singular values of products of projections.

Accordingly, **no novelty is claimed for principal angles, projection products, or the term essential orthogonality**. The project-specific contribution is the exact identification of the PF-282/PF-284 thresholded physical extension angle with the product of the corresponding heavy energy-range projections, together with the form-native identity (5) and its endpoint/witness consequences for the canonical Prime-Flute split.

No external theorem is needed for equations (1)--(21); they are derived directly from the polar decomposition already established in PF-282, spectral thresholding, and elementary Hilbert-space projection calculus. The literature audit fixes the correct classical context and prevents repackaging two-subspace geometry as a new general theorem.

## 7. Boundaries and falsification discipline

This finding does **not** prove that the physical heavy ranges are essentially orthogonal, compactly correlated, or weak-trace correlated. PF-286 makes both heavy spaces infinite-dimensional; it does not choose their angle. Conversely, absence of a fixed-threshold noncompactness witness proves only compactness if it is established uniformly for every orthonormal sequence as in (18); failure to find a witness is not evidence of compactness.

The `O(\tau^{-1})` matched projection count in (8) remains a sufficient route, not a necessary one. PF-284's weighted statistic is the genuine necessary test. A physical estimate may therefore close the endpoint through an asymmetric or threshold-dependent law even if the clean matched count is too large.

The projection formulation is invariant only after the physical `P/H` split and the diagonal energies are fixed. Replacing those projectors by a coordinate split that diagonalizes a convenient model would change the question. Likewise, separability of an isolated corridor does not establish the projection-product estimate for the completed pant or the globally reassembled flute.

Finally, even `T\in\mathcal S_{1,\infty}` would close only the current mixed weak-trace reassembly gate identified by PF-281. It would not by itself produce a trace formula, relative determinant, zeta-zero correspondence, critical-line theorem, or Riemann Hypothesis consequence.