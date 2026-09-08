# VIS-097 — level-four 3-delay signatures can recover cycle assembly order

## Claim

The local-edge information-loss boundary from `VIS-096` is sharp already at delay dimension `m=3`.

There exist two finite real sequences with:

1. the same first and last three-windows;
2. the same unordered multiset of length-four blocks; and therefore
3. the same unordered multiset of oriented edges in their ordinary three-delay polygonal paths,

but with different fourth-level path signatures.

An explicit pair is

`a=(0,0,0,1,0,0,0,1,1,0,0,0)`

and

`b=(0,0,0,1,1,0,0,0,1,0,0,0)`.

Their signatures agree through levels one, two, and three by `VIS-096`, while

`[S^4(X_a)-S^4(X_b)]_(1,2,1,3)=1/4`.

Thus signature level four is a genuine chronology carrier for fixed three-coordinate delay paths: it can distinguish different Eulerian assemblies of the same local four-block inventory.

**Evidence/status:** `EXACT-DERIVED + SHARPNESS/INFORMATION-BOUNDARY + NO-NOVELTY-CLAIM`.

This does not establish any zeta-specific signal. It identifies only the first unaugmented signature depth at which the general local-edge obstruction of `VIS-096` actually fails in an explicit delay-path example.

## 1. Two closed delay cycles with the same base window

Use the base three-window

`o=(0,0,0)`.

Appending the scalar word `1000` returns the three-delay path to `o` through the closed polygonal cycle

`A: 000 -> 001 -> 010 -> 100 -> 000`.

Appending `11000` gives a second closed cycle

`B: 000 -> 001 -> 011 -> 110 -> 100 -> 000`.

Concatenating these scalar append words in opposite orders gives exactly the two sequences above:

`a = 000 | 1000 | 11000`,

`b = 000 | 11000 | 1000`.

The length-four blocks contributed by cycle `A` are

`0001, 0010, 0100, 1000`,

while cycle `B` contributes

`0001, 0011, 0110, 1100, 1000`.

Therefore `a` and `b` have exactly the same length-four block multiset, including multiplicities, and both begin and end at the delay window `000`. Their three-delay paths are respectively the concatenations `A*B` and `B*A` of the same two oriented edge cycles.

## 2. The two cycles have nonparallel level-two signatures

Because `A` and `B` are closed, their first signature levels vanish:

`S^1(A)=S^1(B)=0`.

Direct edge integration gives

`S^2(A) = (1/2) [[0,-1,0],[1,0,-1],[0,1,0]]`

and

`S^2(B) = (1/2) [[0,-2,-1],[2,0,-2],[1,2,0]]`.

These are antisymmetric area tensors, as expected for closed polygonal loops, and they are not proportional. In particular,

`S^2(A)_(1,2)=-1/2`, `S^2(A)_(1,3)=0`,

while

`S^2(B)_(1,2)=-1`, `S^2(B)_(1,3)=-1/2`.

This nonparallel pair of local area tensors is the extra degree of freedom unavailable in the planar case, where the bivector space is one-dimensional.

## 3. Chen multiplication forces an order-sensitive fourth-level commutator

For concatenated paths, Chen multiplicativity gives

`S(A*B)=S(A) tensor S(B)`.

At homogeneous degree four, the closed-loop condition `S^1(A)=S^1(B)=0` removes the degree `1+3` and `3+1` cross terms. Hence

`S^4(A*B)`
` = S^4(A) + S^4(B) + S^2(A) tensor S^2(B)`,

whereas

`S^4(B*A)`
` = S^4(B) + S^4(A) + S^2(B) tensor S^2(A)`.

Subtracting,

`S^4(A*B)-S^4(B*A)`
` = S^2(A) tensor S^2(B) - S^2(B) tensor S^2(A)`.

For the tensor coordinate `(1,2,1,3)`, this is

`S^2(A)_(1,2) S^2(B)_(1,3)`
` - S^2(B)_(1,2) S^2(A)_(1,3)`
` = (-1/2)(-1/2) - (-1)(0)`
` = 1/4`.

