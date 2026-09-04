# WP-143 — Kron relative logdet is exactly a one-mode affine-invariant distance but not a Weil form

**Status:** `EXACT-DERIVED + GEOMETRIC-IDENTIFICATION + NEAR-MISS + PRIME-CIRCLE + KRON-SCHUR + SPD-GEOMETRY + INDEPENDENT-LOCAL-NONNEGATIVITY + MATCHED-COMPOSITE-CONTROL + GLOBAL-BRIDGE-FAILURE + PRIOR-ART-CLASSICALIZATION` for the equal-rank Kron route of `WP-142`.

`WP-142` proved that the equal-rank comparison between the compressed incident operator and its Kron relaxation has the positive, scale-invariant relative determinant

\[
\mathcal R(g)
=
\frac{\det \widehat D}{\det \widehat L}
=
\frac{\left(\sum_i g_i\right)\left(\sum_i g_i^{-1}\right)}{N^2}
=
\frac{A(g)}{H(g)}
\ge 1.
\tag{1}
\]

For the minimal Prime-Circle one-hole conductances this becomes

\[
\mathcal R_m
=
\frac{m(m+1)}{6(m-1)},
\qquad
\log \mathcal R_m
=
\log m-\log 6+\log\frac{m+1}{m-1}.
\tag{2}
\]

The scalar in (2) has a stronger geometric interpretation than was recorded in `WP-142`. The Kron relaxation changes **exactly one generalized SPD eigenmode**. Consequently, for the standard affine-invariant Riemannian metric on the cone of positive-definite matrices,

\[
\boxed{
 d_{\rm AI}(\widehat D,\widehat L)
 =
 \log \mathcal R(g).
}
\tag{3}
\]

Thus the positive logarithmic response of `WP-142` is not merely a determinant inequality: it is exactly an intrinsic SPD geodesic length for the natural unrelaxed/relaxed operator pair. Its nonnegativity follows independently from metric geometry, before any zeta or zero interpretation.

This is a genuine local geometric success, but it still fails the research mandate. The standard affine-invariant metric is classical and is not uniquely forced by Mathia; the same distance identity holds for arbitrary positive conductance stars and therefore remains prime-blind; a metric length is not a quadratic Weil pairing; its square gives `(log R)^2`, not the needed linear local coefficient; and no Gamma/archimedean or global counterterm is generated. The result therefore sharpens the frontier to: **Prime Circle contains an exact positive one-mode SPD geometry behind its local logarithmic defect, but that geometry does not globalize into Weil positivity.**

## 1. General equal-rank Kron pair

Let

\[
g=(g_1,\ldots,g_N)^T,
\qquad
g_i>0,
\qquad
s:=\sum_{i=1}^N g_i,
\qquad
D:=\operatorname{diag}(g_1,\ldots,g_N).
\tag{4}
\]

The star-mesh/Kron Laplacian is

\[
L
=
D-\frac{gg^*}{s}.
\tag{5}
\]

It is positive semidefinite with kernel spanned by the constant vector. Put

\[
\mathcal H:=\mathbf 1^\perp
\tag{6}
\]

and let `Q:R^{N-1}->H` be any isometry. As in `WP-142`, define

\[
\widehat D:=Q^*DQ>0,
\qquad
\widehat L:=Q^*LQ>0,
\qquad
v:=Q^*g.
\tag{7}
\]

Then

\[
\boxed{
\widehat L
=
\widehat D-\frac{vv^*}{s}.
}
\tag{8}
\]

The equal-rank relative determinant is

\[
\mathcal R(g)
:=
\frac{\det\widehat D}{\det\widehat L}
\ge1.
\tag{9}
\]

The inequality can already be read from `0<\widehat L\le\widehat D`, or from the exact arithmetic/harmonic-mean formula (1).

## 2. Kron relaxation moves exactly one generalized SPD eigenmode

Normalize the relaxed operator relative to the incident operator:

\[
M
:=
\widehat D^{-1/2}\widehat L\widehat D^{-1/2}.
\tag{10}
\]

From (8), with

\[
a
:=
\frac{\widehat D^{-1/2}v}{\sqrt{s}},
\tag{11}
\]

we obtain the exact rank-one form

\[
\boxed{
M=I-aa^*.
}
\tag{12}
\]

Because `\widehat L>0`, one has `\|a\|^2<1`. Therefore `M` has eigenvalue `1` with multiplicity `N-2` and one remaining eigenvalue

\[
\mu=1-\|a\|^2>0.
\tag{13}
\]

On the other hand,

\[
\det M
=
\frac{\det\widehat L}{\det\widehat D}
=
\mathcal R(g)^{-1}.
\tag{14}
\]

Since every other eigenvalue equals one,

\[
\boxed{
\mu=\mathcal R(g)^{-1}.
}
\tag{15}
\]

Equivalently, the generalized eigenvalue problem

\[
\widehat L x=\lambda\widehat D x
\tag{16}
\]

has the spectrum

