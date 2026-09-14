# MI-011 — Same-horizon laws are cheap, finite horizon entropy forces a Cesàro gap, and even a squarefree-unit common source can escape superexponentially

**Evidence level:** exact for the floor-quotient Fourier skeleton through [FD-117](../../findings/FD-117-full-farey-discrepancy-field-is-invertibly-equivalent-to-the-quotient-mertens-staircase.md)--[FD-126](../../findings/FD-126-squarefree-unit-common-sources-saturate-on-repeated-square-horizons.md). FD-126 is one permanent squarefree-supported unit-sign source with a global square-root envelope, but its signs are freely chosen and need not equal Möbius or satisfy multiplicative compatibility. No RH consequence is claimed.

FD-117 shows that the complete cumulative Farey discrepancy field is invertibly equivalent to the quotient-Mertens staircase. FD-118 compresses its same-horizon Fourier data to the divisor-closed floor-quotient skeleton `Q_N`, of size `2 sqrt(N)+O(1)`, without losing that source.

FD-119 identifies the coercivity obstruction inside this reversible carrier: in reindexed source coordinates the skeleton has an exact Möbius equality ray, and a fixed true prefix plus the divisor identity can be grafted onto that ray cheaply. FD-120 goes further: a complete single-horizon squarefree/nonsquarefree increment alphabet, `a_N(1)=1`, the exact divisor identity and terminal size `sqrt(N)+O(1)` still permit critical near-saturation when the witness may be reprogrammed with the horizon.

FD-121--FD-124 quantify what one common source costs. Fixed squarefree dilation edges force pair gaps, bounded-ratio integer chains force a positive Cesàro deficit for polynomially bounded sources, and the ratio ceiling can be removed. If

`Lambda_n=(1/n)log(H_n/H_0)`

stays bounded along an infinite subsequence, then the average of `1-S_(H_j)` there stays bounded away from zero. Hence Cesàro saturation requires `Lambda_n->infinity`: the horizons must be superexponentially sparse in the chain index.

FD-125 shows that this condition is qualitatively sharp for the abstract common-source skeleton on repeated squares. FD-126 strengthens the matched control to the physical coefficient alphabet. It constructs one infinite sequence `a` with `a(1)=1`, `a(n)=0` on nonsquarefrees and `a(n)=+-1` on every squarefree integer. Its cumulative source `Y` satisfies

`|Y(n)| << sqrt(n)`

for all `n`, while on `H_(j+1)=H_j^2` one has `|Y(H_j)|=sqrt(H_j)+O(1)` and

`E_(H_j)^Q(Y)=|Y(H_j)|^2+O(H_j^(3/4)(log H_j)^2)`.

Thus the relative skeleton energy still tends to one. The stagewise construction uses the freedom in the squarefree signs to approximate the equality-ray targets at the low quotient coordinates and keeps the remaining prefix energy cheap. It never revises an old sign, so the escape is genuinely one-source and cross-horizon coherent.

This removes a tempting false boundary. Exact squarefree support and unit amplitude are **not** the terminal arithmetic resource. They determine where increments may occur and how large each increment is, but not how their signs correlate. The surviving distinction is the actual Möbius sign law: coprime multiplicativity, growing exact divisor identities across the retained horizons, or another relation that constrains the simultaneous sign assignment rather than its alphabet.

A closing theorem must therefore spend sign correlation at the scale visible to the floor-quotient skeleton. It should prove that the true Möbius source cannot realize the FD-126 low-coordinate equality targets on a superexponential chain, or that doing so incurs a critical relative energy gap. Adding more fixed-depth support information, a stronger pointwise envelope, or another generic common-source consistency condition cannot suffice because the matched control already pays those bills.

**Boundary.** FD-126 does not construct the Möbius function, impose `a(mn)=a(m)a(n)` for coprime inputs, enforce the full family `sum_(d<=H)Y(floor(H/d))=1` on the retained horizons, prove that every superexponential chain admits saturation, or prove/refute RH. The exact conclusion is methodological: the unresolved resource has moved from support/amplitude admissibility to correlation among the physical signs.