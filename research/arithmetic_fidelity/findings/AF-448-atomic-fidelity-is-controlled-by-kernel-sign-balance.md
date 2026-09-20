# AF-448 — Atomic fidelity is controlled by kernel sign balance, not rank alone

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `ATOMIC-MEASURES`, `SPARSE-UNIQUENESS`, `ORIENTED-CIRCUITS`, `CHEBYSHEV-SYSTEM`, `NO-NOVELTY-CLAIM`

## Claim

AF-447 shows that generalized power-moment fidelity is governed by a Chebyshev cardinality threshold. The underlying obstruction can be stated without moments and, for positive sources, it is finer than ordinary rank or spark.

Let `X` be a set, let

\[
\Phi:X\to\mathbb R^m,
\qquad
\Phi(x)=(\phi_1(x),\ldots,\phi_m(x)),
\]

and let the linear observation of a finite atomic signed measure be

\[
\mathcal M_\Phi\!\left(\sum_i a_i\delta_{x_i}\right)
=\sum_i a_i\Phi(x_i).
\]

Write `A_r^\pm` for signed measures with at most `r` distinct atoms and `A_r^+` for nonnegative measures with at most `r` distinct atoms, including the zero measure.

For a nonzero finite atomic kernel relation

\[
\sigma=\sum_i c_i\delta_{x_i}\in\ker\mathcal M_\Phi,
\]

after combining repeated support points define

\[
n_+(\sigma)=\#\{i:c_i>0\},
\qquad
n_-(\sigma)=\#\{i:c_i<0\}.
\]

Then:

### Signed sources: ordinary spark is exact

Define the atomic spark

\[
s(\Phi)
=\min_{0\ne\sigma\in\ker\mathcal M_\Phi}
|\operatorname{supp}\sigma|,
\]

with `s(\Phi)=\infty` when no finite atomic kernel relation exists. Then

\[
\boxed{
\mathcal M_\Phi\text{ is injective on }A_r^\pm
\iff
s(\Phi)>2r.
}
\]

Equivalently, every collection of at most `2r` distinct evaluation vectors `\Phi(x)` must be linearly independent.

### Positive sources: sign balance is the exact invariant

Define the balanced-kernel index

\[
b(\Phi)
=\min_{0\ne\sigma\in\ker\mathcal M_\Phi}
\max\{n_+(\sigma),n_-(\sigma)\},
\]

again with value `\infty` when there is no finite atomic kernel relation. Then

\[
\boxed{
\mathcal M_\Phi\text{ is injective on }A_r^+
\iff
b(\Phi)>r.
}
\]

Thus positivity can preserve exact fidelity even when ordinary spark already permits a signed collision. What matters is not only whether the observation columns are dependent, but whether a kernel dependence has sufficiently few positive and negative coefficients to split into two admissible positive sources.

Always

\[
\boxed{
\left\lceil\frac{s(\Phi)}2\right\rceil
\le b(\Phi)\le s(\Phi)
}
\]

when a finite atomic kernel relation exists. The lower bound is purely cardinal: a relation with `q` nonzero coefficients has `\max(n_+,n_-)\ge\lceil q/2\rceil`. The upper bound follows by taking a spark-minimizing relation.

Consequently, **rank/spark is a complete fidelity invariant for unconstrained signed sparse sources, but not for positive sparse sources**. The orientation of kernel relations is additional retained structure.

## Exact proof

### Signed case

If two distinct measures `\mu,\nu\in A_r^\pm` have the same observation, then

\[
0\ne\sigma=\mu-\nu\in\ker\mathcal M_\Phi
\]

has at most `2r` support points. Hence `s(\Phi)\le2r`.

Conversely, suppose a nonzero kernel relation `\sigma` has `q\le2r` atoms. Partition its support into two sets `I,J` with `|I|\le r` and `|J|\le r`, and write

\[
\mu=\sum_{i\in I}c_i\delta_{x_i},
\qquad
\nu=-\sum_{j\in J}c_j\delta_{x_j}.
\]

Then `\mu,\nu\in A_r^\pm`, `\mu\ne\nu`, and `\mathcal M_\Phi(\mu)=\mathcal M_\Phi(\nu)`. The coefficients may have either sign, so only total support cardinality matters.

### Positive case

If distinct `\mu,\nu\in A_r^+` collide, then `\sigma=\mu-\nu` is a nonzero kernel relation. After cancellation of common support points, every positive coefficient of `\sigma` comes from an atom of `\mu` and every negative coefficient from an atom of `\nu`. Therefore