\[
\boxed{
\{1,\ldots,1,\mathcal R(g)^{-1}\}.
}
\tag{17}
\]

So the determinant defect is not spread over many spectral directions. It is exactly the logarithmic displacement of the unique mode changed by harmonic relaxation.

For `N=2`, the compressed space is one-dimensional and (17) simply contains the single eigenvalue `\mathcal R^{-1}`. If all conductances are equal, `\mathcal R=1` and the displacement vanishes.

## 3. Exact affine-invariant Riemannian distance

For SPD matrices `A,B`, the standard affine-invariant Riemannian distance is

\[
d_{\rm AI}(A,B)
=
\left\|
\log\left(A^{-1/2}BA^{-1/2}\right)
\right\|_F.
\tag{18}
\]

Apply (18) to `(A,B)=(\widehat D,\widehat L)`. By (17), the eigenvalues of the relative SPD operator inside the logarithm are

\[
1,\ldots,1,\mathcal R^{-1}.
\tag{19}
\]

Hence

\[
\begin{aligned}
d_{\rm AI}(\widehat D,\widehat L)^2
&=
(N-2)(\log1)^2
+
\left(\log \mathcal R^{-1}\right)^2\\
&=
(\log\mathcal R)^2.
\end{aligned}
\tag{20}
\]

Since `\mathcal R\ge1`,

\[
\boxed{
 d_{\rm AI}(\widehat D,\widehat L)
 =
 \log\mathcal R(g).
}
\tag{21}
\]

This proves (3).

The corresponding standard affine-invariant geodesic is

\[
\gamma(t)
=
\widehat D^{1/2}
M^t
\widehat D^{1/2},
\qquad 0\le t\le1.
\tag{22}
\]

When `\mathcal R>1`, let `u=a/\|a\|`. Equation (15) gives

\[
\boxed{
M^t
=
I-\left(1-\mathcal R^{-t}\right)uu^*.
}
\tag{23}
\]

Thus the geodesic itself remains a one-mode relaxation in relative coordinates. The logarithmic coordinate is not inferred from an asymptotic determinant expansion: it is the exact geodesic displacement of that single generalized mode.

## 4. Prime Circle specialization

For the minimal one-hole Prime-Circle fiber of `WP-140`--`WP-142`, with odd `m>=3`,

\[
N=m-1,
\qquad
g_j=\frac{1}{4\sin^2(\pi j/m)},
\qquad j=1,\ldots,m-1,
\tag{24}
\]

`WP-142` proved

\[
\mathcal R_m
=
\frac{m(m+1)}{6(m-1)}.
\tag{25}
\]

Combining (21) and (25) yields the exact geometric formula

\[
\boxed{
 d_{\rm AI}(\widehat D_m,\widehat L_m)
 =
 \log\frac{m(m+1)}{6(m-1)}
 =
 \log m-\log6+\log\frac{m+1}{m-1}.
}
\tag{26}
\]

At `m=3` the conductances are equal, so the distance is zero. For `m>3` it is positive. As `m->infinity`,

\[
d_{\rm AI}(\widehat D_m,\widehat L_m)
=
\log m-\log6+O(m^{-1}).
\tag{27}
\]

This identifies the local `+log m` near-miss of `WP-142` with a bona fide positive geometric length rather than merely with a log-volume ratio.

## 5. Adversarial controls: why this still does not produce Weil positivity

### 5.1 The identity is universal for positive conductance stars

Nothing in (4)--(23) uses primality, cyclic geometry, zeta data, or even the Prime-Circle conductance law. For every positive vector `g`,

\[
d_{\rm AI}(\widehat D,\widehat L)
=
\log\frac{A(g)}{H(g)}.
\tag{28}
\]

Therefore matched arbitrary conductance stars reproduce the same mechanism. The Prime-Circle input only chooses a particular shape vector for which `A/H` grows linearly with `m`.

Likewise, the exact specialization (26) holds on the matched odd-composite one-hole controls already used in `WP-142`. The geometry has no intrinsic selector for primes or prime powers.

### 5.2 Common scaling remains invisible

For any `c>0`,

\[
\widehat D(cg)=c\widehat D(g),
\qquad
\widehat L(cg)=c\widehat L(g).
\tag{29}
\]

The affine-invariant distance is congruence/scale invariant, so

\[
\boxed{
 d_{\rm AI}(c\widehat D,c\widehat L)
 =
 d_{\rm AI}(\widehat D,\widehat L).
}
\tag{30}
\]

Thus the distance cannot recover the missing prime logarithm from the common Prime-Circle energy normalization. It only sees conductance **shape**.

### 5.3 Metric length is not the required quadratic pairing

Equation (21) gives a nonnegative distance between two local SPD operators. Weil positivity, however, is a statement about a quadratic/sesquilinear functional on a test-function space whose complete local-to-global decomposition contains finite-prime, archimedean, and global terms.

The most direct Riemannian energy is the **squared** distance,

