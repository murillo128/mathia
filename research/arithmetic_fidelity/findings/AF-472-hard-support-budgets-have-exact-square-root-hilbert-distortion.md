# AF-472 — Hard support budgets have exact square-root Hilbert distortion

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `SOURCE-RESTRICTION`, `SPARSITY`, `POSITIVE-RECOVERY`, `SHARP-DISTORTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-460 and AF-461 leave hard support restrictions as a genuine possible escape from the paired-mixture obstruction, while AF-465 warns that merely removing one bad substructure is not a positive fidelity theorem. For the simplest hard-support model the positive geometry can be computed exactly.

Let `A` be an alphabet with at least `2s` atoms and let

\[
\Delta_s(A)
=\{\mu\ge0:\sum_{a\in A}\mu(a)=1,\ |\operatorname{supp}\mu|\le s\}
\]

with total-variation/`ell^1` distance

\[
d_1(\mu,\nu)=\|\mu-\nu\|_1.
\]

Then the least bi-Lipschitz distortion of `Delta_s(A)` into an arbitrary Hilbert space is exactly

\[
\boxed{c_2(\Delta_s(A),d_1)=\sqrt{s}.}
\tag{1}
\]

In particular, a **fixed** support budget gives a genuine complexity-independent Hilbert-fidelity certificate, uniform in the size of the ambient alphabet. Conversely, if the admissible support budget grows, no Hilbert representation can preserve the original TV geometry with a distortion bound independent of that support complexity.

The canonical coordinate inclusion

\[
I:\Delta_s(A)\longrightarrow \ell^2(A),\qquad I(\mu)=\mu,
\]

already attains the optimum. For every distinct `mu,nu in Delta_s(A)`,

\[
\boxed{
\frac1{\sqrt{2s}}\,d_1(\mu,\nu)
\le
\|\mu-\nu\|_2
\le
\frac1{\sqrt2}\,d_1(\mu,\nu).
}
\tag{2}
\]

The ratio between the two constants is `sqrt(s)`, and both endpoints are attained. A paired-support Hamming cube inside `Delta_s(A)` gives the matching lower bound for every Hilbert embedding.

Thus hard sparsity is not merely an escape from AF-464's negative test. It is a complete positive source-geometry theorem with an exact price: **the Hilbert-fidelity cost is the square root of the maximum simultaneous support size.**

## Upper bound from the positive/negative decomposition

Fix `mu,nu in Delta_s(A)` and write

\[
x=\mu-\nu=x_+-x_-,
\]

where `x_+` and `x_-` have disjoint support. Since `mu` and `nu` are probability measures,

\[
\|x_+\|_1=\|x_-\|_1=:m
\]

and therefore

\[
\|x\|_1=2m.
\tag{3}
\]

Each of `x_+` and `x_-` has support size at most `s`. Cauchy--Schwarz gives

\[
\|x_+\|_2^2\ge \frac{m^2}{s},
\qquad
\|x_-\|_2^2\ge \frac{m^2}{s}.
\]

Hence

\[
\|x\|_2^2
=\|x_+\|_2^2+\|x_-\|_2^2
\ge \frac{2m^2}{s}
=\frac{\|x\|_1^2}{2s},
\]

which proves the left inequality in `(2)`.

For the other direction, a nonnegative vector of total mass `m` satisfies `||u||_2<=||u||_1=m`. Thus

\[
\|x\|_2^2
\le m^2+m^2
=\frac{\|x\|_1^2}{2},
\]

which proves the right inequality in `(2)`.

Both constants are sharp. If `mu=delta_a` and `nu=delta_b` with `a!=b`, then

\[
\frac{\|\mu-\nu\|_2}{\|\mu-\nu\|_1}
=\frac1{\sqrt2}.
\tag{4}
\]

If `mu` and `nu` are uniform probability measures on two disjoint `s`-point supports, then

\[
\frac{\|\mu-\nu\|_2}{\|\mu-\nu\|_1}
=\frac1{\sqrt{2s}}.
\tag{5}
\]

Therefore the coordinate inclusion has distortion exactly `sqrt(s)`.

This upper bound is genuinely source-relative. The full probability simplex has no finite support cap and the same `ell^2` representation has no complexity-independent inverse TV modulus. The hard support constraint changes the admissible secant geometry itself rather than merely deleting an inconvenient proof witness.

## Matching lower bound from the paired-support cube

Choose `2s` distinct atoms

\[
a_1,b_1,\ldots,a_s,b_s
\]

and, for every sign vector `epsilon in {-1,+1}^s`, define

\[
\mu_\varepsilon
=\frac1s\sum_{j=1}^s
\begin{cases}
\delta_{a_j},&\varepsilon_j=+1,\\
\delta_{b_j},&\varepsilon_j=-1.
\end{cases}
\tag{6}
\]

Every `mu_epsilon` belongs to `Delta_s(A)`. If two sign vectors differ in `h` coordinates, then

\[
d_1(\mu_\varepsilon,\mu_\eta)=\frac{2h}{s}.
\tag{7}
\]

So these `2^s` source states form an exactly rescaled copy of the `s`-dimensional Hamming cube with its `ell^1` metric.

Enflo's classical cube inequality gives

\[
c_2(\{-1,+1\}^s,d_H)=\sqrt{s}.
\tag{8}
\]

Scaling the source metric does not change distortion. Hence every Hilbert embedding of `Delta_s(A)` has distortion at least `sqrt(s)`. Together with the coordinate inclusion this proves `(1)`.

The lower-bound witness is the same combinatorial mechanism that drives AF-464, but here the support cap makes the maximal cube dimension **exactly the resource being priced**. When `s` is fixed, the obstruction is bounded and the elementary coordinate map matches it. When `s` grows, the cube grows with it and the optimal distortion must diverge like `sqrt(s)`.

## Relation to AF-460, AF-461, AF-465, and AF-471

AF-460 shows that finitely many bounded linear source constraints do not repel paired sign cubes in an infinite atomic source. AF-461 extends that failure to regular finite-dimensional nonlinear source laws. Both explicitly leave a hard support budget as a possible way to alter the physical secant carrier. AF-472 closes that escape in both directions for the basic sparse simplex:

\[
\boxed{
\text{support}\le s
\quad\Longleftrightarrow\quad
\text{Hilbert TV fidelity is available with sharp cost }\sqrt{s}
}
\tag{9}
\]

where the displayed equivalence is understood for this declared source class and its worst-case distortion, not as a characterization of every possible sparse-like source restriction.

AF-465 supplies the important logical warning that absence of large Hamming cubes is not generally sufficient for Hilbert fidelity. The present result does not contradict that warning: it gives an explicit **positive embedding theorem** for this specific source family. Sparsity works here because every difference has at most `s` positive and `s` negative coordinates, which yields the global norm comparison `(2)` for every admissible pair.

AF-471 classifies exact scalar radial Hilbertization of the unrestricted TV simplex after changing the metric. AF-472 instead keeps the **original TV metric** and changes the **source class**. These are different resources. The unrestricted simplex can be Hilbertized exactly after a singular scalar metric transform such as `sqrt(d_1)`; the `s`-sparse simplex embeds into Hilbert with the original `d_1` up to the sharp finite distortion `sqrt(s)`.

This separation is useful for downstream audits: a claimed arithmetic rescue must say whether it is paying by deforming the metric, by restricting source complexity, or by adding marked structure. Those mechanisms should not be credited interchangeably.

## Prior-art audit

The ingredients are classical and **no theorem-level novelty is claimed** for sparse `ell^1`/`ell^2` norm comparison, Hamming-cube distortion, or Hilbert embeddings.

- Per Enflo, **“On the nonexistence of uniform homeomorphisms between `L_p`-spaces,”** *Arkiv för Matematik* 8 (1969), 103--105, DOI `10.1007/BF02589549`. This is the classical source of the Hamming-cube obstruction; modern metric-embedding surveys record the exact Euclidean distortion `sqrt(s)` of the `s`-cube.
- Paata Ivanisvili, Ramon van Handel, and Alexander Volberg, **“Rademacher type and Enflo type coincide,”** *Annals of Mathematics* 192(2), 665--678 (2020), DOI `10.4007/annals.2020.192.2.8`. This supplies modern context for the cube/type inequality already used by AF-464 and AF-468.
- The support-sensitive `ell^1`/`ell^2` comparison used in `(2)` is the elementary Cauchy--Schwarz sparse-vector inequality ubiquitous in sparse approximation and compressed sensing; no special novelty is attached to it.

A targeted search found the classical ingredients and extensive sparse-vector/metric-embedding literature, but no need to claim a new general embedding theorem. The line-specific contribution is the exact assembly relevant to the open Arithmetic Fidelity source question: on the probability-law source with a hard support cap, the elementary positive embedding and the paired-support cube meet at the same sharp `sqrt(s)` distortion.

## Boundary and falsification audit

- **The hard support cap is load-bearing.** An average support bound, decay condition, entropy bound, or statement that most mass lies on `s` atoms does not imply `(2)`. Such softer hypotheses need their own quantitative tail error.
- **The result is worst-case and pairwise.** It controls every pair in `Delta_s(A)`. A weaker anchored or distributional task may admit a smaller cost; a stronger target such as finite-dimensional Euclidean compression introduces additional dimension/packing constraints.
- **Ambient alphabet size is irrelevant only because the Hilbert target may be infinite-dimensional.** The theorem gives distortion independent of `|A|`, not a finite-dimensional representation independent of alphabet size.
- **Support union may have size `2s`.** The sharp upper bound depends on separate positive and negative supports and cannot be justified by pretending that `mu-nu` is `s`-sparse.
- **No arithmetic discriminator is supplied.** A fixed support cap can preserve whichever TV distinctions already exist on the source, but it does not explain why rational primes rather than a matched control occupy the admissible sparse family.
- **Growing support reopens the obstruction sharply.** If a proposed arithmetic model has support budget `s=s(N)->infinity`, its optimal worst-case Hilbert distortion on the whole admitted sparse simplex is at least `sqrt{s(N)}`. Calling the model “sparse” does not by itself give uniform fidelity.
- **Subclasses can do better.** Equation `(1)` concerns the full `s`-sparse probability simplex. Additional relational restrictions may eliminate the paired cube and improve the distortion, but AF-465 means that such improvement requires a positive theorem for the actual subclass rather than merely failure of this lower-bound witness.

## Arithmetic-fidelity consequence

AF-472 gives the first sharp positive answer to one of the source-side escapes left open by the recent cube obstruction chain. A hard complexity cap can protect the original TV discriminator through Hilbert compression, but the protection has a precise price and disappears uniformly as the cap grows.

For a prime-facing construction, the relevant question is therefore not whether the source is informally “sparse.” One must identify a mathematically forced support/mixture complexity `s`, prove that the **actual admissible arithmetic carrier** obeys that bound at the layer where compression occurs, and then propagate the resulting `sqrt(s)` conditioning cost through the downstream operator or theorem. If `s` necessarily grows, this route alone cannot supply a complexity-independent recovery constant; if `s` is fixed or the arithmetic subclass has stronger geometry, that positive structure must be established explicitly.