\[
n_+(\sigma)\le r,
\qquad
n_-(\sigma)\le r,
\]

so `b(\Phi)\le r`.

Conversely, if a kernel relation satisfies `n_+(\sigma)\le r` and `n_-(\sigma)\le r`, its Jordan decomposition

\[
\sigma=\sigma_+-\sigma_-
\]

has `\sigma_+,\sigma_-\in A_r^+` and

\[
\mathcal M_\Phi(\sigma_+)
=
\mathcal M_\Phi(\sigma_-).
\]

This proves the criterion. In oriented-matroid language, support-minimal kernel witnesses are signed circuits; the positive-source obstruction is therefore a circuit-sign obstruction rather than an unoriented dependence obstruction.

## Positivity can beat spark

The distinction is real even in the smallest example. Let `X={u,v}` and use one scalar channel

\[
\Phi(u)=1,
\qquad
\Phi(v)=-1.
\]

The two columns are dependent, so `s(\Phi)=2` and signed one-atom fidelity fails:

\[
\mathcal M_\Phi(\delta_u)
=
\mathcal M_\Phi(-\delta_v)=1.
\]

But the only kernel relation is proportional to

\[
\delta_u+\delta_v,
\]

whose two coefficients have the same sign. Hence `b(\Phi)=2`, and the map is injective on positive one-atom sources: atoms at `u` produce positive observations and atoms at `v` negative observations, with the magnitude recovering the weight.

So a source-cone law can remove collisions without changing ambient observation rank or ordinary spark. This is the exact finite-atomic version of the broader Arithmetic Fidelity principle that **admissible orientation can carry discriminator information invisible to a dimension count**.

## Chebyshev systems are maximally balanced at the threshold

Now suppose `X` is ordered and `\phi_1,\ldots,\phi_m` form a strict Chebyshev system. Then any `m` distinct evaluation columns are linearly independent. If `X` contains at least `m+1` points,

\[
s(\Phi)=m+1.
\]

For ordered points

\[
x_1<\cdots<x_{m+1},
\]

the one-dimensional dependence among their `m+1` evaluation columns has alternating coefficient signs. This follows directly from the cofactor formula: deleting consecutive columns from the Chebyshev evaluation matrix gives nonzero minors of one common orientation, while the cofactor sign alternates.

Therefore the smallest positive/negative side of a kernel collision is not hidden in an arbitrary dependence. It is fixed by alternation, and

\[
\boxed{
b(\Phi)=\left\lceil\frac{m+1}{2}\right\rceil.}
\]

This gives a sharp three-level classification for positive atomic sources:

- with `m=2K-1` Chebyshev channels, an alternating circuit on `2K` points has `K` positive and `K` negative coefficients, so two distinct positive `K`-atomic sources can collide;
- with `m=2K` channels, every positive `K`-atomic source is uniquely determined among positive sources with at most `K` atoms, because `b=K+1`, yet an alternating circuit on `2K+1` points has side sizes `K` and `K+1`, so a `K`-atomic source can still collide with a `(K+1)`-atomic source;
- with `m=2K+1` channels, no relation supported on at most `2K+1` points exists, so every at-most-`K`-atomic source is separated from every `(K+1)`-atomic source.

The middle line is the missing distinction behind AF-447: **`2K` Chebyshev coordinates already identify the nuisance source inside the fixed `K`-atomic model, but they do not certify that an extra atom is absent.** Detecting a cardinality increase costs one additional coordinate because the competing difference may use `2K+1` support points.

AF-447's inverse-function construction remains stronger in a different direction: it shows that the `K` versus `K+1` collision at `2K` coordinates can occur arbitrarily close to any regular prescribed positive `K`-atomic base source with a sufficiently small added atom. The circuit argument here explains the global combinatorial obstruction but does not replace that local-conditioning statement.

## Generalized power moments are an oriented-circuit instance, not an arithmetic discriminator

For strictly increasing real exponents

\[
\lambda_1<\cdots<\lambda_m
\]

on `(0,\infty)`, the observation curve

\[
\Phi_\Lambda(x)
=
(x^{\lambda_1},\ldots,x^{\lambda_m})
\]

is a Chebyshev system. Hence its atomic spark and balanced-kernel index are exactly the values above. This recovers the exact cardinality thresholds in AF-447 without using consecutiveness, Hankel structure, or a special moment normalization.

