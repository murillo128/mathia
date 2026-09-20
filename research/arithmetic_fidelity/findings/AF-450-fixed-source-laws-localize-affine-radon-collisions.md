# AF-450 — Fixed source laws localize affine Radon collisions

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `SOURCE-LAW`, `FIBERWISE-RADON`, `SPARSE-UNIQUENESS`, `NO-NOVELTY-CLAIM`

## Claim

AF-449 shows that a known total mass changes positive sparse fidelity from conic kernel geometry to affine/Radon geometry. Its boundary note also identifies the next obstruction: with several prescribed source statistics, simply appending the corresponding functions only tests whether two sources have the **same** statistics; it does not say that their common value is the particular prescribed value defining the source class.

That distinction admits an exact classification.

Let

\[
\Psi:X\to\mathbb R^q,
\qquad
\Phi:X\to\mathbb R^m
\]

be respectively a source-law feature map and an observed feature map. For `M>0`, `r\ge1`, and `u\in\mathbb R^q`, define the fixed-source-law class

\[
\mathcal P_{r,M,u}^{\Psi}
=
\left\{
\mu=\sum_{i=1}^k a_i\delta_{x_i}:
1\le k\le r,
\ a_i>0,
\ \mu(X)=M,
\ \int\Psi\,d\mu=M u
\right\}.
\tag{1}
\]

The retained observation is

\[
\mathcal M_\Phi(\mu)=\int\Phi\,d\mu.
\]

For every nonzero finite signed atomic measure `sigma` satisfying

\[
\int (1,\Psi,\Phi)\,d\sigma=0,
\tag{2}
\]

write its Jordan decomposition as `sigma=sigma_+-sigma_-`. The constant coordinate in `(2)` forces

\[
\sigma_+(X)=\sigma_-(X)=:t>0,
\]

and the `Psi` coordinates force the two normalized sides to have one common source-law barycenter

\[
u(\sigma)
:=
\frac1t\int\Psi\,d\sigma_+
=
\frac1t\int\Psi\,d\sigma_-.
\tag{3}
\]

Define the **fiberwise affine balanced-kernel index**

\[
b_u(\Psi,\Phi)
=
\min_{\substack{0\ne\sigma\\
\int(1,\Psi,\Phi)\,d\sigma=0\\
 u(\sigma)=u}}
\max\{n_+(\sigma),n_-(\sigma)\},
\tag{4}
\]

with value `+infinity` when no such finite atomic relation exists.

Then

\[
\boxed{
\mathcal M_\Phi
\text{ is injective on }
\mathcal P_{r,M,u}^{\Psi}
\iff
b_u(\Psi,\Phi)>r.
}
\tag{5}
\]

Thus a fixed affine source law does not merely add coordinates to a global dictionary. It **localizes the relevant Radon circuits by their source-law barycenter**. A low-support affine collision matters to the prescribed class only when its two positive sides lie in the same required `Psi` fiber.

Equivalently, define the order-`r` source-law collision locus

\[
\mathcal U_r(\Psi,\Phi)
=
\{u\in\mathbb R^q:b_u(\Psi,\Phi)\le r\}.
\tag{6}
\]

Then the fixed source law `u` preserves exact `r`-atomic fidelity precisely when

\[
\boxed{u\notin\mathcal U_r(\Psi,\Phi).}
\tag{7}
\]

This separates two questions that a global augmented-rank test conflates: **does any admissible source-law value support a sparse collision, and does the particular source-law value under study support one?**

## Exact derivation

Suppose first that distinct

\[
\mu,\nu\in\mathcal P_{r,M,u}^{\Psi}
\]

have the same retained observation. Set

\[
\sigma=\mu-\nu.
\]

Equal mass gives

\[
\int1\,d\sigma=0,
\]

equal prescribed source law gives

\[
\int\Psi\,d\sigma=0,
\]

and the collision gives

\[
\int\Phi\,d\sigma=0.
\]

After cancelling common atoms,

\[
n_+(\sigma)\le r,
\qquad
n_-(\sigma)\le r.
\]

Moreover the positive and negative parts both have total mass `M` and `Psi` moment `Mu`, so `(3)` gives

\[
u(\sigma)=u.
\]

Hence

\[
b_u(\Psi,\Phi)\le r.
\]

Conversely, suppose a relation in `(4)` has

\[
n_+(\sigma),n_-(\sigma)\le r.
\]

Its two positive parts have equal mass `t`, equal `Psi` moment `tu`, and equal `Phi` moment. Rescale both by `M/t`:

\[
\mu=\frac Mt\sigma_+,
\qquad
\nu=\frac Mt\sigma_-.
\]

Then `mu` and `nu` are distinct members of `(1)` and

\[
\mathcal M_\Phi(\mu)=\mathcal M_\Phi(\nu).
\]

