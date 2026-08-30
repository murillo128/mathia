# AF-001 — Fiberwise recoverability and unconstrained lifts

**Status:** `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`

## Claim

Let `X`, `Y`, and `D` be sets, let

\[
T:X\to Y
\]

be a compression/forgetful map, and let

\[
d:X\to D
\]

be the discriminator whose survival is being tested. Say that `d` is **exactly recoverable from `T`** when there exists a map

\[
r:T(X)\to D
\]

such that

\[
d=r\circ T.
\]

Then:

1. `d` is recoverable from `T` if and only if it is constant on every fiber of `T`:
   \[
   T(x)=T(x')\Longrightarrow d(x)=d(x').
   \]
2. If `S:Y\to Z` is any downstream deterministic map and `d` is recoverable from `S\circ T`, then `d` was already recoverable from `T`. Therefore a discriminator lost at `T` cannot be recreated by later processing that sees only `T(x)`.
3. Given an additional mark `M:X\to A`, `d` is recoverable from `(T,M)` if and only if, inside each `T`-fiber, `M` separates every pair having different `d`-values.
4. If `X` is finite and arbitrary marks are allowed, define
   \[
   m(T,d)=\max_{y\in T(X)}\left|d\bigl(T^{-1}(y)\bigr)\right|.
   \]
   The minimum possible alphabet size `|A|` among all marks `M:X\to A` for which `d` is recoverable from `(T,M)` is exactly `m(T,d)`.

Consequently, **an unconstrained “minimal lift” problem is structurally too weak for Arithmetic Fidelity**. In particular, for a binary discriminator that is genuinely lost by `T`, a two-state mark always restores it, and the trivial choice `M=d` is already admissible. A meaningful lift theory must therefore restrict the admissible marks by additional mathematical structure rather than minimizing alphabet size alone.

## Derivation

For (1), if `d=r\circ T`, equal `T`-values immediately give equal `d`-values. Conversely, if `d` is constant on every `T`-fiber, define

\[
r(y)=d(x)\qquad\text{for any }x\text{ with }T(x)=y.
\]

Fiber constancy makes this well-defined on `T(X)`, and then `d=r\circ T`.

For (2), if

\[
d=q\circ S\circ T
\]

for some `q:S(T(X))\to D`, then

\[
d=(q\circ S)\circ T,
\]

so `d` already factors through `T`. The contrapositive is the deterministic irreversibility statement: once two upstream states with different discriminator values have been identified by `T`, no map of the compressed output alone can separate them later.

For (3), apply (1) to

\[
(T,M):X\to Y\times A.
\]

Two elements lie in the same `(T,M)`-fiber exactly when both their `T`-values and their `M`-values agree. Thus recoverability is equivalent to

\[
T(x)=T(x'),\quad M(x)=M(x')\Longrightarrow d(x)=d(x').
\]

Equivalently, within a fixed `T`-fiber, different `d`-values must receive different `M`-values.

For (4), fix `y`. The distinct values in

\[
d\bigl(T^{-1}(y)\bigr)
\]

must receive distinct marks, so every valid alphabet satisfies

\[
|A|\ge \left|d\bigl(T^{-1}(y)\bigr)\right|.
\]

Taking the maximum gives `|A| >= m(T,d)`.

For the matching upper bound, choose an alphabet `A` of size `m(T,d)`. For every `y`, inject the finite set `d(T^{-1}(y))` into `A`; call the injection `j_y`. Define

\[
M(x)=j_{T(x)}(d(x)).
\]

If `T(x)=T(x')` and `M(x)=M(x')`, injectivity of the corresponding `j_y` implies `d(x)=d(x')`. Hence `(T,M)` recovers `d`, proving the bound is sharp.

## Why this matters for Arithmetic Fidelity

This isolates three different questions that must not be conflated.

First, **survival through a fixed compression is a fiber question**: the relevant discriminator survives exactly when the compression equivalence relation refines the discriminator equivalence relation. This is more targeted than asking whether `T` itself is injective; `T` may collapse many states harmlessly as long as it never merges states with different `d`-values.

Second, **ordinary downstream processing cannot repair an earlier loss**. Any proposed spectrum, trace, determinant, positivity operation, averaging step, or asymptotic observable that is a function only of an already-collapsed representation inherits that collapse. To recover the discriminator, genuinely additional information must enter before or at the loss point.

Third, **“add the smallest marking that restores the discriminator” is vacuous unless admissibility is constrained**. With arbitrary marks, the target discriminator itself can simply be copied into the mark, and the exact finite optimum is determined only by the number of discriminator values mixed inside the worst fiber. Alphabet cardinality therefore measures how many labels are needed, not whether the lift is intrinsic, canonical, local, equivariant, geometric, arithmetic, or independently available.

The next useful theory should therefore study a restricted class `\mathcal M` of admissible lifts and ask whether

\[
\exists M\in\mathcal M\quad d\text{ factors through }(T,M),
\]

or quantify the obstruction when no such `M` exists. Candidate restrictions include naturality/functoriality, equivariance under an intrinsic symmetry group, locality, dependence only on predeclared upstream structure, bounded complexity, or an explicit no-target-leakage condition. Which restrictions are mathematically appropriate is not fixed by this finding.

## Prior art and novelty assessment

The factorization criterion is elementary and classical: it is the set-theoretic form of saying that a function descends to the quotient by the fibers of `T`. Armstrong-style functional dependencies use the same implication pattern: agreement on determining data forces agreement on dependent data.

Blackwell’s comparison-of-experiments theory supplies a much richer probabilistic analogue in which garbling/post-processing orders information structures by informativeness. The deterministic implication in item (2) should not be presented as a new data-processing theorem.

The lift problem is also adjacent to zero-error source coding with side information. Witsenhausen explicitly distinguishes the case where the transmitter also knows the receiver’s side information, for which the alphabet problem is trivial, from the harder decoder-only case governed by graph coloring. Orlitsky–Roche similarly show that function computation with constrained side information leads to nontrivial graph-entropy quantities. These results support, rather than weaken, the obstruction here: **nontriviality comes from the admissible information/coding structure, not from allowing an arbitrary extra label**.

The Mathia-specific contribution of this finding is therefore not a novelty claim for the fiber theorem. It is the exact foundational consequence for this research line: unrestricted minimal lifts must be rejected as a target because they permit hidden copies of the discriminator; future “minimal lift” claims must state an admissible lift class before they can carry mathematical content.

## Boundaries and failure modes

- The exact alphabet formula is stated only for finite `X`. Infinite-cardinal extensions are not needed here and may introduce choice/set-theoretic bookkeeping.
- This finding treats exact deterministic recovery. Approximate, noisy, probabilistic, statistical, or decision-theoretic notions of fidelity require separate definitions.
- A small alphabet does not imply a natural lift; the fiberwise injections `j_y` may vary arbitrarily with `y` and carry no global structure.
- Conversely, failure of exact recoverability does not mean all useful information about `d` is absent. Partial distinguishability, error bounds, mutual information, sufficient statistics, or decision value may survive and belong to later theory.
- The result does not yet identify the correct admissibility class for prime-sensitive lifts and makes no claim about RH.

## Consequence for the line

Treat **admissible lift structure** as part of the mathematical object, not as an afterthought. Any future theorem claiming that marking, phase, orientation, boundary data, provenance, or transverse structure is a “minimal lift” should first specify what family of lifts is allowed and why that family is intrinsic. Without such a restriction, minimal-lift recovery reduces to fiberwise relabeling and cannot distinguish a genuine structural mechanism from simply storing the answer.