\[
 d_{\rm AI}(\widehat D,\widehat L)^2
 =
(\log\mathcal R)^2,
\tag{31}
\]

which already changes the desired linear logarithmic coefficient. Taking the unsquared distance preserves `log R`, but a distance is not a bilinear positive form and no polarization of (21) has been derived that produces the Weil functional.

Embedding an arbitrary nonnegative scalar `x` as a squared Hilbert norm, for example through the classical Brownian representation `x=\|1_{[0,x]}\|_{L^2}^2`, would not cure this defect. It would add an external generic wrapper that works for every positive scalar, exactly the kind of tautological post-processing excluded by the mandate unless the embedding itself is forced by the Mathia geometry.

### 5.4 Positive local coefficients still do not fix the Weil autocorrelation sign

`WP-005` already established the relevant structural obstruction: a locally positive arithmetic coefficient does not remain a positive form after the natural Weil autocorrelation/translation lift. The present distance does not even equal the Mangoldt coefficient exactly, but treating its positive value as a coefficient by hand would face the same global-sign problem rather than solve it.

No construction above supplies the archimedean Gamma term, pole/global counterterms, or a single independent theorem tying those pieces to (21).

## 6. Metric-choice control

The phrase "affine-invariant distance" must not be used to smuggle uniqueness into the result. The standard metric (18) is classical and highly natural, but the SPD cone admits multiple Riemannian metric families; invariance principles alone do not force a unique geometry.

Therefore the strongest justified statement is exactly (21) **for the standard affine-invariant Riemannian metric**. Mathia has not supplied an independent axiom selecting that metric over other established SPD geometries. This is another reason the identification is a near-miss rather than a candidate global proof mechanism.

The one-mode calculation is nevertheless robust algebraically: the relative operator itself has the exact spectrum (17) before any metric is selected. Any successful continuation would have to exploit additional Mathia structure that canonically selects both a geometric functional of this one-mode displacement and a global coupling across arithmetic places.

## 7. Prior-art and novelty audit

The external ingredients are classical. The standard affine-invariant Riemannian geometry of SPD matrices, including the logarithmic relative-operator distance (18), is treated for example in Xavier Pennec, Pierre Fillard, and Nicholas Ayache, *A Riemannian Framework for Tensor Computing*, International Journal of Computer Vision **66** (2006), 41--66, DOI `10.1007/s11263-005-3222-z`. Kron reduction as Schur complementation of graph Laplacians is standard; `WP-142` already anchors Dörfler--Bullo, *Kron Reduction of Graphs With Applications to Electrical Networks*, IEEE Transactions on Circuits and Systems I **60** (2013), 150--163, DOI `10.1109/TCSI.2012.2215780`.

Metric nonuniqueness is also prior art rather than a Mathia observation. Thanwerdas--Pennec, *Is affine-invariance well defined on SPD matrices? A principled continuum of metrics* (2020), DOI `10.1007/978-3-030-26980-7_52`, and their later *O(n)-invariant Riemannian metrics on SPD matrices*, Linear Algebra and its Applications **661** (2023), 163--201, DOI `10.1016/j.laa.2022.12.009`, explicitly study families of invariant SPD metrics.

A bounded directed search over combinations of Kron/Schur reduction, affine-invariant SPD distance, rank-one relaxation, and relative determinants found the expected classical ingredients but no source was identified that assigns arithmetic or Weil significance to the particular identity (21). No historical-priority claim is made. The durable Mathia-specific contribution is the exact specialization of the already-canonical `WP-142` operator pair:

\[
\boxed{
\text{Kron rank-one relaxation}
\Longrightarrow
\text{one nontrivial generalized SPD eigenvalue}
\Longrightarrow
 d_{\rm AI}=\log(A/H)
\Longrightarrow
\text{Prime-Circle }\log m\text{ near-miss, still prime-blind/global-incomplete}.
}
\tag{32}
\]

## 8. Consequence for the search frontier

This result narrows rather than closes the geometric-positivity search.

`WP-140` showed that a raw logarithmic determinant can be only a normalization anomaly. `WP-141` showed that a canonical positive Hessian/Fisher treatment removes that anomaly. `WP-142` then found a scale-free positive relative determinant that survives. The present finding identifies the surviving scalar with an exact one-mode SPD geodesic length.

So the local finite geometry is now stronger than a determinant repackaging: **there really is an independent positive geometric distance behind the response.** What is missing is also sharper. A viable continuation must provide, from Mathia rather than by post-processing,

1. arithmetic support or a canonical coupling that distinguishes genuine prime/prime-power data from matched composite conductance controls;
2. a quadratic or sesquilinear positive structure, not merely a metric length, whose finite local term is compatible with the Weil coefficient;
3. an intrinsic archimedean/global sector in the same object; and
4. a global sign theorem surviving the autocorrelation bridge that defeats locally positive scalar constructions.

Without at least one of those additional structures, the SPD-geodesic interpretation is a geometrically exact near-miss, not a Weil-positivity mechanism.
