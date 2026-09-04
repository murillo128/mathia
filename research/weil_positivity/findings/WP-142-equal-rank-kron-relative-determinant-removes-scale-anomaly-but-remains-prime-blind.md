# WP-142 — equal-rank Kron relative determinant removes the scale anomaly but remains prime-blind

**Status:** `EXACT-DERIVED + NEAR-MISS + DECISIVE-NARROWING + PRIME-CIRCLE + KRON-SCHUR + EQUAL-RANK-RELATIVE-DETERMINANT + SCALE-INVARIANT + INDEPENDENT-LOCAL-SIGN + MATCHED-COMPOSITE-CONTROL + PRIOR-ART-CLASSICALIZATION` for the canonical equal-rank repair of the one-hole determinant route left open by `WP-140` and `WP-141`.

`WP-140` found a striking `+log m` in the minimal one-hole Prime-Circle Kron geometry, but only in a ratio of determinant lines whose ranks differ by one. The logarithm was therefore contaminated by the common energy normalization. `WP-141` then showed that the canonical positive Fisher/Hessian geometry of the same spanning-tree determinant removes precisely that common scale direction.

There is, however, a third canonical construction that survives both objections. Restrict **both** the incident diagonal and the Kron Laplacian to the common mean-zero space `1^perp`, so that their determinant lines have the same rank. The resulting relative determinant is invariant under every common positive rescaling, and its sign follows before any arithmetic interpretation from the operator inequality between unrelaxed and harmonically relaxed energies.

For the minimal Prime-Circle fiber this ratio is exactly

\[
\boxed{
\frac{\det(D_m|_{\mathbf 1^\perp})}
{\det(L_m^{\rm mesh}|_{\mathbf 1^\perp})}
=
\frac{m(m+1)}{6(m-1)}.
}
\tag{1}
\]

Consequently

\[
\boxed{
\log\frac{\det(D_m|_{\mathbf 1^\perp})}
{\det(L_m^{\rm mesh}|_{\mathbf 1^\perp})}
=
\log m-\log 6+\log\frac{m+1}{m-1}
\ge 0.
}
\tag{2}
\]

This is a genuine improvement over the `WP-140` near-miss: the leading `+log m` no longer comes from a rank/scale anomaly, and nonnegativity is independently forced by positive geometry. But it still does **not** furnish a Weil mechanism. Formula (2) is exact for every matched odd composite `m`, does not select prime powers, is not exactly `log m`, and supplies no archimedean/Gamma or global counterterm. The construction therefore isolates a new boundary: **Prime Circle can generate logarithmic growth and an intrinsic sign simultaneously from local conductance heterogeneity, but not arithmetic specificity or global Weil positivity.**

## 1. Canonical equal-rank comparison on the mean-zero space

Use the minimal one-hole geometry of `WP-140`. For odd `m>=3`, put

\[
N:=m-1,
\qquad
g_j:=\frac{1}{4\sin^2(\pi j/m)},
\qquad j=1,\ldots,N,
\tag{3}
\]

and define

\[
D_m:=\operatorname{diag}(g_1,\ldots,g_N),
\qquad
g:=(g_1,\ldots,g_N)^T,
\qquad
s_m:=\sum_{j=1}^N g_j.
\tag{4}
\]

The unnormalized Kron/star-mesh Laplacian is

\[
\boxed{
L_m^{\rm mesh}=D_m-\frac{gg^*}{s_m}\succeq0.
}
\tag{5}
\]

It has

\[
L_m^{\rm mesh}\mathbf1=0,
\qquad
\ker L_m^{\rm mesh}=\mathbb R\mathbf1,
\qquad
\operatorname{rank}L_m^{\rm mesh}=N-1.
\tag{6}
\]

The nullspace is not a chosen gauge: it is the canonical constant mode of the connected Kron Laplacian. Let

\[
H:=\mathbf1^\perp\subset\mathbb R^N
\tag{7}
\]