Therefore the fourth-level signatures differ exactly, despite equality of the endpoint windows and complete unordered local edge inventory.

Combined with `VIS-096`, which proves equality through level three from precisely those data, this makes the degree-four separation sharp for this `m=3` collision.

## 4. Why dimension three is the first natural escape

The mechanism is not that level four is generically mysterious. It is the ordered product of independent loop-area tensors.

For closed pieces whose first signature level vanishes, swapping two pieces first affects the concatenated signature through the commutator-like term

`S^2(A) tensor S^2(B) - S^2(B) tensor S^2(A)`

at total degree four. In the plane every antisymmetric second-level tensor is a scalar multiple of the single area bivector, so this particular mechanism collapses; that is consistent with the stronger planar degree-four obstruction in `VIS-096`.

In three dimensions the bivector space already has dimension three, so distinct local cycles can carry nonparallel signed-area tensors. Their assembly order can then survive even after the unordered oriented-edge current has been quotiented out.

This identifies a precise information carrier for a future visual or statistical use of higher delay signatures: **ordered interaction between local area modes**, rather than merely a richer rendering of the same edge inventory.

## 5. Prior art and novelty assessment

Chen multiplicativity of iterated integrals and the tensor-algebra structure of path signatures are classical. Ben Hambly and Terry Lyons, **Uniqueness for the signature of a path of bounded variation and the reduced path group**, *Annals of Mathematics* 171:1 (2010), 109–167, DOI `10.4007/annals.2010.171.109`, is the existing Mathia source anchor for the standard bounded-variation signature framework and tree-like uniqueness boundary.

The order-sensitive fourth-level term above is an elementary consequence of that classical signature algebra: concatenating two closed loops with noncommuting second-level tensors produces the displayed degree-four cross-term. No novelty is claimed for Chen's identity, tensor noncommutativity, loop areas, or the general fact that higher signature levels encode path order.

The Mathia-specific content is the explicit **sliding-window delay collision** showing that the first open gate left by `VIS-096` is real rather than merely unclassified: two scalar sequences can share the full fixed local four-block inventory and endpoints yet differ at signature level four.

## Boundary and falsification

This finding proves only existence of an order-sensitive level-four feature for the ordinary unaugmented `m=3` delay path.

It does not show that:

- every pair of distinct Eulerian assemblies is separated at level four;
- level four is sufficient to reconstruct the full sequence;
- an analogous level-four separation occurs for planar `m=2` paths, which `VIS-096` rules out under the same local inventory;
- the displayed feature survives any zeta-zero or random-matrix matched control;
- a fourth-level signature statistic has useful asymptotic behavior as delay length or observation scale grows;
- higher signature levels provide an RH criterion or any arithmetic advantage by themselves.

Falsify the explicit claim by showing that the two displayed scalar sequences do not have the same length-four block multiset and endpoint windows, or by direct iterated-integral evaluation showing that their `(1,2,1,3)` fourth-level coordinates agree.

The calculation is exact and finite; no numerical rendering or asymptotic assumption is used.

## Visual consequence

No canonical PNG is retained. The useful geometry is already explicit: two closed delay cycles based at the same window carry different three-dimensional area bivectors, and swapping their order changes the degree-four tensor through the area-area commutator while preserving the complete local edge inventory.

A future visualization can render these two loops and their bivector planes for intuition, but the mathematical separation does not depend on that picture.

## Research consequence

`VIS-096` should no longer be read as merely leaving level four in `m>=3` unclassified. This finding proves that, already for `m=3`, level four can retain chronology beyond the unordered `(m+1)`-block multiset.

For the accepted `CLUE-zeta-critical-strip-multiscale-geometry`, the signature branch therefore changes character at this boundary. Levels through three are exact local-edge nulls, planar level four remains a null, but three-dimensional level four is a legitimate nonlocal information carrier. The next substantive question is not whether level four can remember order in principle; it is whether a pre-registered fourth-level or log-signature observable on an arithmetic delay path carries source-specific structure after matching the relevant local four-block inventory and lower spectral statistics.