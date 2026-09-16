---
id: WP-339
title: Quadratic tail growth is the exact general transport-cost threshold
branch: weil_positivity
status: supported
kind: general-transport-cost-ucp-rigidity-threshold
claim_strength: exact necessary-and-sufficient tail-growth dichotomy for scalar displacement costs to force vanishing Kadison defect under channel convergence; any cost asymptotically weaker than quadratic admits exact-barycentric rare-long-jump counterexamples, while an eventual quadratic lower bound gives a uniform defect estimate; the dyadic prime-power ray realizes the same obstruction for every cost subquadratic along that intrinsic lattice
created: 2026-09-16
related: [WP-332, WP-333, WP-335, WP-336, WP-337, WP-338]
prior_art:
  - Cédric Villani, Optimal Transport: Old and New, Grundlehren der mathematischen Wissenschaften 338, Springer, 2009, especially Wasserstein convergence and moment control
  - Karl-Theodor Sturm, Generalized Orlicz Spaces and Wasserstein Distances for Convex-Concave Scale Functions, Bulletin des Sciences Mathématiques 135 (2011), 795-802, DOI 10.1016/j.bulsci.2011.07.013
  - classical Vitali/de la Vallée-Poussin uniform-integrability criteria for convergence of moments
  - Man-Duen Choi, A Schwarz Inequality for Positive Linear Maps on C*-Algebras, Illinois Journal of Mathematics 18 (1974), 565-574, DOI 10.1215/ijm/1256051007
---

# WP-339 — Quadratic tail growth is the exact general transport-cost threshold

## Claim

`WP-338` classified the power-cost hierarchy: rowwise `W_p` control forces the Markov/UCP Kadison defect to vanish for `p>=2`, while every `p<2` admits rare-long-jump counterexamples with order-one defect. A natural escape is to replace the power cost by a more tailored transport penalty: truncated quadratic cost, Huber cost, an Orlicz cost, a slowly varying correction to `r^2`, or some other scalar function of displacement.

For the source-coordinate readout, this entire class can be classified exactly.

Let `Sigma` be a finite subset of the real line, let

\[
\Psi:C(\Sigma)\to C(\Sigma)
\]

be a Markov/UCP self-map, let `P_x` be its transition law at `x`, and let `X(t)=t`. Write

\[
\varepsilon_x:=1-P_x(\{x\}),
\qquad
K(x):=\Psi(X^2)(x)-\Psi(X)(x)^2.
\tag{1}
\]

For a finite nonnegative Borel cost

\[
c:[0,\infty)\to[0,\infty),
\qquad c(0)=0,
\]

define the rowwise displacement cost

\[
J_c(x):=
\int c(|y-x|)\,dP_x(y).
\tag{2}
\]

Transport to the atom `delta_x` has a unique coupling, so `J_c(x)` is exactly the corresponding scalar optimal-transport cost from `P_x` to `delta_x`.

Then the large-displacement growth of `c` gives a sharp dichotomy.

### Positive side

If there exist `R_0<infinity` and `a>0` such that

\[
c(r)\ge a r^2
\qquad(r\ge R_0),
\tag{3}
\]

then

\[
\boxed{
K(x)
\le
R_0^2\varepsilon_x
+a^{-1}J_c(x).
}
\tag{4}
\]

Consequently,

\[
\boxed{
\|K\|
\le
\frac{R_0^2}{2}\|\Psi-I\|
+a^{-1}\sup_xJ_c(x).
}
\tag{5}
\]

Thus channel convergence together with vanishing `c`-transport cost forces the Kadison defect to vanish whenever `c` eventually dominates a quadratic cost.

### Negative side

Conversely, if

\[
\boxed{
\liminf_{r\to\infty}\frac{c(r)}{r^2}=0,
}
\tag{6}
\]

then there are finite-support Markov/UCP maps satisfying simultaneously

\[
\|\Psi_n-I\|\to0,
\qquad
\Psi_n(X)(x_n)=x_n,
\qquad
J_c(x_n)\to0,
\tag{7}
\]

while

\[
\boxed{K_n(x_n)=1}
\tag{8}
\]

exactly. The counterexample has **exact barycentric preservation**, not merely asymptotic preservation.