The same conclusion holds after restricting the allowed support to any ordered subset of `(0,\infty)` containing enough points, including reciprocal-power arithmetic skeletons previously used in this line. The relevant minors remain nonzero with the same orientation. Therefore **Chebyshev alternation itself cannot distinguish rational primes from matched positive non-prime supports**. Any prime-specific gain must come from an additional arithmetic source law that excludes the offending signed circuits, restricts admissible support/weight patterns, or supplies genuinely independent coordinates.

This sharpens the source-law frontier: lowering an observation threshold is not justified merely by saying that the admissible family has fewer parameters. One must show that the source law actually removes every kernel sign pattern capable of being split into two admissible sources.

## Prior art and novelty audit

The component mathematics is classical and no novelty is claimed for spark, sparse uniqueness, signed circuits, Chebyshev alternation, or nonnegative sparse recovery.

- David L. Donoho and Michael Elad, **“Optimally Sparse Representation in General (Nonorthogonal) Dictionaries via L1 Minimization,”** *Proceedings of the National Academy of Sciences* 100(5), 2197–2202 (2003), DOI `10.1073/pnas.0437847100`, introduce dictionary spark and prove the classical `spark>2r` uniform sparse-uniqueness threshold.
- K. Mahesh Krishna, **“Continuous Donoho-Elad Spark Uncertainty Principle,”** arXiv:`2509.00001` (2025), extends spark language to linear maps on measure spaces. Its support-size notion is measure-theoretic and its general theorem gives the forward sparse-uniqueness implication; the finite-atomic cardinality setting here permits the converse by literally partitioning a finite kernel support.
- Anders Björner, Michel Las Vergnas, Bernd Sturmfels, Neil White, and Günter M. Ziegler, ***Oriented Matroids***, 2nd ed., Cambridge University Press (1999), is the standard source for signed circuits of realizable vector configurations and the sign data carried by minimal linear dependences.
- Samuel Karlin and William J. Studden, ***Tchebycheff Systems: With Applications in Analysis and Statistics***, Interscience/Wiley (1966), supplies the classical Chebyshev-system and moment-space framework behind evaluation-minor orientation and alternation.
- David L. Donoho and Jared Tanner, **“Sparse Nonnegative Solution of Underdetermined Linear Equations by Linear Programming,”** *Proceedings of the National Academy of Sciences* 102(27), 9446–9451 (2005), DOI `10.1073/pnas.0502269102`, connects nonnegative sparse recovery with convex-polytope neighborliness. That recovery problem is not identical to bounded-cardinality injectivity here, but it confirms that positivity changes sparse identifiability through sign/convex geometry rather than through ordinary rank alone.

The Arithmetic Fidelity contribution is the exact reusable audit extracted from these classical languages: for finite atomic compression, **signed fidelity is controlled by support size of kernel relations, positive fidelity by their positive/negative support balance, and Chebyshev channels have alternating circuits that make the relevant positive collision budgets sharp**. This explains why the `2K`, `2K+1` thresholds in AF-447 are model-comparison thresholds rather than merely parameter counts.

## Boundaries and falsification checks

- The sign-balance criterion is for real linear observations. Complex channels require a realification or a separate phase-sensitive formulation; coefficient sign is not intrinsically defined over `\mathbb C`.
- Atomicity is essential to the converse proof. The support is counted by number of atoms, not by ambient measure. General support-measure versions of continuous spark need not admit the finite-support partition argument.
- The zero measure is included in `A_r^+` and `A_r^\pm`. If a source model excludes zero or imposes fixed total mass, the admissible collision criterion must include that additional source law.
- The criterion concerns exact noiseless injectivity. It says nothing by itself about distance between observation classes, condition number, or stable decoding; AF-447's boundary transversality remains a separate robustness gate.
- A source law helps only if it excludes an actual balanced kernel relation or supplies independent information. Rephrasing the target discriminator as a constraint is source-law smuggling.
- Chebyshev alternation is universal over ordered support points. Its circuit orientation is therefore not evidence of rational-prime specificity.

## Consequence for the line

The finite-atomic frontier now has a more precise invariant than latent dimension alone. Given a proposed compression and source law, first inspect the finite kernel relations of its evaluation dictionary. For signed sources, support cardinality is enough. For positive or otherwise cone-constrained sources, retain the **orientation/sign budget** of those relations and ask whether the admissible source class can realize both sides.

For arithmetic applications this yields a concrete next gate: a claimed source law lowers the required observation count only if it can be proved to eliminate the balanced kernel circuits reproduced by matched non-prime controls. If both rational-prime and control sources realize the same oriented circuit structure, the compression remains arithmetically unfaithful even when it is perfectly identifiable inside a narrower nuisance model.
