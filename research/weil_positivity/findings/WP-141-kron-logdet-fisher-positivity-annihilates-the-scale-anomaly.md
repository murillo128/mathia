# WP-141 — Kron logdet Fisher positivity annihilates the scale anomaly

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + PRIME-CIRCLE + KRON-SCHUR + MATRIX-TREE + INFORMATION-GEOMETRIC + MATCHED-COMPOSITE-CONTROL + PRIOR-ART-CLASSICALIZATION` for the most canonical convex/Fisher rescue of the determinant-line near-miss in `WP-140`.

`WP-140` leaves a narrow but natural question. Its minimal one-hole Prime-Circle Kron response is genuinely positive, and a singular pseudodeterminant ratio contains the missing `+log m` at the native inverse-square normalization, but that logarithm is a rank/scale anomaly rather than a sign consequence. Could one recover a genuine positive object by replacing the nonlinear logarithmic determinant readout with the **canonical positive curvature of the same determinant**, namely the Hessian/Fisher metric of its spanning-tree log-partition function?

The answer is no in exactly the direction that matters. The weighted Matrix-Tree theorem turns the positive Kron pseudodeterminant into a spanning-tree partition function. In logarithmic conductance coordinates its Hessian is the covariance matrix of spanning-tree edge indicators and is therefore positive semidefinite. But every spanning tree has the same number of edges, so uniform rescaling of all conductances is a pure exponential-family gauge:

\[
\boxed{
\nabla^2 \log \tau\;\mathbf 1=0.
}
\]

The normalized weighted spanning-tree law is literally unchanged under that rescaling. Hence its Fisher length, Hessian quadratic form, and Bregman divergence are all **exactly zero** along the common scale direction. That is precisely the direction through which `WP-140` can change the coefficient of `log m` while preserving positivity of every underlying operator.

Thus the closest canonical positive geometry attached to the Kron determinant does not explain the anomalous logarithm; it quotients it out. Recovering the `log m` by integrating the first derivative along scale merely re-inserts the externally supplied path length `log m` and gives no quadratic sign theorem. This closes the route

\[
\text{positive Kron response}
\to
\text{log pseudodeterminant}
\to
\text{convex/Fisher Hessian}
\to
\text{positive source of the anomalous }\log m.
\]

The result does **not** exclude a genuinely new determinant-line metric that is not the log-partition/Fisher geometry, an equal-rank finite--archimedean relative determinant formed before normalization, or a nonseparable global construction whose positivity theorem is independent of this scale gauge.

## 1. The Kron pseudodeterminant is a spanning-tree partition function

Use the minimal one-hole response of `WP-140`. For odd `m>=3`, let

\[
L_m^{\rm mesh}
=D_m-\frac{gg^*}{s_m},
\qquad
D_m=\operatorname{diag}(g_1,\ldots,g_{m-1}),
\qquad
s_m=\sum_i g_i.
\tag{1}
\]

`WP-140` identifies this as the Laplacian of the complete star-mesh on

\[
N=m-1
\]

surviving vertices. Its effective edge conductances are

\[
\boxed{
w_{ij}=\frac{g_i g_j}{s_m}>0,
\qquad i\ne j.
}
\tag{2}
\]

Indeed,

\[
\sum_{j\ne i}w_{ij}
=\frac{g_i(s_m-g_i)}{s_m}
=g_i-\frac{g_i^2}{s_m},
\]

which is exactly the diagonal of (1), while the off-diagonal entry is `-w_ij`.

For a connected weighted graph let

\[
\tau(w):=\sum_{T\in\mathcal T}
\prod_{e\in T}w_e
\tag{3}
\]

be its weighted spanning-tree sum. The weighted Matrix-Tree theorem gives

\[
\boxed{
\det' L_m^{\rm mesh}=N\,\tau(w).
}
\tag{4}
\]

The harmless factor `N` contributes no conductance derivative. Therefore the differential geometry of the Kron pseudodeterminant is exactly the differential geometry of `log tau`.

Now introduce logarithmic edge conductances

\[
x_e:=\log w_e
\]

and define

\[
\boxed{
F(x):=\log\tau(e^x)
=\log\sum_{T\in\mathcal T}
\exp\!\left(\sum_{e\in T}x_e\right).
}
\tag{5}
\]

This is the ordinary log-partition function of the weighted spanning-tree exponential family. No regularization, analytic continuation, zero data, or fitted kernel enters (5).

## 2. Its Hessian is a canonical positive covariance form

Let

\[
P_x(T)
:=
\frac{\exp(\sum_{e\in T}x_e)}
{\sum_{T'}\exp(\sum_{e\in T'}x_e)}
\tag{6}
\]

and let `X_e(T)=1_{e in T}`. Direct differentiation of (5) gives

\[
\frac{\partial F}{\partial x_e}
=\mathbb E_x X_e,
\tag{7}
\]

and

\[
\boxed{
\frac{\partial^2F}{\partial x_e\partial x_f}
=\operatorname{Cov}_x(X_e,X_f).
}
\tag{8}
\]

Consequently

\[
\boxed{
H_x:=\nabla^2F(x)\succeq0.
}
\tag{9}
\]

For every real edge perturbation `v`,

\[
v^*H_xv
=\operatorname{Var}_x\!\left(\sum_e v_eX_e\right)
\ge0.
\tag{10}
\]

This is not positivity manufactured after seeing the desired arithmetic. It is the canonical Fisher/covariance metric of the normalized spanning-tree family (6), forced by the positive Matrix-Tree partition function itself.

The first derivative also has the standard electrical interpretation

\[
\frac{\partial F}{\partial x_e}
=P_x(e\in T)
=w_eR_{\rm eff}(e),
\tag{11}
\]

so the same construction can be read entirely in the native resistor-network language of Kron reduction.

If this Hessian retained the normalization direction responsible for `WP-140`'s logarithm, it would be a serious candidate for transferring determinant information into an independently positive quadratic object. It does not.

## 3. Fixed tree cardinality makes the common scale direction exactly null

Every spanning tree on `N=m-1` vertices has exactly

\[
r=N-1=m-2
\tag{12}
\]

edges. Therefore, for the all-ones vector `1` in edge-coordinate space,

\[
\begin{aligned}
F(x+t\mathbf1)
&=\log\sum_T
\exp\!\left(\sum_{e\in T}x_e+rt\right)\\
&=F(x)+rt.
\end{aligned}
\tag{13}
\]

Differentiating twice in `t` gives

\[
\boxed{
\mathbf1^*H_x\mathbf1=0.
}
\tag{14}
\]

Because `H_x` is positive semidefinite, (14) implies the stronger vector identity

\[
\boxed{
H_x\mathbf1=0.
}
\tag{15}
\]

Probabilistically this is even more transparent:

\[
\sum_eX_e(T)=r
\]

is deterministic under every spanning-tree law, so its variance and covariance with every statistic vanish.

The normalized law itself is invariant:

\[
\boxed{
P_{x+t\mathbf1}(T)=P_x(T)
\quad\text{for every }t\in\mathbb R.
}
\tag{16}
\]

Thus every information geometry that depends only on the normalized family sees zero displacement along common scale. In particular the Fisher line element is zero, and the Bregman divergence generated by `F` satisfies

\[
\begin{aligned}
D_F(x+t\mathbf1,x)
&=F(x+t\mathbf1)-F(x)
-\nabla F(x)\cdot(t\mathbf1)\\
&=rt-t\,\mathbb E_x\!\left[\sum_eX_e\right]\\
&=0.
\end{aligned}
\tag{17}
\]

So the failure is not that the positive metric is too small asymptotically. It is **identically blind** to the scale gauge.

## 4. This null direction is exactly the normalization freedom exposed by WP-140

`WP-140` considers a common positive scaling

\[
C_m(c)=c_mL_m^{\rm mesh},
\qquad
\Delta_m(c)=c_mD_m.
\tag{18}
\]

Scaling the Laplacian by `c_m` multiplies every effective mesh conductance (2) by `c_m`, hence in the log coordinates of (5) it is exactly

\[
x\mapsto x+(\log c_m)\mathbf1.
\tag{19}
\]

The singular determinant ratio from `WP-140` obeys

\[
\boxed{
R_m(c)
:=
\log\frac{\det' C_m(c)}{\det\Delta_m(c)}
=
\log\frac{12}{m+1}-\log c_m.
}
\tag{20}
\]

The reason is the one-rank mismatch: `C_m(c)` has `m-2` nonzero determinant directions while `Delta_m(c)` has `m-1`. Hence the ratio retains one inverse power of the common energy unit.

Equations (15)--(20) collide directly. The common scaling changes the candidate arithmetic readout by

\[
R_m(e^tc)-R_m(c)=-t,
\tag{21}
\]

while the canonical positive Hessian gives

\[
\boxed{
\|t\mathbf1\|_{H_x}^2=0
}
\tag{22}
\]

for the same deformation. In particular, at the Prime-Circle normalization

\[
c_m=(4m^2)^{-1},
\tag{23}
\]

the scale contribution contains `2 log m`, yet the Fisher geometry cannot distinguish (23) from any other positive normalization after quotienting to the normalized spanning-tree state.

This is stronger than merely repeating that `R_m` is normalization-sensitive. It shows that the **most canonical positive second-order geometry supplied by the determinant itself removes exactly the degree of freedom that makes the anomalous logarithm possible**.

The incident diagonal does not restore it. If one normalizes the positive incident weights to a probability vector

\[
q_i:=\frac{g_i}{\sum_jg_j},
\tag{24}
\]

then `q` is also invariant under `g -> e^t g`, so its Fisher/Hellinger geometry likewise has zero common-scale tangent. Keeping the unnormalized total mass instead retains the scale only as a first-order scalar, not as an intrinsic positive quadratic response.

## 5. Integrating the score merely puts `log m` in by hand

One possible escape is to avoid the Hessian and retain the first derivative. Equation (13) gives

\[
\frac{d}{dt}F(x+t\mathbf1)=r.
\tag{25}
\]

Integrating from `0` to a chosen `t_m` yields `r t_m`. But to obtain a logarithm one must already choose

\[
t_m\propto\log m.
\tag{26}
\]

Nothing in the positive covariance form chooses that path length. Moreover the derivative `r` is just the fixed cardinality of a spanning tree; it is the same for every graph with the same number of vertices and carries no prime-local information.

The same point appears from the scale score of the normalized law. Since (16) is exact,

\[
\partial_t\log P_{x+t\mathbf1}(T)=0.
\tag{27}
\]

There is therefore no hidden positive statistical fluctuation whose accumulated energy could generate the missing finite-place logarithm. The only surviving scale datum is the unnormalized partition-function degree itself.

This is precisely the datum `WP-140` identified as anomalous. Reintegrating it with an externally specified endpoint does not upgrade it to an independent sign theorem.

## 6. Exact finite check

As a finite falsification check, take a triangle with edge conductances

\[
(w_1,w_2,w_3)=(2,3,5).
\]

Its three spanning-tree weights are

\[
6,\ 10,\ 15,
\]

with total `31`. The edge-indicator covariance matrix obtained from (8) is numerically

\[
H\approx
\begin{pmatrix}
0.24973985&-0.15608741&-0.09365245\\
-0.15608741&0.21852237&-0.06243496\\
-0.09365245&-0.06243496&0.15608741
\end{pmatrix}.
\tag{28}
\]

Its eigenvalues are, to numerical precision,

\[
0,\ 0.229581125,\ 0.394768511,
\tag{29}
\]

and

\[
H(1,1,1)^T=0.
\tag{30}
\]

Directly rescaling all three conductances by `e^t` multiplies every tree weight by `e^{2t}`, so

\[
F(x+t\mathbf1)-F(x)=2t
\]

while the normalized probabilities remain `(6,10,15)/31`. This finite example checks both the PSD statement and the exact scale nullity without relying on asymptotics.

## 7. Matched controls and arithmetic specificity

Nothing in Sections 1--6 uses primality. The construction applies to every connected positive weighted graph and, in particular, to every odd composite `m` in the matched one-hole family already used by `WP-140`.

For any such `m`, the normalized spanning-tree distribution is invariant under common positive scaling. Therefore the Fisher nullity is not an arithmetic selection mechanism; it is universal fixed-cardinality combinatorics. Replacing a prime refinement by a composite refinement leaves the scale-gauge argument unchanged.

This is the correct matched control for the present claim. `WP-140` showed that the anomalous logarithm itself is composite-blind. The present result shows that passing to the determinant's canonical positive curvature does not improve arithmetic specificity: it deletes the anomalous scale before any prime/composite distinction could be made.

A nonuniform deformation can have strictly positive Fisher energy. That does not rescue this route. Nonuniform edge perturbations change the **shape** of the spanning-tree law; they are not the common normalization deformation through which (20) acquires its arbitrary logarithmic coefficient. To use them for Weil positivity one would need a new intrinsic arithmetic coupling that selects a nonuniform direction and simultaneously derives the finite and archimedean terms. That would be a new construction, not a repair of the `WP-140` anomaly.

## 8. Relation to earlier WP findings

This obstruction is not the flatness statement of `WP-083`. There the homogeneous Prime-Circle cover/Jensen family forms a flat semigroup cocycle, and exact Mangoldt support appears only at a singular inverse-scale endpoint. Here the object is the **one-hole Kron determinant**, and the null direction comes from the affine-hull equation for fixed-cardinality spanning-tree incidence vectors.

It is also distinct from `WP-084`. There the Fisher/Hellinger metric of a positive shifted cover family diverges at the covariant boundary. Here the canonical Fisher metric does the opposite: it is exactly zero in the normalization direction. The two negatives therefore constrain different attempts to extract archimedean or finite arithmetic from positive information geometry.

Finally, `WP-043` showed that a cycle-Laplacian shell logdet can recover `Lambda(n)` while its positive spectral multiplier lives in the wrong multiplication pairing. The current calculation addresses a different determinant route left open much later by `WP-140`: whether the **convex curvature of the nonlocal Kron determinant itself** can turn its normalization-sensitive logarithm into a positive quadratic mechanism. Equation (22) answers that question negatively.

## 9. Prior-art and novelty audit

All general ingredients are classical and no theorem-level novelty is claimed for them. Kirchhoff's weighted Matrix-Tree theorem identifies a Laplacian cofactor with the weighted spanning-tree sum. In exponential-family language, the Hessian of a log-partition function is the covariance matrix of its sufficient statistics; see Martin J. Wainwright and Michael I. Jordan, *Graphical Models, Exponential Families, and Variational Inference*, Foundations and Trends in Machine Learning **1** (2008), DOI `10.1561/2200000001`, especially the standard derivative/covariance identity. The spanning-tree incidence vectors lie in the affine hyperplane

\[
\sum_e X_e=N-1,
\]

which is the familiar equality in Edmonds' spanning-tree polytope. The identity `P(e in T)=w_e R_eff(e)` is likewise classical electrical-network/spanning-tree theory.

The repository audit found related but different Mathia results: `WP-043` treats primitive cycle-shell logdet versus spectral positivity; `WP-083` treats flat homogeneous Jensen cover positivity; `WP-084` treats a singular Fisher boundary of fixed-shift cover states; and `WP-140` isolates the one-rank normalization anomaly but explicitly leaves open whether a more intrinsic determinant-line geometry could repair it. None of those records the exact collision (15)--(22) between the Kron determinant's canonical covariance positivity and the scale direction that controls the anomaly.

The durable Mathia-specific content is therefore the synthesis

\[
\boxed{
\text{WP-140 scale anomaly changes the logarithmic readout}
\quad\text{while}\quad
\text{Matrix-Tree Fisher positivity assigns that same direction zero norm}.
}
\tag{31}
\]

A directed literature check found the expected classical matrix-tree, exponential-family/Fisher, effective-resistance, and spanning-tree-polytope ingredients, not a distinct Weil-positivity mechanism based on this Kron scale gauge. This is not a historical-priority claim.

## 10. Scope boundary and falsification surface

The finding rules out only the canonical log-partition/Fisher/Bregman rescue of the `WP-140` normalization anomaly. It does not classify arbitrary metrics on determinant lines, Quillen-type global metrics, equal-rank relative determinants, noncommuting dilations, or a finite--archimedean object assembled before taking a determinant.

A surviving determinant-line route must do more than retain sensitivity to scale. It must derive the scale/reference intrinsically, remove the prime-blind residual terms of `WP-140`, recover exact finite Weil coefficients, generate the Gamma/polar contribution from the same construction, survive composite controls, and possess an independent global sign theorem.

The present claim is directly falsifiable. It fails if the Kron pseudodeterminant is not a weighted spanning-tree partition function, if its log-coordinate Hessian is not the edge-indicator covariance matrix, if spanning trees in the relevant graph do not have fixed cardinality `m-2`, or if a common conductance scale changes the normalized weighted spanning-tree law. Each condition is exact, and the triangle calculation (28)--(30) provides a minimal numerical check.

## Research consequence

`WP-140` showed that the best current nonlocal Prime-Circle boundary response can manufacture the right logarithmic scale only through an unequal-rank normalization anomaly. The most natural attempt to turn that determinant into a genuine positive quadratic geometry now fails for an exact structural reason: **Fisher/covariance positivity lives on shape modulo common scale, while the anomaly lives precisely in common scale**.

The determinant route is therefore narrowed again. A viable continuation cannot obtain its sign merely by differentiating or convexifying the same Kron logdet. It needs genuinely new structure that couples arithmetic scale to a positive global pairing before the normalization gauge is quotiented out.