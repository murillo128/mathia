# AF-439 — Finite Euler moment prefixes have local pole-moving fibers

**Status:** `EXACT-DERIVED`, `CLASSICAL-NEWTON-IDENTITIES`, `CLASSICAL-TRUNCATED-MOMENT-PHENOMENON`, `NEGATIVE/OBSTRUCTION`, `ARITHMETIC-FIDELITY`, `FINITE-PREFIX-NONIDENTIFIABILITY`, `NO-NOVELTY-CLAIM`

## Claim

AF-438 rewrites the normalized Euler coefficients

\[
s_k=\zeta(2k)=\sum_{m\ge1}m^{-2k}
\]

as moments of

\[
\mu=\sum_{m\ge1}m^{-2}\,\delta_{m^{-2}}
\]

and as the Taylor coefficients of the Stieltjes transform

\[
F(z)=\int\frac{d\mu(t)}{1-zt}=\sum_{m\ge1}\frac1{m^2-z}.
\]

The complete exact sequence determines the shell ladder, but a **finite** prefix does not even locally determine the pole locations inside a natural residue-normalized Stieltjes control class.

Fix `N>=1` and choose any `N+1` distinct Euler support points

\[
x_r=j_r^{-2},\qquad r=0,\ldots,N.
\]

There is a nonconstant one-parameter family of positive distinct points

\[
x_r(\tau),\qquad x_r(0)=x_r,
\]

defined for sufficiently small `\tau`, such that

\[
\boxed{
\sum_{r=0}^{N}x_r(\tau)^\ell
=
\sum_{r=0}^{N}x_r^\ell,
\qquad \ell=1,\ldots,N.
}
\]

Every selected point moves to first order. Keeping all unselected Euler atoms fixed and replacing

\[
\sum_{r=0}^{N}x_r\delta_{x_r}
\quad\text{by}\quad
\sum_{r=0}^{N}x_r(\tau)\delta_{x_r(\tau)}
\]

therefore gives a local family of positive measures `\mu_\tau` satisfying

\[
\boxed{
\int t^k\,d\mu_\tau(t)
=
\int t^k\,d\mu(t),
\qquad k=0,\ldots,N-1,
}
\]

while the selected support points are different.

Their Stieltjes terms are

\[
\frac{x_r(\tau)}{1-zx_r(\tau)}
=
\frac1{x_r(\tau)^{-1}-z},
\]

so every selected pole moves from `x_r^{-1}=j_r^2` to `x_r(\tau)^{-1}`, while its residue remains exactly `-1`.

Hence:

\[
\boxed{
\text{the first }N\text{ exact Euler moments do not locally identify }N+1\text{ shell poles, even with the residue law fixed.}
}
\]

This is stronger than merely saying that truncated/noisy pole recovery may be ill-conditioned. On this admissible local control class the finite-prefix inverse is **non-injective before noise is introduced**.

The result does not contradict AF-436 or AF-438. They use the entire exact moment sequence. It instead sharpens AF-438's finite-data frontier: before comparing Padé, Stieltjes, Hankel, or Prony condition numbers, one must specify enough source-side structure to remove these exact finite-prefix fibers.

## Exact construction by Newton identities

Let

\[
P_0(u)=\prod_{r=0}^{N}(u-x_r)
=u^{N+1}-e_1u^N+e_2u^{N-1}-\cdots+(-1)^{N+1}e_{N+1},
\]

where `e_q` are the elementary symmetric functions of the selected nodes.

Newton's identities express the first `N` power sums

\[
p_\ell=\sum_{r=0}^{N}x_r^\ell,
\qquad \ell=1,\ldots,N,
\]

entirely in terms of

\[
e_1,\ldots,e_N.
\]

They do not use the final elementary symmetric function `e_{N+1}`.

Therefore vary only the constant term:

\[
P_\tau(u)
=u^{N+1}-e_1u^N+\cdots+(-1)^Ne_Nu
+(-1)^{N+1}(e_{N+1}+\tau).
\]

