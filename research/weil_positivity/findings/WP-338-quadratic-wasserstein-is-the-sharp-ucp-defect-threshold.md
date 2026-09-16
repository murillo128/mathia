---
id: WP-338
title: Quadratic Wasserstein transport is the sharp UCP-defect stability threshold
branch: weil_positivity
status: supported
kind: wasserstein-ucp-rigidity-threshold
claim_strength: exact rowwise identity between quadratic transport to the source atom and Kadison variance plus barycentric bias; all Wasserstein exponents p at least 2 control the defect, while every p below 2 admits vanishing-transport growing-support Markov/UCP maps with order-one defect, including an exact-barycentric dyadic construction and the intrinsic one-sided Mangoldt witness from WP-337
created: 2026-09-16
related: [WP-332, WP-333, WP-335, WP-336, WP-337]
prior_art:
  - Cédric Villani, Optimal Transport: Old and New, Grundlehren der mathematischen Wissenschaften 338, Springer, 2009, especially the characterization of W_p convergence by weak convergence plus p-th-moment control
  - Man-Duen Choi, A Schwarz Inequality for Positive Linear Maps on C*-Algebras, Illinois Journal of Mathematics 18 (1974), 565-574, DOI 10.1215/ijm/1256051007
---

# WP-338 — Quadratic Wasserstein transport is the sharp UCP-defect stability threshold

## Claim

`WP-333`--`WP-337` show that increasingly strong notions of scalar-law or channel closeness can still miss an order-one Kadison defect when a vanishing amount of mass travels an increasing distance. A natural remaining repair is to replace those notions by a transport metric that prices distance directly.

For ordinary rowwise Wasserstein distance on the real source coordinate, that possibility can be classified exactly.

Let `Sigma` be a finite subset of the real line, let

\[
\Psi:C(\Sigma)\to C(\Sigma)
\]

be a Markov/UCP self-map, let `P_x` be its transition law at `x`, and let `X(t)=t`. Define the barycentric bias and Kadison defect

\[
\beta_x:=\Psi(X)(x)-x,
\qquad
K(x):=\Psi(X^2)(x)-\Psi(X)(x)^2.
\tag{1}
\]

For every finite `p>=1`, transport from `P_x` to the source atom `delta_x` has only one possible coupling. Hence

\[
W_p(P_x,\delta_x)^p
=
\int |y-x|^p\,dP_x(y).
\tag{2}
\]

At the quadratic exponent this gives the exact identity

\[
\boxed{
W_2(P_x,\delta_x)^2=K(x)+\beta_x^2.
}
\tag{3}
\]

Consequently, exact barycentric preservation gives

\[
\boxed{
\beta_x=0
\quad\Longrightarrow\quad
K(x)=W_2(P_x,\delta_x)^2.
}
\tag{4}
\]

More generally, for every `p>=2`, monotonicity of probability-space `L^p` norms yields

\[
0\le K(x)\le W_2(P_x,\delta_x)^2\le W_p(P_x,\delta_x)^2.
\tag{5}
\]

Thus uniform rowwise `W_p` convergence to the identity kernel forces the UCP variance defect to vanish whenever `p>=2`.

The exponent `2` is sharp on the growing supports that occur in the critical Mathia constructions. For every `1<=p<2`, there are support-preserving Markov/UCP maps with

\[
\sup_x W_p(P_x,\delta_x)\to0
\]

while

\[
\|\Psi(X^2)-\Psi(X)^2\|
\not\to0.
\]

This failure already occurs with **exact barycentric preservation** on a dyadic prime-power coordinate ray. It also occurs in the intrinsic one-sided `WP-337` Mangoldt witness while channel norm, two-sided max-divergence, and absolute barycentric bias all vanish.

Therefore the ordinary Wasserstein hierarchy does not provide a non-tautological repair of the `WP-332`--`WP-337` rigidity problem. Subquadratic transport is too weak; quadratic transport is exactly the second-moment/Kadison quantity that must be controlled; stronger exponents merely impose more than that quantity requires.

## 1. Quadratic transport is exactly defect plus squared bias

Put

\[
Z:=Y-x,
\qquad Y\sim P_x.
\]

Then

\[
\mathbb EZ=\beta_x
\]

and, exactly as in `WP-337`,

\[
K(x)=\operatorname{Var}(Z)
=\mathbb EZ^2-(\mathbb EZ)^2.
\tag{6}
\]

Since the second marginal in a transport from `P_x` to `delta_x` is deterministic, the unique coupling sends every `Y` to `x`. Therefore

\[
W_2(P_x,\delta_x)^2
=
\mathbb E|Y-x|^2
=
\mathbb EZ^2.
\tag{7}
\]

Combining (6) and (7) proves (3).

This identity matters conceptually. A proposal to repair approximate multiplicative-domain rigidity by requiring small rowwise `W_2` distance is not importing an independent geometric positivity theorem. On the source coordinate it is requiring precisely

\[
K(x)+\beta_x^2
\]

to be small. In the exact-barycentric case it is literally requiring the Kadison defect itself to be small.