and let `Q:R^{N-1}->H` be any isometry. Define the two positive definite restrictions

\[
\widehat L_m:=Q^*L_m^{\rm mesh}Q,
\qquad
\widehat D_m:=Q^*D_mQ.
\tag{8}
\]

Changing `Q` only orthogonally conjugates these matrices, so their determinants are basis independent. Both live on exactly the same `(N-1)`-dimensional determinant line.

This gives the dimensionless relative determinant

\[
\boxed{
\mathcal R_m
:=
\frac{\det\widehat D_m}{\det\widehat L_m}.
}
\tag{9}
\]

Unlike the singular ratio of `WP-140`, (9) has no rank mismatch.

## 2. Common energy normalization cancels exactly

Let every conductance be multiplied by an arbitrary positive scalar `c`:

\[
g_j\mapsto cg_j.
\tag{10}
\]

Then

\[
D_m\mapsto cD_m,
\qquad
L_m^{\rm mesh}\mapsto cL_m^{\rm mesh}.
\tag{11}
\]

Because both restrictions in (8) have rank `N-1`,

\[
\det\widehat D_m\mapsto c^{N-1}\det\widehat D_m,
\qquad
\det\widehat L_m\mapsto c^{N-1}\det\widehat L_m.
\tag{12}
\]

Therefore

\[
\boxed{
\mathcal R_m(cg)=\mathcal R_m(g).
}
\tag{13}
\]

In particular, the native Prime-Circle normalization

\[
\alpha_m=(2m)^{-2}
\tag{14}
\]

plays **no role** in (9). The `+log m` derived below cannot be created by the `m^{-2}` energy scale that caused the one-zero-mode anomaly in `WP-140`.

This also explains why `WP-141` does not kill the present construction. The spanning-tree Fisher metric intentionally quotients the common scale direction. Here the same scale is quotiented already at the determinant-line level by comparing equal ranks; nontrivial information survives in the **shape/dispersion** of the conductance vector rather than in its total scale.

## 3. The equal-rank determinant ratio has a closed form for arbitrary positive conductances

The denominator is already implicit in `WP-140`. Since `L_m^{\rm mesh}` is a connected weighted Laplacian on `N` vertices, the weighted Matrix-Tree identity gives

\[
\boxed{
\det\widehat L_m
=\det' L_m^{\rm mesh}
=N\frac{\det D_m}{s_m}.
}
\tag{15}
\]

The numerator also has an exact elementary formula. For any positive diagonal

\[
D=\operatorname{diag}(g_1,\ldots,g_N)
\tag{16}
\]

and any orthonormal basis matrix `Q` for `1^perp`, Cauchy--Binet gives

\[
\det(Q^*DQ)
=
\sum_{i=1}^N
\det(Q_{\widehat i})^2
\prod_{j\ne i}g_j.
\tag{17}
\]

The codimension-one normal is `N^{-1/2}1`, hence every maximal minor of `Q` has squared determinant `1/N`. Thus

\[
\boxed{
\det(Q^*DQ)
=
\frac{\det D}{N}
\sum_{i=1}^N\frac1{g_i}.
}
\tag{18}
\]

Combining (15) and (18) yields, for **every** positive conductance vector,

\[
\boxed{
\mathcal R(g)
=
\frac{\left(\sum_i g_i\right)
\left(\sum_i g_i^{-1}\right)}{N^2}.
}
\tag{19}
\]

Equivalently, if `A(g)` and `H(g)` denote the arithmetic and harmonic means,

\[
\boxed{
\mathcal R(g)=\frac{A(g)}{H(g)}.
}
\tag{20}
\]

This representation makes both scale invariance and the eventual logarithmic growth transparent.

## 4. Nonnegativity follows independently from the geometry

On `H=1^perp`, (5) gives

\[
\widehat L_m
=
\widehat D_m-
\frac{(Q^*g)(Q^*g)^*}{s_m}.
\tag{21}
\]

