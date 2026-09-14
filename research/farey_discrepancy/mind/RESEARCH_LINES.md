# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Quantify active-scale Möbius breadth without importing the Mertens target

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-012-unweighted-prime-ancestry-energy-dilutes-fixed-rank-gauge-cuts`.

FD-117--FD-120 reduce same-horizon Farey information to the reversible floor-quotient skeleton. FD-121--FD-124 show that one common polynomially bounded source pays an average cost unless the horizon schedule becomes superexponentially sparse. FD-125--FD-126 realize that sparse escape with one permanent squarefree unit-sign source.

FD-127 shows that any prescribed finite set of exact Möbius prime directions can be factored out while the remaining free core still fits the equality ray. FD-128 strengthens the obstruction qualitatively: an **infinite but sufficiently sparse** prime ancestry set can coexist with `|Y(x)|<<sqrt(x)` and sparse-horizon saturation. Cardinality of the prime family is therefore not the coercive variable.

FD-129 closes the opposite naive repair. If the enforced ancestry contains **every prime up to `Y_j`**, then the synthetic source equals `mu(n)` on `n<=Y_j`. As `Y_j->infinity`, any horizon-uniform envelope imposed on that recovered prefix transfers directly to the physical Mertens function. At the critical `x^(1/2+epsilon)` scale this is equivalent to RH by the classical Littlewood criterion, even if a different synthetic source is chosen at every horizon.

FD-130 now closes the simplest aggregate middle ground. Even with **every prime direction present at the active scale** and exact agreement with Möbius through any fixed multiplicative rank `K`, one common squarefree unit-sign source can have unweighted mean ancestry defect tending to zero while disagreeing with Möbius on a positive density of integers. The defect lives on one rank interface with `O(H)` edges, while the complete ancestry graph has `H omega(1)` edge volume, so total-edge normalization dilutes the cut.

The active-scale breadth theorem must therefore be noncircular **and rank-visible**. It must reduce free-core capacity without reconstructing the whole physical prefix, but it also cannot measure approximate ancestry by a single unweighted global edge mean that makes fixed-rank interfaces disappear.

## Locate the first noncircular scale-visible multiplicative law that breaks the sparse-horizon control

The next source law must couple signs across enough prime directions or horizons at the active scale that stagewise endpoint assignment loses capacity, while leaving a genuinely synthetic comparison class. FD-130 narrows the candidates: useful aggregate breadth must retain multiplicative-level information, for example through rank-sensitive weights, levelwise/primewise defect bounds, a local uniform condition, or anchoring depth that grows with scale. A direct Fourier-skeleton coercivity inequality could bypass coefficient recovery instead.

Complete prime-prefix ancestry remains an information boundary, but FD-129 shows that pairing it with a uniform RH-scale prefix envelope already imports the target. Conversely, complete prime **direction** coverage is not enough when its defect is averaged over the whole expanding edge graph.

## Keep information equivalence, horizon entropy, arithmetic breadth, defect geometry and target recovery separate

FD-117--FD-120 classify information, FD-121--FD-124 price common-source horizon coherence, FD-125--FD-128 identify the sparse multiplicative escape, FD-129 identifies the circular reconstruction boundary, and FD-130 identifies a normalization escape inside full prime breadth. “Unbounded arithmetic rank” is too coarse, “complete growing rank” can be circular when paired with the target envelope, and “small average ancestry defect” can be vacuous when low-rank interfaces have vanishing edge density. Future work must price breadth as a function of scale together with where the defect mass can hide.