Therefore, among scalar displacement penalties combined with channel convergence, eventual quadratic tail growth is the exact universal threshold for controlling the source-coordinate UCP defect. Any genuinely gentler tail penalty fails; any successful one already contains the missing quadratic-moment control in its tail.

For the intrinsic dyadic prime-power coordinate spacing `h=log 2`, the same statement holds with the continuous tail ratio replaced by the lattice ratio

\[
\rho_c^{(h)}
:=
\liminf_{a\to\infty}
\frac{c(ah)}{(ah)^2}.
\tag{9}
\]

If `rho_c^(h)=0`, the exact-barycentric counterexample lies entirely on the dyadic ray. In particular every standard asymptotically subquadratic cost with `c(r)/r^2->0` fails intrinsically on that Mathia-native coordinate geometry.

This closes a broad transport-cost escape left by `WP-338`. It does **not** produce Weil positivity. The threshold is a generic second-moment fact, survives matched non-arithmetic controls, and says that scalar transport can repair the UCP route only by explicitly pricing the very quadratic tail moment whose failure generates the Kadison defect.

**Classification:** `EXACT-DERIVED + LITERATURE-BACKED + GENERAL-COST + SHARP-DICHOTOMY + UCP-READOUT + QUADRATIC-TAIL + EXACT-BARYCENTER + DYADIC-INTRINSIC-WITNESS + MATCHED-CONTROL + DECISIVE-NEGATIVE + NOT-WEIL-POSITIVITY`.

## 1. The defect is bounded by the raw second displacement moment

Fix a row `x`, let `Y` have law `P_x`, and put

\[
Z:=Y-x.
\tag{10}
\]

As in `WP-337` and `WP-338`,

\[
K(x)=\operatorname{Var}(Z).
\tag{11}
\]

Hence

\[
0\le K(x)
\le
\mathbb E Z^2.
\tag{12}
\]

The probability that `Z` is nonzero is exactly

\[
\mathbb P(Z\ne0)=\varepsilon_x.
\tag{13}
\]

For a Markov kernel on `C(Sigma)`, row total variation gives

\[
\|\Psi-I\|=2\sup_x\varepsilon_x.
\tag{14}
\]

So the issue is purely whether the proposed displacement cost can control the second moment of a vanishing amount of off-diagonal mass uniformly as the available propagation radius grows.

## 2. Eventual quadratic domination gives the uniform estimate

Assume (3). Split the second moment at `R_0`:

\[
\mathbb E Z^2
=
\mathbb E\!\left[Z^2;0<|Z|<R_0\right]
+
\mathbb E\!\left[Z^2;|Z|\ge R_0\right].
\tag{15}
\]

The bounded part satisfies

\[
\mathbb E\!\left[Z^2;0<|Z|<R_0\right]
\le
R_0^2\varepsilon_x.
\tag{16}
\]

On the tail, (3) gives

\[
Z^2\le a^{-1}c(|Z|),
\]

so

\[
\mathbb E\!\left[Z^2;|Z|\ge R_0\right]
\le
a^{-1}J_c(x).
\tag{17}
\]

Combining (12), (16), and (17) proves (4). Taking suprema and using (14) proves (5).

No barycentric hypothesis is needed for this direction. The estimate controls the raw second displacement moment, which is stronger than controlling its centered variance.

The conclusion is uniform over support diameter. That is the important point: once the cost pays at least a fixed positive multiple of `r^2` for sufficiently large `r`, rare mass cannot escape to a diverging distance without being seen at the same scale as the Kadison defect.

## 3. Any asymptotic dip below quadratic permits a fixed defect

Assume (6). Choose `r_n->infinity` such that

\[
\frac{c(r_n)}{r_n^2}\to0.
\tag{18}
\]

On the three-point support

\[
\Sigma_n=\{-r_n,0,r_n\},
\]

let every row of `Psi_n` be deterministic except the row at `0`, and set

\[
P_0^{(n)}
=
\left(1-\frac1{r_n^2}\right)\delta_0
+
\frac1{2r_n^2}\delta_{-r_n}
+
\frac1{2r_n^2}\delta_{r_n}.
\tag{19}
\]

For sufficiently large `n`, this is a probability law. The displaced masses are symmetric, so

\[
\boxed{\Psi_n(X)(0)=0.}
\tag{20}
\]

