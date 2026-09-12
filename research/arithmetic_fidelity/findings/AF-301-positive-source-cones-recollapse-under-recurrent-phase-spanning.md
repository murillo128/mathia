# AF-301 — Positive source cones re-collapse when discarded Dirichlet phases positively span the target plane

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `ZERO-COUNT`, `POSITIVE-CONE`, `KRONECKER-WEYL`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-300 leaves positivity as one of the first genuinely non-complex-linear source geometries that can evade its one-direction complex correction. Positivity does change the obstruction, but it does not make coordinate deletion freely faithful. The deleted linear subspace is replaced by a **positive cone of available correction vectors**, and once that cone fills the complex target plane the same fiber-saturation failure returns.

Let

\[
P_c(s)=\sum_{n=1}^N c_n n^{-s},
\qquad c\in\mathbb R_+^N,
\]

and split the coefficient indices into retained coordinates `S` and discarded coordinates `D`, with `S\sqcup D=\{1,\dots,N\}`. Let

\[
q_D(c)=c_S
\]

be the coordinate compression that forgets `c_D`. For a fixed observation point

\[
z=\sigma+it,
\]

write

\[
v_n(z)=n^{-z}\in\mathbb C\simeq\mathbb R^2,
\]

and define the positive response cones

\[
C_S(z)=\operatorname{cone}_+\{v_n(z):n\in S\},
\qquad
C_D(z)=\operatorname{cone}_+\{v_n(z):n\in D\}.
\]

Let

\[
H_z^+=\{c\in\mathbb R_+^N:P_c(z)=0\}
\]

be the positive-source failure set at `z`.

Then the image of this failure set under coordinate deletion is exactly

\[
\boxed{
q_D(H_z^+)
=
\left\{y\in\mathbb R_+^S:
-\sum_{n\in S}y_n v_n(z)\in C_D(z)
\right\}.
}
\tag{1}
\]

Consequently,

\[
\boxed{
q_D(H_z^+)=\mathbb R_+^S
\iff
-C_S(z)\subseteq C_D(z).
}
\tag{2}
\]

In particular, the source-independent sufficient condition

\[
\boxed{C_D(z)=\mathbb C}
\tag{3}
\]

forces **every** retained positive coefficient state to have a positive discarded-coordinate completion with a zero at `z`.

Condition (3) is purely angular. The factors `n^{-\sigma}` are positive scalars, so they do not affect the positive cone. Thus

\[
C_D(\sigma+it)=\mathbb C
\]

exactly when the phase rays

\[
\{e^{-it\log n}:n\in D\}
\]

positively span `\mathbb R^2`; equivalently, they are not all contained in any closed semicircle.

This gives an exact positive-source analogue of AF-300's complex-linear saturation theorem:

- complex-affine sources allow arbitrary complex correction coefficients, so one deleted complex direction can fill one complex scalar response;
- positive sources allow only nonnegative correction coefficients, so collapse is controlled by the **conic coverage** of the deleted response rays rather than by kernel dimension alone.

The distinction is real, but it is not a permanent escape. If `D` contains three integers `d_1,d_2,d_3` for which

\[
\log d_1,\log d_2,\log d_3
\]

are linearly independent over `\mathbb Q`, then there are arbitrarily large heights `t` for which their three phase rays positively span the whole complex plane. Hence for every real `\sigma`,

\[
\boxed{
C_D(\sigma+it)=\mathbb C
}
\tag{4}
\]

at infinitely many, indeed recurrent, heights.

Three distinct primes are the canonical arithmetic instance: if `p,q,r` are distinct primes then `\log p,\log q,\log r` are `\mathbb Q`-linearly independent by unique factorization. Therefore any positive-coordinate compression that forgets coefficients at three distinct prime indices re-enters complete fixed-observer saturation at arbitrarily large heights.

If a zero-count observation family contains one such point `z`, the boundary-zero discriminator cannot factor through `q_D`: a one-monomial positive source is boundary-safe on every contour, while (3) provides a positive failure completion with the same retained coordinates. Positivity has changed the local correction geometry from linear span to positive span, but recurrent Dirichlet phase mixing can restore the full signed target freedom that positivity initially removed.

