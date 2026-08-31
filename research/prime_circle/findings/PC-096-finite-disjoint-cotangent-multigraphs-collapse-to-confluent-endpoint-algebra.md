# PC-096 — finite disjoint cotangent multigraphs collapse to confluent endpoint algebra

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-IDENTITY` + `STRUCTURAL-COLLAPSE` + `DECISIVE-BOUNDARY` for finite networks built only from the intrinsic Prime-Circle cotangent kernel, arbitrary shell-local scalar weights, and globally pairwise-disjoint vertex shells. PC-094 closed the acyclic case by Hermite's simple-pole cotangent identity but left cycles and parallel/repeated edges open because eliminating a vertex can create repeated poles. Those repeated poles do not create a new hidden-shell tensor: ordinary confluent partial fractions reduce them to finitely many one-body Cauchy jets at the neighboring endpoints. Iterating the reduction eliminates every hidden vertex of an arbitrary finite multigraph.

This does **not** cover repeated exact-order shell labels or coincidence strata, where two distinct network vertices range over the same primitive shell and the zero-diagonal convention must be reconciled with possible equal assignments. It also does not cover a genuinely different intrinsic edge operator/tensor, infinite-depth limits, Hardy/Hankel constructions, global uniformization/monodromy, or later cross-level use of the surviving endpoint jets. The exact obstruction is: **finite cyclic/loopy topology and finite edge multiplicity do not by themselves evade the endpoint-compression mechanism when the participating shell sets are globally disjoint.**

## 1. Repeated cotangent poles have a confluent endpoint reduction

For distinct nonzero circle points use the intrinsic oriented cotangent kernel

\[
K(z,u)=i\cot\!\left(\frac{\theta_z-\theta_u}{2}\right)
=-\frac{z+u}{z-u}
=\frac{z+u}{u-z}.
\]

Fix pairwise distinct endpoints `z_1,...,z_d` and positive edge multiplicities `m_1,...,m_d`. Put

\[
R(u)=\prod_{i=1}^{d}K(z_i,u)^{m_i}.
\]

As a rational function of `u`, `R` has a pole of order `m_i` at `u=z_i` and tends to `1` at infinity. Therefore its finite partial-fraction expansion is

\[
\boxed{
R(u)=1+
\sum_{i=1}^{d}\sum_{r=1}^{m_i}
\frac{A_{i,r}}{(u-z_i)^r},
}
\]

where, with

\[
G_i(u)=(u-z_i)^{m_i}R(u)
=(u+z_i)^{m_i}
\prod_{j\ne i}K(z_j,u)^{m_j},
\]

the coefficient of the pole of order `r` is exactly

\[
\boxed{
A_{i,r}
=
\frac{1}{(m_i-r)!}
\left.
\frac{d^{m_i-r}}{du^{m_i-r}}G_i(u)
\right|_{u=z_i}.
}
\]

Let `B` be a finite set disjoint from all `z_i`, and let `f:B->C` be arbitrary. Define the confluent Cauchy transforms

\[
H_{B,r}^{f}(z)
=
\sum_{u\in B}\frac{f(u)}{(u-z)^r},
\qquad
s_B(f)=\sum_{u\in B}f(u).
\]

Multiplying the partial-fraction identity by `f(u)` and summing over `B` gives the exact repeated-star formula

\[
\boxed{
\sum_{u\in B}
 f(u)\prod_{i=1}^{d}K(z_i,u)^{m_i}
=
s_B(f)
+
\sum_{i=1}^{d}\sum_{r=1}^{m_i}
A_{i,r}H_{B,r}^{f}(z_i).
}
\]

Thus a hidden shell attached through arbitrarily many parallel cotangent edges leaves only finitely many **one-body endpoint jets**. No tensor retaining the hidden index survives.

## 2. PC-094 is exactly the simple-pole case

If every `m_i=1`, then

\[
A_{i,1}
=2z_i
\prod_{j\ne i}K(z_j,z_i).
\]

Also

\[
K(z,u)=1+\frac{2z}{u-z},
\]

so for the PC-092/PC-094 transform

\[
(T_Bf)(z)=\sum_{u\in B}f(u)K(z,u)
\]

we have

\[
H_{B,1}^{f}(z)
=
\frac{(T_Bf)(z)-s_B(f)}{2z}.
\]

Substitution into the repeated-star formula recovers Hermite's simple-pole product-to-sum identity used in PC-094. The new ingredient needed for cycles is therefore not a new trigonometric law; it is only the classical confluent/repeated-pole extension of the same rational partial-fraction mechanism.

This is also the exact reason a cycle does not create a new local species merely because vertex elimination produces a parallel edge. A parallel edge raises a pole order; it does not create a new pole location or a new multibody shell index.

## 3. On primitive shells the new data are cyclotomic logarithmic-derivative jets

Take the unweighted hidden set `B=P_n^*`, so

\[
\Phi_n(z)=\prod_{u\in P_n^*}(z-u).
\]

For `z` outside the shell,

\[
\boxed{
H_{P_n^*,1}^{1}(z)
=-\frac{\Phi_n'(z)}{\Phi_n(z)}.
}
\]

Because

\[
\frac{d^{r-1}}{dz^{r-1}}\frac1{u-z}
=(r-1)!\frac1{(u-z)^r},
\]

all higher repeated-pole transforms are exactly

\[
\boxed{
H_{P_n^*,r}^{1}(z)
=
\frac1{(r-1)!}
\frac{d^{r-1}}{dz^{r-1}}
\left(-\frac{\Phi_n'(z)}{\Phi_n(z)}\right).
}
\]

Thus the first extra information created by a repeated cotangent edge is not a new shell period or a new spectral parameter. It is a finite jet of the same endpoint cyclotomic potential already exposed by PC-089. With nonconstant weights the transforms can be arithmetically richer, but they remain one-variable endpoint functions.

## 4. Arbitrary finite disjoint multigraphs close under hidden-vertex elimination

The local repeated-star identity is enough to remove cycles globally. A particularly clean proof uses the Cauchy form of each edge,

\[
K(x,y)=1+\frac{2x}{y-x}.
\]

Consider a finite multigraph `G=(V,E)`. Associate to each vertex `v` a finite set `S_v` of nonzero circle points and a scalar local weight `f_v:S_v->C`. Assume the vertex sets are **globally pairwise disjoint**. Choose any subset of vertices to remain exposed and sum over all other vertex variables. Every edge contributes one factor of `K`; parallel edges are allowed.

Expanding each `K=1+2x/(y-x)` writes the network as a finite linear combination of terms of the form

\[
\boxed{
\left(\prod_{v\in V}g_v(x_v)\right)
\left(\prod_{e=(v,w)}(x_w-x_v)^{-q_e}\right),
}
\]

where `q_e` are positive integers and all numerator monomials have been absorbed into the one-body weights `g_v`. Terms in which a chosen edge contributes its constant `1` simply omit that Cauchy edge.

Now eliminate one hidden variable `u=x_v`. Collect its distinct remaining neighbors as `z_1,...,z_d` and the total Cauchy pole multiplicity toward neighbor `i` as `m_i`. Up to an overall sign, the entire dependence on `u` is

\[
g_v(u)\prod_{i=1}^{d}(u-z_i)^{-m_i}.
\]

The repeated-pole partial fraction formula gives

\[
\prod_{i=1}^{d}(u-z_i)^{-m_i}
=
\sum_{i=1}^{d}\sum_{r=1}^{m_i}
\frac{B_{i,r}(z_1,\ldots,z_d)}{(u-z_i)^r},
\]

with

\[
\boxed{
B_{i,r}
=
\frac1{(m_i-r)!}
\left.
\frac{d^{m_i-r}}{du^{m_i-r}}
\prod_{j\ne i}(u-z_j)^{-m_j}
\right|_{u=z_i}.
}
\]

Every `B_{i,r}` is a finite linear combination of products of powers of pairwise differences `(z_i-z_j)^{-1}`. Summing `u` over its shell therefore replaces the hidden vertex by

\[
\boxed{
\sum_{i,r}
B_{i,r}(z_1,\ldots,z_d)
H_{S_v,r}^{g_v}(z_i).
}
\]

The factor `H_{S_v,r}^{g_v}(z_i)` is a new one-body weight on one surviving neighbor, while `B_{i,r}` belongs to the same finite algebra generated by pairwise Cauchy powers among the surviving vertices. If a term leaves `v` isolated, eliminating it contributes only the scalar `s_{S_v}(g_v)=sum_{u in S_v} g_v(u)`.

Therefore hidden-vertex elimination preserves the class

\[
\boxed{
\text{finite sums of one-body weights}
\times
\text{finite products of pairwise Cauchy powers}.
}
\]

Induction on the number of hidden vertices proves:

\[
\boxed{
\begin{array}{c}
\text{finite cotangent multigraph}\\
+\text{ globally pairwise-disjoint vertex shells}
\end{array}
\Longrightarrow
\text{finite confluent endpoint algebra}.
}
\]

If no vertices are exposed, the result is a scalar. If some remain exposed, the result is a finite sum of endpoint rational Cauchy-multigraph factors multiplied by nested one-body shell transforms. The number and maximal jet order are controlled by the finite graph and its edge multiplicities, **not by the cardinalities of the hidden shells**.

Cycles cause no exception to the induction. Eliminating a vertex on a cycle can create parallel edges or higher pairwise pole orders, but those are exactly the confluent terms handled at the next elimination step.

## 5. What this says about the Prime-Circle loopy escape

PC-094 correctly stopped at trees because its local engine was Hermite's distinct/simple-pole identity. The present confluent extension supplies the missing closure law for the topology it left open:

\[
\boxed{
\text{cycle / loop / parallel edge}
\not\Rightarrow
\text{irreducible finite hidden-shell tensor}
}
\]

as long as different network vertices range over globally disjoint shell sets.

For exact-order Prime-Circle shells this means that any finite network using pairwise distinct shell labels, arbitrary local scalar weights, and only the canonical cotangent edge can be eliminated completely to endpoint profiles and finite Cauchy interactions. Primality can affect the values of the one-body transforms, but it does not alter the confluent composition law.

The same proof works for arbitrary pairwise-disjoint finite sets of nonzero circle points, not merely roots of unity. Hence the mechanism has an immediate matched non-prime control. A claimed prime-specific curvature, associator, holonomy, or spectral carrier arising solely from the presence of a finite loop or a finite repeated cotangent edge must first exhibit information outside this confluent endpoint algebra.

No variable `s`, functional equation, gamma factor, zeta divisor, or critical-line selector is generated. This is a structural negative boundary, not an RH mechanism.

## 6. Prior-art and novelty audit

No historical novelty is claimed for the algebraic engine.

- PC-094 already anchors Warren P. Johnson's account of Hermite's cotangent product identity and its partial-fraction proof. The `m_i=1` case above is exactly that simple-pole mechanism.
- Repeated poles and derivative/Hermite data are the standard confluent extension of Cauchy/Cauchy-Vandermonde rational-function spaces. A directed audit of confluent Cauchy-Vandermonde and rational Hermite interpolation literature found the repeated-pole basis `1/(z-beta)^r` and multiple-pole interpolation squarely classical; there is no basis for presenting the local partial-fraction identity as new.
- The graph-elimination step is a finite induction using that classical local closure. The durable contribution is only the **Prime-Circle research boundary**: the residual finite cyclic/parallel-edge escape left by PC-094 collapses under the globally-disjoint-shell hypothesis.

The result does not classicalize the surviving one-body endpoint jets as arithmetic sequences, nor does it rule out a cross-level limit assembled from them. It only proves that finite graph topology itself does not preserve an additional hidden-shell tensor.

## 7. Stress tests and falsification controls

The theorem is finite and directly auditable.

1. For arbitrary distinct `z_i`, positive multiplicities `m_i`, and a test value `u`, compare `prod_i K(z_i,u)^{m_i}` with the displayed repeated-pole expansion using the derivative coefficients `A_{i,r}`.
2. Set every `m_i=1`; the formula must reduce exactly to the Hermite/PC-094 weighted star identity.
3. For `B=P_n^*` and `f=1`, verify that the first Cauchy transform is `-Phi_n'/Phi_n` and that higher transforms are its normalized derivatives.
4. Choose a finite cycle with at least one hidden vertex, eliminate vertices in two different orders, and compare both endpoint expressions with the direct finite sum. Finite Fubini guarantees equality; a mismatch would expose an error in the local confluent coefficients.
5. Include parallel edges so a pole of order at least two is generated. The reduction must still terminate in endpoint jets of corresponding finite order.
6. Replace primitive shells by arbitrary globally pairwise-disjoint finite point sets. The elimination law must be unchanged.

A counterexample within the globally pairwise-disjoint domain refutes the theorem. A configuration in which two network vertices range over the same exact-order shell does **not**: that is the deliberately excluded coincidence boundary, because assignments with equal coordinates interact with the `K(z,z)=0` convention rather than the rational off-diagonal formula.

## 8. Remaining frontier

Together with PC-092, PC-094 and PC-095, the finite canonical-cotangent hierarchy is now sharper:

- finite serial weighted paths collapse to endpoint displacement;
- finite pairwise-disjoint trees collapse to endpoint forest algebra;
- finite globally-disjoint **multigraphs of arbitrary topology**, including cycles and parallel edges, collapse to a confluent endpoint algebra of finite Cauchy jets.

The finite canonical-cotangent branch therefore survives only where the present proof deliberately loses its hypotheses: **repeated exact-order shell labels/coincidence strata**, or constructions using a genuinely different intrinsic operator/tensor. Infinite-depth limits, Hardy/Hankel operators, global uniformization/monodromy, and cross-level organizations of the surviving one-body jets remain separate and are not affected by this theorem.
