# AF-303 — Fixed coordinate caps do not uniformly repair normalized positive fibers

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `SIMPLEX`, `COEFFICIENT-CAPS`, `KRONECKER-WEYL`, `PRIME-NUMBER-THEOREM`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-302 shows that simplex normalization replaces the unbounded discarded positive cone by a bounded mass-scaled convex hull, but recurrent Dirichlet phases can still put the target value inside that hull. A natural next repair is to cap every coefficient. A **fixed source-independent coordinate cap is still insufficient as a uniform repair** once sufficiently many forgotten rational-prime coordinates are available.

For `alpha>0`, define the capped coefficient simplex

\[
\Delta_N^{(\alpha)}
=
\left\{
 c\in\mathbb R_+^N:
 \sum_{n=1}^N c_n=1,
 \quad c_n\le \alpha\ \forall n
\right\}.
\]

Let

\[
P_c(s)=\sum_{n=1}^N c_n n^{-s},
\]

and let `q_D(c)=c_S` delete a set `D` of coordinates, where `S` is the retained complement.

Fix a vertical line `Re(s)=sigma`. Suppose `D` contains distinct primes `p_1,...,p_m`, with `m>=3`, for which

\[
\boxed{
\max_{1\le j\le m}
\frac{p_j^{\sigma}}{\sum_{k=1}^m p_k^{\sigma}}
<\alpha.
}
\tag{1}
\]

Then there are arbitrarily large heights `t` and two sources

\[
c^*,\widetilde c\in\Delta_N^{(\alpha)}
\]

with

\[
q_D(c^*)=q_D(\widetilde c)=0,
\qquad
P_{c^*}(\sigma+it)=0,
\qquad
P_{\widetilde c}(\sigma+it)\ne0.
\tag{2}
\]

Hence the point-zero discriminator

\[
c\longmapsto 1_{\{P_c(\sigma+it)=0\}}
\]

cannot factor through the coordinate-deletion compression on the capped source class.

Moreover, condition (1) can always be realized with rational primes for any prescribed `alpha>0` and any fixed real `sigma`. Therefore **no fixed positive per-coordinate cap, by itself, gives a uniform arithmetic-fidelity theorem for coordinate deletion over unbounded height**.

The obstruction is narrower than AF-302 and also sharper about what remains open. A cap can protect a specific finite discarded set when it excludes every barycentric zero representation. What fails is the idea that a universal bound `c_n<=alpha`, independent of the discarded response geometry, is enough in principle. Any successful cap-based repair must be geometry/source dependent, limit the number or arrangement of independently phased forgotten coordinates, or impose additional coupling beyond coordinatewise upper bounds.

## Balanced capped polygon construction

Fix `sigma` and write

\[
r_j=p_j^{-\sigma}>0.
\]

Choose target phases

\[
\phi_j=\frac{2\pi(j-1)}{m},
\qquad 1\le j\le m,
\]

and define

\[
\lambda_j^0
=
\frac{r_j^{-1}}{\sum_{k=1}^m r_k^{-1}}
=
\frac{p_j^{\sigma}}{\sum_{k=1}^m p_k^{\sigma}}.
\tag{3}
\]

By (1), every `lambda_j^0` lies strictly between `0` and `alpha`, while

\[
\sum_j\lambda_j^0=1.
\]

The weighting in (3) equalizes the radial response lengths:

\[
\lambda_j^0 r_j
=
\left(\sum_{k=1}^m p_k^{\sigma}\right)^{-1}
\]

for all `j`. Consequently

\[
\sum_{j=1}^m
\lambda_j^0 r_j e^{i\phi_j}
=
\left(\sum_{k=1}^m p_k^{\sigma}\right)^{-1}
\sum_{j=1}^m e^{2\pi i(j-1)/m}
=0.
\tag{4}
\]

Thus unequal Dirichlet radii do not obstruct a capped zero polygon: the barycentric weights can absorb the radii, provided their largest required value remains below the coordinate cap.

This identifies the exact source resource relevant to a fixed cap. It is not simply the number of discarded coordinates. It is the largest normalized inverse-radius weight

\[
\beta_D(\sigma)
:=
\max_j
\frac{p_j^{\sigma}}{\sum_k p_k^{\sigma}}.
\tag{5}
\]

