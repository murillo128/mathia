# AF-302 — Normalized positive fibers re-collapse when the discarded response convex hull contains zero

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `ZERO-COUNT`, `SIMPLEX`, `CONVEX-HULL`, `KRONECKER-WEYL`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-301 shows that for the unbounded positive orthant, coordinate deletion exposes a positive **cone** of discarded corrections and recurrent Dirichlet phases can make that cone fill the complex target plane. Simplex normalization removes the unbounded radial freedom, but it does not restore exact fidelity. It replaces the cone by a **mass-scaled convex hull**, and the same recurrent phase geometry still creates collision fibers whenever that convex hull contains the origin.

Let

\[
P_c(s)=\sum_{n=1}^N c_n n^{-s},
\qquad
\Delta_N=\left\{c\in\mathbb R_+^N:\sum_{n=1}^N c_n=1\right\},
\]

split the indices into retained coordinates `S` and discarded coordinates `D`, and let

\[
q_D(c)=c_S.
\]

For a fixed observation point `z=\sigma+it`, write

\[
v_n(z)=n^{-z}\in\mathbb C\simeq\mathbb R^2,
\qquad
K_D(z)=\operatorname{conv}\{v_d(z):d\in D\}.
\]

The image of the simplex under `q_D` is

\[
\Delta_S^{\le 1}
=
\left\{y\in\mathbb R_+^S:\|y\|_1\le1\right\}.
\]

For `y\in\Delta_S^{\le1}`, define its retained response and remaining discarded mass by

\[
r_S(y;z)=\sum_{n\in S}y_n v_n(z),
\qquad
M(y)=1-\|y\|_1.
\]

Then the set of all evaluations at `z` attained by the normalized-positive fiber over `y` is exactly

\[
\boxed{
\{P_c(z):c\in\Delta_N,\ q_D(c)=y\}
=
r_S(y;z)+M(y)K_D(z).
}
\tag{1}
\]

With the convention `0K_D=\{0\}`, the normalized failure set

\[
H_z^\Delta=\{c\in\Delta_N:P_c(z)=0\}
\]

therefore satisfies

\[
\boxed{
y\in q_D(H_z^\Delta)
\iff
0\in r_S(y;z)+M(y)K_D(z).
}
\tag{2}
\]

Equivalently, when `M(y)>0`,

\[
\boxed{
-\frac{r_S(y;z)}{M(y)}\in K_D(z),
}
\tag{3}
\]

while for `M(y)=0` failure is possible exactly when `r_S(y;z)=0`.

Thus normalization changes the AF-301 reachable correction set from an unbounded cone to a bounded body whose scale is exactly the **unspent coefficient mass** `M(y)`. This is a genuine resource restriction. But exact point-zero fidelity still fails as soon as

\[
\boxed{0\in K_D(z).}
\tag{4}
\]

Indeed, the compressed state `y=0` then has both a failure completion and a safe completion. A convex representation

\[
0=\sum_{d\in D}\lambda_d v_d(z),
\qquad
\lambda_d\ge0,
\qquad
\sum_{d\in D}\lambda_d=1,
\]

defines `c^*\in\Delta_N` supported on `D` with `P_{c^*}(z)=0` and `q_D(c^*)=0`. For any `d_0\in D`, the monomial source `e_{d_0}\in\Delta_N` has the same compressed image but

\[
P_{e_{d_0}}(s)=d_0^{-s}\ne0
\]

for every finite `s`. Hence the discriminator `1_{\{P_c(z)=0\}}` cannot factor through `q_D`.

The obstruction recurs arithmetically. If `D` contains three integers `d_1,d_2,d_3` with `\log d_1,\log d_2,\log d_3` linearly independent over `\mathbb Q`, then for every real `\sigma` there are arbitrarily large heights `t` for which

\[
0\in\operatorname{int}
\operatorname{conv}\{d_1^{-\sigma-it},d_2^{-\sigma-it},d_3^{-\sigma-it}\}.
\tag{5}
\]

Three distinct primes again supply the canonical instance. Consequently, simplex normalization prevents AF-301's **complete saturation of every retained state**, but it does not prevent recurrent exact collision fibers. A normalized positive source is therefore not faithful under coordinate deletion merely because its total coefficient mass is bounded.

