# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Quantify active-scale Möbius breadth without importing the Mertens target

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-011-fixed-depth-physical-data-do-not-create-critical-coercivity-on-a-reversible-farey-skeleton`.

FD-117--FD-120 reduce same-horizon Farey information to the reversible floor-quotient skeleton. FD-121--FD-124 show that one common polynomially bounded source pays an average cost unless the horizon schedule becomes superexponentially sparse. FD-125--FD-126 realize that sparse escape with one permanent squarefree unit-sign source.

FD-127 shows that any prescribed finite set of exact Möbius prime directions can be factored out while the remaining free core still fits the equality ray. FD-128 strengthens the obstruction qualitatively: an **infinite but sufficiently sparse** prime ancestry set can coexist with `|Y(x)|<<sqrt(x)` and sparse-horizon saturation. Cardinality of the prime family is therefore not the coercive variable.

FD-129 now closes the opposite naive repair. If the enforced ancestry contains **every prime up to `Y_j`**, then the synthetic source equals `mu(n)` on `n<=Y_j`. As `Y_j->infinity`, any horizon-uniform envelope imposed on that recovered prefix transfers directly to the physical Mertens function. At the critical `x^(1/2+epsilon)` scale this is equivalent to RH by the classical Littlewood criterion, even if a different synthetic source is chosen at every horizon.

So the active-scale breadth theorem must be noncircular. It must price multiplicative breadth strongly enough to break the sparse-core control **without simultaneously reconstructing the whole physical prefix and assuming the desired uniform Mertens envelope on it**.

## Locate the first noncircular scale-visible multiplicative law that breaks the sparse-horizon control

The next source law must couple signs across enough prime directions or horizons at the active scale that stagewise endpoint assignment loses capacity, while leaving a genuinely synthetic comparison class. Candidate currencies include aggregate/approximate prime breadth, semigroup inverse growth, divisor identities that do not determine every coefficient below a growing cutoff, or energy control restricted to the free rough region.

Complete prime-prefix ancestry is still useful as an information boundary, but FD-129 shows that pairing it with a uniform RH-scale prefix envelope is not an independent coercivity hypothesis; it already contains the target.

## Keep information equivalence, horizon entropy, arithmetic breadth and target recovery separate

FD-117--FD-120 classify information, FD-121--FD-124 price common-source horizon coherence, FD-125--FD-128 identify the sparse multiplicative escape, and FD-129 identifies the opposite circularity boundary. “Unbounded arithmetic rank” is too coarse, but so is “complete growing rank” if the accompanying source control is already uniform on the recovered physical prefix. Future work must price breadth as a function of scale while auditing exactly which physical coefficients and endpoint bounds the hypothesis has already reconstructed.