Since `L_m^{mesh}` has only the constant null direction,

\[
0<\widehat L_m\le\widehat D_m.
\tag{22}
\]

For positive definite matrices, Loewner order implies determinant order, so

\[
\boxed{
\det\widehat L_m\le\det\widehat D_m,
\qquad
\log\mathcal R_m\ge0.
}
\tag{23}
\]

No zeta function, zero data, explicit-formula kernel, analytic continuation, regularization, or RH assumption enters this sign argument. The same conclusion follows from (19) by Cauchy--Schwarz / the arithmetic--harmonic mean inequality:

\[
\left(\sum_i g_i\right)
\left(\sum_i g_i^{-1}\right)
\ge N^2.
\tag{24}
\]

Equality holds exactly when all `g_i` are equal. For the Prime-Circle vector this happens at the degenerate first case `m=3`; for larger odd `m` the inequality is strict.

Thus (23) is a genuine local geometric sign theorem. It is not the global quadratic positivity sought by the research mandate, but unlike the `WP-140` determinant anomaly its sign is actually inherited from the underlying positive relaxation.

## 5. Prime Circle turns conductance heterogeneity into `log m`

For (3), the classical trigonometric sums give

\[
\boxed{
\sum_{j=1}^{m-1}g_j
=
\frac{m^2-1}{12}
}
\tag{25}
\]

and

\[
\boxed{
\sum_{j=1}^{m-1}\frac1{g_j}
=
4\sum_{j=1}^{m-1}\sin^2\frac{\pi j}{m}
=2m.
}
\tag{26}
\]

Since `N=m-1`, substituting into (19) proves

\[
\begin{aligned}
\mathcal R_m
&=
\frac{(m^2-1)(2m)}{12(m-1)^2}\\
&=
\boxed{\frac{m(m+1)}{6(m-1)}}.
\end{aligned}
\tag{27}
\]

Hence

\[
\boxed{
\log\mathcal R_m
=
\log m-\log6+\log\frac{m+1}{m-1}
=
\log m-\log6+O(m^{-1}).
}
\tag{28}
\]

The source of the logarithm is now different from `WP-140`. Indeed,

\[
A(g)
=
\frac{m+1}{12},
\qquad
H(g)
=
\frac{m-1}{2m},
\tag{29}
\]

so the ratio `A(g)/H(g)` grows linearly in `m`. The logarithm records the increasing **heterogeneity between the stiff near-hole conductances and the typical resistance scale**. Uniform rescaling cannot change it.

This is the strongest part of the near-miss: native Prime-Circle geometry supplies both a canonical dimensionless logarithmic response and an independent sign theorem.

## 6. The route still fails the Weil bridge under the required controls

### 6.1 Matched composite controls erase arithmetic specificity

Nothing in (3)--(29) uses primality. The same formulas hold for every odd composite `m` in the matched cyclic one-hole family. Therefore

\[
\boxed{
\log\mathcal R_m
=
\log m-\log6+\log\frac{m+1}{m-1}
}
\tag{30}
\]

cannot by itself detect that `m` is a new prime, a prime power, or even an arithmetic refinement rather than a matched geometric control.

The construction therefore has no intrinsic Mangoldt support selector. It produces a logarithmic cost for cyclic refinement **whether or not that refinement is prime-local**.

### 6.2 The coefficient is not exactly the finite Weil coefficient

Even on a genuine new-prime step, the local scalar is not `log m` but

\[
\log m+
\underbrace{
\left(
-\log6+\log\frac{m+1}{m-1}
\right)
}_{\displaystyle \delta_m}.
\tag{31}
\]

The residual tends to `-log 6` and also contains a nonconstant finite-size correction. Multiplying the dimensionless determinant ratio by `6(m-1)/(m+1)` would manufacture `m`, but no part of the present geometry forces that counterterm. Doing so merely to recover the explicit-formula coefficient would violate the mandate's normalization/counterterm control.