## Exact simplex-fiber geometry

Fix `y\in\Delta_S^{\le1}`. Any source in the fiber `q_D^{-1}(y)\cap\Delta_N` has discarded coefficients `x_d\ge0` satisfying

\[
\sum_{d\in D}x_d=M(y).
\tag{6}
\]

If `M(y)>0`, write `x_d=M(y)\lambda_d` with `\lambda_d\ge0` and `\sum_d\lambda_d=1`. Then

\[
P_c(z)
=
r_S(y;z)
+M(y)\sum_{d\in D}\lambda_d v_d(z),
\]

and the second term ranges exactly over `M(y)K_D(z)`. If `M(y)=0`, all discarded coefficients vanish. This proves (1)--(3).

The formula isolates the resource that was absent in AF-301. There, arbitrarily large discarded coefficients turn the reachable set into the recession cone `C_D(z)`. Here the coefficient budget fixes the total discarded mass, so the reachable set has finite diameter and shrinks linearly as retained mass approaches one.

Let

\[
R_D(z)=\max_{d\in D}|v_d(z)|.
\]

Since `K_D(z)\subseteq \overline B(0,R_D(z))`, every normalized failure completion obeys the necessary bound

\[
\boxed{|r_S(y;z)|\le M(y)R_D(z).}
\tag{7}
\]

Thus normalization really does block sufficiently large retained responses when little discarded mass remains. Conversely, if `0\in\operatorname{int}K_D(z)` and

\[
\rho_D(z)=\operatorname{dist}(0,\partial K_D(z))>0,
\]

then

\[
\overline B(0,\rho_D(z))\subseteq K_D(z),
\]

so every retained state satisfying

\[
\boxed{|r_S(y;z)|\le M(y)\rho_D(z)}
\tag{8}
\]

has a normalized positive completion with a zero at `z`.

Equations (7)--(8) give the first target-scale resource form of the reachable-set invariant suggested after AF-301: the uncertainty is neither binary positivity nor kernel dimension, but a **fiberwise correction body multiplied by the remaining source budget**.

## Convex-hull zero is the normalized form of positive spanning

For a finite set `V\subset\mathbb R^2\setminus\{0\}`, the following are equivalent:

1. `\operatorname{cone}_+(V)=\mathbb R^2`;
2. `V` is not contained in any closed half-plane through the origin;
3. `0\in\operatorname{int}\operatorname{conv}(V)`.

The equivalence is standard finite-dimensional convex geometry and is the same positive-spanning criterion used in AF-301. The normalized statement is not a different angular phenomenon: it is the bounded cross-section of the same cone geometry.

The distinction is in what collapse means. For the unbounded orthant, full positive spanning makes **every** negative retained response reachable because discarded coefficients may be scaled without limit. For the simplex, positive spanning only gives the bounded correction body `M K_D`; large retained responses can escape it. Nevertheless, the fiber over `y=0` always has the full budget `M=1`, and `0\in K_D` is already enough to place both safe and failing sources in that single fiber.

Hence a source constraint can destroy global saturation without restoring factorization. These are different fidelity questions and should not be conflated.

## Kronecker-Weyl gives recurrent normalized collisions

Assume `D` contains `d_1,d_2,d_3` with `\mathbb Q`-linearly independent logarithms. Consider

\[
t\longmapsto
\bigl(
-t\log d_1,
-t\log d_2,
-t\log d_3
\bigr)
\pmod{2\pi}.
\tag{9}
\]

By the continuous Kronecker-Weyl theorem this orbit is dense, indeed equidistributed, in `\mathbb T^3`. The phase triple

\[
(0,2\pi/3,4\pi/3)
\]

has the origin strictly inside the convex hull of its three unit rays. That remains true on an open neighborhood of the triple. Therefore (9) enters such a neighborhood at arbitrarily large heights.

Multiplying the three rays by the positive radial factors `d_j^{-\sigma}` does not change whether their positive cone is the whole plane. By the convex-hull/positive-span equivalence, at each such height

\[
0\in\operatorname{int}
\operatorname{conv}\{d_j^{-\sigma-it}:j=1,2,3\}.
\]

This proves (5). For distinct primes, `\mathbb Q`-linear independence of their logarithms follows from unique factorization exactly as in AF-301.