This proves `(5)`. No dimension argument is involved: the exact invariant is the existence of an admissible signed circuit with the correct **barycentric label** `u`.

## Uniform source-law fidelity is the global augmented criterion

Let

\[
F=(\Psi,\Phi):X\to\mathbb R^{q+m}.
\]

AF-449's affine balanced-kernel index for the joint map is

\[
b_{\mathrm{aff}}(F)
=
\min_{\substack{0\ne\sigma\\
\int(1,\Psi,\Phi)\,d\sigma=0}}
\max\{n_+(\sigma),n_-(\sigma)\}.
\tag{8}
\]

Every relation counted in `(8)` has exactly one barycentric label `u(sigma)` from `(3)`. Therefore

\[
\boxed{
b_{\mathrm{aff}}(F)=\inf_{u\in\mathbb R^q} b_u(\Psi,\Phi).}
\tag{9}
\]

Since the values are positive integers or `+infinity`, the infimum is a minimum whenever a finite relation exists.

Consequently the following are equivalent:

1. `M_Phi` is injective on every fixed-source-law fiber `P_{r,M,u}^Psi`;
2. the joint observation
   \[
   \mu\mapsto\left(\int\Psi\,d\mu,\int\Phi\,d\mu\right)
   \]
   is injective on all fixed-mass positive sources with at most `r` atoms;
3. `b_aff(Psi,Phi)>r`.

The augmented global test is therefore **exact for uniform fidelity over all source-law values**, but it can be strictly too pessimistic for one externally fixed value `u`. Equation `(9)` identifies precisely why: it takes the worst source-law fiber.

## Convex-geometric form

Normalize by the fixed mass and consider the joint point configuration

\[
F(x)=(\Psi(x),\Phi(x)).
\]

Every source in `(1)` produces a convex combination

\[
(u,y)
=
\left(
\frac1M\int\Psi\,d\mu,
\frac1M\int\Phi\,d\mu
\right)
\in\operatorname{conv}F(X)
\tag{10}
\]

using at most `r` points. A collision inside the prescribed source class is exactly a point `(u,y)` admitting two distinct convex representations whose two supports both have size at most `r`.

Hence `U_r` is the projection onto the `Psi` coordinates of the sparse Radon-collision set of the joint configuration. The source law does not need to make the whole joint configuration affinely independent. It only needs to place the required slice

\[
\{u\}\times\mathbb R^m
\]

away from every low-support Radon point.

This is stronger than the slogan that constraints reduce latent dimension. A constraint can remove a collision even when it does not alter the ambient affine rank, and it can fail completely even when it removes nominal degrees of freedom. The decisive object is **which signed circuits intersect the prescribed affine slice**.

## Control: one bad Radon fiber need not contaminate another

Take four source points whose joint features form the square

\[
F(X)=
\{(0,0),(0,1),(1,0),(1,1)\},
\]

where the first coordinate is `Psi` and the second is `Phi`. Let `M=1` and `r=2`.

At source-law value

\[
u=\frac12,
\]

the two diagonals give the collision

\[
\frac12\delta_{(0,0)}+\frac12\delta_{(1,1)}
\quad\text{and}\quad
\frac12\delta_{(0,1)}+\frac12\delta_{(1,0)}.
\tag{11}
\]

Both sources have `Psi` mean `1/2` and `Phi` mean `1/2`, so

\[
b_{1/2}(\Psi,\Phi)=2.
\]

Thus the joint configuration fails uniform two-atomic fidelity and

\[
b_{\mathrm{aff}}(F)=2.
\]

But at source-law value `u=0`, positivity plus `int Psi dmu=0` forces every admissible source to be supported on the two points with `Psi=0`. On those two points the scalar `Phi` mean uniquely determines the mixture weight. Therefore

\[
b_0(\Psi,\Phi)=+\infty,
\]

and `M_Phi` is injective on the entire `u=0` fiber, even though the global augmented dictionary already contains a balanced two-versus-two Radon circuit.

This is the required falsification of the naive rule “if the augmented configuration has an `r`-sparse circuit, every fixed source law is unfaithful.” The circuit is fatal only at its own source-law barycenter.

## Control: a vacuous source law buys nothing

If `Psi` is constant, say

\[
\Psi(x)=u_0
\]

for every `x`, then every fixed-mass source automatically lies in the same source-law fiber `u_0`. Every affine kernel relation has barycentric label `u_0`, so

\[
b_{u_0}(\Psi,\Phi)=b_{\mathrm{aff}}(\Phi).
\tag{12}
\]

The extra source statistic contributes no fidelity. More generally, a prescribed constraint is useful only to the extent that it excludes the actual low-support collision circuits of the retained observation.

## Prior art and novelty audit