Thus the source coordinate is preserved exactly at the only nontrivial row.

The channel error is

\[
\|\Psi_n-I\|
=
\frac2{r_n^2}
\longrightarrow0.
\tag{21}
\]

The generalized transport cost is

\[
J_c(0)
=
\frac{c(r_n)}{r_n^2}
\longrightarrow0.
\tag{22}
\]

But the second moment and variance are both exactly one:

\[
\mathbb EZ^2
=
\frac1{r_n^2}r_n^2
=1,
\qquad
\mathbb EZ=0,
\]

so

\[
\boxed{K_n(0)=1.}
\tag{23}
\]

This proves the converse in the strongest relevant form. The failure is not caused by barycentric drift, source-coordinate bias, or a channel that stays far from the identity. It is exactly the rare-long-jump mechanism, and the only property of the cost used is that it becomes arbitrarily cheap relative to `r^2` along some diverging sequence.

In particular there can be no support-independent modulus `F(s,t)->0` as `(s,t)->(0,0)` satisfying

\[
\|K\|
\le
F\!\left(\|\Psi-I\|,\sup_xJ_c(x)\right)
\tag{24}
\]

for all finite supports whenever (6) holds. The family (19) sends both arguments on the right to zero while the left side remains one.

## 4. Exact threshold in terms of the tail ratio

Define

\[
\rho_c
:=
\liminf_{r\to\infty}\frac{c(r)}{r^2}.
\tag{25}
\]

There are only two cases relevant to a universal defect implication.

If

\[
\rho_c>0,
\]

then some `a>0` and `R_0` satisfy (3), so (5) gives uniform stability.

If

\[
\rho_c=0,
\]

then Section 3 gives exact-barycentric counterexamples.

Thus, under channel convergence,

\[
\boxed{
\text{vanishing scalar }c\text{-transport uniformly forces }K\to0
\iff
\liminf_{r\to\infty}\frac{c(r)}{r^2}>0,
}
\tag{26}
\]

where the implication is meant uniformly over arbitrary growing finite real supports.

This formulation also exposes why local behavior of `c` near zero is irrelevant to the moving-tail obstruction. On bounded displacements, the separate channel error already supplies the factor `epsilon_x`; only the price assigned to distances that diverge with the support can carry an order-one second moment on vanishing mass.

## 5. `WP-338` is the power-law special case

For

\[
c_p(r)=r^p,
\]

one has

\[
\frac{c_p(r)}{r^2}=r^{p-2}.
\tag{27}
\]

Therefore

\[
\rho_{c_p}
=
\begin{cases}
0,&p<2,\\
1,&p=2,\\
+\infty,&p>2.
\end{cases}
\tag{28}
\]

Equation (26) reproduces the sharp `p=2` threshold of `WP-338` without treating powers specially.

More importantly, it rules out apparent interpolations that the power hierarchy does not by itself settle. For example,

\[
c(r)=\frac{r^2}{\log(2+r)}
\tag{29}
\]

is arbitrarily close to quadratic on a logarithmic scale but still has `rho_c=0`, so it fails. The same is true for linear, Huber, bounded, truncated, and every other cost whose tail is `o(r^2)`.

Conversely, any cost satisfying

\[
c(r)\ge a r^2
\]

eventually succeeds only because it directly dominates the second displacement moment on the dangerous tail. This includes genuinely superquadratic Orlicz costs, but such a condition is stronger than what the Kadison defect itself requires rather than a weaker geometric substitute.

## 6. Intrinsic dyadic prime-power realization

The generic three-point support already proves the universal impossibility theorem. The obstruction also lives inside Mathia's dyadic logarithmic coordinate geometry whenever the cost is subquadratic along that lattice.

Put

\[
h=\log2
\]

and take the three prime-power coordinates

\[
y_a=ah,
\qquad
y_{2a}=2ah,
\qquad
y_{3a}=3ah,
\tag{30}
\]

corresponding to `2^a`, `2^{2a}`, and `2^{3a}`. Modify only the row at `y_{2a}` by

\[
P_{y_{2a}}^{(a)}
=
\left(1-\frac1{a^2}\right)\delta_{y_{2a}}
+
\frac1{2a^2}\delta_{y_a}
+
\frac1{2a^2}\delta_{y_{3a}}.
\tag{31}
\]