For `p>=2`, the probability measure `P_x` has total mass one, so

\[
\|Z\|_{L^2(P_x)}\le \|Z\|_{L^p(P_x)}.
\]

Hence

\[
W_2(P_x,\delta_x)\le W_p(P_x,\delta_x),
\tag{8}
\]

and (5) follows.

## 2. Every subquadratic exponent misses a fixed defect

Fix `h>0` and let `a` tend to infinity. Take three points

\[
x_a-ah,
\qquad
x_a,
\qquad
x_a+ah
\]

in the finite support and let every row of `Psi_a` be deterministic except the row at `x_a`. At that row set

\[
P_{x_a}^{(a)}
=
\left(1-\frac1{a^2}\right)\delta_{x_a}
+
\frac1{2a^2}\delta_{x_a-ah}
+
\frac1{2a^2}\delta_{x_a+ah}.
\tag{9}
\]

The two displaced masses cancel in the first moment, so

\[
\boxed{\beta_{x_a}=0.}
\tag{10}
\]

The defect is nevertheless fixed:

\[
\begin{aligned}
K_a(x_a)
&=
\frac1{2a^2}(ah)^2
+
\frac1{2a^2}(ah)^2\\
&=h^2.
\end{aligned}
\tag{11}
\]

For every finite `p>=1`, however,

\[
\begin{aligned}
W_p(P_{x_a}^{(a)},\delta_{x_a})^p
&=
\frac1{2a^2}(ah)^p
+
\frac1{2a^2}(ah)^p\\
&=h^p a^{p-2}.
\end{aligned}
\tag{12}
\]

Therefore

\[
\boxed{
1\le p<2
\quad\Longrightarrow\quad
W_p(P_{x_a}^{(a)},\delta_{x_a})	o0
}
\tag{13}
\]

while `K_a(x_a)=h^2` exactly. At the threshold,

\[
W_2(P_{x_a}^{(a)},\delta_{x_a})=h,
\tag{14}
\]

as required by (4).

The map itself still converges to the identity in channel norm. The moved mass is `a^{-2}`, so

\[
\|\Psi_a-I\|=\frac2{a^2}\to0.
\tag{15}
\]

Thus the obstruction is not caused by a large channel perturbation or by barycentric drift. It is exactly the familiar rare-long-jump mechanism, now measured across the full Wasserstein exponent scale.

Equation (13) also proves a modulus-level impossibility. For any fixed `p<2`, there is no support-diameter-independent function `F_p(t)` with `F_p(t)->0` as `t->0` such that every such row satisfies

\[
K(x)\le F_p\!\left(W_p(P_x,\delta_x)\right).
\tag{16}
\]

The family (9) would make the right side tend to zero while the left side remains `h^2`.

This statement deliberately allows growing support diameter. On a uniformly bounded support, lower transport moments can control higher ones with an explicit diameter factor; that is the same propagation-price phenomenon already isolated in `WP-336` and `WP-337`, not a contradiction to (16).

## 3. The sharp witness can live on the dyadic prime-power ray

The exact-barycentric example is not forced to use an artificial continuum geometry. Take

\[
h=\log2
\]

and, for each large integer `a`, choose three dyadic prime-power coordinates

\[
y_a=a h,
\qquad
y_{2a}=2a h,
\qquad
y_{3a}=3a h.
\tag{17}
\]

These are the logarithmic coordinates of `2^a`, `2^{2a}`, and `2^{3a}`. On any finite cutoff containing all three points, modify only the row at `y_{2a}` by

\[
P_{y_{2a}}^{(a)}
=
\left(1-\frac1{a^2}\right)\delta_{y_{2a}}
+
\frac1{2a^2}\delta_{y_a}
+
\frac1{2a^2}\delta_{y_{3a}}.
\tag{18}
\]

The displacements are exactly `-a log2` and `+a log2`. Hence the same calculation gives

\[
\beta_{y_{2a}}=0,
\qquad
K_a(y_{2a})=(\log2)^2,
\tag{19}
\]

and

\[
W_p(P_{y_{2a}}^{(a)},\delta_{y_{2a}})^p
=(\log2)^p a^{p-2}.
\tag{20}
\]

So the sharp subquadratic failure is already available inside the intrinsic dyadic coordinate geometry relevant to the Mangoldt constructions. It does not require a hand-picked metric space unrelated to Mathia.

This exact-barycentric witness should not be overinterpreted as preserving every scalar source-law divergence used in `WP-333`--`WP-335`; that stronger conjunction is unnecessary for the Wasserstein threshold theorem. The next section records the complementary fact that the actual one-sided `WP-337` source-law witness also has vanishing `W_p` for every `p<2`.

## 4. The WP-337 Mangoldt witness simultaneously defeats subquadratic transport

In `WP-337`, the only modified row has moved mass

\[
\varepsilon_R=\frac1{a_R^2}
\]

across the one-sided displacement

\[
-a_Rh,
\qquad h=\log2,
\]