The underlying convex and moment-set mathematics is classical, and no novelty is claimed for affine dependence, Radon partitions, generalized moment constraints, or finite-atomic descriptions of moment sets.

- H. Radon, **“Mengen konvexer Körper, die einen gemeinsamen Punkt enthalten,”** *Mathematische Annalen* 83 (1921), 113–115, is the classical source for converting affine dependence into intersecting convex hulls.
- A. Björner, M. Las Vergnas, B. Sturmfels, N. White, and G. M. Ziegler, ***Oriented Matroids***, 2nd ed., Cambridge University Press (1999), supplies the signed-circuit language for realizable affine configurations used already in AF-448 and AF-449.
- Gerhard Winkler, **“Extreme Points of Moment Sets,”** *Mathematics of Operations Research* 13(4), 581–587 (1988), DOI `10.1287/moor.13.4.581`, treats probability-measure sets defined by finitely many generalized moment conditions and characterizes their extreme points.
- Iosif Pinelis, **“On the Extreme Points of Moments Sets,”** *Mathematical Methods of Operations Research* 83, 325–349 (2016), DOI `10.1007/s00186-015-0530-0`, gives necessary and sufficient extreme-point conditions for prescribed generalized moment sets and finite-atomic representations under appropriate hypotheses.
- Didier Henrion, Martin Kružík, and Stephan Weis, **“Extreme Points and Faces in the Moment Problem,”** arXiv:`2606.21391` (2026), gives a recent convex-geometric treatment of affinely constrained measure sets, including a characterization of extreme points through injectivity of the constraint map on the smallest containing face and a modern account of finite-atomic moment representations.

Those works establish that prescribed generalized moments define classical convex moment fibers and that affine independence/injectivity is central to their extremal structure. The exact statement `(5)` is derived here directly from Jordan decomposition and Radon geometry; this audit did not locate grounds for a novelty claim. Its durable Arithmetic Fidelity role is narrower: **label every sparse affine collision by the source-law barycenter it realizes, and test only the collision locus belonging to the prescribed source class**. Equation `(9)` then cleanly separates one-fiber fidelity from uniform fidelity across all source-law values.

## Boundaries and falsification checks

- Fixed total mass is part of the theorem. It permits normalization of both sides of a signed relation to probability measures. Without fixed mass the relevant geometry is conic, and the source-law label requires a different formulation.
- The source laws in `(1)` are affine moment constraints. Nonlinear constraints on the measure need not reduce to a barycentric label or to an augmented linear feature map.
- The result concerns exact noiseless injectivity. A fiber can have no exact sparse Radon collision while admitting sequences of nearly colliding sources. Exact exclusion therefore does not imply a positive conditioning margin.
- The Euclidean distance from `u` to `U_r` is not an intrinsic robustness quantity without a normalization/metric on the source-law coordinates. Rescaling `Psi` changes that distance while leaving exact fidelity unchanged.
- The theorem does not say that more source constraints monotonically improve fidelity for an unrelated prescribed class. It says that a given class is faithful exactly when no admissible balanced relation realizes its prescribed values.
- An arbitrary target-dependent `Psi` can trivially encode the answer and is excluded by the line mandate's no-smuggling rule. A useful arithmetic source law must be independently justified and must remove circuits that matched controls still realize.
- Global augmented injectivity is stronger than needed for one fixed `u` but is exactly the right criterion when one wants one decoder valid uniformly over all `u`.
- Empty source-law fibers are vacuously injective. This is not evidence of useful recovery; any application must separately establish that the intended source actually belongs to the prescribed class.
- Nothing here identifies a rational-prime discriminator or implies RH. It supplies a sharper gate for testing future arithmetic constraints.

A direct falsification of `(5)` would require either a collision inside one fixed source-law fiber whose difference fails `(2)` or has a different barycentric label, or a relation counted by `(4)` whose two Jordan parts cannot be rescaled into a collision in `(1)`. Equal affine moments rule out the first possibility, and the common positive mass `t` rules out the second.

## Consequence for the research line

The source-law question can now be split into two exact layers. First compute or characterize the sparse Radon collision locus `U_r` of the joint source/observation geometry. Then ask whether the independently justified arithmetic source value lies outside that locus. This is strictly sharper than counting source parameters or appending all known constraints and demanding global injectivity.

For future arithmetic applications, the key theorem surface is therefore not “a constraint lowers dimension,” but:

\[
\boxed{
\text{the arithmetic source law places the true source fiber outside every matched low-support collision locus.}
}
\]

The next unresolved step is quantitative. Once exact fiberwise collisions are excluded, one still needs a coordinate-invariant separation/conditioning notion for near-collisions inside the same prescribed source-law fiber, together with matched controls showing whether any positive margin is genuinely arithmetic rather than a generic consequence of the constraint geometry.