An archimedean contribution cannot simply be declared to cancel `delta_m`: the discrepancy is attached separately to every finite local refinement and is present equally in composite controls. A successful completion would have to derive any such cancellation from one larger structure.

### 6.3 A positive scalar determinant is not a global Weil quadratic form

Equation (23) proves a nonnegative **scalar log-volume defect**. It does not produce a positive sesquilinear/quadratic pairing on test functions whose local-to-global decomposition equals Weil's explicit formula.

In particular, no argument above supplies the oscillatory prime-power autocorrelation structure, the archimedean Gamma term, the pole/global counterterms, or a theorem identifying their assembled sign with (23). Promoting the scalar determinant response to a Weil kernel by hand would revert to the kind of determinant/repackaging excluded by the line contract.

### 6.4 The sign theorem is universal rather than arithmetic

The identity (20) and inequality (24) hold for every finite positive conductance vector. Their mathematical content is classical arithmetic--harmonic mean positivity. The Prime-Circle specialization is interesting because its particular inverse-square chord conductances make that universal dispersion ratio grow like `m`, not because the inequality itself knows anything about primes.

This universality is precisely the matched-control failure the Weil-positivity mandate requires us to expose.

## 7. Prior-art and novelty audit

The ingredients of the derivation are classical. Kron reduction is Schur complementation of graph Laplacians; the standard repository anchor is Dörfler--Bullo, *Kron Reduction of Graphs With Applications to Electrical Networks*, IEEE Transactions on Circuits and Systems I **60** (2013), 150--163, DOI `10.1109/TCSI.2012.2215780`. Equation (15) is the weighted Matrix-Tree theorem. Equation (18) is a codimension-one Cauchy--Binet identity, while (24) is ordinary Cauchy--Schwarz / arithmetic--harmonic mean inequality. No novelty is claimed for any of those facts.

The relevant current-repository boundary is narrower. `WP-140` compares unequal determinant ranks and proves that its `+log m` is scale anomalous. `WP-141` shows that the canonical Fisher/Hessian geometry annihilates common scale and explicitly leaves equal-rank relative determinants outside its no-go. The present result computes the most immediate equal-rank finite Kron comparison and shows that it **does** evade the scale obstruction, with the exact formula (27), but still fails arithmetic specificity and global completion.

A directed novelty check against Kron/Schur complements, weighted spanning-tree determinants, determinant monotonicity, and arithmetic--harmonic mean inequalities found only the expected classical machinery. The durable Mathia-specific contribution is therefore the exact specialization and frontier change

\[
\boxed{
\text{equal-rank Prime-Circle Kron comparison}
\Longrightarrow
\text{scale-invariant positive }\log m\text{ near-miss}
\Longrightarrow
\text{prime-blind/global-incomplete obstruction}.
}
\tag{32}
\]

This is not a historical-priority claim.

## 8. Consequence for the search frontier

`WP-140` and `WP-141` could have suggested that the only available Prime-Circle logarithm lives in a normalization anomaly that disappears as soon as one insists on genuine positive geometry. Equation (27) disproves that stronger pessimistic interpretation. **A canonical positive, scale-free relative geometry can retain logarithmic growth.**

What it retains, however, is only geometric heterogeneity. The next viable mechanism cannot be another scalar function of the same one-hole conductance profile: such a response will inherit the matched-composite blindness unless some earlier structure already distinguishes prime-power support. Nor is adding an unexplained archimedean correction after taking (28) sufficient.

A genuine escape must therefore introduce, before the final positive readout, at least one new ingredient absent here: a canonical arithmetic selector/coupling that distinguishes prime-power refinements from matched cyclic controls, and a finite--archimedean/global structure whose own positivity survives assembly. The equal-rank construction shows that **normalization is no longer the bottleneck; arithmetic specificity and global coupling are.**