with `a_R->infinity`. Therefore its rowwise transport cost is exactly

\[
W_p(P_R,\delta_{y_{j_R}})^p
=
\frac1{a_R^2}(a_Rh)^p
=h^p a_R^{p-2}.
\tag{21}
\]

For every `1<=p<2`,

\[
\boxed{W_p(P_R,\delta_{y_{j_R}})\to0.}
\tag{22}
\]

But `WP-337` already proved simultaneously that

\[
\|\Psi_R-I\|\to0,
\qquad
\|\Psi_R(X_R)-X_R\|\to0,
\tag{23}
\]

that both source-law max-divergences tend to zero, and that

\[
\|K_R\|	o(\log2)^2.
\tag{24}
\]

At `p=2`, equation (21) gives

\[
W_2(P_R,\delta_{y_{j_R}})=\log2,
\tag{25}
\]

while the exact identity (3) splits that quadratic cost into the defect plus the vanishing squared bias:

\[
(\log2)^2
=
K_R(y_{j_R})+\frac{(\log2)^2}{a_R^2}.
\tag{26}
\]

Thus changing from max-divergence or channel norm to ordinary `W_1`, or indeed to any fixed `W_p` with `p<2`, does not remove the critical moving-tail obstruction. The first exponent that sees it uniformly is exactly the exponent that measures the missing second moment.

## 5. Matched generic control

Nothing in the exponent threshold uses primality. Replace `log2` by an arbitrary fixed spacing `h>0` on an equally spaced growing coordinate family. The laws (9) give exactly

\[
K_a=h^2,
\qquad
W_p^p=h^p a^{p-2}.
\tag{27}
\]

The dyadic construction therefore supplies an intrinsic realization of a generic second-moment phenomenon, not arithmetic selectivity. Any claim that the Wasserstein threshold itself is the missing Mathia-native arithmetic geometry fails the matched-control test.

## 6. Prior-art audit and novelty boundary

The underlying transport fact is classical rather than novel. Standard optimal-transport theory characterizes `W_p` convergence by weak convergence together with `p`-th-moment control; in particular a topology below quadratic moment order does not, on unbounded or growing supports, force convergence of second moments. Villani's *Optimal Transport: Old and New* is a standard reference for this `W_p`/moment characterization.

No novelty is claimed for that theorem. The repository-level delta is the exact identification of its threshold with the Mathia UCP rigidity frontier:

\[
W_2^2
=
\text{Kadison defect}
+
\text{squared barycentric bias},
\tag{28}
\]

combined with the `WP-337` intrinsic critical Mangoldt witness and the exact-barycentric dyadic control. This turns a vague possible repair — “use a transport topology that prices long jumps” — into a complete exponent classification for ordinary rowwise Wasserstein distance.

The audit did not identify a distinct prior-art mechanism in which this Wasserstein observation itself supplies an independent Weil positivity theorem, an arithmetic local-to-global pairing, an archimedean counterterm, or a new multiplicative-domain theorem. Those would be separate claims and are not made here.

## 7. Research consequence

The ordinary rowwise Wasserstein route now has a sharp boundary:

\[
\boxed{
\begin{array}{ll}
1\le p<2: & \text{too weak; vanishing }W_p\text{ can coexist with fixed UCP defect},\\[2mm]
p=2: & W_2^2=K+\beta^2\text{ exactly},\\[2mm]
p>2: & \text{stronger than the quadratic control already sufficient for }K\to0.
\end{array}
}
\tag{29}
\]

This materially narrows the `weil_positivity` search. Replacing the failed scalar divergences or channel norm by `W_1` or another subquadratic transport metric cannot recover the missing positivity. Requiring `W_2` does recover multiplicative-domain stability, but only because it directly controls the second-moment defect whose vanishing is the desired conclusion. That is not an independent geometric sign theorem.

A viable continuation therefore needs more than ordinary rowwise transport closeness. It must either produce an **independent source-side theorem** forcing the quadratic transport energy to vanish for structural arithmetic/geometric reasons, or leave this commutative rowwise category through a genuinely global or noncommutative coupling whose positivity has content beyond restating the Kadison defect.

## 8. What this does not prove

This finding does **not** rule out:

- noncommutative Wasserstein metrics whose geometry is not reducible to scalar row moments;
- globally correlated transport across several prime/local sectors;
- a canonical Dirichlet or intersection energy that independently forces quadratic transport control;
- an infinite-level boundary/cohomological construction in which the archimedean term and the finite-prime term arise from one global positive object.

It rules out the narrower repair in which ordinary rowwise `W_p` convergence is itself supposed to bridge approximate Mathia readouts to UCP multiplicative-domain rigidity without separately paying for the quadratic moment.

## Decision

This passes the substantive-finding gate as a **structural reduction and prior-art redirect**. It closes an explicit loophole left by `WP-337`: transport metrics do not provide a new continuum of possible repairs. The critical exponent is exactly quadratic, and at that exponent the proposed repair becomes the Kadison second-moment defect itself rather than an independently generated geometric positivity mechanism.