## Exact cone-fiber criterion

For retained coefficients `y\in\mathbb R_+^S`, any source in the fiber `q_D^{-1}(y)` has the form

\[
c_n=y_n\quad(n\in S),
\qquad
c_d=x_d\ge0\quad(d\in D).
\]

The zero equation at `z` is

\[
\sum_{d\in D}x_d v_d(z)
=-\sum_{n\in S}y_n v_n(z).
\tag{5}
\]

The left side ranges exactly over `C_D(z)`. This proves (1). As `y` ranges over the retained positive orthant, the right-hand retained response ranges over `-C_S(z)`, giving (2).

The criterion is therefore stronger and more precise than saying merely that positivity blocks the AF-300 correction coefficient. Positivity blocks a fiber correction exactly while the negative retained response falls outside the deleted positive cone. Once the deleted rays positively span `\mathbb C`, there is no blocked response left.

This is also the correct place to distinguish positive-cone admissibility from bounded or normalized positive sources. Equation (1) permits the discarded coefficients to become arbitrarily large. A simplex constraint, coefficient cap, multiplicative relation, integrality condition, or another resource bound replaces `C_D(z)` by a bounded or discrete reachable set and can prevent saturation even when its recession cone is the full plane.

## Positive spanning in the complex plane

For finitely many nonzero vectors in `\mathbb R^2`, their positive span is the whole plane if and only if they are not contained in a closed half-plane through the origin. For unit complex phases this is equivalent to saying that the phases are not all contained in a closed semicircle.

A robust model configuration is

\[
1,
\qquad e^{2\pi i/3},
\qquad e^{4\pi i/3}.
\tag{6}
\]

The origin lies strictly inside their convex hull, so all sufficiently small angular perturbations of this triple still positively span `\mathbb R^2`. Hence full conic coverage is an open phase condition, not a measure-zero exact alignment.

There is also a sharp local count distinction. In a two-dimensional real target, one or two nonzero rays cannot positively span the whole plane: a positive spanning set requires at least three vectors. Thus positivity genuinely raises the simplest coordinate-deletion saturation mechanism from the two real degrees of freedom of one unrestricted complex coefficient to at least three one-sided coordinate rays. What matters after that threshold, however, is their angular placement rather than their number alone.

## Kronecker-Weyl recurrence restores full conic coverage

Assume `D` contains `d_1,d_2,d_3` with `\log d_1,\log d_2,\log d_3` linearly independent over `\mathbb Q`. Consider the continuous torus flow

\[
t\longmapsto
\left(
-t\log d_1,
-t\log d_2,
-t\log d_3
\right)
\pmod{2\pi}.
\tag{7}
\]

Kronecker-Weyl implies that this flow is dense, in fact equidistributed, in `\mathbb T^3`. Choose an open neighborhood `\mathcal U` of the target phase triple

\[
(0,2\pi/3,4\pi/3)
\]

small enough that every triple in `\mathcal U` still positively spans `\mathbb R^2`. Equidistribution gives arbitrarily large `t` with the phase vector (7) in `\mathcal U`.

At every such height, the three discarded Dirichlet response rays already satisfy

\[
\operatorname{cone}_+
\{d_j^{-\sigma-it}:j=1,2,3\}
=\mathbb C
\]

for every `\sigma`, because the factors `d_j^{-\sigma}` only rescale the rays positively. Enlarging `D` cannot destroy positive spanning, proving (4).

For distinct primes the independence hypothesis is automatic. An integer relation

\[
a\log p+b\log q+c\log r=0
\]

would imply

\[
p^a q^b r^c=1,
\]

and unique factorization forces `a=b=c=0`.

Thus the very multiplicative independence that makes prime logarithms useful as torus frequencies also works **against** positivity as a permanent fidelity repair: over sufficiently broad height ranges, the forgotten prime-coordinate phases explore configurations that generate every signed complex correction through nonnegative coefficients.

## Zero-count collision consequence

Let `\Gamma` be any contour containing a point `z` where (3) holds. Suppose first that `S` is nonempty, and choose `m\in S`. The monomial source