The recurrence is robust rather than an exact phase coincidence. At dangerous heights the origin lies in the **interior** of the discarded triangle, so `\rho_D(z)>0`; a neighborhood of retained responses is failure-completable by (8).

## Zero-count consequence

The collision is not limited to the binary value `P_c(z)=0`. The failure source `c^*` above is a nonzero finite exponential polynomial, hence an entire function not identically zero. Its zero at `z` is isolated. Choose a sufficiently small disk around `z` whose boundary contains no zero of `P_{c^*}` and which contains no other zero except the multiplicity at `z`.

Then `P_{c^*}` has positive zero count in that disk, while the same-fiber monomial `d_0^{-s}` has zero count zero. Thus a local zero-count discriminator also cannot factor through the coordinate-deleted normalized source. The contour here is constructed after the collision point; Kronecker-Weyl does not imply that an arbitrary preassigned compact contour contains such a recurrent height.

## Prior art and novelty assessment

The ingredients are classical and this finding makes no novelty claim for convex-hull geometry or Kronecker-Weyl.

- Andrew R. Conn, Katya Scheinberg, and Luis N. Vicente, *Introduction to Derivative-Free Optimization*, SIAM/MOS (2009), Chapter 2, treats positive spanning sets and positive bases. The standard characterization of a positive spanning set by the origin lying in the interior of its convex hull is the convex-geometric bridge used here.
- Alexandre Bailleul, “Explicit Kronecker-Weyl theorems and applications to prime number races,” *Research in Number Theory* 8 (2022), Article 43, DOI `10.1007/s40993-022-00349-2`, gives explicit continuous and discrete Kronecker-Weyl formulations and arithmetic applications. The density/equidistribution step used here is classical Kronecker-Weyl.
- The fact that a linear image of a probability simplex is the convex hull of the images of its vertices is elementary barycentric convexity; equation (1) is that fact specialized fiberwise to the Dirichlet response map.

The durable Arithmetic Fidelity content is the exact specialization to the live AF-301 escape: **normalization converts conic reachability into budgeted convex-hull reachability, but recurrent multiplicatively independent phases still force same-fiber zero collisions.** The new information over AF-301 is the exact mass-scaled fiber body and its quantitative inner/outer radius gates (7)--(8), not the classical ingredients themselves.

## Boundaries and failure modes

- The source is the full coefficient simplex. Coordinate caps, lower bounds, fixed support size, integral/discrete coefficients, multiplicative relations, nonlinear source varieties, or other restrictions can remove the convex combinations used here.
- The compression is coordinate deletion. A nonlinear representation with fibers not equal to simplex sections can behave differently.
- The recurrent obstruction requires at least three discarded responses whose logarithmic frequencies support full planar positive spanning; three distinct primes suffice.
- The recurrence is over unbounded height. It does not force a collision on a prescribed finite height interval or fixed contour.
- Simplex normalization does prevent complete saturation in general. Equation (7) is a real protection and must not be erased by summarizing the result as “normalization does nothing.” What fails is exact factorization, already on the `y=0` fiber, whenever (4) holds.
- The result treats finite Dirichlet polynomials and exact point/zero-count discrimination. It gives no analytic continuation, asymptotic coefficient law, zero matching, or RH implication.

## Consequence for the research line

AF-301 listed simplex normalization as a live way to bound the reachable correction set. The bound is now exact: a retained state with unspent mass `M` can be corrected only through `M K_D(z)`. This is the right resource-aware replacement for the unbounded cone.

But the simplest normalization escape is closed as a route to exact coordinate-deletion fidelity over unbounded heights. Multiplicatively independent forgotten prime coordinates recurrently put the origin inside the discarded response hull, and the zero retained state then contains both safe and failing normalized sources.

The next source-relative escape must therefore constrain more than total mass. Useful candidates are constraints that make the fiberwise reachable set avoid the target failure value—coefficient caps tied to the required barycentric weights, discreteness/integrality, sparsity, multiplicative coupling, support restrictions, nonlinear source relations, or a fixed finite observation window. For each such proposal the correct invariant is now explicit: compute the actual fiberwise reachable correction set together with its available source budget, rather than infer fidelity from positivity or normalization alone.