The two displacements are `-ah` and `+ah`. Hence

\[
\Psi_a(X)(y_{2a})=y_{2a}
\tag{32}
\]

exactly,

\[
\|\Psi_a-I\|=\frac2{a^2}\to0,
\tag{33}
\]

and

\[
\boxed{
K_a(y_{2a})=h^2=(\log2)^2.
}
\tag{34}
\]

The scalar displacement cost is

\[
J_c(y_{2a})
=
\frac{c(ah)}{a^2}
=
h^2\frac{c(ah)}{(ah)^2}.
\tag{35}
\]

Therefore, if

\[
\liminf_{a\to\infty}
\frac{c(ah)}{(ah)^2}=0,
\tag{36}
\]

a subsequence of these intrinsic dyadic maps has vanishing `c`-cost and fixed nonzero defect.

For every regular asymptotically subquadratic cost with `c(r)/r^2->0`, condition (36) holds automatically. Thus the failure is not an artifact of allowing arbitrary real supports.

## 7. Matched generic control

Replace `h=log2` in Section 6 by any fixed spacing `h>0` on an equally spaced growing coordinate lattice. The same maps satisfy

\[
K_a=h^2,
\qquad
\|\Psi_a-I\|=2a^{-2},
\qquad
J_c=h^2\frac{c(ah)}{(ah)^2}.
\tag{37}
\]

Nothing in the theorem distinguishes primes, von Mangoldt weights, the archimedean place, or the explicit formula. The dyadic prime-power ray merely realizes a universal moment obstruction inside an intrinsic Mathia coordinate family.

This matched control is decisive for interpretation. A successful scalar cost cannot count as the missing arithmetic geometry merely because it closes the UCP defect estimate: the same closure theorem holds on every equally spaced non-arithmetic lattice, and its sufficient hypothesis is exactly quadratic tail pricing.

## 8. Prior-art and novelty audit

The surrounding transport and integrability theory is classical. Ordinary `W_p` convergence is tied to control of `p`-th moments; Vitali and de la Vallée-Poussin criteria characterize when convergence in measure/weak convergence can be upgraded to convergence of unbounded moments through uniform integrability. Generalized and Orlicz-type transport costs are also established: Sturm's 2011 construction explicitly builds Wasserstein-type distances from general scale functions rather than only powers.

Accordingly, neither generalized transport costs nor the principle that second moments require suitable tail control is claimed as new mathematics here. The new content relative to the Mathia research state is narrower and exact:

- the full scalar-cost escape left after `WP-338` collapses to the tail ratio `c(r)/r^2`;
- eventual quadratic domination yields the explicit uniform defect estimate (5);
- every failure of that domination along a diverging sequence produces exact-barycentric, channel-close UCP maps with vanishing proposed cost and fixed defect;
- the same obstruction can be realized on the intrinsic dyadic prime-power ray under the corresponding lattice-tail condition.

The result therefore redirects rather than solves the primary problem. Replacing `W_p` by a hand-picked scalar transport penalty cannot create an independent positivity mechanism. If the penalty is genuinely weaker than quadratic on the dangerous tail, it misses the defect; if it is strong enough, it has encoded the missing second moment directly.

## 9. Consequence for the Weil-positivity search

The surviving route cannot be merely

\[
\text{UCP channel close to identity}
+
\text{small scalar displacement cost}
\Longrightarrow
\text{approximate multiplicative domain}
\Longrightarrow
\text{global positivity}.
\]

For scalar costs of displacement, Section 4 exhausts the universal possibilities. A non-tautological advance would have to use structure not reducible to a one-row scalar tail penalty: for example a genuinely global coupling between prime directions and the archimedean sector, a cohomological/intersection constraint, a nonlocal conservation law tying different rows together, or another intrinsic theorem that forbids the rare-long-jump witnesses for arithmetic reasons while failing on the matched generic lattice.

Even then, the research contract still requires the resulting form to recover the finite-prime and archimedean/global terms of a Weil explicit-formula criterion and to obtain nonnegativity independently from RH or inserted zero data. `WP-339` supplies only a sharp exclusion boundary for one broad family of repairs; it is not evidence that such a surviving global geometry exists.