\[
b=e_m
\]

satisfies

\[
P_b(s)=m^{-s}\ne0
\]

for every finite `s`, so it is boundary-safe on every contour.

By (3), the retained state `q_D(b)` has a completion `b'\in\mathbb R_+^N` with

\[
q_D(b')=q_D(b),
\qquad
P_{b'}(z)=0.
\]

Hence `b` and `b'` are indistinguishable after coordinate deletion but lie on opposite sides of exact boundary-failure membership. The zero-count discriminator cannot factor through `q_D`.

If `S` is empty, positive spanning itself supplies a nonzero positive dependence among the discarded rays, hence a nonzero failure source, while any monomial source remains safe; the trivial quotient is again nonfaithful.

The conclusion is exact but local in the observation family. Kronecker-Weyl supplies arbitrarily large dangerous heights; it does **not** say that an arbitrary preassigned compact contour contains one of them.

## Prior art and novelty assessment

The mathematical ingredients are classical, and no claim is made that positive spanning or Kronecker-Weyl recurrence is new.

- Andrew R. Conn, Katya Scheinberg, and Luis N. Vicente, *Introduction to Derivative-Free Optimization*, SIAM/MOS (2009), Chapter 2, develops positive spans and positive bases. In `\mathbb R^2`, the full-plane criterion used here is elementary convex-cone geometry.
- Alexandre Bailleul, “Explicit Kronecker-Weyl theorems and applications to prime number races,” *Research in Number Theory* 8 (2022), develops explicit discrete and continuous Kronecker-Weyl formulations and illustrates the arithmetic use of torus flows. The density statement used above is classical Kronecker-Weyl.
- The `\mathbb Q`-linear independence of logarithms of distinct primes is the elementary unique-factorization consequence written above.

A targeted search did not supply grounds for treating the ingredients as novel. The durable Arithmetic Fidelity contribution is their specialization to AF-300's live source-geometry question: **one-sided source constraints replace linear nullspace saturation by a reachable positive cone, but multiplicatively independent Dirichlet phases can make that cone equal the full complex response plane recurrently.**

This is a partial obstruction, not a classification of positive sources.

## Boundaries and failure modes

- The source is the full unbounded positive orthant `\mathbb R_+^N`. Coefficient caps, simplex normalization, integrality, multiplicative coupling, sparsity, or another bounded/discrete admissible geometry can invalidate the conic saturation step.
- The compression is coordinate deletion. A general nonlinear positive-source representation can have different fibers and is not covered.
- The recurrent theorem requires three discarded indices with `\mathbb Q`-independent logarithms. Three distinct primes suffice; dependent composite indices need separate analysis.
- Kronecker-Weyl gives dangerous heights in an unbounded observation family. It does not force positive spanning on a specified finite contour or finite height band.
- Full conic coverage is sufficient for collapse independently of the retained set. The exact fixed-point criterion is the weaker relation `-C_S(z)\subseteq C_D(z)` from (2); useful failures can therefore occur even when `C_D(z)\ne\mathbb C`.
- The result concerns finite Dirichlet polynomials and exact zero membership at an observation point. It supplies no analytic continuation, zero matching, asymptotic coefficient model, or RH consequence.

## Consequence for the research line

AF-300's positive-source escape is now narrower. Positivity is a genuine categorical change: it prevents an arbitrary complex correction along one deleted coordinate. But the correct replacement invariant is **conic reachability**, not simply a smaller effective dimension.

For coordinate deletion, the first required audit is now exact: compute the deleted response cone at the target observation layer. If that cone covers the negative retained response cone, the compressed fibers are saturated by failure sources. If the forgotten set contains three multiplicatively independent indices and the target ranges over unbounded heights, Kronecker-Weyl guarantees recurrent full-plane conic coverage.

The live escape moves to source constraints that also limit **magnitude, normalization, discreteness, multiplicative coupling, or allowable phase combinations**, or to representations whose fibers are not coordinate-deletion cones. Any proposed positive arithmetic compression should therefore state its reachable correction set, not merely point to nonnegativity as protection from AF-300.