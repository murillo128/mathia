# AF-022 — Finite Weil test vectors have arbitrarily local Beurling-deformation collisions

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`

## Claim

Fix `A>0` and a finite family of real test functions

\[
F_1,\ldots,F_d\in C_c^\infty(0,A),
\qquad d\ge1.
\]

For a locally finite multiset `Q={q_j}` of generalized-prime generator norms satisfying the hypotheses of AF-020, write `\ell_j=\log q_j` and

\[
W_Q(F)
=
\sum_j\sum_{m\ge1}
\ell_j e^{-m\ell_j/2}F(m\ell_j).
\]

Choose an interval

\[
I=(a,b),
\qquad
\frac A2<a<b<A,
\]

and any fixed generalized-prime background multiset `B`. Let

\[
N=d+1
\]

and choose any strictly ordered center

\[
c=(c_1,\ldots,c_N),
\qquad
a<c_1<\cdots<c_N<b.
\]

For an ordered tuple

\[
\ell=(\ell_1,\ldots,\ell_N)
\]

near `c`, define the finite Beurling deformation

\[
Q_\ell
=
B\sqcup\{e^{\ell_1},\ldots,e^{\ell_N}\}.
\]

Then:

1. **Every sufficiently small sphere around every such center contains an exact finite-test collision.** For every sufficiently small `r>0`, there is a unit vector `u\in S^d\subset\mathbb R^{d+1}` such that, with
   \[
   \ell^+=c+ru,
   \qquad
   \ell^-=c-ru,
   \]
   both tuples remain strictly ordered in `I` and
   \[
   \boxed{
   W_{Q_{\ell^+}}(F_i)
   =
   W_{Q_{\ell^-}}(F_i)
   \qquad(1\le i\le d).
   }
   \]

2. **The two generalized-prime systems are genuinely distinct.** Since `u\ne0`, the ordered tuples `\ell^+` and `\ell^-` differ. Strict ordering makes each tuple the unique sorted representative of its added generator multiset, so
   \[
   Q_{\ell^+}\ne Q_{\ell^-}
   \]
   as multisets.

3. **The collision is an actual prime-power-model collision, not an ambient moment-cone witness.** The systems share the entire background `B` and differ only in `d+1` generator norms lying in the compact norm window `(e^a,e^b)`. Their generalized-prime counting functions therefore agree below `e^a` and above `e^b`.

4. **The finite-test map is noninjective on every neighborhood of every center in this `(d+1)`-parameter deformation chamber.** The radius `r` may be chosen arbitrarily small. Hence exact collisions persist at arbitrarily fine scales even though all test values are known with infinite precision.

5. This closes the main arithmetic gap left by AF-021 for one natural matched-control class: finite-dimensional test compression is non-faithful not only on the ambient cone of arbitrary positive measures, but already on a continuously deformable Beurling generalized-prime family whose prime-power weights and locations obey the exact multiplicative structure of AF-020.

The conclusion is still weaker than saying that the **ordinary rational-prime point itself** has a nontrivial fiber. Borsuk--Ulam produces a colliding antipodal pair around the chosen center, not necessarily a second system with the same test vector as the center. A route claiming that finitely many tests uniquely characterize the rational primes could therefore survive only by proving a special-point rigidity theorem; it cannot infer such rigidity from local injectivity of the surrounding generalized-prime model, because that local injectivity is impossible.

## Why the upper half of the support window linearizes the prime-power constraint

AF-021's generic Radon/Tverberg witnesses are arbitrary positive atomic measures and therefore need not lie in the nonlinear image

\[
Q\longmapsto\omega_Q
=
\sum_j\sum_{m\ge1}
\ell_j e^{-m\ell_j/2}\delta_{m\ell_j}.
\]

The interval `I\subset(A/2,A)` gives a simple exact way around that obstruction.

If an added generator logarithm satisfies

\[
\ell_j>\frac A2,
\]

then every higher prime-power location obeys

\[
m\ell_j>A
\qquad(m\ge2).
\]

Since every `F_i` is supported in `(0,A)`, those higher powers are invisible to all retained tests. The entire contribution of the added generator `e^{\ell_j}` is therefore its first-power term

\[
\ell_j e^{-\ell_j/2}F_i(\ell_j).
\]

Define

\[
h_i(t)=t e^{-t/2}F_i(t).
\]

For the deformation tuple `\ell`, the retained vector is exactly

\[
\Psi(\ell)
=
\bigl(W_{Q_\ell}(F_1),\ldots,W_{Q_\ell}(F_d)\bigr)
=
C_B+
\left(
\sum_{j=1}^{d+1}h_1(\ell_j),
\ldots,
\sum_{j=1}^{d+1}h_d(\ell_j)
\right),
\]

where `C_B` is the fixed contribution of the background.

Thus the full prime-power coupling has not been discarded or approximated. It is present in the model, but the declared finite support makes all higher powers of these particular generators exactly invisible. On this chamber the retained destination becomes a continuous map from `d+1` free generator coordinates to only `d` real outputs.

## Borsuk--Ulam gives an exact collision on every small sphere

Let

\[
U
=
\{(\ell_1,\ldots,\ell_{d+1})\in I^{d+1}:
\ell_1<\cdots<\ell_{d+1}\}.
\]

This is an open subset of `\mathbb R^{d+1}`, and the center `c` lies in `U`. Choose `r>0` small enough that

\[
c+r\overline B^{d+1}\subset U.
\]

Restrict the continuous test map `\Psi:U\to\mathbb R^d` to the sphere around `c`:

\[
f:S^d\to\mathbb R^d,
\qquad
f(u)=\Psi(c+ru).
\]

The Borsuk--Ulam theorem gives some `u\in S^d` with

\[
f(u)=f(-u).
\]

Consequently

\[
\Psi(c+ru)=\Psi(c-ru).
\]

Set

\[
\ell^+=c+ru,
\qquad
\ell^-=c-ru.
\]

Both lie in `U`, so both define valid strictly ordered finite generalized-prime additions. Because a point of `S^d` is never zero,

\[
\ell^+\ne\ell^-.
\]

This proves the exact same-destination pair.

Nothing in the argument uses differentiability, generic rank, a regular-value assumption, numerical approximation, or convex mixing of arbitrary measures. Continuity of the actual generalized-prime test map and the dimension mismatch are enough.

Moreover, if `V` is any neighborhood of `c` in `U`, choose `r` small enough that the sphere `c+rS^d` lies in `V`. The same argument gives two distinct points of `V` with the same test vector. Hence `\Psi` is noninjective on every neighborhood of every point of this deformation chamber.

## Matched-control strength

The construction can be made as conservative as desired.

The two systems

\[
Q_+=Q_{\ell^+},
\qquad
Q_-=Q_{\ell^-}
\]

have:

- exactly the same infinite background generalized-prime multiset;
- exactly the same number `d+1` of perturbed generators;
- all changed generator norms confined to `(e^a,e^b)`;
- identical generalized-prime counting functions outside that norm window;
- arbitrarily small coordinate displacement from the same chosen center;
- exactly identical values for all `d` retained tests.

Adding or moving finitely many generators preserves the basic Beurling requirement of a locally finite nondecreasing sequence of real generalized primes greater than one and tending to infinity. It also changes an Euler product only by finitely many Euler factors, so any convergence half-plane supplied by the fixed background is not threatened by this finite perturbation.

One may choose the background and center so that the center itself contains a selected finite block of ordinary rational primes, with all other ordinary primes left fixed. Then the theorem produces arbitrarily small Beurling deformations on the two sides of that rational-prime-centered configuration whose finite test vectors coincide **with each other**.

That last clause is essential. The theorem does not assert

\[
\Psi(\ell^+)=\Psi(c)
\quad\text{or}\quad
\Psi(\ell^-)=\Psi(c).
\]

It proves failure of local injectivity of the surrounding matched-control model, not failure of point-identifiability of `c` itself.

## Relation to AF-021

AF-021 proved that a map from arbitrary positive measures to `d` linear test values has large fibers by affine dependence, Radon's theorem, and Tverberg's theorem. It then left an explicit boundary:

\[
Q
\longmapsto
\bigl(W_Q(F_1),\ldots,W_Q(F_d)\bigr)
\]

might conceivably remain injective because prime-power measures occupy a much narrower nonlinear subset of the positive-measure cone.

AF-022 removes that escape for a broad local Beurling deformation class. The decisive move is not to realize arbitrary Tverberg measures as prime-power measures. Instead, place `d+1` generator logs in `(A/2,A)`, where compact support suppresses every higher power and leaves an honest `(d+1)`-parameter generalized-prime family mapping continuously into `\mathbb R^d`. Borsuk--Ulam then forces a collision directly inside the constrained image.

So the two findings separate two levels of no-go:

\[
\boxed{
\text{AF-021: ambient positive-measure fibers}
}
\]

and

\[
\boxed{
\text{AF-022: actual generalized-prime deformation fibers}.
}
\]

The second is the arithmetic matched-control statement that the first could not supply.

## Relation to AF-007

AF-007 gives a differential obstruction for smooth submersions through the vertical rank

\[
\delta_{T,D}(x)
=
\operatorname{rank}(dD_x|_{\ker dT_x}).
\]

That framework is powerful at regular points but deliberately does not replace global fiber analysis. A map from a higher-dimensional source into a lower-dimensional target can have critical points where derivative rank alone does not produce a useful fiber through the point under study.

AF-022 supplies a complementary topological statement. On each sufficiently small sphere around any center in the `(d+1)`-dimensional generator chamber, Borsuk--Ulam forces a distinct antipodal same-destination pair. Thus exact nearby collisions are certified without asking whether the finite-test map is a submersion or whether any specific Jacobian has full rank.

Again, this does not force a collision **through the center**. Differential, topological-neighborhood, and exact-point fidelity remain distinct categories and should not be conflated.

## Prior art and novelty assessment

The topological and generalized-prime ingredients are classical.

- Karol Borsuk, **“Drei Sätze über die n-dimensionale euklidische Sphäre,”** *Fundamenta Mathematicae* 20 (1933), 177--190, DOI `10.4064/fm-20-1-177-190`, is the original source of the theorem now called Borsuk--Ulam: every continuous map `S^d\to\mathbb R^d` identifies an antipodal pair.
- Arne Beurling, **“Analyse de la loi asymptotique de la distribution des nombres premiers généralisés. I,”** *Acta Mathematica* 68(1) (1937), 255--291, DOI `10.1007/BF02546666`, introduced generalized-prime systems as sequences of real numbers greater than one tending to infinity, with generalized integers generated multiplicatively.

No novelty is claimed for Borsuk--Ulam, finite-dimensional non-embedding phenomena, Beurling generalized primes, or compact-support truncation. The theorem above is a direct specialization of those classical structures to the AF-020/AF-021 compression problem.

The substantive Arithmetic Fidelity result is the exact category-specific obstruction: **for every finite family of compactly supported Weil-weighted tests, the actual generalized-prime source class contains arbitrarily local, finitely supported generator deformations with identical retained test vectors.** The proof identifies a concrete prime-power-compatible deformation chamber rather than importing an arbitrary measure-space collision.

A literature audit found the constituent theories to be mature; this finding therefore makes no broad novelty claim for the topological method. Its value is the reusable exact bridge between the finite-test compression and a matched generalized-prime control family.

## Boundaries and failure modes

- The theorem is for `d` **real-valued** retained tests. For `d` complex-valued tests treated as `2d` real outputs, the same proof uses `2d+1` free generator logarithms and Borsuk--Ulam on `S^{2d}`.
- Compact support is used essentially in this proof to make all higher powers of generators in `(A/2,A)` exactly invisible. Noncompact test families require a separate convergence and continuity argument and may not admit this particular linearized chamber.
- The source class allows continuous Beurling generalized-prime deformations. The theorem does not apply to a source category that permits only the discrete rational primes and forbids matched generalized-prime controls by definition.
- Noninjectivity on every neighborhood does not imply that every point has a nontrivial fiber. A special point can in principle be uniquely identified even when arbitrarily nearby pairs elsewhere collide.
- Therefore this finding does not prove that the ordinary rational primes share their finite-test vector with a different generalized-prime system. Any such stronger statement needs an explicit collision through the rational-prime point or a separate theorem ruling out pointwise uniqueness.
- The result concerns a finite list of exact scalar tests. AF-020 shows that the complete infinite family of compactly supported tests on a visible interval can recover the retained prime-power measure there, so the obstruction cannot be transferred to that full test family.
- A finite-dimensional destination enriched by additional discrete, marked, boundary, operator, or non-test data may evade the theorem if those data are genuinely retained and separate the Borsuk--Ulam pair. The actual destination category must be audited.
- The equality is exact, not numerical, but no claim is made about stability, conditioning, probability, or the size of the displacement needed for approximate collisions under noise.
- The theorem has no implication for the location, multiplicity, or simplicity of zeta zeros and is not evidence for RH.

## Decisive audit test

For any RH, explicit-formula, trace, or positivity route that retains only finitely many real test-function outputs from a prime-power carrier:

1. count the effective real output dimension after removing algebraic redundancies;
2. identify a matched generalized-prime deformation family with more free generator coordinates than retained outputs;
3. check whether a compact-support window, locality restriction, or another exact mechanism yields a continuous admissible parameter chamber;
4. apply an appropriate topological/differential non-injectivity theorem to the **actual constrained source image**, not merely to an ambient measure cone;
5. verify that all additional retained data are included in the destination before declaring a collision;
6. if the route claims the rational-prime point is nevertheless uniquely recoverable, require a separate source-side rigidity theorem proving that special-point property;
7. only after that pointwise rigidity is established may finite-test precision be treated as a rational-prime discriminator.

For the AF-020 model, `d+1` generator logs in `(A/2,A)` provide the canonical first adversarial family for `d` real tests.

## Consequence for the line

AF-021's warning about structured source constraints is now resolved in one important direction. Finite Weil testing does not regain global or local injectivity merely because prime-power measures satisfy multiplicative location/weight constraints.

The current hierarchy is therefore:

\[
\boxed{
\text{full test family on }(0,A)
\;\Longrightarrow\;
\text{exact recovery below }e^A
}
\]

but

\[
\boxed{
\text{any fixed }d\text{-dimensional real test vector}
\;\Longrightarrow\;
\text{arbitrarily local Beurling matched-control collisions}
}
\]

on a natural `(d+1)`-parameter generator-deformation chamber.

This sharpens the next question. A finite-test RH mechanism cannot claim rational-prime specificity from generic identifiability of its retained statistics; generic local identifiability is topologically impossible on the matched Beurling class. What remains is either:

- a genuinely stronger retained structure whose destination dimension/category defeats this deformation argument; or
- an independently proved **special-point rigidity mechanism** explaining why the rational-prime configuration itself is isolated in its fiber despite the unavoidable collisions arbitrarily nearby.