The strict inequality `beta_D(sigma)<alpha` leaves interior slack in the cap constraints.

## The zero representation persists on an open phase set

Define

\[
F(\lambda,\theta)
=
\left(
\sum_{j=1}^m\lambda_j,
\operatorname{Re}\sum_{j=1}^m\lambda_j r_j e^{i\theta_j},
\operatorname{Im}\sum_{j=1}^m\lambda_j r_j e^{i\theta_j}
\right).
\]

At `(lambda^0,phi)` one has

\[
F(\lambda^0,\phi)=(1,0,0).
\]

The derivative with respect to `lambda` has columns

\[
\left(1,r_j\cos\phi_j,r_j\sin\phi_j\right)^T.
\]

Because `m>=3`, three regular-polygon vertices can be chosen non-collinearly, so this `3 x m` derivative has rank `3`. The implicit-function theorem therefore gives a neighborhood `U` of the target phase tuple `phi` in which the equations

\[
\sum_j\lambda_j=1,
\qquad
\sum_j\lambda_j r_j e^{i\theta_j}=0
\tag{6}
\]

have a continuous local solution `lambda(theta)` near `lambda^0`.

The inequalities in (1) are strict. Shrinking `U` if necessary therefore gives

\[
0<\lambda_j(\theta)<\alpha
\qquad
\forall j
\tag{7}
\]

throughout `U`.

So the capped zero configuration is not an isolated exact phase coincidence. It occupies an open set of phase tuples.

## Kronecker-Weyl makes the capped collision recurrent

For distinct rational primes, the logarithms

\[
\log p_1,\ldots,\log p_m
\]

are linearly independent over `\mathbb Q`: an integer relation would exponentiate to a nontrivial multiplicative relation among distinct primes, contradicting unique factorization.

Hence the continuous Kronecker-Weyl theorem makes the orbit

\[
t\longmapsto
(-t\log p_1,\ldots,-t\log p_m)
\pmod{2\pi}
\tag{8}
\]

dense, indeed equidistributed, in `\mathbb T^m`. Since `U` is open and nonempty, the orbit enters `U` at arbitrarily large heights.

At any such height `t`, let

\[
c^*_{p_j}=\lambda_j(\theta(t)),
\qquad
c_n^*=0
\quad\text{otherwise}.
\]

Then `c^*\in\Delta_N^{(\alpha)}`, it is supported entirely on discarded coordinates, and (6) gives

\[
P_{c^*}(\sigma+it)=0.
\tag{9}
\]

To obtain a safe source in the same compression fiber, consider the tangent space

\[
H=\left\{\delta\in\mathbb R^m:\sum_j\delta_j=0\right\}.
\]

The response map

\[
L_t(\delta)
=
\sum_j\delta_j p_j^{-\sigma-it}
\]

is not identically zero on `H`; otherwise `L_t(e_j-e_1)=0` for every `j`, forcing all discarded response vectors to be equal, which is impossible in a sufficiently small neighborhood of the regular-polygon phase tuple. Choose `delta\in H` with `L_t(delta)\ne0`. Because the coefficients in (7) lie strictly inside the cap constraints, for sufficiently small nonzero `epsilon`,

\[
\widetilde c_{p_j}
=
\lambda_j(\theta(t))+\epsilon\delta_j
\]

remains in `(0,alpha)`, still sums to one, and satisfies

\[
P_{\widetilde c}(\sigma+it)
=
\epsilon L_t(\delta)\ne0.
\tag{10}
\]

Both sources have retained state zero, proving (2).

## Rational primes can satisfy every fixed cap

It remains to show that (1) is not a special finite-block assumption.

Fix `alpha>0` and real `sigma`. Choose an integer `m>=3` with

\[
\frac1m<\alpha.
\tag{11}
\]

Choose `eta>0` small enough that

\[
\frac{(1+\eta)^{|\sigma|}}{m}<\alpha.
\tag{12}
\]

For sufficiently large `X`, the prime number theorem implies that the interval

\[
[X,(1+\eta)X]
\]

contains at least `m` primes. Pick any `m` of them. If `sigma>=0`, then

\[
\max_j\frac{p_j^{\sigma}}{\sum_k p_k^{\sigma}}
\le
\frac{((1+\eta)X)^{\sigma}}{mX^{\sigma}}
\le
\frac{(1+\eta)^{|\sigma|}}m
<\alpha.
\]