Because the roots of `P_0` are simple and positive, for all sufficiently small `\tau` the polynomial `P_\tau` has `N+1` nearby simple positive real roots `x_r(\tau)` after a consistent labeling. If one selected node is `1`, restrict to the sign of `\tau` that keeps that root inside `[0,1]`. Shrinking the parameter interval also prevents collisions with every unselected reciprocal-square support point.

The coefficients `e_1,\ldots,e_N` are unchanged, so Newton's identities give

\[
p_\ell(\tau)=p_\ell(0),
\qquad 1\le\ell\le N.
\]

Now the contribution of the selected atoms to the `k`-th moment of the Euler measure is

\[
\sum_{r=0}^{N}x_r\,x_r^k
=\sum_{r=0}^{N}x_r^{k+1}
=p_{k+1}.
\]

Thus preserving `p_1,\ldots,p_N` preserves exactly the first `N` Stieltjes/Taylor moments `k=0,\ldots,N-1`.

## Every selected shell actually moves

The family is not a relabeling or a deformation that leaves some chosen target shell fixed.

Differentiate

\[
P_\tau(x_r(\tau))=0
\]

at `\tau=0`. Since only the constant term varies,

\[
P_0'(x_r)x_r'(0)+(-1)^{N+1}=0,
\]

hence

\[
\boxed{
x_r'(0)=\frac{(-1)^N}{P_0'(x_r)}\ne0.}
\]

All selected roots are simple, so all derivatives are nonzero. Consequently any prescribed shell can be included among the selected `N+1` atoms and moved while the first `N` exact moments remain unchanged.

Equivalently, the tangent vector

