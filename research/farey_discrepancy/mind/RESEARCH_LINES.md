# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Quantify the active-scale breadth of the Möbius sign law

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-011-fixed-depth-physical-data-do-not-create-critical-coercivity-on-a-reversible-farey-skeleton`.

FD-117--FD-120 reduce same-horizon Farey information to the reversible floor-quotient skeleton. FD-121--FD-124 show that one common polynomially bounded source pays an average cost unless the horizon schedule becomes superexponentially sparse. FD-125--FD-126 realize that sparse escape with one permanent squarefree unit-sign source.

FD-127 shows that any prescribed **finite** set of exact Möbius prime directions can be factored out while the remaining free core still fits the equality ray. FD-128 strengthens the obstruction qualitatively: the ancestry set can itself be **infinite**. For a sufficiently sparse infinite prime set `S`, one permanent source satisfies `a_(pn)=-a_n` for every `p in S`, retains `|Y(x)|<<_S sqrt(x)`, and still asymptotically saturates the Fourier skeleton along sufficiently sparse horizons.

Thus cardinality of the prime family is not the coercive variable. The live theorem is quantitative: determine what amount of prime ancestry is visible at scale `H` before the `S`-free core and its triangular inverse lose enough capacity to track

`Y(floor(H/k)) approx Y(H) mu(k)/k`.

Candidate currencies include the density/product profile of active primes below the relevant scale, growth of the semigroup inverse norm, or an equivalent scale-dependent multiplicative rank. A merely infinite but ultra-sparse ancestry set is now an explicit matched control.

## Locate the first scale-visible multiplicative law that breaks the sparse-horizon control

The next source law must couple signs across enough prime directions or horizons **at the active scale** that the stagewise endpoint assignment cannot be solved with subcritical prefix mass. Full Möbius multiplicativity is certainly much stronger, but using it wholesale would hide the threshold. The sharper target is a growth law for the visible prime set or divisor identities that forces a positive critical energy deficit.

## Keep information equivalence, horizon entropy and arithmetic breadth separate

FD-117--FD-120 classify information, FD-121--FD-124 price common-source horizon coherence, and FD-125--FD-128 identify the remaining multiplicative escape. The new boundary is especially important: “unbounded arithmetic rank” is still too coarse. An infinite rank can remain invisible when it enters too sparsely relative to the horizon. Future work should price **rank as a function of scale**, not count formal source constraints globally.