If `sigma<0`, the same estimate follows with the roles of the interval endpoints reversed:

\[
\max_j\frac{p_j^{\sigma}}{\sum_k p_k^{\sigma}}
\le
\frac{X^{\sigma}}{m((1+\eta)X)^{\sigma}}
=
\frac{(1+\eta)^{|\sigma|}}m
<\alpha.
\]

Thus every fixed cap admits sufficiently large finite prime blocks satisfying the recurrent-collision criterion.

The argument does **not** claim that every predetermined finite discarded block defeats every cap. If `alpha` is below the barycentric requirement for that particular response geometry, or if too few coordinates remain available to carry unit mass, the cap can genuinely eliminate the collision. The theorem is a uniform no-go against cap-only repair across enlarging rational-prime source families.

## Prior art and novelty assessment

All ingredients used in the proof are classical, and no novelty claim is made for them.

- Alexandre Bailleul, “Explicit Kronecker-Weyl theorems and applications to prime number races,” *Research in Number Theory* 8 (2022), Article 43, arXiv:`2007.05763`, gives explicit continuous and discrete Kronecker-Weyl formulations. The recurrence step here uses only the classical continuous theorem under rational independence.
- The prime number theorem, in the classical Hadamard/de la Vallée-Poussin form `pi(x)~x/log x`, implies that every fixed relative interval `[X,(1+eta)X]` contains arbitrarily many primes for sufficiently large `X`. De la Vallée-Poussin’s quantitative form is more than is needed here.
- The regular-polygon cancellation, barycentric normalization, rank test, and implicit-function persistence are elementary finite-dimensional convex/analytic geometry.

The durable Arithmetic Fidelity content is the specialization to the live AF-302 escape: **coordinatewise caps that do not adapt to the discarded response geometry can always be overwhelmed by enough independently phased, comparable rational-prime coordinates.** The exact threshold exposed by the proof is the required barycentric weight profile (5), not a generic positivity slogan.

## Boundaries and failure modes

- The theorem is a family-level obstruction. A particular fixed finite discarded set may be protected by a sufficiently small cap.
- The cap is coordinatewise and source-independent. Geometry-adaptive caps that explicitly exclude every feasible zero barycentric vector are outside the no-go statement.
- The construction uses enough discarded rational-prime coordinates to make the inverse-radius barycentric profile fit under the cap. Fixed support cardinality can therefore evade this argument.
- The collision is recurrent over unbounded height. It does not force failure on a prescribed compact vertical interval.
- The source remains a continuous capped simplex. Integrality, a discrete coefficient alphabet, multiplicative coupling, nonlinear source varieties, or arithmetic relations among coefficients may destroy the perturbation and barycentric construction.
- The result concerns exact point-zero fidelity for finite Dirichlet polynomials. It does not establish a zero-count collision, analytic continuation statement, zeta-zero approximation, or RH implication.
- The use of a short relative prime block is only to balance radial factors at the chosen `sigma`. It is not a statement about prime gaps on shrinking absolute scales.

## Consequence for the research line

AF-302 left coefficient caps as one candidate way to constrain the normalized fiberwise reachable body. AF-303 closes the simplest version: a **fixed positive cap per coordinate is not a uniform repair**. For any cap and any fixed vertical line, sufficiently many comparable forgotten primes admit interior capped barycentric weights whose recurrent phases cancel exactly.

The live cap-based question is therefore no longer “does bounding each coefficient help?” It is whether an independently justified source law forces the feasible barycentric polytope to avoid the failure set uniformly in the target regime. Candidate repairs must now pay for at least one additional resource: bounded discarded support size, a cap coupled to the actual response radii/phases, discreteness or integrality, multiplicative/nonlinear coefficient relations, or a finite observation window that prevents the Kronecker recurrence from reaching dangerous phase cells.

This also sharpens the resource interpretation of AF-301--AF-302. Positivity replaces linear nullspace geometry by a reachable cone; normalization takes a bounded cross-section of that cone; fixed coordinate caps carve that cross-section into a polytope. None of those steps alone guarantees fidelity. What matters is whether the **actual feasible fiberwise correction polytope intersects the downstream failure value**.