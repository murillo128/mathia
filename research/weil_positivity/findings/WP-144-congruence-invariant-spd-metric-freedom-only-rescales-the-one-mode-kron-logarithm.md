# WP-144 — Congruence-invariant SPD metric freedom only rescales the one-mode Kron logarithm

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + PRIME-CIRCLE + KRON-SCHUR + SPD-GEOMETRY + METRIC-CLASSIFICATION + INDEPENDENT-LOCAL-NONNEGATIVITY + MATCHED-COMPOSITE-CONTROL + GLOBAL-BRIDGE-FAILURE + PRIOR-ART-CLASSICALIZATION` for the congruence-invariant Riemannian continuation of `WP-143`.

`WP-143` identified the equal-rank Prime-Circle Kron defect with an exact one-mode affine-invariant SPD distance,

\[
d_{\rm AI}(\widehat D,\widehat L)=\log\mathcal R,
\qquad
\mathcal R=\frac{\det\widehat D}{\det\widehat L}\ge1,
\]

but left metric nonuniqueness as a live canonicality objection. The natural question is whether another Riemannian metric satisfying the **same intrinsic congruence invariance** could change the functional dependence enough to repair the Weil mismatch.

It cannot. The classical classification of Riemannian metrics on `SPD_d` invariant under the ordinary congruence action `A -> G A G^T` is

\[
g_A^{\alpha,\beta}(U,V)
=
\alpha\,\operatorname{tr}(A^{-1}UA^{-1}V)
+\beta\,\operatorname{tr}(A^{-1}U)\operatorname{tr}(A^{-1}V),
\tag{1}
\]

with

\[
\alpha>0,
\qquad
\beta>-\frac{\alpha}{d}.
\tag{2}
\]

For the Kron pair of `WP-142`--`WP-143`, the relative operator has exactly one nontrivial generalized eigenvalue,

\[
M:=\widehat D^{-1/2}\widehat L\widehat D^{-1/2}
\sim
\operatorname{diag}(1,\ldots,1,\mathcal R^{-1}).
\tag{3}
\]

Hence every metric in the full congruence-invariant family gives

\[
\boxed{
 d_{\alpha,\beta}(\widehat D,\widehat L)
 =\sqrt{\alpha+\beta}\,\log\mathcal R.
}
\tag{4}
\]

The entire metric freedom therefore collapses to one positive constant on this Mathia-native one-mode defect. It cannot remove the finite-size correction in the Prime-Circle response, turn the distance into a quadratic Weil pairing, introduce prime-power support, or generate the archimedean/global terms. The squared geodesic energy is necessarily

\[
\boxed{
 d_{\alpha,\beta}(\widehat D,\widehat L)^2
 =(\alpha+\beta)(\log\mathcal R)^2,
}
\tag{5}
\]

so the most direct positive quadratic energy actually moves farther from the required linear logarithmic local coefficient.

This closes the strongest metric-choice escape that preserves the original coordinate/congruence symmetry of the Kron operator pair. Power-affine, polar-affine, log-Euclidean, Bures--Wasserstein, deformed-affine, or other SPD geometries are not ruled out by (4), but they no longer represent alternative metrics forced by the **same** congruence action. Using one of them requires an additional Mathia principle selecting a different deformation, action, or transport geometry.

## 1. The full ordinary affine-invariant metric family

Let `SPD_d` be the cone of real symmetric positive-definite `d x d` matrices. The general linear group acts transitively by congruence,

\[
A\longmapsto GAG^T,
\qquad G\in GL_d.
\tag{6}
\]

At the identity, the stabilizer is `O(d)`. An invariant Riemannian metric is therefore determined by an `O(d)`-invariant inner product on the symmetric matrices. The classical classification gives exactly

\[
\langle X,Y\rangle_{\alpha,\beta}
=
\alpha\operatorname{tr}(XY)
+\beta\operatorname{tr}(X)\operatorname{tr}(Y),
\tag{7}
\]

with the positivity conditions (2). Transporting (7) from the identity by the congruence action gives (1).

Up to an overall scale this is a one-parameter family. Thus `WP-143` did not merely choose one metric from an uncontrolled infinite collection: once the ordinary congruence action is fixed, (1) exhausts the Riemannian possibilities.

For later use, write a normalized tangent matrix as

\[
X=A^{-1/2}UA^{-1/2}
=X_0+\frac{\tau}{d}I,
\qquad
\tau=\operatorname{tr}X,
\qquad
\operatorname{tr}X_0=0.
\tag{8}
\]

Then

\[
\|U\|_{A,\alpha,\beta}^2
=
\alpha\operatorname{tr}(X_0^2)
+\left(\frac{\alpha}{d}+\beta\right)\tau^2.
\tag{9}
\]

Equation (9) displays the geometry as the product of a determinant/scale direction and the determinant-one shape space, with constant positive weights. In particular the usual affine geodesic remains the geodesic for the whole family; only the relative weighting of scale and traceless shape changes.

For `A,B in SPD_d`, set

\[
X=\log(A^{-1/2}BA^{-1/2}).
\tag{10}
\]

The resulting squared geodesic distance is therefore

\[
\boxed{
 d_{\alpha,\beta}(A,B)^2
 =
 \alpha\operatorname{tr}(X^2)
 +\beta\bigl(\operatorname{tr}X\bigr)^2.
}
\tag{11}
\]

For `beta=0, alpha=1`, this reduces to the standard affine-invariant distance used in `WP-143`.

## 2. The Kron pair occupies only one logarithmic mode

For the equal-rank Kron construction, `WP-143` proved the exact relative spectrum

\[
\operatorname{Spec}(M)
=
\{1^{\times(d-1)},\mathcal R^{-1}\},
\qquad
\mathcal R\ge1.
\tag{12}
\]

Consequently

\[
X:=\log M
\sim
\operatorname{diag}(0,\ldots,0,-\ell),
\qquad
\ell:=\log\mathcal R\ge0.
\tag{13}
\]

Thus

\[
\operatorname{tr}(X^2)=\ell^2,
\qquad
(\operatorname{tr}X)^2=\ell^2.
\tag{14}
\]

Substituting (14) into (11) gives

\[
d_{\alpha,\beta}^2
=(\alpha+\beta)\ell^2.
\tag{15}
\]

The coefficient is strictly positive. For `d=1`, (2) says `beta>-alpha`; for `d>1`, `beta>-alpha/d>-alpha`. Hence in all dimensions relevant to the compressed Kron pair,

\[
\alpha+\beta>0.
\tag{16}
\]

Taking the positive square root proves (4).

This collapse is stronger than the observation in `WP-143` that the standard affine-invariant metric is nonunique. On the actual Mathia operator pair, **none of the congruence-invariant metric parameters changes the functional shape at all**.

## 3. Prime-Circle specialization: no invariant metric can repair the local coefficient

For the minimal one-hole Prime-Circle fiber, `WP-142` gives

\[
\mathcal R_m
=\frac{m(m+1)}{6(m-1)},
\qquad m\ge3\text{ odd},
\tag{17}
\]

so every metric (1) yields

\[
\boxed{
 d_{\alpha,\beta}(m)
 =c_{\alpha,\beta}
 \left(
 \log m-\log6+\log\frac{m+1}{m-1}
 \right),
}
\tag{18}
\]

where

\[
c_{\alpha,\beta}:=\sqrt{\alpha+\beta}>0.
\tag{19}
\]

No fixed choice of `alpha,beta` can make (18) equal `log m` for all `m`. Indeed, asymptotically

\[
d_{\alpha,\beta}(m)
=c_{\alpha,\beta}\log m-c_{\alpha,\beta}\log6+O(m^{-1}).
\tag{20}
\]

Exact equality with `log m` on an unbounded sequence would force `c_{alpha,beta}=1` from the leading logarithm, after which the nonzero constant `-log 6` remains. The exact correction `log((m+1)/(m-1))` also varies with `m` and cannot be removed by a constant normalization.

There is an even simpler finite obstruction at the degenerate endpoint: at `m=3` all conductances are equal, `R_3=1`, and every invariant distance vanishes, whereas `log 3>0`. Thus metric choice cannot turn the local Kron distance into the exact degree logarithm even before Mangoldt support or critical attenuation is considered.

The same formula holds on the odd-composite controls of `WP-142`--`WP-143`. The metric family does not introduce arithmetic discrimination absent from the conductance shape.

## 4. Why the quadratic Riemannian energy is not a hidden Weil form

One might hope that changing from distance to Riemannian energy solves the main structural objection in `WP-143`, because a squared norm is genuinely quadratic in tangent vectors. Equation (5) shows why it does not.

The logarithmic tangent displacement of the Kron relaxation has magnitude `log R`. Its positive quadratic energy is therefore proportional to `(log R)^2`, not `log R`. Polarizing the tangent norm gives a legitimate positive inner product on the finite-dimensional SPD tangent space, but its scalar on the canonical displacement is quadratic in the local logarithmic defect.

This is not the finite-prime term in the Weil explicit formula. Moreover, no construction here provides a test-function space whose polarization produces the Weil autocorrelation kernel, prime-power support with coefficient `Lambda(n)/sqrt(n)`, the Gamma contribution, or the pole/global counterterms. The local Riemannian sign remains independent and genuine, but it is the sign of the wrong object.

A nonlinear post-processing such as taking a square root of the energy simply returns the distance (4). Conversely, embedding the positive scalar `log R` into an auxiliary Hilbert norm would be a generic wrapper, not a sign theorem forced by the Kron geometry.

## 5. Canonicality boundary: changing the action is new input

The negative result is deliberately scoped to metrics invariant under the ordinary congruence action (6). This is the most natural invariance for an SPD operator pair when changes of coordinates act by congruence.

The SPD literature contains many other geometries: polar-affine and power-affine metrics, deformed-affine families, log-Euclidean metrics, Bures--Wasserstein geometry, and others. Some are obtained by pulling the affine geometry back through a nontrivial diffeomorphism or by replacing the group action under which invariance is demanded.

Those alternatives are not contradicted by (4). But they require an extra choice beyond the intrinsic pair `(Dhat,Lhat)` and its ordinary coordinate covariance. For the present research mandate this matters: metric nonuniqueness cannot itself be used as a free fitting parameter. A surviving alternative must show that Prime Circle, Prime Flute, Prime Lattice, or a genuine global completion independently forces the new deformation/action **before** its arithmetic output is inspected.

So the escape boundary is precise:

\[
\boxed{
\text{same congruence action}
+\text{any invariant Riemannian metric}
+\text{one-mode Kron relaxation}
\Longrightarrow
\text{constant}\times\log\mathcal R.
}
\tag{21}
\]

To change the functional dependence, one must change more than the metric parameter.

## 6. Prior-art and novelty audit

The metric classification is classical, not a Mathia novelty. A direct source is Yann Thanwerdas and Xavier Pennec, *Is affine-invariance well defined on SPD matrices? A principled continuum of metrics*, Geometric Science of Information (2019), arXiv:`1906.01349`. Their Section 2.1 derives the full family (1)--(2) from the `GL_d` congruence action and the `O(d)`-invariant scalar products at the identity, and explicitly notes that it is a one-parameter family up to scale. The same paper develops polar-, power-, and deformed-affine alternatives, making clear that broader metric families arise by changing the deformation/action rather than by finding additional metrics invariant under the original congruence action.

The standard `beta=0` geometry and its matrix-log geodesic distance are classical; `WP-143` already records Pennec--Fillard--Ayache, *A Riemannian Framework for Tensor Computing*, International Journal of Computer Vision 66 (2006), 41--66, DOI `10.1007/s11263-005-3222-z`. Kron reduction itself remains the classical Schur-complement construction anchored in `WP-142` by Dörfler--Bullo, *Kron Reduction of Graphs With Applications to Electrical Networks*, IEEE Transactions on Circuits and Systems I 60 (2013), 150--163, DOI `10.1109/TCSI.2012.2215780`.

A bounded directed search over affine-invariant SPD metrics, rank-one relaxations, Kron/Schur reduction, and generalized eigenvalue distances recovered these classical ingredients but did not identify an arithmetic or Weil interpretation of the specialization (4). No historical-priority claim is made for the elementary one-mode substitution. The Mathia-specific durable content is the obstruction obtained by combining the exhaustive congruence-invariant metric classification with the exact relative spectrum already derived for the canonical Prime-Circle Kron pair.

## 7. Consequence for the Weil-positivity search

`WP-140`--`WP-143` progressively separated a raw determinant anomaly from a scale-free relative determinant and then from a genuine positive SPD distance. The present result removes a remaining ambiguity in that route: **ordinary affine/congruence metric choice has no room to improve the arithmetic shape.** All invariant metrics see exactly the same one-dimensional logarithmic displacement, up to scale.

The local success therefore cannot be promoted by tuning the SPD metric. A further viable construction must add new intrinsic structure that changes one of the load-bearing facts: more than one coupled relative mode, an arithmetic selector acting before scalarization, a nonlocal coupling across prime places, an independently forced non-congruence geometry, or a finite--archimedean object formed before the positivity theorem. Any such extension still has to survive matched composite/generalized controls and produce the full Weil local-to-global decomposition with a sign theorem independent of RH.