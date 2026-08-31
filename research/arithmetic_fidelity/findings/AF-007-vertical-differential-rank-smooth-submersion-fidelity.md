# AF-007 — Vertical differential rank measures smooth fidelity loss under submersions

**Status:** `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `NEGATIVE/OBSTRUCTION`

## Claim

Let

\[
T:M\to N
\]

be a smooth surjective submersion between finite-dimensional smooth manifolds, and let

\[
D:M\to\mathbb R^q
\]

be a smooth discriminator map. For each `x in M`, define the vertical tangent space

\[
V_x=\ker(dT_x)
\]

and the **vertical differential defect**

\[
\delta_{T,D}(x)
=
\operatorname{rank}\left(dD_x\big|_{V_x}\right).
\]

Then:

1. if `D` factors smoothly through `T`, so that
   \[
   D=R\circ T
   \]
   for some smooth `R:N\to\mathbb R^q`, then
   \[
   \delta_{T,D}(x)=0
   \qquad\text{for every }x\in M;
   \]
2. if every fiber of `T` is connected, the converse also holds: `D` factors smoothly through `T` if and only if `\delta_{T,D}` vanishes identically;
3. for any smooth lift
   \[
   L:M\to A
   \]
   into a `k`-dimensional manifold, if `D` is smoothly recoverable from `(T,L)` near `x`, then
   \[
   \delta_{T,D}(x)
   \le
   \operatorname{rank}\left(dL_x\big|_{V_x}\right)
   \le k;
   \]
   hence `\delta_{T,D}(x)` is a pointwise lower bound on the dimension of every smooth lift capable of restoring the discriminator locally;
4. if `\delta_{T,D}` is constant with value `r` on a neighborhood of `x`, then this lower bound is locally sharp when arbitrary target-dependent smooth lifts are allowed: after shrinking the neighborhood there exists a linear projection
   \[
   \pi:\mathbb R^q\to\mathbb R^r
   \]
   such that the lift
   \[
   L=\pi\circ D
   \]
   satisfies
   \[
   D=Q\circ(T,L)
   \]
   locally for some smooth `Q`;
5. if
   \[
   M\xrightarrow{T}N\xrightarrow{S}P
   \]
   is a chain of smooth submersions, then
   \[
   \delta_{S\circ T,D}(x)\ge \delta_{T,D}(x).
   \]
   Thus downstream smooth compression can only enlarge, never shrink, the space of infinitesimally invisible discriminator directions.

Consequently, in the regular smooth setting, Arithmetic Fidelity has an exact **infinitesimal no-go test**: a discriminator that changes along a tangent direction annihilated by the compression cannot be recreated by any smooth downstream map of the compressed data alone. The rank of that vertical change quantifies how many independent smooth discriminator directions are being erased locally.

This does not replace the global fiber criterion of AF-001. It refines it. The differential defect detects continuous/infinitesimal loss, while disconnected fibers or other discrete identifications can remain invisible to first-order analysis.

## Derivation

### Factorization forces vertical annihilation

Assume

\[
D=R\circ T.
\]

By the chain rule,

\[
dD_x=dR_{T(x)}\circ dT_x.
\]

If `v\in V_x=\ker dT_x`, then

\[
dD_x(v)
=dR_{T(x)}(0)
=0.
\]

Therefore

\[
dD_x\big|_{V_x}=0
\]

and `\delta_{T,D}(x)=0` for every `x`.

This implication needs neither connected fibers nor surjectivity; it is purely local.

### Connected fibers make the differential criterion globally sufficient

Now assume `T` is surjective, every fiber `T^{-1}(y)` is connected, and

\[
dD_x\big|_{V_x}=0
\qquad\text{for every }x\in M.
\]

Because `T` is a submersion, each fiber is an embedded submanifold whose tangent space at `x` is precisely `V_x`. The restriction of `D` to a fiber therefore has zero differential everywhere on that fiber.

A connected smooth manifold is path connected, so `D` is constant on each fiber. Hence there is a unique set-theoretic map

\[
R:N\to\mathbb R^q
\]

such that

\[
D=R\circ T.
\]

It remains only to check smoothness. A submersion admits smooth local sections. For every `y in N`, choose a neighborhood `U` and a smooth section

\[
\sigma:U\to M,
\qquad
T\circ\sigma=\operatorname{id}_U.
\]

Then on `U`,

\[
R
=
R\circ T\circ\sigma
=
D\circ\sigma,
\]

which is smooth. Thus `R` is smooth globally.

So, for connected-fiber submersions,

\[
\boxed{
D\text{ descends smoothly through }T
\iff
dD(V)=0.
}
\]

In foliation language, the fibers form a regular foliation and the scalar components of `D` are basic exactly when they are constant along those leaves.

## Lift lower bound from vertical rank

Let

\[
L:M\to A
\]

be a smooth lift into a `k`-dimensional manifold, and suppose that near `x` there is a smooth map `Q` with

\[
D=Q\circ(T,L).
\]

For `v\in V_x`,

\[
dT_x(v)=0,
\]

so the chain rule gives

\[
dD_x(v)
=
dQ_{(T(x),L(x))}\bigl(0,dL_x(v)\bigr).
\]

Therefore the image of `dD_x|_{V_x}` is a linear image of the image of `dL_x|_{V_x}`. Hence

\[
\operatorname{rank}(dD_x|_{V_x})
\le
\operatorname{rank}(dL_x|_{V_x})
\le
\dim A.
\]

This proves

\[
\boxed{
\dim A\ge\delta_{T,D}(x)
}
\]

for every smooth local lift capable of restoring `D`.

The bound is stronger than counting the number `q` of output coordinates of `D`. Several discriminator coordinates may carry only one independent direction of variation along the invisible fiber, while one discriminator coordinate can already force a nonzero defect.

## Local sharpness when the defect rank is constant

Assume

\[
\delta_{T,D}(p)=r
\]

throughout a neighborhood of `x`.

The vertical image

\[
dD_x(V_x)\subseteq\mathbb R^q
\]

has dimension `r`. Choose a linear projection

\[
\pi:\mathbb R^q\to\mathbb R^r
\]

whose restriction to that `r`-dimensional image has rank `r`. After shrinking the neighborhood, the same rank remains `r` because one nonzero `r x r` minor stays nonzero and `dD|_V` itself has rank only `r`.

Set

\[
L=\pi\circ D.
\]

Then on each vertical space,

\[
\operatorname{rank}(dL|_V)=r
=
\operatorname{rank}(dD|_V).
\]

Since

\[
\ker(dD|_V)\subseteq\ker(dL|_V)
\]

and the two kernels have the same dimension, they are equal.

Consider

\[
F=(T,L):M\to N\times\mathbb R^r.
\]

The differential of `F` has rank

\[
\dim N+r,
\]

so, after shrinking again, `F` is a submersion. Moreover,

\[
\ker dF
=
\ker dT\cap\ker dL
=
\ker dT\cap\ker dD.
\]

Thus `dD` annihilates the vertical tangent spaces of `F`. In a sufficiently small submersion chart the fibers of `F` are connected, so the connected-fiber argument above applies locally and gives

\[
D=Q\circ F
=Q\circ(T,L).
\]

Therefore a lift of dimension exactly `r` exists locally.

This sharpness statement is deliberately **not** a natural-lift theorem. The constructed lift is obtained directly from the target discriminator `D`, so it can leak the answer exactly as the unrestricted lifts in AF-001 do. Its value is to identify `r` as the exact local smooth information-loss rank. Any independently admissible lift must meet at least this rank, and may require more structure or fail entirely.

## Composition monotonicity

Let

\[
M\xrightarrow{T}N\xrightarrow{S}P
\]

be smooth submersions. Then

\[
\ker dT_x
\subseteq
\ker d(S\circ T)_x,
\]

because every vector killed by `dT_x` is automatically killed by `dS_{T(x)}\circ dT_x`.

Restricting `dD_x` to a larger subspace cannot reduce the dimension of its image, so

\[
\operatorname{rank}
\left(dD_x\big|_{\ker d(S\circ T)_x}\right)
\ge
\operatorname{rank}
\left(dD_x\big|_{\ker dT_x}\right).
\]

Hence

\[
\boxed{
\delta_{S\circ T,D}(x)
\ge
\delta_{T,D}(x).
}
\]

This is a differential version of AF-001's deterministic irreversibility principle. Once a smooth compression makes a discriminator direction vertical, later smooth compression cannot make that direction observable again without adding new upstream information.

## Exact examples and boundary tests

### Two independent invisible directions require a two-dimensional smooth lift

Take

\[
T:\mathbb R^3\to\mathbb R,
\qquad
T(x,y,z)=x,
\]

and

\[
D(x,y,z)=(y,z,yz).
\]

The vertical space is spanned by `\partial_y,\partial_z`, and

\[
dD|_V
=
\begin{pmatrix}
1&0\\
0&1\\
z&y
\end{pmatrix},
\]

which has rank `2` everywhere. Thus

\[
\delta_{T,D}=2.
\]

No one-dimensional smooth lift can locally recover `D` together with `T`. The lift

\[
L(x,y,z)=(y,z)
\]

has dimension two and is sufficient because

\[
D=(L_1,L_2,L_1L_2).
\]

The three discriminator coordinates therefore contain exactly two independent vertical degrees of freedom.

### A single-point zero defect is not enough

Let

\[
T:\mathbb R^2\to\mathbb R,
\qquad
T(x,y)=x,
\]

and

\[
D(x,y)=y^2.
\]

At every point with `y=0`,

\[
dD(\partial_y)=2y=0,
\]

so `\delta_{T,D}=0` there. But `D` does not factor through `T` on any neighborhood of such a point, because it varies with `y` immediately off the axis.

Thus `\delta(x)=0` is only a first-order statement at one point. Local descent requires vanishing along the vertical distribution throughout a neighborhood, not merely at the base point.

### Disconnected fibers carry loss invisible to every differential test

Consider the double covering

\[
T:S^1\to S^1,
\qquad
T(z)=z^2.
\]

This is a local diffeomorphism, so

\[
\ker dT_z=0
\]

and therefore

\[
\delta_{T,D}(z)=0
\]

for **every** smooth discriminator `D`.

Take

\[
D(z)=\operatorname{Re}(z).
\]

The points `z` and `-z` lie in the same `T`-fiber but generally have different `D`-values, so `D` does not factor through `T`.

The failure is entirely discrete: each fiber consists of two isolated points and has no vertical tangent direction. This shows exactly why connectedness of fibers is needed for the global differential criterion and why infinitesimal fidelity cannot replace AF-001's full fiber audit.

## Arithmetic Fidelity interpretation

AF-001 gives the universal exact rule: a discriminator survives a compression if and only if it is constant on the compression fibers. That rule is complete but can be difficult to use when the objects and fibers are geometric or high-dimensional.

The present result supplies a regular smooth reduction. For connected-fiber submersions, the global fiber condition becomes the differential condition

\[
dD(\ker dT)=0.
\]

When it fails, the rank

\[
\delta_{T,D}(x)
\]

measures the number of independent first-order discriminator directions living inside information that `T` makes invisible.

This produces a two-layer fidelity audit:

1. **vertical/tangent audit:** determine what continuous discriminator variation lies inside `\ker dT`;
2. **global/discrete fiber audit:** determine whether distinct connected components, sheets, monodromy classes, or other globally identified states still carry different discriminator values.

A smooth construction can pass the first layer and fail the second. The double-cover example is the minimal exact witness.

The defect rank also sharpens the idea of a minimal lift. Even before specifying naturality, locality, equivariance, or operator constraints, every smooth lift has a hard dimension floor. But matching that floor with a target-derived lift proves only an information-theoretic possibility, not an intrinsic mechanism. A genuinely useful lift still has to arise independently of the discriminator.

## Prior art and novelty assessment

The mathematical ingredients are classical differential topology and foliation theory.

The submersion/rank theorem gives local coordinates in which a submersion is a projection, identifies the tangent space of a fiber with `\ker dT`, and yields smooth local sections. John M. Lee's *Introduction to Smooth Manifolds* is a standard reference for these facts.

Regular foliations are locally modeled by fibers of submersions; Moerdijk and Mrčun give this as one of the standard equivalent descriptions of a foliation. In foliation terminology, a smooth scalar function constant along leaves is a **basic function**; Molino's treatment of transverse geometry uses this language explicitly. Thus the criterion `dD(V)=0` for descent along connected leaves should not be presented as a new theorem.

The local rank bound and its sharpness are direct consequences of the chain rule, the constant-rank/submersion theorem, and elementary rank arguments. No literature novelty is claimed for those ingredients either.

The Arithmetic Fidelity contribution is the **organization of these classical facts into a smooth fidelity defect**:

\[
\text{compression }T
\longrightarrow
\text{vertical distribution }\ker dT
\longrightarrow
\operatorname{rank}(dD|_{\ker dT})
\longrightarrow
\text{local no-go / lift lower bound}.
\]

This gives the line a reusable infinitesimal audit that is strictly stronger than heuristic dimension counting while remaining explicitly incomplete for discrete/global fiber collapse.

## Boundaries and failure modes

- The exact global equivalence between `\delta=0` and smooth factorization assumes `T` is a surjective submersion with connected fibers.
- Without connected fibers, `\delta=0` controls only constancy on connected fiber components. Discrete sheet labels can still be lost.
- At singular maps where `dT` changes rank, the vertical spaces do not form a regular bundle and the submersion proof does not apply unchanged. Stratified, singular, or tangent-cone refinements require separate theory.
- Vanishing of `\delta` at one point is not a local factorization theorem; the vertical derivative must vanish on an appropriate neighborhood or along the relevant connected fibers.
- The defect is first-order. Higher-order jets may matter near singular or rank-changing points even when the first derivative vanishes.
- The local sharpness construction uses a target-dependent projection of `D` and therefore does not satisfy any no-target-leakage requirement. For an independently fixed admissible lift class, `\delta` is only a lower bound.
- A lift of dimension at least `\delta` can still fail because of topology, global fiber structure, symmetry restrictions, locality, positivity, analytic constraints, or an unsuitable observable class.
- Nothing here establishes that an existing RH construction is a smooth submersion or identifies its prime discriminator. Those hypotheses must be proved in the concrete line before applying this audit.

## Decisive audit test for smooth compression chains

For a proposed smooth compression of structured data:

1. identify the regular locus on which the compression is genuinely a submersion;
2. identify the discriminator map independently of the candidate lift;
3. compute the vertical tangent distribution `V=\ker dT`;
4. evaluate the rank of `dD|_V` rather than comparing ambient dimensions;
5. if the rank is nonzero, record an immediate local no-go for downstream-only smooth recovery and a lower bound on any additional smooth lift;
6. if the rank vanishes, inspect connectedness and the full global fibers before concluding that the discriminator survives;
7. for a compression chain, track the monotone defect as vertical directions accumulate;
8. only after these tests pass should one study more expensive spectral, positive, asymptotic, or arithmetic downstream operations.

## Consequence for the line

Add **vertical differential fidelity** to the Arithmetic Fidelity model library.

The main conceptual gain is a separation between two kinds of forgetting that AF-001 treats uniformly at the set level:

\[
\text{continuous loss}
\quad\text{vs.}\quad
\text{discrete/global loss}.
\]

On regular smooth quotients, continuous loss has a computable local rank and obeys a monotonicity law under further compression. Passing that test does not certify faithfulness; it merely removes the infinitesimal obstruction. The next general layer should address how singular strata, disconnected fibers, monodromy, or higher jets supplement the vertical-rank audit when first-order smooth data are insufficient.