\[
v_r=\frac1{P_0'(x_r)}
\]

lies in the kernel of the `N\times(N+1)` power-sum Jacobian:

\[
\sum_{r=0}^{N}x_r^k v_r=0,
\qquad k=0,\ldots,N-1.
\]

This is the familiar Vandermonde/barycentric null direction. The constant-term family integrates that infinitesimal kernel into an exact local collision curve.

## Stieltjes interpretation

Define

\[
F_\tau(z)=\int\frac{d\mu_\tau(t)}{1-zt}.
\]

The equality of the first `N` moments gives

\[
F_\tau(z)-F_0(z)=O(z^N)
\qquad (z\to0).
\]

Nevertheless, on the selected block,

\[
F_\tau(z)
=
\sum_{r=0}^{N}\frac1{x_r(\tau)^{-1}-z}
+\text{unchanged tail},
\]

so the corresponding pole set changes immediately with `\tau`. Every moved pole continues to have residue `-1`.

Thus the collision is not produced by arbitrary signed weights, residue tuning, or deleting shells. It survives the structural coupling

\[
\text{atom weight}=\text{atom location},
\]

which is exactly what converts the reciprocal support point `x` into a unit-residue pole at `x^{-1}`.

This supplies a sharper finite-prefix obstruction than the ambient positive-measure collision theorem of AF-021. AF-021 allows arbitrary positive atomic measures and proves that finite test families have large convex fibers. Here the fiber passes **locally through the Euler shell measure**, moves prescribed pole locations, and preserves the unit-residue Stieltjes form.

## What structural restriction would remove this fiber?

The collision uses freedom to move `N+1` shell locations continuously while retaining only `N` power sums. It is therefore killed by source models that already fix those locations independently of the observed prefix.

In particular, the family is not an alternative rational-prime shell ladder: the perturbed points need not remain reciprocal squares of integers. It is a matched Stieltjes/generalized-shell control showing what the finite Taylor data themselves fail to determine.

Accordingly, a positive finite-data theorem must declare additional structure such as:

- the exact reciprocal-square support law;
- a finite-support model with sufficiently many additional moments;
- a discrete admissible location class with an independent separation theorem;
- a tail law or recurrence that removes the free constant-term direction;
- another source-side constraint strong enough to make the moment map injective on the stated model class.

Without such a restriction, asking whether a particular reconstruction algorithm is stable is premature: different nearby admissible sources already produce exactly the same data.

## Relation to AF-436, AF-437, and AF-438

AF-436 proves exact infinite-sequence recoverability and exhibits the exponentially shrinking shell-resolution ladder. AF-437 shows that recursive peeling amplifies earlier-shell errors exponentially. AF-438 then gives an exact non-peeling Stieltjes carrier in which all shells coexist as poles.

The present result separates a fourth issue:

\[
\text{complete exact sequence: identifiable}
\quad\neq\quad
\text{finite exact prefix: identifiable on an unrestricted nearby shell class}.
\]

The failure here is prior to numerical conditioning. It means that the next stable-recovery comparison cannot be posed only as "Padé versus peeling from the first `N` moments." It must first specify the admissible source model. Only after that model is injectively parameterized by the retained data does a condition-number comparison answer a well-posed inverse problem.

## Prior-art and novelty audit

The mathematical ingredients are classical.

Newton's identities between power sums and elementary symmetric functions are standard symmetric-polynomial theory. The fact used here is precisely that for `N+1` roots, the first `N` power sums determine `e_1,\ldots,e_N` but leave the final product `e_{N+1}` free.

The broader phenomenon belongs to the classical truncated moment problem. Di Dio and Schmuedgen analyze finite-dimensional moment maps, their moment cones, atomic representing measures, and regularity/singularity structure:

- Philipp J. di Dio and Konrad Schmuedgen, **"The multidimensional truncated Moment Problem: The Moment Cone"**, arXiv:1809.00584, https://arxiv.org/abs/1809.00584.

AF-021 already imported the general convex-geometric nonuniqueness boundary for finite test families using Radon/Tverberg and the truncated-moment framework. This finding does not claim a new theorem about truncated moments in general.

For finite atomic reconstruction and conditioning, Prony-type literature explicitly studies recovery of nodes and amplitudes from moment data and the geometry of same/nearby moment fibers. A relevant modern reference is:

- Andrey Akinshin, Gil Goldman, Yosef Yomdin, **"Geometry of error amplification in solving Prony system with near-colliding nodes"**, arXiv:1701.04058, https://arxiv.org/abs/1701.04058.

No novelty is claimed for Newton identities, Vandermonde kernels, truncated-moment nonuniqueness, Prony varieties, or the implicit-function argument.

The Arithmetic Fidelity contribution is the exact placement of this classical local fiber at the live AF-438 boundary: the first `N` Euler/Stieltjes coefficients admit a nearby pole-moving control that preserves the unit-residue law, so finite-prefix joint recovery is not a well-posed fidelity question until its source-side admissibility class is narrowed.

## Boundaries and falsification checks

- The perturbed shell locations are continuous controls, not necessarily reciprocal squares of integers. The result therefore does not show a collision inside the exact rational-integer shell family.
- The pole residues remain `-1`, but the perturbed source is not the cotangent/Euler source and need not satisfy its global functional identities.
- The theorem concerns the first `N` Taylor coefficients. Adding the next independent power sum generically fixes the previously free elementary symmetric coefficient for this selected finite block.
- The unchanged infinite tail is legitimate because the collision is created entirely inside a finite selected block; all tail moments cancel identically between source and control.
- The result is exact and local. It does not quantify how far the collision curve can be continued before roots collide, leave the positive interval, or hit untouched support points.
- AF-021 remains the general ambient positive-measure theorem. This result is stored separately because it preserves the unit-residue Stieltjes structure and moves poles locally through the specific Euler source rather than merely exhibiting some same-moment measures.
- The obstruction disappears if the admissible model fixes the reciprocal-square support a priori. Stability on that narrower model remains a separate question.

## Consequence for the research line

The immediate finite/noisy frontier after AF-438 must be split into **identifiability first, conditioning second**.

For broad nearby Stieltjes shell models, finite-prefix pole recovery fails the identifiability gate exactly, even without noise. Any useful comparison with AF-437's peeling instability must therefore work on a narrower source class that independently forbids the Newton/Prony collision direction. Once such a class is declared, its inverse conditioning can be studied honestly rather than attributing an information-theoretic fiber to a reconstruction algorithm.